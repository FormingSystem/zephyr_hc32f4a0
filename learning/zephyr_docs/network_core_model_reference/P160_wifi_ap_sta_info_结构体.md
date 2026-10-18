---
id: learning.zephyr-docs.network-core-model-reference.page-160
title: wifi_ap_sta_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ap__sta__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第160章\_wifi\_ap\_sta\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ap__sta__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接入点（AP）模式：已连接站点（STA）的详情。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

接入点（AP）模式：已连接站点（STA）的详情。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 160.1\_数据成员（Data Fields）

<a id="r_a7d8bd52340d4937a4b5b7d2c00662441"></a>

```c
enum wifi_link_mode link_mode
```

相关声明：[wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)、[link_mode](#a7d8bd52340d4937a4b5b7d2c00662441)。

链路模式（Link mode），参见枚举 `wifi_link_mode`。

<a id="r_a7db904376ec73b774aa9d8236c15b3f6"></a>

```c
uint8_t mac [WIFI_MAC_ADDR_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mac](#a7db904376ec73b774aa9d8236c15b3f6)、[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

介质访问控制地址（MAC address）。

<a id="r_a7f7c8b144bb3464af5213708591eefda"></a>

```c
uint8_t mac_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mac_length](#a7f7c8b144bb3464af5213708591eefda)。

MAC 地址长度（MAC address length）。

<a id="r_a838c9a4288c9bc7e97afe2334c678f34"></a>

```c
bool twt_capable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[twt_capable](#a838c9a4288c9bc7e97afe2334c678f34)。

是否支持目标唤醒时间（Target Wake Time，TWT）。

## 160.2\_详细说明（Detailed Documentation）

<a id="a7d8bd52340d4937a4b5b7d2c00662441"></a>

### `link_mode`

```c
enum wifi_link_mode wifi_ap_sta_info::link_mode
```

链路模式（Link mode），参见枚举 `wifi_link_mode`。

<a id="a7db904376ec73b774aa9d8236c15b3f6"></a>

### `mac`

```c
uint8_t wifi_ap_sta_info::mac[WIFI_MAC_ADDR_LEN]
```

介质访问控制地址（MAC address）。

<a id="a7f7c8b144bb3464af5213708591eefda"></a>

### `mac_length`

```c
uint8_t wifi_ap_sta_info::mac_length
```

MAC 地址长度（MAC address length）。

<a id="a838c9a4288c9bc7e97afe2334c678f34"></a>

### `twt_capable`

```c
bool wifi_ap_sta_info::twt_capable
```

是否支持目标唤醒时间（Target Wake Time，TWT）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 160.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P159_wifi_ap_config_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P161_wifi_band_channel_结构体.md)
