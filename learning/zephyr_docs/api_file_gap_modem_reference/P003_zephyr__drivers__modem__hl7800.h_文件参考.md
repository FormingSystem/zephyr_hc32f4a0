---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-3
title: zephyr__drivers__modem__hl7800.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_modem\_\_hl7800.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HL7800调制解调器（Modem）的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <time.h>
```

查看此文件的源码。

HL7800 调制解调器（Modem）的公共 API 头文件，允许应用控制 HL7800 调制解调器。Copyright (c) 2020 Laird Connectivity；SPDX-License-Identifier: Apache-2.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_mdm_5Fhl7800_5Fapn"></a>

```c
struct mdm_hl7800_apn
```

相关声明：[mdm_hl7800_apn](../modem_wireless_model_reference/P035_mdm_hl7800_apn_结构体.md)。

接入点名称（Access Point Name，APN）的配置。

<a id="r_mdm_5Fhl7800_5Fsite_5Fsurvey"></a>

```c
struct mdm_hl7800_site_survey
```

相关声明：[mdm_hl7800_site_survey](../modem_wireless_model_reference/P040_mdm_hl7800_site_survey_结构体.md)。

现场勘测结果（Site Survey Result）。

<a id="r_mdm_5Fhl7800_5Fcompound_5Fevent"></a>

```c
struct mdm_hl7800_compound_event
```

相关声明：[mdm_hl7800_compound_event](../modem_wireless_model_reference/P037_mdm_hl7800_compound_event_结构体.md)。

由代码和字符串组成的事件数据（Event Data）。

<a id="r_mdm_5Fhl7800_5Fpolte_5Fregistration_5Fevent_5Fdata"></a>

```c
struct mdm_hl7800_polte_registration_event_data
```

相关声明：[mdm_hl7800_polte_registration_event_data](../modem_wireless_model_reference/P039_mdm_hl7800_polte_registration_event_data_结构体.md)。

PoLTE注册结果（Registration Result）。

<a id="r_mdm_5Fhl7800_5Fpolte_5Flocation_5Fdata"></a>

```c
struct mdm_hl7800_polte_location_data
```

相关声明：[mdm_hl7800_polte_location_data](../modem_wireless_model_reference/P038_mdm_hl7800_polte_location_data_结构体.md)。

PoLTE定位响应（Location Response）。

<a id="r_mdm_5Fhl7800_5Fcallback_5Fagent"></a>

```c
struct mdm_hl7800_callback_agent
```

相关声明：[mdm_hl7800_callback_agent](../modem_wireless_model_reference/P036_mdm_hl7800_callback_agent_结构体.md)。

事件回调注册（Event Callback Registration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga2a9d979df7a39d049f341ce3706343a1"></a>

```c
#define MDM_HL7800_REVISION_MAX_SIZE 29
```

相关声明：[MDM_HL7800_REVISION_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2a9d979df7a39d049f341ce3706343a1)。

固件修订版本字符串（Firmware Revision String）的大小，包括结尾的 `NUL`。

<a id="r_ga506266d9f3df21657fa27c92e2a4b3a9"></a>

```c
#define MDM_HL7800_REVISION_MAX_STRLEN (MDM_HL7800_REVISION_MAX_SIZE - 1)
```

相关声明：[MDM_HL7800_REVISION_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga506266d9f3df21657fa27c92e2a4b3a9)、[MDM_HL7800_REVISION_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2a9d979df7a39d049f341ce3706343a1)。

固件修订版本字符串（Firmware Revision String）的最大长度。

<a id="r_gaadb01caea83021e2a32f863372e0bc40"></a>

```c
#define MDM_HL7800_IMEI_SIZE 16
```

相关声明：[MDM_HL7800_IMEI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaadb01caea83021e2a32f863372e0bc40)。

国际移动设备标识（International Mobile Equipment Identity，IMEI）字符串的大小，包括结尾的 `NUL`。

<a id="r_gaec5666644e15e4bfb8970815488c273e"></a>

```c
#define MDM_HL7800_IMEI_STRLEN (MDM_HL7800_IMEI_SIZE - 1)
```

相关声明：[MDM_HL7800_IMEI_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaec5666644e15e4bfb8970815488c273e)、[MDM_HL7800_IMEI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaadb01caea83021e2a32f863372e0bc40)。

IMEI 字符串的长度。

<a id="r_ga633ec3cdd878098287fea81ee7b02b43"></a>

```c
#define MDM_HL7800_ICCID_MAX_SIZE 21
```

相关声明：[MDM_HL7800_ICCID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga633ec3cdd878098287fea81ee7b02b43)。

集成电路卡标识符（Integrated Circuit Card Identifier，ICCID）字符串的大小，包括结尾的 `NUL`。

<a id="r_ga32865364e6fd4641b9be897bfd6c293f"></a>

```c
#define MDM_HL7800_ICCID_MAX_STRLEN (MDM_HL7800_ICCID_MAX_SIZE - 1)
```

相关声明：[MDM_HL7800_ICCID_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga32865364e6fd4641b9be897bfd6c293f)、[MDM_HL7800_ICCID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga633ec3cdd878098287fea81ee7b02b43)。

ICCID 字符串的最大长度。

<a id="r_gae842bbecef777b83225577189205e085"></a>

```c
#define MDM_HL7800_SERIAL_NUMBER_SIZE 15
```

相关声明：[MDM_HL7800_SERIAL_NUMBER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae842bbecef777b83225577189205e085)。

序列号字符串（Serial Number String）的大小，包括结尾的 `NUL`。

<a id="r_ga10594faa869ccfdcd9d51309cf52d7c7"></a>

```c
#define MDM_HL7800_SERIAL_NUMBER_STRLEN (MDM_HL7800_SERIAL_NUMBER_SIZE - 1)
```

相关声明：[MDM_HL7800_SERIAL_NUMBER_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga10594faa869ccfdcd9d51309cf52d7c7)、[MDM_HL7800_SERIAL_NUMBER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae842bbecef777b83225577189205e085)。

序列号字符串（Serial Number String）的长度。

<a id="r_ga5cc5aad6ab04405999246790dd850046"></a>

```c
#define MDM_HL7800_APN_MAX_SIZE 64
```

相关声明：[MDM_HL7800_APN_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5cc5aad6ab04405999246790dd850046)。

接入点名称（Access Point Name，APN）的大小，包括结尾的 `NUL`。

<a id="r_gacb5d0f96845b17b84c746dcea6bd732a"></a>

```c
#define MDM_HL7800_APN_USERNAME_MAX_SIZE 65
```

相关声明：[MDM_HL7800_APN_USERNAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gacb5d0f96845b17b84c746dcea6bd732a)。

APN 用户名（Username）的大小，包括结尾的 `NUL`。

<a id="r_gabc1a2d9744225bc82f3f4b14d365a0fe"></a>

```c
#define MDM_HL7800_APN_PASSWORD_MAX_SIZE 65
```

相关声明：[MDM_HL7800_APN_PASSWORD_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gabc1a2d9744225bc82f3f4b14d365a0fe)。

APN 密码（Password）的大小，包括结尾的 `NUL`。

<a id="r_gaf58865f84686e963f5c3fdff2eaea26a"></a>

```c
#define MDM_HL7800_APN_MAX_STRLEN (MDM_HL7800_APN_MAX_SIZE - 1)
```

相关声明：[MDM_HL7800_APN_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf58865f84686e963f5c3fdff2eaea26a)、[MDM_HL7800_APN_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5cc5aad6ab04405999246790dd850046)。

接入点名称（Access Point Name，APN）的最大长度。

<a id="r_ga80f2f5814be64d8ad75b5ced8017ca0d"></a>

```c
#define MDM_HL7800_APN_USERNAME_MAX_STRLEN (MDM_HL7800_APN_USERNAME_MAX_SIZE - 1)
```

相关声明：[MDM_HL7800_APN_USERNAME_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga80f2f5814be64d8ad75b5ced8017ca0d)、[MDM_HL7800_APN_USERNAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gacb5d0f96845b17b84c746dcea6bd732a)。

APN 用户名（Username）的最大长度。

<a id="r_ga2e0973dd337183b6df1209df6a70e017"></a>

```c
#define MDM_HL7800_APN_PASSWORD_MAX_STRLEN (MDM_HL7800_APN_PASSWORD_MAX_SIZE - 1)
```

相关声明：[MDM_HL7800_APN_PASSWORD_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2e0973dd337183b6df1209df6a70e017)、[MDM_HL7800_APN_PASSWORD_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gabc1a2d9744225bc82f3f4b14d365a0fe)。

APN 密码（Password）的最大长度。

<a id="r_ga8364e415a31bdce35ce76039de657b36"></a>

```c
#define MDM_HL7800_LTE_BAND_STR_SIZE 21
```

相关声明：[MDM_HL7800_LTE_BAND_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8364e415a31bdce35ce76039de657b36)。

LTE 频段配置字符串（Band Configuration String）的大小，包括结尾的 `NUL`。

<a id="r_ga3381c94afeaabed84e2027d4b947df2d"></a>

```c
#define MDM_HL7800_LTE_BAND_STRLEN (MDM_HL7800_LTE_BAND_STR_SIZE - 1)
```

相关声明：[MDM_HL7800_LTE_BAND_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3381c94afeaabed84e2027d4b947df2d)、[MDM_HL7800_LTE_BAND_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8364e415a31bdce35ce76039de657b36)。

LTE 频段配置字符串（Band Configuration String）的最大长度。

<a id="r_ga523acdbfa564f3e83d93f7fbc50b8bc8"></a>

```c
#define MDM_HL7800_IMSI_MIN_STR_SIZE 15
```

相关声明：[MDM_HL7800_IMSI_MIN_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga523acdbfa564f3e83d93f7fbc50b8bc8)。

国际移动用户标识（International Mobile Subscriber Identity，IMSI）字符串的最小大小，包括结尾的 `NUL`。

<a id="r_gac93538b6d4666aed22cef92b71e63df7"></a>

```c
#define MDM_HL7800_IMSI_MAX_STR_SIZE 16
```

相关声明：[MDM_HL7800_IMSI_MAX_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gac93538b6d4666aed22cef92b71e63df7)。

IMSI 字符串的最大大小，包括结尾的 `NUL`。

<a id="r_ga645750b25f14ccfb2b6137243081a7ad"></a>

```c
#define MDM_HL7800_IMSI_MAX_STRLEN (MDM_HL7800_IMSI_MAX_STR_SIZE - 1)
```

相关声明：[MDM_HL7800_IMSI_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga645750b25f14ccfb2b6137243081a7ad)、[MDM_HL7800_IMSI_MAX_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gac93538b6d4666aed22cef92b71e63df7)。

IMSI 字符串的最大长度。

<a id="r_gaf4840e7a40163477ccd00601467a8e8f"></a>

```c
#define MDM_HL7800_MAX_GPS_STR_SIZE 33
```

相关声明：[MDM_HL7800_MAX_GPS_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf4840e7a40163477ccd00601467a8e8f)。

GPS 字符串的大小，包括结尾的 `NUL`。

<a id="r_ga10db6322599d499eccf8116f692a42e1"></a>

```c
#define MDM_HL7800_MAX_POLTE_USER_ID_SIZE 16
```

相关声明：[MDM_HL7800_MAX_POLTE_USER_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga10db6322599d499eccf8116f692a42e1)。

PoLTE 用户 ID 字符串（User ID String）的大小，包括结尾的 `NUL`。

<a id="r_ga781329540d46b975eb8d6bf9870cf4a8"></a>

```c
#define MDM_HL7800_MAX_POLTE_PASSWORD_SIZE 16
```

相关声明：[MDM_HL7800_MAX_POLTE_PASSWORD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga781329540d46b975eb8d6bf9870cf4a8)。

PoLTE 密码字符串（Password String）的大小，包括结尾的 `NUL`。

<a id="r_ga060fccbbb60656b655abb3a8ad59f428"></a>

```c
#define MDM_HL7800_MAX_POLTE_LOCATION_STR_SIZE 33
```

相关声明：[MDM_HL7800_MAX_POLTE_LOCATION_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga060fccbbb60656b655abb3a8ad59f428)。

PoLTE 位置字符串（Location String）的大小，包括结尾的 `NUL`。

<a id="r_gafbafa9aa28ebfdca72e19fca6cb944ea"></a>

```c
#define MDM_HL7800_POLTE_SERVER_ERROR 10
```

相关声明：[MDM_HL7800_POLTE_SERVER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafbafa9aa28ebfdca72e19fca6cb944ea)。

无法访问 PoLTE 服务器时，`HL7800_EVENT_POLTE` 报告的状态。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_gafa044d03d9bfbc2f63088da4f094edfc"></a>

```c
typedef void(* mdm_hl7800_event_callback_t) (enum mdm_hl7800_event event, void *event_data)
```

相关声明：[mdm_hl7800_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa044d03d9bfbc2f63088da4f094edfc)、[mdm_hl7800_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3f7b0647d9ff01328e5536478a73aaf9)。

事件回调（Event Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga2d26759e8ea3aca2e8e4a6cccac2361a"></a>

```c
enum mdm_hl7800_radio_mode { MDM_RAT_CAT_M1 = 0 , MDM_RAT_CAT_NB1 }
```

相关声明：[mdm_hl7800_radio_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2d26759e8ea3aca2e8e4a6cccac2361a)、[MDM_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga2d26759e8ea3aca2e8e4a6cccac2361aac95a4a3318b0683972336c1036f0548e)、[MDM_RAT_CAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga2d26759e8ea3aca2e8e4a6cccac2361aa30bba3902918ea11995cd3db20319d61)。

无线接入技术（Radio Access Technology，RAT）。

<a id="r_ga3f7b0647d9ff01328e5536478a73aaf9"></a>

```c
enum mdm_hl7800_event { HL7800_EVENT_RESERVED = 0 , HL7800_EVENT_NETWORK_STATE_CHANGE , HL7800_EVENT_APN_UPDATE , HL7800_EVENT_RSSI , HL7800_EVENT_SINR , HL7800_EVENT_STARTUP_STATE_CHANGE , HL7800_EVENT_SLEEP_STATE_CHANGE , HL7800_EVENT_RAT , HL7800_EVENT_BANDS , HL7800_EVENT_ACTIVE_BANDS , HL7800_EVENT_FOTA_STATE , HL7800_EVENT_FOTA_COUNT , HL7800_EVENT_REVISION , HL7800_EVENT_GPS , HL7800_EVENT_GPS_POSITION_STATUS , HL7800_EVENT_POLTE_REGISTRATION , HL7800_EVENT_POLTE_LOCATE_STATUS , HL7800_EVENT_POLTE , HL7800_EVENT_SITE_SURVEY , HL7800_EVENT_STATE }
```

相关声明：[mdm_hl7800_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3f7b0647d9ff01328e5536478a73aaf9)、[HL7800_EVENT_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7147e1d7ea1df5eb7604c3246a94ec0a)、[HL7800_EVENT_NETWORK_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a08a58f10e3d58022ac945b2e68d4145a)、[HL7800_EVENT_APN_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a4cf6f0344fa2348f378756e77d5f2804)、[HL7800_EVENT_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9abb822dfaec7e96462be791857f9b3fba)、[HL7800_EVENT_SINR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9ac76f3fec60d1ffeca58405cf38bd50fe)、[HL7800_EVENT_STARTUP_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a0d25a89cd39d581c82ae73fe0a85ba21)、[HL7800_EVENT_SLEEP_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7bd6e3e3c19ed2c5ac138c16e03b2562)、[HL7800_EVENT_RAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9ac22e246ac6bc5794ae0772bf3dbf5086)、[HL7800_EVENT_BANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a327cd78d882a1a36716236f2cdf28c31)、[HL7800_EVENT_ACTIVE_BANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aad01f254032296551f621c888530e9d1)、[HL7800_EVENT_FOTA_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aedd9ae54dfa7a007c18e2a345d0cb0c5)、[HL7800_EVENT_FOTA_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a3848abb978d465bd0a831fc0b66a33c3)、[HL7800_EVENT_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a8a3b921d5bdb205f44576852467c38e2)、[HL7800_EVENT_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9af3410e6ff2caa844c3b6f9963df485d1)、[HL7800_EVENT_GPS_POSITION_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a0b9e7d1fcb8f043c5ac0b242e4c6c772)、[HL7800_EVENT_POLTE_REGISTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aead019c4cd55d1f54fb16ddef7f8277c)、[HL7800_EVENT_POLTE_LOCATE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7ee246b282ac147aafa45969060c5280)、[HL7800_EVENT_POLTE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a1fb1cd6b652c52ebf12e9741649f8630)、[HL7800_EVENT_SITE_SURVEY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a37463d52131771a296fb141c797b3e14)、[HL7800_EVENT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a9189ebbdcf3175881a0e55ac9867acbf)。

向 `mdm_hl7800_event_callback_t` 报告的事件类型（Event Type）。

<a id="r_ga4b00cc03cc14b3812bed4a57aeea822c"></a>

```c
enum mdm_hl7800_state { HL7800_STATE_NOT_READY = 0 , HL7800_STATE_INITIALIZED }
```

相关声明：[mdm_hl7800_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4b00cc03cc14b3812bed4a57aeea822c)、[HL7800_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga4b00cc03cc14b3812bed4a57aeea822caccfc2361ab2bea50b510c428786a9a07)、[HL7800_STATE_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga4b00cc03cc14b3812bed4a57aeea822ca44858cd6e73be2697e39f60aa54565be)。

驱动状态（Driver State）。

<a id="r_gaefcf9c39983d8f3f58bcd1a24ca04e99"></a>

```c
enum mdm_hl7800_startup_state { HL7800_STARTUP_STATE_READY = 0 , HL7800_STARTUP_STATE_WAITING_FOR_ACCESS_CODE , HL7800_STARTUP_STATE_SIM_NOT_PRESENT , HL7800_STARTUP_STATE_SIMLOCK , HL7800_STARTUP_STATE_UNRECOVERABLE_ERROR , HL7800_STARTUP_STATE_UNKNOWN , HL7800_STARTUP_STATE_INACTIVE_SIM }
```

相关声明：[mdm_hl7800_startup_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaefcf9c39983d8f3f58bcd1a24ca04e99)、[HL7800_STARTUP_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99aac2ef169e3273dd11331acae3abb9c6e)、[HL7800_STARTUP_STATE_WAITING_FOR_ACCESS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a60dd736ae85eeafaefce839b623c530f)、[HL7800_STARTUP_STATE_SIM_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a92593373e0efcb87471c6d0325f1c2e6)、[HL7800_STARTUP_STATE_SIMLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a098e678b80c7148972d572f6dac763d6)、[HL7800_STARTUP_STATE_UNRECOVERABLE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a1b88f9edf57f6fe1b9f4b31ecb196632)、[HL7800_STARTUP_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a9d2a5fd088822989fc109cb3add31393)、[HL7800_STARTUP_STATE_INACTIVE_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a9999f1a90165d5996a7a2ff415db53d6)。

调制解调器启动状态（Modem Startup State）。

<a id="r_ga65c8ed3a7c2a2aee39ca65e57f33b773"></a>

```c
enum mdm_hl7800_network_state { HL7800_NOT_REGISTERED = 0 , HL7800_HOME_NETWORK , HL7800_SEARCHING , HL7800_REGISTRATION_DENIED , HL7800_OUT_OF_COVERAGE , HL7800_ROAMING , HL7800_EMERGENCY = 8 , HL7800_UNABLE_TO_CONFIGURE = 0xf0 }
```

相关声明：[mdm_hl7800_network_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga65c8ed3a7c2a2aee39ca65e57f33b773)、[HL7800_NOT_REGISTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a94fe4bdd729ba6df15d9e9aa53998599)、[HL7800_HOME_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a7e5bdc7f85c2d2f6ec62beee156e887d)、[HL7800_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a1ad9a81e5ce65dc6eee98a87f880f86a)、[HL7800_REGISTRATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a4eeb75667b400acaff56ad282bfe6a7c)、[HL7800_OUT_OF_COVERAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773ae3f6d693bbe0d0c09a41a0e013fe5a82)、[HL7800_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a9d7e014131f399f000965803ccb5e889)、[HL7800_EMERGENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a04cac2efa21c949edeefc105effa4a39)、[HL7800_UNABLE_TO_CONFIGURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a2502129bf7729cce4b1b96ac66dfdd86)。

网络注册状态（Network Registration State）。

<a id="r_ga3396149e553c32a597739096efe2aff7"></a>

```c
enum mdm_hl7800_sleep { HL7800_SLEEP_UNINITIALIZED = 0 , HL7800_SLEEP_HIBERNATE , HL7800_SLEEP_AWAKE , HL7800_SLEEP_LITE_HIBERNATE , HL7800_SLEEP_SLEEP }
```

相关声明：[mdm_hl7800_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3396149e553c32a597739096efe2aff7)、[HL7800_SLEEP_UNINITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7af81cd0793c7faded881246c6a44b099a)、[HL7800_SLEEP_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7af1253aa2135a3c1fb0f3a47a1f0265a4)、[HL7800_SLEEP_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7ac7bf9c4685d31858b98d4188747387ba)、[HL7800_SLEEP_LITE_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7a58c8b0b7a63a3f85b14d0cd0eea4b452)、[HL7800_SLEEP_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7a37e4283b77e32e890f7cc3eca3985289)。

睡眠状态（Sleep state）。

<a id="r_ga8ed2ea65436083a9b1a49bb1f64574f3"></a>

```c
enum mdm_hl7800_fota_state { HL7800_FOTA_IDLE , HL7800_FOTA_START , HL7800_FOTA_WIP , HL7800_FOTA_PAD , HL7800_FOTA_SEND_EOT , HL7800_FOTA_FILE_ERROR , HL7800_FOTA_INSTALL , HL7800_FOTA_REBOOT_AND_RECONFIGURE , HL7800_FOTA_COMPLETE }
```

相关声明：[mdm_hl7800_fota_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8ed2ea65436083a9b1a49bb1f64574f3)、[HL7800_FOTA_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3ab7d67051e56e05be47da306377bb8801)、[HL7800_FOTA_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3ae6b160137651a7375551760f938b9da8)、[HL7800_FOTA_WIP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a722b66bd586cc4375253341f1df8d189)、[HL7800_FOTA_PAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a481fdc3814098383af7b593d4f61ea7b)、[HL7800_FOTA_SEND_EOT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3aa78ef13656312bb81aa957a515b337d7)、[HL7800_FOTA_FILE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3aaf2423203fdb79510efa9550e2a09bf9)、[HL7800_FOTA_INSTALL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a6761ef6c52c40786c8b595950499851e)、[HL7800_FOTA_REBOOT_AND_RECONFIGURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a5e517d07a386297b5d80110cabc1864b)、[HL7800_FOTA_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3abd185b07f408b4b7ecb292f31aa6d19a)。

固件更新状态（Firmware Update State）。

<a id="r_gaf999018ef3ca438a9d3cb7b6611300d2"></a>

```c
enum mdm_hl7800_functionality { HL7800_FUNCTIONALITY_MINIMUM = 0 , HL7800_FUNCTIONALITY_FULL = 1 , HL7800_FUNCTIONALITY_AIRPLANE = 4 }
```

相关声明：[mdm_hl7800_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf999018ef3ca438a9d3cb7b6611300d2)、[HL7800_FUNCTIONALITY_MINIMUM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2ae2c5fac661bdf514debc98b3e248cea4)、[HL7800_FUNCTIONALITY_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2ad1e22b662121c8c71b9d34810958b6c2)、[HL7800_FUNCTIONALITY_AIRPLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2a2aca52c7dc8ade5db478f8eaebc4bc33)。

调制解调器功能级别（Modem Functionality Level），遵循 `+CFUN` 的取值。

<a id="r_ga5b6a53d0353ae153f715163ca4e6043b"></a>

```c
enum mdm_hl7800_gnss_event { HL7800_GNSS_EVENT_INVALID = -1 , HL7800_GNSS_EVENT_INIT , HL7800_GNSS_EVENT_START , HL7800_GNSS_EVENT_STOP , HL7800_GNSS_EVENT_POSITION }
```

相关声明：[mdm_hl7800_gnss_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5b6a53d0353ae153f715163ca4e6043b)、[HL7800_GNSS_EVENT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba3349e6599deabd375c68bb3688bd9bfd)、[HL7800_GNSS_EVENT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba3b0b73d5b585d4ed44e00504be60c8ef)、[HL7800_GNSS_EVENT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba689418f8d35440fe71507ee871f20de1)、[HL7800_GNSS_EVENT_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043bae83741a25baa0ffc3837b0653b01c318)、[HL7800_GNSS_EVENT_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba2df7e19144b20afb4bf3566804729db1)。

调制解调器报告的全球导航卫星系统事件（GNSS Event）。

<a id="r_ga5253bceab7f3da57f9a2d3918ee72625"></a>

```c
enum mdm_hl7800_gnss_status { HL7800_GNSS_STATUS_INVALID = -1 , HL7800_GNSS_STATUS_FAILURE , HL7800_GNSS_STATUS_SUCCESS }
```

相关声明：[mdm_hl7800_gnss_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5253bceab7f3da57f9a2d3918ee72625)、[HL7800_GNSS_STATUS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625aadc2b5c2e8b257e8b12ae7c4f5f35d76)、[HL7800_GNSS_STATUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625a830898a215c51c8a17aab3fb175083b3)、[HL7800_GNSS_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625ab989ec2e119be4f23a37cac5203225ab)。

GNSS 事件的状态（Status）。

<a id="r_gaec06e58e1c79e23577d424806b6e696b"></a>

```c
enum mdm_hl7800_gnss_position_event { HL7800_GNSS_POSITION_EVENT_INVALID = -1 , HL7800_GNSS_POSITION_EVENT_LOST_OR_NOT_AVAILABLE_YET , HL7800_GNSS_POSITION_EVENT_PREDICTION_AVAILABLE , HL7800_GNSS_POSITION_EVENT_2D_AVAILABLE , HL7800_GNSS_POSITION_EVENT_3D_AVAILABLE , HL7800_GNSS_POSITION_EVENT_FIXED_TO_INVALID }
```

相关声明：[mdm_hl7800_gnss_position_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaec06e58e1c79e23577d424806b6e696b)、[HL7800_GNSS_POSITION_EVENT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696babf5377809190c648e6f3624b4b0b82ee)、[HL7800_GNSS_POSITION_EVENT_LOST_OR_NOT_AVAILABLE_YET](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696bac41b513dd45d2d038b9d7a4a9bae8fe3)、[HL7800_GNSS_POSITION_EVENT_PREDICTION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696bad41adce29331d1917c97e94b6409a9b5)、[HL7800_GNSS_POSITION_EVENT_2D_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba1cf9c2fe042ab784450451f36b83818d)、[HL7800_GNSS_POSITION_EVENT_3D_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba6bd45fa147597e9c278ec0f27c42efc7)、[HL7800_GNSS_POSITION_EVENT_FIXED_TO_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba9822e7c1f4a238658592a539d18d0c6d)。

`HL7800_EVENT_GPS_POSITION_STATUS` 报告的定位状态（Position Fix Status）。

<a id="r_ga45fd97039bb3add8ddb09f803ce9b038"></a>

```c
enum mdm_hl7800_gps_string_types { HL7800_GPS_STR_LATITUDE , HL7800_GPS_STR_LONGITUDE , HL7800_GPS_STR_GPS_TIME , HL7800_GPS_STR_FIX_TYPE , HL7800_GPS_STR_HEPE , HL7800_GPS_STR_ALTITUDE , HL7800_GPS_STR_ALT_UNC , HL7800_GPS_STR_DIRECTION , HL7800_GPS_STR_HOR_SPEED , HL7800_GPS_STR_VER_SPEED }
```

相关声明：[mdm_hl7800_gps_string_types](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga45fd97039bb3add8ddb09f803ce9b038)、[HL7800_GPS_STR_LATITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a5faac685b9958871cc3feb990e593b8b)、[HL7800_GPS_STR_LONGITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a56f4e3a1a3b2eaacb2c34ec486165de8)、[HL7800_GPS_STR_GPS_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a17989267e59a5169abb7f4d4c8bb3694)、[HL7800_GPS_STR_FIX_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a7cd77b6bf81380fdaba8cdad863a60be)、[HL7800_GPS_STR_HEPE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038aca3dac785dc09cc6d0780c2ce1956de4)、[HL7800_GPS_STR_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a1eac295eb05a3c4617d35c9fd29aebf6)、[HL7800_GPS_STR_ALT_UNC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a39502c1243b0df6765d6025e8173f214)、[HL7800_GPS_STR_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038af5bef33ea67240657038a288f600ec25)、[HL7800_GPS_STR_HOR_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038ac7f6f8e1d00b25b551a1560b7d998fc8)、[HL7800_GPS_STR_VER_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a40e32118c8039cfd3c6ef72c8a4d7f85)。

`HL7800_EVENT_GPS` 报告的 GPS 字符串类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_gae270849872a22823512cc87b0bbf877e"></a>

```c
int32_t mdm_hl7800_power_off (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_power_off](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae270849872a22823512cc87b0bbf877e)。

