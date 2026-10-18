---
id: learning.zephyr-docs.api-source-reference.page-161
title: npm10xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_npm10xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h.html)。

## 161.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00026"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="foldopen00190"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga144c19663856ce0a8fc32db02c867360"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga164233569fe1f2e9ee00acc74e6f92c7"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga27625e2cceaea478514452bc0c9a2a1b"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga2bd8018f8aab66569a5fa052893e0c25"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga4cdc0f26a0193e0c1e58404f632029c7"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga5e155e4ba41999daccf9c2046ae60ad3"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga5ff11ba2820c426dfeeb959b511b66f2"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga6c7cf9f9606495ede2575174e60211fb"></a>
<a id="agroup__mfd__interface__npm10xx_html_ga917abc6c5ed263f28a04bc96598d0009"></a>
<a id="agroup__mfd__interface__npm10xx_html_gab2a9bae08f020392e33bfb98efff2f32"></a>
<a id="agroup__mfd__interface__npm10xx_html_gab6640de2b0c8007f3b8f13b31a66a00a"></a>
<a id="agroup__mfd__interface__npm10xx_html_gad6169c136db8c4d56552793d5da2e666"></a>
<a id="agroup__mfd__interface__npm10xx_html_gad9da1db5f865d5a39f1bc348c6f5fafd"></a>
<a id="agroup__mfd__interface__npm10xx_html_gae67bf6f3efdcd948ebc5034e56540d71"></a>
<a id="agroup__mfd__interface__npm10xx_html_gae775dcf89711147276ce11578ea7b6d2"></a>
<a id="agroup__mfd__interface__npm10xx_html_gaeb4cf7992c48aa4ad5747e58ec3a0020"></a>
<a id="agroup__mfd__interface__npm10xx_html_gga164233569fe1f2e9ee00acc74e6f92c7a1cfa5ca4c49b40e9b78da256908a89d6"></a>
<a id="agroup__mfd__interface__npm10xx_html_gga164233569fe1f2e9ee00acc74e6f92c7a9ce4e5b0bbe115a52dcb297f1cce6d64"></a>
<a id="agroup__mfd__interface__npm10xx_html_gga164233569fe1f2e9ee00acc74e6f92c7ab1f535e92914be861eee60738b0280a4"></a>
<a id="agroup__mfd__interface__npm10xx_html_ggab6640de2b0c8007f3b8f13b31a66a00aa5542f06dba5176ccfed1e024c2a75e50"></a>
<a id="agroup__mfd__interface__npm10xx_html_ggab6640de2b0c8007f3b8f13b31a66a00aaa7523d301dc05610fdf8de9ca2996031"></a>
<a id="agroup__mfd__interface__npm10xx_html_ggab6640de2b0c8007f3b8f13b31a66a00aaa9c904dbc9b8f339cd15fcf02991e7c4"></a>
<a id="agroup__mfd__interface__npm10xx_html_ggab6640de2b0c8007f3b8f13b31a66a00aac6b17d0c7aa2536c4c3af6900ee857bf"></a>
<a id="agroup__mfd__interface__npm10xx_html_ggab6640de2b0c8007f3b8f13b31a66a00aafae6fbde2b5e0a178a794ee43b7987d8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmfd__npm10xx__event__callback_html"></a>
<a id="astructmfd__npm10xx__event__callback_html_a778f6145e68bf2c371b1700c4586630b"></a>
<a id="astructmfd__npm10xx__event__callback_html_a7a94c66197c7339cbeff18e99106ff9d"></a>
<a id="astructmfd__npm10xx__event__callback_html_a8056fcfbc6c04118502a67b90c301124"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MFD_NPM10XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MFD_NPM10XX_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/sys/slist.h>
#include <zephyr/sys/clock.h>
#include <zephyr/device.h>


#define NPM10XX_RSTREAS_HIBERNATE     BIT(0)
#define NPM10XX_RSTREAS_BOOTMON       BIT(1)
#define NPM10XX_RSTREAS_WATCHDOG      BIT(2)
#define NPM10XX_RSTREAS_LONGPRESS     BIT(3)
#define NPM10XX_RSTREAS_THERMAL       BIT(4)
#define NPM10XX_RSTREAS_POF           BIT(5)
#define NPM10XX_RSTREAS_SW            BIT(6)
#define NPM10XX_RSTREAS_SHIPERR       BIT(7)
#define NPM10XX_RSTREAS_TIMER         BIT(8)
#define NPM10XX_RSTREAS_BUTTON        BIT(9)
#define NPM10XX_RSTREAS_HIBERNATEVBUS BIT(10)
#define NPM10XX_RSTREAS_WATCHDOGSOFT  BIT(11)

