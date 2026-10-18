---
id: learning.zephyr-docs.api-service-topic-reference.page-8
title: CS35L5X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_CS35L5X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CS35L5X 智能放大器（Smart amplifier）。

<a id="details"></a>

CS35L5X 智能放大器（Smart amplifier）。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_cs35l5x_2Eh"></a>

```c
file cs35l5x.h
```

相关声明：[cs35l5x.h](../api_file_supplement_reference/P020_zephyr__drivers__audio__cs35l5x.h_文件参考.md)。

提供CS35L5X智能放大器（Smart Amplifier）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.2\_枚举（Enumerations）

<a id="r_gac504b102ed625a997eaf9ea7fe4ba726"></a>

```c
enum cs35l5x_channel_t { CS35L5X_CHANNEL_ASP1_TX1 = AUDIO_CHANNEL_PRIV_START , CS35L5X_CHANNEL_ASP1_TX2 , CS35L5X_CHANNEL_ASP1_TX3 , CS35L5X_CHANNEL_ASP1_TX4 }
```

相关声明：[cs35l5x_channel_t](#gac504b102ed625a997eaf9ea7fe4ba726)、[CS35L5X_CHANNEL_ASP1_TX1](#ggac504b102ed625a997eaf9ea7fe4ba726a1b4f60477f60a4e4a7876f021314125f)、[CS35L5X_CHANNEL_ASP1_TX2](#ggac504b102ed625a997eaf9ea7fe4ba726a5eb803f387d8d24d22ad655b5bde2bdd)、[CS35L5X_CHANNEL_ASP1_TX3](#ggac504b102ed625a997eaf9ea7fe4ba726a2aab2605fc245fe34be7c02dd1ae8ce3)、[CS35L5X_CHANNEL_ASP1_TX4](#ggac504b102ed625a997eaf9ea7fe4ba726a403a074eea1aeede5fb4148d50a254ae)。

用于 asp1 传输（Transmission）的自定义通道（Custom Channels）。

## 8.3\_详细说明（Detailed Documentation）

<a id="gac504b102ed625a997eaf9ea7fe4ba726"></a>

### `cs35l5x_channel_t`

```c
enum cs35l5x_channel_t
```

```c
#include <zephyr/drivers/audio/cs35l5x.h>
```

用于 asp1 传输（Transmission）的自定义通道（Custom Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CS35L5X_CHANNEL_ASP1_TX1` | ASP1 TX1 通道索引（Channel Index）。 |
| `CS35L5X_CHANNEL_ASP1_TX2` | ASP1 TX2 通道索引（Channel Index）。 |
| `CS35L5X_CHANNEL_ASP1_TX3` | ASP1 TX3 通道索引（Channel Index）。 |
| `CS35L5X_CHANNEL_ASP1_TX4` | ASP1 TX4 通道索引（Channel Index）。 |


## 8.4\_原页交叉引用（Cross References）

- [cs35l5x.h](../api_file_supplement_reference/P020_zephyr__drivers__audio__cs35l5x.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac504b102ed625a997eaf9ea7fe4ba726a1b4f60477f60a4e4a7876f021314125f"></a>
<a id="ggac504b102ed625a997eaf9ea7fe4ba726a5eb803f387d8d24d22ad655b5bde2bdd"></a>
<a id="ggac504b102ed625a997eaf9ea7fe4ba726a2aab2605fc245fe34be7c02dd1ae8ce3"></a>
<a id="ggac504b102ed625a997eaf9ea7fe4ba726a403a074eea1aeede5fb4148d50a254ae"></a>

---

[上一章](P007_CoAP 管理器事件（CoAP Manager Events）.md) · [返回大纲](大纲.md) · [下一章](P009_以太网库（Ethernet Library）.md)
