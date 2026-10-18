---
id: learning.zephyr-docs.api-source-reference.page-123
title: device_runtime.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/device__runtime_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_device\_runtime.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/device__runtime_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P070_设备运行时电源头文件.md)。

## 123.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00174"></a>
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
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
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
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="foldopen00356"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="foldopen00394"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="foldopen00413"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="foldopen00432"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__subsys__pm__device__runtime_html_ga530d4be65757fb2276ab6f631953e045"></a>
<a id="agroup__subsys__pm__device__runtime_html_ga605cd2a3d0ea31efe6bd0b9a6f723219"></a>
<a id="agroup__subsys__pm__device__runtime_html_ga98daba53a992fb6bd2c2b31cb445844f"></a>
<a id="agroup__subsys__pm__device__runtime_html_ga9e90089b0ab78f365905418646e196c6"></a>
<a id="agroup__subsys__pm__device__runtime_html_gaa7fc78138e282b0eae7da67876baee80"></a>
<a id="agroup__subsys__pm__device__runtime_html_gaabcd2cc694c9e201dd87bf42f02b454c"></a>
<a id="agroup__subsys__pm__device__runtime_html_gad643d0c63b7091cdfa68d6e99b6048a0"></a>
<a id="agroup__subsys__pm__device__runtime_html_gadc36f344b2cb40c33d5b37eefd120c98"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2015 Intel Corporation.
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_PM_DEVICE_RUNTIME_H_
#define ZEPHYR_INCLUDE_PM_DEVICE_RUNTIME_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_PM_DEVICE_RUNTIME) || defined(__DOXYGEN__)
int pm_device_runtime_auto_enable(const struct device *dev);

int pm_device_runtime_enable(const struct device *dev);

int pm_device_runtime_disable(const struct device *dev);

int pm_device_runtime_get(const struct device *dev);

int pm_device_runtime_put(const struct device *dev);

int pm_device_runtime_put_async(const struct device *dev, k_timeout_t delay);

bool pm_device_runtime_is_enabled(const struct device *dev);

int pm_device_runtime_usage(const struct device *dev);

#else

static inline int pm_device_runtime_auto_enable(const struct device *dev)
{
        ARG_UNUSED(dev);
        return 0;
}

static inline int pm_device_runtime_enable(const struct device *dev)
{
        ARG_UNUSED(dev);
        return 0;
}

static inline int pm_device_runtime_disable(const struct device *dev)
{
        ARG_UNUSED(dev);
        return 0;
}

static inline int pm_device_runtime_get(const struct device *dev)
{
        ARG_UNUSED(dev);
        return 0;
}

static inline int pm_device_runtime_put(const struct device *dev)
{
        ARG_UNUSED(dev);
        return 0;
}

static inline int pm_device_runtime_put_async(const struct device *dev,
                k_timeout_t delay)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(delay);
        return 0;
}

static inline bool pm_device_runtime_is_enabled(const struct device *dev)
{
        ARG_UNUSED(dev);
        return false;
}

static inline int pm_device_runtime_usage(const struct device *dev)
{
        ARG_UNUSED(dev);
        return -ENOSYS;
}

#endif

#define LOG_DBG_PM_DEVICE_RUNTIME_GET(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_DBG("Failed to resume %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_DBG("Failed to resume %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_WRN_PM_DEVICE_RUNTIME_GET(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_WRN("Failed to resume %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_WRN("Failed to resume %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_ERR_PM_DEVICE_RUNTIME_GET(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_ERR("Failed to resume %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_ERR("Failed to resume %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_DBG_PM_DEVICE_RUNTIME_PUT(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_DBG("Failed to suspend %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_DBG("Failed to suspend %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_WRN_PM_DEVICE_RUNTIME_PUT(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_WRN("Failed to suspend %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_WRN("Failed to suspend %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_ERR_PM_DEVICE_RUNTIME_PUT(dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_ERR("Failed to suspend %s", (dev) ? (dev)->name : "(null)")), \
                    (LOG_ERR("Failed to suspend %s (%d)", (dev) ? (dev)->name : "(null)", \
                             GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_DBG_PM_DEVICE_RUNTIME_GET(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_DBG(_log_inst, "Failed to resume %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_DBG(_log_inst, "Failed to resume %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_WRN_PM_DEVICE_RUNTIME_GET(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_WRN(_log_inst, "Failed to resume %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_WRN(_log_inst, "Failed to resume %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_ERR_PM_DEVICE_RUNTIME_GET(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_ERR(_log_inst, "Failed to resume %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_ERR(_log_inst, "Failed to resume %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_DBG_PM_DEVICE_RUNTIME_PUT(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_DBG(_log_inst, "Failed to suspend %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_DBG(_log_inst, "Failed to suspend %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_WRN_PM_DEVICE_RUNTIME_PUT(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_WRN(_log_inst, "Failed to suspend %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_WRN(_log_inst, "Failed to suspend %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))

#define LOG_INST_ERR_PM_DEVICE_RUNTIME_PUT(_log_inst, dev, ...) \
        COND_CODE_1(IS_EQ(NUM_VA_ARGS(__VA_ARGS__), 0), \
                    (LOG_INST_ERR(_log_inst, "Failed to suspend %s", \
                                  (dev) ? (dev)->name : "(null)")), \
                    (LOG_INST_ERR(_log_inst, "Failed to suspend %s (%d)", \
                                  (dev) ? (dev)->name : "(null)", \
                                  GET_ARGS_FIRST_N(1, __VA_ARGS__))))


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_PM_DEVICE_RUNTIME_H_ */
```

## 123.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2015 Intel Corporation.。

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 446 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PM_DEVICE_RUNTIME_H_`。

## 123.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P070_设备运行时电源头文件.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [pm_device_runtime_auto_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gadc36f344b2cb40c33d5b37eefd120c98)
- [device](../device_reference/P002_设备对象结构.md)
- [pm_device_runtime_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gaabcd2cc694c9e201dd87bf42f02b454c)
- [pm_device_runtime_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gaa7fc78138e282b0eae7da67876baee80)
- [pm_device_runtime_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga530d4be65757fb2276ab6f631953e045)
- [pm_device_runtime_put](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga98daba53a992fb6bd2c2b31cb445844f)
- [pm_device_runtime_put_async](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga9e90089b0ab78f365905418646e196c6)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pm_device_runtime_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga605cd2a3d0ea31efe6bd0b9a6f723219)
- [pm_device_runtime_usage](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gad643d0c63b7091cdfa68d6e99b6048a0)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P122_decoder.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P124_dfd.h_源码浏览.md)
