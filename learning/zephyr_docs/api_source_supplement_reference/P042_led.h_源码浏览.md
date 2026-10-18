---
id: learning.zephyr-docs.api-source-supplement-reference.page-42
title: led.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_led.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html)。

## 42.1\_原始可见代码（Source Code）

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
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00059"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
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
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
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
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
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
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
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
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="foldopen00404"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="foldopen00421"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="foldopen00436"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="foldopen00450"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="foldopen00482"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="foldopen00508"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="foldopen00549"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="foldopen00564"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__led__interface__backend_html_ga3828b1e544a2f64378d5c3bfbbaa0c77"></a>
<a id="agroup__led__interface__backend_html_ga5ae67fe64f97b0e716f9eb2f3a34f1fd"></a>
<a id="agroup__led__interface__backend_html_ga66dac12510c3a2281378d532ba6db2ae"></a>
<a id="agroup__led__interface__backend_html_ga977317f3208d5336463edf9979def4ae"></a>
<a id="agroup__led__interface__backend_html_gad13f55702668133575658d2ccc295339"></a>
<a id="agroup__led__interface__backend_html_gad3c655794f58045459cbd910592d2cdd"></a>
<a id="agroup__led__interface__backend_html_gae24caa14f6aa41c2a509d2eaf468463f"></a>
<a id="agroup__led__interface_html_ga01ee05a71058adf86e950805524865a0"></a>
<a id="agroup__led__interface_html_ga22c9dbe76f06fec327aebe06448d1542"></a>
<a id="agroup__led__interface_html_ga24d4007f81483d0fe8b9988288adf59a"></a>
<a id="agroup__led__interface_html_ga4a30a26f21d80f40ce3364880e0dfee3"></a>
<a id="agroup__led__interface_html_ga4f31fecd215e5597999be4d16b0d2dd5"></a>
<a id="agroup__led__interface_html_ga717bdbe76331b6286c58feb6e3e214dd"></a>
<a id="agroup__led__interface_html_ga7bb18ca9f746ebcfbfc397886643f16d"></a>
<a id="agroup__led__interface_html_ga8b6618e4fea4f44f218f95fd16abc16b"></a>
<a id="agroup__led__interface_html_ga94dd46cc96f6ade5cebaa46a5f7ca5ea"></a>
<a id="agroup__led__interface_html_ga9925483b97073354f7be6b40aa2dad1a"></a>
<a id="agroup__led__interface_html_gaa2994b959c730dad3432481bba278497"></a>
<a id="agroup__led__interface_html_gaa2b262a309e4ede4cb5715c69d900804"></a>
<a id="agroup__led__interface_html_gab3581c7571b4623696ad57d25d6bd96f"></a>
<a id="agroup__led__interface_html_gaca479fd77518331f4fc84f788e345882"></a>
<a id="agroup__led__interface_html_gad4daafd7fcab22d1d68745b7264d0f73"></a>
<a id="agroup__led__interface_html_gaecc33acfc2b1dde870b411d7f30eed82"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructled__driver__api_html"></a>
<a id="astructled__driver__api_html_a19ad736a130da2aff6bd5b299d8c33a7"></a>
<a id="astructled__driver__api_html_a336f30f2c1bd3d99213cae66911c142a"></a>
<a id="astructled__driver__api_html_a7c68219e44bcf6e766e64fd3967ecf7e"></a>
<a id="astructled__driver__api_html_a9c3e3c4d40c4b8219755df6df96b0058"></a>
<a id="astructled__driver__api_html_a9ce7322282f8c525256d3c16a514ecc4"></a>
<a id="astructled__driver__api_html_ada1dfb1830b48afb020c7e60dbd92337"></a>
<a id="astructled__driver__api_html_af1974c5cc20c818e0e387b34cd14ac3b"></a>
<a id="astructled__dt__spec_html"></a>
<a id="astructled__dt__spec_html_a72c5ff64b89344ca9644fd2b4f4c9515"></a>
<a id="astructled__dt__spec_html_ad92b9ee24cb31fcc0a2352bcf831cecb"></a>
<a id="astructled__info_html"></a>
<a id="astructled__info_html_a5d01795e49663654e9fe4a821797956a"></a>
<a id="astructled__info_html_a7f87ebb0718e1dc189e6d48d5bb97c55"></a>
<a id="astructled__info_html_a8daacbe0a68d7ff710938722003fceaf"></a>
<a id="astructled__info_html_ab6db05157b960669e3b01154a9621530"></a>

