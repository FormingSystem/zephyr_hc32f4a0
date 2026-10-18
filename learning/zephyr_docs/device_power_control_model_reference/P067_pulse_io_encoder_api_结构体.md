---
id: learning.zephyr-docs.device-power-control-model-reference.page-67
title: pulse_io_encoder_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__encoder__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_pulse\_io\_encoder\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__encoder__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

编码器虚表（Encoder Vtable）：将协议字节转换为脉冲符号。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

编码器虚表（Encoder Vtable）：将协议字节转换为脉冲符号。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_ab5d90fd2dc5832a0f9d48078b1d1193c"></a>

```c
int(* encode )(const struct pulse_io_bit_template *tmpl, const uint8_t *bytes, size_t nbytes, struct pulse_symbol *out, size_t out_cap, size_t *produced)
```

相关声明：[encode](#ab5d90fd2dc5832a0f9d48078b1d1193c)、[pulse_io_bit_template](P062_pulse_io_bit_template_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pulse_symbol](P070_pulse_symbol_结构体.md)。

将字节流展开为脉冲符号。

## 67.2\_详细说明（Detailed Documentation）

<a id="ab5d90fd2dc5832a0f9d48078b1d1193c"></a>

### `encode`

```c
int(* pulse_io_encoder_api::encode) (const struct pulse_io_bit_template *tmpl, const uint8_t *bytes, size_t nbytes, struct pulse_symbol *out, size_t out_cap, size_t *produced)
```

将字节流展开为脉冲符号。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [pulse_io_bit_template](P062_pulse_io_bit_template_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pulse_symbol](P070_pulse_symbol_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_pulse_io_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_pulse_io_rx_req_结构体.md)
