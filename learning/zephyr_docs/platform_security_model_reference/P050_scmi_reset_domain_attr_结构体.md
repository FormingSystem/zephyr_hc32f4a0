---
id: learning.zephyr-docs.platform-security-model-reference.page-50
title: scmi_reset_domain_attr_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__reset__domain__attr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_scmi\_reset\_domain\_attr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__reset__domain__attr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的复位域（Reset Domain）属性。

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）的复位域（Reset Domain）属性。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a47e672531778348a1da1b835374a7b1b"></a>

```c
uint32_t latency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[latency](#a47e672531778348a1da1b835374a7b1b)。

复位生效所需的最长时间，单位为微秒。

<a id="r_a23258ab925ea86f304d49fdb5c562fd3"></a>

```c
char name [16]
```

相关声明：[name](#a23258ab925ea86f304d49fdb5c562fd3)。

复位域名称（Reset domain name）。

<a id="r_a5f130ce02cc05af0caa6abbdb9affea4"></a>

```c
bool is_async_sup:1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_async_sup](#a5f130ce02cc05af0caa6abbdb9affea4)。

是否支持异步复位（Asynchronous reset）。

<a id="r_a5a64c890789e2e9fb273cca050e24ade"></a>

```c
bool is_notifications_sup:1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_notifications_sup](#a5a64c890789e2e9fb273cca050e24ade)。

是否支持复位通知（Reset notifications）。

<a id="r_a8b8d31eba1f64f0f5cef64dea229848d"></a>

```c
bool is_latency_valid:1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_latency_valid](#a8b8d31eba1f64f0f5cef64dea229848d)。

复位延迟值是否有效。

## 50.2\_详细说明（Detailed Documentation）

<a id="a5f130ce02cc05af0caa6abbdb9affea4"></a>

### `is_async_sup`

```c
bool scmi_reset_domain_attr::is_async_sup
```

是否支持异步复位（Asynchronous reset）。

<a id="a8b8d31eba1f64f0f5cef64dea229848d"></a>

### `is_latency_valid`

```c
bool scmi_reset_domain_attr::is_latency_valid
```

复位延迟值是否有效。

<a id="a5a64c890789e2e9fb273cca050e24ade"></a>

### `is_notifications_sup`

```c
bool scmi_reset_domain_attr::is_notifications_sup
```

是否支持复位通知（Reset notifications）。

<a id="a47e672531778348a1da1b835374a7b1b"></a>

### `latency`

```c
uint32_t scmi_reset_domain_attr::latency
```

复位生效所需的最长时间，单位为微秒。

<a id="a23258ab925ea86f304d49fdb5c562fd3"></a>

### `name`

```c
char scmi_reset_domain_attr::name[16]
```

复位域名称（Reset domain name）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/reset.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/reset.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_scmi_protocol_version_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_scmi_system_power_state_config_结构体.md)
