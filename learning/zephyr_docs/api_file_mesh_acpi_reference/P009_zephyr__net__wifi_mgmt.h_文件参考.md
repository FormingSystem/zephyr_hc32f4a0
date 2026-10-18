---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-9
title: zephyr__net__wifi_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_net\_\_wifi\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi第二层协议栈（L2 Stack）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/wifi.h>
#include <zephyr/net/ethernet.h>
#include <zephyr/net/offloaded_netdev.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

Wi-Fi第二层协议栈（L2 Stack）的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_wifi_5Fversion"></a>

```c
struct wifi_version
```

相关声明：[wifi_version](../network_core_model_reference/P190_wifi_version_结构体.md)。

Wi-Fi版本（Version）。

<a id="r_wifi_5Fband_5Fchannel"></a>

```c
struct wifi_band_channel
```

相关声明：[wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)。

用于唯一标识频段-信道对（Band-Channel Pair）的Wi-Fi结构。

<a id="r_wifi_5Fscan_5Fparams"></a>

```c
struct wifi_scan_params
```

相关声明：[wifi_scan_params](../network_core_model_reference/P185_wifi_scan_params_结构体.md)。

Wi-Fi扫描参数（Scan Parameters）的结构。

<a id="r_wifi_5Fscan_5Fresult"></a>

```c
struct wifi_scan_result
```

相关声明：[wifi_scan_result](../network_core_model_reference/P186_wifi_scan_result_结构体.md)。

Wi-Fi扫描结果（Scan Result）；每个结果通过net_mgmt_event_callback的info属性提供，见net_mgmt.h。

<a id="r_wifi_5Fconnect_5Freq_5Fparams"></a>

```c
struct wifi_connect_req_params
```

相关声明：[wifi_connect_req_params](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md)。

Wi-Fi连接请求（Connect Request）的参数。

<a id="r_wifi_5Fstatus"></a>

```c
struct wifi_status
```

相关声明：[wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)。

命令与事件通用的Wi-Fi状态（Status）。

<a id="r_wifi_5Fiface_5Fstatus"></a>

```c
struct wifi_iface_status
```

相关声明：[wifi_iface_status](../network_core_model_reference/P175_wifi_iface_status_结构体.md)。

Wi-Fi接口状态（Interface Status）。

<a id="r_wifi_5Fps_5Fparams"></a>

```c
struct wifi_ps_params
```

相关声明：[wifi_ps_params](../network_core_model_reference/P181_wifi_ps_params_结构体.md)。

Wi-Fi省电参数（Power Save Parameters）。

<a id="r_wifi_5Fbtwt_5Fparams"></a>

```c
struct wifi_btwt_params
```

相关声明：[wifi_btwt_params](../network_core_model_reference/P163_wifi_btwt_params_结构体.md)。

Wi-Fi广播目标唤醒时间（Broadcast TWT）的参数。

<a id="r_wifi_5Ftwt_5Fparams"></a>

```c
struct wifi_twt_params
```

相关声明：[wifi_twt_params](../network_core_model_reference/P189_wifi_twt_params_结构体.md)。

Wi-Fi目标唤醒时间（TWT）的参数。

<a id="r_wifi_5Ftwt_5Fflow_5Finfo"></a>

```c
struct wifi_twt_flow_info
```

相关声明：[wifi_twt_flow_info](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md)。

Wi-Fi目标唤醒时间流（TWT Flow）的信息。

<a id="r_wifi_5Fenterprise_5Fcreds_5Fparams"></a>

```c
struct wifi_enterprise_creds_params
```

相关声明：[wifi_enterprise_creds_params](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md)。

Wi-Fi企业模式凭据（Enterprise Mode Credentials）。

<a id="r_wifi_5Fps_5Fconfig"></a>

```c
struct wifi_ps_config
```

相关声明：[wifi_ps_config](../network_core_model_reference/P180_wifi_ps_config_结构体.md)。

Wi-Fi省电配置（Power Save Configuration）。

<a id="r_wifi_5F11k_5Fparams"></a>

```c
struct wifi_11k_params
```

相关声明：[wifi_11k_params](../network_core_model_reference/P158_wifi_11k_params_结构体.md)。

Wi-Fi 802.11k参数。

<a id="r_wifi_5Freg_5Fchan_5Finfo"></a>

```c
struct wifi_reg_chan_info
```

相关声明：[wifi_reg_chan_info](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md)。

各信道的监管属性（Regulatory Attributes）。

<a id="r_wifi_5Freg_5Fdomain"></a>

```c
struct wifi_reg_domain
```

相关声明：[wifi_reg_domain](../network_core_model_reference/P184_wifi_reg_domain_结构体.md)。

监管域（Regulatory Domain）的信息或配置。

<a id="r_wifi_5Fraw_5Fscan_5Fresult"></a>

```c
struct wifi_raw_scan_result
```

相关声明：[wifi_raw_scan_result](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md)。

Wi-Fi原始扫描结果（Raw Scan Result）。

<a id="r_wifi_5Fap_5Fsta_5Finfo"></a>

```c
struct wifi_ap_sta_info
```

相关声明：[wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)。

接入点（AP）模式：已连接站点（STA）的详情。

<a id="r_wifi_5Fmode_5Finfo"></a>

```c
struct wifi_mode_info
```

相关声明：[wifi_mode_info](../network_core_model_reference/P177_wifi_mode_info_结构体.md)。

Wi-Fi模式设置（Mode Setup）。

<a id="r_wifi_5Ffilter_5Finfo"></a>

```c
struct wifi_filter_info
```

相关声明：[wifi_filter_info](../network_core_model_reference/P174_wifi_filter_info_结构体.md)。

Wi-Fi监听、混杂和发送注入模式（Monitor, Promiscuous, TX-Injection Modes）的过滤器设置。

<a id="r_wifi_5Fchannel_5Finfo"></a>

```c
struct wifi_channel_info
```

相关声明：[wifi_channel_info](../network_core_model_reference/P164_wifi_channel_info_结构体.md)。

Wi-Fi监听及发送注入模式（Monitor / TX-Injection Modes）的信道设置。

<a id="r_wifi_5Fap_5Fconfig_5Fparams"></a>

```c
struct wifi_ap_config_params
```

相关声明：[wifi_ap_config_params](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md)。

Wi-Fi接入点（AP）的配置参数。

<a id="r_wifi_5Fconfig_5Fparams"></a>

```c
struct wifi_config_params
```

相关声明：[wifi_config_params](../network_core_model_reference/P166_wifi_config_params_结构体.md)。

Wi-Fi站点（STA）的配置参数。

<a id="r_wifi_5Fwps_5Fconfig_5Fparams"></a>

```c
struct wifi_wps_config_params
```

相关声明：[wifi_wps_config_params](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md)。

Wi-Fi保护设置（WPS）的配置。

<a id="r_wifi_5Fbgscan_5Fparams"></a>

```c
struct wifi_bgscan_params
```

相关声明：[wifi_bgscan_params](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md)。

