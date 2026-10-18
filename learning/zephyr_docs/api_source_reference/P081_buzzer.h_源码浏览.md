---
id: learning.zephyr-docs.api-source-reference.page-81
title: buzzer.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_buzzer.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h.html)。

## 81.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__buzzer__interface__backend_html_ga19d504c3b6dc816706d5cdd9dec37e3f"></a>
<a id="agroup__buzzer__interface__backend_html_gac6ae53a4674a3c1ca96a7e41735f9ff3"></a>
<a id="agroup__buzzer__interface__backend_html_gad6e97a02e02eaf1f127203a856018cf3"></a>
<a id="agroup__buzzer__interface__backend_html_gae36ee5133f2877ee6bd119214744b362"></a>
<a id="agroup__buzzer__interface_html_ga11d8fa4f540452ee487164a4af200868"></a>
<a id="agroup__buzzer__interface_html_ga6ad479424be12d83cab59656cf94cde0"></a>
<a id="agroup__buzzer__interface_html_ga8990f4ef56d763b59a59e9fc69782106"></a>
<a id="agroup__buzzer__interface_html_gad22c8c78d97814b849d87e42b1363ea9"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbuzzer__driver__api_html"></a>
<a id="astructbuzzer__driver__api_html_a2a1984f5925f744a57d10238377bc3e6"></a>
<a id="astructbuzzer__driver__api_html_a3a3154d8eaf631acbc1056a7126bfe64"></a>
<a id="astructbuzzer__driver__api_html_a43e80b2dfc113835c30a7f7de7617244"></a>
<a id="astructbuzzer__driver__api_html_a49d9150361b55a6e6f7f082cea7bc484"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2026 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_BUZZER_H_
#define ZEPHYR_INCLUDE_DRIVERS_BUZZER_H_


#include <errno.h>
#include <stdint.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BUZZER_FREQ_REST 0U

#define BUZZER_VOLUME_MAX 100U

#define BUZZER_DURATION_FOREVER UINT32_MAX


typedef int (*buzzer_tone_t)(const struct device *dev, uint32_t freq_hz,
                             uint32_t duration_ms);

typedef int (*buzzer_set_volume_t)(const struct device *dev, uint8_t percent);

typedef int (*buzzer_beep_t)(const struct device *dev, uint32_t duration_ms);

typedef int (*buzzer_stop_t)(const struct device *dev);

__subsystem struct buzzer_driver_api {
        buzzer_tone_t tone;
        buzzer_set_volume_t set_volume;
        buzzer_beep_t beep;
        buzzer_stop_t stop;
};


static inline int buzzer_tone(const struct device *dev, uint32_t freq_hz,
                              uint32_t duration_ms)
{
        return DEVICE_API_GET(buzzer, dev)->tone(dev, freq_hz, duration_ms);
}

static inline int buzzer_set_volume(const struct device *dev, uint8_t percent)
{
        return DEVICE_API_GET(buzzer, dev)->set_volume(dev, percent);
}

static inline int buzzer_beep(const struct device *dev, uint32_t duration_ms)
{
        return DEVICE_API_GET(buzzer, dev)->beep(dev, duration_ms);
}

static inline int buzzer_stop(const struct device *dev)
{
        return DEVICE_API_GET(buzzer, dev)->stop(dev);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_BUZZER_H_ */
```

## 81.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Carlo Caione <ccaione@baylibre.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 205 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BUZZER_H_`。

## 81.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [buzzer_tone_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gac6ae53a4674a3c1ca96a7e41735f9ff3)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [buzzer_set_volume_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#ga19d504c3b6dc816706d5cdd9dec37e3f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buzzer_beep_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gae36ee5133f2877ee6bd119214744b362)
- [buzzer_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gad6e97a02e02eaf1f127203a856018cf3)
- [buzzer_driver_api](../hardware/P146_蜂鸣器驱动操作表.md)
- [tone](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a49d9150361b55a6e6f7f082cea7bc484)
- [set_volume](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a43e80b2dfc113835c30a7f7de7617244)
- [beep](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a3a3154d8eaf631acbc1056a7126bfe64)
- [stop](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a2a1984f5925f744a57d10238377bc3e6)
- [buzzer_tone](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga11d8fa4f540452ee487164a4af200868)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [buzzer_set_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga6ad479424be12d83cab59656cf94cde0)
- [buzzer_beep](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#gad22c8c78d97814b849d87e42b1363ea9)
- [buzzer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga8990f4ef56d763b59a59e9fc69782106)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [buzzer_driver_api::stop](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a2a1984f5925f744a57d10238377bc3e6)
- [buzzer_driver_api::beep](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a3a3154d8eaf631acbc1056a7126bfe64)
- [buzzer_driver_api::set_volume](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a43e80b2dfc113835c30a7f7de7617244)
- [buzzer_driver_api::tone](https://docs.zephyrproject.org/latest/doxygen/html/structbuzzer__driver__api.html#a49d9150361b55a6e6f7f082cea7bc484)

---

[上一章](P080_busy_sim.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P082_callback_defines.h_源码浏览.md)
