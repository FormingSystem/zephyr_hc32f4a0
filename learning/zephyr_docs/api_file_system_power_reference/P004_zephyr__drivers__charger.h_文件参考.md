---
id: learning.zephyr-docs.api-file-system-power-reference.page-4
title: zephyr__drivers__charger.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_charger.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池充电器（Battery Charger）驱动API的主头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/charger.h>
```

查看此文件的源码。

电池充电器（Battery Charger）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

<a id="r_charger_5Fdriver_5Fapi"></a>

```c
struct charger_driver_api
```

相关声明：[charger_driver_api](../device_power_control_model_reference/P002_charger_driver_api_结构体.md)。

驱动操作（Driver Operations）：充电器（Charger）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_ga4ce808890de2d01cdb75feddbf275635"></a>

```c
typedef uint16_t charger_prop_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)。

充电器属性（Charger Property）的标识符。

<a id="r_ga9325615cdd8985cbb3407257afb387a2"></a>

```c
typedef int32_t charger_custom_value_int_t
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[charger_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga9325615cdd8985cbb3407257afb387a2)。

自定义有符号整数属性值（Signed Integer Property Value）的类型。

<a id="r_gaa7a6c34b4871673151671eae1fac84da"></a>

```c
typedef uint32_t charger_custom_value_uint_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[charger_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaa7a6c34b4871673151671eae1fac84da)。

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

<a id="r_ga3b448c73ef8c4844ccbe7adb1f2458fe"></a>

