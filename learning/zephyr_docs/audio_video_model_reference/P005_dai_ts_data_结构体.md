---
id: learning.zephyr-docs.audio-video-model-reference.page-5
title: dai_ts_data_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdai__ts__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_dai\_ts\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdai__ts__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（DAI）的时间戳数据。

```c
#include <zephyr/drivers/dai.h>
```

<a id="details"></a>

数字音频接口（DAI）的时间戳数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a11133d72485786e75a9d94f218fe699b"></a>

```c
uint64_t walclk
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[walclk](#a11133d72485786e75a9d94f218fe699b)。

墙钟（Wall clock）。

<a id="r_a933cbc19cc837683581db806702fba36"></a>

```c
uint64_t sample
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[sample](#a933cbc19cc837683581db806702fba36)。

采样计数（Sample count）。

<a id="r_ace2686aa6ff5aed346705cbb0d198d36"></a>

```c
uint32_t walclk_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[walclk_rate](#ace2686aa6ff5aed346705cbb0d198d36)。

频率，单位为 Hz，例如下列数值。

## 5.2\_详细说明（Detailed Documentation）

<a id="a933cbc19cc837683581db806702fba36"></a>

### `sample`

```c
uint64_t dai_ts_data::sample
```

采样计数（Sample count）。

<a id="a11133d72485786e75a9d94f218fe699b"></a>

### `walclk`

```c
uint64_t dai_ts_data::walclk
```

墙钟（Wall clock）。

<a id="ace2686aa6ff5aed346705cbb0d198d36"></a>

### `walclk_rate`

```c
uint32_t dai_ts_data::walclk_rate
```

频率，单位为 Hz，例如下列数值。

`19200000`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dai.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dai.h](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_dai_ts_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_dmic_cfg_结构体.md)
