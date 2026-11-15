---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-9
title: audio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2usb_2audio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_audio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2usb_2audio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P071_zephyr__dt-bindings__usb__audio.h_文件参考.md)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
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
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_USB_AUDIO_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_USB_AUDIO_H

/* USB Device Class Definition for Audio Devices Release 2.0 May 31, 2006
 * A.7 Audio Function Category Codes
 */
#define AUDIO_FUNCTION_SUBCLASS_UNDEFINED       0x00
#define AUDIO_FUNCTION_DESKTOP_SPEAKER          0x01
#define AUDIO_FUNCTION_HOME_THEATER             0x02
#define AUDIO_FUNCTION_MICROPHONE               0x03
#define AUDIO_FUNCTION_HEADSET                  0x04
#define AUDIO_FUNCTION_TELEPHONE                0x05
#define AUDIO_FUNCTION_CONVERTER                0x06
#define AUDIO_FUNCTION_VOICE_SOUND_RECORDER     0x07
#define AUDIO_FUNCTION_IO_BOX                   0x08
#define AUDIO_FUNCTION_MUSICAL_INSTRUMENT       0x09
#define AUDIO_FUNCTION_PRO_AUDIO                0x0A
#define AUDIO_FUNCTION_AUDIO_VIDEO              0x0B
#define AUDIO_FUNCTION_CONTROL_PANEL            0x0C
#define AUDIO_FUNCTION_OTHER                    0xFF


/* USB Device Class Definition for Terminal Types
 * Both "Universal Serial Bus Device Class Definition for Terminal Types"
 * Release 2.0 May 31, 2006 and Release 3.0 September 22, 2016 contain exactly
 * the same terminal types and values.
 */

/* 2.1 USB Terminal Types */
#define USB_TERMINAL_UNDEFINED                                  0x0100
#define USB_TERMINAL_STREAMING                                  0x0101
#define USB_TERMINAL_VENDOR_SPECIFIC                            0x01FF

/* 2.2 Input Terminal Types */
#define INPUT_TERMINAL_UNDEFINED                                0x0200
#define INPUT_TERMINAL_MICROPHONE                               0x0201
#define INPUT_TERMINAL_DESKTOP_MICROPHONE                       0x0202
#define INPUT_TERMINAL_PERSONAL_MICROPHONE                      0x0203
#define INPUT_TERMINAL_OMNI_DIRECTIONAL_MICROPHONE              0x0204
#define INPUT_TERMINAL_MICROPHONE_ARRAY                         0x0205
#define INPUT_TERMINAL_PROCESSING_MICROPHONE_ARRAY              0x0206

/* 2.3 Output Terminal Types */
#define OUTPUT_TERMINAL_UNDEFINED                               0x0300
#define OUTPUT_TERMINAL_SPEAKER                                 0x0301
#define OUTPUT_TERMINAL_HEADPHONES                              0x0302
#define OUTPUT_TERMINAL_HEAD_MOUNTED_DISPLAY_AUDIO              0x0303
#define OUTPUT_TERMINAL_DESKTOP_SPEAKER                         0x0304
#define OUTPUT_TERMINAL_ROOM_SPEAKER                            0x0305
#define OUTPUT_TERMINAL_COMMUNICATION_SPEAKER                   0x0306
#define OUTPUT_TERMINAL_LOW_FREQUENCY_EFFECTS_SPEAKER           0x0307

/* 2.4 Bi-directional Terminal Types */
#define BIDIRECTIONAL_TERMINAL_UNDEFINED                        0x0400
#define BIDIRECTIONAL_TERMINAL_HANDSET                          0x0401
#define BIDIRECTIONAL_TERMINAL_HEADSET                          0x0402
#define BIDIRECTIONAL_TERMINAL_SPEAKERPHONE_NO_ECHO_REDUCTION   0x0403
#define BIDIRECTIONAL_TERMINAL_ECHO_SUPPRESSING_SPEAKERPHONE    0x0404
#define BIDIRECTIONAL_TERMINAL_ECHO_CANCELLING_SPEAKERPHONE     0x0405

/* 2.5 Telephony Terminal Types */
#define TELEPHONY_TERMINAL_UNDEFINED                            0x0500
#define TELEPHONY_TERMINAL_PHONE_LINE                           0x0501
#define TELEPHONY_TERMINAL_TELEPHONE                            0x0502
#define TELEPHONY_TERMINAL_DOWN_LINE_PHONE                      0x0503

