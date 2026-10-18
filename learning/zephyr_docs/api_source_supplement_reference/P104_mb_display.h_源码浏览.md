---
id: learning.zephyr-docs.api-source-supplement-reference.page-104
title: mb_display.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_mb\_display.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h.html)。

## 104.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00037"></a>
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
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="agroup__mb__display_html_ga2a6e20d57d0d65033281dd7c3ea19126"></a>
<a id="agroup__mb__display_html_ga750a177cffbb90ab38392d9ebad9a8eb"></a>
<a id="agroup__mb__display_html_ga94e3eadd1cf386b8d9494ccfa8afaa40"></a>
<a id="agroup__mb__display_html_ga993a6a0225206f53170d25d9177c1225"></a>
<a id="agroup__mb__display_html_gad15b3635993007d8aad9364cbe29311b"></a>
<a id="agroup__mb__display_html_gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a"></a>
<a id="agroup__mb__display_html_gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5"></a>
<a id="agroup__mb__display_html_gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69"></a>
<a id="agroup__mb__display_html_gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdio_8h_html"></a>
<a id="astructmb__image_html"></a>
<a id="astructmb__image_html_a044fee7be7fb1e5b3e2c2dab74011d9a"></a>
<a id="astructmb__image_html_a158f0bdbb7d135da0dcf5c6b997d0ff5"></a>
<a id="astructmb__image_html_a2af8f97c0ddc8cf463cf83a483e3025b"></a>
<a id="astructmb__image_html_a506e5ac82c7229ba7e89f67de8fbcbe2"></a>
<a id="astructmb__image_html_a88455e59017a73533e727671019f6ea0"></a>
<a id="astructmb__image_html_a93ec1bb1c0cdc09de75d00976bd23eeb"></a>
<a id="astructmb__image_html_ad7eb096bb15a0bb8378bae32804fe6c6"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DISPLAY_MB_DISPLAY_H_
#define ZEPHYR_INCLUDE_DISPLAY_MB_DISPLAY_H_


#include <stdio.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

struct mb_image {
        union {
                struct {
                        uint8_t c1:1,
                                c2:1,
                                c3:1,
                                c4:1,
                                c5:1;
                } r[5];
                uint8_t row[5];
        };
};

enum mb_display_mode {
        MB_DISPLAY_MODE_DEFAULT,

        MB_DISPLAY_MODE_SINGLE,

        MB_DISPLAY_MODE_SCROLL,

        /* Display flags, i.e. modifiers to the chosen mode */

        MB_DISPLAY_FLAG_LOOP        = BIT(16),
};

#define MB_IMAGE(_rows...) { .r = { _rows } }

struct mb_display;

struct mb_display *mb_display_get(void);

void mb_display_image(struct mb_display *disp, uint32_t mode, int32_t duration,
                      const struct mb_image *img, uint8_t img_count);

__printf_like(4, 5) void mb_display_print(struct mb_display *disp,
                                          uint32_t mode, int32_t duration,
                                          const char *fmt, ...);

void mb_display_stop(struct mb_display *disp);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DISPLAY_MB_DISPLAY_H_ */
```

## 104.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 65 行

显示标志（Display flags），即对所选模式的修饰项。

### 注释 3：原第 171 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DISPLAY_MB_DISPLAY_H_`。

## 104.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h.html)
- [stdio.h](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [c1](../device_power_control_model_reference/P026_mb_image_结构体.md#a044fee7be7fb1e5b3e2c2dab74011d9a)
- [c2](../device_power_control_model_reference/P026_mb_image_结构体.md#ad7eb096bb15a0bb8378bae32804fe6c6)
- [c3](../device_power_control_model_reference/P026_mb_image_结构体.md#a88455e59017a73533e727671019f6ea0)
- [c4](../device_power_control_model_reference/P026_mb_image_结构体.md#a506e5ac82c7229ba7e89f67de8fbcbe2)
- [c5](../device_power_control_model_reference/P026_mb_image_结构体.md#a2af8f97c0ddc8cf463cf83a483e3025b)
- [r](../device_power_control_model_reference/P026_mb_image_结构体.md#a93ec1bb1c0cdc09de75d00976bd23eeb)
- [row](../device_power_control_model_reference/P026_mb_image_结构体.md#a158f0bdbb7d135da0dcf5c6b997d0ff5)
- [mb_display_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga750a177cffbb90ab38392d9ebad9a8eb)
- [MB_DISPLAY_MODE_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5)
- [MB_DISPLAY_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a)
- [MB_DISPLAY_MODE_SCROLL](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69)
- [MB_DISPLAY_FLAG_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [mb_display_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga94e3eadd1cf386b8d9494ccfa8afaa40)
- [mb_display_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga2a6e20d57d0d65033281dd7c3ea19126)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [mb_display_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga993a6a0225206f53170d25d9177c1225)
- [mb_display_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gad15b3635993007d8aad9364cbe29311b)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mb_image::c1](../device_power_control_model_reference/P026_mb_image_结构体.md#a044fee7be7fb1e5b3e2c2dab74011d9a)
- [mb_image::row](../device_power_control_model_reference/P026_mb_image_结构体.md#a158f0bdbb7d135da0dcf5c6b997d0ff5)
- [mb_image::c5](../device_power_control_model_reference/P026_mb_image_结构体.md#a2af8f97c0ddc8cf463cf83a483e3025b)
- [mb_image::c4](../device_power_control_model_reference/P026_mb_image_结构体.md#a506e5ac82c7229ba7e89f67de8fbcbe2)
- [mb_image::c3](../device_power_control_model_reference/P026_mb_image_结构体.md#a88455e59017a73533e727671019f6ea0)
- [mb_image::r](../device_power_control_model_reference/P026_mb_image_结构体.md#a93ec1bb1c0cdc09de75d00976bd23eeb)
- [mb_image::c2](../device_power_control_model_reference/P026_mb_image_结构体.md#ad7eb096bb15a0bb8378bae32804fe6c6)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P103_max22017.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P105_mchp-xec-dmac.h_源码浏览.md)
