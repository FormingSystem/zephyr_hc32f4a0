---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-10
title: bt_bap_ascs_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__ascs__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_bap\_ascs\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__ascs__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存 ASE 控制点通知（ASE Control Point Notification）字段值的结构体。

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

<a id="details"></a>

保存 ASE 控制点通知（ASE Control Point Notification）字段值的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a8ea364298f7e3e784b7878215db63d91"></a>

```c
enum bt_bap_ascs_rsp_code code
```

相关声明：[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[code](#a8ea364298f7e3e784b7878215db63d91)。

响应码（Response Code）字段的值。

```c
union {
```

<a id="r_af8dedd2f0f00093f4cfaa594d1750f01"></a>

```c
enum bt_bap_ascs_reason reason
```

相关声明：[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)、[reason](#a138532bc40f60547c56d8b108ad44d1e)。

响应原因（Response Reason）。

<a id="r_a96e99236e7f1fa601405db36ba637c16"></a>

```c
enum bt_audio_metadata_type metadata_type
```

相关声明：[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)、[metadata_type](#a736f44864015244a8b48a859eff6b902)。

响应元数据类型（Response Metadata Type）。

<a id="r_af3f7fda04ebefbe15f70918c293f4e89"></a>

```c
};
```

原因（Reason）字段的值。

## 10.2\_详细说明（Detailed Documentation）

<a id="af3f7fda04ebefbe15f70918c293f4e89"></a>

### `[union]`

```c
union { ... } bt_bap_ascs_rsp
```

原因（Reason）字段的值。

此值的含义取决于响应码（Response Code）字段。

<a id="a8ea364298f7e3e784b7878215db63d91"></a>

### `code`

```c
enum bt_bap_ascs_rsp_code bt_bap_ascs_rsp::code
```

响应码（Response Code）字段的值。

接受以下响应码：

- `BT_BAP_ASCS_RSP_CODE_SUCCESS`
- `BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_CONF_REJECTED`
- `BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED`
- `BT_BAP_ASCS_RSP_CODE_NO_MEM`
- `BT_BAP_ASCS_RSP_CODE_UNSPECIFIED`

<a id="a736f44864015244a8b48a859eff6b902"></a>

### `metadata_type`

```c
enum bt_audio_metadata_type bt_bap_ascs_rsp::metadata_type
```

响应元数据类型（Response Metadata Type）。

如果响应码是以下值之一：

- `BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED`：必须使用元数据类型（Metadata Type）的值。

<a id="a138532bc40f60547c56d8b108ad44d1e"></a>

### `reason`

```c
enum bt_bap_ascs_reason bt_bap_ascs_rsp::reason
```

响应原因（Response Reason）。

如果响应码是以下值之一：

- `BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_CONF_REJECTED`：可以使用 `bt_bap_ascs_reason` 中的所有值。

如果响应码是以下值之一：

- `BT_BAP_ASCS_RSP_CODE_SUCCESS`
- `BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED`
- `BT_BAP_ASCS_RSP_CODE_NO_MEM`
- `BT_BAP_ASCS_RSP_CODE_UNSPECIFIED`：只能使用 `BT_BAP_ASCS_REASON_NONE`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/ascs.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html)
- [bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)
- [bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)
- [BT_BAP_ASCS_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)
- [BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)
- [BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)
- [BT_BAP_ASCS_RSP_CODE_CONF_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)
- [BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)
- [BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)
- [BT_BAP_ASCS_RSP_CODE_NO_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)
- [BT_BAP_ASCS_RSP_CODE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)
- [BT_BAP_ASCS_REASON_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_bt_audio_codec_octets_per_codec_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_bap_base_codec_id_结构体.md)