/* 2.6 External Terminal Types */
#define EXTERNAL_TERMINAL_UNDEFINED                             0x0600
#define EXTERNAL_TERMINAL_ANALOG_CONNECTOR                      0x0601
#define EXTERNAL_TERMINAL_DIGITAL_AUDIO_INTERFACE               0x0602
#define EXTERNAL_TERMINAL_LINE_CONNECTOR                        0x0603
#define EXTERNAL_TERMINAL_LEGACY_AUDIO_CONNECTOR                0x0604
#define EXTERNAL_TERMINAL_SPDIF_INTERFACE                       0x0605
#define EXTERNAL_TERMINAL_1394_DA_STREAM                        0x0606
#define EXTERNAL_TERMINAL_1394_DV_STREAM_SOUNDTRACK             0x0607
#define EXTERNAL_TERMINAL_ADAT_LIGHTPIPE                        0x0608
#define EXTERNAL_TERMINAL_TDIF                                  0x0609
#define EXTERNAL_TERMINAL_MADI                                  0x060A

/* 2.7 Embedded Function Terminal Types */
#define EMBEDDED_TERMINAL_UNDEFINED                             0x0700
#define EMBEDDED_TERMINAL_LEVEL_CALIBRATION_NOISE_SOURCE        0x0701
#define EMBEDDED_TERMINAL_EQUALIZATION_NOISE                    0x0702
#define EMBEDDED_TERMINAL_CD_PLAYER                             0x0703
#define EMBEDDED_TERMINAL_DAT                                   0x0704
#define EMBEDDED_TERMINAL_DCC                                   0x0705
#define EMBEDDED_TERMINAL_COMPRESSED_AUDIO_PLAYER               0x0706
#define EMBEDDED_TERMINAL_ANALOG_TAPE                           0x0707
#define EMBEDDED_TERMINAL_PHONOGRAPH                            0x0708
#define EMBEDDED_TERMINAL_VCR_AUDIO                             0x0709
#define EMBEDDED_TERMINAL_VIDEO_DISC_AUDIO                      0x070A
#define EMBEDDED_TERMINAL_DVD_AUDIO                             0x070B
#define EMBEDDED_TERMINAL_TV_TUNER_AUDIO                        0x070C
#define EMBEDDED_TERMINAL_SATELLITE_RECEIVER_AUDIO              0x070D
#define EMBEDDED_TERMINAL_CABLE_TUNER_AUDIO                     0x070E
#define EMBEDDED_TERMINAL_DSS_AUDIO                             0x070F
#define EMBEDDED_TERMINAL_RADIO_RECEIVER                        0x0710
#define EMBEDDED_TERMINAL_RADIO_TRANSMITTER                     0x0711
#define EMBEDDED_TERMINAL_MULTI_TRACK_RECORDER                  0x0712
#define EMBEDDED_TERMINAL_SYNTHESIZER                           0x0713
#define EMBEDDED_TERMINAL_PIANO                                 0x0714
#define EMBEDDED_TERMINAL_GUITAR                                0x0715
#define EMBEDDED_TERMINAL_DRUMS_RHYTHM                          0x0716
#define EMBEDDED_TERMINAL_OTHER_MUSICAL_INSTRUMENT              0x0717

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_USB_AUDIO_H */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

《USB 音频设备类定义》（USB Device Class Definition for Audio Devices），2.0 版，2006 年 5 月 31 日；附录 A.7“音频功能类别代码”（Audio Function Category Codes）。

### 注释 3：原第 29 行

《USB 终端类型设备类定义》（USB Device Class Definition for Terminal Types）。《通用串行总线终端类型设备类定义》（Universal Serial Bus Device Class Definition for Terminal Types）的 2.0 版（2006 年 5 月 31 日）和 3.0 版（2016 年 9 月 22 日）包含完全相同的终端类型及取值。

### 注释 4：原第 35 行

2.1 USB 终端类型（USB Terminal Types）。

### 注释 5：原第 40 行

2.2 输入终端类型（Input Terminal Types）。

### 注释 6：原第 49 行

2.3 输出终端类型（Output Terminal Types）。

### 注释 7：原第 59 行

2.4 双向终端类型（Bi-directional Terminal Types）。

### 注释 8：原第 67 行

2.5 电话终端类型（Telephony Terminal Types）。

### 注释 9：原第 73 行

2.6 外部终端类型（External Terminal Types）。

### 注释 10：原第 86 行

2.7 嵌入式功能终端类型（Embedded Function Terminal Types）。

### 注释 11：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_USB_AUDIO_H`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P071_zephyr__dt-bindings__usb__audio.h_文件参考.md)

---

[上一章](P008_dns_resolve.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_esp32c5_clock.h_源码浏览.md)
