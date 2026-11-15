---
id: learning.zephyr-docs.network-core-model-reference.page-190
title: wifi_version_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__version.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第190章\_wifi\_version\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__version.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi版本（Version）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi版本（Version）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 190.1\_数据成员（Data Fields）

<a id="r_aea828bdb512440d6aa3cc853525c4971"></a>

```c
const char * drv_version
```

相关声明：[drv_version](#aea828bdb512440d6aa3cc853525c4971)。

驱动版本（Driver version）。

<a id="r_a4bf2cbdf5c43ff21718ccf19646c164e"></a>

```c
const char * fw_version
```

相关声明：[fw_version](#a4bf2cbdf5c43ff21718ccf19646c164e)。

固件版本（Firmware Version）。

## 190.2\_详细说明（Detailed Documentation）

<a id="aea828bdb512440d6aa3cc853525c4971"></a>

### `drv_version`

```c
const char* wifi_version::drv_version
```

驱动版本（Driver version）。

<a id="a4bf2cbdf5c43ff21718ccf19646c164e"></a>

### `fw_version`

```c
const char* wifi_version::fw_version
```

固件版本（Firmware Version）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 190.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P189_wifi_twt_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P191_wifi_wps_config_params_结构体.md)