Wi-Fi后台扫描参数（Background Scan Parameters）。

<a id="r_wifi_5Fmgmt_5Fops"></a>

```c
struct wifi_mgmt_ops
```

相关声明：[wifi_mgmt_ops](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md)。

Wi-Fi管理（Management）API。

<a id="r_net_5Fwifi_5Fmgmt_5Foffload"></a>

```c
struct net_wifi_mgmt_offload
```

相关声明：[net_wifi_mgmt_offload](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md)。

Wi-Fi管理卸载（Management Offload）API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga1c277da90986fa52dca182c4d922646f"></a>

```c
#define NET_REQUEST_WIFI_SCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_SCAN)
```

相关声明：[NET_REQUEST_WIFI_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1c277da90986fa52dca182c4d922646f)、[NET_REQUEST_WIFI_CMD_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)。

请求 Wi-Fi 扫描（Scan）。

<a id="r_gaa7ab2a97950a22736bb69f60b459f0f6"></a>

```c
#define NET_REQUEST_WIFI_CONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONNECT)
```

相关声明：[NET_REQUEST_WIFI_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa7ab2a97950a22736bb69f60b459f0f6)、[NET_REQUEST_WIFI_CMD_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)。

请求 Wi-Fi 连接（Connect）。

<a id="r_ga90afd8d4e83056463ec6e667ed8ea60a"></a>

```c
#define NET_REQUEST_WIFI_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_DISCONNECT)
```

相关声明：[NET_REQUEST_WIFI_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga90afd8d4e83056463ec6e667ed8ea60a)、[NET_REQUEST_WIFI_CMD_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)。

请求 Wi-Fi 断开连接（Disconnect）。

<a id="r_ga638d2eb0a5029c1af46a91b523ed8589"></a>

```c
#define NET_REQUEST_WIFI_AP_ENABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_ENABLE)
```

相关声明：[NET_REQUEST_WIFI_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga638d2eb0a5029c1af46a91b523ed8589)、[NET_REQUEST_WIFI_CMD_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)。

请求启用 Wi-Fi 接入点（Access Point，AP）。

<a id="r_gaf81f62bf4c9e331a095acbf0d24ca1a2"></a>

```c
#define NET_REQUEST_WIFI_AP_DISABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_DISABLE)
```

相关声明：[NET_REQUEST_WIFI_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf81f62bf4c9e331a095acbf0d24ca1a2)、[NET_REQUEST_WIFI_CMD_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)。

请求禁用 Wi-Fi 接入点（Access Point，AP）。

<a id="r_ga9918582d4e7bb0952daf993ee34e166d"></a>

```c
#define NET_REQUEST_WIFI_AP_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD)
```

相关声明：[NET_REQUEST_WIFI_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9918582d4e7bb0952daf993ee34e166d)、[NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)。

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_ga3e45f6ee3801553619d8eb7d0af506eb"></a>

```c
#define NET_REQUEST_WIFI_IFACE_STATUS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_IFACE_STATUS)
```

相关声明：[NET_REQUEST_WIFI_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e45f6ee3801553619d8eb7d0af506eb)、[NET_REQUEST_WIFI_CMD_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)。

请求 Wi-Fi 网络接口状态（Network Interface Status）。

<a id="r_gadd9b5b206c7ee2e40c30a37c7b4fc002"></a>

```c
#define NET_REQUEST_WIFI_11K_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadd9b5b206c7ee2e40c30a37c7b4fc002)、[NET_REQUEST_WIFI_CMD_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)。

请求 Wi-Fi 802.11k 配置（Configuration）。

<a id="r_ga4a2b1e8befd7376749b1d4fbcf98376f"></a>

```c
#define NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST)
```

相关声明：[NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a2b1e8befd7376749b1d4fbcf98376f)、[NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)。

请求执行 Wi-Fi 802.11k 邻居请求（Neighbor Request）。

<a id="r_ga68aaced888f98e1ba4e6b61b53e5e2ba"></a>

```c
#define NET_REQUEST_WIFI_PS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS)
```

相关声明：[NET_REQUEST_WIFI_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga68aaced888f98e1ba4e6b61b53e5e2ba)、[NET_REQUEST_WIFI_CMD_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)。

请求 Wi-Fi 省电（Power Save）操作。

<a id="r_gab84fd7e9ca0bf0b2b9d08889dda26aad"></a>

```c
#define NET_REQUEST_WIFI_TWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_TWT)
```

相关声明：[NET_REQUEST_WIFI_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab84fd7e9ca0bf0b2b9d08889dda26aad)、[NET_REQUEST_WIFI_CMD_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)。

请求 Wi-Fi 目标唤醒时间（Target Wake Time，TWT）操作。

<a id="r_gaf1a806a89b0fd20de950c6e085351134"></a>

```c
#define NET_REQUEST_WIFI_BTWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTWT)
```

相关声明：[NET_REQUEST_WIFI_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1a806a89b0fd20de950c6e085351134)、[NET_REQUEST_WIFI_CMD_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)。

请求建立 Wi-Fi 广播目标唤醒时间流（Broadcast TWT Flow Setup）。

<a id="r_ga1032f3773cfe6130da4d4d498b044ee2"></a>

```c
#define NET_REQUEST_WIFI_PS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1032f3773cfe6130da4d4d498b044ee2)、[NET_REQUEST_WIFI_CMD_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)。

请求 Wi-Fi 省电配置（Power Save Configuration）。

<a id="r_ga2b27d102b779a6d846b375854768fb7f"></a>

```c
#define NET_REQUEST_WIFI_REG_DOMAIN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_REG_DOMAIN)
```

相关声明：[NET_REQUEST_WIFI_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2b27d102b779a6d846b375854768fb7f)、[NET_REQUEST_WIFI_CMD_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)。

请求 Wi-Fi 监管域（Regulatory Domain）。

<a id="r_ga9b4da60a8108b0cc431ac1eecfca0cd0"></a>

```c
#define NET_REQUEST_WIFI_MODE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_MODE)
```

相关声明：[NET_REQUEST_WIFI_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9b4da60a8108b0cc431ac1eecfca0cd0)、[NET_REQUEST_WIFI_CMD_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)。

请求当前 Wi-Fi 模式（Mode）。

<a id="r_ga3098e817d12bf4619c9fd2698508fb4e"></a>

```c
#define NET_REQUEST_WIFI_PACKET_FILTER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PACKET_FILTER)
```

相关声明：[NET_REQUEST_WIFI_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3098e817d12bf4619c9fd2698508fb4e)、[NET_REQUEST_WIFI_CMD_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)。

请求 Wi-Fi 分组过滤器（Packet Filter）。

<a id="r_gad9614d2368f8399850aaec05e40bdc78"></a>

```c
#define NET_REQUEST_WIFI_CHANNEL (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CHANNEL)
```

相关声明：[NET_REQUEST_WIFI_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad9614d2368f8399850aaec05e40bdc78)、[NET_REQUEST_WIFI_CMD_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)。

