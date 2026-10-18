---
id: learning.zephyr-docs.api-source-supplement-reference.page-94
title: types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h.html)。

## 94.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00086"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00116"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00157"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00291"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00347"></a>
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
<a id="l00362"></a>
<a id="l00363"></a>
<a id="agroup__video__types_html_ga0f50f287c4075e992fbab6d8a990d7a8"></a>
<a id="agroup__video__types_html_ga43aa9bdc7283175df8165332a29c3f6c"></a>
<a id="agroup__video__types_html_ga6abf1fc9c35cf1d1648cde7616e7cad1"></a>
<a id="agroup__video__types_html_gad386b2994b56844ebe713f156b9dfe4e"></a>
<a id="agroup__video__types_html_gae375c0586e3505632cc69348935c9b54"></a>
<a id="agroup__video__types_html_gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8"></a>
<a id="agroup__video__types_html_gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8"></a>
<a id="agroup__video__types_html_gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3"></a>
<a id="agroup__video__types_html_gga43aa9bdc7283175df8165332a29c3f6cac00864424ada665a3c88d7fa0c1800c3"></a>
<a id="agroup__video__types_html_gga43aa9bdc7283175df8165332a29c3f6caf2c2b2b000bd4685a429e5ff2c169425"></a>
<a id="agroup__video__types_html_gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4"></a>
<a id="agroup__video__types_html_gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b"></a>
<a id="agroup__video__types_html_ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1"></a>
<a id="agroup__video__types_html_ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083"></a>
<a id="agroup__video__types_html_ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f"></a>
<a id="agroup__video__types_html_ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49"></a>
<a id="agroup__video__types_html_ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20"></a>
<a id="agroup__video__types_html_ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17"></a>
<a id="agroup__video__types_html_ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructdevice_html"></a>
<a id="astructvideo__buffer_html"></a>
<a id="astructvideo__buffer_html_a17505a283ab5ef65047b798cb49aa9e1"></a>
<a id="astructvideo__buffer_html_a3f040775c683c91740c8bda5c96e621b"></a>
<a id="astructvideo__buffer_html_a46dd9bd9398ff74e4f9859a07b9c48af"></a>
<a id="astructvideo__buffer_html_a687f782126d32b36b3b07aaa976a83a4"></a>
<a id="astructvideo__buffer_html_a6a62d7a50c717dc6bc85e2d8f6ae95e3"></a>
<a id="astructvideo__buffer_html_a84550afc674ad543c8c709d55ececda2"></a>
<a id="astructvideo__buffer_html_ab184d528487042650af105eb7d37381e"></a>
<a id="astructvideo__buffer_html_abe25963ea5e42d6fe42de1f21b554b87"></a>
<a id="astructvideo__buffer_html_af5c1abf09e0047334e03afbc64226eba"></a>
<a id="astructvideo__caps_html"></a>
<a id="astructvideo__caps_html_a2b2604a36a2f7a5013d9383ab5ef198a"></a>
<a id="astructvideo__caps_html_a31520f03f621082bbf516efce23ef1f6"></a>
<a id="astructvideo__caps_html_ac82d9f03ecc316c6d9910beac021c5f8"></a>
<a id="astructvideo__caps_html_adb454a88504d9fd6e40510171a53b185"></a>
<a id="astructvideo__control_html"></a>
<a id="astructvideo__control_html_a9068d0a2e351688a9077e607042a4ed3"></a>
<a id="astructvideo__control_html_a9ff5d90ec4ccb2b23dbd84c0eacdad75"></a>
<a id="astructvideo__control_html_ab0504077a3dcc37f5781a54baeb1e65f"></a>
<a id="astructvideo__ctrl__query_html"></a>
<a id="astructvideo__ctrl__query_html_a0b2744becc777f7465fd9981c9e639f6"></a>
<a id="astructvideo__ctrl__query_html_a37ac4deb89a9d5e4b30ff9293301feb5"></a>
<a id="astructvideo__ctrl__query_html_a56323de13c279c678ffcddc2ea355eea"></a>
<a id="astructvideo__ctrl__query_html_a5a9cc00ce51abb9e3748100dc5d9403e"></a>
<a id="astructvideo__ctrl__query_html_a9444f2b8c981e61ec1b01a498b3d5506"></a>
<a id="astructvideo__ctrl__query_html_aa534262295f6bf6816222d32f2b0986a"></a>
<a id="astructvideo__ctrl__query_html_ad0d74a650e83dece50ca2d46d9e5c750"></a>
<a id="astructvideo__ctrl__query_html_afc3e9b8a15e2d4eb04b17e0f7cd6a8cb"></a>
<a id="astructvideo__ctrl__range_html"></a>
<a id="astructvideo__ctrl__range_html_a0814e901d0edfcfa8be5419eb5bf063e"></a>
<a id="astructvideo__ctrl__range_html_a25e816ab3403881ea1b0db70fbe736f1"></a>
<a id="astructvideo__ctrl__range_html_a3c2108ece802872716abf1672ccde5fa"></a>
<a id="astructvideo__ctrl__range_html_a7acb36bff57836f7bffd3ccbb2e4691e"></a>
<a id="astructvideo__ctrl__range_html_a9912a5060e6615388b5c8f013eaa3c51"></a>
<a id="astructvideo__ctrl__range_html_a9f339e7fce8f61b939d68421169a7030"></a>
<a id="astructvideo__ctrl__range_html_ab1ca560d28446134189cd7d585bd146a"></a>
<a id="astructvideo__ctrl__range_html_ac41aad65e524036c1f01f164726dc209"></a>
<a id="astructvideo__format__cap_html"></a>
<a id="astructvideo__format__cap_html_a512907acd398e053d48d26aab611772e"></a>
<a id="astructvideo__format__cap_html_a539b75ac7b1eadc8c9ee9395b5b2fba9"></a>
<a id="astructvideo__format__cap_html_ab45cdeb28d93d670f06caca449fccd66"></a>
<a id="astructvideo__format__cap_html_ab86710dfc4da3b5d0f9dd5017f971aad"></a>
<a id="astructvideo__format__cap_html_ae5f4de43c4fdaa6bc7085042ec67cd5f"></a>
<a id="astructvideo__format__cap_html_ae6f82b60ad822a37a3c97a71892d8d35"></a>
<a id="astructvideo__format__cap_html_af5beb952295592dc9dc235a4151b2f59"></a>
<a id="astructvideo__format_html"></a>
<a id="astructvideo__format_html_a0e71fa7a0abd7740d5245021ba1acbb0"></a>
<a id="astructvideo__format_html_a233841606bfe82626f94906bf47f5f87"></a>
<a id="astructvideo__format_html_a42a2dfacc89f692c36c448b3ea297a90"></a>
<a id="astructvideo__format_html_a7b0cc009ac03437e7e3e86b45545b693"></a>
<a id="astructvideo__format_html_aa4cd70933938ec6f52175232cf403ef6"></a>
<a id="astructvideo__format_html_adb8bf2c8d59125c050cdfe160c30f5ef"></a>
<a id="astructvideo__frmival__enum_html"></a>
<a id="astructvideo__frmival__enum_html_a7654ce36fd942885b193da57579d88ed"></a>
<a id="astructvideo__frmival__enum_html_a8c103777cd5db24a2197ef994b8d008d"></a>
<a id="astructvideo__frmival__enum_html_aa3fda4e99646bff1d902198437982124"></a>
<a id="astructvideo__frmival__enum_html_aec62b54ed1152d6b3ea80c24ce7624f7"></a>
<a id="astructvideo__frmival__enum_html_af22ef303cdc75fd48b698ff72b57354c"></a>
<a id="astructvideo__frmival__stepwise_html"></a>
<a id="astructvideo__frmival__stepwise_html_aec892104241a9d4204c87af51765ee2f"></a>
<a id="astructvideo__frmival__stepwise_html_af1c5a40da9fe7ad30185464eccf5b438"></a>
<a id="astructvideo__frmival__stepwise_html_afc3c4e4fe3641952c4e6fc494fa85760"></a>
<a id="astructvideo__frmival_html"></a>
<a id="astructvideo__frmival_html_a57ee282f01da0f1ef1db2558d777631c"></a>
<a id="astructvideo__frmival_html_aba4a6700ea733c3b07ee6445856c580a"></a>
<a id="astructvideo__rect_html"></a>
<a id="astructvideo__rect_html_a26403179cc6d65ff6c07a4b31b1a5050"></a>
<a id="astructvideo__rect_html_a57d79483c9fc9bd800437160bd30664d"></a>
<a id="astructvideo__rect_html_a769fd3843bcb11211eccdd766d09d83a"></a>
<a id="astructvideo__rect_html_a94da5de0a4cc682556acd00fc05a8ea5"></a>
<a id="astructvideo__selection_html"></a>
<a id="astructvideo__selection_html_a2e634792c0758a3dd576e4871c250bd2"></a>
<a id="astructvideo__selection_html_aec9dd0ae07f995f490ebdd86d48c1a63"></a>
<a id="astructvideo__selection_html_afe358118a1d3c373888674f331dd05f1"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 * Copyright 2025 NXP
 * Copyright (c) 2025 STMicroelectronics
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_VIDEO_TYPES_H
#define ZEPHYR_INCLUDE_VIDEO_TYPES_H


