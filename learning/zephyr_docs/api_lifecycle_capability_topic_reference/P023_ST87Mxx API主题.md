---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-23
title: ST87Mxx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_ST87Mxx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

意法半导体（STMicroelectronics）ST87Mxx 蜂窝调制解调器。

<a id="details"></a>

意法半导体（STMicroelectronics）ST87Mxx 蜂窝调制解调器。

<a id="header-groups"></a>
<a id="groups"></a>

## 23.1\_主题（Topics）

<a id="r_st87mxx_5Fgnss_5Fconfiguration"></a>

相关声明：[全球导航卫星系统（GNSS）配置](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md)。

<a id="r_st87mxx_5Fconstants"></a>

相关声明：[ST87Mxx 常量（Constants）](../api_platform_topic_reference/P123_ST87Mxx 常量（Constants）.md)。

<a id="r_st87mxx_5Fwscan_5Fconfiguration"></a>

相关声明：[Wi-Fi 扫描配置（Scanning configuration）](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 23.2\_文件（Files）

<a id="r_st87mxx_5Fapp_5Fservices_2Eh"></a>

```c
file st87mxx_app_services.h
```

相关声明：[st87mxx_app_services.h](../api_file_system_power_reference/P040_zephyr__drivers__modem__st87mxx_app_services.h_文件参考.md)。

ST87Mxx调制解调器（Modems）扩展蜂窝通信API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.3\_数据结构（Data Structures）

<a id="r_st87mxx_5Fwifiscan_5Fparams"></a>

```c
struct st87mxx_wifiscan_params
```

相关声明：[st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)。

ST87Mxx Wi-Fi扫描操作（Scan Operation）的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.4\_类型定义（Typedefs）

<a id="r_ga36695a0b14a8ac128692a3a543a2e1b1"></a>

```c
typedef void st87mxx_get_beacon_data_callback_t(char const *const string)
```

相关声明：[st87mxx_get_beacon_data_callback_t](#ga36695a0b14a8ac128692a3a543a2e1b1)。

在 Wi-Fi 扫描数据（Scan Data）可用时捕获该数据的回调。

<a id="r_ga92a4c4d49be58a5d8c3db059116cd38e"></a>

```c
typedef void st87mxx_get_pos_callback_t(char const *const string)
```

相关声明：[st87mxx_get_pos_callback_t](#ga92a4c4d49be58a5d8c3db059116cd38e)。

获取位置（Positions）的回调。

<a id="r_ga64d19b3167aae5fd3b4a372222534e23"></a>

```c
typedef void st87mxx_get_rssi_callback_t(char const *const string)
```

相关声明：[st87mxx_get_rssi_callback_t](#ga64d19b3167aae5fd3b4a372222534e23)。

获取接收信号强度指示值（RSSI Values）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 23.5\_枚举（Enumerations）

<a id="r_ga6c28c45f3910a0e33a8026fc87133247"></a>

```c
enum sequence_state { SEQUENCE_NONE = 0 , SEQUENCE_ONGOING = 1 , SEQUENCE_TIMED_OUT = 2 }
```

相关声明：[sequence_state](#ga6c28c45f3910a0e33a8026fc87133247)、[SEQUENCE_NONE](#gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d)、[SEQUENCE_ONGOING](#gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd)、[SEQUENCE_TIMED_OUT](#gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd)。

应用服务序列状态（Application Services Sequence State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.6\_函数（Functions）

<a id="r_ga2227c0f901ef6acc105f7a823f014958"></a>

```c
void st87mxx_app_services_init (void)
```

相关声明：[st87mxx_app_services_init](#ga2227c0f901ef6acc105f7a823f014958)。

启动应用服务（Application Services）的 API，包括 GNSS、WSCAN 和 RSSI 采集。

<a id="r_gaf711155377231afc1ad969cb397818cd"></a>

```c
int st87mxx_gnss_getfix (uint32_t nb_position, st87mxx_get_pos_callback_t *get_pos_callback_func, uint32_t timeout)
```

相关声明：[st87mxx_gnss_getfix](#gaf711155377231afc1ad969cb397818cd)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[st87mxx_get_pos_callback_t](#ga92a4c4d49be58a5d8c3db059116cd38e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 ST87Mxx GNSS 位置（Position）的 API。

<a id="r_gaea2db4c02a45f514f14c2f2913a36915"></a>

```c
void st87mxx_gnss_stop (void)
```

相关声明：[st87mxx_gnss_stop](#gaea2db4c02a45f514f14c2f2913a36915)。

停止 GNSS 功能（Feature）的 API。

<a id="r_ga48d42b0ba645e8caa53b49e4842c1276"></a>

```c
int st87mxx_wifiscan (st87mxx_wifiscan_params *wscan_params)
```

相关声明：[st87mxx_wifiscan](#ga48d42b0ba645e8caa53b49e4842c1276)、[st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)。

启动用于定位的 Wi-Fi 扫描（WSCAN）功能的 API。

<a id="r_ga462eeda7a3702664f9c8d80a7d780c64"></a>

```c
void st87mxx_wifiscan_stop (void)
```

相关声明：[st87mxx_wifiscan_stop](#ga462eeda7a3702664f9c8d80a7d780c64)。

停止 Wi-Fi 扫描（Scan）的 API。

<a id="r_gae459a9137139217ee997b7e48fcc30f6"></a>

```c
int st87mxx_getrssi (st87mxx_get_rssi_callback_t *get_rssi_callback_func)
```

相关声明：[st87mxx_getrssi](#gae459a9137139217ee997b7e48fcc30f6)、[st87mxx_get_rssi_callback_t](#ga64d19b3167aae5fd3b4a372222534e23)。

异步（Asynchronously）获取 RSSI 的 API。

<a id="r_gafefe0b51707586c520dd966c4a271fa1"></a>

```c
sequence_state st87mxx_app_services_getstate (void)
```

相关声明：[sequence_state](#ga6c28c45f3910a0e33a8026fc87133247)、[st87mxx_app_services_getstate](#gafefe0b51707586c520dd966c4a271fa1)。

获取应用服务序列状态（Application Services Sequence State）的 API。

## 23.7\_详细说明（Detailed Documentation）

<a id="ga36695a0b14a8ac128692a3a543a2e1b1"></a>

### `st87mxx_get_beacon_data_callback_t`

```c
typedef void st87mxx_get_beacon_data_callback_t(char const *const string)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

在 Wi-Fi 扫描数据（Scan Data）可用时捕获该数据的回调。

Wi-Fi 扫描（WSCAN）数据示例：`1,-73,48:29:52:14:3E:B0,Livebox-3EB0`，各字段依次为通道编号（Channel Number）、接收电平（RxLevel）、MAC 地址（BSSID）和 SSID 名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `string` | 用于写入数据（Data）的字符串。 |

<a id="ga92a4c4d49be58a5d8c3db059116cd38e"></a>

### `st87mxx_get_pos_callback_t`

```c
typedef void st87mxx_get_pos_callback_t(char const *const string)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

获取位置（Positions）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `string` | 用于写入位置（Position）的字符串。 |

<a id="ga64d19b3167aae5fd3b4a372222534e23"></a>

### `st87mxx_get_rssi_callback_t`

```c
typedef void st87mxx_get_rssi_callback_t(char const *const string)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

获取接收信号强度指示值（RSSI Values）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `string` | 用于写入接收信号强度指示（RSSI）的字符串。 |

<a id="ga6c28c45f3910a0e33a8026fc87133247"></a>

### `sequence_state`

```c
enum sequence_state
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

应用服务序列状态（Application Services Sequence State）。

表示当前没有应用服务序列（Application Service Sequence）运行、某个序列正在执行，或序列已超时。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SEQUENCE_NONE` | 尚未启动序列（Sequence）。 |
| `SEQUENCE_ONGOING` | 序列（Sequence）正在执行。 |
| `SEQUENCE_TIMED_OUT` | 序列（Sequence）已超过超时时间（Timeout）。 |

<a id="gafefe0b51707586c520dd966c4a271fa1"></a>

### `st87mxx_app_services_getstate()`

```c
sequence_state st87mxx_app_services_getstate ( void )
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

获取应用服务序列状态（Application Services Sequence State）的 API。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `State` | 当前序列（Current Sequence）的。 |

<a id="ga2227c0f901ef6acc105f7a823f014958"></a>

### `st87mxx_app_services_init()`

```c
void st87mxx_app_services_init ( void )
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

启动应用服务（Application Services）的 API，包括 GNSS、WSCAN 和 RSSI 采集。

应在任何应用服务（Application Services）之前调用本函数。注意：同一时刻只能运行一项应用服务。

<a id="gae459a9137139217ee997b7e48fcc30f6"></a>

### `st87mxx_getrssi()`

```c
int st87mxx_getrssi ( st87mxx_get_rssi_callback_t * get_rssi_callback_func)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

异步（Asynchronously）获取 RSSI 的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `get_rssi_callback_func` | 指向输出回调函数（Output Callback Function）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `API` | 执行状态（Execution Status）。 |

<a id="gaf711155377231afc1ad969cb397818cd"></a>

### `st87mxx_gnss_getfix()`

```c
int st87mxx_gnss_getfix ( uint32_t nb_position, st87mxx_get_pos_callback_t * get_pos_callback_func, uint32_t timeout )
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

获取 ST87Mxx GNSS 位置（Position）的 API。

回调返回的位置（Position）默认采用 ST_AT 格式，可通过修改 `GNSS_CONSTELLATION_ID` 常量设为 NMEA 格式。此常量名按原文保留。

ST_AT 格式示例：

```text
#GNSSFIX: 0,2291,461282763,48.15370,-01.56719,130.2, 33.6,00.0,00.0,52.2,2.4,9.5,7.7,5,11,2.4,30,-0.1,20,1.4,09,1.7,06,-0.3
```

详细格式如下；原文格式串中的字段标识符保留：

```text
#GNSSFIX: validity,week_number,time_of_week,latitude,longitude, altitude,accuracy
[,std_dev_altitude,hdop,gdop,pdop] <- If GNSS_FORMAT_ST_ACCURACY is 1
[,number_of_satellites,satellite1_id,satellite1_residual,..., satelliten_id,satelliten_residual] <- If GNSS_FORMAT_ST_SATELLITES is 1
[,orientation_degree,semi_major,semi_minor] <- If GNSS_FORMAT_ST_ORIENTATION is 1
```

基础字段依次为有效性（Validity）、周编号（Week Number）、周内时间（Time of Week）、纬度（Latitude）、经度（Longitude）、高度（Altitude）和精度（Accuracy）。`GNSS_FORMAT_ST_ACCURACY` 为 `1` 时，附加高度标准差（Standard Deviation of Altitude）及 HDOP、GDOP、PDOP 精度因子；`GNSS_FORMAT_ST_SATELLITES` 为 `1` 时，附加卫星数量（Number of Satellites）及各卫星 ID 与残差（Residual）；`GNSS_FORMAT_ST_ORIENTATION` 为 `1` 时，附加方位角（Orientation Degree）、半长轴（Semi-major）与半短轴（Semi-minor）。

NMEA 格式示例：

```text
$GPGLL,4809.2231,N,00134.281,W,091218,A,A*6C
```

更多信息参见原文引用的 [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb_position` | 要采样的 GNSS 位置（Position）数量；`0` 表示无限。 |
| `get_pos_callback_func` | 指向输出回调函数（Output Callback Function）的指针。 |
| `timeout` | 超时时间（Timeout），单位为秒；到期后取消请求。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Execution` | 状态（Status）。 |

<a id="gaea2db4c02a45f514f14c2f2913a36915"></a>

### `st87mxx_gnss_stop()`

```c
void st87mxx_gnss_stop ( void )
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

停止 GNSS 功能（Feature）的 API。

<a id="ga48d42b0ba645e8caa53b49e4842c1276"></a>

### `st87mxx_wifiscan()`

```c
int st87mxx_wifiscan ( st87mxx_wifiscan_params * wscan_params)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

启动用于定位的 Wi-Fi 扫描（WSCAN）功能的 API。

Wi-Fi 扫描（WSCAN）通常用于 GNSS 不可用时获取粗略位置，例如室内环境。其主要目的是检测并列出附近所有可用 Wi-Fi 网络。发起扫描后，ST87MXX 会侦听附近 Wi-Fi 接入点（AP）发送的信标（Beacons），从中获取网络信息并发现网络。检测到的网络列表可发送到第三方定位服务器（Localization Server）以获取位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wscan_params` | 包含启动 WSCAN 功能参数（Parameters）的结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Execution` | 状态（Status）。 |

<a id="ga462eeda7a3702664f9c8d80a7d780c64"></a>

### `st87mxx_wifiscan_stop()`

```c
void st87mxx_wifiscan_stop ( void )
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

停止 Wi-Fi 扫描（Scan）的 API。


## 23.8\_原页交叉引用（Cross References）

- [全球导航卫星系统（GNSS）配置](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md)
- [ST87Mxx 常量（Constants）](../api_platform_topic_reference/P123_ST87Mxx 常量（Constants）.md)
- [Wi-Fi 扫描配置（Scanning configuration）](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md)
- [st87mxx_app_services.h](../api_file_system_power_reference/P040_zephyr__drivers__modem__st87mxx_app_services.h_文件参考.md)
- [st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [https://en.wikipedia.org/wiki/NMEA_0183](https://en.wikipedia.org/wiki/NMEA_0183)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d"></a>
<a id="gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd"></a>
<a id="gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_安全Shell（SSH）密钥生成（Keygen）的API。.md) · [返回大纲](大纲.md) · [下一章](P024_USB 电力传输电源数据对象（USB Power Delivery Power Data Objects）.md)
