---
id: learning.zephyr-docs.network-core-model-reference.page-158
title: wifi_11k_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__11k__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_wifi\_11k\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__11k__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi 802.11k参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi 802.11k参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 158.1\_数据成员（Data Fields）

<a id="r_ae6029ed4bada41f18df0329d0da7401e"></a>

```c
enum wifi_mgmt_op oper
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[oper](#ae6029ed4bada41f18df0329d0da7401e)。

802.11k 命令操作（11k command operation）。

<a id="r_a739c3e94b025aae2fcf5680aecf3d646"></a>

```c
bool enable_11k
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_11k](#a739c3e94b025aae2fcf5680aecf3d646)。

启用／禁用 802.11k（11k enable/disable）。

<a id="r_a64ace23c71837417678ceb9cc8d5f216"></a>

```c
uint8_t ssid [WIFI_SSID_MAX_LEN+1]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid](#a64ace23c71837417678ceb9cc8d5f216)、[WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)。

服务集标识符（SSID）。

## 158.2\_详细说明（Detailed Documentation）

<a id="a739c3e94b025aae2fcf5680aecf3d646"></a>

### `enable_11k`

```c
bool wifi_11k_params::enable_11k
```

启用／禁用 802.11k（11k enable/disable）。

<a id="ae6029ed4bada41f18df0329d0da7401e"></a>

### `oper`

```c
enum wifi_mgmt_op wifi_11k_params::oper
```

802.11k 命令操作（11k command operation）。

<a id="a64ace23c71837417678ceb9cc8d5f216"></a>

### `ssid`

```c
uint8_t wifi_11k_params::ssid[WIFI_SSID_MAX_LEN+1]
```

服务集标识符（SSID）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 158.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P157_net_wifi_mgmt_offload_结构体.md) · [返回大纲](大纲.md) · [下一章](P159_wifi_ap_config_params_结构体.md)
