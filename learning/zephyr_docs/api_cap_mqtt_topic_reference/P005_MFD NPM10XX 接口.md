---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-5
title: MFD NPM10XX 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_MFD NPM10XX 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自（Since）4.4 起提供，版本（Version）0.3.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_mfd_5Fnpm10xx_5Fevent_5Fcallback"></a>

```c
struct mfd_npm10xx_event_callback
```

相关声明：[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)。

NPM10xx多功能设备（MFD）的回调结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_gab2a9bae08f020392e33bfb98efff2f32"></a>

```c
typedef uint64_t npm10xx_event_t
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[npm10xx_event_t](#gab2a9bae08f020392e33bfb98efff2f32)。

标识供事件回调（Event Callback）使用的一组事件。

<a id="r_ga4cdc0f26a0193e0c1e58404f632029c7"></a>

```c
typedef uint16_t npm10xx_rstreas_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[npm10xx_rstreas_t](#ga4cdc0f26a0193e0c1e58404f632029c7)。

标识复位原因（Reset Reason）。

<a id="r_ga917abc6c5ed263f28a04bc96598d0009"></a>

```c
typedef void(* npm10xx_callback_handler_t) (const struct device *mfd_npm10xx_dev, struct mfd_npm10xx_event_callback *cb, npm10xx_event_t events)
```

相关声明：[npm10xx_callback_handler_t](#ga917abc6c5ed263f28a04bc96598d0009)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)、[npm10xx_event_t](#gab2a9bae08f020392e33bfb98efff2f32)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_ga164233569fe1f2e9ee00acc74e6f92c7"></a>

```c
enum mfd_npm10xx_hibernate_mode { NPM10XX_HIBERNATE_VBAT , NPM10XX_HIBERNATE_VBUS_WAIT , NPM10XX_HIBERNATE_VBUS_NOWAIT }
```

相关声明：[mfd_npm10xx_hibernate_mode](#ga164233569fe1f2e9ee00acc74e6f92c7)、[NPM10XX_HIBERNATE_VBAT](#gga164233569fe1f2e9ee00acc74e6f92c7a1cfa5ca4c49b40e9b78da256908a89d6)、[NPM10XX_HIBERNATE_VBUS_WAIT](#gga164233569fe1f2e9ee00acc74e6f92c7a9ce4e5b0bbe115a52dcb297f1cce6d64)、[NPM10XX_HIBERNATE_VBUS_NOWAIT](#gga164233569fe1f2e9ee00acc74e6f92c7ab1f535e92914be861eee60738b0280a4)。

nPM10xx 深度休眠模式（Hibernate Modes）。

<a id="r_gab6640de2b0c8007f3b8f13b31a66a00a"></a>

```c
enum mfd_npm10xx_standby_op { NPM10XX_STANDBY1_ENTER_WAIT , NPM10XX_STANDBY1_ENTER_NOWAIT , NPM10XX_STANDBY2_ENTER_WAIT , NPM10XX_STANDBY2_ENTER_NOWAIT , NPM10XX_STANDBY_EXIT }
```

相关声明：[mfd_npm10xx_standby_op](#gab6640de2b0c8007f3b8f13b31a66a00a)、[NPM10XX_STANDBY1_ENTER_WAIT](#ggab6640de2b0c8007f3b8f13b31a66a00aa5542f06dba5176ccfed1e024c2a75e50)、[NPM10XX_STANDBY1_ENTER_NOWAIT](#ggab6640de2b0c8007f3b8f13b31a66a00aaa7523d301dc05610fdf8de9ca2996031)、[NPM10XX_STANDBY2_ENTER_WAIT](#ggab6640de2b0c8007f3b8f13b31a66a00aaa9c904dbc9b8f339cd15fcf02991e7c4)、[NPM10XX_STANDBY2_ENTER_NOWAIT](#ggab6640de2b0c8007f3b8f13b31a66a00aafae6fbde2b5e0a178a794ee43b7987d8)、[NPM10XX_STANDBY_EXIT](#ggab6640de2b0c8007f3b8f13b31a66a00aac6b17d0c7aa2536c4c3af6900ee857bf)。

nPM10xx 待机操作（Standby Operations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga5ff11ba2820c426dfeeb959b511b66f2"></a>

```c
int mfd_npm10xx_reset (const struct device *dev)
```

相关声明：[mfd_npm10xx_reset](#ga5ff11ba2820c426dfeeb959b511b66f2)、[device](../device_reference/P002_设备对象结构.md)。

复位 nPM10xx 电源管理集成电路（PMIC）设备。

<a id="r_ga2bd8018f8aab66569a5fa052893e0c25"></a>

```c
int mfd_npm10xx_get_reset_reason (const struct device *dev, npm10xx_rstreas_t *reason)
```

相关声明：[mfd_npm10xx_get_reset_reason](#ga2bd8018f8aab66569a5fa052893e0c25)、[device](../device_reference/P002_设备对象结构.md)、[npm10xx_rstreas_t](#ga4cdc0f26a0193e0c1e58404f632029c7)。

获取并清除 nPM10xx 电源管理集成电路（PMIC）设备的复位原因（Reset Reason）。

<a id="r_gad9da1db5f865d5a39f1bc348c6f5fafd"></a>

```c
int mfd_npm10xx_hibernate (const struct device *dev, enum mfd_npm10xx_hibernate_mode mode, k_timeout_t time)
```

相关声明：[mfd_npm10xx_hibernate](#gad9da1db5f865d5a39f1bc348c6f5fafd)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_hibernate_mode](#ga164233569fe1f2e9ee00acc74e6f92c7)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)。

触发 nPM10xx 电源管理集成电路（PMIC）设备的深度休眠模式（Hibernate Mode）。

<a id="r_gad6169c136db8c4d56552793d5da2e666"></a>

```c
int mfd_npm10xx_standby (const struct device *dev, enum mfd_npm10xx_standby_op operation)
```

相关声明：[mfd_npm10xx_standby](#gad6169c136db8c4d56552793d5da2e666)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_standby_op](#gab6640de2b0c8007f3b8f13b31a66a00a)。

使 nPM10xx 电源管理集成电路（PMIC）设备进入或退出 VBUS 待机模式（Standby Mode）。

<a id="r_gae67bf6f3efdcd948ebc5034e56540d71"></a>

```c
int mfd_npm10xx_manage_callback (const struct device *dev, struct mfd_npm10xx_event_callback *callback, bool add)
```

相关声明：[mfd_npm10xx_manage_callback](#gae67bf6f3efdcd948ebc5034e56540d71)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

管理 nPM10xx 事件回调（Event Callbacks）。

<a id="r_ga5e155e4ba41999daccf9c2046ae60ad3"></a>

```c
int mfd_npm10xx_timer_set (const struct device *dev, k_timeout_t timeout)
```

相关声明：[mfd_npm10xx_timer_set](#ga5e155e4ba41999daccf9c2046ae60ad3)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置 nPM10xx 设备定时器的超时值（Timeout Value）。

<a id="r_ga6c7cf9f9606495ede2575174e60211fb"></a>

```c
int mfd_npm10xx_timer_start (const struct device *dev)
```

相关声明：[mfd_npm10xx_timer_start](#ga6c7cf9f9606495ede2575174e60211fb)、[device](../device_reference/P002_设备对象结构.md)。

启动 nPM10xx 设备的定时器（Timer）。

<a id="r_ga144c19663856ce0a8fc32db02c867360"></a>

```c
int mfd_npm10xx_timer_stop (const struct device *dev)
```

相关声明：[mfd_npm10xx_timer_stop](#ga144c19663856ce0a8fc32db02c867360)、[device](../device_reference/P002_设备对象结构.md)。

停止 nPM10xx 设备的定时器（Timer）。

<a id="r_ga27625e2cceaea478514452bc0c9a2a1b"></a>

```c
int mfd_npm10xx_timer_status_get (const struct device *dev, bool *busy)
```

相关声明：[mfd_npm10xx_timer_status_get](#ga27625e2cceaea478514452bc0c9a2a1b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取 nPM10xx 设备的定时器状态（Timer Status）。

<a id="r_gae775dcf89711147276ce11578ea7b6d2"></a>

```c
int mfd_npm10xx_scratch_read (const struct device *dev, uint8_t *val)
```

相关声明：[mfd_npm10xx_scratch_read](#gae775dcf89711147276ce11578ea7b6d2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 `SCRATCH` 寄存器（Register）。

<a id="r_gaeb4cf7992c48aa4ad5747e58ec3a0020"></a>

```c
int mfd_npm10xx_scratch_write (const struct device *dev, uint8_t val)
```

相关声明：[mfd_npm10xx_scratch_write](#gaeb4cf7992c48aa4ad5747e58ec3a0020)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 `SCRATCH` 寄存器（Register）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.5\_复位原因（RESET reasons）

<a id="r_gaa01e18082e07f933a6bf0c4a8f6f24c1"></a>

```c
#define NPM10XX_RSTREAS_HIBERNATE BIT(0)
```

相关声明：[NPM10XX_RSTREAS_HIBERNATE](#gaa01e18082e07f933a6bf0c4a8f6f24c1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因连接 VBUS 而退出 VBAT 深度休眠模式（Hibernate Mode）。

<a id="r_ga1d6e5782bf0e1c2ea395a2b9dd884723"></a>

```c
#define NPM10XX_RSTREAS_BOOTMON BIT(1)
```

相关声明：[NPM10XX_RSTREAS_BOOTMON](#ga1d6e5782bf0e1c2ea395a2b9dd884723)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启动监视器复位（Boot Monitor Reset）。

<a id="r_gaa0266596048079a4b90dd3df6199666a"></a>

```c
#define NPM10XX_RSTREAS_WATCHDOG BIT(2)
```

相关声明：[NPM10XX_RSTREAS_WATCHDOG](#gaa0266596048079a4b90dd3df6199666a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗复位（Watchdog Reset）。

<a id="r_ga762cca53f636dd8a3e2fcd7017b3abdd"></a>

```c
#define NPM10XX_RSTREAS_LONGPRESS BIT(3)
```

相关声明：[NPM10XX_RSTREAS_LONGPRESS](#ga762cca53f636dd8a3e2fcd7017b3abdd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

长按复位（Longpress Reset）。

<a id="r_ga167467b923a5f81bdaec1e4e1d91a368"></a>

```c
#define NPM10XX_RSTREAS_THERMAL BIT(4)
```

相关声明：[NPM10XX_RSTREAS_THERMAL](#ga167467b923a5f81bdaec1e4e1d91a368)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

热关断复位（Thermal Shutdown Reset）。

<a id="r_gad79d6bf2c570e8a51700e17cfeb5a817"></a>

```c
#define NPM10XX_RSTREAS_POF BIT(5)
```

相关声明：[NPM10XX_RSTREAS_POF](#gad79d6bf2c570e8a51700e17cfeb5a817)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源故障复位（POF Reset）。

<a id="r_ga7cb7ea1ce7b2bc41f0388c2f5b740b5a"></a>

```c
#define NPM10XX_RSTREAS_SW BIT(6)
```

相关声明：[NPM10XX_RSTREAS_SW](#ga7cb7ea1ce7b2bc41f0388c2f5b740b5a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

软件复位（Software Reset），通过任务寄存器（Task Register）触发。

<a id="r_gaea70fe0bf1a583800673b9a5335dce85"></a>

```c
#define NPM10XX_RSTREAS_SHIPERR BIT(7)
```

相关声明：[NPM10XX_RSTREAS_SHIPERR](#gaea70fe0bf1a583800673b9a5335dce85)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

进入运输模式（Ship Mode）出错引起的复位。

<a id="r_ga0738fae4151077589ea32b200769ab24"></a>

```c
#define NPM10XX_RSTREAS_TIMER BIT(8)
```

相关声明：[NPM10XX_RSTREAS_TIMER](#ga0738fae4151077589ea32b200769ab24)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因定时器（Timer）而退出深度休眠模式（Hibernate Mode）。

<a id="r_ga5a06e1bd3cc551ee5001f7e27c3b5e14"></a>

```c
#define NPM10XX_RSTREAS_BUTTON BIT(9)
```

相关声明：[NPM10XX_RSTREAS_BUTTON](#ga5a06e1bd3cc551ee5001f7e27c3b5e14)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因 SHPHLD 按钮而退出深度休眠模式（Hibernate Mode）。

<a id="r_ga13b8e4b033016d7865f25ff58b579127"></a>

```c
#define NPM10XX_RSTREAS_HIBERNATEVBUS BIT(10)
```

相关声明：[NPM10XX_RSTREAS_HIBERNATEVBUS](#ga13b8e4b033016d7865f25ff58b579127)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因 VBUS 断开而退出 VBUS 深度休眠模式（Hibernate Mode）。

<a id="r_ga680b731e93c19e430b5c3b1011337d3f"></a>

```c
#define NPM10XX_RSTREAS_WATCHDOGSOFT BIT(11)
```

相关声明：[NPM10XX_RSTREAS_WATCHDOGSOFT](#ga680b731e93c19e430b5c3b1011337d3f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗软复位（Watchdog Soft Reset）。

## 5.6\_模数转换事件（ADC events）

<a id="r_ga8d1937763166b6efa9ab159b3a571144"></a>

```c
#define NPM10XX_EVENT_ADC_VBAT BIT64(0)
```

相关声明：[NPM10XX_EVENT_ADC_VBAT](#ga8d1937763166b6efa9ab159b3a571144)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VBAT 转换已就绪（Conversion Ready）。

<a id="r_gad542c7d4583b8c0ac2b7c102af6899df"></a>

```c
#define NPM10XX_EVENT_ADC_NTC BIT64(1)
```

相关声明：[NPM10XX_EVENT_ADC_NTC](#gad542c7d4583b8c0ac2b7c102af6899df)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 NTC 转换已就绪（Conversion Ready）。

<a id="r_gab3bb0ccba78d150cba683b8d75b0db1e"></a>

```c
#define NPM10XX_EVENT_ADC_DIETEMP BIT64(2)
```

相关声明：[NPM10XX_EVENT_ADC_DIETEMP](#gab3bb0ccba78d150cba683b8d75b0db1e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的芯片温度（Die Temperature）转换已就绪。

<a id="r_gad639d50b74e582bce18a5c122f12049e"></a>

```c
#define NPM10XX_EVENT_ADC_VSYS BIT64(3)
```

相关声明：[NPM10XX_EVENT_ADC_VSYS](#gad639d50b74e582bce18a5c122f12049e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VSYS 转换已就绪（Conversion Ready）。

<a id="r_gaf7c1e1854dde20198a8df113a17d60d8"></a>

```c
#define NPM10XX_EVENT_ADC_VBUS BIT64(4)
```

相关声明：[NPM10XX_EVENT_ADC_VBUS](#gaf7c1e1854dde20198a8df113a17d60d8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VBUS 转换已就绪（Conversion Ready）。

<a id="r_ga749dfc8a4494e29423d74dd98e7e9c56"></a>

```c
#define NPM10XX_EVENT_ADC_VSET BIT64(5)
```

相关声明：[NPM10XX_EVENT_ADC_VSET](#ga749dfc8a4494e29423d74dd98e7e9c56)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VSET 转换已就绪（Conversion Ready）。

<a id="r_ga629d48940054d66218e62c3113654e1b"></a>

```c
#define NPM10XX_EVENT_ADC_OFFSET BIT64(6)
```

相关声明：[NPM10XX_EVENT_ADC_OFFSET](#ga629d48940054d66218e62c3113654e1b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 OFFSET 转换已就绪（Conversion Ready）。

<a id="r_ga6332911d314425042f86638253a1b4e9"></a>

```c
#define NPM10XX_EVENT_IBATVBAT BIT64(7)
```

相关声明：[NPM10XX_EVENT_IBATVBAT](#ga6332911d314425042f86638253a1b4e9)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

IBAT／VBAT 电池电流和／或电压转换已就绪（Conversion Ready）。

## 5.7\_充电器事件（CHARGER events）

<a id="r_gacdd4bb994fdc27cca82d76a8f4be0144"></a>

```c
#define NPM10XX_EVENT_CHARGE BIT64(8)
```

相关声明：[NPM10XX_EVENT_CHARGE](#gacdd4bb994fdc27cca82d76a8f4be0144)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电器已启动（Charger Started）。

<a id="r_ga43ea2f80d5d5ad538e46e97bf6ad68e8"></a>

```c
#define NPM10XX_EVENT_DISCHARGE BIT64(9)
```

相关声明：[NPM10XX_EVENT_DISCHARGE](#ga43ea2f80d5d5ad538e46e97bf6ad68e8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池放电已开始（Battery Discharge Started）。

<a id="r_ga8d024bf2914c1885c10b97d97c85121e"></a>

```c
#define NPM10XX_EVENT_DROPOUT BIT64(10)
```

相关声明：[NPM10XX_EVENT_DROPOUT](#ga8d024bf2914c1885c10b97d97c85121e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

压差控制环路已激活（Dropout Loop Activated）。

<a id="r_ga50f4ff61c0f3e281764a2099d8eb107f"></a>

```c
#define NPM10XX_EVENT_SUPPLEMENT BIT64(11)
```

相关声明：[NPM10XX_EVENT_SUPPLEMENT](#ga50f4ff61c0f3e281764a2099d8eb107f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

补充供电模式已激活（Supplement Mode Activated）。

<a id="r_ga83ee75ea61f37a26c91df2806cbedf77"></a>

```c
#define NPM10XX_EVENT_COMPLETE BIT64(12)
```

相关声明：[NPM10XX_EVENT_COMPLETE](#ga83ee75ea61f37a26c91df2806cbedf77)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池充电已完成（Battery Charging Completed）。

<a id="r_gac70fb8807559882b67dd551a58d0e240"></a>

```c
#define NPM10XX_EVENT_BATILIM BIT64(13)
```

相关声明：[NPM10XX_EVENT_BATILIM](#gac70fb8807559882b67dd551a58d0e240)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池放电限制已激活（Battery Discharge Limit Activated）。

<a id="r_ga8612c9106a981d48574456ec6d4aeb9f"></a>

```c
#define NPM10XX_EVENT_ITERM BIT64(14)
```

相关声明：[NPM10XX_EVENT_ITERM](#ga8612c9106a981d48574456ec6d4aeb9f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电电流（Charging Current）低于 `ITERM`。

<a id="r_ga1b280e6da1cde61fdf29037a8b2e473c"></a>

```c
#define NPM10XX_EVENT_VTERM BIT64(16)
```

相关声明：[NPM10XX_EVENT_VTERM](#ga1b280e6da1cde61fdf29037a8b2e473c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）已达到 `VTERM`。

<a id="r_gac8ab9f678ea4975623dc696611857998"></a>

```c
#define NPM10XX_EVENT_RECHARGE BIT64(17)
```

相关声明：[NPM10XX_EVENT_RECHARGE](#gac8ab9f678ea4975623dc696611857998)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）低于 `VRECHARGE`。

<a id="r_ga6435230e68729fa078f0f55ec64cd0ca"></a>

```c
#define NPM10XX_EVENT_VTHROTTLE BIT64(18)
```

相关声明：[NPM10XX_EVENT_VTHROTTLE](#ga6435230e68729fa078f0f55ec64cd0ca)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VTHROTTLE`。

<a id="r_gafe6fd2bf306f411e8205be428fafd5cc"></a>

```c
#define NPM10XX_EVENT_VWEAK BIT64(19)
```

相关声明：[NPM10XX_EVENT_VWEAK](#gafe6fd2bf306f411e8205be428fafd5cc)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VWEAK`。

<a id="r_gae932ded31cc4cf403b66f34853362cbd"></a>

```c
#define NPM10XX_EVENT_VTRICKLE BIT64(20)
```

相关声明：[NPM10XX_EVENT_VTRICKLE](#gae932ded31cc4cf403b66f34853362cbd)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VTRICKLEFAST`。

<a id="r_ga623b4394d8f00798d934d83f63622656"></a>

```c
#define NPM10XX_EVENT_VBATLOW BIT64(21)
```

相关声明：[NPM10XX_EVENT_VBATLOW](#ga623b4394d8f00798d934d83f63622656)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）低于 `VBATLOW`。

<a id="r_ga75a1e71dec354020c692a7311c44ea0f"></a>

```c
#define NPM10XX_EVENT_NTCCOLD BIT64(24)
```

相关声明：[NPM10XX_EVENT_NTCCOLD](#ga75a1e71dec354020c692a7311c44ea0f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于寒冷区域（Cold Region）。

<a id="r_ga155922438a707ad10c3d5a3292e0c75c"></a>

```c
#define NPM10XX_EVENT_NTCCOOL BIT64(25)
```

相关声明：[NPM10XX_EVENT_NTCCOOL](#ga155922438a707ad10c3d5a3292e0c75c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于较冷区域（Cool Region）。

<a id="r_ga22d0d980fd12fa98a6350451ae7edf59"></a>

```c
#define NPM10XX_EVENT_NTCWARM BIT64(26)
```

相关声明：[NPM10XX_EVENT_NTCWARM](#ga22d0d980fd12fa98a6350451ae7edf59)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于温暖区域（Warm Region）。

<a id="r_ga2bdf786c80456f00a39c160d1a046986"></a>

```c
#define NPM10XX_EVENT_NTCHOT BIT64(27)
```

相关声明：[NPM10XX_EVENT_NTCHOT](#ga2bdf786c80456f00a39c160d1a046986)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于高温区域（Hot Region）。

<a id="r_ga3e354453e00614129bbcf58583391f7b"></a>

```c
#define NPM10XX_EVENT_DIETEMP BIT64(28)
```

相关声明：[NPM10XX_EVENT_DIETEMP](#ga3e354453e00614129bbcf58583391f7b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

芯片温度（Die Temperature）超过 `TCHGREDUCE`。

<a id="r_gadd6c59e1160fb519a38abb8a2cc924ea"></a>

```c
#define NPM10XX_EVENT_ERROR BIT64(29)
```

相关声明：[NPM10XX_EVENT_ERROR](#gadd6c59e1160fb519a38abb8a2cc924ea)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电错误（Charging Error）。

<a id="r_gaef29381e85d461ccf05009bcb9b2e5ff"></a>

```c
#define NPM10XX_EVENT_VSYSWRNPE BIT64(30)
```

相关声明：[NPM10XX_EVENT_VSYSWRNPE](#gaef29381e85d461ccf05009bcb9b2e5ff)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 `VSYSWRNR` 阈值（Threshold）。

<a id="r_gae953485b6e852cbaee0d2e62db1d02f1"></a>

```c
#define NPM10XX_EVENT_VSYSWRNNE BIT64(31)
```

相关声明：[NPM10XX_EVENT_VSYSWRNNE](#gae953485b6e852cbaee0d2e62db1d02f1)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 `VSYSWRNF` 阈值（Threshold）。

## 5.8\_SYSREG／VBUS事件（SYSREG/VBUS events）

<a id="r_ga18b584396d3620d541e761a7f68ed94a"></a>

```c
#define NPM10XX_EVENT_VBUSOVPE BIT64(32)
```

相关声明：[NPM10XX_EVENT_VBUSOVPE](#ga18b584396d3620d541e761a7f68ed94a)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS 过压（Overvoltage）。

<a id="r_ga073825db8abf74874653bf48d52573e5"></a>

```c
#define NPM10XX_EVENT_VBUSOVNE BIT64(33)
```

相关声明：[NPM10XX_EVENT_VBUSOVNE](#ga073825db8abf74874653bf48d52573e5)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 过压（Overvoltage）已消除。

<a id="r_ga078b8604922045a722e4d777b4a2cfa9"></a>

```c
#define NPM10XX_EVENT_VBUSUNDERPE BIT64(34)
```

相关声明：[NPM10XX_EVENT_VBUSUNDERPE](#ga078b8604922045a722e4d777b4a2cfa9)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS 欠压（Undervoltage）。

<a id="r_ga86dd9b11368443698e13bc6c17b4575c"></a>

```c
#define NPM10XX_EVENT_VBUSUNDERNE BIT64(35)
```

相关声明：[NPM10XX_EVENT_VBUSUNDERNE](#ga86dd9b11368443698e13bc6c17b4575c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 欠压（Undervoltage）已消除。

<a id="r_gaab1a75798b2252723392c6b8ed0682f8"></a>

```c
#define NPM10XX_EVENT_VBUSPRESENTPE BIT64(36)
```

相关声明：[NPM10XX_EVENT_VBUSPRESENTPE](#gaab1a75798b2252723392c6b8ed0682f8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS。

<a id="r_ga1fdd5ae85149b0d31d51df4727968396"></a>

```c
#define NPM10XX_EVENT_VBUSPRESENTNE BIT64(37)
```

相关声明：[NPM10XX_EVENT_VBUSPRESENTNE](#ga1fdd5ae85149b0d31d51df4727968396)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 已移除。

<a id="r_ga443745fe8fe1c9145f2e4b80e8332068"></a>

```c
#define NPM10XX_EVENT_VBUSOKPE BIT64(38)
```

相关声明：[NPM10XX_EVENT_VBUSOKPE](#ga443745fe8fe1c9145f2e4b80e8332068)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 在限制范围内（Within Limit）。

<a id="r_gaf46bb53cfebec5cfeea06a0eac9a7b8b"></a>

```c
#define NPM10XX_EVENT_VBUSOKNE BIT64(39)
```

相关声明：[NPM10XX_EVENT_VBUSOKNE](#gaf46bb53cfebec5cfeea06a0eac9a7b8b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 超出限制范围（Outside the Limit）。

## 5.9\_通用输入输出事件（GPIO events）

<a id="r_gabb776a944d00755f4a7b3b0049833486"></a>

```c
#define NPM10XX_EVENT_GPIO0PE BIT64(40)
```

相关声明：[NPM10XX_EVENT_GPIO0PE](#gabb776a944d00755f4a7b3b0049833486)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO0 上出现上升沿（Rising Edge）。

<a id="r_gaef166e04ca328fc79ced45ef80307b26"></a>

```c
#define NPM10XX_EVENT_GPIO0NE BIT64(41)
```

相关声明：[NPM10XX_EVENT_GPIO0NE](#gaef166e04ca328fc79ced45ef80307b26)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO0 上出现下降沿（Falling Edge）。

<a id="r_gab8a55e8cd43f312c6024f7b84c145fdf"></a>

```c
#define NPM10XX_EVENT_GPIO1PE BIT64(42)
```

相关声明：[NPM10XX_EVENT_GPIO1PE](#gab8a55e8cd43f312c6024f7b84c145fdf)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO1 上出现上升沿（Rising Edge）。

<a id="r_gad606f6364d310d5d794583eea12cae48"></a>

```c
#define NPM10XX_EVENT_GPIO1NE BIT64(43)
```

相关声明：[NPM10XX_EVENT_GPIO1NE](#gad606f6364d310d5d794583eea12cae48)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO1 上出现下降沿（Falling Edge）。

<a id="r_gae7170a3c6576d9c771f4366e24990c42"></a>

```c
#define NPM10XX_EVENT_GPIO2PE BIT64(44)
```

相关声明：[NPM10XX_EVENT_GPIO2PE](#gae7170a3c6576d9c771f4366e24990c42)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO2 上出现上升沿（Rising Edge）。

<a id="r_ga0cf08cd51b179ad270b90f478f754f22"></a>

```c
#define NPM10XX_EVENT_GPIO2NE BIT64(45)
```

相关声明：[NPM10XX_EVENT_GPIO2NE](#ga0cf08cd51b179ad270b90f478f754f22)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO2 上出现下降沿（Falling Edge）。

## 5.10\_系统事件（SYSTEM events）

<a id="r_gaedf4086fe313a695e1195cad941f5fe8"></a>

```c
#define NPM10XX_EVENT_TIMERTIMEOUT BIT64(48)
```

相关声明：[NPM10XX_EVENT_TIMERTIMEOUT](#gaedf4086fe313a695e1195cad941f5fe8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

通用定时器到期（General Purpose Timer Expired）。

<a id="r_ga5204062fa8946f9f672766fa9f365763"></a>

```c
#define NPM10XX_EVENT_TIMERFREE BIT64(49)
```

相关声明：[NPM10XX_EVENT_TIMERFREE](#ga5204062fa8946f9f672766fa9f365763)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

定时器空闲事件（Timer Free Event）。

<a id="r_gaf5b5dd70a03d270c6aed0dbf69637d11"></a>

```c
#define NPM10XX_EVENT_TIMERPREWARN BIT64(50)
```

相关声明：[NPM10XX_EVENT_TIMERPREWARN](#gaf5b5dd70a03d270c6aed0dbf69637d11)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

定时器到期前的预警事件（Pre-Warning Event）。

<a id="r_ga8ceb82aab97e7066f2158ff35db5bf4d"></a>

```c
#define NPM10XX_EVENT_LDOSWOC BIT64(51)
```

相关声明：[NPM10XX_EVENT_LDOSWOC](#ga8ceb82aab97e7066f2158ff35db5bf4d)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

LOADSW1／LDO1 过流（Overcurrent）。

<a id="r_ga60df5df26a6fb86ba906d244be5aed5e"></a>

```c
#define NPM10XX_EVENT_LOADSWOC BIT64(52)
```

相关声明：[NPM10XX_EVENT_LOADSWOC](#ga60df5df26a6fb86ba906d244be5aed5e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

LOADSW2 过流（Overcurrent）。

<a id="r_ga5f382672aab5750ade14b9ed069de1ba"></a>

```c
#define NPM10XX_EVENT_SHPHLDPE BIT64(53)
```

相关声明：[NPM10XX_EVENT_SHPHLDPE](#ga5f382672aab5750ade14b9ed069de1ba)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

SHPHLD 上出现上升沿（Rising Edge）。

<a id="r_ga7a27f6e42764fc6958d711878cc9f07a"></a>

```c
#define NPM10XX_EVENT_SHPHLDNE BIT64(54)
```

相关声明：[NPM10XX_EVENT_SHPHLDNE](#ga7a27f6e42764fc6958d711878cc9f07a)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

SHPHLD 上出现下降沿（Falling Edge）。

<a id="r_gab9c1c24039d32874c6769f6b89f1bf7d"></a>

```c
#define NPM10XX_EVENT_ADCTEST BIT64(55)
```

相关声明：[NPM10XX_EVENT_ADCTEST](#gab9c1c24039d32874c6769f6b89f1bf7d)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 测试完成（Test Finished）。

## 5.11\_详细说明（Detailed Documentation）

<a id="gab3bb0ccba78d150cba683b8d75b0db1e"></a>

### `NPM10XX_EVENT_ADC_DIETEMP`

```c
#define NPM10XX_EVENT_ADC_DIETEMP BIT64(2)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的芯片温度（Die Temperature）转换已就绪。

<a id="gad542c7d4583b8c0ac2b7c102af6899df"></a>

### `NPM10XX_EVENT_ADC_NTC`

```c
#define NPM10XX_EVENT_ADC_NTC BIT64(1)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 NTC 转换已就绪（Conversion Ready）。

<a id="ga629d48940054d66218e62c3113654e1b"></a>

### `NPM10XX_EVENT_ADC_OFFSET`

```c
#define NPM10XX_EVENT_ADC_OFFSET BIT64(6)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 OFFSET 转换已就绪（Conversion Ready）。

<a id="ga8d1937763166b6efa9ab159b3a571144"></a>

### `NPM10XX_EVENT_ADC_VBAT`

```c
#define NPM10XX_EVENT_ADC_VBAT BIT64(0)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 VBAT 转换已就绪（Conversion Ready）。

<a id="gaf7c1e1854dde20198a8df113a17d60d8"></a>

### `NPM10XX_EVENT_ADC_VBUS`

```c
#define NPM10XX_EVENT_ADC_VBUS BIT64(4)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 VBUS 转换已就绪（Conversion Ready）。

<a id="ga749dfc8a4494e29423d74dd98e7e9c56"></a>

### `NPM10XX_EVENT_ADC_VSET`

```c
#define NPM10XX_EVENT_ADC_VSET BIT64(5)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 VSET 转换已就绪（Conversion Ready）。

<a id="gad639d50b74e582bce18a5c122f12049e"></a>

### `NPM10XX_EVENT_ADC_VSYS`

```c
#define NPM10XX_EVENT_ADC_VSYS BIT64(3)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 的 VSYS 转换已就绪（Conversion Ready）。

<a id="gab9c1c24039d32874c6769f6b89f1bf7d"></a>

### `NPM10XX_EVENT_ADCTEST`

```c
#define NPM10XX_EVENT_ADCTEST BIT64(55)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

ADC 测试完成（Test Finished）。

<a id="gac70fb8807559882b67dd551a58d0e240"></a>

### `NPM10XX_EVENT_BATILIM`

```c
#define NPM10XX_EVENT_BATILIM BIT64(13)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池放电限制已激活（Battery Discharge Limit Activated）。

<a id="gacdd4bb994fdc27cca82d76a8f4be0144"></a>

### `NPM10XX_EVENT_CHARGE`

```c
#define NPM10XX_EVENT_CHARGE BIT64(8)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

充电器已启动（Charger Started）。

<a id="ga83ee75ea61f37a26c91df2806cbedf77"></a>

### `NPM10XX_EVENT_COMPLETE`

```c
#define NPM10XX_EVENT_COMPLETE BIT64(12)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池充电已完成（Battery Charging Completed）。

<a id="ga3e354453e00614129bbcf58583391f7b"></a>

### `NPM10XX_EVENT_DIETEMP`

```c
#define NPM10XX_EVENT_DIETEMP BIT64(28)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

芯片温度（Die Temperature）超过 `TCHGREDUCE`。

<a id="ga43ea2f80d5d5ad538e46e97bf6ad68e8"></a>

### `NPM10XX_EVENT_DISCHARGE`

```c
#define NPM10XX_EVENT_DISCHARGE BIT64(9)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池放电已开始（Battery Discharge Started）。

<a id="ga8d024bf2914c1885c10b97d97c85121e"></a>

### `NPM10XX_EVENT_DROPOUT`

```c
#define NPM10XX_EVENT_DROPOUT BIT64(10)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

压差控制环路已激活（Dropout Loop Activated）。

<a id="gadd6c59e1160fb519a38abb8a2cc924ea"></a>

### `NPM10XX_EVENT_ERROR`

```c
#define NPM10XX_EVENT_ERROR BIT64(29)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

充电错误（Charging Error）。

<a id="gaef166e04ca328fc79ced45ef80307b26"></a>

### `NPM10XX_EVENT_GPIO0NE`

```c
#define NPM10XX_EVENT_GPIO0NE BIT64(41)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO0 上出现下降沿（Falling Edge）。

<a id="gabb776a944d00755f4a7b3b0049833486"></a>

### `NPM10XX_EVENT_GPIO0PE`

```c
#define NPM10XX_EVENT_GPIO0PE BIT64(40)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO0 上出现上升沿（Rising Edge）。

<a id="gad606f6364d310d5d794583eea12cae48"></a>

### `NPM10XX_EVENT_GPIO1NE`

```c
#define NPM10XX_EVENT_GPIO1NE BIT64(43)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO1 上出现下降沿（Falling Edge）。

<a id="gab8a55e8cd43f312c6024f7b84c145fdf"></a>

### `NPM10XX_EVENT_GPIO1PE`

```c
#define NPM10XX_EVENT_GPIO1PE BIT64(42)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO1 上出现上升沿（Rising Edge）。

<a id="ga0cf08cd51b179ad270b90f478f754f22"></a>

### `NPM10XX_EVENT_GPIO2NE`

```c
#define NPM10XX_EVENT_GPIO2NE BIT64(45)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO2 上出现下降沿（Falling Edge）。

<a id="gae7170a3c6576d9c771f4366e24990c42"></a>

### `NPM10XX_EVENT_GPIO2PE`

```c
#define NPM10XX_EVENT_GPIO2PE BIT64(44)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

GPIO2 上出现上升沿（Rising Edge）。

<a id="ga6332911d314425042f86638253a1b4e9"></a>

### `NPM10XX_EVENT_IBATVBAT`

```c
#define NPM10XX_EVENT_IBATVBAT BIT64(7)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

IBAT／VBAT 电池电流和／或电压转换已就绪（Conversion Ready）。

<a id="ga8612c9106a981d48574456ec6d4aeb9f"></a>

### `NPM10XX_EVENT_ITERM`

```c
#define NPM10XX_EVENT_ITERM BIT64(14)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

充电电流（Charging Current）低于 `ITERM`。

<a id="ga8ceb82aab97e7066f2158ff35db5bf4d"></a>

### `NPM10XX_EVENT_LDOSWOC`

```c
#define NPM10XX_EVENT_LDOSWOC BIT64(51)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

LOADSW1／LDO1 过流（Overcurrent）。

<a id="ga60df5df26a6fb86ba906d244be5aed5e"></a>

### `NPM10XX_EVENT_LOADSWOC`

```c
#define NPM10XX_EVENT_LOADSWOC BIT64(52)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

LOADSW2 过流（Overcurrent）。

<a id="ga75a1e71dec354020c692a7311c44ea0f"></a>

### `NPM10XX_EVENT_NTCCOLD`

```c
#define NPM10XX_EVENT_NTCCOLD BIT64(24)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池温度处于寒冷区域（Cold Region）。

<a id="ga155922438a707ad10c3d5a3292e0c75c"></a>

### `NPM10XX_EVENT_NTCCOOL`

```c
#define NPM10XX_EVENT_NTCCOOL BIT64(25)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池温度处于较冷区域（Cool Region）。

<a id="ga2bdf786c80456f00a39c160d1a046986"></a>

### `NPM10XX_EVENT_NTCHOT`

```c
#define NPM10XX_EVENT_NTCHOT BIT64(27)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池温度处于高温区域（Hot Region）。

<a id="ga22d0d980fd12fa98a6350451ae7edf59"></a>

### `NPM10XX_EVENT_NTCWARM`

```c
#define NPM10XX_EVENT_NTCWARM BIT64(26)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池温度处于温暖区域（Warm Region）。

<a id="gac8ab9f678ea4975623dc696611857998"></a>

### `NPM10XX_EVENT_RECHARGE`

```c
#define NPM10XX_EVENT_RECHARGE BIT64(17)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）低于 `VRECHARGE`。

<a id="ga7a27f6e42764fc6958d711878cc9f07a"></a>

### `NPM10XX_EVENT_SHPHLDNE`

```c
#define NPM10XX_EVENT_SHPHLDNE BIT64(54)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

SHPHLD 上出现下降沿（Falling Edge）。

<a id="ga5f382672aab5750ade14b9ed069de1ba"></a>

### `NPM10XX_EVENT_SHPHLDPE`

```c
#define NPM10XX_EVENT_SHPHLDPE BIT64(53)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

SHPHLD 上出现上升沿（Rising Edge）。

<a id="ga50f4ff61c0f3e281764a2099d8eb107f"></a>

### `NPM10XX_EVENT_SUPPLEMENT`

```c
#define NPM10XX_EVENT_SUPPLEMENT BIT64(11)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

补充供电模式已激活（Supplement Mode Activated）。

<a id="ga5204062fa8946f9f672766fa9f365763"></a>

### `NPM10XX_EVENT_TIMERFREE`

```c
#define NPM10XX_EVENT_TIMERFREE BIT64(49)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

定时器空闲事件（Timer Free Event）。

<a id="gaf5b5dd70a03d270c6aed0dbf69637d11"></a>

### `NPM10XX_EVENT_TIMERPREWARN`

```c
#define NPM10XX_EVENT_TIMERPREWARN BIT64(50)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

定时器到期前的预警事件（Pre-Warning Event）。

<a id="gaedf4086fe313a695e1195cad941f5fe8"></a>

### `NPM10XX_EVENT_TIMERTIMEOUT`

```c
#define NPM10XX_EVENT_TIMERTIMEOUT BIT64(48)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

通用定时器到期（General Purpose Timer Expired）。

<a id="ga623b4394d8f00798d934d83f63622656"></a>

### `NPM10XX_EVENT_VBATLOW`

```c
#define NPM10XX_EVENT_VBATLOW BIT64(21)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）低于 `VBATLOW`。

<a id="gaf46bb53cfebec5cfeea06a0eac9a7b8b"></a>

### `NPM10XX_EVENT_VBUSOKNE`

```c
#define NPM10XX_EVENT_VBUSOKNE BIT64(39)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

VBUS 超出限制范围（Outside the Limit）。

<a id="ga443745fe8fe1c9145f2e4b80e8332068"></a>

### `NPM10XX_EVENT_VBUSOKPE`

```c
#define NPM10XX_EVENT_VBUSOKPE BIT64(38)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

VBUS 在限制范围内（Within Limit）。

<a id="ga073825db8abf74874653bf48d52573e5"></a>

### `NPM10XX_EVENT_VBUSOVNE`

```c
#define NPM10XX_EVENT_VBUSOVNE BIT64(33)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

VBUS 过压（Overvoltage）已消除。

<a id="ga18b584396d3620d541e761a7f68ed94a"></a>

### `NPM10XX_EVENT_VBUSOVPE`

```c
#define NPM10XX_EVENT_VBUSOVPE BIT64(32)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

检测到 VBUS 过压（Overvoltage）。

<a id="ga1fdd5ae85149b0d31d51df4727968396"></a>

### `NPM10XX_EVENT_VBUSPRESENTNE`

```c
#define NPM10XX_EVENT_VBUSPRESENTNE BIT64(37)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

VBUS 已移除。

<a id="gaab1a75798b2252723392c6b8ed0682f8"></a>

### `NPM10XX_EVENT_VBUSPRESENTPE`

```c
#define NPM10XX_EVENT_VBUSPRESENTPE BIT64(36)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

检测到 VBUS。

<a id="ga86dd9b11368443698e13bc6c17b4575c"></a>

### `NPM10XX_EVENT_VBUSUNDERNE`

```c
#define NPM10XX_EVENT_VBUSUNDERNE BIT64(35)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

VBUS 欠压（Undervoltage）已消除。

<a id="ga078b8604922045a722e4d777b4a2cfa9"></a>

### `NPM10XX_EVENT_VBUSUNDERPE`

```c
#define NPM10XX_EVENT_VBUSUNDERPE BIT64(34)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

检测到 VBUS 欠压（Undervoltage）。

<a id="gae953485b6e852cbaee0d2e62db1d02f1"></a>

### `NPM10XX_EVENT_VSYSWRNNE`

```c
#define NPM10XX_EVENT_VSYSWRNNE BIT64(31)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

检测到 `VSYSWRNF` 阈值（Threshold）。

<a id="gaef29381e85d461ccf05009bcb9b2e5ff"></a>

### `NPM10XX_EVENT_VSYSWRNPE`

```c
#define NPM10XX_EVENT_VSYSWRNPE BIT64(30)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

检测到 `VSYSWRNR` 阈值（Threshold）。

<a id="ga1b280e6da1cde61fdf29037a8b2e473c"></a>

### `NPM10XX_EVENT_VTERM`

```c
#define NPM10XX_EVENT_VTERM BIT64(16)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）已达到 `VTERM`。

<a id="ga6435230e68729fa078f0f55ec64cd0ca"></a>

### `NPM10XX_EVENT_VTHROTTLE`

```c
#define NPM10XX_EVENT_VTHROTTLE BIT64(18)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）高于 `VTHROTTLE`。

<a id="gae932ded31cc4cf403b66f34853362cbd"></a>

### `NPM10XX_EVENT_VTRICKLE`

```c
#define NPM10XX_EVENT_VTRICKLE BIT64(20)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）高于 `VTRICKLEFAST`。

<a id="gafe6fd2bf306f411e8205be428fafd5cc"></a>

### `NPM10XX_EVENT_VWEAK`

```c
#define NPM10XX_EVENT_VWEAK BIT64(19)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电池电压（Battery Voltage）高于 `VWEAK`。

<a id="ga1d6e5782bf0e1c2ea395a2b9dd884723"></a>

### `NPM10XX_RSTREAS_BOOTMON`

```c
#define NPM10XX_RSTREAS_BOOTMON BIT(1)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

启动监视器复位（Boot Monitor Reset）。

<a id="ga5a06e1bd3cc551ee5001f7e27c3b5e14"></a>

### `NPM10XX_RSTREAS_BUTTON`

```c
#define NPM10XX_RSTREAS_BUTTON BIT(9)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

因 SHPHLD 按钮而退出深度休眠模式（Hibernate Mode）。

<a id="gaa01e18082e07f933a6bf0c4a8f6f24c1"></a>

### `NPM10XX_RSTREAS_HIBERNATE`

```c
#define NPM10XX_RSTREAS_HIBERNATE BIT(0)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

因连接 VBUS 而退出 VBAT 深度休眠模式（Hibernate Mode）。

<a id="ga13b8e4b033016d7865f25ff58b579127"></a>

### `NPM10XX_RSTREAS_HIBERNATEVBUS`

```c
#define NPM10XX_RSTREAS_HIBERNATEVBUS BIT(10)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

因 VBUS 断开而退出 VBUS 深度休眠模式（Hibernate Mode）。

<a id="ga762cca53f636dd8a3e2fcd7017b3abdd"></a>

### `NPM10XX_RSTREAS_LONGPRESS`

```c
#define NPM10XX_RSTREAS_LONGPRESS BIT(3)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

长按复位（Longpress Reset）。

<a id="gad79d6bf2c570e8a51700e17cfeb5a817"></a>

### `NPM10XX_RSTREAS_POF`

```c
#define NPM10XX_RSTREAS_POF BIT(5)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

电源故障复位（POF Reset）。

<a id="gaea70fe0bf1a583800673b9a5335dce85"></a>

### `NPM10XX_RSTREAS_SHIPERR`

```c
#define NPM10XX_RSTREAS_SHIPERR BIT(7)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

进入运输模式（Ship Mode）出错引起的复位。

<a id="ga7cb7ea1ce7b2bc41f0388c2f5b740b5a"></a>

### `NPM10XX_RSTREAS_SW`

```c
#define NPM10XX_RSTREAS_SW BIT(6)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

软件复位（Software Reset），通过任务寄存器（Task Register）触发。

<a id="ga167467b923a5f81bdaec1e4e1d91a368"></a>

### `NPM10XX_RSTREAS_THERMAL`

```c
#define NPM10XX_RSTREAS_THERMAL BIT(4)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

热关断复位（Thermal Shutdown Reset）。

<a id="ga0738fae4151077589ea32b200769ab24"></a>

### `NPM10XX_RSTREAS_TIMER`

```c
#define NPM10XX_RSTREAS_TIMER BIT(8)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

因定时器（Timer）而退出深度休眠模式（Hibernate Mode）。

<a id="gaa0266596048079a4b90dd3df6199666a"></a>

### `NPM10XX_RSTREAS_WATCHDOG`

```c
#define NPM10XX_RSTREAS_WATCHDOG BIT(2)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

看门狗复位（Watchdog Reset）。

<a id="ga680b731e93c19e430b5c3b1011337d3f"></a>

### `NPM10XX_RSTREAS_WATCHDOGSOFT`

```c
#define NPM10XX_RSTREAS_WATCHDOGSOFT BIT(11)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

看门狗软复位（Watchdog Soft Reset）。

<a id="ga917abc6c5ed263f28a04bc96598d0009"></a>

### `npm10xx_callback_handler_t`

```c
typedef void(* npm10xx_callback_handler_t) (const struct device *mfd_npm10xx_dev, struct mfd_npm10xx_event_callback *cb, npm10xx_event_t events)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

定义应用程序回调处理函数的签名（Function Signature）。

注（Note）：如果原始 `struct mfd_npm10xx_event_callback` 存放于另一个私有结构体中，可使用 `cb` 指针通过 `CONTAINER_OF()` 获取私有数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mfd_npm10xx_dev` | nPM10xx 多功能设备（MFD）。 |
| `cb` | 拥有此处理函数的原始 `struct mfd_npm10xx_event_callback`。 |
| `events` | 触发回调处理函数的事件掩码（Event Mask）。 |

<a id="gab2a9bae08f020392e33bfb98efff2f32"></a>

### `npm10xx_event_t`

```c
typedef uint64_t npm10xx_event_t
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

标识供事件回调（Event Callback）使用的一组事件。

<a id="ga4cdc0f26a0193e0c1e58404f632029c7"></a>

### `npm10xx_rstreas_t`

```c
typedef uint16_t npm10xx_rstreas_t
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

标识复位原因（Reset Reason）。

获取后，预期与 `NPM10XX_RSTREAS_*` 宏进行比对。

<a id="ga164233569fe1f2e9ee00acc74e6f92c7"></a>

### `mfd_npm10xx_hibernate_mode`

```c
enum mfd_npm10xx_hibernate_mode
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

nPM10xx 深度休眠模式（Hibernate Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_HIBERNATE_VBAT` | 由 VBAT 供电时进入深度休眠（Hibernate）。 |
| `NPM10XX_HIBERNATE_VBUS_WAIT` | 由 VBUS 供电时进入深度休眠（Hibernate），等待充电完成。 |
| `NPM10XX_HIBERNATE_VBUS_NOWAIT` | 由 VBUS 供电时进入深度休眠（Hibernate），不等待充电完成。 |

<a id="gab6640de2b0c8007f3b8f13b31a66a00a"></a>

### `mfd_npm10xx_standby_op`

```c
enum mfd_npm10xx_standby_op
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

nPM10xx 待机操作（Standby Operations）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_STANDBY1_ENTER_WAIT` | 进入 VBUS 待机 1 模式（Standby1），VBUS 最高为 12 V，等待充电完成。 |
| `NPM10XX_STANDBY1_ENTER_NOWAIT` | 进入 VBUS 待机 1 模式（Standby1），VBUS 最高为 12 V，不等待充电完成。 |
| `NPM10XX_STANDBY2_ENTER_WAIT` | 进入 VBUS 待机 2 模式（Standby2），VBUS 最高为 5.5 V，等待充电完成。 |
| `NPM10XX_STANDBY2_ENTER_NOWAIT` | 进入 VBUS 待机 2 模式（Standby2），VBUS 最高为 5.5 V，不等待充电完成。 |
| `NPM10XX_STANDBY_EXIT` | 退出 VBUS 待机模式（Standby Mode）。 |

<a id="ga2bd8018f8aab66569a5fa052893e0c25"></a>

### `mfd_npm10xx_get_reset_reason()`

```c
int mfd_npm10xx_get_reset_reason ( const struct device * dev, npm10xx_rstreas_t * reason )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

获取并清除 nPM10xx 电源管理集成电路（PMIC）设备的复位原因（Reset Reason）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `reason` | 指向用于写入复位原因（Reset Reason）的变量的指针。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gad9da1db5f865d5a39f1bc348c6f5fafd"></a>

### `mfd_npm10xx_hibernate()`

```c
int mfd_npm10xx_hibernate ( const struct device * dev, enum mfd_npm10xx_hibernate_mode mode, k_timeout_t time )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

触发 nPM10xx 电源管理集成电路（PMIC）设备的深度休眠模式（Hibernate Mode）。

这将关闭所有电源输出及由其供电的所有设备。VBUS 出现时自动退出 VBAT 深度休眠模式（Hibernate Mode）；VBUS 移除时退出 VBUS 深度休眠模式。也可配置 SHPHLD 按钮以退出深度休眠模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `mode` | 要触发的深度休眠模式（Hibernate Mode）。 |
| `time` | 深度休眠模式（Hibernate Mode）的超时。使用 `K_FOREVER` 可无限期休眠。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gae67bf6f3efdcd948ebc5034e56540d71"></a>

### `mfd_npm10xx_manage_callback()`

```c
int mfd_npm10xx_manage_callback ( const struct device * dev, struct mfd_npm10xx_event_callback * callback, bool add )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

管理 nPM10xx 事件回调（Event Callbacks）。

移除回调时，若已没有回调处理某个事件，则禁用该事件的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `callback` | 指向要加入列表或从列表移除的回调（Callback）的指针。 |
| `add` | 指示插入或移除回调的布尔值（Boolean）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga5ff11ba2820c426dfeeb959b511b66f2"></a>

### `mfd_npm10xx_reset()`

```c
int mfd_npm10xx_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

复位 nPM10xx 电源管理集成电路（PMIC）设备。

关闭所有电源输出并执行内部复位（Internal Reset）。清除复位寄存器以外的所有寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gae775dcf89711147276ce11578ea7b6d2"></a>

### `mfd_npm10xx_scratch_read()`

```c
int mfd_npm10xx_scratch_read ( const struct device * dev, uint8_t * val )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

读取 `SCRATCH` 寄存器（Register）。

其内容跨复位保留，仅在上电复位／欠压复位（Power-On/Brown-Out Reset）和运输模式（Ship Mode）下清除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `val` | 读取到的 `SCRATCH` 值。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gaeb4cf7992c48aa4ad5747e58ec3a0020"></a>

### `mfd_npm10xx_scratch_write()`

```c
int mfd_npm10xx_scratch_write ( const struct device * dev, uint8_t val )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

写入 `SCRATCH` 寄存器（Register）。

其内容跨复位保留，仅在上电复位／欠压复位（Power-On/Brown-Out Reset）和运输模式（Ship Mode）下清除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `val` | 要写入的 `SCRATCH` 值。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gad6169c136db8c4d56552793d5da2e666"></a>

### `mfd_npm10xx_standby()`

```c
int mfd_npm10xx_standby ( const struct device * dev, enum mfd_npm10xx_standby_op operation )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

使 nPM10xx 电源管理集成电路（PMIC）设备进入或退出 VBUS 待机模式（Standby Mode）。

VBUS 待机模式（Standby Modes）降低从 VBUS 汲取的静态电流（Quiescent Current）。VBUS 不再存在时，设备自动退出这些模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `operation` | 要执行的待机操作（Standby Operation）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga5e155e4ba41999daccf9c2046ae60ad3"></a>

### `mfd_npm10xx_timer_set()`

```c
int mfd_npm10xx_timer_set ( const struct device * dev, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

设置 nPM10xx 设备定时器的超时值（Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `timeout` | 定时器超时值（Timer Timeout Value）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga6c7cf9f9606495ede2575174e60211fb"></a>

### `mfd_npm10xx_timer_start()`

```c
int mfd_npm10xx_timer_start ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

启动 nPM10xx 设备的定时器（Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga27625e2cceaea478514452bc0c9a2a1b"></a>

### `mfd_npm10xx_timer_status_get()`

```c
int mfd_npm10xx_timer_status_get ( const struct device * dev, bool * busy )
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

获取 nPM10xx 设备的定时器状态（Timer Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |
| `busy` | 指向用于存储忙状态（Busy Status）的 `bool` 变量的指针。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga144c19663856ce0a8fc32db02c867360"></a>

### `mfd_npm10xx_timer_stop()`

```c
int mfd_npm10xx_timer_stop ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

停止 nPM10xx 设备的定时器（Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | nPM10xx 多功能设备（MFD）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 5.12\_原页交叉引用（Cross References）

- [mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)
- [zephyr/drivers/mfd/npm10xx.h](../api_file_power_ots_reference/P001_zephyr__drivers__mfd__npm10xx.h_文件参考.md)
- [CONTAINER_OF()](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga164233569fe1f2e9ee00acc74e6f92c7a1cfa5ca4c49b40e9b78da256908a89d6"></a>
<a id="gga164233569fe1f2e9ee00acc74e6f92c7a9ce4e5b0bbe115a52dcb297f1cce6d64"></a>
<a id="gga164233569fe1f2e9ee00acc74e6f92c7ab1f535e92914be861eee60738b0280a4"></a>
<a id="ggab6640de2b0c8007f3b8f13b31a66a00aa5542f06dba5176ccfed1e024c2a75e50"></a>
<a id="ggab6640de2b0c8007f3b8f13b31a66a00aaa7523d301dc05610fdf8de9ca2996031"></a>
<a id="ggab6640de2b0c8007f3b8f13b31a66a00aaa9c904dbc9b8f339cd15fcf02991e7c4"></a>
<a id="ggab6640de2b0c8007f3b8f13b31a66a00aafae6fbde2b5e0a178a794ee43b7987d8"></a>
<a id="ggab6640de2b0c8007f3b8f13b31a66a00aac6b17d0c7aa2536c4c3af6900ee857bf"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_多功能设备（MFD）MAX2221X.md) · [返回大纲](大纲.md) · [下一章](P006_MQTT-SN 客户端库.md)
