---
id: learning.zephyr-docs.storage.zms
title: Zephyr内存存储ZMS
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/zms/zms.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_Zephyr内存存储ZMS

原文：[Zephyr Memory Storage (ZMS)](https://docs.zephyrproject.org/latest/services/storage/zms/zms.html)。读取日期：2026-10-12，`latest`。

**Zephyr内存存储（Zephyr Memory Storage，ZMS）**是一种面向各类非易失存储技术的键值存储系统。它支持传统片上 NOR Flash，也支持 **阻变随机存取存储器（Resistive Random-Access Memory，RRAM）**、**磁阻随机存取存储器（Magnetoresistive Random-Access Memory，MRAM）** 等无须独立擦除操作、可以直接覆盖数据的存储器。

## 6.1\_总体行为与扇区布局

ZMS 将空间划分为至少两个扇区，在当前扇区不断写入键值对，直到写满。键写入分配表条目（Allocation Table Entry，ATE），称为 ID-ATE，从扇区底部开始存放；值称为 data，从扇区顶部开始原样存放。每个扇区末尾还保存头部 ATE，用于描述打开、关闭等状态以及当前 ZMS 版本。

当前扇区 N 满时，先确认下一个扇区 N+1 为空，将扇区 N+2 中仍有效的 ATE 搬到 N+1，以完成垃圾回收；擦除被回收扇区，再写入 `garbage_collect_done` ATE 和 close ATE，关闭当前扇区。随后转入下一扇区继续写入。到分区末尾后，回收并擦除第一个扇区，再从那里循环。

三个扇区的原文布局示意如下。表格从上到下对应原文的扇区顶部到底部：

| 扇区0：已关闭 | 扇区1：打开 | 扇区2：空 |
| --- | --- | --- |
| `Data_a0` | `Data_b0` | `Data_c0` |
| `Data_a1` | `Data_b1` | `Data_c1` |
| `Data_a2` | `Data_b2` | `Data_c2` |
| `GC_done` | `.` | `.` |
| `.` | `.` | `.` |
| `.` | `.` | `.` |
| `.` | `ID ATE_b2` | `ID ATE_c2` |
| `ID ATE_a2` | `ID ATE_b1` | `ID ATE_c1` |
| `ID ATE_a1` | `ID ATE_b0` | `ID ATE_c0` |
| `ID ATE_a0` | `GC_done ATE` | `GC_done ATE` |
| `Close ATE (cyc=1)` | `Close ATE (cyc=1)` | `Close ATE (cyc=1)` |
| `Empty ATE (cyc=1)` | `Empty ATE (cyc=2)` | `Empty ATE (cyc=2)` |

各元素的作用：

- Empty ATE：擦除扇区时写入，位于扇区最后一个位置。
- Close ATE：关闭扇区时写入，位于倒数第二个位置。
- GC_done ATE：表示下一扇区已经完成垃圾回收，可处在扇区的任意位置。
- ID ATE：保存 `zms_id_t` 类型的键，并描述数据位置、大小及 CRC32。
- Data：对应 ID-ATE 的实际值。

> 译注：表中“空”扇区仍画出了旧数据和 ATE，因为逻辑有效性还取决于循环计数是否匹配；不应把空扇区理解为每个物理字节都必须恢复到擦除值。上面的 N+1、N+2 按扇区环循环解释。

## 6.2\_挂载与初始化

挂载首先取得 Flash 参数，检查 `sector_size`、`sector_count` 等配置，再调用内部 `zms_init` 函数使存储可用。默认情况下，`zms_mount()` 无法挂载时返回错误；面向恢复的场景可以使用 `zms_mount_force()`，第一次挂载失败时自动清除并重新初始化分区。

> 译注：`zms_mount_force()` 是可能擦除已有数据的恢复接口，不等同于无损修复；需要保留数据时不能用它替代正常挂载错误处理。

可通过 `zms_fs.mount_flags` 设置可选挂载标志：

| 设置 | 行为 |
| --- | --- |
| `mount_flags = 0` | 分区处于擦除状态且找不到有效 ZMS 头部时，`zms_mount()` 创建初始头部，即格式化分区 |
| `ZMS_MOUNT_FLAG_NO_FORMAT` | 相同情况下不格式化，返回 `-ENOTSUP` |

挂载前必须初始化 `zms_fs` 中的以下成员：

```c
struct zms_fs {
        /** File system offset in flash **/
        off_t offset;

        /** Storage system is split into sectors, each sector size must be multiple of
         * erase-blocks if the device has erase capabilities
         */
        uint32_t sector_size;
        /** Number of sectors in the file system */
        uint32_t sector_count;

        /** Optional mount behavior flags (enum zms_mount_flags) */
        uint32_t mount_flags;

        /** Flash device runtime structure */
        const struct device *flash_device;
};
```

其中 `offset` 为区域在 Flash 中的偏移；`sector_size` 是扇区大小，设备需要擦除时必须为擦除块大小的整数倍；`sector_count` 为扇区数；`mount_flags` 为可选标志；`flash_device` 为设备运行时对象指针。

ZMS 采用向前追加的写入方式，因此初始化必须找回上次停止的扇区与条目位置。先寻找“已关闭扇区后紧跟打开扇区”的组合，再在打开扇区中恢复最后写入的 ATE；随后检查下一个扇区是否为空，不为空则擦除。

## 6.3\_写入、读取与历史

为避免对同一 ID 重复写入相同值，ZMS 会在各扇区查找该 ID，并比较数据；相同则不写。需要更新时，在扇区中写入 ATE 和数据，删除操作则不写数据。当前扇区无法容纳数据加 ATE 时，转入下一个扇区，对新打开扇区之后的扇区执行垃圾回收并擦除。

读取默认从新到旧遍历 ATE，寻找同一 ID 的最新有效条目，取回数据并返回读取字节数。指定非零历史计数时，读取同一 ID 的较早版本。

## 6.4\_枚举条目

应用可以枚举记录，无须预先提供 ID 列表。如果 ID 来自有效载荷，例如打包后的地址，且应用没有单独维护 Flash 索引，这尤其有用。通常在启动时利用持久化的 ID 和长度元数据重建内存状态。

| 接口 | 用途 |
| --- | --- |
| `zms_iter_init()` | 初始化迭代器状态 |
| `zms_iter_init_with_config()` | 初始化时配置 ID 位掩码、包含边界的 ID 范围、谓词回调，或组合这些过滤条件 |
| `zms_iter_next()` | 每次取得一个当前有效的唯一 ID 条目 |
| `zms_iter_next_all()` | 返回所有匹配条目，包括完整历史和删除标记 |

### 6.4.1\_两种遍历方式

`zms_iter_next()` 返回唯一的当前有效 `(id, len)` 对：跳过扇区头部条目、跳过 `len == 0` 的删除标记；一个 ID 出现多次时只返回最新有效版本。为保证唯一性，需要检查候选 ID 是否还有更新记录，因此可能增加扫描。

`zms_iter_next_all()` 更快，按遇到的顺序返回所有匹配 `(id, len)` 对，包括同一 ID 的历史版本与删除标记，不执行唯一性过滤；应用自行按策略过滤或合并。

两者返回值均为：找到条目时返回 `1`，输出 ID 与长度；枚举结束返回 `0`；出错返回负 errno，例如 `-EINVAL`、`-EIO`、`-ENXIO`。

迭代器总会报告 ID 与长度。如果提供非空数据缓冲区，还能直接复制存放在 ATE 内的小数据。较大条目或未提供缓冲区时，应显式调用 `zms_read()` 读取最新值，或用 `zms_read_hist()` 读取旧版本。

### 6.4.2\_遍历边界与并发写入

`zms_iter_init()` 捕获遍历边界，初始化之后写入的条目不属于本次遍历。在两次 `zms_iter_next()` 或 `zms_iter_next_all()` 之间，禁止对同一 `zms_fs` 调用 `zms_write()`，删除也包含在内。如果写入触发垃圾回收，迭代行为未定义。

这个限制也适用于执行遍历的线程自身，与是否加锁无关。下面的锁只阻止其他线程在遍历期间写入。

`zms_fs` 的 `zms_lock` 字段是内部写互斥锁，类型为 `struct k_mutex`；`zms_write()` 和 `zms_delete()` 在写入时内部持有它。多个线程共用同一实例时，可以在整个遍历期间持有这把锁：

```c
k_mutex_lock(&fs.zms_lock, K_FOREVER);

rc = zms_iter_init(&fs, &iter);
/* ... */

while ((rc = zms_iter_next(&fs, &iter, &id, &len, NULL, 0)) == 1) {
  /* ... */
}

k_mutex_unlock(&fs.zms_lock);
```

### 6.4.3\_过滤与读取示例

下面示例同时配置位掩码、范围和谓词过滤，并为 ATE 内联数据提供缓冲区：

```c
struct zms_iter iter;
bool predicate_id_not_2(zms_id_t id)
{
  return id != (zms_id_t)2;
}

struct zms_iter_config iter_config = {
  .mask_id = (zms_id_t)0x03,
  .min_id = (zms_id_t)0x01,
  .max_id = (zms_id_t)0x03,
  .use_mask = true,
  .use_range = true,
  .use_predicate = true,
  .predicate_func = predicate_id_not_2,
};
zms_id_t id;
size_t len;
uint8_t data[ZMS_DATA_IN_ATE_SIZE];
int rc;

/* Block writes from other threads for the duration of the traversal. */
k_mutex_lock(&fs.zms_lock, K_FOREVER);

rc = zms_iter_init_with_config(&fs, &iter, &iter_config);
if (rc) {
  /* handle error */
}

while ((rc = zms_iter_next(&fs, &iter, &id, &len, data, sizeof(data))) == 1) {
  /* id: entry ID matching configured mask/range/predicate, len: current stored size */
  /* data: filled with the entry's content when it is small enough to be
   * stored directly inside the ATE; otherwise left untouched, in which case
   * zms_read() must be used to fetch it.
   */
  printk("id=0x%llx len=%zu\n", (unsigned long long)id, len);
}

k_mutex_unlock(&fs.zms_lock);

if (rc < 0) {
  /* handle iterator error */
}
```

如果只需要 `(id, len)`，可将 `data/data_len` 设为 `NULL/0`。提供缓冲区时，也只有 ATE 内联数据会被复制，大数据仍需 `zms_read()`。

将 `zms_iter_config` 清零，或者不启用 `use_mask`、`use_range`、`use_predicate`，即可保留默认行为：接受整个 `zms_id_t` 范围内的所有 ID。若想知道某个枚举 ID 有多少历史版本，可递增 `cnt` 调用 `zms_read_hist()`，直到返回 `-ENOENT`。

> 译注：示例错误处理处仍是占位注释。初始化失败后应走正确的解锁与退出路径，不能继续使用无效迭代器。大数据条目不会更新内联数据缓冲区，因此不能把缓冲区中前一次留下的内容当作当前条目的数据。

## 6.5\_空闲空间、循环计数与垃圾回收

> 译注：以下几节分别说明空间查询的成本、旧记录如何失效，以及应用如何把回收工作安排到合适时机。

### 6.5.1\_计算空闲空间

ZMS 可以返回分区剩余空间，但需要遍历所有扇区中的有效 ATE，并为每个候选检查其他历史记录，因而非常耗时。不建议频繁调用，以免拖慢调用线程。

> 译注：原文这里写“检查是否存在更旧的记录”；计算当前有效占用实际需要识别条目是否被更新记录覆盖。应以所用版本实现和 **应用程序编程接口（Application Programming Interface，API）** 定义为准，不把每个历史条目都当作当前有效数据。

### 6.5.2\_循环计数器

每个扇区有一个 `uint8_t` 类型的主循环计数器，保存在 Empty ATE 中。其他 ATE 的计数必须与它相同才有效。条目搬到另一个扇区时，必须采用目标扇区的计数。

通过递增 Empty ATE 的循环计数并写入这一个 ATE，就能使扇区内旧 ATE 全部失效。关闭扇区时写入 Close ATE，其计数必须与 Empty ATE 一致；未使用的剩余区域用无效填充数据写满，避免旧 ATE 恰好具有有效循环计数。

> 译注：这里的单次写入失效机制主要针对可直接覆盖的介质。NOR Flash 再次编程前的物理擦除要求仍然存在，不能仅修改计数器就绕过硬件擦除。

### 6.5.3\_主动安排垃圾回收

有些应用要求存储写入延迟有明确上界。当前扇区接近写满时，一次写入可能触发扇区切换和垃圾回收，导致实时约束无法满足。ZMS 提供查询当前扇区剩余空间的 API，应用可以自行选择接近写满时的切换时机，把回收提前执行，从而避免下一次写入再触发回收。

> 译注：这一保证以预留空间足够容纳下一条数据及其元数据、且没有其他写入消耗空间为前提，不是任何长度或并发条件下的固定延迟保证。

## 6.6\_ATE结构

一个条目使用十六字节编码信息，具体结构由应用选择的 ATE 格式决定。ZMS 定义多种格式，运行时通过 Empty ATE 中的 `metadata` 字段识别；该字段在各种格式中位于相同字节位置。

### 6.6.1\_三十二位ID格式

以下将原文合并单元格表改排为字节区间表，保留字段布局：

| 字节位置 | 字段或解释 |
| --- | --- |
| 0 | `crc8` |
| 1 | `cycle_cnt` |
| 2–3 | `len` |
| 4–7 | `id` |
| 8–15 | `len <= 8` 时为内联 `data` |
| 8–11 | 非上述内联形式时为 `offset` |
| 12–15 | 根据条目用途为 `data_crc` 或 `metadata` |

这是默认格式，详见 `zms_ate` API 文档。可选 `data_crc` 用于检查保存在扇区顶部的数据完整性。

> 原文注意：只在完整读取数据时检查数据 **循环冗余校验（Cyclic Redundancy Check，CRC）**，部分读取不检查，因为 CRC 覆盖整个条目。
>
> 原文警告：对原来未启用 CRC 的已有 ZMS 内容启用 CRC，会使已有数据全部失效。

### 6.6.2\_六十四位ID格式

启用 Kconfig 配置项 `CONFIG_ZMS_ID_64BIT` 时采用此格式：

| 字节位置 | 字段或解释 |
| --- | --- |
| 0 | `crc8` |
| 1 | `cycle_cnt` |
| 2–3 | `len` |
| 4–11 | `id` |
| 12–15 | 根据条目用途为 `data`（`len <= 4`）、`offset` 或 `metadata` |

> 原文警告：选择与已有 ZMS 内容不同的 ATE 格式，会使已有数据全部失效。
>
> 原文注意：Settings 的 ZMS 后端不支持六十四位 ID 格式。

## 6.7\_用户数据可用空间

ZMS 始终保留一个空扇区用于垃圾回收。例如四个扇区中只有三个保存键值对，空闲扇区会在四个扇区间轮转。

原文称单次可写入扇区的数据长度上限为 64K，并说明未来版本可能变化。

> 译注：这不是允许恰好写入 65,536 字节的精确边界。本地实现检查 `len > UINT16_MAX`，因此还有 65,535 字节的字段上限，以及扇区可用容量和对齐限制。不要直接以原文“64K”作为调用长度。

### 6.7.1\_小数据

足够小的数据直接保存在 ATE 中，无须另写到扇区顶部；可内联的长度取决于 ATE 格式。原文给出的最大用户数据空间公式为：

$$
\frac{(\mathrm{NUM\_SECTORS}-1)\times(\mathrm{SECTOR\_SIZE}-5\times\mathrm{ATE\_SIZE})\times\mathrm{DATA\_SIZE}}{\mathrm{ATE\_SIZE}}
$$

`NUM_SECTORS` 为总扇区数，`SECTOR_SIZE` 为扇区大小，`ATE_SIZE` 为十六字节；五个 ATE 预留给头部和删除条目。`DATA_SIZE` 按格式为八或四字节。

四个 1024 字节扇区，采用默认格式存储八字节值时，用户数据空间为 `3 × 944 × 8 / 16 = 1416` 字节。

### 6.7.2\_大数据

超过内联容量的数据另存于扇区顶部。若数据为 N 字节，另需十六字节 ATE，即键值对总占用为 `N + 16` 字节，因此可用空间与实际数据长度有关。

例如四个 1024 字节扇区保存六十四字节值：三个扇区用于存储，每个可用 944 字节，容纳 `floor(944 / (64 + 16)) = 11` 条，用户数据总量为 `11 × 3 × 64 = 2112` 字节。

### 6.7.3\_可用空间计算器

原页提供[可用空间计算器](https://docs.zephyrproject.org/latest/services/storage/zms/zms.html#available-space-calculator)。它根据 ZMS 配置估算容量，可切换高级模式，使用实际混合数据集替代平均值。下面完整翻译其输入项与提示；Markdown 中不运行原页 JavaScript，计算操作仍在原页完成。

<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Nordic Semiconductor ASA -->
<!-- 计算器表单、提示及结果说明据官方 Apache-2.0 组件翻译。 -->

| 英文界面项 | 中文含义及提示 |
| --- | --- |
| Advanced mode | 高级模式，逐行输入实际条目 |
| Entries (ID:data per line) | 每行一个 `ID:data`，数据用十六进制表示，替代平均大小和条目数以模拟混合数据集 |
| Write Block Size (bytes) | 写块大小：设备一次可写的最少字节数，查 Flash 参数和设备树 |
| Flash Type | 介质类型：无需显式擦除的 RRAM/MRAM，或需要显式块擦除的 NOR Flash |
| Erase Block Size (bytes) | 最小擦除块字节数，例如 4096；NOR Flash 扇区大小必须为其整数倍 |
| Sector Size (bytes) | ZMS 扇区字节数，需容纳预留的五个 ATE，并按写块对齐；NOR Flash 还需按擦除块对齐 |
| Number of Sectors | 扇区数，至少两个，其中一个保留给垃圾回收，可用扇区数为总数减一 |
| Average Data Size (bytes) | 单个值的平均有效载荷字节数，不含 ZMS 元数据 |
| Number of Data Items | 同时保存的不同条目，即唯一 ID 数量；与平均长度共同估算数据集 |
| Use with Settings Subsystem | 是否通过 Settings 使用 ZMS；选择“是”会计入名称、值和链表节点等额外记录 |
| Average Path Size (bytes) | 设置键路径的平均字节长度，例如 `bt/cf` 或 `/data/key1`；仅 Settings 模式使用 |
| ID Type | 三十二位或六十四位 ID；分别最多内联八或四字节，与 `CONFIG_ZMS_ID_64BIT` 对应 |
| Calculate Available Space | 计算可用空间 |

高级模式中，直接使用 ZMS 时输入如 `0x01:010203`，ID 和数据都为十六进制；Settings 模式输入如 `/data/key1:010203`，路径是普通文本，数据仍为十六进制。忽略冒号周围空白、空行及以 `#` 开始的行；十六进制数据可带空格或下划线，必须非空、字符合法且有偶数个十六进制数字。启用高级模式但没有条目、缺少 `ID:data` 格式、ID 为空或不是有效十六进制时会报错。Settings 模式按 UTF-8 字节数计算路径，并固定使用三十二位 ID。

结果的中文含义如下：

| 结果 | 含义 |
| --- | --- |
| Settings Mode / Advanced Mode | 当前是否启用 Settings 或高级模式 |
| Average Path Size (rounded) | 按写块向上对齐的平均路径大小；高级模式不使用该平均值 |
| Parsed Data Items / Total Parsed Data Bytes / Total Parsed Effective Size | 解析出的条目数、有效载荷总字节数、计入元数据和对齐后的总占用 |
| ATE Size (rounded) / Header Size | 按写块对齐的 ATE 大小；每扇区头部预留五个 ATE |
| Sector Effective Size | 减去头部开销后的单扇区有效空间 |
| Available Sectors for Data / Total Available Space | 总扇区数减一，以及所有数据扇区的有效空间总和 |
| Storage Per Item (with metadata) | 一条记录计入元数据及对齐后的占用；高级模式取解析结果平均值 |
| Items per Sector / Total Items That Can Fit | 每扇区及全部数据扇区可容纳的条目数 |
| Total Data Storage Capacity | 可存放的用户数据总量，不含元数据 |
| Total Storage Requirement | 当前整个数据集所需空间及其占可用空间的百分比 |
| Storage Efficiency | 用户数据字节数除以总存储需求 |
| For Your Requested Items | 对指定条目数报告可装入的数量、数据容量和占用空间 |

写块、数据大小、条目数和适用时的路径长度必须大于零；扇区数至少为二。脚本要求扇区严格大于五个对齐后的 ATE，并满足写块及擦除块对齐；单条有效占用不能超过扇区有效容量。总需求超过可用空间时提示增加空间或减小数据集；占用超过 50% 时提示应把有效数据限制在可用空间的一半以内。请求条目装不下时，会报告可容纳的数量。

> 译注：表单提示写“至少五个 ATE”，脚本实际使用严格大于判断，因为还要留下数据空间。高级模式按平均有效占用估计可容纳数量，不是对任意混合条目排列执行真实写入模拟；同一 ID 重复行也不会自动去重。正文简式以十六字节 ATE 为前提，写块更大时计算器会向上对齐。

## 6.8\_磨损均衡与寿命

ZMS 针对无需擦除的器件进行了优化。依赖擦除值的存储系统，例如 **非易失存储（Non-Volatile Storage，NVS）**，在这类器件上需要用大量写入模拟擦除，既降低寿命，也增加写入和空白设备初始化延迟。ZMS 用循环计数避免这种模拟擦除，并保证一次扇区写入周期内每个存储位置只写一次。

例如，4096 字节扇区、十六字节写块的无需擦除器件，用 NVS 模拟擦除需要 256 次写入，用 ZMS 只需一次十六字节写入；原文把这一操作描述为快 256 倍。

> 译注：这里的 256 倍对应写入次数之比；实际耗时还受驱动、总线和器件时序影响，不能视为任何硬件上的实测加速比。

垃圾回收搬移有效数据也产生写入，减少存储单元寿命。为降低影响，建议分区大小按可能写入数据的最大有效占用量（含头部）约两倍规划。

### 6.8.1\_寿命公式

传统 Flash 与 RRAM/MRAM 的寿命都受存储单元可擦写次数限制。Flash 必须按页擦除后再写；无需擦除的介质可以直接覆盖。

假设同一 ID 的四字节变量每分钟改变一次，分区有四个 1024 字节扇区，每次记录占十六字节，每扇区可用 944 字节。向前追加循环一周后，再次写到第一个扇区第一个位置需要 `944 × 4 / 16 = 236` 分钟。因为只更新同一 ID，且分区足够大，旧数据已被更新覆盖，该例无需垃圾回收搬移。若器件允许写入 20,000 次，估算寿命为 4,720,000 分钟，约九年。

一般地，内联小数据的 `effective_size` 为十六字节，大数据为 `16 + sizeof(data)`。设一组待更新数据总有效占用为 `TOTAL_EFFECTIVE_SIZE`，并已按约两倍有效数据量配置分区，以免回收总是搬移条目，则寿命分钟数为：

$$
\frac{\mathrm{SECTOR\_EFFECTIVE\_SIZE}\times\mathrm{SECTOR\_NUMBER}\times\mathrm{MAX\_NUM\_WRITES}}{\mathrm{TOTAL\_EFFECTIVE\_SIZE}\times\mathrm{WR\_MIN}}
$$

`SECTOR_EFFECTIVE_SIZE` 为扇区大小减八十字节头部，`SECTOR_NUMBER` 为扇区数，`MAX_NUM_WRITES` 为器件允许写入次数，`TOTAL_EFFECTIVE_SIZE` 为整组数据有效占用，`WR_MIN` 为每分钟更新整组数据的次数。

### 6.8.2\_器件寿命计算器

原页的[器件寿命计算器](https://docs.zephyrproject.org/latest/services/storage/zms/zms.html#device-lifetime-calculator)与容量计算器使用相同的介质、布局、数据、Settings 和高级模式字段，另增加：

| 界面项 | 中文含义 |
| --- | --- |
| Writes per Minute | 每分钟写入次数；提示以 `1` 表示每分钟一次、约 `0.017` 表示每小时一次 |
| Maximum Writes per Cell Before Wear-out | 单元磨损前允许的最大编程/擦除次数，应取器件手册值；原页用典型 NOR 的 100,000 次举例，RRAM/MRAM 往往更高 |
| Calculate Lifetime | 计算寿命 |

结果除布局、每条占用、每扇区数量和总需求外，还报告 `Cycles through Storage`（整组数据重复写入多少遍，才使一个单元的磨损计数增加一次）、`GC Write Amplification`（垃圾回收额外物理写入的放大倍数）、`Expected Lifetime`（预计总分钟数及年、日、时、分分解）。高级模式显示解析出的条目、数据字节和有效占用总量；使用相同的输入校验和空间不足、超过 50% 占用提示。

> 译注：公式的更新频率是“整组数据每分钟更新次数”，表单提示却写“一个存储项的更新次数”；脚本将整组有效占用与该频率相乘。多个键的更新频率不同，不能直接把某个键的频率填入并当成精确结果。脚本另以占用率 `u` 估算 GC 写放大 `max(1, u / (1-u))`，并在接近满容量时作上限截断；这是估算模型。更新分布、长期不变的有效键、实际擦写时序及硬件耐久度都会影响结果，占用低于一半不保证所有工作负载都没有搬移。

## 6.9\_功能与演进

与 NVS 等已有存储系统相比，ZMS 引入了许多功能，并将从初始版本继续演进，以满足新存储技术对低延迟、更大容量等方面的要求。

### 6.9.1\_版本1已有功能

- 支持无需擦除的器件，只需一次写入即可使一个扇区失效。
- 支持大分区、大扇区及六十四位地址空间。
- 支持三十二位和六十四位 ID。
- 小数据直接保存在 ATE 内。
- 内置数据 CRC32，并存于相应 ATE 格式中。
- 支持 ZMS 格式版本，以便后续演进。
- 支持平台需要的大写块。
- 支持适应不同应用需求的多种 ATE 格式。
- 支持 `zms_mount_force()` 强制挂载恢复：失败后自动清除并重新初始化分区。
- 支持加速重复 ID 查找的缓存，并可为不同分区实例配置不同大小。
- 支持 `zms_iter_init()`、`zms_iter_next()`，无须预声明 ID 列表即可枚举有效条目。

### 6.9.2\_原文列出的未来功能

- 同时挂载采用不同 ATE 格式的多个实例；目前同一应用中的实例必须使用相同格式。
- 对周期性写入且数据不超过半个分区、总能找到同 ID 旧版本的应用，允许跳过垃圾回收。
- 将 ID 分为命名空间，并按需分配，处理不同子系统或示例的 ID 冲突。
- 根据循环计数取得器件磨损值。
- 增加出错后的存储分区恢复函数。
- 提供把 NVS 条目迁移为 ZMS 条目的库或应用。

> 译注：这些是原页列出的演进方向，不代表已经实现。其“恢复函数”条目与前面已列出的强制清除恢复也不能混同；强制清除不等于保留数据的恢复。

### 6.9.3\_与NVS、FCB的选择

这里比较的是简单、非层次化的存储系统，不是完整文件系统。Zephyr 中功能范围相近的还有 NVS 和 **Flash循环缓冲区（Flash Circular Buffer，FCB）**，选择取决于应用与硬件：

| 情况 | 原文建议与理由 |
| --- | --- |
| RRAM、MRAM 等无需擦除器件 | ZMS 针对此类介质设计，用一次写入替代大量写入模拟擦除 |
| 大写块，或所需扇区大小不同于传统 Flash 擦除页 | ZMS 可以定制这些参数并支持相应设备 |
| 传统 Flash | NVS 元数据及头部更小，擦除不需 ZMS 那样的额外写入；原文据此推荐 NVS，并认为其读写更快 |
| 需要超过 64K 个 ID | ZMS 的 ID 最宽可达六十四位 |
| **先进先出（First In, First Out，FIFO）** 方式保存数据 | FCB 更适合这种工作方式 |

先核对各方案是否存在功能或硬件限制。如果 NVS 和 ZMS 都可用，再结合前述寿命计算做选择。

## 6.10\_性能建议

> 译注：以下建议分别针对介质布局、**随机存取存储器（Random Access Memory，RAM）** 中的查找缓存和 ID 格式；容量、回收延迟与内存开销需要一起权衡。

### 6.10.1\_扇区大小与数量

根据实际有效容量合理设置分区，建议为要保存的键值对预留约两倍空间。单个扇区必须能够容纳最大的数据条目。增大扇区会使一次垃圾回收更慢，但发生频率更低；减小扇区则相反。

原文指出 Settings 会把一个路径—值拆为两条 ZMS 记录，因此容量计算要包含两份 ATE 开销。小数据存于 ATE 内可以提高性能；例如 Settings 路径不超过八字节时，可能更快。

> 译注：同页计算器按“路径、值、链表节点”三类记录计算 Settings 开销；本地 `settings_zms.c` 也包含独立链表节点存储。因此“两条”不能当作当前所有版本的完整开销模型，实际容量应以所用后端实现为准。八字节内联阈值适用于默认三十二位 ID 格式。

### 6.10.2\_缓存大小

直接使用 ZMS API 时，建议缓存条目数至少等于不同 ID 的数量。每增加一个缓存条目增加八字节 RAM，应权衡选择。

通过 Settings 使用时，原文按每个设置拆为两个 ZMS 条目，建议缓存至少为设置项数的两倍。

> 译注：此处同样沿用原文“两条”的简化描述。存在链表节点等额外 ID 时，两倍不是完整工作集的保证；应按实际访问的 ID 数和可用 RAM 规划。

### 6.10.3\_按实例手动配置缓存

启用 `CONFIG_ZMS_LOOKUP_CACHE_MANUAL` 时，每个 `zms_fs` 可提供自己的查找缓存，而不是使用全局 `CONFIG_ZMS_LOOKUP_CACHE_SIZE`。必须在 `zms_mount()` 前调用 `zms_set_lookup_cache()` 分配缓存；未指定缓冲区的实例不启用查找缓存。

```c
static struct zms_fs zms_a;
static struct zms_fs zms_b;
static uint64_t zms_a_cache[512];
static uint64_t zms_b_cache[32];

zms_set_lookup_cache(&zms_a, zms_a_cache, ARRAY_SIZE(zms_a_cache));
zms_set_lookup_cache(&zms_b, zms_b_cache, ARRAY_SIZE(zms_b_cache));
```

### 6.10.4\_ID大小

六十四位 ID 空间通常超出多数应用需求，没有明确需求时建议使用三十二位。即使在六十四位系统上，六十四位 ID 也可能对代码大小和性能产生轻微影响，因为存储中的 ID 字节位置并不按八字节边界对齐。

## 6.11\_API与示例

接口由 `zms.h` 提供，见 [ZMS 数据结构](P058_Zephyr内存存储数据结构目录.md)和 [ZMS API](P059_Zephyr内存存储接口.md)。

- [ZMS 存储示例](P089_Zephyr内存存储示例.md)：通过 ZMS 保存和读取数据。
- [ZMS 循环计数验证](P090_ZMS循环计数验证示例.md)：验证垃圾回收期间扇区循环计数是否正确，包括跨越 `uint8_t` 回绕边界的情况。

> 译注：本地新接口头文件是 `<zephyr/kvss/zms.h>`，旧 `<zephyr/fs/zms.h>` 已作为兼容头标记弃用；使用时核对当前工程版本。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：设置子系统](P005_设置子系统.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：文件系统](P007_文件系统.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：设置子系统](P005_设置子系统.md) · [下一章：文件系统](P007_文件系统.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
