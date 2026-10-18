---
id: learning.zephyr-docs.network-core-model-reference.page-1
title: ieee802154_address_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ieee802154\_address\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAC寻址字段（Addressing Fields）中的短地址值或扩展地址值。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

MAC寻址字段（Addressing Fields）中的短地址值或扩展地址值。布局与第7.2.2节的地址字段一致；存在扩展地址时，使用柔性成员保存其8个八位组。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a51e1a3f14fbd7cccfdca20056eb9b1a4"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#a3fecbe4e7ad6a32d57af1fbdaca5c881)。

16位短地址（Short Address）。

<a id="r_a452acdc37b6d7257580687c761f71714"></a>

```c
uint8_t ext_addr [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_addr](#ac954ef5b107997dbb953a0efae865ab1)。

64位扩展地址（Extended Address）的起始位置，共8个八位组。

<a id="r_aa8ae402eee69586ca8ca6b59f7c2da63"></a>

```c
};
```

地址字段（Address Field）中的短地址或扩展地址。

## 1.2\_详细说明（Detailed Documentation）

<a id="aa8ae402eee69586ca8ca6b59f7c2da63"></a>

### `[union]`

```c
union { ... } ieee802154_address
```

地址字段（Address Field）中的短地址或扩展地址。

根据寻址模式（Addressing Mode）互斥，见第7.2.2节。

<a id="ac954ef5b107997dbb953a0efae865ab1"></a>

### `ext_addr`

```c
uint8_t ieee802154_address::ext_addr[0]
```

64位扩展地址（Extended Address）的起始位置，共8个八位组。

<a id="a3fecbe4e7ad6a32d57af1fbdaca5c881"></a>

### `short_addr`

```c
uint16_t ieee802154_address::short_addr
```

16位短地址（Short Address）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_address](P001_ieee802154_address_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_ieee802154_address_field_结构体.md)
