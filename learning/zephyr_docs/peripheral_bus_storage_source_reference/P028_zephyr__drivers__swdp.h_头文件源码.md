---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-28
title: zephyr__drivers__swdp.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr__drivers__swdp.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)。

## 28.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__swdp__interface_html_ga02e1b57447bd836cff26cc007ced6b59"></a>
<a id="agroup__swdp__interface_html_ga084283204c12b2eb0de05c6d72217ee7"></a>
<a id="agroup__swdp__interface_html_ga1b652fa82819ea8a393eb08b47acb33f"></a>
<a id="agroup__swdp__interface_html_ga3b23bf1ffc3d378bc19c3d50d5476dda"></a>
<a id="agroup__swdp__interface_html_ga8466b58965837c3cdf8c259ae38a2d1a"></a>
<a id="agroup__swdp__interface_html_gab71cacb48078e8f76349354d915514e1"></a>
<a id="agroup__swdp__interface_html_gae1f3d9d1bb1f7f588196ec30e75b3952"></a>
<a id="agroup__swdp__interface_html_gaeac761589b00b889adebf3bd94d4253f"></a>
<a id="agroup__swdp__interface_html_gaf9b640f9a4b59c2294f45f238287d6eb"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructswdp__api_html"></a>
<a id="astructswdp__api_html_a0480ec7f5479382457ac2e9c264e46f4"></a>
<a id="astructswdp__api_html_a3b2a89ee837aae3731ba0d2ba8c1c323"></a>
<a id="astructswdp__api_html_a4a4e268bc2e80b0fa3af76c8fb6d70c7"></a>
<a id="astructswdp__api_html_a62b5b2285bdec6d9e6069f1671ad1bc3"></a>
<a id="astructswdp__api_html_a642cd297ace3437669be092ca4061911"></a>
<a id="astructswdp__api_html_aa7e408b542b1bd9134b86f2a257cf004"></a>
<a id="astructswdp__api_html_aba201f47bb6037334b3da19d17ea7349"></a>
<a id="astructswdp__api_html_ac0e08f227a18d087fa98894caa277282"></a>
<a id="astructswdp__api_html_af83ae99fb199d5506256c13aec92f1a7"></a>

```c
/*
 * Copyright (c) 2019 PHYTEC Messtechnik GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SWDP_H_
#define ZEPHYR_INCLUDE_SWDP_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif



#define SWDP_REQUEST_APnDP                      BIT(0)
#define SWDP_REQUEST_RnW                        BIT(1)
#define SWDP_REQUEST_A2                         BIT(2)
#define SWDP_REQUEST_A3                         BIT(3)



#define SWDP_ACK_OK                             BIT(0)
#define SWDP_ACK_WAIT                           BIT(1)
#define SWDP_ACK_FAULT                          BIT(2)


#define SWDP_TRANSFER_ERROR                     BIT(3)


#define SWDP_SWCLK_PIN                  0U
#define SWDP_SWDIO_PIN                  1U
#define SWDP_nRESET_PIN                 7U


struct swdp_api {
        int (*swdp_output_sequence)(const struct device *dev,
                                    uint32_t count,
                                    const uint8_t *data);

        int (*swdp_input_sequence)(const struct device *dev,
                                   uint32_t count,
                                   uint8_t *data);

        int (*swdp_transfer)(const struct device *dev,
                             uint8_t request,
                             uint32_t *data,
                             uint8_t idle_cycles,
                             uint8_t *response);

        int (*swdp_set_pins)(const struct device *dev,
                             uint8_t pins, uint8_t value);

        int (*swdp_get_pins)(const struct device *dev, uint8_t *state);

        int (*swdp_set_clock)(const struct device *dev, uint32_t clock);

        int (*swdp_configure)(const struct device *dev,
                              uint8_t turnaround,
                              bool data_phase);

        int (*swdp_port_on)(const struct device *dev);

        int (*swdp_port_off)(const struct device *dev);
};

__syscall int swdp_output_sequence(const struct device *dev,
                                   const uint32_t count,
                                   const uint8_t *const data);

static inline int z_impl_swdp_output_sequence(const struct device *dev,
                                              const uint32_t count,
                                              const uint8_t *const data)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_output_sequence(dev, count, data);
}

__syscall int swdp_input_sequence(const struct device *dev,
                                  const uint32_t count,
                                  uint8_t *const buf);

static inline int z_impl_swdp_input_sequence(const struct device *dev,
                                             const uint32_t count,
                                             uint8_t *const buf)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_input_sequence(dev, count, buf);
}

__syscall int swdp_transfer(const struct device *dev,
                            const uint8_t request,
                            uint32_t *const data,
                            const uint8_t idle_cycles,
                            uint8_t *const response);

static inline int z_impl_swdp_transfer(const struct device *dev,
                                       const uint8_t request,
                                       uint32_t *const data,
                                       const uint8_t idle_cycles,
                                       uint8_t *const response)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_transfer(dev, request, data, idle_cycles, response);
}

__syscall int swdp_set_pins(const struct device *dev,
                            const uint8_t pins,
                            const uint8_t value);

static inline int z_impl_swdp_set_pins(const struct device *dev,
                                       const uint8_t pins,
                                       const uint8_t value)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_set_pins(dev, pins, value);
}

__syscall int swdp_get_pins(const struct device *dev,
                            uint8_t *const state);

static inline int z_impl_swdp_get_pins(const struct device *dev,
                                       uint8_t *const state)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_get_pins(dev, state);
}

__syscall int swdp_set_clock(const struct device *dev,
                             const uint32_t clock);

static inline int z_impl_swdp_set_clock(const struct device *dev,
                                         const uint32_t clock)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_set_clock(dev, clock);
}

__syscall int swdp_port_on(const struct device *dev);

static inline int z_impl_swdp_port_on(const struct device *dev)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_port_on(dev);
}

__syscall int swdp_port_off(const struct device *dev);

static inline int z_impl_swdp_port_off(const struct device *dev)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_port_off(dev);
}

__syscall int swdp_configure(const struct device *dev,
                             const uint8_t turnaround,
                             const bool data_phase);

static inline int z_impl_swdp_configure(const struct device *dev,
                                        const uint8_t turnaround,
                                        const bool data_phase)
{
        const struct swdp_api *api = dev->api;

        return api->swdp_configure(dev, turnaround, data_phase);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/swdp.h>

#endif /* ZEPHYR_INCLUDE_SWDP_H_ */
```

