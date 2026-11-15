---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-11
title: QEMU 固件配置（fw_cfg）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_QEMU 固件配置（fw\_cfg）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

QEMU 固件配置（Firmware configuration，fw_cfg）驱动接口。

<a id="details"></a>

QEMU 固件配置（Firmware Configuration，fw_cfg）驱动接口。**引入版本（Since）：**4.4.0。**版本（Version）：**0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_qemu_5Ffwcfg_2Eh"></a>

```c
file qemu_fwcfg.h
```

相关声明：[qemu_fwcfg.h](../api_file_interface_reference/P044_zephyr__drivers__firmware__qemu_fwcfg__qemu_fwcfg.h_文件参考.md)。

QEMU固件配置（Firmware Configuration，fw_cfg）驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_ga118812a7348407f9e487c5f55e825ba2"></a>

```c
int qemu_fwcfg_read_item (const struct device *dev, uint16_t key, void *buf, size_t len)
```

相关声明：[qemu_fwcfg_read_item](#ga118812a7348407f9e487c5f55e825ba2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `fw_cfg` 条目中读取数据。

<a id="r_gae48557d89be4df85a9308c9a0c8b4454"></a>

```c
int qemu_fwcfg_write_item (const struct device *dev, uint16_t key, const void *buf, size_t len)
```

相关声明：[qemu_fwcfg_write_item](#gae48557d89be4df85a9308c9a0c8b4454)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `fw_cfg` 条目写入数据。

<a id="r_gac3b30171a9b46599efa30324d44b58a8"></a>

```c
int qemu_fwcfg_get_features (const struct device *dev, uint32_t *features)
```

相关声明：[qemu_fwcfg_get_features](#gac3b30171a9b46599efa30324d44b58a8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取设备报告的 `fw_cfg` 功能位（feature bits）。

<a id="r_gabfbe0c933d36f47b1e54c0e95c981eae"></a>

```c
int qemu_fwcfg_find_file (const struct device *dev, const char *file, uint16_t *select, uint32_t *size)
```

相关声明：[qemu_fwcfg_find_file](#gabfbe0c933d36f47b1e54c0e95c981eae)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[select](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在 `fw_cfg` 文件目录中查找文件条目（file entry）。

<a id="r_gaab1f00f9d5d9df199b9d35fbb6aa2f64"></a>

```c
bool qemu_fwcfg_dma_supported (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[qemu_fwcfg_dma_supported](#gaab1f00f9d5d9df199b9d35fbb6aa2f64)、[device](../device_reference/P002_设备对象结构.md)。

检查 `fw_cfg` DMA 功能是否可用。

## 11.3\_详细说明（Detailed Documentation）

<a id="gaab1f00f9d5d9df199b9d35fbb6aa2f64"></a>

### `qemu_fwcfg_dma_supported()`

```c
bool qemu_fwcfg_dma_supported ( const struct device * dev)
```

```c
#include <zephyr/drivers/firmware/qemu_fwcfg/qemu_fwcfg.h>
```

检查 `fw_cfg` DMA 功能是否可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 固件配置（fw_cfg）设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 直接内存访问（DMA）功能可用时。 |
| `false` | 其他情况。 |

<a id="gabfbe0c933d36f47b1e54c0e95c981eae"></a>

### `qemu_fwcfg_find_file()`

```c
int qemu_fwcfg_find_file ( const struct device * dev, const char * file, uint16_t * select, uint32_t * size )
```

```c
#include <zephyr/drivers/firmware/qemu_fwcfg/qemu_fwcfg.h>
```

在 `fw_cfg` 文件目录中查找文件条目（file entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 固件配置（fw_cfg）设备。 |
| `file` | 要搜索的文件名称（File Name）。 |
| `select` | 用于保存文件选择键（Selector Key）的指针。 |
| `size` | 用于保存文件大小的指针，大小以字节为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOENT` | 文件不存在时。 |

<a id="gac3b30171a9b46599efa30324d44b58a8"></a>

### `qemu_fwcfg_get_features()`

```c
int qemu_fwcfg_get_features ( const struct device * dev, uint32_t * features )
```

```c
#include <zephyr/drivers/firmware/qemu_fwcfg/qemu_fwcfg.h>
```

获取设备报告的 `fw_cfg` 功能位（feature bits）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 固件配置（fw_cfg）设备。 |
| `features` | 用于保存功能位（Feature Bits）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga118812a7348407f9e487c5f55e825ba2"></a>

### `qemu_fwcfg_read_item()`

```c
int qemu_fwcfg_read_item ( const struct device * dev, uint16_t key, void * buf, size_t len )
```

```c
#include <zephyr/drivers/firmware/qemu_fwcfg/qemu_fwcfg.h>
```

从 `fw_cfg` 条目中读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 固件配置（fw_cfg）设备。 |
| `key` | fw_cfg 项的选择键（Selector Key）。 |
| `buf` | 目标缓冲区。 |
| `len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 设备报告输入／输出错误（I/O Error）时。 |
| `-ETIMEDOUT` | DMA 传输未及时完成时。 |

<a id="gae48557d89be4df85a9308c9a0c8b4454"></a>

### `qemu_fwcfg_write_item()`

```c
int qemu_fwcfg_write_item ( const struct device * dev, uint16_t key, const void * buf, size_t len )
```

```c
#include <zephyr/drivers/firmware/qemu_fwcfg/qemu_fwcfg.h>
```

向 `fw_cfg` 条目写入数据。

仅在 fw_cfg DMA 功能可用时支持写入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 固件配置（fw_cfg）设备。 |
| `key` | fw_cfg 项的选择键（Selector Key）。 |
| `buf` | 源缓冲区。 |
| `len` | 要写入的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | 不支持 DMA 写入时。 |
| `-EIO` | 设备报告输入／输出错误（I/O Error）时。 |
| `-ETIMEDOUT` | DMA 传输未及时完成时。 |


## 11.4\_原页交叉引用（Cross References）

- [qemu_fwcfg.h](../api_file_interface_reference/P044_zephyr__drivers__firmware__qemu_fwcfg__qemu_fwcfg.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [select](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_PAJ7620 API主题.md) · [返回大纲](大纲.md) · [下一章](P012_RM3100 API主题.md)
