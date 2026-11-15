---
id: learning.zephyr-docs.api-hl78xx-modem-reference.page-1
title: HL78xx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_HL78xx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sierra Wireless HL78xx 蜂窝调制解调器（Cellular modems）。

<a id="details"></a>

Sierra Wireless HL78xx 蜂窝调制解调器（Cellular modems）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_hl78xx_5Fapis_2Eh"></a>

```c
file hl78xx_apis.h
```

相关声明：[hl78xx_apis.h](../api_file_modem_network_reference/P001_zephyr__drivers__modem__hl78xx_apis.h_文件参考.md)。

HL78xx调制解调器（Modems）扩展蜂窝通信API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_kselacq_5Fsyntax"></a>

```c
struct kselacq_syntax
```

相关声明：[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

KSELACQ无线接入技术（RAT）的配置语法。

<a id="r_hl78xx_5Fcxreg_5Fstatus"></a>

```c
struct hl78xx_cxreg_status
```

相关声明：[hl78xx_cxreg_status](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md)。

缓存的+CEREG/+CREG注册详情。

<a id="r_hl78xx_5Fnetwork_5Foperator"></a>

```c
struct hl78xx_network_operator
```

相关声明：[hl78xx_network_operator](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md)。

缓存的网络运营商信息（Network Operator Information）。

<a id="r_hl78xx_5Fnetwork_5Finfo"></a>

```c
struct hl78xx_network_info
```

相关声明：[hl78xx_network_info](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md)。

缓存的网络信息（Network Information）。

<a id="r_hl78xx_5Fagnss_5Fstatus"></a>

```c
struct hl78xx_agnss_status
```

相关声明：[hl78xx_agnss_status](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md)。

辅助全球导航卫星系统（A-GNSS）的辅助数据状态结构。

<a id="r_k_5Fcellmeas_5Fsignal_5Finfo"></a>

```c
struct k_cellmeas_signal_info
```

相关声明：[k_cellmeas_signal_info](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md)。

蜂窝通信测量信号信息（Cellular Measurement Signal Information）。

<a id="r_hl78xx_5Fnetwork"></a>

```c
struct hl78xx_network
```

相关声明：[hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)。

蜂窝网络（Cellular Network）结构。

<a id="r_hl78xx_5Fctzeu_5Fupdate"></a>

```c
struct hl78xx_ctzeu_update
```

相关声明：[hl78xx_ctzeu_update](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md)。

已解析的+CTZEU更新载荷。

<a id="r_hl78xx_5Fevt"></a>

```c
struct hl78xx_evt
```

相关声明：[hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)。

HL78xx的事件结构。

<a id="r_nmea_5Fmatch_5Fgsa_5Fdata"></a>

```c
struct nmea_match_gsa_data
```

相关声明：[nmea_match_gsa_data](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md)。

已解析的GSA语句数据，即GNSS精度衰减因子（DOP）及活动卫星数据。

<a id="r_nmea_5Fmatch_5Fgst_5Fdata"></a>

```c
struct nmea_match_gst_data
```

相关声明：[nmea_match_gst_data](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md)。

已解析的GST语句数据，即GNSS伪距误差统计（Pseudorange Error Statistics）。

<a id="r_nmea_5Fmatch_5Fepu_5Fdata"></a>

```c
struct nmea_match_epu_data
```

相关声明：[nmea_match_epu_data](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md)。

已解析的EPU语句数据，即HL78xx专有的位置误差（Position Error）数据。

<a id="r_hl78xx_5Fgnss_5Fnmea_5Faux_5Fdata"></a>

```c
struct hl78xx_gnss_nmea_aux_data
```

相关声明：[hl78xx_gnss_nmea_aux_data](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md)。

全部GNSS辅助NMEA数据的容器。

<a id="r_hl78xx_5Fgnss_5Faux_5Fdata_5Fcallback"></a>

```c
struct hl78xx_gnss_aux_data_callback
```

相关声明：[hl78xx_gnss_aux_data_callback](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md)。

全球导航卫星系统（GNSS）辅助数据的回调结构。

<a id="r_hl78xx_5Fat_5Fnotification"></a>

```c
struct hl78xx_at_notification
```

相关声明：[hl78xx_at_notification](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md)。

已解析的主动AT通知（Unsolicited AT Notification）载荷。

<a id="r_hl78xx_5Fat_5Fmonitor_5Fentry"></a>

```c
struct hl78xx_at_monitor_entry
```

相关声明：[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

AT监测器（AT Monitor）的条目结构。

<a id="r_hl78xx_5Fevt_5Fmonitor_5Fentry"></a>

```c
struct hl78xx_evt_monitor_entry
```

相关声明：[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

事件监测器（Event Monitor）的条目结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.3\_宏定义（Macros）

<a id="r_ga8c28a5a32edb83ea0b0120dd3b00451f"></a>

```c
#define CSQ_RSSI_UNKNOWN (99)
```

相关声明：[CSQ_RSSI_UNKNOWN](#ga8c28a5a32edb83ea0b0120dd3b00451f)。

`AT+CSQ` 命令返回的未知接收信号强度指示（RSSI）值。

<a id="r_gab2c8054a088aa6927aa10f1aed1587ae"></a>

```c
#define CSQ_RSSI_MAX (31)
```

相关声明：[CSQ_RSSI_MAX](#gab2c8054a088aa6927aa10f1aed1587ae)。

`AT+CSQ` 命令返回的最大有效接收信号强度指示（RSSI）编码。

<a id="r_ga03c48d45ba1dfcdeabba881f2b1cd936"></a>

```c
#define CESQ_RSRP_UNKNOWN (255)
```

相关声明：[CESQ_RSRP_UNKNOWN](#ga03c48d45ba1dfcdeabba881f2b1cd936)。

`AT+CESQ` 命令返回的未知参考信号接收功率（RSRP）值。

<a id="r_gacb02197961c70e98147ae25e4c11d4de"></a>

```c
#define CESQ_RSRP_MAX (97)
```

相关声明：[CESQ_RSRP_MAX](#gacb02197961c70e98147ae25e4c11d4de)。

`AT+CESQ` 命令返回的最大有效参考信号接收功率（RSRP）编码。

<a id="r_ga9a4429e44439c5ebdd18ccd549f832f5"></a>

```c
#define CESQ_RSRQ_UNKNOWN (255)
```

相关声明：[CESQ_RSRQ_UNKNOWN](#ga9a4429e44439c5ebdd18ccd549f832f5)。

`AT+CESQ` 命令返回的未知参考信号接收质量（RSRQ）值。

<a id="r_ga7d02276973c71eded42d4242a34ca745"></a>

```c
#define CESQ_RSRQ_MAX (34)
```

相关声明：[CESQ_RSRQ_MAX](#ga7d02276973c71eded42d4242a34ca745)。

`AT+CESQ` 命令返回的最大有效参考信号接收质量（RSRQ）编码。

<a id="r_gac53a8b20d353944744e259f1f9008d44"></a>

```c
#define HL78XX_MODEM_AT_ERROR 1
```

相关声明：[HL78XX_MODEM_AT_ERROR](#gac53a8b20d353944744e259f1f9008d44)。

公共 AT 辅助函数返回通用 `ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga23bb6b58819d70eb379f89a3878c07d0"></a>

```c
#define HL78XX_MODEM_AT_CME_ERROR 2
```

相关声明：[HL78XX_MODEM_AT_CME_ERROR](#ga23bb6b58819d70eb379f89a3878c07d0)。

公共 AT 辅助函数返回 `+CME ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga0fef7f6b540d959bf391ac39d8c2738a"></a>

```c
#define HL78XX_MODEM_AT_CMS_ERROR 3
```

相关声明：[HL78XX_MODEM_AT_CMS_ERROR](#ga0fef7f6b540d959bf391ac39d8c2738a)。

公共 AT 辅助函数返回 `+CMS ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga72dfe852d4d6365d80f33b918f631501"></a>

```c
#define CSQ_RSSI_TO_DB(v)
```

相关声明：[CSQ_RSSI_TO_DB](#ga72dfe852d4d6365d80f33b918f631501)。

将 CSQ 接收信号强度指示（RSSI）值转换为 dBm。

<a id="r_ga309cc2c1be1d4006e2ccb8d59cb3e916"></a>

```c
#define CESQ_RSRP_TO_DB(v)
```

相关声明：[CESQ_RSRP_TO_DB](#ga309cc2c1be1d4006e2ccb8d59cb3e916)。

将 CESQ 参考信号接收功率（RSRP）值转换为 dBm。

<a id="r_ga536c21c42099fc04ac85a634ffa41d24"></a>

```c
#define CESQ_RSRQ_TO_DB(v)
```

相关声明：[CESQ_RSRQ_TO_DB](#ga536c21c42099fc04ac85a634ffa41d24)。

将 CESQ 参考信号接收质量（RSRQ）值转换为 dB。

<a id="r_ga734b46dfd78fbf6fc938a6f9115f2cc7"></a>

```c
#define PAUSED 1
```

相关声明：[PAUSED](#ga734b46dfd78fbf6fc938a6f9115f2cc7)。

监视器已暂停。

<a id="r_ga3a6d3cd70078e6046471ec528a09cd19"></a>

```c
#define ACTIVE 0
```

相关声明：[ACTIVE](#ga3a6d3cd70078e6046471ec528a09cd19)。

监视器（Monitor）处于活动状态，默认值。

<a id="r_ga9587840c88858d1c26bd3afedd96bd68"></a>

```c
#define MDM_MANUFACTURER_LENGTH 20
```

相关声明：[MDM_MANUFACTURER_LENGTH](#ga9587840c88858d1c26bd3afedd96bd68)。

调制解调器制造商字符串（Modem Manufacturer String）的最大长度。

<a id="r_ga694436b7ecedfd934f78afa9f404cadb"></a>

```c
#define MDM_MODEL_LENGTH 32
```

相关声明：[MDM_MODEL_LENGTH](#ga694436b7ecedfd934f78afa9f404cadb)。

调制解调器型号字符串（Modem Model String）的最大长度。

<a id="r_ga6327f0d9596ad616f844687ac0fbc4f9"></a>

```c
#define MDM_REVISION_LENGTH 64
```

相关声明：[MDM_REVISION_LENGTH](#ga6327f0d9596ad616f844687ac0fbc4f9)。

调制解调器修订版本字符串（Modem Revision String）的最大长度。

<a id="r_ga9213ea6a80a1f80b10ade16314fa56dd"></a>

```c
#define MDM_IMEI_LENGTH 16
```

相关声明：[MDM_IMEI_LENGTH](#ga9213ea6a80a1f80b10ade16314fa56dd)。

调制解调器国际移动设备识别码（IMEI）字符串的最大长度。

<a id="r_ga9c11717136907c549f2ddb5c9bab48b7"></a>

```c
#define MDM_IMSI_LENGTH 23
```

相关声明：[MDM_IMSI_LENGTH](#ga9c11717136907c549f2ddb5c9bab48b7)。

调制解调器国际移动用户识别码（IMSI）字符串的最大长度。

<a id="r_gaa14eef37d2beacdb02a50ec4eb93d1fd"></a>

```c
#define MDM_ICCID_LENGTH 22
```

相关声明：[MDM_ICCID_LENGTH](#gaa14eef37d2beacdb02a50ec4eb93d1fd)。

调制解调器集成电路卡识别码（ICCID）字符串的最大长度。

<a id="r_ga2586187555aed092ffbf40e7991cc266"></a>

```c
#define MDM_APN_MAX_LENGTH 64
```

相关声明：[MDM_APN_MAX_LENGTH](#ga2586187555aed092ffbf40e7991cc266)。

接入点名称（APN）字符串的最大长度。

<a id="r_ga0a99d20ad7b62fd41c0118e2f5af522b"></a>

```c
#define MDM_MAX_CERT_LENGTH 4096
```

相关声明：[MDM_MAX_CERT_LENGTH](#ga0a99d20ad7b62fd41c0118e2f5af522b)。

证书（Certificate）的最大长度。

<a id="r_gaad7153fc809f017cd727bc60988fd799"></a>

```c
#define MDM_MAX_HOSTNAME_LEN 128
```

相关声明：[MDM_MAX_HOSTNAME_LEN](#gaad7153fc809f017cd727bc60988fd799)。

主机名（Hostname）的最大长度。

<a id="r_gae2d73fc3652b58cc2d2b8bfb72f6e86d"></a>

```c
#define MDM_SERIAL_NUMBER_LENGTH 32
```

相关声明：[MDM_SERIAL_NUMBER_LENGTH](#gae2d73fc3652b58cc2d2b8bfb72f6e86d)。

序列号字符串（Serial Number String）的最大长度。

<a id="r_gaea97e8a895c9bad91eead2e631934bda"></a>

```c
#define HL78XX_CTZEU_UTIME_MAX_LEN 32
```

相关声明：[HL78XX_CTZEU_UTIME_MAX_LEN](#gaea97e8a895c9bad91eead2e631934bda)。

用于提取出的 `+CTZEU` 通用时间字符串（Universal Time Strings）的推荐缓冲区大小。

<a id="r_ga0d3e4dcb509b56886297f2f451f4d952"></a>

```c
#define HL78XX_CEREG_TIMER_STR_LEN 9
```

相关声明：[HL78XX_CEREG_TIMER_STR_LEN](#ga0d3e4dcb509b56886297f2f451f4d952)。

CEREG 定时器字符串（Timer String）的最大长度。

<a id="r_ga1dd356d88b67261a642ba50730b31b48"></a>

```c
#define HL78XX_NETWORK_ADDRESS_MAX_LEN 46
```

相关声明：[HL78XX_NETWORK_ADDRESS_MAX_LEN](#ga1dd356d88b67261a642ba50730b31b48)。

网络地址字符串（Network Address String）的最大长度。

<a id="r_ga8bc5d49dd46c8bff682528127310a1eb"></a>

```c
#define MDM_HL78XX_EOF_PATTERN "--EOF--Pattern--"
```

相关声明：[MDM_HL78XX_EOF_PATTERN](#ga8bc5d49dd46c8bff682528127310a1eb)。

用于指示文件结束（End-of-file）或数据传输完成（Completion of Data Transmission）的模式。

<a id="r_ga00e8685b8a1c0b4a9b5ba18dfdd7c879"></a>

```c
#define MDM_HL78XX_TERMINATION_PATTERN "+++"
```

相关声明：[MDM_HL78XX_TERMINATION_PATTERN](#ga00e8685b8a1c0b4a9b5ba18dfdd7c879)。

用于退出数据模式（Data Mode）、返回命令模式（Command Mode）的转义／终止序列（Escape/Termination Sequence）。

<a id="r_gab53f7ed6e7b4b70f7675184e666bf9f0"></a>

```c
#define MDM_HL78XX_CONNECT_STRING "CONNECT"
```

相关声明：[MDM_HL78XX_CONNECT_STRING](#gab53f7ed6e7b4b70f7675184e666bf9f0)。

表示已成功建立数据连接（Data Connection）的响应字符串。

<a id="r_gae2b96cddac89ab608658fe11bfdac45e"></a>

```c
#define MDM_HL78XX_NO_CARRIER_STRING "NO CARRIER"
```

相关声明：[MDM_HL78XX_NO_CARRIER_STRING](#gae2b96cddac89ab608658fe11bfdac45e)。

表示连接已丢失或终止（Lost or Terminated）的响应字符串。

<a id="r_ga1760f6b6b71f238b2e4a4f2082899dd7"></a>

```c
#define MDM_HL78XX_CME_ERROR_STRING "+CME ERROR: "
```

相关声明：[MDM_HL78XX_CME_ERROR_STRING](#ga1760f6b6b71f238b2e4a4f2082899dd7)。

移动设备（Mobile Equipment，CME）错误响应的前缀，通常后跟错误码（Error Code）。

<a id="r_ga65d332f108a5cbc6e3038db4fa2fee65"></a>

```c
#define MDM_HL78XX_CMS_ERROR_STRING "+CMS ERROR: "
```

相关声明：[MDM_HL78XX_CMS_ERROR_STRING](#ga65d332f108a5cbc6e3038db4fa2fee65)。

消息服务（Message Service，CMS）错误响应的前缀，通常与短信（SMS）操作相关。

<a id="r_gac06ec76b0de379682110e590c4b400de"></a>

```c
#define MDM_HL78XX_ERROR_STRING "ERROR"
```

相关声明：[MDM_HL78XX_ERROR_STRING](#gac06ec76b0de379682110e590c4b400de)。

表示命令失败（Command Failure）的通用错误响应字符串。

<a id="r_ga08eaa30cab6c59b2b4e9e33ff8c12704"></a>

```c
#define MDM_HL78XX_OK_STRING "OK"
```

相关声明：[MDM_HL78XX_OK_STRING](#ga08eaa30cab6c59b2b4e9e33ff8c12704)。

表示 AT 命令成功执行（Successful Execution）的标准响应字符串。

<a id="r_ga6b0f0f61bd70c9e09031ecdb9dcf2f52"></a>

```c
#define MDM_HL78XX_DESIRED_VERSION_STRING
```

相关声明：[MDM_HL78XX_DESIRED_VERSION_STRING](#ga6b0f0f61bd70c9e09031ecdb9dcf2f52)。

期望的固件版本字符串（Firmware Version String）。

<a id="r_ga0381c6c5a47121b422c0f5d456e86432"></a>

```c
#define HL78XX_MONITOR_ACTIVE false
```

相关声明：[HL78XX_MONITOR_ACTIVE](#ga0381c6c5a47121b422c0f5d456e86432)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

HL78xx 监视器（Monitor）的初始活动状态（Active State）。

<a id="r_gac485491202b429e8512c210360d1b2f9"></a>

```c
#define HL78XX_MONITOR_PAUSED true
```

相关声明：[HL78XX_MONITOR_PAUSED](#gac485491202b429e8512c210360d1b2f9)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

HL78xx 监视器（Monitor）的初始暂停状态（Paused State）。

<a id="r_gabe2427817d9dea113ac5f748b9148357"></a>

```c
#define HL78XX_MONITOR_INITIAL_PAUSED(...)
```

相关声明：[HL78XX_MONITOR_INITIAL_PAUSED](#gabe2427817d9dea113ac5f748b9148357)。

解析可选的监视器初始状态参数（Monitor Initial State Argument）。

<a id="r_gaa23bb8ced0d5b912309228525736234a"></a>

```c
#define HL78XX_EVT_MONITOR(name, _handler, ...)
```

相关声明：[HL78XX_EVT_MONITOR](#gaa23bb8ced0d5b912309228525736234a)。

定义事件监视器（Event Monitor），在系统工作队列线程（System Workqueue Thread）中接收通知。

<a id="r_ga48b0f02ea31d612d867db6bf2a62fb46"></a>

```c
#define HL78XX_AT_MONITOR_ANY NULL
```

相关声明：[HL78XX_AT_MONITOR_ANY](#ga48b0f02ea31d612d867db6bf2a62fb46)。

监视任何已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_gadc4cc789837650b5e20e9bf5f6d85067"></a>

```c
#define HL78XX_AT_MONITOR(name, _filter, _handler, ...)
```

相关声明：[HL78XX_AT_MONITOR](#gadc4cc789837650b5e20e9bf5f6d85067)。

定义 AT 监视器（AT Monitor），在系统工作队列线程（System Workqueue Thread）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_ga370b450dc0ab247343d3406e7fc664da"></a>

```c
#define HL78XX_AT_MONITOR_DIRECT(name, _filter, _handler, ...)
```

相关声明：[HL78XX_AT_MONITOR_DIRECT](#ga370b450dc0ab247343d3406e7fc664da)。

定义 AT 监视器（AT Monitor），直接在 HL78xx 调制解调器接收工作队列上下文（RX Workqueue Context）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_ga7da0c70a3435693c416c28a27b4ab1c5"></a>

```c
#define GNSS_AUX_DATA_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_AUX_DATA_CALLBACK_DEFINE](#ga7da0c70a3435693c416c28a27b4ab1c5)。

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

<a id="r_gab77a5c59a2b5297b7bc69afffb21dc73"></a>

```c
#define GNSS_DT_AUX_DATA_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_AUX_DATA_CALLBACK_DEFINE](#gab77a5c59a2b5297b7bc69afffb21dc73)。

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.4\_类型定义（Typedefs）

<a id="r_ga82793d1f4c0c8f03ae27b29afa1c3d3f"></a>

```c
typedef bool(* hl78xx_runtime_band_provider_t) (const struct device *dev, enum hl78xx_cell_rat_mode rat, uint16_t *band, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_runtime_band_provider_t](#ga82793d1f4c0c8f03ae27b29afa1c3d3f)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_cell_rat_mode](#ga298f953be96ab47be40b5440a2573182)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于为无线接入技术（RAT）提供可选运行时频段覆盖设置（Runtime Band Override）的回调。

<a id="r_ga9198bafcc7c78243fc72ca2b0bc926ed"></a>

```c
typedef void(* hl78xx_gnss_aux_data_callback_t) (const struct device *dev, const struct hl78xx_gnss_nmea_aux_data *aux_data, uint16_t size)
```

相关声明：[hl78xx_gnss_aux_data_callback_t](#ga9198bafcc7c78243fc72ca2b0bc926ed)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_gnss_nmea_aux_data](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

全球导航卫星系统（GNSS）辅助数据回调的函数类型（Callback Function Type）。

<a id="r_ga03910e4575bfd4ed439e1c9a0220c7a2"></a>

```c
typedef int(* hl78xx_api_configure_networks) (const struct device *dev, const struct hl78xx_network *networks, uint8_t size)
```

相关声明：[hl78xx_api_configure_networks](#ga03910e4575bfd4ed439e1c9a0220c7a2)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于配置网络（Networks）的 API 函数指针。

<a id="r_ga6bf75bd8e583b4e076b73268a712977d"></a>

```c
typedef int(* hl78xx_api_get_supported_networks) (const struct device *dev, const struct hl78xx_network **networks, uint8_t *size)
```

相关声明：[hl78xx_api_get_supported_networks](#ga6bf75bd8e583b4e076b73268a712977d)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于获取支持的网络（Supported Networks）的 API 函数指针。

<a id="r_ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a"></a>

```c
typedef int(* hl78xx_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[hl78xx_api_get_signal](#ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

用于获取网络信号强度（signal strength）的 API。

<a id="r_gaa7cb75a0ef3cd4cb607bb0e3f3b3468f"></a>

```c
typedef int(* hl78xx_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[hl78xx_api_get_modem_info](#gaa7cb75a0ef3cd4cb607bb0e3f3b3468f)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)。

用于获取调制解调器信息（Modem Information）的 API 函数指针。

<a id="r_ga586f65e3f3ea8852261be04ce7ba67ba"></a>

```c
typedef int(* hl78xx_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[hl78xx_api_get_registration_status](#ga586f65e3f3ea8852261be04ce7ba67ba)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga7309390ed507748fdb72cf078b8e08a4)。

用于获取注册状态（registration status）的 API。

<a id="r_ga7cf1c4b11a828c186771200cd00b3bc8"></a>

```c
typedef int(* hl78xx_api_set_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_api_set_phone_functionality](#ga7cf1c4b11a828c186771200cd00b3bc8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于设置电话功能（Phone Functionality）的 API 函数指针。

<a id="r_gab3bcb3ba4cef24971acc41aa0815abe5"></a>

```c
typedef int(* hl78xx_api_get_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_api_get_phone_functionality](#gab3bcb3ba4cef24971acc41aa0815abe5)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)。

用于获取电话功能（Phone Functionality）的 API。

<a id="r_ga8201489ac8055efa3019ffd8f3201644"></a>

```c
typedef int(* hl78xx_api_send_at_cmd) (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_api_send_at_cmd](#ga8201489ac8055efa3019ffd8f3201644)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于获取电话功能（Phone Functionality）的 API。

<a id="r_ga98fde2c3465abce3b4b7d94816bc029c"></a>

```c
typedef void(* hl78xx_at_monitor_handler_t) (const struct hl78xx_at_notification *notif, struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_handler_t](#ga98fde2c3465abce3b4b7d94816bc029c)、[hl78xx_at_notification](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

AT 监视器处理函数（AT Monitor Handler）的函数类型。

<a id="r_ga517a58c85701991214ddb3a9d786f367"></a>

```c
typedef void(* hl78xx_at_monitor_release_t) (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_release_t](#ga517a58c85701991214ddb3a9d786f367)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

AT 监视器释放函数（AT Monitor Release）的函数类型。

<a id="r_gade4999c5b603813020cd52a93687b76f"></a>

```c
typedef void(* hl78xx_evt_monitor_dispatcher_t) (struct hl78xx_evt *notif)
```

相关声明：[hl78xx_evt_monitor_dispatcher_t](#gade4999c5b603813020cd52a93687b76f)、[hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)。

事件监视器分派函数（Event Monitor Dispatcher）的函数类型。

<a id="r_gaa1346c7b8b44abae64f59cc8d5fa9c01"></a>

```c
typedef void(* hl78xx_evt_monitor_handler_t) (struct hl78xx_evt *notif, struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_handler_t](#gaa1346c7b8b44abae64f59cc8d5fa9c01)、[hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

事件监视器处理函数（Event Monitor Handler）的函数类型。

<a id="r_ga774bbdee241bfb63374fdc74d2353a3d"></a>

```c
typedef void(* hl78xx_evt_monitor_release_t) (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_release_t](#ga774bbdee241bfb63374fdc74d2353a3d)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

事件监视器释放函数（Event Monitor Release）的函数类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.5\_枚举（Enumerations）

<a id="r_ga298f953be96ab47be40b5440a2573182"></a>

```c
enum hl78xx_cell_rat_mode { HL78XX_RAT_CAT_M1 = 0 , HL78XX_RAT_NB1 , HL78XX_RAT_GSM , HL78XX_RAT_NBNTN , HL78XX_RAT_MODE_AUTO , HL78XX_RAT_MODE_NONE , HL78XX_RAT_COUNT = HL78XX_RAT_MODE_NONE }
```

相关声明：[hl78xx_cell_rat_mode](#ga298f953be96ab47be40b5440a2573182)、[HL78XX_RAT_CAT_M1](#gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b)、[HL78XX_RAT_NB1](#gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e)、[HL78XX_RAT_GSM](#gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d)、[HL78XX_RAT_NBNTN](#gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d)、[HL78XX_RAT_MODE_AUTO](#gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b)、[HL78XX_RAT_MODE_NONE](#gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f)、[HL78XX_RAT_COUNT](#gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422)。

蜂窝无线接入技术（Cellular Radio Access Technologies）。

<a id="r_gaf2ab6a096dff081e7cbbba13b06de3cc"></a>

```c
enum hl78xx_kselacq_rat { HL78XX_KSELACQ_RAT_CLEAR = 0 , HL78XX_KSELACQ_RAT_CAT_M1 = 1 , HL78XX_KSELACQ_RAT_NB1 = 2 , HL78XX_KSELACQ_RAT_GSM = 3 }
```

相关声明：[hl78xx_kselacq_rat](#gaf2ab6a096dff081e7cbbba13b06de3cc)、[HL78XX_KSELACQ_RAT_CLEAR](#ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850)、[HL78XX_KSELACQ_RAT_CAT_M1](#ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f)、[HL78XX_KSELACQ_RAT_NB1](#ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca)、[HL78XX_KSELACQ_RAT_GSM](#ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30)。

原始 `AT+KSELACQ` 首选列表（PRL）中的无线接入技术（RAT）条目。

<a id="r_ga39a3de13bd706571cd7348ea46b7b708"></a>

```c
enum hl78xx_phone_functionality { HL78XX_SIM_POWER_OFF , HL78XX_FULLY_FUNCTIONAL , HL78XX_AIRPLANE = 4 }
```

相关声明：[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)、[HL78XX_SIM_POWER_OFF](#gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf)、[HL78XX_FULLY_FUNCTIONAL](#gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba)、[HL78XX_AIRPLANE](#gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570)。

电话功能模式（Phone Functionality Modes）。

<a id="r_ga0b3efb75d166d9d4bf163ffc6bb68fc0"></a>

```c
enum hl78xx_sim_slot { HL78XX_SIM_SLOT_1 = 0 , HL78XX_SIM_SLOT_2 = 1 }
```

相关声明：[hl78xx_sim_slot](#ga0b3efb75d166d9d4bf163ffc6bb68fc0)、[HL78XX_SIM_SLOT_1](#gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576)、[HL78XX_SIM_SLOT_2](#gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794)。

由可选 SIM 切换 GPIO（SIM-switch GPIO）驱动的外部 SIM 卡槽选择（External SIM Slot Selection）。

<a id="r_ga618c248d23a1db1b027333c92adf99a1"></a>

```c
enum hl78xx_modem_restart_mode { HL78XX_MODEM_RESTART_HARD = 0 , HL78XX_MODEM_RESTART_SOFT }
```

相关声明：[hl78xx_modem_restart_mode](#ga618c248d23a1db1b027333c92adf99a1)、[HL78XX_MODEM_RESTART_HARD](#gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc)、[HL78XX_MODEM_RESTART_SOFT](#gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8)。

由驱动管理的调制解调器重启模式（Driver-managed Modem Restart Modes）。

<a id="r_gab4a85c57d2f77c04a887f6552abff48a"></a>

```c
enum hl78xx_module_status { HL78XX_MODULE_READY = 0 , HL78XX_MODULE_WAITING_FOR_ACCESS_CODE , HL78XX_MODULE_SIM_NOT_PRESENT , HL78XX_MODULE_SIMLOCK , HL78XX_MODULE_UNRECOVERABLE_ERROR , HL78XX_MODULE_UNKNOWN_STATE , HL78XX_MODULE_INACTIVE_SIM }
```

相关声明：[hl78xx_module_status](#gab4a85c57d2f77c04a887f6552abff48a)、[HL78XX_MODULE_READY](#ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db)、[HL78XX_MODULE_WAITING_FOR_ACCESS_CODE](#ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820)、[HL78XX_MODULE_SIM_NOT_PRESENT](#ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9)、[HL78XX_MODULE_SIMLOCK](#ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f)、[HL78XX_MODULE_UNRECOVERABLE_ERROR](#ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294)、[HL78XX_MODULE_UNKNOWN_STATE](#ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6)、[HL78XX_MODULE_INACTIVE_SIM](#ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3)。

模块状态码（Module Status Codes）。

<a id="r_gaadcca229cbccc9832734bcc4e2a443e6"></a>

```c
enum hl78xx_modem_info_type { HL78XX_MODEM_INFO_SERIAL_NUMBER , HL78XX_MODEM_INFO_CURRENT_BAUD_RATE , HL78XX_MODEM_INFO_FW_VERSION }
```

相关声明：[hl78xx_modem_info_type](#gaadcca229cbccc9832734bcc4e2a443e6)、[HL78XX_MODEM_INFO_SERIAL_NUMBER](#ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8)、[HL78XX_MODEM_INFO_CURRENT_BAUD_RATE](#ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd)、[HL78XX_MODEM_INFO_FW_VERSION](#ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca)。

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

<a id="r_ga2d26ae6044baac5995f4184abe4faad3"></a>

```c
enum hl78xx_operator_format { HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC = 0 , HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC , HL78XX_OPERATOR_FORMAT_NUMERIC }
```

相关声明：[hl78xx_operator_format](#ga2d26ae6044baac5995f4184abe4faad3)、[HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC](#gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c)、[HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC](#gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164)、[HL78XX_OPERATOR_FORMAT_NUMERIC](#gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9)。

网络运营商格式选项（Network Operator Format Options）。

<a id="r_ga563d651fff3621c1e21d7c47d19fd218"></a>

```c
enum hl78xx_network_info_type { HL78XX_NETWORK_INFO_APN , HL78XX_NETWORK_INFO_CURRENT_RAT , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC , HL78XX_NETWORK_INFO_OPERATOR_FORMAT , HL78XX_NETWORK_INFO_TAC , HL78XX_NETWORK_INFO_MCC , HL78XX_NETWORK_INFO_MNC , HL78XX_NETWORK_INFO_CELL_ID , HL78XX_NETWORK_INFO_IP_ADDRESS , HL78XX_NETWORK_INFO_DNS_PRIMARY , HL78XX_NETWORK_INFO_ACTIVE_BAND , HL78XX_NETWORK_INFO_SINR }
```

相关声明：[hl78xx_network_info_type](#ga563d651fff3621c1e21d7c47d19fd218)、[HL78XX_NETWORK_INFO_APN](#gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe)、[HL78XX_NETWORK_INFO_CURRENT_RAT](#gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA](#gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA](#gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC](#gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a)、[HL78XX_NETWORK_INFO_OPERATOR_FORMAT](#gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520)、[HL78XX_NETWORK_INFO_TAC](#gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f)、[HL78XX_NETWORK_INFO_MCC](#gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c)、[HL78XX_NETWORK_INFO_MNC](#gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb)、[HL78XX_NETWORK_INFO_CELL_ID](#gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650)、[HL78XX_NETWORK_INFO_IP_ADDRESS](#gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771)、[HL78XX_NETWORK_INFO_DNS_PRIMARY](#gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73)、[HL78XX_NETWORK_INFO_ACTIVE_BAND](#gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc)、[HL78XX_NETWORK_INFO_SINR](#gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48)。

缓存的网络信息类型（Cached Network Information Types）。

<a id="r_gabb0e5a4dd5c2e29d62ba27f6022f01f5"></a>

```c
enum nmea_output_port { NMEA_OUTPUT_NONE = 0x00 , NMEA_OUTPUT_USB_NMEA_PORT = 0x01 , NMEA_OUTPUT_UART1 = 0x03 , NMEA_OUTPUT_SAME_PORT = 0x04 , NMEA_OUTPUT_CMUX_DLC1 = 0x05 , NMEA_OUTPUT_CMUX_DLC2 = 0x06 , NMEA_OUTPUT_CMUX_DLC3 = 0x07 , NMEA_OUTPUT_CMUX_DLC4 = 0x08 }
```

相关声明：[nmea_output_port](#gabb0e5a4dd5c2e29d62ba27f6022f01f5)、[NMEA_OUTPUT_NONE](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9)、[NMEA_OUTPUT_USB_NMEA_PORT](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c)、[NMEA_OUTPUT_UART1](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589)、[NMEA_OUTPUT_SAME_PORT](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3)、[NMEA_OUTPUT_CMUX_DLC1](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf)、[NMEA_OUTPUT_CMUX_DLC2](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f)、[NMEA_OUTPUT_CMUX_DLC3](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d)、[NMEA_OUTPUT_CMUX_DLC4](#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1)。

NMEA 输出端口选项（Output Port Options）。

<a id="r_ga7d4975dffccffac27c9dccb85c02d549"></a>

```c
enum hl78xx_agnss_mode { HL78XX_AGNSS_MODE_INVALID = 0 , HL78XX_AGNSS_MODE_VALID = 1 }
```

相关声明：[hl78xx_agnss_mode](#ga7d4975dffccffac27c9dccb85c02d549)、[HL78XX_AGNSS_MODE_INVALID](#gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288)、[HL78XX_AGNSS_MODE_VALID](#gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d)。

辅助全球导航卫星系统（A-GNSS）辅助数据有效期模式（Assistance Data Validity Mode）。

<a id="r_gae9cf9c13242bc674dd7b0b79a69b8f31"></a>

```c
enum hl78xx_agnss_days { HL78XX_AGNSS_DAYS_1 = 1 , HL78XX_AGNSS_DAYS_2 = 2 , HL78XX_AGNSS_DAYS_3 = 3 , HL78XX_AGNSS_DAYS_7 = 7 , HL78XX_AGNSS_DAYS_14 = 14 , HL78XX_AGNSS_DAYS_28 = 28 }
```

相关声明：[hl78xx_agnss_days](#gae9cf9c13242bc674dd7b0b79a69b8f31)、[HL78XX_AGNSS_DAYS_1](#ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876)、[HL78XX_AGNSS_DAYS_2](#ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34)、[HL78XX_AGNSS_DAYS_3](#ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8)、[HL78XX_AGNSS_DAYS_7](#ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a)、[HL78XX_AGNSS_DAYS_14](#ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816)、[HL78XX_AGNSS_DAYS_28](#ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459)。

待下载的预测辅助数据（Predicted Assistance Data）天数，用于写命令；或距离其过期的天数，用于读命令。

<a id="r_ga6340324dcb76101c66b902bb9a14dbd3"></a>

```c
enum power_down_event { POWER_DOWN_EVENT_ENTER = 0 , POWER_DOWN_EVENT_EXIT , POWER_DOWN_EVENT_NONE }
```

相关声明：[power_down_event](#ga6340324dcb76101c66b902bb9a14dbd3)、[POWER_DOWN_EVENT_ENTER](#gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa)、[POWER_DOWN_EVENT_EXIT](#gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1)、[POWER_DOWN_EVENT_NONE](#gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b)。

掉电事件类型（Power Down Event Types）。

<a id="r_ga50bd06a27371c5c79de5bef125d6b5f3"></a>

```c
enum hl78xx_power_down_response { HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE = 0 , HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE , HL78XX_POWER_DOWN_RESPONSE_ABORT }
```

相关声明：[hl78xx_power_down_response](#ga50bd06a27371c5c79de5bef125d6b5f3)、[HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE](#gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a)、[HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE](#gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985)、[HL78XX_POWER_DOWN_RESPONSE_ABORT](#gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e)。

应用程序对待处理掉电请求（Pending Power-down Request）的响应。

<a id="r_ga5d8a5b00f354e98abc2effa560f3bac8"></a>

```c
enum hl78xx_edrx_event { HL78XX_EDRX_EVENT_IDLE_EXIT = 0 , HL78XX_EDRX_EVENT_IDLE_ENTER , HL78XX_EDRX_EVENT_IDLE_NONE }
```

相关声明：[hl78xx_edrx_event](#ga5d8a5b00f354e98abc2effa560f3bac8)、[HL78XX_EDRX_EVENT_IDLE_EXIT](#gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8)、[HL78XX_EDRX_EVENT_IDLE_ENTER](#gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5)、[HL78XX_EDRX_EVENT_IDLE_NONE](#gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a)。

扩展非连续接收（eDRX）事件类型。

<a id="r_gae891e3155a0ebf72433dd58ae4c36512"></a>

```c
enum hl78xx_psmev_event { HL78XX_PSM_EVENT_EXIT = 0 , HL78XX_PSM_EVENT_ENTER , HL78XX_PSM_EVENT_NONE }
```

相关声明：[hl78xx_psmev_event](#gae891e3155a0ebf72433dd58ae4c36512)、[HL78XX_PSM_EVENT_EXIT](#ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94)、[HL78XX_PSM_EVENT_ENTER](#ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda)、[HL78XX_PSM_EVENT_NONE](#ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553)。

省电模式（PSM）事件类型。

<a id="r_ga8a864475f6e9673f85ec7c56028992a5"></a>

```c
enum hl78xx_evt_type { HL78XX_LTE_RAT_UPDATE , HL78XX_LTE_REGISTRATION_STAT_UPDATE , HL78XX_LTE_SIM_REGISTRATION , HL78XX_LTE_MODEM_STARTUP , HL78XX_LTE_FOTA_UPDATE_STATUS , HL78XX_LTE_DNS_READY , HL78XX_LTE_AT_CMD_READY , HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE , HL78XX_LTE_CTZEU_UPDATE , HL78XX_GNSS_ENGINE_READY , HL78XX_GNSS_EVENT_INIT , HL78XX_GNSS_EVENT_START , HL78XX_GNSS_EVENT_STOP , HL78XX_GNSS_EVENT_POSITION , HL78XX_GNSS_EVENT_START_BLOCKED , HL78XX_GNSS_EVENT_SEARCH_TIMEOUT , HL78XX_GNSS_EVENT_MODE_EXITED , HL78XX_EDRX_IDLE_UPDATE , HL78XX_LTE_PSMEV_UPDATE , HL78XX_POWER_DOWN_UPDATE , HL78XX_VGPIO_LOW , HL78XX_VGPIO_HIGH , HL78XX_GPIO6_LOW , HL78XX_GPIO6_HIGH , HL78XX_CELLMEAS_UPDATE , HL78XX_EVT_TYPE_COUNT }
```

相关声明：[hl78xx_evt_type](#ga8a864475f6e9673f85ec7c56028992a5)、[HL78XX_LTE_RAT_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5)、[HL78XX_LTE_REGISTRATION_STAT_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95)、[HL78XX_LTE_SIM_REGISTRATION](#gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9)、[HL78XX_LTE_MODEM_STARTUP](#gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839)、[HL78XX_LTE_FOTA_UPDATE_STATUS](#gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92)、[HL78XX_LTE_DNS_READY](#gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8)、[HL78XX_LTE_AT_CMD_READY](#gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73)、[HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5)、[HL78XX_LTE_CTZEU_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6)、[HL78XX_GNSS_ENGINE_READY](#gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b)、[HL78XX_GNSS_EVENT_INIT](#gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae)、[HL78XX_GNSS_EVENT_START](#gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5)、[HL78XX_GNSS_EVENT_STOP](#gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61)、[HL78XX_GNSS_EVENT_POSITION](#gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c)、[HL78XX_GNSS_EVENT_START_BLOCKED](#gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07)、[HL78XX_GNSS_EVENT_SEARCH_TIMEOUT](#gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429)、[HL78XX_GNSS_EVENT_MODE_EXITED](#gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916)、[HL78XX_EDRX_IDLE_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3)、[HL78XX_LTE_PSMEV_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7)、[HL78XX_POWER_DOWN_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2)、[HL78XX_VGPIO_LOW](#gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc)、[HL78XX_VGPIO_HIGH](#gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63)、[HL78XX_GPIO6_LOW](#gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe)、[HL78XX_GPIO6_HIGH](#gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52)、[HL78XX_CELLMEAS_UPDATE](#gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254)、[HL78XX_EVT_TYPE_COUNT](#gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790)。

HL78xx 事件类型（Event Types）。

<a id="r_ga5453000edbd52c54f7193de4852aa9a8"></a>

```c
enum wdsi_indication { WDSI_BOOTSTRAP_CREDENTIALS_PRESENT = 0 , WDSI_USER_AGREEMENT_REQUEST = 1 , WDSI_FIRMWARE_DOWNLOAD_REQUEST = 2 , WDSI_FIRMWARE_INSTALL_REQUEST = 3 , WDSI_AUTHENTICATION_START = 4 , WDSI_AUTHENTICATION_FAILED = 5 , WDSI_AUTHENTICATION_SUCCESS = 6 , WDSI_CONNECTION_DENIED = 7 , WDSI_DM_SESSION_CLOSED = 8 , WDSI_FIRMWARE_AVAILABLE = 9 , WDSI_FIRMWARE_DOWNLOADED = 10 , WDSI_FIRMWARE_DOWNLOAD_ISSUE = 11 , WDSI_PACKAGE_VERIFIED_CERTIFIED = 12 , WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED = 13 , WDSI_FIRMWARE_UPDATE_START = 14 , WDSI_FIRMWARE_UPDATE_FAILED = 15 , WDSI_FIRMWARE_UPDATE_SUCCESS = 16 , WDSI_DOWNLOAD_IN_PROGRESS = 18 , WDSI_SESSION_STARTED = 23 }
```

相关声明：[wdsi_indication](#ga5453000edbd52c54f7193de4852aa9a8)、[WDSI_BOOTSTRAP_CREDENTIALS_PRESENT](#gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339)、[WDSI_USER_AGREEMENT_REQUEST](#gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2)、[WDSI_FIRMWARE_DOWNLOAD_REQUEST](#gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68)、[WDSI_FIRMWARE_INSTALL_REQUEST](#gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5)、[WDSI_AUTHENTICATION_START](#gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1)、[WDSI_AUTHENTICATION_FAILED](#gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6)、[WDSI_AUTHENTICATION_SUCCESS](#gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608)、[WDSI_CONNECTION_DENIED](#gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a)、[WDSI_DM_SESSION_CLOSED](#gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2)、[WDSI_FIRMWARE_AVAILABLE](#gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8)、[WDSI_FIRMWARE_DOWNLOADED](#gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd)、[WDSI_FIRMWARE_DOWNLOAD_ISSUE](#gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184)、[WDSI_PACKAGE_VERIFIED_CERTIFIED](#gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7)、[WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED](#gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5)、[WDSI_FIRMWARE_UPDATE_START](#gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458)、[WDSI_FIRMWARE_UPDATE_FAILED](#gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc)、[WDSI_FIRMWARE_UPDATE_SUCCESS](#gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f)、[WDSI_DOWNLOAD_IN_PROGRESS](#gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0)、[WDSI_SESSION_STARTED](#gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d)。

设备服务指示（Device Services Indications，`+WDSI`）。

<a id="r_ga95d1ccc5899adf1b2eda6aa0777b7e80"></a>

```c
enum hl78xx_gnss_event_type { HL78XX_GNSSEV_INITIALISATION = 0 , HL78XX_GNSSEV_START = 1 , HL78XX_GNSSEV_STOP = 2 , HL78XX_GNSSEV_POSITION = 3 }
```

相关声明：[hl78xx_gnss_event_type](#ga95d1ccc5899adf1b2eda6aa0777b7e80)、[HL78XX_GNSSEV_INITIALISATION](#gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21)、[HL78XX_GNSSEV_START](#gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740)、[HL78XX_GNSSEV_STOP](#gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da)、[HL78XX_GNSSEV_POSITION](#gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533)。

全球导航卫星系统（GNSS）事件类型。

<a id="r_ga9b9da1841754d723cddc103800b141ae"></a>

```c
enum hl78xx_event_status { HL78XX_STATUS_FAILED = 0 , HL78XX_STATUS_SUCCESS = 1 }
```

相关声明：[hl78xx_event_status](#ga9b9da1841754d723cddc103800b141ae)、[HL78XX_STATUS_FAILED](#gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e)、[HL78XX_STATUS_SUCCESS](#gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd)。

GNSS 事件状态。

<a id="r_ga2a471bc1b92dba1e316b2b27e3778e1a"></a>

```c
enum gnss_position_events { GNSS_FIX_LOST_OR_UNAVAILABLE = 0 , GNSS_ESTIMATED_POSITION_AVAILABLE = 1 , GNSS_2D_POSITION_AVAILABLE = 2 , GNSS_3D_POSITION_AVAILABLE = 3 , GNSS_FIX_CHANGED_TO_INVALID = 4 }
```

相关声明：[gnss_position_events](#ga2a471bc1b92dba1e316b2b27e3778e1a)、[GNSS_FIX_LOST_OR_UNAVAILABLE](#gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d)、[GNSS_ESTIMATED_POSITION_AVAILABLE](#gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306)、[GNSS_2D_POSITION_AVAILABLE](#gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8)、[GNSS_3D_POSITION_AVAILABLE](#gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407)、[GNSS_FIX_CHANGED_TO_INVALID](#gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa)。

全球导航卫星系统（GNSS）位置事件（Position Events），`eventType = 3`。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.6\_函数（Functions）

<a id="r_gaab36b1992acffc8b25b8140da1a79577"></a>

```c
int hl78xx_api_func_set_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_api_func_set_phone_functionality](#gaab36b1992acffc8b25b8140da1a79577)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置电话功能模式（Phone Functionality Mode），内部实现。

<a id="r_gad39b680650d8a3f1ea20bc18fa6101d4"></a>

```c
int hl78xx_api_func_restart (const struct device *dev, enum hl78xx_modem_restart_mode mode)
```

相关声明：[hl78xx_api_func_restart](#gad39b680650d8a3f1ea20bc18fa6101d4)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_restart_mode](#ga618c248d23a1db1b027333c92adf99a1)。

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

<a id="r_gaca72419e4396a45b296a65f89877dbb8"></a>

```c
int hl78xx_api_func_get_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_api_func_get_phone_functionality](#gaca72419e4396a45b296a65f89877dbb8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)。

获取电话功能模式（Phone Functionality Mode），内部实现。

<a id="r_gae50586b4f939abacda6739850c118982"></a>

```c
int hl78xx_api_func_get_signal (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[hl78xx_api_func_get_signal](#gae50586b4f939abacda6739850c118982)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取网络信号强度（Network Signal Strength），内部实现。

<a id="r_ga5f9c8c8087e1e6008f290ddfe42e3d97"></a>

```c
int hl78xx_api_func_get_modem_info (const struct device *dev, enum hl78xx_modem_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_api_func_get_modem_info](#ga5f9c8c8087e1e6008f290ddfe42e3d97)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_info_type](#gaadcca229cbccc9832734bcc4e2a443e6)。

获取厂商专用的调制解调器信息（Vendor-specific Modem Information），内部实现。

<a id="r_gacddf878e52d0642279e147add9c8bdad"></a>

```c
int hl78xx_api_func_get_modem_info_standard (const struct device *dev, enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[hl78xx_api_func_get_modem_info_standard](#gacddf878e52d0642279e147add9c8bdad)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)。

从缓存获取标准调制解调器信息（Modem Information），采用 Zephyr 蜂窝 API（Cellular API）。

<a id="r_gac08824e4662cb5fcb316e6a0e1e5ba17"></a>

```c
int hl78xx_api_func_get_network_info (const struct device *dev, enum hl78xx_network_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_api_func_get_network_info](#gac08824e4662cb5fcb316e6a0e1e5ba17)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network_info_type](#ga563d651fff3621c1e21d7c47d19fd218)。

获取缓存的厂商专用网络信息（Vendor-specific Network Information）。

<a id="r_gadd718f794b24c9610e97f7460519e577"></a>

```c
int hl78xx_api_func_get_rsrp_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_rsrp_validity](#gadd718f794b24c9610e97f7460519e577)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收功率（RSRP）是否达到配置的最低阈值。

<a id="r_ga79c8b3e0581e6418526b3aa86e6bbb5a"></a>

```c
int hl78xx_api_func_get_rsrq_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_rsrq_validity](#ga79c8b3e0581e6418526b3aa86e6bbb5a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收质量（RSRQ）是否达到配置的最低阈值。

<a id="r_ga069a0709408fef75514dfaf12bc42cb5"></a>

```c
int hl78xx_api_func_get_sinr_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_sinr_validity](#ga069a0709408fef75514dfaf12bc42cb5)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前信号与干扰加噪声比（SINR）是否达到配置的最低阈值。

<a id="r_gab8e5ae21bd129d61735c9cfe3df557d2"></a>

```c
int hl78xx_api_func_set_network_operator_format (const struct device *dev, enum hl78xx_operator_format format)
```

相关声明：[hl78xx_api_func_set_network_operator_format](#gab8e5ae21bd129d61735c9cfe3df557d2)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_operator_format](#ga2d26ae6044baac5995f4184abe4faad3)。

设置 `+COPS` 网络运营商格式（Network Operator Format）。

<a id="r_gafc8c324c2beb2c59c9f15542d06b85ee"></a>

```c
int hl78xx_api_func_set_prl (const struct device *dev, const struct kselacq_syntax kselacq_rats)
```

相关声明：[hl78xx_api_func_set_prl](#gafc8c324c2beb2c59c9f15542d06b85ee)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

通过 `AT+KSELACQ` 设置新的首选无线接入技术列表（Preferred RAT List）。

<a id="r_ga4c2dc7d53dd4780d8f1e00e9889248d3"></a>

```c
int hl78xx_api_func_get_prl (const struct device *dev, struct kselacq_syntax *kselacq_rats)
```

相关声明：[hl78xx_api_func_get_prl](#ga4c2dc7d53dd4780d8f1e00e9889248d3)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

获取当前首选无线接入技术列表（Preferred RAT List）。

<a id="r_ga1640ce244f1a4de52efa0b7c33f7b02a"></a>

```c
int hl78xx_api_func_set_autorat_inhibit (const struct device *dev, bool inhibit)
```

相关声明：[hl78xx_api_func_set_autorat_inhibit](#ga1640ce244f1a4de52efa0b7c33f7b02a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

禁止启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

<a id="r_ga6adcbc5395d078be2fc9c6e62612f603"></a>

```c
bool hl78xx_api_func_at_is_busy (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_api_func_at_is_busy](#ga6adcbc5395d078be2fc9c6e62612f603)、[device](../device_reference/P002_设备对象结构.md)。

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

<a id="r_gac6ed6d4f41003cb2517f802762d5b239"></a>

```c
int hl78xx_set_runtime_band_provider (const struct device *dev, hl78xx_runtime_band_provider_t provider, void *user_data)
```

相关声明：[hl78xx_set_runtime_band_provider](#gac6ed6d4f41003cb2517f802762d5b239)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_runtime_band_provider_t](#ga82793d1f4c0c8f03ae27b29afa1c3d3f)。

为驱动注册或清除运行时频段提供器（Runtime Band Provider）。

<a id="r_gae3f2ed904a3b0784d64d2d1537ce9564"></a>

```c
int hl78xx_api_func_modem_dynamic_cmd_send (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_api_func_modem_dynamic_cmd_send](#gae3f2ed904a3b0784d64d2d1537ce9564)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送动态 AT 命令（Dynamic AT Command），内部实现。

<a id="r_ga45a97bfc5f73d1877357dc1f410c61cd"></a>

```c
int hl78xx_modem_at_send (const struct device *dev, const char *cmd)
```

相关声明：[hl78xx_modem_at_send](#ga45a97bfc5f73d1877357dc1f410c61cd)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

向调制解调器（Modem）发送预先格式化的 AT 命令。

<a id="r_ga3e9edd942cbf32b5a2eec259c44e5ee4"></a>

```c
int hl78xx_modem_at_cmd (const struct device *dev, char *response, size_t response_size, const char *cmd)
```

相关声明：[hl78xx_modem_at_cmd](#ga3e9edd942cbf32b5a2eec259c44e5ee4)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

发送预先格式化的 AT 命令，并将完整的调制解调器响应（Modem Response）复制到调用者提供的缓冲区。

<a id="r_gabe520e9e9a5e48ab05e238f6b59b8cda"></a>

```c
static int hl78xx_get_modem_info (const struct device *dev, const enum hl78xx_modem_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_get_modem_info](#gabe520e9e9a5e48ab05e238f6b59b8cda)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_info_type](#gaadcca229cbccc9832734bcc4e2a443e6)。

获取设备调制解调器信息（Modem Info）。

<a id="r_gaedfc9112048d6c987ee7fefa4e8abd55"></a>

```c
static int hl78xx_get_network_info (const struct device *dev, enum hl78xx_network_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_get_network_info](#gaedfc9112048d6c987ee7fefa4e8abd55)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network_info_type](#ga563d651fff3621c1e21d7c47d19fd218)。

获取设备缓存的网络信息（Cached Network Info）。

<a id="r_ga65f087ad92a0f2bfb15d4f7b627c754f"></a>

```c
static int hl78xx_get_rsrp_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_rsrp_validity](#ga65f087ad92a0f2bfb15d4f7b627c754f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收功率（RSRP）是否达到配置的阈值。

<a id="r_gab49ab6eb5aa0cfcdea4e6e7bcabd1d48"></a>

```c
static int hl78xx_get_rsrq_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_rsrq_validity](#gab49ab6eb5aa0cfcdea4e6e7bcabd1d48)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收质量（RSRQ）是否达到配置的阈值。

<a id="r_ga06800817986b9a4b0291cc22c808dfae"></a>

```c
static int hl78xx_get_sinr_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_sinr_validity](#ga06800817986b9a4b0291cc22c808dfae)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前信号与干扰加噪声比（SINR）是否达到配置的阈值。

<a id="r_gad564df9a12ad4ee40caeffec1099a93b"></a>

```c
static int hl78xx_set_prl (const struct device *dev, struct kselacq_syntax prl)
```

相关声明：[hl78xx_set_prl](#gad564df9a12ad4ee40caeffec1099a93b)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

设置新的原始 `AT+KSELACQ` 首选无线接入技术列表（Preferred RAT List）。

<a id="r_gaad6374b5c5ef64886c6d8fdde0cba3c4"></a>

```c
static int hl78xx_set_autorat_inhibit (const struct device *dev, bool inhibit)
```

相关声明：[hl78xx_set_autorat_inhibit](#gaad6374b5c5ef64886c6d8fdde0cba3c4)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

禁止或允许启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

<a id="r_gad2673b87d730da42b4d2109e849277cc"></a>

```c
static bool hl78xx_at_is_busy (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_at_is_busy](#gad2673b87d730da42b4d2109e849277cc)、[device](../device_reference/P002_设备对象结构.md)。

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

<a id="r_gaee99182459b5971ebaa7892989b0e8df"></a>

```c
static int hl78xx_set_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_set_phone_functionality](#gaee99182459b5971ebaa7892989b0e8df)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器的电话功能模式（Phone Functionality Mode）。

<a id="r_ga2c4ff4a9b1d5d2530700327e1d4af6e0"></a>

```c
static int hl78xx_restart_modem (const struct device *dev, enum hl78xx_modem_restart_mode mode)
```

相关声明：[hl78xx_restart_modem](#ga2c4ff4a9b1d5d2530700327e1d4af6e0)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_restart_mode](#ga618c248d23a1db1b027333c92adf99a1)。

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

<a id="r_gaf778d092ad7f9b67b0930c0da2375996"></a>

```c
static int hl78xx_get_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_get_phone_functionality](#gaf778d092ad7f9b67b0930c0da2375996)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](#ga39a3de13bd706571cd7348ea46b7b708)。

获取调制解调器当前的电话功能模式（Phone Functionality Mode）。

<a id="r_gae7102c14fda882e87bff0f0828ab4263"></a>

```c
static int hl78xx_modem_cmd_send (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_modem_cmd_send](#gae7102c14fda882e87bff0f0828ab4263)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向调制解调器（Modem）发送 AT 命令，并等待匹配的响应（Matched Response）。

<a id="r_gaba7b5c599c1b9285b9dcfbae91ac5e7f"></a>

```c
static int hl78xx_modem_at_err_type (int error)
```

相关声明：[hl78xx_modem_at_err_type](#gaba7b5c599c1b9285b9dcfbae91ac5e7f)。

返回编码在 `hl78xx_modem_at_send`／`cmd` 返回值中的调制解调器错误类型（Modem Error Type）。

<a id="r_ga13ead2b7a66530a1fbe15e5c4d9addeb"></a>

```c
static int hl78xx_modem_at_err (int error)
```

相关声明：[hl78xx_modem_at_err](#ga13ead2b7a66530a1fbe15e5c4d9addeb)。

返回编码在 `hl78xx_modem_at_send`／`cmd` 中的调制解调器 CME／CMS 错误码（Error Code）。

<a id="r_ga9dd8be5c6d35de4122ab5604bf5b17ce"></a>

```c
static int hl78xx_parse_rssi (uint8_t rssi, int16_t *value)
```

相关声明：[hl78xx_parse_rssi](#ga9dd8be5c6d35de4122ab5604bf5b17ce)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始接收信号强度指示（RSSI）值转换为 dBm。

<a id="r_ga8abfb51de22c24f1870d2b5f4b3b60ee"></a>

```c
static int hl78xx_parse_rsrp (uint8_t rsrp, int16_t *value)
```

相关声明：[hl78xx_parse_rsrp](#ga8abfb51de22c24f1870d2b5f4b3b60ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始参考信号接收功率（RSRP）值转换为 dBm。

<a id="r_ga09f7b39a934d38a2d3da8deefc3d2758"></a>

```c
static int hl78xx_parse_rsrq (uint8_t rsrq, int16_t *value)
```

相关声明：[hl78xx_parse_rsrq](#ga09f7b39a934d38a2d3da8deefc3d2758)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始参考信号接收质量（RSRQ）值转换为 dB。

<a id="r_gadfb6a494068c978908ed0bd968b81a5f"></a>

```c
static void hl78xx_evt_monitor_pause (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_pause](#gadfb6a494068c978908ed0bd968b81a5f)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

暂停监视器（Monitor）。

<a id="r_gab3a63acd15fc9bd6a7d9ded9ed1731fa"></a>

```c
static void hl78xx_evt_monitor_resume (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_resume](#gab3a63acd15fc9bd6a7d9ded9ed1731fa)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

恢复监视器（Monitor）。

<a id="r_gab08189be0b4dc7f03428d829f0170bbe"></a>

```c
static void hl78xx_at_monitor_pause (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_pause](#gab08189be0b4dc7f03428d829f0170bbe)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

暂停 AT 监视器（AT Monitor）。

<a id="r_ga2723fa7f912913d299629fdba4efb130"></a>

```c
static void hl78xx_at_monitor_resume (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_resume](#ga2723fa7f912913d299629fdba4efb130)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

恢复 AT 监视器（AT Monitor）。

<a id="r_ga051a63a86e9ca353434b23e1adf5d543"></a>

```c
int hl78xx_at_monitor_register (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_register](#ga051a63a86e9ca353434b23e1adf5d543)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

注册 AT 监视器（AT Monitor）。

<a id="r_ga1244a8f6b7e5e488ab596aa5341ad66a"></a>

```c
int hl78xx_at_monitor_unregister (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_unregister](#ga1244a8f6b7e5e488ab596aa5341ad66a)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

注销 AT 监视器（AT Monitor）。

<a id="r_ga8265e020ad0d8c3e69f2219173530720"></a>

```c
int hl78xx_evt_notif_handler_set (hl78xx_evt_monitor_dispatcher_t handler)
```

相关声明：[hl78xx_evt_notif_handler_set](#ga8265e020ad0d8c3e69f2219173530720)、[hl78xx_evt_monitor_dispatcher_t](#gade4999c5b603813020cd52a93687b76f)。

设置 HL78xx 调制解调器事件（Modem Events）的事件通知处理函数（Event Notification Handler）。

<a id="r_ga6590e5352cbd8ff6ea0580edd64eb0d0"></a>

```c
int hl78xx_evt_monitor_register (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_register](#ga6590e5352cbd8ff6ea0580edd64eb0d0)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

注册事件监视器（Event Monitor）。

<a id="r_gaf4c623e7bed92b6ea3964b59df04e98e"></a>

```c
int hl78xx_evt_monitor_unregister (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_unregister](#gaf4c623e7bed92b6ea3964b59df04e98e)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

注销事件监视器（Event Monitor）。

<a id="r_gaf8cbf3de84df41d7066b9a07f106c17b"></a>

```c
enum cellular_access_technology hl78xx_rat_to_access_tech (enum hl78xx_cell_rat_mode rat_mode)
```

相关声明：[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)、[hl78xx_rat_to_access_tech](#gaf8cbf3de84df41d7066b9a07f106c17b)、[hl78xx_cell_rat_mode](#ga298f953be96ab47be40b5440a2573182)。

将 HL78xx 无线接入技术模式（RAT Mode）转换为标准蜂窝 API（Cellular API）表示。

<a id="r_gac9f87f986b0b745bf8e370896113066f"></a>

```c
enum hl78xx_cell_rat_mode hl78xx_access_tech_to_rat (enum cellular_access_technology access_tech)
```

相关声明：[hl78xx_cell_rat_mode](#ga298f953be96ab47be40b5440a2573182)、[hl78xx_access_tech_to_rat](#gac9f87f986b0b745bf8e370896113066f)、[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)。

将标准蜂窝接入技术（Cellular Access Technology）转换为 HL78xx 无线接入技术模式（RAT Mode）。

<a id="r_gaf34ed3d29904f1a18c0c75a0de4bc727"></a>

```c
int hl78xx_start_airvantage_dm_session (const struct device *dev)
```

相关声明：[hl78xx_start_airvantage_dm_session](#gaf34ed3d29904f1a18c0c75a0de4bc727)、[device](../device_reference/P002_设备对象结构.md)。

启动 AirVantage 设备管理（Device Management，DM）会话。

<a id="r_ga9018c8332803eaada4083390c40ac3f0"></a>

```c
int hl78xx_stop_airvantage_dm_session (const struct device *dev)
```

相关声明：[hl78xx_stop_airvantage_dm_session](#ga9018c8332803eaada4083390c40ac3f0)、[device](../device_reference/P002_设备对象结构.md)。

停止 AirVantage 设备管理（Device Management，DM）会话。

<a id="r_ga803bf7a13a7b57477dbfa4d6b3faa14e"></a>

```c
int hl78xx_set_wake_pin_low (const struct device *dev)
```

相关声明：[hl78xx_set_wake_pin_low](#ga803bf7a13a7b57477dbfa4d6b3faa14e)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器的 `WAKE` 引脚驱动为低电平（Low）。

<a id="r_gae3e97cdf80470496d6d8542f61f985c0"></a>

```c
int hl78xx_set_wake_pin_high (const struct device *dev)
```

相关声明：[hl78xx_set_wake_pin_high](#gae3e97cdf80470496d6d8542f61f985c0)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器的 `WAKE` 引脚驱动为高电平（High）。

<a id="r_ga9bac621e2f74d598329f61cd95b0291b"></a>

```c
int hl78xx_set_active_sim (const struct device *dev, enum hl78xx_sim_slot sim_slot)
```

相关声明：[hl78xx_set_active_sim](#ga9bac621e2f74d598329f61cd95b0291b)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_sim_slot](#ga0b3efb75d166d9d4bf163ffc6bb68fc0)。

选择活动的外部 SIM 卡槽（Active External SIM Slot）。

<a id="r_ga7cc4861b1449b551246204b84779c621"></a>

```c
int hl78xx_wakeup_modem (const struct device *dev)
```

相关声明：[hl78xx_wakeup_modem](#ga7cc4861b1449b551246204b84779c621)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器从省电模式（PSM）睡眠中唤醒。

<a id="r_ga41d66fc0e8681bf6a68f47af5bcacb90"></a>

```c
int hl78xx_edrx_get_time_to_sleep (const struct device *dev)
```

相关声明：[hl78xx_edrx_get_time_to_sleep](#ga41d66fc0e8681bf6a68f47af5bcacb90)、[device](../device_reference/P002_设备对象结构.md)。

获取调制解调器进入扩展非连续接收空闲状态（eDRX Idle State）前的剩余时间。

<a id="r_ga9e9d288506708b275cc98e508bc8251d"></a>

```c
int hl78xx_enter_gnss_mode (const struct device *dev)
```

相关声明：[hl78xx_enter_gnss_mode](#ga9e9d288506708b275cc98e508bc8251d)、[device](../device_reference/P002_设备对象结构.md)。

进入全球导航卫星系统（GNSS）模式。

<a id="r_ga475545d83cf5fd883fd11fb0db8400ed"></a>

```c
int hl78xx_exit_gnss_mode (const struct device *dev)
```

相关声明：[hl78xx_exit_gnss_mode](#ga475545d83cf5fd883fd11fb0db8400ed)、[device](../device_reference/P002_设备对象结构.md)。

退出全球导航卫星系统（GNSS）模式，返回长期演进（LTE）模式。

<a id="r_ga48f504b9bb41d4a13ac592f763aeb207"></a>

```c
int hl78xx_queue_gnss_search (const struct device *dev)
```

相关声明：[hl78xx_queue_gnss_search](#ga48f504b9bb41d4a13ac592f763aeb207)、[device](../device_reference/P002_设备对象结构.md)。

将 GNSS 位置搜索（Position Search）加入队列。

<a id="r_ga5a1949cd23380056b4ee1775b1e6cc3b"></a>

```c
int hl78xx_gnss_set_nmea_output (const struct device *dev, enum nmea_output_port port)
```

相关声明：[hl78xx_gnss_set_nmea_output](#ga5a1949cd23380056b4ee1775b1e6cc3b)、[device](../device_reference/P002_设备对象结构.md)、[nmea_output_port](#gabb0e5a4dd5c2e29d62ba27f6022f01f5)。

设置 GNSS 的 NMEA 输出端口（Output Port）。

<a id="r_gae349d6b96ef9ae67b5ed01d0a8fa2cb0"></a>

```c
int hl78xx_gnss_set_search_timeout (const struct device *dev, uint32_t timeout_ms)
```

相关声明：[hl78xx_gnss_set_search_timeout](#gae349d6b96ef9ae67b5ed01d0a8fa2cb0)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 GNSS 搜索超时（Search Timeout）。

<a id="r_ga209d0579899aef4ade5cf8de1251a323"></a>

```c
int hl78xx_gnss_get_search_timeout_remaining (const struct device *dev, uint32_t *timeout_ms)
```

相关声明：[hl78xx_gnss_get_search_timeout_remaining](#ga209d0579899aef4ade5cf8de1251a323)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取剩余的 GNSS 搜索超时（Search Timeout）。

<a id="r_ga0238b9a2de4683369a0be7a6ed481938"></a>

```c
int hl78xx_gnss_get_latest_known_fix (const struct device *dev)
```

相关声明：[hl78xx_gnss_get_latest_known_fix](#ga0238b9a2de4683369a0be7a6ed481938)、[device](../device_reference/P002_设备对象结构.md)。

从调制解调器获取最新已知的 GNSS 定位结果（Fix）。

<a id="r_ga473c72484a8a758470ff7043de7ab48d"></a>

```c
int hl78xx_gnss_assist_data_get_status (const struct device *dev, struct hl78xx_agnss_status *status)
```

相关声明：[hl78xx_gnss_assist_data_get_status](#ga473c72484a8a758470ff7043de7ab48d)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_agnss_status](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md)。

获取辅助全球导航卫星系统（A-GNSS）的辅助数据状态（Assistance Data Status）。

<a id="r_gabf8fcaa1b5a59d5a2cac3c467f93c9f8"></a>

```c
int hl78xx_gnss_assist_data_download (const struct device *dev, enum hl78xx_agnss_days days)
```

相关声明：[hl78xx_gnss_assist_data_download](#gabf8fcaa1b5a59d5a2cac3c467f93c9f8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_agnss_days](#gae9cf9c13242bc674dd7b0b79a69b8f31)。

下载辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

<a id="r_ga452b1ee210417569b3cdfc30db25622a"></a>

```c
int hl78xx_gnss_assist_data_delete (const struct device *dev)
```

相关声明：[hl78xx_gnss_assist_data_delete](#ga452b1ee210417569b3cdfc30db25622a)、[device](../device_reference/P002_设备对象结构.md)。

删除辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

<a id="r_gac7291340f8699bb37cd864516615ea05"></a>

```c
int hl78xx_power_down_trigger (const struct device *dev, k_timeout_t delay)
```

相关声明：[hl78xx_power_down_trigger](#gac7291340f8699bb37cd864516615ea05)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

经过调用者提供的延迟后，触发 HL78xx 关机流程（Shutdown Process）。

<a id="r_ga98af31968e3bf0fc72dea5d56e97e122"></a>

```c
int hl78xx_power_down_cancel (const struct device *dev)
```

相关声明：[hl78xx_power_down_cancel](#ga98af31968e3bf0fc72dea5d56e97e122)、[device](../device_reference/P002_设备对象结构.md)。

取消待处理的 HL78xx 第一阶段关机定时器（Stage-1 Shutdown Timer）。

<a id="r_ga249a5bf6cdbd69ec930724bf2541de72"></a>

```c
int hl78xx_power_down_respond (const struct device *dev, enum hl78xx_power_down_response response, uint32_t timeout_s)
```

相关声明：[hl78xx_power_down_respond](#ga249a5bf6cdbd69ec930724bf2541de72)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_power_down_response](#ga50bd06a27371c5c79de5bef125d6b5f3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

响应待处理的 HL78XX 掉电更新（Power-down Update）。

<a id="r_ga2bcaada6a58dfbe3658fc6bcb3090fff"></a>

```c
void hl78xx_power_down_confirm (const struct device *dev)
```

相关声明：[hl78xx_power_down_confirm](#ga2bcaada6a58dfbe3658fc6bcb3090fff)、[device](../device_reference/P002_设备对象结构.md)。

确认应用程序清理（Application Cleanup）已完成，调制解调器可以继续执行物理关机（Physical Shutdown）。

## 1.7\_详细说明（Detailed Documentation）

<a id="ga3a6d3cd70078e6046471ec528a09cd19"></a>

### `ACTIVE`

```c
#define ACTIVE 0
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

监视器（Monitor）处于活动状态，默认值。

<a id="gacb02197961c70e98147ae25e4c11d4de"></a>

### `CESQ_RSRP_MAX`

```c
#define CESQ_RSRP_MAX (97)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CESQ` 命令返回的最大有效参考信号接收功率（RSRP）编码。

<a id="ga309cc2c1be1d4006e2ccb8d59cb3e916"></a>

### `CESQ_RSRP_TO_DB`

```c
#define CESQ_RSRP_TO_DB ( v)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
(-141 + (v))
```

将 CESQ 参考信号接收功率（RSRP）值转换为 dBm。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 参考信号接收功率（RSRP）值，范围 0–97。 |

**返回（Returns）**：返回值：以 dBm 表示的保守下界代表值，范围 -141 至 -44。

<a id="ga03c48d45ba1dfcdeabba881f2b1cd936"></a>

### `CESQ_RSRP_UNKNOWN`

```c
#define CESQ_RSRP_UNKNOWN (255)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CESQ` 命令返回的未知参考信号接收功率（RSRP）值。

<a id="ga7d02276973c71eded42d4242a34ca745"></a>

### `CESQ_RSRQ_MAX`

```c
#define CESQ_RSRQ_MAX (34)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CESQ` 命令返回的最大有效参考信号接收质量（RSRQ）编码。

<a id="ga536c21c42099fc04ac85a634ffa41d24"></a>

### `CESQ_RSRQ_TO_DB`

```c
#define CESQ_RSRQ_TO_DB ( v)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
(((v) == 0U) ? -21 : (-20 + ((v) / 2)))
```

将 CESQ 参考信号接收质量（RSRQ）值转换为 dB。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 参考信号接收质量（RSRQ）值，范围 0–34。 |

**返回（Returns）**：返回值：以 dB 表示的保守整数代表值，范围 -21 至 -3。

<a id="ga9a4429e44439c5ebdd18ccd549f832f5"></a>

### `CESQ_RSRQ_UNKNOWN`

```c
#define CESQ_RSRQ_UNKNOWN (255)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CESQ` 命令返回的未知参考信号接收质量（RSRQ）值。

<a id="gab2c8054a088aa6927aa10f1aed1587ae"></a>

### `CSQ_RSSI_MAX`

```c
#define CSQ_RSSI_MAX (31)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CSQ` 命令返回的最大有效接收信号强度指示（RSSI）编码。

<a id="ga72dfe852d4d6365d80f33b918f631501"></a>

### `CSQ_RSSI_TO_DB`

```c
#define CSQ_RSSI_TO_DB ( v)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
(-113 + (2 * (v)))
```

将 CSQ 接收信号强度指示（RSSI）值转换为 dBm。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 接收信号强度指示（RSSI）值，范围 0–31。 |

**返回（Returns）**：返回值：以 dBm 表示的信号强度，范围 -113 至 -51。

<a id="ga8c28a5a32edb83ea0b0120dd3b00451f"></a>

### `CSQ_RSSI_UNKNOWN`

```c
#define CSQ_RSSI_UNKNOWN (99)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

`AT+CSQ` 命令返回的未知接收信号强度指示（RSSI）值。

<a id="ga7da0c70a3435693c416c28a27b4ab1c5"></a>

### `GNSS_AUX_DATA_CALLBACK_DEFINE`

```c
#define GNSS_AUX_DATA_CALLBACK_DEFINE ( _dev, _callback )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(hl78xx_gnss_aux_data_callback,                        \
                                     _hl78xx_gnss_aux_data_callback__##_callback) = {      \
        .dev = _dev,                                                                       \
        .callback = _callback,                                                             \
}
```

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 设备指针（Device Pointer）。 |
| `_callback` | 回调函数。 |

<a id="gab77a5c59a2b5297b7bc69afffb21dc73"></a>

### `GNSS_DT_AUX_DATA_CALLBACK_DEFINE`

```c
#define GNSS_DT_AUX_DATA_CALLBACK_DEFINE ( _node_id, _callback )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(hl78xx_gnss_aux_data_callback,                        \
                                     _CONCAT_4(_hl78xx_gnss_aux_data_callback_,            \
                                               DT_DEP_ORD(_node_id), _, _callback)) = {    \
        .dev = DEVICE_DT_GET(_node_id),                                                    \
        .callback = _callback,                                                             \
}
```

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_node_id` | 设备树（Devicetree）节点标识符。 |
| `_callback` | 回调函数。 |

<a id="gadc4cc789837650b5e20e9bf5f6d85067"></a>

### `HL78XX_AT_MONITOR`

```c
#define HL78XX_AT_MONITOR ( name, _filter, _handler, ... )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
static STRUCT_SECTION_ITERABLE(hl78xx_at_monitor_entry, name) = {                          \
        .filter = _filter,                                                                 \
        .handler = _handler,                                                               \
        .next = NULL,                                                                      \
        .flags = {                                                                         \
                .direct = false,                                                           \
                .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
        }}
```

定义 AT 监视器（AT Monitor），在系统工作队列线程（System Workqueue Thread）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 监视器（Monitor）名称。 |
| `_filter` | 要接收的主动上报 AT 通知的精确匹配模式；指定 `HL78XX_AT_MONITOR_ANY` 可接收所有已解析的通知。 |
| `_handler` | 监视器回调（Monitor Callback）。 |
| `...` | 可选的监视器初始状态，取值为 `HL78XX_MONITOR_ACTIVE` 或 `HL78XX_MONITOR_PAUSED`。默认初始状态为活动。 |

<a id="ga48b0f02ea31d612d867db6bf2a62fb46"></a>

### `HL78XX_AT_MONITOR_ANY`

```c
#define HL78XX_AT_MONITOR_ANY NULL
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

监视任何已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="ga370b450dc0ab247343d3406e7fc664da"></a>

### `HL78XX_AT_MONITOR_DIRECT`

```c
#define HL78XX_AT_MONITOR_DIRECT ( name, _filter, _handler, ... )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
static STRUCT_SECTION_ITERABLE(hl78xx_at_monitor_entry, name) = {                          \
        .filter = _filter,                                                                 \
        .handler = _handler,                                                               \
        .next = NULL,                                                                      \
        .flags = {                                                                         \
                .direct = true,                                                            \
                .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
        }}
```

定义 AT 监视器（AT Monitor），直接在 HL78xx 调制解调器接收工作队列上下文（RX Workqueue Context）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

直接监视器回调在 HL78xx 调制解调器的接收工作队列（RX Workqueue）上下文中运行。处理函数应尽量简短，必须避免执行可能长时间阻塞调制解调器接收处理的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 监视器（Monitor）名称。 |
| `_filter` | 要接收的主动上报 AT 通知的精确匹配模式；指定 `HL78XX_AT_MONITOR_ANY` 可接收所有已解析的通知。 |
| `_handler` | 监视器回调（Monitor Callback）。 |
| `...` | 可选的监视器初始状态，取值为 `HL78XX_MONITOR_ACTIVE` 或 `HL78XX_MONITOR_PAUSED`。默认初始状态为活动。 |

<a id="ga0d3e4dcb509b56886297f2f451f4d952"></a>

### `HL78XX_CEREG_TIMER_STR_LEN`

```c
#define HL78XX_CEREG_TIMER_STR_LEN 9
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

CEREG 定时器字符串（Timer String）的最大长度。

<a id="gaea97e8a895c9bad91eead2e631934bda"></a>

### `HL78XX_CTZEU_UTIME_MAX_LEN`

```c
#define HL78XX_CTZEU_UTIME_MAX_LEN 32
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于提取出的 `+CTZEU` 通用时间字符串（Universal Time Strings）的推荐缓冲区大小。

<a id="gaa23bb8ced0d5b912309228525736234a"></a>

### `HL78XX_EVT_MONITOR`

```c
#define HL78XX_EVT_MONITOR ( name, _handler, ... )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
static STRUCT_SECTION_ITERABLE(hl78xx_evt_monitor_entry, name) = {                         \
        .handler = _handler,                                                               \
        .next = NULL,                                                                      \
        .flags = {                                                                         \
                .direct = false,                                                           \
                .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
        }}
```

定义事件监视器（Event Monitor），在系统工作队列线程（System Workqueue Thread）中接收通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 监视器（Monitor）名称。 |
| `_handler` | 监视器回调（Monitor Callback）。 |
| `...` | 可选的监视器初始状态，取值为 `HL78XX_MONITOR_ACTIVE` 或 `HL78XX_MONITOR_PAUSED`。默认初始状态为活动。 |

<a id="ga23bb6b58819d70eb379f89a3878c07d0"></a>

### `HL78XX_MODEM_AT_CME_ERROR`

```c
#define HL78XX_MODEM_AT_CME_ERROR 2
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

公共 AT 辅助函数返回 `+CME ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="ga0fef7f6b540d959bf391ac39d8c2738a"></a>

### `HL78XX_MODEM_AT_CMS_ERROR`

```c
#define HL78XX_MODEM_AT_CMS_ERROR 3
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

公共 AT 辅助函数返回 `+CMS ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="gac53a8b20d353944744e259f1f9008d44"></a>

### `HL78XX_MODEM_AT_ERROR`

```c
#define HL78XX_MODEM_AT_ERROR 1
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

公共 AT 辅助函数返回通用 `ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="ga0381c6c5a47121b422c0f5d456e86432"></a>

### `HL78XX_MONITOR_ACTIVE`

```c
#define HL78XX_MONITOR_ACTIVE false
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

HL78xx 监视器（Monitor）的初始活动状态（Active State）。

定义初始状态应为活动的监视器时，可将此值用作可选的 `state` 参数。

<a id="gabe2427817d9dea113ac5f748b9148357"></a>

### `HL78XX_MONITOR_INITIAL_PAUSED`

```c
#define HL78XX_MONITOR_INITIAL_PAUSED ( ...)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
COND_CODE_1(IS_EMPTY(__VA_ARGS__), (false), (__VA_ARGS__))
```

解析可选的监视器初始状态参数（Monitor Initial State Argument）。

若未提供可选的 `state` 参数，监视器以活动状态启动；否则使用所提供的状态值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `...` | 可选的监视器初始状态，取值为 `HL78XX_MONITOR_ACTIVE` 或 `HL78XX_MONITOR_PAUSED`。 |

<a id="gac485491202b429e8512c210360d1b2f9"></a>

### `HL78XX_MONITOR_PAUSED`

```c
#define HL78XX_MONITOR_PAUSED true
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

HL78xx 监视器（Monitor）的初始暂停状态（Paused State）。

定义初始状态应为暂停的监视器时，可将此值用作可选的 `state` 参数。

<a id="ga1dd356d88b67261a642ba50730b31b48"></a>

### `HL78XX_NETWORK_ADDRESS_MAX_LEN`

```c
#define HL78XX_NETWORK_ADDRESS_MAX_LEN 46
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

网络地址字符串（Network Address String）的最大长度。

<a id="ga2586187555aed092ffbf40e7991cc266"></a>

### `MDM_APN_MAX_LENGTH`

```c
#define MDM_APN_MAX_LENGTH 64
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

接入点名称（APN）字符串的最大长度。

<a id="ga1760f6b6b71f238b2e4a4f2082899dd7"></a>

### `MDM_HL78XX_CME_ERROR_STRING`

```c
#define MDM_HL78XX_CME_ERROR_STRING "+CME ERROR: "
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

移动设备（Mobile Equipment，CME）错误响应的前缀，通常后跟错误码（Error Code）。

<a id="ga65d332f108a5cbc6e3038db4fa2fee65"></a>

### `MDM_HL78XX_CMS_ERROR_STRING`

```c
#define MDM_HL78XX_CMS_ERROR_STRING "+CMS ERROR: "
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

消息服务（Message Service，CMS）错误响应的前缀，通常与短信（SMS）操作相关。

<a id="gab53f7ed6e7b4b70f7675184e666bf9f0"></a>

### `MDM_HL78XX_CONNECT_STRING`

```c
#define MDM_HL78XX_CONNECT_STRING "CONNECT"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

表示已成功建立数据连接（Data Connection）的响应字符串。

<a id="ga6b0f0f61bd70c9e09031ecdb9dcf2f52"></a>

### `MDM_HL78XX_DESIRED_VERSION_STRING`

```c
#define MDM_HL78XX_DESIRED_VERSION_STRING
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

展开值（Value）：

```c
(sizeof(CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION) > 1                                        \
         ? CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION                                          \
         : "HL7812.5.7.4.0")
```

期望的固件版本字符串（Firmware Version String）。

<a id="ga8bc5d49dd46c8bff682528127310a1eb"></a>

### `MDM_HL78XX_EOF_PATTERN`

```c
#define MDM_HL78XX_EOF_PATTERN "--EOF--Pattern--"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于指示文件结束（End-of-file）或数据传输完成（Completion of Data Transmission）的模式。

<a id="gac06ec76b0de379682110e590c4b400de"></a>

### `MDM_HL78XX_ERROR_STRING`

```c
#define MDM_HL78XX_ERROR_STRING "ERROR"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

表示命令失败（Command Failure）的通用错误响应字符串。

<a id="gae2b96cddac89ab608658fe11bfdac45e"></a>

### `MDM_HL78XX_NO_CARRIER_STRING`

```c
#define MDM_HL78XX_NO_CARRIER_STRING "NO CARRIER"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

表示连接已丢失或终止（Lost or Terminated）的响应字符串。

<a id="ga08eaa30cab6c59b2b4e9e33ff8c12704"></a>

### `MDM_HL78XX_OK_STRING`

```c
#define MDM_HL78XX_OK_STRING "OK"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

表示 AT 命令成功执行（Successful Execution）的标准响应字符串。

<a id="ga00e8685b8a1c0b4a9b5ba18dfdd7c879"></a>

### `MDM_HL78XX_TERMINATION_PATTERN`

```c
#define MDM_HL78XX_TERMINATION_PATTERN "+++"
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于退出数据模式（Data Mode）、返回命令模式（Command Mode）的转义／终止序列（Escape/Termination Sequence）。

<a id="gaa14eef37d2beacdb02a50ec4eb93d1fd"></a>

### `MDM_ICCID_LENGTH`

```c
#define MDM_ICCID_LENGTH 22
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器集成电路卡识别码（ICCID）字符串的最大长度。

<a id="ga9213ea6a80a1f80b10ade16314fa56dd"></a>

### `MDM_IMEI_LENGTH`

```c
#define MDM_IMEI_LENGTH 16
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器国际移动设备识别码（IMEI）字符串的最大长度。

<a id="ga9c11717136907c549f2ddb5c9bab48b7"></a>

### `MDM_IMSI_LENGTH`

```c
#define MDM_IMSI_LENGTH 23
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器国际移动用户识别码（IMSI）字符串的最大长度。

<a id="ga9587840c88858d1c26bd3afedd96bd68"></a>

### `MDM_MANUFACTURER_LENGTH`

```c
#define MDM_MANUFACTURER_LENGTH 20
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器制造商字符串（Modem Manufacturer String）的最大长度。

<a id="ga0a99d20ad7b62fd41c0118e2f5af522b"></a>

### `MDM_MAX_CERT_LENGTH`

```c
#define MDM_MAX_CERT_LENGTH 4096
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

证书（Certificate）的最大长度。

<a id="gaad7153fc809f017cd727bc60988fd799"></a>

### `MDM_MAX_HOSTNAME_LEN`

```c
#define MDM_MAX_HOSTNAME_LEN 128
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

主机名（Hostname）的最大长度。

<a id="ga694436b7ecedfd934f78afa9f404cadb"></a>

### `MDM_MODEL_LENGTH`

```c
#define MDM_MODEL_LENGTH 32
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器型号字符串（Modem Model String）的最大长度。

<a id="ga6327f0d9596ad616f844687ac0fbc4f9"></a>

### `MDM_REVISION_LENGTH`

```c
#define MDM_REVISION_LENGTH 64
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

调制解调器修订版本字符串（Modem Revision String）的最大长度。

<a id="gae2d73fc3652b58cc2d2b8bfb72f6e86d"></a>

### `MDM_SERIAL_NUMBER_LENGTH`

```c
#define MDM_SERIAL_NUMBER_LENGTH 32
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

序列号字符串（Serial Number String）的最大长度。

<a id="ga734b46dfd78fbf6fc938a6f9115f2cc7"></a>

### `PAUSED`

```c
#define PAUSED 1
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

监视器已暂停。

<a id="ga03910e4575bfd4ed439e1c9a0220c7a2"></a>

### `hl78xx_api_configure_networks`

```c
typedef int(* hl78xx_api_configure_networks) (const struct device *dev, const struct hl78xx_network *networks, uint8_t size)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于配置网络（Networks）的 API 函数指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `networks` | 网络配置数组。 |
| `size` | 数组中的网络数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaa7cb75a0ef3cd4cb607bb0e3f3b3468f"></a>

### `hl78xx_api_get_modem_info`

```c
typedef int(* hl78xx_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取调制解调器信息（Modem Information）的 API 函数指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 调制解调器信息类型。 |
| `info` | 用于保存信息字符串的缓冲区。 |
| `size` | 信息缓冲区大小。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gab3bcb3ba4cef24971acc41aa0815abe5"></a>

### `hl78xx_api_get_phone_functionality`

```c
typedef int(* hl78xx_api_get_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取电话功能（Phone Functionality）的 API。

<a id="ga586f65e3f3ea8852261be04ce7ba67ba"></a>

### `hl78xx_api_get_registration_status`

```c
typedef int(* hl78xx_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取注册状态（registration status）的 API。

<a id="ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a"></a>

### `hl78xx_api_get_signal`

```c
typedef int(* hl78xx_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取网络信号强度（signal strength）的 API。

<a id="ga6bf75bd8e583b4e076b73268a712977d"></a>

### `hl78xx_api_get_supported_networks`

```c
typedef int(* hl78xx_api_get_supported_networks) (const struct device *dev, const struct hl78xx_network **networks, uint8_t *size)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取支持的网络（Supported Networks）的 API 函数指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `networks` | 用于接收网络数组的指针。 |
| `size` | 用于接收数组大小的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga8201489ac8055efa3019ffd8f3201644"></a>

### `hl78xx_api_send_at_cmd`

```c
typedef int(* hl78xx_api_send_at_cmd) (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于获取电话功能（Phone Functionality）的 API。

<a id="ga7cf1c4b11a828c186771200cd00b3bc8"></a>

### `hl78xx_api_set_phone_functionality`

```c
typedef int(* hl78xx_api_set_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于设置电话功能（Phone Functionality）的 API 函数指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `functionality` | 电话功能模式（Phone Functionality Mode）。 |
| `reset` | 是否复位调制解调器。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga98fde2c3465abce3b4b7d94816bc029c"></a>

### `hl78xx_at_monitor_handler_t`

```c
typedef void(* hl78xx_at_monitor_handler_t) (const struct hl78xx_at_notification *notif, struct hl78xx_at_monitor_entry *mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

AT 监视器处理函数（AT Monitor Handler）的函数类型。

用于接收已解析的主动上报 AT 通知（Unsolicited AT Notification）的用户回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `notif` | 指向已解析 AT 通知的指针。 |
| `mon` | 指向接收到通知的监视器条目的指针。 |

<a id="ga517a58c85701991214ddb3a9d786f367"></a>

### `hl78xx_at_monitor_release_t`

```c
typedef void(* hl78xx_at_monitor_release_t) (struct hl78xx_at_monitor_entry *mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

AT 监视器释放函数（AT Monitor Release）的函数类型。

在 AT 监视器条目被释放且不再被引用时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向正在释放的监视器条目的指针。 |

<a id="gade4999c5b603813020cd52a93687b76f"></a>

### `hl78xx_evt_monitor_dispatcher_t`

```c
typedef void(* hl78xx_evt_monitor_dispatcher_t) (struct hl78xx_evt *notif)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

事件监视器分派函数（Event Monitor Dispatcher）的函数类型。

调用此函数，将事件分发给已注册的监视器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `notif` | 指向事件通知的指针。 |

<a id="gaa1346c7b8b44abae64f59cc8d5fa9c01"></a>

### `hl78xx_evt_monitor_handler_t`

```c
typedef void(* hl78xx_evt_monitor_handler_t) (struct hl78xx_evt *notif, struct hl78xx_evt_monitor_entry *mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

事件监视器处理函数（Event Monitor Handler）的函数类型。

用于接收事件通知的用户回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `notif` | 指向事件通知的指针。 |
| `mon` | 指向接收到事件的监视器条目的指针。 |

<a id="ga774bbdee241bfb63374fdc74d2353a3d"></a>

### `hl78xx_evt_monitor_release_t`

```c
typedef void(* hl78xx_evt_monitor_release_t) (struct hl78xx_evt_monitor_entry *mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

事件监视器释放函数（Event Monitor Release）的函数类型。

在事件监视器条目被释放且不再被引用时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向正在释放的监视器条目的指针。 |

<a id="ga9198bafcc7c78243fc72ca2b0bc926ed"></a>

### `hl78xx_gnss_aux_data_callback_t`

```c
typedef void(* hl78xx_gnss_aux_data_callback_t) (const struct device *dev, const struct hl78xx_gnss_nmea_aux_data *aux_data, uint16_t size)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

全球导航卫星系统（GNSS）辅助数据回调的函数类型（Callback Function Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `aux_data` | 指向辅助 NMEA 数据结构的指针。 |
| `size` | 辅助数据的大小。 |

<a id="ga82793d1f4c0c8f03ae27b29afa1c3d3f"></a>

### `hl78xx_runtime_band_provider_t`

```c
typedef bool(* hl78xx_runtime_band_provider_t) (const struct device *dev, enum hl78xx_cell_rat_mode rat, uint16_t *band, void *user_data)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

用于为无线接入技术（RAT）提供可选运行时频段覆盖设置（Runtime Band Override）的回调。

调制解调器驱动不关心调用者如何保存或推导运行时频段选择。注册提供者（Provider）后，`hl78xx_band_cfg()` 会为请求的无线接入技术（RAT）查询覆盖频段；若未提供，则回退到 Kconfig 默认值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `rat` | 当前正在配置的无线接入技术（RAT）。 |
| `band` | 输出频段编号，仅在回调返回 `true` 时写入。 |
| `user_data` | 注册时传入的、由调用者拥有的不透明上下文（Opaque Context）。 |

**返回（Returns）**：返回值：当 `rat` 存在有效的运行时频段覆盖值时返回 `true`。

<a id="ga2a471bc1b92dba1e316b2b27e3778e1a"></a>

### `gnss_position_events`

```c
enum gnss_position_events
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

全球导航卫星系统（GNSS）位置事件（Position Events），`eventType = 3`。

调制解调器报告的定位状态（Position Fix Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_FIX_LOST_OR_UNAVAILABLE` | 0——GNSS 定位已丢失，或者尚不可用。 |
| `GNSS_ESTIMATED_POSITION_AVAILABLE` | 1——有可用的估算 GNSS 位置，即预测位置（Predicted Position）。 |
| `GNSS_2D_POSITION_AVAILABLE` | 2——有可用的二维 GNSS 位置。 |
| `GNSS_3D_POSITION_AVAILABLE` | 3——有可用的三维位置。 |
| `GNSS_FIX_CHANGED_TO_INVALID` | 4——GNSS 定位已变为无效位置。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

<a id="gae9cf9c13242bc674dd7b0b79a69b8f31"></a>

### `hl78xx_agnss_days`

```c
enum hl78xx_agnss_days
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

待下载的预测辅助数据（Predicted Assistance Data）天数，用于写命令；或距离其过期的天数，用于读命令。

`AT+GNSSAD=1,<days>` 命令仅接受这些值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_AGNSS_DAYS_1` | 请求 1 天的辅助 GNSS（A-GNSS）辅助数据。 |
| `HL78XX_AGNSS_DAYS_2` | 请求 2 天的辅助 GNSS（A-GNSS）辅助数据。 |
| `HL78XX_AGNSS_DAYS_3` | 请求 3 天的辅助 GNSS（A-GNSS）辅助数据。 |
| `HL78XX_AGNSS_DAYS_7` | 请求 7 天的辅助 GNSS（A-GNSS）辅助数据。 |
| `HL78XX_AGNSS_DAYS_14` | 请求 14 天的辅助 GNSS（A-GNSS）辅助数据。 |
| `HL78XX_AGNSS_DAYS_28` | 请求 28 天的辅助 GNSS（A-GNSS）辅助数据。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

<a id="ga7d4975dffccffac27c9dccb85c02d549"></a>

### `hl78xx_agnss_mode`

```c
enum hl78xx_agnss_mode
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

辅助全球导航卫星系统（A-GNSS）辅助数据有效期模式（Assistance Data Validity Mode）。

`AT+GNSSAD?` 读取命令返回的模式值，或写入命令使用的模式值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_AGNSS_MODE_INVALID` | 数据无效（读取）／删除数据（写入）。 |
| `HL78XX_AGNSS_MODE_VALID` | 数据有效（读取）／下载数据（写入）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

<a id="ga298f953be96ab47be40b5440a2573182"></a>

### `hl78xx_cell_rat_mode`

```c
enum hl78xx_cell_rat_mode
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

蜂窝无线接入技术（Cellular Radio Access Technologies）。

HL78xx 调制解调器支持的无线接入技术（RAT）模式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_RAT_CAT_M1` | LTE Cat-M1 无线接入技术。 |
| `HL78XX_RAT_NB1` | 窄带物联网（NB-IoT）无线接入技术。 |
| `HL78XX_RAT_GSM` | 全球移动通信系统（GSM）无线接入技术，仅限 HL7812。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_12` 时可用。 |
| `HL78XX_RAT_NBNTN` | NB-IoT 非地面网络（Non-Terrestrial Network，NTN），适用于 HL7812 固件 R6 及更高版本。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_12_FW_R6` 时可用。 |
| `HL78XX_RAT_MODE_AUTO` | 自动无线接入技术选择模式（Automatic RAT Selection）。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。 |
| `HL78XX_RAT_MODE_NONE` | 无无线接入技术模式（No RAT Mode）。 |
| `HL78XX_RAT_COUNT` | 有效无线接入技术（RAT）模式的数量。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_12` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_12_FW_R6` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

<a id="ga5d8a5b00f354e98abc2effa560f3bac8"></a>

### `hl78xx_edrx_event`

```c
enum hl78xx_edrx_event
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

扩展非连续接收（eDRX）事件类型。

调制解调器报告的扩展非连续接收（eDRX）事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_EDRX_EVENT_IDLE_EXIT` | 调制解调器已退出 eDRX 空闲模式。 |
| `HL78XX_EDRX_EVENT_IDLE_ENTER` | 调制解调器已进入 eDRX 空闲模式。 |
| `HL78XX_EDRX_EVENT_IDLE_NONE` | 无 eDRX 事件。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_EDRX`。

<a id="ga9b9da1841754d723cddc103800b141ae"></a>

### `hl78xx_event_status`

```c
enum hl78xx_event_status
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

GNSS 事件状态。

GNSS 操作的状态码（Status Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_STATUS_FAILED` | 操作失败（Operation Failed）。 |
| `HL78XX_STATUS_SUCCESS` | 操作成功（Operation Succeeded）。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

<a id="ga8a864475f6e9673f85ec7c56028992a5"></a>

### `hl78xx_evt_type`

```c
enum hl78xx_evt_type
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

HL78xx 事件类型（Event Types）。

来自 HL78xx 调制解调器的异步事件通知（Asynchronous Event Notification）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_LTE_RAT_UPDATE` | LTE 无线接入技术（RAT）已变化。 |
| `HL78XX_LTE_REGISTRATION_STAT_UPDATE` | LTE 网络注册状态已变化。 |
| `HL78XX_LTE_SIM_REGISTRATION` | 用户识别模块（SIM）注册状态已变化。 |
| `HL78XX_LTE_MODEM_STARTUP` | 调制解调器启动完成。 |
| `HL78XX_LTE_FOTA_UPDATE_STATUS` | 无线固件升级（FOTA）状态已变化。 |
| `HL78XX_LTE_DNS_READY` | 域名解析（DNS）流程完成，调制解调器已准备好传输数据。 |
| `HL78XX_LTE_AT_CMD_READY` | AT 命令接口已准备好供应用使用。 |
| `HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE` | 电话功能已变化（`+CFUN`）。 |
| `HL78XX_LTE_CTZEU_UPDATE` | 扩展时区和世界时间更新（`+CTZEU`）。 |
| `HL78XX_GNSS_ENGINE_READY` | GNSS 引擎已初始化并就绪。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_INIT` | GNSS 引擎初始化事件。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_START` | GNSS 搜索已开始。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_STOP` | GNSS 搜索已停止。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_POSITION` | 已获得 GNSS 定位结果（Position Fix）。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_START_BLOCKED` | 由于 LTE 处于活动状态，GNSS 启动失败；两者共享射频（RF）路径。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_SEARCH_TIMEOUT` | GNSS 搜索超时。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_GNSS_EVENT_MODE_EXITED` | 已退出 GNSS 模式；调制解调器现在处于飞行模式（Airplane Mode），用户可以决定下一步操作。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 时可用。 |
| `HL78XX_EDRX_IDLE_UPDATE` | 已进入扩展非连续接收（eDRX）空闲模式。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_EDRX` 时可用。 |
| `HL78XX_LTE_PSMEV_UPDATE` | 调制解调器省电模式（PSM）事件更新。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_PSM` 时可用。 |
| `HL78XX_POWER_DOWN_UPDATE` | 调制解调器关断（Power-down）事件更新。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_POWER_DOWN` 时可用。 |
| `HL78XX_VGPIO_LOW` | VGPIO 引脚变为低电平（LOW）。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。 |
| `HL78XX_VGPIO_HIGH` | VGPIO 引脚变为高电平（HIGH）。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。 |
| `HL78XX_GPIO6_LOW` | GPIO6 引脚变为低电平（LOW），表示进入睡眠或关断状态。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。 |
| `HL78XX_GPIO6_HIGH` | GPIO6 引脚变为高电平（HIGH），表示从睡眠或关断状态唤醒。注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。 |
| `HL78XX_CELLMEAS_UPDATE` | 蜂窝测量（Cellular Measurement）更新。 |
| `HL78XX_EVT_TYPE_COUNT` | 事件类型数量。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_EDRX` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_PSM` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_POWER_DOWN` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。

<a id="ga95d1ccc5899adf1b2eda6aa0777b7e80"></a>

### `hl78xx_gnss_event_type`

```c
enum hl78xx_gnss_event_type
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

全球导航卫星系统（GNSS）事件类型。

调制解调器报告的 GNSS 事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_GNSSEV_INITIALISATION` | GNSS 引擎初始化事件。 |
| `HL78XX_GNSSEV_START` | GNSS 搜索开始事件。 |
| `HL78XX_GNSSEV_STOP` | GNSS 搜索停止事件。 |
| `HL78XX_GNSSEV_POSITION` | GNSS 定位事件（Position Fix Event）。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

<a id="gaf2ab6a096dff081e7cbbba13b06de3cc"></a>

### `hl78xx_kselacq_rat`

```c
enum hl78xx_kselacq_rat
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

原始 `AT+KSELACQ` 首选列表（PRL）中的无线接入技术（RAT）条目。

这些值直接遵循调制解调器命令语法，与枚举 `hl78xx_cell_rat_mode` 的数值编码不同。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_KSELACQ_RAT_CLEAR` | 清除首选无线接入技术列表（Preferred RAT List，PRL），并禁用自动无线接入技术（RAT）切换。 |
| `HL78XX_KSELACQ_RAT_CAT_M1` | 用于 Cat-M1 的首选无线接入技术列表（Preferred RAT List，PRL）条目。 |
| `HL78XX_KSELACQ_RAT_NB1` | 用于 NB-IoT 的首选无线接入技术列表（Preferred RAT List，PRL）条目。 |
| `HL78XX_KSELACQ_RAT_GSM` | 用于 GSM 的首选无线接入技术列表（Preferred RAT List，PRL）条目。仅在 HL7812 上支持。 |

<a id="gaadcca229cbccc9832734bcc4e2a443e6"></a>

### `hl78xx_modem_info_type`

```c
enum hl78xx_modem_info_type
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

可查询的调制解调器信息类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_MODEM_INFO_SERIAL_NUMBER` | 调制解调器序列号（Modem Serial Number）。 |
| `HL78XX_MODEM_INFO_CURRENT_BAUD_RATE` | 当前波特率（Baud Rate）。 |
| `HL78XX_MODEM_INFO_FW_VERSION` | 固件版本（Firmware Version）。 |

<a id="ga618c248d23a1db1b027333c92adf99a1"></a>

### `hl78xx_modem_restart_mode`

```c
enum hl78xx_modem_restart_mode
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

由驱动管理的调制解调器重启模式（Driver-managed Modem Restart Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_MODEM_RESTART_HARD` | 通过专用复位引脚重启调制解调器。 |
| `HL78XX_MODEM_RESTART_SOFT` | 通过发送 `AT+CFUN=4,1` 重启调制解调器。 |

<a id="gab4a85c57d2f77c04a887f6552abff48a"></a>

### `hl78xx_module_status`

```c
enum hl78xx_module_status
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

模块状态码（Module Status Codes）。

`AT+CPIN?` 返回的状态码，用于指示 SIM 和模块状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_MODULE_READY` | 模块已准备好接收终端设备（TE）的命令。不需要访问码（Access Code）。 |
| `HL78XX_MODULE_WAITING_FOR_ACCESS_CODE` | 模块正在等待访问码（Access Code）。使用 `AT+CPIN?` 确定所需访问码。 |
| `HL78XX_MODULE_SIM_NOT_PRESENT` | 未插入 SIM 卡。 |
| `HL78XX_MODULE_SIMLOCK` | 模块处于“SIMlock”（SIM 锁定）状态。 |
| `HL78XX_MODULE_UNRECOVERABLE_ERROR` | 不可恢复错误（Unrecoverable Error）。 |
| `HL78XX_MODULE_UNKNOWN_STATE` | 未知状态（Unknown State）。 |
| `HL78XX_MODULE_INACTIVE_SIM` | SIM 未激活。 |

<a id="ga563d651fff3621c1e21d7c47d19fd218"></a>

### `hl78xx_network_info_type`

```c
enum hl78xx_network_info_type
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

缓存的网络信息类型（Cached Network Information Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_NETWORK_INFO_APN` | 接入点名称（Access Point Name，APN）。 |
| `HL78XX_NETWORK_INFO_CURRENT_RAT` | 当前无线接入技术（Radio Access Technology，RAT）。 |
| `HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA` | 采用长字母数字格式的网络运营商名称。 |
| `HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA` | 采用短字母数字格式的网络运营商名称。 |
| `HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC` | 采用数字格式的网络运营商名称。 |
| `HL78XX_NETWORK_INFO_OPERATOR_FORMAT` | 从 `+COPS` 获取的当前运营商格式。 |
| `HL78XX_NETWORK_INFO_TAC` | 从 `+CEREG` 获取的跟踪区码（Tracking Area Code）。 |
| `HL78XX_NETWORK_INFO_MCC` | 从数字格式运营商标识解析的移动国家码（Mobile Country Code，MCC）。 |
| `HL78XX_NETWORK_INFO_MNC` | 从数字格式运营商标识解析的移动网络码（Mobile Network Code，MNC）。 |
| `HL78XX_NETWORK_INFO_CELL_ID` | 从 `+CEREG` 获取的小区标识（Cell ID）。 |
| `HL78XX_NETWORK_INFO_IP_ADDRESS` | 分组数据协议（PDP）IP 地址。 |
| `HL78XX_NETWORK_INFO_DNS_PRIMARY` | 主域名服务器（Primary DNS）地址。 |
| `HL78XX_NETWORK_INFO_ACTIVE_BAND` | 从 `AT+KBND?` 的位图（Bitmap）解码出的活动频段编号。 |
| `HL78XX_NETWORK_INFO_SINR` | 最近一次 `+KCELLMEAS` 主动上报结果码（URC）中的信号与干扰加噪声比（SINR）。 |

<a id="ga2d26ae6044baac5995f4184abe4faad3"></a>

### `hl78xx_operator_format`

```c
enum hl78xx_operator_format
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

网络运营商格式选项（Network Operator Format Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC` | 长字母数字格式的运营商名称，`AT+COPS` 格式 0。 |
| `HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC` | 短字母数字格式的运营商名称，`AT+COPS` 格式 1。 |
| `HL78XX_OPERATOR_FORMAT_NUMERIC` | 数字格式的运营商名称，即 MCC-MNC，`AT+COPS` 格式 2。 |

<a id="ga39a3de13bd706571cd7348ea46b7b708"></a>

### `hl78xx_phone_functionality`

```c
enum hl78xx_phone_functionality
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

电话功能模式（Phone Functionality Modes）。

用于控制调制解调器运行状态的 `AT+CFUN` 命令模式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_SIM_POWER_OFF` | SIM 和调制解调器断电，处于最小功能（Minimum Functionality）状态。 |
| `HL78XX_FULLY_FUNCTIONAL` | 完整功能（Full Functionality），调制解调器可正常工作。 |
| `HL78XX_AIRPLANE` | 飞行模式（Airplane Mode），射频（RF）发射器禁用。 |

<a id="ga50bd06a27371c5c79de5bef125d6b5f3"></a>

### `hl78xx_power_down_response`

```c
enum hl78xx_power_down_response
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

应用程序对待处理掉电请求（Pending Power-down Request）的响应。

当以 `POWER_DOWN_EVENT_ENTER` 分发 `HL78XX_POWER_DOWN_UPDATE` 之后，这些值控制驱动如何处理第二阶段的关机工作。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE` | 驱动工作队列一旦能够运行关机工作，就继续执行关机。 |
| `HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE` | 从当前时刻起，按调用者提供的超时时长延长关机宽限期（Shutdown Grace Period）。 |
| `HL78XX_POWER_DOWN_RESPONSE_ABORT` | 完全中止待执行的关机：应用仍拥有调制解调器，可能正在搜索、重连、切换 SIM 或进行无线固件升级（FOTA）。取消已调度的关机工作，并重新允许喂送非活动计时器（Inactivity Timer）。仅在关机宽限期尚未结束时有效。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

<a id="gae891e3155a0ebf72433dd58ae4c36512"></a>

### `hl78xx_psmev_event`

```c
enum hl78xx_psmev_event
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

省电模式（PSM）事件类型。

调制解调器报告的省电模式（Power Saving Mode，PSM）事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_PSM_EVENT_EXIT` | 调制解调器已退出 PSM 模式。 |
| `HL78XX_PSM_EVENT_ENTER` | 调制解调器已进入 PSM 模式。 |
| `HL78XX_PSM_EVENT_NONE` | 无 PSM 事件。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_PSM`。

<a id="ga0b3efb75d166d9d4bf163ffc6bb68fc0"></a>

### `hl78xx_sim_slot`

```c
enum hl78xx_sim_slot
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

由可选 SIM 切换 GPIO（SIM-switch GPIO）驱动的外部 SIM 卡槽选择（External SIM Slot Selection）。

卡槽 1 对应 SIM 切换 GPIO 的逻辑低电平，卡槽 2 对应逻辑高电平。设备树（Devicetree）的极性标志仍适用于物理引脚。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_SIM_SLOT_1` | 选择 SIM 卡槽 1，逻辑低电平。 |
| `HL78XX_SIM_SLOT_2` | 选择 SIM 卡槽 2，逻辑高电平。 |

<a id="gabb0e5a4dd5c2e29d62ba27f6022f01f5"></a>

### `nmea_output_port`

```c
enum nmea_output_port
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

NMEA 输出端口选项（Output Port Options）。

调制解调器输出 GNSS NMEA 语句的端口选择。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NMEA_OUTPUT_NONE` | `0x00`——不输出 NMEA 帧。 |
| `NMEA_OUTPUT_USB_NMEA_PORT` | `0x01`——通过 USB 上的专用 NMEA 端口输出 NMEA 帧。 |
| `NMEA_OUTPUT_UART1` | `0x03`——通过 UART1 输出 NMEA 帧。 |
| `NMEA_OUTPUT_SAME_PORT` | `0x04`——通过收到 `+GNSSNMEA` 的同一端口输出 NMEA 帧。 |
| `NMEA_OUTPUT_CMUX_DLC1` | `0x05`——通过 CMUX 数据链路连接 1（DLC1）输出 NMEA 帧。 |
| `NMEA_OUTPUT_CMUX_DLC2` | `0x06`——通过 CMUX 数据链路连接 2（DLC2）输出 NMEA 帧。 |
| `NMEA_OUTPUT_CMUX_DLC3` | `0x07`——通过 CMUX 数据链路连接 3（DLC3）输出 NMEA 帧。 |
| `NMEA_OUTPUT_CMUX_DLC4` | `0x08`——通过 CMUX 数据链路连接 4（DLC4）输出 NMEA 帧。 |

<a id="ga6340324dcb76101c66b902bb9a14dbd3"></a>

### `power_down_event`

```c
enum power_down_event
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

掉电事件类型（Power Down Event Types）。

调制解调器报告的关断（Power Down）事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `POWER_DOWN_EVENT_ENTER` | 关断事件：调制解调器正在进入关断模式。 |
| `POWER_DOWN_EVENT_EXIT` | 关断事件：调制解调器正在退出关断模式。 |
| `POWER_DOWN_EVENT_NONE` | 无关断事件。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

<a id="ga5453000edbd52c54f7193de4852aa9a8"></a>

### `wdsi_indication`

```c
enum wdsi_indication
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设备服务指示（Device Services Indications，`+WDSI`）。

表示 AirVantage 设备服务指示（Device Services Indication）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WDSI_BOOTSTRAP_CREDENTIALS_PRESENT` | 如果存在引导服务器（Bootstrap Server）的凭据，则在启动时触发。 |
| `WDSI_USER_AGREEMENT_REQUEST` | 设备请求用户同意连接 AirVantage。 |
| `WDSI_FIRMWARE_DOWNLOAD_REQUEST` | AirVantage 请求设备下载固件包（Firmware Package）。 |
| `WDSI_FIRMWARE_INSTALL_REQUEST` | AirVantage 请求设备安装固件包（Firmware Package）。 |
| `WDSI_AUTHENTICATION_START` | 开始向引导服务器（Bootstrap Server）或设备管理服务器（DM Server）进行认证。 |
| `WDSI_AUTHENTICATION_FAILED` | 认证失败（Authentication Failed）。 |
| `WDSI_AUTHENTICATION_SUCCESS` | 认证成功，开始会话（Session）。 |
| `WDSI_CONNECTION_DENIED` | 服务器拒绝连接。 |
| `WDSI_DM_SESSION_CLOSED` | 设备管理（DM）会话已关闭。 |
| `WDSI_FIRMWARE_AVAILABLE` | 有可供下载的固件包。 |
| `WDSI_FIRMWARE_DOWNLOADED` | 固件包已下载并保存。 |
| `WDSI_FIRMWARE_DOWNLOAD_ISSUE` | 固件下载出现问题，原因由子码（Subcode）指示。 |
| `WDSI_PACKAGE_VERIFIED_CERTIFIED` | 固件包已验证并通过认证。 |
| `WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED` | 固件包已验证，但未通过认证。 |
| `WDSI_FIRMWARE_UPDATE_START` | 开始固件更新。 |
| `WDSI_FIRMWARE_UPDATE_FAILED` | 固件更新失败（Firmware Update Failed）。 |
| `WDSI_FIRMWARE_UPDATE_SUCCESS` | 固件更新成功（Firmware Updated Successfully）。 |
| `WDSI_DOWNLOAD_IN_PROGRESS` | 正在下载，同时指示完成百分比。 |
| `WDSI_SESSION_STARTED` | 已与引导服务器（Bootstrap Server，`+WDSI: 23,0`）或设备管理服务器（DM Server，`+WDSI: 23,1`）建立会话。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_AIRVANTAGE`。

<a id="gac9f87f986b0b745bf8e370896113066f"></a>

### `hl78xx_access_tech_to_rat()`

```c
enum hl78xx_cell_rat_mode hl78xx_access_tech_to_rat ( enum cellular_access_technology access_tech)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将标准蜂窝接入技术（Cellular Access Technology）转换为 HL78xx 无线接入技术模式（RAT Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `access_tech` | 标准蜂窝接入技术（Cellular Access Technology）。 |

**返回（Returns）**：返回值：对应的 HL78xx 无线接入技术（RAT）模式。

<a id="ga6adcbc5395d078be2fc9c6e62612f603"></a>

### `hl78xx_api_func_at_is_busy()`

```c
bool hl78xx_api_func_at_is_busy ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

面向这样的调用者：在自己的工作队列（Work Queue）中驱动动态 AT 命令，并希望避免发起会因 `-EBUSY` 而被拒绝的发送。

这是无锁轮询（Lock-free Poll），天然存在竞争条件：脚本可能在查询与发送之间启动。因此它仅是一项优化；调用者仍必须检查发送操作本身的返回值，并在返回 `-EBUSY` 时重试。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |

**返回（Returns）**：返回值：有脚本正在运行，或者 `dev` 无效时，返回 `true`。

<a id="ga5f9c8c8087e1e6008f290ddfe42e3d97"></a>

### `hl78xx_api_func_get_modem_info()`

```c
int hl78xx_api_func_get_modem_info ( const struct device * dev, enum hl78xx_modem_info_type type, void * info, size_t size )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取厂商专用的调制解调器信息（Vendor-specific Modem Information），内部实现。

用于获取 HL78xx 专用调制解调器信息的内部函数。用户应改用 `hl78xx_get_modem_info()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 要获取的调制解调器信息类型。 |
| `info` | 用于保存调制解调器信息的指针。 |
| `size` | 信息缓冲区大小。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gacddf878e52d0642279e147add9c8bdad"></a>

### `hl78xx_api_func_get_modem_info_standard()`

```c
int hl78xx_api_func_get_modem_info_standard ( const struct device * dev, enum cellular_modem_info_type type, char * info, size_t size )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

从缓存获取标准调制解调器信息（Modem Information），采用 Zephyr 蜂窝 API（Cellular API）。

读取驱动在初始化脚本执行期间缓存的标识字段。不发送任何 AT 命令，可以安全地从任意上下文调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | Zephyr 蜂窝调制解调器信息类型。 |
| `info` | 用于保存信息字符串的缓冲区。 |
| `size` | 缓冲区大小，单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0；不处理该类型时返回 `-ENOTSUP`；失败时返回负的 `errno` 错误码。

<a id="gac08824e4662cb5fcb316e6a0e1e5ba17"></a>

### `hl78xx_api_func_get_network_info()`

```c
int hl78xx_api_func_get_network_info ( const struct device * dev, enum hl78xx_network_info_type type, void * info, size_t size )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取缓存的厂商专用网络信息（Vendor-specific Network Information）。

用于获取 HL78xx 专用网络信息的内部函数。用户应改用 `hl78xx_get_network_info()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 要获取的网络信息类型。 |
| `info` | 用于保存网络信息的指针。 |
| `size` | 信息缓冲区大小。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gaca72419e4396a45b296a65f89877dbb8"></a>

### `hl78xx_api_func_get_phone_functionality()`

```c
int hl78xx_api_func_get_phone_functionality ( const struct device * dev, enum hl78xx_phone_functionality * functionality )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取电话功能模式（Phone Functionality Mode），内部实现。

用于查询调制解调器电话功能模式（Phone Functionality Mode）的内部函数。用户应改用 `hl78xx_get_phone_functionality()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `functionality` | 用于保存当前电话功能模式的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="ga4c2dc7d53dd4780d8f1e00e9889248d3"></a>

### `hl78xx_api_func_get_prl()`

```c
int hl78xx_api_func_get_prl ( const struct device * dev, struct kselacq_syntax * kselacq_rats )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取当前首选无线接入技术列表（Preferred RAT List）。

从调制解调器缓存中获取当前原始 `AT+KSELACQ` 首选无线接入技术列表（Preferred RAT List，PRL）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `kselacq_rats` | 用于保存当前首选无线接入技术列表（Preferred RAT List，PRL）条目的指针。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gadd718f794b24c9610e97f7460519e577"></a>

### `hl78xx_api_func_get_rsrp_validity()`

```c
int hl78xx_api_func_get_rsrp_validity ( const struct device * dev, bool * is_valid )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前参考信号接收功率（RSRP）是否达到配置的最低阈值。

使用驱动的标准信号查询路径，并将返回的参考信号接收功率（RSRP，单位 dBm）与 `CONFIG_MODEM_MIN_ALLOWED_SIGNAL_STRENGTH` 比较。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga79c8b3e0581e6418526b3aa86e6bbb5a"></a>

### `hl78xx_api_func_get_rsrq_validity()`

```c
int hl78xx_api_func_get_rsrq_validity ( const struct device * dev, bool * is_valid )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前参考信号接收质量（RSRQ）是否达到配置的最低阈值。

使用驱动的标准信号查询路径，并将返回的参考信号接收质量（RSRQ，单位 dB）与 `CONFIG_MODEM_MIN_ALLOWED_SIGNAL_QUALITY` 比较。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gae50586b4f939abacda6739850c118982"></a>

### `hl78xx_api_func_get_signal()`

```c
int hl78xx_api_func_get_signal ( const struct device * dev, const enum cellular_signal_type type, int16_t * value )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取网络信号强度（Network Signal Strength），内部实现。

用于获取蜂窝信号强度指标的内部函数。用户应改用标准蜂窝 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 要获取的信号类型，例如 RSSI、RSRP、RSRQ 等。 |
| `value` | 用于保存信号值的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="ga069a0709408fef75514dfaf12bc42cb5"></a>

### `hl78xx_api_func_get_sinr_validity()`

```c
int hl78xx_api_func_get_sinr_validity ( const struct device * dev, bool * is_valid )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前信号与干扰加噪声比（SINR）是否达到配置的最低阈值。

使用从 `+KCELLMEAS` 得到的缓存信号与干扰加噪声比（SINR）值，并以 dB 为单位与 `CONFIG_MODEM_MIN_ALLOWED_SINR` 比较。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gae3f2ed904a3b0784d64d2d1537ce9564"></a>

### `hl78xx_api_func_modem_dynamic_cmd_send()`

```c
int hl78xx_api_func_modem_dynamic_cmd_send ( const struct device * dev, const char * cmd, uint16_t cmd_size, const struct modem_chat_match * response_matches, uint16_t matches_size )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

发送动态 AT 命令（Dynamic AT Command），内部实现。

用于向调制解调器发送任意 AT 命令的内部函数。用户应改用 `hl78xx_modem_cmd_send()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `cmd` | 要发送的 AT 命令。 |
| `cmd_size` | AT 命令的大小。 |
| `response_matches` | 预期的响应匹配模式（Response Pattern）。 |
| `matches_size` | 响应匹配模式的数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gad39b680650d8a3f1ea20bc18fa6101d4"></a>

### `hl78xx_api_func_restart()`

```c
int hl78xx_api_func_restart ( const struct device * dev, enum hl78xx_modem_restart_mode mode )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

硬重启（Hard Restart）进入复位引脚状态机路径。软重启（Soft Restart）进入驱动负责的 `AT+CFUN=4,1` 路径，等待调制解调器报告重启指示后，再重新执行初始化。

软重启要求调制解调器的 Chat 路径处于活动状态。如果调制解调器处于睡眠、空闲或关机过渡状态，调用返回 `-EAGAIN`。如果无法发出软复位请求，或者调制解调器始终未报告重启指示，则在具备硬件重启控制的情况下，驱动回退到完整重启路径。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `mode` | 请求的重启模式。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果 `dev` 或 `mode` 无效。 |
| `-ENOTSUP` | 如果请求硬重启，但未配置复位 GPIO。 |
| `-EAGAIN` | 如果请求软重启，但调制解调器尚未准备好接受 AT 命令。 |
| `-EBUSY` | 如果已有另一次重启正在进行。 |

<a id="ga1640ce244f1a4de52efa0b7c33f7b02a"></a>

### `hl78xx_api_func_set_autorat_inhibit()`

```c
int hl78xx_api_func_set_autorat_inhibit ( const struct device * dev, bool inhibit )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

禁止启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

通常，`hl78xx_rat_cfg()` 发现首选无线接入技术列表（Preferred RAT List，PRL）已清空时，会重新应用 `CONFIG_MODEM_HL78XX_AUTORAT_PRL_PROFILES`，并请求重启。主动清空 PRL 的调用者（参见 `HL78XX_KSELACQ_RAT_CLEAR`）必须先设置此抑制标志，否则下次重启会悄然撤销该更改。

该抑制状态不会持久保存：主动清空的 PRL 一经恢复，就应立即清除此标志；否则调制解调器启动后将没有 PRL，且自动 RAT（Auto-RAT）处于关闭状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `inhibit` | `true` 表示抑制恢复，`false` 表示重新允许恢复。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gab8e5ae21bd129d61735c9cfe3df557d2"></a>

### `hl78xx_api_func_set_network_operator_format()`

```c
int hl78xx_api_func_set_network_operator_format ( const struct device * dev, enum hl78xx_operator_format format )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置 `+COPS` 网络运营商格式（Network Operator Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `format` | 要设置的目标运营商格式。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gaab36b1992acffc8b25b8140da1a79577"></a>

### `hl78xx_api_func_set_phone_functionality()`

```c
int hl78xx_api_func_set_phone_functionality ( const struct device * dev, enum hl78xx_phone_functionality functionality, bool reset )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置电话功能模式（Phone Functionality Mode），内部实现。

用于设置调制解调器电话功能模式（Phone Functionality Mode）的内部函数。用户应改用 `hl78xx_set_phone_functionality()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `functionality` | 要设置的电话功能模式。 |
| `reset` | 若为 `true`，则在应用功能变更时同时复位调制解调器。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gafc8c324c2beb2c59c9f15542d06b85ee"></a>

### `hl78xx_api_func_set_prl()`

```c
int hl78xx_api_func_set_prl ( const struct device * dev, const struct kselacq_syntax kselacq_rats )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

通过 `AT+KSELACQ` 设置新的首选无线接入技术列表（Preferred RAT List）。

立即发送 `AT+KSELACQ=0,<rat1>,<rat2>,<rat3>`，更新驱动缓存的 PRL 值，但不强制调制解调器立即重启。

允许重复的无线接入技术（RAT）条目，以影响调制解调器的搜索顺序。若要清除首选无线接入技术列表（Preferred RAT List，PRL）并禁用自动 RAT 切换，请将 `rat1`、`rat2`、`rat3` 都设为 `HL78XX_KSELACQ_RAT_CLEAR`；此时驱动发送 `AT+KSELACQ=0,0`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `kselacq_rats` | 要设置的原始 `AT+KSELACQ` 首选无线接入技术列表（Preferred RAT List，PRL）条目。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负的 `errno` 错误码。

<a id="gad2673b87d730da42b4d2109e849277cc"></a>

### `hl78xx_at_is_busy()`

```c
bool hl78xx_at_is_busy ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

其设计本身存在竞争条件（Race Condition）；参见 `hl78xx_api_func_at_is_busy()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 如果有脚本正在运行，或者 `dev` 无效。 |

<a id="gab08189be0b4dc7f03428d829f0170bbe"></a>

### `hl78xx_at_monitor_pause()`

```c
void hl78xx_at_monitor_pause ( struct hl78xx_at_monitor_entry * mon)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

暂停 AT 监视器（AT Monitor）。

暂停监视器 `mon`，使其不再接收已解析的主动上报 AT 通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 要暂停的监视器。 |

<a id="ga051a63a86e9ca353434b23e1adf5d543"></a>

### `hl78xx_at_monitor_register()`

```c
int hl78xx_at_monitor_register ( struct hl78xx_at_monitor_entry * mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

注册 AT 监视器（AT Monitor）。

将运行时监视器加入已注册 AT 监视器列表。该条目不得已经注册，也不得仍持有上一次注册遗留的运行时引用。

监视器条目首次注册之前应进行零初始化（Zero Initialization）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向要注册的监视器条目的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`mon` 为 `NULL` 时返回 `-EINVAL`；`mon` 已注册时返回 `-EALREADY`；`mon` 仍有未释放的运行时引用时返回 `-EBUSY`；运行时监视器数量已达到上限时返回 `-ENOMEM`。

<a id="ga2723fa7f912913d299629fdba4efb130"></a>

### `hl78xx_at_monitor_resume()`

```c
void hl78xx_at_monitor_resume ( struct hl78xx_at_monitor_entry * mon)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

恢复 AT 监视器（AT Monitor）。

恢复向监视器 `mon` 转发已解析的主动上报 AT 通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 要恢复的监视器。 |

<a id="ga1244a8f6b7e5e488ab596aa5341ad66a"></a>

### `hl78xx_at_monitor_unregister()`

```c
int hl78xx_at_monitor_unregister ( struct hl78xx_at_monitor_entry * mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

注销 AT 监视器（AT Monitor）。

从后续分发快照（Dispatch Snapshot）中移除运行时监视器。本函数不会等待已经在执行的回调，也不会等待已捕获该监视器条目的快照。

如果监视器条目是动态分配的，调用者不得在本函数返回后立即释放或复用它。应在条目中提供释放回调（Release Callback），并在该回调中释放条目。最后一个运行时引用被丢弃后，才会调用释放回调。

可以从监视器回调中调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向要注销的监视器条目的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`mon` 为 `NULL` 时返回 `-EINVAL`；`mon` 未注册时返回 `-ENOENT`。

<a id="ga41d66fc0e8681bf6a68f47af5bcacb90"></a>

### `hl78xx_edrx_get_time_to_sleep()`

```c
int hl78xx_edrx_get_time_to_sleep ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取调制解调器进入扩展非连续接收空闲状态（eDRX Idle State）前的剩余时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 和 `CONFIG_MODEM_HL78XX_EDRX` 时可用。

**返回（Returns）**：返回值：剩余时间，单位为毫秒；失败时返回负的 `errno` 错误码。

<a id="ga9e9d288506708b275cc98e508bc8251d"></a>

### `hl78xx_enter_gnss_mode()`

```c
int hl78xx_enter_gnss_mode ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

进入全球导航卫星系统（GNSS）模式。

将调制解调器从 LTE 模式切换到 GNSS 模式。具体转换过程取决于调制解调器当前的电源状态：

不使用低功耗模式时，即默认／飞行模式路径：

- 关闭载波（Carrier Off）：通知应用并关闭套接字（Socket）。
- 将调制解调器置于飞行模式（`AT+CFUN=4`）。
- 初始化 GNSS 引擎。
- 完成后触发 `HL78XX_GNSS_ENGINE_READY` 事件。

使用低功耗模式时，即省电模式（PSM）路径：

- 将 GNSS 标记为待处理（Pending）。
- 等待调制解调器进入 PSM 睡眠（`PSMEV:1`）。
- 唤醒调制解调器，仅唤醒 UART；LTE 仍保持休眠。
- 初始化 GNSS 引擎；无需 `CFUN=4`，因为射频路径已空闲。
- 完成后触发 `HL78XX_GNSS_ENGINE_READY` 事件。

根据 HL78xx GNSS 应用说明第 5.3 节，“可以在 PSM 模式下使用 GNSS”，因为此时 LTE 调制解调器不可用，共享的射频接收（RF RX）路径处于空闲状态。

进入 GNSS 模式后，调用 `hl78xx_queue_gnss_search()` 开始获取定位结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gadfb6a494068c978908ed0bd968b81a5f"></a>

### `hl78xx_evt_monitor_pause()`

```c
void hl78xx_evt_monitor_pause ( struct hl78xx_evt_monitor_entry * mon)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

暂停监视器（Monitor）。

暂停监视器 `mon` 接收通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 要暂停的监视器。 |

<a id="ga6590e5352cbd8ff6ea0580edd64eb0d0"></a>

### `hl78xx_evt_monitor_register()`

```c
int hl78xx_evt_monitor_register ( struct hl78xx_evt_monitor_entry * mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

注册事件监视器（Event Monitor）。

将运行时监视器加入已注册事件监视器列表。该条目不得已经注册，也不得仍持有上一次注册遗留的运行时引用。

监视器条目首次注册之前应进行零初始化（Zero Initialization）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向要注册的监视器条目的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`mon` 为 `NULL` 时返回 `-EINVAL`；`mon` 已注册时返回 `-EALREADY`；`mon` 仍有未释放的运行时引用时返回 `-EBUSY`；运行时监视器数量已达到上限时返回 `-ENOMEM`。

<a id="gab3a63acd15fc9bd6a7d9ded9ed1731fa"></a>

### `hl78xx_evt_monitor_resume()`

```c
void hl78xx_evt_monitor_resume ( struct hl78xx_evt_monitor_entry * mon)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

恢复监视器（Monitor）。

恢复向监视器 `mon` 转发通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 要恢复的监视器。 |

<a id="gaf4c623e7bed92b6ea3964b59df04e98e"></a>

### `hl78xx_evt_monitor_unregister()`

```c
int hl78xx_evt_monitor_unregister ( struct hl78xx_evt_monitor_entry * mon)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

注销事件监视器（Event Monitor）。

从后续分发快照（Dispatch Snapshot）中移除运行时监视器。本函数不会等待已经在执行的回调，也不会等待已捕获该监视器条目的快照。

如果监视器条目是动态分配的，调用者不得在本函数返回后立即释放或复用它。应在条目中提供释放回调（Release Callback），并在该回调中释放条目。最后一个运行时引用被丢弃后，才会调用释放回调。

可以从监视器回调中调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 指向要注销的监视器条目的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`mon` 为 `NULL` 时返回 `-EINVAL`；`mon` 未注册时返回 `-ENOENT`。

<a id="ga8265e020ad0d8c3e69f2219173530720"></a>

### `hl78xx_evt_notif_handler_set()`

```c
int hl78xx_evt_notif_handler_set ( hl78xx_evt_monitor_dispatcher_t handler)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置 HL78xx 调制解调器事件（Modem Events）的事件通知处理函数（Event Notification Handler）。

注册回调处理函数，以接收 HL78xx 调制解调器的异步事件通知，例如网络注册变化、GNSS 更新或调制解调器生成的其他事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handler` | 事件监视器回调的函数指针。传入 `NULL` 可清除现有处理函数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果 `handler` 参数无效。 |

<a id="ga475545d83cf5fd883fd11fb0db8400ed"></a>

### `hl78xx_exit_gnss_mode()`

```c
int hl78xx_exit_gnss_mode ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

退出全球导航卫星系统（GNSS）模式，返回长期演进（LTE）模式。

将调制解调器从 GNSS 模式切回 LTE 模式。这会执行以下操作：

- 停止任何正在进行的 GNSS 搜索。
- 触发 `HL78XX_GNSS_EVENT_MODE_EXITED` 事件。

事件触发后，下一步取决于电源模式：

- 飞行模式：用户必须调用 `hl78xx_api_func_set_phone_functionality(dev, HL78XX_FULLY_FUNCTIONAL, ...)` 恢复 LTE。
- PSM 模式：驱动自动转回 `AWAIT_REGISTERED`，调制解调器将重新注册到 LTE。低功耗 PSM（LOW-POWER-PSM）模式：用户无需执行任何操作，在 `kcellmeasure` 或套接字数据传输开始后，调制解调器会自动转回 LTE 注册流程。
- 低功耗 PSM（LOW-POWER-PSM）模式：用户无需执行任何操作，在 `kcellmeasure` 或套接字数据传输开始后，调制解调器会自动转回 LTE 注册流程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0；当前不在 GNSS 模式时返回 `-EALREADY`；失败时返回负的 `errno` 错误码。

<a id="gabe520e9e9a5e48ab05e238f6b59b8cda"></a>

### `hl78xx_get_modem_info()`

```c
int hl78xx_get_modem_info ( const struct device * dev, const enum hl78xx_modem_info_type type, void * info, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
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
| `0` | 成功时。 |
| `-ENOTSUP` | 如果蜂窝网络设备不支持该 API。 |
| `-ENODATA` | 如果调制解调器未提供所请求的信息。 |
| `Negative` | 其他情况下返回 Chat 模块的 `errno` 错误码。 |

<a id="gaedfc9112048d6c987ee7fefa4e8abd55"></a>

### `hl78xx_get_network_info()`

```c
int hl78xx_get_network_info ( const struct device * dev, enum hl78xx_network_info_type type, void * info, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取设备缓存的网络信息（Cached Network Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `type` | 请求的网络信息类型。 |
| `info` | 信息的目标缓冲区。 |
| `size` | 目标缓冲区大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | 如果不支持该类型。 |
| `-ENODATA` | 如果调制解调器未提供所请求的信息。 |
| `Negative` | 其他情况下返回 Chat 模块的 `errno` 错误码。 |

<a id="gaf778d092ad7f9b67b0930c0da2375996"></a>

### `hl78xx_get_phone_functionality()`

```c
int hl78xx_get_phone_functionality ( const struct device * dev, enum hl78xx_phone_functionality * functionality )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取调制解调器当前的电话功能模式（Phone Functionality Mode）。

查询调制解调器，获取当前运行模式，例如完整功能（Full Functionality）、飞行模式（Airplane Mode）或最小功能（Minimum Functionality）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `functionality` | 用于保存获取到的功能模式的指针，参见枚举 `hl78xx_phone_functionality`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果输入参数无效。 |
| `-EIO` | 如果调制解调器未响应或返回错误。 |

<a id="ga65f087ad92a0f2bfb15d4f7b627c754f"></a>

### `hl78xx_get_rsrp_validity()`

```c
int hl78xx_get_rsrp_validity ( const struct device * dev, bool * is_valid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前参考信号接收功率（RSRP）是否达到配置的阈值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `Negative` | 失败时返回 `errno` 错误码。 |

<a id="gab49ab6eb5aa0cfcdea4e6e7bcabd1d48"></a>

### `hl78xx_get_rsrq_validity()`

```c
int hl78xx_get_rsrq_validity ( const struct device * dev, bool * is_valid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前参考信号接收质量（RSRQ）是否达到配置的阈值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `Negative` | 失败时返回 `errno` 错误码。 |

<a id="ga06800817986b9a4b0291cc22c808dfae"></a>

### `hl78xx_get_sinr_validity()`

```c
int hl78xx_get_sinr_validity ( const struct device * dev, bool * is_valid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

检查当前信号与干扰加噪声比（SINR）是否达到配置的阈值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `is_valid` | 输出标志，达到阈值时设为 `true`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `Negative` | 失败时返回 `errno` 错误码。 |

<a id="ga452b1ee210417569b3cdfc30db25622a"></a>

### `hl78xx_gnss_assist_data_delete()`

```c
int hl78xx_gnss_assist_data_delete ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

删除辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

使用 `AT+GNSSAD=0` 命令删除调制解调器中保存的所有辅助数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 和 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gabf8fcaa1b5a59d5a2cac3c467f93c9f8"></a>

### `hl78xx_gnss_assist_data_download()`

```c
int hl78xx_gnss_assist_data_download ( const struct device * dev, enum hl78xx_agnss_days days )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

下载辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

使用 `AT+GNSSAD=1,<days>` 命令，开始从网络下载预测辅助数据。需要有效的网络连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `days` | 要下载的预测数据天数。有效值为 1、2、3、7、14、28。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 和 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

**返回（Returns）**：返回值：成功时返回 0；`days` 值无效时返回 `-EINVAL`；失败时返回负的 `errno` 错误码。

<a id="ga473c72484a8a758470ff7043de7ab48d"></a>

### `hl78xx_gnss_assist_data_get_status()`

```c
int hl78xx_gnss_assist_data_get_status ( const struct device * dev, struct hl78xx_agnss_status * status )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取辅助全球导航卫星系统（A-GNSS）的辅助数据状态（Assistance Data Status）。

使用 `AT+GNSSAD?` 命令，查询调制解调器中辅助 GNSS（A-GNSS）辅助数据的有效性和到期情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `status` | 指向用于接收状态的结构的指针。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS` 和 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga0238b9a2de4683369a0be7a6ed481938"></a>

### `hl78xx_gnss_get_latest_known_fix()`

```c
int hl78xx_gnss_get_latest_known_fix ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

从调制解调器获取最新已知的 GNSS 定位结果（Fix）。

使用 `AT+GNSSLOC?` 查询调制解调器最后已知的位置。结果通过 GNSS 数据回调交付。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0；另一脚本正在运行时返回 `-EBUSY`；其他失败情况下返回负的 `errno` 错误码。

<a id="ga209d0579899aef4ade5cf8de1251a323"></a>

### `hl78xx_gnss_get_search_timeout_remaining()`

```c
int hl78xx_gnss_get_search_timeout_remaining ( const struct device * dev, uint32_t * timeout_ms )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

获取剩余的 GNSS 搜索超时（Search Timeout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `timeout_ms` | 指向用于接收剩余超时时间的变量的指针，单位为毫秒。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga5a1949cd23380056b4ee1775b1e6cc3b"></a>

### `hl78xx_gnss_set_nmea_output()`

```c
int hl78xx_gnss_set_nmea_output ( const struct device * dev, enum nmea_output_port port )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置 GNSS 的 NMEA 输出端口（Output Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `port` | NMEA 输出端口配置。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0；GNSS 搜索处于活动状态时返回 `-EBUSY`；失败时返回负的 `errno` 错误码。

<a id="gae349d6b96ef9ae67b5ed01d0a8fa2cb0"></a>

### `hl78xx_gnss_set_search_timeout()`

```c
int hl78xx_gnss_set_search_timeout ( const struct device * dev, uint32_t timeout_ms )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置 GNSS 搜索超时（Search Timeout）。

如果 GNSS 搜索已经处于活动状态，则从本函数调用时刻起，用新值替换剩余超时时间。将 `timeout_ms` 设为 0 可禁用当前搜索的超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |
| `timeout_ms` | 超时时间，单位为毫秒；0 表示不超时。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga3e9edd942cbf32b5a2eec259c44e5ee4"></a>

### `hl78xx_modem_at_cmd()`

```c
int hl78xx_modem_at_cmd ( const struct device * dev, char * response, size_t response_size, const char * cmd )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

发送预先格式化的 AT 命令，并将完整的调制解调器响应（Modem Response）复制到调用者提供的缓冲区。

需要可变参数时，调用者必须先用 `snprintf()` 格式化命令字符串。响应缓冲区接收驱动收集的完整调制解调器响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `response` | 用于接收完整调制解调器响应的输出缓冲区。 |
| `response_size` | 输出缓冲区大小。 |
| `cmd` | 要发送的 AT 命令字符串。 |

**返回（Returns）**：返回值：成功时返回 0；返回正数表示编码后的调制解调器错误；失败时也可能返回负的 `errno` 错误码。

<a id="ga13ead2b7a66530a1fbe15e5c4d9addeb"></a>

### `hl78xx_modem_at_err()`

```c
int hl78xx_modem_at_err ( int error)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

返回编码在 `hl78xx_modem_at_send`／`cmd` 中的调制解调器 CME／CMS 错误码（Error Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `error` | `hl78xx_modem_at_send()` 或 `hl78xx_modem_at_cmd()` 的返回值。 |

**返回（Returns）**：返回值：编码后的调制解调器错误值；对于通用 `ERROR` 响应，返回 0。

<a id="gaba7b5c599c1b9285b9dcfbae91ac5e7f"></a>

### `hl78xx_modem_at_err_type()`

```c
int hl78xx_modem_at_err_type ( int error)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

返回编码在 `hl78xx_modem_at_send`／`cmd` 返回值中的调制解调器错误类型（Modem Error Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `error` | `hl78xx_modem_at_send()` 或 `hl78xx_modem_at_cmd()` 的返回值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `HL78XX_MODEM_AT_ERROR` | 用于 `ERROR` 响应。 |
| `HL78XX_MODEM_AT_CME_ERROR` | 用于 `+CME ERROR` 响应。 |
| `HL78XX_MODEM_AT_CMS_ERROR` | 用于 `+CMS ERROR` 响应。 |

<a id="ga45a97bfc5f73d1877357dc1f410c61cd"></a>

### `hl78xx_modem_at_send()`

```c
int hl78xx_modem_at_send ( const struct device * dev, const char * cmd )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

向调制解调器（Modem）发送预先格式化的 AT 命令。

收到 `OK` 响应时返回 0；收到 `ERROR`／`+CME ERROR`／`+CMS ERROR` 响应时返回编码后的正数调制解调器错误；传输失败时返回负的 `errno` 错误码。需要可变参数时，调用者必须先用 `snprintf()` 格式化命令字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `cmd` | 要发送的 AT 命令字符串。 |

**返回（Returns）**：返回值：成功时返回 0；返回正数表示编码后的调制解调器错误；失败时也可能返回负的 `errno` 错误码。

<a id="gae7102c14fda882e87bff0f0828ab4263"></a>

### `hl78xx_modem_cmd_send()`

```c
int hl78xx_modem_cmd_send ( const struct device * dev, const char * cmd, uint16_t cmd_size, const struct modem_chat_match * response_matches, uint16_t matches_size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

向调制解调器（Modem）发送 AT 命令，并等待匹配的响应（Matched Response）。

向调制解调器发送指定的 AT 命令，并等待与响应匹配表中某个预期模式匹配的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `cmd` | 指向待发送 AT 命令字符串的指针。 |
| `cmd_size` | AT 命令字符串的长度，单位为字节。 |
| `response_matches` | 指向预期响应模式数组的指针，参见结构 `modem_chat_match`。 |
| `matches_size` | 数组中的响应模式数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 命令发送成功且响应匹配时。 |
| `-EINVAL` | 任一参数无效时。 |
| `-ETIMEDOUT` | 如果调制解调器未在预期时间内响应。 |
| `-EIO` | 通信失败或响应不匹配时。 |

<a id="ga8abfb51de22c24f1870d2b5f4b3b60ee"></a>

### `hl78xx_parse_rsrp()`

```c
int hl78xx_parse_rsrp ( uint8_t rsrp, int16_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器提供的原始参考信号接收功率（RSRP）值转换为 dBm。

解析调制解调器报告的参考信号接收功率（Reference Signal Received Power，RSRP）值，并将其转换为对应的 dBm 信号强度，通常依据 3GPP TS 36.133 规范。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rsrp` | 原始 RSRP 值，通常范围为 0–97；未知时为 255。 |
| `value` | 用于保存转换后的 RSRP 值的指针，单位为 dBm。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 转换成功时。 |
| `-EINVAL` | 如果 RSRP 值超出范围或表示未知值。 |

<a id="ga09f7b39a934d38a2d3da8deefc3d2758"></a>

### `hl78xx_parse_rsrq()`

```c
int hl78xx_parse_rsrq ( uint8_t rsrq, int16_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器提供的原始参考信号接收质量（RSRQ）值转换为 dB。

解析调制解调器提供的参考信号接收质量（Reference Signal Received Quality，RSRQ）值，并按照 3GPP TS 36.133 将其转换为以分贝（dB）表示的信号质量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rsrq` | 原始 RSRQ 值，通常范围为 0–34；未知时为 255。 |
| `value` | 用于保存转换后的 RSRQ 值的指针，单位为 dB。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 转换成功时。 |
| `-EINVAL` | 如果 RSRQ 值超出有效范围或表示未知。 |

<a id="ga9dd8be5c6d35de4122ab5604bf5b17ce"></a>

### `hl78xx_parse_rssi()`

```c
int hl78xx_parse_rssi ( uint8_t rssi, int16_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器提供的原始接收信号强度指示（RSSI）值转换为 dBm。

解析调制解调器报告的接收信号强度指示（RSSI）值，通常来自 AT 命令响应，并按照 3GPP TS 27.007 将其转换为对应的 dBm 信号强度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rssi` | 原始 RSSI 值，范围为 0–31；未知或无法检测时为 99。 |
| `value` | 用于保存转换后的 RSSI 值的指针，单位为 dBm。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 转换成功时。 |
| `-EINVAL` | 如果 RSSI 值超出有效范围或不受支持。 |

<a id="ga98af31968e3bf0fc72dea5d56e97e122"></a>

### `hl78xx_power_down_cancel()`

```c
int hl78xx_power_down_cancel ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

取消待处理的 HL78xx 第一阶段关机定时器（Stage-1 Shutdown Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 HL78xx 调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

**返回（Returns）**：返回值：成功时返回 0；参数无效时返回 `-EINVAL`；没有待执行的第一阶段关机计时器时返回 `-ENOENT`。

<a id="ga2bcaada6a58dfbe3658fc6bcb3090fff"></a>

### `hl78xx_power_down_confirm()`

```c
void hl78xx_power_down_confirm ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

确认应用程序清理（Application Cleanup）已完成，调制解调器可以继续执行物理关机（Physical Shutdown）。

如果没有待执行的关机，此调用不执行任何操作（No-op）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 HL78xx 调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

<a id="ga249a5bf6cdbd69ec930724bf2541de72"></a>

### `hl78xx_power_down_respond()`

```c
int hl78xx_power_down_respond ( const struct device * dev, enum hl78xx_power_down_response response, uint32_t timeout_s )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

响应待处理的 HL78XX 掉电更新（Power-down Update）。

收到带有 `POWER_DOWN_EVENT_ENTER` 的 `HL78XX_POWER_DOWN_UPDATE` 后调用此函数。使用 `HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE` 可允许调制解调器立即继续执行物理关机；使用 `HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE` 可将关机宽限期延长到本次调用时刻之后 `timeout_s` 秒。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 HL78xx 调制解调器设备的指针。 |
| `response` | 请求对待执行关机采取的处理方式。 |
| `timeout_s` | `response` 为 `HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE` 时，表示新的宽限期，单位为秒；其他情况下忽略。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

**返回（Returns）**：返回值：成功时返回 0；参数无效时返回 `-EINVAL`；没有待执行的应用控制关机时返回 `-ENOENT`。

<a id="gac7291340f8699bb37cd864516615ea05"></a>

### `hl78xx_power_down_trigger()`

```c
int hl78xx_power_down_trigger ( const struct device * dev, k_timeout_t delay )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

经过调用者提供的延迟后，触发 HL78xx 关机流程（Shutdown Process）。

这会覆盖当前任何待执行的第一阶段关断延迟。传入 `K_NO_WAIT` 可立即分发 `HL78XX_POWER_DOWN_UPDATE`；也可传入 `K_SECONDS(5)` 等相对延迟，以便稍后开始正常关机流程（Graceful Shutdown）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 HL78xx 调制解调器设备的指针。 |
| `delay` | 执行第一阶段关断通知前的延迟。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

**返回（Returns）**：返回值：成功时返回 0，参数无效时返回 `-EINVAL`。

<a id="ga48f504b9bb41d4a13ac592f763aeb207"></a>

### `hl78xx_queue_gnss_search()`

```c
int hl78xx_queue_gnss_search ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将 GNSS 位置搜索（Position Search）加入队列。

启动 GNSS 卫星搜索以获取定位结果（Position Fix）。必须在 `hl78xx_enter_gnss_mode()` 之后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向全球导航卫星系统（GNSS）设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaf8cbf3de84df41d7066b9a07f106c17b"></a>

### `hl78xx_rat_to_access_tech()`

```c
enum cellular_access_technology hl78xx_rat_to_access_tech ( enum hl78xx_cell_rat_mode rat_mode)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将 HL78xx 无线接入技术模式（RAT Mode）转换为标准蜂窝 API（Cellular API）表示。

将 HL78xx 专用的无线接入技术（RAT）枚举映射为标准 Zephyr 蜂窝 API 的接入技术枚举。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rat_mode` | HL78xx 无线接入技术（RAT）模式。 |

**返回（Returns）**：返回值：对应的 `cellular_access_technology` 值。

<a id="ga2c4ff4a9b1d5d2530700327e1d4af6e0"></a>

### `hl78xx_restart_modem()`

```c
int hl78xx_restart_modem ( const struct device * dev, enum hl78xx_modem_restart_mode mode )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `mode` | 要执行的重启模式。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `Negative` | 失败时返回 `errno` 错误码。 |

<a id="ga9bac621e2f74d598329f61cd95b0291b"></a>

### `hl78xx_set_active_sim()`

```c
int hl78xx_set_active_sim ( const struct device * dev, enum hl78xx_sim_slot sim_slot )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

选择活动的外部 SIM 卡槽（Active External SIM Slot）。

这仅驱动调制解调器设备树节点提供的可选 `mdm-sim-switch-gpios` 信号线，不执行任何调制解调器状态转换或重启序列。因此，调用者仅应在调制解调器处于对所连接硬件安全的状态时切换 SIM。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |
| `sim_slot` | 要选择的 SIM 卡槽，仅支持卡槽 1 和卡槽 2。 |

**返回（Returns）**：返回值：成功时返回 0；`dev` 或 `sim_slot` 无效时返回 `-EINVAL`；设备树中未配置调制解调器 SIM 切换 GPIO 时返回 `-ENOTSUP`；失败时返回 GPIO 驱动给出的负 `errno` 错误码。

<a id="gaad6374b5c5ef64886c6d8fdde0cba3c4"></a>

### `hl78xx_set_autorat_inhibit()`

```c
int hl78xx_set_autorat_inhibit ( const struct device * dev, bool inhibit )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

禁止或允许启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `inhibit` | `true` 表示抑制恢复，`false` 表示重新允许恢复。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果输入无效。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

<a id="gaee99182459b5971ebaa7892989b0e8df"></a>

### `hl78xx_set_phone_functionality()`

```c
int hl78xx_set_phone_functionality ( const struct device * dev, enum hl78xx_phone_functionality functionality, bool reset )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置调制解调器的电话功能模式（Phone Functionality Mode）。

配置调制解调器的运行状态，例如完整功能（Full Functionality）、飞行模式（Airplane Mode）或最小功能（Minimum Functionality）。也可选择在此转换期间复位调制解调器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `functionality` | 要设置的目标电话功能模式，例如完整功能、飞行模式或最小功能；参见枚举 `hl78xx_phone_functionality`。 |
| `reset` | 若为 `true`，则在应用功能变更时同时复位调制解调器。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果传入无效参数。 |
| `-EIO` | 与调制解调器通信失败或命令失败时。 |

<a id="gad564df9a12ad4ee40caeffec1099a93b"></a>

### `hl78xx_set_prl()`

```c
int hl78xx_set_prl ( const struct device * dev, struct kselacq_syntax prl )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

设置新的原始 `AT+KSELACQ` 首选无线接入技术列表（Preferred RAT List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备实例的指针。 |
| `prl` | 以原始 `AT+KSELACQ` 值表示的首选无线接入技术列表（Preferred RAT List，PRL）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 如果输入无效。 |
| `Negative` | 调制解调器命令失败时返回 `errno` 错误码。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_AUTORAT` 时可用。

<a id="gac6ed6d4f41003cb2517f802762d5b239"></a>

### `hl78xx_set_runtime_band_provider()`

```c
int hl78xx_set_runtime_band_provider ( const struct device * dev, hl78xx_runtime_band_provider_t provider, void * user_data )
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

为驱动注册或清除运行时频段提供器（Runtime Band Provider）。

注册提供者（Provider）后，`hl78xx_band_cfg()` 可以使用其针对各无线接入技术（RAT）的频段覆盖值，替代默认的 Kconfig 位图。传入 `NULL` 可清除提供者。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 蜂窝网络设备实例（Cellular Network Device Instance）。 |
| `provider` | 用于获取运行时频段覆盖值的回调。 |
| `user_data` | 回传给提供者（Provider）的不透明上下文（Opaque Context）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gae3e97cdf80470496d6d8542f61f985c0"></a>

### `hl78xx_set_wake_pin_high()`

```c
int hl78xx_set_wake_pin_high ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器的 `WAKE` 引脚驱动为高电平（High）。

这直接对应驱动内部的 `gpio_pin_set_dt(&config->mdm_gpio_wake, 1)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`dev` 无效时返回 `-EINVAL`；设备树中未配置调制解调器 WAKE GPIO 时返回 `-ENOTSUP`；失败时返回 GPIO 驱动给出的负 `errno` 错误码。

<a id="ga803bf7a13a7b57477dbfa4d6b3faa14e"></a>

### `hl78xx_set_wake_pin_low()`

```c
int hl78xx_set_wake_pin_low ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器的 `WAKE` 引脚驱动为低电平（Low）。

这直接对应驱动内部的 `gpio_pin_set_dt(&config->mdm_gpio_wake, 0)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`dev` 无效时返回 `-EINVAL`；设备树中未配置调制解调器 WAKE GPIO 时返回 `-ENOTSUP`；失败时返回 GPIO 驱动给出的负 `errno` 错误码。

<a id="gaf34ed3d29904f1a18c0c75a0de4bc727"></a>

### `hl78xx_start_airvantage_dm_session()`

```c
int hl78xx_start_airvantage_dm_session ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

启动 AirVantage 设备管理（Device Management，DM）会话。

发起到 Sierra Wireless AirVantage 服务器的连接，以执行设备管理（Device Management）操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_AIRVANTAGE`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga9018c8332803eaada4083390c40ac3f0"></a>

### `hl78xx_stop_airvantage_dm_session()`

```c
int hl78xx_stop_airvantage_dm_session ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

停止 AirVantage 设备管理（Device Management，DM）会话。

终止当前到 AirVantage 服务器的连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_AIRVANTAGE`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga7cc4861b1449b551246204b84779c621"></a>

### `hl78xx_wakeup_modem()`

```c
int hl78xx_wakeup_modem ( const struct device * dev)
```

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

将调制解调器从省电模式（PSM）睡眠中唤醒。

向调制解调器发送唤醒信号，触发驱动状态机中的 `RESUME` 事件。调制解调器将重新打开 UART 总线，随后进入 GNSS 流程（若在 PSM 后模式中存在待处理的 GNSS 请求），或者进入 LTE 注册流程（`AWAIT_REGISTERED`）。

这是面向用户的 PSM 后（POST-PSM）GNSS 工作流程 API：

- `hl78xx_enter_gnss_mode()`：将 GNSS 请求加入队列，调制解调器进入 PSM。
- 调制解调器睡眠，等待用户触发。
- `hl78xx_wakeup_modem()`：唤醒调制解调器，先运行 GNSS，再运行 LTE。
- GNSS 完成，调制解调器返回 LTE 注册流程。

也可独立于 GNSS 使用，为任意目的唤醒调制解调器，例如在下一个 PSM 周期之前提前发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向调制解调器设备的指针。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE` 时可用。

**返回（Returns）**：返回值：成功时返回 0；调制解调器不在睡眠状态时返回 `-EALREADY`；`dev` 无效时返回 `-EINVAL`。


## 1.8\_原页交叉引用（Cross References）

- [hl78xx_apis.h](../api_file_modem_network_reference/P001_zephyr__drivers__modem__hl78xx_apis.h_文件参考.md)
- [kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)
- [hl78xx_cxreg_status](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md)
- [hl78xx_network_operator](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md)
- [hl78xx_network_info](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md)
- [hl78xx_agnss_status](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md)
- [k_cellmeas_signal_info](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md)
- [hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)
- [hl78xx_ctzeu_update](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md)
- [hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)
- [nmea_match_gsa_data](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md)
- [nmea_match_gst_data](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md)
- [nmea_match_epu_data](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md)
- [hl78xx_gnss_nmea_aux_data](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md)
- [hl78xx_gnss_aux_data_callback](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md)
- [hl78xx_at_notification](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md)
- [hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)
- [hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)
- [cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)
- [cellular_registration_status](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga7309390ed507748fdb72cf078b8e08a4)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [DT_DEP_ORD](../dt_node_reference/P004_设备树依赖顺序宏.md#ga5b96dccfd349dd0ddba1812aa942c1bd)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [IS_EMPTY](../util_reference/P001_通用工具公共接口.md#gab9487eea703d51cb1f235432dab4a1c7)
- [CONFIG_HL78XX_GNSS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS)
- [CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE)
- [CONFIG_MODEM_HL78XX_12](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_12)
- [CONFIG_MODEM_HL78XX_12_FW_R6](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_12_FW_R6)
- [CONFIG_MODEM_HL78XX_AUTORAT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AUTORAT)
- [CONFIG_MODEM_HL78XX_EDRX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_EDRX)
- [CONFIG_MODEM_HL78XX_LOW_POWER_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)
- [CONFIG_MODEM_HL78XX_PSM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_PSM)
- [CONFIG_MODEM_HL78XX_POWER_DOWN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_POWER_DOWN)
- [CONFIG_MODEM_HL78XX_AIRVANTAGE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AIRVANTAGE)
- [EAGAIN](../error_reference/P003_系统错误号公共接口.md#gaf0fac1cea1165b4debec7f686edf3313)
- [snprintf()](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a8524c494bbe2f2e686d35c3bd7ca4f2a)
- [K_SECONDS(5)](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructhl78xx__gnss__aux__data__callback_html"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-dep-ord_html_ga5b96dccfd349dd0ddba1812aa942c1bd"></a>
<a id="agroup__hl78xx__interface_html_gabe2427817d9dea113ac5f748b9148357"></a>
<a id="astructhl78xx__at__monitor__entry_html"></a>
<a id="astructhl78xx__evt__monitor__entry_html"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__sys-util_html_gab9487eea703d51cb1f235432dab4a1c7"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d"></a>
<a id="gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306"></a>
<a id="gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8"></a>
<a id="gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407"></a>
<a id="gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816"></a>
<a id="ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459"></a>
<a id="gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288"></a>
<a id="gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d"></a>
<a id="gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b"></a>
<a id="gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e"></a>
<a id="gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d"></a>
<a id="gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d"></a>
<a id="gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b"></a>
<a id="gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f"></a>
<a id="gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422"></a>
<a id="gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8"></a>
<a id="gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5"></a>
<a id="gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a"></a>
<a id="gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e"></a>
<a id="gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254"></a>
<a id="gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790"></a>
<a id="gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21"></a>
<a id="gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740"></a>
<a id="gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da"></a>
<a id="gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533"></a>
<a id="ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850"></a>
<a id="ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f"></a>
<a id="ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca"></a>
<a id="ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30"></a>
<a id="ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8"></a>
<a id="ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd"></a>
<a id="ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca"></a>
<a id="gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc"></a>
<a id="gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6"></a>
<a id="ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc"></a>
<a id="gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48"></a>
<a id="gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c"></a>
<a id="gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164"></a>
<a id="gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9"></a>
<a id="gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf"></a>
<a id="gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba"></a>
<a id="gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570"></a>
<a id="gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a"></a>
<a id="gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985"></a>
<a id="gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e"></a>
<a id="ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94"></a>
<a id="ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda"></a>
<a id="ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553"></a>
<a id="gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576"></a>
<a id="gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d"></a>
<a id="ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1"></a>
<a id="gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa"></a>
<a id="gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1"></a>
<a id="gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0"></a>
<a id="gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md)
