---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-6
title: zephyr__audio__midi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_audio\_\_midi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MIDI 2.0通用MIDI数据包（Universal MIDI Packet，UMP）定义的头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

MIDI 2.0通用MIDI数据包（Universal MIDI Packet，UMP）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_midi_5Fump"></a>

```c
struct midi_ump
```

相关声明：[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

通用MIDI数据包（Universal MIDI Packet）的容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3"></a>

```c
#define UMP_MT_UTILITY 0x00
```

相关声明：[UMP_MT_UTILITY](../usb/P101_UMP消息类型.md#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)。

工具消息（Utility Messages）。

<a id="r_gab8f194f60f1b5de7f050009275e44412"></a>

```c
#define UMP_MT_SYS_RT_COMMON 0x01
```

相关声明：[UMP_MT_SYS_RT_COMMON](../usb/P101_UMP消息类型.md#gab8f194f60f1b5de7f050009275e44412)。

系统实时消息（System Real Time）和系统公共消息（System Common），不含系统专用消息（System Exclusive）。

<a id="r_gae086e5899933e436715ed2321607ef36"></a>

```c
#define UMP_MT_MIDI1_CHANNEL_VOICE 0x02
```

相关声明：[UMP_MT_MIDI1_CHANNEL_VOICE](../usb/P101_UMP消息类型.md#gae086e5899933e436715ed2321607ef36)。

MIDI 1.0 通道语音消息（Channel Voice Messages）。

<a id="r_ga235bf38958774c9ccc8864b98cff7ff9"></a>

```c
#define UMP_MT_DATA_64 0x03
```

相关声明：[UMP_MT_DATA_64](../usb/P101_UMP消息类型.md#ga235bf38958774c9ccc8864b98cff7ff9)。

64 位数据消息（Data Messages），包含系统专用消息（System Exclusive）。

<a id="r_ga9f2ac215138eb6e958df9558547f805a"></a>

```c
#define UMP_MT_MIDI2_CHANNEL_VOICE 0x04
```

相关声明：[UMP_MT_MIDI2_CHANNEL_VOICE](../usb/P101_UMP消息类型.md#ga9f2ac215138eb6e958df9558547f805a)。

MIDI 2.0 通道语音消息（Channel Voice Messages）。

<a id="r_gabe19506f8d84dbc84a46114768853d5b"></a>

```c
#define UMP_MT_DATA_128 0x05
```

相关声明：[UMP_MT_DATA_128](../usb/P101_UMP消息类型.md#gabe19506f8d84dbc84a46114768853d5b)。

128 位数据消息（Data Messages）。

<a id="r_ga916fba3c7a01dfff98f94c700a585fd5"></a>

```c
#define UMP_MT_FLEX_DATA 0x0d
```

相关声明：[UMP_MT_FLEX_DATA](../usb/P101_UMP消息类型.md#ga916fba3c7a01dfff98f94c700a585fd5)。

灵活数据消息（Flex Data Messages）。

<a id="r_gae14fb523ae456ca3e49a86de7d197e55"></a>

```c
#define UMP_MT_UMP_STREAM 0x0f
```

相关声明：[UMP_MT_UMP_STREAM](../usb/P101_UMP消息类型.md#gae14fb523ae456ca3e49a86de7d197e55)。

通用 MIDI 数据包流消息（UMP Stream Message）。

<a id="r_gafab438886f69fb74a6e058f9343867aa"></a>

```c
#define UMP_MT(ump)
```

相关声明：[UMP_MT](../usb/P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)。

通用 MIDI 数据包（Universal MIDI Packet，UMP）的消息类型字段（Message Type Field）。

<a id="r_gac718c321652066f1537ead1524137949"></a>

```c
#define UMP_NUM_WORDS_LOOKUP_TABLE
```

相关声明：[UMP_NUM_WORDS_LOOKUP_TABLE](../usb/P098_通用MIDI数据包定义.md#gac718c321652066f1537ead1524137949)。

UMP 共有 16 种消息类型（Message Type），每种长度可为 1–4 个 `uint32`。

<a id="r_ga31e6cb035180b3afca9980307a07c038"></a>

```c
#define UMP_NUM_WORDS(ump)
```

相关声明：[UMP_NUM_WORDS](../usb/P098_通用MIDI数据包定义.md#ga31e6cb035180b3afca9980307a07c038)。

通用 MIDI 数据包（UMP）的大小，以 32 位字（32-bit Word）为单位。

<a id="r_ga497e212c131b7366878e46f63727cab5"></a>

```c
#define UMP_GROUP(ump)
```

相关声明：[UMP_GROUP](../usb/P098_通用MIDI数据包定义.md#ga497e212c131b7366878e46f63727cab5)。

通用 MIDI 数据包（UMP）的 MIDI 组字段（Group Field）。

<a id="r_ga407db6234865dd53a0939b9e6ca7455c"></a>

```c
#define UMP_MIDI_STATUS(ump)
```

相关声明：[UMP_MIDI_STATUS](../usb/P098_通用MIDI数据包定义.md#ga407db6234865dd53a0939b9e6ca7455c)。

MIDI 通道语音消息或系统消息的状态字节（Status Byte）。

<a id="r_gac3af021e7300ab96e449da048545900f"></a>

```c
#define UMP_MIDI_COMMAND(ump)
```

相关声明：[UMP_MIDI_COMMAND](../usb/P098_通用MIDI数据包定义.md#gac3af021e7300ab96e449da048545900f)。

MIDI 通道语音消息（Channel Voice Message）的命令（Command）。

<a id="r_ga8ecdaa13831c0cf1abf79da0b343416f"></a>

```c
#define UMP_MIDI_CHANNEL(ump)
```

相关声明：[UMP_MIDI_CHANNEL](../usb/P098_通用MIDI数据包定义.md#ga8ecdaa13831c0cf1abf79da0b343416f)。

MIDI 通道语音消息（Channel Voice Message）的通道（Channel）。

<a id="r_gac64740902864ecb903f70083f2c638d2"></a>

```c
#define UMP_MIDI1_P1(ump)
```

相关声明：[UMP_MIDI1_P1](../usb/P098_通用MIDI数据包定义.md#gac64740902864ecb903f70083f2c638d2)。

MIDI1 通道语音消息或系统消息的第一个参数（First Parameter）。

<a id="r_ga1c6c6f8928071d4d77744404e62168b4"></a>

```c
#define UMP_MIDI1_P2(ump)
```

相关声明：[UMP_MIDI1_P2](../usb/P098_通用MIDI数据包定义.md#ga1c6c6f8928071d4d77744404e62168b4)。

MIDI1 通道语音消息或系统消息的第二个参数（Second Parameter）。

<a id="r_gac05c1718b33d08a92bae9b4974ced501"></a>

```c
#define UMP_MIDI1_CHANNEL_VOICE(group, command, channel, p1, p2)
```

相关声明：[UMP_MIDI1_CHANNEL_VOICE](../usb/P098_通用MIDI数据包定义.md#gac05c1718b33d08a92bae9b4974ced501)、[group](../posix_system_model_reference/P003_group_结构体.md)。

使用 MIDI1 通道语音消息（Channel Voice Message）初始化通用 MIDI 数据包（UMP）。

<a id="r_ga8300450177c4f1ec7c11ed7d8886f87e"></a>

```c
#define UMP_MIDI_NOTE_OFF 0x8
```

相关声明：[UMP_MIDI_NOTE_OFF](../usb/P100_MIDI命令常量.md#ga8300450177c4f1ec7c11ed7d8886f87e)。

音符关闭（Note Off）：`p1` 为音符编号（Note Number），`p2` 为力度（Velocity）。

<a id="r_ga85749d1edff030bc0d8b131b9116911e"></a>

```c
#define UMP_MIDI_NOTE_ON 0x9
```

相关声明：[UMP_MIDI_NOTE_ON](../usb/P100_MIDI命令常量.md#ga85749d1edff030bc0d8b131b9116911e)。

音符开启（Note On）：`p1` 为音符编号（Note Number），`p2` 为力度（Velocity）。

<a id="r_ga7fae224629121ad30f9f38241885452c"></a>

```c
#define UMP_MIDI_AFTERTOUCH 0xa
```

相关声明：[UMP_MIDI_AFTERTOUCH](../usb/P100_MIDI命令常量.md#ga7fae224629121ad30f9f38241885452c)。

复音触后（Polyphonic Aftertouch）：`p1` 为音符编号（Note Number），`p2` 为数据（Data）。

<a id="r_gad4b17d74027a541957c933074d0f2d1e"></a>

```c
#define UMP_MIDI_CONTROL_CHANGE 0xb
```

相关声明：[UMP_MIDI_CONTROL_CHANGE](../usb/P100_MIDI命令常量.md#gad4b17d74027a541957c933074d0f2d1e)。

控制变更（Control Change）：`p1` 为索引（Index），`p2` 为数据（Data）。

<a id="r_gaad34de6aae0e22f5c84ef50e488e2d1a"></a>

```c
#define UMP_MIDI_PROGRAM_CHANGE 0xc
```

相关声明：[UMP_MIDI_PROGRAM_CHANGE](../usb/P100_MIDI命令常量.md#gaad34de6aae0e22f5c84ef50e488e2d1a)。

控制变更（Control Change，原文用语）：`p1` 为音色程序（Program）。

<a id="r_gaf5708894b80514023949e163f9687fb8"></a>

```c
#define UMP_MIDI_CHAN_AFTERTOUCH 0xd
```

相关声明：[UMP_MIDI_CHAN_AFTERTOUCH](../usb/P100_MIDI命令常量.md#gaf5708894b80514023949e163f9687fb8)。

通道触后（Channel Aftertouch）：`p1` 为数据（Data）。

<a id="r_gab11535e72a74baa71491264dd2c16192"></a>

```c
#define UMP_MIDI_PITCH_BEND 0xe
```

相关声明：[UMP_MIDI_PITCH_BEND](../usb/P100_MIDI命令常量.md#gab11535e72a74baa71491264dd2c16192)。

弯音（Pitch Bend）：`p1` 为最低有效部分（LSB），`p2` 为最高有效部分（MSB）。

<a id="r_ga06562acb0ec4d618d2e05b94c0a1bc4f"></a>

```c
#define UMP_SYS_RT_COMMON(group, status, p1, p2)
```

相关声明：[UMP_SYS_RT_COMMON](../usb/P098_通用MIDI数据包定义.md#ga06562acb0ec4d618d2e05b94c0a1bc4f)、[group](../posix_system_model_reference/P003_group_结构体.md)。

使用系统实时消息（System Real Time）和系统公共消息（System Common）初始化通用 MIDI 数据包（UMP）。

<a id="r_ga85394094ca6d908b7886adc4caceb671"></a>

```c
#define UMP_SYS_MIDI_TIME_CODE 0xf1
```

相关声明：[UMP_SYS_MIDI_TIME_CODE](../usb/P102_MIDI系统消息状态.md#ga85394094ca6d908b7886adc4caceb671)。

MIDI 时间码（MIDI Time Code），无参数。

<a id="r_ga254845a2c32a190b0bfc217025c5ad1d"></a>

```c
#define UMP_SYS_SONG_POSITION 0xf2
```

相关声明：[UMP_SYS_SONG_POSITION](../usb/P102_MIDI系统消息状态.md#ga254845a2c32a190b0bfc217025c5ad1d)。

乐曲位置指针（Song Position Pointer）：`p1` 为最低有效部分（LSB），`p2` 为最高有效部分（MSB）。

<a id="r_ga1d27e0f6fffd7ec05f58b56be78d9a8d"></a>

```c
#define UMP_SYS_SONG_SELECT 0xf3
```

相关声明：[UMP_SYS_SONG_SELECT](../usb/P102_MIDI系统消息状态.md#ga1d27e0f6fffd7ec05f58b56be78d9a8d)。

乐曲选择（Song Select）：`p1` 为乐曲编号（Song Number）。

<a id="r_ga4aa12e0cdb101a38b938876ebdcca64b"></a>

```c
#define UMP_SYS_TUNE_REQUEST 0xf6
```

相关声明：[UMP_SYS_TUNE_REQUEST](../usb/P102_MIDI系统消息状态.md#ga4aa12e0cdb101a38b938876ebdcca64b)。

调音请求（Tune Request），无参数。

<a id="r_gae064f3f47a9387076f5045e12e6ef7b7"></a>

```c
#define UMP_SYS_TIMING_CLOCK 0xf8
```

相关声明：[UMP_SYS_TIMING_CLOCK](../usb/P102_MIDI系统消息状态.md#gae064f3f47a9387076f5045e12e6ef7b7)。

定时时钟（Timing Clock），无参数。

<a id="r_ga368ad3719080979709699feb3d002dff"></a>

```c
#define UMP_SYS_START 0xfa
```

相关声明：[UMP_SYS_START](../usb/P102_MIDI系统消息状态.md#ga368ad3719080979709699feb3d002dff)。

开始（Start），无参数。

<a id="r_ga766b54e3caced69c147dbc94eb932595"></a>

```c
#define UMP_SYS_CONTINUE 0xfb
```

相关声明：[UMP_SYS_CONTINUE](../usb/P102_MIDI系统消息状态.md#ga766b54e3caced69c147dbc94eb932595)。

继续（Continue），无参数。

<a id="r_ga95542dda8f7f73f738c3ae298ca42f44"></a>

```c
#define UMP_SYS_STOP 0xfc
```

相关声明：[UMP_SYS_STOP](../usb/P102_MIDI系统消息状态.md#ga95542dda8f7f73f738c3ae298ca42f44)。

停止（Stop），无参数。

<a id="r_gaeb794e3933a2488eadb5f57ba971f81d"></a>

```c
#define UMP_SYS_ACTIVE_SENSING 0xfe
```

相关声明：[UMP_SYS_ACTIVE_SENSING](../usb/P102_MIDI系统消息状态.md#gaeb794e3933a2488eadb5f57ba971f81d)。

活动感知（Active Sensing），无参数。

<a id="r_ga5bd5358ae1847774409216f4e246f6f4"></a>

```c
#define UMP_SYS_RESET 0xff
```

相关声明：[UMP_SYS_RESET](../usb/P102_MIDI系统消息状态.md#ga5bd5358ae1847774409216f4e246f6f4)。

复位（Reset），无参数。

<a id="r_gaa964f1d5ebc6ffe3d360f9f4a303d0c7"></a>

```c
#define UMP_STREAM_FORMAT(ump)
```

相关声明：[UMP_STREAM_FORMAT](../usb/P103_UMP流消息字段.md#gaa964f1d5ebc6ffe3d360f9f4a303d0c7)。

UMP 流消息格式（UMP Stream Message Format）。

<a id="r_ga1437c75d99f58d138ea1ff04d5012b11"></a>

```c
#define UMP_STREAM_FORMAT_COMPLETE 0x00
```

相关声明：[UMP_STREAM_FORMAT_COMPLETE](../usb/P104_UMP流消息格式.md#ga1437c75d99f58d138ea1ff04d5012b11)。

完整消息位于一个 UMP 中。

<a id="r_ga145b3798cf8ada61a57feb6489aaa3f0"></a>

```c
#define UMP_STREAM_FORMAT_START 0x01
```

相关声明：[UMP_STREAM_FORMAT_START](../usb/P104_UMP流消息格式.md#ga145b3798cf8ada61a57feb6489aaa3f0)。

跨两个或更多 UMP 的消息起始部分（Start）。

<a id="r_ga8e84c4586cd1dcb5b0749669508608fd"></a>

```c
#define UMP_STREAM_FORMAT_CONTINUE 0x02
```

相关声明：[UMP_STREAM_FORMAT_CONTINUE](../usb/P104_UMP流消息格式.md#ga8e84c4586cd1dcb5b0749669508608fd)。

跨三个或更多 UMP 的消息中间延续部分（Continuing）。

<a id="r_gaf975fd5766fbddd0a3f1113c1d5c2fb1"></a>

```c
#define UMP_STREAM_FORMAT_END 0x03
```

相关声明：[UMP_STREAM_FORMAT_END](../usb/P104_UMP流消息格式.md#gaf975fd5766fbddd0a3f1113c1d5c2fb1)。

跨两个或更多 UMP 的消息结束部分（End）。

<a id="r_ga27ee62e9a2c2f6e23de61d8f5c42c0a8"></a>

```c
#define UMP_STREAM_STATUS(ump)
```

相关声明：[UMP_STREAM_STATUS](../usb/P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)。

UMP 流消息（UMP Stream Message）的状态字段（Status Field）。

<a id="r_gab753d923dd8a6045f85f5ac7032fd040"></a>

```c
#define UMP_STREAM_STATUS_EP_DISCOVERY 0x00
```

相关声明：[UMP_STREAM_STATUS_EP_DISCOVERY](../usb/P105_UMP流消息状态.md#gab753d923dd8a6045f85f5ac7032fd040)。

端点发现消息（Endpoint Discovery Message）。

<a id="r_ga1ff08a079dd9b84aa297ca73043342db"></a>

```c
#define UMP_STREAM_STATUS_EP_INFO 0x01
```

相关声明：[UMP_STREAM_STATUS_EP_INFO](../usb/P105_UMP流消息状态.md#ga1ff08a079dd9b84aa297ca73043342db)。

端点信息通知消息（Endpoint Info Notification Message）。

<a id="r_gaa53b5c80022e1888515f2c0616d9cfc3"></a>

```c
#define UMP_STREAM_STATUS_DEVICE_IDENT 0x02
```

相关声明：[UMP_STREAM_STATUS_DEVICE_IDENT](../usb/P105_UMP流消息状态.md#gaa53b5c80022e1888515f2c0616d9cfc3)。

设备身份通知消息（Device Identity Notification Message）。

<a id="r_gac9673eeb745526fd27f0e213ee06caa5"></a>

```c
#define UMP_STREAM_STATUS_EP_NAME 0x03
```

相关声明：[UMP_STREAM_STATUS_EP_NAME](../usb/P105_UMP流消息状态.md#gac9673eeb745526fd27f0e213ee06caa5)。

端点名称通知（Endpoint Name Notification）。

<a id="r_ga0edc8d182d71946828609b964bae1da8"></a>

```c
#define UMP_STREAM_STATUS_PROD_ID 0x04
```

相关声明：[UMP_STREAM_STATUS_PROD_ID](../usb/P105_UMP流消息状态.md#ga0edc8d182d71946828609b964bae1da8)。

产品实例标识符通知消息（Product Instance ID Notification Message）。

<a id="r_gaf28a14d200e97003c248ca1ad452244a"></a>

```c
#define UMP_STREAM_STATUS_CONF_REQ 0x05
```

相关声明：[UMP_STREAM_STATUS_CONF_REQ](../usb/P105_UMP流消息状态.md#gaf28a14d200e97003c248ca1ad452244a)。

流配置请求消息（Stream Configuration Request Message）。

<a id="r_ga182a95d09f4bef5976a64e5e02938ff8"></a>

```c
#define UMP_STREAM_STATUS_CONF_NOTIF 0x06
```

相关声明：[UMP_STREAM_STATUS_CONF_NOTIF](../usb/P105_UMP流消息状态.md#ga182a95d09f4bef5976a64e5e02938ff8)。

流配置通知消息（Stream Configuration Notification Message）。

<a id="r_gae0e25c309feb67ea77046a7587017b07"></a>

```c
#define UMP_STREAM_STATUS_FB_DISCOVERY 0x10
```

相关声明：[UMP_STREAM_STATUS_FB_DISCOVERY](../usb/P105_UMP流消息状态.md#gae0e25c309feb67ea77046a7587017b07)。

功能块发现消息（Function Block Discovery Message）。

<a id="r_ga4634c6db944bd4c582765f23fc7a4f35"></a>

```c
#define UMP_STREAM_STATUS_FB_INFO 0x11
```

相关声明：[UMP_STREAM_STATUS_FB_INFO](../usb/P105_UMP流消息状态.md#ga4634c6db944bd4c582765f23fc7a4f35)。

功能块信息通知（Function Block Info Notification）。

<a id="r_gaabf613ea856aa266cfdf13a32f300eee"></a>

```c
#define UMP_STREAM_STATUS_FB_NAME 0x12
```

相关声明：[UMP_STREAM_STATUS_FB_NAME](../usb/P105_UMP流消息状态.md#gaabf613ea856aa266cfdf13a32f300eee)。

功能块名称通知（Function Block Name Notification）。

<a id="r_gacbefffaacf70b546d5b7055bcefe7f16"></a>

```c
#define UMP_STREAM_EP_DISCOVERY_FILTER(ump)
```

相关声明：[UMP_STREAM_EP_DISCOVERY_FILTER](../usb/P103_UMP流消息字段.md#gacbefffaacf70b546d5b7055bcefe7f16)。

端点发现消息（Endpoint Discovery Message）的过滤位图（Filter Bitmap）。

<a id="r_ga6a234420b601ba9899b9a0c81e10daee"></a>

```c
#define UMP_EP_DISC_FILTER_EP_INFO BIT(0)
```

相关声明：[UMP_EP_DISC_FILTER_EP_INFO](../usb/P106_UMP端点发现过滤位.md#ga6a234420b601ba9899b9a0c81e10daee)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求端点信息通知（Endpoint Info Notification）。

<a id="r_ga07a1a713e27f2e1d59531f51699e65c8"></a>

```c
#define UMP_EP_DISC_FILTER_DEVICE_ID BIT(1)
```

相关声明：[UMP_EP_DISC_FILTER_DEVICE_ID](../usb/P106_UMP端点发现过滤位.md#ga07a1a713e27f2e1d59531f51699e65c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求设备身份通知（Device Identity Notification）。

<a id="r_gadc49c22e63a6119aa19fc655cbdd75f2"></a>

```c
#define UMP_EP_DISC_FILTER_EP_NAME BIT(2)
```

相关声明：[UMP_EP_DISC_FILTER_EP_NAME](../usb/P106_UMP端点发现过滤位.md#gadc49c22e63a6119aa19fc655cbdd75f2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求端点名称通知（Endpoint Name Notification）。

<a id="r_gad0a5a402d072dc843453cf4416dcb571"></a>

```c
#define UMP_EP_DISC_FILTER_PRODUCT_ID BIT(3)
```

相关声明：[UMP_EP_DISC_FILTER_PRODUCT_ID](../usb/P106_UMP端点发现过滤位.md#gad0a5a402d072dc843453cf4416dcb571)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求产品实例标识符通知（Product Instance ID Notification）。

<a id="r_ga72d2233a8760e3127bd7b4d133e12b3b"></a>

```c
#define UMP_EP_DISC_FILTER_STREAM_CFG BIT(4)
```

相关声明：[UMP_EP_DISC_FILTER_STREAM_CFG](../usb/P106_UMP端点发现过滤位.md#ga72d2233a8760e3127bd7b4d133e12b3b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求流配置通知（Stream Configuration Notification）。

<a id="r_gac7134040f1026e2c4ee20286100b1312"></a>

```c
#define UMP_STREAM_FB_DISCOVERY_FILTER(ump)
```

相关声明：[UMP_STREAM_FB_DISCOVERY_FILTER](../usb/P103_UMP流消息字段.md#gac7134040f1026e2c4ee20286100b1312)。

功能块发现消息（Function Block Discovery Message）的过滤位图（Filter Bitmap）。

<a id="r_ga7a6a56afd9298976899b0b2100b79223"></a>

```c
#define UMP_STREAM_FB_DISCOVERY_NUM(ump)
```

相关声明：[UMP_STREAM_FB_DISCOVERY_NUM](../usb/P103_UMP流消息字段.md#ga7a6a56afd9298976899b0b2100b79223)。

功能块发现消息（Function Block Discovery Message）中请求的块编号（Block Number）。

<a id="r_gaf0bc0e4083f74cfea57a0c52f7b5b1f6"></a>

```c
#define UMP_FB_DISC_FILTER_INFO BIT(0)
```

相关声明：[UMP_FB_DISC_FILTER_INFO](../usb/P107_UMP功能块发现过滤位.md#gaf0bc0e4083f74cfea57a0c52f7b5b1f6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求功能块信息通知（Function Block Info Notification）。

<a id="r_ga3552456370892c941d2c76f7029e0306"></a>

```c
#define UMP_FB_DISC_FILTER_NAME BIT(1)
```

相关声明：[UMP_FB_DISC_FILTER_NAME](../usb/P107_UMP功能块发现过滤位.md#ga3552456370892c941d2c76f7029e0306)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求功能块名称通知（Function Block Name Notification）。


## 6.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P529_midi.h_源码浏览.md)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [UMP_MT_UTILITY](../usb/P101_UMP消息类型.md#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)
- [UMP_MT_SYS_RT_COMMON](../usb/P101_UMP消息类型.md#gab8f194f60f1b5de7f050009275e44412)
- [UMP_MT_MIDI1_CHANNEL_VOICE](../usb/P101_UMP消息类型.md#gae086e5899933e436715ed2321607ef36)
- [UMP_MT_DATA_64](../usb/P101_UMP消息类型.md#ga235bf38958774c9ccc8864b98cff7ff9)
- [UMP_MT_MIDI2_CHANNEL_VOICE](../usb/P101_UMP消息类型.md#ga9f2ac215138eb6e958df9558547f805a)
- [UMP_MT_DATA_128](../usb/P101_UMP消息类型.md#gabe19506f8d84dbc84a46114768853d5b)
- [UMP_MT_FLEX_DATA](../usb/P101_UMP消息类型.md#ga916fba3c7a01dfff98f94c700a585fd5)
- [UMP_MT_UMP_STREAM](../usb/P101_UMP消息类型.md#gae14fb523ae456ca3e49a86de7d197e55)
- [UMP_MT](../usb/P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)
- [UMP_NUM_WORDS_LOOKUP_TABLE](../usb/P098_通用MIDI数据包定义.md#gac718c321652066f1537ead1524137949)
- [UMP_NUM_WORDS](../usb/P098_通用MIDI数据包定义.md#ga31e6cb035180b3afca9980307a07c038)
- [UMP_GROUP](../usb/P098_通用MIDI数据包定义.md#ga497e212c131b7366878e46f63727cab5)
- [UMP_MIDI_STATUS](../usb/P098_通用MIDI数据包定义.md#ga407db6234865dd53a0939b9e6ca7455c)
- [UMP_MIDI_COMMAND](../usb/P098_通用MIDI数据包定义.md#gac3af021e7300ab96e449da048545900f)
- [UMP_MIDI_CHANNEL](../usb/P098_通用MIDI数据包定义.md#ga8ecdaa13831c0cf1abf79da0b343416f)
- [UMP_MIDI1_P1](../usb/P098_通用MIDI数据包定义.md#gac64740902864ecb903f70083f2c638d2)
- [UMP_MIDI1_P2](../usb/P098_通用MIDI数据包定义.md#ga1c6c6f8928071d4d77744404e62168b4)
- [UMP_MIDI1_CHANNEL_VOICE](../usb/P098_通用MIDI数据包定义.md#gac05c1718b33d08a92bae9b4974ced501)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [UMP_MIDI_NOTE_OFF](../usb/P100_MIDI命令常量.md#ga8300450177c4f1ec7c11ed7d8886f87e)
- [UMP_MIDI_NOTE_ON](../usb/P100_MIDI命令常量.md#ga85749d1edff030bc0d8b131b9116911e)
- [UMP_MIDI_AFTERTOUCH](../usb/P100_MIDI命令常量.md#ga7fae224629121ad30f9f38241885452c)
- [UMP_MIDI_CONTROL_CHANGE](../usb/P100_MIDI命令常量.md#gad4b17d74027a541957c933074d0f2d1e)
- [UMP_MIDI_PROGRAM_CHANGE](../usb/P100_MIDI命令常量.md#gaad34de6aae0e22f5c84ef50e488e2d1a)
- [UMP_MIDI_CHAN_AFTERTOUCH](../usb/P100_MIDI命令常量.md#gaf5708894b80514023949e163f9687fb8)
- [UMP_MIDI_PITCH_BEND](../usb/P100_MIDI命令常量.md#gab11535e72a74baa71491264dd2c16192)
- [UMP_SYS_RT_COMMON](../usb/P098_通用MIDI数据包定义.md#ga06562acb0ec4d618d2e05b94c0a1bc4f)
- [UMP_SYS_MIDI_TIME_CODE](../usb/P102_MIDI系统消息状态.md#ga85394094ca6d908b7886adc4caceb671)
- [UMP_SYS_SONG_POSITION](../usb/P102_MIDI系统消息状态.md#ga254845a2c32a190b0bfc217025c5ad1d)
- [UMP_SYS_SONG_SELECT](../usb/P102_MIDI系统消息状态.md#ga1d27e0f6fffd7ec05f58b56be78d9a8d)
- [UMP_SYS_TUNE_REQUEST](../usb/P102_MIDI系统消息状态.md#ga4aa12e0cdb101a38b938876ebdcca64b)
- [UMP_SYS_TIMING_CLOCK](../usb/P102_MIDI系统消息状态.md#gae064f3f47a9387076f5045e12e6ef7b7)
- [UMP_SYS_START](../usb/P102_MIDI系统消息状态.md#ga368ad3719080979709699feb3d002dff)
- [UMP_SYS_CONTINUE](../usb/P102_MIDI系统消息状态.md#ga766b54e3caced69c147dbc94eb932595)
- [UMP_SYS_STOP](../usb/P102_MIDI系统消息状态.md#ga95542dda8f7f73f738c3ae298ca42f44)
- [UMP_SYS_ACTIVE_SENSING](../usb/P102_MIDI系统消息状态.md#gaeb794e3933a2488eadb5f57ba971f81d)
- [UMP_SYS_RESET](../usb/P102_MIDI系统消息状态.md#ga5bd5358ae1847774409216f4e246f6f4)
- [UMP_STREAM_FORMAT](../usb/P103_UMP流消息字段.md#gaa964f1d5ebc6ffe3d360f9f4a303d0c7)
- [UMP_STREAM_FORMAT_COMPLETE](../usb/P104_UMP流消息格式.md#ga1437c75d99f58d138ea1ff04d5012b11)
- [UMP_STREAM_FORMAT_START](../usb/P104_UMP流消息格式.md#ga145b3798cf8ada61a57feb6489aaa3f0)
- [UMP_STREAM_FORMAT_CONTINUE](../usb/P104_UMP流消息格式.md#ga8e84c4586cd1dcb5b0749669508608fd)
- [UMP_STREAM_FORMAT_END](../usb/P104_UMP流消息格式.md#gaf975fd5766fbddd0a3f1113c1d5c2fb1)
- [UMP_STREAM_STATUS](../usb/P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)
- [UMP_STREAM_STATUS_EP_DISCOVERY](../usb/P105_UMP流消息状态.md#gab753d923dd8a6045f85f5ac7032fd040)
- [UMP_STREAM_STATUS_EP_INFO](../usb/P105_UMP流消息状态.md#ga1ff08a079dd9b84aa297ca73043342db)
- [UMP_STREAM_STATUS_DEVICE_IDENT](../usb/P105_UMP流消息状态.md#gaa53b5c80022e1888515f2c0616d9cfc3)
- [UMP_STREAM_STATUS_EP_NAME](../usb/P105_UMP流消息状态.md#gac9673eeb745526fd27f0e213ee06caa5)
- [UMP_STREAM_STATUS_PROD_ID](../usb/P105_UMP流消息状态.md#ga0edc8d182d71946828609b964bae1da8)
- [UMP_STREAM_STATUS_CONF_REQ](../usb/P105_UMP流消息状态.md#gaf28a14d200e97003c248ca1ad452244a)
- [UMP_STREAM_STATUS_CONF_NOTIF](../usb/P105_UMP流消息状态.md#ga182a95d09f4bef5976a64e5e02938ff8)
- [UMP_STREAM_STATUS_FB_DISCOVERY](../usb/P105_UMP流消息状态.md#gae0e25c309feb67ea77046a7587017b07)
- [UMP_STREAM_STATUS_FB_INFO](../usb/P105_UMP流消息状态.md#ga4634c6db944bd4c582765f23fc7a4f35)
- [UMP_STREAM_STATUS_FB_NAME](../usb/P105_UMP流消息状态.md#gaabf613ea856aa266cfdf13a32f300eee)
- [UMP_STREAM_EP_DISCOVERY_FILTER](../usb/P103_UMP流消息字段.md#gacbefffaacf70b546d5b7055bcefe7f16)
- [UMP_EP_DISC_FILTER_EP_INFO](../usb/P106_UMP端点发现过滤位.md#ga6a234420b601ba9899b9a0c81e10daee)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [UMP_EP_DISC_FILTER_DEVICE_ID](../usb/P106_UMP端点发现过滤位.md#ga07a1a713e27f2e1d59531f51699e65c8)
- [UMP_EP_DISC_FILTER_EP_NAME](../usb/P106_UMP端点发现过滤位.md#gadc49c22e63a6119aa19fc655cbdd75f2)
- [UMP_EP_DISC_FILTER_PRODUCT_ID](../usb/P106_UMP端点发现过滤位.md#gad0a5a402d072dc843453cf4416dcb571)
- [UMP_EP_DISC_FILTER_STREAM_CFG](../usb/P106_UMP端点发现过滤位.md#ga72d2233a8760e3127bd7b4d133e12b3b)
- [UMP_STREAM_FB_DISCOVERY_FILTER](../usb/P103_UMP流消息字段.md#gac7134040f1026e2c4ee20286100b1312)
- [UMP_STREAM_FB_DISCOVERY_NUM](../usb/P103_UMP流消息字段.md#ga7a6a56afd9298976899b0b2100b79223)
- [UMP_FB_DISC_FILTER_INFO](../usb/P107_UMP功能块发现过滤位.md#gaf0bc0e4083f74cfea57a0c52f7b5b1f6)
- [UMP_FB_DISC_FILTER_NAME](../usb/P107_UMP功能块发现过滤位.md#ga3552456370892c941d2c76f7029e0306)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__comparator__infineon-autanalog-ptcomp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__misc__max2221x__max2221x.h_文件参考.md)
