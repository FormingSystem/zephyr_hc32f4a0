---
id: learning.zephyr-docs.api-file-supplement-reference.page-20
title: zephyr__drivers__audio__cs35l5x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs35l5x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_drivers\_\_audio\_\_cs35l5x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cs35l5x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供CS35L5X智能放大器（Smart Amplifier）API的头文件。

<a id="details"></a>

```c
#include <zephyr/audio/codec.h>
```

查看此文件的源码。

提供CS35L5X智能放大器（Smart Amplifier）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.1\_枚举（Enumerations）

<a id="r_gac504b102ed625a997eaf9ea7fe4ba726"></a>

```c
enum cs35l5x_channel_t { CS35L5X_CHANNEL_ASP1_TX1 = AUDIO_CHANNEL_PRIV_START , CS35L5X_CHANNEL_ASP1_TX2 , CS35L5X_CHANNEL_ASP1_TX3 , CS35L5X_CHANNEL_ASP1_TX4 }
```

相关声明：[cs35l5x_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#gac504b102ed625a997eaf9ea7fe4ba726)、[CS35L5X_CHANNEL_ASP1_TX1](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a1b4f60477f60a4e4a7876f021314125f)、[CS35L5X_CHANNEL_ASP1_TX2](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a5eb803f387d8d24d22ad655b5bde2bdd)、[CS35L5X_CHANNEL_ASP1_TX3](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a2aab2605fc245fe34be7c02dd1ae8ce3)、[CS35L5X_CHANNEL_ASP1_TX4](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a403a074eea1aeede5fb4148d50a254ae)。

用于 asp1 传输（Transmission）的自定义通道（Custom Channels）。


## 20.2\_原页交叉引用（Cross References）

- [zephyr/audio/codec.h](../api_source_supplement_reference/P032_codec.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P035_cs35l5x.h_源码浏览.md)
- [cs35l5x_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#gac504b102ed625a997eaf9ea7fe4ba726)
- [CS35L5X_CHANNEL_ASP1_TX1](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a1b4f60477f60a4e4a7876f021314125f)
- [CS35L5X_CHANNEL_ASP1_TX2](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a5eb803f387d8d24d22ad655b5bde2bdd)
- [CS35L5X_CHANNEL_ASP1_TX3](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a2aab2605fc245fe34be7c02dd1ae8ce3)
- [CS35L5X_CHANNEL_ASP1_TX4](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html#ggac504b102ed625a997eaf9ea7fe4ba726a403a074eea1aeede5fb4148d50a254ae)

<a id="header-details"></a>

---

[上一章](P019_zephyr__drivers__clock_control__clock_control_silabs_siwx91x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__dma__dma_esp32.h_文件参考.md)