请求 Wi-Fi 信道（Channel）。

<a id="r_gaa3e52e08d89a1104f07207e52b81d503"></a>

```c
#define NET_REQUEST_WIFI_AP_STA_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT)
```

相关声明：[NET_REQUEST_WIFI_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa3e52e08d89a1104f07207e52b81d503)、[NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)。

请求 Wi-Fi 接入点（AP）断开某个站点（Station）的连接。

<a id="r_ga3e60c29ca9ce95d17a7fff087290f7f1"></a>

```c
#define NET_REQUEST_WIFI_VERSION (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_VERSION)
```

相关声明：[NET_REQUEST_WIFI_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e60c29ca9ce95d17a7fff087290f7f1)、[NET_REQUEST_WIFI_CMD_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)。

请求 Wi-Fi 版本（Version）。

<a id="r_gac6483341435ff380a2d4a69430899c1a"></a>

```c
#define NET_REQUEST_WIFI_CONN_PARAMS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONN_PARAMS)
```

相关声明：[NET_REQUEST_WIFI_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac6483341435ff380a2d4a69430899c1a)、[NET_REQUEST_WIFI_CMD_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)。

请求 Wi-Fi 连接参数（Connection Parameters）。

<a id="r_ga22d80ef0ffb15e4286d7b1c3325d5334"></a>

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD)
```

相关声明：[NET_REQUEST_WIFI_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22d80ef0ffb15e4286d7b1c3325d5334)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)。

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_gaf4a78d230f5e0743a6aaf152ddda1c67"></a>

```c
#define NET_REQUEST_WIFI_AP_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM)
```

相关声明：[NET_REQUEST_WIFI_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf4a78d230f5e0743a6aaf152ddda1c67)、[NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)。

请求配置 Wi-Fi 接入点参数（AP Parameters）。

<a id="r_ga4d9dbfcf719df5639a0d592b4b8d4322"></a>

```c
#define NET_REQUEST_WIFI_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONFIG_PARAM)
```

相关声明：[NET_REQUEST_WIFI_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d9dbfcf719df5639a0d592b4b8d4322)、[NET_REQUEST_WIFI_CMD_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)。

请求配置 Wi-Fi 站点参数（STA Parameters）。

<a id="r_ga4f644b4c980628ffd556458eddc0933d"></a>

```c
#define NET_REQUEST_WIFI_BTM_QUERY (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTM_QUERY)
```

相关声明：[NET_REQUEST_WIFI_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4f644b4c980628ffd556458eddc0933d)、[NET_REQUEST_WIFI_CMD_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)。

请求 Wi-Fi 基本服务集转换管理查询（BSS Transition Management，BTM Query）。

<a id="r_ga9070995249eb35de37e2b60c4426f840"></a>

```c
#define NET_REQUEST_WIFI_PMKSA_FLUSH (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PMKSA_FLUSH)
```

相关声明：[NET_REQUEST_WIFI_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9070995249eb35de37e2b60c4426f840)、[NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)。

请求清空 Wi-Fi 成对主密钥安全关联缓存条目（PMKSA Cache Entries）。

<a id="r_gae5dc7835e11487187663dfe65a15f22b"></a>

```c
#define NET_REQUEST_WIFI_ENTERPRISE_CREDS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS)
```

相关声明：[NET_REQUEST_WIFI_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae5dc7835e11487187663dfe65a15f22b)、[NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)。

设置 Wi‑Fi 企业模式的 CA／客户端证书及密钥（CA/client certificate and key）。

<a id="r_ga2678ea372335af008d9bd3333f7a7de1"></a>

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2678ea372335af008d9bd3333f7a7de1)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)。

请求配置 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_ga649a63bc7d315ebdd89464ff48b3fada"></a>

```c
#define NET_REQUEST_WIFI_WPS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_WPS_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga649a63bc7d315ebdd89464ff48b3fada)、[NET_REQUEST_WIFI_CMD_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)。

请求 Wi-Fi 保护设置配置（Wi-Fi Protected Setup，WPS Configuration）。

<a id="r_ga89cc123bb5c30140d2ce0a8b741b1086"></a>

```c
#define NET_REQUEST_WIFI_START_ROAMING (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_START_ROAMING)
```

相关声明：[NET_REQUEST_WIFI_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga89cc123bb5c30140d2ce0a8b741b1086)、[NET_REQUEST_WIFI_CMD_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)。

请求开始 Wi-Fi 漫游（Roaming）。

<a id="r_ga373031970a29331bf1b30d1654c128f0"></a>

