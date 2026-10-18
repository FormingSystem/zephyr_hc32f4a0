---
id: learning.zephyr-docs.audio-video-model-reference.page-4
title: dai_ts_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdai__ts__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_dai\_ts\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdai__ts__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（DAI）的时间戳配置。

```c
#include <zephyr/drivers/dai.h>
```

<a id="details"></a>

数字音频接口（DAI）的时间戳配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_ac17d3da9de6d860f2fa04286a4c43a1d"></a>

```c
uint32_t walclk_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[walclk_rate](#ac17d3da9de6d860f2fa04286a4c43a1d)。

频率，单位为 Hz，例如下列数值。

<a id="r_a2b0be9c840de941e4a87c422fa82356d"></a>

```c
int type
```

相关声明：[type](#a2b0be9c840de941e4a87c422fa82356d)。

DAI 的类型，例如同步串行端口（SSP）、数字麦克风（DMIC）或高清音频（HDA）等。

<a id="r_afdaf1a4ef6a00201b3790187ec44370f"></a>

```c
int direction
```

相关声明：[direction](#afdaf1a4ef6a00201b3790187ec44370f)。

方向：播放或采集（playback/capture）。

<a id="r_aff3dc52737d1261cd56c084c104691eb"></a>

```c
int index
```

相关声明：[index](#aff3dc52737d1261cd56c084c104691eb)。

用于选择正确时间戳寄存器的 SSPx 索引。

<a id="r_ab874249dcb9377fafa35764b4f1c0ea0"></a>

```c
int dma_id
```

相关声明：[dma_id](#ab874249dcb9377fafa35764b4f1c0ea0)。

DMA 实例 ID。

<a id="r_aa87fc1e3072490e44f65bc7690f85ce8"></a>

```c
int dma_chan_index
```

相关声明：[dma_chan_index](#aa87fc1e3072490e44f65bc7690f85ce8)。

所使用 DMA 通道的索引。

<a id="r_a37c6379686435994b9050d1e9c249756"></a>

```c
int dma_chan_count
```

相关声明：[dma_chan_count](#a37c6379686435994b9050d1e9c249756)。

单个 DMA 中的通道数。

## 4.2\_详细说明（Detailed Documentation）

<a id="afdaf1a4ef6a00201b3790187ec44370f"></a>

### `direction`

```c
int dai_ts_cfg::direction
```

方向：播放或采集（playback/capture）。

<a id="a37c6379686435994b9050d1e9c249756"></a>

### `dma_chan_count`

```c
int dai_ts_cfg::dma_chan_count
```

单个 DMA 中的通道数。

<a id="aa87fc1e3072490e44f65bc7690f85ce8"></a>

### `dma_chan_index`

```c
int dai_ts_cfg::dma_chan_index
```

所使用 DMA 通道的索引。

<a id="ab874249dcb9377fafa35764b4f1c0ea0"></a>

### `dma_id`

```c
int dai_ts_cfg::dma_id
```

DMA 实例 ID。

<a id="aff3dc52737d1261cd56c084c104691eb"></a>

### `index`

```c
int dai_ts_cfg::index
```

用于选择正确时间戳寄存器的 SSPx 索引。

<a id="a2b0be9c840de941e4a87c422fa82356d"></a>

### `type`

```c
int dai_ts_cfg::type
```

DAI 的类型，例如同步串行端口（SSP）、数字麦克风（DMIC）或高清音频（HDA）等。

<a id="ac17d3da9de6d860f2fa04286a4c43a1d"></a>

### `walclk_rate`

```c
uint32_t dai_ts_cfg::walclk_rate
```

频率，单位为 Hz，例如下列数值。

`19200000`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dai.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dai.h](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_dai_properties_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_dai_ts_data_结构体.md)
