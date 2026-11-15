---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-1
title: zephyr__drivers__dali.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dali_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr__drivers__dali.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dali_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P001_zephyr__drivers__dali.h_头文件参考.md)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00081"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00114"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__dali__interface__backend_html_ga00ceb1581576430fa6864a073eaa73b0"></a>
<a id="agroup__dali__interface__backend_html_gac6b54d7e448fd97e8936d4fd04177da0"></a>
<a id="agroup__dali__interface_html_ga0e295a9e86bc694d1516cb50cb579f91"></a>
<a id="agroup__dali__interface_html_ga79f624e680f364a0790119b3d5e09083"></a>
<a id="agroup__dali__interface_html_ga7ab4bdd2312ee38e473e7a2b56983166"></a>
<a id="agroup__dali__interface_html_ga7fc3646c3814fb3bebba8e77e0c0d424"></a>
<a id="agroup__dali__interface_html_gac25513281a022dce8bfe4a2fe46b609e"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962"></a>
<a id="agroup__dali__interface_html_gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdali__driver__api_html"></a>
<a id="astructdali__driver__api_html_a46e38012b78f141dad104f780a029161"></a>
<a id="astructdali__driver__api_html_a5f4fd21a37c64adb724e0f1986b2097c"></a>
<a id="astructdali__frame_html"></a>
<a id="astructdali__frame_html_a1fe86b3e83933bb32f6025414ed2405d"></a>
<a id="astructdali__frame_html_a401d83846d0ef76cee430ab1085f3ed6"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2026 by Sven Hädrich <sven.haedrich@sevenlab.de>
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DALI_H_
#define ZEPHYR_INCLUDE_DRIVERS_DALI_H_


#include <zephyr/device.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/__assert.h>
#include <errno.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

enum dali_event_type {
        DALI_FRAME_CORRUPT,
        DALI_FRAME_BACKWARD,
        DALI_FRAME_GEAR,
        DALI_FRAME_DEVICE,
        DALI_FRAME_FIRMWARE,
        DALI_EVENT_BUS_FAILURE,
        DALI_EVENT_BUS_IDLE,
};

struct dali_frame {
        uint32_t data;
        enum dali_event_type event_type;
};

typedef void (*dali_receive_callback_t)(const struct device *dev, struct dali_frame frame,
                                        void *user_data);

typedef void (*dali_transmit_callback_t)(const struct device *dev, int error, void *user_data);


typedef int (*dali_api_set_receive_callback_t)(const struct device *dev,
                                               dali_receive_callback_t callback, void *user_data);

typedef int (*dali_api_transmit_t)(const struct device *dev, const struct dali_frame *frame,
                                   dali_transmit_callback_t callback, void *user_data);

__subsystem struct dali_driver_api {
        dali_api_set_receive_callback_t set_receive_callback;
        dali_api_transmit_t transmit;
};


__syscall int dali_set_receive_callback(const struct device *dev, dali_receive_callback_t callback,
                                        void *user_data);

static inline int z_impl_dali_set_receive_callback(const struct device *dev,
                                                   dali_receive_callback_t callback,
                                                   void *user_data)
{
        return DEVICE_API_GET(dali, dev)->set_receive_callback(dev, callback, user_data);
}

__syscall int dali_transmit(const struct device *dev, const struct dali_frame *frame,
                            dali_transmit_callback_t callback, void *user_data);

static inline int z_impl_dali_transmit(const struct device *dev, const struct dali_frame *frame,
                                       dali_transmit_callback_t callback, void *user_data)
{
        return DEVICE_API_GET(dali, dev)->transmit(dev, frame, callback, user_data);
}

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/dali.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_DALI_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 by Sven Hädrich <sven.haedrich@sevenlab.de>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 185 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DALI_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P001_zephyr__drivers__dali.h_头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [dali_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga0e295a9e86bc694d1516cb50cb579f91)
- [DALI_FRAME_CORRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65)
- [DALI_FRAME_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941)
- [DALI_FRAME_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e)
- [DALI_FRAME_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718)
- [DALI_FRAME_FIRMWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf)
- [DALI_EVENT_BUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d)
- [DALI_EVENT_BUS_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962)
- [dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [data](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md#a1fe86b3e83933bb32f6025414ed2405d)
- [event_type](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md#a401d83846d0ef76cee430ab1085f3ed6)
- [dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)
- [device](../device_reference/P002_设备对象结构.md)
- [dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)
- [dali_api_set_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#ga00ceb1581576430fa6864a073eaa73b0)
- [dali_api_transmit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#gac6b54d7e448fd97e8936d4fd04177da0)
- [dali_driver_api](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md)
- [set_receive_callback](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md#a46e38012b78f141dad104f780a029161)
- [transmit](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md#a5f4fd21a37c64adb724e0f1986b2097c)
- [dali_set_receive_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga79f624e680f364a0790119b3d5e09083)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [dali_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gac25513281a022dce8bfe4a2fe46b609e)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dali_driver_api::set_receive_callback](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md#a46e38012b78f141dad104f780a029161)
- [dali_driver_api::transmit](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md#a5f4fd21a37c64adb724e0f1986b2097c)
- [dali_frame::data](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md#a1fe86b3e83933bb32f6025414ed2405d)
- [dali_frame::event_type](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md#a401d83846d0ef76cee430ab1085f3ed6)

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__misc__devmux__devmux.h_头文件源码.md)
