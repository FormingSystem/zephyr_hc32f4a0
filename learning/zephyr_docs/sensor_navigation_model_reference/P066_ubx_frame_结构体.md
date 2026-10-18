---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-66
title: ubx_frame_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_ubx\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__frame.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_acf80f38e8f26bb32848ae2978a1f87a1"></a>

```c
uint8_t preamble_sync_char_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[preamble_sync_char_1](#acf80f38e8f26bb32848ae2978a1f87a1)。

<a id="r_ac61fb72df7c1cd8a9bacb787071cb77d"></a>

```c
uint8_t preamble_sync_char_2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[preamble_sync_char_2](#ac61fb72df7c1cd8a9bacb787071cb77d)。

<a id="r_a2dcc29a82e7dfff2d1e4194f1bc035e8"></a>

```c
uint8_t class
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[class](#a2dcc29a82e7dfff2d1e4194f1bc035e8)。

<a id="r_a4e578da5900365d498708f7a61d48ba4"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a4e578da5900365d498708f7a61d48ba4)。

<a id="r_a77b5030a6b95aef58b1c17f0368dd7ce"></a>

```c
uint16_t payload_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[payload_size](#a77b5030a6b95aef58b1c17f0368dd7ce)。

<a id="r_a70c465b5bd1e9837c253d78fb210f4ce"></a>

```c
uint8_t payload_and_checksum []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_and_checksum](#a70c465b5bd1e9837c253d78fb210f4ce)。

## 66.2\_详细说明（Detailed Documentation）

<a id="a2dcc29a82e7dfff2d1e4194f1bc035e8"></a>

### `class`

```c
uint8_t ubx_frame::class
```

<a id="a4e578da5900365d498708f7a61d48ba4"></a>

### `id`

```c
uint8_t ubx_frame::id
```

<a id="a70c465b5bd1e9837c253d78fb210f4ce"></a>

### `payload_and_checksum`

```c
uint8_t ubx_frame::payload_and_checksum[]
```

<a id="a77b5030a6b95aef58b1c17f0368dd7ce"></a>

### `payload_size`

```c
uint16_t ubx_frame::payload_size
```

<a id="acf80f38e8f26bb32848ae2978a1f87a1"></a>

### `preamble_sync_char_1`

```c
uint8_t ubx_frame::preamble_sync_char_1
```

<a id="ac61fb72df7c1cd8a9bacb787071cb77d"></a>

### `preamble_sync_char_2`

```c
uint8_t ubx_frame::preamble_sync_char_2
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_ubx_cfg_val_u8_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_ubx_frame_match_结构体.md)
