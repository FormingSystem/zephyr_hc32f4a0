---
id: learning.zephyr-docs.network-core-model-reference.page-6
title: ieee802154_aux_security_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__aux__security__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_ieee802154\_aux\_security\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__aux__security__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

启用安全机制时位于寻址字段之后的辅助安全头（Auxiliary Security Header，ASH）。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

启用安全机制后位于寻址字段之后的辅助安全头（Auxiliary Security Header，ASH）。见第9.4节及图9-4。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a75a365c8c642f17aedc5c08754272c79"></a>

```c
struct ieee802154_security_control_field control
```

相关声明：[ieee802154_security_control_field](P043_ieee802154_security_control_field_结构体.md)、[control](#a75a365c8c642f17aedc5c08754272c79)。

安全控制字段（Security Control Field）。

<a id="r_a4c9113e6ce77856e09822866c281d5eb"></a>

```c
uint32_t frame_counter
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frame_counter](#a4c9113e6ce77856e09822866c281d5eb)。

帧计数器字段（Frame Counter Field），长度为4个八位组。

<a id="r_a7c7facc1f1b9fa5fedd94e9a6afe2f0b"></a>

```c
struct ieee802154_key_identifier_field kif
```

相关声明：[ieee802154_key_identifier_field](P033_ieee802154_key_identifier_field_结构体.md)、[kif](#a7c7facc1f1b9fa5fedd94e9a6afe2f0b)。

密钥标识符字段（Key Identifier Field）；长度取决于密钥标识符模式（Key Identifier Mode）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a75a365c8c642f17aedc5c08754272c79"></a>

### `control`

```c
struct ieee802154_security_control_field ieee802154_aux_security_hdr::control
```

安全控制字段（Security Control Field）。

<a id="a4c9113e6ce77856e09822866c281d5eb"></a>

### `frame_counter`

```c
uint32_t ieee802154_aux_security_hdr::frame_counter
```

帧计数器字段（Frame Counter Field），长度为4个八位组。

<a id="a7c7facc1f1b9fa5fedd94e9a6afe2f0b"></a>

### `kif`

```c
struct ieee802154_key_identifier_field ieee802154_aux_security_hdr::kif
```

密钥标识符字段（Key Identifier Field）；长度取决于密钥标识符模式（Key Identifier Mode）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [ieee802154_security_control_field](P043_ieee802154_security_control_field_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ieee802154_key_identifier_field](P033_ieee802154_key_identifier_field_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_ieee802154_attr_value_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_ieee802154_beacon_结构体.md)