关闭 HL7800 电源（Power Off）。

<a id="r_ga956932a3c7d45f5ab0c3c99aa1decfb4"></a>

```c
int32_t mdm_hl7800_reset (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga956932a3c7d45f5ab0c3c99aa1decfb4)。

复位（Reset）HL7800，并允许其重新配置。

<a id="r_ga430e2a1e2e8173dab93cf7b1e1fcb24d"></a>

```c
void mdm_hl7800_wakeup (bool awake)
```

相关声明：[mdm_hl7800_wakeup](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga430e2a1e2e8173dab93cf7b1e1fcb24d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制发往 HL7800 的唤醒信号（Wake Signals）。

<a id="r_ga41a1f8f29c6ac8b53e5ef05f156a64a9"></a>

```c
int32_t mdm_hl7800_send_at_cmd (const uint8_t *data, uint8_t resp_timeout, char *resp, uint16_t *resp_len)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_send_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga41a1f8f29c6ac8b53e5ef05f156a64a9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 HL7800 发送 AT 命令（AT Command）。

<a id="r_gad7d20cde62d5e7c987672cc9c10b152e"></a>

```c
void mdm_hl7800_get_signal_quality (int *rsrp, int *sinr)
```

相关声明：[mdm_hl7800_get_signal_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gad7d20cde62d5e7c987672cc9c10b152e)。