#define NPM10XX_EVENT_ADC_VBAT    BIT64(0)
#define NPM10XX_EVENT_ADC_NTC     BIT64(1)
#define NPM10XX_EVENT_ADC_DIETEMP BIT64(2)
#define NPM10XX_EVENT_ADC_VSYS    BIT64(3)
#define NPM10XX_EVENT_ADC_VBUS    BIT64(4)
#define NPM10XX_EVENT_ADC_VSET    BIT64(5)
#define NPM10XX_EVENT_ADC_OFFSET  BIT64(6)
#define NPM10XX_EVENT_IBATVBAT    BIT64(7)

#define NPM10XX_EVENT_CHARGE     BIT64(8)
#define NPM10XX_EVENT_DISCHARGE  BIT64(9)
#define NPM10XX_EVENT_DROPOUT    BIT64(10)
#define NPM10XX_EVENT_SUPPLEMENT BIT64(11)
#define NPM10XX_EVENT_COMPLETE   BIT64(12)
#define NPM10XX_EVENT_BATILIM    BIT64(13)
#define NPM10XX_EVENT_ITERM      BIT64(14)
#define NPM10XX_EVENT_VTERM      BIT64(16)
#define NPM10XX_EVENT_RECHARGE   BIT64(17)
#define NPM10XX_EVENT_VTHROTTLE  BIT64(18)
#define NPM10XX_EVENT_VWEAK      BIT64(19)
#define NPM10XX_EVENT_VTRICKLE   BIT64(20)
#define NPM10XX_EVENT_VBATLOW    BIT64(21)
#define NPM10XX_EVENT_NTCCOLD    BIT64(24)
#define NPM10XX_EVENT_NTCCOOL    BIT64(25)
#define NPM10XX_EVENT_NTCWARM    BIT64(26)
#define NPM10XX_EVENT_NTCHOT     BIT64(27)
#define NPM10XX_EVENT_DIETEMP    BIT64(28)
#define NPM10XX_EVENT_ERROR      BIT64(29)
#define NPM10XX_EVENT_VSYSWRNPE  BIT64(30)
#define NPM10XX_EVENT_VSYSWRNNE  BIT64(31)

#define NPM10XX_EVENT_VBUSOVPE      BIT64(32)
#define NPM10XX_EVENT_VBUSOVNE      BIT64(33)
#define NPM10XX_EVENT_VBUSUNDERPE   BIT64(34)
#define NPM10XX_EVENT_VBUSUNDERNE   BIT64(35)
#define NPM10XX_EVENT_VBUSPRESENTPE BIT64(36)
#define NPM10XX_EVENT_VBUSPRESENTNE BIT64(37)
#define NPM10XX_EVENT_VBUSOKPE      BIT64(38)
#define NPM10XX_EVENT_VBUSOKNE      BIT64(39)

#define NPM10XX_EVENT_GPIO0PE BIT64(40)
#define NPM10XX_EVENT_GPIO0NE BIT64(41)
#define NPM10XX_EVENT_GPIO1PE BIT64(42)
#define NPM10XX_EVENT_GPIO1NE BIT64(43)
#define NPM10XX_EVENT_GPIO2PE BIT64(44)
#define NPM10XX_EVENT_GPIO2NE BIT64(45)

#define NPM10XX_EVENT_TIMERTIMEOUT BIT64(48)
#define NPM10XX_EVENT_TIMERFREE    BIT64(49)
#define NPM10XX_EVENT_TIMERPREWARN BIT64(50)
#define NPM10XX_EVENT_LDOSWOC      BIT64(51)
#define NPM10XX_EVENT_LOADSWOC     BIT64(52)
#define NPM10XX_EVENT_SHPHLDPE     BIT64(53)
#define NPM10XX_EVENT_SHPHLDNE     BIT64(54)
#define NPM10XX_EVENT_ADCTEST      BIT64(55)

