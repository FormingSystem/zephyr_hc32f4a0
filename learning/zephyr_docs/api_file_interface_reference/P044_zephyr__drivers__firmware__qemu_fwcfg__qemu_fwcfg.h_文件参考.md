---
id: learning.zephyr-docs.api-file-interface-reference.page-44
title: zephyr__drivers__firmware__qemu_fwcfg__qemu_fwcfg.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_drivers\_\_firmware\_\_qemu\_fwcfg\_\_qemu\_fwcfg.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

QEMU固件配置（Firmware Configuration，fw_cfg）驱动的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

QEMU固件配置（Firmware Configuration，fw_cfg）驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 44.1\_函数（Functions）

<a id="r_ga118812a7348407f9e487c5f55e825ba2"></a>

```c
int qemu_fwcfg_read_item (const struct device *dev, uint16_t key, void *buf, size_t len)
```

相关声明：[qemu_fwcfg_read_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#ga118812a7348407f9e487c5f55e825ba2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `fw_cfg` 条目中读取数据。

<a id="r_gae48557d89be4df85a9308c9a0c8b4454"></a>

```c
int qemu_fwcfg_write_item (const struct device *dev, uint16_t key, const void *buf, size_t len)
```

相关声明：[qemu_fwcfg_write_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gae48557d89be4df85a9308c9a0c8b4454)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `fw_cfg` 条目写入数据。

<a id="r_gac3b30171a9b46599efa30324d44b58a8"></a>

```c
int qemu_fwcfg_get_features (const struct device *dev, uint32_t *features)
```

相关声明：[qemu_fwcfg_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gac3b30171a9b46599efa30324d44b58a8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取设备报告的 `fw_cfg` 功能位（feature bits）。

<a id="r_gabfbe0c933d36f47b1e54c0e95c981eae"></a>

```c
int qemu_fwcfg_find_file (const struct device *dev, const char *file, uint16_t *select, uint32_t *size)
```

相关声明：[qemu_fwcfg_find_file](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gabfbe0c933d36f47b1e54c0e95c981eae)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[select](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在 `fw_cfg` 文件目录中查找文件条目（file entry）。

<a id="r_gaab1f00f9d5d9df199b9d35fbb6aa2f64"></a>

```c
bool qemu_fwcfg_dma_supported (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[qemu_fwcfg_dma_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gaab1f00f9d5d9df199b9d35fbb6aa2f64)、[device](../device_reference/P002_设备对象结构.md)。

检查 `fw_cfg` DMA 功能是否可用。


## 44.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P691_qemu_fwcfg.h_源码浏览.md)
- [qemu_fwcfg_read_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#ga118812a7348407f9e487c5f55e825ba2)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [qemu_fwcfg_write_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gae48557d89be4df85a9308c9a0c8b4454)
- [qemu_fwcfg_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gac3b30171a9b46599efa30324d44b58a8)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [qemu_fwcfg_find_file](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gabfbe0c933d36f47b1e54c0e95c981eae)
- [select](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [qemu_fwcfg_dma_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gaab1f00f9d5d9df199b9d35fbb6aa2f64)

<a id="header-details"></a>

---

[上一章](P043_zephyr__drivers__pinctrl__pinctrl_rp1_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__dt-bindings__clock__ra_clock.h_文件参考.md)
