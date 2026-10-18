---
id: learning.zephyr-docs.usb.api-142
title: 旧版USB音频头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__audio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_旧版USB音频头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__audio_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 142.1\_阅读说明与来源

译注：本页说明旧版USB音频设备类（USB Audio Device Class）接口，头文件以USB Audio v1.0文档为依据。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 音频设备类（USB Audio Device Class）的公共头文件。

```c
#include <zephyr/usb/usb_ch9.h>
```

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/net_buf.h>
```

```c
#include <zephyr/sys/util.h>
```

USB 音频设备类（USB Audio Device Class）的公共头文件。

本头文件遵循以下文档：

- USB 音频设备类定义（USB Device Class Definition for Audio Devices，audio10.pdf）。

以下补充文档也被视为 USB Audio v1.0 的组成部分：

- USB 音频数据格式类定义（USB Device Class Definition for Audio Data Formats，frmts10.pdf）。
- USB 终端类型类定义（USB Device Class Definition for Terminal Types，termt10.pdf）。

## 142.2\_数据结构（Data Structures）

<a id="r_usb_5Faudio_5Ffu_5Fevt"></a>

```c
struct usb_audio_fu_evt
```

功能单元（Feature Unit）事件结构。

相关声明：[usb_audio_fu_evt](P143_旧版USB音频功能单元事件.md)。

<a id="r_usb_5Faudio_5Fops"></a>

```c
struct usb_audio_ops
```

供用户应用与音频设备交互的音频回调（Audio Callback）。

相关声明：[usb_audio_ops](P144_旧版USB音频回调接口.md)。

## 142.3\_类型定义（Typedefs）

<a id="r_a8f289f2b4d0a7d3accdc6308cb5661e8"></a>

```c
typedef void(* usb_audio_data_request_cb_t) (const struct device *dev)
```

此回调类型通知应用：主机已请求设备数据，现在可以向主机（Host）发送数据。

相关声明：[usb_audio_data_request_cb_t](P142_旧版USB音频头文件接口.md#a8f289f2b4d0a7d3accdc6308cb5661e8)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a57bc8c499f03323db38f5604f8ebcda2"></a>

```c
typedef void(* usb_audio_data_completion_cb_t) (const struct device *dev, struct net_buf *buffer, size_t size)
```

此回调类型通知应用：数据已成功发送或接收。

相关声明：[usb_audio_data_completion_cb_t](P142_旧版USB音频头文件接口.md#a57bc8c499f03323db38f5604f8ebcda2)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_a692362e834622532b7be71d5e0bdc219"></a>

```c
typedef void(* usb_audio_feature_updated_cb_t) (const struct device *dev, const struct usb_audio_fu_evt *evt)
```

此回调类型通知应用：主机修改了设备已配置的某项功能。

相关声明：[usb_audio_feature_updated_cb_t](P142_旧版USB音频头文件接口.md#a692362e834622532b7be71d5e0bdc219)、[device](../device_reference/P002_设备对象结构.md)、[usb_audio_fu_evt](P143_旧版USB音频功能单元事件.md)。

## 142.4\_枚举（Enumerations）

<a id="r_a4885d280ebe68e42cf068524038ec582"></a>

```c
enum usb_audio_int_subclass_codes {
    USB_AUDIO_SUBCLASS_UNDEFINED = 0x00,
    USB_AUDIO_AUDIOCONTROL = 0x01,
    USB_AUDIO_AUDIOSTREAMING = 0x02,
    USB_AUDIO_MIDISTREAMING = 0x03
}
```

音频接口子类代码（Audio Interface Subclass Codes）。

相关声明：[usb_audio_int_subclass_codes](P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582)、[USB_AUDIO_SUBCLASS_UNDEFINED](P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2)、[USB_AUDIO_AUDIOCONTROL](P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac)、[USB_AUDIO_AUDIOSTREAMING](P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892)、[USB_AUDIO_MIDISTREAMING](P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2)。

<a id="r_ab5e6c883af53c089c7fcdee4d2249d9a"></a>

```c
enum usb_audio_cs_ac_int_desc_subtypes {
    USB_AUDIO_AC_DESCRIPTOR_UNDEFINED = 0x00,
    USB_AUDIO_HEADER = 0x01,
    USB_AUDIO_INPUT_TERMINAL = 0x02,
    USB_AUDIO_OUTPUT_TERMINAL = 0x03,
    USB_AUDIO_MIXER_UNIT = 0x04,
    USB_AUDIO_SELECTOR_UNIT = 0x05,
    USB_AUDIO_FEATURE_UNIT = 0x06,
    USB_AUDIO_PROCESSING_UNIT = 0x07,
    USB_AUDIO_EXTENSION_UNIT = 0x08
}
```

音频类专用的音频控制（Audio Control，AC）接口描述符子类型。

相关声明：[usb_audio_cs_ac_int_desc_subtypes](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9a)、[USB_AUDIO_AC_DESCRIPTOR_UNDEFINED](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d)、[USB_AUDIO_HEADER](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51)、[USB_AUDIO_INPUT_TERMINAL](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343)、[USB_AUDIO_OUTPUT_TERMINAL](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f)、[USB_AUDIO_MIXER_UNIT](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe)、[USB_AUDIO_SELECTOR_UNIT](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5)、[USB_AUDIO_FEATURE_UNIT](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7)、[USB_AUDIO_PROCESSING_UNIT](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab)、[USB_AUDIO_EXTENSION_UNIT](P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1)。

<a id="r_ade80a3c7e04049fd27e4e39269baaeeb"></a>

```c
enum usb_audio_cs_as_int_desc_subtypes {
    USB_AUDIO_AS_DESCRIPTOR_UNDEFINED = 0x00,
    USB_AUDIO_AS_GENERAL = 0x01,
    USB_AUDIO_FORMAT_TYPE = 0x02,
    USB_AUDIO_FORMAT_SPECIFIC = 0x03
}
```

音频类专用的音频流（Audio Streaming，AS）接口描述符子类型，参见 audio10.pdf 的表 A-6。

相关声明：[usb_audio_cs_as_int_desc_subtypes](P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeb)、[USB_AUDIO_AS_DESCRIPTOR_UNDEFINED](P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e)、[USB_AUDIO_AS_GENERAL](P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84)、[USB_AUDIO_FORMAT_TYPE](P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4)、[USB_AUDIO_FORMAT_SPECIFIC](P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a)。

<a id="r_ad6eb1c3ec75aef329ea973d1cb4dc6ad"></a>

```c
enum usb_audio_cs_req_codes {
    USB_AUDIO_REQUEST_CODE_UNDEFINED = 0x00,
    USB_AUDIO_SET_CUR = 0x01,
    USB_AUDIO_GET_CUR = 0x81,
    USB_AUDIO_SET_MIN = 0x02,
    USB_AUDIO_GET_MIN = 0x82,
    USB_AUDIO_SET_MAX = 0x03,
    USB_AUDIO_GET_MAX = 0x83,
    USB_AUDIO_SET_RES = 0x04,
    USB_AUDIO_GET_RES = 0x84,
    USB_AUDIO_SET_MEM = 0x05,
    USB_AUDIO_GET_MEM = 0x85,
    USB_AUDIO_GET_STAT = 0xFF
}
```

音频类专用请求代码（Audio Class-Specific Request Codes），参见 audio10.pdf 的表 A-9。

相关声明：[usb_audio_cs_req_codes](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ad)、[USB_AUDIO_REQUEST_CODE_UNDEFINED](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220)、[USB_AUDIO_SET_CUR](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d)、[USB_AUDIO_GET_CUR](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6)、[USB_AUDIO_SET_MIN](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab)、[USB_AUDIO_GET_MIN](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6)、[USB_AUDIO_SET_MAX](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707)、[USB_AUDIO_GET_MAX](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb)、[USB_AUDIO_SET_RES](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7)、[USB_AUDIO_GET_RES](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485)、[USB_AUDIO_SET_MEM](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0)、[USB_AUDIO_GET_MEM](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259)、[USB_AUDIO_GET_STAT](P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109)。

<a id="r_a4d49f239cc36daf8bd0cfa36c5fb75d2"></a>

```c
enum usb_audio_fucs {
    USB_AUDIO_FU_CONTROL_UNDEFINED = 0x00,
    USB_AUDIO_FU_MUTE_CONTROL = 0x01,
    USB_AUDIO_FU_VOLUME_CONTROL = 0x02,
    USB_AUDIO_FU_BASS_CONTROL = 0x03,
    USB_AUDIO_FU_MID_CONTROL = 0x04,
    USB_AUDIO_FU_TREBLE_CONTROL = 0x05,
    USB_AUDIO_FU_GRAPHIC_EQUALIZER_CONTROL = 0x06,
    USB_AUDIO_FU_AUTOMATIC_GAIN_CONTROL = 0x07,
    USB_AUDIO_FU_DELAY_CONTROL = 0x08,
    USB_AUDIO_FU_BASS_BOOST_CONTROL = 0x09,
    USB_AUDIO_FU_LOUDNESS_CONTROL = 0x0A
}
```

功能单元控制选择器（Feature Unit Control Selectors），参见 audio10.pdf 的表 A-11。

相关声明：[usb_audio_fucs](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2)、[USB_AUDIO_FU_CONTROL_UNDEFINED](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794)、[USB_AUDIO_FU_MUTE_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d)、[USB_AUDIO_FU_VOLUME_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8)、[USB_AUDIO_FU_BASS_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc)、[USB_AUDIO_FU_MID_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601)、[USB_AUDIO_FU_TREBLE_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89)、[USB_AUDIO_FU_GRAPHIC_EQUALIZER_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5)、[USB_AUDIO_FU_AUTOMATIC_GAIN_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f)、[USB_AUDIO_FU_DELAY_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da)、[USB_AUDIO_FU_BASS_BOOST_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3)、[USB_AUDIO_FU_LOUDNESS_CONTROL](P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d)。

<a id="r_ad73e9e9b72475496b6c483f78605e79e"></a>

```c
enum usb_audio_terminal_types {
    USB_AUDIO_USB_UNDEFINED = 0x0100,
    USB_AUDIO_USB_STREAMING = 0x0101,
    USB_AUDIO_USB_VENDOR_SPEC = 0x01FF,
    USB_AUDIO_IN_UNDEFINED = 0x0200,
    USB_AUDIO_IN_MICROPHONE = 0x0201,
    USB_AUDIO_IN_DESKTOP_MIC = 0x0202,
    USB_AUDIO_IN_PERSONAL_MIC = 0x0203,
    USB_AUDIO_IN_OM_DIR_MIC = 0x0204,
    USB_AUDIO_IN_MIC_ARRAY = 0x0205,
    USB_AUDIO_IN_PROC_MIC_ARRAY = 0x0205,
    USB_AUDIO_OUT_UNDEFINED = 0x0300,
    USB_AUDIO_OUT_SPEAKER = 0x0301,
    USB_AUDIO_OUT_HEADPHONES = 0x0302,
    USB_AUDIO_OUT_HEAD_AUDIO = 0x0303,
    USB_AUDIO_OUT_DESKTOP_SPEAKER = 0x0304,
    USB_AUDIO_OUT_ROOM_SPEAKER = 0x0305,
    USB_AUDIO_OUT_COMM_SPEAKER = 0x0306,
    USB_AUDIO_OUT_LOW_FREQ_SPEAKER = 0x0307,
    USB_AUDIO_IO_UNDEFINED = 0x0400,
    USB_AUDIO_IO_HANDSET = 0x0401,
    USB_AUDIO_IO_HEADSET = 0x0402,
    USB_AUDIO_IO_SPEAKERPHONE_ECHO_NONE = 0x0403,
    USB_AUDIO_IO_SPEAKERPHONE_ECHO_SUP = 0x0404,
    USB_AUDIO_IO_SPEAKERPHONE_ECHO_CAN = 0x0405
}
```

USB 终端类型（Terminal Types），参见 termt10.pdf 的表 2-1 至表 2-4。

相关声明：[usb_audio_terminal_types](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79e)、[USB_AUDIO_USB_UNDEFINED](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4)、[USB_AUDIO_USB_STREAMING](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661)、[USB_AUDIO_USB_VENDOR_SPEC](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486)、[USB_AUDIO_IN_UNDEFINED](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57)、[USB_AUDIO_IN_MICROPHONE](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d)、[USB_AUDIO_IN_DESKTOP_MIC](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a)、[USB_AUDIO_IN_PERSONAL_MIC](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749)、[USB_AUDIO_IN_OM_DIR_MIC](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b)、[USB_AUDIO_IN_MIC_ARRAY](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262)、[USB_AUDIO_IN_PROC_MIC_ARRAY](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86)、[USB_AUDIO_OUT_UNDEFINED](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0)、[USB_AUDIO_OUT_SPEAKER](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c)、[USB_AUDIO_OUT_HEADPHONES](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9)、[USB_AUDIO_OUT_HEAD_AUDIO](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73)、[USB_AUDIO_OUT_DESKTOP_SPEAKER](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795)、[USB_AUDIO_OUT_ROOM_SPEAKER](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213)、[USB_AUDIO_OUT_COMM_SPEAKER](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b)、[USB_AUDIO_OUT_LOW_FREQ_SPEAKER](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480)、[USB_AUDIO_IO_UNDEFINED](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8)、[USB_AUDIO_IO_HANDSET](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207)、[USB_AUDIO_IO_HEADSET](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e)、[USB_AUDIO_IO_SPEAKERPHONE_ECHO_NONE](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d)、[USB_AUDIO_IO_SPEAKERPHONE_ECHO_SUP](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6)、[USB_AUDIO_IO_SPEAKERPHONE_ECHO_CAN](P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14)。

<a id="r_acbdc8b284d108983fb204cbd679043bb"></a>

```c
enum usb_audio_direction {
    USB_AUDIO_IN = 0x00,
    USB_AUDIO_OUT = 0x01
}
```

音频设备方向（Audio Device Direction）。

相关声明：[usb_audio_direction](P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bb)、[USB_AUDIO_IN](P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd)、[USB_AUDIO_OUT](P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba)。

## 142.5\_函数（Functions）

<a id="r_af314d5beb1d16377855313d46148a86c"></a>

```c
size_t usb_audio_get_in_frame_size (const struct device *dev)
```

取得主机可接受的帧大小（Frame Size）。

相关声明：[usb_audio_get_in_frame_size](P142_旧版USB音频头文件接口.md#af314d5beb1d16377855313d46148a86c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a6a69824dadab0c36bb6a6ce378da8ba5"></a>

```c
void usb_audio_register (const struct device *dev, const struct usb_audio_ops *ops)
```

注册 USB 音频设备，使其可以使用。

相关声明：[usb_audio_register](P142_旧版USB音频头文件接口.md#a6a69824dadab0c36bb6a6ce378da8ba5)、[device](../device_reference/P002_设备对象结构.md)、[usb_audio_ops](P144_旧版USB音频回调接口.md)。

<a id="r_af1874c929638325e9e2a44da0e613041"></a>

```c
int usb_audio_send (const struct device *dev, struct net_buf *buffer, size_t len)
```

通过 USB 音频设备发送数据。

相关声明：[usb_audio_send](P142_旧版USB音频头文件接口.md#af1874c929638325e9e2a44da0e613041)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

## 142.6\_详细说明（Detailed Documentation）

<a id="a57bc8c499f03323db38f5604f8ebcda2"></a>

### 142.6.1\_`usb_audio_data_completion_cb_t`

```c
typedef void(* usb_audio_data_completion_cb_t) (const struct device *dev, struct net_buf *buffer, size_t size)
```

此回调类型通知应用：数据已成功发送或接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 触发此次回调的设备。 |
| `buffer` | 指向已成功发送或接收的 net_buf 数据块。如果应用使用 data_written_cb 和／或 data_received_cb 回调，则应用须自行释放缓冲区。 |
| `size` | 已成功发送或接收的数据量。 |

<a id="a8f289f2b4d0a7d3accdc6308cb5661e8"></a>

### 142.6.2\_`usb_audio_data_request_cb_t`

```c
typedef void(* usb_audio_data_request_cb_t) (const struct device *dev)
```

此回调类型通知应用：主机已请求设备数据，现在可以向主机（Host）发送数据。

发送数据时应使用 usb_audio_send() API 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 主机请求其数据的设备。 |

**注意（Note）**：用户也可以不使用此回调，而在每 1 ms 执行的任务中尝试发送。如果主机没有请求数据，每 1 ms 发送也可能失败并返回 -EAGAIN。

<a id="a692362e834622532b7be71d5e0bdc219"></a>

### 142.6.3\_`usb_audio_feature_updated_cb_t`

```c
typedef void(* usb_audio_feature_updated_cb_t) (const struct device *dev, const struct usb_audio_fu_evt *evt)
```

此回调类型通知应用：主机修改了设备已配置的某项功能。

适用于所有设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB 音频设备。 |
| `evt` | 指向供应用解析的事件。所指结构是临时对象，仅在本次回调执行期间有效。 |

**警告（Warning）**：主机可能不会使用全部已配置的功能。

<a id="ab5e6c883af53c089c7fcdee4d2249d9a"></a>

### 142.6.4\_`usb_audio_cs_ac_int_desc_subtypes`

```c
enum usb_audio_cs_ac_int_desc_subtypes
```

音频类专用的音频控制（Audio Control，AC）接口描述符子类型。

参见 audio10.pdf 的表 A-5。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_AC_DESCRIPTOR_UNDEFINED` |  |
| `USB_AUDIO_HEADER` |  |
| `USB_AUDIO_INPUT_TERMINAL` |  |
| `USB_AUDIO_OUTPUT_TERMINAL` |  |
| `USB_AUDIO_MIXER_UNIT` |  |
| `USB_AUDIO_SELECTOR_UNIT` |  |
| `USB_AUDIO_FEATURE_UNIT` |  |
| `USB_AUDIO_PROCESSING_UNIT` |  |
| `USB_AUDIO_EXTENSION_UNIT` |  |

