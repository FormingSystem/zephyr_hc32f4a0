---
id: learning.zephyr-docs.system-service-model-reference.page-27
title: flash_area_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_flash\_area\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

闪存分区（Flash Partition）。

```c
#include <zephyr/storage/flash_map.h>
```

<a id="details"></a>

Flash 分区（Flash partition）。此结构体表示 Flash 设备上的固定大小分区，每个分区包含一个或多个 Flash 扇区（sector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_acfe73a1f4f00fdf58129b21e5b71f5d4"></a>

```c
uint8_t fa_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fa_id](#acfe73a1f4f00fdf58129b21e5b71f5d4)。

ID 编号。

<a id="r_af98b8f20c0219bfcdd2fc20037845a99"></a>

```c
uint16_t pad16
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pad16](#af98b8f20c0219bfcdd2fc20037845a99)。

<a id="r_a3a362ad9aa44725a0b0188042a2ee257"></a>

```c
off_t fa_off
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[fa_off](#a3a362ad9aa44725a0b0188042a2ee257)。

相对于 Flash 设备起始位置的起始偏移量。

<a id="r_a6c3c23c4c628f48c92505dddf4b24edf"></a>

```c
size_t fa_size
```

相关声明：[fa_size](#a6c3c23c4c628f48c92505dddf4b24edf)。

总大小。

<a id="r_a941637492ab4e321e3b08de19cd769d2"></a>

```c
const struct device * fa_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[fa_dev](#a941637492ab4e321e3b08de19cd769d2)。

提供后备存储的 Flash 设备。

## 27.2\_详细说明（Detailed Documentation）

<a id="a941637492ab4e321e3b08de19cd769d2"></a>

### `fa_dev`

```c
const struct device* flash_area::fa_dev
```

提供后备存储的 Flash 设备。

<a id="acfe73a1f4f00fdf58129b21e5b71f5d4"></a>

### `fa_id`

```c
uint8_t flash_area::fa_id
```

ID 编号。

<a id="a3a362ad9aa44725a0b0188042a2ee257"></a>

### `fa_off`

```c
off_t flash_area::fa_off
```

相对于 Flash 设备起始位置的起始偏移量。

<a id="a6c3c23c4c628f48c92505dddf4b24edf"></a>

### `fa_size`

```c
size_t flash_area::fa_size
```

总大小。

<a id="af98b8f20c0219bfcdd2fc20037845a99"></a>

### `pad16`

```c
uint16_t flash_area::pad16
```

本数据类型文档由以下文件生成：

- `zephyr/storage/flash_map.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/storage/flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_enum_mgmt_detail_output_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_flash_img_check_结构体.md)
