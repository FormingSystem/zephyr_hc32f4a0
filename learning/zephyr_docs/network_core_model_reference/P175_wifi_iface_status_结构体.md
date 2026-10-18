---
id: learning.zephyr-docs.network-core-model-reference.page-175
title: wifi_iface_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__iface__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第175章\_wifi\_iface\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__iface__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi接口状态（Interface Status）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi接口状态（Interface Status）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 175.1\_数据成员（Data Fields）

<a id="r_ac52806155be3d64954ac6d109e76ec57"></a>

```c
int state
```

相关声明：[state](#ac52806155be3d64954ac6d109e76ec57)。

接口状态（Interface state），参见枚举 `wifi_iface_state`。

<a id="r_ad82f281941e4f6ce1ef0bca008e26d41"></a>

```c
unsigned int ssid_len
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[ssid_len](#ad82f281941e4f6ce1ef0bca008e26d41)。

服务集标识符长度（SSID length）。

<a id="r_a3ab671471bcdfeb5b955d156d39f2bb3"></a>

```c
char ssid [WIFI_SSID_MAX_LEN+1]
```

相关声明：[ssid](#a3ab671471bcdfeb5b955d156d39f2bb3)、[WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)。

服务集标识符（SSID）。

<a id="r_a5d5d19056a1a15365fbdd94274a0fc5e"></a>

```c
char bssid [WIFI_MAC_ADDR_LEN]
```

相关声明：[bssid](#a5d5d19056a1a15365fbdd94274a0fc5e)、[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

基本服务集标识符（BSSID）。

<a id="r_ae1c141a18f4e225af2c22a8cb4f882a8"></a>

```c
enum wifi_frequency_bands band
```

相关声明：[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)、[band](#ae1c141a18f4e225af2c22a8cb4f882a8)。

频段（Frequency band）。

<a id="r_a6432663156e5b2c424d254ed1eae0144"></a>

```c
unsigned int channel
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[channel](#a6432663156e5b2c424d254ed1eae0144)。

信道（Channel）。

<a id="r_ad33d2ec149a8d556e2472dd842ceadc0"></a>

```c
enum wifi_iface_mode iface_mode
```

相关声明：[wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)、[iface_mode](#ad33d2ec149a8d556e2472dd842ceadc0)。

接口模式（Interface mode），参见枚举 `wifi_iface_mode`。

<a id="r_ae2de076d79f2172793d65fe9cd31edc4"></a>

```c
enum wifi_link_mode link_mode
```

相关声明：[wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)、[link_mode](#ae2de076d79f2172793d65fe9cd31edc4)。

链路模式（Link mode），参见枚举 `wifi_link_mode`。

<a id="r_a361c0e8a385fdc21f16258c25c2bc8d1"></a>

```c
enum wifi_wpa3_enterprise_type wpa3_ent_type
```

相关声明：[wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)、[wpa3_ent_type](#a361c0e8a385fdc21f16258c25c2bc8d1)。

WPA3 企业类型（WPA3 enterprise type）。

<a id="r_a625ecec1abec8dd65cf155eab21a01b5"></a>

```c
enum wifi_security_type security
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[security](#a625ecec1abec8dd65cf155eab21a01b5)。

安全类型（Security type），参见枚举 `wifi_security_type`。

<a id="r_a9a899c28b51158e8973886f84d7d8950"></a>

```c
enum wifi_wep_key_type wep_key_type
```

相关声明：[wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)、[wep_key_type](#a9a899c28b51158e8973886f84d7d8950)。

有线等效保密密钥类型（WEP key type），为 64 位或 128 位，参见枚举 `wifi_wep_key_type`。

<a id="r_aa1a9b644fd355526125ddd32416b7c24"></a>

```c
enum wifi_mfp_options mfp
```

相关声明：[wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)、[mfp](#aa1a9b644fd355526125ddd32416b7c24)。

管理帧保护选项（MFP options），参见枚举 `wifi_mfp_options`。

<a id="r_a4e593147b88eb4938d55a4de72fcc7f6"></a>

```c
int rssi
```

相关声明：[rssi](#a4e593147b88eb4938d55a4de72fcc7f6)。

接收信号强度指示（RSSI）。

<a id="r_aae6c8cbaa16c81d308f08114d5103a3d"></a>

```c
unsigned char dtim_period
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[dtim_period](#aae6c8cbaa16c81d308f08114d5103a3d)。

投递流量指示消息周期（DTIM period）。

<a id="r_a241bfbe70628006b515b5f9e4f97665c"></a>

```c
unsigned short beacon_interval
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[beacon_interval](#a241bfbe70628006b515b5f9e4f97665c)。

信标间隔（Beacon interval）。

<a id="r_acfde8d64b463a9f553aa4fb689dc1917"></a>

```c
bool twt_capable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[twt_capable](#acfde8d64b463a9f553aa4fb689dc1917)。

是否支持目标唤醒时间（Target Wake Time，TWT）。

<a id="r_a43f239b0bc305e4c1c5f7fd9bb5753bf"></a>

```c
float current_phy_tx_rate
```

相关声明：[current_phy_tx_rate](#a43f239b0bc305e4c1c5f7fd9bb5753bf)。

当前 802.11 物理层发送数据速率（PHY TX data rate），单位为 Mbps。

## 175.2\_详细说明（Detailed Documentation）

<a id="ae1c141a18f4e225af2c22a8cb4f882a8"></a>

### `band`

```c
enum wifi_frequency_bands wifi_iface_status::band
```

频段（Frequency band）。

<a id="a241bfbe70628006b515b5f9e4f97665c"></a>

### `beacon_interval`

```c
unsigned short wifi_iface_status::beacon_interval
```

信标间隔（Beacon interval）。

<a id="a5d5d19056a1a15365fbdd94274a0fc5e"></a>

### `bssid`

```c
char wifi_iface_status::bssid[WIFI_MAC_ADDR_LEN]
```

基本服务集标识符（BSSID）。

<a id="a6432663156e5b2c424d254ed1eae0144"></a>

### `channel`

```c
unsigned int wifi_iface_status::channel
```

信道（Channel）。

<a id="a43f239b0bc305e4c1c5f7fd9bb5753bf"></a>

### `current_phy_tx_rate`

```c
float wifi_iface_status::current_phy_tx_rate
```

当前 802.11 物理层发送数据速率（PHY TX data rate），单位为 Mbps。

<a id="aae6c8cbaa16c81d308f08114d5103a3d"></a>

### `dtim_period`

```c
unsigned char wifi_iface_status::dtim_period
```

投递流量指示消息周期（DTIM period）。

<a id="ad33d2ec149a8d556e2472dd842ceadc0"></a>

### `iface_mode`

```c
enum wifi_iface_mode wifi_iface_status::iface_mode
```

接口模式（Interface mode），参见枚举 `wifi_iface_mode`。

<a id="ae2de076d79f2172793d65fe9cd31edc4"></a>

### `link_mode`

```c
enum wifi_link_mode wifi_iface_status::link_mode
```

链路模式（Link mode），参见枚举 `wifi_link_mode`。

<a id="aa1a9b644fd355526125ddd32416b7c24"></a>

### `mfp`

```c
enum wifi_mfp_options wifi_iface_status::mfp
```

管理帧保护选项（MFP options），参见枚举 `wifi_mfp_options`。

<a id="a4e593147b88eb4938d55a4de72fcc7f6"></a>

### `rssi`

```c
int wifi_iface_status::rssi
```

接收信号强度指示（RSSI）。

<a id="a625ecec1abec8dd65cf155eab21a01b5"></a>

### `security`

```c
enum wifi_security_type wifi_iface_status::security
```

安全类型（Security type），参见枚举 `wifi_security_type`。

<a id="a3ab671471bcdfeb5b955d156d39f2bb3"></a>

### `ssid`

```c
char wifi_iface_status::ssid[WIFI_SSID_MAX_LEN+1]
```

服务集标识符（SSID）。

<a id="ad82f281941e4f6ce1ef0bca008e26d41"></a>

### `ssid_len`

```c
unsigned int wifi_iface_status::ssid_len
```

服务集标识符长度（SSID length）。

<a id="ac52806155be3d64954ac6d109e76ec57"></a>

### `state`

```c
int wifi_iface_status::state
```

接口状态（Interface state），参见枚举 `wifi_iface_state`。

<a id="acfde8d64b463a9f553aa4fb689dc1917"></a>

### `twt_capable`

```c
bool wifi_iface_status::twt_capable
```

是否支持目标唤醒时间（Target Wake Time，TWT）。

<a id="a9a899c28b51158e8973886f84d7d8950"></a>

### `wep_key_type`

```c
enum wifi_wep_key_type wifi_iface_status::wep_key_type
```

有线等效保密密钥类型（WEP key type），为 64 位或 128 位，参见枚举 `wifi_wep_key_type`。

<a id="a361c0e8a385fdc21f16258c25c2bc8d1"></a>

### `wpa3_ent_type`

```c
enum wifi_wpa3_enterprise_type wifi_iface_status::wpa3_ent_type
```

WPA3 企业类型（WPA3 enterprise type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 175.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga981961f747b919d61d3ccbd41e4508b4)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)
- [wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P174_wifi_filter_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P176_wifi_mgmt_ops_结构体.md)
