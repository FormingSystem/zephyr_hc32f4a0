---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-65
title: ubx_cfg_val_u8_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u8.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_ubx\_cfg\_val\_u8\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u8.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a793646932ce054ab8561078981f57250"></a>

```c
struct ubx_cfg_val_hdr hdr
```

相关声明：[ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)、[hdr](#a793646932ce054ab8561078981f57250)。

<a id="r_a2c1cbf9a552608150eafc1f2d92b03b5"></a>

```c
uint32_t key
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[key](#a2c1cbf9a552608150eafc1f2d92b03b5)。

<a id="r_a325aaaf688433cab710d0c3e835fb9ed"></a>

```c
uint8_t value
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value](#a325aaaf688433cab710d0c3e835fb9ed)。

## 65.2\_详细说明（Detailed Documentation）

<a id="a793646932ce054ab8561078981f57250"></a>

### `hdr`

```c
struct ubx_cfg_val_hdr ubx_cfg_val_u8::hdr
```

<a id="a2c1cbf9a552608150eafc1f2d92b03b5"></a>

### `key`

```c
uint32_t ubx_cfg_val_u8::key
```

<a id="a325aaaf688433cab710d0c3e835fb9ed"></a>

### `value`

```c
uint8_t ubx_cfg_val_u8::value
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_ubx_cfg_val_u32_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_ubx_frame_结构体.md)