```c
/*
 * Copyright (c) 2018 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_LED_H_
#define ZEPHYR_INCLUDE_DRIVERS_LED_H_


#include <errno.h>

#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

#define LED_BRIGHTNESS_MAX 100u

struct led_info {
        const char *label;
        uint32_t index;
        uint8_t num_colors;
        const uint8_t *color_mapping;
};


typedef int (*led_api_blink)(const struct device *dev, uint32_t led,
                             uint32_t delay_on, uint32_t delay_off);

typedef int (*led_api_get_info)(const struct device *dev, uint32_t led,
                                const struct led_info **info);

typedef int (*led_api_set_brightness)(const struct device *dev, uint32_t led,
                                      uint8_t value);
typedef int (*led_api_set_color)(const struct device *dev, uint32_t led,
                                 uint8_t num_colors, const uint8_t *color);

typedef int (*led_api_on)(const struct device *dev, uint32_t led);

typedef int (*led_api_off)(const struct device *dev, uint32_t led);

typedef int (*led_api_write_channels)(const struct device *dev,
                                      uint32_t start_channel,
                                      uint32_t num_channels,
                                      const uint8_t *buf);

__subsystem struct led_driver_api {
        led_api_on on;
        led_api_off off;
        led_api_set_brightness set_brightness;
        led_api_blink blink;
        led_api_get_info get_info;
        led_api_set_color set_color;
        led_api_write_channels write_channels;
};


__syscall int led_blink(const struct device *dev, uint32_t led,
                            uint32_t delay_on, uint32_t delay_off);

static inline int z_impl_led_blink(const struct device *dev, uint32_t led,
                                   uint32_t delay_on, uint32_t delay_off)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->blink == NULL) {
                return -ENOSYS;
        }
        return api->blink(dev, led, delay_on, delay_off);
}

__syscall int led_get_info(const struct device *dev, uint32_t led,
                           const struct led_info **info);

static inline int z_impl_led_get_info(const struct device *dev, uint32_t led,
                                      const struct led_info **info)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->get_info == NULL) {
                *info = NULL;
                return -ENOSYS;
        }
        return api->get_info(dev, led, info);
}

__syscall int led_set_brightness(const struct device *dev, uint32_t led,
                                     uint8_t value);

static inline int z_impl_led_set_brightness(const struct device *dev,
                                            uint32_t led,
                                            uint8_t value)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->set_brightness == NULL) {
                if (api->on == NULL || api->off == NULL) {
                        return -ENOSYS;
                }
        }

        if (value > LED_BRIGHTNESS_MAX) {
                return -EINVAL;
        }

        if (api->set_brightness == NULL) {
                if (value) {
                        return api->on(dev, led);
                } else {
                        return api->off(dev, led);
                }
        }

        return api->set_brightness(dev, led, value);
}

__syscall int led_write_channels(const struct device *dev,
                                 uint32_t start_channel,
                                 uint32_t num_channels, const uint8_t *buf);

static inline int
z_impl_led_write_channels(const struct device *dev, uint32_t start_channel,
                          uint32_t num_channels, const uint8_t *buf)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->write_channels == NULL) {
                return -ENOSYS;
        }
        return api->write_channels(dev, start_channel, num_channels, buf);
}

__syscall int led_set_channel(const struct device *dev,
                              uint32_t channel, uint8_t value);

static inline int z_impl_led_set_channel(const struct device *dev,
                                         uint32_t channel, uint8_t value)
{
        return z_impl_led_write_channels(dev, channel, 1, &value);
}

__syscall int led_set_color(const struct device *dev, uint32_t led,
                            uint8_t num_colors, const uint8_t *color);

static inline int z_impl_led_set_color(const struct device *dev, uint32_t led,
                                       uint8_t num_colors, const uint8_t *color)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->set_color == NULL) {
                return -ENOSYS;
        }
        return api->set_color(dev, led, num_colors, color);
}

__syscall int led_on(const struct device *dev, uint32_t led);

static inline int z_impl_led_on(const struct device *dev, uint32_t led)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->set_brightness == NULL && api->on == NULL) {
                return -ENOSYS;
        }

        if (api->on == NULL) {
                return api->set_brightness(dev, led, LED_BRIGHTNESS_MAX);
        }

        return api->on(dev, led);
}

__syscall int led_off(const struct device *dev, uint32_t led);

static inline int z_impl_led_off(const struct device *dev, uint32_t led)
{
        const struct led_driver_api *api = DEVICE_API_GET(led, dev);

        if (api->set_brightness == NULL && api->off == NULL) {
                return -ENOSYS;
        }

        if (api->off == NULL) {
                return api->set_brightness(dev, led, 0);
        }

        return api->off(dev, led);
}

/*
 * LED DT helpers.
 */

struct led_dt_spec {
        const struct device *dev;
        uint32_t index;
};

static inline int led_blink_dt(const struct led_dt_spec *spec, uint32_t delay_on,
                               uint32_t delay_off)
{
        return led_blink(spec->dev, spec->index, delay_on, delay_off);
}

static inline int led_get_info_dt(const struct led_dt_spec *spec, const struct led_info **info)
{
        return led_get_info(spec->dev, spec->index, info);
}

static inline int led_set_brightness_dt(const struct led_dt_spec *spec,
                                        uint8_t value)
{
        return led_set_brightness(spec->dev, spec->index, value);
}

static inline int led_set_color_dt(const struct led_dt_spec *spec, uint8_t num_colors,
                                   const uint8_t *color)
{
        return led_set_color(spec->dev, spec->index, num_colors, color);
}

static inline int led_on_dt(const struct led_dt_spec *spec)
{
        return led_on(spec->dev, spec->index);
}

static inline int led_off_dt(const struct led_dt_spec *spec)
{
        return led_off(spec->dev, spec->index);
}

static inline bool led_is_ready_dt(const struct led_dt_spec *spec)
{
        return device_is_ready(spec->dev);
}

#define LED_DT_SPEC_GET(node_id)                                               \
        {                                                                      \
                .dev = DEVICE_DT_GET(DT_PARENT(node_id)),                      \
                .index = DT_NODE_CHILD_IDX(node_id),                           \
        }

#define LED_DT_SPEC_GET_OR(node_id, default_value)                             \
        COND_CODE_1(DT_NODE_EXISTS(node_id),                                   \
                    (LED_DT_SPEC_GET(node_id)),                                \
                    (default_value))


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/led.h>

#endif  /* ZEPHYR_INCLUDE_DRIVERS_LED_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 392 行

LED 设备树（DT）辅助工具。

### 注释 3：原第 579 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_LED_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [led_info](../hardware/P204_LED信息结构.md)
- [label](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a5d01795e49663654e9fe4a821797956a)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [index](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a7f87ebb0718e1dc189e6d48d5bb97c55)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_colors](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#ab6db05157b960669e3b01154a9621530)
- [color_mapping](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a8daacbe0a68d7ff710938722003fceaf)
- [led_api_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad3c655794f58045459cbd910592d2cdd)
- [device](../device_reference/P002_设备对象结构.md)
- [led_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga3828b1e544a2f64378d5c3bfbbaa0c77)
- [led_api_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gae24caa14f6aa41c2a509d2eaf468463f)
- [led_api_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga977317f3208d5336463edf9979def4ae)
- [led_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad13f55702668133575658d2ccc295339)
- [led_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)
- [led_api_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga66dac12510c3a2281378d532ba6db2ae)
- [led_driver_api](../hardware/P206_LED驱动函数表.md)
- [on](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9ce7322282f8c525256d3c16a514ecc4)
- [off](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a19ad736a130da2aff6bd5b299d8c33a7)
- [set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9c3e3c4d40c4b8219755df6df96b0058)
- [blink](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#af1974c5cc20c818e0e387b34cd14ac3b)
- [get_info](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a7c68219e44bcf6e766e64fd3967ecf7e)
- [set_color](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a336f30f2c1bd3d99213cae66911c142a)
- [write_channels](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#ada1dfb1830b48afb020c7e60dbd92337)
- [led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga9925483b97073354f7be6b40aa2dad1a)
- [led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaca479fd77518331f4fc84f788e345882)
- [LED_BRIGHTNESS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga7bb18ca9f746ebcfbfc397886643f16d)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga24d4007f81483d0fe8b9988288adf59a)
- [led_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga717bdbe76331b6286c58feb6e3e214dd)
- [led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)
- [led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gad4daafd7fcab22d1d68745b7264d0f73)
- [led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga22c9dbe76f06fec327aebe06448d1542)
- [led_dt_spec](../hardware/P203_LED设备树描述结构.md)
- [dev](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#ad92b9ee24cb31fcc0a2352bcf831cecb)
- [index](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#a72c5ff64b89344ca9644fd2b4f4c9515)
- [led_blink_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gab3581c7571b4623696ad57d25d6bd96f)
- [led_get_info_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga01ee05a71058adf86e950805524865a0)
- [led_set_brightness_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaecc33acfc2b1dde870b411d7f30eed82)
- [led_set_color_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4a30a26f21d80f40ce3364880e0dfee3)
- [led_on_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2b262a309e4ede4cb5715c69d900804)
- [led_off_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga8b6618e4fea4f44f218f95fd16abc16b)
- [led_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2994b959c730dad3432481bba278497)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [led_driver_api::off](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a19ad736a130da2aff6bd5b299d8c33a7)
- [led_driver_api::set_color](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a336f30f2c1bd3d99213cae66911c142a)
- [led_driver_api::get_info](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a7c68219e44bcf6e766e64fd3967ecf7e)
- [led_driver_api::set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9c3e3c4d40c4b8219755df6df96b0058)
- [led_driver_api::on](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9ce7322282f8c525256d3c16a514ecc4)
- [led_driver_api::write_channels](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#ada1dfb1830b48afb020c7e60dbd92337)
- [led_driver_api::blink](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#af1974c5cc20c818e0e387b34cd14ac3b)
- [led_dt_spec::index](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#a72c5ff64b89344ca9644fd2b4f4c9515)
- [led_dt_spec::dev](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#ad92b9ee24cb31fcc0a2352bcf831cecb)
- [led_info::label](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a5d01795e49663654e9fe4a821797956a)
- [led_info::index](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a7f87ebb0718e1dc189e6d48d5bb97c55)
- [led_info::color_mapping](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a8daacbe0a68d7ff710938722003fceaf)
- [led_info::num_colors](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#ab6db05157b960669e3b01154a9621530)

---

[上一章](P041_display.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_mipi_dsi.h_源码浏览.md)
