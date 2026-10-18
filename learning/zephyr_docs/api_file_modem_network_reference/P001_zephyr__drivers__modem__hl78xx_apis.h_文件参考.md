---
id: learning.zephyr-docs.api-file-modem-network-reference.page-1
title: zephyr__drivers__modem__hl78xx_apis.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_modem\_\_hl78xx\_apis.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HL78xx调制解调器（Modems）扩展蜂窝通信API的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <errno.h>
#include <stddef.h>
#include <stdint.h>
#include <time.h>
#include <zephyr/drivers/cellular.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

HL78xx调制解调器（Modems）扩展蜂窝通信API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga8c28a5a32edb83ea0b0120dd3b00451f"></a>

```c
#define CSQ_RSSI_UNKNOWN (99)
```

相关声明：[CSQ_RSSI_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8c28a5a32edb83ea0b0120dd3b00451f)。

`AT+CSQ` 命令返回的未知接收信号强度指示（RSSI）值。

<a id="r_gab2c8054a088aa6927aa10f1aed1587ae"></a>

```c
#define CSQ_RSSI_MAX (31)
```

相关声明：[CSQ_RSSI_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab2c8054a088aa6927aa10f1aed1587ae)。

`AT+CSQ` 命令返回的最大有效接收信号强度指示（RSSI）编码。

<a id="r_ga03c48d45ba1dfcdeabba881f2b1cd936"></a>

```c
#define CESQ_RSRP_UNKNOWN (255)
```

相关声明：[CESQ_RSRP_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03c48d45ba1dfcdeabba881f2b1cd936)。

`AT+CESQ` 命令返回的未知参考信号接收功率（RSRP）值。

<a id="r_gacb02197961c70e98147ae25e4c11d4de"></a>

```c
#define CESQ_RSRP_MAX (97)
```

相关声明：[CESQ_RSRP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacb02197961c70e98147ae25e4c11d4de)。

`AT+CESQ` 命令返回的最大有效参考信号接收功率（RSRP）编码。

<a id="r_ga9a4429e44439c5ebdd18ccd549f832f5"></a>

```c
#define CESQ_RSRQ_UNKNOWN (255)
```

相关声明：[CESQ_RSRQ_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9a4429e44439c5ebdd18ccd549f832f5)。

`AT+CESQ` 命令返回的未知参考信号接收质量（RSRQ）值。

<a id="r_ga7d02276973c71eded42d4242a34ca745"></a>

```c
#define CESQ_RSRQ_MAX (34)
```

相关声明：[CESQ_RSRQ_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d02276973c71eded42d4242a34ca745)。

`AT+CESQ` 命令返回的最大有效参考信号接收质量（RSRQ）编码。

<a id="r_gac53a8b20d353944744e259f1f9008d44"></a>

```c
#define HL78XX_MODEM_AT_ERROR 1
```

相关声明：[HL78XX_MODEM_AT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac53a8b20d353944744e259f1f9008d44)。

公共 AT 辅助函数返回通用 `ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga23bb6b58819d70eb379f89a3878c07d0"></a>

```c
#define HL78XX_MODEM_AT_CME_ERROR 2
```

相关声明：[HL78XX_MODEM_AT_CME_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga23bb6b58819d70eb379f89a3878c07d0)。

公共 AT 辅助函数返回 `+CME ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga0fef7f6b540d959bf391ac39d8c2738a"></a>

```c
#define HL78XX_MODEM_AT_CMS_ERROR 3
```

相关声明：[HL78XX_MODEM_AT_CMS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0fef7f6b540d959bf391ac39d8c2738a)。

公共 AT 辅助函数返回 `+CMS ERROR` 响应时使用的调制解调器响应类型（Modem Response Type）。

<a id="r_ga72dfe852d4d6365d80f33b918f631501"></a>

```c
#define CSQ_RSSI_TO_DB(v)
```

相关声明：[CSQ_RSSI_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga72dfe852d4d6365d80f33b918f631501)。

将 CSQ 接收信号强度指示（RSSI）值转换为 dBm。

<a id="r_ga309cc2c1be1d4006e2ccb8d59cb3e916"></a>

```c
#define CESQ_RSRP_TO_DB(v)
```

相关声明：[CESQ_RSRP_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga309cc2c1be1d4006e2ccb8d59cb3e916)。

将 CESQ 参考信号接收功率（RSRP）值转换为 dBm。

<a id="r_ga536c21c42099fc04ac85a634ffa41d24"></a>

```c
#define CESQ_RSRQ_TO_DB(v)
```

相关声明：[CESQ_RSRQ_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga536c21c42099fc04ac85a634ffa41d24)。

将 CESQ 参考信号接收质量（RSRQ）值转换为 dB。

<a id="r_ga734b46dfd78fbf6fc938a6f9115f2cc7"></a>

```c
#define PAUSED 1
```

相关声明：[PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga734b46dfd78fbf6fc938a6f9115f2cc7)。

监视器已暂停。

<a id="r_ga3a6d3cd70078e6046471ec528a09cd19"></a>

```c
#define ACTIVE 0
```

相关声明：[ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga3a6d3cd70078e6046471ec528a09cd19)。

监视器（Monitor）处于活动状态，默认值。

<a id="r_ga9587840c88858d1c26bd3afedd96bd68"></a>

```c
#define MDM_MANUFACTURER_LENGTH 20
```

相关声明：[MDM_MANUFACTURER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9587840c88858d1c26bd3afedd96bd68)。

调制解调器制造商字符串（Modem Manufacturer String）的最大长度。

<a id="r_ga694436b7ecedfd934f78afa9f404cadb"></a>

```c
#define MDM_MODEL_LENGTH 32
```

相关声明：[MDM_MODEL_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga694436b7ecedfd934f78afa9f404cadb)。

调制解调器型号字符串（Modem Model String）的最大长度。

<a id="r_ga6327f0d9596ad616f844687ac0fbc4f9"></a>

```c
#define MDM_REVISION_LENGTH 64
```

相关声明：[MDM_REVISION_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6327f0d9596ad616f844687ac0fbc4f9)。

调制解调器修订版本字符串（Modem Revision String）的最大长度。

<a id="r_ga9213ea6a80a1f80b10ade16314fa56dd"></a>

```c
#define MDM_IMEI_LENGTH 16
```

相关声明：[MDM_IMEI_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9213ea6a80a1f80b10ade16314fa56dd)。

调制解调器国际移动设备识别码（IMEI）字符串的最大长度。

<a id="r_ga9c11717136907c549f2ddb5c9bab48b7"></a>

```c
#define MDM_IMSI_LENGTH 23
```

相关声明：[MDM_IMSI_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9c11717136907c549f2ddb5c9bab48b7)。

调制解调器国际移动用户识别码（IMSI）字符串的最大长度。

<a id="r_gaa14eef37d2beacdb02a50ec4eb93d1fd"></a>

```c
#define MDM_ICCID_LENGTH 22
```

相关声明：[MDM_ICCID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa14eef37d2beacdb02a50ec4eb93d1fd)。

调制解调器集成电路卡识别码（ICCID）字符串的最大长度。

<a id="r_ga2586187555aed092ffbf40e7991cc266"></a>

```c
#define MDM_APN_MAX_LENGTH 64
```

相关声明：[MDM_APN_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2586187555aed092ffbf40e7991cc266)。

接入点名称（APN）字符串的最大长度。

<a id="r_ga0a99d20ad7b62fd41c0118e2f5af522b"></a>

```c
#define MDM_MAX_CERT_LENGTH 4096
```

相关声明：[MDM_MAX_CERT_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0a99d20ad7b62fd41c0118e2f5af522b)。

证书（Certificate）的最大长度。

<a id="r_gaad7153fc809f017cd727bc60988fd799"></a>

```c
#define MDM_MAX_HOSTNAME_LEN 128
```

相关声明：[MDM_MAX_HOSTNAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaad7153fc809f017cd727bc60988fd799)。

主机名（Hostname）的最大长度。

<a id="r_gae2d73fc3652b58cc2d2b8bfb72f6e86d"></a>

```c
#define MDM_SERIAL_NUMBER_LENGTH 32
```

相关声明：[MDM_SERIAL_NUMBER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae2d73fc3652b58cc2d2b8bfb72f6e86d)。

序列号字符串（Serial Number String）的最大长度。

<a id="r_gaea97e8a895c9bad91eead2e631934bda"></a>

```c
#define HL78XX_CTZEU_UTIME_MAX_LEN 32
```

相关声明：[HL78XX_CTZEU_UTIME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaea97e8a895c9bad91eead2e631934bda)。

用于提取出的 `+CTZEU` 通用时间字符串（Universal Time Strings）的推荐缓冲区大小。

<a id="r_ga0d3e4dcb509b56886297f2f451f4d952"></a>

```c
#define HL78XX_CEREG_TIMER_STR_LEN 9
```

相关声明：[HL78XX_CEREG_TIMER_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0d3e4dcb509b56886297f2f451f4d952)。

CEREG 定时器字符串（Timer String）的最大长度。

<a id="r_ga1dd356d88b67261a642ba50730b31b48"></a>

```c
#define HL78XX_NETWORK_ADDRESS_MAX_LEN 46
```

相关声明：[HL78XX_NETWORK_ADDRESS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1dd356d88b67261a642ba50730b31b48)。

网络地址字符串（Network Address String）的最大长度。

<a id="r_ga8bc5d49dd46c8bff682528127310a1eb"></a>

```c
#define MDM_HL78XX_EOF_PATTERN "--EOF--Pattern--"
```

相关声明：[MDM_HL78XX_EOF_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8bc5d49dd46c8bff682528127310a1eb)。

用于指示文件结束（End-of-file）或数据传输完成（Completion of Data Transmission）的模式。

<a id="r_ga00e8685b8a1c0b4a9b5ba18dfdd7c879"></a>

```c
#define MDM_HL78XX_TERMINATION_PATTERN "+++"
```

相关声明：[MDM_HL78XX_TERMINATION_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga00e8685b8a1c0b4a9b5ba18dfdd7c879)。

用于退出数据模式（Data Mode）、返回命令模式（Command Mode）的转义／终止序列（Escape/Termination Sequence）。

<a id="r_gab53f7ed6e7b4b70f7675184e666bf9f0"></a>

```c
#define MDM_HL78XX_CONNECT_STRING "CONNECT"
```

相关声明：[MDM_HL78XX_CONNECT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab53f7ed6e7b4b70f7675184e666bf9f0)。

表示已成功建立数据连接（Data Connection）的响应字符串。

<a id="r_gae2b96cddac89ab608658fe11bfdac45e"></a>

```c
#define MDM_HL78XX_NO_CARRIER_STRING "NO CARRIER"
```

