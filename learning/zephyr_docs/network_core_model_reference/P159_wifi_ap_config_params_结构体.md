---
id: learning.zephyr-docs.network-core-model-reference.page-159
title: wifi_ap_config_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ap__config__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第159章\_wifi\_ap\_config\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ap__config__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi接入点（AP）的配置参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi接入点（AP）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 159.1\_数据成员（Data Fields）

<a id="r_a4c391cf504a994ed0bc4971afdf76774"></a>

```c
enum wifi_ap_config_param type
```

相关声明：[wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)、[type](#a4c391cf504a994ed0bc4971afdf76774)。

用于标识不同接入点参数（AP parameters）的参数。

<a id="r_a289866d9209450e893281b4c198a546a"></a>

```c
uint32_t max_inactivity
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_inactivity](#a289866d9209450e893281b4c198a546a)。

用于设置站点最大非活动持续时间（Maximum inactivity duration for stations）的参数。

<a id="r_a7fc0fad99f53ed8e1ac40b74ec98bf9a"></a>

```c
uint32_t max_num_sta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_num_sta](#a7fc0fad99f53ed8e1ac40b74ec98bf9a)。

用于设置最大站点数（Maximum number of stations）的参数。

<a id="r_aba4e43dff01fa026c8dbbfff670d3097"></a>

```c
enum wifi_frequency_bandwidths bandwidth
```

相关声明：[wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)、[bandwidth](#aba4e43dff01fa026c8dbbfff670d3097)。

用于指定频段（Frequency band）的参数。

## 159.2\_详细说明（Detailed Documentation）

<a id="aba4e43dff01fa026c8dbbfff670d3097"></a>

### `bandwidth`

```c
enum wifi_frequency_bandwidths wifi_ap_config_params::bandwidth
```

用于指定频段（Frequency band）的参数。

<a id="a289866d9209450e893281b4c198a546a"></a>

### `max_inactivity`

```c
uint32_t wifi_ap_config_params::max_inactivity
```

用于设置站点最大非活动持续时间（Maximum inactivity duration for stations）的参数。

<a id="a7fc0fad99f53ed8e1ac40b74ec98bf9a"></a>

### `max_num_sta`

```c
uint32_t wifi_ap_config_params::max_num_sta
```

用于设置最大站点数（Maximum number of stations）的参数。

<a id="a4c391cf504a994ed0bc4971afdf76774"></a>

### `type`

```c
enum wifi_ap_config_param wifi_ap_config_params::type
```

用于标识不同接入点参数（AP parameters）的参数。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 159.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P158_wifi_11k_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P160_wifi_ap_sta_info_结构体.md)
