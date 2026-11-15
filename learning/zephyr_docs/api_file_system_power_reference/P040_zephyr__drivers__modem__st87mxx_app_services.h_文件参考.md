---
id: learning.zephyr-docs.api-file-system-power-reference.page-40
title: zephyr__drivers__modem__st87mxx_app_services.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_drivers\_\_modem\_\_st87mxx\_app\_services.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST87Mxx调制解调器（Modems）扩展蜂窝通信API的头文件。

查看此文件的源码。

<a id="details"></a>

ST87Mxx调制解调器（Modems）扩展蜂窝通信API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 40.1\_数据结构（Data Structures）

<a id="r_st87mxx_5Fwifiscan_5Fparams"></a>

```c
struct st87mxx_wifiscan_params
```

相关声明：[st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)。

ST87Mxx Wi-Fi扫描操作（Scan Operation）的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 40.2\_宏定义（Macros）

<a id="r_ga54b2d06b56d845ca68886b94719fe64b"></a>

```c
#define APP_MDM_CMD_TIMEOUT K_SECONDS(180)
```

相关声明：[APP_MDM_CMD_TIMEOUT](../api_platform_topic_reference/P123_ST87Mxx 常量（Constants）.md#ga54b2d06b56d845ca68886b94719fe64b)、[K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)。

应用服务序列（Application Services Sequences）的默认超时（Default Timeout）。

<a id="r_gae9e5cd8119ca22dcfca38e80eb9e67b5"></a>

```c
#define GNSS_NB_MAX_POSITION 100
```

相关声明：[GNSS_NB_MAX_POSITION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9e5cd8119ca22dcfca38e80eb9e67b5)。

采样位置（Sample Position）数量上限。

<a id="r_gac8b2c26a1f22ddd6c86c711440705fc0"></a>

```c
#define GNSS_CONSTELLATION_ID 0
```

相关声明：[GNSS_CONSTELLATION_ID](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gac8b2c26a1f22ddd6c86c711440705fc0)。

GNSS 星座选择（Constellation Selection）：`0` 为 GPS，`1` 为 GALLILEO，`2` 为 GPS+GALLILEO。原文将 Galileo 拼作 `GALLILEO`。

<a id="r_ga1afd16e81b65c2e7a4fa55aa0895d542"></a>

```c
#define GNSS_FORMAT_TYPE 0
```

相关声明：[GNSS_FORMAT_TYPE](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga1afd16e81b65c2e7a4fa55aa0895d542)。

GNSS 数据格式选择（Data Format Selection）：`0` 为 ST_AT，`1` 为 NMEA。

<a id="r_gac44b0f5695f8e52c6180814794df0966"></a>

```c
#define GNSS_FORMAT_ST_POSITION 1
```

相关声明：[GNSS_FORMAT_ST_POSITION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gac44b0f5695f8e52c6180814794df0966)。

为 GNSS 启用 ST_AT 格式时使用的参数（Parameters）。

<a id="r_ga278ff798327ebe4a97f5f40a94bdd19e"></a>

```c
#define GNSS_FORMAT_ST_ACCURACY 0
```

相关声明：[GNSS_FORMAT_ST_ACCURACY](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga278ff798327ebe4a97f5f40a94bdd19e)。

精度数据（Accuracy Data）。

<a id="r_gae58c597d5bdfdca7d2d7364166d3dfb9"></a>

```c
#define GNSS_FORMAT_ST_SATELLITES 0
```

相关声明：[GNSS_FORMAT_ST_SATELLITES](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae58c597d5bdfdca7d2d7364166d3dfb9)。

卫星信息（Satellites Info）。

<a id="r_ga52795780fd3c29a7bcf3578f5c68dc51"></a>

```c
#define GNSS_FORMAT_ST_ORIENTATION 0
```

相关声明：[GNSS_FORMAT_ST_ORIENTATION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga52795780fd3c29a7bcf3578f5c68dc51)。

方位信息（Orientation Info）。

<a id="r_ga88310315fe7e1af0a79b2ecf96c58695"></a>

```c
#define GNSS_NMEA_GPGGA 1
```

相关声明：[GNSS_NMEA_GPGGA](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga88310315fe7e1af0a79b2ecf96c58695)。

为 GNSS 启用 NMEA 格式时使用的参数（Parameters）。

<a id="r_gae9e75d7eddd291e5bf44e73196f7214e"></a>

```c
#define GNSS_NMEA_GPGSA 0
```

相关声明：[GNSS_NMEA_GPGSA](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9e75d7eddd291e5bf44e73196f7214e)。

`$GPGSA` 语句信息（Info）。

<a id="r_gae9089b6e0aafd2f90510267771d84421"></a>

```c
#define GNSS_NMEA_GPGSV 0
```

相关声明：[GNSS_NMEA_GPGSV](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9089b6e0aafd2f90510267771d84421)。

`$GPGSV` 语句信息（Info）。

<a id="r_ga92c0f36c2f84bd0d6e43e6bcc3363b20"></a>

```c
#define GNSS_NMEA_GPGLL 1
```

相关声明：[GNSS_NMEA_GPGLL](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga92c0f36c2f84bd0d6e43e6bcc3363b20)。

`$GPGLL` 语句信息（Info）。

<a id="r_ga107dac8cf6c95dad3e924e0275dfca9a"></a>

```c
#define GNSS_NMEA_GPRMC 0
```

相关声明：[GNSS_NMEA_GPRMC](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga107dac8cf6c95dad3e924e0275dfca9a)。

`$GPRMS` 语句信息（Info）。

<a id="r_ga3d8409b1a22446f3926589e15d73db25"></a>

```c
#define GNSS_NMEA_GPVTG 1
```

相关声明：[GNSS_NMEA_GPVTG](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga3d8409b1a22446f3926589e15d73db25)。

`$GPVTG` 语句信息（Info）。

<a id="r_gac67a00c5b9b85afbb2c76a3b44d04f9d"></a>

```c
#define URC_MODE 1
```

相关声明：[URC_MODE](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#gac67a00c5b9b85afbb2c76a3b44d04f9d)。

为避免 UART 反复传输过多数据，主机（Host）可设置筛选模式（filter mode），使整个 Wi-Fi 扫描期间发现的每个基本服务集标识符（BSSID）仅显示一次。

<a id="r_ga9e38942a920e3dbb9101c0388fdf137d"></a>

```c
#define HOPPING_TIME 1024
```

相关声明：[HOPPING_TIME](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#ga9e38942a920e3dbb9101c0388fdf137d)。

跳频时间（hopping time）指切换到下一个信道之前的扫描时长，单位为毫秒。

<a id="r_ga468e1c5d4d85203d0d644dd0e022dec3"></a>

```c
#define ANT_SEL 1
```

相关声明：[ANT_SEL](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#ga468e1c5d4d85203d0d644dd0e022dec3)。

为天线选择合适的 ST87 输入端：全球导航卫星系统（GNSS）或窄带物联网（NB-IoT）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 40.3\_类型定义（Typedefs）

<a id="r_ga36695a0b14a8ac128692a3a543a2e1b1"></a>

```c
typedef void st87mxx_get_beacon_data_callback_t(char const *const string)
```

相关声明：[st87mxx_get_beacon_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga36695a0b14a8ac128692a3a543a2e1b1)。

在 Wi-Fi 扫描数据（Scan Data）可用时捕获该数据的回调。

<a id="r_ga92a4c4d49be58a5d8c3db059116cd38e"></a>

```c
typedef void st87mxx_get_pos_callback_t(char const *const string)
```

相关声明：[st87mxx_get_pos_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga92a4c4d49be58a5d8c3db059116cd38e)。

获取位置（Positions）的回调。

<a id="r_ga64d19b3167aae5fd3b4a372222534e23"></a>

```c
typedef void st87mxx_get_rssi_callback_t(char const *const string)
```

相关声明：[st87mxx_get_rssi_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga64d19b3167aae5fd3b4a372222534e23)。

获取接收信号强度指示值（RSSI Values）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 40.4\_枚举（Enumerations）

<a id="r_ga6c28c45f3910a0e33a8026fc87133247"></a>

```c
enum sequence_state { SEQUENCE_NONE = 0 , SEQUENCE_ONGOING = 1 , SEQUENCE_TIMED_OUT = 2 }
```

相关声明：[sequence_state](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga6c28c45f3910a0e33a8026fc87133247)、[SEQUENCE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d)、[SEQUENCE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd)、[SEQUENCE_TIMED_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd)。

应用服务序列状态（Application Services Sequence State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.5\_函数（Functions）

<a id="r_ga2227c0f901ef6acc105f7a823f014958"></a>

```c
void st87mxx_app_services_init (void)
```

相关声明：[st87mxx_app_services_init](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga2227c0f901ef6acc105f7a823f014958)。

启动应用服务（Application Services）的 API，包括 GNSS、WSCAN 和 RSSI 采集。

<a id="r_gaf711155377231afc1ad969cb397818cd"></a>

```c
int st87mxx_gnss_getfix (uint32_t nb_position, st87mxx_get_pos_callback_t *get_pos_callback_func, uint32_t timeout)
```

相关声明：[st87mxx_gnss_getfix](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaf711155377231afc1ad969cb397818cd)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[st87mxx_get_pos_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga92a4c4d49be58a5d8c3db059116cd38e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 ST87Mxx GNSS 位置（Position）的 API。

<a id="r_gaea2db4c02a45f514f14c2f2913a36915"></a>

```c
void st87mxx_gnss_stop (void)
```

相关声明：[st87mxx_gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaea2db4c02a45f514f14c2f2913a36915)。

停止 GNSS 功能（Feature）的 API。

<a id="r_ga48d42b0ba645e8caa53b49e4842c1276"></a>

```c
int st87mxx_wifiscan (st87mxx_wifiscan_params *wscan_params)
```

相关声明：[st87mxx_wifiscan](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga48d42b0ba645e8caa53b49e4842c1276)、[st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)。

启动用于定位的 Wi-Fi 扫描（WSCAN）功能的 API。

<a id="r_ga462eeda7a3702664f9c8d80a7d780c64"></a>

```c
void st87mxx_wifiscan_stop (void)
```

相关声明：[st87mxx_wifiscan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga462eeda7a3702664f9c8d80a7d780c64)。

停止 Wi-Fi 扫描（Scan）的 API。

<a id="r_gae459a9137139217ee997b7e48fcc30f6"></a>

```c
int st87mxx_getrssi (st87mxx_get_rssi_callback_t *get_rssi_callback_func)
```

相关声明：[st87mxx_getrssi](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gae459a9137139217ee997b7e48fcc30f6)、[st87mxx_get_rssi_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga64d19b3167aae5fd3b4a372222534e23)。

异步（Asynchronously）获取 RSSI 的 API。

<a id="r_gafefe0b51707586c520dd966c4a271fa1"></a>

```c
sequence_state st87mxx_app_services_getstate (void)
```

相关声明：[sequence_state](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga6c28c45f3910a0e33a8026fc87133247)、[st87mxx_app_services_getstate](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gafefe0b51707586c520dd966c4a271fa1)。

获取应用服务序列状态（Application Services Sequence State）的 API。


## 40.6\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P813_st87mxx_app_services.h_源码浏览.md)
- [st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)
- [APP_MDM_CMD_TIMEOUT](../api_platform_topic_reference/P123_ST87Mxx 常量（Constants）.md#ga54b2d06b56d845ca68886b94719fe64b)
- [K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [GNSS_NB_MAX_POSITION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9e5cd8119ca22dcfca38e80eb9e67b5)
- [GNSS_CONSTELLATION_ID](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gac8b2c26a1f22ddd6c86c711440705fc0)
- [GNSS_FORMAT_TYPE](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga1afd16e81b65c2e7a4fa55aa0895d542)
- [GNSS_FORMAT_ST_POSITION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gac44b0f5695f8e52c6180814794df0966)
- [GNSS_FORMAT_ST_ACCURACY](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga278ff798327ebe4a97f5f40a94bdd19e)
- [GNSS_FORMAT_ST_SATELLITES](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae58c597d5bdfdca7d2d7364166d3dfb9)
- [GNSS_FORMAT_ST_ORIENTATION](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga52795780fd3c29a7bcf3578f5c68dc51)
- [GNSS_NMEA_GPGGA](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga88310315fe7e1af0a79b2ecf96c58695)
- [GNSS_NMEA_GPGSA](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9e75d7eddd291e5bf44e73196f7214e)
- [GNSS_NMEA_GPGSV](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#gae9089b6e0aafd2f90510267771d84421)
- [GNSS_NMEA_GPGLL](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga92c0f36c2f84bd0d6e43e6bcc3363b20)
- [GNSS_NMEA_GPRMC](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga107dac8cf6c95dad3e924e0275dfca9a)
- [GNSS_NMEA_GPVTG](../api_interaction_transport_topic_reference/P018_全球导航卫星系统（GNSS）配置.md#ga3d8409b1a22446f3926589e15d73db25)
- [URC_MODE](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#gac67a00c5b9b85afbb2c76a3b44d04f9d)
- [HOPPING_TIME](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#ga9e38942a920e3dbb9101c0388fdf137d)
- [ANT_SEL](../api_protocol_topic_reference/P059_Wi-Fi 扫描配置（Scanning configuration）.md#ga468e1c5d4d85203d0d644dd0e022dec3)
- [st87mxx_get_beacon_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga36695a0b14a8ac128692a3a543a2e1b1)
- [st87mxx_get_pos_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga92a4c4d49be58a5d8c3db059116cd38e)
- [st87mxx_get_rssi_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga64d19b3167aae5fd3b4a372222534e23)
- [sequence_state](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga6c28c45f3910a0e33a8026fc87133247)
- [SEQUENCE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d)
- [SEQUENCE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd)
- [SEQUENCE_TIMED_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd)
- [st87mxx_app_services_init](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga2227c0f901ef6acc105f7a823f014958)
- [st87mxx_gnss_getfix](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaf711155377231afc1ad969cb397818cd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [st87mxx_gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaea2db4c02a45f514f14c2f2913a36915)
- [st87mxx_wifiscan](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga48d42b0ba645e8caa53b49e4842c1276)
- [st87mxx_wifiscan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga462eeda7a3702664f9c8d80a7d780c64)
- [st87mxx_getrssi](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gae459a9137139217ee997b7e48fcc30f6)
- [st87mxx_app_services_getstate](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gafefe0b51707586c520dd966c4a271fa1)

<a id="header-details"></a>

---

[上一章](P039_zephyr__mgmt__mcumgr__transport__smp_raw_dummy.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__drivers__sensor__tdk_apex.h_文件参考.md)
