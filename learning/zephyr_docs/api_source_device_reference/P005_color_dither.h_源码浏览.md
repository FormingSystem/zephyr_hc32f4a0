---
id: learning.zephyr-docs.api-source-device-reference.page-5
title: color_dither.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_color\_dither.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h.html)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
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
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00192"></a>
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
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00232"></a>
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
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
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
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="adrivers_2display_8h_html"></a>
<a id="agroup__display__color__dither_html_ga38578e4fd14280d9e623172b2bfabd15"></a>
<a id="agroup__display__color__dither_html_ga79ff5454e68af2c1bb5eedf25904dca2"></a>
<a id="agroup__display__color__dither_html_gaad0ed338c68320c61543c2986e3f7a0a"></a>
<a id="agroup__display__color__dither_html_gab765e6926c9f1f1f693c5016bce04efc"></a>
<a id="agroup__display__interface_html_gac346bc56771052a8fe919c3ec23d7c9c"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>
<a id="astructdisplay__buffer__descriptor_html"></a>
<a id="astructdisplay__capabilities_html"></a>
<a id="astructdisplay__color__dither__state_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DISPLAY_COLOR_DITHER_H_
#define ZEPHYR_INCLUDE_DRIVERS_DISPLAY_COLOR_DITHER_H_


#include <zephyr/drivers/display.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

struct display_color_dither_rgb_error {
        int16_t r;
        int16_t g;
        int16_t b;
};

#if defined(CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888)
#define COLOR_DITHER_DEFAULT_FMT PIXEL_FORMAT_RGB_888
#elif defined(CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565)
#define COLOR_DITHER_DEFAULT_FMT PIXEL_FORMAT_RGB_565
#else
#define COLOR_DITHER_DEFAULT_FMT PIXEL_FORMAT_I_4
#endif

#define COLOR_DITHER_I4_BYTES(w, h) (DIV_ROUND_UP((w), 2U) * (h))

/*
 * Per-instance row buffers for the error-diffusion algorithms only.
 */
#if defined(CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON)
#define COLOR_DITHER_ERRDIFF_NROWS 3
#elif defined(CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG)
#define COLOR_DITHER_ERRDIFF_NROWS 2
#else
#define COLOR_DITHER_ERRDIFF_NROWS 0
#endif

#if COLOR_DITHER_ERRDIFF_NROWS > 0
#define COLOR_DITHER_ERRDIFF_LEN(w)   ((w) + 2U)
#define COLOR_DITHER_ERRDIFF_ROW(tag) color_dither_errdiff_row_##tag

#define COLOR_DITHER_ERRDIFF_DEFINE(tag, w)                                                        \
        static struct display_color_dither_rgb_error COLOR_DITHER_ERRDIFF_ROW(                     \
                tag)[COLOR_DITHER_ERRDIFF_NROWS][COLOR_DITHER_ERRDIFF_LEN(w)]
#define COLOR_DITHER_ERRDIFF_R0(tag) COLOR_DITHER_ERRDIFF_ROW(tag)[0]
#define COLOR_DITHER_ERRDIFF_R1(tag) COLOR_DITHER_ERRDIFF_ROW(tag)[1]
#if COLOR_DITHER_ERRDIFF_NROWS >= 3
#define COLOR_DITHER_ERRDIFF_R2(tag) COLOR_DITHER_ERRDIFF_ROW(tag)[2]
#else
#define COLOR_DITHER_ERRDIFF_R2(tag) NULL
#endif

#else /* no error-diffusion algorithm selected */
#define COLOR_DITHER_ERRDIFF_DEFINE(tag, w)
#define COLOR_DITHER_ERRDIFF_LEN(w)  0U
#define COLOR_DITHER_ERRDIFF_R0(tag) NULL
#define COLOR_DITHER_ERRDIFF_R1(tag) NULL
#define COLOR_DITHER_ERRDIFF_R2(tag) NULL
#endif


struct display_color_dither_state {
#if defined(CONFIG_DISPLAY_COLOR_DITHER)
        enum display_pixel_format input_format;
        uint8_t *converted_buf;
        size_t converted_buf_size;
        struct display_color_dither_rgb_error *err_rows[3];
        size_t err_row_len;
#elif defined(CONFIG_CPP)
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t c;
#endif /* CONFIG_DISPLAY_COLOR_DITHER */
};

#if defined(CONFIG_DISPLAY_COLOR_DITHER) || defined(__DOXYGEN__)

