---
id: learning.zephyr-docs.api-source-reference.page-184
title: wuc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_wuc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h.html)。

## 184.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00168"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00200"></a>
<a id="l00204"></a>
<a id="l00208"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00217"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="foldopen00251"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00263"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00295"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00309"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="foldopen00325"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__wuc__interface__backend_html_ga52c4fa3a73d2f3ef392c61b6c0133f6b"></a>
<a id="agroup__wuc__interface__backend_html_ga821a6abcc315fcd10e88e2f45641127e"></a>
<a id="agroup__wuc__interface__backend_html_ga94ca8c28ef9f1328ddddd3a5489204e2"></a>
<a id="agroup__wuc__interface__backend_html_gad36d204bead7c8ce4999858d16dca3ad"></a>
<a id="agroup__wuc__interface_html_ga28999754c6980fcfdae275adb0e811be"></a>
<a id="agroup__wuc__interface_html_ga4f280e6dc432be25c6a542abcf927b60"></a>
<a id="agroup__wuc__interface_html_ga7c7d2cc85a6b88cf01ce214f4f8e2904"></a>
<a id="agroup__wuc__interface_html_gab4a363a52e46b5d28fc8fb946ea7a29a"></a>
<a id="agroup__wuc__interface_html_gac03165353edf5e3a5273b60d7e1a1c8e"></a>
<a id="agroup__wuc__interface_html_gac3747f4707d490e620963d1c46a19af8"></a>
<a id="agroup__wuc__interface_html_gacac1135652beabd7858f3b01683a973b"></a>
<a id="agroup__wuc__interface_html_gafce93565e572eaddc98006f33f127ef5"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructwuc__driver__api_html"></a>
<a id="astructwuc__driver__api_html_a0662ddbad43d57e2a0beaa8f30643721"></a>
<a id="astructwuc__driver__api_html_a8b3036c2a04f94c467688f7cd880c5ae"></a>
<a id="astructwuc__driver__api_html_ab4a5c36416c1e1ccc86a784cb477fdb4"></a>
<a id="astructwuc__driver__api_html_ad95894cabddb42e772887ec38f0b11b7"></a>
<a id="astructwuc__dt__spec_html"></a>
<a id="astructwuc__dt__spec_html_a7c0c301fad56d99ca1d35007b6da88fc"></a>
<a id="astructwuc__dt__spec_html_ab617463172da938eb1e7e97a4ec0bb67"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_WUC_H_
#define ZEPHYR_INCLUDE_DRIVERS_WUC_H_


#include <errno.h>
#include <stddef.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

struct wuc_dt_spec {
        const struct device *dev;
        uint32_t id;
};

#define WUC_DT_SPEC_GET_BY_IDX(node_id, idx)                                                       \
        {.dev = DEVICE_DT_GET(DT_WUC_BY_IDX(node_id, idx)), .id = DT_WUC_ID_BY_IDX(node_id, idx)}

#define WUC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)                                     \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, wakeup_ctrls),                    \
                    (WUC_DT_SPEC_GET_BY_IDX(node_id, idx)),             \
                    (default_value))

#define WUC_DT_SPEC_GET(node_id) WUC_DT_SPEC_GET_BY_IDX(node_id, 0)

#define WUC_DT_SPEC_GET_OR(node_id, default_value)                                                 \
        WUC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)

#define WUC_DT_SPEC_INST_GET_BY_IDX(inst, idx) WUC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)

#define WUC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)                                   \
        COND_CODE_1(DT_PROP_HAS_IDX(DT_DRV_INST(inst), wakeup_ctrls, idx), \
                (WUC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)),       \
                (default_value))

#define WUC_DT_SPEC_INST_GET(inst) WUC_DT_SPEC_INST_GET_BY_IDX(inst, 0)

#define WUC_DT_SPEC_INST_GET_OR(inst, default_value)                                               \
        WUC_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)


typedef int (*wuc_api_enable_wakeup_source)(const struct device *dev, uint32_t id);

typedef int (*wuc_api_disable_wakeup_source)(const struct device *dev, uint32_t id);

typedef int (*wuc_api_check_wakeup_source_triggered)(const struct device *dev, uint32_t id);

