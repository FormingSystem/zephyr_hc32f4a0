---
id: learning.zephyr-docs.api-source-reference.page-908
title: video.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第908章\_video.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)。

## 908.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00046"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00246"></a>
<a id="l00252"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00289"></a>
<a id="l00295"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00402"></a>
<a id="l00408"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00516"></a>
<a id="l00522"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="acontrols_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="aformats_8h_html"></a>
<a id="agroup__clock__apis_html_ga0501e82515b2bdf36453c4cc80f5e0cc"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__video__api__buffers_html_ga036c42c1e7dbaa97eb2789dfc3a3c1d7"></a>
<a id="agroup__video__api__buffers_html_ga195914c7f03f2241702c77d41d1ab750"></a>
<a id="agroup__video__api__buffers_html_ga4d3c1458b8c30cff9ac5e6a62d6391c9"></a>
<a id="agroup__video__api__buffers_html_ga8ec3f0b83ba64947570dfe06ad5e2cbd"></a>
<a id="agroup__video__api__buffers_html_gaa65b69cdc4271a07ad26c4850ff96e45"></a>
<a id="agroup__video__api__buffers_html_gaae3a7eee506e77dd130fae74107f6533"></a>
<a id="agroup__video__api__buffers_html_gaba208d8f4747952acbec5b84f474e31b"></a>
<a id="agroup__video__api__buffers_html_gaee6eb26310a40d3f18161b3567f9e0a9"></a>
<a id="agroup__video__api__caps_html_ga1bf94d7b435524d0face3f713c4dca9d"></a>
<a id="agroup__video__api__caps_html_ga3d2d1692e4adab02948b11f38407610f"></a>
<a id="agroup__video__api__caps_html_gadbf59fd2d77b3d164cacf56bd4ae81ce"></a>
<a id="agroup__video__api__control_html_ga1cce17a3dfc881a1080708c7bc417aac"></a>
<a id="agroup__video__api__control_html_ga2bff04c6abc344350d6b0036289a701e"></a>
<a id="agroup__video__api__control_html_ga41e450607b4dc062fac682728ec7a79d"></a>
<a id="agroup__video__api__control_html_ga71853c720e6df1def4c945e23d103298"></a>
<a id="agroup__video__api__control_html_ga8813a656a66adc6bfb10fb7f27194898"></a>
<a id="agroup__video__api__format_html_ga0c30d2802c82b28cbb5029e7bc52b5b4"></a>
<a id="agroup__video__api__format_html_ga1deb2dbafd7f4eeb602a3f78aaeb5e33"></a>
<a id="agroup__video__api__format_html_ga6ea31432d37e0f8f46e0f6c2690ee3e9"></a>
<a id="agroup__video__api__format_html_ga774ef89a7321a6842890005ad53c1594"></a>
<a id="agroup__video__api__format_html_ga8db8c17f3cb418e44620816e9a5cf706"></a>
<a id="agroup__video__api__format_html_ga9de739567bff0a8ce915d389294e35ec"></a>
<a id="agroup__video__api__frmival_html_ga09efb2f6e1f56075cf0c44871266d634"></a>
<a id="agroup__video__api__frmival_html_ga2834be95778244a2446b62e673bbb187"></a>
<a id="agroup__video__api__frmival_html_ga46c5bca5cd3caf762f9dd4998b6e21de"></a>
<a id="agroup__video__api__frmival_html_ga6b3c7456b2527cc441a100ff50787dc2"></a>
<a id="agroup__video__api__frmival_html_ga99722c1e31aa6b73f443c22593b76e87"></a>
<a id="agroup__video__api__frmival_html_gafa448552f4257d761d96976cbe3da928"></a>
<a id="agroup__video__api__stream_html_ga77c694bfc3ff8d51a5a74dcd211b2563"></a>
<a id="agroup__video__api__stream_html_gaa4d62da5137d0392ce8a19f794478610"></a>
<a id="agroup__video__types_html_gad386b2994b56844ebe713f156b9dfe4e"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ainclude_2zephyr_2video_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructdevice_html"></a>
<a id="astructk__poll__signal_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructvideo__buffer_html"></a>
<a id="astructvideo__buffer_html_a3f040775c683c91740c8bda5c96e621b"></a>
<a id="astructvideo__buffer_html_a46dd9bd9398ff74e4f9859a07b9c48af"></a>
<a id="astructvideo__caps_html"></a>
<a id="astructvideo__control_html"></a>
<a id="astructvideo__ctrl__query_html"></a>
<a id="astructvideo__format__cap_html"></a>
<a id="astructvideo__format_html"></a>
<a id="astructvideo__frmival__enum_html"></a>
<a id="astructvideo__frmival__stepwise_html"></a>
<a id="astructvideo__frmival_html"></a>
<a id="astructvideo__frmival_html_a57ee282f01da0f1ef1db2558d777631c"></a>
<a id="astructvideo__frmival_html_aba4a6700ea733c3b07ee6445856c580a"></a>
<a id="astructvideo__selection_html"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 * Copyright 2025 NXP
 * Copyright (c) 2025 STMicroelectronics
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_VIDEO_VIDEO_H
#define ZEPHYR_INCLUDE_VIDEO_VIDEO_H


