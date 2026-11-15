---
id: learning.zephyr-docs.network-core-model-reference.page-191
title: wifi_wps_config_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__wps__config__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_wifi\_wps\_config\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__wps__config__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi保护设置（WPS）的配置。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi保护设置（WPS）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 191.1\_数据成员（Data Fields）

<a id="r_aa7a10889c5cd5124983b0f7242d23b7e"></a>

```c
enum wifi_wps_op oper
```

相关声明：[wifi_wps_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c36ae1a5171d3fbaeebf95c16be496d)、[oper](#aa7a10889c5cd5124983b0f7242d23b7e)。

Wi‑Fi 保护设置操作（WPS operation）。

<a id="r_a962bd6513c564150e0c75112b96bbe15"></a>

```c
char pin [8+1]
```

相关声明：[pin](#a962bd6513c564150e0c75112b96bbe15)。

个人识别码值（PIN value）。

## 191.2\_详细说明（Detailed Documentation）

<a id="aa7a10889c5cd5124983b0f7242d23b7e"></a>

### `oper`

```c
enum wifi_wps_op wifi_wps_config_params::oper
```

Wi‑Fi 保护设置操作（WPS operation）。

<a id="a962bd6513c564150e0c75112b96bbe15"></a>

### `pin`

```c
char wifi_wps_config_params::pin[8+1]
```

个人识别码值（PIN value）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 191.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_wps_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c36ae1a5171d3fbaeebf95c16be496d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P190_wifi_version_结构体.md) · [返回大纲](大纲.md)
