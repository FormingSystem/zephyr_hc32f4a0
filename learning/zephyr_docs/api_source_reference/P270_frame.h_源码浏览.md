---
id: learning.zephyr-docs.api-source-reference.page-270
title: frame.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/frame_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第270章\_frame.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html)。

## 270.1\_原始可见代码（Source Code）

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
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
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
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2f"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442"></a>
<a id="aframe_8h_html_a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4"></a>
<a id="aframe_8h_html_ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhttp2__settings__field_html"></a>
<a id="astructhttp2__settings__field_html_a3093b8f2b69ae06972fecbe89a18c342"></a>
<a id="astructhttp2__settings__field_html_a66561355ba380a09c0ca8df583c085b8"></a>

```c
/*
 * Copyright (c) 2023, Emna Rekik
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_HTTP_FRAME_H_
#define ZEPHYR_INCLUDE_NET_HTTP_FRAME_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

enum http2_frame_type {
        HTTP2_DATA_FRAME = 0x00,
        HTTP2_HEADERS_FRAME = 0x01,
        HTTP2_PRIORITY_FRAME = 0x02,
        HTTP2_RST_STREAM_FRAME = 0x03,
        HTTP2_SETTINGS_FRAME = 0x04,
        HTTP2_PUSH_PROMISE_FRAME = 0x05,
        HTTP2_PING_FRAME = 0x06,
        HTTP2_GOAWAY_FRAME = 0x07,
        HTTP2_WINDOW_UPDATE_FRAME = 0x08,
        HTTP2_CONTINUATION_FRAME = 0x09
};


#define HTTP2_FLAG_SETTINGS_ACK 0x01
#define HTTP2_FLAG_END_HEADERS  0x04
#define HTTP2_FLAG_END_STREAM   0x01
#define HTTP2_FLAG_PADDED       0x08
#define HTTP2_FLAG_PRIORITY     0x20

#define HTTP2_FRAME_HEADER_SIZE      9
#define HTTP2_FRAME_LENGTH_OFFSET    0
#define HTTP2_FRAME_TYPE_OFFSET      3
#define HTTP2_FRAME_FLAGS_OFFSET     4
#define HTTP2_FRAME_STREAM_ID_OFFSET 5
#define HTTP2_FRAME_STREAM_ID_MASK   0x7FFFFFFF

#define HTTP2_HEADERS_FRAME_PRIORITY_LEN 5
#define HTTP2_PRIORITY_FRAME_LEN 5
#define HTTP2_RST_STREAM_FRAME_LEN 4


struct http2_settings_field {
        uint16_t id;
        uint32_t value;
} __packed;

enum http2_settings {
        HTTP2_SETTINGS_HEADER_TABLE_SIZE = 1,
        HTTP2_SETTINGS_ENABLE_PUSH = 2,
        HTTP2_SETTINGS_MAX_CONCURRENT_STREAMS = 3,
        HTTP2_SETTINGS_INITIAL_WINDOW_SIZE = 4,
        HTTP2_SETTINGS_MAX_FRAME_SIZE = 5,
        HTTP2_SETTINGS_MAX_HEADER_LIST_SIZE = 6,
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_HTTP_FRAME_H_ */
```

## 270.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Emna Rekik。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 92 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HTTP_FRAME_H_`。

## 270.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [http2_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2f)
- [HTTP2_DATA_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561)
- [HTTP2_HEADERS_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb)
- [HTTP2_PRIORITY_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15)
- [HTTP2_RST_STREAM_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49)
- [HTTP2_SETTINGS_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123)
- [HTTP2_PUSH_PROMISE_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442)
- [HTTP2_PING_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff)
- [HTTP2_GOAWAY_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8)
- [HTTP2_WINDOW_UPDATE_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4)
- [HTTP2_CONTINUATION_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822)
- [http2_settings_field](../network_service_model_reference/P024_http2_settings_field_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [id](../network_service_model_reference/P024_http2_settings_field_结构体.md#a66561355ba380a09c0ca8df583c085b8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [value](../network_service_model_reference/P024_http2_settings_field_结构体.md#a3093b8f2b69ae06972fecbe89a18c342)
- [http2_settings](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559)
- [HTTP2_SETTINGS_HEADER_TABLE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06)
- [HTTP2_SETTINGS_ENABLE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4)
- [HTTP2_SETTINGS_MAX_CONCURRENT_STREAMS](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304)
- [HTTP2_SETTINGS_INITIAL_WINDOW_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0)
- [HTTP2_SETTINGS_MAX_FRAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e)
- [HTTP2_SETTINGS_MAX_HEADER_LIST_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705)
- [http2_settings_field::value](../network_service_model_reference/P024_http2_settings_field_结构体.md#a3093b8f2b69ae06972fecbe89a18c342)
- [http2_settings_field::id](../network_service_model_reference/P024_http2_settings_field_结构体.md#a66561355ba380a09c0ca8df583c085b8)

---

[上一章](P269_fota_http.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P271_nvs.h_源码浏览.md)