#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/video/controls.h>
#include <zephyr/video/formats.h>
#include <zephyr/video/types.h>

#ifdef __cplusplus
extern "C" {
#endif


int video_enqueue(const struct device *dev, struct video_buffer *buf);

int video_dequeue(const struct device *dev, struct video_buffer **vbuf, k_timeout_t timeout);

struct video_buffer *video_buffer_aligned_alloc(size_t size, size_t align, k_timeout_t timeout);

struct video_buffer *video_buffer_alloc(size_t size, k_timeout_t timeout);

struct video_buffer *video_import_buffer(uint8_t *mem, size_t sz);

int video_buffer_release(struct video_buffer *buf);

int video_transfer_buffer(const struct device *src, const struct device *sink,
                          enum video_buf_type src_type, enum video_buf_type sink_type,
                          k_timeout_t timeout);

int video_set_signal(const struct device *dev, struct k_poll_signal *sig);



int video_set_ctrl(const struct device *dev, struct video_control *control);

int video_get_ctrl(const struct device *dev, struct video_control *control);

int video_query_ctrl(struct video_ctrl_query *cq);

void video_print_ctrl(const struct video_ctrl_query *const cq);

int64_t video_get_csi_link_freq(const struct device *dev, uint8_t bpp, uint8_t lane_nb);



int video_stream_start(const struct device *dev, enum video_buf_type type);

int video_stream_stop(const struct device *dev, enum video_buf_type type);



int video_enum_frmival(const struct device *dev, struct video_frmival_enum *fie);

int video_set_frmival(const struct device *dev, struct video_frmival *frmival);

int video_get_frmival(const struct device *dev, struct video_frmival *frmival);

static inline uint64_t video_frmival_nsec(const struct video_frmival *frmival)
{
        if (frmival == NULL || frmival->denominator == 0) {
                return -EINVAL;
        }

        return (uint64_t)NSEC_PER_SEC * frmival->numerator / frmival->denominator;
}

int video_closest_frmival_stepwise(const struct video_frmival_stepwise *stepwise,
                                   const struct video_frmival *desired,
                                   struct video_frmival *match);

int video_closest_frmival(const struct device *dev, struct video_frmival_enum *match);



int video_estimate_fmt_size(struct video_format *fmt);

int video_set_compose_format(const struct device *dev, struct video_format *fmt);

int video_set_format(const struct device *dev, struct video_format *fmt);

int video_get_format(const struct device *dev, struct video_format *fmt);

int video_set_selection(const struct device *dev, struct video_selection *sel);

int video_get_selection(const struct device *dev, struct video_selection *sel);



int video_get_caps(const struct device *dev, struct video_caps *caps);

int video_transform_cap(const struct device *const dev,
                        const struct video_format_cap *const cap,
                        struct video_format_cap *const res_cap,
                        enum video_buf_type type, uint16_t ind);

int video_format_caps_index(const struct video_format_cap *fmts, const struct video_format *fmt,
                            size_t *idx);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_VIDEO_VIDEO_H */
```

## 908.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

版权（Copyright）：2025 NXP。

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 596 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_VIDEO_VIDEO_H`。

## 908.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/video/controls.h](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html)
- [zephyr/video/formats.h](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html)
- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h.html)
- [video_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga036c42c1e7dbaa97eb2789dfc3a3c1d7)
- [device](../device_reference/P002_设备对象结构.md)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [video_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaba208d8f4747952acbec5b84f474e31b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [video_buffer_aligned_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga195914c7f03f2241702c77d41d1ab750)
- [size](../audio_video_model_reference/P051_video_buffer_结构体.md#a3f040775c683c91740c8bda5c96e621b)
- [video_buffer_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaee6eb26310a40d3f18161b3567f9e0a9)
- [video_import_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaa65b69cdc4271a07ad26c4850ff96e45)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_buffer_release](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaae3a7eee506e77dd130fae74107f6533)
- [video_transfer_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga4d3c1458b8c30cff9ac5e6a62d6391c9)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [video_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga8ec3f0b83ba64947570dfe06ad5e2cbd)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [video_set_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga1cce17a3dfc881a1080708c7bc417aac)
- [video_control](../audio_video_model_reference/P053_video_control_结构体.md)
- [video_get_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga71853c720e6df1def4c945e23d103298)
- [video_query_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga8813a656a66adc6bfb10fb7f27194898)
- [video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)
- [video_print_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga2bff04c6abc344350d6b0036289a701e)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [video_get_csi_link_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga41e450607b4dc062fac682728ec7a79d)
- [video_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html#gaa4d62da5137d0392ce8a19f794478610)
- [type](../audio_video_model_reference/P051_video_buffer_结构体.md#a46dd9bd9398ff74e4f9859a07b9c48af)
- [video_stream_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html#ga77c694bfc3ff8d51a5a74dcd211b2563)
- [video_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga09efb2f6e1f56075cf0c44871266d634)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga46c5bca5cd3caf762f9dd4998b6e21de)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga2834be95778244a2446b62e673bbb187)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [video_frmival_nsec](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga6b3c7456b2527cc441a100ff50787dc2)
- [denominator](../audio_video_model_reference/P061_video_frmival_结构体.md#aba4a6700ea733c3b07ee6445856c580a)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [numerator](../audio_video_model_reference/P061_video_frmival_结构体.md#a57ee282f01da0f1ef1db2558d777631c)
- [video_closest_frmival_stepwise](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#gafa448552f4257d761d96976cbe3da928)
- [video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)
- [video_closest_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga99722c1e31aa6b73f443c22593b76e87)
- [video_estimate_fmt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga774ef89a7321a6842890005ad53c1594)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_set_compose_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga9de739567bff0a8ce915d389294e35ec)
- [video_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga1deb2dbafd7f4eeb602a3f78aaeb5e33)
- [video_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga8db8c17f3cb418e44620816e9a5cf706)
- [video_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga6ea31432d37e0f8f46e0f6c2690ee3e9)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [video_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga0c30d2802c82b28cbb5029e7bc52b5b4)
- [video_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html#ga1bf94d7b435524d0face3f713c4dca9d)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_transform_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html#ga3d2d1692e4adab02948b11f38407610f)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [video_format_caps_index](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html#gadbf59fd2d77b3d164cacf56bd4ae81ce)
- [controls.h](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [formats.h](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [video_buffer::size](../audio_video_model_reference/P051_video_buffer_结构体.md#a3f040775c683c91740c8bda5c96e621b)
- [video_buffer::type](../audio_video_model_reference/P051_video_buffer_结构体.md#a46dd9bd9398ff74e4f9859a07b9c48af)
- [video_frmival::numerator](../audio_video_model_reference/P061_video_frmival_结构体.md#a57ee282f01da0f1ef1db2558d777631c)
- [video_frmival::denominator](../audio_video_model_reference/P061_video_frmival_结构体.md#aba4a6700ea733c3b07ee6445856c580a)

---

[上一章](P907_video-interfaces.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P909_virtio.h_源码浏览.md)