```c
#define NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

相关声明：[NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga373031970a29331bf1b30d1654c128f0)、[NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)。

通知 Wi-Fi 邻居报告（Neighbor Report）处理完成。

<a id="r_ga36992c3098d2a1e87f31a18ce369bcc8"></a>

```c
#define NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD)
```

相关声明：[NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga36992c3098d2a1e87f31a18ce369bcc8)、[NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)。

请求配置 Wi-Fi 基本服务集最大空闲周期（BSS Maximum Idle Period）。

<a id="r_ga9d407a15b9804aea6673d603aec9f0e9"></a>

```c
#define NET_REQUEST_WIFI_BGSCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BGSCAN)
```

相关声明：[NET_REQUEST_WIFI_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9d407a15b9804aea6673d603aec9f0e9)、[NET_REQUEST_WIFI_CMD_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)。

请求 Wi-Fi 后台扫描配置（Background Scan Configuration）。

<a id="r_ga4b3de0f402a8f0012ea65c4ab50d2761"></a>

```c
#define NET_REQUEST_WIFI_P2P_OPER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_P2P_OPER)
```

相关声明：[NET_REQUEST_WIFI_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4b3de0f402a8f0012ea65c4ab50d2761)、[NET_REQUEST_WIFI_CMD_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)。

请求 Wi-Fi 直连操作（Wi-Fi Direct，P2P）。

<a id="r_ga436a927d47eb9abe683b89f2b128cd6e"></a>

```c
#define NET_EVENT_WIFI_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_RESULT)
```

相关声明：[NET_EVENT_WIFI_SCAN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga436a927d47eb9abe683b89f2b128cd6e)。

报告 Wi-Fi 扫描结果（Scan Result）时发出的事件。

<a id="r_ga8ce35a12e5338e9a65970382b4a26b88"></a>

```c
#define NET_EVENT_WIFI_SCAN_DONE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_DONE)
```

相关声明：[NET_EVENT_WIFI_SCAN_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8ce35a12e5338e9a65970382b4a26b88)。

Wi-Fi 扫描完成（Scan Done）时发出的事件。

<a id="r_ga0e8feafcc5efd85d04be91f407c0b7c4"></a>

```c
#define NET_EVENT_WIFI_CONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_CONNECT_RESULT)
```

相关声明：[NET_EVENT_WIFI_CONNECT_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0e8feafcc5efd85d04be91f407c0b7c4)。

报告 Wi-Fi 连接结果（Connect Result）时发出的事件。

<a id="r_ga8cbbe69bd60f42fdbb06f4f1e15410c8"></a>

```c
#define NET_EVENT_WIFI_DISCONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_RESULT)
```

相关声明：[NET_EVENT_WIFI_DISCONNECT_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8cbbe69bd60f42fdbb06f4f1e15410c8)。

报告 Wi-Fi 断开连接结果（Disconnect Result）时发出的事件。

<a id="r_ga99e11fc15582b94d4243de7733e47ebb"></a>

```c
#define NET_EVENT_WIFI_IFACE_STATUS (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_IFACE_STATUS)
```

相关声明：[NET_EVENT_WIFI_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga99e11fc15582b94d4243de7733e47ebb)。

报告 Wi-Fi 网络接口状态（Network Interface Status）时发出的事件。

<a id="r_gaeb968a5d2a8d68a8c634cca18dbcf9c6"></a>

```c
#define NET_EVENT_WIFI_TWT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT)
```

相关声明：[NET_EVENT_WIFI_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaeb968a5d2a8d68a8c634cca18dbcf9c6)。

报告 Wi-Fi 目标唤醒时间信息（TWT Information）时发出的事件。

<a id="r_ga682d95b5d06a9b175c10d712acca8a49"></a>

```c
#define NET_EVENT_WIFI_TWT_SLEEP_STATE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE)
```

相关声明：[NET_EVENT_WIFI_TWT_SLEEP_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga682d95b5d06a9b175c10d712acca8a49)。

报告 Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep State）时发出的事件。

<a id="r_gaea8d222282ddef6992330763afc759a4"></a>

```c
#define NET_EVENT_WIFI_RAW_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT)
```

相关声明：[NET_EVENT_WIFI_RAW_SCAN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaea8d222282ddef6992330763afc759a4)。

报告 Wi-Fi 原始扫描结果（Raw Scan Result）时发出的事件。

<a id="r_ga40027feb7ec42c846fd99b56bbd2256d"></a>

```c
#define NET_EVENT_WIFI_DISCONNECT_COMPLETE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE)
```

相关声明：[NET_EVENT_WIFI_DISCONNECT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga40027feb7ec42c846fd99b56bbd2256d)。

Wi-Fi 断开连接完成（Disconnect Completed）时发出的事件。

<a id="r_ga8da47e9d3e594840fb7a7d59f45ea9ce"></a>

```c
#define NET_EVENT_WIFI_SIGNAL_CHANGE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SIGNAL_CHANGE)
```

相关声明：[NET_EVENT_WIFI_SIGNAL_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8da47e9d3e594840fb7a7d59f45ea9ce)。

已连接接入点（AP）的信号变化事件（Signal Change）。

<a id="r_ga7ed4bc9f25055f5a35270a4c6a0bedcc"></a>

```c
#define NET_EVENT_WIFI_NEIGHBOR_REP_COMP (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

相关声明：[NET_EVENT_WIFI_NEIGHBOR_REP_COMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ed4bc9f25055f5a35270a4c6a0bedcc)。

邻居报告完成事件（Neighbor Report Completed）。

<a id="r_ga1d678fbae0f092814392c0ab4087cb73"></a>

```c
#define NET_EVENT_WIFI_AP_ENABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT)
```

相关声明：[NET_EVENT_WIFI_AP_ENABLE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1d678fbae0f092814392c0ab4087cb73)。

报告 Wi-Fi 接入点启用结果（AP Enable Result）时发出的事件。

<a id="r_ga104296fdb38edf868bea1a46f572d101"></a>

```c
#define NET_EVENT_WIFI_AP_DISABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT)
```

相关声明：[NET_EVENT_WIFI_AP_DISABLE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga104296fdb38edf868bea1a46f572d101)。

报告 Wi-Fi 接入点禁用结果（AP Disable Result）时发出的事件。

<a id="r_gacc392179948bfd5bed6702dc8fb5cd9d"></a>

```c
#define NET_EVENT_WIFI_AP_STA_CONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_CONNECTED)
```

相关声明：[NET_EVENT_WIFI_AP_STA_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gacc392179948bfd5bed6702dc8fb5cd9d)。

接入点模式（AP Mode）下，Wi-Fi 站点（Station）连接成功时发出的事件。

<a id="r_ga3e8154ce1808665dd165f793ddec1673"></a>

```c
#define NET_EVENT_WIFI_AP_STA_DISCONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED)
```

相关声明：[NET_EVENT_WIFI_AP_STA_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e8154ce1808665dd165f793ddec1673)。

Wi-Fi 站点（Station）与接入点（AP）断开连接时发出的事件。

<a id="r_gadfcff8ac6645c5b6b8645c1612ad4e3a"></a>

```c
#define NET_EVENT_WIFI_P2P_DEVICE_FOUND (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND)
```

相关声明：[NET_EVENT_WIFI_P2P_DEVICE_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadfcff8ac6645c5b6b8645c1612ad4e3a)。

发现 P2P 设备（P2P Device Found）时发出的事件。

<a id="r_ga38d92ba342887e46c957b820d89a7a20"></a>

```c
#define WIFI_BTWT_AGREEMENT_MAX 5
```

相关声明：[WIFI_BTWT_AGREEMENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38d92ba342887e46c957b820d89a7a20)。

广播目标唤醒时间协定集（Broadcast TWT Agreement Sets）的最大数量。

<a id="r_ga3a6bfa37bd7850342279d304df20977d"></a>

```c
#define MAX_REG_CHAN_NUM 42
```

相关声明：[MAX_REG_CHAN_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3a6bfa37bd7850342279d304df20977d)。

最大监管信道数量（Max Regulatory Channel Number）。

<a id="r_ga234d72d7c881e67ff49fb6c474c622e3"></a>

```c
#define WIFI_WPS_PIN_MAX_LEN 8
```

相关声明：[WIFI_WPS_PIN_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga234d72d7c881e67ff49fb6c474c622e3)。

Wi-Fi 保护设置个人识别码（WPS PIN）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_gad34b366f1c315207ce0da587ca96d8d8"></a>

```c
typedef void(* scan_result_cb_t) (struct net_if *iface, int status, struct wifi_scan_result *entry)
```

相关声明：[scan_result_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad34b366f1c315207ce0da587ca96d8d8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_scan_result](../network_core_model_reference/P186_wifi_scan_result_结构体.md)。

扫描结果回调（Scan Result Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_ga99a55137188119f65f9d2bb4f57cac77"></a>

