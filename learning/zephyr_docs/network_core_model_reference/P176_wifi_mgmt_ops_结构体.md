---
id: learning.zephyr-docs.network-core-model-reference.page-176
title: wifi_mgmt_ops_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__mgmt__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_wifi\_mgmt\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__mgmt__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi管理（Management）API。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi管理（Management）API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 176.1\_数据成员（Data Fields）

<a id="r_acc20fd11dcd09edb72d03f8737801c06"></a>

```c
int(* scan )(const struct device *dev, struct net_if *iface, struct wifi_scan_params *params, scan_result_cb_t cb)
```

相关声明：[scan](#acc20fd11dcd09edb72d03f8737801c06)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_scan_params](P185_wifi_scan_params_结构体.md)、[scan_result_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad34b366f1c315207ce0da587ca96d8d8)。

扫描 Wi‑Fi 网络（Scan）。

<a id="r_a65a4e87ee94aa5c7a551aa9b39289708"></a>

```c
int(* connect )(const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

相关声明：[connect](#a65a4e87ee94aa5c7a551aa9b39289708)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_connect_req_params](P167_wifi_connect_req_params_结构体.md)。

连接 Wi‑Fi 网络（Connect）。

<a id="r_a8489951fc1baee17e56070187f4d77b0"></a>

```c
int(* disconnect )(const struct device *dev, struct net_if *iface)
```

相关声明：[disconnect](#a8489951fc1baee17e56070187f4d77b0)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

断开 Wi‑Fi 网络连接（Disconnect）。

<a id="r_aa34fff15f9e0aadf244f9e0cf37b367b"></a>

```c
int(* ap_enable )(const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

相关声明：[ap_enable](#aa34fff15f9e0aadf244f9e0cf37b367b)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_connect_req_params](P167_wifi_connect_req_params_结构体.md)。

启用接入点模式（AP mode）。

<a id="r_a3264be8040227d1e91a8223cabcd4e53"></a>

```c
int(* ap_disable )(const struct device *dev, struct net_if *iface)
```

相关声明：[ap_disable](#a3264be8040227d1e91a8223cabcd4e53)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

禁用接入点模式（AP mode）。

<a id="r_ad6e04312b0e7680f87ce801b2540db10"></a>

```c
int(* ap_sta_disconnect )(const struct device *dev, struct net_if *iface, const uint8_t *mac)
```

相关声明：[ap_sta_disconnect](#ad6e04312b0e7680f87ce801b2540db10)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使站点（STA）断开与接入点（AP）的连接。

<a id="r_a930cbd9e4661d137ae37cd89afd451b2"></a>

```c
int(* iface_status )(const struct device *dev, struct net_if *iface, struct wifi_iface_status *status)
```

相关声明：[iface_status](#a930cbd9e4661d137ae37cd89afd451b2)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_iface_status](P175_wifi_iface_status_结构体.md)。

获取接口状态（Interface status）。

<a id="r_abb2b7c033e77af36acde5d420effe8d1"></a>

```c
int(* get_stats )(const struct device *dev, struct net_if *iface, struct net_stats_wifi *stats)
```

相关声明：[get_stats](#abb2b7c033e77af36acde5d420effe8d1)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[net_stats_wifi](P153_net_stats_wifi_结构体.md)。

获取 Wi‑Fi 统计信息（Statistics）。

<a id="r_a7bd0f326e9eeedbc3c768c5ecf207c06"></a>

```c
int(* reset_stats )(const struct device *dev, struct net_if *iface)
```

相关声明：[reset_stats](#a7bd0f326e9eeedbc3c768c5ecf207c06)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

重置 Wi‑Fi 统计信息（Statistics）。

<a id="r_ab3b7dce2feb0ecbca3d4668dc9e41032"></a>

```c
int(* cfg_11k )(const struct device *dev, struct net_if *iface, struct wifi_11k_params *params)
```

相关声明：[cfg_11k](#ab3b7dce2feb0ecbca3d4668dc9e41032)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_11k_params](P158_wifi_11k_params_结构体.md)。

设置或获取 802.11k 状态（11K status）。

<a id="r_a16fc04b7572234f6e7c207d82e0b4625"></a>

```c
int(* send_11k_neighbor_request )(const struct device *dev, struct net_if *iface, struct wifi_11k_params *params)
```

相关声明：[send_11k_neighbor_request](#a16fc04b7572234f6e7c207d82e0b4625)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_11k_params](P158_wifi_11k_params_结构体.md)。

发送 802.11k 邻居请求（11k neighbor request）。

<a id="r_a37e6c41f4b1223b8952171abb5cd9d89"></a>

```c
int(* set_power_save )(const struct device *dev, struct net_if *iface, struct wifi_ps_params *params)
```

相关声明：[set_power_save](#a37e6c41f4b1223b8952171abb5cd9d89)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_ps_params](P181_wifi_ps_params_结构体.md)。

设置省电状态（Power save status）。

<a id="r_af2089cba9ba73593b8d5b4329f2fddff"></a>

```c
int(* set_twt )(const struct device *dev, struct net_if *iface, struct wifi_twt_params *params)
```

相关声明：[set_twt](#af2089cba9ba73593b8d5b4329f2fddff)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_twt_params](P189_wifi_twt_params_结构体.md)。

建立或拆除目标唤醒时间流（TWT flow）。

<a id="r_a50421d54785d4f8d768c8a35fcda0ca5"></a>

```c
int(* set_btwt )(const struct device *dev, struct net_if *iface, struct wifi_twt_params *params)
```

相关声明：[set_btwt](#a50421d54785d4f8d768c8a35fcda0ca5)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_twt_params](P189_wifi_twt_params_结构体.md)。

建立广播目标唤醒时间流（BTWT flow）。

<a id="r_a9278c8779748e64ad70cfbeef5a297dd"></a>

```c
int(* get_power_save_config )(const struct device *dev, struct net_if *iface, struct wifi_ps_config *config)
```

相关声明：[get_power_save_config](#a9278c8779748e64ad70cfbeef5a297dd)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_ps_config](P180_wifi_ps_config_结构体.md)。

获取省电配置（Power save configuration）。

<a id="r_a80b09c5ea77c99a4dfffb5a21f0c8867"></a>

```c
int(* reg_domain )(const struct device *dev, struct net_if *iface, struct wifi_reg_domain *reg_domain)
```

相关声明：[reg_domain](#a80b09c5ea77c99a4dfffb5a21f0c8867)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_reg_domain](P184_wifi_reg_domain_结构体.md)。

设置或获取监管域（Regulatory domain）。

<a id="r_a5642ca19f2f25ba7a53d9efb30d7bd59"></a>

```c
int(* filter )(const struct device *dev, struct net_if *iface, struct wifi_filter_info *filter)
```

相关声明：[filter](#a5642ca19f2f25ba7a53d9efb30d7bd59)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_filter_info](P174_wifi_filter_info_结构体.md)。

设置或获取监听模式（Monitor mode）和混杂模式（Promiscuous mode）的数据包过滤器设置。

<a id="r_a0bfeb2a8f463dc49ca3d433ee17d3dd9"></a>

```c
int(* mode )(const struct device *dev, struct net_if *iface, struct wifi_mode_info *mode)
```

相关声明：[mode](#a0bfeb2a8f463dc49ca3d433ee17d3dd9)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_mode_info](P177_wifi_mode_info_结构体.md)。

设置或获取工作模式（Mode of operation）。

<a id="r_a365e9aafc5399e1a9f37c9b4f347534c"></a>

```c
int(* channel )(const struct device *dev, struct net_if *iface, struct wifi_channel_info *channel)
```

相关声明：[channel](#a365e9aafc5399e1a9f37c9b4f347534c)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_channel_info](P164_wifi_channel_info_结构体.md)。

设置或获取当前工作信道（Channel of operation）。

<a id="r_ad241d490ac3e10c58c87da004d706407"></a>

```c
int(* btm_query )(const struct device *dev, struct net_if *iface, uint8_t reason)
```

相关声明：[btm_query](#ad241d490ac3e10c58c87da004d706407)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送基本服务集转换管理查询（BTM query）。

<a id="r_a6198f23a4cdeb5b0e413b7a66c1fa442"></a>

```c
bool(* bss_support_neighbor_rep )(const struct device *dev, struct net_if *iface)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bss_support_neighbor_rep](#a6198f23a4cdeb5b0e413b7a66c1fa442)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

检查接入点（AP）是否支持邻居报告（Neighbor Report）。

<a id="r_ac6d82f5f2defdc657f056f0e6103e04b"></a>

```c
int(* bss_ext_capab )(const struct device *dev, struct net_if *iface, int capab)
```

相关声明：[bss_ext_capab](#ac6d82f5f2defdc657f056f0e6103e04b)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

判断接入点（AP）是否支持该能力（Capability）。

<a id="r_a8d37cec74b3d523257120b75f471e92f"></a>

```c
int(* legacy_roam )(const struct device *dev, struct net_if *iface)
```

相关声明：[legacy_roam](#a8d37cec74b3d523257120b75f471e92f)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

发送传统扫描请求（Legacy scan）。

<a id="r_a7b788903271a427363d22808659a3ee9"></a>

```c
int(* get_version )(const struct device *dev, struct net_if *iface, struct wifi_version *params)
```

相关声明：[get_version](#a7b788903271a427363d22808659a3ee9)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_version](P190_wifi_version_结构体.md)。

获取 Wi‑Fi 驱动和固件版本（Driver and Firmware version）。

<a id="r_ab5368326d558de972ce5806dd9a99f22"></a>

```c
int(* get_conn_params )(const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

相关声明：[get_conn_params](#ab5368326d558de972ce5806dd9a99f22)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_connect_req_params](P167_wifi_connect_req_params_结构体.md)。

获取最近使用的 Wi‑Fi 连接参数（Connection parameters）。

<a id="r_aed7b6daf7264c1450cc5d31530a2043a"></a>

```c
int(* set_rts_threshold )(const struct device *dev, struct net_if *iface, unsigned int rts_threshold)
```

相关声明：[set_rts_threshold](#aed7b6daf7264c1450cc5d31530a2043a)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

设置请求发送阈值（RTS threshold）。

<a id="r_a01b2ac4cd8a1f039bdba3adb2586d3cb"></a>

```c
int(* ap_config_params )(const struct device *dev, struct net_if *iface, struct wifi_ap_config_params *params)
```

相关声明：[ap_config_params](#a01b2ac4cd8a1f039bdba3adb2586d3cb)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_ap_config_params](P159_wifi_ap_config_params_结构体.md)。

配置接入点参数（AP parameter）。

<a id="r_a63e7bcc4d3bb9ee7e073a6c55abddcc2"></a>

```c
int(* config_params )(const struct device *dev, struct net_if *iface, struct wifi_config_params *params)
```

相关声明：[config_params](#a63e7bcc4d3bb9ee7e073a6c55abddcc2)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_config_params](P166_wifi_config_params_结构体.md)。

配置站点参数（STA parameter）。

<a id="r_a76e76d96e307bc10bd14e4ea7b5dbed6"></a>

```c
int(* pmksa_flush )(const struct device *dev, struct net_if *iface)
```

相关声明：[pmksa_flush](#a76e76d96e307bc10bd14e4ea7b5dbed6)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

清空成对主密钥安全关联缓存条目（PMKSA cache entries）。

<a id="r_ad3c8908b6a3752adf59d5a4170175f83"></a>

```c
int(* get_rts_threshold )(const struct device *dev, struct net_if *iface, unsigned int *rts_threshold)
```

相关声明：[get_rts_threshold](#ad3c8908b6a3752adf59d5a4170175f83)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

设置 Wi‑Fi 企业模式的 CA／客户端证书及密钥（CA/client certificate and key）。

<a id="r_ab8e11d463ff7000a090e0609f002a97c"></a>

```c
int(* wps_config )(const struct device *dev, struct net_if *iface, struct wifi_wps_config_params *params)
```

相关声明：[wps_config](#ab8e11d463ff7000a090e0609f002a97c)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_wps_config_params](P191_wifi_wps_config_params_结构体.md)。

启动 Wi‑Fi 保护设置的按钮配置／PIN 连接（WPS PBC/PIN connection）。

<a id="r_a69f2ec3a03e77b4eb9d9fdd7315edf18"></a>

```c
int(* candidate_scan )(const struct device *dev, struct net_if *iface, struct wifi_scan_params *params)
```

相关声明：[candidate_scan](#a69f2ec3a03e77b4eb9d9fdd7315edf18)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_scan_params](P185_wifi_scan_params_结构体.md)。

触发候选扫描（Candidate scan）。

<a id="r_ac4ed6d4d1088f6e23d5256d156e42955"></a>

```c
int(* start_11r_roaming )(const struct device *dev, struct net_if *iface)
```

相关声明：[start_11r_roaming](#ac4ed6d4d1088f6e23d5256d156e42955)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

启动 802.11r 漫游（11r roaming）。

<a id="r_a26eaabf9621b16d332e20777b188d4ad"></a>

```c
int(* set_bss_max_idle_period )(const struct device *dev, struct net_if *iface, unsigned short bss_max_idle_period)
```

相关声明：[set_bss_max_idle_period](#a26eaabf9621b16d332e20777b188d4ad)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

设置基本服务集最大空闲周期（BSS max idle period）。

<a id="r_a0aa02b0d69479b95d6e1a0971b16ee92"></a>

```c
int(* set_bgscan )(const struct device *dev, struct net_if *iface, struct wifi_bgscan_params *params)
```

相关声明：[set_bgscan](#a0aa02b0d69479b95d6e1a0971b16ee92)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)、[wifi_bgscan_params](P162_wifi_bgscan_params_结构体.md)。

配置后台扫描（Background scanning）。

<a id="r_a40d53afce76b5b7614ee95e41ea46635"></a>

```c
uint32_t(* get_iface_caps )(const struct device *dev, struct net_if *iface)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_iface_caps](#a40d53afce76b5b7614ee95e41ea46635)、[device](../device_reference/P002_设备对象结构.md)、[net_if](P079_net_if_结构体.md)。

获取接口支持的角色（Supported roles），属于静态驱动能力（Static driver capability）。

## 176.2\_详细说明（Detailed Documentation）

<a id="a01b2ac4cd8a1f039bdba3adb2586d3cb"></a>

### `ap_config_params`

```c
int(* wifi_mgmt_ops::ap_config_params) (const struct device *dev, struct net_if *iface, struct wifi_ap_config_params *params)
```

配置接入点参数（AP parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于接入点参数配置操作（AP parameter configuration）的网络接口。 |
| `params` | 接入点模式参数的配置信息（AP mode parameter configuration information）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a3264be8040227d1e91a8223cabcd4e53"></a>

### `ap_disable`

```c
int(* wifi_mgmt_ops::ap_disable) (const struct device *dev, struct net_if *iface)
```

禁用接入点模式（AP mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 接入点（AP）使用的网络接口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="aa34fff15f9e0aadf244f9e0cf37b367b"></a>

### `ap_enable`

```c
int(* wifi_mgmt_ops::ap_enable) (const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

启用接入点模式（AP mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 接入点（AP）使用的网络接口。 |
| `params` | 接入点模式参数（AP mode parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ad6e04312b0e7680f87ce801b2540db10"></a>

### `ap_sta_disconnect`

```c
int(* wifi_mgmt_ops::ap_sta_disconnect) (const struct device *dev, struct net_if *iface, const uint8_t *mac)
```

使站点（STA）断开与接入点（AP）的连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 接入点（AP）使用的网络接口。 |
| `mac` | 要断开连接的站点（STA）的 MAC 地址。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ac6d82f5f2defdc657f056f0e6103e04b"></a>

### `bss_ext_capab`

```c
int(* wifi_mgmt_ops::bss_ext_capab) (const struct device *dev, struct net_if *iface, int capab)
```

判断接入点（AP）是否支持该能力（Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于能力查询操作（Capability operation）的网络接口。 |
| `capab` | 要判断的能力（Capability）。 |

**返回（Returns）**：返回值（Returns）：支持时为 `1`，不支持时为 `0`。

<a id="a6198f23a4cdeb5b0e413b7a66c1fa442"></a>

### `bss_support_neighbor_rep`

```c
bool(* wifi_mgmt_ops::bss_support_neighbor_rep) (const struct device *dev, struct net_if *iface)
```

检查接入点（AP）是否支持邻居报告（Neighbor Report）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于邻居报告操作（Neighbor Report operation）的网络接口。 |

**返回（Returns）**：返回值（Returns）：支持时为 `true`，不支持时为 `false`。

<a id="ad241d490ac3e10c58c87da004d706407"></a>

### `btm_query`

```c
int(* wifi_mgmt_ops::btm_query) (const struct device *dev, struct net_if *iface, uint8_t reason)
```

发送基本服务集转换管理查询（BTM query）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于基本服务集转换管理查询操作（BTM query）的网络接口。 |
| `reason` | 查询原因（Query reason）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a69f2ec3a03e77b4eb9d9fdd7315edf18"></a>

### `candidate_scan`

```c
int(* wifi_mgmt_ops::candidate_scan) (const struct device *dev, struct net_if *iface, struct wifi_scan_params *params)
```

触发候选扫描（Candidate scan）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于扫描操作（Scan operation）的网络接口。 |
| `params` | 扫描参数（Scan parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ab3b7dce2feb0ecbca3d4668dc9e41032"></a>

### `cfg_11k`

```c
int(* wifi_mgmt_ops::cfg_11k) (const struct device *dev, struct net_if *iface, struct wifi_11k_params *params)
```

设置或获取 802.11k 状态（11K status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于 802.11k 操作（11k operation）的网络接口。 |
| `params` | 802.11k 参数（11k parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a365e9aafc5399e1a9f37c9b4f347534c"></a>

### `channel`

```c
int(* wifi_mgmt_ops::channel) (const struct device *dev, struct net_if *iface, struct wifi_channel_info *channel)
```

设置或获取当前工作信道（Channel of operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于信道操作（Channel operation）的网络接口。 |
| `channel` | 设置（Settings）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a63e7bcc4d3bb9ee7e073a6c55abddcc2"></a>

### `config_params`

```c
int(* wifi_mgmt_ops::config_params) (const struct device *dev, struct net_if *iface, struct wifi_config_params *params)
```

配置站点参数（STA parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于站点参数配置操作（STA parameter configuration）的网络接口。 |
| `params` | 站点模式参数的配置信息（STA mode parameter configuration information）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a65a4e87ee94aa5c7a551aa9b39289708"></a>

### `connect`

```c
int(* wifi_mgmt_ops::connect) (const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

连接 Wi‑Fi 网络（Connect）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于连接（Connection）的网络接口。 |
| `params` | 连接参数（Connect parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a8489951fc1baee17e56070187f4d77b0"></a>

### `disconnect`

```c
int(* wifi_mgmt_ops::disconnect) (const struct device *dev, struct net_if *iface)
```

断开 Wi‑Fi 网络连接（Disconnect）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 要断开连接（Disconnect）的网络接口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a5642ca19f2f25ba7a53d9efb30d7bd59"></a>

### `filter`

```c
int(* wifi_mgmt_ops::filter) (const struct device *dev, struct net_if *iface, struct wifi_filter_info *filter)
```

设置或获取监听模式（Monitor mode）和混杂模式（Promiscuous mode）的数据包过滤器设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于过滤器操作（Filter operation）的网络接口。 |
| `filter` | 过滤器设置（Filter settings）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ab5368326d558de972ce5806dd9a99f22"></a>

### `get_conn_params`

```c
int(* wifi_mgmt_ops::get_conn_params) (const struct device *dev, struct net_if *iface, struct wifi_connect_req_params *params)
```

获取最近使用的 Wi‑Fi 连接参数（Connection parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于获取连接参数（Get connection parameters）的网络接口。 |
| `params` | 最近使用的 Wi‑Fi 连接参数（Connection parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a40d53afce76b5b7614ee95e41ea46635"></a>

### `get_iface_caps`

```c
uint32_t(* wifi_mgmt_ops::get_iface_caps) (const struct device *dev, struct net_if *iface)
```

获取接口支持的角色（Supported roles），属于静态驱动能力（Static driver capability）。

认证请求端（Supplicant）在添加接口时读取一次，并将其视为每个接口的静态属性（Static per-interface property）。驱动不能用它在运行时通知角色变化（Role change）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 要查询的网络接口（Network interface）。 |

**返回（Returns）**：返回值（Returns）：支持角色的 `BIT(enum wifi_nm_iface_type)` 位集合。返回 `0` 时，由调用者使用默认值。

<a id="a9278c8779748e64ad70cfbeef5a297dd"></a>

### `get_power_save_config`

```c
int(* wifi_mgmt_ops::get_power_save_config) (const struct device *dev, struct net_if *iface, struct wifi_ps_config *config)
```

获取省电配置（Power save configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于省电操作（Power save operation）的网络接口。 |
| `config` | 省电配置（Power save configuration）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ad3c8908b6a3752adf59d5a4170175f83"></a>

### `get_rts_threshold`

```c
int(* wifi_mgmt_ops::get_rts_threshold) (const struct device *dev, struct net_if *iface, unsigned int *rts_threshold)
```

设置 Wi‑Fi 企业模式的 CA／客户端证书及密钥（CA/client certificate and key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于企业凭据操作（Enterprise credentials operation）的网络接口。 |
| `creds` | 指向 CA／客户端证书及密钥（CA/client certificate and key）的指针。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于请求发送阈值操作（RTS threshold operation）的网络接口。 |
| `rts_threshold` | 指向请求发送阈值（RTS threshold value）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。获取请求发送阈值（RTS threshold value）。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="abb2b7c033e77af36acde5d420effe8d1"></a>

### `get_stats`

```c
int(* wifi_mgmt_ops::get_stats) (const struct device *dev, struct net_if *iface, struct net_stats_wifi *stats)
```

获取 Wi‑Fi 统计信息（Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于获取统计信息（Statistics）的网络接口。 |
| `stats` | Wi‑Fi 统计信息（Wi-Fi statistics）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a7b788903271a427363d22808659a3ee9"></a>

### `get_version`

```c
int(* wifi_mgmt_ops::get_version) (const struct device *dev, struct net_if *iface, struct wifi_version *params)
```

获取 Wi‑Fi 驱动和固件版本（Driver and Firmware version）。

实现 `get_version` 函数的驱动不得使用栈（Stack）来分配由 `params` 结构成员返回的版本信息指针所指向的数据。版本指针参数应指向只读存储器（ROM，首选）或随机存取存储器（RAM）中的静态内存（Static memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于获取版本（Get version）的网络接口。 |
| `params` | 版本参数（Version parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a930cbd9e4661d137ae37cd89afd451b2"></a>

### `iface_status`

```c
int(* wifi_mgmt_ops::iface_status) (const struct device *dev, struct net_if *iface, struct wifi_iface_status *status)
```

获取接口状态（Interface status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于获取状态（Status）的网络接口。 |
| `status` | 接口状态（Interface status）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a8d37cec74b3d523257120b75f471e92f"></a>

### `legacy_roam`

```c
int(* wifi_mgmt_ops::legacy_roam) (const struct device *dev, struct net_if *iface)
```

发送传统扫描请求（Legacy scan）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于传统扫描操作（Legacy scan operation）的网络接口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a0bfeb2a8f463dc49ca3d433ee17d3dd9"></a>

### `mode`

```c
int(* wifi_mgmt_ops::mode) (const struct device *dev, struct net_if *iface, struct wifi_mode_info *mode)
```

设置或获取工作模式（Mode of operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于模式操作（Mode operation）的网络接口。 |
| `mode` | 设置（Settings）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a76e76d96e307bc10bd14e4ea7b5dbed6"></a>

### `pmksa_flush`

```c
int(* wifi_mgmt_ops::pmksa_flush) (const struct device *dev, struct net_if *iface)
```

清空成对主密钥安全关联缓存条目（PMKSA cache entries）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于清空成对主密钥安全关联缓存（PMKSA flush）的网络接口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a80b09c5ea77c99a4dfffb5a21f0c8867"></a>

### `reg_domain`

```c
int(* wifi_mgmt_ops::reg_domain) (const struct device *dev, struct net_if *iface, struct wifi_reg_domain *reg_domain)
```

设置或获取监管域（Regulatory domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于监管域操作（Regulatory domain operation）的网络接口。 |
| `reg_domain` | 监管域（Regulatory domain）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a7bd0f326e9eeedbc3c768c5ecf207c06"></a>

### `reset_stats`

```c
int(* wifi_mgmt_ops::reset_stats) (const struct device *dev, struct net_if *iface)
```

重置 Wi‑Fi 统计信息（Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于重置统计信息（Reset statistics）的网络接口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="acc20fd11dcd09edb72d03f8737801c06"></a>

### `scan`

```c
int(* wifi_mgmt_ops::scan) (const struct device *dev, struct net_if *iface, struct wifi_scan_params *params, scan_result_cb_t cb)
```

扫描 Wi‑Fi 网络（Scan）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于扫描（Scan）的网络接口。 |
| `params` | 扫描参数（Scan parameters）。 |
| `cb` | 每获得一项结果时调用的回调（Callback）。驱动应针对每项结果调用 `cb` 参数指定的回调。Wi‑Fi 管理部分（Wi-Fi mgmt）负责触发必要事件等处理。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a16fc04b7572234f6e7c207d82e0b4625"></a>

### `send_11k_neighbor_request`

```c
int(* wifi_mgmt_ops::send_11k_neighbor_request) (const struct device *dev, struct net_if *iface, struct wifi_11k_params *params)
```

发送 802.11k 邻居请求（11k neighbor request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于 802.11k 操作（11k operation）的网络接口。 |
| `params` | 802.11k 参数（11k parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a0aa02b0d69479b95d6e1a0971b16ee92"></a>

### `set_bgscan`

```c
int(* wifi_mgmt_ops::set_bgscan) (const struct device *dev, struct net_if *iface, struct wifi_bgscan_params *params)
```

配置后台扫描（Background scanning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于后台扫描操作（Background scanning operation）的网络接口。 |
| `params` | 后台扫描配置参数（Background scanning configuration parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a26eaabf9621b16d332e20777b188d4ad"></a>

### `set_bss_max_idle_period`

```c
int(* wifi_mgmt_ops::set_bss_max_idle_period) (const struct device *dev, struct net_if *iface, unsigned short bss_max_idle_period)
```

设置基本服务集最大空闲周期（BSS max idle period）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于基本服务集最大空闲周期操作（BSS max idle period operation）的网络接口。 |
| `bss_max_idle_period` | 最大空闲周期值（Max idle period value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a50421d54785d4f8d768c8a35fcda0ca5"></a>

### `set_btwt`

```c
int(* wifi_mgmt_ops::set_btwt) (const struct device *dev, struct net_if *iface, struct wifi_twt_params *params)
```

建立广播目标唤醒时间流（BTWT flow）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于广播目标唤醒时间操作（BTWT operation）的网络接口。 |
| `params` | 广播目标唤醒时间参数（BTWT parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="a37e6c41f4b1223b8952171abb5cd9d89"></a>

### `set_power_save`

```c
int(* wifi_mgmt_ops::set_power_save) (const struct device *dev, struct net_if *iface, struct wifi_ps_params *params)
```

设置省电状态（Power save status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于省电操作（Power save operation）的网络接口。 |
| `params` | 省电参数（Power save parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="aed7b6daf7264c1450cc5d31530a2043a"></a>

### `set_rts_threshold`

```c
int(* wifi_mgmt_ops::set_rts_threshold) (const struct device *dev, struct net_if *iface, unsigned int rts_threshold)
```

设置请求发送阈值（RTS threshold）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于请求发送阈值操作（RTS threshold operation）的网络接口。 |
| `rts_threshold` | 请求发送阈值（RTS threshold value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="af2089cba9ba73593b8d5b4329f2fddff"></a>

### `set_twt`

```c
int(* wifi_mgmt_ops::set_twt) (const struct device *dev, struct net_if *iface, struct wifi_twt_params *params)
```

建立或拆除目标唤醒时间流（TWT flow）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于目标唤醒时间操作（TWT operation）的网络接口。 |
| `params` | 目标唤醒时间参数（TWT parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ac4ed6d4d1088f6e23d5256d156e42955"></a>

### `start_11r_roaming`

```c
int(* wifi_mgmt_ops::start_11r_roaming) (const struct device *dev, struct net_if *iface)
```

启动 802.11r 漫游（11r roaming）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于漫游操作（Roaming operation）的网络接口。 |

**已弃用（Deprecated）**：已弃用（Deprecated）：由连接请求参数（Connection request parameters）控制。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ab8e11d463ff7000a090e0609f002a97c"></a>

### `wps_config`

```c
int(* wifi_mgmt_ops::wps_config) (const struct device *dev, struct net_if *iface, struct wifi_wps_config_params *params)
```

启动 Wi‑Fi 保护设置的按钮配置／PIN 连接（WPS PBC/PIN connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `iface` | 用于 Wi‑Fi 保护设置操作（WPS operation）的网络接口。 |
| `params` | Wi‑Fi 保护设置操作参数（WPS operation parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 176.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if](P079_net_if_结构体.md)
- [wifi_scan_params](P185_wifi_scan_params_结构体.md)
- [scan_result_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad34b366f1c315207ce0da587ca96d8d8)
- [wifi_connect_req_params](P167_wifi_connect_req_params_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_iface_status](P175_wifi_iface_status_结构体.md)
- [net_stats_wifi](P153_net_stats_wifi_结构体.md)
- [wifi_11k_params](P158_wifi_11k_params_结构体.md)
- [wifi_ps_params](P181_wifi_ps_params_结构体.md)
- [wifi_twt_params](P189_wifi_twt_params_结构体.md)
- [wifi_ps_config](P180_wifi_ps_config_结构体.md)
- [wifi_reg_domain](P184_wifi_reg_domain_结构体.md)
- [wifi_filter_info](P174_wifi_filter_info_结构体.md)
- [wifi_mode_info](P177_wifi_mode_info_结构体.md)
- [wifi_channel_info](P164_wifi_channel_info_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [wifi_version](P190_wifi_version_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [wifi_ap_config_params](P159_wifi_ap_config_params_结构体.md)
- [wifi_config_params](P166_wifi_config_params_结构体.md)
- [wifi_wps_config_params](P191_wifi_wps_config_params_结构体.md)
- [wifi_bgscan_params](P162_wifi_bgscan_params_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BIT(enum wifi_nm_iface_type)](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000101)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P175_wifi_iface_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P177_wifi_mode_info_结构体.md)
