---
id: learning.zephyr-docs.api-file-signal-device-reference.page-4
title: zephyr__drivers__cellular.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_cellular.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝调制解调器（Cellular Modem）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>
```

查看此文件的源码。

蜂窝调制解调器（Cellular Modem）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

<a id="r_cellular_5Fdriver_5Fapi"></a>

```c
struct cellular_driver_api
```

相关声明：[cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)。

驱动操作（Driver Operations）：蜂窝通信（Cellular）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga47b3cae8fd86f6cec69cda46b8e70be4"></a>

```c
#define CELLULAR_EUTRAN_CELL_ID_MAX 0xFFFFFFFU
```

相关声明：[CELLULAR_EUTRAN_CELL_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga47b3cae8fd86f6cec69cda46b8e70be4)。

演进通用陆地无线接入网全局小区标识符（E-UTRAN Global Cell Identifier，GCI）为 28 位值。

<a id="r_ga08556787615b6f43d8f162ec5da69653"></a>

```c
#define CELLULAR_EUTRAN_CELL_ID_INVALID UINT32_MAX
```

相关声明：[CELLULAR_EUTRAN_CELL_ID_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga08556787615b6f43d8f162ec5da69653)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

未知 E-UTRAN 全局小区标识符（GCI）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga84efd3405e5233358514c7d634710042"></a>

```c
typedef uint32_t cellular_event_mask_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)。

<a id="r_gac9d02d18ed6e0af07e480cde678afdc1"></a>

```c
typedef void(* cellular_event_cb_t) (const struct device *dev, enum cellular_event event, const void *payload, void *user_data)
```

相关声明：[cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga27c0b71128c782a7f42832b82eb94411)。

蜂窝事件回调（Cellular Event Callback）原型。

<a id="r_ga71ddc5b9e09da398d02caadc91ef3cfc"></a>

```c
typedef int(* cellular_api_configure_networks) (const struct device *dev, const struct cellular_network *networks, uint8_t size)
```

相关声明：[cellular_api_configure_networks](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga71ddc5b9e09da398d02caadc91ef3cfc)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于配置网络的 API。

<a id="r_ga6aa2c51fa80d5420593021c35444308a"></a>

```c
typedef int(* cellular_api_get_supported_networks) (const struct device *dev, const struct cellular_network **networks, uint8_t *size)
```

相关声明：[cellular_api_get_supported_networks](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga6aa2c51fa80d5420593021c35444308a)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于获取支持的网络的 API。

<a id="r_ga75cac77838970288d4d23647eaafd30b"></a>

```c
typedef int(* cellular_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[cellular_api_get_signal](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga75cac77838970288d4d23647eaafd30b)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

用于获取网络信号强度（signal strength）的 API。

<a id="r_ga03095206ae2b77ce232dd05b172bd56d"></a>

```c
typedef int(* cellular_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[cellular_api_get_modem_info](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga03095206ae2b77ce232dd05b172bd56d)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)。

用于获取调制解调器（modem）信息的 API。

<a id="r_ga08a0966933caa70d7044342ed2ad8eb6"></a>