获取 HL7800 的信号质量（Signal Quality）。

<a id="r_gaf84e782e572faf543a37a40147660eb0"></a>

```c
char * mdm_hl7800_get_iccid (void)
```

相关声明：[mdm_hl7800_get_iccid](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf84e782e572faf543a37a40147660eb0)。

获取 SIM 卡的 ICCID。

<a id="r_ga1f3a7b2dd7654941006c4a8d5a46af01"></a>

```c
char * mdm_hl7800_get_sn (void)
```

相关声明：[mdm_hl7800_get_sn](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1f3a7b2dd7654941006c4a8d5a46af01)。

获取 HL7800 的序列号（Serial Number）。

<a id="r_ga4278b7f58b77048b8e833d9215183a5f"></a>

```c
char * mdm_hl7800_get_imei (void)
```

相关声明：[mdm_hl7800_get_imei](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4278b7f58b77048b8e833d9215183a5f)。

获取 HL7800 的 IMEI。

<a id="r_gac65dc452be996e5366360abb314a4d98"></a>

```c
char * mdm_hl7800_get_fw_version (void)
```

相关声明：[mdm_hl7800_get_fw_version](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gac65dc452be996e5366360abb314a4d98)。

获取 HL7800 的固件版本（Firmware Version）。

<a id="r_ga581582e3f7b07f04e6b33e481e2d6e42"></a>

