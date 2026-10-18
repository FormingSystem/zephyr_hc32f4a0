---
id: learning.zephyr-docs.api-source-reference.page-552
title: mpipe_message.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第552章\_mpipe\_message.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)。

## 552.1\_原始可见代码（Source Code）

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
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="agroup__mpipe__message_html_ga2cbfffc03b1b703e80f73c70207cf049"></a>
<a id="agroup__mpipe__message_html_ga371e6503fe08971ce1a2606d0a034b41"></a>
<a id="agroup__mpipe__message_html_ga686a716e86c28adfbb11dc0c1e172c22"></a>
<a id="agroup__mpipe__message_html_gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc"></a>
<a id="agroup__mpipe__message_html_gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c"></a>
<a id="agroup__mpipe__message_html_gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__message_html"></a>
<a id="astructmpipe__message_html_a05db95499949220a3009d837a897bb9d"></a>
<a id="astructmpipe__message_html_a45622118757cf3df3271380752700b42"></a>
<a id="astructmpipe__message_html_a8559ee9f5039c992ed46636e3d953c49"></a>
<a id="astructmpipe__message_html_abb655d25f900b38c77164962970a493f"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_MESSAGE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_MESSAGE_H_


#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/sys/util_macro.h>

#include <zephyr/mpipe/mpipe_element.h>

enum mpipe_message_type {
        MPIPE_MESSAGE_UNKNOWN = 0,
        MPIPE_MESSAGE_EOS = BIT(0),
        MPIPE_MESSAGE_ERROR = BIT(1),
};

#define MPIPE_MESSAGE_ANY UINT32_MAX

enum mpipe_error_domain {
        MPIPE_ERROR_FAILED = 0,
        MPIPE_ERROR_CAPS,
        MPIPE_ERROR_BUFFER_POOL,
        MPIPE_ERROR_FLOW,
        MPIPE_ERROR_RESOURCE,
        MPIPE_ERROR_DOMAIN_END,
};

struct mpipe_message {
        struct mpipe_element *origin;
        uint32_t type;
        int32_t code;
        uint8_t domain;
};

int mpipe_message_post(const struct mpipe_message *message);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_MESSAGE_H_ */
```

## 552.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 166 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_MESSAGE_H_`。

## 552.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga2cbfffc03b1b703e80f73c70207cf049)
- [MPIPE_MESSAGE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f)
- [MPIPE_MESSAGE_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MPIPE_MESSAGE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc)
- [mpipe_error_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga686a716e86c28adfbb11dc0c1e172c22)
- [MPIPE_ERROR_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3)
- [MPIPE_ERROR_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121)
- [MPIPE_ERROR_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba)
- [MPIPE_ERROR_FLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79)
- [MPIPE_ERROR_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6)
- [MPIPE_ERROR_DOMAIN_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a)
- [mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [origin](../audio_video_model_reference/P023_mpipe_message_结构体.md#abb655d25f900b38c77164962970a493f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [type](../audio_video_model_reference/P023_mpipe_message_结构体.md#a45622118757cf3df3271380752700b42)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [code](../audio_video_model_reference/P023_mpipe_message_结构体.md#a8559ee9f5039c992ed46636e3d953c49)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [domain](../audio_video_model_reference/P023_mpipe_message_结构体.md#a05db95499949220a3009d837a897bb9d)
- [mpipe_message_post](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga371e6503fe08971ce1a2606d0a034b41)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_message::domain](../audio_video_model_reference/P023_mpipe_message_结构体.md#a05db95499949220a3009d837a897bb9d)
- [mpipe_message::type](../audio_video_model_reference/P023_mpipe_message_结构体.md#a45622118757cf3df3271380752700b42)
- [mpipe_message::code](../audio_video_model_reference/P023_mpipe_message_结构体.md#a8559ee9f5039c992ed46636e3d953c49)
- [mpipe_message::origin](../audio_video_model_reference/P023_mpipe_message_结构体.md#abb655d25f900b38c77164962970a493f)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P551_mpipe_fake_src.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P553_mpipe_object.h_源码浏览.md)
