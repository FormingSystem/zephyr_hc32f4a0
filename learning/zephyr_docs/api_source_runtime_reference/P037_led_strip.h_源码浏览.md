---
id: learning.zephyr-docs.api-source-runtime-reference.page-37
title: led_strip.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_led\_strip.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h.html)。

## 37.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00114"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
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
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__led__strip__interface__backend_html_ga3487e5d4a339898f88a225bb3678776b"></a>
<a id="agroup__led__strip__interface__backend_html_gaa36be40a962173021a547192d0d39151"></a>
<a id="agroup__led__strip__interface__backend_html_gab11579a7b5b7febfd48fa12560254501"></a>
<a id="agroup__led__strip__interface_html_ga6e63331a5be2430968ab8b60692f8d67"></a>
<a id="agroup__led__strip__interface_html_ga7f94eab0b357a81cccb5f0ea1575714a"></a>
<a id="agroup__led__strip__interface_html_ga846b1d37bc6f7ed2014bea9603788b34"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_gaa1591a4f3a86360108de5b9ba34980ca"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructled__rgb_html"></a>
<a id="astructled__rgb_html_a2b3072dbddc32f7a93b87b9ed01e1a33"></a>
<a id="astructled__rgb_html_ab24a1948906fcb4c5978a84ac46b779a"></a>
<a id="astructled__rgb_html_abf071f86f224daa42b3b905071e550af"></a>
<a id="astructled__strip__driver__api_html"></a>
<a id="astructled__strip__driver__api_html_a083406f6a5b5ce034268315b7075d671"></a>
<a id="astructled__strip__driver__api_html_ad5969b78c4b77d570669abd5143ec228"></a>
<a id="astructled__strip__driver__api_html_af0f7a73d61589355b520f76073013425"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 * Copyright (c) 2024 Jamie McCrae
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_LED_STRIP_H_
#define ZEPHYR_INCLUDE_DRIVERS_LED_STRIP_H_


#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

struct led_rgb {
#ifdef CONFIG_LED_STRIP_RGB_SCRATCH
        /*
         * Pad/scratch space needed by some drivers. Users should
         * ignore.
         */
        uint8_t scratch;
#endif
        uint8_t r;
        uint8_t g;
        uint8_t b;
};


typedef int (*led_api_update_rgb)(const struct device *dev,
                                  struct led_rgb *pixels,
                                  size_t num_pixels);

typedef int (*led_api_update_channels)(const struct device *dev,
                                       uint8_t *channels,
                                       size_t num_channels);

typedef size_t (*led_api_length)(const struct device *dev);

__subsystem struct led_strip_driver_api {
        led_api_update_rgb update_rgb;
        led_api_length length;
        led_api_update_channels update_channels;
};


static inline int led_strip_update_rgb(const struct device *dev,
                                       struct led_rgb *pixels,
                                       size_t num_pixels)
{
        const struct led_strip_driver_api *api = DEVICE_API_GET(led_strip, dev);

        /* Allow for out-of-tree drivers that do not have this function for 2 Zephyr releases
         * until making it mandatory, function added after Zephyr 3.6
         */
        if (api->length != NULL) {
                /* Ensure supplied pixel size is valid for this device */
                if (api->length(dev) < num_pixels) {
                        return -ERANGE;
                }
        }

        return api->update_rgb(dev, pixels, num_pixels);
}

static inline int led_strip_update_channels(const struct device *dev,
                                            uint8_t *channels,
                                            size_t num_channels)
{
        const struct led_strip_driver_api *api = DEVICE_API_GET(led_strip, dev);

        if (api->update_channels == NULL) {
                return -ENOSYS;
        }

        return api->update_channels(dev, channels, num_channels);
}

static inline size_t led_strip_length(const struct device *dev)
{
        return DEVICE_API_GET(led_strip, dev)->length(dev);
}

#ifdef __cplusplus
}
#endif


#endif  /* ZEPHYR_INCLUDE_DRIVERS_LED_STRIP_H_ */
```

## 37.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

版权（Copyright）：© 2024 Jamie McCrae。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

某些驱动需要的填充/临时空间（Pad/scratch space），用户应忽略。

### 注释 3：原第 133 行

允许树外驱动（Out-of-tree drivers）在两个 Zephyr 发行版本内暂不提供此函数，之后才将其设为必需。该函数在 Zephyr 3.6 之后加入。

### 注释 4：原第 137 行

确保所提供的像素大小对该设备有效。

### 注释 5：原第 194 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_LED_STRIP_H_`。

## 37.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [led_rgb](../hardware/P209_LED灯带颜色结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [r](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#a2b3072dbddc32f7a93b87b9ed01e1a33)
- [g](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#ab24a1948906fcb4c5978a84ac46b779a)
- [b](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#abf071f86f224daa42b3b905071e550af)
- [led_api_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gaa36be40a962173021a547192d0d39151)
- [device](../device_reference/P002_设备对象结构.md)
- [led_api_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gab11579a7b5b7febfd48fa12560254501)
- [led_api_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#ga3487e5d4a339898f88a225bb3678776b)
- [led_strip_driver_api](../hardware/P211_LED灯带驱动函数表.md)
- [update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#af0f7a73d61589355b520f76073013425)
- [length](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#a083406f6a5b5ce034268315b7075d671)
- [update_channels](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#ad5969b78c4b77d570669abd5143ec228)
- [led_strip_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga6e63331a5be2430968ab8b60692f8d67)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ERANGE](../error_reference/P003_系统错误号公共接口.md#gaa1591a4f3a86360108de5b9ba34980ca)
- [led_strip_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga846b1d37bc6f7ed2014bea9603788b34)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [led_strip_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [led_rgb::r](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#a2b3072dbddc32f7a93b87b9ed01e1a33)
- [led_rgb::g](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#ab24a1948906fcb4c5978a84ac46b779a)
- [led_rgb::b](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#abf071f86f224daa42b3b905071e550af)
- [led_strip_driver_api::length](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#a083406f6a5b5ce034268315b7075d671)
- [led_strip_driver_api::update_channels](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#ad5969b78c4b77d570669abd5143ec228)
- [led_strip_driver_api::update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#af0f7a73d61589355b520f76073013425)

---

[上一章](P036_kobject.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P038_types.h_源码浏览.md)
