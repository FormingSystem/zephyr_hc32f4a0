---
id: learning.zephyr-docs.usb.api-144
title: 旧版USB音频回调接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__audio__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第144章\_旧版USB音频回调接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__audio__ops.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 144.1\_阅读说明与来源

译注：本页说明旧版USB音频设备类（USB Audio Device Class）接口，头文件以USB Audio v1.0文档为依据。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

供用户应用与音频设备交互的音频回调（Audio Callback）。

```c
#include <zephyr/usb/class/usb_audio.h>
```

供用户应用与音频设备交互的音频回调（Audio Callback）。

usb_audio_ops 结构包含与 USB 音频设备交互所需的全部相关回调。每个回调均可选，可以保留为 NULL；这不会破坏协议栈，但可能使 USB 音频设备无法发挥作用。根据设备类型，为了按预期发送或接收数据，某些回调实际上是必需的。更多信息见上述各回调的说明。

## 144.2\_数据成员（Data Fields）

<a id="r_a6ee19a7aef47561f14981b7e7ebd8ac7"></a>

```c
usb_audio_data_request_cb_t data_request_cb
```

可以发送数据时调用的回调。

相关声明：[usb_audio_data_request_cb_t](P142_旧版USB音频头文件接口.md#a8f289f2b4d0a7d3accdc6308cb5661e8)、[data_request_cb](P144_旧版USB音频回调接口.md#a6ee19a7aef47561f14981b7e7ebd8ac7)。

<a id="r_a2752018597ba5bd4e9a80d1ae650bf8b"></a>

```c
usb_audio_data_completion_cb_t data_written_cb
```

具备发送能力的设备成功写出数据时调用的回调。

相关声明：[usb_audio_data_completion_cb_t](P142_旧版USB音频头文件接口.md#a57bc8c499f03323db38f5604f8ebcda2)、[data_written_cb](P144_旧版USB音频回调接口.md#a2752018597ba5bd4e9a80d1ae650bf8b)。

<a id="r_a483af21f54537bef1a6ae3be2cd3717d"></a>

```c
usb_audio_data_completion_cb_t data_received_cb
```

具备接收能力的设备成功收到数据时调用的回调。

相关声明：[usb_audio_data_completion_cb_t](P142_旧版USB音频头文件接口.md#a57bc8c499f03323db38f5604f8ebcda2)、[data_received_cb](P144_旧版USB音频回调接口.md#a483af21f54537bef1a6ae3be2cd3717d)。

<a id="r_a861823185efb5c9a06b900799adb9efb"></a>

```c
usb_audio_feature_updated_cb_t feature_update_cb
```

主机修改功能时调用的回调。

相关声明：[usb_audio_feature_updated_cb_t](P142_旧版USB音频头文件接口.md#a692362e834622532b7be71d5e0bdc219)、[feature_update_cb](P144_旧版USB音频回调接口.md#a861823185efb5c9a06b900799adb9efb)。

## 144.3\_详细说明（Detailed Documentation）

<a id="a483af21f54537bef1a6ae3be2cd3717d"></a>

### 144.3.1\_`data_received_cb`

```c
usb_audio_data_completion_cb_t usb_audio_ops::data_received_cb
```

具备接收能力的设备成功收到数据时调用的回调。

适用于耳麦和耳机；麦克风不使用此回调。

> 译注（源码核对）：当前接收路径只有在该回调存在时才分配缓冲区并调用usb_read()；读取失败或长度为0时由驱动释放，成功后交给应用回调。没有接收回调不等价于应用仍能自动取得音频数据。

<a id="a6ee19a7aef47561f14981b7e7ebd8ac7"></a>

### 144.3.2\_`data_request_cb`

```c
usb_audio_data_request_cb_t usb_audio_ops::data_request_cb
```

可以发送数据时调用的回调。

<a id="a2752018597ba5bd4e9a80d1ae650bf8b"></a>

### 144.3.3\_`data_written_cb`

```c
usb_audio_data_completion_cb_t usb_audio_ops::data_written_cb
```

具备发送能力的设备成功写出数据时调用的回调。

适用于耳麦和麦克风；耳机不使用此回调。

<a id="a861823185efb5c9a06b900799adb9efb"></a>

### 144.3.4\_`feature_update_cb`

```c
usb_audio_feature_updated_cb_t usb_audio_ops::feature_update_cb
```

主机修改功能时调用的回调。

> 译注（源码核对）：当前实现处理静音和音量控制，只在成功的主机到设备SET_CUR请求后通知应用；读出当前值并不会触发相同的功能更新事件。其他已枚举控制选择器不代表此实现全部支持。

## 144.4\_源码跟踪与使用边界

译注依据保存的[官方音频头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_audio.h)及[旧版音频实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/audio/audio.c)，摘要见[来源记录](../SOURCES.md)。当前头文件已将三个公开函数标为__deprecated，并指向[新版UAC2设备接口](P089_USB音频2设备API.md)；本页仍按官方网页展示保留旧声明。本仓库的[音频头文件](../../../include/zephyr/usb/class/usb_audio.h)和[实现](../../../subsys/usb/device/class/audio/audio.c)可用于相对路径跟踪，版本可能与网页不同。相关应用见[旧版耳麦示例](P138_旧版USB音频耳麦示例.md)与[旧版麦克风／耳机示例](P139_旧版USB麦克风与耳机示例.md)。本批未构建、播放、录音或进行USB硬件测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P143_旧版USB音频功能单元事件.md) · [返回大纲](大纲.md) · [下一章](P145_USBBOS支持API.md)
