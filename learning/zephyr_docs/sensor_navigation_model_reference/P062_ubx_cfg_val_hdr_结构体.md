---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-62
title: ubx_cfg_val_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_ubx\_cfg\_val\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a4d7a91e9521428e5b528ced88b030cd3"></a>

```c
uint8_t ver
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ver](#a4d7a91e9521428e5b528ced88b030cd3)。

<a id="r_aa835050e25c8db0a5a88954ff0def88c"></a>

```c
uint8_t layer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[layer](#aa835050e25c8db0a5a88954ff0def88c)。

<a id="r_a6206dc714df9656cc37e0b802ab541b8"></a>

```c
uint16_t position
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[position](#a6206dc714df9656cc37e0b802ab541b8)。

## 62.2\_详细说明（Detailed Documentation）

<a id="aa835050e25c8db0a5a88954ff0def88c"></a>

### `layer`

```c
uint8_t ubx_cfg_val_hdr::layer
```

<a id="a6206dc714df9656cc37e0b802ab541b8"></a>

### `position`

```c
uint16_t ubx_cfg_val_hdr::position
```

<a id="a4d7a91e9521428e5b528ced88b030cd3"></a>

### `ver`

```c
uint8_t ubx_cfg_val_hdr::ver
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_ubx_cfg_rst_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_ubx_cfg_val_u16_结构体.md)
