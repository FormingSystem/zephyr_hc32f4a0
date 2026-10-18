---
id: learning.zephyr-docs.network-core-model-reference.page-186
title: wifi_scan_result_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__scan__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_wifi\_scan\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__scan__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi扫描结果（Scan Result）；每个结果通过net_mgmt_event_callback的info属性提供，见net_mgmt.h。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi扫描结果（Scan Result）；每个结果通过net_mgmt_event_callback的info属性提供，见net_mgmt.h。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 186.1\_数据成员（Data Fields）

<a id="r_aaefb8f5c9510e4f5002ae306d853ade8"></a>

```c
uint8_t ssid [WIFI_SSID_MAX_LEN+1]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid](#aaefb8f5c9510e4f5002ae306d853ade8)、[WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)。

服务集标识符（SSID）。

<a id="r_a2c1c2f4265b914df08fc75deb8b69d39"></a>

```c
uint8_t ssid_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid_length](#a2c1c2f4265b914df08fc75deb8b69d39)。

服务集标识符长度（SSID length）。

<a id="r_a38201c9dd798dc11b5bda3ce97b02e92"></a>

```c
uint8_t band
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[band](#a38201c9dd798dc11b5bda3ce97b02e92)。

频段（Frequency band）。

<a id="r_adbbfd7692ee5ffd6344fe78b9d91c840"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#adbbfd7692ee5ffd6344fe78b9d91c840)。

信道（Channel）。

<a id="r_af2d3dc5d115e3db76d3bc115510b0a5a"></a>

```c
enum wifi_security_type security
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[security](#af2d3dc5d115e3db76d3bc115510b0a5a)。

安全类型（Security type）。

<a id="r_abb7de47c605ec05c8fe0a06ecbd2b7b6"></a>

```c
enum wifi_wpa3_enterprise_type wpa3_ent_type
```

相关声明：[wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)、[wpa3_ent_type](#abb7de47c605ec05c8fe0a06ecbd2b7b6)。

WPA3 企业类型（WPA3 enterprise type）。

<a id="r_acaa3fb30ebf6df22bfac6380698ed28e"></a>

```c
enum wifi_mfp_options mfp
```

相关声明：[wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)、[mfp](#acaa3fb30ebf6df22bfac6380698ed28e)。

管理帧保护选项（MFP options）。

<a id="r_a76aa012136e3721fd4a482a22b93546f"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a76aa012136e3721fd4a482a22b93546f)。

接收信号强度指示（RSSI）。

<a id="r_a4fdbc4dc4d5c8b279223e8c06624f434"></a>

```c
uint8_t mac [WIFI_MAC_ADDR_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mac](#a4fdbc4dc4d5c8b279223e8c06624f434)、[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

基本服务集标识符（BSSID）。

<a id="r_a8fca0dabec00ebd7ed4800098ec9d451"></a>

```c
uint8_t mac_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mac_length](#a8fca0dabec00ebd7ed4800098ec9d451)。

基本服务集标识符长度（BSSID length）。

## 186.2\_详细说明（Detailed Documentation）

<a id="a38201c9dd798dc11b5bda3ce97b02e92"></a>

### `band`

```c
uint8_t wifi_scan_result::band
```

频段（Frequency band）。

<a id="adbbfd7692ee5ffd6344fe78b9d91c840"></a>

### `channel`

```c
uint8_t wifi_scan_result::channel
```

信道（Channel）。

<a id="a4fdbc4dc4d5c8b279223e8c06624f434"></a>

### `mac`

```c
uint8_t wifi_scan_result::mac[WIFI_MAC_ADDR_LEN]
```

基本服务集标识符（BSSID）。

<a id="a8fca0dabec00ebd7ed4800098ec9d451"></a>

### `mac_length`

```c
uint8_t wifi_scan_result::mac_length
```

基本服务集标识符长度（BSSID length）。

<a id="acaa3fb30ebf6df22bfac6380698ed28e"></a>

### `mfp`

```c
enum wifi_mfp_options wifi_scan_result::mfp
```

管理帧保护选项（MFP options）。

<a id="a76aa012136e3721fd4a482a22b93546f"></a>

### `rssi`

```c
int8_t wifi_scan_result::rssi
```

接收信号强度指示（RSSI）。

<a id="af2d3dc5d115e3db76d3bc115510b0a5a"></a>

### `security`

```c
enum wifi_security_type wifi_scan_result::security
```

安全类型（Security type）。

<a id="aaefb8f5c9510e4f5002ae306d853ade8"></a>

### `ssid`

```c
uint8_t wifi_scan_result::ssid[WIFI_SSID_MAX_LEN+1]
```

服务集标识符（SSID）。

<a id="a2c1c2f4265b914df08fc75deb8b69d39"></a>

### `ssid_length`

```c
uint8_t wifi_scan_result::ssid_length
```

服务集标识符长度（SSID length）。

<a id="abb7de47c605ec05c8fe0a06ecbd2b7b6"></a>

### `wpa3_ent_type`

```c
enum wifi_wpa3_enterprise_type wifi_scan_result::wpa3_ent_type
```

WPA3 企业类型（WPA3 enterprise type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 186.3\_原页交叉引用（Cross References）

- [net_mgmt_event_callback](P110_net_mgmt_event_callback_结构体.md)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P185_wifi_scan_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P187_wifi_status_结构体.md)
