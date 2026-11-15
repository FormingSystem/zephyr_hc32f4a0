---
id: learning.zephyr-docs.usb.api-143
title: 旧版USB音频功能单元事件
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__audio__fu__evt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_旧版USB音频功能单元事件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__audio__fu__evt.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 143.1\_阅读说明与来源

译注：本页说明旧版USB音频设备类（USB Audio Device Class）接口，头文件以USB Audio v1.0文档为依据。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

功能单元（Feature Unit）事件结构。

```c
#include <zephyr/usb/class/usb_audio.h>
```

功能单元（Feature Unit）事件结构。

当主机修改设备的某项功能时，feature_update_cb 使用此事件结构通知应用。

## 143.2\_数据成员（Data Fields）

<a id="r_a5baf5d4e2a39337dc9c21c4465d5ad8e"></a>

```c
enum usb_audio_direction dir
```

发生变化的设备方向。

相关声明：[usb_audio_direction](P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bb)、[dir](P143_旧版USB音频功能单元事件.md#a5baf5d4e2a39337dc9c21c4465d5ad8e)。

<a id="r_a1cb4849aae8b9a4e667ed126e9bce26b"></a>

```c
enum usb_audio_fucs cs
```

发生变化的功能控制选择器。

相关声明：[usb_audio_fucs](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2)、[cs](P143_旧版USB音频功能单元事件.md#a1cb4849aae8b9a4e667ed126e9bce26b)。

<a id="r_a9313b39f178c8a86d680a950ce505713"></a>

```c
uint8_t channel
```

发生变化的设备声道。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](P143_旧版USB音频功能单元事件.md#a9313b39f178c8a86d680a950ce505713)。

<a id="r_a6ef19bf7d37c3d636edba243dac8ecb2"></a>

```c
uint8_t val_len
```

val 字段的长度。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[val_len](P143_旧版USB音频功能单元事件.md#a6ef19bf7d37c3d636edba243dac8ecb2)。

<a id="r_a47c6c7c00fac32a04bffd251d715dc39"></a>

```c
const void * val
```

已设置的功能值。

相关声明：[val](P143_旧版USB音频功能单元事件.md#a47c6c7c00fac32a04bffd251d715dc39)。

## 143.3\_详细说明（Detailed Documentation）

<a id="a9313b39f178c8a86d680a950ce505713"></a>

### 143.3.1\_`channel`

```c
uint8_t usb_audio_fu_evt::channel
```

发生变化的设备声道。

值为 0xFF 时，表示所有声道均发生变化。

> 译注（源码核对）：上方0xFF语义按头文件原注释翻译。当前控制请求实现先检查ch >= ch_cnt，再把请求中的声道号写入事件；没有单独的0xFF广播分支，因此不能仅凭注释认为主机发送0xFF一定被接受。

<a id="a1cb4849aae8b9a4e667ed126e9bce26b"></a>

### 143.3.2\_`cs`

```c
enum usb_audio_fucs usb_audio_fu_evt::cs
```

发生变化的功能控制选择器。

<a id="a5baf5d4e2a39337dc9c21c4465d5ad8e"></a>

### 143.3.3\_`dir`

```c
enum usb_audio_direction usb_audio_fu_evt::dir
```

发生变化的设备方向。

仅适用于耳麦设备。

<a id="a47c6c7c00fac32a04bffd251d715dc39"></a>

### 143.3.4\_`val`

```c
const void* usb_audio_fu_evt::val
```

已设置的功能值。

> 译注（源码核对）：当前静音与音量处理将val指向驱动内部控制值。evt结构本身由栈上临时对象传入回调；需要异步处理时，应在回调期间按cs和val_len复制所需数据，不保留临时evt指针，也不要假定val指向独立且永久不变的副本。

<a id="a6ef19bf7d37c3d636edba243dac8ecb2"></a>

### 143.3.5\_`val_len`

```c
uint8_t usb_audio_fu_evt::val_len
```

val 字段的长度。

## 143.4\_源码跟踪与使用边界

译注依据保存的[官方音频头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_audio.h)及[旧版音频实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/audio/audio.c)，摘要见[来源记录](../SOURCES.md)。当前头文件已将三个公开函数标为__deprecated，并指向[新版UAC2设备接口](P089_USB音频2设备API.md)；本页仍按官方网页展示保留旧声明。本仓库的[音频头文件](../../../include/zephyr/usb/class/usb_audio.h)和[实现](../../../subsys/usb/device/class/audio/audio.c)可用于相对路径跟踪，版本可能与网页不同。相关应用见[旧版耳麦示例](P138_旧版USB音频耳麦示例.md)与[旧版麦克风／耳机示例](P139_旧版USB麦克风与耳机示例.md)。本批未构建、播放、录音或进行USB硬件测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P142_旧版USB音频头文件接口.md) · [返回大纲](大纲.md) · [下一章](P144_旧版USB音频回调接口.md)
