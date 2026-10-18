---
id: learning.zephyr-docs.api-source-reference.page-279
title: ft8xx_copro.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第279章\_ft8xx\_copro.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html)。

## 279.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00054"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ft8xx__copro_html_ga35d0500600e8c1d1df653952fab5d86c"></a>
<a id="agroup__ft8xx__copro_html_ga3605bc23d9555ac51fc6292cb6f2a02c"></a>
<a id="agroup__ft8xx__copro_html_ga3b9454e8a6a824bd87c675037047c069"></a>
<a id="agroup__ft8xx__copro_html_ga72e1feafde7bb230cd798ba23f414de9"></a>
<a id="agroup__ft8xx__copro_html_ga93e61278bacec915bb360244ab43dbb7"></a>
<a id="agroup__ft8xx__copro_html_ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea"></a>
<a id="agroup__ft8xx__copro_html_gab47b9c79db405686168cf1516ea0a00d"></a>
<a id="agroup__ft8xx__copro_html_gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9"></a>
<a id="agroup__ft8xx__copro_html_gac946f044f2fbb6381ea4af268084d828"></a>
<a id="agroup__ft8xx__copro_html_gacc68ff73da90a9c822185f2ceba5a910"></a>
<a id="agroup__ft8xx__copro_html_gafa5c3fe004456cfd531edf781c11c00d"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2020 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COPRO_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COPRO_H_

#include <stdint.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


#define FT8XX_OPT_3D        0
#define FT8XX_OPT_RGB565    0
#define FT8XX_OPT_MONO      1
#define FT8XX_OPT_NODL      2
#define FT8XX_OPT_FLAT      256
#define FT8XX_OPT_SIGNED    256
#define FT8XX_OPT_CENTERX   512
#define FT8XX_OPT_CENTERY   1024
#define FT8XX_OPT_CENTER    1536
#define FT8XX_OPT_RIGHTX    2048
#define FT8XX_OPT_NOBACK    4096
#define FT8XX_OPT_NOTICKS   8192
#define FT8XX_OPT_NOHM      16384
#define FT8XX_OPT_NOPOINTER 16384
#define FT8XX_OPT_NOSECS    32768
#define FT8XX_OPT_NOHANDS   49152

void ft8xx_copro_cmd(const struct device *dev, uint32_t cmd);

void ft8xx_copro_cmd_dlstart(const struct device *dev);

void ft8xx_copro_cmd_swap(const struct device *dev);

void ft8xx_copro_cmd_fgcolor(const struct device *dev, uint32_t color);

void ft8xx_copro_cmd_bgcolor(const struct device *dev, uint32_t color);

void ft8xx_copro_cmd_slider(const struct device *dev,
                            int16_t x,
                            int16_t y,
                            int16_t width,
                            int16_t height,
                            uint16_t options,
                            uint16_t val,
                            uint16_t range);

void ft8xx_copro_cmd_toggle(const struct device *dev,
                            int16_t x,
                            int16_t y,
                            int16_t width,
                            int16_t font,
                            uint16_t options,
                            uint16_t state,
                            const char *string);

void ft8xx_copro_cmd_track(const struct device *dev,
                           int16_t x,
                           int16_t y,
                           int16_t width,
                           int16_t height,
                           int16_t tag);

void ft8xx_copro_cmd_text(const struct device *dev,
                          int16_t x,
                          int16_t y,
                          int16_t font,
                          uint16_t options,
                          const char *string);

void ft8xx_copro_cmd_number(const struct device *dev,
                            int16_t x,
                            int16_t y,
                            int16_t font,
                            uint16_t options,
                            int32_t number);

void ft8xx_copro_cmd_calibrate(const struct device *dev, uint32_t *result);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COPRO_H_ */
```

## 279.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 291 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COPRO_H_`。

## 279.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [ft8xx_copro_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [ft8xx_copro_cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9)
- [ft8xx_copro_cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3605bc23d9555ac51fc6292cb6f2a02c)
- [ft8xx_copro_cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab47b9c79db405686168cf1516ea0a00d)
- [ft8xx_copro_cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gafa5c3fe004456cfd531edf781c11c00d)
- [ft8xx_copro_cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3b9454e8a6a824bd87c675037047c069)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ft8xx_copro_cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga93e61278bacec915bb360244ab43dbb7)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [ft8xx_copro_cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac946f044f2fbb6381ea4af268084d828)
- [ft8xx_copro_cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga35d0500600e8c1d1df653952fab5d86c)
- [ft8xx_copro_cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga72e1feafde7bb230cd798ba23f414de9)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [ft8xx_copro_cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc68ff73da90a9c822185f2ceba5a910)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P278_ft8xx_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P280_ft8xx_dl.h_源码浏览.md)