```c
char * mdm_hl7800_get_imsi (void)
```

相关声明：[mdm_hl7800_get_imsi](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga581582e3f7b07f04e6b33e481e2d6e42)。

获取 IMSI。

<a id="r_ga3bf4e149e475d8a7c1f462c7de2dda80"></a>

```c
int32_t mdm_hl7800_update_apn (char *access_point_name)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_update_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3bf4e149e475d8a7c1f462c7de2dda80)。

更新调制解调器中的接入点名称（Access Point Name，APN）。

<a id="r_ga9d295b105e71346fcb283959d2641079"></a>

```c
int32_t mdm_hl7800_update_rat (enum mdm_hl7800_radio_mode value)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_update_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga9d295b105e71346fcb283959d2641079)、[mdm_hl7800_radio_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2d26759e8ea3aca2e8e4a6cccac2361a)。

更新无线接入技术（Radio Access Technology，RAT）模式。

<a id="r_ga0b3822e97cbb77f4edab74e8bf2c903e"></a>

```c
bool mdm_hl7800_valid_rat (uint8_t value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mdm_hl7800_valid_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga0b3822e97cbb77f4edab74e8bf2c903e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查无线接入技术（Radio Access Technology）值是否有效。

<a id="r_gafab74f2bd3806a23192cae18f65226ad"></a>

```c
int mdm_hl7800_register_event_callback (struct mdm_hl7800_callback_agent *agent)
```

相关声明：[mdm_hl7800_register_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafab74f2bd3806a23192cae18f65226ad)、[mdm_hl7800_callback_agent](../modem_wireless_model_reference/P036_mdm_hl7800_callback_agent_结构体.md)。

注册在调制解调器事件（Modem Event）发生时调用的函数。

<a id="r_gae2015e7399a17a862048eed89b036c6d"></a>

```c
int mdm_hl7800_unregister_event_callback (struct mdm_hl7800_callback_agent *agent)
```

相关声明：[mdm_hl7800_unregister_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae2015e7399a17a862048eed89b036c6d)、[mdm_hl7800_callback_agent](../modem_wireless_model_reference/P036_mdm_hl7800_callback_agent_结构体.md)。

注销事件回调函数（Event Callback Function）。

<a id="r_gaaac620a4653d772f4d44a73834a8b4cc"></a>

```c
void mdm_hl7800_generate_status_events (void)
```

相关声明：[mdm_hl7800_generate_status_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaaac620a4653d772f4d44a73834a8b4cc)。

强制调制解调器模块生成状态事件（Status Events）。

<a id="r_gafa95fa49240c3412521bade1245bc573"></a>

```c
int32_t mdm_hl7800_get_local_time (struct tm *tm, int32_t *offset)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_get_local_time](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa95fa49240c3412521bade1245bc573)、[tm](../posix_system_model_reference/P025_tm_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

从调制解调器的实时时钟（Real-Time Clock）获取本地时间。

<a id="r_ga4ab20a8fd307c0397d733695b401b031"></a>

```c
int32_t mdm_hl7800_update_fw (char *file_path)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_update_fw](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4ab20a8fd307c0397d733695b401b031)。

通过 XMODEM 协议更新 HL7800。

<a id="r_ga2bb74593dea9486754af21e50f4a6291"></a>

```c
int32_t mdm_hl7800_get_operator_index (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_get_operator_index](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2bb74593dea9486754af21e50f4a6291)。

从调制解调器读取运营商索引（Operator Index）。

<a id="r_ga32dc9651acf319448da38709fc488d16"></a>

```c
int32_t mdm_hl7800_get_functionality (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_get_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga32dc9651acf319448da38709fc488d16)。

获取调制解调器功能状态（Modem Functionality）。

<a id="r_ga1ca397e9e9db680dc6083ba2b4c08a70"></a>

```c
int32_t mdm_hl7800_set_functionality (enum mdm_hl7800_functionality mode)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_set_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1ca397e9e9db680dc6083ba2b4c08a70)、[mdm_hl7800_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf999018ef3ca438a9d3cb7b6611300d2)。