enum mfd_npm10xx_hibernate_mode {
        NPM10XX_HIBERNATE_VBAT,
        NPM10XX_HIBERNATE_VBUS_WAIT,
        NPM10XX_HIBERNATE_VBUS_NOWAIT,
};

enum mfd_npm10xx_standby_op {
        NPM10XX_STANDBY1_ENTER_WAIT,
        NPM10XX_STANDBY1_ENTER_NOWAIT,
        NPM10XX_STANDBY2_ENTER_WAIT,
        NPM10XX_STANDBY2_ENTER_NOWAIT,
        NPM10XX_STANDBY_EXIT,
};

typedef uint64_t npm10xx_event_t;

typedef uint16_t npm10xx_rstreas_t;

struct mfd_npm10xx_event_callback;

typedef void (*npm10xx_callback_handler_t)(const struct device *mfd_npm10xx_dev,
                                           struct mfd_npm10xx_event_callback *cb,
                                           npm10xx_event_t events);

struct mfd_npm10xx_event_callback {
        sys_snode_t node;
        npm10xx_event_t event_mask;
        npm10xx_callback_handler_t handler;
};

int mfd_npm10xx_reset(const struct device *dev);

int mfd_npm10xx_get_reset_reason(const struct device *dev, npm10xx_rstreas_t *reason);

int mfd_npm10xx_hibernate(const struct device *dev, enum mfd_npm10xx_hibernate_mode mode,
                          k_timeout_t time);

int mfd_npm10xx_standby(const struct device *dev, enum mfd_npm10xx_standby_op operation);

int mfd_npm10xx_manage_callback(const struct device *dev,
                                struct mfd_npm10xx_event_callback *callback, bool add);

int mfd_npm10xx_timer_set(const struct device *dev, k_timeout_t timeout);

int mfd_npm10xx_timer_start(const struct device *dev);

int mfd_npm10xx_timer_stop(const struct device *dev);

int mfd_npm10xx_timer_status_get(const struct device *dev, bool *busy);

int mfd_npm10xx_scratch_read(const struct device *dev, uint8_t *val);

int mfd_npm10xx_scratch_write(const struct device *dev, uint8_t val);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MFD_NPM10XX_H_ */
```

## 161.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 391 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MFD_NPM10XX_H_`。

## 161.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
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
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [npm10xx_rstreas_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga4cdc0f26a0193e0c1e58404f632029c7)
- [mfd_npm10xx_event_callback](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md)
- [npm10xx_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga917abc6c5ed263f28a04bc96598d0009)
- [device](../device_reference/P002_设备对象结构.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a7a94c66197c7339cbeff18e99106ff9d)
- [event_mask](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a778f6145e68bf2c371b1700c4586630b)
- [handler](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a8056fcfbc6c04118502a67b90c301124)
- [mfd_npm10xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5ff11ba2820c426dfeeb959b511b66f2)
- [mfd_npm10xx_get_reset_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga2bd8018f8aab66569a5fa052893e0c25)
- [mfd_npm10xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad9da1db5f865d5a39f1bc348c6f5fafd)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [mfd_npm10xx_standby](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gad6169c136db8c4d56552793d5da2e666)
- [mfd_npm10xx_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae67bf6f3efdcd948ebc5034e56540d71)
- [mfd_npm10xx_timer_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga5e155e4ba41999daccf9c2046ae60ad3)
- [mfd_npm10xx_timer_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga6c7cf9f9606495ede2575174e60211fb)
- [mfd_npm10xx_timer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga144c19663856ce0a8fc32db02c867360)
- [mfd_npm10xx_timer_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga27625e2cceaea478514452bc0c9a2a1b)
- [mfd_npm10xx_scratch_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gae775dcf89711147276ce11578ea7b6d2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_npm10xx_scratch_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gaeb4cf7992c48aa4ad5747e58ec3a0020)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [mfd_npm10xx_event_callback::event_mask](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a778f6145e68bf2c371b1700c4586630b)
- [mfd_npm10xx_event_callback::node](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a7a94c66197c7339cbeff18e99106ff9d)
- [mfd_npm10xx_event_callback::handler](../device_power_control_model_reference/P033_mfd_npm10xx_event_callback_结构体.md#a8056fcfbc6c04118502a67b90c301124)

---

[上一章](P160_axp192.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P162_npm13xx.h_源码浏览.md)
