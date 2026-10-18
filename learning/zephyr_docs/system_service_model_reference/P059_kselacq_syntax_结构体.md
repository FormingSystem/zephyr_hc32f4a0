---
id: learning.zephyr-docs.system-service-model-reference.page-59
title: kselacq_syntax_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structkselacq__syntax.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_kselacq\_syntax\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structkselacq__syntax.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

KSELACQ无线接入技术（RAT）的配置语法。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

KSELACQ无线接入技术（RAT）的配置语法。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a96ce49c04407034f9f7b64bb28a1ab27"></a>

```c
bool mode
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[mode](#a96ce49c04407034f9f7b64bb28a1ab27)。

0 表示配置首选无线接入技术列表（Preferred RAT List，PRL）；1 为保留值。

<a id="r_ac62bc66e12deed5b1b7072f436d2cda8"></a>

```c
enum hl78xx_kselacq_rat rat1
```

相关声明：[hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)、[rat1](#ac62bc66e12deed5b1b7072f436d2cda8)。

PRL 位置 1 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

<a id="r_a0fe51e6bcae3f2195f62952a8022bda0"></a>

```c
enum hl78xx_kselacq_rat rat2
```

相关声明：[hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)、[rat2](#a0fe51e6bcae3f2195f62952a8022bda0)。

PRL 位置 2 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

<a id="r_a8c0973f97ef1cac8cf606e4420b2913b"></a>

```c
enum hl78xx_kselacq_rat rat3
```

相关声明：[hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)、[rat3](#a8c0973f97ef1cac8cf606e4420b2913b)。

PRL 位置 3 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

## 59.2\_详细说明（Detailed Documentation）

<a id="a96ce49c04407034f9f7b64bb28a1ab27"></a>

### `mode`

```c
bool kselacq_syntax::mode
```

0 表示配置首选无线接入技术列表（Preferred RAT List，PRL）；1 为保留值。

<a id="ac62bc66e12deed5b1b7072f436d2cda8"></a>

### `rat1`

```c
enum hl78xx_kselacq_rat kselacq_syntax::rat1
```

PRL 位置 1 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

<a id="a0fe51e6bcae3f2195f62952a8022bda0"></a>

### `rat2`

```c
enum hl78xx_kselacq_rat kselacq_syntax::rat2
```

PRL 位置 2 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

<a id="a8c0973f97ef1cac8cf606e4420b2913b"></a>

### `rat3`

```c
enum hl78xx_kselacq_rat kselacq_syntax::rat3
```

PRL 位置 3 的首选无线接入技术（RAT），以原始 `AT+KSELACQ` 值表示。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_k_cellmeas_signal_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_linear_range_结构体.md)