相关声明：[MDM_HL78XX_NO_CARRIER_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae2b96cddac89ab608658fe11bfdac45e)。

表示连接已丢失或终止（Lost or Terminated）的响应字符串。

<a id="r_ga1760f6b6b71f238b2e4a4f2082899dd7"></a>

```c
#define MDM_HL78XX_CME_ERROR_STRING "+CME ERROR: "
```

相关声明：[MDM_HL78XX_CME_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1760f6b6b71f238b2e4a4f2082899dd7)。

移动设备（Mobile Equipment，CME）错误响应的前缀，通常后跟错误码（Error Code）。

<a id="r_ga65d332f108a5cbc6e3038db4fa2fee65"></a>

```c
#define MDM_HL78XX_CMS_ERROR_STRING "+CMS ERROR: "
```

相关声明：[MDM_HL78XX_CMS_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga65d332f108a5cbc6e3038db4fa2fee65)。

消息服务（Message Service，CMS）错误响应的前缀，通常与短信（SMS）操作相关。

<a id="r_gac06ec76b0de379682110e590c4b400de"></a>

```c
#define MDM_HL78XX_ERROR_STRING "ERROR"
```

相关声明：[MDM_HL78XX_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac06ec76b0de379682110e590c4b400de)。

表示命令失败（Command Failure）的通用错误响应字符串。

<a id="r_ga08eaa30cab6c59b2b4e9e33ff8c12704"></a>

```c
#define MDM_HL78XX_OK_STRING "OK"
```

相关声明：[MDM_HL78XX_OK_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga08eaa30cab6c59b2b4e9e33ff8c12704)。

表示 AT 命令成功执行（Successful Execution）的标准响应字符串。

<a id="r_ga6b0f0f61bd70c9e09031ecdb9dcf2f52"></a>

```c
#define MDM_HL78XX_DESIRED_VERSION_STRING
```

相关声明：[MDM_HL78XX_DESIRED_VERSION_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6b0f0f61bd70c9e09031ecdb9dcf2f52)。

期望的固件版本字符串（Firmware Version String）。

<a id="r_ga0381c6c5a47121b422c0f5d456e86432"></a>

```c
#define HL78XX_MONITOR_ACTIVE false
```

相关声明：[HL78XX_MONITOR_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0381c6c5a47121b422c0f5d456e86432)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

HL78xx 监视器（Monitor）的初始活动状态（Active State）。

<a id="r_gac485491202b429e8512c210360d1b2f9"></a>

```c
#define HL78XX_MONITOR_PAUSED true
```

相关声明：[HL78XX_MONITOR_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac485491202b429e8512c210360d1b2f9)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

HL78xx 监视器（Monitor）的初始暂停状态（Paused State）。

<a id="r_gabe2427817d9dea113ac5f748b9148357"></a>

```c
#define HL78XX_MONITOR_INITIAL_PAUSED(...)
```

相关声明：[HL78XX_MONITOR_INITIAL_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabe2427817d9dea113ac5f748b9148357)。

解析可选的监视器初始状态参数（Monitor Initial State Argument）。

<a id="r_gaa23bb8ced0d5b912309228525736234a"></a>

```c
#define HL78XX_EVT_MONITOR(name, _handler, ...)
```

相关声明：[HL78XX_EVT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa23bb8ced0d5b912309228525736234a)。

定义事件监视器（Event Monitor），在系统工作队列线程（System Workqueue Thread）中接收通知。

<a id="r_ga48b0f02ea31d612d867db6bf2a62fb46"></a>

```c
#define HL78XX_AT_MONITOR_ANY NULL
```

相关声明：[HL78XX_AT_MONITOR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga48b0f02ea31d612d867db6bf2a62fb46)。

监视任何已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_gadc4cc789837650b5e20e9bf5f6d85067"></a>

```c
#define HL78XX_AT_MONITOR(name, _filter, _handler, ...)
```

相关声明：[HL78XX_AT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadc4cc789837650b5e20e9bf5f6d85067)。

定义 AT 监视器（AT Monitor），在系统工作队列线程（System Workqueue Thread）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_ga370b450dc0ab247343d3406e7fc664da"></a>

```c
#define HL78XX_AT_MONITOR_DIRECT(name, _filter, _handler, ...)
```

相关声明：[HL78XX_AT_MONITOR_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga370b450dc0ab247343d3406e7fc664da)。

定义 AT 监视器（AT Monitor），直接在 HL78xx 调制解调器接收工作队列上下文（RX Workqueue Context）中接收已解析的主动上报 AT 通知（Unsolicited AT Notification）。

<a id="r_ga7da0c70a3435693c416c28a27b4ab1c5"></a>

```c
#define GNSS_AUX_DATA_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_AUX_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7da0c70a3435693c416c28a27b4ab1c5)。

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

<a id="r_gab77a5c59a2b5297b7bc69afffb21dc73"></a>

```c
#define GNSS_DT_AUX_DATA_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_AUX_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab77a5c59a2b5297b7bc69afffb21dc73)。

注册回调结构体（Callback Structure），接收发布的全球导航卫星系统（GNSS）辅助数据。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga82793d1f4c0c8f03ae27b29afa1c3d3f"></a>