```c
enum net_request_wifi_cmd { NET_REQUEST_WIFI_CMD_SCAN = 1 , NET_REQUEST_WIFI_CMD_CONNECT , NET_REQUEST_WIFI_CMD_DISCONNECT , NET_REQUEST_WIFI_CMD_AP_ENABLE , NET_REQUEST_WIFI_CMD_AP_DISABLE , NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD , NET_REQUEST_WIFI_CMD_IFACE_STATUS , NET_REQUEST_WIFI_CMD_11K_CONFIG , NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST , NET_REQUEST_WIFI_CMD_PS , NET_REQUEST_WIFI_CMD_TWT , NET_REQUEST_WIFI_CMD_BTWT , NET_REQUEST_WIFI_CMD_PS_CONFIG , NET_REQUEST_WIFI_CMD_REG_DOMAIN , NET_REQUEST_WIFI_CMD_MODE , NET_REQUEST_WIFI_CMD_PACKET_FILTER , NET_REQUEST_WIFI_CMD_CHANNEL , NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT , NET_REQUEST_WIFI_CMD_VERSION , NET_REQUEST_WIFI_CMD_CONN_PARAMS , NET_REQUEST_WIFI_CMD_RTS_THRESHOLD , NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM , NET_REQUEST_WIFI_CMD_CONFIG_PARAM , NET_REQUEST_WIFI_CMD_DPP , NET_REQUEST_WIFI_CMD_NAN , NET_REQUEST_WIFI_CMD_BTM_QUERY , NET_REQUEST_WIFI_CMD_PMKSA_FLUSH , NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS , NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG , NET_REQUEST_WIFI_CMD_WPS_CONFIG , NET_REQUEST_WIFI_CMD_START_ROAMING , NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE , NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN , NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG , NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD , NET_REQUEST_WIFI_CMD_BGSCAN , NET_REQUEST_WIFI_CMD_P2P_OPER }
```

相关声明：[net_request_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga99a55137188119f65f9d2bb4f57cac77)、[NET_REQUEST_WIFI_CMD_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)、[NET_REQUEST_WIFI_CMD_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)、[NET_REQUEST_WIFI_CMD_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)、[NET_REQUEST_WIFI_CMD_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)、[NET_REQUEST_WIFI_CMD_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)、[NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)、[NET_REQUEST_WIFI_CMD_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)、[NET_REQUEST_WIFI_CMD_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)、[NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)、[NET_REQUEST_WIFI_CMD_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)、[NET_REQUEST_WIFI_CMD_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)、[NET_REQUEST_WIFI_CMD_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)、[NET_REQUEST_WIFI_CMD_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)、[NET_REQUEST_WIFI_CMD_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)、[NET_REQUEST_WIFI_CMD_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)、[NET_REQUEST_WIFI_CMD_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)、[NET_REQUEST_WIFI_CMD_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)、[NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)、[NET_REQUEST_WIFI_CMD_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)、[NET_REQUEST_WIFI_CMD_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)、[NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)、[NET_REQUEST_WIFI_CMD_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)、[NET_REQUEST_WIFI_CMD_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)、[NET_REQUEST_WIFI_CMD_NAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e)、[NET_REQUEST_WIFI_CMD_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)、[NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)、[NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)、[NET_REQUEST_WIFI_CMD_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)、[NET_REQUEST_WIFI_CMD_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)、[NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)、[NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)、[NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413)、[NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)、[NET_REQUEST_WIFI_CMD_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)、[NET_REQUEST_WIFI_CMD_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)。

Wi-Fi 管理命令（Management Commands）。

<a id="r_gac2638308cbb0d268831f1618cf8e1fa8"></a>

```c
enum net_event_wifi_cmd { NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) }
```

相关声明：[net_event_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac2638308cbb0d268831f1618cf8e1fa8)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)。

Wi-Fi 管理事件（Management Events）。

<a id="r_gac782af0a60b202fd19597cabb7bd3a9a"></a>

```c
enum wifi_disconn_reason { WIFI_REASON_DISCONN_SUCCESS = 0 , WIFI_REASON_DISCONN_UNSPECIFIED , WIFI_REASON_DISCONN_USER_REQUEST , WIFI_REASON_DISCONN_AP_LEAVING , WIFI_REASON_DISCONN_INACTIVITY }
```

相关声明：[wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)、[WIFI_REASON_DISCONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)、[WIFI_REASON_DISCONN_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)、[WIFI_REASON_DISCONN_USER_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)、[WIFI_REASON_DISCONN_AP_LEAVING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)、[WIFI_REASON_DISCONN_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)。

Wi-Fi 断开连接原因码（Disconnect Reason Codes）。

<a id="r_gaaf730bf76adc06434c7ac63bf0417884"></a>

```c
enum wifi_ap_status { WIFI_STATUS_AP_SUCCESS = 0 , WIFI_STATUS_AP_FAIL , WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED , WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED , WIFI_STATUS_AP_SSID_NOT_ALLOWED , WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED , WIFI_STATUS_AP_OP_NOT_SUPPORTED , WIFI_STATUS_AP_OP_NOT_PERMITTED }
```

相关声明：[wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)、[WIFI_STATUS_AP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)、[WIFI_STATUS_AP_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)、[WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)、[WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)、[WIFI_STATUS_AP_SSID_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)、[WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)、[WIFI_STATUS_AP_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)、[WIFI_STATUS_AP_OP_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)。

Wi-Fi 接入点模式结果码（AP Mode Result Codes）。

<a id="r_gae129d0783276e662575af2314eef86cd"></a>