```c
typedef bool charger_custom_value_bool_t
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[charger_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga3b448c73ef8c4844ccbe7adb1f2458fe)。

自定义布尔属性值（Boolean Property Value）的类型。

<a id="r_ga7666697bde91b66829113efe151d1cb2"></a>

```c
typedef void(* charger_status_notifier_t) (enum charger_status status)
```

相关声明：[charger_status_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga7666697bde91b66829113efe151d1cb2)、[charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)。

用于通知系统充电器状态变化（Charger Status Change）的回调。

<a id="r_gab29c2fafc53988555d72974199f25475"></a>

```c
typedef void(* charger_online_notifier_t) (enum charger_online online)
```

相关声明：[charger_online_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gab29c2fafc53988555d72974199f25475)、[charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)。

用于通知系统充电器在线状态变化（Charger Online Change）的回调。

<a id="r_gafb7488129e0a6c086d3ff0ffadb6c82b"></a>

```c
typedef int(* charger_get_property_t) (const struct device *dev, const charger_prop_t prop, union charger_propval *val)
```

相关声明：[charger_get_property_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#gafb7488129e0a6c086d3ff0ffadb6c82b)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

用于获取充电器属性（charger property）的回调 API。

<a id="r_ga6556781abf0e81eee431c88cb894a8e6"></a>

```c
typedef int(* charger_set_property_t) (const struct device *dev, const charger_prop_t prop, const union charger_propval *val)
```

相关声明：[charger_set_property_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#ga6556781abf0e81eee431c88cb894a8e6)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

用于设置充电器属性的回调 API。

<a id="r_gaf035c2972693a8763fd08b7db8c9c0bd"></a>

```c
typedef int(* charger_charge_enable_t) (const struct device *dev, const bool enable)
```

相关声明：[charger_charge_enable_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#gaf035c2972693a8763fd08b7db8c9c0bd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于启用或禁用充电周期（charge cycle）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_ga6eb3b4cc76e4f1e34732b7853eb860b7"></a>

```c
enum charger_property { CHARGER_PROP_ONLINE = 0 , CHARGER_PROP_PRESENT , CHARGER_PROP_STATUS , CHARGER_PROP_CHARGE_TYPE , CHARGER_PROP_HEALTH , CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA , CHARGER_PROP_PRECHARGE_CURRENT_UA , CHARGER_PROP_CHARGE_TERM_CURRENT_UA , CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV , CHARGER_PROP_INPUT_REGULATION_CURRENT_UA , CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV , CHARGER_PROP_INPUT_CURRENT_NOTIFICATION , CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION , CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV , CHARGER_PROP_STATUS_NOTIFICATION , CHARGER_PROP_ONLINE_NOTIFICATION , CHARGER_PROP_COMMON_COUNT , CHARGER_PROP_CUSTOM_BEGIN = CHARGER_PROP_COMMON_COUNT + 1 , CHARGER_PROP_MAX = UINT16_MAX }
```

相关声明：[charger_property](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga6eb3b4cc76e4f1e34732b7853eb860b7)、[CHARGER_PROP_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526)、[CHARGER_PROP_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b)、[CHARGER_PROP_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6)、[CHARGER_PROP_CHARGE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)、[CHARGER_PROP_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)、[CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306)、[CHARGER_PROP_PRECHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)、[CHARGER_PROP_CHARGE_TERM_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)、[CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf)、[CHARGER_PROP_INPUT_REGULATION_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085)、[CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0)、[CHARGER_PROP_INPUT_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe)、[CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72)、[CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0)、[CHARGER_PROP_STATUS_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b)、[CHARGER_PROP_ONLINE_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7)、[CHARGER_PROP_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)、[CHARGER_PROP_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)、[CHARGER_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)。

运行时动态电池参数（Runtime Dynamic Battery Parameters）。

<a id="r_gad95d2b1aaf18ac3a1c536f2d40317c19"></a>

```c
enum charger_online { CHARGER_ONLINE_OFFLINE = 0 , CHARGER_ONLINE_FIXED , CHARGER_ONLINE_PROGRAMMABLE }
```

相关声明：[charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)、[CHARGER_ONLINE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)、[CHARGER_ONLINE_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)、[CHARGER_ONLINE_PROGRAMMABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)。

外部供电状态（External Supply States）。

<a id="r_ga4a3c46bc0916082d15e665f7665c89d7"></a>

```c
enum charger_status { CHARGER_STATUS_UNKNOWN = 0 , CHARGER_STATUS_CHARGING , CHARGER_STATUS_DISCHARGING , CHARGER_STATUS_NOT_CHARGING , CHARGER_STATUS_FULL }
```

相关声明：[charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)、[CHARGER_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)、[CHARGER_STATUS_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)、[CHARGER_STATUS_DISCHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)、[CHARGER_STATUS_NOT_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)、[CHARGER_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)。

充电状态（Charging States）。

<a id="r_gaee833a379a8674621d2fdf9b57d1f803"></a>

```c
enum charger_charge_type { CHARGER_CHARGE_TYPE_UNKNOWN = 0 , CHARGER_CHARGE_TYPE_NONE , CHARGER_CHARGE_TYPE_TRICKLE , CHARGER_CHARGE_TYPE_FAST , CHARGER_CHARGE_TYPE_STANDARD , CHARGER_CHARGE_TYPE_ADAPTIVE , CHARGER_CHARGE_TYPE_LONGLIFE , CHARGER_CHARGE_TYPE_BYPASS }
```

相关声明：[charger_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaee833a379a8674621d2fdf9b57d1f803)、[CHARGER_CHARGE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)、[CHARGER_CHARGE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)、[CHARGER_CHARGE_TYPE_TRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)、[CHARGER_CHARGE_TYPE_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)、[CHARGER_CHARGE_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)、[CHARGER_CHARGE_TYPE_ADAPTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)、[CHARGER_CHARGE_TYPE_LONGLIFE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)、[CHARGER_CHARGE_TYPE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)。

充电算法类型（Charge Algorithm Types）。

<a id="r_gaab33241d3b85ab0770be9b1bd17e4412"></a>

```c
enum charger_health { CHARGER_HEALTH_UNKNOWN = 0 , CHARGER_HEALTH_GOOD , CHARGER_HEALTH_OVERHEAT , CHARGER_HEALTH_OVERVOLTAGE , CHARGER_HEALTH_UNSPEC_FAILURE , CHARGER_HEALTH_COLD , CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE , CHARGER_HEALTH_SAFETY_TIMER_EXPIRE , CHARGER_HEALTH_CALIBRATION_REQUIRED , CHARGER_HEALTH_WARM , CHARGER_HEALTH_COOL , CHARGER_HEALTH_HOT , CHARGER_HEALTH_NO_BATTERY }
```

相关声明：[charger_health](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaab33241d3b85ab0770be9b1bd17e4412)、[CHARGER_HEALTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)、[CHARGER_HEALTH_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)、[CHARGER_HEALTH_OVERHEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)、[CHARGER_HEALTH_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)、[CHARGER_HEALTH_UNSPEC_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)、[CHARGER_HEALTH_COLD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)、[CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)、[CHARGER_HEALTH_SAFETY_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)、[CHARGER_HEALTH_CALIBRATION_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)、[CHARGER_HEALTH_WARM](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)、[CHARGER_HEALTH_COOL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)、[CHARGER_HEALTH_HOT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)、[CHARGER_HEALTH_NO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)。

充电器健康状况（Charger Health Conditions）。

<a id="r_ga2e7d7f15725db4d502bc3f46476a310d"></a>

```c
enum charger_notification_severity { CHARGER_SEVERITY_PEAK = 0 , CHARGER_SEVERITY_CRITICAL , CHARGER_SEVERITY_WARNING }
```

相关声明：[charger_notification_severity](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga2e7d7f15725db4d502bc3f46476a310d)、[CHARGER_SEVERITY_PEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)、[CHARGER_SEVERITY_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)、[CHARGER_SEVERITY_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)。

用于系统通知的充电器严重性级别（Charger Severity Levels）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga00e5b61d517c93d7d3c863b14b07b738"></a>

```c
int charger_get_prop (const struct device *dev, const charger_prop_t prop, union charger_propval *val)
```

相关声明：[charger_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga00e5b61d517c93d7d3c863b14b07b738)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

获取电池充电器属性（Battery Charger Property）。

<a id="r_ga0036e3f5924585457a99a2e444ef5aab"></a>

```c
int charger_set_prop (const struct device *dev, const charger_prop_t prop, const union charger_propval *val)
```

相关声明：[charger_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga0036e3f5924585457a99a2e444ef5aab)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

设置电池充电器属性（Battery Charger Property）。

<a id="r_gace1ea9841574d75d314db078df5a0b3a"></a>

```c
int charger_charge_enable (const struct device *dev, const bool enable)
```

相关声明：[charger_charge_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gace1ea9841574d75d314db078df5a0b3a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用充电周期（Charge Cycle）。


## 4.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P007_charger.h_源码浏览.md)
- [charger_current_notifier](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md)
- [charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)
- [charger_property](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga6eb3b4cc76e4f1e34732b7853eb860b7)
- [charger_driver_api](../device_power_control_model_reference/P002_charger_driver_api_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [charger_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga9325615cdd8985cbb3407257afb387a2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [charger_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaa7a6c34b4871673151671eae1fac84da)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [charger_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga3b448c73ef8c4844ccbe7adb1f2458fe)
- [charger_status_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga7666697bde91b66829113efe151d1cb2)
- [charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)
- [charger_online_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gab29c2fafc53988555d72974199f25475)
- [charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)
- [charger_get_property_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#gafb7488129e0a6c086d3ff0ffadb6c82b)
- [device](../device_reference/P002_设备对象结构.md)
- [charger_set_property_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#ga6556781abf0e81eee431c88cb894a8e6)
- [charger_charge_enable_t](../api_device_topic_reference/P007_充电器驱动后端 API（Charger Driver Backend API）.md#gaf035c2972693a8763fd08b7db8c9c0bd)
- [CHARGER_PROP_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526)
- [CHARGER_PROP_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b)
- [CHARGER_PROP_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6)
- [CHARGER_PROP_CHARGE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)
- [CHARGER_PROP_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)
- [CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306)
- [CHARGER_PROP_PRECHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)
- [CHARGER_PROP_CHARGE_TERM_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)
- [CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf)
- [CHARGER_PROP_INPUT_REGULATION_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085)
- [CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0)
- [CHARGER_PROP_INPUT_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe)
- [CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72)
- [CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0)
- [CHARGER_PROP_STATUS_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b)
- [CHARGER_PROP_ONLINE_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7)
- [CHARGER_PROP_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)
- [CHARGER_PROP_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)
- [CHARGER_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)
- [CHARGER_ONLINE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)
- [CHARGER_ONLINE_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)
- [CHARGER_ONLINE_PROGRAMMABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)
- [CHARGER_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)
- [CHARGER_STATUS_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)
- [CHARGER_STATUS_DISCHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)
- [CHARGER_STATUS_NOT_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)
- [CHARGER_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)
- [charger_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaee833a379a8674621d2fdf9b57d1f803)
- [CHARGER_CHARGE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)
- [CHARGER_CHARGE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)
- [CHARGER_CHARGE_TYPE_TRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)
- [CHARGER_CHARGE_TYPE_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)
- [CHARGER_CHARGE_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)
- [CHARGER_CHARGE_TYPE_ADAPTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)
- [CHARGER_CHARGE_TYPE_LONGLIFE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)
- [CHARGER_CHARGE_TYPE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)
- [charger_health](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaab33241d3b85ab0770be9b1bd17e4412)
- [CHARGER_HEALTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)
- [CHARGER_HEALTH_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)
- [CHARGER_HEALTH_OVERHEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)
- [CHARGER_HEALTH_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)
- [CHARGER_HEALTH_UNSPEC_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)
- [CHARGER_HEALTH_COLD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)
- [CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)
- [CHARGER_HEALTH_SAFETY_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)
- [CHARGER_HEALTH_CALIBRATION_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)
- [CHARGER_HEALTH_WARM](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)
- [CHARGER_HEALTH_COOL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)
- [CHARGER_HEALTH_HOT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)
- [CHARGER_HEALTH_NO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)
- [charger_notification_severity](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga2e7d7f15725db4d502bc3f46476a310d)
- [CHARGER_SEVERITY_PEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)
- [CHARGER_SEVERITY_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)
- [CHARGER_SEVERITY_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)
- [charger_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga00e5b61d517c93d7d3c863b14b07b738)
- [charger_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga0036e3f5924585457a99a2e444ef5aab)
- [charger_charge_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gace1ea9841574d75d314db078df5a0b3a)

<a id="header-details"></a>

---

[上一章](P003_zephyr__dt-bindings__clock__bflb_bl70xl_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__cleanup.h_文件参考.md)