<a id="ade80a3c7e04049fd27e4e39269baaeeb"></a>

### 142.6.5\_`usb_audio_cs_as_int_desc_subtypes`

```c
enum usb_audio_cs_as_int_desc_subtypes
```

音频类专用的音频流（Audio Streaming，AS）接口描述符子类型，参见 audio10.pdf 的表 A-6。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_AS_DESCRIPTOR_UNDEFINED` |  |
| `USB_AUDIO_AS_GENERAL` |  |
| `USB_AUDIO_FORMAT_TYPE` |  |
| `USB_AUDIO_FORMAT_SPECIFIC` |  |

<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ad"></a>

### 142.6.6\_`usb_audio_cs_req_codes`

```c
enum usb_audio_cs_req_codes
```

音频类专用请求代码（Audio Class-Specific Request Codes），参见 audio10.pdf 的表 A-9。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_REQUEST_CODE_UNDEFINED` |  |
| `USB_AUDIO_SET_CUR` |  |
| `USB_AUDIO_GET_CUR` |  |
| `USB_AUDIO_SET_MIN` |  |
| `USB_AUDIO_GET_MIN` |  |
| `USB_AUDIO_SET_MAX` |  |
| `USB_AUDIO_GET_MAX` |  |
| `USB_AUDIO_SET_RES` |  |
| `USB_AUDIO_GET_RES` |  |
| `USB_AUDIO_SET_MEM` |  |
| `USB_AUDIO_GET_MEM` |  |
| `USB_AUDIO_GET_STAT` |  |

