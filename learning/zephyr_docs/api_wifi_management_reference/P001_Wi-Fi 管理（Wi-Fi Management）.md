---
id: learning.zephyr-docs.api-wifi-management-reference.page-1
title: Wi-Fi 管理（Wi-Fi Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Wi-Fi 管理（Wi-Fi Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi 管理 API

<a id="details"></a>

Wi-Fi 管理接口（Wi-Fi Management API）。引入版本（Since）：1.12。接口版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_esp_5Fwifi_5Fmesh"></a>

相关声明：[ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）](../api_usb_gnss_topic_reference/P008_ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）.md)。

ESP32 Wi-Fi Mesh API

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_wifi_2Eh"></a>

```c
file wifi.h
```

相关声明：[wifi.h](../api_file_network_pcie_reference/P015_zephyr__net__wifi.h_文件参考.md)。

IEEE 802.11协议与通用Wi-Fi定义。

<a id="r_wifi_5Fcerts_2Eh"></a>

```c
file wifi_certs.h
```

相关声明：[wifi_certs.h](../api_file_network_device_reference/P043_zephyr__net__wifi_certs.h_文件参考.md)。

Wi-Fi企业模式凭据设置（Enterprise Mode Credentials Setup）的API。

<a id="r_wifi_5Fmgmt_2Eh"></a>

```c
file wifi_mgmt.h
```

相关声明：[wifi_mgmt.h](../api_file_mesh_acpi_reference/P009_zephyr__net__wifi_mgmt.h_文件参考.md)。

Wi-Fi第二层协议栈（L2 Stack）的公共头文件。

<a id="r_wifi_5Futils_2Eh"></a>

```c
file wifi_utils.h
```

相关声明：[wifi_utils.h](../api_file_protocol_service_reference/P034_zephyr__net__wifi_utils.h_文件参考.md)。

Wi-Fi子系统（Subsystem）使用的工具函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

<a id="r_wifi_5Fcipher_5Fdesc"></a>

```c
struct wifi_cipher_desc
```

相关声明：[wifi_cipher_desc](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md)。

密码算法能力与名称说明（Cipher Capability and Name Description）。

<a id="r_wifi_5Feap_5Fcipher_5Fconfig"></a>

```c
struct wifi_eap_cipher_config
```

相关声明：[wifi_eap_cipher_config](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md)。

可扩展认证协议（EAP）的密码算法配置。

<a id="r_wifi_5Feap_5Fconfig"></a>

```c
struct wifi_eap_config
```

相关声明：[wifi_eap_config](../network_core_model_reference/P172_wifi_eap_config_结构体.md)。

可扩展认证协议（EAP）的方法配置。

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

## 1.4\_宏定义（Macros）

<a id="r_ga6766ef7bcb001f1fb526a4083b6cd8bc"></a>

```c
#define WIFI_COUNTRY_CODE_LEN 2
```