typedef int (*wuc_api_clear_wakeup_source_triggered)(const struct device *dev, uint32_t id);

__subsystem struct wuc_driver_api {
        wuc_api_enable_wakeup_source enable;
        wuc_api_disable_wakeup_source disable;
        wuc_api_check_wakeup_source_triggered triggered;
        wuc_api_clear_wakeup_source_triggered clear;
};


static inline int wuc_enable_wakeup_source(const struct device *dev, uint32_t id)
{
        return DEVICE_API_GET(wuc, dev)->enable(dev, id);
}

static inline int wuc_enable_wakeup_source_dt(const struct wuc_dt_spec *spec)
{
        return wuc_enable_wakeup_source(spec->dev, spec->id);
}

static inline int wuc_disable_wakeup_source(const struct device *dev, uint32_t id)
{
        return DEVICE_API_GET(wuc, dev)->disable(dev, id);
}

static inline int wuc_disable_wakeup_source_dt(const struct wuc_dt_spec *spec)
{
        return wuc_disable_wakeup_source(spec->dev, spec->id);
}

static inline int wuc_check_wakeup_source_triggered(const struct device *dev, uint32_t id)
{
        if (DEVICE_API_GET(wuc, dev)->triggered == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(wuc, dev)->triggered(dev, id);
}

static inline int wuc_check_wakeup_source_triggered_dt(const struct wuc_dt_spec *spec)
{
        return wuc_check_wakeup_source_triggered(spec->dev, spec->id);
}

static inline int wuc_clear_wakeup_source_triggered(const struct device *dev, uint32_t id)
{
        if (DEVICE_API_GET(wuc, dev)->clear == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(wuc, dev)->clear(dev, id);
}

static inline int wuc_clear_wakeup_source_triggered_dt(const struct wuc_dt_spec *spec)
{
        return wuc_clear_wakeup_source_triggered(spec->dev, spec->id);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_WUC_H_ */
```

## 184.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 336 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_WUC_H_`。

## 184.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md#a7c0c301fad56d99ca1d35007b6da88fc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [id](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md#ab617463172da938eb1e7e97a4ec0bb67)
- [wuc_api_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga94ca8c28ef9f1328ddddd3a5489204e2)
- [wuc_api_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#gad36d204bead7c8ce4999858d16dca3ad)
- [wuc_api_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga821a6abcc315fcd10e88e2f45641127e)
- [wuc_api_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga52c4fa3a73d2f3ef392c61b6c0133f6b)
- [wuc_driver_api](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md)
- [enable](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#ab4a5c36416c1e1ccc86a784cb477fdb4)
- [disable](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#a8b3036c2a04f94c467688f7cd880c5ae)
- [triggered](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#a0662ddbad43d57e2a0beaa8f30643721)
- [clear](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#ad95894cabddb42e772887ec38f0b11b7)
- [wuc_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga28999754c6980fcfdae275adb0e811be)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [wuc_enable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac3747f4707d490e620963d1c46a19af8)
- [wuc_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gacac1135652beabd7858f3b01683a973b)
- [wuc_disable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga7c7d2cc85a6b88cf01ce214f4f8e2904)
- [wuc_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac03165353edf5e3a5273b60d7e1a1c8e)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [wuc_check_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gab4a363a52e46b5d28fc8fb946ea7a29a)
- [wuc_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga4f280e6dc432be25c6a542abcf927b60)
- [wuc_clear_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gafce93565e572eaddc98006f33f127ef5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [wuc_driver_api::triggered](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#a0662ddbad43d57e2a0beaa8f30643721)
- [wuc_driver_api::disable](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#a8b3036c2a04f94c467688f7cd880c5ae)
- [wuc_driver_api::enable](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#ab4a5c36416c1e1ccc86a784cb477fdb4)
- [wuc_driver_api::clear](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md#ad95894cabddb42e772887ec38f0b11b7)
- [wuc_dt_spec::dev](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md#a7c0c301fad56d99ca1d35007b6da88fc)
- [wuc_dt_spec::id](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md#ab617463172da938eb1e7e97a4ec0bb67)

---

[上一章](P183_video.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P185_ds3231.h_源码浏览.md)