```c
typedef bool(* hl78xx_runtime_band_provider_t) (const struct device *dev, enum hl78xx_cell_rat_mode rat, uint16_t *band, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_runtime_band_provider_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga82793d1f4c0c8f03ae27b29afa1c3d3f)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于为无线接入技术（RAT）提供可选运行时频段覆盖设置（Runtime Band Override）的回调。

<a id="r_ga9198bafcc7c78243fc72ca2b0bc926ed"></a>

```c
typedef void(* hl78xx_gnss_aux_data_callback_t) (const struct device *dev, const struct hl78xx_gnss_nmea_aux_data *aux_data, uint16_t size)
```

相关声明：[hl78xx_gnss_aux_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9198bafcc7c78243fc72ca2b0bc926ed)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_gnss_nmea_aux_data](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

全球导航卫星系统（GNSS）辅助数据回调的函数类型（Callback Function Type）。

<a id="r_ga03910e4575bfd4ed439e1c9a0220c7a2"></a>

```c
typedef int(* hl78xx_api_configure_networks) (const struct device *dev, const struct hl78xx_network *networks, uint8_t size)
```

相关声明：[hl78xx_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03910e4575bfd4ed439e1c9a0220c7a2)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于配置网络（Networks）的 API 函数指针。

<a id="r_ga6bf75bd8e583b4e076b73268a712977d"></a>

```c
typedef int(* hl78xx_api_get_supported_networks) (const struct device *dev, const struct hl78xx_network **networks, uint8_t *size)
```

相关声明：[hl78xx_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6bf75bd8e583b4e076b73268a712977d)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于获取支持的网络（Supported Networks）的 API 函数指针。

<a id="r_ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a"></a>

```c
typedef int(* hl78xx_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[hl78xx_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

用于获取网络信号强度（signal strength）的 API。

<a id="r_gaa7cb75a0ef3cd4cb607bb0e3f3b3468f"></a>

```c
typedef int(* hl78xx_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[hl78xx_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa7cb75a0ef3cd4cb607bb0e3f3b3468f)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)。

用于获取调制解调器信息（Modem Information）的 API 函数指针。

<a id="r_ga586f65e3f3ea8852261be04ce7ba67ba"></a>

```c
typedef int(* hl78xx_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[hl78xx_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga586f65e3f3ea8852261be04ce7ba67ba)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga7309390ed507748fdb72cf078b8e08a4)。

用于获取注册状态（registration status）的 API。

<a id="r_ga7cf1c4b11a828c186771200cd00b3bc8"></a>

```c
typedef int(* hl78xx_api_set_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_api_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cf1c4b11a828c186771200cd00b3bc8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于设置电话功能（Phone Functionality）的 API 函数指针。

<a id="r_gab3bcb3ba4cef24971acc41aa0815abe5"></a>

```c
typedef int(* hl78xx_api_get_phone_functionality) (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_api_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3bcb3ba4cef24971acc41aa0815abe5)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)。

用于获取电话功能（Phone Functionality）的 API。

<a id="r_ga8201489ac8055efa3019ffd8f3201644"></a>

```c
typedef int(* hl78xx_api_send_at_cmd) (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_api_send_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8201489ac8055efa3019ffd8f3201644)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于获取电话功能（Phone Functionality）的 API。

<a id="r_ga98fde2c3465abce3b4b7d94816bc029c"></a>

```c
typedef void(* hl78xx_at_monitor_handler_t) (const struct hl78xx_at_notification *notif, struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98fde2c3465abce3b4b7d94816bc029c)、[hl78xx_at_notification](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

AT 监视器处理函数（AT Monitor Handler）的函数类型。

<a id="r_ga517a58c85701991214ddb3a9d786f367"></a>

```c
typedef void(* hl78xx_at_monitor_release_t) (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga517a58c85701991214ddb3a9d786f367)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

AT 监视器释放函数（AT Monitor Release）的函数类型。

<a id="r_gade4999c5b603813020cd52a93687b76f"></a>

```c
typedef void(* hl78xx_evt_monitor_dispatcher_t) (struct hl78xx_evt *notif)
```

相关声明：[hl78xx_evt_monitor_dispatcher_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gade4999c5b603813020cd52a93687b76f)、[hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)。

事件监视器分派函数（Event Monitor Dispatcher）的函数类型。

<a id="r_gaa1346c7b8b44abae64f59cc8d5fa9c01"></a>

```c
typedef void(* hl78xx_evt_monitor_handler_t) (struct hl78xx_evt *notif, struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa1346c7b8b44abae64f59cc8d5fa9c01)、[hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

事件监视器处理函数（Event Monitor Handler）的函数类型。

<a id="r_ga774bbdee241bfb63374fdc74d2353a3d"></a>

```c
typedef void(* hl78xx_evt_monitor_release_t) (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga774bbdee241bfb63374fdc74d2353a3d)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

事件监视器释放函数（Event Monitor Release）的函数类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga298f953be96ab47be40b5440a2573182"></a>

```c
enum hl78xx_cell_rat_mode { HL78XX_RAT_CAT_M1 = 0 , HL78XX_RAT_NB1 , HL78XX_RAT_GSM , HL78XX_RAT_NBNTN , HL78XX_RAT_MODE_AUTO , HL78XX_RAT_MODE_NONE , HL78XX_RAT_COUNT = HL78XX_RAT_MODE_NONE }
```

相关声明：[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[HL78XX_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b)、[HL78XX_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e)、[HL78XX_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d)、[HL78XX_RAT_NBNTN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d)、[HL78XX_RAT_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b)、[HL78XX_RAT_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f)、[HL78XX_RAT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422)。

蜂窝无线接入技术（Cellular Radio Access Technologies）。

<a id="r_gaf2ab6a096dff081e7cbbba13b06de3cc"></a>

```c
enum hl78xx_kselacq_rat { HL78XX_KSELACQ_RAT_CLEAR = 0 , HL78XX_KSELACQ_RAT_CAT_M1 = 1 , HL78XX_KSELACQ_RAT_NB1 = 2 , HL78XX_KSELACQ_RAT_GSM = 3 }
```

相关声明：[hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)、[HL78XX_KSELACQ_RAT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850)、[HL78XX_KSELACQ_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f)、[HL78XX_KSELACQ_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca)、[HL78XX_KSELACQ_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30)。

原始 `AT+KSELACQ` 首选列表（PRL）中的无线接入技术（RAT）条目。

<a id="r_ga39a3de13bd706571cd7348ea46b7b708"></a>

```c
enum hl78xx_phone_functionality { HL78XX_SIM_POWER_OFF , HL78XX_FULLY_FUNCTIONAL , HL78XX_AIRPLANE = 4 }
```

相关声明：[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)、[HL78XX_SIM_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf)、[HL78XX_FULLY_FUNCTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba)、[HL78XX_AIRPLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570)。

电话功能模式（Phone Functionality Modes）。

<a id="r_ga0b3efb75d166d9d4bf163ffc6bb68fc0"></a>

```c
enum hl78xx_sim_slot { HL78XX_SIM_SLOT_1 = 0 , HL78XX_SIM_SLOT_2 = 1 }
```

相关声明：[hl78xx_sim_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0b3efb75d166d9d4bf163ffc6bb68fc0)、[HL78XX_SIM_SLOT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576)、[HL78XX_SIM_SLOT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794)。

由可选 SIM 切换 GPIO（SIM-switch GPIO）驱动的外部 SIM 卡槽选择（External SIM Slot Selection）。

<a id="r_ga618c248d23a1db1b027333c92adf99a1"></a>

```c
enum hl78xx_modem_restart_mode { HL78XX_MODEM_RESTART_HARD = 0 , HL78XX_MODEM_RESTART_SOFT }
```

相关声明：[hl78xx_modem_restart_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga618c248d23a1db1b027333c92adf99a1)、[HL78XX_MODEM_RESTART_HARD](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc)、[HL78XX_MODEM_RESTART_SOFT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8)。

由驱动管理的调制解调器重启模式（Driver-managed Modem Restart Modes）。

<a id="r_gab4a85c57d2f77c04a887f6552abff48a"></a>

```c
enum hl78xx_module_status { HL78XX_MODULE_READY = 0 , HL78XX_MODULE_WAITING_FOR_ACCESS_CODE , HL78XX_MODULE_SIM_NOT_PRESENT , HL78XX_MODULE_SIMLOCK , HL78XX_MODULE_UNRECOVERABLE_ERROR , HL78XX_MODULE_UNKNOWN_STATE , HL78XX_MODULE_INACTIVE_SIM }
```

相关声明：[hl78xx_module_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab4a85c57d2f77c04a887f6552abff48a)、[HL78XX_MODULE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db)、[HL78XX_MODULE_WAITING_FOR_ACCESS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820)、[HL78XX_MODULE_SIM_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9)、[HL78XX_MODULE_SIMLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f)、[HL78XX_MODULE_UNRECOVERABLE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294)、[HL78XX_MODULE_UNKNOWN_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6)、[HL78XX_MODULE_INACTIVE_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3)。

模块状态码（Module Status Codes）。

<a id="r_gaadcca229cbccc9832734bcc4e2a443e6"></a>

```c
enum hl78xx_modem_info_type { HL78XX_MODEM_INFO_SERIAL_NUMBER , HL78XX_MODEM_INFO_CURRENT_BAUD_RATE , HL78XX_MODEM_INFO_FW_VERSION }
```

相关声明：[hl78xx_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaadcca229cbccc9832734bcc4e2a443e6)、[HL78XX_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8)、[HL78XX_MODEM_INFO_CURRENT_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd)、[HL78XX_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca)。

蜂窝调制解调器信息类型（Cellular Modem Info Type）。

<a id="r_ga2d26ae6044baac5995f4184abe4faad3"></a>

```c
enum hl78xx_operator_format { HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC = 0 , HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC , HL78XX_OPERATOR_FORMAT_NUMERIC }
```

相关声明：[hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)、[HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c)、[HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164)、[HL78XX_OPERATOR_FORMAT_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9)。

网络运营商格式选项（Network Operator Format Options）。

<a id="r_ga563d651fff3621c1e21d7c47d19fd218"></a>

```c
enum hl78xx_network_info_type { HL78XX_NETWORK_INFO_APN , HL78XX_NETWORK_INFO_CURRENT_RAT , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA , HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC , HL78XX_NETWORK_INFO_OPERATOR_FORMAT , HL78XX_NETWORK_INFO_TAC , HL78XX_NETWORK_INFO_MCC , HL78XX_NETWORK_INFO_MNC , HL78XX_NETWORK_INFO_CELL_ID , HL78XX_NETWORK_INFO_IP_ADDRESS , HL78XX_NETWORK_INFO_DNS_PRIMARY , HL78XX_NETWORK_INFO_ACTIVE_BAND , HL78XX_NETWORK_INFO_SINR }
```

相关声明：[hl78xx_network_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga563d651fff3621c1e21d7c47d19fd218)、[HL78XX_NETWORK_INFO_APN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe)、[HL78XX_NETWORK_INFO_CURRENT_RAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c)、[HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a)、[HL78XX_NETWORK_INFO_OPERATOR_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520)、[HL78XX_NETWORK_INFO_TAC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f)、[HL78XX_NETWORK_INFO_MCC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c)、[HL78XX_NETWORK_INFO_MNC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb)、[HL78XX_NETWORK_INFO_CELL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650)、[HL78XX_NETWORK_INFO_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771)、[HL78XX_NETWORK_INFO_DNS_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73)、[HL78XX_NETWORK_INFO_ACTIVE_BAND](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc)、[HL78XX_NETWORK_INFO_SINR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48)。

缓存的网络信息类型（Cached Network Information Types）。

<a id="r_gabb0e5a4dd5c2e29d62ba27f6022f01f5"></a>

```c
enum nmea_output_port { NMEA_OUTPUT_NONE = 0x00 , NMEA_OUTPUT_USB_NMEA_PORT = 0x01 , NMEA_OUTPUT_UART1 = 0x03 , NMEA_OUTPUT_SAME_PORT = 0x04 , NMEA_OUTPUT_CMUX_DLC1 = 0x05 , NMEA_OUTPUT_CMUX_DLC2 = 0x06 , NMEA_OUTPUT_CMUX_DLC3 = 0x07 , NMEA_OUTPUT_CMUX_DLC4 = 0x08 }
```

相关声明：[nmea_output_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabb0e5a4dd5c2e29d62ba27f6022f01f5)、[NMEA_OUTPUT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9)、[NMEA_OUTPUT_USB_NMEA_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c)、[NMEA_OUTPUT_UART1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589)、[NMEA_OUTPUT_SAME_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3)、[NMEA_OUTPUT_CMUX_DLC1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf)、[NMEA_OUTPUT_CMUX_DLC2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f)、[NMEA_OUTPUT_CMUX_DLC3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d)、[NMEA_OUTPUT_CMUX_DLC4](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1)。

NMEA 输出端口选项（Output Port Options）。

<a id="r_ga7d4975dffccffac27c9dccb85c02d549"></a>

```c
enum hl78xx_agnss_mode { HL78XX_AGNSS_MODE_INVALID = 0 , HL78XX_AGNSS_MODE_VALID = 1 }
```

相关声明：[hl78xx_agnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d4975dffccffac27c9dccb85c02d549)、[HL78XX_AGNSS_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288)、[HL78XX_AGNSS_MODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d)。

辅助全球导航卫星系统（A-GNSS）辅助数据有效期模式（Assistance Data Validity Mode）。

<a id="r_gae9cf9c13242bc674dd7b0b79a69b8f31"></a>

```c
enum hl78xx_agnss_days { HL78XX_AGNSS_DAYS_1 = 1 , HL78XX_AGNSS_DAYS_2 = 2 , HL78XX_AGNSS_DAYS_3 = 3 , HL78XX_AGNSS_DAYS_7 = 7 , HL78XX_AGNSS_DAYS_14 = 14 , HL78XX_AGNSS_DAYS_28 = 28 }
```

相关声明：[hl78xx_agnss_days](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae9cf9c13242bc674dd7b0b79a69b8f31)、[HL78XX_AGNSS_DAYS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876)、[HL78XX_AGNSS_DAYS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34)、[HL78XX_AGNSS_DAYS_3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8)、[HL78XX_AGNSS_DAYS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a)、[HL78XX_AGNSS_DAYS_14](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816)、[HL78XX_AGNSS_DAYS_28](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459)。

待下载的预测辅助数据（Predicted Assistance Data）天数，用于写命令；或距离其过期的天数，用于读命令。

<a id="r_ga6340324dcb76101c66b902bb9a14dbd3"></a>

```c
enum power_down_event { POWER_DOWN_EVENT_ENTER = 0 , POWER_DOWN_EVENT_EXIT , POWER_DOWN_EVENT_NONE }
```

相关声明：[power_down_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6340324dcb76101c66b902bb9a14dbd3)、[POWER_DOWN_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa)、[POWER_DOWN_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1)、[POWER_DOWN_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b)。

掉电事件类型（Power Down Event Types）。

<a id="r_ga50bd06a27371c5c79de5bef125d6b5f3"></a>

```c
enum hl78xx_power_down_response { HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE = 0 , HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE , HL78XX_POWER_DOWN_RESPONSE_ABORT }
```

相关声明：[hl78xx_power_down_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga50bd06a27371c5c79de5bef125d6b5f3)、[HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a)、[HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985)、[HL78XX_POWER_DOWN_RESPONSE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e)。

应用程序对待处理掉电请求（Pending Power-down Request）的响应。

<a id="r_ga5d8a5b00f354e98abc2effa560f3bac8"></a>

```c
enum hl78xx_edrx_event { HL78XX_EDRX_EVENT_IDLE_EXIT = 0 , HL78XX_EDRX_EVENT_IDLE_ENTER , HL78XX_EDRX_EVENT_IDLE_NONE }
```

相关声明：[hl78xx_edrx_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5d8a5b00f354e98abc2effa560f3bac8)、[HL78XX_EDRX_EVENT_IDLE_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8)、[HL78XX_EDRX_EVENT_IDLE_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5)、[HL78XX_EDRX_EVENT_IDLE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a)。

扩展非连续接收（eDRX）事件类型。

<a id="r_gae891e3155a0ebf72433dd58ae4c36512"></a>

```c
enum hl78xx_psmev_event { HL78XX_PSM_EVENT_EXIT = 0 , HL78XX_PSM_EVENT_ENTER , HL78XX_PSM_EVENT_NONE }
```

相关声明：[hl78xx_psmev_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae891e3155a0ebf72433dd58ae4c36512)、[HL78XX_PSM_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94)、[HL78XX_PSM_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda)、[HL78XX_PSM_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553)。

省电模式（PSM）事件类型。

<a id="r_ga8a864475f6e9673f85ec7c56028992a5"></a>

```c
enum hl78xx_evt_type { HL78XX_LTE_RAT_UPDATE , HL78XX_LTE_REGISTRATION_STAT_UPDATE , HL78XX_LTE_SIM_REGISTRATION , HL78XX_LTE_MODEM_STARTUP , HL78XX_LTE_FOTA_UPDATE_STATUS , HL78XX_LTE_DNS_READY , HL78XX_LTE_AT_CMD_READY , HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE , HL78XX_LTE_CTZEU_UPDATE , HL78XX_GNSS_ENGINE_READY , HL78XX_GNSS_EVENT_INIT , HL78XX_GNSS_EVENT_START , HL78XX_GNSS_EVENT_STOP , HL78XX_GNSS_EVENT_POSITION , HL78XX_GNSS_EVENT_START_BLOCKED , HL78XX_GNSS_EVENT_SEARCH_TIMEOUT , HL78XX_GNSS_EVENT_MODE_EXITED , HL78XX_EDRX_IDLE_UPDATE , HL78XX_LTE_PSMEV_UPDATE , HL78XX_POWER_DOWN_UPDATE , HL78XX_VGPIO_LOW , HL78XX_VGPIO_HIGH , HL78XX_GPIO6_LOW , HL78XX_GPIO6_HIGH , HL78XX_CELLMEAS_UPDATE , HL78XX_EVT_TYPE_COUNT }
```

相关声明：[hl78xx_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8a864475f6e9673f85ec7c56028992a5)、[HL78XX_LTE_RAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5)、[HL78XX_LTE_REGISTRATION_STAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95)、[HL78XX_LTE_SIM_REGISTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9)、[HL78XX_LTE_MODEM_STARTUP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839)、[HL78XX_LTE_FOTA_UPDATE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92)、[HL78XX_LTE_DNS_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8)、[HL78XX_LTE_AT_CMD_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73)、[HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5)、[HL78XX_LTE_CTZEU_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6)、[HL78XX_GNSS_ENGINE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b)、[HL78XX_GNSS_EVENT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae)、[HL78XX_GNSS_EVENT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5)、[HL78XX_GNSS_EVENT_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61)、[HL78XX_GNSS_EVENT_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c)、[HL78XX_GNSS_EVENT_START_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07)、[HL78XX_GNSS_EVENT_SEARCH_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429)、[HL78XX_GNSS_EVENT_MODE_EXITED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916)、[HL78XX_EDRX_IDLE_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3)、[HL78XX_LTE_PSMEV_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7)、[HL78XX_POWER_DOWN_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2)、[HL78XX_VGPIO_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc)、[HL78XX_VGPIO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63)、[HL78XX_GPIO6_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe)、[HL78XX_GPIO6_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52)、[HL78XX_CELLMEAS_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254)、[HL78XX_EVT_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790)。

HL78xx 事件类型（Event Types）。

<a id="r_ga5453000edbd52c54f7193de4852aa9a8"></a>

```c
enum wdsi_indication { WDSI_BOOTSTRAP_CREDENTIALS_PRESENT = 0 , WDSI_USER_AGREEMENT_REQUEST = 1 , WDSI_FIRMWARE_DOWNLOAD_REQUEST = 2 , WDSI_FIRMWARE_INSTALL_REQUEST = 3 , WDSI_AUTHENTICATION_START = 4 , WDSI_AUTHENTICATION_FAILED = 5 , WDSI_AUTHENTICATION_SUCCESS = 6 , WDSI_CONNECTION_DENIED = 7 , WDSI_DM_SESSION_CLOSED = 8 , WDSI_FIRMWARE_AVAILABLE = 9 , WDSI_FIRMWARE_DOWNLOADED = 10 , WDSI_FIRMWARE_DOWNLOAD_ISSUE = 11 , WDSI_PACKAGE_VERIFIED_CERTIFIED = 12 , WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED = 13 , WDSI_FIRMWARE_UPDATE_START = 14 , WDSI_FIRMWARE_UPDATE_FAILED = 15 , WDSI_FIRMWARE_UPDATE_SUCCESS = 16 , WDSI_DOWNLOAD_IN_PROGRESS = 18 , WDSI_SESSION_STARTED = 23 }
```

相关声明：[wdsi_indication](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5453000edbd52c54f7193de4852aa9a8)、[WDSI_BOOTSTRAP_CREDENTIALS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339)、[WDSI_USER_AGREEMENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2)、[WDSI_FIRMWARE_DOWNLOAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68)、[WDSI_FIRMWARE_INSTALL_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5)、[WDSI_AUTHENTICATION_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1)、[WDSI_AUTHENTICATION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6)、[WDSI_AUTHENTICATION_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608)、[WDSI_CONNECTION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a)、[WDSI_DM_SESSION_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2)、[WDSI_FIRMWARE_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8)、[WDSI_FIRMWARE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd)、[WDSI_FIRMWARE_DOWNLOAD_ISSUE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184)、[WDSI_PACKAGE_VERIFIED_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7)、[WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5)、[WDSI_FIRMWARE_UPDATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458)、[WDSI_FIRMWARE_UPDATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc)、[WDSI_FIRMWARE_UPDATE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f)、[WDSI_DOWNLOAD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0)、[WDSI_SESSION_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d)。

设备服务指示（Device Services Indications，`+WDSI`）。

<a id="r_ga95d1ccc5899adf1b2eda6aa0777b7e80"></a>

```c
enum hl78xx_gnss_event_type { HL78XX_GNSSEV_INITIALISATION = 0 , HL78XX_GNSSEV_START = 1 , HL78XX_GNSSEV_STOP = 2 , HL78XX_GNSSEV_POSITION = 3 }
```

相关声明：[hl78xx_gnss_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga95d1ccc5899adf1b2eda6aa0777b7e80)、[HL78XX_GNSSEV_INITIALISATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21)、[HL78XX_GNSSEV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740)、[HL78XX_GNSSEV_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da)、[HL78XX_GNSSEV_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533)。

全球导航卫星系统（GNSS）事件类型。

<a id="r_ga9b9da1841754d723cddc103800b141ae"></a>

```c
enum hl78xx_event_status { HL78XX_STATUS_FAILED = 0 , HL78XX_STATUS_SUCCESS = 1 }
```

相关声明：[hl78xx_event_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9b9da1841754d723cddc103800b141ae)、[HL78XX_STATUS_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e)、[HL78XX_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd)。

GNSS 事件状态。

<a id="r_ga2a471bc1b92dba1e316b2b27e3778e1a"></a>

```c
enum gnss_position_events { GNSS_FIX_LOST_OR_UNAVAILABLE = 0 , GNSS_ESTIMATED_POSITION_AVAILABLE = 1 , GNSS_2D_POSITION_AVAILABLE = 2 , GNSS_3D_POSITION_AVAILABLE = 3 , GNSS_FIX_CHANGED_TO_INVALID = 4 }
```

相关声明：[gnss_position_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2a471bc1b92dba1e316b2b27e3778e1a)、[GNSS_FIX_LOST_OR_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d)、[GNSS_ESTIMATED_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306)、[GNSS_2D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8)、[GNSS_3D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407)、[GNSS_FIX_CHANGED_TO_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa)。

全球导航卫星系统（GNSS）位置事件（Position Events），`eventType = 3`。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gaab36b1992acffc8b25b8140da1a79577"></a>

```c
int hl78xx_api_func_set_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_api_func_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaab36b1992acffc8b25b8140da1a79577)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置电话功能模式（Phone Functionality Mode），内部实现。

<a id="r_gad39b680650d8a3f1ea20bc18fa6101d4"></a>

```c
int hl78xx_api_func_restart (const struct device *dev, enum hl78xx_modem_restart_mode mode)
```

相关声明：[hl78xx_api_func_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad39b680650d8a3f1ea20bc18fa6101d4)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_restart_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga618c248d23a1db1b027333c92adf99a1)。

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

<a id="r_gaca72419e4396a45b296a65f89877dbb8"></a>

```c
int hl78xx_api_func_get_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_api_func_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaca72419e4396a45b296a65f89877dbb8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)。

获取电话功能模式（Phone Functionality Mode），内部实现。

<a id="r_gae50586b4f939abacda6739850c118982"></a>

```c
int hl78xx_api_func_get_signal (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[hl78xx_api_func_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae50586b4f939abacda6739850c118982)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取网络信号强度（Network Signal Strength），内部实现。

<a id="r_ga5f9c8c8087e1e6008f290ddfe42e3d97"></a>

```c
int hl78xx_api_func_get_modem_info (const struct device *dev, enum hl78xx_modem_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_api_func_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5f9c8c8087e1e6008f290ddfe42e3d97)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaadcca229cbccc9832734bcc4e2a443e6)。

获取厂商专用的调制解调器信息（Vendor-specific Modem Information），内部实现。

<a id="r_gacddf878e52d0642279e147add9c8bdad"></a>

```c
int hl78xx_api_func_get_modem_info_standard (const struct device *dev, enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[hl78xx_api_func_get_modem_info_standard](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacddf878e52d0642279e147add9c8bdad)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)。

从缓存获取标准调制解调器信息（Modem Information），采用 Zephyr 蜂窝 API（Cellular API）。

<a id="r_gac08824e4662cb5fcb316e6a0e1e5ba17"></a>

```c
int hl78xx_api_func_get_network_info (const struct device *dev, enum hl78xx_network_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_api_func_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac08824e4662cb5fcb316e6a0e1e5ba17)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga563d651fff3621c1e21d7c47d19fd218)。

获取缓存的厂商专用网络信息（Vendor-specific Network Information）。

<a id="r_gadd718f794b24c9610e97f7460519e577"></a>

```c
int hl78xx_api_func_get_rsrp_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadd718f794b24c9610e97f7460519e577)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收功率（RSRP）是否达到配置的最低阈值。

<a id="r_ga79c8b3e0581e6418526b3aa86e6bbb5a"></a>

```c
int hl78xx_api_func_get_rsrq_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga79c8b3e0581e6418526b3aa86e6bbb5a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收质量（RSRQ）是否达到配置的最低阈值。

<a id="r_ga069a0709408fef75514dfaf12bc42cb5"></a>

```c
int hl78xx_api_func_get_sinr_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_api_func_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga069a0709408fef75514dfaf12bc42cb5)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前信号与干扰加噪声比（SINR）是否达到配置的最低阈值。