设置飞行（Airplane）、正常（Normal）或精简功能（Reduced Functionality）模式。

<a id="r_ga2946b1d49c63084188f5f6c5dcebaaf2"></a>

```c
int32_t mdm_hl7800_set_gps_rate (uint32_t rate)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_set_gps_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2946b1d49c63084188f5f6c5dcebaaf2)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

`rate` 非零时：将调制解调器置于飞行模式（Airplane Mode）。

<a id="r_ga8501f6d4883ee8577b5cda0f76d2a3dc"></a>

```c
int32_t mdm_hl7800_polte_register (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_polte_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8501f6d4883ee8577b5cda0f76d2a3dc)。

向 `polte.io` 注册调制解调器／SIM。

<a id="r_ga22eb248b7aeb36a1c9895c8de6808f08"></a>

```c
int32_t mdm_hl7800_polte_enable (char *user, char *password)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_polte_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga22eb248b7aeb36a1c9895c8de6808f08)。

启用 PoLTE。

<a id="r_ga1708f077ddb438f93b246b223e52a80d"></a>

```c
int32_t mdm_hl7800_polte_locate (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_polte_locate](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1708f077ddb438f93b246b223e52a80d)。

使用 PoLTE 定位设备（Locate Device）。

<a id="r_ga975a4cd75d9d89dd23b182af2376ef91"></a>