<a id="acbdc8b284d108983fb204cbd679043bb"></a>

### 142.6.7\_`usb_audio_direction`

```c
enum usb_audio_direction
```

音频设备方向（Audio Device Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_IN` |  |
| `USB_AUDIO_OUT` |  |

<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2"></a>

### 142.6.8\_`usb_audio_fucs`

```c
enum usb_audio_fucs
```

功能单元控制选择器（Feature Unit Control Selectors），参见 audio10.pdf 的表 A-11。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_FU_CONTROL_UNDEFINED` |  |
| `USB_AUDIO_FU_MUTE_CONTROL` |  |
| `USB_AUDIO_FU_VOLUME_CONTROL` |  |
| `USB_AUDIO_FU_BASS_CONTROL` |  |
| `USB_AUDIO_FU_MID_CONTROL` |  |
| `USB_AUDIO_FU_TREBLE_CONTROL` |  |
| `USB_AUDIO_FU_GRAPHIC_EQUALIZER_CONTROL` |  |
| `USB_AUDIO_FU_AUTOMATIC_GAIN_CONTROL` |  |
| `USB_AUDIO_FU_DELAY_CONTROL` |  |
| `USB_AUDIO_FU_BASS_BOOST_CONTROL` |  |
| `USB_AUDIO_FU_LOUDNESS_CONTROL` |  |

