---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-10
title: 电池充电器（Battery Charger）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_电池充电器（Battery Charger）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池充电器接口。

<a id="details"></a>

电池充电器接口（Battery Charger Interfaces）。自 3.5 引入，版本 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 10.1\_主题（Topics）

<a id="r_charger_5Finterface_5Fbackend"></a>

相关声明：[充电器驱动后端 API（Charger Driver Backend API）](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md)。

<a id="r_charger_5Finterface_5Fext"></a>

相关声明：[设备专用充电器 API 扩展（Device-specific Charger API extensions）](../api_topic_reference/P016_设备专用充电器 API 扩展（Device-specific Charger API extensions）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 10.2\_文件（Files）

<a id="r_charger_2Eh"></a>

```c
file charger.h
```

相关声明：[charger.h](../api_file_system_power_reference/P004_zephyr__drivers__charger.h_文件参考.md)。

电池充电器（Battery Charger）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.3\_数据结构（Data Structures）

<a id="r_charger_5Fcurrent_5Fnotifier"></a>

```c
struct charger_current_notifier
```

相关声明：[charger_current_notifier](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md)。

充电器（Charger）通知系统所用的输入电流阈值。

<a id="r_charger_5Fpropval"></a>

```c
union charger_propval
```

相关声明：[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

charger_property值的容器（Container）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.4\_类型定义（Typedefs）

<a id="r_ga4ce808890de2d01cdb75feddbf275635"></a>

```c
typedef uint16_t charger_prop_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[charger_prop_t](#ga4ce808890de2d01cdb75feddbf275635)。

充电器属性（Charger Property）的标识符。

<a id="r_ga9325615cdd8985cbb3407257afb387a2"></a>

```c
typedef int32_t charger_custom_value_int_t
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[charger_custom_value_int_t](#ga9325615cdd8985cbb3407257afb387a2)。

自定义有符号整数属性值（Signed Integer Property Value）的类型。

<a id="r_gaa7a6c34b4871673151671eae1fac84da"></a>

```c
typedef uint32_t charger_custom_value_uint_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[charger_custom_value_uint_t](#gaa7a6c34b4871673151671eae1fac84da)。

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

<a id="r_ga3b448c73ef8c4844ccbe7adb1f2458fe"></a>

```c
typedef bool charger_custom_value_bool_t
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[charger_custom_value_bool_t](#ga3b448c73ef8c4844ccbe7adb1f2458fe)。

自定义布尔属性值（Boolean Property Value）的类型。

<a id="r_ga7666697bde91b66829113efe151d1cb2"></a>

```c
typedef void(* charger_status_notifier_t) (enum charger_status status)
```

相关声明：[charger_status_notifier_t](#ga7666697bde91b66829113efe151d1cb2)、[charger_status](#ga4a3c46bc0916082d15e665f7665c89d7)。

用于通知系统充电器状态变化（Charger Status Change）的回调。

<a id="r_gab29c2fafc53988555d72974199f25475"></a>

```c
typedef void(* charger_online_notifier_t) (enum charger_online online)
```

相关声明：[charger_online_notifier_t](#gab29c2fafc53988555d72974199f25475)、[charger_online](#gad95d2b1aaf18ac3a1c536f2d40317c19)。

用于通知系统充电器在线状态变化（Charger Online Change）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.5\_枚举（Enumerations）

<a id="r_ga6eb3b4cc76e4f1e34732b7853eb860b7"></a>

```c
enum charger_property { CHARGER_PROP_ONLINE = 0 , CHARGER_PROP_PRESENT , CHARGER_PROP_STATUS , CHARGER_PROP_CHARGE_TYPE , CHARGER_PROP_HEALTH , CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA , CHARGER_PROP_PRECHARGE_CURRENT_UA , CHARGER_PROP_CHARGE_TERM_CURRENT_UA , CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV , CHARGER_PROP_INPUT_REGULATION_CURRENT_UA , CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV , CHARGER_PROP_INPUT_CURRENT_NOTIFICATION , CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION , CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV , CHARGER_PROP_STATUS_NOTIFICATION , CHARGER_PROP_ONLINE_NOTIFICATION , CHARGER_PROP_COMMON_COUNT , CHARGER_PROP_CUSTOM_BEGIN = CHARGER_PROP_COMMON_COUNT + 1 , CHARGER_PROP_MAX = UINT16_MAX }
```

相关声明：[charger_property](#ga6eb3b4cc76e4f1e34732b7853eb860b7)、[CHARGER_PROP_ONLINE](#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526)、[CHARGER_PROP_PRESENT](#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b)、[CHARGER_PROP_STATUS](#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6)、[CHARGER_PROP_CHARGE_TYPE](#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)、[CHARGER_PROP_HEALTH](#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)、[CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306)、[CHARGER_PROP_PRECHARGE_CURRENT_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)、[CHARGER_PROP_CHARGE_TERM_CURRENT_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)、[CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf)、[CHARGER_PROP_INPUT_REGULATION_CURRENT_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085)、[CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0)、[CHARGER_PROP_INPUT_CURRENT_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe)、[CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72)、[CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0)、[CHARGER_PROP_STATUS_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b)、[CHARGER_PROP_ONLINE_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7)、[CHARGER_PROP_COMMON_COUNT](#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)、[CHARGER_PROP_CUSTOM_BEGIN](#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)、[CHARGER_PROP_MAX](#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)。

运行时动态电池参数（Runtime Dynamic Battery Parameters）。

<a id="r_gad95d2b1aaf18ac3a1c536f2d40317c19"></a>

```c
enum charger_online { CHARGER_ONLINE_OFFLINE = 0 , CHARGER_ONLINE_FIXED , CHARGER_ONLINE_PROGRAMMABLE }
```

相关声明：[charger_online](#gad95d2b1aaf18ac3a1c536f2d40317c19)、[CHARGER_ONLINE_OFFLINE](#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)、[CHARGER_ONLINE_FIXED](#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)、[CHARGER_ONLINE_PROGRAMMABLE](#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)。

外部供电状态（External Supply States）。

<a id="r_ga4a3c46bc0916082d15e665f7665c89d7"></a>

```c
enum charger_status { CHARGER_STATUS_UNKNOWN = 0 , CHARGER_STATUS_CHARGING , CHARGER_STATUS_DISCHARGING , CHARGER_STATUS_NOT_CHARGING , CHARGER_STATUS_FULL }
```

相关声明：[charger_status](#ga4a3c46bc0916082d15e665f7665c89d7)、[CHARGER_STATUS_UNKNOWN](#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)、[CHARGER_STATUS_CHARGING](#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)、[CHARGER_STATUS_DISCHARGING](#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)、[CHARGER_STATUS_NOT_CHARGING](#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)、[CHARGER_STATUS_FULL](#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)。

充电状态（Charging States）。

<a id="r_gaee833a379a8674621d2fdf9b57d1f803"></a>

```c
enum charger_charge_type { CHARGER_CHARGE_TYPE_UNKNOWN = 0 , CHARGER_CHARGE_TYPE_NONE , CHARGER_CHARGE_TYPE_TRICKLE , CHARGER_CHARGE_TYPE_FAST , CHARGER_CHARGE_TYPE_STANDARD , CHARGER_CHARGE_TYPE_ADAPTIVE , CHARGER_CHARGE_TYPE_LONGLIFE , CHARGER_CHARGE_TYPE_BYPASS }
```

相关声明：[charger_charge_type](#gaee833a379a8674621d2fdf9b57d1f803)、[CHARGER_CHARGE_TYPE_UNKNOWN](#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)、[CHARGER_CHARGE_TYPE_NONE](#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)、[CHARGER_CHARGE_TYPE_TRICKLE](#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)、[CHARGER_CHARGE_TYPE_FAST](#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)、[CHARGER_CHARGE_TYPE_STANDARD](#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)、[CHARGER_CHARGE_TYPE_ADAPTIVE](#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)、[CHARGER_CHARGE_TYPE_LONGLIFE](#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)、[CHARGER_CHARGE_TYPE_BYPASS](#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)。

充电算法类型（Charge Algorithm Types）。

<a id="r_gaab33241d3b85ab0770be9b1bd17e4412"></a>

```c
enum charger_health { CHARGER_HEALTH_UNKNOWN = 0 , CHARGER_HEALTH_GOOD , CHARGER_HEALTH_OVERHEAT , CHARGER_HEALTH_OVERVOLTAGE , CHARGER_HEALTH_UNSPEC_FAILURE , CHARGER_HEALTH_COLD , CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE , CHARGER_HEALTH_SAFETY_TIMER_EXPIRE , CHARGER_HEALTH_CALIBRATION_REQUIRED , CHARGER_HEALTH_WARM , CHARGER_HEALTH_COOL , CHARGER_HEALTH_HOT , CHARGER_HEALTH_NO_BATTERY }
```

相关声明：[charger_health](#gaab33241d3b85ab0770be9b1bd17e4412)、[CHARGER_HEALTH_UNKNOWN](#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)、[CHARGER_HEALTH_GOOD](#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)、[CHARGER_HEALTH_OVERHEAT](#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)、[CHARGER_HEALTH_OVERVOLTAGE](#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)、[CHARGER_HEALTH_UNSPEC_FAILURE](#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)、[CHARGER_HEALTH_COLD](#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)、[CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE](#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)、[CHARGER_HEALTH_SAFETY_TIMER_EXPIRE](#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)、[CHARGER_HEALTH_CALIBRATION_REQUIRED](#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)、[CHARGER_HEALTH_WARM](#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)、[CHARGER_HEALTH_COOL](#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)、[CHARGER_HEALTH_HOT](#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)、[CHARGER_HEALTH_NO_BATTERY](#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)。

充电器健康状况（Charger Health Conditions）。

<a id="r_ga2e7d7f15725db4d502bc3f46476a310d"></a>

```c
enum charger_notification_severity { CHARGER_SEVERITY_PEAK = 0 , CHARGER_SEVERITY_CRITICAL , CHARGER_SEVERITY_WARNING }
```

相关声明：[charger_notification_severity](#ga2e7d7f15725db4d502bc3f46476a310d)、[CHARGER_SEVERITY_PEAK](#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)、[CHARGER_SEVERITY_CRITICAL](#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)、[CHARGER_SEVERITY_WARNING](#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)。

用于系统通知的充电器严重性级别（Charger Severity Levels）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.6\_函数（Functions）

<a id="r_ga00e5b61d517c93d7d3c863b14b07b738"></a>

```c
int charger_get_prop (const struct device *dev, const charger_prop_t prop, union charger_propval *val)
```

相关声明：[charger_get_prop](#ga00e5b61d517c93d7d3c863b14b07b738)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

获取电池充电器属性（Battery Charger Property）。

<a id="r_ga0036e3f5924585457a99a2e444ef5aab"></a>

```c
int charger_set_prop (const struct device *dev, const charger_prop_t prop, const union charger_propval *val)
```

相关声明：[charger_set_prop](#ga0036e3f5924585457a99a2e444ef5aab)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

设置电池充电器属性（Battery Charger Property）。

<a id="r_gace1ea9841574d75d314db078df5a0b3a"></a>

```c
int charger_charge_enable (const struct device *dev, const bool enable)
```

相关声明：[charger_charge_enable](#gace1ea9841574d75d314db078df5a0b3a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用充电周期（Charge Cycle）。

## 10.7\_详细说明（Detailed Documentation）

<a id="ga3b448c73ef8c4844ccbe7adb1f2458fe"></a>

### `charger_custom_value_bool_t`

```c
typedef bool charger_custom_value_bool_t
```

```c
#include <zephyr/drivers/charger.h>
```

自定义布尔属性值（Boolean Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 CHARGER_PROP_CUSTOM_BEGIN）使用，通常用于特性／状态标志，例如 jeita_active。

<a id="ga9325615cdd8985cbb3407257afb387a2"></a>

### `charger_custom_value_int_t`

```c
typedef int32_t charger_custom_value_int_t
```

```c
#include <zephyr/drivers/charger.h>
```

自定义有符号整数属性值（Signed Integer Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 CHARGER_PROP_CUSTOM_BEGIN）使用。

<a id="gaa7a6c34b4871673151671eae1fac84da"></a>

### `charger_custom_value_uint_t`

```c
typedef uint32_t charger_custom_value_uint_t
```

```c
#include <zephyr/drivers/charger.h>
```

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 CHARGER_PROP_CUSTOM_BEGIN）使用。

<a id="gab29c2fafc53988555d72974199f25475"></a>

### `charger_online_notifier_t`

```c
typedef void(* charger_online_notifier_t) (enum charger_online online)
```

```c
#include <zephyr/drivers/charger.h>
```

用于通知系统充电器在线状态变化（Charger Online Change）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `online` | 当前外部电源状态（External Supply State）。 |

<a id="ga4ce808890de2d01cdb75feddbf275635"></a>

### `charger_prop_t`

```c
typedef uint16_t charger_prop_t
```

```c
#include <zephyr/drivers/charger.h>
```

充电器属性（Charger Property）的标识符。

标识符列表参见 charger_property。

<a id="ga7666697bde91b66829113efe151d1cb2"></a>

### `charger_status_notifier_t`

```c
typedef void(* charger_status_notifier_t) (enum charger_status status)
```

```c
#include <zephyr/drivers/charger.h>
```

用于通知系统充电器状态变化（Charger Status Change）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 当前充电状态（Charging State）。 |

<a id="gaee833a379a8674621d2fdf9b57d1f803"></a>

### `charger_charge_type`

```c
enum charger_charge_type
```

```c
#include <zephyr/drivers/charger.h>
```

充电算法类型（Charge Algorithm Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_CHARGE_TYPE_UNKNOWN` | 充电类型未知（Unknown Charge Type）。 |
| `CHARGER_CHARGE_TYPE_NONE` | 未进行充电（Not Charging）。 |
| `CHARGER_CHARGE_TYPE_TRICKLE` | 正以期望的最低充电速率（Slowest Desired Charge Rate）充电，通常用于电池检测或预处理。 |
| `CHARGER_CHARGE_TYPE_FAST` | 正以期望的最高充电速率（Fastest Desired Charge Rate）充电。 |
| `CHARGER_CHARGE_TYPE_STANDARD` | 正以中等充电速率（Moderate Charge Rate）充电。 |
| `CHARGER_CHARGE_TYPE_ADAPTIVE` | 充电器设备正在动态调整充电（Dynamically Adjusted Charging）。 |
| `CHARGER_CHARGE_TYPE_LONGLIFE` | 正以降低的充电速率（Reduced Charge Rate）充电，以保护电池健康。 |
| `CHARGER_CHARGE_TYPE_BYPASS` | 充电器设备被旁路（Bypassed），由外部处理功率转换，通常由智能墙插适配器（Smart Wall Adaptor）承担。 |

<a id="gaab33241d3b85ab0770be9b1bd17e4412"></a>

### `charger_health`

```c
enum charger_health
```

```c
#include <zephyr/drivers/charger.h>
```

充电器健康状况（Charger Health Conditions）。

这些条件决定能否充电或充电速率（Charge Rate）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_HEALTH_UNKNOWN` | 充电器健康状态未知（Unknown Health Condition）。 |
| `CHARGER_HEALTH_GOOD` | 充电器健康状态良好（Good Health Condition）。 |
| `CHARGER_HEALTH_OVERHEAT` | 充电器设备过热（Overheated）。 |
| `CHARGER_HEALTH_OVERVOLTAGE` | 电池电压超过过压阈值（Overvoltage Threshold）。 |
| `CHARGER_HEALTH_UNSPEC_FAILURE` | 电池或充电器设备发生未指定故障（Unspecified Failure）。 |
| `CHARGER_HEALTH_COLD` | 电池温度低于冷阈值（Cold Threshold）。 |
| `CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE` | 充电器的看门狗定时器（Watchdog Timer）已到期。 |
| `CHARGER_HEALTH_SAFETY_TIMER_EXPIRE` | 充电器的安全定时器（Safety Timer）已到期。 |
| `CHARGER_HEALTH_CALIBRATION_REQUIRED` | 充电器设备需要校准（Calibration）。 |
| `CHARGER_HEALTH_WARM` | 电池温度处于温暖范围（Warm Range）。 |
| `CHARGER_HEALTH_COOL` | 电池温度处于偏凉范围（Cool Range）。 |
| `CHARGER_HEALTH_HOT` | 电池温度低于热阈值（Hot Threshold）。（原文为 below，保留其表述。） |
| `CHARGER_HEALTH_NO_BATTERY` | 充电器设备未检测到电池。 |

<a id="ga2e7d7f15725db4d502bc3f46476a310d"></a>

### `charger_notification_severity`

```c
enum charger_notification_severity
```

```c
#include <zephyr/drivers/charger.h>
```

用于系统通知的充电器严重性级别（Charger Severity Levels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_SEVERITY_PEAK` | 最严重等级（Most Severe Level），通常立即触发。 |
| `CHARGER_SEVERITY_CRITICAL` | 比警告等级（Warning Level）严重，但低于峰值等级（Peak）。 |
| `CHARGER_SEVERITY_WARNING` | 基本严重等级（Base Severity Level）。 |

<a id="gad95d2b1aaf18ac3a1c536f2d40317c19"></a>

### `charger_online`

```c
enum charger_online
```

```c
#include <zephyr/drivers/charger.h>
```

外部供电状态（External Supply States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_ONLINE_OFFLINE` | 外部电源不存在（External Supply Not Present）。 |
| `CHARGER_ONLINE_FIXED` | 外部电源存在，输出固定（Fixed Output）。 |
| `CHARGER_ONLINE_PROGRAMMABLE` | 外部电源存在，输出可编程（Programmable Output）。 |

<a id="ga6eb3b4cc76e4f1e34732b7853eb860b7"></a>

### `charger_property`

```c
enum charger_property
```

```c
#include <zephyr/drivers/charger.h>
```

运行时动态电池参数（Runtime Dynamic Battery Parameters）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_PROP_ONLINE` | 指示充电器是否存在外部电源（External Supply）。值的类型应为 enum charger_online。 |
| `CHARGER_PROP_PRESENT` | 报告是否存在电池（Battery Present）。值的类型应为 bool。 |
| `CHARGER_PROP_STATUS` | 表示充电器的充电状态（Charging Status）。值的类型应为 enum charger_status。 |
| `CHARGER_PROP_CHARGE_TYPE` | 表示充电器的充电算法类型（Charging Algorithm Type）。值的类型应为 enum charger_charge_type。 |
| `CHARGER_PROP_HEALTH` | 表示充电器的健康状态（Health）。值的类型应为 enum charger_health。 |
| `CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA` | 配置充电所用的吸收电流（Current Sink），单位为 µA。 |
| `CHARGER_PROP_PRECHARGE_CURRENT_UA` | 配置预处理（Conditioning）所用的吸收电流（Current Sink），单位为 µA。 |
| `CHARGER_PROP_CHARGE_TERM_CURRENT_UA` | 配置充电终止目标电流（Charge Termination Target），单位为 µA。 |
| `CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV` | 配置充电电压调节目标（Charge Voltage Regulation Target），单位为 µV。 |
| `CHARGER_PROP_INPUT_REGULATION_CURRENT_UA` | 配置输入电流调节目标（Input Current Regulation Target），单位为 µA。此值是上升电流阈值，通过减小充电电流输出进行调节。 |
| `CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV` | 配置输入电压调节目标（Input Voltage Regulation Target），单位为 µV。此值是下降电压阈值，通过减小充电电流输出进行调节。 |
| `CHARGER_PROP_INPUT_CURRENT_NOTIFICATION` | 配置根据输入电流水平和持续时间（Input Current Level and Timing）向系统发出通知的行为。值的类型应为 struct charger_current_notifier。 |
| `CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION` | 配置根据电池放电电流水平和持续时间（Battery Discharge Current Level and Timing）向系统发出通知的行为。值的类型应为 struct charger_current_notifier。 |
| `CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV` | 配置向系统发出通知的系统电压下降阈值（Falling System Voltage Threshold），单位为 µV。 |
| `CHARGER_PROP_STATUS_NOTIFICATION` | 配置根据充电器状态变化（Charger Status Change）向系统发出通知的行为。值的类型应为 charger_status_notifier_t。 |
| `CHARGER_PROP_ONLINE_NOTIFICATION` | 配置根据充电器在线状态变化（Charger Online Change）向系统发出通知的行为。值的类型应为 charger_online_notifier_t。 |
| `CHARGER_PROP_COMMON_COUNT` | 保留值，用于界定通用充电器属性（Common Charger Properties）的结束位置。 |
| `CHARGER_PROP_CUSTOM_BEGIN` | 保留值，用于界定下游自定义属性（Downstream Custom Properties）。应使用此符号值，因为其实际数值可能随 API 后续版本改变。 |
| `CHARGER_PROP_MAX` | 保留值，用于界定有效枚举属性（Valid Enum Properties）的结束位置。 |

<a id="ga4a3c46bc0916082d15e665f7665c89d7"></a>

### `charger_status`

```c
enum charger_status
```

```c
#include <zephyr/drivers/charger.h>
```

充电状态（Charging States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHARGER_STATUS_UNKNOWN` | 充电设备状态未知（Unknown State）。 |
| `CHARGER_STATUS_CHARGING` | 充电设备正在为电池充电（Charging）。 |
| `CHARGER_STATUS_DISCHARGING` | 充电设备无法为电池充电（Unable to Charge）。 |
| `CHARGER_STATUS_NOT_CHARGING` | 充电设备当前未为电池充电（Not Charging）。 |
| `CHARGER_STATUS_FULL` | 电池已满（Full），充电设备不会尝试充电。 |

<a id="gace1ea9841574d75d314db078df5a0b3a"></a>

### `charger_charge_enable()`

```c
int charger_charge_enable ( const struct device * dev, const bool enable )
```

```c
#include <zephyr/drivers/charger.h>
```

启用或禁用充电周期（Charge Cycle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池充电器设备（Battery Charger Device）的指针。 |
| `enable` | true 启用充电周期（Charge Cycle），false 禁用充电周期。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与充电器通信失败。 |
| `-EINVAL` | 启动充电的条件（Conditions for Initiating Charging）无效。 |

<a id="ga00e5b61d517c93d7d3c863b14b07b738"></a>

### `charger_get_prop()`

```c
int charger_get_prop ( const struct device * dev, const charger_prop_t prop, union charger_propval * val )
```

```c
#include <zephyr/drivers/charger.h>
```

获取电池充电器属性（Battery Charger Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池充电器设备（Battery Charger Device）的指针。 |
| `prop` | 要获取的充电器属性（Charger Property）。 |
| `val` | 指向 charger_propval 联合体（Union）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `<0` | 获取属性（Property）失败。 |

<a id="ga0036e3f5924585457a99a2e444ef5aab"></a>

### `charger_set_prop()`

```c
int charger_set_prop ( const struct device * dev, const charger_prop_t prop, const union charger_propval * val )
```

```c
#include <zephyr/drivers/charger.h>
```

设置电池充电器属性（Battery Charger Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池充电器设备（Battery Charger Device）的指针。 |
| `prop` | 要设置的充电器属性（Charger Property）。 |
| `val` | 指向 charger_propval 联合体（Union）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `<0` | 设置属性（Property）失败。 |


## 10.8\_原页交叉引用（Cross References）

- [充电器驱动后端 API（Charger Driver Backend API）](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md)
- [设备专用充电器 API 扩展（Device-specific Charger API extensions）](../api_topic_reference/P016_设备专用充电器 API 扩展（Device-specific Charger API extensions）.md)
- [charger.h](../api_file_system_power_reference/P004_zephyr__drivers__charger.h_文件参考.md)
- [charger_current_notifier](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md)
- [charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f"></a>
<a id="ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1"></a>
<a id="ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b"></a>
<a id="gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b"></a>
<a id="gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8"></a>
<a id="gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885"></a>
<a id="ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3"></a>
<a id="ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6"></a>
<a id="ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3"></a>
<a id="gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e"></a>
<a id="gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5"></a>
<a id="gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad"></a>
<a id="gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e"></a>
<a id="gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658"></a>
<a id="gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_蜂窝通信（Cellular）.md) · [返回大纲](大纲.md) · [下一章](P011_以太网介质无关接口支持函数（Ethernet MII Support Functions）.md)