#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

enum video_buf_type {
        VIDEO_BUF_TYPE_INPUT = 1,
        VIDEO_BUF_TYPE_OUTPUT = 2,
};

enum video_buf_memory {
        VIDEO_MEMORY_INTERNAL = 1,
        VIDEO_MEMORY_EXTERNAL = 2,
};

struct video_buffer {
        /* It must be kept as first field of the struct if used for @ref k_fifo APIs. */
        void *driver_data;
        enum video_buf_type type;
        uint8_t memory;
        uint8_t *buffer;
        uint16_t index;
        uint32_t size;
        uint32_t bytesused;
        uint32_t timestamp;
        uint16_t line_offset;
};

struct video_format {
        enum video_buf_type type;
        uint32_t pixelformat;
        uint32_t width;
        uint32_t height;
        uint32_t pitch;
        uint32_t size;
};

struct video_format_cap {
        uint32_t pixelformat;
        uint32_t width_min;
        uint32_t width_max;
        uint32_t height_min;
        uint32_t height_max;
        uint16_t width_step;
        uint16_t height_step;
};

struct video_caps {
        enum video_buf_type type;
        const struct video_format_cap *format_caps;
        uint8_t min_vbuf_count;
        size_t buf_align;
};

struct video_ctrl_range {
        union {
                int32_t min;
                int64_t min64;
        };
        union {
                int32_t max;
                int64_t max64;
        };
        union {
                int32_t step;
                int64_t step64;
        };
        union {
                int32_t def;
                int64_t def64;
        };
};