```c
typedef int(* cellular_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[cellular_api_get_registration_status](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga08a0966933caa70d7044342ed2ad8eb6)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)。

用于获取注册状态（registration status）的 API。

<a id="r_ga30f5fef993f17b001e2df9c89bdaf288"></a>

```c
typedef int(* cellular_api_get_network_status) (const struct device *dev, struct cellular_evt_network_status *status)
```

相关声明：[cellular_api_get_network_status](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga30f5fef993f17b001e2df9c89bdaf288)、[device](../device_reference/P002_设备对象结构.md)、[cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)。

用于获取最近一次上报的网络（服务小区，serving cell）状态的 API。

<a id="r_gabf5bd5a939a300b8493f7c803b9128f0"></a>

```c
typedef int(* cellular_api_set_apn) (const struct device *dev, const char *apn)
```

相关声明：[cellular_api_set_apn](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#gabf5bd5a939a300b8493f7c803b9128f0)、[device](../device_reference/P002_设备对象结构.md)。

用于编程设置接入点名称（APN）的 API。

<a id="r_gacbf9c85b2ea95321beee0ba75d5977f7"></a>

```c
typedef int(* cellular_api_set_callback) (const struct device *dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void *user_data)
```

相关声明：[cellular_api_set_callback](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#gacbf9c85b2ea95321beee0ba75d5977f7)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)、[cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)。

用于注册异步回调的 API。

<a id="r_ga975fe3a63ed2dd936faa619846f8b701"></a>

```c
typedef const struct cellular_stats *(* cellular_api_get_stats) (const struct device *dev)
```

相关声明：[cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)、[cellular_api_get_stats](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga975fe3a63ed2dd936faa619846f8b701)、[device](../device_reference/P002_设备对象结构.md)。

用于读取运行统计信息（operational statistics）的 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga168002533ce39996e68bda2c2e92428e"></a>

```c
enum cellular_access_technology { CELLULAR_ACCESS_TECHNOLOGY_GSM = 0 , CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT = 1 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN = 2 , CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS = 3 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA = 4 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA = 5 , CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA = 6 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN = 7 , CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT = 8 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1 = 9 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN = 10 , CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN = 11 , CELLULAR_ACCESS_TECHNOLOGY_NG_RAN = 12 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL = 13 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT = 14 , CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT = 15 , CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT = 16 , CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN = 255 }
```

相关声明：[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[CELLULAR_ACCESS_TECHNOLOGY_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255)、[CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c)、[CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74)、[CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1)、[CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f)、[CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37)、[CELLULAR_ACCESS_TECHNOLOGY_NG_RAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15)、[CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de)、[CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383)、[CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117)。

蜂窝接入技术（Cellular Access Technologies），参见 3GPP TS 27.007 的 AcT。

<a id="r_ga746c0862b9a5da7c766e42e4d6025f47"></a>

```c
enum cellular_signal_type { CELLULAR_SIGNAL_RSSI , CELLULAR_SIGNAL_RSRP , CELLULAR_SIGNAL_RSRQ }
```

相关声明：[cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)、[CELLULAR_SIGNAL_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a)、[CELLULAR_SIGNAL_RSRP](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a)、[CELLULAR_SIGNAL_RSRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338)。

蜂窝信号类型（Cellular Signal Type）。

<a id="r_gad6e38e31d82075c51933fcbb2ff2de30"></a>

```c
enum cellular_modem_info_type { CELLULAR_MODEM_INFO_IMEI , CELLULAR_MODEM_INFO_MODEL_ID , CELLULAR_MODEM_INFO_MANUFACTURER , CELLULAR_MODEM_INFO_FW_VERSION , CELLULAR_MODEM_INFO_SIM_IMSI , CELLULAR_MODEM_INFO_SIM_ICCID , CELLULAR_MODEM_INFO_SERIAL_NUMBER }
```

相关声明：[cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)、[CELLULAR_MODEM_INFO_IMEI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de)、[CELLULAR_MODEM_INFO_MODEL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8)、[CELLULAR_MODEM_INFO_MANUFACTURER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1)、[CELLULAR_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027)、[CELLULAR_MODEM_INFO_SIM_IMSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245)、[CELLULAR_MODEM_INFO_SIM_ICCID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)、[CELLULAR_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed)。

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

<a id="r_ga7309390ed507748fdb72cf078b8e08a4"></a>

```c
enum cellular_registration_status { CELLULAR_REGISTRATION_NOT_REGISTERED = 0 , CELLULAR_REGISTRATION_REGISTERED_HOME = 1 , CELLULAR_REGISTRATION_SEARCHING = 2 , CELLULAR_REGISTRATION_DENIED = 3 , CELLULAR_REGISTRATION_UNKNOWN = 4 , CELLULAR_REGISTRATION_REGISTERED_ROAMING = 5 , CELLULAR_REGISTRATION_SMS_ONLY_HOME = 6 , CELLULAR_REGISTRATION_SMS_ONLY_ROAMING = 7 , CELLULAR_REGISTRATION_EMERGENCY_ONLY = 8 , CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME = 9 , CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING = 10 , CELLULAR_REGISTRATION_RLOS = 11 }
```

相关声明：[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)、[CELLULAR_REGISTRATION_NOT_REGISTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27)、[CELLULAR_REGISTRATION_REGISTERED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe)、[CELLULAR_REGISTRATION_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175)、[CELLULAR_REGISTRATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e)、[CELLULAR_REGISTRATION_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1)、[CELLULAR_REGISTRATION_REGISTERED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d)、[CELLULAR_REGISTRATION_SMS_ONLY_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b)、[CELLULAR_REGISTRATION_SMS_ONLY_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27)、[CELLULAR_REGISTRATION_EMERGENCY_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3)、[CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252)、[CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97)、[CELLULAR_REGISTRATION_RLOS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b)。

蜂窝注册状态（Cellular Registration Status），参见 3GPP TS 27.007。

<a id="r_ga27c0b71128c782a7f42832b82eb94411"></a>

```c
enum cellular_event { CELLULAR_EVENT_MODEM_INFO_CHANGED = BIT(0) , CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED = BIT(1) , CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT = BIT(2) , CELLULAR_EVENT_NETWORK_STATUS_CHANGED = BIT(3) , CELLULAR_EVENT_MODEM_SUSPENDED = BIT(4) }
```

相关声明：[cellular_event](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga27c0b71128c782a7f42832b82eb94411)、[CELLULAR_EVENT_MODEM_INFO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb)、[CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a)、[CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)、[CELLULAR_EVENT_NETWORK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99)、[CELLULAR_EVENT_MODEM_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c)。

蜂窝驱动异步发出的事件（Asynchronous Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_gaa53d52e58221c998eec272a4d063bdd4"></a>

```c
static int cellular_configure_networks (const struct device *dev, const struct cellular_network *networks, uint8_t size)
```

相关声明：[cellular_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gaa53d52e58221c998eec272a4d063bdd4)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为设备配置蜂窝网络（Cellular Networks）。

<a id="r_ga70340d22df56665b1d113abc8b314a95"></a>

```c
static int cellular_get_supported_networks (const struct device *dev, const struct cellular_network **networks, uint8_t *size)
```

相关声明：[cellular_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga70340d22df56665b1d113abc8b314a95)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取设备支持的蜂窝网络（Cellular Networks）。

<a id="r_ga022eb4eecc300b14110107a46824cac0"></a>

```c
static int cellular_get_signal (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[cellular_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga022eb4eecc300b14110107a46824cac0)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取设备信号（Signal）。

<a id="r_ga757f0802fd72d61d035a81057f23d5ca"></a>

```c
static int cellular_get_modem_info (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[cellular_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga757f0802fd72d61d035a81057f23d5ca)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)。

获取设备调制解调器信息（Modem Info）。

<a id="r_gae0ca6816f75b89055aa31370196e2c98"></a>

```c
static int cellular_get_registration_status (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[cellular_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gae0ca6816f75b89055aa31370196e2c98)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)。

获取设备的网络注册状态（Network Registration Status）。

<a id="r_gad1e37b428eaacc7442f6a6cb2e1404a5"></a>

```c
static int cellular_get_network_status (const struct device *dev, struct cellular_evt_network_status *status)
```

相关声明：[cellular_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad1e37b428eaacc7442f6a6cb2e1404a5)、[device](../device_reference/P002_设备对象结构.md)、[cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)。

获取最近报告的网络状态，即服务小区状态（Serving Cell Status）。

<a id="r_ga4494e4d41149ea48fd1e0d8fe9b441dd"></a>

```c
static int cellular_set_apn (const struct device *dev, const char *apn)
```

相关声明：[cellular_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga4494e4d41149ea48fd1e0d8fe9b441dd)、[device](../device_reference/P002_设备对象结构.md)。

设置分组数据协议（PDP）上下文使用的接入点名称（APN）。

<a id="r_ga7b6e210b9e5222b789af52b4ef8cc850"></a>

```c
static int cellular_set_callback (const struct device *dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void *user_data)
```

相关声明：[cellular_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7b6e210b9e5222b789af52b4ef8cc850)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)、[cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)。

