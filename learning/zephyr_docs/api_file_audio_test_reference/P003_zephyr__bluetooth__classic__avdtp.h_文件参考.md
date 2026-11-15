---
id: learning.zephyr-docs.api-file-audio-test-reference.page-3
title: zephyr__bluetooth__classic__avdtp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_bluetooth\_\_classic\_\_avdtp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音视频分发传输协议（Audio/Video Distribution Transport Protocol）的头文件。

查看此文件的源码。

<a id="details"></a>

音视频分发传输协议（Audio/Video Distribution Transport Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Favdtp_5Fsep_5Finfo"></a>

```c
struct bt_avdtp_sep_info
```

相关声明：[bt_avdtp_sep_info](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md)。

AVDTP 流端点信息。

<a id="r_bt_5Favdtp_5Fsep_5Fops"></a>

```c
struct bt_avdtp_sep_ops
```

相关声明：[bt_avdtp_sep_ops](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md)。

AVDTP 流端点操作结构体（SEP Operations Structure）。

<a id="r_bt_5Favdtp_5Fsep"></a>

```c
struct bt_avdtp_sep
```

相关声明：[bt_avdtp_sep](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md)。

AVDTP 流端点（Stream End Point）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_a5d8b4d0a44eafbfbab57decd950da669"></a>

```c
#define AVDTP_VERSION_1_3 0x0103
```

