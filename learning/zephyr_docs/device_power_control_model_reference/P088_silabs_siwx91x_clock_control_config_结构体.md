---
id: learning.zephyr-docs.device-power-control-model-reference.page-88
title: silabs_siwx91x_clock_control_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__siwx91x__clock__control__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_silabs\_siwx91x\_clock\_control\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__siwx91x__clock__control__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SiWx91x时钟管理器的多路选择/门控时钟（Mux / Gate Clock）配置。

```c
#include <zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h>
```

<a id="details"></a>

SiWx91x时钟管理器的多路选择/门控时钟（Mux / Gate Clock）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_aa14c50b1e6a313daa690b016cdb7305c"></a>

```c
uint32_t clkid
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clkid](#aa14c50b1e6a313daa690b016cdb7305c)。

时钟标识符，取 `SIWX91X_CLK_*`。

<a id="r_a5907249c723db10770838f2d2bb435fb"></a>

```c
uint32_t ref_clkid
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ref_clkid](#a5907249c723db10770838f2d2bb435fb)。

父时钟/参考时钟标识符。

<a id="r_a3376c611ad9f1450b340d5e2b764c641"></a>

```c
uint32_t clock_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clock_div](#a3376c611ad9f1450b340d5e2b764c641)。

多路复用器之后应用的可选分频器。

## 88.2\_详细说明（Detailed Documentation）

<a id="aa14c50b1e6a313daa690b016cdb7305c"></a>

### `clkid`

```c
uint32_t silabs_siwx91x_clock_control_config::clkid
```

时钟标识符，取 `SIWX91X_CLK_*`。

<a id="a3376c611ad9f1450b340d5e2b764c641"></a>

### `clock_div`

```c
uint32_t silabs_siwx91x_clock_control_config::clock_div
```

多路复用器之后应用的可选分频器。

<a id="a5907249c723db10770838f2d2bb435fb"></a>

### `ref_clkid`

```c
uint32_t silabs_siwx91x_clock_control_config::ref_clkid
```

父时钟/参考时钟标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_silabs_clock_control_cmu_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_silabs_siwx91x_clock_control_pll_config_结构体.md)