订阅异步蜂窝事件（Asynchronous Cellular Events）。

<a id="r_ga12d74b4ec0821f5eed95f24350789ed3"></a>

```c
static const struct cellular_stats * cellular_get_stats (const struct device *dev)
```

相关声明：[cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)、[cellular_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga12d74b4ec0821f5eed95f24350789ed3)、[device](../device_reference/P002_设备对象结构.md)。

从蜂窝设备读取运行统计（Operational Statistics）。


## 4.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P025_cellular.h_源码浏览.md)
- [cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)
- [cellular_evt_modem_info](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md)
- [CELLULAR_EVENT_MODEM_INFO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb)
- [cellular_evt_registration_status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md)
- [CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a)
- [cellular_evt_modem_comms_check_result](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md)
- [CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)
- [cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)
- [CELLULAR_EVENT_NETWORK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99)
- [cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)
- [cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)
- [CELLULAR_EUTRAN_CELL_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga47b3cae8fd86f6cec69cda46b8e70be4)
- [CELLULAR_EUTRAN_CELL_ID_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga08556787615b6f43d8f162ec5da69653)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)
- [cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)
- [device](../device_reference/P002_设备对象结构.md)
- [cellular_event](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga27c0b71128c782a7f42832b82eb94411)
- [cellular_api_configure_networks](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga71ddc5b9e09da398d02caadc91ef3cfc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cellular_api_get_supported_networks](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga6aa2c51fa80d5420593021c35444308a)
- [cellular_api_get_signal](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga75cac77838970288d4d23647eaafd30b)
- [cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [cellular_api_get_modem_info](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga03095206ae2b77ce232dd05b172bd56d)
- [cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)
- [cellular_api_get_registration_status](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga08a0966933caa70d7044342ed2ad8eb6)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [cellular_api_get_network_status](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga30f5fef993f17b001e2df9c89bdaf288)
- [cellular_api_set_apn](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#gabf5bd5a939a300b8493f7c803b9128f0)
- [cellular_api_set_callback](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#gacbf9c85b2ea95321beee0ba75d5977f7)
- [cellular_api_get_stats](../api_network_time_topic_reference/P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md#ga975fe3a63ed2dd936faa619846f8b701)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1)
- [CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f)
- [CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37)
- [CELLULAR_ACCESS_TECHNOLOGY_NG_RAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de)
- [CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383)
- [CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117)
- [CELLULAR_SIGNAL_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a)
- [CELLULAR_SIGNAL_RSRP](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a)
- [CELLULAR_SIGNAL_RSRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338)
- [CELLULAR_MODEM_INFO_IMEI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de)
- [CELLULAR_MODEM_INFO_MODEL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8)
- [CELLULAR_MODEM_INFO_MANUFACTURER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1)
- [CELLULAR_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027)
- [CELLULAR_MODEM_INFO_SIM_IMSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245)
- [CELLULAR_MODEM_INFO_SIM_ICCID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)
- [CELLULAR_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed)
- [CELLULAR_REGISTRATION_NOT_REGISTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27)
- [CELLULAR_REGISTRATION_REGISTERED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe)
- [CELLULAR_REGISTRATION_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175)
- [CELLULAR_REGISTRATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e)
- [CELLULAR_REGISTRATION_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1)
- [CELLULAR_REGISTRATION_REGISTERED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d)
- [CELLULAR_REGISTRATION_SMS_ONLY_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b)
- [CELLULAR_REGISTRATION_SMS_ONLY_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27)
- [CELLULAR_REGISTRATION_EMERGENCY_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3)
- [CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252)
- [CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97)
- [CELLULAR_REGISTRATION_RLOS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b)
- [CELLULAR_EVENT_MODEM_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c)
- [cellular_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gaa53d52e58221c998eec272a4d063bdd4)
- [cellular_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga70340d22df56665b1d113abc8b314a95)
- [cellular_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga022eb4eecc300b14110107a46824cac0)
- [cellular_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga757f0802fd72d61d035a81057f23d5ca)
- [cellular_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gae0ca6816f75b89055aa31370196e2c98)
- [cellular_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad1e37b428eaacc7442f6a6cb2e1404a5)
- [cellular_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga4494e4d41149ea48fd1e0d8fe9b441dd)
- [cellular_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7b6e210b9e5222b789af52b4ef8cc850)
- [cellular_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga12d74b4ec0821f5eed95f24350789ed3)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__sensor__ccs811.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__display__cfb.h_文件参考.md)