相关声明：[WIFI_COUNTRY_CODE_LEN](#ga6766ef7bcb001f1fb526a4083b6cd8bc)。

国家代码字符串长度（Country Code String Length）。

<a id="r_gad62c60666c9fdffe2e0e9c4388f87886"></a>

```c
#define WIFI_SSID_MAX_LEN 32
```

相关声明：[WIFI_SSID_MAX_LEN](#gad62c60666c9fdffe2e0e9c4388f87886)。

最大服务集标识符长度（Maximum SSID Length）。

<a id="r_gaa8e19abf8c85f237ba5033740ceff553"></a>

```c
#define WIFI_PSK_MIN_LEN 8
```

相关声明：[WIFI_PSK_MIN_LEN](#gaa8e19abf8c85f237ba5033740ceff553)。

最小预共享密钥长度（Minimum PSK Length）。

<a id="r_gad7c3b99c974b342935180a28fdc5ddfc"></a>

```c
#define WIFI_PSK_MAX_LEN 64
```

相关声明：[WIFI_PSK_MAX_LEN](#gad7c3b99c974b342935180a28fdc5ddfc)。

最大预共享密钥长度（Maximum PSK Length）。

<a id="r_gaf466d0b11462b3f190d579702cb9ee51"></a>

```c
#define WIFI_WEP_KEY_MAX_LEN 26
```

相关声明：[WIFI_WEP_KEY_MAX_LEN](#gaf466d0b11462b3f190d579702cb9ee51)。

最大 WEP 密钥长度（Maximum WEP Key Length）；WEP-104 为 26 个十六进制字符。

<a id="r_ga7d6424d6770b2357f0b8abb456ae53fc"></a>

```c
#define WIFI_PSK_PBKDF2_KEY_LEN 32
```

相关声明：[WIFI_PSK_PBKDF2_KEY_LEN](#ga7d6424d6770b2357f0b8abb456ae53fc)。

PBKDF2 密钥长度（Key Length）。

<a id="r_gab63fa744cc2e049cfd635ab0a187971f"></a>

```c
#define WIFI_SAE_PSWD_MAX_LEN 128
```

相关声明：[WIFI_SAE_PSWD_MAX_LEN](#gab63fa744cc2e049cfd635ab0a187971f)。

最大 SAW 密码长度（Max SAW Password Length，原文写作 SAW）。

<a id="r_ga29409ff83a53c6464decdde9bdd04de6"></a>

```c
#define WIFI_MAC_ADDR_LEN 6
```

相关声明：[WIFI_MAC_ADDR_LEN](#ga29409ff83a53c6464decdde9bdd04de6)。

MAC 地址长度（MAC address length）。

<a id="r_gac6904487661f157274b0b60833f6684a"></a>

```c
#define WIFI_ENT_IDENTITY_MAX_LEN 64
```

相关声明：[WIFI_ENT_IDENTITY_MAX_LEN](#gac6904487661f157274b0b60833f6684a)。

最大企业身份长度（Maximum Enterprise Identity Length）。

<a id="r_gae2fd55924f4078187431f7a1184f217f"></a>

```c
#define WIFI_ENT_PSWD_MAX_LEN 128
```

相关声明：[WIFI_ENT_PSWD_MAX_LEN](#gae2fd55924f4078187431f7a1184f217f)。

最大企业密码长度（Maximum Enterprise Password Length）。

<a id="r_ga260e473dac1e823fd298a2c982470e0b"></a>

```c
#define WIFI_CHANNEL_MIN 1
```

相关声明：[WIFI_CHANNEL_MIN](#ga260e473dac1e823fd298a2c982470e0b)。

最小信道编号（Minimum Channel Number）。

<a id="r_ga8ea9141108f93b419f6a6530bf67bd95"></a>

```c
#define WIFI_CHANNEL_MAX 233
```

相关声明：[WIFI_CHANNEL_MAX](#ga8ea9141108f93b419f6a6530bf67bd95)。

最大信道编号（Maximum Channel Number）。

<a id="r_ga3876cd718af9f8a7b3682546da854544"></a>

```c
#define WIFI_CHANNEL_ANY 255
```

相关声明：[WIFI_CHANNEL_ANY](#ga3876cd718af9f8a7b3682546da854544)。

任意信道编号（Any Channel Number）。

<a id="r_gaa1a74ef94af57a7ea966c691c065a46d"></a>

```c
#define WIFI_INTERFACE_INDEX_MIN 1
```

相关声明：[WIFI_INTERFACE_INDEX_MIN](#gaa1a74ef94af57a7ea966c691c065a46d)。

网络接口索引最小值（Network Interface Index Minimum）。

<a id="r_gaa6cbecd7d4197d453038d3da7ef6be7b"></a>

```c
#define WIFI_INTERFACE_INDEX_MAX 255
```

相关声明：[WIFI_INTERFACE_INDEX_MAX](#gaa6cbecd7d4197d453038d3da7ef6be7b)。

网络接口索引最大值（Network Interface Index Maximum）。

<a id="r_ga1c277da90986fa52dca182c4d922646f"></a>

```c
#define NET_REQUEST_WIFI_SCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_SCAN)
```

相关声明：[NET_REQUEST_WIFI_SCAN](#ga1c277da90986fa52dca182c4d922646f)、[NET_REQUEST_WIFI_CMD_SCAN](#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)。

请求 Wi-Fi 扫描（Scan）。

<a id="r_gaa7ab2a97950a22736bb69f60b459f0f6"></a>

```c
#define NET_REQUEST_WIFI_CONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONNECT)
```

相关声明：[NET_REQUEST_WIFI_CONNECT](#gaa7ab2a97950a22736bb69f60b459f0f6)、[NET_REQUEST_WIFI_CMD_CONNECT](#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)。

请求 Wi-Fi 连接（Connect）。

<a id="r_ga90afd8d4e83056463ec6e667ed8ea60a"></a>

```c
#define NET_REQUEST_WIFI_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_DISCONNECT)
```

相关声明：[NET_REQUEST_WIFI_DISCONNECT](#ga90afd8d4e83056463ec6e667ed8ea60a)、[NET_REQUEST_WIFI_CMD_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)。

请求 Wi-Fi 断开连接（Disconnect）。

<a id="r_ga638d2eb0a5029c1af46a91b523ed8589"></a>

```c
#define NET_REQUEST_WIFI_AP_ENABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_ENABLE)
```

相关声明：[NET_REQUEST_WIFI_AP_ENABLE](#ga638d2eb0a5029c1af46a91b523ed8589)、[NET_REQUEST_WIFI_CMD_AP_ENABLE](#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)。

请求启用 Wi-Fi 接入点（Access Point，AP）。

<a id="r_gaf81f62bf4c9e331a095acbf0d24ca1a2"></a>

```c
#define NET_REQUEST_WIFI_AP_DISABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_DISABLE)
```

相关声明：[NET_REQUEST_WIFI_AP_DISABLE](#gaf81f62bf4c9e331a095acbf0d24ca1a2)、[NET_REQUEST_WIFI_CMD_AP_DISABLE](#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)。

请求禁用 Wi-Fi 接入点（Access Point，AP）。

<a id="r_ga9918582d4e7bb0952daf993ee34e166d"></a>

```c
#define NET_REQUEST_WIFI_AP_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD)
```

相关声明：[NET_REQUEST_WIFI_AP_RTS_THRESHOLD](#ga9918582d4e7bb0952daf993ee34e166d)、[NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)。

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_ga3e45f6ee3801553619d8eb7d0af506eb"></a>

```c
#define NET_REQUEST_WIFI_IFACE_STATUS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_IFACE_STATUS)
```

相关声明：[NET_REQUEST_WIFI_IFACE_STATUS](#ga3e45f6ee3801553619d8eb7d0af506eb)、[NET_REQUEST_WIFI_CMD_IFACE_STATUS](#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)。

请求 Wi-Fi 网络接口状态（Network Interface Status）。

<a id="r_gadd9b5b206c7ee2e40c30a37c7b4fc002"></a>

```c
#define NET_REQUEST_WIFI_11K_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_11K_CONFIG](#gadd9b5b206c7ee2e40c30a37c7b4fc002)、[NET_REQUEST_WIFI_CMD_11K_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)。

请求 Wi-Fi 802.11k 配置（Configuration）。

<a id="r_ga4a2b1e8befd7376749b1d4fbcf98376f"></a>

```c
#define NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST)
```

相关声明：[NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST](#ga4a2b1e8befd7376749b1d4fbcf98376f)、[NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)。

请求执行 Wi-Fi 802.11k 邻居请求（Neighbor Request）。

<a id="r_ga68aaced888f98e1ba4e6b61b53e5e2ba"></a>

```c
#define NET_REQUEST_WIFI_PS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS)
```

相关声明：[NET_REQUEST_WIFI_PS](#ga68aaced888f98e1ba4e6b61b53e5e2ba)、[NET_REQUEST_WIFI_CMD_PS](#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)。

请求 Wi-Fi 省电（Power Save）操作。

<a id="r_gab84fd7e9ca0bf0b2b9d08889dda26aad"></a>

```c
#define NET_REQUEST_WIFI_TWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_TWT)
```

相关声明：[NET_REQUEST_WIFI_TWT](#gab84fd7e9ca0bf0b2b9d08889dda26aad)、[NET_REQUEST_WIFI_CMD_TWT](#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)。

请求 Wi-Fi 目标唤醒时间（Target Wake Time，TWT）操作。

<a id="r_gaf1a806a89b0fd20de950c6e085351134"></a>

```c
#define NET_REQUEST_WIFI_BTWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTWT)
```

相关声明：[NET_REQUEST_WIFI_BTWT](#gaf1a806a89b0fd20de950c6e085351134)、[NET_REQUEST_WIFI_CMD_BTWT](#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)。

请求建立 Wi-Fi 广播目标唤醒时间流（Broadcast TWT Flow Setup）。

<a id="r_ga1032f3773cfe6130da4d4d498b044ee2"></a>

```c
#define NET_REQUEST_WIFI_PS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_PS_CONFIG](#ga1032f3773cfe6130da4d4d498b044ee2)、[NET_REQUEST_WIFI_CMD_PS_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)。

请求 Wi-Fi 省电配置（Power Save Configuration）。

<a id="r_ga2b27d102b779a6d846b375854768fb7f"></a>

```c
#define NET_REQUEST_WIFI_REG_DOMAIN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_REG_DOMAIN)
```

相关声明：[NET_REQUEST_WIFI_REG_DOMAIN](#ga2b27d102b779a6d846b375854768fb7f)、[NET_REQUEST_WIFI_CMD_REG_DOMAIN](#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)。

请求 Wi-Fi 监管域（Regulatory Domain）。

<a id="r_ga9b4da60a8108b0cc431ac1eecfca0cd0"></a>

```c
#define NET_REQUEST_WIFI_MODE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_MODE)
```

相关声明：[NET_REQUEST_WIFI_MODE](#ga9b4da60a8108b0cc431ac1eecfca0cd0)、[NET_REQUEST_WIFI_CMD_MODE](#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)。

请求当前 Wi-Fi 模式（Mode）。

<a id="r_ga3098e817d12bf4619c9fd2698508fb4e"></a>

```c
#define NET_REQUEST_WIFI_PACKET_FILTER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PACKET_FILTER)
```

相关声明：[NET_REQUEST_WIFI_PACKET_FILTER](#ga3098e817d12bf4619c9fd2698508fb4e)、[NET_REQUEST_WIFI_CMD_PACKET_FILTER](#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)。

请求 Wi-Fi 分组过滤器（Packet Filter）。

<a id="r_gad9614d2368f8399850aaec05e40bdc78"></a>

```c
#define NET_REQUEST_WIFI_CHANNEL (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CHANNEL)
```

相关声明：[NET_REQUEST_WIFI_CHANNEL](#gad9614d2368f8399850aaec05e40bdc78)、[NET_REQUEST_WIFI_CMD_CHANNEL](#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)。

请求 Wi-Fi 信道（Channel）。

<a id="r_gaa3e52e08d89a1104f07207e52b81d503"></a>

```c
#define NET_REQUEST_WIFI_AP_STA_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT)
```

相关声明：[NET_REQUEST_WIFI_AP_STA_DISCONNECT](#gaa3e52e08d89a1104f07207e52b81d503)、[NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)。

请求 Wi-Fi 接入点（AP）断开某个站点（Station）的连接。

<a id="r_ga3e60c29ca9ce95d17a7fff087290f7f1"></a>

```c
#define NET_REQUEST_WIFI_VERSION (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_VERSION)
```

相关声明：[NET_REQUEST_WIFI_VERSION](#ga3e60c29ca9ce95d17a7fff087290f7f1)、[NET_REQUEST_WIFI_CMD_VERSION](#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)。

请求 Wi-Fi 版本（Version）。

<a id="r_gac6483341435ff380a2d4a69430899c1a"></a>

```c
#define NET_REQUEST_WIFI_CONN_PARAMS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONN_PARAMS)
```

相关声明：[NET_REQUEST_WIFI_CONN_PARAMS](#gac6483341435ff380a2d4a69430899c1a)、[NET_REQUEST_WIFI_CMD_CONN_PARAMS](#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)。

请求 Wi-Fi 连接参数（Connection Parameters）。

<a id="r_ga22d80ef0ffb15e4286d7b1c3325d5334"></a>

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD)
```

相关声明：[NET_REQUEST_WIFI_RTS_THRESHOLD](#ga22d80ef0ffb15e4286d7b1c3325d5334)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)。

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_gaf4a78d230f5e0743a6aaf152ddda1c67"></a>

```c
#define NET_REQUEST_WIFI_AP_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM)
```

相关声明：[NET_REQUEST_WIFI_AP_CONFIG_PARAM](#gaf4a78d230f5e0743a6aaf152ddda1c67)、[NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)。

请求配置 Wi-Fi 接入点参数（AP Parameters）。

<a id="r_ga4d9dbfcf719df5639a0d592b4b8d4322"></a>

```c
#define NET_REQUEST_WIFI_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONFIG_PARAM)
```

相关声明：[NET_REQUEST_WIFI_CONFIG_PARAM](#ga4d9dbfcf719df5639a0d592b4b8d4322)、[NET_REQUEST_WIFI_CMD_CONFIG_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)。

请求配置 Wi-Fi 站点参数（STA Parameters）。

<a id="r_ga4f644b4c980628ffd556458eddc0933d"></a>

```c
#define NET_REQUEST_WIFI_BTM_QUERY (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTM_QUERY)
```

相关声明：[NET_REQUEST_WIFI_BTM_QUERY](#ga4f644b4c980628ffd556458eddc0933d)、[NET_REQUEST_WIFI_CMD_BTM_QUERY](#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)。

请求 Wi-Fi 基本服务集转换管理查询（BSS Transition Management，BTM Query）。

<a id="r_ga9070995249eb35de37e2b60c4426f840"></a>

```c
#define NET_REQUEST_WIFI_PMKSA_FLUSH (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PMKSA_FLUSH)
```

相关声明：[NET_REQUEST_WIFI_PMKSA_FLUSH](#ga9070995249eb35de37e2b60c4426f840)、[NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)。

请求清空 Wi-Fi 成对主密钥安全关联缓存条目（PMKSA Cache Entries）。

<a id="r_gae5dc7835e11487187663dfe65a15f22b"></a>

```c
#define NET_REQUEST_WIFI_ENTERPRISE_CREDS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS)
```

相关声明：[NET_REQUEST_WIFI_ENTERPRISE_CREDS](#gae5dc7835e11487187663dfe65a15f22b)、[NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)。

设置 Wi‑Fi 企业模式的 CA／客户端证书及密钥（CA/client certificate and key）。

<a id="r_ga2678ea372335af008d9bd3333f7a7de1"></a>

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG](#ga2678ea372335af008d9bd3333f7a7de1)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)。

请求配置 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="r_ga649a63bc7d315ebdd89464ff48b3fada"></a>

```c
#define NET_REQUEST_WIFI_WPS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_WPS_CONFIG)
```

相关声明：[NET_REQUEST_WIFI_WPS_CONFIG](#ga649a63bc7d315ebdd89464ff48b3fada)、[NET_REQUEST_WIFI_CMD_WPS_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)。

请求 Wi-Fi 保护设置配置（Wi-Fi Protected Setup，WPS Configuration）。

<a id="r_ga89cc123bb5c30140d2ce0a8b741b1086"></a>

```c
#define NET_REQUEST_WIFI_START_ROAMING (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_START_ROAMING)
```

相关声明：[NET_REQUEST_WIFI_START_ROAMING](#ga89cc123bb5c30140d2ce0a8b741b1086)、[NET_REQUEST_WIFI_CMD_START_ROAMING](#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)。

请求开始 Wi-Fi 漫游（Roaming）。

<a id="r_ga373031970a29331bf1b30d1654c128f0"></a>

```c
#define NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

相关声明：[NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE](#ga373031970a29331bf1b30d1654c128f0)、[NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)。

通知 Wi-Fi 邻居报告（Neighbor Report）处理完成。

<a id="r_ga36992c3098d2a1e87f31a18ce369bcc8"></a>

```c
#define NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD)
```

相关声明：[NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD](#ga36992c3098d2a1e87f31a18ce369bcc8)、[NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)。

请求配置 Wi-Fi 基本服务集最大空闲周期（BSS Maximum Idle Period）。

<a id="r_ga9d407a15b9804aea6673d603aec9f0e9"></a>

```c
#define NET_REQUEST_WIFI_BGSCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BGSCAN)
```

相关声明：[NET_REQUEST_WIFI_BGSCAN](#ga9d407a15b9804aea6673d603aec9f0e9)、[NET_REQUEST_WIFI_CMD_BGSCAN](#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)。

请求 Wi-Fi 后台扫描配置（Background Scan Configuration）。

<a id="r_ga4b3de0f402a8f0012ea65c4ab50d2761"></a>

```c
#define NET_REQUEST_WIFI_P2P_OPER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_P2P_OPER)
```

相关声明：[NET_REQUEST_WIFI_P2P_OPER](#ga4b3de0f402a8f0012ea65c4ab50d2761)、[NET_REQUEST_WIFI_CMD_P2P_OPER](#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)。

请求 Wi-Fi 直连操作（Wi-Fi Direct，P2P）。

<a id="r_ga436a927d47eb9abe683b89f2b128cd6e"></a>

```c
#define NET_EVENT_WIFI_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_RESULT)
```

相关声明：[NET_EVENT_WIFI_SCAN_RESULT](#ga436a927d47eb9abe683b89f2b128cd6e)。

报告 Wi-Fi 扫描结果（Scan Result）时发出的事件。

<a id="r_ga8ce35a12e5338e9a65970382b4a26b88"></a>

```c
#define NET_EVENT_WIFI_SCAN_DONE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_DONE)
```

相关声明：[NET_EVENT_WIFI_SCAN_DONE](#ga8ce35a12e5338e9a65970382b4a26b88)。

Wi-Fi 扫描完成（Scan Done）时发出的事件。

<a id="r_ga0e8feafcc5efd85d04be91f407c0b7c4"></a>

```c
#define NET_EVENT_WIFI_CONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_CONNECT_RESULT)
```

相关声明：[NET_EVENT_WIFI_CONNECT_RESULT](#ga0e8feafcc5efd85d04be91f407c0b7c4)。

报告 Wi-Fi 连接结果（Connect Result）时发出的事件。

<a id="r_ga8cbbe69bd60f42fdbb06f4f1e15410c8"></a>

```c
#define NET_EVENT_WIFI_DISCONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_RESULT)
```

相关声明：[NET_EVENT_WIFI_DISCONNECT_RESULT](#ga8cbbe69bd60f42fdbb06f4f1e15410c8)。

报告 Wi-Fi 断开连接结果（Disconnect Result）时发出的事件。

<a id="r_ga99e11fc15582b94d4243de7733e47ebb"></a>

```c
#define NET_EVENT_WIFI_IFACE_STATUS (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_IFACE_STATUS)
```

相关声明：[NET_EVENT_WIFI_IFACE_STATUS](#ga99e11fc15582b94d4243de7733e47ebb)。

报告 Wi-Fi 网络接口状态（Network Interface Status）时发出的事件。

<a id="r_gaeb968a5d2a8d68a8c634cca18dbcf9c6"></a>

```c
#define NET_EVENT_WIFI_TWT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT)
```

相关声明：[NET_EVENT_WIFI_TWT](#gaeb968a5d2a8d68a8c634cca18dbcf9c6)。

报告 Wi-Fi 目标唤醒时间信息（TWT Information）时发出的事件。

<a id="r_ga682d95b5d06a9b175c10d712acca8a49"></a>

```c
#define NET_EVENT_WIFI_TWT_SLEEP_STATE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE)
```

相关声明：[NET_EVENT_WIFI_TWT_SLEEP_STATE](#ga682d95b5d06a9b175c10d712acca8a49)。

报告 Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep State）时发出的事件。

<a id="r_gaea8d222282ddef6992330763afc759a4"></a>

```c
#define NET_EVENT_WIFI_RAW_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT)
```

相关声明：[NET_EVENT_WIFI_RAW_SCAN_RESULT](#gaea8d222282ddef6992330763afc759a4)。

报告 Wi-Fi 原始扫描结果（Raw Scan Result）时发出的事件。

<a id="r_ga40027feb7ec42c846fd99b56bbd2256d"></a>

```c
#define NET_EVENT_WIFI_DISCONNECT_COMPLETE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE)
```

相关声明：[NET_EVENT_WIFI_DISCONNECT_COMPLETE](#ga40027feb7ec42c846fd99b56bbd2256d)。

Wi-Fi 断开连接完成（Disconnect Completed）时发出的事件。

<a id="r_ga8da47e9d3e594840fb7a7d59f45ea9ce"></a>

```c
#define NET_EVENT_WIFI_SIGNAL_CHANGE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SIGNAL_CHANGE)
```

相关声明：[NET_EVENT_WIFI_SIGNAL_CHANGE](#ga8da47e9d3e594840fb7a7d59f45ea9ce)。

已连接接入点（AP）的信号变化事件（Signal Change）。

<a id="r_ga7ed4bc9f25055f5a35270a4c6a0bedcc"></a>

```c
#define NET_EVENT_WIFI_NEIGHBOR_REP_COMP (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

相关声明：[NET_EVENT_WIFI_NEIGHBOR_REP_COMP](#ga7ed4bc9f25055f5a35270a4c6a0bedcc)。

邻居报告完成事件（Neighbor Report Completed）。

<a id="r_ga1d678fbae0f092814392c0ab4087cb73"></a>

```c
#define NET_EVENT_WIFI_AP_ENABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT)
```

相关声明：[NET_EVENT_WIFI_AP_ENABLE_RESULT](#ga1d678fbae0f092814392c0ab4087cb73)。

报告 Wi-Fi 接入点启用结果（AP Enable Result）时发出的事件。

<a id="r_ga104296fdb38edf868bea1a46f572d101"></a>

```c
#define NET_EVENT_WIFI_AP_DISABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT)
```

相关声明：[NET_EVENT_WIFI_AP_DISABLE_RESULT](#ga104296fdb38edf868bea1a46f572d101)。

报告 Wi-Fi 接入点禁用结果（AP Disable Result）时发出的事件。

<a id="r_gacc392179948bfd5bed6702dc8fb5cd9d"></a>

```c
#define NET_EVENT_WIFI_AP_STA_CONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_CONNECTED)
```

相关声明：[NET_EVENT_WIFI_AP_STA_CONNECTED](#gacc392179948bfd5bed6702dc8fb5cd9d)。

接入点模式（AP Mode）下，Wi-Fi 站点（Station）连接成功时发出的事件。

<a id="r_ga3e8154ce1808665dd165f793ddec1673"></a>

```c
#define NET_EVENT_WIFI_AP_STA_DISCONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED)
```

相关声明：[NET_EVENT_WIFI_AP_STA_DISCONNECTED](#ga3e8154ce1808665dd165f793ddec1673)。

Wi-Fi 站点（Station）与接入点（AP）断开连接时发出的事件。

<a id="r_gadfcff8ac6645c5b6b8645c1612ad4e3a"></a>

```c
#define NET_EVENT_WIFI_P2P_DEVICE_FOUND (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND)
```

相关声明：[NET_EVENT_WIFI_P2P_DEVICE_FOUND](#gadfcff8ac6645c5b6b8645c1612ad4e3a)。

发现 P2P 设备（P2P Device Found）时发出的事件。

<a id="r_ga38d92ba342887e46c957b820d89a7a20"></a>

```c
#define WIFI_BTWT_AGREEMENT_MAX 5
```

相关声明：[WIFI_BTWT_AGREEMENT_MAX](#ga38d92ba342887e46c957b820d89a7a20)。

广播目标唤醒时间协定集（Broadcast TWT Agreement Sets）的最大数量。

<a id="r_ga3a6bfa37bd7850342279d304df20977d"></a>

```c
#define MAX_REG_CHAN_NUM 42
```

相关声明：[MAX_REG_CHAN_NUM](#ga3a6bfa37bd7850342279d304df20977d)。

最大监管信道数量（Max Regulatory Channel Number）。

<a id="r_ga234d72d7c881e67ff49fb6c474c622e3"></a>

```c
#define WIFI_WPS_PIN_MAX_LEN 8
```

相关声明：[WIFI_WPS_PIN_MAX_LEN](#ga234d72d7c881e67ff49fb6c474c622e3)。

Wi-Fi 保护设置个人识别码（WPS PIN）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_gad34b366f1c315207ce0da587ca96d8d8"></a>

```c
typedef void(* scan_result_cb_t) (struct net_if *iface, int status, struct wifi_scan_result *entry)
```

相关声明：[scan_result_cb_t](#gad34b366f1c315207ce0da587ca96d8d8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_scan_result](../network_core_model_reference/P186_wifi_scan_result_结构体.md)。

扫描结果回调（Scan Result Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_ga86a5741e54aeb3e290142b0de217b8a8"></a>

```c
enum wifi_conn_status { WIFI_STATUS_CONN_SUCCESS = 0 , WIFI_STATUS_CONN_FAIL , WIFI_STATUS_CONN_WRONG_PASSWORD , WIFI_STATUS_CONN_TIMEOUT , WIFI_STATUS_CONN_AP_NOT_FOUND , WIFI_STATUS_CONN_AUTH_REJECT , WIFI_STATUS_CONN_ASSOC_REJECT , WIFI_STATUS_CONN_LAST_STATUS , WIFI_STATUS_DISCONN_FIRST_STATUS = WIFI_STATUS_CONN_LAST_STATUS }
```

相关声明：[wifi_conn_status](#ga86a5741e54aeb3e290142b0de217b8a8)、[WIFI_STATUS_CONN_SUCCESS](#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)、[WIFI_STATUS_CONN_FAIL](#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)、[WIFI_STATUS_CONN_WRONG_PASSWORD](#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)、[WIFI_STATUS_CONN_TIMEOUT](#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)、[WIFI_STATUS_CONN_AP_NOT_FOUND](#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)、[WIFI_STATUS_CONN_AUTH_REJECT](#gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91)、[WIFI_STATUS_CONN_ASSOC_REJECT](#gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb)、[WIFI_STATUS_CONN_LAST_STATUS](#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)、[WIFI_STATUS_DISCONN_FIRST_STATUS](#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)。

Wi-Fi 连接结果代码（Connect Result Codes）。

<a id="r_gadde31a04fa25ed805115c6b31854cd9c"></a>

```c
enum wifi_security_type { WIFI_SECURITY_TYPE_NONE = 0 , WIFI_SECURITY_TYPE_PSK , WIFI_SECURITY_TYPE_PSK_SHA256 , WIFI_SECURITY_TYPE_SAE , WIFI_SECURITY_TYPE_SAE_HNP = WIFI_SECURITY_TYPE_SAE , WIFI_SECURITY_TYPE_SAE_H2E , WIFI_SECURITY_TYPE_SAE_AUTO , WIFI_SECURITY_TYPE_WAPI , WIFI_SECURITY_TYPE_EAP , WIFI_SECURITY_TYPE_EAP_TLS = WIFI_SECURITY_TYPE_EAP , WIFI_SECURITY_TYPE_WEP , WIFI_SECURITY_TYPE_WPA_PSK , WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL , WIFI_SECURITY_TYPE_DPP , WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2 , WIFI_SECURITY_TYPE_EAP_PEAP_GTC , WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2 , WIFI_SECURITY_TYPE_EAP_PEAP_TLS , WIFI_SECURITY_TYPE_FT_PSK , WIFI_SECURITY_TYPE_FT_SAE , WIFI_SECURITY_TYPE_FT_EAP , WIFI_SECURITY_TYPE_FT_EAP_SHA384 , WIFI_SECURITY_TYPE_SAE_EXT_KEY , WIFI_SECURITY_TYPE_WEP_OPEN , WIFI_SECURITY_TYPE_WEP_SHARED , WIFI_SECURITY_TYPE_OWE , WIFI_SECURITY_TYPE_PSK_SHA384 , WIFI_SECURITY_TYPE_FT_PSK_SHA384 }
```

相关声明：[wifi_security_type](#gadde31a04fa25ed805115c6b31854cd9c)、[WIFI_SECURITY_TYPE_NONE](#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)、[WIFI_SECURITY_TYPE_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)、[WIFI_SECURITY_TYPE_PSK_SHA256](#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)、[WIFI_SECURITY_TYPE_SAE](#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)、[WIFI_SECURITY_TYPE_SAE_HNP](#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91)、[WIFI_SECURITY_TYPE_SAE_H2E](#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df)、[WIFI_SECURITY_TYPE_SAE_AUTO](#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0)、[WIFI_SECURITY_TYPE_WAPI](#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)、[WIFI_SECURITY_TYPE_EAP](#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)、[WIFI_SECURITY_TYPE_EAP_TLS](#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40)、[WIFI_SECURITY_TYPE_WEP](#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)、[WIFI_SECURITY_TYPE_WPA_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)、[WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL](#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)、[WIFI_SECURITY_TYPE_DPP](#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f)、[WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2](#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212)、[WIFI_SECURITY_TYPE_EAP_PEAP_GTC](#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5)、[WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2](#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d)、[WIFI_SECURITY_TYPE_EAP_PEAP_TLS](#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477)、[WIFI_SECURITY_TYPE_FT_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5)、[WIFI_SECURITY_TYPE_FT_SAE](#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092)、[WIFI_SECURITY_TYPE_FT_EAP](#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)、[WIFI_SECURITY_TYPE_FT_EAP_SHA384](#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)、[WIFI_SECURITY_TYPE_SAE_EXT_KEY](#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02)、[WIFI_SECURITY_TYPE_WEP_OPEN](#ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7)、[WIFI_SECURITY_TYPE_WEP_SHARED](#ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122)、[WIFI_SECURITY_TYPE_OWE](#ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca)、[WIFI_SECURITY_TYPE_PSK_SHA384](#ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814)、[WIFI_SECURITY_TYPE_FT_PSK_SHA384](#ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f)。

IEEE 802.11 安全类型（Security Types）。

<a id="r_gafc901312b5988481b34d05a031d6c0db"></a>

```c
enum wifi_wep_key_type { WIFI_WEP_KEY_TYPE_UNKNOWN = 0 , WIFI_WEP_KEY_TYPE_64 , WIFI_WEP_KEY_TYPE_128 }
```

相关声明：[wifi_wep_key_type](#gafc901312b5988481b34d05a031d6c0db)、[WIFI_WEP_KEY_TYPE_UNKNOWN](#ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104)、[WIFI_WEP_KEY_TYPE_64](#ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484)、[WIFI_WEP_KEY_TYPE_128](#ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f)。

WEP 密钥类型（Key Type），依据密钥长度（Key Length）确定。

<a id="r_ga92b6fa6755491c3bd61f895213d07331"></a>

```c
enum wifi_eap_type { WIFI_EAP_TYPE_NONE = 0 , WIFI_EAP_TYPE_GTC = 6 , WIFI_EAP_TYPE_TLS = 13 , WIFI_EAP_TYPE_TTLS = 21 , WIFI_EAP_TYPE_PEAP = 25 , WIFI_EAP_TYPE_MSCHAPV2 = 26 }
```

相关声明：[wifi_eap_type](#ga92b6fa6755491c3bd61f895213d07331)、[WIFI_EAP_TYPE_NONE](#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b)、[WIFI_EAP_TYPE_GTC](#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f)、[WIFI_EAP_TYPE_TLS](#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38)、[WIFI_EAP_TYPE_TTLS](#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac)、[WIFI_EAP_TYPE_PEAP](#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f)、[WIFI_EAP_TYPE_MSCHAPV2](#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f)。

EPA 方法类型（EPA Method Types，原文写作 EPA）。

<a id="r_ga48fea1f0c7d2700cef47068f96c6b71a"></a>

```c
enum wifi_wpa3_enterprise_type { WIFI_WPA3_ENTERPRISE_NA = 0 , WIFI_WPA3_ENTERPRISE_SUITEB = 1 , WIFI_WPA3_ENTERPRISE_SUITEB_192 , WIFI_WPA3_ENTERPRISE_ONLY }
```

相关声明：[wifi_wpa3_enterprise_type](#ga48fea1f0c7d2700cef47068f96c6b71a)、[WIFI_WPA3_ENTERPRISE_NA](#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1)、[WIFI_WPA3_ENTERPRISE_SUITEB](#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589)、[WIFI_WPA3_ENTERPRISE_SUITEB_192](#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa)、[WIFI_WPA3_ENTERPRISE_ONLY](#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa)。

WPA3 企业安全类型（WPA3 Enterprise Security Types）。

<a id="r_ga218525a9d9ee64524f983e52d5767562"></a>

```c
enum wifi_eap_tls_cipher_type { WIFI_EAP_TLS_NONE , WIFI_EAP_TLS_ECC_P384 , WIFI_EAP_TLS_RSA_3K }
```

相关声明：[wifi_eap_tls_cipher_type](#ga218525a9d9ee64524f983e52d5767562)、[WIFI_EAP_TLS_NONE](#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df)、[WIFI_EAP_TLS_ECC_P384](#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9)、[WIFI_EAP_TLS_RSA_3K](#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17)。

EAP TLS 密码类型（Cipher Types）。

<a id="r_ga7f7b23ac019ca504a2006f0376735645"></a>

```c
enum wifi_cipher_type { WPA_CAPA_ENC_CCMP , WPA_CAPA_ENC_GCMP , WPA_CAPA_ENC_GCMP_256 }
```

相关声明：[wifi_cipher_type](#ga7f7b23ac019ca504a2006f0376735645)、[WPA_CAPA_ENC_CCMP](#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)、[WPA_CAPA_ENC_GCMP](#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)、[WPA_CAPA_ENC_GCMP_256](#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)。

组密码与成对密码类型（Group Cipher and Pairwise Cipher Types）。

<a id="r_gaf84d5e1a68393483fc6063c06b8f26e0"></a>

```c
enum wifi_group_mgmt_cipher_type { WPA_CAPA_ENC_BIP , WPA_CAPA_ENC_BIP_GMAC_128 , WPA_CAPA_ENC_BIP_GMAC_256 }
```

相关声明：[wifi_group_mgmt_cipher_type](#gaf84d5e1a68393483fc6063c06b8f26e0)、[WPA_CAPA_ENC_BIP](#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)、[WPA_CAPA_ENC_BIP_GMAC_128](#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)、[WPA_CAPA_ENC_BIP_GMAC_256](#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)。

组管理密码类型（Group Management Cipher Types）。

<a id="r_ga1f252da47d9650023d7fff6d08e49c76"></a>

```c
enum wifi_mfp_options { WIFI_MFP_DISABLE = 0 , WIFI_MFP_OPTIONAL , WIFI_MFP_REQUIRED }
```

相关声明：[wifi_mfp_options](#ga1f252da47d9650023d7fff6d08e49c76)、[WIFI_MFP_DISABLE](#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)、[WIFI_MFP_OPTIONAL](#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)、[WIFI_MFP_REQUIRED](#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)。

IEEE 802.11w 管理帧保护（Management Frame Protection，MFP）。

<a id="r_ga1e2f0439a322355fa7368ea880c9c15d"></a>

```c
enum wifi_frequency_bands { WIFI_FREQ_BAND_2_4_GHZ = 0 , WIFI_FREQ_BAND_5_GHZ , WIFI_FREQ_BAND_6_GHZ , WIFI_FREQ_BAND_SUB_1_GHZ , __WIFI_FREQ_BAND_AFTER_LAST , WIFI_FREQ_BAND_MAX = __WIFI_FREQ_BAND_AFTER_LAST - 1 , WIFI_FREQ_BAND_UNKNOWN }
```

相关声明：[wifi_frequency_bands](#ga1e2f0439a322355fa7368ea880c9c15d)、[WIFI_FREQ_BAND_2_4_GHZ](#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)、[WIFI_FREQ_BAND_5_GHZ](#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)、[WIFI_FREQ_BAND_6_GHZ](#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)、[WIFI_FREQ_BAND_SUB_1_GHZ](#gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211)、[WIFI_FREQ_BAND_MAX](#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)、[WIFI_FREQ_BAND_UNKNOWN](#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)。

IEEE 802.11 工作频段（Operational Frequency Bands），并非穷举。

<a id="r_ga3b01cead3c2eb4581fe85e2aaaffbd49"></a>

```c
enum wifi_frequency_bandwidths { WIFI_FREQ_BANDWIDTH_20MHZ = 1 , WIFI_FREQ_BANDWIDTH_40MHZ , WIFI_FREQ_BANDWIDTH_80MHZ , WIFI_FREQ_BANDWIDTH_1MHZ , WIFI_FREQ_BANDWIDTH_2MHZ , WIFI_FREQ_BANDWIDTH_4MHZ , WIFI_FREQ_BANDWIDTH_8MHZ , __WIFI_FREQ_BANDWIDTH_AFTER_LAST , WIFI_FREQ_BANDWIDTH_MAX = __WIFI_FREQ_BANDWIDTH_AFTER_LAST - 1 , WIFI_FREQ_BANDWIDTH_UNKNOWN }
```

相关声明：[wifi_frequency_bandwidths](#ga3b01cead3c2eb4581fe85e2aaaffbd49)、[WIFI_FREQ_BANDWIDTH_20MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5)、[WIFI_FREQ_BANDWIDTH_40MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1)、[WIFI_FREQ_BANDWIDTH_80MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb)、[WIFI_FREQ_BANDWIDTH_1MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc)、[WIFI_FREQ_BANDWIDTH_2MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134)、[WIFI_FREQ_BANDWIDTH_4MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510)、[WIFI_FREQ_BANDWIDTH_8MHZ](#gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c)、[WIFI_FREQ_BANDWIDTH_MAX](#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90)、[WIFI_FREQ_BANDWIDTH_UNKNOWN](#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)。

IEEE 802.11 工作频率带宽（Operational Frequency Bandwidths），并非穷举。

<a id="r_ga981961f747b919d61d3ccbd41e4508b4"></a>

```c
enum wifi_iface_state { WIFI_STATE_DISCONNECTED = 0 , WIFI_STATE_INTERFACE_DISABLED , WIFI_STATE_INACTIVE , WIFI_STATE_SCANNING , WIFI_STATE_AUTHENTICATING , WIFI_STATE_ASSOCIATING , WIFI_STATE_ASSOCIATED , WIFI_STATE_4WAY_HANDSHAKE , WIFI_STATE_GROUP_HANDSHAKE , WIFI_STATE_COMPLETED }
```

相关声明：[wifi_iface_state](#ga981961f747b919d61d3ccbd41e4508b4)、[WIFI_STATE_DISCONNECTED](#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)、[WIFI_STATE_INTERFACE_DISABLED](#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)、[WIFI_STATE_INACTIVE](#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)、[WIFI_STATE_SCANNING](#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)、[WIFI_STATE_AUTHENTICATING](#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)、[WIFI_STATE_ASSOCIATING](#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)、[WIFI_STATE_ASSOCIATED](#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)、[WIFI_STATE_4WAY_HANDSHAKE](#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)、[WIFI_STATE_GROUP_HANDSHAKE](#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)、[WIFI_STATE_COMPLETED](#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)。

Wi-Fi 接口状态（Interface States）。

<a id="r_ga584f6239ac14e2bedc5e6bd72756423b"></a>

```c
enum wifi_iface_mode { WIFI_MODE_INFRA = 0 , WIFI_MODE_IBSS = 1 , WIFI_MODE_AP = 2 , WIFI_MODE_P2P_GO = 3 , WIFI_MODE_P2P_GROUP_FORMATION = 4 , WIFI_MODE_MESH = 5 }
```

相关声明：[wifi_iface_mode](#ga584f6239ac14e2bedc5e6bd72756423b)、[WIFI_MODE_INFRA](#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)、[WIFI_MODE_IBSS](#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)、[WIFI_MODE_AP](#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)、[WIFI_MODE_P2P_GO](#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)、[WIFI_MODE_P2P_GROUP_FORMATION](#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)、[WIFI_MODE_MESH](#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)。

Wi-Fi 接口模式（Interface Modes）。

<a id="r_gabdb2a784d4727b71ab44cca04e422c62"></a>

```c
enum wifi_link_mode { WIFI_0 = 0 , WIFI_1 , WIFI_2 , WIFI_3 , WIFI_4 , WIFI_5 , WIFI_6 , WIFI_6E , WIFI_7 }
```

相关声明：[wifi_link_mode](#gabdb2a784d4727b71ab44cca04e422c62)、[WIFI_0](#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)、[WIFI_1](#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)、[WIFI_2](#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)、[WIFI_3](#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)、[WIFI_4](#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)、[WIFI_5](#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)、[WIFI_6](#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)、[WIFI_6E](#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)、[WIFI_7](#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)。

Wi-Fi 链路工作模式（Link Operating Modes）。

<a id="r_gad30e29eda65ccafdbd7f11865937b8ea"></a>

```c
enum wifi_scan_type { WIFI_SCAN_TYPE_ACTIVE = 0 , WIFI_SCAN_TYPE_PASSIVE }
```

相关声明：[wifi_scan_type](#gad30e29eda65ccafdbd7f11865937b8ea)、[WIFI_SCAN_TYPE_ACTIVE](#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)、[WIFI_SCAN_TYPE_PASSIVE](#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)。

Wi-Fi 扫描类型（Scanning Types）。

<a id="r_ga0fffeb57b68fb8cdef9d3d571368b8ca"></a>

```c
enum wifi_ps { WIFI_PS_DISABLED = 0 , WIFI_PS_ENABLED }
```

相关声明：[wifi_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca)、[WIFI_PS_DISABLED](#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)、[WIFI_PS_ENABLED](#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)。

Wi-Fi 省电状态（Power Save States）。

<a id="r_gaffae7d2a754be5eb952ad2b83edad54c"></a>

```c
enum wifi_ps_mode { WIFI_PS_MODE_LEGACY = 0 , WIFI_PS_MODE_WMM }
```

相关声明：[wifi_ps_mode](#gaffae7d2a754be5eb952ad2b83edad54c)、[WIFI_PS_MODE_LEGACY](#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)、[WIFI_PS_MODE_WMM](#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)。

Wi-Fi 省电模式（Power Save Modes）。

<a id="r_ga4a9243eeb974111d6047fd3d8d9cbf35"></a>

```c
enum wifi_operational_modes { WIFI_STA_MODE = BIT(0) , WIFI_MONITOR_MODE = BIT(1) , WIFI_TX_INJECTION_MODE = BIT(2) , WIFI_PROMISCUOUS_MODE = BIT(3) , WIFI_AP_MODE = BIT(4) , WIFI_SOFTAP_MODE = BIT(5) }
```

相关声明：[wifi_operational_modes](#ga4a9243eeb974111d6047fd3d8d9cbf35)、[WIFI_STA_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)、[WIFI_MONITOR_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)、[WIFI_TX_INJECTION_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)、[WIFI_PROMISCUOUS_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)、[WIFI_AP_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)、[WIFI_SOFTAP_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)。

Wi-Fi 工作模式（Operational Mode）。

<a id="r_gaa60495242c66a3fac294886856121c1f"></a>

```c
enum wifi_filter { WIFI_PACKET_FILTER_ALL = BIT(0) , WIFI_PACKET_FILTER_MGMT = BIT(1) , WIFI_PACKET_FILTER_DATA = BIT(2) , WIFI_PACKET_FILTER_CTRL = BIT(3) }
```

相关声明：[wifi_filter](#gaa60495242c66a3fac294886856121c1f)、[WIFI_PACKET_FILTER_ALL](#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)、[WIFI_PACKET_FILTER_MGMT](#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)、[WIFI_PACKET_FILTER_DATA](#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)、[WIFI_PACKET_FILTER_CTRL](#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)。

模式过滤器设置（Mode Filter Settings）。

<a id="r_gad0e998aeb1b27c4f203ca76339d323a3"></a>

```c
enum wifi_twt_operation { WIFI_TWT_SETUP = 0 , WIFI_TWT_TEARDOWN }
```

相关声明：[wifi_twt_operation](#gad0e998aeb1b27c4f203ca76339d323a3)、[WIFI_TWT_SETUP](#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)、[WIFI_TWT_TEARDOWN](#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)。

Wi-Fi 目标唤醒时间操作（Target Wake Time Operations，TWT）。

<a id="r_ga695123cd534e2499f516a07fdc5cafa8"></a>

```c
enum wifi_twt_negotiation_type { WIFI_TWT_INDIVIDUAL = 0 , WIFI_TWT_BROADCAST , WIFI_TWT_WAKE_TBTT }
```

相关声明：[wifi_twt_negotiation_type](#ga695123cd534e2499f516a07fdc5cafa8)、[WIFI_TWT_INDIVIDUAL](#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)、[WIFI_TWT_BROADCAST](#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)、[WIFI_TWT_WAKE_TBTT](#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)。

Wi-Fi 目标唤醒时间协商类型（TWT Negotiation Types）。

<a id="r_ga31c78afc89bfdc4b54cee177843f8022"></a>

```c
enum wifi_twt_setup_cmd { WIFI_TWT_SETUP_CMD_REQUEST = 0 , WIFI_TWT_SETUP_CMD_SUGGEST , WIFI_TWT_SETUP_CMD_DEMAND , WIFI_TWT_SETUP_CMD_GROUPING , WIFI_TWT_SETUP_CMD_ACCEPT , WIFI_TWT_SETUP_CMD_ALTERNATE , WIFI_TWT_SETUP_CMD_DICTATE , WIFI_TWT_SETUP_CMD_REJECT }
```

相关声明：[wifi_twt_setup_cmd](#ga31c78afc89bfdc4b54cee177843f8022)、[WIFI_TWT_SETUP_CMD_REQUEST](#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)、[WIFI_TWT_SETUP_CMD_SUGGEST](#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)、[WIFI_TWT_SETUP_CMD_DEMAND](#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)、[WIFI_TWT_SETUP_CMD_GROUPING](#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)、[WIFI_TWT_SETUP_CMD_ACCEPT](#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)、[WIFI_TWT_SETUP_CMD_ALTERNATE](#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)、[WIFI_TWT_SETUP_CMD_DICTATE](#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)、[WIFI_TWT_SETUP_CMD_REJECT](#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)。

Wi-Fi 目标唤醒时间建立命令（TWT Setup Commands）。

<a id="r_ga4d03aedac13ee4512d7717ac624f319a"></a>

```c
enum wifi_twt_setup_resp_status { WIFI_TWT_RESP_RECEIVED = 0 , WIFI_TWT_RESP_NOT_RECEIVED }
```

相关声明：[wifi_twt_setup_resp_status](#ga4d03aedac13ee4512d7717ac624f319a)、[WIFI_TWT_RESP_RECEIVED](#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)、[WIFI_TWT_RESP_NOT_RECEIVED](#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)。

Wi-Fi 目标唤醒时间协商状态（TWT Negotiation Status）。

<a id="r_ga97fa304f9a1db2294a93cccd4c93bcf6"></a>

```c
enum wifi_twt_fail_reason { WIFI_TWT_FAIL_UNSPECIFIED , WIFI_TWT_FAIL_CMD_EXEC_FAIL , WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED , WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS , WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED , WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB , WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB , WIFI_TWT_FAIL_OPERATION_IN_PROGRESS , WIFI_TWT_FAIL_INVALID_FLOW_ID , WIFI_TWT_FAIL_IP_NOT_ASSIGNED , WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS }
```

相关声明：[wifi_twt_fail_reason](#ga97fa304f9a1db2294a93cccd4c93bcf6)、[WIFI_TWT_FAIL_UNSPECIFIED](#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)、[WIFI_TWT_FAIL_CMD_EXEC_FAIL](#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)、[WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED](#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)、[WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS](#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)、[WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED](#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)、[WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB](#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)、[WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB](#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)、[WIFI_TWT_FAIL_OPERATION_IN_PROGRESS](#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)、[WIFI_TWT_FAIL_INVALID_FLOW_ID](#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)、[WIFI_TWT_FAIL_IP_NOT_ASSIGNED](#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)、[WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS](#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)。

目标唤醒时间错误码（TWT Error Codes）。

<a id="r_gad3709d07aaa3ed59b48f9dd7bd181989"></a>

```c
enum wifi_twt_teardown_status { WIFI_TWT_TEARDOWN_SUCCESS = 0 , WIFI_TWT_TEARDOWN_FAILED }
```

相关声明：[wifi_twt_teardown_status](#gad3709d07aaa3ed59b48f9dd7bd181989)、[WIFI_TWT_TEARDOWN_SUCCESS](#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)、[WIFI_TWT_TEARDOWN_FAILED](#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)。

Wi-Fi 目标唤醒时间拆除状态（TWT Teardown Status）。

<a id="r_gabe45d132797047c098041331c8f6f912"></a>

```c
enum wifi_ps_param_type { WIFI_PS_PARAM_STATE , WIFI_PS_PARAM_LISTEN_INTERVAL , WIFI_PS_PARAM_WAKEUP_MODE , WIFI_PS_PARAM_MODE , WIFI_PS_PARAM_EXIT_STRATEGY , WIFI_PS_PARAM_TIMEOUT }
```

相关声明：[wifi_ps_param_type](#gabe45d132797047c098041331c8f6f912)、[WIFI_PS_PARAM_STATE](#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)、[WIFI_PS_PARAM_LISTEN_INTERVAL](#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)、[WIFI_PS_PARAM_WAKEUP_MODE](#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)、[WIFI_PS_PARAM_MODE](#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)、[WIFI_PS_PARAM_EXIT_STRATEGY](#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)、[WIFI_PS_PARAM_TIMEOUT](#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)。

Wi-Fi省电参数（Power Save Parameters）。

<a id="r_gac7f907644847e905d67c709fa4afae7f"></a>

```c
enum wifi_ps_wakeup_mode { WIFI_PS_WAKEUP_MODE_DTIM = 0 , WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL }
```

相关声明：[wifi_ps_wakeup_mode](#gac7f907644847e905d67c709fa4afae7f)、[WIFI_PS_WAKEUP_MODE_DTIM](#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)、[WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL](#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)。

Wi-Fi 省电模式（Power Save Modes）。

<a id="r_ga2d424d1711389fb784e916a87ff854b7"></a>

```c
enum wifi_ps_exit_strategy { WIFI_PS_EXIT_CUSTOM_ALGO = 0 , WIFI_PS_EXIT_EVERY_TIM }
```

相关声明：[wifi_ps_exit_strategy](#ga2d424d1711389fb784e916a87ff854b7)、[WIFI_PS_EXIT_CUSTOM_ALGO](#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)、[WIFI_PS_EXIT_EVERY_TIM](#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)。

Wi‑Fi 省电退出策略（Power save exit strategy）。

<a id="r_gad98099584d2222ede93aba42b1fbaff0"></a>

```c
enum wifi_config_ps_param_fail_reason { WIFI_PS_PARAM_FAIL_UNSPECIFIED , WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL , WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED , WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS , WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED , WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED , WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID , WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY }
```

相关声明：[wifi_config_ps_param_fail_reason](#gad98099584d2222ede93aba42b1fbaff0)、[WIFI_PS_PARAM_FAIL_UNSPECIFIED](#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)、[WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL](#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)、[WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED](#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)、[WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS](#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)、[WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED](#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)、[WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED](#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)、[WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID](#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)、[WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY](#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)。

Wi-Fi 省电错误码（Power Save Error Codes）。

<a id="r_ga4fced9c3627d8f65d75e1651b11916b0"></a>

```c
enum wifi_btm_query_reason { WIFI_BTM_QUERY_REASON_UNSPECIFIED = 0 , WIFI_BTM_QUERY_REASON_LOW_RSSI = 16 , WIFI_BTM_QUERY_REASON_LEAVING_ESS = 20 }
```

相关声明：[wifi_btm_query_reason](#ga4fced9c3627d8f65d75e1651b11916b0)、[WIFI_BTM_QUERY_REASON_UNSPECIFIED](#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58)、[WIFI_BTM_QUERY_REASON_LOW_RSSI](#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257)、[WIFI_BTM_QUERY_REASON_LEAVING_ESS](#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49)。

IEEE 802.11v 基本服务集转换管理查询原因（BTM Query Reasons，BSS Transition Management）。

<a id="r_ga83546cf946a9123c563609e8903d9642"></a>

```c
enum wifi_ap_config_param { WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY = BIT(0) , WIFI_AP_CONFIG_PARAM_MAX_NUM_STA = BIT(1) , WIFI_AP_CONFIG_PARAM_BANDWIDTH = BIT(2) , WIFI_AP_CONFIG_PARAM_HT_CAPAB = BIT(3) , WIFI_AP_CONFIG_PARAM_VHT_CAPAB = BIT(4) }
```

相关声明：[wifi_ap_config_param](#ga83546cf946a9123c563609e8903d9642)、[WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY](#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)、[WIFI_AP_CONFIG_PARAM_MAX_NUM_STA](#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)、[WIFI_AP_CONFIG_PARAM_BANDWIDTH](#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7)、[WIFI_AP_CONFIG_PARAM_HT_CAPAB](#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199)、[WIFI_AP_CONFIG_PARAM_VHT_CAPAB](#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902)。

Wi-Fi 接入点模式配置参数（AP Mode Configuration Parameter）。

<a id="r_ga7ef91a39c2cc6bb454d870a8a80f8439"></a>

```c
enum wifi_config_param { WIFI_CONFIG_PARAM_OKC = BIT(0) }
```

相关声明：[wifi_config_param](#ga7ef91a39c2cc6bb454d870a8a80f8439)、[WIFI_CONFIG_PARAM_OKC](#gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3)。

Wi-Fi 站点模式配置参数（STA Mode Configuration Parameter）。

<a id="r_ga99a55137188119f65f9d2bb4f57cac77"></a>

```c
enum net_request_wifi_cmd { NET_REQUEST_WIFI_CMD_SCAN = 1 , NET_REQUEST_WIFI_CMD_CONNECT , NET_REQUEST_WIFI_CMD_DISCONNECT , NET_REQUEST_WIFI_CMD_AP_ENABLE , NET_REQUEST_WIFI_CMD_AP_DISABLE , NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD , NET_REQUEST_WIFI_CMD_IFACE_STATUS , NET_REQUEST_WIFI_CMD_11K_CONFIG , NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST , NET_REQUEST_WIFI_CMD_PS , NET_REQUEST_WIFI_CMD_TWT , NET_REQUEST_WIFI_CMD_BTWT , NET_REQUEST_WIFI_CMD_PS_CONFIG , NET_REQUEST_WIFI_CMD_REG_DOMAIN , NET_REQUEST_WIFI_CMD_MODE , NET_REQUEST_WIFI_CMD_PACKET_FILTER , NET_REQUEST_WIFI_CMD_CHANNEL , NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT , NET_REQUEST_WIFI_CMD_VERSION , NET_REQUEST_WIFI_CMD_CONN_PARAMS , NET_REQUEST_WIFI_CMD_RTS_THRESHOLD , NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM , NET_REQUEST_WIFI_CMD_CONFIG_PARAM , NET_REQUEST_WIFI_CMD_DPP , NET_REQUEST_WIFI_CMD_NAN , NET_REQUEST_WIFI_CMD_BTM_QUERY , NET_REQUEST_WIFI_CMD_PMKSA_FLUSH , NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS , NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG , NET_REQUEST_WIFI_CMD_WPS_CONFIG , NET_REQUEST_WIFI_CMD_START_ROAMING , NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE , NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN , NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG , NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD , NET_REQUEST_WIFI_CMD_BGSCAN , NET_REQUEST_WIFI_CMD_P2P_OPER }
```

相关声明：[net_request_wifi_cmd](#ga99a55137188119f65f9d2bb4f57cac77)、[NET_REQUEST_WIFI_CMD_SCAN](#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)、[NET_REQUEST_WIFI_CMD_CONNECT](#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)、[NET_REQUEST_WIFI_CMD_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)、[NET_REQUEST_WIFI_CMD_AP_ENABLE](#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)、[NET_REQUEST_WIFI_CMD_AP_DISABLE](#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)、[NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)、[NET_REQUEST_WIFI_CMD_IFACE_STATUS](#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)、[NET_REQUEST_WIFI_CMD_11K_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)、[NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)、[NET_REQUEST_WIFI_CMD_PS](#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)、[NET_REQUEST_WIFI_CMD_TWT](#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)、[NET_REQUEST_WIFI_CMD_BTWT](#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)、[NET_REQUEST_WIFI_CMD_PS_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)、[NET_REQUEST_WIFI_CMD_REG_DOMAIN](#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)、[NET_REQUEST_WIFI_CMD_MODE](#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)、[NET_REQUEST_WIFI_CMD_PACKET_FILTER](#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)、[NET_REQUEST_WIFI_CMD_CHANNEL](#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)、[NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)、[NET_REQUEST_WIFI_CMD_VERSION](#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)、[NET_REQUEST_WIFI_CMD_CONN_PARAMS](#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)、[NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)、[NET_REQUEST_WIFI_CMD_CONFIG_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)、[NET_REQUEST_WIFI_CMD_DPP](#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)、[NET_REQUEST_WIFI_CMD_NAN](#gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e)、[NET_REQUEST_WIFI_CMD_BTM_QUERY](#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)、[NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)、[NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)、[NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)、[NET_REQUEST_WIFI_CMD_WPS_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)、[NET_REQUEST_WIFI_CMD_START_ROAMING](#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)、[NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)、[NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN](#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)、[NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413)、[NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)、[NET_REQUEST_WIFI_CMD_BGSCAN](#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)、[NET_REQUEST_WIFI_CMD_P2P_OPER](#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)。

Wi-Fi 管理命令（Management Commands）。

<a id="r_gac2638308cbb0d268831f1618cf8e1fa8"></a>

```c
enum net_event_wifi_cmd { NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) , NET_MGMT_CMD =(NET_EVENT_WIFI_CMD_SCAN_RESULT) }
```

相关声明：[net_event_wifi_cmd](#gac2638308cbb0d268831f1618cf8e1fa8)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)、[NET_MGMT_CMD](#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)。

Wi-Fi 管理事件（Management Events）。

<a id="r_gac782af0a60b202fd19597cabb7bd3a9a"></a>

```c
enum wifi_disconn_reason { WIFI_REASON_DISCONN_SUCCESS = 0 , WIFI_REASON_DISCONN_UNSPECIFIED , WIFI_REASON_DISCONN_USER_REQUEST , WIFI_REASON_DISCONN_AP_LEAVING , WIFI_REASON_DISCONN_INACTIVITY }
```

相关声明：[wifi_disconn_reason](#gac782af0a60b202fd19597cabb7bd3a9a)、[WIFI_REASON_DISCONN_SUCCESS](#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)、[WIFI_REASON_DISCONN_UNSPECIFIED](#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)、[WIFI_REASON_DISCONN_USER_REQUEST](#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)、[WIFI_REASON_DISCONN_AP_LEAVING](#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)、[WIFI_REASON_DISCONN_INACTIVITY](#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)。

Wi-Fi 断开连接原因码（Disconnect Reason Codes）。

<a id="r_gaaf730bf76adc06434c7ac63bf0417884"></a>

```c
enum wifi_ap_status { WIFI_STATUS_AP_SUCCESS = 0 , WIFI_STATUS_AP_FAIL , WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED , WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED , WIFI_STATUS_AP_SSID_NOT_ALLOWED , WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED , WIFI_STATUS_AP_OP_NOT_SUPPORTED , WIFI_STATUS_AP_OP_NOT_PERMITTED }
```

相关声明：[wifi_ap_status](#gaaf730bf76adc06434c7ac63bf0417884)、[WIFI_STATUS_AP_SUCCESS](#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)、[WIFI_STATUS_AP_FAIL](#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)、[WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)、[WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED](#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)、[WIFI_STATUS_AP_SSID_NOT_ALLOWED](#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)、[WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)、[WIFI_STATUS_AP_OP_NOT_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)、[WIFI_STATUS_AP_OP_NOT_PERMITTED](#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)。

Wi-Fi 接入点模式结果码（AP Mode Result Codes）。

<a id="r_gae129d0783276e662575af2314eef86cd"></a>

```c
enum wifi_mgmt_op { WIFI_MGMT_GET = 0 , WIFI_MGMT_SET = 1 }
```

相关声明：[wifi_mgmt_op](#gae129d0783276e662575af2314eef86cd)、[WIFI_MGMT_GET](#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)、[WIFI_MGMT_SET](#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)。

用于任意命令的通用获取／设置操作（Get/Set Operation）。

<a id="r_ga38c184ea35c02f304cccdf389ca6d552"></a>

```c
enum wifi_twt_sleep_state { WIFI_TWT_STATE_SLEEP = 0 , WIFI_TWT_STATE_AWAKE = 1 }
```

相关声明：[wifi_twt_sleep_state](#ga38c184ea35c02f304cccdf389ca6d552)、[WIFI_TWT_STATE_SLEEP](#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)、[WIFI_TWT_STATE_AWAKE](#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)。

Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep States）。

<a id="r_ga4c36ae1a5171d3fbaeebf95c16be496d"></a>

```c
enum wifi_wps_op { WIFI_WPS_PBC = 0 , WIFI_WPS_PIN_GET = 1 , WIFI_WPS_PIN_SET = 2 }
```

相关声明：[wifi_wps_op](#ga4c36ae1a5171d3fbaeebf95c16be496d)、[WIFI_WPS_PBC](#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)、[WIFI_WPS_PIN_GET](#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)、[WIFI_WPS_PIN_SET](#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)。

Wi-Fi 保护设置操作（WPS Operation）。

<a id="r_ga0cc87c00cbee0d0aca833119dbf0d74e"></a>

```c
enum wifi_sap_iface_state { WIFI_SAP_IFACE_UNINITIALIZED , WIFI_SAP_IFACE_DISABLED , WIFI_SAP_IFACE_COUNTRY_UPDATE , WIFI_SAP_IFACE_ACS , WIFI_SAP_IFACE_HT_SCAN , WIFI_SAP_IFACE_DFS , WIFI_SAP_IFACE_NO_IR , WIFI_SAP_IFACE_ENABLED }
```

相关声明：[wifi_sap_iface_state](#ga0cc87c00cbee0d0aca833119dbf0d74e)、[WIFI_SAP_IFACE_UNINITIALIZED](#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)、[WIFI_SAP_IFACE_DISABLED](#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)、[WIFI_SAP_IFACE_COUNTRY_UPDATE](#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)、[WIFI_SAP_IFACE_ACS](#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)、[WIFI_SAP_IFACE_HT_SCAN](#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)、[WIFI_SAP_IFACE_DFS](#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)、[WIFI_SAP_IFACE_NO_IR](#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)、[WIFI_SAP_IFACE_ENABLED](#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)。

Wi-Fi 接入点状态（AP Status）。

<a id="r_gaacc27e95277622f56ef35e129aaac4d0"></a>

```c
enum wifi_bgscan_type { WIFI_BGSCAN_NONE = 0 , WIFI_BGSCAN_SIMPLE , WIFI_BGSCAN_LEARN }
```

相关声明：[wifi_bgscan_type](#gaacc27e95277622f56ef35e129aaac4d0)、[WIFI_BGSCAN_NONE](#ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9)、[WIFI_BGSCAN_SIMPLE](#ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe)、[WIFI_BGSCAN_LEARN](#ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911)。

Wi-Fi 后台扫描实现（Background Scan Implementation）。

<a id="r_ga03ab29789adfe867c4ebaddc39482344"></a>

```c
enum wifi_ext_capab { WIFI_EXT_CAPAB_20_40_COEX = 0 , WIFI_EXT_CAPAB_GLK = 1 , WIFI_EXT_CAPAB_EXT_CHAN_SWITCH = 2 , WIFI_EXT_CAPAB_TIM_BROADCAST = 18 , WIFI_EXT_CAPAB_BSS_TRANSITION = 19 }
```

相关声明：[wifi_ext_capab](#ga03ab29789adfe867c4ebaddc39482344)、[WIFI_EXT_CAPAB_20_40_COEX](#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)、[WIFI_EXT_CAPAB_GLK](#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)、[WIFI_EXT_CAPAB_EXT_CHAN_SWITCH](#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)、[WIFI_EXT_CAPAB_TIM_BROADCAST](#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)、[WIFI_EXT_CAPAB_BSS_TRANSITION](#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)。

IEEE 802.11 扩展能力（Extended Capabilities）的位位置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_ga9bb9f658d7806e42b3ee351fb3e7dfa0"></a>

```c
const char * wifi_security_txt (enum wifi_security_type security)
```

相关声明：[wifi_security_txt](#ga9bb9f658d7806e42b3ee351fb3e7dfa0)、[wifi_security_type](#gadde31a04fa25ed805115c6b31854cd9c)。

获取易读安全类型名称（Security Type Name）的辅助函数。

<a id="r_gaf67f2900be88fdf3f282400d09f2ab88"></a>

```c
const char * wifi_wpa3_enterprise_txt (enum wifi_wpa3_enterprise_type wpa3_ent)
```

相关声明：[wifi_wpa3_enterprise_txt](#gaf67f2900be88fdf3f282400d09f2ab88)、[wifi_wpa3_enterprise_type](#ga48fea1f0c7d2700cef47068f96c6b71a)。

获取易读 WPA3 企业安全类型名称（WPA3 Enterprise Security Type Name）的辅助函数。

<a id="r_gaf957fd93d98988347e009038cb694c04"></a>

```c
const char * wifi_wep_key_type_txt (enum wifi_wep_key_type wep_key_type)
```

相关声明：[wifi_wep_key_type_txt](#gaf957fd93d98988347e009038cb694c04)、[wifi_wep_key_type](#gafc901312b5988481b34d05a031d6c0db)。

获取易读 WEP 密钥类型名称（WEP Key Type Name）的辅助函数。

<a id="r_ga22354241197a9227fdba77e67d471f5c"></a>

```c
const char * wifi_mfp_txt (enum wifi_mfp_options mfp)
```

相关声明：[wifi_mfp_txt](#ga22354241197a9227fdba77e67d471f5c)、[wifi_mfp_options](#ga1f252da47d9650023d7fff6d08e49c76)。

获取易读管理帧保护名称（MFP Name）的辅助函数。

<a id="r_ga44f875bf0d931b66d582f5dca2d65ed5"></a>

```c
const char * wifi_band_txt (enum wifi_frequency_bands band)
```

相关声明：[wifi_band_txt](#ga44f875bf0d931b66d582f5dca2d65ed5)、[wifi_frequency_bands](#ga1e2f0439a322355fa7368ea880c9c15d)。

获取易读频段名称（Frequency Band Name）的辅助函数。

<a id="r_ga7ff13294abf2dc27acbb3021afb2faee"></a>

```c
const char * wifi_bandwidth_txt (enum wifi_frequency_bandwidths bandwidth)
```

相关声明：[wifi_bandwidth_txt](#ga7ff13294abf2dc27acbb3021afb2faee)、[wifi_frequency_bandwidths](#ga3b01cead3c2eb4581fe85e2aaaffbd49)。

获取易读频率带宽名称（Frequency Bandwidth Name）的辅助函数。

<a id="r_ga03d306912dc96178e21d3c82c104582f"></a>

```c
const char * wifi_state_txt (enum wifi_iface_state state)
```

相关声明：[wifi_state_txt](#ga03d306912dc96178e21d3c82c104582f)、[wifi_iface_state](#ga981961f747b919d61d3ccbd41e4508b4)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取易读接口状态名称（Interface State Name）的辅助函数。

<a id="r_gad78536ce1f30accfa45f258b6bf8c73d"></a>

```c
const char * wifi_mode_txt (enum wifi_iface_mode mode)
```

相关声明：[wifi_mode_txt](#gad78536ce1f30accfa45f258b6bf8c73d)、[wifi_iface_mode](#ga584f6239ac14e2bedc5e6bd72756423b)。

获取易读接口模式名称（Interface Mode Name）的辅助函数。

<a id="r_ga0d9d6e2150fb187025300904357f7b4d"></a>

```c
const char * wifi_link_mode_txt (enum wifi_link_mode link_mode)
```

相关声明：[wifi_link_mode_txt](#ga0d9d6e2150fb187025300904357f7b4d)、[wifi_link_mode](#gabdb2a784d4727b71ab44cca04e422c62)。

获取易读链路模式名称（Link Mode Name）的辅助函数。

<a id="r_gafbeb5f7fa97fd2ba0c691da0f8853ef2"></a>

```c
const char * wifi_ps_txt (enum wifi_ps ps_name)
```

相关声明：[wifi_ps_txt](#gafbeb5f7fa97fd2ba0c691da0f8853ef2)、[wifi_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca)。

获取易读省电名称（Power Save Name）的辅助函数。

<a id="r_gadb21d49f64e04fba59433e51d5b3481c"></a>

```c
const char * wifi_ps_mode_txt (enum wifi_ps_mode ps_mode)
```

相关声明：[wifi_ps_mode_txt](#gadb21d49f64e04fba59433e51d5b3481c)、[wifi_ps_mode](#gaffae7d2a754be5eb952ad2b83edad54c)。

获取易读省电模式名称（Power Save Mode Name）的辅助函数。

<a id="r_gadb125925e851bf7569424cd4295e7712"></a>

```c
const char * wifi_twt_operation_txt (enum wifi_twt_operation twt_operation)
```

相关声明：[wifi_twt_operation_txt](#gadb125925e851bf7569424cd4295e7712)、[wifi_twt_operation](#gad0e998aeb1b27c4f203ca76339d323a3)。

获取易读目标唤醒时间操作名称（TWT Operation Name）的辅助函数。

<a id="r_ga6a74e999d63ee491df68447219ef2a0d"></a>

```c
const char * wifi_twt_negotiation_type_txt (enum wifi_twt_negotiation_type twt_negotiation)
```

相关声明：[wifi_twt_negotiation_type_txt](#ga6a74e999d63ee491df68447219ef2a0d)、[wifi_twt_negotiation_type](#ga695123cd534e2499f516a07fdc5cafa8)。

获取易读目标唤醒时间协商类型名称（TWT Negotiation Type Name）的辅助函数。

<a id="r_gae3ca047cc6ef6b6a2e44ba6574d41a44"></a>

```c
const char * wifi_twt_setup_cmd_txt (enum wifi_twt_setup_cmd twt_setup)
```

相关声明：[wifi_twt_setup_cmd_txt](#gae3ca047cc6ef6b6a2e44ba6574d41a44)、[wifi_twt_setup_cmd](#ga31c78afc89bfdc4b54cee177843f8022)。

获取易读目标唤醒时间建立命令名称（TWT Setup Command Name）的辅助函数。

<a id="r_gab2e6a6e1d8358a8f34d67bd632709b3d"></a>

```c
static const char * wifi_twt_get_err_code_str (int16_t err_no)
```

相关声明：[wifi_twt_get_err_code_str](#gab2e6a6e1d8358a8f34d67bd632709b3d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取易读目标唤醒时间错误码名称（TWT Error Code Name）的辅助函数。

<a id="r_ga6fd645f891234136b3028574a0af9666"></a>

```c
const char * wifi_ps_wakeup_mode_txt (enum wifi_ps_wakeup_mode ps_wakeup_mode)
```

相关声明：[wifi_ps_wakeup_mode_txt](#ga6fd645f891234136b3028574a0af9666)、[wifi_ps_wakeup_mode](#gac7f907644847e905d67c709fa4afae7f)。

获取易读省电唤醒模式名称（Power Save Wakeup Mode Name）的辅助函数。

<a id="r_ga034bfcd7891caeb31820579b5ee22a7b"></a>

```c
const char * wifi_ps_exit_strategy_txt (enum wifi_ps_exit_strategy ps_exit_strategy)
```

相关声明：[wifi_ps_exit_strategy_txt](#ga034bfcd7891caeb31820579b5ee22a7b)、[wifi_ps_exit_strategy](#ga2d424d1711389fb784e916a87ff854b7)。

获取易读省电退出策略名称（Power Save Exit Strategy Name）的辅助函数。

<a id="r_ga8b72e7989964963a25f42ed1dba240a0"></a>

```c
static const char * wifi_ps_get_config_err_code_str (int16_t err_no)
```

相关声明：[wifi_ps_get_config_err_code_str](#ga8b72e7989964963a25f42ed1dba240a0)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取易读省电错误码名称（Power Save Error Code Name）的辅助函数。

<a id="r_gac18305e124523b7cc9eb6adb05d987a8"></a>

```c
const char * wifi_conn_status_txt (enum wifi_conn_status status)
```

相关声明：[wifi_conn_status_txt](#gac18305e124523b7cc9eb6adb05d987a8)、[wifi_conn_status](#ga86a5741e54aeb3e290142b0de217b8a8)。

根据状态码（Status Code）获取易读状态名称（Status Name）的辅助函数。

<a id="r_ga1bea051b0c184cb859f27b36e3593bf2"></a>

```c
const char * wifi_disconn_reason_txt (enum wifi_disconn_reason reason)
```

相关声明：[wifi_disconn_reason_txt](#ga1bea051b0c184cb859f27b36e3593bf2)、[wifi_disconn_reason](#gac782af0a60b202fd19597cabb7bd3a9a)。

用于获取易读的断开连接原因名称（Disconnect Reason Name）的辅助函数。

<a id="r_ga036416696b1e3bc458ddbaf07a08d69d"></a>

```c
void wifi_mgmt_raise_connect_result_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_connect_result_event](#ga036416696b1e3bc458ddbaf07a08d69d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理连接结果事件（Connect Result Event）。

<a id="r_gabdf7753c247587eface6e829686d120c"></a>

```c
void wifi_mgmt_raise_connect_result_status_event (struct net_if *iface, const struct wifi_status *status)
```

相关声明：[wifi_mgmt_raise_connect_result_status_event](#gabdf7753c247587eface6e829686d120c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)。

带 IEEE 802.11 代码的 Wi-Fi 管理连接结果事件（Connect Result Event）。

<a id="r_ga3b6edcf9b51afbf7a327d1a344bd7b87"></a>

```c
void wifi_mgmt_raise_disconnect_result_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_disconnect_result_event](#ga3b6edcf9b51afbf7a327d1a344bd7b87)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

<a id="r_ga3f7c4f252ab9621fbf3b9bd937253858"></a>

```c
void wifi_mgmt_raise_disconnect_result_status_event (struct net_if *iface, const struct wifi_status *status)
```

相关声明：[wifi_mgmt_raise_disconnect_result_status_event](#ga3f7c4f252ab9621fbf3b9bd937253858)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)。

带 IEEE 802.11 代码的 Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

<a id="r_ga7da6af0747bcba85f8afab30c92b5b43"></a>

```c
void wifi_mgmt_raise_iface_status_event (struct net_if *iface, struct wifi_iface_status *iface_status)
```

相关声明：[wifi_mgmt_raise_iface_status_event](#ga7da6af0747bcba85f8afab30c92b5b43)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_iface_status](../network_core_model_reference/P175_wifi_iface_status_结构体.md)。

Wi-Fi 管理接口状态事件（Interface Status Event）。

<a id="r_ga39404d15243ca084b253cae8fc07e374"></a>

```c
void wifi_mgmt_raise_twt_event (struct net_if *iface, struct wifi_twt_params *twt_params)
```

相关声明：[wifi_mgmt_raise_twt_event](#ga39404d15243ca084b253cae8fc07e374)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_twt_params](../network_core_model_reference/P189_wifi_twt_params_结构体.md)。

Wi-Fi 管理目标唤醒时间事件（TWT Event）。

<a id="r_ga18f09a3196588b51d6c0644f82f639d7"></a>

```c
void wifi_mgmt_raise_twt_sleep_state (struct net_if *iface, int twt_sleep_state)
```

相关声明：[wifi_mgmt_raise_twt_sleep_state](#ga18f09a3196588b51d6c0644f82f639d7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理目标唤醒时间睡眠状态事件（TWT Sleep State Event）。

<a id="r_ga71c99913bded844c4ca32ed9155bc470"></a>

```c
void wifi_mgmt_raise_raw_scan_result_event (struct net_if *iface, struct wifi_raw_scan_result *raw_scan_info)
```

相关声明：[wifi_mgmt_raise_raw_scan_result_event](#ga71c99913bded844c4ca32ed9155bc470)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_raw_scan_result](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md)。

Wi-Fi 管理原始扫描结果事件（Raw Scan Result Event）。

<a id="r_gaa75246d6dc55dada389c9d31e2607d5c"></a>

```c
void wifi_mgmt_raise_disconnect_complete_event (struct net_if *iface, int status)
```

相关声明：[wifi_mgmt_raise_disconnect_complete_event](#gaa75246d6dc55dada389c9d31e2607d5c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

Wi-Fi 管理断开连接完成事件（Disconnect Complete Event）。

<a id="r_ga67b52edeff76c2211b038f4aa90b8982"></a>

```c
void wifi_mgmt_raise_ap_enable_result_event (struct net_if *iface, enum wifi_ap_status status)
```

相关声明：[wifi_mgmt_raise_ap_enable_result_event](#ga67b52edeff76c2211b038f4aa90b8982)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_status](#gaaf730bf76adc06434c7ac63bf0417884)。

Wi-Fi 管理接入点模式启用结果事件（AP Mode Enable Result Event）。

<a id="r_gadee15c6a492a8ee13bea43812debb5d9"></a>

```c
void wifi_mgmt_raise_ap_disable_result_event (struct net_if *iface, enum wifi_ap_status status)
```

相关声明：[wifi_mgmt_raise_ap_disable_result_event](#gadee15c6a492a8ee13bea43812debb5d9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_status](#gaaf730bf76adc06434c7ac63bf0417884)。

Wi-Fi 管理接入点模式禁用结果事件（AP Mode Disable Result Event）。

<a id="r_gac8f17f0aa3e426a5cdb731727b9b9ce3"></a>

```c
void wifi_mgmt_raise_ap_sta_connected_event (struct net_if *iface, struct wifi_ap_sta_info *sta_info)
```

相关声明：[wifi_mgmt_raise_ap_sta_connected_event](#gac8f17f0aa3e426a5cdb731727b9b9ce3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)。

Wi-Fi 管理接入点模式站点已连接事件（AP Mode STA Connected Event）。

<a id="r_ga49fb9c3908be61d847b31c99be6afc42"></a>

```c
void wifi_mgmt_raise_ap_sta_disconnected_event (struct net_if *iface, struct wifi_ap_sta_info *sta_info)
```

相关声明：[wifi_mgmt_raise_ap_sta_disconnected_event](#ga49fb9c3908be61d847b31c99be6afc42)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)。

Wi-Fi 管理接入点模式站点已断开事件（AP Mode STA Disconnected Event）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.8\_Wi-Fi 工具函数（Utility Functions）

Wi-Fi 子系统（Subsystem）的工具函数（Utility Functions）。

<a id="r_ga4c91cd7dff0fd9e5402970f3222dc20d"></a>

```c
int wifi_utils_parse_scan_bands (char *scan_bands_str, uint8_t *band_map)
```

相关声明：[wifi_utils_parse_scan_bands](#ga4c91cd7dff0fd9e5402970f3222dc20d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将频段说明字符串（Band Specification String）转换为表示频段的位图（Bitmap）。

<a id="r_ga471a96d3fb6d610a591508b52d4c05a4"></a>

```c
int wifi_utils_parse_scan_ssids (char *scan_ssids_str, const char *ssids[], uint8_t num_ssids)
```

相关声明：[wifi_utils_parse_scan_ssids](#ga471a96d3fb6d610a591508b52d4c05a4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将包含 SSID 的字符串追加到 SSID 字符串数组（String Array）。

<a id="r_gaba9f3117bcef9da1efc1841d3bd9adfd"></a>

```c
int wifi_utils_parse_scan_chan (char *scan_chan_str, struct wifi_band_channel *chan, uint8_t max_channels)
```

相关声明：[wifi_utils_parse_scan_chan](#gaba9f3117bcef9da1efc1841d3bd9adfd)、[wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将包含扫描信道说明（Scan Channel Specification）的字符串转换为数组。

<a id="r_gaf1872d0ed2efd3737a36dcc0ab13f18e"></a>

```c
bool wifi_utils_validate_chan (uint8_t band, uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan](#gaf1872d0ed2efd3737a36dcc0ab13f18e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据频段（Band）验证信道（Channel）。

<a id="r_gaf408ba9f75354d3eca735b4804fdf199"></a>

```c
bool wifi_utils_validate_chan_2g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_2g](#gaf408ba9f75354d3eca735b4804fdf199)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 2.4 GHz 频段（Band）验证信道（Channel）。

<a id="r_gae013eee6d6b74126c29d6ca7b2036310"></a>

```c
bool wifi_utils_validate_chan_5g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_5g](#gae013eee6d6b74126c29d6ca7b2036310)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 5 GHz 频段（Band）验证信道（Channel）。

<a id="r_ga2606742e23f48da5ca1660aeac47888b"></a>

```c
bool wifi_utils_validate_chan_6g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_6g](#ga2606742e23f48da5ca1660aeac47888b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 6 GHz 频段（Band）验证信道（Channel）。

<a id="r_ga6fb496c072323dee6f09bfa44c42685f"></a>

```c
enum wifi_frequency_bands wifi_utils_chan_to_band (uint16_t chan)
```

相关声明：[wifi_frequency_bands](#ga1e2f0439a322355fa7368ea880c9c15d)、[wifi_utils_chan_to_band](#ga6fb496c072323dee6f09bfa44c42685f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取信道所属频段（Frequency Band）。

<a id="r_ga428896bb7947b4fb46bf240b5179c7a3"></a>

```c
uint16_t wifi_utils_chan_to_freq (enum wifi_frequency_bands band, uint16_t chan)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[wifi_utils_chan_to_freq](#ga428896bb7947b4fb46bf240b5179c7a3)、[wifi_frequency_bands](#ga1e2f0439a322355fa7368ea880c9c15d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将信道编号（Channel Number）转换为中心频率（Center Frequency）。

<a id="r_gaa9f346e3f44ad3441813a39bef559e2a"></a>

```c
uint16_t wifi_utils_freq_to_chan (uint16_t freq)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[wifi_utils_freq_to_chan](#gaa9f346e3f44ad3441813a39bef559e2a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将中心频率（Center Frequency）转换为信道编号（Channel Number）。

<a id="r_ga1104c3c97b460f9f3e15a7a9c56e80af"></a>

```c
#define WIFI_UTILS_MAX_BAND_STR_LEN 3
```

相关声明：[WIFI_UTILS_MAX_BAND_STR_LEN](#ga1104c3c97b460f9f3e15a7a9c56e80af)。

频段说明字符串（Band Specification String）的最大长度。

<a id="r_gaacc3c661affda7b376a4024efd645f0b"></a>

```c
#define WIFI_UTILS_MAX_CHAN_STR_LEN 4
```

相关声明：[WIFI_UTILS_MAX_CHAN_STR_LEN](#gaacc3c661affda7b376a4024efd645f0b)。

信道说明字符串（Channel Specification String）的最大长度。

## 1.9\_详细说明（Detailed Documentation）

<a id="ga3a6bfa37bd7850342279d304df20977d"></a>

### `MAX_REG_CHAN_NUM`

```c
#define MAX_REG_CHAN_NUM 42
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

最大监管信道数量（Max Regulatory Channel Number）。

<a id="ga104296fdb38edf868bea1a46f572d101"></a>

### `NET_EVENT_WIFI_AP_DISABLE_RESULT`

```c
#define NET_EVENT_WIFI_AP_DISABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 接入点禁用结果（AP Disable Result）时发出的事件。

<a id="ga1d678fbae0f092814392c0ab4087cb73"></a>

### `NET_EVENT_WIFI_AP_ENABLE_RESULT`

```c
#define NET_EVENT_WIFI_AP_ENABLE_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 接入点启用结果（AP Enable Result）时发出的事件。

<a id="gacc392179948bfd5bed6702dc8fb5cd9d"></a>

### `NET_EVENT_WIFI_AP_STA_CONNECTED`

```c
#define NET_EVENT_WIFI_AP_STA_CONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_CONNECTED)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

接入点模式（AP Mode）下，Wi-Fi 站点（Station）连接成功时发出的事件。

<a id="ga3e8154ce1808665dd165f793ddec1673"></a>

### `NET_EVENT_WIFI_AP_STA_DISCONNECTED`

```c
#define NET_EVENT_WIFI_AP_STA_DISCONNECTED (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 站点（Station）与接入点（AP）断开连接时发出的事件。

<a id="ga0e8feafcc5efd85d04be91f407c0b7c4"></a>

### `NET_EVENT_WIFI_CONNECT_RESULT`

```c
#define NET_EVENT_WIFI_CONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_CONNECT_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 连接结果（Connect Result）时发出的事件。

<a id="ga40027feb7ec42c846fd99b56bbd2256d"></a>

### `NET_EVENT_WIFI_DISCONNECT_COMPLETE`

```c
#define NET_EVENT_WIFI_DISCONNECT_COMPLETE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 断开连接完成（Disconnect Completed）时发出的事件。

<a id="ga8cbbe69bd60f42fdbb06f4f1e15410c8"></a>

### `NET_EVENT_WIFI_DISCONNECT_RESULT`

```c
#define NET_EVENT_WIFI_DISCONNECT_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 断开连接结果（Disconnect Result）时发出的事件。

<a id="ga99e11fc15582b94d4243de7733e47ebb"></a>

### `NET_EVENT_WIFI_IFACE_STATUS`

```c
#define NET_EVENT_WIFI_IFACE_STATUS (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_IFACE_STATUS)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 网络接口状态（Network Interface Status）时发出的事件。

<a id="ga7ed4bc9f25055f5a35270a4c6a0bedcc"></a>

### `NET_EVENT_WIFI_NEIGHBOR_REP_COMP`

```c
#define NET_EVENT_WIFI_NEIGHBOR_REP_COMP (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

邻居报告完成事件（Neighbor Report Completed）。

<a id="gadfcff8ac6645c5b6b8645c1612ad4e3a"></a>

### `NET_EVENT_WIFI_P2P_DEVICE_FOUND`

```c
#define NET_EVENT_WIFI_P2P_DEVICE_FOUND (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

发现 P2P 设备（P2P Device Found）时发出的事件。

<a id="gaea8d222282ddef6992330763afc759a4"></a>

### `NET_EVENT_WIFI_RAW_SCAN_RESULT`

```c
#define NET_EVENT_WIFI_RAW_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 原始扫描结果（Raw Scan Result）时发出的事件。

<a id="ga8ce35a12e5338e9a65970382b4a26b88"></a>

### `NET_EVENT_WIFI_SCAN_DONE`

```c
#define NET_EVENT_WIFI_SCAN_DONE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_DONE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 扫描完成（Scan Done）时发出的事件。

<a id="ga436a927d47eb9abe683b89f2b128cd6e"></a>

### `NET_EVENT_WIFI_SCAN_RESULT`

```c
#define NET_EVENT_WIFI_SCAN_RESULT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_RESULT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 扫描结果（Scan Result）时发出的事件。

<a id="ga8da47e9d3e594840fb7a7d59f45ea9ce"></a>

### `NET_EVENT_WIFI_SIGNAL_CHANGE`

```c
#define NET_EVENT_WIFI_SIGNAL_CHANGE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SIGNAL_CHANGE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

已连接接入点（AP）的信号变化事件（Signal Change）。

<a id="gaeb968a5d2a8d68a8c634cca18dbcf9c6"></a>

### `NET_EVENT_WIFI_TWT`

```c
#define NET_EVENT_WIFI_TWT (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 目标唤醒时间信息（TWT Information）时发出的事件。

<a id="ga682d95b5d06a9b175c10d712acca8a49"></a>

### `NET_EVENT_WIFI_TWT_SLEEP_STATE`

```c
#define NET_EVENT_WIFI_TWT_SLEEP_STATE (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

报告 Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep State）时发出的事件。

<a id="gadd9b5b206c7ee2e40c30a37c7b4fc002"></a>

### `NET_REQUEST_WIFI_11K_CONFIG`

```c
#define NET_REQUEST_WIFI_11K_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_CONFIG)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 802.11k 配置（Configuration）。

<a id="ga4a2b1e8befd7376749b1d4fbcf98376f"></a>

### `NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST`

```c
#define NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求执行 Wi-Fi 802.11k 邻居请求（Neighbor Request）。

<a id="gaf4a78d230f5e0743a6aaf152ddda1c67"></a>

### `NET_REQUEST_WIFI_AP_CONFIG_PARAM`

```c
#define NET_REQUEST_WIFI_AP_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求配置 Wi-Fi 接入点参数（AP Parameters）。

<a id="gaf81f62bf4c9e331a095acbf0d24ca1a2"></a>

### `NET_REQUEST_WIFI_AP_DISABLE`

```c
#define NET_REQUEST_WIFI_AP_DISABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_DISABLE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求禁用 Wi-Fi 接入点（Access Point，AP）。

<a id="ga638d2eb0a5029c1af46a91b523ed8589"></a>

### `NET_REQUEST_WIFI_AP_ENABLE`

```c
#define NET_REQUEST_WIFI_AP_ENABLE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_ENABLE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求启用 Wi-Fi 接入点（Access Point，AP）。

<a id="ga9918582d4e7bb0952daf993ee34e166d"></a>

### `NET_REQUEST_WIFI_AP_RTS_THRESHOLD`

```c
#define NET_REQUEST_WIFI_AP_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="gaa3e52e08d89a1104f07207e52b81d503"></a>

### `NET_REQUEST_WIFI_AP_STA_DISCONNECT`

```c
#define NET_REQUEST_WIFI_AP_STA_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 接入点（AP）断开某个站点（Station）的连接。

<a id="ga9d407a15b9804aea6673d603aec9f0e9"></a>

### `NET_REQUEST_WIFI_BGSCAN`

```c
#define NET_REQUEST_WIFI_BGSCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BGSCAN)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 后台扫描配置（Background Scan Configuration）。

<a id="ga36992c3098d2a1e87f31a18ce369bcc8"></a>

### `NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD`

```c
#define NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求配置 Wi-Fi 基本服务集最大空闲周期（BSS Maximum Idle Period）。

<a id="ga4f644b4c980628ffd556458eddc0933d"></a>

### `NET_REQUEST_WIFI_BTM_QUERY`

```c
#define NET_REQUEST_WIFI_BTM_QUERY (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTM_QUERY)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 基本服务集转换管理查询（BSS Transition Management，BTM Query）。

<a id="gaf1a806a89b0fd20de950c6e085351134"></a>

### `NET_REQUEST_WIFI_BTWT`

```c
#define NET_REQUEST_WIFI_BTWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTWT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求建立 Wi-Fi 广播目标唤醒时间流（Broadcast TWT Flow Setup）。

<a id="gad9614d2368f8399850aaec05e40bdc78"></a>

### `NET_REQUEST_WIFI_CHANNEL`

```c
#define NET_REQUEST_WIFI_CHANNEL (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CHANNEL)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 信道（Channel）。

<a id="ga4d9dbfcf719df5639a0d592b4b8d4322"></a>

### `NET_REQUEST_WIFI_CONFIG_PARAM`

```c
#define NET_REQUEST_WIFI_CONFIG_PARAM (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONFIG_PARAM)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求配置 Wi-Fi 站点参数（STA Parameters）。

<a id="gac6483341435ff380a2d4a69430899c1a"></a>

### `NET_REQUEST_WIFI_CONN_PARAMS`

```c
#define NET_REQUEST_WIFI_CONN_PARAMS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONN_PARAMS)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 连接参数（Connection Parameters）。

<a id="gaa7ab2a97950a22736bb69f60b459f0f6"></a>

### `NET_REQUEST_WIFI_CONNECT`

```c
#define NET_REQUEST_WIFI_CONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONNECT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 连接（Connect）。

<a id="ga90afd8d4e83056463ec6e667ed8ea60a"></a>

### `NET_REQUEST_WIFI_DISCONNECT`

```c
#define NET_REQUEST_WIFI_DISCONNECT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_DISCONNECT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 断开连接（Disconnect）。

<a id="gae5dc7835e11487187663dfe65a15f22b"></a>

### `NET_REQUEST_WIFI_ENTERPRISE_CREDS`

```c
#define NET_REQUEST_WIFI_ENTERPRISE_CREDS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

设置 Wi‑Fi 企业模式的 CA／客户端证书及密钥（CA/client certificate and key）。

<a id="ga3e45f6ee3801553619d8eb7d0af506eb"></a>

### `NET_REQUEST_WIFI_IFACE_STATUS`

```c
#define NET_REQUEST_WIFI_IFACE_STATUS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_IFACE_STATUS)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 网络接口状态（Network Interface Status）。

<a id="ga9b4da60a8108b0cc431ac1eecfca0cd0"></a>

### `NET_REQUEST_WIFI_MODE`

```c
#define NET_REQUEST_WIFI_MODE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_MODE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求当前 Wi-Fi 模式（Mode）。

<a id="ga373031970a29331bf1b30d1654c128f0"></a>

### `NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE`

```c
#define NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

通知 Wi-Fi 邻居报告（Neighbor Report）处理完成。

<a id="ga4b3de0f402a8f0012ea65c4ab50d2761"></a>

### `NET_REQUEST_WIFI_P2P_OPER`

```c
#define NET_REQUEST_WIFI_P2P_OPER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_P2P_OPER)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 直连操作（Wi-Fi Direct，P2P）。

<a id="ga3098e817d12bf4619c9fd2698508fb4e"></a>

### `NET_REQUEST_WIFI_PACKET_FILTER`

```c
#define NET_REQUEST_WIFI_PACKET_FILTER (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PACKET_FILTER)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 分组过滤器（Packet Filter）。

<a id="ga9070995249eb35de37e2b60c4426f840"></a>

### `NET_REQUEST_WIFI_PMKSA_FLUSH`

```c
#define NET_REQUEST_WIFI_PMKSA_FLUSH (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PMKSA_FLUSH)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求清空 Wi-Fi 成对主密钥安全关联缓存条目（PMKSA Cache Entries）。

<a id="ga68aaced888f98e1ba4e6b61b53e5e2ba"></a>

### `NET_REQUEST_WIFI_PS`

```c
#define NET_REQUEST_WIFI_PS (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 省电（Power Save）操作。

<a id="ga1032f3773cfe6130da4d4d498b044ee2"></a>

### `NET_REQUEST_WIFI_PS_CONFIG`

```c
#define NET_REQUEST_WIFI_PS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS_CONFIG)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 省电配置（Power Save Configuration）。

<a id="ga2b27d102b779a6d846b375854768fb7f"></a>

### `NET_REQUEST_WIFI_REG_DOMAIN`

```c
#define NET_REQUEST_WIFI_REG_DOMAIN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_REG_DOMAIN)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 监管域（Regulatory Domain）。

<a id="ga22d80ef0ffb15e4286d7b1c3325d5334"></a>

### `NET_REQUEST_WIFI_RTS_THRESHOLD`

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="ga2678ea372335af008d9bd3333f7a7de1"></a>

### `NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG`

```c
#define NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求配置 Wi-Fi 发送请求阈值（RTS Threshold）。

<a id="ga1c277da90986fa52dca182c4d922646f"></a>

### `NET_REQUEST_WIFI_SCAN`

```c
#define NET_REQUEST_WIFI_SCAN (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_SCAN)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 扫描（Scan）。

<a id="ga89cc123bb5c30140d2ce0a8b741b1086"></a>

### `NET_REQUEST_WIFI_START_ROAMING`

```c
#define NET_REQUEST_WIFI_START_ROAMING (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_START_ROAMING)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求开始 Wi-Fi 漫游（Roaming）。

<a id="gab84fd7e9ca0bf0b2b9d08889dda26aad"></a>

### `NET_REQUEST_WIFI_TWT`

```c
#define NET_REQUEST_WIFI_TWT (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_TWT)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 目标唤醒时间（Target Wake Time，TWT）操作。

<a id="ga3e60c29ca9ce95d17a7fff087290f7f1"></a>

### `NET_REQUEST_WIFI_VERSION`

```c
#define NET_REQUEST_WIFI_VERSION (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_VERSION)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 版本（Version）。

<a id="ga649a63bc7d315ebdd89464ff48b3fada"></a>

### `NET_REQUEST_WIFI_WPS_CONFIG`

```c
#define NET_REQUEST_WIFI_WPS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_WPS_CONFIG)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

请求 Wi-Fi 保护设置配置（Wi-Fi Protected Setup，WPS Configuration）。

<a id="ga38d92ba342887e46c957b820d89a7a20"></a>

### `WIFI_BTWT_AGREEMENT_MAX`

```c
#define WIFI_BTWT_AGREEMENT_MAX 5
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

广播目标唤醒时间协定集（Broadcast TWT Agreement Sets）的最大数量。

<a id="ga3876cd718af9f8a7b3682546da854544"></a>

### `WIFI_CHANNEL_ANY`

```c
#define WIFI_CHANNEL_ANY 255
```

```c
#include <zephyr/net/wifi.h>
```

任意信道编号（Any Channel Number）。

<a id="ga8ea9141108f93b419f6a6530bf67bd95"></a>

### `WIFI_CHANNEL_MAX`

```c
#define WIFI_CHANNEL_MAX 233
```

```c
#include <zephyr/net/wifi.h>
```

最大信道编号（Maximum Channel Number）。

<a id="ga260e473dac1e823fd298a2c982470e0b"></a>

### `WIFI_CHANNEL_MIN`

```c
#define WIFI_CHANNEL_MIN 1
```

```c
#include <zephyr/net/wifi.h>
```

最小信道编号（Minimum Channel Number）。

<a id="ga6766ef7bcb001f1fb526a4083b6cd8bc"></a>

### `WIFI_COUNTRY_CODE_LEN`

```c
#define WIFI_COUNTRY_CODE_LEN 2
```

```c
#include <zephyr/net/wifi.h>
```

国家代码字符串长度（Country Code String Length）。

<a id="gac6904487661f157274b0b60833f6684a"></a>

### `WIFI_ENT_IDENTITY_MAX_LEN`

```c
#define WIFI_ENT_IDENTITY_MAX_LEN 64
```

```c
#include <zephyr/net/wifi.h>
```

最大企业身份长度（Maximum Enterprise Identity Length）。

<a id="gae2fd55924f4078187431f7a1184f217f"></a>

### `WIFI_ENT_PSWD_MAX_LEN`

```c
#define WIFI_ENT_PSWD_MAX_LEN 128
```

```c
#include <zephyr/net/wifi.h>
```

最大企业密码长度（Maximum Enterprise Password Length）。

<a id="gaa6cbecd7d4197d453038d3da7ef6be7b"></a>

### `WIFI_INTERFACE_INDEX_MAX`

```c
#define WIFI_INTERFACE_INDEX_MAX 255
```

```c
#include <zephyr/net/wifi.h>
```

网络接口索引最大值（Network Interface Index Maximum）。

<a id="gaa1a74ef94af57a7ea966c691c065a46d"></a>

### `WIFI_INTERFACE_INDEX_MIN`

```c
#define WIFI_INTERFACE_INDEX_MIN 1
```

```c
#include <zephyr/net/wifi.h>
```

网络接口索引最小值（Network Interface Index Minimum）。

<a id="ga29409ff83a53c6464decdde9bdd04de6"></a>

### `WIFI_MAC_ADDR_LEN`

```c
#define WIFI_MAC_ADDR_LEN 6
```

```c
#include <zephyr/net/wifi.h>
```

MAC 地址长度（MAC address length）。

<a id="gad7c3b99c974b342935180a28fdc5ddfc"></a>

### `WIFI_PSK_MAX_LEN`

```c
#define WIFI_PSK_MAX_LEN 64
```

```c
#include <zephyr/net/wifi.h>
```

最大预共享密钥长度（Maximum PSK Length）。

<a id="gaa8e19abf8c85f237ba5033740ceff553"></a>

### `WIFI_PSK_MIN_LEN`

```c
#define WIFI_PSK_MIN_LEN 8
```

```c
#include <zephyr/net/wifi.h>
```

最小预共享密钥长度（Minimum PSK Length）。

<a id="ga7d6424d6770b2357f0b8abb456ae53fc"></a>

### `WIFI_PSK_PBKDF2_KEY_LEN`

```c
#define WIFI_PSK_PBKDF2_KEY_LEN 32
```

```c
#include <zephyr/net/wifi.h>
```

PBKDF2 密钥长度（Key Length）。

<a id="gab63fa744cc2e049cfd635ab0a187971f"></a>

### `WIFI_SAE_PSWD_MAX_LEN`

```c
#define WIFI_SAE_PSWD_MAX_LEN 128
```

```c
#include <zephyr/net/wifi.h>
```

最大 SAW 密码长度（Max SAW Password Length，原文写作 SAW）。

<a id="gad62c60666c9fdffe2e0e9c4388f87886"></a>

### `WIFI_SSID_MAX_LEN`

```c
#define WIFI_SSID_MAX_LEN 32
```

```c
#include <zephyr/net/wifi.h>
```

最大服务集标识符长度（Maximum SSID Length）。

<a id="ga1104c3c97b460f9f3e15a7a9c56e80af"></a>

### `WIFI_UTILS_MAX_BAND_STR_LEN`

```c
#define WIFI_UTILS_MAX_BAND_STR_LEN 3
```

```c
#include <zephyr/net/wifi_utils.h>
```

频段说明字符串（Band Specification String）的最大长度。

<a id="gaacc3c661affda7b376a4024efd645f0b"></a>

### `WIFI_UTILS_MAX_CHAN_STR_LEN`

```c
#define WIFI_UTILS_MAX_CHAN_STR_LEN 4
```

```c
#include <zephyr/net/wifi_utils.h>
```

信道说明字符串（Channel Specification String）的最大长度。

<a id="gaf466d0b11462b3f190d579702cb9ee51"></a>

### `WIFI_WEP_KEY_MAX_LEN`

```c
#define WIFI_WEP_KEY_MAX_LEN 26
```

```c
#include <zephyr/net/wifi.h>
```

最大 WEP 密钥长度（Maximum WEP Key Length）；WEP-104 为 26 个十六进制字符。

<a id="ga234d72d7c881e67ff49fb6c474c622e3"></a>

### `WIFI_WPS_PIN_MAX_LEN`

```c
#define WIFI_WPS_PIN_MAX_LEN 8
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 保护设置个人识别码（WPS PIN）的最大长度。

<a id="gad34b366f1c315207ce0da587ca96d8d8"></a>

### `scan_result_cb_t`

```c
typedef void(* scan_result_cb_t) (struct net_if *iface, int status, struct wifi_scan_result *entry)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

扫描结果回调（Scan Result Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 扫描结果状态（Scan Result Status）。 |
| `entry` | 扫描结果条目（Scan Result Entry）。 |

<a id="gac2638308cbb0d268831f1618cf8e1fa8"></a>

### `net_event_wifi_cmd`

```c
enum net_event_wifi_cmd
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理事件（Management Events）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |
| `NET_MGMT_CMD` | 扫描结果可用（Scan Results Available）；发现点对点设备（P2P Device Found）；认证请求方专用事件（Supplicant-specific Event）；STA 与 AP 断开；STA 连接 AP；AP 模式禁用结果；AP 模式启用结果；邻居报告完成（Neighbor Report Complete）；邻居报告（Neighbor Report）；信号变化事件（Signal Change Event）；断开连接完成；原始扫描结果可用；目标唤醒时间（TWT）睡眠状态，可为清醒或睡眠，应用可据此判断能否发送数据；TWT 事件；接口状态（Interface Status）；断开连接结果；连接结果；扫描完成。 |

<a id="ga99a55137188119f65f9d2bb4f57cac77"></a>

### `net_request_wifi_cmd`

```c
enum net_request_wifi_cmd
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理命令（Management Commands）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_REQUEST_WIFI_CMD_SCAN` | 扫描 Wi‑Fi 网络（Scan）。 |
| `NET_REQUEST_WIFI_CMD_CONNECT` | 连接 Wi‑Fi 网络（Connect）。 |
| `NET_REQUEST_WIFI_CMD_DISCONNECT` | 断开 Wi‑Fi 网络连接（Disconnect）。 |
| `NET_REQUEST_WIFI_CMD_AP_ENABLE` | 启用接入点模式（AP mode）。 |
| `NET_REQUEST_WIFI_CMD_AP_DISABLE` | 禁用接入点模式（AP mode）。 |
| `NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD` | 设置 AP 请求发送阈值（RTS Threshold）。 |
| `NET_REQUEST_WIFI_CMD_IFACE_STATUS` | 获取接口状态（Interface status）。 |
| `NET_REQUEST_WIFI_CMD_11K_CONFIG` | 设置或获取 802.11k 状态（11k Status）。 |
| `NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST` | 发送 802.11k 邻居请求（11k neighbor request）。 |
| `NET_REQUEST_WIFI_CMD_PS` | 设置省电状态（Power save status）。 |
| `NET_REQUEST_WIFI_CMD_TWT` | 建立或拆除目标唤醒时间流（TWT flow）。 |
| `NET_REQUEST_WIFI_CMD_BTWT` | 建立广播目标唤醒时间流（BTWT flow）。 |
| `NET_REQUEST_WIFI_CMD_PS_CONFIG` | 获取省电配置（Power save configuration）。 |
| `NET_REQUEST_WIFI_CMD_REG_DOMAIN` | 设置或获取监管域（Regulatory domain）。 |
| `NET_REQUEST_WIFI_CMD_MODE` | 设置或获取工作模式（Mode of Operation）。 |
| `NET_REQUEST_WIFI_CMD_PACKET_FILTER` | 设置或获取当前模式的数据包过滤器（Packet Filter）设置。 |
| `NET_REQUEST_WIFI_CMD_CHANNEL` | 设置或获取监听模式（Monitor Mode）或发送注入模式（TX-Injection Mode）的 Wi-Fi 信道。 |
| `NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT` | 使站点（STA）断开与接入点（AP）的连接。 |
| `NET_REQUEST_WIFI_CMD_VERSION` | 获取 Wi-Fi 驱动和固件版本（Driver and Firmware Versions）。 |
| `NET_REQUEST_WIFI_CMD_CONN_PARAMS` | 获取 Wi-Fi 最近一次连接参数（Latest Connection Parameters）。 |
| `NET_REQUEST_WIFI_CMD_RTS_THRESHOLD` | 设置请求发送阈值（RTS Threshold）。 |
| `NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM` | 配置接入点参数（AP parameter）。 |
| `NET_REQUEST_WIFI_CMD_CONFIG_PARAM` | 配置站点参数（STA parameter）。 |
| `NET_REQUEST_WIFI_CMD_DPP` | 设备配网协议操作（DPP Actions）。 |
| `NET_REQUEST_WIFI_CMD_NAN` | 邻居感知网络操作（NAN Actions）。 |
| `NET_REQUEST_WIFI_CMD_BTM_QUERY` | 基本服务集转换管理查询（BSS Transition Management Query）。 |
| `NET_REQUEST_WIFI_CMD_PMKSA_FLUSH` | 清空成对主密钥安全关联缓存条目（PMKSA cache entries）。 |
| `NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS` | 设置企业模式凭据（Enterprise Mode Credential）。 |
| `NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG` | 获取请求发送阈值（RTS Threshold）。 |
| `NET_REQUEST_WIFI_CMD_WPS_CONFIG` | Wi-Fi 保护设置配置（WPS Config）。 |
| `NET_REQUEST_WIFI_CMD_START_ROAMING` | 开始漫游（Roaming）。 |
| `NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE` | 邻居报告完成（Neighbor Report Complete）。 |
| `NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN` | 指定扫描（Specific Scan）。 |
| `NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG` | 接入点的 Wi-Fi 保护设置配置（AP WPS Config）。 |
| `NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD` | 配置基本服务集最大空闲周期（BSS Maximum Idle Period）。 |
| `NET_REQUEST_WIFI_CMD_BGSCAN` | 配置后台扫描（Background scanning）。 |
| `NET_REQUEST_WIFI_CMD_P2P_OPER` | Wi-Fi 直连／点对点操作（Wi-Fi Direct/P2P Operations）。 |

<a id="ga83546cf946a9123c563609e8903d9642"></a>

### `wifi_ap_config_param`

```c
enum wifi_ap_config_param
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 接入点模式配置参数（AP Mode Configuration Parameter）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY` | 用于 AP 模式配置参数 `ap_max_inactivity`。 |
| `WIFI_AP_CONFIG_PARAM_MAX_NUM_STA` | 用于 AP 模式配置参数 `max_num_sta`。 |
| `WIFI_AP_CONFIG_PARAM_BANDWIDTH` | 用于 AP 模式配置参数 `bandwidth`。 |
| `WIFI_AP_CONFIG_PARAM_HT_CAPAB` | 用于 AP 模式配置参数 `ht_capab`。 |
| `WIFI_AP_CONFIG_PARAM_VHT_CAPAB` | 用于 AP 模式配置参数 `vht_capab`。 |

<a id="gaaf730bf76adc06434c7ac63bf0417884"></a>

### `wifi_ap_status`

```c
enum wifi_ap_status
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 接入点模式结果码（AP Mode Result Codes）。

在 AP 模式启用或禁用结果事件中，叠加用于 `wifi_status`，提供详细状态（Detailed Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_STATUS_AP_SUCCESS` | AP 模式启用或禁用成功（Successful）。 |
| `WIFI_STATUS_AP_FAIL` | AP 模式启用或禁用失败：通用失败（Generic Failure）。 |
| `WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED` | AP 模式启用失败：不支持的信道（Channel Not Supported）。 |
| `WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED` | AP 模式启用失败：信道不允许（Channel Not Allowed）。 |
| `WIFI_STATUS_AP_SSID_NOT_ALLOWED` | AP 模式启用失败：SSID 不允许（SSID Not Allowed）。 |
| `WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED` | AP 模式启用失败：不支持的身份验证类型（Authentication Type Not Supported）。 |
| `WIFI_STATUS_AP_OP_NOT_SUPPORTED` | AP 模式启用失败：不支持的操作（Operation Not Supported）。 |
| `WIFI_STATUS_AP_OP_NOT_PERMITTED` | AP 模式启用失败：操作不被许可（Operation Not Permitted）。 |

<a id="gaacc27e95277622f56ef35e129aaac4d0"></a>

### `wifi_bgscan_type`

```c
enum wifi_bgscan_type
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 后台扫描实现（Background Scan Implementation）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_BGSCAN_NONE` | 无（None）：禁用后台扫描（Background Scan）。 |
| `WIFI_BGSCAN_SIMPLE` | 简单模式（Simple）：基于信号强度进行周期性扫描。 |
| `WIFI_BGSCAN_LEARN` | 学习网络使用的信道（Learn Channels），属于实验功能。 |

<a id="ga4fced9c3627d8f65d75e1651b11916b0"></a>

### `wifi_btm_query_reason`

```c
enum wifi_btm_query_reason
```

```c
#include <zephyr/net/wifi.h>
```

IEEE 802.11v 基本服务集转换管理查询原因（BTM Query Reasons，BSS Transition Management）。

参见 IEEE Std 802.11v-2011 表 7-43x：转换及转换查询原因表（Transition and Transition Query Reasons Table）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_BTM_QUERY_REASON_UNSPECIFIED` | 未指定（Unspecified）。 |
| `WIFI_BTM_QUERY_REASON_LOW_RSSI` | 接收信号强度指示较低（Low RSSI）。 |
| `WIFI_BTM_QUERY_REASON_LEAVING_ESS` | 离开扩展服务集（Leaving ESS）。 |

<a id="ga7f7b23ac019ca504a2006f0376735645"></a>

### `wifi_cipher_type`

```c
enum wifi_cipher_type
```

```c
#include <zephyr/net/wifi.h>
```

组密码与成对密码类型（Group Cipher and Pairwise Cipher Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WPA_CAPA_ENC_CCMP` | 结合 CBC-MAC 的 AES 计数器模式（CCMP-128）。 |
| `WPA_CAPA_ENC_GCMP` | 128 位伽罗瓦／计数器模式协议（Galois/Counter Mode Protocol）。 |
| `WPA_CAPA_ENC_GCMP_256` | 256 位伽罗瓦／计数器模式协议（Galois/Counter Mode Protocol）。 |

<a id="ga7ef91a39c2cc6bb454d870a8a80f8439"></a>

### `wifi_config_param`

```c
enum wifi_config_param
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 站点模式配置参数（STA Mode Configuration Parameter）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_CONFIG_PARAM_OKC` | 用于 STA 模式配置参数 OKC（机会式密钥缓存）。 |

<a id="gad98099584d2222ede93aba42b1fbaff0"></a>

### `wifi_config_ps_param_fail_reason`

```c
enum wifi_config_ps_param_fail_reason
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 省电错误码（Power Save Error Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_PARAM_FAIL_UNSPECIFIED` | 未指定的错误（Unspecified Error）。 |
| `WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL` | 命令执行失败（Command Execution Failed）。 |
| `WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED` | 不支持的参数（Parameter Not Supported）。 |
| `WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS` | 无法获取接口状态（Interface Status）。 |
| `WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED` | 设备未连接 AP（Not Connected）。 |
| `WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED` | 设备已经连接 AP（Already Connected）。 |
| `WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID` | 监听间隔超出范围（Listen Interval Out of Range）。 |
| `WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY` | 退出策略无效（Invalid Exit Strategy）。 |

<a id="ga86a5741e54aeb3e290142b0de217b8a8"></a>

### `wifi_conn_status`

```c
enum wifi_conn_status
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 连接结果代码（Connect Result Codes）。

在连接结果事件（Connect Result Event）中，叠加用于 `wifi_status`，提供详细状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_STATUS_CONN_SUCCESS` | 连接成功（Connection Successful）。 |
| `WIFI_STATUS_CONN_FAIL` | 连接失败：通用失败（Generic Failure）。 |
| `WIFI_STATUS_CONN_WRONG_PASSWORD` | 连接失败：密码错误（Wrong Password）。可以推测的四次握手（4-way Handshake）失败原因包括：1）密钥错误；2）EAPoL 帧丢失导致超时。原因 1 更有可能，因此向用户报告口令／密码错误（Wrong Passphrase/Password）。 |
| `WIFI_STATUS_CONN_TIMEOUT` | 连接超时（Connection Timed Out）。 |
| `WIFI_STATUS_CONN_AP_NOT_FOUND` | 连接失败：未找到 AP（AP Not Found）。 |
| `WIFI_STATUS_CONN_AUTH_REJECT` | 连接失败：AP 拒绝身份验证（Authentication Rejected）。身份验证帧中的 IEEE 802.11 状态码通过 `wifi_status` 的 `status_code` 字段报告。 |
| `WIFI_STATUS_CONN_ASSOC_REJECT` | 连接失败：AP 拒绝关联（Association Rejected）。关联／重新关联响应帧中的 IEEE 802.11 状态码通过 `wifi_status` 的 `status_code` 字段报告。 |
| `WIFI_STATUS_CONN_LAST_STATUS` | 最近一次连接状态（Last Connection Status）。 |
| `WIFI_STATUS_DISCONN_FIRST_STATUS` | 连接已断开状态（Connection Disconnected Status）。 |

<a id="gac782af0a60b202fd19597cabb7bd3a9a"></a>

### `wifi_disconn_reason`

```c
enum wifi_disconn_reason
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 断开连接原因码（Disconnect Reason Codes）。

在断开连接结果事件（Disconnect Result Event）中，叠加用于 `wifi_status`，提供详细原因。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_REASON_DISCONN_SUCCESS` | 成功（Success），将状态字段复用于表示原因（Reason）。 |
| `WIFI_REASON_DISCONN_UNSPECIFIED` | 未指定原因（Unspecified Reason）。 |
| `WIFI_REASON_DISCONN_USER_REQUEST` | 因用户请求断开连接（User Request）。 |
| `WIFI_REASON_DISCONN_AP_LEAVING` | 因 AP 离开断开连接（AP Leaving）。 |
| `WIFI_REASON_DISCONN_INACTIVITY` | 因无活动断开连接（Inactivity）。 |

<a id="ga218525a9d9ee64524f983e52d5767562"></a>

### `wifi_eap_tls_cipher_type`

```c
enum wifi_eap_tls_cipher_type
```

```c
#include <zephyr/net/wifi.h>
```

EAP TLS 密码类型（Cipher Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_EAP_TLS_NONE` | 使用 NONE 的 EAP TLS。 |
| `WIFI_EAP_TLS_ECC_P384` | 使用 ECDH 与 ECDSA、曲线为 p384 的 EAP TLS。 |
| `WIFI_EAP_TLS_RSA_3K` | 使用 ECDH 与 RSA、RSA 密钥大于 3K 的 EAP TLS。 |

<a id="ga92b6fa6755491c3bd61f895213d07331"></a>

### `wifi_eap_type`

```c
enum wifi_eap_type
```

```c
#include <zephyr/net/wifi.h>
```

EPA 方法类型（EPA Method Types，原文写作 EPA）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_EAP_TYPE_NONE` | 无 EPA 安全保护（No EPA Security）。译注：原文使用 EPA，保留其缩写；该组条目描述 EAP 方法。 |
| `WIFI_EAP_TYPE_GTC` | EPA GTC 安全（EPA GTC Security），参见 RFC 3748 第 5 节。译注：原文使用 EPA，保留其缩写。 |
| `WIFI_EAP_TYPE_TLS` | EPA TLS 安全（EPA TLS Security），参见 RFC 5216。译注：原文使用 EPA，保留其缩写。 |
| `WIFI_EAP_TYPE_TTLS` | EPA TTLS 安全（EPA TTLS Security），参见 RFC 5281。译注：原文使用 EPA，保留其缩写。 |
| `WIFI_EAP_TYPE_PEAP` | EPA PEAP 安全（EPA PEAP Security），参见 `draft-josefsson-pppext-eap-tls-eap-06.txt`。译注：原文使用 EPA，保留其缩写。 |
| `WIFI_EAP_TYPE_MSCHAPV2` | EPA MSCHAPV2 安全（EPA MSCHAPV2 Security），参见 `draft-kamath-pppext-eap-mschapv2-00.txt`。译注：原文使用 EPA，保留其缩写。 |

<a id="ga03ab29789adfe867c4ebaddc39482344"></a>

### `wifi_ext_capab`

```c
enum wifi_ext_capab
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

IEEE 802.11 扩展能力（Extended Capabilities）的位位置。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_EXT_CAPAB_20_40_COEX` | 支持 20/40 MHz 基本服务集共存管理（20/40 BSS Coexistence Management）。 |
| `WIFI_EXT_CAPAB_GLK` | 支持通用链路（General Link，GLK）。 |
| `WIFI_EXT_CAPAB_EXT_CHAN_SWITCH` | 支持扩展信道切换（Extended Channel Switching）。 |
| `WIFI_EXT_CAPAB_TIM_BROADCAST` | 支持流量指示映射广播（TIM Broadcast）。 |
| `WIFI_EXT_CAPAB_BSS_TRANSITION` | 支持基本服务集转换管理（BSS Transition Management）。 |

<a id="gaa60495242c66a3fac294886856121c1f"></a>

### `wifi_filter`

```c
enum wifi_filter
```

```c
#include <zephyr/net/wifi.h>
```

模式过滤器设置（Mode Filter Settings）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PACKET_FILTER_ALL` | 支持嗅探管理、数据和控制数据包（Management, Data and Control Packet Sniffing）。 |
| `WIFI_PACKET_FILTER_MGMT` | 仅支持嗅探管理数据包（Management Packets）。 |
| `WIFI_PACKET_FILTER_DATA` | 仅支持嗅探数据数据包（Data Packets）。 |
| `WIFI_PACKET_FILTER_CTRL` | 仅支持嗅探控制数据包（Control Packets）。 |

<a id="ga1e2f0439a322355fa7368ea880c9c15d"></a>

### `wifi_frequency_bands`

```c
enum wifi_frequency_bands
```

```c
#include <zephyr/net/wifi.h>
```

IEEE 802.11 工作频段（Operational Frequency Bands），并非穷举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_FREQ_BAND_2_4_GHZ` | 2.4 GHz 频段（Band）。 |
| `WIFI_FREQ_BAND_5_GHZ` | 5 GHz 频段（Band）。 |
| `WIFI_FREQ_BAND_6_GHZ` | 6 GHz 频段（Band），用于 Wi-Fi 6E，也扩展至 7 GHz。 |
| `WIFI_FREQ_BAND_SUB_1_GHZ` | 低于 1 GHz 的频段（Sub-1GHz Band），用于 Wi-Fi HaLow、802.11ah。 |
| `WIFI_FREQ_BAND_MAX` | 可用的最高频段（Highest Frequency Band）。 |
| `WIFI_FREQ_BAND_UNKNOWN` | 无效频段（Invalid Frequency Band）。 |

<a id="ga3b01cead3c2eb4581fe85e2aaaffbd49"></a>

### `wifi_frequency_bandwidths`

```c
enum wifi_frequency_bandwidths
```

```c
#include <zephyr/net/wifi.h>
```

IEEE 802.11 工作频率带宽（Operational Frequency Bandwidths），并非穷举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_FREQ_BANDWIDTH_20MHZ` | 20 MHz 带宽（Bandwidth）。 |
| `WIFI_FREQ_BANDWIDTH_40MHZ` | 40 MHz 带宽（Bandwidth）。 |
| `WIFI_FREQ_BANDWIDTH_80MHZ` | 80 MHz 带宽（Bandwidth）。 |
| `WIFI_FREQ_BANDWIDTH_1MHZ` | 1 MHz 带宽（Bandwidth），仅适用于低于 1 GHz 的信道。 |
| `WIFI_FREQ_BANDWIDTH_2MHZ` | 2 MHz 带宽（Bandwidth），仅适用于低于 1 GHz 的信道。 |
| `WIFI_FREQ_BANDWIDTH_4MHZ` | 4 MHz 带宽（Bandwidth），仅适用于低于 1 GHz 的信道。 |
| `WIFI_FREQ_BANDWIDTH_8MHZ` | 8 MHz 带宽（Bandwidth），仅适用于低于 1 GHz 的信道。 |
| `WIFI_FREQ_BANDWIDTH_MAX` | 可用的最高频率带宽（Highest Frequency Bandwidth）。 |
| `WIFI_FREQ_BANDWIDTH_UNKNOWN` | 无效频率带宽（Invalid Frequency Bandwidth）。 |

<a id="gaf84d5e1a68393483fc6063c06b8f26e0"></a>

### `wifi_group_mgmt_cipher_type`

```c
enum wifi_group_mgmt_cipher_type
```

```c
#include <zephyr/net/wifi.h>
```

组管理密码类型（Group Management Cipher Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WPA_CAPA_ENC_BIP` | 128 位广播／组播完整性协议的基于分组密码的消息认证码（Broadcast/Multicast Integrity Protocol Cipher-based Message Authentication Code）。 |
| `WPA_CAPA_ENC_BIP_GMAC_128` | 128 位广播／组播完整性协议的伽罗瓦消息认证码（Broadcast/Multicast Integrity Protocol Galois Message Authentication Code）。 |
| `WPA_CAPA_ENC_BIP_GMAC_256` | 256 位广播／组播完整性协议的伽罗瓦消息认证码（Broadcast/Multicast Integrity Protocol Galois Message Authentication Code）。 |

<a id="ga584f6239ac14e2bedc5e6bd72756423b"></a>

### `wifi_iface_mode`

```c
enum wifi_iface_mode
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 接口模式（Interface Modes）。

依据（Based on）：[wpa_supplicant 的 defs.h 定义](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_MODE_INFRA` | 基础设施站点模式（Infrastructure Station Mode）。 |
| `WIFI_MODE_IBSS` | 独立基本服务集／自组织站点模式（IBSS/Ad-hoc Station Mode）。 |
| `WIFI_MODE_AP` | 接入点模式（AP Mode）。 |
| `WIFI_MODE_P2P_GO` | 点对点组所有者模式（P2P Group Owner Mode）。 |
| `WIFI_MODE_P2P_GROUP_FORMATION` | 点对点组形成模式（P2P Group Formation Mode）。 |
| `WIFI_MODE_MESH` | 802.11s 网状网络模式（Mesh Mode）。 |

<a id="ga981961f747b919d61d3ccbd41e4508b4"></a>

### `wifi_iface_state`

```c
enum wifi_iface_state
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 接口状态（Interface States）。

依据（Based on）：[wpa_supplicant 的 defs.h 定义](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_STATE_DISCONNECTED` | 接口已断开连接（Disconnected）。 |
| `WIFI_STATE_INTERFACE_DISABLED` | 接口已通过管理操作禁用（Administratively Disabled）。 |
| `WIFI_STATE_INACTIVE` | 配置中没有已启用的网络（Enabled Networks）。 |
| `WIFI_STATE_SCANNING` | 接口正在扫描网络（Scanning）。 |
| `WIFI_STATE_AUTHENTICATING` | 正在与网络进行身份验证（Authentication）。 |
| `WIFI_STATE_ASSOCIATING` | 正在与网络进行关联（Association）。 |
| `WIFI_STATE_ASSOCIATED` | 已完成与网络的关联（Association Completed）。 |
| `WIFI_STATE_4WAY_HANDSHAKE` | 正在与网络执行四次握手（4-way Handshake）。 |
| `WIFI_STATE_GROUP_HANDSHAKE` | 正在与网络交换组密钥（Group Key Exchange）。 |
| `WIFI_STATE_COMPLETED` | 全部身份验证已完成（Authentication Completed），可以传输数据。 |

<a id="gabdb2a784d4727b71ab44cca04e422c62"></a>

### `wifi_link_mode`

```c
enum wifi_link_mode
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 链路工作模式（Link Operating Modes）。

依据（As per）：[Wi-Fi 的版本与代际](https://en.wikipedia.org/wiki/Wi-Fi#Versions_and_generations)。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_0` | 802.11，遗留版本（Legacy）。 |
| `WIFI_1` | 802.11b 标准（Standard）。 |
| `WIFI_2` | 802.11a 标准（Standard）。 |
| `WIFI_3` | 802.11g 标准（Standard）。 |
| `WIFI_4` | 802.11n 标准（Standard）。 |
| `WIFI_5` | 802.11ac 标准（Standard）。 |
| `WIFI_6` | 802.11ax 标准（Standard）。 |
| `WIFI_6E` | 802.11ax，6 GHz 频段（Band）。 |
| `WIFI_7` | 802.11be 标准（Standard）。 |

<a id="ga1f252da47d9650023d7fff6d08e49c76"></a>

### `wifi_mfp_options`

```c
enum wifi_mfp_options
```

```c
#include <zephyr/net/wifi.h>
```

IEEE 802.11w 管理帧保护（Management Frame Protection，MFP）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_MFP_DISABLE` | 禁用管理帧保护（MFP Disabled）。 |
| `WIFI_MFP_OPTIONAL` | 可选管理帧保护（MFP Optional）。 |
| `WIFI_MFP_REQUIRED` | 强制要求管理帧保护（MFP Required）。 |

<a id="gae129d0783276e662575af2314eef86cd"></a>

### `wifi_mgmt_op`

```c
enum wifi_mgmt_op
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

用于任意命令的通用获取／设置操作（Get/Set Operation）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_MGMT_GET` | 获取操作（Get Operation）。 |
| `WIFI_MGMT_SET` | 设置操作（Set Operation）。 |

<a id="ga4a9243eeb974111d6047fd3d8d9cbf35"></a>

### `wifi_operational_modes`

```c
enum wifi_operational_modes
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 工作模式（Operational Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_STA_MODE` | 启用站点模式设置（STA Mode）。 |
| `WIFI_MONITOR_MODE` | 启用监听模式设置（Monitor Mode）。 |
| `WIFI_TX_INJECTION_MODE` | 启用发送注入模式设置（TX Injection Mode）。 |
| `WIFI_PROMISCUOUS_MODE` | 启用混杂模式设置（Promiscuous Mode）。 |
| `WIFI_AP_MODE` | 启用接入点模式设置（AP Mode）。 |
| `WIFI_SOFTAP_MODE` | 启用软件接入点模式设置（SoftAP Mode）。 |

<a id="ga0fffeb57b68fb8cdef9d3d571368b8ca"></a>

### `wifi_ps`

```c
enum wifi_ps
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 省电状态（Power Save States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_DISABLED` | 禁用省电（Power Save Disabled）。 |
| `WIFI_PS_ENABLED` | 启用省电（Power Save Enabled）。 |

<a id="ga2d424d1711389fb784e916a87ff854b7"></a>

### `wifi_ps_exit_strategy`

```c
enum wifi_ps_exit_strategy
```

```c
#include <zephyr/net/wifi.h>
```

Wi‑Fi 省电退出策略（Power save exit strategy）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_EXIT_CUSTOM_ALGO` | 自定义算法（Custom Algorithm）：驱动／固件根据流量决定如何退出省电状态，例如发送省电轮询（PS-Poll）、完全退出省电，或两者混合。 |
| `WIFI_PS_EXIT_EVERY_TIM` | 每次收到流量指示映射（TIM）时退出省电，通常通过发送 QoS 空数据帧（QoS NULL）或其他任意数据帧，获取已缓存的流量。 |

<a id="gaffae7d2a754be5eb952ad2b83edad54c"></a>

### `wifi_ps_mode`

```c
enum wifi_ps_mode
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 省电模式（Power Save Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_MODE_LEGACY` | 遗留省电模式（Legacy Power Save Mode）。 |
| `WIFI_PS_MODE_WMM` | Wi-Fi 多媒体省电模式（WMM Power Save Mode）。 |

<a id="gabe45d132797047c098041331c8f6f912"></a>

### `wifi_ps_param_type`

```c
enum wifi_ps_param_type
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi省电参数（Power Save Parameters）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_PARAM_STATE` | 省电状态（Power save state）。 |
| `WIFI_PS_PARAM_LISTEN_INTERVAL` | 省电监听间隔（Power Save Listen Interval），单位为（短）信标间隔（Beacon Intervals）。 |
| `WIFI_PS_PARAM_WAKEUP_MODE` | 省电唤醒模式（Power Save Wakeup Mode）。 |
| `WIFI_PS_PARAM_MODE` | 省电模式（Power Save Mode）。 |
| `WIFI_PS_PARAM_EXIT_STRATEGY` | 退出省电策略（Power Save Exit Strategy）。 |
| `WIFI_PS_PARAM_TIMEOUT` | 省电超时（Power Save Timeout）。 |

<a id="gac7f907644847e905d67c709fa4afae7f"></a>

### `wifi_ps_wakeup_mode`

```c
enum wifi_ps_wakeup_mode
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 省电模式（Power Save Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_PS_WAKEUP_MODE_DTIM` | 基于投递流量指示消息的唤醒（DTIM-based Wakeup）。 |
| `WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL` | 基于监听间隔的唤醒（Listen Interval-based Wakeup）。 |

<a id="ga0cc87c00cbee0d0aca833119dbf0d74e"></a>

### `wifi_sap_iface_state`

```c
enum wifi_sap_iface_state
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 接入点状态（AP Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_SAP_IFACE_UNINITIALIZED` | 接口未初始化（Uninitialized）。 |
| `WIFI_SAP_IFACE_DISABLED` | 接口已禁用（Disabled）。 |
| `WIFI_SAP_IFACE_COUNTRY_UPDATE` | 正在更新国家代码（Country Code Update）。 |
| `WIFI_SAP_IFACE_ACS` | 正在自动选择信道（Automatic Channel Selection）。 |
| `WIFI_SAP_IFACE_HT_SCAN` | 正在进行高吞吐量扫描（HT Scan）。 |
| `WIFI_SAP_IFACE_DFS` | 正在进行动态频率选择（Dynamic Frequency Selection）。 |
| `WIFI_SAP_IFACE_NO_IR` | 所选信道不允许主动发射（Initiating Radiation）。 |
| `WIFI_SAP_IFACE_ENABLED` | 接口已启用（Enabled）。 |

<a id="gad30e29eda65ccafdbd7f11865937b8ea"></a>

### `wifi_scan_type`

```c
enum wifi_scan_type
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 扫描类型（Scanning Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_SCAN_TYPE_ACTIVE` | 主动扫描（Active Scanning），默认方式。 |
| `WIFI_SCAN_TYPE_PASSIVE` | 被动扫描（Passive Scanning）。 |

<a id="gadde31a04fa25ed805115c6b31854cd9c"></a>

### `wifi_security_type`

```c
enum wifi_security_type
```

```c
#include <zephyr/net/wifi.h>
```

IEEE 802.11 安全类型（Security Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_SECURITY_TYPE_NONE` | 无安全保护（No Security）。 |
| `WIFI_SECURITY_TYPE_PSK` | WPA2-PSK 安全（Security）。 |
| `WIFI_SECURITY_TYPE_PSK_SHA256` | WPA2-PSK-SHA256 安全（Security）。 |
| `WIFI_SECURITY_TYPE_SAE` | WPA3-SAE 安全（Security）。 |
| `WIFI_SECURITY_TYPE_SAE_HNP` | 使用试探循环（Hunting-and-pecking Loop）的 WPA3-SAE 安全。 |
| `WIFI_SECURITY_TYPE_SAE_H2E` | 使用哈希到元素（Hash-to-element）的 WPA3-SAE 安全。 |
| `WIFI_SECURITY_TYPE_SAE_AUTO` | 同时启用试探循环（Hunting-and-pecking Loop）和哈希到元素（Hash-to-element）的 WPA3-SAE 安全。 |
| `WIFI_SECURITY_TYPE_WAPI` | GB 15629.11-2003 WAPI 安全（Security）。 |
| `WIFI_SECURITY_TYPE_EAP` | 企业级 EAP 安全（Enterprise EAP）。 |
| `WIFI_SECURITY_TYPE_EAP_TLS` | 企业级 EAP TLS 安全（Enterprise EAP TLS）。 |
| `WIFI_SECURITY_TYPE_WEP` | 有线等效保密 WEP 安全（WEP Security）。 |
| `WIFI_SECURITY_TYPE_WPA_PSK` | WPA-PSK 安全（Security）。 |
| `WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL` | WPA/WPA2/WPA3 PSK 安全（Security）。 |
| `WIFI_SECURITY_TYPE_DPP` | 设备配网协议 DPP 安全（DPP Security）。 |
| `WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2` | 企业级 EAP PEAP MSCHAPV2 安全（Enterprise）。 |
| `WIFI_SECURITY_TYPE_EAP_PEAP_GTC` | 企业级 EAP PEAP GTC 安全（Enterprise）。 |
| `WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2` | 企业级 EAP TTLS MSCHAPV2 安全（Enterprise）。 |
| `WIFI_SECURITY_TYPE_EAP_PEAP_TLS` | 企业级 EAP PEAP 安全（Enterprise）。 |
| `WIFI_SECURITY_TYPE_FT_PSK` | 快速转换预共享密钥安全（FT-PSK Security）。 |
| `WIFI_SECURITY_TYPE_FT_SAE` | 快速转换对等实体同时认证安全（FT-SAE Security）。 |
| `WIFI_SECURITY_TYPE_FT_EAP` | 快速转换可扩展认证协议安全（FT-EAP Security）。 |
| `WIFI_SECURITY_TYPE_FT_EAP_SHA384` | FT-EAP-SHA384 安全（Security）。 |
| `WIFI_SECURITY_TYPE_SAE_EXT_KEY` | SAE 扩展密钥（Extended Key），使用依赖群组的哈希（Group-dependent Hashing）。 |
| `WIFI_SECURITY_TYPE_WEP_OPEN` | 采用开放系统身份验证（Open System Authentication）的 WEP 安全。 |
| `WIFI_SECURITY_TYPE_WEP_SHARED` | 采用共享密钥身份验证（Shared Key Authentication）的 WEP 安全。 |
| `WIFI_SECURITY_TYPE_OWE` | 机会式无线加密安全（Opportunistic Wireless Encryption，OWE）。 |
| `WIFI_SECURITY_TYPE_PSK_SHA384` | WPA2-PSK-SHA384 安全（Security）。 |
| `WIFI_SECURITY_TYPE_FT_PSK_SHA384` | FT-PSK-SHA384 安全（Security）。 |

<a id="ga97fa304f9a1db2294a93cccd4c93bcf6"></a>

### `wifi_twt_fail_reason`

```c
enum wifi_twt_fail_reason
```

```c
#include <zephyr/net/wifi.h>
```

目标唤醒时间错误码（TWT Error Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_FAIL_UNSPECIFIED` | 未指定的错误（Unspecified Error）。 |
| `WIFI_TWT_FAIL_CMD_EXEC_FAIL` | 命令执行失败（Command Execution Failed）。 |
| `WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED` | 不支持的操作（Operation Not Supported）。 |
| `WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS` | 无法获取接口状态（Interface Status）。 |
| `WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED` | 设备未连接 AP（Not Connected）。 |
| `WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB` | 对端不具备高效率能力（HE，即 802.11ax／Wi-Fi 6）。 |
| `WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB` | 对端不具备目标唤醒时间能力（TWT Capability）。 |
| `WIFI_TWT_FAIL_OPERATION_IN_PROGRESS` | 已有目标唤醒时间流（TWT Flow）正在进行。 |
| `WIFI_TWT_FAIL_INVALID_FLOW_ID` | 协商流标识符无效（Invalid Negotiated Flow ID）。 |
| `WIFI_TWT_FAIL_IP_NOT_ASSIGNED` | 尚未分配或配置 IP 地址（IP Address）。 |
| `WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS` | 流已存在（Flow Already Exists）。 |

<a id="ga695123cd534e2499f516a07fdc5cafa8"></a>

### `wifi_twt_negotiation_type`

```c
enum wifi_twt_negotiation_type
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 目标唤醒时间协商类型（TWT Negotiation Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_INDIVIDUAL` | 目标唤醒时间单独协商（TWT Individual Negotiation）。 |
| `WIFI_TWT_BROADCAST` | 目标唤醒时间广播协商（TWT Broadcast Negotiation）。 |
| `WIFI_TWT_WAKE_TBTT` | 目标唤醒时间唤醒 TBTT 协商（TWT Wake TBTT Negotiation）。 |

<a id="gad0e998aeb1b27c4f203ca76339d323a3"></a>

### `wifi_twt_operation`

```c
enum wifi_twt_operation
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 目标唤醒时间操作（Target Wake Time Operations，TWT）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_SETUP` | 目标唤醒时间建立操作（TWT Setup）。 |
| `WIFI_TWT_TEARDOWN` | 目标唤醒时间拆除操作（TWT Teardown）。 |

<a id="ga31c78afc89bfdc4b54cee177843f8022"></a>

### `wifi_twt_setup_cmd`

```c
enum wifi_twt_setup_cmd
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 目标唤醒时间建立命令（TWT Setup Commands）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_SETUP_CMD_REQUEST` | 目标唤醒时间建立请求（TWT Setup Request）。 |
| `WIFI_TWT_SETUP_CMD_SUGGEST` | 目标唤醒时间建立建议（TWT Setup Suggest），AP 可以修改参数。 |
| `WIFI_TWT_SETUP_CMD_DEMAND` | 目标唤醒时间建立要求（TWT Setup Demand），AP 不可修改参数。 |
| `WIFI_TWT_SETUP_CMD_GROUPING` | 目标唤醒时间建立分组（TWT Setup Grouping），对 TWT 流分组。 |
| `WIFI_TWT_SETUP_CMD_ACCEPT` | 目标唤醒时间建立接受（TWT Setup Accept），参数已被 AP 接受。 |
| `WIFI_TWT_SETUP_CMD_ALTERNATE` | 目标唤醒时间建立替代（TWT Setup Alternate），AP 建议替代参数。 |
| `WIFI_TWT_SETUP_CMD_DICTATE` | 目标唤醒时间建立指定（TWT Setup Dictate），参数由 AP 指定。 |
| `WIFI_TWT_SETUP_CMD_REJECT` | 目标唤醒时间建立拒绝（TWT Setup Reject），参数已被 AP 拒绝。 |

<a id="ga4d03aedac13ee4512d7717ac624f319a"></a>

### `wifi_twt_setup_resp_status`

```c
enum wifi_twt_setup_resp_status
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 目标唤醒时间协商状态（TWT Negotiation Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_RESP_RECEIVED` | 已收到 TWT 请求对应的响应（TWT Response）。 |
| `WIFI_TWT_RESP_NOT_RECEIVED` | 未收到 TWT 请求对应的响应（TWT Response）。 |

<a id="ga38c184ea35c02f304cccdf389ca6d552"></a>

### `wifi_twt_sleep_state`

```c
enum wifi_twt_sleep_state
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 目标唤醒时间睡眠状态（TWT Sleep States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_STATE_SLEEP` | 目标唤醒时间睡眠状态（TWT Sleep State）：睡眠。 |
| `WIFI_TWT_STATE_AWAKE` | 目标唤醒时间睡眠状态（TWT Sleep State）：清醒。 |

<a id="gad3709d07aaa3ed59b48f9dd7bd181989"></a>

### `wifi_twt_teardown_status`

```c
enum wifi_twt_teardown_status
```

```c
#include <zephyr/net/wifi.h>
```

Wi-Fi 目标唤醒时间拆除状态（TWT Teardown Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TWT_TEARDOWN_SUCCESS` | 目标唤醒时间拆除成功（TWT Teardown Success）。 |
| `WIFI_TWT_TEARDOWN_FAILED` | 目标唤醒时间拆除失败（TWT Teardown Failure）。 |

<a id="gafc901312b5988481b34d05a031d6c0db"></a>

### `wifi_wep_key_type`

```c
enum wifi_wep_key_type
```

```c
#include <zephyr/net/wifi.h>
```

WEP 密钥类型（Key Type），依据密钥长度（Key Length）确定。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_WEP_KEY_TYPE_UNKNOWN` | WEP 密钥类型未知或不适用（Unknown or Not Applicable）。 |
| `WIFI_WEP_KEY_TYPE_64` | WEP-64：40 位密钥（Key），使用 5 个 ASCII 字符或 10 个十六进制字符。 |
| `WIFI_WEP_KEY_TYPE_128` | WEP-128：104 位密钥（Key），使用 13 个 ASCII 字符或 26 个十六进制字符。 |

<a id="ga48fea1f0c7d2700cef47068f96c6b71a"></a>

### `wifi_wpa3_enterprise_type`

```c
enum wifi_wpa3_enterprise_type
```

```c
#include <zephyr/net/wifi.h>
```

WPA3 企业安全类型（WPA3 Enterprise Security Types）。

详情参见 [Wi-Fi 联盟 WPA3 规范 v3.4](https://www.wi-fi.org/file/wpa3-specification) 第 3 节（Section 3）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_WPA3_ENTERPRISE_NA` | 不采用 WPA3 企业模式（Enterprise），而采用 WPA2 企业模式或个人模式（Personal）。 |
| `WIFI_WPA3_ENTERPRISE_SUITEB` | WPA3 企业模式 Suite-B（PMFR + WPA3-Suite-B）。 |
| `WIFI_WPA3_ENTERPRISE_SUITEB_192` | WPA3 企业模式 Suite-B-192（PMFR + WPA3-Suite-B-192）。 |
| `WIFI_WPA3_ENTERPRISE_ONLY` | 仅 WPA3 企业模式（Enterprise Only），要求 PMFR，并禁用 WPA2-ENT。 |

<a id="ga4c36ae1a5171d3fbaeebf95c16be496d"></a>

### `wifi_wps_op`

```c
enum wifi_wps_op
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 保护设置操作（WPS Operation）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_WPS_PBC` | Wi-Fi 保护设置按钮配置（WPS PBC）。 |
| `WIFI_WPS_PIN_GET` | 获取 WPS PIN 码（PIN Number）。 |
| `WIFI_WPS_PIN_SET` | 设置 WPS PIN 码（PIN Number）。 |

<a id="ga44f875bf0d931b66d582f5dca2d65ed5"></a>

### `wifi_band_txt()`

```c
const char * wifi_band_txt ( enum wifi_frequency_bands band)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读频段名称（Frequency Band Name）的辅助函数。

<a id="ga7ff13294abf2dc27acbb3021afb2faee"></a>

### `wifi_bandwidth_txt()`

```c
const char * wifi_bandwidth_txt ( enum wifi_frequency_bandwidths bandwidth)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读频率带宽名称（Frequency Bandwidth Name）的辅助函数。

<a id="gac18305e124523b7cc9eb6adb05d987a8"></a>

### `wifi_conn_status_txt()`

```c
const char * wifi_conn_status_txt ( enum wifi_conn_status status)
```

```c
#include <zephyr/net/wifi.h>
```

根据状态码（Status Code）获取易读状态名称（Status Name）的辅助函数。

<a id="ga1bea051b0c184cb859f27b36e3593bf2"></a>

### `wifi_disconn_reason_txt()`

```c
const char * wifi_disconn_reason_txt ( enum wifi_disconn_reason reason)
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

用于获取易读的断开连接原因名称（Disconnect Reason Name）的辅助函数。

<a id="ga0d9d6e2150fb187025300904357f7b4d"></a>

### `wifi_link_mode_txt()`

```c
const char * wifi_link_mode_txt ( enum wifi_link_mode link_mode)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读链路模式名称（Link Mode Name）的辅助函数。

<a id="ga22354241197a9227fdba77e67d471f5c"></a>

### `wifi_mfp_txt()`

```c
const char * wifi_mfp_txt ( enum wifi_mfp_options mfp)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读管理帧保护名称（MFP Name）的辅助函数。

<a id="gadee15c6a492a8ee13bea43812debb5d9"></a>

### `wifi_mgmt_raise_ap_disable_result_event()`

```c
void wifi_mgmt_raise_ap_disable_result_event ( struct net_if * iface, enum wifi_ap_status status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理接入点模式禁用结果事件（AP Mode Disable Result Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | AP 模式禁用结果状态（Disable Result Status）。 |

<a id="ga67b52edeff76c2211b038f4aa90b8982"></a>

### `wifi_mgmt_raise_ap_enable_result_event()`

```c
void wifi_mgmt_raise_ap_enable_result_event ( struct net_if * iface, enum wifi_ap_status status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理接入点模式启用结果事件（AP Mode Enable Result Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | AP 模式启用结果状态（Enable Result Status）。 |

<a id="gac8f17f0aa3e426a5cdb731727b9b9ce3"></a>

### `wifi_mgmt_raise_ap_sta_connected_event()`

```c
void wifi_mgmt_raise_ap_sta_connected_event ( struct net_if * iface, struct wifi_ap_sta_info * sta_info )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理接入点模式站点已连接事件（AP Mode STA Connected Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `sta_info` | 站点信息（STA Information）。 |

<a id="ga49fb9c3908be61d847b31c99be6afc42"></a>

### `wifi_mgmt_raise_ap_sta_disconnected_event()`

```c
void wifi_mgmt_raise_ap_sta_disconnected_event ( struct net_if * iface, struct wifi_ap_sta_info * sta_info )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理接入点模式站点已断开事件（AP Mode STA Disconnected Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `sta_info` | 站点信息（STA Information）。 |

<a id="ga036416696b1e3bc458ddbaf07a08d69d"></a>

### `wifi_mgmt_raise_connect_result_event()`

```c
void wifi_mgmt_raise_connect_result_event ( struct net_if * iface, int status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理连接结果事件（Connect Result Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 连接结果状态（Connect Result Status）。 |

<a id="gabdf7753c247587eface6e829686d120c"></a>

### `wifi_mgmt_raise_connect_result_status_event()`

```c
void wifi_mgmt_raise_connect_result_status_event ( struct net_if * iface, const struct wifi_status * status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

带 IEEE 802.11 代码的 Wi-Fi 管理连接结果事件（Connect Result Event）。

如果已知导致失败的原始 IEEE 802.11 状态码或原因码（Status/Reason Code），应使用此函数代替 `wifi_mgmt_raise_connect_result_event()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 连接结果状态及代码（Connect Result Status and Codes）。 |

<a id="gaa75246d6dc55dada389c9d31e2607d5c"></a>

### `wifi_mgmt_raise_disconnect_complete_event()`

```c
void wifi_mgmt_raise_disconnect_complete_event ( struct net_if * iface, int status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理断开连接完成事件（Disconnect Complete Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 断开连接完成状态（Disconnect Complete Status）。 |

<a id="ga3b6edcf9b51afbf7a327d1a344bd7b87"></a>

### `wifi_mgmt_raise_disconnect_result_event()`

```c
void wifi_mgmt_raise_disconnect_result_event ( struct net_if * iface, int status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 断开连接结果状态（Disconnect Result Status）。 |

<a id="ga3f7c4f252ab9621fbf3b9bd937253858"></a>

### `wifi_mgmt_raise_disconnect_result_status_event()`

```c
void wifi_mgmt_raise_disconnect_result_status_event ( struct net_if * iface, const struct wifi_status * status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

带 IEEE 802.11 代码的 Wi-Fi 管理断开连接结果事件（Disconnect Result Event）。

如果已知导致断开连接的原始 IEEE 802.11 原因码（Reason Code），应使用此函数代替 `wifi_mgmt_raise_disconnect_result_event()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `status` | 断开连接结果状态及代码（Disconnect Result Status and Codes）。 |

<a id="ga7da6af0747bcba85f8afab30c92b5b43"></a>

### `wifi_mgmt_raise_iface_status_event()`

```c
void wifi_mgmt_raise_iface_status_event ( struct net_if * iface, struct wifi_iface_status * iface_status )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理接口状态事件（Interface Status Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `iface_status` | 接口状态（Interface status）。 |

<a id="ga71c99913bded844c4ca32ed9155bc470"></a>

### `wifi_mgmt_raise_raw_scan_result_event()`

```c
void wifi_mgmt_raise_raw_scan_result_event ( struct net_if * iface, struct wifi_raw_scan_result * raw_scan_info )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理原始扫描结果事件（Raw Scan Result Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `raw_scan_info` | 原始扫描结果（Raw Scan Result）。 |

<a id="ga39404d15243ca084b253cae8fc07e374"></a>

### `wifi_mgmt_raise_twt_event()`

```c
void wifi_mgmt_raise_twt_event ( struct net_if * iface, struct wifi_twt_params * twt_params )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理目标唤醒时间事件（TWT Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `twt_params` | 目标唤醒时间参数（TWT parameters）。 |

<a id="ga18f09a3196588b51d6c0644f82f639d7"></a>

### `wifi_mgmt_raise_twt_sleep_state()`

```c
void wifi_mgmt_raise_twt_sleep_state ( struct net_if * iface, int twt_sleep_state )
```

```c
#include <zephyr/net/wifi_mgmt.h>
```

Wi-Fi 管理目标唤醒时间睡眠状态事件（TWT Sleep State Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `twt_sleep_state` | 目标唤醒时间睡眠状态（TWT Sleep State）。 |

<a id="gad78536ce1f30accfa45f258b6bf8c73d"></a>

### `wifi_mode_txt()`

```c
const char * wifi_mode_txt ( enum wifi_iface_mode mode)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读接口模式名称（Interface Mode Name）的辅助函数。

<a id="ga034bfcd7891caeb31820579b5ee22a7b"></a>

### `wifi_ps_exit_strategy_txt()`

```c
const char * wifi_ps_exit_strategy_txt ( enum wifi_ps_exit_strategy ps_exit_strategy)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读省电退出策略名称（Power Save Exit Strategy Name）的辅助函数。

<a id="ga8b72e7989964963a25f42ed1dba240a0"></a>

### `wifi_ps_get_config_err_code_str()`

```c
const char * wifi_ps_get_config_err_code_str ( int16_t err_no)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/wifi.h>
```

获取易读省电错误码名称（Power Save Error Code Name）的辅助函数。

<a id="gadb21d49f64e04fba59433e51d5b3481c"></a>

### `wifi_ps_mode_txt()`

```c
const char * wifi_ps_mode_txt ( enum wifi_ps_mode ps_mode)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读省电模式名称（Power Save Mode Name）的辅助函数。

<a id="gafbeb5f7fa97fd2ba0c691da0f8853ef2"></a>

### `wifi_ps_txt()`

```c
const char * wifi_ps_txt ( enum wifi_ps ps_name)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读省电名称（Power Save Name）的辅助函数。

<a id="ga6fd645f891234136b3028574a0af9666"></a>

### `wifi_ps_wakeup_mode_txt()`

```c
const char * wifi_ps_wakeup_mode_txt ( enum wifi_ps_wakeup_mode ps_wakeup_mode)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读省电唤醒模式名称（Power Save Wakeup Mode Name）的辅助函数。

<a id="ga9bb9f658d7806e42b3ee351fb3e7dfa0"></a>

### `wifi_security_txt()`

```c
const char * wifi_security_txt ( enum wifi_security_type security)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读安全类型名称（Security Type Name）的辅助函数。

<a id="ga03d306912dc96178e21d3c82c104582f"></a>

### `wifi_state_txt()`

```c
const char * wifi_state_txt ( enum wifi_iface_state state)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读接口状态名称（Interface State Name）的辅助函数。

<a id="gab2e6a6e1d8358a8f34d67bd632709b3d"></a>

### `wifi_twt_get_err_code_str()`

```c
const char * wifi_twt_get_err_code_str ( int16_t err_no)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/wifi.h>
```

获取易读目标唤醒时间错误码名称（TWT Error Code Name）的辅助函数。

<a id="ga6a74e999d63ee491df68447219ef2a0d"></a>

### `wifi_twt_negotiation_type_txt()`

```c
const char * wifi_twt_negotiation_type_txt ( enum wifi_twt_negotiation_type twt_negotiation)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读目标唤醒时间协商类型名称（TWT Negotiation Type Name）的辅助函数。

<a id="gadb125925e851bf7569424cd4295e7712"></a>

### `wifi_twt_operation_txt()`

```c
const char * wifi_twt_operation_txt ( enum wifi_twt_operation twt_operation)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读目标唤醒时间操作名称（TWT Operation Name）的辅助函数。

<a id="gae3ca047cc6ef6b6a2e44ba6574d41a44"></a>

### `wifi_twt_setup_cmd_txt()`

```c
const char * wifi_twt_setup_cmd_txt ( enum wifi_twt_setup_cmd twt_setup)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读目标唤醒时间建立命令名称（TWT Setup Command Name）的辅助函数。

<a id="ga6fb496c072323dee6f09bfa44c42685f"></a>

### `wifi_utils_chan_to_band()`

```c
enum wifi_frequency_bands wifi_utils_chan_to_band ( uint16_t chan)
```

```c
#include <zephyr/net/wifi_utils.h>
```

获取信道所属频段（Frequency Band）。

不同频段的信道编号（Channel Numbers）并不唯一：`1–14` 在 2.4 GHz 和 6 GHz 频段都有效，5 GHz 与 6 GHz 在 `14` 以上的编号也有重叠。仅凭信道编号无法区分，所以返回匹配的最低频段。如果调用方已知无线电工作在 6 GHz 频段，就不得使用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要查找的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_FREQ_BAND_UNKNOWN` | 该信道在任何频段中都无效（Invalid）时。 |

**返回（Returns）**：返回值（Returns）：信道所属频段（Band）。

<a id="ga428896bb7947b4fb46bf240b5179c7a3"></a>

### `wifi_utils_chan_to_freq()`

```c
uint16_t wifi_utils_chan_to_freq ( enum wifi_frequency_bands band, uint16_t chan )
```

```c
#include <zephyr/net/wifi_utils.h>
```

将信道编号（Channel Number）转换为中心频率（Center Frequency）。

必须提供频段（Band），因为不同频段的信道编号并不唯一：`1–14` 在 2.4 GHz 和 6 GHz 频段都有效，5 GHz 与 6 GHz 在 `14` 以上的编号也有重叠。如果尚不知道频段，使用 `wifi_utils_chan_to_band()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `band` | 信道所属频段（Band）。 |
| `chan` | 要转换的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 信道在该频段中无效，或该频段不提供信道到频率的映射（Channel-to-frequency Mapping），例如 `WIFI_FREQ_BAND_SUB_1_GHZ`。 |

**返回（Returns）**：返回值（Returns）：中心频率（Center Frequency），单位为 MHz。

<a id="gaa9f346e3f44ad3441813a39bef559e2a"></a>

### `wifi_utils_freq_to_chan()`

```c
uint16_t wifi_utils_freq_to_chan ( uint16_t freq)
```

```c
#include <zephyr/net/wifi_utils.h>
```

将中心频率（Center Frequency）转换为信道编号（Channel Number）。

这是 `wifi_utils_chan_to_freq()` 的逆操作。无需提供频段，因为中心频率（Center Frequency）在各频段之间唯一。如果还需要频段，对结果使用 `wifi_utils_chan_to_band()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `freq` | 中心频率（Center frequency），单位为 MHz。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 该频率不是任何频段中的信道中心频率（Channel Center Frequency）。 |

**返回（Returns）**：返回值（Returns）：信道编号（Channel Number）。

<a id="ga4c91cd7dff0fd9e5402970f3222dc20d"></a>

### `wifi_utils_parse_scan_bands()`

```c
int wifi_utils_parse_scan_bands ( char * scan_bands_str, uint8_t * band_map )
```

```c
#include <zephyr/net/wifi_utils.h>
```

将频段说明字符串（Band Specification String）转换为表示频段的位图（Bitmap）。

此函数解析以逗号分隔的 Wi-Fi 频段值字符串（Frequency Band String），并将其转换为位图（Bitmap）。字符串可使用以下字符表示频段：

- `2`：2.4 GHz 频段（Band）。
- `5`：5 GHz 频段（Band）。
- `6`：6 GHz 频段（Band）。

生成位图（Bitmap）中各频段的位位置参见 `wifi_frequency_bands`。

例如，字符串 `"2,5,6"` 转换为位图值（Bitmap Value）`0x7`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `scan_bands_str` | 字符串（String）。译注：原文在“String which spe.”处截断，未提供完整参数说明。 |
| `band_map` | 指向待更新位图变量（Bitmap Variable）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时的值（Value）。译注：原文只写“value in case of failure”，未在此说明具体数值。 |

<a id="gaba9f3117bcef9da1efc1841d3bd9adfd"></a>

### `wifi_utils_parse_scan_chan()`

```c
int wifi_utils_parse_scan_chan ( char * scan_chan_str, struct wifi_band_channel * chan, uint8_t max_channels )
```

```c
#include <zephyr/net/wifi_utils.h>
```

将包含扫描信道说明（Scan Channel Specification）的字符串转换为数组。

此函数解析指定待扫描信道的字符串，并将其转换为数组（Array）。

信道字符串（Channel String）必须按下述方式使用冒号 `:`、逗号 `,`、连字符 `-` 和下划线 `_` 分隔符进行格式化：

- 冒号（Colon）将其前面的值标识为频段。频段值必须位于该频段的信道之前，例如 `2:`；其中 `2` 表示 2.4 GHz，`5` 表示 5 GHz，`6` 表示 6 GHz。
- 连字符（Hyphen）`-` 用于表示信道范围，例如 `2-7`、`32-48`。
- 逗号（Comma）用于分隔同一频段内的信道值。信道可以单独指定，例如 `2,6,48`，也可以用连字符指定范围，例如 `1-14`、`32-48`。
- 下划线（Underscore）`_` 用于分隔多组频段与信道集合，例如 `2:1,2_5:36,40`。
- 任何位置都不得出现空格（Spaces），包括逗号前后、连字符前后等。

同时指定 2.4 GHz 和 5 GHz 频段信道的示例（Channel Specification）：`2:1,5,7,9-11_5:36-48,100,163-167`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `scan_chan_str` | 按上述格式表示的信道列表（Channel List）。 |
| `chan` | 指向数组（Array）的指针，用于保存解析出的信道。 |
| `max_channels` | 可保存的最大信道数量（Maximum Number of Channels）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时的值（Value）。译注：原文只写“value in case of failure”，未在此说明具体数值。 |

<a id="ga471a96d3fb6d610a591508b52d4c05a4"></a>

### `wifi_utils_parse_scan_ssids()`

```c
int wifi_utils_parse_scan_ssids ( char * scan_ssids_str, const char * ssids[], uint8_t num_ssids )
```

```c
#include <zephyr/net/wifi_utils.h>
```

将包含 SSID 的字符串追加到 SSID 字符串数组（String Array）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `scan_ssids_str` | 要追加到待扫描 SSID 列表的字符串（String）。 |
| `ssids` | 指向数组（Array）的指针，用于保存 SSID 指针。 |
| `num_ssids` | 可保存的最大 SSID 数量（Maximum Number of SSIDs）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时的值（Value）。译注：原文只写“value in case of failure”，未在此说明具体数值。 |

<a id="gaf1872d0ed2efd3737a36dcc0ab13f18e"></a>

### `wifi_utils_validate_chan()`

```c
bool wifi_utils_validate_chan ( uint8_t band, uint16_t chan )
```

```c
#include <zephyr/net/wifi_utils.h>
```

根据频段（Band）验证信道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `band` | 用于验证信道的频段（Band）。 |
| `chan` | 要验证的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 信道对该频段有效（Valid）时。 |
| `false` | 信道对该频段无效（Invalid）时。 |

<a id="gaf408ba9f75354d3eca735b4804fdf199"></a>

### `wifi_utils_validate_chan_2g()`

```c
bool wifi_utils_validate_chan_2g ( uint16_t chan)
```

```c
#include <zephyr/net/wifi_utils.h>
```

按 2.4 GHz 频段（Band）验证信道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要验证的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 信道对该频段有效（Valid）时。 |
| `false` | 信道对该频段无效（Invalid）时。 |

<a id="gae013eee6d6b74126c29d6ca7b2036310"></a>

### `wifi_utils_validate_chan_5g()`

```c
bool wifi_utils_validate_chan_5g ( uint16_t chan)
```

```c
#include <zephyr/net/wifi_utils.h>
```

按 5 GHz 频段（Band）验证信道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要验证的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 信道对该频段有效（Valid）时。 |
| `false` | 信道对该频段无效（Invalid）时。 |

<a id="ga2606742e23f48da5ca1660aeac47888b"></a>

### `wifi_utils_validate_chan_6g()`

```c
bool wifi_utils_validate_chan_6g ( uint16_t chan)
```

```c
#include <zephyr/net/wifi_utils.h>
```

按 6 GHz 频段（Band）验证信道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要验证的信道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 信道对该频段有效（Valid）时。 |
| `false` | 信道对该频段无效（Invalid）时。 |

<a id="gaf957fd93d98988347e009038cb694c04"></a>

### `wifi_wep_key_type_txt()`

```c
const char * wifi_wep_key_type_txt ( enum wifi_wep_key_type wep_key_type)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读 WEP 密钥类型名称（WEP Key Type Name）的辅助函数。

<a id="gaf67f2900be88fdf3f282400d09f2ab88"></a>

### `wifi_wpa3_enterprise_txt()`

```c
const char * wifi_wpa3_enterprise_txt ( enum wifi_wpa3_enterprise_type wpa3_ent)
```

```c
#include <zephyr/net/wifi.h>
```

获取易读 WPA3 企业安全类型名称（WPA3 Enterprise Security Type Name）的辅助函数。


## 1.10\_原页交叉引用（Cross References）

- [ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）](../api_usb_gnss_topic_reference/P008_ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）.md)
- [wifi.h](../api_file_network_pcie_reference/P015_zephyr__net__wifi.h_文件参考.md)
- [wifi_certs.h](../api_file_network_device_reference/P043_zephyr__net__wifi_certs.h_文件参考.md)
- [wifi_mgmt.h](../api_file_mesh_acpi_reference/P009_zephyr__net__wifi_mgmt.h_文件参考.md)
- [wifi_utils.h](../api_file_protocol_service_reference/P034_zephyr__net__wifi_utils.h_文件参考.md)
- [wifi_cipher_desc](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md)
- [wifi_eap_cipher_config](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md)
- [wifi_eap_config](../network_core_model_reference/P172_wifi_eap_config_结构体.md)
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
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [RFC 3748, section-5](https://datatracker.ietf.org/doc/html/rfc3748#section-5)
- [RFC 5216](https://datatracker.ietf.org/doc/html/rfc5216)
- [RFC 5281](https://datatracker.ietf.org/doc/html/rfc5281)
- [https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)
- [https://en.wikipedia.org/wiki/Wi-Fi#Versions_and_generations](https://en.wikipedia.org/wiki/Wi-Fi#Versions_and_generations)
- [https://www.wi-fi.org/file/wpa3-specification](https://www.wi-fi.org/file/wpa3-specification)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178"></a>
<a id="gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833"></a>
<a id="gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c"></a>
<a id="gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958"></a>
<a id="gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7"></a>
<a id="gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199"></a>
<a id="gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca"></a>
<a id="ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe"></a>
<a id="ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9"></a>
<a id="ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe"></a>
<a id="ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911"></a>
<a id="gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58"></a>
<a id="gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257"></a>
<a id="gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49"></a>
<a id="gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1"></a>
<a id="gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d"></a>
<a id="gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4"></a>
<a id="gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f"></a>
<a id="ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f"></a>
<a id="gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18"></a>
<a id="ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042"></a>
<a id="ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c"></a>
<a id="ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7"></a>
<a id="ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204"></a>
<a id="ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6"></a>
<a id="gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df"></a>
<a id="gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9"></a>
<a id="gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f"></a>
<a id="gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f"></a>
<a id="gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68"></a>
<a id="gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7"></a>
<a id="gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e"></a>
<a id="gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056"></a>
<a id="gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba"></a>
<a id="ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b"></a>
<a id="ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc"></a>
<a id="ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244"></a>
<a id="ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5"></a>
<a id="gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90"></a>
<a id="gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d"></a>
<a id="ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8"></a>
<a id="ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70"></a>
<a id="ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521"></a>
<a id="gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e"></a>
<a id="gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6"></a>
<a id="ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934"></a>
<a id="gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969"></a>
<a id="gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf"></a>
<a id="gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840"></a>
<a id="ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd"></a>
<a id="ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd"></a>
<a id="gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623"></a>
<a id="gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82"></a>
<a id="gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47"></a>
<a id="gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5"></a>
<a id="gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832"></a>
<a id="ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd"></a>
<a id="ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5"></a>
<a id="ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d"></a>
<a id="ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90"></a>
<a id="ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8"></a>
<a id="ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab"></a>
<a id="ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03"></a>
<a id="ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29"></a>
<a id="ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6"></a>
<a id="ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a"></a>
<a id="gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda"></a>
<a id="ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9"></a>
<a id="ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814"></a>
<a id="ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee"></a>
<a id="gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c"></a>
<a id="gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0"></a>
<a id="gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa"></a>
<a id="gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978"></a>
<a id="ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45"></a>
<a id="ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3"></a>
<a id="gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565"></a>
<a id="gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286"></a>
<a id="gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72"></a>
<a id="gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c"></a>
<a id="gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0"></a>
<a id="ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965"></a>
<a id="ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d"></a>
<a id="ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104"></a>
<a id="ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484"></a>
<a id="ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f"></a>
<a id="gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1"></a>
<a id="gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589"></a>
<a id="gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa"></a>
<a id="gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa"></a>
<a id="gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88"></a>
<a id="gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d"></a>
<a id="gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md)