```c
int32_t mdm_hl7800_perform_site_survey (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_perform_site_survey](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga975a4cd75d9d89dd23b182af2376ef91)。

执行现场勘测（Site Survey）。

<a id="r_ga2388ecc33d15263091c63185ccda3ea3"></a>

```c
int mdm_hl7800_set_desired_sleep_level (enum mdm_hl7800_sleep level)
```

相关声明：[mdm_hl7800_set_desired_sleep_level](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2388ecc33d15263091c63185ccda3ea3)、[mdm_hl7800_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3396149e553c32a597739096efe2aff7)。

设置所需的睡眠级别（Sleep Level）。

<a id="r_ga16ac0447c88a9f025fc13009e63f46ef"></a>

```c
void mdm_hl7800_register_wake_test_point_callback (void(*func)(int state))
```

相关声明：[mdm_hl7800_register_wake_test_point_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga16ac0447c88a9f025fc13009e63f46ef)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

允许将 `WAKE_UP` 信号映射到开发板上用户可接触的测试点（Test Point）。

<a id="r_ga0e5213411b27b4c5eeffd746464332a8"></a>

```c
void mdm_hl7800_register_gpio6_callback (void(*func)(int state))
```

相关声明：[mdm_hl7800_register_gpio6_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga0e5213411b27b4c5eeffd746464332a8)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

允许将 `P1.12_GPIO6` 信号映射到开发板上用户可接触的测试点（Test Point）。

<a id="r_gaead5a1419d87676f13fdea12f705b125"></a>

```c
void mdm_hl7800_register_cts_callback (void(*func)(int state))
```

相关声明：[mdm_hl7800_register_cts_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaead5a1419d87676f13fdea12f705b125)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

允许将 `UART1_CTS` 信号映射到开发板上用户可接触的测试点（Test Point）。

<a id="r_ga935e3010e0a2d633e366711c09f634f1"></a>

```c
int32_t mdm_hl7800_set_bands (const char *bands)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mdm_hl7800_set_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga935e3010e0a2d633e366711c09f634f1)。

设置 LTE 连接可用的频段（Bands）。

<a id="r_ga838f6aab78e6f41028d381823cb6b118"></a>

