---
id: learning.zephyr-docs.audio-video-model-reference.page-44
title: pdm_io_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpdm__io__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_pdm\_io\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpdm__io__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

脉冲密度调制（PDM）的输入输出信号配置。

```c
#include <zephyr/audio/dmic.h>
```

<a id="details"></a>

脉冲密度调制（PDM）的输入输出信号配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="pub-attribs-0"></a>

### 所有 PDM 控制器共有的参数（Parameters common to all PDM controllers）

<a id="r_ae308635d30eaee617cb62c03c0255f37"></a>

```c
uint32_t min_pdm_clk_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_pdm_clk_freq](#ae308635d30eaee617cb62c03c0255f37)。

麦克风支持的最低时钟频率。

<a id="r_a4f07b2239435b0ac21e1049413d1a03a"></a>

```c
uint32_t max_pdm_clk_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_pdm_clk_freq](#a4f07b2239435b0ac21e1049413d1a03a)。

麦克风支持的最高时钟频率。

<a id="r_a14d6d390746f7731c4ff203a4beec5fe"></a>

```c
uint8_t min_pdm_clk_dc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_pdm_clk_dc](#a14d6d390746f7731c4ff203a4beec5fe)。

麦克风支持的最小占空比（duty cycle），单位为百分比。

<a id="r_aa03fbcc1f17fb2597bfa8c1898b74455"></a>

```c
uint8_t max_pdm_clk_dc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_pdm_clk_dc](#aa03fbcc1f17fb2597bfa8c1898b74455)。

麦克风支持的最大占空比（duty cycle），单位为百分比。

<a id="pub-attribs-1"></a>

### 每个 PDM 控制器各自的参数（Parameters unique to each PDM controller）

<a id="r_a4a12d293f2c8edae3e7e5b71646ee55e"></a>

```c
uint8_t pdm_clk_pol
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_clk_pol](#a4a12d293f2c8edae3e7e5b71646ee55e)。

用于选择是否反转 PDM 时钟的位掩码。

<a id="r_aa242b3383b20e0673ed47eea8450e9a7"></a>

```c
uint8_t pdm_data_pol
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_data_pol](#aa242b3383b20e0673ed47eea8450e9a7)。

用于选择是否反转麦克风数据的位掩码。

<a id="r_a692d7e838db86ca84558eb3e3170551a"></a>

```c
uint32_t pdm_clk_skew
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pdm_clk_skew](#a692d7e838db86ca84558eb3e3170551a)。

各 PDM 端口的时钟偏斜（clock skew）值集合。

## 44.2\_详细说明（Detailed Documentation）

<a id="aa03fbcc1f17fb2597bfa8c1898b74455"></a>

### `max_pdm_clk_dc`

```c
uint8_t pdm_io_cfg::max_pdm_clk_dc
```

麦克风支持的最大占空比（duty cycle），单位为百分比。

<a id="a4f07b2239435b0ac21e1049413d1a03a"></a>

### `max_pdm_clk_freq`

```c
uint32_t pdm_io_cfg::max_pdm_clk_freq
```

麦克风支持的最高时钟频率。

<a id="a14d6d390746f7731c4ff203a4beec5fe"></a>

### `min_pdm_clk_dc`

```c
uint8_t pdm_io_cfg::min_pdm_clk_dc
```

麦克风支持的最小占空比（duty cycle），单位为百分比。

<a id="ae308635d30eaee617cb62c03c0255f37"></a>

### `min_pdm_clk_freq`

```c
uint32_t pdm_io_cfg::min_pdm_clk_freq
```

麦克风支持的最低时钟频率。

<a id="a4a12d293f2c8edae3e7e5b71646ee55e"></a>

### `pdm_clk_pol`

```c
uint8_t pdm_io_cfg::pdm_clk_pol
```

用于选择是否反转 PDM 时钟的位掩码。

<a id="a692d7e838db86ca84558eb3e3170551a"></a>

### `pdm_clk_skew`

```c
uint32_t pdm_io_cfg::pdm_clk_skew
```

各 PDM 端口的时钟偏斜（clock skew）值集合。

<a id="aa242b3383b20e0673ed47eea8450e9a7"></a>

### `pdm_data_pol`

```c
uint8_t pdm_io_cfg::pdm_data_pol
```

用于选择是否反转麦克风数据的位掩码。

本数据类型文档由以下文件生成：

- `zephyr/audio/dmic.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_pdm_chan_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_sbc_decoder_结构体.md)
