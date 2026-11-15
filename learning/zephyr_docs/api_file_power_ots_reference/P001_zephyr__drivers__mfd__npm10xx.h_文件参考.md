---
id: learning.zephyr-docs.api-file-power-ots-reference.page-1
title: zephyr__drivers__mfd__npm10xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_mfd\_\_npm10xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

nPM10xx电源管理集成电路（PMIC）的多功能设备（MFD）接口。

<a id="details"></a>

```c
#include <zephyr/sys/slist.h>
#include <zephyr/sys/clock.h>
#include <zephyr/device.h>
```

查看此文件的源码。

nPM10xx电源管理集成电路（PMIC）的多功能设备（MFD）接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_mfd_5Fnpm10xx_5Fevent_5Fcallback"></a>

```c
struct mfd_npm10xx_event_callback
```

相关声明：[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)。

NPM10xx多功能设备（MFD）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 复位原因（RESET reasons）

<a id="r_gaa01e18082e07f933a6bf0c4a8f6f24c1"></a>

```c
#define NPM10XX_RSTREAS_HIBERNATE BIT(0)
```

相关声明：[NPM10XX_RSTREAS_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaa01e18082e07f933a6bf0c4a8f6f24c1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因连接 VBUS 而退出 VBAT 深度休眠模式（Hibernate Mode）。

<a id="r_ga1d6e5782bf0e1c2ea395a2b9dd884723"></a>

```c
#define NPM10XX_RSTREAS_BOOTMON BIT(1)
```

相关声明：[NPM10XX_RSTREAS_BOOTMON](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1d6e5782bf0e1c2ea395a2b9dd884723)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启动监视器复位（Boot Monitor Reset）。

<a id="r_gaa0266596048079a4b90dd3df6199666a"></a>

```c
#define NPM10XX_RSTREAS_WATCHDOG BIT(2)
```

相关声明：[NPM10XX_RSTREAS_WATCHDOG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaa0266596048079a4b90dd3df6199666a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗复位（Watchdog Reset）。

<a id="r_ga762cca53f636dd8a3e2fcd7017b3abdd"></a>

```c
#define NPM10XX_RSTREAS_LONGPRESS BIT(3)
```

相关声明：[NPM10XX_RSTREAS_LONGPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga762cca53f636dd8a3e2fcd7017b3abdd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

长按复位（Longpress Reset）。

<a id="r_ga167467b923a5f81bdaec1e4e1d91a368"></a>

```c
#define NPM10XX_RSTREAS_THERMAL BIT(4)
```

相关声明：[NPM10XX_RSTREAS_THERMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga167467b923a5f81bdaec1e4e1d91a368)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

热关断复位（Thermal Shutdown Reset）。

<a id="r_gad79d6bf2c570e8a51700e17cfeb5a817"></a>

```c
#define NPM10XX_RSTREAS_POF BIT(5)
```

相关声明：[NPM10XX_RSTREAS_POF](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad79d6bf2c570e8a51700e17cfeb5a817)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源故障复位（POF Reset）。

<a id="r_ga7cb7ea1ce7b2bc41f0388c2f5b740b5a"></a>

```c
#define NPM10XX_RSTREAS_SW BIT(6)
```

相关声明：[NPM10XX_RSTREAS_SW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga7cb7ea1ce7b2bc41f0388c2f5b740b5a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

软件复位（Software Reset），通过任务寄存器（Task Register）触发。

<a id="r_gaea70fe0bf1a583800673b9a5335dce85"></a>

```c
#define NPM10XX_RSTREAS_SHIPERR BIT(7)
```

相关声明：[NPM10XX_RSTREAS_SHIPERR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaea70fe0bf1a583800673b9a5335dce85)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

进入运输模式（Ship Mode）出错引起的复位。

<a id="r_ga0738fae4151077589ea32b200769ab24"></a>

```c
#define NPM10XX_RSTREAS_TIMER BIT(8)
```

相关声明：[NPM10XX_RSTREAS_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga0738fae4151077589ea32b200769ab24)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因定时器（Timer）而退出深度休眠模式（Hibernate Mode）。

<a id="r_ga5a06e1bd3cc551ee5001f7e27c3b5e14"></a>

```c
#define NPM10XX_RSTREAS_BUTTON BIT(9)
```

相关声明：[NPM10XX_RSTREAS_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5a06e1bd3cc551ee5001f7e27c3b5e14)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因 SHPHLD 按钮而退出深度休眠模式（Hibernate Mode）。

<a id="r_ga13b8e4b033016d7865f25ff58b579127"></a>

```c
#define NPM10XX_RSTREAS_HIBERNATEVBUS BIT(10)
```

相关声明：[NPM10XX_RSTREAS_HIBERNATEVBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga13b8e4b033016d7865f25ff58b579127)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因 VBUS 断开而退出 VBUS 深度休眠模式（Hibernate Mode）。

<a id="r_ga680b731e93c19e430b5c3b1011337d3f"></a>

```c
#define NPM10XX_RSTREAS_WATCHDOGSOFT BIT(11)
```

相关声明：[NPM10XX_RSTREAS_WATCHDOGSOFT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga680b731e93c19e430b5c3b1011337d3f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗软复位（Watchdog Soft Reset）。

<a id="define-members-1"></a>

### 模数转换事件（ADC events）

<a id="r_ga8d1937763166b6efa9ab159b3a571144"></a>

```c
#define NPM10XX_EVENT_ADC_VBAT BIT64(0)
```

相关声明：[NPM10XX_EVENT_ADC_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8d1937763166b6efa9ab159b3a571144)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VBAT 转换已就绪（Conversion Ready）。

<a id="r_gad542c7d4583b8c0ac2b7c102af6899df"></a>

```c
#define NPM10XX_EVENT_ADC_NTC BIT64(1)
```

相关声明：[NPM10XX_EVENT_ADC_NTC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad542c7d4583b8c0ac2b7c102af6899df)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 NTC 转换已就绪（Conversion Ready）。

<a id="r_gab3bb0ccba78d150cba683b8d75b0db1e"></a>

```c
#define NPM10XX_EVENT_ADC_DIETEMP BIT64(2)
```

相关声明：[NPM10XX_EVENT_ADC_DIETEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab3bb0ccba78d150cba683b8d75b0db1e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的芯片温度（Die Temperature）转换已就绪。

<a id="r_gad639d50b74e582bce18a5c122f12049e"></a>

```c
#define NPM10XX_EVENT_ADC_VSYS BIT64(3)
```

相关声明：[NPM10XX_EVENT_ADC_VSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad639d50b74e582bce18a5c122f12049e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VSYS 转换已就绪（Conversion Ready）。

<a id="r_gaf7c1e1854dde20198a8df113a17d60d8"></a>

```c
#define NPM10XX_EVENT_ADC_VBUS BIT64(4)
```

相关声明：[NPM10XX_EVENT_ADC_VBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf7c1e1854dde20198a8df113a17d60d8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VBUS 转换已就绪（Conversion Ready）。

<a id="r_ga749dfc8a4494e29423d74dd98e7e9c56"></a>

```c
#define NPM10XX_EVENT_ADC_VSET BIT64(5)
```

相关声明：[NPM10XX_EVENT_ADC_VSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga749dfc8a4494e29423d74dd98e7e9c56)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 VSET 转换已就绪（Conversion Ready）。

<a id="r_ga629d48940054d66218e62c3113654e1b"></a>

```c
#define NPM10XX_EVENT_ADC_OFFSET BIT64(6)
```

相关声明：[NPM10XX_EVENT_ADC_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga629d48940054d66218e62c3113654e1b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 的 OFFSET 转换已就绪（Conversion Ready）。

<a id="r_ga6332911d314425042f86638253a1b4e9"></a>

```c
#define NPM10XX_EVENT_IBATVBAT BIT64(7)
```

相关声明：[NPM10XX_EVENT_IBATVBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6332911d314425042f86638253a1b4e9)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

IBAT／VBAT 电池电流和／或电压转换已就绪（Conversion Ready）。

<a id="define-members-2"></a>

### 充电器事件（CHARGER events）

<a id="r_gacdd4bb994fdc27cca82d76a8f4be0144"></a>

```c
#define NPM10XX_EVENT_CHARGE BIT64(8)
```

相关声明：[NPM10XX_EVENT_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gacdd4bb994fdc27cca82d76a8f4be0144)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电器已启动（Charger Started）。

<a id="r_ga43ea2f80d5d5ad538e46e97bf6ad68e8"></a>

```c
#define NPM10XX_EVENT_DISCHARGE BIT64(9)
```

相关声明：[NPM10XX_EVENT_DISCHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga43ea2f80d5d5ad538e46e97bf6ad68e8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池放电已开始（Battery Discharge Started）。

<a id="r_ga8d024bf2914c1885c10b97d97c85121e"></a>

```c
#define NPM10XX_EVENT_DROPOUT BIT64(10)
```

相关声明：[NPM10XX_EVENT_DROPOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8d024bf2914c1885c10b97d97c85121e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

压差控制环路已激活（Dropout Loop Activated）。

<a id="r_ga50f4ff61c0f3e281764a2099d8eb107f"></a>

```c
#define NPM10XX_EVENT_SUPPLEMENT BIT64(11)
```

相关声明：[NPM10XX_EVENT_SUPPLEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga50f4ff61c0f3e281764a2099d8eb107f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

补充供电模式已激活（Supplement Mode Activated）。

<a id="r_ga83ee75ea61f37a26c91df2806cbedf77"></a>

```c
#define NPM10XX_EVENT_COMPLETE BIT64(12)
```

相关声明：[NPM10XX_EVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga83ee75ea61f37a26c91df2806cbedf77)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池充电已完成（Battery Charging Completed）。

<a id="r_gac70fb8807559882b67dd551a58d0e240"></a>

```c
#define NPM10XX_EVENT_BATILIM BIT64(13)
```

相关声明：[NPM10XX_EVENT_BATILIM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gac70fb8807559882b67dd551a58d0e240)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池放电限制已激活（Battery Discharge Limit Activated）。

<a id="r_ga8612c9106a981d48574456ec6d4aeb9f"></a>

```c
#define NPM10XX_EVENT_ITERM BIT64(14)
```

相关声明：[NPM10XX_EVENT_ITERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8612c9106a981d48574456ec6d4aeb9f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电电流（Charging Current）低于 `ITERM`。

<a id="r_ga1b280e6da1cde61fdf29037a8b2e473c"></a>

```c
#define NPM10XX_EVENT_VTERM BIT64(16)
```

相关声明：[NPM10XX_EVENT_VTERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1b280e6da1cde61fdf29037a8b2e473c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）已达到 `VTERM`。

<a id="r_gac8ab9f678ea4975623dc696611857998"></a>

```c
#define NPM10XX_EVENT_RECHARGE BIT64(17)
```

相关声明：[NPM10XX_EVENT_RECHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gac8ab9f678ea4975623dc696611857998)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）低于 `VRECHARGE`。

<a id="r_ga6435230e68729fa078f0f55ec64cd0ca"></a>

```c
#define NPM10XX_EVENT_VTHROTTLE BIT64(18)
```

相关声明：[NPM10XX_EVENT_VTHROTTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6435230e68729fa078f0f55ec64cd0ca)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VTHROTTLE`。

<a id="r_gafe6fd2bf306f411e8205be428fafd5cc"></a>

```c
#define NPM10XX_EVENT_VWEAK BIT64(19)
```

相关声明：[NPM10XX_EVENT_VWEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gafe6fd2bf306f411e8205be428fafd5cc)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VWEAK`。

<a id="r_gae932ded31cc4cf403b66f34853362cbd"></a>

```c
#define NPM10XX_EVENT_VTRICKLE BIT64(20)
```

相关声明：[NPM10XX_EVENT_VTRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae932ded31cc4cf403b66f34853362cbd)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）高于 `VTRICKLEFAST`。

<a id="r_ga623b4394d8f00798d934d83f63622656"></a>

```c
#define NPM10XX_EVENT_VBATLOW BIT64(21)
```

相关声明：[NPM10XX_EVENT_VBATLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga623b4394d8f00798d934d83f63622656)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池电压（Battery Voltage）低于 `VBATLOW`。

<a id="r_ga75a1e71dec354020c692a7311c44ea0f"></a>

```c
#define NPM10XX_EVENT_NTCCOLD BIT64(24)
```

相关声明：[NPM10XX_EVENT_NTCCOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga75a1e71dec354020c692a7311c44ea0f)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于寒冷区域（Cold Region）。

<a id="r_ga155922438a707ad10c3d5a3292e0c75c"></a>

```c
#define NPM10XX_EVENT_NTCCOOL BIT64(25)
```

相关声明：[NPM10XX_EVENT_NTCCOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga155922438a707ad10c3d5a3292e0c75c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于较冷区域（Cool Region）。

<a id="r_ga22d0d980fd12fa98a6350451ae7edf59"></a>

```c
#define NPM10XX_EVENT_NTCWARM BIT64(26)
```

相关声明：[NPM10XX_EVENT_NTCWARM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga22d0d980fd12fa98a6350451ae7edf59)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于温暖区域（Warm Region）。

<a id="r_ga2bdf786c80456f00a39c160d1a046986"></a>

```c
#define NPM10XX_EVENT_NTCHOT BIT64(27)
```

相关声明：[NPM10XX_EVENT_NTCHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga2bdf786c80456f00a39c160d1a046986)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

电池温度处于高温区域（Hot Region）。

<a id="r_ga3e354453e00614129bbcf58583391f7b"></a>

```c
#define NPM10XX_EVENT_DIETEMP BIT64(28)
```

相关声明：[NPM10XX_EVENT_DIETEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga3e354453e00614129bbcf58583391f7b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

芯片温度（Die Temperature）超过 `TCHGREDUCE`。

<a id="r_gadd6c59e1160fb519a38abb8a2cc924ea"></a>

```c
#define NPM10XX_EVENT_ERROR BIT64(29)
```

相关声明：[NPM10XX_EVENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gadd6c59e1160fb519a38abb8a2cc924ea)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

充电错误（Charging Error）。

<a id="r_gaef29381e85d461ccf05009bcb9b2e5ff"></a>

```c
#define NPM10XX_EVENT_VSYSWRNPE BIT64(30)
```

相关声明：[NPM10XX_EVENT_VSYSWRNPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaef29381e85d461ccf05009bcb9b2e5ff)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 `VSYSWRNR` 阈值（Threshold）。

<a id="r_gae953485b6e852cbaee0d2e62db1d02f1"></a>

```c
#define NPM10XX_EVENT_VSYSWRNNE BIT64(31)
```

相关声明：[NPM10XX_EVENT_VSYSWRNNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae953485b6e852cbaee0d2e62db1d02f1)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 `VSYSWRNF` 阈值（Threshold）。

<a id="define-members-3"></a>

### SYSREG／VBUS事件（SYSREG/VBUS events）

<a id="r_ga18b584396d3620d541e761a7f68ed94a"></a>

```c
#define NPM10XX_EVENT_VBUSOVPE BIT64(32)
```

相关声明：[NPM10XX_EVENT_VBUSOVPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga18b584396d3620d541e761a7f68ed94a)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS 过压（Overvoltage）。

<a id="r_ga073825db8abf74874653bf48d52573e5"></a>

```c
#define NPM10XX_EVENT_VBUSOVNE BIT64(33)
```

相关声明：[NPM10XX_EVENT_VBUSOVNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga073825db8abf74874653bf48d52573e5)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 过压（Overvoltage）已消除。

<a id="r_ga078b8604922045a722e4d777b4a2cfa9"></a>

```c
#define NPM10XX_EVENT_VBUSUNDERPE BIT64(34)
```

相关声明：[NPM10XX_EVENT_VBUSUNDERPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga078b8604922045a722e4d777b4a2cfa9)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS 欠压（Undervoltage）。

<a id="r_ga86dd9b11368443698e13bc6c17b4575c"></a>

```c
#define NPM10XX_EVENT_VBUSUNDERNE BIT64(35)
```

相关声明：[NPM10XX_EVENT_VBUSUNDERNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga86dd9b11368443698e13bc6c17b4575c)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 欠压（Undervoltage）已消除。

<a id="r_gaab1a75798b2252723392c6b8ed0682f8"></a>

```c
#define NPM10XX_EVENT_VBUSPRESENTPE BIT64(36)
```

相关声明：[NPM10XX_EVENT_VBUSPRESENTPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaab1a75798b2252723392c6b8ed0682f8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

检测到 VBUS。

<a id="r_ga1fdd5ae85149b0d31d51df4727968396"></a>

```c
#define NPM10XX_EVENT_VBUSPRESENTNE BIT64(37)
```

相关声明：[NPM10XX_EVENT_VBUSPRESENTNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1fdd5ae85149b0d31d51df4727968396)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 已移除。

<a id="r_ga443745fe8fe1c9145f2e4b80e8332068"></a>

```c
#define NPM10XX_EVENT_VBUSOKPE BIT64(38)
```

相关声明：[NPM10XX_EVENT_VBUSOKPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga443745fe8fe1c9145f2e4b80e8332068)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 在限制范围内（Within Limit）。

<a id="r_gaf46bb53cfebec5cfeea06a0eac9a7b8b"></a>

```c
#define NPM10XX_EVENT_VBUSOKNE BIT64(39)
```

相关声明：[NPM10XX_EVENT_VBUSOKNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf46bb53cfebec5cfeea06a0eac9a7b8b)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

VBUS 超出限制范围（Outside the Limit）。

<a id="define-members-4"></a>

### 通用输入输出事件（GPIO events）

<a id="r_gabb776a944d00755f4a7b3b0049833486"></a>

```c
#define NPM10XX_EVENT_GPIO0PE BIT64(40)
```

相关声明：[NPM10XX_EVENT_GPIO0PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gabb776a944d00755f4a7b3b0049833486)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO0 上出现上升沿（Rising Edge）。

<a id="r_gaef166e04ca328fc79ced45ef80307b26"></a>

```c
#define NPM10XX_EVENT_GPIO0NE BIT64(41)
```

相关声明：[NPM10XX_EVENT_GPIO0NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaef166e04ca328fc79ced45ef80307b26)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO0 上出现下降沿（Falling Edge）。

<a id="r_gab8a55e8cd43f312c6024f7b84c145fdf"></a>

```c
#define NPM10XX_EVENT_GPIO1PE BIT64(42)
```

相关声明：[NPM10XX_EVENT_GPIO1PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab8a55e8cd43f312c6024f7b84c145fdf)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO1 上出现上升沿（Rising Edge）。

<a id="r_gad606f6364d310d5d794583eea12cae48"></a>

```c
#define NPM10XX_EVENT_GPIO1NE BIT64(43)
```

相关声明：[NPM10XX_EVENT_GPIO1NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad606f6364d310d5d794583eea12cae48)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO1 上出现下降沿（Falling Edge）。

<a id="r_gae7170a3c6576d9c771f4366e24990c42"></a>

```c
#define NPM10XX_EVENT_GPIO2PE BIT64(44)
```

相关声明：[NPM10XX_EVENT_GPIO2PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae7170a3c6576d9c771f4366e24990c42)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO2 上出现上升沿（Rising Edge）。

<a id="r_ga0cf08cd51b179ad270b90f478f754f22"></a>

```c
#define NPM10XX_EVENT_GPIO2NE BIT64(45)
```

相关声明：[NPM10XX_EVENT_GPIO2NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga0cf08cd51b179ad270b90f478f754f22)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

GPIO2 上出现下降沿（Falling Edge）。

<a id="define-members-5"></a>

### 系统事件（SYSTEM events）

<a id="r_gaedf4086fe313a695e1195cad941f5fe8"></a>

```c
#define NPM10XX_EVENT_TIMERTIMEOUT BIT64(48)
```

相关声明：[NPM10XX_EVENT_TIMERTIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaedf4086fe313a695e1195cad941f5fe8)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

通用定时器到期（General Purpose Timer Expired）。

<a id="r_ga5204062fa8946f9f672766fa9f365763"></a>

```c
#define NPM10XX_EVENT_TIMERFREE BIT64(49)
```

相关声明：[NPM10XX_EVENT_TIMERFREE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5204062fa8946f9f672766fa9f365763)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

定时器空闲事件（Timer Free Event）。

<a id="r_gaf5b5dd70a03d270c6aed0dbf69637d11"></a>

```c
#define NPM10XX_EVENT_TIMERPREWARN BIT64(50)
```

相关声明：[NPM10XX_EVENT_TIMERPREWARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf5b5dd70a03d270c6aed0dbf69637d11)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

定时器到期前的预警事件（Pre-Warning Event）。

<a id="r_ga8ceb82aab97e7066f2158ff35db5bf4d"></a>

```c
#define NPM10XX_EVENT_LDOSWOC BIT64(51)
```

相关声明：[NPM10XX_EVENT_LDOSWOC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8ceb82aab97e7066f2158ff35db5bf4d)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

LOADSW1／LDO1 过流（Overcurrent）。

<a id="r_ga60df5df26a6fb86ba906d244be5aed5e"></a>

```c
#define NPM10XX_EVENT_LOADSWOC BIT64(52)
```

相关声明：[NPM10XX_EVENT_LOADSWOC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga60df5df26a6fb86ba906d244be5aed5e)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

LOADSW2 过流（Overcurrent）。

<a id="r_ga5f382672aab5750ade14b9ed069de1ba"></a>

```c
#define NPM10XX_EVENT_SHPHLDPE BIT64(53)
```

相关声明：[NPM10XX_EVENT_SHPHLDPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5f382672aab5750ade14b9ed069de1ba)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

SHPHLD 上出现上升沿（Rising Edge）。

<a id="r_ga7a27f6e42764fc6958d711878cc9f07a"></a>

```c
#define NPM10XX_EVENT_SHPHLDNE BIT64(54)
```

相关声明：[NPM10XX_EVENT_SHPHLDNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga7a27f6e42764fc6958d711878cc9f07a)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

SHPHLD 上出现下降沿（Falling Edge）。

<a id="r_gab9c1c24039d32874c6769f6b89f1bf7d"></a>

```c
#define NPM10XX_EVENT_ADCTEST BIT64(55)
```

相关声明：[NPM10XX_EVENT_ADCTEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab9c1c24039d32874c6769f6b89f1bf7d)、[BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)。

ADC 测试完成（Test Finished）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gab2a9bae08f020392e33bfb98efff2f32"></a>

```c
typedef uint64_t npm10xx_event_t
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)。

标识供事件回调（Event Callback）使用的一组事件。

<a id="r_ga4cdc0f26a0193e0c1e58404f632029c7"></a>

```c
typedef uint16_t npm10xx_rstreas_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[npm10xx_rstreas_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga4cdc0f26a0193e0c1e58404f632029c7)。

标识复位原因（Reset Reason）。

<a id="r_ga917abc6c5ed263f28a04bc96598d0009"></a>

```c
typedef void(* npm10xx_callback_handler_t) (const struct device *mfd_npm10xx_dev, struct mfd_npm10xx_event_callback *cb, npm10xx_event_t events)
```

相关声明：[npm10xx_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga917abc6c5ed263f28a04bc96598d0009)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)、[npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga164233569fe1f2e9ee00acc74e6f92c7"></a>

```c
enum mfd_npm10xx_hibernate_mode { NPM10XX_HIBERNATE_VBAT , NPM10XX_HIBERNATE_VBUS_WAIT , NPM10XX_HIBERNATE_VBUS_NOWAIT }
```

相关声明：[mfd_npm10xx_hibernate_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga164233569fe1f2e9ee00acc74e6f92c7)、[NPM10XX_HIBERNATE_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7a1cfa5ca4c49b40e9b78da256908a89d6)、[NPM10XX_HIBERNATE_VBUS_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7a9ce4e5b0bbe115a52dcb297f1cce6d64)、[NPM10XX_HIBERNATE_VBUS_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7ab1f535e92914be861eee60738b0280a4)。

nPM10xx 深度休眠模式（Hibernate Modes）。

<a id="r_gab6640de2b0c8007f3b8f13b31a66a00a"></a>

```c
enum mfd_npm10xx_standby_op { NPM10XX_STANDBY1_ENTER_WAIT , NPM10XX_STANDBY1_ENTER_NOWAIT , NPM10XX_STANDBY2_ENTER_WAIT , NPM10XX_STANDBY2_ENTER_NOWAIT , NPM10XX_STANDBY_EXIT }
```

相关声明：[mfd_npm10xx_standby_op](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab6640de2b0c8007f3b8f13b31a66a00a)、[NPM10XX_STANDBY1_ENTER_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aa5542f06dba5176ccfed1e024c2a75e50)、[NPM10XX_STANDBY1_ENTER_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aaa7523d301dc05610fdf8de9ca2996031)、[NPM10XX_STANDBY2_ENTER_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aaa9c904dbc9b8f339cd15fcf02991e7c4)、[NPM10XX_STANDBY2_ENTER_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aafae6fbde2b5e0a178a794ee43b7987d8)、[NPM10XX_STANDBY_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aac6b17d0c7aa2536c4c3af6900ee857bf)。

nPM10xx 待机操作（Standby Operations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_ga5ff11ba2820c426dfeeb959b511b66f2"></a>

```c
int mfd_npm10xx_reset (const struct device *dev)
```

相关声明：[mfd_npm10xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5ff11ba2820c426dfeeb959b511b66f2)、[device](../device_reference/P002_设备对象结构.md)。

复位 nPM10xx 电源管理集成电路（PMIC）设备。

<a id="r_ga2bd8018f8aab66569a5fa052893e0c25"></a>

```c
int mfd_npm10xx_get_reset_reason (const struct device *dev, npm10xx_rstreas_t *reason)
```

相关声明：[mfd_npm10xx_get_reset_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga2bd8018f8aab66569a5fa052893e0c25)、[device](../device_reference/P002_设备对象结构.md)、[npm10xx_rstreas_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga4cdc0f26a0193e0c1e58404f632029c7)。

获取并清除 nPM10xx 电源管理集成电路（PMIC）设备的复位原因（Reset Reason）。

<a id="r_gad9da1db5f865d5a39f1bc348c6f5fafd"></a>

```c
int mfd_npm10xx_hibernate (const struct device *dev, enum mfd_npm10xx_hibernate_mode mode, k_timeout_t time)
```

相关声明：[mfd_npm10xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad9da1db5f865d5a39f1bc348c6f5fafd)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_hibernate_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga164233569fe1f2e9ee00acc74e6f92c7)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)。

触发 nPM10xx 电源管理集成电路（PMIC）设备的深度休眠模式（Hibernate Mode）。

<a id="r_gad6169c136db8c4d56552793d5da2e666"></a>

```c
int mfd_npm10xx_standby (const struct device *dev, enum mfd_npm10xx_standby_op operation)
```

相关声明：[mfd_npm10xx_standby](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad6169c136db8c4d56552793d5da2e666)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_standby_op](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab6640de2b0c8007f3b8f13b31a66a00a)。

使 nPM10xx 电源管理集成电路（PMIC）设备进入或退出 VBUS 待机模式（Standby Mode）。

<a id="r_gae67bf6f3efdcd948ebc5034e56540d71"></a>

```c
int mfd_npm10xx_manage_callback (const struct device *dev, struct mfd_npm10xx_event_callback *callback, bool add)
```

相关声明：[mfd_npm10xx_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae67bf6f3efdcd948ebc5034e56540d71)、[device](../device_reference/P002_设备对象结构.md)、[mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

管理 nPM10xx 事件回调（Event Callbacks）。

<a id="r_ga5e155e4ba41999daccf9c2046ae60ad3"></a>

```c
int mfd_npm10xx_timer_set (const struct device *dev, k_timeout_t timeout)
```

相关声明：[mfd_npm10xx_timer_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5e155e4ba41999daccf9c2046ae60ad3)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置 nPM10xx 设备定时器的超时值（Timeout Value）。

<a id="r_ga6c7cf9f9606495ede2575174e60211fb"></a>

```c
int mfd_npm10xx_timer_start (const struct device *dev)
```

相关声明：[mfd_npm10xx_timer_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6c7cf9f9606495ede2575174e60211fb)、[device](../device_reference/P002_设备对象结构.md)。

启动 nPM10xx 设备的定时器（Timer）。

<a id="r_ga144c19663856ce0a8fc32db02c867360"></a>

```c
int mfd_npm10xx_timer_stop (const struct device *dev)
```

相关声明：[mfd_npm10xx_timer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga144c19663856ce0a8fc32db02c867360)、[device](../device_reference/P002_设备对象结构.md)。

停止 nPM10xx 设备的定时器（Timer）。

<a id="r_ga27625e2cceaea478514452bc0c9a2a1b"></a>

```c
int mfd_npm10xx_timer_status_get (const struct device *dev, bool *busy)
```

相关声明：[mfd_npm10xx_timer_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga27625e2cceaea478514452bc0c9a2a1b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取 nPM10xx 设备的定时器状态（Timer Status）。

<a id="r_gae775dcf89711147276ce11578ea7b6d2"></a>

```c
int mfd_npm10xx_scratch_read (const struct device *dev, uint8_t *val)
```

相关声明：[mfd_npm10xx_scratch_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae775dcf89711147276ce11578ea7b6d2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 `SCRATCH` 寄存器（Register）。

<a id="r_gaeb4cf7992c48aa4ad5747e58ec3a0020"></a>

```c
int mfd_npm10xx_scratch_write (const struct device *dev, uint8_t val)
```

相关声明：[mfd_npm10xx_scratch_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaeb4cf7992c48aa4ad5747e58ec3a0020)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 `SCRATCH` 寄存器（Register）。


## 1.6\_原页交叉引用（Cross References）

- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P161_npm10xx.h_源码浏览.md)
- [mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)
- [NPM10XX_RSTREAS_HIBERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaa01e18082e07f933a6bf0c4a8f6f24c1)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [NPM10XX_RSTREAS_BOOTMON](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1d6e5782bf0e1c2ea395a2b9dd884723)
- [NPM10XX_RSTREAS_WATCHDOG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaa0266596048079a4b90dd3df6199666a)
- [NPM10XX_RSTREAS_LONGPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga762cca53f636dd8a3e2fcd7017b3abdd)
- [NPM10XX_RSTREAS_THERMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga167467b923a5f81bdaec1e4e1d91a368)
- [NPM10XX_RSTREAS_POF](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad79d6bf2c570e8a51700e17cfeb5a817)
- [NPM10XX_RSTREAS_SW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga7cb7ea1ce7b2bc41f0388c2f5b740b5a)
- [NPM10XX_RSTREAS_SHIPERR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaea70fe0bf1a583800673b9a5335dce85)
- [NPM10XX_RSTREAS_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga0738fae4151077589ea32b200769ab24)
- [NPM10XX_RSTREAS_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5a06e1bd3cc551ee5001f7e27c3b5e14)
- [NPM10XX_RSTREAS_HIBERNATEVBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga13b8e4b033016d7865f25ff58b579127)
- [NPM10XX_RSTREAS_WATCHDOGSOFT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga680b731e93c19e430b5c3b1011337d3f)
- [NPM10XX_EVENT_ADC_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8d1937763166b6efa9ab159b3a571144)
- [BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)
- [NPM10XX_EVENT_ADC_NTC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad542c7d4583b8c0ac2b7c102af6899df)
- [NPM10XX_EVENT_ADC_DIETEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab3bb0ccba78d150cba683b8d75b0db1e)
- [NPM10XX_EVENT_ADC_VSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad639d50b74e582bce18a5c122f12049e)
- [NPM10XX_EVENT_ADC_VBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf7c1e1854dde20198a8df113a17d60d8)
- [NPM10XX_EVENT_ADC_VSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga749dfc8a4494e29423d74dd98e7e9c56)
- [NPM10XX_EVENT_ADC_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga629d48940054d66218e62c3113654e1b)
- [NPM10XX_EVENT_IBATVBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6332911d314425042f86638253a1b4e9)
- [NPM10XX_EVENT_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gacdd4bb994fdc27cca82d76a8f4be0144)
- [NPM10XX_EVENT_DISCHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga43ea2f80d5d5ad538e46e97bf6ad68e8)
- [NPM10XX_EVENT_DROPOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8d024bf2914c1885c10b97d97c85121e)
- [NPM10XX_EVENT_SUPPLEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga50f4ff61c0f3e281764a2099d8eb107f)
- [NPM10XX_EVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga83ee75ea61f37a26c91df2806cbedf77)
- [NPM10XX_EVENT_BATILIM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gac70fb8807559882b67dd551a58d0e240)
- [NPM10XX_EVENT_ITERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8612c9106a981d48574456ec6d4aeb9f)
- [NPM10XX_EVENT_VTERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1b280e6da1cde61fdf29037a8b2e473c)
- [NPM10XX_EVENT_RECHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gac8ab9f678ea4975623dc696611857998)
- [NPM10XX_EVENT_VTHROTTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6435230e68729fa078f0f55ec64cd0ca)
- [NPM10XX_EVENT_VWEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gafe6fd2bf306f411e8205be428fafd5cc)
- [NPM10XX_EVENT_VTRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae932ded31cc4cf403b66f34853362cbd)
- [NPM10XX_EVENT_VBATLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga623b4394d8f00798d934d83f63622656)
- [NPM10XX_EVENT_NTCCOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga75a1e71dec354020c692a7311c44ea0f)
- [NPM10XX_EVENT_NTCCOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga155922438a707ad10c3d5a3292e0c75c)
- [NPM10XX_EVENT_NTCWARM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga22d0d980fd12fa98a6350451ae7edf59)
- [NPM10XX_EVENT_NTCHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga2bdf786c80456f00a39c160d1a046986)
- [NPM10XX_EVENT_DIETEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga3e354453e00614129bbcf58583391f7b)
- [NPM10XX_EVENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gadd6c59e1160fb519a38abb8a2cc924ea)
- [NPM10XX_EVENT_VSYSWRNPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaef29381e85d461ccf05009bcb9b2e5ff)
- [NPM10XX_EVENT_VSYSWRNNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae953485b6e852cbaee0d2e62db1d02f1)
- [NPM10XX_EVENT_VBUSOVPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga18b584396d3620d541e761a7f68ed94a)
- [NPM10XX_EVENT_VBUSOVNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga073825db8abf74874653bf48d52573e5)
- [NPM10XX_EVENT_VBUSUNDERPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga078b8604922045a722e4d777b4a2cfa9)
- [NPM10XX_EVENT_VBUSUNDERNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga86dd9b11368443698e13bc6c17b4575c)
- [NPM10XX_EVENT_VBUSPRESENTPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaab1a75798b2252723392c6b8ed0682f8)
- [NPM10XX_EVENT_VBUSPRESENTNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga1fdd5ae85149b0d31d51df4727968396)
- [NPM10XX_EVENT_VBUSOKPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga443745fe8fe1c9145f2e4b80e8332068)
- [NPM10XX_EVENT_VBUSOKNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf46bb53cfebec5cfeea06a0eac9a7b8b)
- [NPM10XX_EVENT_GPIO0PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gabb776a944d00755f4a7b3b0049833486)
- [NPM10XX_EVENT_GPIO0NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaef166e04ca328fc79ced45ef80307b26)
- [NPM10XX_EVENT_GPIO1PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab8a55e8cd43f312c6024f7b84c145fdf)
- [NPM10XX_EVENT_GPIO1NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad606f6364d310d5d794583eea12cae48)
- [NPM10XX_EVENT_GPIO2PE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae7170a3c6576d9c771f4366e24990c42)
- [NPM10XX_EVENT_GPIO2NE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga0cf08cd51b179ad270b90f478f754f22)
- [NPM10XX_EVENT_TIMERTIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaedf4086fe313a695e1195cad941f5fe8)
- [NPM10XX_EVENT_TIMERFREE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5204062fa8946f9f672766fa9f365763)
- [NPM10XX_EVENT_TIMERPREWARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaf5b5dd70a03d270c6aed0dbf69637d11)
- [NPM10XX_EVENT_LDOSWOC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga8ceb82aab97e7066f2158ff35db5bf4d)
- [NPM10XX_EVENT_LOADSWOC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga60df5df26a6fb86ba906d244be5aed5e)
- [NPM10XX_EVENT_SHPHLDPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5f382672aab5750ade14b9ed069de1ba)
- [NPM10XX_EVENT_SHPHLDNE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga7a27f6e42764fc6958d711878cc9f07a)
- [NPM10XX_EVENT_ADCTEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab9c1c24039d32874c6769f6b89f1bf7d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [npm10xx_rstreas_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga4cdc0f26a0193e0c1e58404f632029c7)
- [npm10xx_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga917abc6c5ed263f28a04bc96598d0009)
- [device](../device_reference/P002_设备对象结构.md)
- [mfd_npm10xx_hibernate_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga164233569fe1f2e9ee00acc74e6f92c7)
- [NPM10XX_HIBERNATE_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7a1cfa5ca4c49b40e9b78da256908a89d6)
- [NPM10XX_HIBERNATE_VBUS_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7a9ce4e5b0bbe115a52dcb297f1cce6d64)
- [NPM10XX_HIBERNATE_VBUS_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gga164233569fe1f2e9ee00acc74e6f92c7ab1f535e92914be861eee60738b0280a4)
- [mfd_npm10xx_standby_op](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab6640de2b0c8007f3b8f13b31a66a00a)
- [NPM10XX_STANDBY1_ENTER_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aa5542f06dba5176ccfed1e024c2a75e50)
- [NPM10XX_STANDBY1_ENTER_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aaa7523d301dc05610fdf8de9ca2996031)
- [NPM10XX_STANDBY2_ENTER_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aaa9c904dbc9b8f339cd15fcf02991e7c4)
- [NPM10XX_STANDBY2_ENTER_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aafae6fbde2b5e0a178a794ee43b7987d8)
- [NPM10XX_STANDBY_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ggab6640de2b0c8007f3b8f13b31a66a00aac6b17d0c7aa2536c4c3af6900ee857bf)
- [mfd_npm10xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5ff11ba2820c426dfeeb959b511b66f2)
- [mfd_npm10xx_get_reset_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga2bd8018f8aab66569a5fa052893e0c25)
- [mfd_npm10xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad9da1db5f865d5a39f1bc348c6f5fafd)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)
- [mfd_npm10xx_standby](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad6169c136db8c4d56552793d5da2e666)
- [mfd_npm10xx_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae67bf6f3efdcd948ebc5034e56540d71)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mfd_npm10xx_timer_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5e155e4ba41999daccf9c2046ae60ad3)
- [mfd_npm10xx_timer_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6c7cf9f9606495ede2575174e60211fb)
- [mfd_npm10xx_timer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga144c19663856ce0a8fc32db02c867360)
- [mfd_npm10xx_timer_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga27625e2cceaea478514452bc0c9a2a1b)
- [mfd_npm10xx_scratch_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae775dcf89711147276ce11578ea7b6d2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_npm10xx_scratch_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaeb4cf7992c48aa4ad5747e58ec3a0020)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__mfd__max2221x.h_文件参考.md)