<a id="r_gab8e5ae21bd129d61735c9cfe3df557d2"></a>

```c
int hl78xx_api_func_set_network_operator_format (const struct device *dev, enum hl78xx_operator_format format)
```

相关声明：[hl78xx_api_func_set_network_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab8e5ae21bd129d61735c9cfe3df557d2)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)。

设置 `+COPS` 网络运营商格式（Network Operator Format）。

<a id="r_gafc8c324c2beb2c59c9f15542d06b85ee"></a>

```c
int hl78xx_api_func_set_prl (const struct device *dev, const struct kselacq_syntax kselacq_rats)
```

相关声明：[hl78xx_api_func_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gafc8c324c2beb2c59c9f15542d06b85ee)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

通过 `AT+KSELACQ` 设置新的首选无线接入技术列表（Preferred RAT List）。

<a id="r_ga4c2dc7d53dd4780d8f1e00e9889248d3"></a>

```c
int hl78xx_api_func_get_prl (const struct device *dev, struct kselacq_syntax *kselacq_rats)
```

相关声明：[hl78xx_api_func_get_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga4c2dc7d53dd4780d8f1e00e9889248d3)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

获取当前首选无线接入技术列表（Preferred RAT List）。

<a id="r_ga1640ce244f1a4de52efa0b7c33f7b02a"></a>

