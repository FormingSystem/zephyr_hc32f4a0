---
id: learning.zephyr-docs.storage.storagehdr-4
title: Zephyr内存存储头文件
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kvss_2zms_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第75章\_Zephyr内存存储头文件

原文：[kvss_2zms_8h](https://docs.zephyrproject.org/latest/doxygen/html/kvss_2zms_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/kvss/zms.h` 声明**Zephyr 内存存储（Zephyr Memory Storage，ZMS）应用编程接口（Application Programming Interface，API）**。

## 75.1\_包含关系

官方头文件的包含项如下：

```c
#include <sys/types.h>
#include <zephyr/drivers/flash.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/toolchain.h>
```

[查看官方源文件页面](https://docs.zephyrproject.org/latest/doxygen/html/kvss_2zms_8h_source.html)。

## 75.2\_结构、宏与类型

**分配表条目（Allocation Table Entry，ATE）**可内嵌小数据；**迭代器（Iterator）**用于遍历存储内容。

| 结构 | 中文说明 |
| --- | --- |
| `struct zms_fs` | ZMS 文件系统实例 |
| `struct zms_iter_config` | 带配置迭代器初始化所用的配置 |
| `struct zms_iter` | 两种迭代推进接口使用的不透明状态（Opaque State） |

| 宏及原页定义 | 中文说明 |
| --- | --- |
| `ZMS_DATA_IN_ATE_SIZE 8` | 直接存储在 ATE 中的最大数据字节数 |
| `ZMS_ITER_ID_MIN ((zms_id_t)0)` | 迭代器范围过滤的默认最小标识符 |
| `ZMS_ITER_ID_MAX ((zms_id_t)~(zms_id_t)0)` | 迭代器范围过滤的默认最大标识符 |
| `ZMS_ITER_MASK_ALL ZMS_ITER_ID_MAX` | 接受全部标识符的默认掩码 |
| [`ZMS_ITER_CONFIG_DEFAULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga1ee4de45e9df1784664fcba45e9a8788) | [`zms_iter_config`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html) 的默认初始化器；本页未展开宏体 |

类型 [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) 用作标识符，[`zms_iter_predicate_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga73c4c209bc4fbb8125781088b15eef64) 是初始化时使用的谓词回调（Predicate Callback）。以下保留原页显示的声明，配置对宽度的影响详见[ZMS数据结构](P058_Zephyr内存存储数据结构目录.md)。

```c
typedef uint32_t zms_id_t;
typedef bool (*zms_iter_predicate_t)(zms_id_t id);
```

枚举 [`zms_mount_flags`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga5f9a7529c95876c29b6a0fd7a230fc92) 定义普通和强制挂载的选项；[`ZMS_MOUNT_FLAG_NO_FORMAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#gga5f9a7529c95876c29b6a0fd7a230fc92a0b00eefe2f9cc169d285ad8255521c87) 为禁止挂载时自动格式化的标志，`BIT(0)` 是第 0 位掩码。

```c
enum zms_mount_flags {
    ZMS_MOUNT_FLAG_NO_FORMAT = BIT(0)
};
```

## 75.3\_函数声明与中文索引

函数 [`zms_mount()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga962625b12f21cf030a35c944a2de380e)：将 ZMS 文件系统挂载到 `fs` 指定的设备。

```c
int zms_mount(struct zms_fs *fs);
```

函数 [`zms_mount_force()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gab5a3adcdc5eecbb8a1bcb9d1c7709837)：挂载文件系统；第一次挂载失败时清空分区再挂载。

```c
int zms_mount_force(struct zms_fs *fs);
```

函数 [`zms_clear()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gafe06d28af34fbecf2bd666ef11095ed1)：从设备清除 ZMS 文件系统。

```c
int zms_clear(struct zms_fs *fs);
```

函数 [`zms_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga218132ef5cb0f2157721cb62886de842)：写入一个条目。

```c
ssize_t zms_write(struct zms_fs *fs, zms_id_t id, const void *data, size_t len);
```

函数 [`zms_delete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga60ad1d79cd4f3ada1cf726d422c120c3)：删除一个条目。

```c
int zms_delete(struct zms_fs *fs, zms_id_t id);
```

函数 [`zms_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f)：读取一个条目。

```c
ssize_t zms_read(struct zms_fs *fs, zms_id_t id, void *data, size_t len);
```

函数 [`zms_read_hist()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga6cedc2fe5bfe8aa6183d41273897f0e7)：读取条目的历史版本。

```c
ssize_t zms_read_hist(struct zms_fs *fs, zms_id_t id, void *data, size_t len, uint32_t cnt);
```

函数 [`zms_get_data_length()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8871cfa165587b259a8043d22bf669a4)：查询给定标识符条目的数据长度。

```c
ssize_t zms_get_data_length(struct zms_fs *fs, zms_id_t id);
```

函数 [`zms_calc_free_space()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga02be33c18632687133f53557b5ee8bc2)：计算文件系统可用空闲空间。

```c
ssize_t zms_calc_free_space(struct zms_fs *fs);
```

函数 [`zms_active_sector_free_space()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga76e06261e54f9d2ee65f7d31328e3bcc)：查询当前活动扇区的连续空闲空间。

```c
ssize_t zms_active_sector_free_space(struct zms_fs *fs);
```

函数 [`zms_sector_use_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga90a6f8c47f02641ca33ee42a7c709750)：关闭当前活动扇区并切换到下一个扇区。

```c
int zms_sector_use_next(struct zms_fs *fs);
```

函数 [`zms_get_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga31b8d970e70fd7cbb94a0dc068dbdcfc)：返回所有扇区中的最大再利用循环次数（Recycle Count）。

```c
int zms_get_num_cycles(struct zms_fs *fs, uint32_t *cycles);
```

函数 [`zms_get_sector_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga4aa193a3c357335a6d403139371803ab)：返回指定扇区的再利用循环次数。

```c
int zms_get_sector_num_cycles(struct zms_fs *fs, uint32_t sector, uint32_t *cycles);
```

函数 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34)：根据过滤配置初始化迭代器。

```c
int zms_iter_init_with_config(const struct zms_fs *fs, struct zms_iter *iter, const struct zms_iter_config *config);
```

函数 [`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d)：初始化迭代器。

```c
int zms_iter_init(const struct zms_fs *fs, struct zms_iter *iter);
```

函数 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3)：前进到下一个仍有效的条目（Live Entry）。

```c
int zms_iter_next(struct zms_fs *fs, struct zms_iter *iter, zms_id_t *id, size_t *len, void *data, size_t data_len);
```

函数 [`zms_iter_next_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348)：前进到下一个匹配的 ATE。

```c
int zms_iter_next_all(struct zms_fs *fs, struct zms_iter *iter, zms_id_t *id, size_t *len, void *data, size_t data_len);
```

参数、返回值和使用条件见[对应接口参考](P059_Zephyr内存存储接口.md)。

---

[上一章：Zephyr内存存储旧接口头文件](P074_Zephyr内存存储旧接口头文件.md) · [下一章：设置子系统头文件](P076_设置子系统头文件.md) · [返回大纲](大纲.md)