struct video_control {
        uint32_t id;
        union {
                int32_t val;
                int64_t val64;
        };
};

struct video_ctrl_query {
        const struct device *dev;
        uint32_t id;
        uint32_t type;
        const char *name;
        uint32_t flags;
        struct video_ctrl_range range;
        union {
                const char *const *menu;
                const int64_t *int_menu;
        };
};

enum video_signal_result {
        VIDEO_BUF_DONE,
        VIDEO_BUF_ABORTED,
        VIDEO_BUF_ERROR,
};

enum video_selection_target {
        VIDEO_SEL_TGT_CROP,
        VIDEO_SEL_TGT_CROP_BOUND,
        VIDEO_SEL_TGT_NATIVE_SIZE,
        VIDEO_SEL_TGT_COMPOSE,
        VIDEO_SEL_TGT_COMPOSE_BOUND,
};

struct video_rect {
        uint32_t left;
        uint32_t top;
        uint32_t width;
        uint32_t height;
};

struct video_selection {
        enum video_buf_type type;
        enum video_selection_target target;
        struct video_rect rect;
};

enum video_frmival_type {
        VIDEO_FRMIVAL_TYPE_DISCRETE = 1,
        VIDEO_FRMIVAL_TYPE_STEPWISE = 2,
};

struct video_frmival {
        uint32_t numerator;
        uint32_t denominator;
};

struct video_frmival_stepwise {
        struct video_frmival min;
        struct video_frmival max;
        struct video_frmival step;
};