<a id="a4885d280ebe68e42cf068524038ec582"></a>

### 142.6.9\_`usb_audio_int_subclass_codes`

```c
enum usb_audio_int_subclass_codes
```

音频接口子类代码（Audio Interface Subclass Codes）。

参见 audio10.pdf 的表 A-2。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_SUBCLASS_UNDEFINED` |  |
| `USB_AUDIO_AUDIOCONTROL` |  |
| `USB_AUDIO_AUDIOSTREAMING` |  |
| `USB_AUDIO_MIDISTREAMING` |  |

<a id="ad73e9e9b72475496b6c483f78605e79e"></a>

### 142.6.10\_`usb_audio_terminal_types`

```c
enum usb_audio_terminal_types
```

USB 终端类型（Terminal Types），参见 termt10.pdf 的表 2-1 至表 2-4。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_AUDIO_USB_UNDEFINED` | 未定义的 USB 终端（USB Undefined）。 |
| `USB_AUDIO_USB_STREAMING` | USB 流传输终端（USB Streaming）。 |
| `USB_AUDIO_USB_VENDOR_SPEC` | USB 厂商专用终端（USB Vendor Specific）。 |
| `USB_AUDIO_IN_UNDEFINED` | 未定义的输入终端（Input Undefined）。 |
| `USB_AUDIO_IN_MICROPHONE` | 麦克风（Microphone）。 |
| `USB_AUDIO_IN_DESKTOP_MIC` | 桌面麦克风（Desktop Microphone）。 |
| `USB_AUDIO_IN_PERSONAL_MIC` | 个人麦克风（Personal Microphone）。 |
| `USB_AUDIO_IN_OM_DIR_MIC` | 全向麦克风（Omnidirectional Microphone）。 |
| `USB_AUDIO_IN_MIC_ARRAY` | 麦克风阵列（Microphone Array）。 |
| `USB_AUDIO_IN_PROC_MIC_ARRAY` | 带处理功能的麦克风阵列（Processing Microphone Array）。 |
| `USB_AUDIO_OUT_UNDEFINED` | 未定义的输出终端（Output Undefined）。 |
| `USB_AUDIO_OUT_SPEAKER` | 扬声器（Speaker）。 |
| `USB_AUDIO_OUT_HEADPHONES` | 耳机（Headphones）。 |
| `USB_AUDIO_OUT_HEAD_AUDIO` | 头戴式显示器音频（Head-Mounted Display Audio）。 |
| `USB_AUDIO_OUT_DESKTOP_SPEAKER` | 桌面扬声器（Desktop Speaker）。 |
| `USB_AUDIO_OUT_ROOM_SPEAKER` | 房间扬声器（Room Speaker）。 |
| `USB_AUDIO_OUT_COMM_SPEAKER` | 通信扬声器（Communication Speaker）。 |
| `USB_AUDIO_OUT_LOW_FREQ_SPEAKER` | 低频效果扬声器（Low-Frequency Effects Speaker）。 |
| `USB_AUDIO_IO_UNDEFINED` | 未定义的双向终端（Bidirectional Undefined）。 |
| `USB_AUDIO_IO_HANDSET` | 手持听筒（Handset）。 |
| `USB_AUDIO_IO_HEADSET` | 耳麦（Headset）。 |
| `USB_AUDIO_IO_SPEAKERPHONE_ECHO_NONE` | 免提电话，无回声抑制（Speakerphone, No Echo Reduction）。 |
| `USB_AUDIO_IO_SPEAKERPHONE_ECHO_SUP` | 免提电话，具有回声抑制（Speakerphone, Echo Reduction）。 |
| `USB_AUDIO_IO_SPEAKERPHONE_ECHO_CAN` | 免提电话，具有回声消除（Speakerphone, Echo Cancellation）。 |

