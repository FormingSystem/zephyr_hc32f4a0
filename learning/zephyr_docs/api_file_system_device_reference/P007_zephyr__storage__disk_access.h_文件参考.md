---
id: learning.zephyr-docs.api-file-system-device-reference.page-7
title: zephyr__storage__disk_access.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_storage\_\_disk\_access.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘访问层（Disk Access Layer）的API。

<a id="details"></a>

```c
#include <zephyr/drivers/disk.h>
```

查看此文件的源码。

磁盘访问层 API（Disk Access layer API）。本文件包含用于访问磁盘的 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.1\_枚举（Enumerations）

<a id="r_gab666eac293bae609ee600ebb2b105373"></a>

```c
enum disk_access_erase_type { DISK_ACCESS_ERASE_PHYSICAL = 0 }
```

相关声明：[disk_access_erase_type](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gab666eac293bae609ee600ebb2b105373)、[DISK_ACCESS_ERASE_PHYSICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.2\_函数（Functions）

<a id="r_gaba3fead8c0ce65945b440bf824fd4144"></a>

```c
int disk_access_init (const char *pdrv)
```

相关声明：[disk_access_init](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaba3fead8c0ce65945b440bf824fd4144)。

执行所需的初始化。

<a id="r_gac5348a854fe68a607672118c91346133"></a>

```c
int disk_access_status (const char *pdrv)
```

相关声明：[disk_access_status](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)。

获取磁盘状态（disk status）。

<a id="r_ga5152825bf2a70902e65dbc596a944a1b"></a>

```c
int disk_access_read (const char *pdrv, uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[disk_access_read](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga5152825bf2a70902e65dbc596a944a1b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从磁盘读取数据。

<a id="r_gaa0495600320a71ea9e861fcf19da7184"></a>

```c
int disk_access_write (const char *pdrv, const uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[disk_access_write](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaa0495600320a71ea9e861fcf19da7184)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向磁盘写入数据。

<a id="r_gafb8528762248a3dcbe7e4d0a9ee31890"></a>

```c
int disk_access_erase (const char *pdrv, uint32_t start_sector, uint32_t num_sector, enum disk_access_erase_type erase_type)
```

相关声明：[disk_access_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gafb8528762248a3dcbe7e4d0a9ee31890)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[disk_access_erase_type](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gab666eac293bae609ee600ebb2b105373)。

从磁盘擦除数据。

<a id="r_ga152d85821d73644fea7ffde27b7c953c"></a>

```c
int disk_access_ioctl (const char *pdrv, uint8_t cmd, void *buff)
```

相关声明：[disk_access_ioctl](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga152d85821d73644fea7ffde27b7c953c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

获取／配置磁盘参数（disk parameters）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/disk.h](../peripheral_bus_storage_source_reference/P003_zephyr__drivers__disk.h_头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P135_disk_access.h_源码浏览.md)
- [disk_access_erase_type](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gab666eac293bae609ee600ebb2b105373)
- [DISK_ACCESS_ERASE_PHYSICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6)
- [disk_access_init](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaba3fead8c0ce65945b440bf824fd4144)
- [disk_access_status](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)
- [disk_access_read](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga5152825bf2a70902e65dbc596a944a1b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [disk_access_write](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaa0495600320a71ea9e861fcf19da7184)
- [disk_access_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gafb8528762248a3dcbe7e4d0a9ee31890)
- [disk_access_ioctl](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga152d85821d73644fea7ffde27b7c953c)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>

---

[上一章](P006_zephyr__dt-bindings__input__cst8xx-gesture-codes.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__xen__dmop.h_文件参考.md)
