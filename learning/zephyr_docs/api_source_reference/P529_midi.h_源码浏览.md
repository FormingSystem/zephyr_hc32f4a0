---
id: learning.zephyr-docs.api-source-reference.page-529
title: midi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/midi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第529章\_midi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)。

## 529.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="l00043"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="foldopen00190"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00228"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="foldopen00335"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="foldopen00343"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructmidi__ump_html"></a>
<a id="astructmidi__ump_html_a9c38cadb8046ba91b080604ac66ea89f"></a>

```c
/*
 * Copyright (c) 2024 Titouan Christophe
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUDIO_MIDI_H_
#define ZEPHYR_INCLUDE_AUDIO_MIDI_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>



struct midi_ump {
        uint32_t data[4];
};


#define UMP_MT_UTILITY             0x00
#define UMP_MT_SYS_RT_COMMON       0x01
#define UMP_MT_MIDI1_CHANNEL_VOICE 0x02
#define UMP_MT_DATA_64             0x03
#define UMP_MT_MIDI2_CHANNEL_VOICE 0x04
#define UMP_MT_DATA_128            0x05
#define UMP_MT_FLEX_DATA           0x0d
#define UMP_MT_UMP_STREAM          0x0f

#define UMP_MT(ump) \
        ((ump).data[0] >> 28)

#define UMP_NUM_WORDS_LOOKUP_TABLE \
        ((0U << 0) | (0U << 2) | (0U << 4) | (1U << 6) | \
        (1U << 8) | (3U << 10) | (0U << 12) | (0U << 14) | \
        (1U << 16) | (1U << 18) | (1U << 20) | (2U << 22) | \
        (2U << 24) | (3U << 26) | (3U << 28) | (3U << 30))

#define UMP_NUM_WORDS(ump) \
        (1 + ((UMP_NUM_WORDS_LOOKUP_TABLE >> (2 * UMP_MT(ump))) & 3))

#define UMP_GROUP(ump) \
        (((ump).data[0] >> 24) & 0xF)

#define UMP_MIDI_STATUS(ump) \
        (((ump).data[0] >> 16) & 0xFF)

#define UMP_MIDI_COMMAND(ump) \
        (UMP_MIDI_STATUS(ump) >> 4)

#define UMP_MIDI_CHANNEL(ump) \
        (UMP_MIDI_STATUS(ump) & 0xF)

#define UMP_MIDI1_P1(ump) \
        (((ump).data[0] >> 8) & 0x7F)

#define UMP_MIDI1_P2(ump) \
        ((ump).data[0] & 0x7F)

#define UMP_MIDI1_CHANNEL_VOICE(group, command, channel, p1, p2) \
        (struct midi_ump) {.data = {                             \
                (UMP_MT_MIDI1_CHANNEL_VOICE << 28)               \
                | (((group) & 0x0f) << 24)                       \
                | (((command) & 0x0f) << 20)                     \
                | (((channel) & 0x0f) << 16)                     \
                | (((p1) & 0x7f) << 8)                           \
                | ((p2) & 0x7f)                                  \
        }}

#define UMP_MIDI_NOTE_OFF        0x8
#define UMP_MIDI_NOTE_ON         0x9
#define UMP_MIDI_AFTERTOUCH      0xa
#define UMP_MIDI_CONTROL_CHANGE  0xb
#define UMP_MIDI_PROGRAM_CHANGE  0xc
#define UMP_MIDI_CHAN_AFTERTOUCH 0xd
#define UMP_MIDI_PITCH_BEND      0xe

#define UMP_SYS_RT_COMMON(group, status, p1, p2) \
        (struct midi_ump) {.data = {             \
                (UMP_MT_SYS_RT_COMMON << 28)     \
                | (((group) & 0x0f) << 24)       \
                | ((status) << 16)               \
                | (((p1) & 0x7f) << 8)           \
                | ((p2) & 0x7f)                  \
        }}

#define UMP_SYS_MIDI_TIME_CODE 0xf1
#define UMP_SYS_SONG_POSITION  0xf2
#define UMP_SYS_SONG_SELECT    0xf3
#define UMP_SYS_TUNE_REQUEST   0xf6
#define UMP_SYS_TIMING_CLOCK   0xf8
#define UMP_SYS_START          0xfa
#define UMP_SYS_CONTINUE       0xfb
#define UMP_SYS_STOP           0xfc
#define UMP_SYS_ACTIVE_SENSING 0xfe
#define UMP_SYS_RESET          0xff



#define UMP_STREAM_FORMAT(ump) \
        (((ump).data[0] >> 26) & 0x03)


#define UMP_STREAM_FORMAT_COMPLETE 0x00
#define UMP_STREAM_FORMAT_START    0x01
#define UMP_STREAM_FORMAT_CONTINUE 0x02
#define UMP_STREAM_FORMAT_END      0x03


#define UMP_STREAM_STATUS(ump) \
        (((ump).data[0] >> 16) & 0x3FF)


#define UMP_STREAM_STATUS_EP_DISCOVERY 0x00
#define UMP_STREAM_STATUS_EP_INFO      0x01
#define UMP_STREAM_STATUS_DEVICE_IDENT 0x02
#define UMP_STREAM_STATUS_EP_NAME      0x03
#define UMP_STREAM_STATUS_PROD_ID      0x04
#define UMP_STREAM_STATUS_CONF_REQ     0x05
#define UMP_STREAM_STATUS_CONF_NOTIF   0x06
#define UMP_STREAM_STATUS_FB_DISCOVERY 0x10
#define UMP_STREAM_STATUS_FB_INFO      0x11
#define UMP_STREAM_STATUS_FB_NAME      0x12

#define UMP_STREAM_EP_DISCOVERY_FILTER(ump) \
        ((ump).data[1] & 0xFF)


#define UMP_EP_DISC_FILTER_EP_INFO    BIT(0)
#define UMP_EP_DISC_FILTER_DEVICE_ID  BIT(1)
#define UMP_EP_DISC_FILTER_EP_NAME    BIT(2)
#define UMP_EP_DISC_FILTER_PRODUCT_ID BIT(3)
#define UMP_EP_DISC_FILTER_STREAM_CFG BIT(4)

#define UMP_STREAM_FB_DISCOVERY_FILTER(ump) \
        ((ump).data[0] & 0xFF)

#define UMP_STREAM_FB_DISCOVERY_NUM(ump) \
        (((ump).data[0] >> 8) & 0xFF)

#define UMP_FB_DISC_FILTER_INFO BIT(0)
#define UMP_FB_DISC_FILTER_NAME BIT(1)



#ifdef __cplusplus
}
#endif

#endif
```

## 529.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Titouan Christophe。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 529.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [data](../usb/P099_通用MIDI数据包结构.md#a9c38cadb8046ba91b080604ac66ea89f)
- [midi_ump::data](../usb/P099_通用MIDI数据包结构.md#a9c38cadb8046ba91b080604ac66ea89f)

---

[上一章](P528_midi2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P530_mii.h_源码浏览.md)