> 译注（源码核对）：原网页与本次保存的头文件都把USB_AUDIO_IN_MIC_ARRAY和USB_AUDIO_IN_PROC_MIC_ARRAY写为0x0205。本译文保留两项原值，不擅自根据名称推断并改写数值。

<a id="af314d5beb1d16377855313d46148a86c"></a>

### 142.6.11\_`usb_audio_get_in_frame_size()`

```c
size_t usb_audio_get_in_frame_size ( const struct device * dev)
```

取得主机可接受的帧大小（Frame Size）。

此函数返回主机期望输入设备提供的帧大小；返回值取决于输入设备的以下配置：

- 声道数量（Number of Channels）。
- 采样频率（Sampling Frequency）。
- 采样分辨率（Sample Resolution）。设备通过设备树覆盖文件（Devicetree Overlay）配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 需要查询帧大小的输入设备（Input Device）。 |

**已弃用（Deprecated）**：请改用[USB音频类2设备API（USB Audio Class 2 Device API）](P089_USB音频2设备API.md)。

**警告（Warning）**：不要对仅支持 OUT 的设备（耳机）使用此函数。对于仅支持 OUT 的设备，此函数应返回 0。

> 译注（源码核对）：当前函数直接返回设备数据中的in_frame_size，不与主机发起新的协商。该值来自配置；它不是收到任意主机请求后自动测得的帧长度。

