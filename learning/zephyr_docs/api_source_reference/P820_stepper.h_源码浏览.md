---
id: learning.zephyr-docs.api-source-reference.page-820
title: stepper.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第820章\_stepper.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)。

## 820.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00105"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00150"></a>
<a id="l00154"></a>
<a id="l00158"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00168"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
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
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__stepper__hw__driver__backend_html_ga01d81191585ac83ca1cdd2bcff16e7cb"></a>
<a id="agroup__stepper__hw__driver__backend_html_ga3bdb240620979bb7c1aec00bdc1e7391"></a>
<a id="agroup__stepper__hw__driver__backend_html_gab72c41a4685429cdb01365c66a247bb8"></a>
<a id="agroup__stepper__hw__driver__backend_html_gac903b636e01a33fa52882f0d70e745b3"></a>
<a id="agroup__stepper__hw__driver__backend_html_gae2e5fe2ffa722cafe649bc6fbd945296"></a>
<a id="agroup__stepper__hw__driver_html_ga3196866d26d23c04313d802f2d8c61c1"></a>
<a id="agroup__stepper__hw__driver_html_ga3395b5f8b401d8175067edfb25c2e0e8"></a>
<a id="agroup__stepper__hw__driver_html_ga609ddefa299ba40a997c626e4a36bdef"></a>
<a id="agroup__stepper__hw__driver_html_ga7df452f0e21c8db860616a9e8854b11a"></a>
<a id="agroup__stepper__hw__driver_html_gaa5e17e04a470832a305cef048694ec0a"></a>
<a id="agroup__stepper__hw__driver_html_gab1534238fbf8d2270ea4f69d3a558b5f"></a>
<a id="agroup__stepper__hw__driver_html_gab892a6b8d8fb34db0e682dd8f7de4218"></a>
<a id="agroup__stepper__hw__driver_html_gad8d053f92eb3a194652b4600af531e30"></a>
<a id="agroup__stepper__hw__driver_html_gad9fff2d103daad42fe49c7bbd5233b1b"></a>
<a id="agroup__stepper__hw__driver_html_ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445"></a>
<a id="agroup__stepper__hw__driver_html_ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14"></a>
<a id="agroup__stepper__hw__driver_html_ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructstepper__driver__api_html"></a>
<a id="astructstepper__driver__api_html_a2050fcc7db6132d13d4f7747c9dc3726"></a>
<a id="astructstepper__driver__api_html_a2efdff790e747e967a35af02ad2727b0"></a>
<a id="astructstepper__driver__api_html_a9eec21bcfb1c8da1a6ba678bd0bd024d"></a>
<a id="astructstepper__driver__api_html_ac0a42ffe845e2c86a41c2aa185cbc078"></a>
<a id="astructstepper__driver__api_html_adf13dfaee4e9194792bfafae9922f39f"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Carl Zeiss Meditec AG
 * SPDX-FileCopyrightText: Copyright (c) 2024 Jilay Sandeep Pandya
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_STEPPER_H_
#define ZEPHYR_INCLUDE_DRIVERS_STEPPER_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif


enum stepper_micro_step_resolution {
        STEPPER_MICRO_STEP_1 = 1,
        STEPPER_MICRO_STEP_2 = 2,
        STEPPER_MICRO_STEP_4 = 4,
        STEPPER_MICRO_STEP_8 = 8,
        STEPPER_MICRO_STEP_16 = 16,
        STEPPER_MICRO_STEP_32 = 32,
        STEPPER_MICRO_STEP_64 = 64,
        STEPPER_MICRO_STEP_128 = 128,
        STEPPER_MICRO_STEP_256 = 256,
};

#define MICRO_STEP_RES_INDEX(res) LOG2(res)

#define VALID_MICRO_STEP_RES(res)                                                                  \
        ((res) == STEPPER_MICRO_STEP_1 || (res) == STEPPER_MICRO_STEP_2 ||                 \
         (res) == STEPPER_MICRO_STEP_4 || (res) == STEPPER_MICRO_STEP_8 ||                 \
         (res) == STEPPER_MICRO_STEP_16 || (res) == STEPPER_MICRO_STEP_32 ||               \
         (res) == STEPPER_MICRO_STEP_64 || (res) == STEPPER_MICRO_STEP_128 ||              \
         (res) == STEPPER_MICRO_STEP_256)

enum stepper_event {
        STEPPER_EVENT_STALL_DETECTED = 0,
        STEPPER_EVENT_FAULT_DETECTED = 1,
};

typedef void (*stepper_event_cb_t)(const struct device *dev, const enum stepper_event event,
                                   void *user_data);


typedef int (*stepper_enable_t)(const struct device *dev);

typedef int (*stepper_disable_t)(const struct device *dev);

typedef int (*stepper_set_micro_step_res_t)(const struct device *dev,
                                            const enum stepper_micro_step_resolution resolution);

typedef int (*stepper_get_micro_step_res_t)(const struct device *dev,
                                            enum stepper_micro_step_resolution *resolution);