```c
uint32_t mdm_hl7800_log_filter_set (uint32_t level)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mdm_hl7800_log_filter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga838f6aab78e6f41028d381823cb6b118)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置调制解调器的日志级别（Log Level）。


## 3.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P029_hl7800.h_源码浏览.md)
- [mdm_hl7800_apn](../modem_wireless_model_reference/P035_mdm_hl7800_apn_结构体.md)
- [mdm_hl7800_site_survey](../modem_wireless_model_reference/P040_mdm_hl7800_site_survey_结构体.md)
- [mdm_hl7800_compound_event](../modem_wireless_model_reference/P037_mdm_hl7800_compound_event_结构体.md)
- [mdm_hl7800_polte_registration_event_data](../modem_wireless_model_reference/P039_mdm_hl7800_polte_registration_event_data_结构体.md)
- [mdm_hl7800_polte_location_data](../modem_wireless_model_reference/P038_mdm_hl7800_polte_location_data_结构体.md)
- [mdm_hl7800_callback_agent](../modem_wireless_model_reference/P036_mdm_hl7800_callback_agent_结构体.md)
- [MDM_HL7800_REVISION_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2a9d979df7a39d049f341ce3706343a1)
- [MDM_HL7800_REVISION_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga506266d9f3df21657fa27c92e2a4b3a9)
- [MDM_HL7800_IMEI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaadb01caea83021e2a32f863372e0bc40)
- [MDM_HL7800_IMEI_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaec5666644e15e4bfb8970815488c273e)
- [MDM_HL7800_ICCID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga633ec3cdd878098287fea81ee7b02b43)
- [MDM_HL7800_ICCID_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga32865364e6fd4641b9be897bfd6c293f)
- [MDM_HL7800_SERIAL_NUMBER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae842bbecef777b83225577189205e085)
- [MDM_HL7800_SERIAL_NUMBER_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga10594faa869ccfdcd9d51309cf52d7c7)
- [MDM_HL7800_APN_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5cc5aad6ab04405999246790dd850046)
- [MDM_HL7800_APN_USERNAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gacb5d0f96845b17b84c746dcea6bd732a)
- [MDM_HL7800_APN_PASSWORD_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gabc1a2d9744225bc82f3f4b14d365a0fe)
- [MDM_HL7800_APN_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf58865f84686e963f5c3fdff2eaea26a)
- [MDM_HL7800_APN_USERNAME_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga80f2f5814be64d8ad75b5ced8017ca0d)
- [MDM_HL7800_APN_PASSWORD_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2e0973dd337183b6df1209df6a70e017)
- [MDM_HL7800_LTE_BAND_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8364e415a31bdce35ce76039de657b36)
- [MDM_HL7800_LTE_BAND_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3381c94afeaabed84e2027d4b947df2d)
- [MDM_HL7800_IMSI_MIN_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga523acdbfa564f3e83d93f7fbc50b8bc8)
- [MDM_HL7800_IMSI_MAX_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gac93538b6d4666aed22cef92b71e63df7)
- [MDM_HL7800_IMSI_MAX_STRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga645750b25f14ccfb2b6137243081a7ad)
- [MDM_HL7800_MAX_GPS_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf4840e7a40163477ccd00601467a8e8f)
- [MDM_HL7800_MAX_POLTE_USER_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga10db6322599d499eccf8116f692a42e1)
- [MDM_HL7800_MAX_POLTE_PASSWORD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga781329540d46b975eb8d6bf9870cf4a8)
- [MDM_HL7800_MAX_POLTE_LOCATION_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga060fccbbb60656b655abb3a8ad59f428)
- [MDM_HL7800_POLTE_SERVER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafbafa9aa28ebfdca72e19fca6cb944ea)
- [HL7800_EVENT_POLTE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a1fb1cd6b652c52ebf12e9741649f8630)
- [mdm_hl7800_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa044d03d9bfbc2f63088da4f094edfc)
- [mdm_hl7800_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3f7b0647d9ff01328e5536478a73aaf9)
- [mdm_hl7800_radio_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2d26759e8ea3aca2e8e4a6cccac2361a)
- [MDM_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga2d26759e8ea3aca2e8e4a6cccac2361aac95a4a3318b0683972336c1036f0548e)
- [MDM_RAT_CAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga2d26759e8ea3aca2e8e4a6cccac2361aa30bba3902918ea11995cd3db20319d61)
- [HL7800_EVENT_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7147e1d7ea1df5eb7604c3246a94ec0a)
- [HL7800_EVENT_NETWORK_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a08a58f10e3d58022ac945b2e68d4145a)
- [HL7800_EVENT_APN_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a4cf6f0344fa2348f378756e77d5f2804)
- [HL7800_EVENT_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9abb822dfaec7e96462be791857f9b3fba)
- [HL7800_EVENT_SINR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9ac76f3fec60d1ffeca58405cf38bd50fe)
- [HL7800_EVENT_STARTUP_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a0d25a89cd39d581c82ae73fe0a85ba21)
- [HL7800_EVENT_SLEEP_STATE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7bd6e3e3c19ed2c5ac138c16e03b2562)
- [HL7800_EVENT_RAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9ac22e246ac6bc5794ae0772bf3dbf5086)
- [HL7800_EVENT_BANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a327cd78d882a1a36716236f2cdf28c31)
- [HL7800_EVENT_ACTIVE_BANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aad01f254032296551f621c888530e9d1)
- [HL7800_EVENT_FOTA_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aedd9ae54dfa7a007c18e2a345d0cb0c5)
- [HL7800_EVENT_FOTA_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a3848abb978d465bd0a831fc0b66a33c3)
- [HL7800_EVENT_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a8a3b921d5bdb205f44576852467c38e2)
- [HL7800_EVENT_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9af3410e6ff2caa844c3b6f9963df485d1)
- [HL7800_EVENT_GPS_POSITION_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a0b9e7d1fcb8f043c5ac0b242e4c6c772)
- [HL7800_EVENT_POLTE_REGISTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9aead019c4cd55d1f54fb16ddef7f8277c)
- [HL7800_EVENT_POLTE_LOCATE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a7ee246b282ac147aafa45969060c5280)
- [HL7800_EVENT_SITE_SURVEY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a37463d52131771a296fb141c797b3e14)
- [HL7800_EVENT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3f7b0647d9ff01328e5536478a73aaf9a9189ebbdcf3175881a0e55ac9867acbf)
- [mdm_hl7800_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4b00cc03cc14b3812bed4a57aeea822c)
- [HL7800_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga4b00cc03cc14b3812bed4a57aeea822caccfc2361ab2bea50b510c428786a9a07)
- [HL7800_STATE_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga4b00cc03cc14b3812bed4a57aeea822ca44858cd6e73be2697e39f60aa54565be)
- [mdm_hl7800_startup_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaefcf9c39983d8f3f58bcd1a24ca04e99)
- [HL7800_STARTUP_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99aac2ef169e3273dd11331acae3abb9c6e)
- [HL7800_STARTUP_STATE_WAITING_FOR_ACCESS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a60dd736ae85eeafaefce839b623c530f)
- [HL7800_STARTUP_STATE_SIM_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a92593373e0efcb87471c6d0325f1c2e6)
- [HL7800_STARTUP_STATE_SIMLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a098e678b80c7148972d572f6dac763d6)
- [HL7800_STARTUP_STATE_UNRECOVERABLE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a1b88f9edf57f6fe1b9f4b31ecb196632)
- [HL7800_STARTUP_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a9d2a5fd088822989fc109cb3add31393)
- [HL7800_STARTUP_STATE_INACTIVE_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaefcf9c39983d8f3f58bcd1a24ca04e99a9999f1a90165d5996a7a2ff415db53d6)
- [mdm_hl7800_network_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga65c8ed3a7c2a2aee39ca65e57f33b773)
- [HL7800_NOT_REGISTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a94fe4bdd729ba6df15d9e9aa53998599)
- [HL7800_HOME_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a7e5bdc7f85c2d2f6ec62beee156e887d)
- [HL7800_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a1ad9a81e5ce65dc6eee98a87f880f86a)
- [HL7800_REGISTRATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a4eeb75667b400acaff56ad282bfe6a7c)
- [HL7800_OUT_OF_COVERAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773ae3f6d693bbe0d0c09a41a0e013fe5a82)
- [HL7800_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a9d7e014131f399f000965803ccb5e889)
- [HL7800_EMERGENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a04cac2efa21c949edeefc105effa4a39)
- [HL7800_UNABLE_TO_CONFIGURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga65c8ed3a7c2a2aee39ca65e57f33b773a2502129bf7729cce4b1b96ac66dfdd86)
- [mdm_hl7800_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3396149e553c32a597739096efe2aff7)
- [HL7800_SLEEP_UNINITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7af81cd0793c7faded881246c6a44b099a)
- [HL7800_SLEEP_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7af1253aa2135a3c1fb0f3a47a1f0265a4)
- [HL7800_SLEEP_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7ac7bf9c4685d31858b98d4188747387ba)
- [HL7800_SLEEP_LITE_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7a58c8b0b7a63a3f85b14d0cd0eea4b452)
- [HL7800_SLEEP_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga3396149e553c32a597739096efe2aff7a37e4283b77e32e890f7cc3eca3985289)
- [mdm_hl7800_fota_state](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8ed2ea65436083a9b1a49bb1f64574f3)
- [HL7800_FOTA_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3ab7d67051e56e05be47da306377bb8801)
- [HL7800_FOTA_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3ae6b160137651a7375551760f938b9da8)
- [HL7800_FOTA_WIP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a722b66bd586cc4375253341f1df8d189)
- [HL7800_FOTA_PAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a481fdc3814098383af7b593d4f61ea7b)
- [HL7800_FOTA_SEND_EOT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3aa78ef13656312bb81aa957a515b337d7)
- [HL7800_FOTA_FILE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3aaf2423203fdb79510efa9550e2a09bf9)
- [HL7800_FOTA_INSTALL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a6761ef6c52c40786c8b595950499851e)
- [HL7800_FOTA_REBOOT_AND_RECONFIGURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3a5e517d07a386297b5d80110cabc1864b)
- [HL7800_FOTA_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga8ed2ea65436083a9b1a49bb1f64574f3abd185b07f408b4b7ecb292f31aa6d19a)
- [mdm_hl7800_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf999018ef3ca438a9d3cb7b6611300d2)
- [HL7800_FUNCTIONALITY_MINIMUM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2ae2c5fac661bdf514debc98b3e248cea4)
- [HL7800_FUNCTIONALITY_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2ad1e22b662121c8c71b9d34810958b6c2)
- [HL7800_FUNCTIONALITY_AIRPLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaf999018ef3ca438a9d3cb7b6611300d2a2aca52c7dc8ade5db478f8eaebc4bc33)
- [mdm_hl7800_gnss_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5b6a53d0353ae153f715163ca4e6043b)
- [HL7800_GNSS_EVENT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba3349e6599deabd375c68bb3688bd9bfd)
- [HL7800_GNSS_EVENT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba3b0b73d5b585d4ed44e00504be60c8ef)
- [HL7800_GNSS_EVENT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba689418f8d35440fe71507ee871f20de1)
- [HL7800_GNSS_EVENT_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043bae83741a25baa0ffc3837b0653b01c318)
- [HL7800_GNSS_EVENT_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5b6a53d0353ae153f715163ca4e6043ba2df7e19144b20afb4bf3566804729db1)
- [mdm_hl7800_gnss_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga5253bceab7f3da57f9a2d3918ee72625)
- [HL7800_GNSS_STATUS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625aadc2b5c2e8b257e8b12ae7c4f5f35d76)
- [HL7800_GNSS_STATUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625a830898a215c51c8a17aab3fb175083b3)
- [HL7800_GNSS_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga5253bceab7f3da57f9a2d3918ee72625ab989ec2e119be4f23a37cac5203225ab)
- [mdm_hl7800_gnss_position_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaec06e58e1c79e23577d424806b6e696b)
- [HL7800_GNSS_POSITION_EVENT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696babf5377809190c648e6f3624b4b0b82ee)
- [HL7800_GNSS_POSITION_EVENT_LOST_OR_NOT_AVAILABLE_YET](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696bac41b513dd45d2d038b9d7a4a9bae8fe3)
- [HL7800_GNSS_POSITION_EVENT_PREDICTION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696bad41adce29331d1917c97e94b6409a9b5)
- [HL7800_GNSS_POSITION_EVENT_2D_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba1cf9c2fe042ab784450451f36b83818d)
- [HL7800_GNSS_POSITION_EVENT_3D_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba6bd45fa147597e9c278ec0f27c42efc7)
- [HL7800_GNSS_POSITION_EVENT_FIXED_TO_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ggaec06e58e1c79e23577d424806b6e696ba9822e7c1f4a238658592a539d18d0c6d)
- [mdm_hl7800_gps_string_types](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga45fd97039bb3add8ddb09f803ce9b038)
- [HL7800_GPS_STR_LATITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a5faac685b9958871cc3feb990e593b8b)
- [HL7800_GPS_STR_LONGITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a56f4e3a1a3b2eaacb2c34ec486165de8)
- [HL7800_GPS_STR_GPS_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a17989267e59a5169abb7f4d4c8bb3694)
- [HL7800_GPS_STR_FIX_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a7cd77b6bf81380fdaba8cdad863a60be)
- [HL7800_GPS_STR_HEPE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038aca3dac785dc09cc6d0780c2ce1956de4)
- [HL7800_GPS_STR_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a1eac295eb05a3c4617d35c9fd29aebf6)
- [HL7800_GPS_STR_ALT_UNC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a39502c1243b0df6765d6025e8173f214)
- [HL7800_GPS_STR_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038af5bef33ea67240657038a288f600ec25)
- [HL7800_GPS_STR_HOR_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038ac7f6f8e1d00b25b551a1560b7d998fc8)
- [HL7800_GPS_STR_VER_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gga45fd97039bb3add8ddb09f803ce9b038a40e32118c8039cfd3c6ef72c8a4d7f85)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [mdm_hl7800_power_off](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae270849872a22823512cc87b0bbf877e)
- [mdm_hl7800_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga956932a3c7d45f5ab0c3c99aa1decfb4)
- [mdm_hl7800_wakeup](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga430e2a1e2e8173dab93cf7b1e1fcb24d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mdm_hl7800_send_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga41a1f8f29c6ac8b53e5ef05f156a64a9)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mdm_hl7800_get_signal_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gad7d20cde62d5e7c987672cc9c10b152e)
- [mdm_hl7800_get_iccid](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaf84e782e572faf543a37a40147660eb0)
- [mdm_hl7800_get_sn](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1f3a7b2dd7654941006c4a8d5a46af01)
- [mdm_hl7800_get_imei](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4278b7f58b77048b8e833d9215183a5f)
- [mdm_hl7800_get_fw_version](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gac65dc452be996e5366360abb314a4d98)
- [mdm_hl7800_get_imsi](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga581582e3f7b07f04e6b33e481e2d6e42)
- [mdm_hl7800_update_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga3bf4e149e475d8a7c1f462c7de2dda80)
- [mdm_hl7800_update_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga9d295b105e71346fcb283959d2641079)
- [mdm_hl7800_valid_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga0b3822e97cbb77f4edab74e8bf2c903e)
- [mdm_hl7800_register_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafab74f2bd3806a23192cae18f65226ad)
- [mdm_hl7800_unregister_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gae2015e7399a17a862048eed89b036c6d)
- [mdm_hl7800_generate_status_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaaac620a4653d772f4d44a73834a8b4cc)
- [mdm_hl7800_get_local_time](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa95fa49240c3412521bade1245bc573)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [mdm_hl7800_update_fw](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga4ab20a8fd307c0397d733695b401b031)
- [mdm_hl7800_get_operator_index](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2bb74593dea9486754af21e50f4a6291)
- [mdm_hl7800_get_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga32dc9651acf319448da38709fc488d16)
- [mdm_hl7800_set_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1ca397e9e9db680dc6083ba2b4c08a70)
- [mdm_hl7800_set_gps_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2946b1d49c63084188f5f6c5dcebaaf2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mdm_hl7800_polte_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga8501f6d4883ee8577b5cda0f76d2a3dc)
- [mdm_hl7800_polte_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga22eb248b7aeb36a1c9895c8de6808f08)
- [mdm_hl7800_polte_locate](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga1708f077ddb438f93b246b223e52a80d)
- [mdm_hl7800_perform_site_survey](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga975a4cd75d9d89dd23b182af2376ef91)
- [mdm_hl7800_set_desired_sleep_level](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga2388ecc33d15263091c63185ccda3ea3)
- [mdm_hl7800_register_wake_test_point_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga16ac0447c88a9f025fc13009e63f46ef)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [mdm_hl7800_register_gpio6_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga0e5213411b27b4c5eeffd746464332a8)
- [mdm_hl7800_register_cts_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gaead5a1419d87676f13fdea12f705b125)
- [mdm_hl7800_set_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga935e3010e0a2d633e366711c09f634f1)
- [mdm_hl7800_log_filter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#ga838f6aab78e6f41028d381823cb6b118)

<a id="header-details"></a>

---

[上一章](P002_zephyr__bluetooth__gap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__net_event.h_文件参考.md)
