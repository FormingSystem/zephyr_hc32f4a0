---
id: learning.zephyr-docs.device-power-control-model-reference.page-65
title: pulse_io_decoder_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__decoder__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_pulse\_io\_decoder\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__decoder__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

解码器虚表（Decoder Vtable）：将脉冲符号转换为协议字节。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

解码器虚函数表（Decoder vtable）：将脉冲符号转换为协议字节。`tolerance_ticks` 指定逐符号的容差，在将捕获的持续时间与位模板匹配时使用，以容纳接收流中的时序漂移。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a3898c1fec9586b45606c9071ddba21a5"></a>

```c
int(* decode )(const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks, const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap, size_t *produced)
```

相关声明：[decode](#a3898c1fec9586b45606c9071ddba21a5)、[pulse_io_bit_template](P062_pulse_io_bit_template_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pulse_symbol](P070_pulse_symbol_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据捕获的脉冲符号重建字节流。

## 65.2\_详细说明（Detailed Documentation）

<a id="a3898c1fec9586b45606c9071ddba21a5"></a>

### `decode`

```c
int(* pulse_io_decoder_api::decode) (const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks, const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap, size_t *produced)
```

根据捕获的脉冲符号重建字节流。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [pulse_io_bit_template](P062_pulse_io_bit_template_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pulse_symbol](P070_pulse_symbol_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_pulse_io_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_pulse_io_driver_api_结构体.md)
