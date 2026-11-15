---
id: learning.zephyr-docs.api-source-supplement-reference.page-240
title: usbh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第240章\_usbh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P078_USB主机栈头文件接口.md)。

## 240.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00038"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="abitarray_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__usb__host__core__api_html_ga799fa25976930bb2ec39f351f91321ff"></a>
<a id="agroup__usb__host__core__api_html_ga9a0b6b3d13573de570a95985450fa869"></a>
<a id="agroup__usb__host__core__api_html_ga9f5874fb7d02f323f389b079a677372f"></a>
<a id="agroup__usb__host__core__api_html_gafa107bce1b2c0af5618f5cc6345a17e2"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructuhc__transfer_html"></a>
<a id="astructusb__device_html"></a>
<a id="astructusbh__class__api_html"></a>
<a id="astructusbh__class__api_html_a9758f521dbcaf4d04469e2e6d1e02792"></a>
<a id="astructusbh__class__api_html_aa589062f79f6ce4773b97be830061631"></a>
<a id="astructusbh__class__api_html_ac285cd96fbcdb36e689e71d6343afabd"></a>
<a id="astructusbh__class__api_html_ac9ba5ead8de356de9852f366a2d2509b"></a>
<a id="astructusbh__class__api_html_af8c42e60c7110f971d99cb36fb8c50f8"></a>
<a id="astructusbh__class__api_html_affc96d2f5cfc0759d53c939a40ef4b90"></a>
<a id="astructusbh__class__data_html"></a>
<a id="astructusbh__class__data_html_a1712aeca7d6d92a27593c9e6d10119d5"></a>
<a id="astructusbh__class__data_html_a5c30d8b884acb177c7351fdca0c3aca6"></a>
<a id="astructusbh__class__data_html_aa4e1255c33954ee65e8855d194564b0e"></a>
<a id="astructusbh__class__data_html_ab81986dc2d5f95c779999cedfc4d08e2"></a>
<a id="astructusbh__class__data_html_af5aaa5e6a088eb4b5c06d3fecabbbba2"></a>
<a id="astructusbh__class__filter_html"></a>
<a id="astructusbh__class__filter_html_a07dbc7ed52af241a25bcb481438c3f2f"></a>
<a id="astructusbh__class__filter_html_a202e2f9e25b49c790f979654575452ee"></a>
<a id="astructusbh__class__filter_html_aa2b4eafefe108ecb978c21d00ad0561c"></a>
<a id="astructusbh__class__filter_html_aad46cc5db6098c402098e4c2d0503f88"></a>
<a id="astructusbh__class__filter_html_adeede762ef1ff70888f794b688de01c2"></a>
<a id="astructusbh__context_html"></a>
<a id="astructusbh__context_html_a043d232f5927e2b26a99b0ac3de8717f"></a>
<a id="astructusbh__context_html_a21ae15801166839d3fce3ecaf634e0f7"></a>
<a id="astructusbh__context_html_a2fc9fa080e8d7eb9f6649f4f11b11f88"></a>
<a id="astructusbh__context_html_a3fbaf512dd1f68706684b4adf845ee51"></a>
<a id="astructusbh__context_html_ab0896f1266f674ba1dd62a102962f2b6"></a>
<a id="astructusbh__context_html_ac331b6555c6f1cf668ff92e3d092eedc"></a>
<a id="astructusbh__context_html_aefdff404508b92733f66142f1c299e01"></a>
<a id="astructusbh__status_html"></a>
<a id="astructusbh__status_html_a456a7050403bb854b4e3a3225bec94b2"></a>
<a id="astructusbh__status_html_a89bdc78fa77ab48deecc3670029e8354"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="auhc_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright Nordic Semiconductor ASA
 * SPDX-FileCopyrightText: Copyright 2025 NXP
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USBH_H_
#define ZEPHYR_INCLUDE_USBH_H_

#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/bitarray.h>
#include <zephyr/drivers/usb/uhc.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


struct usbh_status {
        unsigned int initialized : 1;
        unsigned int enabled : 1;
};

struct usbh_context {
        const char *name;
        struct k_mutex mutex;
        const struct device *dev;
        struct usbh_status status;
        sys_dlist_t udevs;
        struct usb_device *root;
        struct sys_bitarray *addr_ba;
};

