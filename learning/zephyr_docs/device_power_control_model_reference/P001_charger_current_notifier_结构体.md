---
id: learning.zephyr-docs.device-power-control-model-reference.page-1
title: charger_current_notifier_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcharger__current__notifier.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_charger\_current\_notifier\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcharger__current__notifier.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

充电器（Charger）通知系统所用的输入电流阈值。

```c
#include <zephyr/drivers/charger.h>
```

<a id="details"></a>

充电器（Charger）通知系统所用的输入电流阈值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a22c26477263e5abedb200de36a29d9de"></a>

```c
uint8_t severity
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[severity](#a22c26477263e5abedb200de36a29d9de)。

通知的严重程度（Severity），其中 `CHARGER_SEVERITY_PEAK` 最严重。

<a id="r_acb54706bf47f55e197e799393b9eb87e"></a>

```c
uint32_t current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[current_ua](#acb54706bf47f55e197e799393b9eb87e)。

需要超过的电流阈值（Current threshold）。

<a id="r_a4998999ef893d18fa64b86ec4fd9ad94"></a>

```c
uint32_t duration_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[duration_us](#a4998999ef893d18fa64b86ec4fd9ad94)。

超额电流持续多长时间后通知系统。

## 1.2\_详细说明（Detailed Documentation）

<a id="acb54706bf47f55e197e799393b9eb87e"></a>

### `current_ua`

```c
uint32_t charger_current_notifier::current_ua
```

需要超过的电流阈值（Current threshold）。

<a id="a4998999ef893d18fa64b86ec4fd9ad94"></a>

### `duration_us`

```c
uint32_t charger_current_notifier::duration_us
```

超额电流持续多长时间后通知系统。

<a id="a22c26477263e5abedb200de36a29d9de"></a>

### `severity`

```c
uint8_t charger_current_notifier::severity
```

通知的严重程度（Severity），其中 `CHARGER_SEVERITY_PEAK` 最严重。

本数据类型文档由以下文件生成：

- `zephyr/drivers/charger.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_charger_driver_api_结构体.md)