```c
int hl78xx_api_func_set_autorat_inhibit (const struct device *dev, bool inhibit)
```

相关声明：[hl78xx_api_func_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1640ce244f1a4de52efa0b7c33f7b02a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

禁止启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

<a id="r_ga6adcbc5395d078be2fc9c6e62612f603"></a>

```c
bool hl78xx_api_func_at_is_busy (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_api_func_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6adcbc5395d078be2fc9c6e62612f603)、[device](../device_reference/P002_设备对象结构.md)。

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

<a id="r_gac6ed6d4f41003cb2517f802762d5b239"></a>

```c
int hl78xx_set_runtime_band_provider (const struct device *dev, hl78xx_runtime_band_provider_t provider, void *user_data)
```

相关声明：[hl78xx_set_runtime_band_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac6ed6d4f41003cb2517f802762d5b239)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_runtime_band_provider_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga82793d1f4c0c8f03ae27b29afa1c3d3f)。

为驱动注册或清除运行时频段提供器（Runtime Band Provider）。

<a id="r_gae3f2ed904a3b0784d64d2d1537ce9564"></a>

```c
int hl78xx_api_func_modem_dynamic_cmd_send (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_api_func_modem_dynamic_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3f2ed904a3b0784d64d2d1537ce9564)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送动态 AT 命令（Dynamic AT Command），内部实现。

<a id="r_ga45a97bfc5f73d1877357dc1f410c61cd"></a>

```c
int hl78xx_modem_at_send (const struct device *dev, const char *cmd)
```

相关声明：[hl78xx_modem_at_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga45a97bfc5f73d1877357dc1f410c61cd)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

向调制解调器（Modem）发送预先格式化的 AT 命令。

<a id="r_ga3e9edd942cbf32b5a2eec259c44e5ee4"></a>

```c
int hl78xx_modem_at_cmd (const struct device *dev, char *response, size_t response_size, const char *cmd)
```

相关声明：[hl78xx_modem_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga3e9edd942cbf32b5a2eec259c44e5ee4)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

发送预先格式化的 AT 命令，并将完整的调制解调器响应（Modem Response）复制到调用者提供的缓冲区。

<a id="r_gabe520e9e9a5e48ab05e238f6b59b8cda"></a>

```c
static int hl78xx_get_modem_info (const struct device *dev, const enum hl78xx_modem_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabe520e9e9a5e48ab05e238f6b59b8cda)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaadcca229cbccc9832734bcc4e2a443e6)。

获取设备调制解调器信息（Modem Info）。

<a id="r_gaedfc9112048d6c987ee7fefa4e8abd55"></a>

```c
static int hl78xx_get_network_info (const struct device *dev, enum hl78xx_network_info_type type, void *info, size_t size)
```

相关声明：[hl78xx_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaedfc9112048d6c987ee7fefa4e8abd55)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_network_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga563d651fff3621c1e21d7c47d19fd218)。

获取设备缓存的网络信息（Cached Network Info）。

<a id="r_ga65f087ad92a0f2bfb15d4f7b627c754f"></a>

```c
static int hl78xx_get_rsrp_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga65f087ad92a0f2bfb15d4f7b627c754f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收功率（RSRP）是否达到配置的阈值。

<a id="r_gab49ab6eb5aa0cfcdea4e6e7bcabd1d48"></a>

```c
static int hl78xx_get_rsrq_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab49ab6eb5aa0cfcdea4e6e7bcabd1d48)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前参考信号接收质量（RSRQ）是否达到配置的阈值。

<a id="r_ga06800817986b9a4b0291cc22c808dfae"></a>

```c
static int hl78xx_get_sinr_validity (const struct device *dev, bool *is_valid)
```

相关声明：[hl78xx_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga06800817986b9a4b0291cc22c808dfae)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查当前信号与干扰加噪声比（SINR）是否达到配置的阈值。

<a id="r_gad564df9a12ad4ee40caeffec1099a93b"></a>

```c
static int hl78xx_set_prl (const struct device *dev, struct kselacq_syntax prl)
```

相关声明：[hl78xx_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad564df9a12ad4ee40caeffec1099a93b)、[device](../device_reference/P002_设备对象结构.md)、[kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)。

设置新的原始 `AT+KSELACQ` 首选无线接入技术列表（Preferred RAT List）。

<a id="r_gaad6374b5c5ef64886c6d8fdde0cba3c4"></a>

```c
static int hl78xx_set_autorat_inhibit (const struct device *dev, bool inhibit)
```

相关声明：[hl78xx_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaad6374b5c5ef64886c6d8fdde0cba3c4)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

禁止或允许启动时恢复自动无线接入技术（Auto-RAT）的首选列表（PRL）。

<a id="r_gad2673b87d730da42b4d2109e849277cc"></a>

```c
static bool hl78xx_at_is_busy (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hl78xx_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad2673b87d730da42b4d2109e849277cc)、[device](../device_reference/P002_设备对象结构.md)。

报告调制解调器会话脚本（Modem Chat Script）当前是否正在执行。

<a id="r_gaee99182459b5971ebaa7892989b0e8df"></a>

```c
static int hl78xx_set_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality functionality, bool reset)
```

相关声明：[hl78xx_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaee99182459b5971ebaa7892989b0e8df)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器的电话功能模式（Phone Functionality Mode）。

<a id="r_ga2c4ff4a9b1d5d2530700327e1d4af6e0"></a>

```c
static int hl78xx_restart_modem (const struct device *dev, enum hl78xx_modem_restart_mode mode)
```

相关声明：[hl78xx_restart_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2c4ff4a9b1d5d2530700327e1d4af6e0)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_modem_restart_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga618c248d23a1db1b027333c92adf99a1)。

请求由驱动管理的调制解调器重启（Driver-managed Modem Restart）。

<a id="r_gaf778d092ad7f9b67b0930c0da2375996"></a>

```c
static int hl78xx_get_phone_functionality (const struct device *dev, enum hl78xx_phone_functionality *functionality)
```

相关声明：[hl78xx_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf778d092ad7f9b67b0930c0da2375996)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)。

获取调制解调器当前的电话功能模式（Phone Functionality Mode）。

<a id="r_gae7102c14fda882e87bff0f0828ab4263"></a>

```c
static int hl78xx_modem_cmd_send (const struct device *dev, const char *cmd, uint16_t cmd_size, const struct modem_chat_match *response_matches, uint16_t matches_size)
```

