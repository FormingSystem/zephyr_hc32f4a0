---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-85
title: sdio_cis_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdio__cis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_sdio\_cis\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdio__cis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SDIO通用卡信息结构（CIS）元组的属性。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

SDIO 公共卡信息结构（Card Information Structure，CIS）元组属性。功能 1–7 还有其他属性，但由于协议栈未使用这些数据，此处不读取它们。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_a04c8a774c65f683185e5a32e15afb67c"></a>

```c
uint16_t manf_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[manf_id](#a04c8a774c65f683185e5a32e15afb67c)。

制造商 ID（Manufacturer ID）。

<a id="r_ad52e1df89176f728734ce0e69fb2b4c8"></a>

```c
uint16_t manf_code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[manf_code](#ad52e1df89176f728734ce0e69fb2b4c8)。

制造商代码（Manufacturer code）。

<a id="r_ad38be5cade97ac92de62094d8e3b8549"></a>

```c
uint8_t func_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[func_id](#ad38be5cade97ac92de62094d8e3b8549)。

SDIO 设备类别功能 ID（Device class function ID）。

<a id="r_a1b340e20630994f91314be17dd9055ca"></a>

```c
uint16_t max_blk_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_blk_size](#a1b340e20630994f91314be17dd9055ca)。

最大传输块大小。

<a id="r_a56d3ee1d6b8d0d87e0efdbda15b7076d"></a>

```c
uint8_t max_speed
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_speed](#a56d3ee1d6b8d0d87e0efdbda15b7076d)。

最大传输速率。

<a id="r_a86a01890f31788ae5465b1c8dc47bcf2"></a>

```c
uint16_t rdy_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rdy_timeout](#a86a01890f31788ae5465b1c8dc47bcf2)。

I/O 就绪超时（I/O ready timeout）。

## 85.2\_详细说明（Detailed Documentation）

<a id="ad38be5cade97ac92de62094d8e3b8549"></a>

### `func_id`

```c
uint8_t sdio_cis::func_id
```

SDIO 设备类别功能 ID（Device class function ID）。

<a id="ad52e1df89176f728734ce0e69fb2b4c8"></a>

### `manf_code`

```c
uint16_t sdio_cis::manf_code
```

制造商代码（Manufacturer code）。

<a id="a04c8a774c65f683185e5a32e15afb67c"></a>

### `manf_id`

```c
uint16_t sdio_cis::manf_id
```

制造商 ID（Manufacturer ID）。

<a id="a1b340e20630994f91314be17dd9055ca"></a>

### `max_blk_size`

```c
uint16_t sdio_cis::max_blk_size
```

最大传输块大小。

<a id="a56d3ee1d6b8d0d87e0efdbda15b7076d"></a>

### `max_speed`

```c
uint8_t sdio_cis::max_speed
```

最大传输速率。

<a id="a86a01890f31788ae5465b1c8dc47bcf2"></a>

### `rdy_timeout`

```c
uint16_t sdio_cis::rdy_timeout
```

I/O 就绪超时（I/O ready timeout）。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_sdhc_io_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_sdio_func_结构体.md)