#define USBH_CONTROLLER_DEFINE(device_name, uhc_dev)                    \
        SYS_BITARRAY_DEFINE_STATIC(ba_##device_name, 128);              \
        static STRUCT_SECTION_ITERABLE(usbh_context, device_name) = {   \
                .name = STRINGIFY(device_name),                         \
                .mutex = Z_MUTEX_INITIALIZER(device_name.mutex),        \
                .dev = uhc_dev,                                         \
                .addr_ba = &ba_##device_name,                           \
        }

struct usbh_class_data;

struct usbh_class_filter {
        uint16_t vid;
        uint16_t pid;
        uint8_t class;
        uint8_t sub;
        uint8_t proto;
        uint8_t flags;
};

struct usbh_class_api {
        int (*init)(struct usbh_class_data *const c_data);
        int (*completion_cb)(struct usbh_class_data *const c_data,
                             struct uhc_transfer *const xfer);
        int (*probe)(struct usbh_class_data *const c_data,
                     struct usb_device *const udev,
                     const uint8_t iface);
        int (*removed)(struct usbh_class_data *const c_data);
        int (*suspended)(struct usbh_class_data *const c_data);
        int (*resumed)(struct usbh_class_data *const c_data);
};

struct usbh_class_data {
        const char *name;
        struct usb_device *udev;
        uint8_t iface;
        struct usbh_class_api *api;
        void *priv;
};

enum usbh_class_state {
        USBH_CLASS_STATE_IDLE,
        USBH_CLASS_STATE_BOUND,
        USBH_CLASS_STATE_ERROR,
};
/* @endcond */

struct usbh_class_node {
        struct usbh_class_data *const c_data;
        const struct usbh_class_filter *filters;
        enum usbh_class_state state;
};
/* @endcond */

#define USBH_DEFINE_CLASS(class_name, class_api, class_priv, filt)              \
        static struct usbh_class_data UTIL_CAT(class_data_, class_name) = {     \
                .name = STRINGIFY(class_name),                                  \
                .api = class_api,                                               \
                .priv = class_priv,                                             \
        };                                                                      \
        static STRUCT_SECTION_ITERABLE(usbh_class_node, class_name) = {         \
                .c_data = &UTIL_CAT(class_data_, class_name),                   \
                .filters = filt,                                                \
        };

int usbh_init(struct usbh_context *uhs_ctx);

int usbh_enable(struct usbh_context *uhs_ctx);

int usbh_disable(struct usbh_context *uhs_ctx);

int usbh_shutdown(struct usbh_context *const uhs_ctx);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USBH_H_ */
```

## 240.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright Nordic Semiconductor ASA。

SPDX 文件版权声明（FileCopyrightText）：Copyright 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 149 行

Doxygen 条件文档块结束标记：`@endcond`。

### 注释 3：原第 165 行

Doxygen 条件文档块结束标记：`@endcond`。

### 注释 4：原第 240 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USBH_H_`。

## 240.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P078_USB主机栈头文件接口.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/bitarray.h](../bitarray_reference/P002_位数组头文件参考.md)
- [zephyr/drivers/usb/uhc.h](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usbh_status](../usb/P084_USB主机状态.md)
- [initialized](../usb/P084_USB主机状态.md#a89bdc78fa77ab48deecc3670029e8354)
- [enabled](../usb/P084_USB主机状态.md#a456a7050403bb854b4e3a3225bec94b2)
- [usbh_context](../usb/P083_USB主机上下文.md)
- [name](../usb/P083_USB主机上下文.md#ab0896f1266f674ba1dd62a102962f2b6)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](../usb/P083_USB主机上下文.md#a3fbaf512dd1f68706684b4adf845ee51)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../usb/P083_USB主机上下文.md#aefdff404508b92733f66142f1c299e01)
- [status](../usb/P083_USB主机上下文.md#a21ae15801166839d3fce3ecaf634e0f7)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [udevs](../usb/P083_USB主机上下文.md#a2fc9fa080e8d7eb9f6649f4f11b11f88)
- [usb_device](../usb/P080_USB主机设备对象.md)
- [root](../usb/P083_USB主机上下文.md#a043d232f5927e2b26a99b0ac3de8717f)
- [addr_ba](../usb/P083_USB主机上下文.md#ac331b6555c6f1cf668ff92e3d092eedc)
- [usbh_class_data](../usb/P086_USB主机类驱动数据.md)
- [usbh_class_filter](../usb/P087_USB主机类匹配条件.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [vid](../usb/P087_USB主机类匹配条件.md#aad46cc5db6098c402098e4c2d0503f88)
- [pid](../usb/P087_USB主机类匹配条件.md#a07dbc7ed52af241a25bcb481438c3f2f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sub](../usb/P087_USB主机类匹配条件.md#aa2b4eafefe108ecb978c21d00ad0561c)
- [proto](../usb/P087_USB主机类匹配条件.md#adeede762ef1ff70888f794b688de01c2)
- [flags](../usb/P087_USB主机类匹配条件.md#a202e2f9e25b49c790f979654575452ee)
- [usbh_class_api](../usb/P085_USB主机类驱动接口.md)
- [init](../usb/P085_USB主机类驱动接口.md#aa589062f79f6ce4773b97be830061631)
- [completion_cb](../usb/P085_USB主机类驱动接口.md#af8c42e60c7110f971d99cb36fb8c50f8)
- [uhc_transfer](../usb/P077_USB主机传输结构.md)
- [probe](../usb/P085_USB主机类驱动接口.md#ac285cd96fbcdb36e689e71d6343afabd)
- [removed](../usb/P085_USB主机类驱动接口.md#affc96d2f5cfc0759d53c939a40ef4b90)
- [suspended](../usb/P085_USB主机类驱动接口.md#ac9ba5ead8de356de9852f366a2d2509b)
- [resumed](../usb/P085_USB主机类驱动接口.md#a9758f521dbcaf4d04469e2e6d1e02792)
- [name](../usb/P086_USB主机类驱动数据.md#a5c30d8b884acb177c7351fdca0c3aca6)
- [udev](../usb/P086_USB主机类驱动数据.md#ab81986dc2d5f95c779999cedfc4d08e2)
- [iface](../usb/P086_USB主机类驱动数据.md#aa4e1255c33954ee65e8855d194564b0e)
- [api](../usb/P086_USB主机类驱动数据.md#a1712aeca7d6d92a27593c9e6d10119d5)
- [priv](../usb/P086_USB主机类驱动数据.md#af5aaa5e6a088eb4b5c06d3fecabbbba2)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [usbh_init](../usb/P079_USB主机核心API.md#ga9a0b6b3d13573de570a95985450fa869)
- [usbh_enable](../usb/P079_USB主机核心API.md#ga799fa25976930bb2ec39f351f91321ff)
- [usbh_disable](../usb/P079_USB主机核心API.md#ga9f5874fb7d02f323f389b079a677372f)
- [usbh_shutdown](../usb/P079_USB主机核心API.md#gafa107bce1b2c0af5618f5cc6345a17e2)
- [bitarray.h](../bitarray_reference/P002_位数组头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [usbh_class_api::resumed](../usb/P085_USB主机类驱动接口.md#a9758f521dbcaf4d04469e2e6d1e02792)
- [usbh_class_api::init](../usb/P085_USB主机类驱动接口.md#aa589062f79f6ce4773b97be830061631)
- [usbh_class_api::probe](../usb/P085_USB主机类驱动接口.md#ac285cd96fbcdb36e689e71d6343afabd)
- [usbh_class_api::suspended](../usb/P085_USB主机类驱动接口.md#ac9ba5ead8de356de9852f366a2d2509b)
- [usbh_class_api::completion_cb](../usb/P085_USB主机类驱动接口.md#af8c42e60c7110f971d99cb36fb8c50f8)
- [usbh_class_api::removed](../usb/P085_USB主机类驱动接口.md#affc96d2f5cfc0759d53c939a40ef4b90)
- [usbh_class_data::api](../usb/P086_USB主机类驱动数据.md#a1712aeca7d6d92a27593c9e6d10119d5)
- [usbh_class_data::name](../usb/P086_USB主机类驱动数据.md#a5c30d8b884acb177c7351fdca0c3aca6)
- [usbh_class_data::iface](../usb/P086_USB主机类驱动数据.md#aa4e1255c33954ee65e8855d194564b0e)
- [usbh_class_data::udev](../usb/P086_USB主机类驱动数据.md#ab81986dc2d5f95c779999cedfc4d08e2)
- [usbh_class_data::priv](../usb/P086_USB主机类驱动数据.md#af5aaa5e6a088eb4b5c06d3fecabbbba2)
- [usbh_class_filter::pid](../usb/P087_USB主机类匹配条件.md#a07dbc7ed52af241a25bcb481438c3f2f)
- [usbh_class_filter::flags](../usb/P087_USB主机类匹配条件.md#a202e2f9e25b49c790f979654575452ee)
- [usbh_class_filter::sub](../usb/P087_USB主机类匹配条件.md#aa2b4eafefe108ecb978c21d00ad0561c)
- [usbh_class_filter::vid](../usb/P087_USB主机类匹配条件.md#aad46cc5db6098c402098e4c2d0503f88)
- [usbh_class_filter::proto](../usb/P087_USB主机类匹配条件.md#adeede762ef1ff70888f794b688de01c2)
- [usbh_context::root](../usb/P083_USB主机上下文.md#a043d232f5927e2b26a99b0ac3de8717f)
- [usbh_context::status](../usb/P083_USB主机上下文.md#a21ae15801166839d3fce3ecaf634e0f7)
- [usbh_context::udevs](../usb/P083_USB主机上下文.md#a2fc9fa080e8d7eb9f6649f4f11b11f88)
- [usbh_context::mutex](../usb/P083_USB主机上下文.md#a3fbaf512dd1f68706684b4adf845ee51)
- [usbh_context::name](../usb/P083_USB主机上下文.md#ab0896f1266f674ba1dd62a102962f2b6)
- [usbh_context::addr_ba](../usb/P083_USB主机上下文.md#ac331b6555c6f1cf668ff92e3d092eedc)
- [usbh_context::dev](../usb/P083_USB主机上下文.md#aefdff404508b92733f66142f1c299e01)
- [usbh_status::enabled](../usb/P084_USB主机状态.md#a456a7050403bb854b4e3a3225bec94b2)
- [usbh_status::initialized](../usb/P084_USB主机状态.md#a89bdc78fa77ab48deecc3670029e8354)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [uhc.h](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html)

---

[上一章](P239_usbd_hid.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P241_utsname.h_源码浏览.md)