struct video_frmival_enum {
        uint32_t index;
        const struct video_format *format;
        enum video_frmival_type type;
        union {
                struct video_frmival discrete;
                struct video_frmival_stepwise stepwise;
        };
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_VIDEO_TYPES_H */
```

## 94.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

版权（Copyright）：2025 NXP。

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 68 行

如果用于 `k_fifo` API，必须将其保持为结构体的第一个字段。

### 注释 3：原第 363 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_VIDEO_TYPES_H`。

## 94.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [VIDEO_BUF_TYPE_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1)
- [VIDEO_BUF_TYPE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083)
- [video_buf_memory](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga43aa9bdc7283175df8165332a29c3f6c)
- [VIDEO_MEMORY_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga43aa9bdc7283175df8165332a29c3f6cac00864424ada665a3c88d7fa0c1800c3)
- [VIDEO_MEMORY_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga43aa9bdc7283175df8165332a29c3f6caf2c2b2b000bd4685a429e5ff2c169425)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [driver_data](../audio_video_model_reference/P051_video_buffer_结构体.md#ab184d528487042650af105eb7d37381e)
- [type](../audio_video_model_reference/P051_video_buffer_结构体.md#a46dd9bd9398ff74e4f9859a07b9c48af)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [memory](../audio_video_model_reference/P051_video_buffer_结构体.md#a687f782126d32b36b3b07aaa976a83a4)
- [buffer](../audio_video_model_reference/P051_video_buffer_结构体.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [index](../audio_video_model_reference/P051_video_buffer_结构体.md#a84550afc674ad543c8c709d55ececda2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [size](../audio_video_model_reference/P051_video_buffer_结构体.md#a3f040775c683c91740c8bda5c96e621b)
- [bytesused](../audio_video_model_reference/P051_video_buffer_结构体.md#a17505a283ab5ef65047b798cb49aa9e1)
- [timestamp](../audio_video_model_reference/P051_video_buffer_结构体.md#af5c1abf09e0047334e03afbc64226eba)
- [line_offset](../audio_video_model_reference/P051_video_buffer_结构体.md#abe25963ea5e42d6fe42de1f21b554b87)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [type](../audio_video_model_reference/P059_video_format_结构体.md#a233841606bfe82626f94906bf47f5f87)
- [pixelformat](../audio_video_model_reference/P059_video_format_结构体.md#adb8bf2c8d59125c050cdfe160c30f5ef)
- [width](../audio_video_model_reference/P059_video_format_结构体.md#a7b0cc009ac03437e7e3e86b45545b693)
- [height](../audio_video_model_reference/P059_video_format_结构体.md#a0e71fa7a0abd7740d5245021ba1acbb0)
- [pitch](../audio_video_model_reference/P059_video_format_结构体.md#aa4cd70933938ec6f52175232cf403ef6)
- [size](../audio_video_model_reference/P059_video_format_结构体.md#a42a2dfacc89f692c36c448b3ea297a90)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [pixelformat](../audio_video_model_reference/P060_video_format_cap_结构体.md#af5beb952295592dc9dc235a4151b2f59)
- [width_min](../audio_video_model_reference/P060_video_format_cap_结构体.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)
- [width_max](../audio_video_model_reference/P060_video_format_cap_结构体.md#ab45cdeb28d93d670f06caca449fccd66)
- [height_min](../audio_video_model_reference/P060_video_format_cap_结构体.md#ae6f82b60ad822a37a3c97a71892d8d35)
- [height_max](../audio_video_model_reference/P060_video_format_cap_结构体.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)
- [width_step](../audio_video_model_reference/P060_video_format_cap_结构体.md#ab86710dfc4da3b5d0f9dd5017f971aad)
- [height_step](../audio_video_model_reference/P060_video_format_cap_结构体.md#a512907acd398e053d48d26aab611772e)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [type](../audio_video_model_reference/P052_video_caps_结构体.md#a31520f03f621082bbf516efce23ef1f6)
- [format_caps](../audio_video_model_reference/P052_video_caps_结构体.md#adb454a88504d9fd6e40510171a53b185)
- [min_vbuf_count](../audio_video_model_reference/P052_video_caps_结构体.md#a2b2604a36a2f7a5013d9383ab5ef198a)
- [buf_align](../audio_video_model_reference/P052_video_caps_结构体.md#ac82d9f03ecc316c6d9910beac021c5f8)
- [video_ctrl_range](../audio_video_model_reference/P056_video_ctrl_range_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [min](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a0814e901d0edfcfa8be5419eb5bf063e)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [min64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a25e816ab3403881ea1b0db70fbe736f1)
- [max](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a3c2108ece802872716abf1672ccde5fa)
- [max64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a7acb36bff57836f7bffd3ccbb2e4691e)
- [step](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#ab1ca560d28446134189cd7d585bd146a)
- [step64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a9912a5060e6615388b5c8f013eaa3c51)
- [def](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#ac41aad65e524036c1f01f164726dc209)
- [def64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a9f339e7fce8f61b939d68421169a7030)
- [video_control](../audio_video_model_reference/P053_video_control_结构体.md)
- [id](../audio_video_model_reference/P053_video_control_结构体.md#a9ff5d90ec4ccb2b23dbd84c0eacdad75)
- [val](../audio_video_model_reference/P053_video_control_结构体.md#a9068d0a2e351688a9077e607042a4ed3)
- [val64](../audio_video_model_reference/P053_video_control_结构体.md#ab0504077a3dcc37f5781a54baeb1e65f)
- [video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#aa534262295f6bf6816222d32f2b0986a)
- [id](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a9444f2b8c981e61ec1b01a498b3d5506)
- [type](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a5a9cc00ce51abb9e3748100dc5d9403e)
- [name](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a0b2744becc777f7465fd9981c9e639f6)
- [flags](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb)
- [range](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a37ac4deb89a9d5e4b30ff9293301feb5)
- [menu](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a56323de13c279c678ffcddc2ea355eea)
- [int_menu](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#ad0d74a650e83dece50ca2d46d9e5c750)
- [video_signal_result](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga0f50f287c4075e992fbab6d8a990d7a8)
- [VIDEO_BUF_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)
- [VIDEO_BUF_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)
- [VIDEO_BUF_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)
- [video_selection_target](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gae375c0586e3505632cc69348935c9b54)
- [VIDEO_SEL_TGT_CROP](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17)
- [VIDEO_SEL_TGT_CROP_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1)
- [VIDEO_SEL_TGT_NATIVE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20)
- [VIDEO_SEL_TGT_COMPOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49)
- [VIDEO_SEL_TGT_COMPOSE_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f)
- [video_rect](../audio_video_model_reference/P064_video_rect_结构体.md)
- [left](../audio_video_model_reference/P064_video_rect_结构体.md#a94da5de0a4cc682556acd00fc05a8ea5)
- [top](../audio_video_model_reference/P064_video_rect_结构体.md#a769fd3843bcb11211eccdd766d09d83a)
- [width](../audio_video_model_reference/P064_video_rect_结构体.md#a26403179cc6d65ff6c07a4b31b1a5050)
- [height](../audio_video_model_reference/P064_video_rect_结构体.md#a57d79483c9fc9bd800437160bd30664d)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [type](../audio_video_model_reference/P065_video_selection_结构体.md#aec9dd0ae07f995f490ebdd86d48c1a63)
- [target](../audio_video_model_reference/P065_video_selection_结构体.md#afe358118a1d3c373888674f331dd05f1)
- [rect](../audio_video_model_reference/P065_video_selection_结构体.md#a2e634792c0758a3dd576e4871c250bd2)
- [video_frmival_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga6abf1fc9c35cf1d1648cde7616e7cad1)
- [VIDEO_FRMIVAL_TYPE_DISCRETE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4)
- [VIDEO_FRMIVAL_TYPE_STEPWISE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [numerator](../audio_video_model_reference/P061_video_frmival_结构体.md#a57ee282f01da0f1ef1db2558d777631c)
- [denominator](../audio_video_model_reference/P061_video_frmival_结构体.md#aba4a6700ea733c3b07ee6445856c580a)
- [video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)
- [min](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#aec892104241a9d4204c87af51765ee2f)
- [max](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#af1c5a40da9fe7ad30185464eccf5b438)
- [step](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#afc3c4e4fe3641952c4e6fc494fa85760)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [index](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#a7654ce36fd942885b193da57579d88ed)
- [format](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#a8c103777cd5db24a2197ef994b8d008d)
- [type](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#aec62b54ed1152d6b3ea80c24ce7624f7)
- [discrete](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#af22ef303cdc75fd48b698ff72b57354c)
- [stepwise](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#aa3fda4e99646bff1d902198437982124)
- [video_buffer::bytesused](../audio_video_model_reference/P051_video_buffer_结构体.md#a17505a283ab5ef65047b798cb49aa9e1)
- [video_buffer::size](../audio_video_model_reference/P051_video_buffer_结构体.md#a3f040775c683c91740c8bda5c96e621b)
- [video_buffer::type](../audio_video_model_reference/P051_video_buffer_结构体.md#a46dd9bd9398ff74e4f9859a07b9c48af)
- [video_buffer::memory](../audio_video_model_reference/P051_video_buffer_结构体.md#a687f782126d32b36b3b07aaa976a83a4)
- [video_buffer::buffer](../audio_video_model_reference/P051_video_buffer_结构体.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)
- [video_buffer::index](../audio_video_model_reference/P051_video_buffer_结构体.md#a84550afc674ad543c8c709d55ececda2)
- [video_buffer::driver_data](../audio_video_model_reference/P051_video_buffer_结构体.md#ab184d528487042650af105eb7d37381e)
- [video_buffer::line_offset](../audio_video_model_reference/P051_video_buffer_结构体.md#abe25963ea5e42d6fe42de1f21b554b87)
- [video_buffer::timestamp](../audio_video_model_reference/P051_video_buffer_结构体.md#af5c1abf09e0047334e03afbc64226eba)
- [video_caps::min_vbuf_count](../audio_video_model_reference/P052_video_caps_结构体.md#a2b2604a36a2f7a5013d9383ab5ef198a)
- [video_caps::type](../audio_video_model_reference/P052_video_caps_结构体.md#a31520f03f621082bbf516efce23ef1f6)
- [video_caps::buf_align](../audio_video_model_reference/P052_video_caps_结构体.md#ac82d9f03ecc316c6d9910beac021c5f8)
- [video_caps::format_caps](../audio_video_model_reference/P052_video_caps_结构体.md#adb454a88504d9fd6e40510171a53b185)
- [video_control::val](../audio_video_model_reference/P053_video_control_结构体.md#a9068d0a2e351688a9077e607042a4ed3)
- [video_control::id](../audio_video_model_reference/P053_video_control_结构体.md#a9ff5d90ec4ccb2b23dbd84c0eacdad75)
- [video_control::val64](../audio_video_model_reference/P053_video_control_结构体.md#ab0504077a3dcc37f5781a54baeb1e65f)
- [video_ctrl_query::name](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a0b2744becc777f7465fd9981c9e639f6)
- [video_ctrl_query::range](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a37ac4deb89a9d5e4b30ff9293301feb5)
- [video_ctrl_query::menu](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a56323de13c279c678ffcddc2ea355eea)
- [video_ctrl_query::type](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a5a9cc00ce51abb9e3748100dc5d9403e)
- [video_ctrl_query::id](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#a9444f2b8c981e61ec1b01a498b3d5506)
- [video_ctrl_query::dev](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#aa534262295f6bf6816222d32f2b0986a)
- [video_ctrl_query::int_menu](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#ad0d74a650e83dece50ca2d46d9e5c750)
- [video_ctrl_query::flags](../audio_video_model_reference/P055_video_ctrl_query_结构体.md#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb)
- [video_ctrl_range::min](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a0814e901d0edfcfa8be5419eb5bf063e)
- [video_ctrl_range::min64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a25e816ab3403881ea1b0db70fbe736f1)
- [video_ctrl_range::max](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a3c2108ece802872716abf1672ccde5fa)
- [video_ctrl_range::max64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a7acb36bff57836f7bffd3ccbb2e4691e)
- [video_ctrl_range::step64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a9912a5060e6615388b5c8f013eaa3c51)
- [video_ctrl_range::def64](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#a9f339e7fce8f61b939d68421169a7030)
- [video_ctrl_range::step](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#ab1ca560d28446134189cd7d585bd146a)
- [video_ctrl_range::def](../audio_video_model_reference/P056_video_ctrl_range_结构体.md#ac41aad65e524036c1f01f164726dc209)
- [video_format_cap::height_step](../audio_video_model_reference/P060_video_format_cap_结构体.md#a512907acd398e053d48d26aab611772e)
- [video_format_cap::width_min](../audio_video_model_reference/P060_video_format_cap_结构体.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)
- [video_format_cap::width_max](../audio_video_model_reference/P060_video_format_cap_结构体.md#ab45cdeb28d93d670f06caca449fccd66)
- [video_format_cap::width_step](../audio_video_model_reference/P060_video_format_cap_结构体.md#ab86710dfc4da3b5d0f9dd5017f971aad)
- [video_format_cap::height_max](../audio_video_model_reference/P060_video_format_cap_结构体.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)
- [video_format_cap::height_min](../audio_video_model_reference/P060_video_format_cap_结构体.md#ae6f82b60ad822a37a3c97a71892d8d35)
- [video_format_cap::pixelformat](../audio_video_model_reference/P060_video_format_cap_结构体.md#af5beb952295592dc9dc235a4151b2f59)
- [video_format::height](../audio_video_model_reference/P059_video_format_结构体.md#a0e71fa7a0abd7740d5245021ba1acbb0)
- [video_format::type](../audio_video_model_reference/P059_video_format_结构体.md#a233841606bfe82626f94906bf47f5f87)
- [video_format::size](../audio_video_model_reference/P059_video_format_结构体.md#a42a2dfacc89f692c36c448b3ea297a90)
- [video_format::width](../audio_video_model_reference/P059_video_format_结构体.md#a7b0cc009ac03437e7e3e86b45545b693)
- [video_format::pitch](../audio_video_model_reference/P059_video_format_结构体.md#aa4cd70933938ec6f52175232cf403ef6)
- [video_format::pixelformat](../audio_video_model_reference/P059_video_format_结构体.md#adb8bf2c8d59125c050cdfe160c30f5ef)
- [video_frmival_enum::index](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#a7654ce36fd942885b193da57579d88ed)
- [video_frmival_enum::format](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#a8c103777cd5db24a2197ef994b8d008d)
- [video_frmival_enum::stepwise](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#aa3fda4e99646bff1d902198437982124)
- [video_frmival_enum::type](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#aec62b54ed1152d6b3ea80c24ce7624f7)
- [video_frmival_enum::discrete](../audio_video_model_reference/P062_video_frmival_enum_结构体.md#af22ef303cdc75fd48b698ff72b57354c)
- [video_frmival_stepwise::min](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#aec892104241a9d4204c87af51765ee2f)
- [video_frmival_stepwise::max](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#af1c5a40da9fe7ad30185464eccf5b438)
- [video_frmival_stepwise::step](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md#afc3c4e4fe3641952c4e6fc494fa85760)
- [video_frmival::numerator](../audio_video_model_reference/P061_video_frmival_结构体.md#a57ee282f01da0f1ef1db2558d777631c)
- [video_frmival::denominator](../audio_video_model_reference/P061_video_frmival_结构体.md#aba4a6700ea733c3b07ee6445856c580a)
- [video_rect::width](../audio_video_model_reference/P064_video_rect_结构体.md#a26403179cc6d65ff6c07a4b31b1a5050)
- [video_rect::height](../audio_video_model_reference/P064_video_rect_结构体.md#a57d79483c9fc9bd800437160bd30664d)
- [video_rect::top](../audio_video_model_reference/P064_video_rect_结构体.md#a769fd3843bcb11211eccdd766d09d83a)
- [video_rect::left](../audio_video_model_reference/P064_video_rect_结构体.md#a94da5de0a4cc682556acd00fc05a8ea5)
- [video_selection::rect](../audio_video_model_reference/P065_video_selection_结构体.md#a2e634792c0758a3dd576e4871c250bd2)
- [video_selection::type](../audio_video_model_reference/P065_video_selection_结构体.md#aec9dd0ae07f995f490ebdd86d48c1a63)
- [video_selection::target](../audio_video_model_reference/P065_video_selection_结构体.md#afe358118a1d3c373888674f331dd05f1)

---

[上一章](P093_time.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P095_intc_infineon_aurix.h_源码浏览.md)
