---
id: learning.zephyr-docs.modem-wireless-model-reference.page-40
title: mdm_hl7800_site_survey_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__site__survey.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_mdm\_hl7800\_site\_survey\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__site__survey.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

现场勘测结果（Site Survey Result）。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

现场勘测结果（Site Survey Result）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_aa22e2191ac864718a097fa674dc1adc8"></a>

```c
uint32_t earfcn
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[earfcn](#aa22e2191ac864718a097fa674dc1adc8)。

演进型通用陆地无线接入绝对射频信道号（EUTRA Absolute Radio Frequency Channel Number）。

<a id="r_a9e8ec0ba55bc7686e0b4b093d9057179"></a>

```c
uint32_t cell_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cell_id](#a9e8ec0ba55bc7686e0b4b093d9057179)。

小区标识（Cell identity）。

<a id="r_a725a5a647c999bbae2da828eaee481cf"></a>

```c
int rsrp
```

相关声明：[rsrp](#a725a5a647c999bbae2da828eaee481cf)。

参考信号接收功率（Reference Signal Received Power，RSRP）。

<a id="r_a4517603844797cc6e46d96b1773c78c7"></a>

```c
int rsrq
```

相关声明：[rsrq](#a4517603844797cc6e46d96b1773c78c7)。

参考信号接收质量（Reference Signal Received Quality，RSRQ）。

## 40.2\_详细说明（Detailed Documentation）

<a id="a9e8ec0ba55bc7686e0b4b093d9057179"></a>

### `cell_id`

```c
uint32_t mdm_hl7800_site_survey::cell_id
```

小区标识（Cell identity）。

<a id="aa22e2191ac864718a097fa674dc1adc8"></a>

### `earfcn`

```c
uint32_t mdm_hl7800_site_survey::earfcn
```

演进型通用陆地无线接入绝对射频信道号（EUTRA Absolute Radio Frequency Channel Number）。

<a id="a725a5a647c999bbae2da828eaee481cf"></a>

### `rsrp`

```c
int mdm_hl7800_site_survey::rsrp
```

参考信号接收功率（Reference Signal Received Power，RSRP）。

<a id="a4517603844797cc6e46d96b1773c78c7"></a>

### `rsrq`

```c
int mdm_hl7800_site_survey::rsrq
```

参考信号接收质量（Reference Signal Received Quality，RSRQ）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_mdm_hl7800_polte_registration_event_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_modem_backend_tty_结构体.md)