相关声明：[hl78xx_modem_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae7102c14fda882e87bff0f0828ab4263)、[device](../device_reference/P002_设备对象结构.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向调制解调器（Modem）发送 AT 命令，并等待匹配的响应（Matched Response）。

<a id="r_gaba7b5c599c1b9285b9dcfbae91ac5e7f"></a>

```c
static int hl78xx_modem_at_err_type (int error)
```

相关声明：[hl78xx_modem_at_err_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaba7b5c599c1b9285b9dcfbae91ac5e7f)。

返回编码在 `hl78xx_modem_at_send`／`cmd` 返回值中的调制解调器错误类型（Modem Error Type）。

<a id="r_ga13ead2b7a66530a1fbe15e5c4d9addeb"></a>

```c
static int hl78xx_modem_at_err (int error)
```

相关声明：[hl78xx_modem_at_err](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga13ead2b7a66530a1fbe15e5c4d9addeb)。

返回编码在 `hl78xx_modem_at_send`／`cmd` 中的调制解调器 CME／CMS 错误码（Error Code）。

<a id="r_ga9dd8be5c6d35de4122ab5604bf5b17ce"></a>

```c
static int hl78xx_parse_rssi (uint8_t rssi, int16_t *value)
```

相关声明：[hl78xx_parse_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9dd8be5c6d35de4122ab5604bf5b17ce)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始接收信号强度指示（RSSI）值转换为 dBm。

<a id="r_ga8abfb51de22c24f1870d2b5f4b3b60ee"></a>

```c
static int hl78xx_parse_rsrp (uint8_t rsrp, int16_t *value)
```

相关声明：[hl78xx_parse_rsrp](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8abfb51de22c24f1870d2b5f4b3b60ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始参考信号接收功率（RSRP）值转换为 dBm。

<a id="r_ga09f7b39a934d38a2d3da8deefc3d2758"></a>

```c
static int hl78xx_parse_rsrq (uint8_t rsrq, int16_t *value)
```

相关声明：[hl78xx_parse_rsrq](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga09f7b39a934d38a2d3da8deefc3d2758)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将调制解调器提供的原始参考信号接收质量（RSRQ）值转换为 dB。

<a id="r_gadfb6a494068c978908ed0bd968b81a5f"></a>

```c
static void hl78xx_evt_monitor_pause (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadfb6a494068c978908ed0bd968b81a5f)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

暂停监视器（Monitor）。

<a id="r_gab3a63acd15fc9bd6a7d9ded9ed1731fa"></a>

```c
static void hl78xx_evt_monitor_resume (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3a63acd15fc9bd6a7d9ded9ed1731fa)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

恢复监视器（Monitor）。

<a id="r_gab08189be0b4dc7f03428d829f0170bbe"></a>

```c
static void hl78xx_at_monitor_pause (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab08189be0b4dc7f03428d829f0170bbe)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

暂停 AT 监视器（AT Monitor）。

<a id="r_ga2723fa7f912913d299629fdba4efb130"></a>

```c
static void hl78xx_at_monitor_resume (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2723fa7f912913d299629fdba4efb130)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

恢复 AT 监视器（AT Monitor）。

<a id="r_ga051a63a86e9ca353434b23e1adf5d543"></a>

```c
int hl78xx_at_monitor_register (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga051a63a86e9ca353434b23e1adf5d543)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

注册 AT 监视器（AT Monitor）。

<a id="r_ga1244a8f6b7e5e488ab596aa5341ad66a"></a>

```c
int hl78xx_at_monitor_unregister (struct hl78xx_at_monitor_entry *mon)
```

相关声明：[hl78xx_at_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1244a8f6b7e5e488ab596aa5341ad66a)、[hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)。

注销 AT 监视器（AT Monitor）。

<a id="r_ga8265e020ad0d8c3e69f2219173530720"></a>

```c
int hl78xx_evt_notif_handler_set (hl78xx_evt_monitor_dispatcher_t handler)
```

相关声明：[hl78xx_evt_notif_handler_set](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8265e020ad0d8c3e69f2219173530720)、[hl78xx_evt_monitor_dispatcher_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gade4999c5b603813020cd52a93687b76f)。

设置 HL78xx 调制解调器事件（Modem Events）的事件通知处理函数（Event Notification Handler）。

<a id="r_ga6590e5352cbd8ff6ea0580edd64eb0d0"></a>

```c
int hl78xx_evt_monitor_register (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6590e5352cbd8ff6ea0580edd64eb0d0)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

注册事件监视器（Event Monitor）。

<a id="r_gaf4c623e7bed92b6ea3964b59df04e98e"></a>

```c
int hl78xx_evt_monitor_unregister (struct hl78xx_evt_monitor_entry *mon)
```

相关声明：[hl78xx_evt_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf4c623e7bed92b6ea3964b59df04e98e)、[hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)。

注销事件监视器（Event Monitor）。

<a id="r_gaf8cbf3de84df41d7066b9a07f106c17b"></a>

```c
enum cellular_access_technology hl78xx_rat_to_access_tech (enum hl78xx_cell_rat_mode rat_mode)
```

相关声明：[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)、[hl78xx_rat_to_access_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf8cbf3de84df41d7066b9a07f106c17b)、[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)。

将 HL78xx 无线接入技术模式（RAT Mode）转换为标准蜂窝 API（Cellular API）表示。

<a id="r_gac9f87f986b0b745bf8e370896113066f"></a>

```c
enum hl78xx_cell_rat_mode hl78xx_access_tech_to_rat (enum cellular_access_technology access_tech)
```

相关声明：[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[hl78xx_access_tech_to_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac9f87f986b0b745bf8e370896113066f)、[cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)。

将标准蜂窝接入技术（Cellular Access Technology）转换为 HL78xx 无线接入技术模式（RAT Mode）。

<a id="r_gaf34ed3d29904f1a18c0c75a0de4bc727"></a>

```c
int hl78xx_start_airvantage_dm_session (const struct device *dev)
```

相关声明：[hl78xx_start_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf34ed3d29904f1a18c0c75a0de4bc727)、[device](../device_reference/P002_设备对象结构.md)。

启动 AirVantage 设备管理（Device Management，DM）会话。

<a id="r_ga9018c8332803eaada4083390c40ac3f0"></a>

```c
int hl78xx_stop_airvantage_dm_session (const struct device *dev)
```

相关声明：[hl78xx_stop_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9018c8332803eaada4083390c40ac3f0)、[device](../device_reference/P002_设备对象结构.md)。

停止 AirVantage 设备管理（Device Management，DM）会话。

<a id="r_ga803bf7a13a7b57477dbfa4d6b3faa14e"></a>

```c
int hl78xx_set_wake_pin_low (const struct device *dev)
```

相关声明：[hl78xx_set_wake_pin_low](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga803bf7a13a7b57477dbfa4d6b3faa14e)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器的 `WAKE` 引脚驱动为低电平（Low）。

<a id="r_gae3e97cdf80470496d6d8542f61f985c0"></a>

```c
int hl78xx_set_wake_pin_high (const struct device *dev)
```

相关声明：[hl78xx_set_wake_pin_high](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3e97cdf80470496d6d8542f61f985c0)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器的 `WAKE` 引脚驱动为高电平（High）。

<a id="r_ga9bac621e2f74d598329f61cd95b0291b"></a>

```c
int hl78xx_set_active_sim (const struct device *dev, enum hl78xx_sim_slot sim_slot)
```

相关声明：[hl78xx_set_active_sim](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9bac621e2f74d598329f61cd95b0291b)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_sim_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0b3efb75d166d9d4bf163ffc6bb68fc0)。

选择活动的外部 SIM 卡槽（Active External SIM Slot）。

<a id="r_ga7cc4861b1449b551246204b84779c621"></a>

```c
int hl78xx_wakeup_modem (const struct device *dev)
```

相关声明：[hl78xx_wakeup_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cc4861b1449b551246204b84779c621)、[device](../device_reference/P002_设备对象结构.md)。

将调制解调器从省电模式（PSM）睡眠中唤醒。

<a id="r_ga41d66fc0e8681bf6a68f47af5bcacb90"></a>

```c
int hl78xx_edrx_get_time_to_sleep (const struct device *dev)
```

相关声明：[hl78xx_edrx_get_time_to_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga41d66fc0e8681bf6a68f47af5bcacb90)、[device](../device_reference/P002_设备对象结构.md)。

获取调制解调器进入扩展非连续接收空闲状态（eDRX Idle State）前的剩余时间。

<a id="r_ga9e9d288506708b275cc98e508bc8251d"></a>

```c
int hl78xx_enter_gnss_mode (const struct device *dev)
```

相关声明：[hl78xx_enter_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9e9d288506708b275cc98e508bc8251d)、[device](../device_reference/P002_设备对象结构.md)。

进入全球导航卫星系统（GNSS）模式。

<a id="r_ga475545d83cf5fd883fd11fb0db8400ed"></a>

```c
int hl78xx_exit_gnss_mode (const struct device *dev)
```

相关声明：[hl78xx_exit_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga475545d83cf5fd883fd11fb0db8400ed)、[device](../device_reference/P002_设备对象结构.md)。

退出全球导航卫星系统（GNSS）模式，返回长期演进（LTE）模式。

<a id="r_ga48f504b9bb41d4a13ac592f763aeb207"></a>

```c
int hl78xx_queue_gnss_search (const struct device *dev)
```

相关声明：[hl78xx_queue_gnss_search](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga48f504b9bb41d4a13ac592f763aeb207)、[device](../device_reference/P002_设备对象结构.md)。

将 GNSS 位置搜索（Position Search）加入队列。

<a id="r_ga5a1949cd23380056b4ee1775b1e6cc3b"></a>

```c
int hl78xx_gnss_set_nmea_output (const struct device *dev, enum nmea_output_port port)
```

相关声明：[hl78xx_gnss_set_nmea_output](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5a1949cd23380056b4ee1775b1e6cc3b)、[device](../device_reference/P002_设备对象结构.md)、[nmea_output_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabb0e5a4dd5c2e29d62ba27f6022f01f5)。

设置 GNSS 的 NMEA 输出端口（Output Port）。

<a id="r_gae349d6b96ef9ae67b5ed01d0a8fa2cb0"></a>

```c
int hl78xx_gnss_set_search_timeout (const struct device *dev, uint32_t timeout_ms)
```

相关声明：[hl78xx_gnss_set_search_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae349d6b96ef9ae67b5ed01d0a8fa2cb0)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 GNSS 搜索超时（Search Timeout）。

<a id="r_ga209d0579899aef4ade5cf8de1251a323"></a>

```c
int hl78xx_gnss_get_search_timeout_remaining (const struct device *dev, uint32_t *timeout_ms)
```

相关声明：[hl78xx_gnss_get_search_timeout_remaining](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga209d0579899aef4ade5cf8de1251a323)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取剩余的 GNSS 搜索超时（Search Timeout）。

<a id="r_ga0238b9a2de4683369a0be7a6ed481938"></a>

```c
int hl78xx_gnss_get_latest_known_fix (const struct device *dev)
```

相关声明：[hl78xx_gnss_get_latest_known_fix](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0238b9a2de4683369a0be7a6ed481938)、[device](../device_reference/P002_设备对象结构.md)。

从调制解调器获取最新已知的 GNSS 定位结果（Fix）。

<a id="r_ga473c72484a8a758470ff7043de7ab48d"></a>

```c
int hl78xx_gnss_assist_data_get_status (const struct device *dev, struct hl78xx_agnss_status *status)
```

相关声明：[hl78xx_gnss_assist_data_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga473c72484a8a758470ff7043de7ab48d)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_agnss_status](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md)。

获取辅助全球导航卫星系统（A-GNSS）的辅助数据状态（Assistance Data Status）。

<a id="r_gabf8fcaa1b5a59d5a2cac3c467f93c9f8"></a>

```c
int hl78xx_gnss_assist_data_download (const struct device *dev, enum hl78xx_agnss_days days)
```

相关声明：[hl78xx_gnss_assist_data_download](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabf8fcaa1b5a59d5a2cac3c467f93c9f8)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_agnss_days](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae9cf9c13242bc674dd7b0b79a69b8f31)。

下载辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

<a id="r_ga452b1ee210417569b3cdfc30db25622a"></a>

```c
int hl78xx_gnss_assist_data_delete (const struct device *dev)
```

相关声明：[hl78xx_gnss_assist_data_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga452b1ee210417569b3cdfc30db25622a)、[device](../device_reference/P002_设备对象结构.md)。

删除辅助全球导航卫星系统（A-GNSS）的辅助数据（Assistance Data）。

<a id="r_gac7291340f8699bb37cd864516615ea05"></a>

```c
int hl78xx_power_down_trigger (const struct device *dev, k_timeout_t delay)
```

相关声明：[hl78xx_power_down_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac7291340f8699bb37cd864516615ea05)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

经过调用者提供的延迟后，触发 HL78xx 关机流程（Shutdown Process）。

<a id="r_ga98af31968e3bf0fc72dea5d56e97e122"></a>

```c
int hl78xx_power_down_cancel (const struct device *dev)
```

相关声明：[hl78xx_power_down_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98af31968e3bf0fc72dea5d56e97e122)、[device](../device_reference/P002_设备对象结构.md)。

取消待处理的 HL78xx 第一阶段关机定时器（Stage-1 Shutdown Timer）。

<a id="r_ga249a5bf6cdbd69ec930724bf2541de72"></a>

```c
int hl78xx_power_down_respond (const struct device *dev, enum hl78xx_power_down_response response, uint32_t timeout_s)
```

