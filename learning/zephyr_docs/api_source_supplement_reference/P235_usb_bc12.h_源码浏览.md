---
id: learning.zephyr-docs.api-source-supplement-reference.page-235
title: usb_bc12.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第235章\_usb\_bc12.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html)。

## 235.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00101"></a>
<a id="l00106"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__b12__interface_html_ga035f4e4ba27f76094145571ebea97d73"></a>
<a id="agroup__b12__interface_html_ga0db43c4cc595cb76738cf24d97fa5228"></a>
<a id="agroup__b12__interface_html_ga2a879017d34392308d4c078178db8407"></a>
<a id="agroup__b12__interface_html_ga9ae800d490c2cbd3234a81c503649bdb"></a>
<a id="agroup__b12__interface_html_gaeb039486c7826fe493e7f402212f2661"></a>
<a id="agroup__b12__interface_html_gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef"></a>
<a id="agroup__b12__interface_html_gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22"></a>
<a id="agroup__b12__interface_html_gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50"></a>
<a id="agroup__b12__interface_html_gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astructbc12__partner__state_html"></a>
<a id="astructbc12__partner__state_html_a1cdea094ae13acbb46fcae6f60ec3a7b"></a>
<a id="astructbc12__partner__state_html_a3a04b815fcc4c283d342b071dda1a0da"></a>
<a id="astructbc12__partner__state_html_a4c1a653bd2393d79680f75afef334ac9"></a>
<a id="astructbc12__partner__state_html_a4da4a226fd933eea17da379687d49acf"></a>
<a id="astructbc12__partner__state_html_adeeb33acadfa0e1a8a57b862dfad97a1"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_USB_BC12_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_USB_BC12_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


/* FIXME - make these Kconfig options */


#define BC12_CHARGER_VOLTAGE_UV  5000 * 1000
#define BC12_CHARGER_MIN_CURR_UA 2500
#define BC12_CHARGER_MAX_CURR_UA 1500 * 1000


#define BC12_CURR_UA(val) CLAMP(val, BC12_CHARGER_MIN_CURR_UA, BC12_CHARGER_MAX_CURR_UA)

enum bc12_role {
        BC12_DISCONNECTED,
        BC12_PORTABLE_DEVICE,
        BC12_CHARGING_PORT,
};

enum bc12_type {
        BC12_TYPE_NONE,
        BC12_TYPE_SDP,
        BC12_TYPE_DCP,
        BC12_TYPE_CDP,
        BC12_TYPE_PROPRIETARY,
        BC12_TYPE_UNKNOWN,
        BC12_TYPE_COUNT,
};

struct bc12_partner_state {
        enum bc12_role bc12_role;
        union {
                struct {
                        enum bc12_type type;
                        int current_ua;
                        int voltage_uv;
                };
                struct {
                        bool pd_partner_connected;
                };
        };
};

typedef void (*bc12_callback_t)(const struct device *dev, struct bc12_partner_state *state,
                                void *user_data);

__subsystem struct bc12_driver_api {
        int (*set_role)(const struct device *dev, enum bc12_role role);
        int (*set_result_cb)(const struct device *dev, bc12_callback_t cb, void *user_data);
};

__syscall int bc12_set_role(const struct device *dev, enum bc12_role role);

static inline int z_impl_bc12_set_role(const struct device *dev, enum bc12_role role)
{
        return DEVICE_API_GET(bc12, dev)->set_role(dev, role);
}

__syscall int bc12_set_result_cb(const struct device *dev, bc12_callback_t cb, void *user_data);

static inline int z_impl_bc12_set_result_cb(const struct device *dev, bc12_callback_t cb,
                                            void *user_data)
{
        return DEVICE_API_GET(bc12, dev)->set_result_cb(dev, cb, user_data);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/usb_bc12.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_USB_BC12_H_ */
```

## 235.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

待修复（FIXME）：将这些项改为 Kconfig 选项。

### 注释 3：原第 193 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_USB_BC12_H_`。

## 235.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [bc12_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga035f4e4ba27f76094145571ebea97d73)
- [BC12_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22)
- [BC12_PORTABLE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48)
- [BC12_CHARGING_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef)
- [bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)
- [BC12_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6)
- [BC12_TYPE_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425)
- [BC12_TYPE_DCP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3)
- [BC12_TYPE_CDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c)
- [BC12_TYPE_PROPRIETARY](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2)
- [BC12_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30)
- [BC12_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)
- [bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)
- [bc12_role](../driver_model_reference/P025_BC12伙伴状态.md#a4da4a226fd933eea17da379687d49acf)
- [type](../driver_model_reference/P025_BC12伙伴状态.md#adeeb33acadfa0e1a8a57b862dfad97a1)
- [current_ua](../driver_model_reference/P025_BC12伙伴状态.md#a3a04b815fcc4c283d342b071dda1a0da)
- [voltage_uv](../driver_model_reference/P025_BC12伙伴状态.md#a1cdea094ae13acbb46fcae6f60ec3a7b)
- [pd_partner_connected](../driver_model_reference/P025_BC12伙伴状态.md#a4c1a653bd2393d79680f75afef334ac9)
- [bc12_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaeb039486c7826fe493e7f402212f2661)
- [device](../device_reference/P002_设备对象结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bc12_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga2a879017d34392308d4c078178db8407)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [bc12_set_result_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga0db43c4cc595cb76738cf24d97fa5228)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [bc12_partner_state::voltage_uv](../driver_model_reference/P025_BC12伙伴状态.md#a1cdea094ae13acbb46fcae6f60ec3a7b)
- [bc12_partner_state::current_ua](../driver_model_reference/P025_BC12伙伴状态.md#a3a04b815fcc4c283d342b071dda1a0da)
- [bc12_partner_state::pd_partner_connected](../driver_model_reference/P025_BC12伙伴状态.md#a4c1a653bd2393d79680f75afef334ac9)
- [bc12_partner_state::bc12_role](../driver_model_reference/P025_BC12伙伴状态.md#a4da4a226fd933eea17da379687d49acf)
- [bc12_partner_state::type](../driver_model_reference/P025_BC12伙伴状态.md#adeeb33acadfa0e1a8a57b862dfad97a1)

---

[上一章](P234_usb_audio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P236_usb_dc.h_源码浏览.md)
