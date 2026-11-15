---
id: learning.zephyr-docs.api-source-reference.page-84
title: can_fake.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_can\_fake.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h.html)。

## 84.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="adrivers_2can_8h_html"></a>
<a id="agroup__can__controller_html_ga0b2a1456e66f4522a30cf1400fdfced7"></a>
<a id="agroup__can__controller_html_gaab9525fafab78c0da0a78a2dae39bd6f"></a>
<a id="agroup__can__controller_html_gab3675297d3e528bf19e2072f6a84bfca"></a>
<a id="agroup__can__controller_html_gac7ec472c26c564dd7067c49f67c8d2f7"></a>
<a id="agroup__can__fake_html_ga0378d66c4a1d72d5431751e094c6f21a"></a>
<a id="agroup__can__fake_html_ga12660dfbe19e04500673df058093da39"></a>
<a id="agroup__can__fake_html_ga14053f40abcd885d5039342a48691afc"></a>
<a id="agroup__can__fake_html_ga18314694d1939ec4983ef33681a8dcb3"></a>
<a id="agroup__can__fake_html_ga28f41cee87de64240f5a4c173bcc13ee"></a>
<a id="agroup__can__fake_html_ga336125a9f719700f59c5b36c8f6c9701"></a>
<a id="agroup__can__fake_html_ga37fb033aa3e1df477a2e879a5a823034"></a>
<a id="agroup__can__fake_html_ga4d396abead1d8ed677f00b64198f2597"></a>
<a id="agroup__can__fake_html_ga5ab6c1a56f20e14e7a3ee7f41f77e722"></a>
<a id="agroup__can__fake_html_ga657de26af4b7860d1b485640ce979535"></a>
<a id="agroup__can__fake_html_ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0"></a>
<a id="agroup__can__fake_html_gad2ef4f3a82cf93968123ac7f24ee5162"></a>
<a id="agroup__can__fake_html_gae27f8832b6bca338bc40d4b75ba07a2d"></a>
<a id="agroup__can__fake_html_gae42496e147592f98352c5fa6f6a1a665"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructcan__bus__err__cnt_html"></a>
<a id="astructcan__filter_html"></a>
<a id="astructcan__frame_html"></a>
<a id="astructcan__timing_html"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2022 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CAN_CAN_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_CAN_CAN_FAKE_H_

#include <zephyr/drivers/can.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int, fake_can_start, const struct device *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_stop, const struct device *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_set_timing, const struct device *, const struct can_timing *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_set_timing_data, const struct device *,
                        const struct can_timing *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_get_capabilities, const struct device *, can_mode_t *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_set_mode, const struct device *, can_mode_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_send, const struct device *, const struct can_frame *,
                        k_timeout_t, can_tx_callback_t, void *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_add_rx_filter, const struct device *, can_rx_callback_t,
                        void *, const struct can_filter *);

DECLARE_FAKE_VOID_FUNC(fake_can_remove_rx_filter, const struct device *, int);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_recover, const struct device *, k_timeout_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_get_state, const struct device *, enum can_state *,
                        struct can_bus_err_cnt *);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_state_change_callbacks_enabled, const struct device *, bool);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_get_max_filters, const struct device *, bool);

DECLARE_FAKE_VALUE_FUNC(int, fake_can_get_core_clock, const struct device *, uint32_t *);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CAN_CAN_FAKE_H_ */
```

## 84.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Vestas Wind Systems A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 93 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CAN_CAN_FAKE_H_`。

## 84.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h.html)
- [zephyr/drivers/can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [fake_can_start](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga336125a9f719700f59c5b36c8f6c9701)
- [device](../device_reference/P002_设备对象结构.md)
- [fake_can_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga14053f40abcd885d5039342a48691afc)
- [fake_can_set_timing](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga37fb033aa3e1df477a2e879a5a823034)
- [can_timing](../hardware/P366_CAN时序结构.md)
- [fake_can_set_timing_data](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga12660dfbe19e04500673df058093da39)
- [fake_can_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga5ab6c1a56f20e14e7a3ee7f41f77e722)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [fake_can_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga28f41cee87de64240f5a4c173bcc13ee)
- [fake_can_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae27f8832b6bca338bc40d4b75ba07a2d)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)
- [fake_can_add_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae42496e147592f98352c5fa6f6a1a665)
- [can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [fake_can_remove_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gad2ef4f3a82cf93968123ac7f24ee5162)
- [fake_can_recover](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0)
- [fake_can_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga18314694d1939ec4983ef33681a8dcb3)
- [can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)
- [can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)
- [fake_can_state_change_callbacks_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga0378d66c4a1d72d5431751e094c6f21a)
- [fake_can_get_max_filters](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga4d396abead1d8ed677f00b64198f2597)
- [fake_can_get_core_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga657de26af4b7860d1b485640ce979535)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)

---

[上一章](P083_callbacks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P085_ccid.h_源码浏览.md)