```c
enum wifi_mgmt_op { WIFI_MGMT_GET = 0 , WIFI_MGMT_SET = 1 }
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[WIFI_MGMT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)、[WIFI_MGMT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)。

用于任意命令的通用获取／设置操作（Get/Set Operation）。

<a id="r_ga38c184ea35c02f304cccdf389ca6d552"></a>

```c
enum wifi_twt_sleep_state { WIFI_TWT_STATE_SLEEP = 0 , WIFI_TWT_STATE_AWAKE = 1 }
```

相关声明：[wifi_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38c184ea35c02f304cccdf389ca6d552)、[WIFI_TWT_STATE_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)、[WIFI_TWT_STATE_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)。

Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep States）。

<a id="r_ga4c36ae1a5171d3fbaeebf95c16be496d"></a>

```c
enum wifi_wps_op { WIFI_WPS_PBC = 0 , WIFI_WPS_PIN_GET = 1 , WIFI_WPS_PIN_SET = 2 }
```

相关声明：[wifi_wps_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c36ae1a5171d3fbaeebf95c16be496d)、[WIFI_WPS_PBC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)、[WIFI_WPS_PIN_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)、[WIFI_WPS_PIN_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)。

Wi-Fi 保护设置操作（WPS Operation）。

<a id="r_ga0cc87c00cbee0d0aca833119dbf0d74e"></a>

```c
enum wifi_sap_iface_state { WIFI_SAP_IFACE_UNINITIALIZED , WIFI_SAP_IFACE_DISABLED , WIFI_SAP_IFACE_COUNTRY_UPDATE , WIFI_SAP_IFACE_ACS , WIFI_SAP_IFACE_HT_SCAN , WIFI_SAP_IFACE_DFS , WIFI_SAP_IFACE_NO_IR , WIFI_SAP_IFACE_ENABLED }
```

相关声明：[wifi_sap_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0cc87c00cbee0d0aca833119dbf0d74e)、[WIFI_SAP_IFACE_UNINITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)、[WIFI_SAP_IFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)、[WIFI_SAP_IFACE_COUNTRY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)、[WIFI_SAP_IFACE_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)、[WIFI_SAP_IFACE_HT_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)、[WIFI_SAP_IFACE_DFS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)、[WIFI_SAP_IFACE_NO_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)、[WIFI_SAP_IFACE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)。

Wi-Fi 接入点状态（AP Status）。

<a id="r_gaacc27e95277622f56ef35e129aaac4d0"></a>

```c
enum wifi_bgscan_type { WIFI_BGSCAN_NONE = 0 , WIFI_BGSCAN_SIMPLE , WIFI_BGSCAN_LEARN }
```

相关声明：[wifi_bgscan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc27e95277622f56ef35e129aaac4d0)、[WIFI_BGSCAN_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9)、[WIFI_BGSCAN_SIMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe)、[WIFI_BGSCAN_LEARN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911)。

Wi-Fi 后台扫描实现（Background Scan Implementation）。

<a id="r_ga03ab29789adfe867c4ebaddc39482344"></a>

```c
enum wifi_ext_capab { WIFI_EXT_CAPAB_20_40_COEX = 0 , WIFI_EXT_CAPAB_GLK = 1 , WIFI_EXT_CAPAB_EXT_CHAN_SWITCH = 2 , WIFI_EXT_CAPAB_TIM_BROADCAST = 18 , WIFI_EXT_CAPAB_BSS_TRANSITION = 19 }
```

相关声明：[wifi_ext_capab](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03ab29789adfe867c4ebaddc39482344)、[WIFI_EXT_CAPAB_20_40_COEX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)、[WIFI_EXT_CAPAB_GLK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)、[WIFI_EXT_CAPAB_EXT_CHAN_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)、[WIFI_EXT_CAPAB_TIM_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)、[WIFI_EXT_CAPAB_BSS_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)。

IEEE 802.11 扩展能力（Extended Capabilities）的位位置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga1bea051b0c184cb859f27b36e3593bf2"></a>

```c
const char * wifi_disconn_reason_txt (enum wifi_disconn_reason reason)
```

相关声明：[wifi_disconn_reason_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1bea051b0c184cb859f27b36e3593bf2)、[wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)。

用于获取易读的断开连接原因名称（Disconnect Reason Name）的辅助函数。

<a id="r_ga036416696b1e3bc458ddbaf07a08d69d"></a>

```c
void wifi_mgmt_raise_connect_result_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_connect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga036416696b1e3bc458ddbaf07a08d69d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理连接结果事件（Connect Result Event）。

<a id="r_gabdf7753c247587eface6e829686d120c"></a>

```c
void wifi_mgmt_raise_connect_result_status_event (struct net_if *iface, const struct wifi_status *status)
```

相关声明：[wifi_mgmt_raise_connect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdf7753c247587eface6e829686d120c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)。

带 IEEE 802.11 代码的 Wi-Fi 管理连接结果事件（Connect Result Event）。

<a id="r_ga3b6edcf9b51afbf7a327d1a344bd7b87"></a>

```c
void wifi_mgmt_raise_disconnect_result_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_disconnect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b6edcf9b51afbf7a327d1a344bd7b87)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

<a id="r_ga3f7c4f252ab9621fbf3b9bd937253858"></a>

```c
void wifi_mgmt_raise_disconnect_result_status_event (struct net_if *iface, const struct wifi_status *status)
```

相关声明：[wifi_mgmt_raise_disconnect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3f7c4f252ab9621fbf3b9bd937253858)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)。

带 IEEE 802.11 代码的 Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

<a id="r_ga7da6af0747bcba85f8afab30c92b5b43"></a>

```c
void wifi_mgmt_raise_iface_status_event (struct net_if *iface, struct wifi_iface_status *iface_status)
```

相关声明：[wifi_mgmt_raise_iface_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7da6af0747bcba85f8afab30c92b5b43)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_iface_status](../network_core_model_reference/P175_wifi_iface_status_结构体.md)。

Wi-Fi 管理接口状态事件（Interface Status Event）。

<a id="r_ga39404d15243ca084b253cae8fc07e374"></a>

```c
void wifi_mgmt_raise_twt_event (struct net_if *iface, struct wifi_twt_params *twt_params)
```

相关声明：[wifi_mgmt_raise_twt_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga39404d15243ca084b253cae8fc07e374)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_twt_params](../network_core_model_reference/P189_wifi_twt_params_结构体.md)。

Wi-Fi 管理目标唤醒时间事件（TWT Event）。

<a id="r_ga18f09a3196588b51d6c0644f82f639d7"></a>

```c
void wifi_mgmt_raise_twt_sleep_state (struct net_if *iface, int twt_sleep_state)
```

相关声明：[wifi_mgmt_raise_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga18f09a3196588b51d6c0644f82f639d7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理目标唤醒时间睡眠状态事件（TWT Sleep State Event）。

<a id="r_ga71c99913bded844c4ca32ed9155bc470"></a>

```c
void wifi_mgmt_raise_raw_scan_result_event (struct net_if *iface, struct wifi_raw_scan_result *raw_scan_info)
```

相关声明：[wifi_mgmt_raise_raw_scan_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga71c99913bded844c4ca32ed9155bc470)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_raw_scan_result](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md)。

Wi-Fi 管理原始扫描结果事件（Raw Scan Result Event）。

<a id="r_gaa75246d6dc55dada389c9d31e2607d5c"></a>

```c
void wifi_mgmt_raise_disconnect_complete_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_disconnect_complete_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa75246d6dc55dada389c9d31e2607d5c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理断开连接完成事件（Disconnect Complete Event）。

<a id="r_ga67b52edeff76c2211b038f4aa90b8982"></a>

```c
void wifi_mgmt_raise_ap_enable_result_event (struct net_if *iface, enum wifi_ap_status status)
```

相关声明：[wifi_mgmt_raise_ap_enable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga67b52edeff76c2211b038f4aa90b8982)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)。

Wi-Fi 管理接入点模式启用结果事件（AP Mode Enable Result Event）。

<a id="r_gadee15c6a492a8ee13bea43812debb5d9"></a>

```c
void wifi_mgmt_raise_ap_disable_result_event (struct net_if *iface, enum wifi_ap_status status)
```

相关声明：[wifi_mgmt_raise_ap_disable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadee15c6a492a8ee13bea43812debb5d9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)。

Wi-Fi 管理接入点模式禁用结果事件（AP Mode Disable Result Event）。

<a id="r_gac8f17f0aa3e426a5cdb731727b9b9ce3"></a>

```c
void wifi_mgmt_raise_ap_sta_connected_event (struct net_if *iface, struct wifi_ap_sta_info *sta_info)
```

相关声明：[wifi_mgmt_raise_ap_sta_connected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac8f17f0aa3e426a5cdb731727b9b9ce3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)。

Wi-Fi 管理接入点模式站点已连接事件（AP Mode STA Connected Event）。

<a id="r_ga49fb9c3908be61d847b31c99be6afc42"></a>