typedef int (*stepper_set_event_cb_t)(const struct device *dev, stepper_event_cb_t callback,
                                      void *user_data);

__subsystem struct stepper_driver_api {
        stepper_enable_t enable;
        stepper_disable_t disable;
        stepper_set_micro_step_res_t set_micro_step_res;
        stepper_get_micro_step_res_t get_micro_step_res;
        stepper_set_event_cb_t set_event_cb;
};


__syscall int stepper_enable(const struct device *dev);

static inline int z_impl_stepper_enable(const struct device *dev)
{
        return DEVICE_API_GET(stepper, dev)->enable(dev);
}

__syscall int stepper_disable(const struct device *dev);

static inline int z_impl_stepper_disable(const struct device *dev)
{
        return DEVICE_API_GET(stepper, dev)->disable(dev);
}

__syscall int stepper_set_micro_step_res(const struct device *dev,
                                             enum stepper_micro_step_resolution res);

static inline int z_impl_stepper_set_micro_step_res(const struct device *dev,
                                                        enum stepper_micro_step_resolution res)
{
        if (!VALID_MICRO_STEP_RES(res)) {
                return -EINVAL;
        }
        return DEVICE_API_GET(stepper, dev)->set_micro_step_res(dev, res);
}

__syscall int stepper_get_micro_step_res(const struct device *dev,
                                             enum stepper_micro_step_resolution *res);

static inline int z_impl_stepper_get_micro_step_res(const struct device *dev,
                                                        enum stepper_micro_step_resolution *res)
{
        __ASSERT_NO_MSG(res != NULL);
        return DEVICE_API_GET(stepper, dev)->get_micro_step_res(dev, res);
}

__syscall int stepper_set_event_cb(const struct device *dev, stepper_event_cb_t callback,
                                       void *user_data);

static inline int z_impl_stepper_set_event_cb(const struct device *dev,
                                                  stepper_event_cb_t cb, void *user_data)
{
        if (DEVICE_API_GET(stepper, dev)->set_event_cb == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(stepper, dev)->set_event_cb(dev, cb, user_data);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/stepper.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_STEPPER_H_ */
```

## 820.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Carl Zeiss Meditec AG。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Jilay Sandeep Pandya。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 280 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_STEPPER_H_`。

## 820.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)
- [STEPPER_MICRO_STEP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)
- [STEPPER_MICRO_STEP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)
- [STEPPER_MICRO_STEP_4](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)
- [STEPPER_MICRO_STEP_8](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)
- [STEPPER_MICRO_STEP_16](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)
- [STEPPER_MICRO_STEP_32](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)
- [STEPPER_MICRO_STEP_64](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)
- [STEPPER_MICRO_STEP_128](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)
- [STEPPER_MICRO_STEP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)
- [stepper_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab1534238fbf8d2270ea4f69d3a558b5f)
- [STEPPER_EVENT_STALL_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)
- [STEPPER_EVENT_FAULT_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4)
- [stepper_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga7df452f0e21c8db860616a9e8854b11a)
- [device](../device_reference/P002_设备对象结构.md)
- [stepper_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gab72c41a4685429cdb01365c66a247bb8)
- [stepper_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga3bdb240620979bb7c1aec00bdc1e7391)
- [stepper_set_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga01d81191585ac83ca1cdd2bcff16e7cb)
- [stepper_get_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gae2e5fe2ffa722cafe649bc6fbd945296)
- [stepper_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gac903b636e01a33fa52882f0d70e745b3)
- [stepper_driver_api](../hardware/P236_步进硬件驱动函数表.md)
- [enable](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a2050fcc7db6132d13d4f7747c9dc3726)
- [disable](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a2efdff790e747e967a35af02ad2727b0)
- [set_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#ac0a42ffe845e2c86a41c2aa185cbc078)
- [get_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a9eec21bcfb1c8da1a6ba678bd0bd024d)
- [set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#adf13dfaee4e9194792bfafae9922f39f)
- [stepper_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3395b5f8b401d8175067edfb25c2e0e8)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [stepper_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab892a6b8d8fb34db0e682dd8f7de4218)
- [stepper_set_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga609ddefa299ba40a997c626e4a36bdef)
- [VALID_MICRO_STEP_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3196866d26d23c04313d802f2d8c61c1)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [stepper_get_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gaa5e17e04a470832a305cef048694ec0a)
- [stepper_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad9fff2d103daad42fe49c7bbd5233b1b)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stepper_driver_api::enable](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a2050fcc7db6132d13d4f7747c9dc3726)
- [stepper_driver_api::disable](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a2efdff790e747e967a35af02ad2727b0)
- [stepper_driver_api::get_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#a9eec21bcfb1c8da1a6ba678bd0bd024d)
- [stepper_driver_api::set_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#ac0a42ffe845e2c86a41c2aa185cbc078)
- [stepper_driver_api::set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__driver__api.html#adf13dfaee4e9194792bfafae9922f39f)

---

[上一章](P819_stcc4.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P821_stepper_ctrl.h_源码浏览.md)
