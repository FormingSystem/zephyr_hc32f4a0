---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-52
title: mux_control_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmux__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_mux\_control\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmux__control.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单条多路复用器（MUX）控制线仅用于寻址的说明符。

```c
#include <zephyr/drivers/mux.h>
```

<a id="details"></a>

单条多路复用器（MUX）控制线的纯寻址说明符（Addressing-only specifier）。一个 `mux_control` 标识 MUX 控制器的单个输出。其 `cells` 数组仅保存设备树 `mux-controls` 说明符的寻址部分，不包含状态单元（State cell）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a39c222d2b469939eddf03b75abe7001b"></a>

```c
const uint32_t * cells
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cells](#a39c222d2b469939eddf03b75abe7001b)。

指向设备树说明符中寻址单元（Addressing cells）的指针。

<a id="r_a3c4c949a57de565642d00fe0b6380ad7"></a>

```c
size_t len
```

相关声明：[len](#a3c4c949a57de565642d00fe0b6380ad7)。

寻址单元数量，与 `#mux-control-cells` 一致。

## 52.2\_详细说明（Detailed Documentation）

<a id="a39c222d2b469939eddf03b75abe7001b"></a>

### `cells`

```c
const uint32_t* mux_control::cells
```

指向设备树说明符中寻址单元（Addressing cells）的指针。

<a id="a3c4c949a57de565642d00fe0b6380ad7"></a>

### `len`

```c
size_t mux_control::len
```

寻址单元数量，与 `#mux-control-cells` 一致。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mux.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mux.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mux_control](P052_mux_control_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_mspi_xfer_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_mux_control_driver_api_结构体.md)