#define DISPLAY_COLOR_DITHER_DEFINE(inst)                                                          \
        static uint8_t color_dither_buf_##inst[COLOR_DITHER_I4_BYTES(DT_INST_PROP(inst, width),    \
                                                                     DT_INST_PROP(inst, height))]; \
        COLOR_DITHER_ERRDIFF_DEFINE(inst, DT_INST_PROP(inst, width))

#define DISPLAY_COLOR_DITHER_INIT(inst)                                                            \
        {                                                                                          \
                .input_format = COLOR_DITHER_DEFAULT_FMT,                                          \
                .converted_buf = color_dither_buf_##inst,                                          \
                .converted_buf_size = sizeof(color_dither_buf_##inst),                             \
                .err_rows =                                                                        \
                        {                                                                          \
                                COLOR_DITHER_ERRDIFF_R0(inst),                                     \
                                COLOR_DITHER_ERRDIFF_R1(inst),                                     \
                                COLOR_DITHER_ERRDIFF_R2(inst),                                     \
                        },                                                                         \
                .err_row_len = COLOR_DITHER_ERRDIFF_LEN(DT_INST_PROP(inst, width)),                \
        }

int display_color_dither_prepare(const struct device *dev, struct display_color_dither_state *state,
                                 const struct display_buffer_descriptor **desc, const void **buf,
                                 struct display_buffer_descriptor *scratch);

void display_color_dither_patch_caps(struct display_color_dither_state *state,
                                     struct display_capabilities *caps);

int display_color_dither_set_input_format(struct display_color_dither_state *state,
                                          enum display_pixel_format pf);

bool display_color_dither_is_active(const struct display_color_dither_state *state,
                                    enum display_pixel_format current_pixel_format);

#else /* !CONFIG_DISPLAY_COLOR_DITHER */


#define DISPLAY_COLOR_DITHER_DEFINE(inst)
#define DISPLAY_COLOR_DITHER_INIT(inst)                                                            \
        {                                                                                          \
        }

static inline int display_color_dither_prepare(const struct device *dev,
                                               struct display_color_dither_state *state,
                                               const struct display_buffer_descriptor **desc,
                                               const void **buf,
                                               struct display_buffer_descriptor *scratch)
{
        (void)dev;
        (void)state;
        (void)desc;
        (void)buf;
        (void)scratch;

        return 0;
}

static inline void display_color_dither_patch_caps(struct display_color_dither_state *state,
                                                   struct display_capabilities *caps)
{
        (void)state;
        (void)caps;
}

static inline int display_color_dither_set_input_format(struct display_color_dither_state *state,
                                                        enum display_pixel_format pf)
{
        (void)state;

        return pf == PIXEL_FORMAT_I_4 ? 0 : -ENOTSUP;
}

static inline bool display_color_dither_is_active(const struct display_color_dither_state *state,
                                                  enum display_pixel_format current_pixel_format)
{
        (void)state;
        (void)current_pixel_format;

        return false;
}


#endif /* CONFIG_DISPLAY_COLOR_DITHER */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_DISPLAY_COLOR_DITHER_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors SPDX-License-Identifier: Apache-2.0.

### 注释 2：原第 125 行

每个实例的行缓冲区（Per-Instance Row Buffers），仅供误差扩散算法（Error-Diffusion Algorithms）使用。

### 注释 3：原第 151 行

未选择误差扩散算法（Error-Diffusion Algorithm）。

### 注释 4：原第 196 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 5：原第 200 行

条件编译配置（Configuration）标记：`CONFIG_DISPLAY_COLOR_DITHER`。

### 注释 6：原第 331 行

条件编译（Conditional Compilation）：`!CONFIG_DISPLAY_COLOR_DITHER`。

### 注释 7：原第 381 行

条件编译配置（Configuration）标记：`CONFIG_DISPLAY_COLOR_DITHER`。

### 注释 8：原第 391 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DISPLAY_COLOR_DITHER_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h.html)
- [zephyr/drivers/display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [display_color_dither_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gab765e6926c9f1f1f693c5016bce04efc)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [display_color_dither_patch_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gaad0ed338c68320c61543c2986e3f7a0a)
- [display_capabilities](../hardware/P216_显示能力结构.md)
- [display_color_dither_set_input_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga38578e4fd14280d9e623172b2bfabd15)
- [display_color_dither_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga79ff5454e68af2c1bb5eedf25904dca2)
- [PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P004_coap_service.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_demand_paging.h_源码浏览.md)
