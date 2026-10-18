---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-9
title: 蜂窝通信（Cellular）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_蜂窝通信（Cellular）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝调制解调器（Cellular modems）接口。

<a id="details"></a>

蜂窝调制解调器接口（Cellular Modem Interfaces）。自 3.6 引入，版本 0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 9.1\_主题（Topics）

<a id="r_cellular_5Finterface_5Fbackend"></a>

相关声明：[蜂窝通信驱动后端 API（Cellular Driver Backend API）](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md)。

<a id="r_cellular_5Finterface_5Fext"></a>

相关声明：[设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）](../api_topic_reference/P015_设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 9.2\_文件（Files）

<a id="r_cellular_2Eh"></a>

```c
file cellular.h
```

相关声明：[cellular.h](../api_file_signal_device_reference/P004_zephyr__drivers__cellular.h_文件参考.md)。

蜂窝调制解调器（Cellular Modem）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.3\_数据结构（Data Structures）

<a id="r_cellular_5Fnetwork"></a>

```c
struct cellular_network
```

相关声明：[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)。

蜂窝网络（Cellular Network）结构。

<a id="r_cellular_5Fevt_5Fmodem_5Finfo"></a>

```c
struct cellular_evt_modem_info
```

相关声明：[cellular_evt_modem_info](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md)。

CELLULAR_EVENT_MODEM_INFO_CHANGED事件的载荷（Payload）。

<a id="r_cellular_5Fevt_5Fregistration_5Fstatus"></a>

```c
struct cellular_evt_registration_status
```

相关声明：[cellular_evt_registration_status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md)。

CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED事件的载荷（Payload）。

<a id="r_cellular_5Fevt_5Fmodem_5Fcomms_5Fcheck_5Fresult"></a>

```c
struct cellular_evt_modem_comms_check_result
```

相关声明：[cellular_evt_modem_comms_check_result](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md)。

CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT事件的载荷（Payload）。

<a id="r_cellular_5Fevt_5Fnetwork_5Fstatus"></a>

```c
struct cellular_evt_network_status
```

相关声明：[cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)。

CELLULAR_EVENT_NETWORK_STATUS_CHANGED事件的载荷（Payload）。

<a id="r_cellular_5Fstats"></a>

```c
struct cellular_stats
```

相关声明：[cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)。

蜂窝链路（Cellular Link）的运行统计信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.4\_宏定义（Macros）

<a id="r_ga47b3cae8fd86f6cec69cda46b8e70be4"></a>

```c
#define CELLULAR_EUTRAN_CELL_ID_MAX 0xFFFFFFFU
```

相关声明：[CELLULAR_EUTRAN_CELL_ID_MAX](#ga47b3cae8fd86f6cec69cda46b8e70be4)。

演进通用陆地无线接入网全局小区标识符（E-UTRAN Global Cell Identifier，GCI）为 28 位值。

<a id="r_ga08556787615b6f43d8f162ec5da69653"></a>

```c
#define CELLULAR_EUTRAN_CELL_ID_INVALID UINT32_MAX
```

相关声明：[CELLULAR_EUTRAN_CELL_ID_INVALID](#ga08556787615b6f43d8f162ec5da69653)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

未知 E-UTRAN 全局小区标识符（GCI）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.5\_类型定义（Typedefs）

<a id="r_ga84efd3405e5233358514c7d634710042"></a>

```c
typedef uint32_t cellular_event_mask_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[cellular_event_mask_t](#ga84efd3405e5233358514c7d634710042)。

<a id="r_gac9d02d18ed6e0af07e480cde678afdc1"></a>

```c
typedef void(* cellular_event_cb_t) (const struct device *dev, enum cellular_event event, const void *payload, void *user_data)
```

相关声明：[cellular_event_cb_t](#gac9d02d18ed6e0af07e480cde678afdc1)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event](#ga27c0b71128c782a7f42832b82eb94411)。

蜂窝事件回调（Cellular Event Callback）原型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.6\_枚举（Enumerations）

<a id="r_ga168002533ce39996e68bda2c2e92428e"></a>

```c
enum cellular_access_technology { CELLULAR_ACCESS_TECHNOLOGY_GSM = 0 , CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT = 1 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN = 2 , CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS = 3 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA = 4 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA = 5 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA = 6 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN = 7 , CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT = 8 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1 = 9 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN = 10 , CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN = 11 , CELLULAR_ACCESS_TECHNOLOGY_NG_RAN = 12 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL = 13 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT = 14 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT = 15 , CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT = 16 , CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN = 255 }
```

相关声明：[cellular_access_technology](#ga168002533ce39996e68bda2c2e92428e)、[CELLULAR_ACCESS_TECHNOLOGY_GSM](#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255)、[CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT](#gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN](#gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c)、[CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS](#gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA](#gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA](#gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA](#gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN](#gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1)、[CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT](#gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1](#gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN](#gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f)、[CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN](#gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37)、[CELLULAR_ACCESS_TECHNOLOGY_NG_RAN](#gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL](#gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT](#gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT](#gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de)、[CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT](#gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383)、[CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN](#gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117)。

蜂窝接入技术（Cellular Access Technologies），参见 3GPP TS 27.007 的 AcT。

<a id="r_ga746c0862b9a5da7c766e42e4d6025f47"></a>

```c
enum cellular_signal_type { CELLULAR_SIGNAL_RSSI , CELLULAR_SIGNAL_RSRP , CELLULAR_SIGNAL_RSRQ }
```

相关声明：[cellular_signal_type](#ga746c0862b9a5da7c766e42e4d6025f47)、[CELLULAR_SIGNAL_RSSI](#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a)、[CELLULAR_SIGNAL_RSRP](#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a)、[CELLULAR_SIGNAL_RSRQ](#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338)。

蜂窝信号类型（Cellular Signal Type）。

<a id="r_gad6e38e31d82075c51933fcbb2ff2de30"></a>

```c
enum cellular_modem_info_type { CELLULAR_MODEM_INFO_IMEI , CELLULAR_MODEM_INFO_MODEL_ID , CELLULAR_MODEM_INFO_MANUFACTURER , CELLULAR_MODEM_INFO_FW_VERSION , CELLULAR_MODEM_INFO_SIM_IMSI , CELLULAR_MODEM_INFO_SIM_ICCID , CELLULAR_MODEM_INFO_SERIAL_NUMBER }
```

相关声明：[cellular_modem_info_type](#gad6e38e31d82075c51933fcbb2ff2de30)、[CELLULAR_MODEM_INFO_IMEI](#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de)、[CELLULAR_MODEM_INFO_MODEL_ID](#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8)、[CELLULAR_MODEM_INFO_MANUFACTURER](#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1)、[CELLULAR_MODEM_INFO_FW_VERSION](#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027)、[CELLULAR_MODEM_INFO_SIM_IMSI](#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245)、[CELLULAR_MODEM_INFO_SIM_ICCID](#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)、[CELLULAR_MODEM_INFO_SERIAL_NUMBER](#ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed)。

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

<a id="r_ga7309390ed507748fdb72cf078b8e08a4"></a>

```c
enum cellular_registration_status { CELLULAR_REGISTRATION_NOT_REGISTERED = 0 , CELLULAR_REGISTRATION_REGISTERED_HOME = 1 , CELLULAR_REGISTRATION_SEARCHING = 2 , CELLULAR_REGISTRATION_DENIED = 3 , CELLULAR_REGISTRATION_UNKNOWN = 4 , CELLULAR_REGISTRATION_REGISTERED_ROAMING = 5 , CELLULAR_REGISTRATION_SMS_ONLY_HOME = 6 , CELLULAR_REGISTRATION_SMS_ONLY_ROAMING = 7 , CELLULAR_REGISTRATION_EMERGENCY_ONLY = 8 , CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME = 9 , CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING = 10 , CELLULAR_REGISTRATION_RLOS = 11 }
```

相关声明：[cellular_registration_status](#ga7309390ed507748fdb72cf078b8e08a4)、[CELLULAR_REGISTRATION_NOT_REGISTERED](#gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27)、[CELLULAR_REGISTRATION_REGISTERED_HOME](#gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe)、[CELLULAR_REGISTRATION_SEARCHING](#gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175)、[CELLULAR_REGISTRATION_DENIED](#gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e)、[CELLULAR_REGISTRATION_UNKNOWN](#gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1)、[CELLULAR_REGISTRATION_REGISTERED_ROAMING](#gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d)、[CELLULAR_REGISTRATION_SMS_ONLY_HOME](#gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b)、[CELLULAR_REGISTRATION_SMS_ONLY_ROAMING](#gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27)、[CELLULAR_REGISTRATION_EMERGENCY_ONLY](#gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3)、[CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME](#gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252)、[CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING](#gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97)、[CELLULAR_REGISTRATION_RLOS](#gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b)。

蜂窝注册状态（Cellular Registration Status），参见 3GPP TS 27.007。

<a id="r_ga27c0b71128c782a7f42832b82eb94411"></a>

```c
enum cellular_event { CELLULAR_EVENT_MODEM_INFO_CHANGED = BIT(0) , CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED = BIT(1) , CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT = BIT(2) , CELLULAR_EVENT_NETWORK_STATUS_CHANGED = BIT(3) , CELLULAR_EVENT_MODEM_SUSPENDED = BIT(4) }
```

相关声明：[cellular_event](#ga27c0b71128c782a7f42832b82eb94411)、[CELLULAR_EVENT_MODEM_INFO_CHANGED](#gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb)、[CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED](#gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a)、[CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT](#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)、[CELLULAR_EVENT_NETWORK_STATUS_CHANGED](#gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99)、[CELLULAR_EVENT_MODEM_SUSPENDED](#gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c)。

蜂窝驱动异步发出的事件（Asynchronous Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.7\_函数（Functions）

<a id="r_gaa53d52e58221c998eec272a4d063bdd4"></a>

```c
static int cellular_configure_networks (const struct device *dev, const struct cellular_network *networks, uint8_t size)
```

相关声明：[cellular_configure_networks](#gaa53d52e58221c998eec272a4d063bdd4)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为设备配置蜂窝网络（Cellular Networks）。

<a id="r_ga70340d22df56665b1d113abc8b314a95"></a>

```c
static int cellular_get_supported_networks (const struct device *dev, const struct cellular_network **networks, uint8_t *size)
```

相关声明：[cellular_get_supported_networks](#ga70340d22df56665b1d113abc8b314a95)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取设备支持的蜂窝网络（Cellular Networks）。

<a id="r_ga022eb4eecc300b14110107a46824cac0"></a>

```c
static int cellular_get_signal (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[cellular_get_signal](#ga022eb4eecc300b14110107a46824cac0)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取设备信号（Signal）。

<a id="r_ga757f0802fd72d61d035a81057f23d5ca"></a>

```c
static int cellular_get_modem_info (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[cellular_get_modem_info](#ga757f0802fd72d61d035a81057f23d5ca)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](#gad6e38e31d82075c51933fcbb2ff2de30)。

获取设备调制解调器信息（Modem Info）。

<a id="r_gae0ca6816f75b89055aa31370196e2c98"></a>

```c
static int cellular_get_registration_status (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[cellular_get_registration_status](#gae0ca6816f75b89055aa31370196e2c98)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](#ga7309390ed507748fdb72cf078b8e08a4)。

获取设备的网络注册状态（Network Registration Status）。

<a id="r_gad1e37b428eaacc7442f6a6cb2e1404a5"></a>

```c
static int cellular_get_network_status (const struct device *dev, struct cellular_evt_network_status *status)
```

相关声明：[cellular_get_network_status](#gad1e37b428eaacc7442f6a6cb2e1404a5)、[device](../device_reference/P002_设备对象结构.md)、[cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)。

获取最近报告的网络状态，即服务小区状态（Serving Cell Status）。

<a id="r_ga4494e4d41149ea48fd1e0d8fe9b441dd"></a>

```c
static int cellular_set_apn (const struct device *dev, const char *apn)
```

相关声明：[cellular_set_apn](#ga4494e4d41149ea48fd1e0d8fe9b441dd)、[device](../device_reference/P002_设备对象结构.md)。

设置分组数据协议（PDP）上下文使用的接入点名称（APN）。

<a id="r_ga7b6e210b9e5222b789af52b4ef8cc850"></a>

```c
static int cellular_set_callback (const struct device *dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void *user_data)
```

相关声明：[cellular_set_callback](#ga7b6e210b9e5222b789af52b4ef8cc850)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event_mask_t](#ga84efd3405e5233358514c7d634710042)、[cellular_event_cb_t](#gac9d02d18ed6e0af07e480cde678afdc1)。

订阅异步蜂窝事件（Asynchronous Cellular Events）。

<a id="r_ga12d74b4ec0821f5eed95f24350789ed3"></a>

```c
static const struct cellular_stats * cellular_get_stats (const struct device *dev)
```

相关声明：[cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)、[cellular_get_stats](#ga12d74b4ec0821f5eed95f24350789ed3)、[device](../device_reference/P002_设备对象结构.md)。

从蜂窝设备读取运行统计（Operational Statistics）。

<a id="r_ga2ae42cd17e07ca8e24aa75352c07e5fe"></a>

```c
int cellular_modem_pause_periodic_script (const struct device *dev)
```

相关声明：[cellular_modem_pause_periodic_script](#ga2ae42cd17e07ca8e24aa75352c07e5fe)、[device](../device_reference/P002_设备对象结构.md)。

暂停 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。

<a id="r_ga5dc375b9ab33b2468846b8ca77a2106b"></a>

```c
int cellular_modem_resume_periodic_script (const struct device *dev)
```

相关声明：[cellular_modem_resume_periodic_script](#ga5dc375b9ab33b2468846b8ca77a2106b)、[device](../device_reference/P002_设备对象结构.md)。

恢复 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。

## 9.8\_详细说明（Detailed Documentation）

<a id="ga08556787615b6f43d8f162ec5da69653"></a>

### `CELLULAR_EUTRAN_CELL_ID_INVALID`

```c
#define CELLULAR_EUTRAN_CELL_ID_INVALID UINT32_MAX
```

```c
#include <zephyr/drivers/cellular.h>
```

未知 E-UTRAN 全局小区标识符（GCI）。

<a id="ga47b3cae8fd86f6cec69cda46b8e70be4"></a>

### `CELLULAR_EUTRAN_CELL_ID_MAX`

```c
#define CELLULAR_EUTRAN_CELL_ID_MAX 0xFFFFFFFU
```

```c
#include <zephyr/drivers/cellular.h>
```

演进通用陆地无线接入网全局小区标识符（E-UTRAN Global Cell Identifier，GCI）为 28 位值。

<a id="gac9d02d18ed6e0af07e480cde678afdc1"></a>

### `cellular_event_cb_t`

```c
typedef void(* cellular_event_cb_t) (const struct device *dev, enum cellular_event event, const void *payload, void *user_data)
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝事件回调（Cellular Event Callback）原型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 产生事件的蜂窝设备（Cellular Device）。 |
| `event` | 发生的 cellular_event 类型。 |
| `payload` | 指向该类型专用有效载荷（Kind-specific Payload）的指针；类型未定义有效载荷时为 NULL。 |
| `user_data` | 注册回调时提供的指针。 |

**说明（Note）**：注意：驱动直接从自身上下文（Context）调用回调。如有需要，应将繁重处理转交工作队列（Work Queue）。

<a id="ga84efd3405e5233358514c7d634710042"></a>

### `cellular_event_mask_t`

```c
typedef uint32_t cellular_event_mask_t
```

```c
#include <zephyr/drivers/cellular.h>
```

<a id="ga168002533ce39996e68bda2c2e92428e"></a>

### `cellular_access_technology`

```c
enum cellular_access_technology
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝接入技术（Cellular Access Technologies），参见 3GPP TS 27.007 的 AcT。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CELLULAR_ACCESS_TECHNOLOGY_GSM` | 全球移动通信系统（Global System for Mobile Communications，GSM），2G，3GPP Rel 99。 |
| `CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT` | 带宽和频谱受限的 GSM 变体（Bandwidth & Spectrum Limited GSM），2G，3GPP Rel 99。 |
| `CELLULAR_ACCESS_TECHNOLOGY_UTRAN` | 通用移动通信系统陆地无线接入网（UMTS Terrestrial Radio Access Network，UTRAN），3G，3GPP Rel 99。 |
| `CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS` | GSM 增强型通用分组无线业务（Enhanced General Packet Radio Service），2.5G，3GPP Rel 99。 |
| `CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA` | 支持高速下行分组接入（High Speed Downlink Packet Access，HSDPA）的 UTRAN，3.5G，3GPP Rel 5。 |
| `CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA` | 支持高速上行分组接入（High Speed Uplink Packet Access，HSUPA）的 UTRAN，3.75G，3GPP Rel 6。 |
| `CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA` | 支持 HSDPA 和 HSUDP 的 UTRAN，即高速分组接入（HSPA），3.75G，3GPP Rel 6。（原文写作 HSUDP，保留该拼写疑点。） |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN` | 演进型 UTRAN（Evolved UTRAN），4G，3GPP Rel 8。 |
| `CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT` | 面向物联网的扩展覆盖 GSM（Extended Coverage GSM for IoT），2G，3GPP Rel 13。 |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1` | EUTRAN 窄带物联网（Narrowband-IoT），4G，3GPP Rel 13。 |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN` | 连接 5G 核心网（5G Core Network）的 LTE／E-UTRA，5G，3GPP Rel 15。 |
| `CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN` | 使用 5G 核心网的新空口（New Radio），5G，3GPP Rel 15。 |
| `CELLULAR_ACCESS_TECHNOLOGY_NG_RAN` | 下一代无线接入网（Next Generation RAN），5G，3GPP Rel 15。 |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL` | LTE／E-UTRA 与 NR 双连接（Dual Connectivity），5G，3GPP Rel 15。 |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT` | 卫星窄带物联网（Narrowband-IoT over Satellite），4G，3GPP Rel 17。 |
| `CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT` | 卫星 LTE 宽带（LTE Wideband over Satellite），4G，3GPP Rel 17。 |
| `CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT` | 卫星下一代无线接入网（Next Generation RAN over Satellite），5G，3GPP Rel 17。 |
| `CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN` | 未知接入技术（Unknown Access Technology）。 |

<a id="ga27c0b71128c782a7f42832b82eb94411"></a>

### `cellular_event`

```c
enum cellular_event
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝驱动异步发出的事件（Asynchronous Events）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CELLULAR_EVENT_MODEM_INFO_CHANGED` | 一个或多个调制解调器信息字段（Modem-info Fields）发生变化，例如 IMSI 变为可用。 |
| `CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED` | 蜂窝网络注册状态（Cellular Network Registration Status）变化。 |
| `CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT` | 与调制解调器的通信链路检查（Communications Link Check）结果。 |
| `CELLULAR_EVENT_NETWORK_STATUS_CHANGED` | 蜂窝网络状态（Cellular Network Status）变化。 |
| `CELLULAR_EVENT_MODEM_SUSPENDED` | 蜂窝调制解调器挂起回调（Cellular Modem Suspension Callback）。 |

<a id="gad6e38e31d82075c51933fcbb2ff2de30"></a>

### `cellular_modem_info_type`

```c
enum cellular_modem_info_type
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CELLULAR_MODEM_INFO_IMEI` | 国际移动设备识别码（International Mobile Equipment Identity，IMEI）。 |
| `CELLULAR_MODEM_INFO_MODEL_ID` | 调制解调器型号 ID（Modem Model ID）。 |
| `CELLULAR_MODEM_INFO_MANUFACTURER` | 调制解调器制造商（Modem Manufacturer）。 |
| `CELLULAR_MODEM_INFO_FW_VERSION` | 调制解调器固件版本（Modem Firmware Version）。 |
| `CELLULAR_MODEM_INFO_SIM_IMSI` | 国际移动用户识别码（International Mobile Subscriber Identity，IMSI）。 |
| `CELLULAR_MODEM_INFO_SIM_ICCID` | 集成电路卡识别码（Integrated Circuit Card Identification Number，ICCID），用于 SIM。 |
| `CELLULAR_MODEM_INFO_SERIAL_NUMBER` | 调制解调器序列号（Modem Serial Number）。 |

<a id="ga7309390ed507748fdb72cf078b8e08a4"></a>

### `cellular_registration_status`

```c
enum cellular_registration_status
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝注册状态（Cellular Registration Status），参见 3GPP TS 27.007。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CELLULAR_REGISTRATION_NOT_REGISTERED` | 未注册，也未搜索（Not Registered, Not Searching）。 |
| `CELLULAR_REGISTRATION_REGISTERED_HOME` | 已注册到归属网络（Home Network）。 |
| `CELLULAR_REGISTRATION_SEARCHING` | 未注册，正在搜索运营商（Searching for an Operator）。 |
| `CELLULAR_REGISTRATION_DENIED` | 注册被拒绝（Registration Denied）。 |
| `CELLULAR_REGISTRATION_UNKNOWN` | 未知（Unknown），例如超出覆盖范围。 |
| `CELLULAR_REGISTRATION_REGISTERED_ROAMING` | 已注册，正在漫游（Roaming）。 |
| `CELLULAR_REGISTRATION_SMS_ONLY_HOME` | 在归属网络注册为仅短信（SMS Only）。 |
| `CELLULAR_REGISTRATION_SMS_ONLY_ROAMING` | 在漫游网络注册为仅短信（SMS Only）。 |
| `CELLULAR_REGISTRATION_EMERGENCY_ONLY` | 仅附着以使用紧急承载服务（Emergency Bearer Services）。 |
| `CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME` | 在归属网络注册为不优先使用电路域回落（CSFB Not Preferred）。 |
| `CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING` | 在漫游网络注册为不优先使用电路域回落（CSFB Not Preferred）。 |
| `CELLULAR_REGISTRATION_RLOS` | 已附着以访问受限本地运营商服务（Restricted Local Operator Services）。 |

<a id="ga746c0862b9a5da7c766e42e4d6025f47"></a>

### `cellular_signal_type`

```c
enum cellular_signal_type
```

```c
#include <zephyr/drivers/cellular.h>
```

蜂窝信号类型（Cellular Signal Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CELLULAR_SIGNAL_RSSI` |  |
| `CELLULAR_SIGNAL_RSRP` |  |
| `CELLULAR_SIGNAL_RSRQ` |  |

<a id="gaa53d52e58221c998eec272a4d063bdd4"></a>

### `cellular_configure_networks()`

```c
int cellular_configure_networks ( const struct device * dev, const struct cellular_network * networks, uint8_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

为设备配置蜂窝网络（Cellular Networks）。

蜂窝网络设备（Cellular Network Devices）至少支持一种蜂窝接入技术（Cellular Access Technology）。每种接入技术定义一组频段（Bands），设备支持其中全部或部分频段。

蜂窝设备一次只能使用一种蜂窝网络技术（Cellular Network Technology），且必须仅使用所提供的蜂窝网络配置。提供多个配置时，按给出顺序确定优先级，第一项优先级最高。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `networks` | 要应用的蜂窝网络配置列表（Cellular Network Configuration List）。 |
| `size` | 蜂窝网络配置列表的大小（List Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 任一所提供的蜂窝网络配置（Cellular Network Configuration）无效或不受支持。 |
| `-ENOTSUP` | 蜂窝网络设备不支持此 API。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga757f0802fd72d61d035a81057f23d5ca"></a>

### `cellular_get_modem_info()`

```c
int cellular_get_modem_info ( const struct device * dev, const enum cellular_modem_info_type type, char * info, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

获取设备调制解调器信息（Modem Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 所请求的调制解调器信息类型（Modem Info Type）。 |
| `info` | 信息字符串目标位置（Info String Destination）。 |
| `size` | 信息字符串大小（Info String Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 蜂窝网络设备不支持此 API。 |
| `-ENODATA` | 调制解调器未提供请求的信息。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gad1e37b428eaacc7442f6a6cb2e1404a5"></a>

### `cellular_get_network_status()`

```c
int cellular_get_network_status ( const struct device * dev, struct cellular_evt_network_status * status )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

获取最近报告的网络状态，即服务小区状态（Serving Cell Status）。

返回驱动最近观测到的网络状态（Network Status），即 CELLULAR_EVENT_NETWORK_STATUS_CHANGED 传递的状态；不会触发新的查询。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `status` | 网络状态快照（Network Status Snapshot）的目标位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 蜂窝网络设备不支持此 API。 |
| `-ENODATA` | 没有当前网络状态，例如首次报告前，或注册状态变化后、下一次轮询刷新之前。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae0ca6816f75b89055aa31370196e2c98"></a>

### `cellular_get_registration_status()`

```c
int cellular_get_registration_status ( const struct device * dev, enum cellular_access_technology tech, enum cellular_registration_status * status )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

获取设备的网络注册状态（Network Registration Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `tech` | 要获取状态的接入技术（Access Technology）。 |
| `status` | 给定接入技术的注册状态（Registration Status）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 蜂窝网络设备不支持此 API。 |
| `-ENODATA` | 调制解调器未提供请求的信息。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga022eb4eecc300b14110107a46824cac0"></a>

### `cellular_get_signal()`

```c
int cellular_get_signal ( const struct device * dev, const enum cellular_signal_type type, int16_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

获取设备信号（Signal）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 所请求的信号信息类型（Signal Information Type）。 |
| `value` | 信号强度（Signal Strength）的目标位置，为 RSSI、RSRP 或 RSRQ 之一。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 蜂窝网络设备不支持此 API。 |
| `-ENODATA` | 设备当前状态不允许轮询信号（Poll Signal）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga12d74b4ec0821f5eed95f24350789ed3"></a>

### `cellular_get_stats()`

```c
const struct cellular_stats * cellular_get_stats ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

从蜂窝设备读取运行统计（Operational Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |

**返回（Returns）**：返回：指向设备实时统计数据（Live Statistics）的指针；设备未实现此 API 时为 NULL。

<a id="ga70340d22df56665b1d113abc8b314a95"></a>

### `cellular_get_supported_networks()`

```c
int cellular_get_supported_networks ( const struct device * dev, const struct cellular_network ** networks, uint8_t * size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

获取设备支持的蜂窝网络（Cellular Networks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `networks` | 指向支持的蜂窝网络配置列表（Supported Cellular Network Configuration List）的指针。 |
| `size` | 蜂窝网络配置列表的大小（List Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 蜂窝网络设备不支持此 API。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga2ae42cd17e07ca8e24aa75352c07e5fe"></a>

### `cellular_modem_pause_periodic_script()`

```c
int cellular_modem_pause_periodic_script ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

暂停 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。

暂停后，已调度的周期脚本（Periodic Script）不再运行，直到调用 cellular_modem_resume_periodic_script()。调用时已在执行的脚本可继续完成；抑制从下一次计划运行开始生效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 通过 MODEM_CELLULAR_DEFINE_INSTANCE() 创建的蜂窝设备，不得为 NULL。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 设备未配置周期性交互脚本（Periodic Chat Script）。 |
| `-EINVAL` | 周期脚本（Periodic Script）已暂停。 |

**参阅（See Also）**：另请参见 cellular_modem_resume_periodic_script。

<a id="ga5dc375b9ab33b2468846b8ca77a2106b"></a>

### `cellular_modem_resume_periodic_script()`

```c
int cellular_modem_resume_periodic_script ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

恢复 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。

重新启用周期脚本（Periodic Script）。若暂停期间至少跳过了一次计划运行，则立即执行脚本；否则按配置的间隔重新启动周期定时器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 通过 MODEM_CELLULAR_DEFINE_INSTANCE() 创建的蜂窝设备，不得为 NULL。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 设备未配置周期性交互脚本（Periodic Chat Script）。 |
| `-EINVAL` | 周期脚本（Periodic Script）目前未暂停。 |

**参阅（See Also）**：另请参见 cellular_modem_pause_periodic_script。

<a id="ga4494e4d41149ea48fd1e0d8fe9b441dd"></a>

### `cellular_set_apn()`

```c
int cellular_set_apn ( const struct device * dev, const char * apn )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

设置分组数据协议（PDP）上下文使用的接入点名称（APN）。

驱动应立即复制字符串，在内部将请求加入队列后返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝设备（Cellular Device）。 |
| `apn` | 以零结尾的接入点名称字符串（APN String），最大长度由驱动决定。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 蜂窝网络设备不支持此 API。 |
| `-EINVAL` | 接入点名称（APN）字符串无效或过长。 |
| `-EALREADY` | 接入点名称（APN）与当前值相同，无需处理。 |
| `-EBUSY` | 调制解调器已拨号（Dialled），无法修改接入点名称（APN）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7b6e210b9e5222b789af52b4ef8cc850"></a>

### `cellular_set_callback()`

```c
int cellular_set_callback ( const struct device * dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/cellular.h>
```

订阅异步蜂窝事件（Asynchronous Cellular Events）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝设备（Cellular Device）。 |
| `mask` | 要订阅的事件掩码（Event Mask）。 |
| `cb` | 事件发生时调用的回调（Callback）；为 NULL 时取消订阅。 |
| `user_data` | 指向传给回调的用户数据（User Data）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 驱动不支持事件回调（Event Callbacks）。 |
| `-EINVAL` | 参数错误（Bad Parameters）。 |
| `-ENOMEM` | 没有空间容纳另一个订阅者（Subscriber）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 9.9\_原页交叉引用（Cross References）

- [蜂窝通信驱动后端 API（Cellular Driver Backend API）](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md)
- [设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）](../api_topic_reference/P015_设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）.md)
- [cellular.h](../api_file_signal_device_reference/P004_zephyr__drivers__cellular.h_文件参考.md)
- [cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)
- [cellular_evt_modem_info](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md)
- [cellular_evt_registration_status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md)
- [cellular_evt_modem_comms_check_result](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md)
- [cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)
- [cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [zephyr/drivers/modem/modem_cellular.h](../api_file_network_device_reference/P024_zephyr__drivers__modem__modem_cellular.h_文件参考.md)
- [MODEM_CELLULAR_DEFINE_INSTANCE()](../api_lifecycle_capability_topic_reference/P011_蜂窝调制解调器驱动定义宏（Driver definition macros）.md#ga4b61e995f86377dfbab0ca81d1efe492)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255"></a>
<a id="gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c"></a>
<a id="gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc"></a>
<a id="gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2"></a>
<a id="gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f"></a>
<a id="gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a"></a>
<a id="gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15"></a>
<a id="gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de"></a>
<a id="gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383"></a>
<a id="gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117"></a>
<a id="gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb"></a>
<a id="gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a"></a>
<a id="gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910"></a>
<a id="gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99"></a>
<a id="gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d"></a>
<a id="ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97"></a>
<a id="gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b"></a>
<a id="gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a"></a>
<a id="gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a"></a>
<a id="gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_电话承载服务（Telephone Bearer Service，TBS）.md) · [返回大纲](大纲.md) · [下一章](P010_电池充电器（Battery Charger）.md)