<a id="a6a69824dadab0c36bb6a6ce378da8ba5"></a>

### 142.6.12\_`usb_audio_register()`

```c
void usb_audio_register ( const struct device * dev, const struct usb_audio_ops * ops )
```

注册 USB 音频设备，使其可以使用。

必须调用此函数，设备才能工作并响应所有相关请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB 音频设备。 |
| `ops` | USB 音频回调结构；这些回调用于通知用户当前发生的事件。 |

**已弃用（Deprecated）**：请改用[USB音频类2设备API（USB Audio Class 2 Device API）](P089_USB音频2设备API.md)。

> 译注（源码核对）：当前实现保留ops指针而不是复制回调表，因此回调表应在设备使用期间持续有效，例如采用示例中的静态对象。注册会将设备加入内部列表并把收发启用状态设为false；它不代替usb_enable()，源码也没有把重复注册作为无操作处理。

<a id="af1874c929638325e9e2a44da0e613041"></a>

### 142.6.13\_`usb_audio_send()`

```c
int usb_audio_send ( const struct device * dev, struct net_buf * buffer, size_t len )
```

通过 USB 音频设备发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 通过自身 ISO IN 等时输入端点发送数据的 USB 音频设备。 |
| `buffer` | 指向待发送的缓冲区。对于输入设备，用户负责管理缓冲区。发送出错时，用户必须决定丢弃缓冲区还是重新发送。成功发送后，如果应用提供 data_written_cb 回调，则将缓冲区交给该回调；否则自动释放。用户必须提供合适的 net_buf 数据块，尤其要确保其大小合适；可通过 usb_audio_get_in_frame_size() API 函数取得相关大小信息。 |
| `len` | 待发送数据的长度。 |