```c
void wifi_mgmt_raise_ap_sta_disconnected_event (struct net_if *iface, struct wifi_ap_sta_info *sta_info)
```

相关声明：[wifi_mgmt_raise_ap_sta_disconnected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga49fb9c3908be61d847b31c99be6afc42)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)。

Wi-Fi 管理接入点模式站点已断开事件（AP Mode STA Disconnected Event）。


## 9.6\_原页交叉引用（Cross References）

- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [zephyr/net/wifi.h](../api_source_runtime_reference/P067_wifi.h_源码浏览.md)
- [zephyr/net/ethernet.h](../api_source_socket_ethernet_reference/P003_ethernet.h_源码浏览.md)
- [zephyr/net/offloaded_netdev.h](../api_source_supplement_reference/P139_offloaded_netdev.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [查看此文件的源码。](../api_source_http_wifi_reference/P009_wifi_mgmt.h_源码浏览.md)
- [wifi_version](../network_core_model_reference/P190_wifi_version_结构体.md)
- [wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)
- [wifi_scan_params](../network_core_model_reference/P185_wifi_scan_params_结构体.md)
- [wifi_scan_result](../network_core_model_reference/P186_wifi_scan_result_结构体.md)
- [net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)
- [net_mgmt.h](../api_file_storage_event_reference/P015_zephyr__net__net_mgmt.h_文件参考.md)
- [wifi_connect_req_params](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md)
- [wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)
- [wifi_iface_status](../network_core_model_reference/P175_wifi_iface_status_结构体.md)
- [wifi_ps_params](../network_core_model_reference/P181_wifi_ps_params_结构体.md)
- [wifi_btwt_params](../network_core_model_reference/P163_wifi_btwt_params_结构体.md)
- [wifi_twt_params](../network_core_model_reference/P189_wifi_twt_params_结构体.md)
- [wifi_twt_flow_info](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md)
- [wifi_enterprise_creds_params](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md)
- [wifi_ps_config](../network_core_model_reference/P180_wifi_ps_config_结构体.md)
- [wifi_11k_params](../network_core_model_reference/P158_wifi_11k_params_结构体.md)
- [wifi_reg_chan_info](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md)
- [wifi_reg_domain](../network_core_model_reference/P184_wifi_reg_domain_结构体.md)
- [wifi_raw_scan_result](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md)
- [wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)
- [wifi_mode_info](../network_core_model_reference/P177_wifi_mode_info_结构体.md)
- [wifi_filter_info](../network_core_model_reference/P174_wifi_filter_info_结构体.md)
- [wifi_channel_info](../network_core_model_reference/P164_wifi_channel_info_结构体.md)
- [wifi_ap_config_params](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md)
- [wifi_config_params](../network_core_model_reference/P166_wifi_config_params_结构体.md)
- [wifi_wps_config_params](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md)
- [wifi_bgscan_params](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md)
- [wifi_mgmt_ops](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md)
- [net_wifi_mgmt_offload](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md)
- [NET_REQUEST_WIFI_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1c277da90986fa52dca182c4d922646f)
- [NET_REQUEST_WIFI_CMD_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)
- [NET_REQUEST_WIFI_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa7ab2a97950a22736bb69f60b459f0f6)
- [NET_REQUEST_WIFI_CMD_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)
- [NET_REQUEST_WIFI_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga90afd8d4e83056463ec6e667ed8ea60a)
- [NET_REQUEST_WIFI_CMD_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)
- [NET_REQUEST_WIFI_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga638d2eb0a5029c1af46a91b523ed8589)
- [NET_REQUEST_WIFI_CMD_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)
- [NET_REQUEST_WIFI_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf81f62bf4c9e331a095acbf0d24ca1a2)
- [NET_REQUEST_WIFI_CMD_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)
- [NET_REQUEST_WIFI_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9918582d4e7bb0952daf993ee34e166d)
- [NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)
- [NET_REQUEST_WIFI_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e45f6ee3801553619d8eb7d0af506eb)
- [NET_REQUEST_WIFI_CMD_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)
- [NET_REQUEST_WIFI_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadd9b5b206c7ee2e40c30a37c7b4fc002)
- [NET_REQUEST_WIFI_CMD_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)
- [NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a2b1e8befd7376749b1d4fbcf98376f)
- [NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)
- [NET_REQUEST_WIFI_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga68aaced888f98e1ba4e6b61b53e5e2ba)
- [NET_REQUEST_WIFI_CMD_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)
- [NET_REQUEST_WIFI_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab84fd7e9ca0bf0b2b9d08889dda26aad)
- [NET_REQUEST_WIFI_CMD_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)
- [NET_REQUEST_WIFI_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1a806a89b0fd20de950c6e085351134)
- [NET_REQUEST_WIFI_CMD_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)
- [NET_REQUEST_WIFI_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1032f3773cfe6130da4d4d498b044ee2)
- [NET_REQUEST_WIFI_CMD_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)
- [NET_REQUEST_WIFI_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2b27d102b779a6d846b375854768fb7f)
- [NET_REQUEST_WIFI_CMD_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)
- [NET_REQUEST_WIFI_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9b4da60a8108b0cc431ac1eecfca0cd0)
- [NET_REQUEST_WIFI_CMD_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)
- [NET_REQUEST_WIFI_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3098e817d12bf4619c9fd2698508fb4e)
- [NET_REQUEST_WIFI_CMD_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)
- [NET_REQUEST_WIFI_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad9614d2368f8399850aaec05e40bdc78)
- [NET_REQUEST_WIFI_CMD_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)
- [NET_REQUEST_WIFI_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa3e52e08d89a1104f07207e52b81d503)
- [NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)
- [NET_REQUEST_WIFI_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e60c29ca9ce95d17a7fff087290f7f1)
- [NET_REQUEST_WIFI_CMD_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)
- [NET_REQUEST_WIFI_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac6483341435ff380a2d4a69430899c1a)
- [NET_REQUEST_WIFI_CMD_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)
- [NET_REQUEST_WIFI_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22d80ef0ffb15e4286d7b1c3325d5334)
- [NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)
- [NET_REQUEST_WIFI_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf4a78d230f5e0743a6aaf152ddda1c67)
- [NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)
- [NET_REQUEST_WIFI_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d9dbfcf719df5639a0d592b4b8d4322)
- [NET_REQUEST_WIFI_CMD_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)
- [NET_REQUEST_WIFI_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4f644b4c980628ffd556458eddc0933d)
- [NET_REQUEST_WIFI_CMD_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)
- [NET_REQUEST_WIFI_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9070995249eb35de37e2b60c4426f840)
- [NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)
- [NET_REQUEST_WIFI_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae5dc7835e11487187663dfe65a15f22b)
- [NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)
- [NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2678ea372335af008d9bd3333f7a7de1)
- [NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)
- [NET_REQUEST_WIFI_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga649a63bc7d315ebdd89464ff48b3fada)
- [NET_REQUEST_WIFI_CMD_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)
- [NET_REQUEST_WIFI_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga89cc123bb5c30140d2ce0a8b741b1086)
- [NET_REQUEST_WIFI_CMD_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)
- [NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga373031970a29331bf1b30d1654c128f0)
- [NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)
- [NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga36992c3098d2a1e87f31a18ce369bcc8)
- [NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)
- [NET_REQUEST_WIFI_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9d407a15b9804aea6673d603aec9f0e9)
- [NET_REQUEST_WIFI_CMD_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)
- [NET_REQUEST_WIFI_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4b3de0f402a8f0012ea65c4ab50d2761)
- [NET_REQUEST_WIFI_CMD_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)
- [NET_EVENT_WIFI_SCAN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga436a927d47eb9abe683b89f2b128cd6e)
- [NET_EVENT_WIFI_SCAN_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8ce35a12e5338e9a65970382b4a26b88)
- [NET_EVENT_WIFI_CONNECT_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0e8feafcc5efd85d04be91f407c0b7c4)
- [NET_EVENT_WIFI_DISCONNECT_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8cbbe69bd60f42fdbb06f4f1e15410c8)
- [NET_EVENT_WIFI_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga99e11fc15582b94d4243de7733e47ebb)
- [NET_EVENT_WIFI_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaeb968a5d2a8d68a8c634cca18dbcf9c6)
- [NET_EVENT_WIFI_TWT_SLEEP_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga682d95b5d06a9b175c10d712acca8a49)
- [NET_EVENT_WIFI_RAW_SCAN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaea8d222282ddef6992330763afc759a4)
- [NET_EVENT_WIFI_DISCONNECT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga40027feb7ec42c846fd99b56bbd2256d)
- [NET_EVENT_WIFI_SIGNAL_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8da47e9d3e594840fb7a7d59f45ea9ce)
- [NET_EVENT_WIFI_NEIGHBOR_REP_COMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ed4bc9f25055f5a35270a4c6a0bedcc)
- [NET_EVENT_WIFI_AP_ENABLE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1d678fbae0f092814392c0ab4087cb73)
- [NET_EVENT_WIFI_AP_DISABLE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga104296fdb38edf868bea1a46f572d101)
- [NET_EVENT_WIFI_AP_STA_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gacc392179948bfd5bed6702dc8fb5cd9d)
- [NET_EVENT_WIFI_AP_STA_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e8154ce1808665dd165f793ddec1673)
- [NET_EVENT_WIFI_P2P_DEVICE_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadfcff8ac6645c5b6b8645c1612ad4e3a)
- [WIFI_BTWT_AGREEMENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38d92ba342887e46c957b820d89a7a20)
- [MAX_REG_CHAN_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3a6bfa37bd7850342279d304df20977d)
- [WIFI_WPS_PIN_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga234d72d7c881e67ff49fb6c474c622e3)
- [scan_result_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad34b366f1c315207ce0da587ca96d8d8)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_request_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga99a55137188119f65f9d2bb4f57cac77)
- [NET_REQUEST_WIFI_CMD_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)
- [NET_REQUEST_WIFI_CMD_NAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e)
- [NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)
- [NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413)
- [net_event_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac2638308cbb0d268831f1618cf8e1fa8)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)
- [WIFI_REASON_DISCONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)
- [WIFI_REASON_DISCONN_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)
- [WIFI_REASON_DISCONN_USER_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)
- [WIFI_REASON_DISCONN_AP_LEAVING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)
- [WIFI_REASON_DISCONN_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)
- [wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)
- [WIFI_STATUS_AP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)
- [WIFI_STATUS_AP_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)
- [WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)
- [WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)
- [WIFI_STATUS_AP_SSID_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)
- [WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)
- [WIFI_STATUS_AP_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)
- [WIFI_STATUS_AP_OP_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)
- [WIFI_MGMT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)
- [WIFI_MGMT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)
- [wifi_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38c184ea35c02f304cccdf389ca6d552)
- [WIFI_TWT_STATE_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)
- [WIFI_TWT_STATE_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)
- [wifi_wps_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c36ae1a5171d3fbaeebf95c16be496d)
- [WIFI_WPS_PBC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)
- [WIFI_WPS_PIN_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)
- [WIFI_WPS_PIN_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)
- [wifi_sap_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0cc87c00cbee0d0aca833119dbf0d74e)
- [WIFI_SAP_IFACE_UNINITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)
- [WIFI_SAP_IFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)
- [WIFI_SAP_IFACE_COUNTRY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)
- [WIFI_SAP_IFACE_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)
- [WIFI_SAP_IFACE_HT_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)
- [WIFI_SAP_IFACE_DFS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)
- [WIFI_SAP_IFACE_NO_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)
- [WIFI_SAP_IFACE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)
- [wifi_bgscan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc27e95277622f56ef35e129aaac4d0)
- [WIFI_BGSCAN_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9)
- [WIFI_BGSCAN_SIMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe)
- [WIFI_BGSCAN_LEARN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911)
- [wifi_ext_capab](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03ab29789adfe867c4ebaddc39482344)
- [WIFI_EXT_CAPAB_20_40_COEX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)
- [WIFI_EXT_CAPAB_GLK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)
- [WIFI_EXT_CAPAB_EXT_CHAN_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)
- [WIFI_EXT_CAPAB_TIM_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)
- [WIFI_EXT_CAPAB_BSS_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)
- [wifi_disconn_reason_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1bea051b0c184cb859f27b36e3593bf2)
- [wifi_mgmt_raise_connect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga036416696b1e3bc458ddbaf07a08d69d)
- [wifi_mgmt_raise_connect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdf7753c247587eface6e829686d120c)
- [wifi_mgmt_raise_disconnect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b6edcf9b51afbf7a327d1a344bd7b87)
- [wifi_mgmt_raise_disconnect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3f7c4f252ab9621fbf3b9bd937253858)
- [wifi_mgmt_raise_iface_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7da6af0747bcba85f8afab30c92b5b43)
- [wifi_mgmt_raise_twt_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga39404d15243ca084b253cae8fc07e374)
- [wifi_mgmt_raise_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga18f09a3196588b51d6c0644f82f639d7)
- [wifi_mgmt_raise_raw_scan_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga71c99913bded844c4ca32ed9155bc470)
- [wifi_mgmt_raise_disconnect_complete_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa75246d6dc55dada389c9d31e2607d5c)
- [wifi_mgmt_raise_ap_enable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga67b52edeff76c2211b038f4aa90b8982)
- [wifi_mgmt_raise_ap_disable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadee15c6a492a8ee13bea43812debb5d9)
- [wifi_mgmt_raise_ap_sta_connected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac8f17f0aa3e426a5cdb731727b9b9ce3)
- [wifi_mgmt_raise_ap_sta_disconnected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga49fb9c3908be61d847b31c99be6afc42)

<a id="header-details"></a>

---

[上一章](P008_zephyr__dt-bindings__sensor__qdec_nxp_s32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__wuc__wuc_nxp_llwu.h_文件参考.md)