相关声明：[AVDTP_VERSION_1_3](#a5d8b4d0a44eafbfbab57decd950da669)。

音视频分发传输协议（AVDTP）版本 1.3 的值。

<a id="r_ac48da324b40d53e9c290bf3f41de8741"></a>

```c
#define AVDTP_VERSION AVDTP_VERSION_1_3
```

相关声明：[AVDTP_VERSION](#ac48da324b40d53e9c290bf3f41de8741)、[AVDTP_VERSION_1_3](#a5d8b4d0a44eafbfbab57decd950da669)。

Zephyr 使用的 AVDTP 版本（Version）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_affc7226c1b7795a3d2f51cb4ffaf6d21"></a>

```c
enum bt_avdtp_err_code { BT_AVDTP_SUCCESS = 0x00 , BT_AVDTP_TIME_OUT = 0xFF , BT_AVDTP_BAD_HEADER_FORMAT = 0x01 , BT_AVDTP_BAD_LENGTH = 0x11 , BT_AVDTP_BAD_ACP_SEID = 0x12 , BT_AVDTP_SEP_IN_USE = 0x13 , BT_AVDTP_SEP_NOT_IN_USE = 0x14 , BT_AVDTP_BAD_SERV_CATEGORY = 0x17 , BT_AVDTP_BAD_PAYLOAD_FORMAT = 0x18 , BT_AVDTP_NOT_SUPPORTED_COMMAND = 0x19 , BT_AVDTP_INVALID_CAPABILITIES = 0x1A , BT_AVDTP_BAD_RECOVERY_TYPE = 0x22 , BT_AVDTP_BAD_MEDIA_TRANSPORT_FORMAT = 0x23 , BT_AVDTP_BAD_RECOVERY_FORMAT = 0x25 , BT_AVDTP_BAD_ROHC_FORMAT = 0x26 , BT_AVDTP_BAD_CP_FORMAT = 0x27 , BT_AVDTP_BAD_MULTIPLEXING_FORMAT = 0x28 , BT_AVDTP_UNSUPPORTED_CONFIGURATION = 0x29 , BT_AVDTP_BAD_STATE = 0x31 }
```

相关声明：[bt_avdtp_err_code](#affc7226c1b7795a3d2f51cb4ffaf6d21)、[BT_AVDTP_SUCCESS](#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af)、[BT_AVDTP_TIME_OUT](#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a)、[BT_AVDTP_BAD_HEADER_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f)、[BT_AVDTP_BAD_LENGTH](#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9)、[BT_AVDTP_BAD_ACP_SEID](#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064)、[BT_AVDTP_SEP_IN_USE](#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8)、[BT_AVDTP_SEP_NOT_IN_USE](#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445)、[BT_AVDTP_BAD_SERV_CATEGORY](#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6)、[BT_AVDTP_BAD_PAYLOAD_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0)、[BT_AVDTP_NOT_SUPPORTED_COMMAND](#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75)、[BT_AVDTP_INVALID_CAPABILITIES](#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20)、[BT_AVDTP_BAD_RECOVERY_TYPE](#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee)、[BT_AVDTP_BAD_MEDIA_TRANSPORT_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35)、[BT_AVDTP_BAD_RECOVERY_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099)、[BT_AVDTP_BAD_ROHC_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7)、[BT_AVDTP_BAD_CP_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da)、[BT_AVDTP_BAD_MULTIPLEXING_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14)、[BT_AVDTP_UNSUPPORTED_CONFIGURATION](#affc7226c1b7795a3d2f51cb4ffaf6d21a57665911c0fa0f58660407c05a523320)、[BT_AVDTP_BAD_STATE](#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818)。

AVDTP 错误码（Error Code）。

<a id="r_a28b828df32df5a40e8487dc4dee78757"></a>

```c
enum bt_avdtp_sep_type { BT_AVDTP_SOURCE = 0 , BT_AVDTP_SINK = 1 }
```

相关声明：[bt_avdtp_sep_type](#a28b828df32df5a40e8487dc4dee78757)、[BT_AVDTP_SOURCE](#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f)、[BT_AVDTP_SINK](#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9)。

流端点类型（Stream End Point Type）。

<a id="r_a6e9f13217ede2687e206b6a8cbd9137f"></a>

```c
enum bt_avdtp_media_type { BT_AVDTP_AUDIO = 0x00 , BT_AVDTP_VIDEO = 0x01 , BT_AVDTP_MULTIMEDIA = 0x02 }
```

相关声明：[bt_avdtp_media_type](#a6e9f13217ede2687e206b6a8cbd9137f)、[BT_AVDTP_AUDIO](#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)、[BT_AVDTP_VIDEO](#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee)、[BT_AVDTP_MULTIMEDIA](#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4)。

流端点媒体类型（Stream End Point Media Type）。

<a id="r_a8427dfa4dcd3fe8ac6eaf2471bad7e51"></a>

```c
enum bt_avdtp_service_category { BT_AVDTP_SERVICE_MEDIA_TRANSPORT = 0x01 , BT_AVDTP_SERVICE_REPORTING = 0x02 , BT_AVDTP_SERVICE_MEDIA_RECOVERY = 0x03 , BT_AVDTP_SERVICE_CONTENT_PROTECTION = 0x04 , BT_AVDTP_SERVICE_HEADER_COMPRESSION = 0x05 , BT_AVDTP_SERVICE_MULTIPLEXING = 0x06 , BT_AVDTP_SERVICE_MEDIA_CODEC = 0x07 , BT_AVDTP_SERVICE_DELAY_REPORTING = 0x08 }
```

相关声明：[bt_avdtp_service_category](#a8427dfa4dcd3fe8ac6eaf2471bad7e51)、[BT_AVDTP_SERVICE_MEDIA_TRANSPORT](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c)、[BT_AVDTP_SERVICE_REPORTING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37)、[BT_AVDTP_SERVICE_MEDIA_RECOVERY](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902)、[BT_AVDTP_SERVICE_CONTENT_PROTECTION](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642)、[BT_AVDTP_SERVICE_HEADER_COMPRESSION](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73)、[BT_AVDTP_SERVICE_MULTIPLEXING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439)、[BT_AVDTP_SERVICE_MEDIA_CODEC](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e)、[BT_AVDTP_SERVICE_DELAY_REPORTING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0)。

服务类别类型（Service Category Type）。

<a id="r_a4cf69d936236918ec0fc7adecb6080e3"></a>

```c
enum bt_avdtp_recovery_type { BT_AVDTP_RECOVERY_TYPE_FORBIDDEN = 0x00 , BT_ADVTP_RECOVERY_TYPE_RFC2733 = 0x01 }
```

相关声明：[bt_avdtp_recovery_type](#a4cf69d936236918ec0fc7adecb6080e3)、[BT_AVDTP_RECOVERY_TYPE_FORBIDDEN](#a4cf69d936236918ec0fc7adecb6080e3a9c31ee783c40c6f9ce82975915b2bf7d)、[BT_ADVTP_RECOVERY_TYPE_RFC2733](#a4cf69d936236918ec0fc7adecb6080e3adbf6d71be0000eb3fec4a4d27dc73ce0)。

服务类别中的恢复能力类型（Recovery Capabilities Type）。

## 3.4\_详细说明（Detailed Documentation）

<a id="ac48da324b40d53e9c290bf3f41de8741"></a>

### `AVDTP_VERSION`

```c
#define AVDTP_VERSION AVDTP_VERSION_1_3
```

Zephyr 使用的 AVDTP 版本（Version）。

<a id="a5d8b4d0a44eafbfbab57decd950da669"></a>

### `AVDTP_VERSION_1_3`

```c
#define AVDTP_VERSION_1_3 0x0103
```

音视频分发传输协议（AVDTP）版本 1.3 的值。

<a id="affc7226c1b7795a3d2f51cb4ffaf6d21"></a>

### `bt_avdtp_err_code`

```c
enum bt_avdtp_err_code
```

AVDTP 错误码（Error Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVDTP_SUCCESS` | 响应成功（Success），此值不来自 AVDTP 规范。 |
| `BT_AVDTP_TIME_OUT` | 请求超时且未收到响应（Timeout without Response），此值不来自 AVDTP 规范。 |
| `BT_AVDTP_BAD_HEADER_FORMAT` | 请求数据包头部格式错误（Header Format Error）。 |
| `BT_AVDTP_BAD_LENGTH` | 请求数据包长度与预期长度不匹配。 |
| `BT_AVDTP_BAD_ACP_SEID` | 请求命令指定了无效、不可寻址的接收方流端点标识符（ACP SEID）。 |
| `BT_AVDTP_SEP_IN_USE` | 流端点（SEP）正在使用。 |
| `BT_AVDTP_SEP_NOT_IN_USE` | 流端点（SEP）未被使用。 |
| `BT_AVDTP_BAD_SERV_CATEGORY` | 请求数据包中的服务类别值（Service Category）未在 AVDTP 中定义。 |
| `BT_AVDTP_BAD_PAYLOAD_FORMAT` | 请求命令的负载格式（Payload Format）不正确。 |
| `BT_AVDTP_NOT_SUPPORTED_COMMAND` | 设备不支持所请求的命令（Command）。 |
| `BT_AVDTP_INVALID_CAPABILITIES` | 重新配置命令（Reconfigure Command）试图重新配置流端点（SEP）的传输服务 codec_cap；仅允许重新配置应用服务 codec_cap（Application Service）。 |
| `BT_AVDTP_BAD_RECOVERY_TYPE` | 所请求的恢复类型（Recovery Type）未在 AVDTP 中定义。 |
| `BT_AVDTP_BAD_MEDIA_TRANSPORT_FORMAT` | 媒体传输能力（Media Transport Capability）的格式不正确。 |
| `BT_AVDTP_BAD_RECOVERY_FORMAT` | 恢复服务能力（Recovery Service Capability）的格式不正确。 |
| `BT_AVDTP_BAD_ROHC_FORMAT` | 头部压缩服务能力（Header Compression Service Capability）的格式不正确。 |
| `BT_AVDTP_BAD_CP_FORMAT` | 内容保护服务能力（Content Protection Service Capability）的格式不正确。 |
| `BT_AVDTP_BAD_MULTIPLEXING_FORMAT` | 复用服务能力（Multiplexing Service Capability）的格式不正确。 |
| `BT_AVDTP_UNSUPPORTED_CONFIGURATION` | 不支持该配置（Configuration）。 |
| `BT_AVDTP_BAD_STATE` | 表示接收方（ACP）状态机处于无法处理该信号的无效状态。这也包括发起方（INT）收到某命令请求、而它当前正等待同一命令响应的情况。 |

<a id="a6e9f13217ede2687e206b6a8cbd9137f"></a>

### `bt_avdtp_media_type`

```c
enum bt_avdtp_media_type
```

流端点媒体类型（Stream End Point Media Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVDTP_AUDIO` | 音频媒体类型（Audio Media Type）。 |
| `BT_AVDTP_VIDEO` | 视频媒体类型（Video Media Type）。 |
| `BT_AVDTP_MULTIMEDIA` | 多媒体类型（Multimedia Media Type）。 |

<a id="a4cf69d936236918ec0fc7adecb6080e3"></a>

### `bt_avdtp_recovery_type`

```c
enum bt_avdtp_recovery_type
```

服务类别中的恢复能力类型（Recovery Capabilities Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVDTP_RECOVERY_TYPE_FORBIDDEN` | 禁止（Forbidden）。 |
| `BT_ADVTP_RECOVERY_TYPE_RFC2733` | RFC 2733 规范。 |

<a id="a28b828df32df5a40e8487dc4dee78757"></a>

### `bt_avdtp_sep_type`

```c
enum bt_avdtp_sep_type
```

流端点类型（Stream End Point Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVDTP_SOURCE` | 源角色（Source Role）。 |
| `BT_AVDTP_SINK` | 接收端角色（Sink Role）。 |

<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51"></a>

### `bt_avdtp_service_category`

```c
enum bt_avdtp_service_category
```

服务类别类型（Service Category Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVDTP_SERVICE_MEDIA_TRANSPORT` | 媒体传输（Media Transport）。 |
| `BT_AVDTP_SERVICE_REPORTING` | 报告（Reporting）。 |
| `BT_AVDTP_SERVICE_MEDIA_RECOVERY` | 恢复（Recovery）。 |
| `BT_AVDTP_SERVICE_CONTENT_PROTECTION` | 内容保护（Content Protection）。 |
| `BT_AVDTP_SERVICE_HEADER_COMPRESSION` | 头部压缩（Header Compression）。 |
| `BT_AVDTP_SERVICE_MULTIPLEXING` | 复用（Multiplexing）。 |
| `BT_AVDTP_SERVICE_MEDIA_CODEC` | 媒体编解码器（Media Codec）。 |
| `BT_AVDTP_SERVICE_DELAY_REPORTING` | 延迟报告（Delay Reporting）。 |


## 3.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P018_avdtp.h_源码浏览.md)
- [bt_avdtp_sep_info](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md)
- [bt_avdtp_sep_ops](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md)
- [bt_avdtp_sep](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a57665911c0fa0f58660407c05a523320"></a>
<a id="affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818"></a>
<a id="a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58"></a>
<a id="a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee"></a>
<a id="a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4"></a>
<a id="a4cf69d936236918ec0fc7adecb6080e3a9c31ee783c40c6f9ce82975915b2bf7d"></a>
<a id="a4cf69d936236918ec0fc7adecb6080e3adbf6d71be0000eb3fec4a4d27dc73ce0"></a>
<a id="a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f"></a>
<a id="a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e"></a>
<a id="a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0"></a>

---

[上一章](P002_zephyr__dt-bindings__dma__ameba_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__audio__cap.h_文件参考.md)
