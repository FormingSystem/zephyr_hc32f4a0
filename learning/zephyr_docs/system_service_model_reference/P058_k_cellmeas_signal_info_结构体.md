---
id: learning.zephyr-docs.system-service-model-reference.page-58
title: k_cellmeas_signal_info_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__cellmeas__signal__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_k\_cellmeas\_signal\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__cellmeas__signal__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝通信测量信号信息（Cellular Measurement Signal Information）。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

蜂窝测量信号信息（Cellular measurement signal information）。保存调制解调器在小区测量过程中报告的接收信号功率值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_aedf20f274705729bd3c3b5246baec391"></a>

```c
int16_t rsrp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rsrp](#aedf20f274705729bd3c3b5246baec391)。

参考信号接收功率（Reference Signal Received Power，RSRP），单位为 dBm。

## 58.2\_详细说明（Detailed Documentation）

<a id="aedf20f274705729bd3c3b5246baec391"></a>

### `rsrp`

```c
int16_t k_cellmeas_signal_info::rsrp
```

参考信号接收功率（Reference Signal Received Power，RSRP），单位为 dBm。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_input_touchscreen_common_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_kselacq_syntax_结构体.md)
