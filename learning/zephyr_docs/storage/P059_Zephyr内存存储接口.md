---
id: learning.zephyr-docs.storage.zmsapi-2
title: Zephyr内存存储接口
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第59章\_Zephyr内存存储接口

原文：[group__zms__high__level__api](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html)。读取日期：2026-10-13，`latest`。

本页为**Zephyr 内存存储（Zephyr Memory Storage，ZMS）应用编程接口（Application Programming Interface，API）**，声明于 `zephyr/kvss/zms.h`。各函数的 `fs` 参数指向文件系统实例。**分配表条目（Allocation Table Entry，ATE）**记录条目信息，**迭代器（Iterator）**用于遍历；标识符类型 [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9)、挂载标志和过滤配置见[数据结构参考](P058_Zephyr内存存储数据结构目录.md)。

```c
#include <zephyr/kvss/zms.h>
```

## 59.1\_挂载文件系统

[`zms_mount()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga962625b12f21cf030a35c944a2de380e) 函数的声明如下：

```c
int zms_mount(struct zms_fs * fs);
```

将 ZMS 文件系统挂载到 `fs` 指定的设备。若闪存区域已擦除且没有有效的 ZMS 头部，默认会格式化该区域并创建有效头部。在 `fs->mount_flags` 中设置 [`ZMS_MOUNT_FLAG_NO_FORMAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#gga5f9a7529c95876c29b6a0fd7a230fc92a0b00eefe2f9cc169d285ad8255521c87) 可禁用自动格式化，此时改为挂载失败。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-ENOTSUP` | 检测到的文件系统不是 ZMS |
| `-EPROTONOSUPPORT` | 不支持该 ZMS 版本 |
| `-EINVAL` | `fs == NULL`，或闪存参数、扇区布局无效 |
| `-ENXIO` | 设备错误 |
| `-EIO` | 存储器读写错误 |

## 59.2\_强制挂载

[`zms_mount_force()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gab5a3adcdc5eecbb8a1bcb9d1c7709837) 函数的声明如下：

```c
int zms_mount_force(struct zms_fs * fs);
```

将 ZMS 文件系统挂载到 `fs` 指定设备。**第一次挂载失败时，会清空分区后再尝试挂载。**

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-ENOTSUP` | 检测到的文件系统不是 ZMS |
| `-EPROTONOSUPPORT` | 不支持该 ZMS 版本 |
| `-EINVAL` | `fs == NULL`，或闪存参数、扇区布局无效 |
| `-ENXIO` | 设备错误 |
| `-EIO` | 存储器读写错误 |

## 59.3\_清除文件系统

[`zms_clear()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gafe06d28af34fbecf2bd666ef11095ed1) 函数的声明如下：

```c
int zms_clear(struct zms_fs * fs);
```

从设备中清除 ZMS 文件系统。**完成后必须重新挂载。**

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EACCES` | `fs` 尚未挂载 |
| `-ENXIO` | 设备错误 |
| `-EIO` | 存储器读写错误 |
| `-EINVAL` | `fs == NULL` |

## 59.4\_写入条目

[`zms_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga218132ef5cb0f2157721cb62886de842) 函数的声明如下：

```c
ssize_t zms_write(struct zms_fs * fs, zms_id_t id, const void * data, size_t len);
```

写入 `id` 标识的条目，`data` 指向待写数据，`len` 为写入字节数，原页注明最大 **64 KiB**。

`len == 0` 实际删除条目，等价于 [`zms_delete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga60ad1d79cd4f3ada1cf726d422c120c3)；无法区分已删除条目和长度为 0 的数据条目。成功返回写入字节数，即 `len` 或 0；尝试重写已存储的相同数据时，不发生闪存写入，返回 0。失败返回 `errno.h` 中定义的错误码的负值。

| 错误返回值 | 含义 |
| --- | --- |
| `-EACCES` | ZMS 尚未初始化 |
| `-ENXIO` | 设备错误 |
| `-EIO` | 存储器读写错误 |
| `-EINVAL` | `fs == NULL` 或 `len` 无效 |
| `-ENOSPC` | 设备没有剩余空间 |

## 59.5\_删除条目

[`zms_delete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga60ad1d79cd4f3ada1cf726d422c120c3) 函数的声明如下：

```c
int zms_delete(struct zms_fs * fs, zms_id_t id);
```

删除 `id` 指定的条目。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EACCES` | ZMS 尚未初始化 |
| `-ENXIO` | 设备错误 |
| `-EIO` | 存储器读写错误 |
| `-EINVAL` | `fs == NULL` |

## 59.6\_读取条目

[`zms_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f) 函数的声明如下：

```c
ssize_t zms_read(struct zms_fs * fs, zms_id_t id, void * data, size_t len);
```

读取 `id` 指定的条目到 `data` 指向的缓冲区，`len` 是最多读取的字节数。

成功返回实际读取字节数（原页标注为大于 0），等于请求长度；若已存数据更短，则小于请求长度。失败返回 `errno.h` 错误码的负值。

| 错误返回值 | 含义 |
| --- | --- |
| `-EACCES` | ZMS 尚未初始化 |
| `-EIO` | 存储器读写错误 |
| `-ENOENT` | 不存在指定 `id` 的条目 |
| `-EINVAL` | `fs == NULL` |

## 59.7\_读取历史条目

[`zms_read_hist()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga6cedc2fe5bfe8aa6183d41273897f0e7) 函数的声明如下：

```c
ssize_t zms_read_hist(struct zms_fs * fs, zms_id_t id, void * data, size_t len, uint32_t cnt);
```

读取 `id` 指定条目的**历史版本（History Revision）**，`data` 指向缓冲区，`len` 为请求读取的字节数。历史计数参数 `cnt` 为 0 时读取最新版本，为 1 时读取前一版本，依此类推。

原页说明：成功返回读取字节数（大于 0），等于请求长度；若返回值大于请求长度，则表示尚有数据未读完。失败返回 `errno.h` 错误码的负值。

译注：此处保留原页的历史读取返回值说明，它与 [`zms_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f) 的“最多读取”说明不同，不能混为一种长度约定，也不能据此认为超过缓冲区容量的字节已被复制。

| 错误返回值 | 含义 |
| --- | --- |
| `-EACCES` | ZMS 尚未初始化 |
| `-EIO` | 存储器读写错误 |
| `-ENOENT` | 不存在与 `id` 和历史计数匹配的条目 |
| `-EINVAL` | `fs == NULL` |

## 59.8\_查询条目长度

[`zms_get_data_length()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8871cfa165587b259a8043d22bf669a4) 函数的声明如下：

```c
ssize_t zms_get_data_length(struct zms_fs * fs, zms_id_t id);
```

获取 `id` 指定条目的数据长度。返回 ATE 中记录的数据长度；原页描述为 ATE 中包含的数据字节数，并将成功结果列为指定条目的长度（大于 0）。失败返回 `errno.h` 错误码的负值。

| 错误返回值 | 含义 |
| --- | --- |
| `-EACCES` | ZMS 尚未初始化 |
| `-EIO` | 存储器读写错误 |
| `-ENOENT` | 不存在指定 `id` 的条目 |
| `-EINVAL` | `fs == NULL` |

## 59.9\_计算总空闲空间

[`zms_calc_free_space()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga02be33c18632687133f53557b5ee8bc2) 函数的声明如下：

```c
ssize_t zms_calc_free_space(struct zms_fs * fs);
```

计算文件系统可用空闲空间，成功返回仍可写入的字节数（大于等于 0），失败返回 `errno.h` 错误码的负值。计算较耗时，尤其是在**串行外设接口（Serial Peripheral Interface，SPI）**闪存上。

| 错误返回值 | 含义 |
| --- | --- |
| `-EACCES` | ZMS 尚未初始化 |
| `-EIO` | 存储器读写错误 |
| `-EINVAL` | `fs == NULL` |

## 59.10\_查询活动扇区连续空间

[`zms_active_sector_free_space()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga76e06261e54f9d2ee65f7d31328e3bcc) 函数的声明如下：

```c
ssize_t zms_active_sector_free_space(struct zms_fs * fs);
```

查询当前**活动扇区（Active Sector）**的连续空闲空间。

| 返回值 | 含义 |
| --- | --- |
| `>= 0` | 当前扇区空闲字节数，即不自动前进到下一个扇区时仍能写入的字节数 |
| `-EACCES` | ZMS 尚未初始化 |
| `-EINVAL` | `fs == NULL` |

## 59.11\_主动切换扇区

[`zms_sector_use_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga90a6f8c47f02641ca33ee42a7c709750) 函数的声明如下：

```c
int zms_sector_use_next(struct zms_fs * fs);
```

关闭当前活动扇区并切换到下一个扇区，同时在新扇区调用**垃圾回收（Garbage Collection）**过程。

**原文警告：** 该函数为特定场景提供，与 ZMS 避免不必要闪存擦除的目标冲突。大量使用可能导致闪存设备过早失效。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EACCES` | ZMS 尚未初始化 |
| `-EIO` | 存储器读写错误 |
| `-EINVAL` | `fs == NULL` |

## 59.12\_查询最大扇区循环计数

[`zms_get_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga31b8d970e70fd7cbb94a0dc068dbdcfc) 函数的声明如下：

```c
int zms_get_num_cycles(struct zms_fs * fs, uint32_t * cycles);
```

遍历所有扇区，读取各扇区**空 ATE（Empty ATE）**中的 32 位循环计数，将最大值写入 `cycles` 指向的位置，可在测试中用于估计写入循环消耗。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EINVAL` | `fs` 或 `cycles` 为 `NULL` |
| `-EACCES` | 文件系统未挂载 |

## 59.13\_查询指定扇区循环计数

[`zms_get_sector_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga4aa193a3c357335a6d403139371803ab) 函数的声明如下：

```c
int zms_get_sector_num_cycles(struct zms_fs * fs, uint32_t sector, uint32_t * cycles);
```

读取指定扇区的循环计数。`sector` 是从 0 开始的扇区索引，必须小于 `fs->sector_count`；`cycles` 指向接收 32 位循环计数的位置。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EINVAL` | `fs` 或 `cycles` 为 `NULL`，或扇区索引越界 |
| `-EACCES` | 文件系统未挂载 |
| `-ENOENT` | 该扇区没有有效的空 ATE |

## 59.14\_初始化迭代器

[`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d) 函数的声明如下：

```c
int zms_iter_init(const struct zms_fs * fs, struct zms_iter * iter);
```

以已挂载的 `fs` 初始化 `iter` 迭代器状态，记录当前写入位置作为遍历边界。原文说明，此调用后写入或删除的条目不会出现在随后 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 的结果中。

**调用者不得在 [`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d) 到最后一次 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 之间向 `fs` 写入或删除。** 遍历边界的说明不解除这一约束。

成功返回 0；`fs` 或 `iter` 为 `NULL`，或者文件系统未挂载时，返回 `-EINVAL`。

## 59.15\_带过滤配置初始化迭代器

[`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 函数的声明如下：

```c
int zms_iter_init_with_config(const struct zms_fs * fs, struct zms_iter * iter, const struct zms_iter_config * config);
```

以已挂载的 `fs`、待初始化的 `iter` 和调用者提供的 `config` 初始化迭代器，记录当前写入位置作为遍历边界。原文说明，之后写入或删除的条目不会出现在随后 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 的结果中。

启用的过滤条件共同限制返回条目：

- `config->use_mask == true` 时，要求 `(id & config->mask_id) == id`。
- `config->use_range == true` 时，要求标识符位于包含端点的 `[config->min_id, config->max_id]` 区间。
- `config->use_predicate == true` 时，要求 `config->predicate_func(id)` 返回 `true`。

禁用掩码或范围过滤时，分别回退到 [`ZMS_ITER_MASK_ALL`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#gaa03cc6d1704e0ac7e5af869a7211677e) 或完整的 `[ZMS_ITER_ID_MIN, ZMS_ITER_ID_MAX]` 范围；谓词过滤默认禁用。

**调用者不得在该初始化调用到最后一次 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 之间向 `fs` 写入或删除。**

成功返回 0。以下任一情况返回 `-EINVAL`：`fs`、`iter` 或 `config` 为 `NULL`；文件系统未挂载；启用 `use_predicate` 却将 `predicate_func` 设为 `NULL`；配置的范围无效。

## 59.16\_遍历有效最新条目

[`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 函数的声明如下：

```c
int zms_iter_next(struct zms_fs * fs, struct zms_iter * iter, zms_id_t * id, size_t * len, void * data, size_t data_len);
```

按**从新到旧**的顺序遍历 ATE 环。对每个标识符，只返回最近写入且未删除的条目（长度大于 0），自动跳过更旧历史版本与**删除标记（Delete Marker）**。

| 参数 | 含义 |
| --- | --- |
| `fs` | 已挂载实例 |
| `iter` | 通过 [`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d) 或 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 初始化的状态 |
| `id` | 返回 1 时写入找到的条目标识符 |
| `len` | 返回 1 时写入存储的数据长度，单位为字节 |
| `data` | 调用者可选分配的缓冲区；为 `NULL` 时不复制数据 |
| `data_len` | `data` 缓冲区的字节容量；`data == NULL` 时忽略 |

仅当返回长度不超过 [`ZMS_DATA_IN_ATE_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga758c42a254d0e64596c35c7ac644aedc)、数据直接保存在 ATE 内且提供了缓冲区时，才直接复制数据，不额外读取闪存。最多复制 `data_len` 字节；要取得全部内嵌数据，应确保 `data_len >= *len`。更大条目的数据不会复制，必须用 [`zms_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f) 读取。

| 返回值 | 含义 |
| --- | --- |
| `1` | 找到条目，`id` 和 `len` 输出有效 |
| `0` | 已无条目，遍历完成 |
| `-EINVAL` | `fs`、`iter`、`id` 或 `len` 为 `NULL`，或文件系统未挂载 |
| `-EIO` | 闪存读取错误 |
| `-ENXIO` | 设备错误 |

## 59.17\_遍历全部匹配ATE

[`zms_iter_next_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348) 函数的声明如下：

```c
int zms_iter_next_all(struct zms_fs * fs, struct zms_iter * iter, zms_id_t * id, size_t * len, void * data, size_t data_len);
```

按**从新到旧**遍历 ATE 环，返回全部匹配 ATE，包括删除标记（长度为 0）和更旧的历史版本。该函数不进行标识符唯一性过滤，因此同一标识符可多次出现。

| 参数 | 含义 |
| --- | --- |
| `fs` | 已挂载实例 |
| `iter` | 通过 [`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d) 或 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 初始化的状态 |
| `id` | 返回 1 时写入条目标识符 |
| `len` | 返回 1 时写入存储数据字节数；0 表示删除标记 |
| `data` | 可选的调用者缓冲区；为 `NULL` 时跳过复制 |
| `data_len` | 缓冲区字节容量；`data == NULL` 时忽略 |

只有直接存于 ATE 内、长度不超过 [`ZMS_DATA_IN_ATE_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga758c42a254d0e64596c35c7ac644aedc) 的非删除数据才会复制到非空缓冲区，无需额外闪存读取。最多复制 `data_len` 字节，完整接收需满足 `data_len >= *len`。更大条目和删除标记均不复制；读取最新值用 [`zms_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f)，读取旧版本用 [`zms_read_hist()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga6cedc2fe5bfe8aa6183d41273897f0e7)。

| 返回值 | 含义 |
| --- | --- |
| `1` | 找到条目，`id` 和 `len` 有效 |
| `0` | 已无条目，遍历完成 |
| `-EINVAL` | `fs`、`iter`、`id` 或 `len` 为 `NULL`，或文件系统未挂载 |
| `-EIO` | 闪存读取错误 |
| `-ENXIO` | 设备错误 |

---

[上一章：Zephyr内存存储数据结构目录](P058_Zephyr内存存储数据结构目录.md) · [下一章：Zephyr内存存储实例结构](P060_Zephyr内存存储实例结构.md) · [返回大纲](大纲.md)