**已弃用（Deprecated）**：请改用[USB音频类2设备API（USB Audio Class 2 Device API）](P089_USB音频2设备API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负错误值。

> 译注（源码核对）：当前实现检查首个端点是否为IN、主机是否选择活动发送接口、len是否超过buffer->size；相应失败返回-EINVAL或-EAGAIN。通过检查后交给usb_transfer()，并使用USB_TRANS_NO_ZLP。返回0表示提交成功，完成后的缓冲区释放依赖完成回调路径；立即失败时仍由调用者处理缓冲区，不能在成功提交后立即释放。

## 142.7\_源码跟踪与使用边界

译注依据保存的[官方音频头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_audio.h)及[旧版音频实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/audio/audio.c)，摘要见[来源记录](../SOURCES.md)。当前头文件已将三个公开函数标为__deprecated，并指向[新版UAC2设备接口](P089_USB音频2设备API.md)；本页仍按官方网页展示保留旧声明。本仓库的[音频头文件](../../../include/zephyr/usb/class/usb_audio.h)和[实现](../../../subsys/usb/device/class/audio/audio.c)可用于相对路径跟踪，版本可能与网页不同。相关应用见[旧版耳麦示例](P138_旧版USB音频耳麦示例.md)与[旧版麦克风／耳机示例](P139_旧版USB麦克风与耳机示例.md)。本批未构建、播放、录音或进行USB硬件测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab"></a>
<a id="ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1"></a>
<a id="ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e"></a>
<a id="ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84"></a>
<a id="ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4"></a>
<a id="ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259"></a>
<a id="ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109"></a>
<a id="acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd"></a>
<a id="acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3"></a>
<a id="a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d"></a>
<a id="a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2"></a>
<a id="a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac"></a>
<a id="a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892"></a>
<a id="a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d"></a>
<a id="ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6"></a>
<a id="ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P141_旧版WebUSB浏览器演示.md) · [返回大纲](大纲.md) · [下一章](P143_旧版USB音频功能单元事件.md)