## 28.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 PHYTEC Messtechnik GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 391 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SWDP_H_`。

## 28.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [swdp_api](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md)
- [swdp_output_sequence](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a4a4e268bc2e80b0fa3af76c8fb6d70c7)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [swdp_input_sequence](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a0480ec7f5479382457ac2e9c264e46f4)
- [swdp_transfer](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a3b2a89ee837aae3731ba0d2ba8c1c323)
- [swdp_set_pins](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#af83ae99fb199d5506256c13aec92f1a7)
- [swdp_get_pins](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#ac0e08f227a18d087fa98894caa277282)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [swdp_set_clock](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#aba201f47bb6037334b3da19d17ea7349)
- [swdp_configure](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a62b5b2285bdec6d9e6069f1671ad1bc3)
- [swdp_port_on](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a642cd297ace3437669be092ca4061911)
- [swdp_port_off](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#aa7e408b542b1bd9134b86f2a257cf004)
- [swdp_output_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga084283204c12b2eb0de05c6d72217ee7)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [swdp_input_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga1b652fa82819ea8a393eb08b47acb33f)
- [swdp_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gab71cacb48078e8f76349354d915514e1)
- [swdp_set_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga8466b58965837c3cdf8c259ae38a2d1a)
- [swdp_get_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga3b23bf1ffc3d378bc19c3d50d5476dda)
- [swdp_set_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaf9b640f9a4b59c2294f45f238287d6eb)
- [swdp_port_on](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga02e1b57447bd836cff26cc007ced6b59)
- [swdp_port_off](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaeac761589b00b889adebf3bd94d4253f)
- [swdp_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gae1f3d9d1bb1f7f588196ec30e75b3952)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [swdp_api::swdp_input_sequence](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a0480ec7f5479382457ac2e9c264e46f4)
- [swdp_api::swdp_transfer](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a3b2a89ee837aae3731ba0d2ba8c1c323)
- [swdp_api::swdp_output_sequence](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a4a4e268bc2e80b0fa3af76c8fb6d70c7)
- [swdp_api::swdp_configure](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a62b5b2285bdec6d9e6069f1671ad1bc3)
- [swdp_api::swdp_port_on](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#a642cd297ace3437669be092ca4061911)
- [swdp_api::swdp_port_off](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#aa7e408b542b1bd9134b86f2a257cf004)
- [swdp_api::swdp_set_clock](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#aba201f47bb6037334b3da19d17ea7349)
- [swdp_api::swdp_get_pins](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#ac0e08f227a18d087fa98894caa277282)
- [swdp_api::swdp_set_pins](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md#af83ae99fb199d5506256c13aec92f1a7)

---

[上一章](P027_zephyr__drivers__smbus.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__w1.h_头文件源码.md)