相关声明：[hl78xx_power_down_respond](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga249a5bf6cdbd69ec930724bf2541de72)、[device](../device_reference/P002_设备对象结构.md)、[hl78xx_power_down_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga50bd06a27371c5c79de5bef125d6b5f3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

响应待处理的 HL78XX 掉电更新（Power-down Update）。

<a id="r_ga2bcaada6a58dfbe3658fc6bcb3090fff"></a>

```c
void hl78xx_power_down_confirm (const struct device *dev)
```

相关声明：[hl78xx_power_down_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2bcaada6a58dfbe3658fc6bcb3090fff)、[device](../device_reference/P002_设备对象结构.md)。

确认应用程序清理（Application Cleanup）已完成，调制解调器可以继续执行物理关机（Physical Shutdown）。


## 1.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/drivers/cellular.h](../api_source_supplement_reference/P025_cellular.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P030_hl78xx_apis.h_源码浏览.md)
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
- [CSQ_RSSI_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8c28a5a32edb83ea0b0120dd3b00451f)
- [CSQ_RSSI_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab2c8054a088aa6927aa10f1aed1587ae)
- [CESQ_RSRP_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03c48d45ba1dfcdeabba881f2b1cd936)
- [CESQ_RSRP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacb02197961c70e98147ae25e4c11d4de)
- [CESQ_RSRQ_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9a4429e44439c5ebdd18ccd549f832f5)
- [CESQ_RSRQ_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d02276973c71eded42d4242a34ca745)
- [HL78XX_MODEM_AT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac53a8b20d353944744e259f1f9008d44)
- [HL78XX_MODEM_AT_CME_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga23bb6b58819d70eb379f89a3878c07d0)
- [HL78XX_MODEM_AT_CMS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0fef7f6b540d959bf391ac39d8c2738a)
- [CSQ_RSSI_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga72dfe852d4d6365d80f33b918f631501)
- [CESQ_RSRP_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga309cc2c1be1d4006e2ccb8d59cb3e916)
- [CESQ_RSRQ_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga536c21c42099fc04ac85a634ffa41d24)
- [PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga734b46dfd78fbf6fc938a6f9115f2cc7)
- [ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga3a6d3cd70078e6046471ec528a09cd19)
- [MDM_MANUFACTURER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9587840c88858d1c26bd3afedd96bd68)
- [MDM_MODEL_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga694436b7ecedfd934f78afa9f404cadb)
- [MDM_REVISION_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6327f0d9596ad616f844687ac0fbc4f9)
- [MDM_IMEI_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9213ea6a80a1f80b10ade16314fa56dd)
- [MDM_IMSI_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9c11717136907c549f2ddb5c9bab48b7)
- [MDM_ICCID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa14eef37d2beacdb02a50ec4eb93d1fd)
- [MDM_APN_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2586187555aed092ffbf40e7991cc266)
- [MDM_MAX_CERT_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0a99d20ad7b62fd41c0118e2f5af522b)
- [MDM_MAX_HOSTNAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaad7153fc809f017cd727bc60988fd799)
- [MDM_SERIAL_NUMBER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae2d73fc3652b58cc2d2b8bfb72f6e86d)
- [HL78XX_CTZEU_UTIME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaea97e8a895c9bad91eead2e631934bda)
- [HL78XX_CEREG_TIMER_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0d3e4dcb509b56886297f2f451f4d952)
- [HL78XX_NETWORK_ADDRESS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1dd356d88b67261a642ba50730b31b48)
- [MDM_HL78XX_EOF_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8bc5d49dd46c8bff682528127310a1eb)
- [MDM_HL78XX_TERMINATION_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga00e8685b8a1c0b4a9b5ba18dfdd7c879)
- [MDM_HL78XX_CONNECT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab53f7ed6e7b4b70f7675184e666bf9f0)
- [MDM_HL78XX_NO_CARRIER_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae2b96cddac89ab608658fe11bfdac45e)
- [MDM_HL78XX_CME_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1760f6b6b71f238b2e4a4f2082899dd7)
- [MDM_HL78XX_CMS_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga65d332f108a5cbc6e3038db4fa2fee65)
- [MDM_HL78XX_ERROR_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac06ec76b0de379682110e590c4b400de)
- [MDM_HL78XX_OK_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga08eaa30cab6c59b2b4e9e33ff8c12704)
- [MDM_HL78XX_DESIRED_VERSION_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6b0f0f61bd70c9e09031ecdb9dcf2f52)
- [HL78XX_MONITOR_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0381c6c5a47121b422c0f5d456e86432)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [HL78XX_MONITOR_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac485491202b429e8512c210360d1b2f9)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [HL78XX_MONITOR_INITIAL_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabe2427817d9dea113ac5f748b9148357)
- [HL78XX_EVT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa23bb8ced0d5b912309228525736234a)
- [HL78XX_AT_MONITOR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga48b0f02ea31d612d867db6bf2a62fb46)
- [HL78XX_AT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadc4cc789837650b5e20e9bf5f6d85067)
- [HL78XX_AT_MONITOR_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga370b450dc0ab247343d3406e7fc664da)
- [GNSS_AUX_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7da0c70a3435693c416c28a27b4ab1c5)
- [GNSS_DT_AUX_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab77a5c59a2b5297b7bc69afffb21dc73)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [hl78xx_runtime_band_provider_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga82793d1f4c0c8f03ae27b29afa1c3d3f)
- [device](../device_reference/P002_设备对象结构.md)
- [hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [hl78xx_gnss_aux_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9198bafcc7c78243fc72ca2b0bc926ed)
- [hl78xx_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03910e4575bfd4ed439e1c9a0220c7a2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hl78xx_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6bf75bd8e583b4e076b73268a712977d)
- [hl78xx_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a)
- [cellular_signal_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga746c0862b9a5da7c766e42e4d6025f47)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [hl78xx_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa7cb75a0ef3cd4cb607bb0e3f3b3468f)
- [cellular_modem_info_type](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#gad6e38e31d82075c51933fcbb2ff2de30)
- [hl78xx_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga586f65e3f3ea8852261be04ce7ba67ba)
- [cellular_access_technology](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga168002533ce39996e68bda2c2e92428e)
- [cellular_registration_status](../api_media_cellular_topic_reference/P009_蜂窝通信（Cellular）.md#ga7309390ed507748fdb72cf078b8e08a4)
- [hl78xx_api_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cf1c4b11a828c186771200cd00b3bc8)
- [hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)
- [hl78xx_api_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3bcb3ba4cef24971acc41aa0815abe5)
- [hl78xx_api_send_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8201489ac8055efa3019ffd8f3201644)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [hl78xx_at_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98fde2c3465abce3b4b7d94816bc029c)
- [hl78xx_at_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga517a58c85701991214ddb3a9d786f367)
- [hl78xx_evt_monitor_dispatcher_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gade4999c5b603813020cd52a93687b76f)
- [hl78xx_evt_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa1346c7b8b44abae64f59cc8d5fa9c01)
- [hl78xx_evt_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga774bbdee241bfb63374fdc74d2353a3d)
- [HL78XX_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b)
- [HL78XX_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e)
- [HL78XX_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d)
- [HL78XX_RAT_NBNTN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d)
- [HL78XX_RAT_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b)
- [HL78XX_RAT_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f)
- [HL78XX_RAT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422)
- [hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)
- [HL78XX_KSELACQ_RAT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850)
- [HL78XX_KSELACQ_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f)
- [HL78XX_KSELACQ_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca)
- [HL78XX_KSELACQ_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30)
- [HL78XX_SIM_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf)
- [HL78XX_FULLY_FUNCTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba)
- [HL78XX_AIRPLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570)
- [hl78xx_sim_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0b3efb75d166d9d4bf163ffc6bb68fc0)
- [HL78XX_SIM_SLOT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576)
- [HL78XX_SIM_SLOT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794)
- [hl78xx_modem_restart_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga618c248d23a1db1b027333c92adf99a1)
- [HL78XX_MODEM_RESTART_HARD](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc)
- [HL78XX_MODEM_RESTART_SOFT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8)
- [hl78xx_module_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab4a85c57d2f77c04a887f6552abff48a)
- [HL78XX_MODULE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db)
- [HL78XX_MODULE_WAITING_FOR_ACCESS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820)
- [HL78XX_MODULE_SIM_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9)
- [HL78XX_MODULE_SIMLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f)
- [HL78XX_MODULE_UNRECOVERABLE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294)
- [HL78XX_MODULE_UNKNOWN_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6)
- [HL78XX_MODULE_INACTIVE_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3)
- [hl78xx_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaadcca229cbccc9832734bcc4e2a443e6)
- [HL78XX_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8)
- [HL78XX_MODEM_INFO_CURRENT_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd)
- [HL78XX_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca)
- [hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)
- [HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c)
- [HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164)
- [HL78XX_OPERATOR_FORMAT_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9)
- [hl78xx_network_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga563d651fff3621c1e21d7c47d19fd218)
- [HL78XX_NETWORK_INFO_APN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe)
- [HL78XX_NETWORK_INFO_CURRENT_RAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a)
- [HL78XX_NETWORK_INFO_OPERATOR_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520)
- [HL78XX_NETWORK_INFO_TAC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f)
- [HL78XX_NETWORK_INFO_MCC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c)
- [HL78XX_NETWORK_INFO_MNC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb)
- [HL78XX_NETWORK_INFO_CELL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650)
- [HL78XX_NETWORK_INFO_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771)
- [HL78XX_NETWORK_INFO_DNS_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73)
- [HL78XX_NETWORK_INFO_ACTIVE_BAND](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc)
- [HL78XX_NETWORK_INFO_SINR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48)
- [nmea_output_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabb0e5a4dd5c2e29d62ba27f6022f01f5)
- [NMEA_OUTPUT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9)
- [NMEA_OUTPUT_USB_NMEA_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c)
- [NMEA_OUTPUT_UART1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589)
- [NMEA_OUTPUT_SAME_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3)
- [NMEA_OUTPUT_CMUX_DLC1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf)
- [NMEA_OUTPUT_CMUX_DLC2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f)
- [NMEA_OUTPUT_CMUX_DLC3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d)
- [NMEA_OUTPUT_CMUX_DLC4](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1)
- [hl78xx_agnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d4975dffccffac27c9dccb85c02d549)
- [HL78XX_AGNSS_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288)
- [HL78XX_AGNSS_MODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d)
- [hl78xx_agnss_days](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae9cf9c13242bc674dd7b0b79a69b8f31)
- [HL78XX_AGNSS_DAYS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876)
- [HL78XX_AGNSS_DAYS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34)
- [HL78XX_AGNSS_DAYS_3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8)
- [HL78XX_AGNSS_DAYS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a)
- [HL78XX_AGNSS_DAYS_14](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816)
- [HL78XX_AGNSS_DAYS_28](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459)
- [power_down_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6340324dcb76101c66b902bb9a14dbd3)
- [POWER_DOWN_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa)
- [POWER_DOWN_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1)
- [POWER_DOWN_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b)
- [hl78xx_power_down_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga50bd06a27371c5c79de5bef125d6b5f3)
- [HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a)
- [HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985)
- [HL78XX_POWER_DOWN_RESPONSE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e)
- [hl78xx_edrx_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5d8a5b00f354e98abc2effa560f3bac8)
- [HL78XX_EDRX_EVENT_IDLE_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8)
- [HL78XX_EDRX_EVENT_IDLE_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5)
- [HL78XX_EDRX_EVENT_IDLE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a)
- [hl78xx_psmev_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae891e3155a0ebf72433dd58ae4c36512)
- [HL78XX_PSM_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94)
- [HL78XX_PSM_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda)
- [HL78XX_PSM_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553)
- [hl78xx_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8a864475f6e9673f85ec7c56028992a5)
- [HL78XX_LTE_RAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5)
- [HL78XX_LTE_REGISTRATION_STAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95)
- [HL78XX_LTE_SIM_REGISTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9)
- [HL78XX_LTE_MODEM_STARTUP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839)
- [HL78XX_LTE_FOTA_UPDATE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92)
- [HL78XX_LTE_DNS_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8)
- [HL78XX_LTE_AT_CMD_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73)
- [HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5)
- [HL78XX_LTE_CTZEU_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6)
- [HL78XX_GNSS_ENGINE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b)
- [HL78XX_GNSS_EVENT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae)
- [HL78XX_GNSS_EVENT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5)
- [HL78XX_GNSS_EVENT_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61)
- [HL78XX_GNSS_EVENT_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c)
- [HL78XX_GNSS_EVENT_START_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07)
- [HL78XX_GNSS_EVENT_SEARCH_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429)
- [HL78XX_GNSS_EVENT_MODE_EXITED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916)
- [HL78XX_EDRX_IDLE_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3)
- [HL78XX_LTE_PSMEV_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7)
- [HL78XX_POWER_DOWN_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2)
- [HL78XX_VGPIO_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc)
- [HL78XX_VGPIO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63)
- [HL78XX_GPIO6_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe)
- [HL78XX_GPIO6_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52)
- [HL78XX_CELLMEAS_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254)
- [HL78XX_EVT_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790)
- [wdsi_indication](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5453000edbd52c54f7193de4852aa9a8)
- [WDSI_BOOTSTRAP_CREDENTIALS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339)
- [WDSI_USER_AGREEMENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2)
- [WDSI_FIRMWARE_DOWNLOAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68)
- [WDSI_FIRMWARE_INSTALL_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5)
- [WDSI_AUTHENTICATION_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1)
- [WDSI_AUTHENTICATION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6)
- [WDSI_AUTHENTICATION_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608)
- [WDSI_CONNECTION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a)
- [WDSI_DM_SESSION_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2)
- [WDSI_FIRMWARE_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8)
- [WDSI_FIRMWARE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd)
- [WDSI_FIRMWARE_DOWNLOAD_ISSUE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184)
- [WDSI_PACKAGE_VERIFIED_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7)
- [WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5)
- [WDSI_FIRMWARE_UPDATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458)
- [WDSI_FIRMWARE_UPDATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc)
- [WDSI_FIRMWARE_UPDATE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f)
- [WDSI_DOWNLOAD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0)
- [WDSI_SESSION_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d)
- [hl78xx_gnss_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga95d1ccc5899adf1b2eda6aa0777b7e80)
- [HL78XX_GNSSEV_INITIALISATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21)
- [HL78XX_GNSSEV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740)
- [HL78XX_GNSSEV_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da)
- [HL78XX_GNSSEV_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533)
- [hl78xx_event_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9b9da1841754d723cddc103800b141ae)
- [HL78XX_STATUS_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e)
- [HL78XX_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd)
- [gnss_position_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2a471bc1b92dba1e316b2b27e3778e1a)
- [GNSS_FIX_LOST_OR_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d)
- [GNSS_ESTIMATED_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306)
- [GNSS_2D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8)
- [GNSS_3D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407)
- [GNSS_FIX_CHANGED_TO_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa)
- [hl78xx_api_func_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaab36b1992acffc8b25b8140da1a79577)
- [hl78xx_api_func_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad39b680650d8a3f1ea20bc18fa6101d4)
- [hl78xx_api_func_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaca72419e4396a45b296a65f89877dbb8)
- [hl78xx_api_func_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae50586b4f939abacda6739850c118982)
- [hl78xx_api_func_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5f9c8c8087e1e6008f290ddfe42e3d97)
- [hl78xx_api_func_get_modem_info_standard](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacddf878e52d0642279e147add9c8bdad)
- [hl78xx_api_func_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac08824e4662cb5fcb316e6a0e1e5ba17)
- [hl78xx_api_func_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadd718f794b24c9610e97f7460519e577)
- [hl78xx_api_func_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga79c8b3e0581e6418526b3aa86e6bbb5a)
- [hl78xx_api_func_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga069a0709408fef75514dfaf12bc42cb5)
- [hl78xx_api_func_set_network_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab8e5ae21bd129d61735c9cfe3df557d2)
- [hl78xx_api_func_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gafc8c324c2beb2c59c9f15542d06b85ee)
- [hl78xx_api_func_get_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga4c2dc7d53dd4780d8f1e00e9889248d3)
- [hl78xx_api_func_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1640ce244f1a4de52efa0b7c33f7b02a)
- [hl78xx_api_func_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6adcbc5395d078be2fc9c6e62612f603)
- [hl78xx_set_runtime_band_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac6ed6d4f41003cb2517f802762d5b239)
- [hl78xx_api_func_modem_dynamic_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3f2ed904a3b0784d64d2d1537ce9564)
- [hl78xx_modem_at_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga45a97bfc5f73d1877357dc1f410c61cd)
- [hl78xx_modem_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga3e9edd942cbf32b5a2eec259c44e5ee4)
- [hl78xx_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabe520e9e9a5e48ab05e238f6b59b8cda)
- [hl78xx_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaedfc9112048d6c987ee7fefa4e8abd55)
- [hl78xx_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga65f087ad92a0f2bfb15d4f7b627c754f)
- [hl78xx_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab49ab6eb5aa0cfcdea4e6e7bcabd1d48)
- [hl78xx_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga06800817986b9a4b0291cc22c808dfae)
- [hl78xx_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad564df9a12ad4ee40caeffec1099a93b)
- [hl78xx_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaad6374b5c5ef64886c6d8fdde0cba3c4)
- [hl78xx_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad2673b87d730da42b4d2109e849277cc)
- [hl78xx_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaee99182459b5971ebaa7892989b0e8df)
- [hl78xx_restart_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2c4ff4a9b1d5d2530700327e1d4af6e0)
- [hl78xx_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf778d092ad7f9b67b0930c0da2375996)
- [hl78xx_modem_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae7102c14fda882e87bff0f0828ab4263)
- [hl78xx_modem_at_err_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaba7b5c599c1b9285b9dcfbae91ac5e7f)
- [hl78xx_modem_at_err](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga13ead2b7a66530a1fbe15e5c4d9addeb)
- [hl78xx_parse_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9dd8be5c6d35de4122ab5604bf5b17ce)
- [hl78xx_parse_rsrp](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8abfb51de22c24f1870d2b5f4b3b60ee)
- [hl78xx_parse_rsrq](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga09f7b39a934d38a2d3da8deefc3d2758)
- [hl78xx_evt_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadfb6a494068c978908ed0bd968b81a5f)
- [hl78xx_evt_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3a63acd15fc9bd6a7d9ded9ed1731fa)
- [hl78xx_at_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab08189be0b4dc7f03428d829f0170bbe)
- [hl78xx_at_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2723fa7f912913d299629fdba4efb130)
- [hl78xx_at_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga051a63a86e9ca353434b23e1adf5d543)
- [hl78xx_at_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1244a8f6b7e5e488ab596aa5341ad66a)
- [hl78xx_evt_notif_handler_set](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8265e020ad0d8c3e69f2219173530720)
- [hl78xx_evt_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6590e5352cbd8ff6ea0580edd64eb0d0)
- [hl78xx_evt_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf4c623e7bed92b6ea3964b59df04e98e)
- [hl78xx_rat_to_access_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf8cbf3de84df41d7066b9a07f106c17b)
- [hl78xx_access_tech_to_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac9f87f986b0b745bf8e370896113066f)
- [hl78xx_start_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf34ed3d29904f1a18c0c75a0de4bc727)
- [hl78xx_stop_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9018c8332803eaada4083390c40ac3f0)
- [hl78xx_set_wake_pin_low](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga803bf7a13a7b57477dbfa4d6b3faa14e)
- [hl78xx_set_wake_pin_high](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3e97cdf80470496d6d8542f61f985c0)
- [hl78xx_set_active_sim](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9bac621e2f74d598329f61cd95b0291b)
- [hl78xx_wakeup_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cc4861b1449b551246204b84779c621)
- [hl78xx_edrx_get_time_to_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga41d66fc0e8681bf6a68f47af5bcacb90)
- [hl78xx_enter_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9e9d288506708b275cc98e508bc8251d)
- [hl78xx_exit_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga475545d83cf5fd883fd11fb0db8400ed)
- [hl78xx_queue_gnss_search](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga48f504b9bb41d4a13ac592f763aeb207)
- [hl78xx_gnss_set_nmea_output](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5a1949cd23380056b4ee1775b1e6cc3b)
- [hl78xx_gnss_set_search_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae349d6b96ef9ae67b5ed01d0a8fa2cb0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [hl78xx_gnss_get_search_timeout_remaining](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga209d0579899aef4ade5cf8de1251a323)
- [hl78xx_gnss_get_latest_known_fix](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0238b9a2de4683369a0be7a6ed481938)
- [hl78xx_gnss_assist_data_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga473c72484a8a758470ff7043de7ab48d)
- [hl78xx_gnss_assist_data_download](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabf8fcaa1b5a59d5a2cac3c467f93c9f8)
- [hl78xx_gnss_assist_data_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga452b1ee210417569b3cdfc30db25622a)
- [hl78xx_power_down_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac7291340f8699bb37cd864516615ea05)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [hl78xx_power_down_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98af31968e3bf0fc72dea5d56e97e122)
- [hl78xx_power_down_respond](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga249a5bf6cdbd69ec930724bf2541de72)
- [hl78xx_power_down_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2bcaada6a58dfbe3658fc6bcb3090fff)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__net__lwm2m.h_文件参考.md)
