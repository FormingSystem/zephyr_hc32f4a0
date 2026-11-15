---
id: learning.zephyr-docs.api-source-reference.page-685
title: pwm_utils.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第685章\_pwm\_utils.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html)。

## 685.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
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
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="adevicetree_8h_html"></a>
<a id="adrivers_2pwm_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__pwm__interface_html_ga5bc9607de7643cb78476ed354c51560b"></a>
<a id="agroup__single-linked-list__apis_html_ga296560229ffdfd0054c9c7b0602825a6"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_gac962e3ec8440e4adb2ba6682dbf186ff"></a>
<a id="agroup__single-linked-list__apis_html_gacf3aaf32a6a3389229b548588c6d655e"></a>
<a id="agroup__single-linked-list__apis_html_gaefa93f17fb5412b376360bf06d3e8a78"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="apwm__utils_8h_html_aa5e4496e8856b41b0992c33953f60426"></a>
<a id="apwm__utils_8h_html_ab51f5b6439ced8b87cd5953d8f510f65"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructpwm__event__callback_html"></a>
<a id="astructpwm__event__callback_html_a0f14cc1f7e4735e88f28ff4cfecbcec5"></a>
<a id="astructpwm__event__callback_html_a56f5f3b2589dffb88a8d893fe7d259ab"></a>

```c
/*
 * Copyright (c) 2025 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_UTILS_H_
#define ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_UTILS_H_

#include <stdbool.h>
#include <stdint.h>
#include <errno.h>

#include <zephyr/devicetree.h>
#include <zephyr/drivers/pwm.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

static inline int pwm_manage_event_callback(sys_slist_t *callbacks,
                                            struct pwm_event_callback *callback, bool set)
{
        __ASSERT_NO_MSG(callback != NULL);
        __ASSERT_NO_MSG(callback->handler != NULL);

        if (!sys_slist_is_empty(callbacks)) {
                if (!sys_slist_find_and_remove(callbacks, &callback->node)) {
                        if (!set) {
                                return -EINVAL;
                        }
                }
        } else if (!set) {
                return -EINVAL;
        }

        if (set) {
                sys_slist_prepend(callbacks, &callback->node);
        }

        return 0;
}

static inline void pwm_fire_event_callbacks(sys_slist_t *list, const struct device *dev,
                                            uint32_t channel, pwm_events_t events)
{
        struct pwm_event_callback *cb, *tmp;

        SYS_SLIST_FOR_EACH_CONTAINER_SAFE(list, cb, tmp, node) {
                if (cb->channel == channel) {
                        __ASSERT_NO_MSG(cb->handler != NULL);

                        cb->handler(dev, cb, channel, events);
                }
        }
}

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_UTILS_H_ */
```

## 685.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_UTILS_H_`。

## 685.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/drivers/pwm.h](../pwm_driver_reference/P001_PWM驱动头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [pwm_manage_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html#ab51f5b6439ced8b87cd5953d8f510f65)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [pwm_event_callback](../hardware/P257_PWM事件回调结构.md)
- [handler](../hardware/P257_PWM事件回调结构.md#a56f5f3b2589dffb88a8d893fe7d259ab)
- [sys_slist_is_empty](../slist_reference/P001_单向链表公共接口.md#gaefa93f17fb5412b376360bf06d3e8a78)
- [sys_slist_find_and_remove](../slist_reference/P001_单向链表公共接口.md#ga296560229ffdfd0054c9c7b0602825a6)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [sys_slist_prepend](../slist_reference/P001_单向链表公共接口.md#gac962e3ec8440e4adb2ba6682dbf186ff)
- [pwm_fire_event_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html#aa5e4496e8856b41b0992c33953f60426)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)
- [SYS_SLIST_FOR_EACH_CONTAINER_SAFE](../slist_reference/P001_单向链表公共接口.md#gacf3aaf32a6a3389229b548588c6d655e)
- [channel](../hardware/P257_PWM事件回调结构.md#a0f14cc1f7e4735e88f28ff4cfecbcec5)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pwm.h](../pwm_driver_reference/P001_PWM驱动头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [pwm_event_callback::channel](../hardware/P257_PWM事件回调结构.md#a0f14cc1f7e4735e88f28ff4cfecbcec5)
- [pwm_event_callback::handler](../hardware/P257_PWM事件回调结构.md#a56f5f3b2589dffb88a8d893fe7d259ab)

---

[上一章](P684_pwm_fake.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P686_qdec_bee.h_源码浏览.md)
