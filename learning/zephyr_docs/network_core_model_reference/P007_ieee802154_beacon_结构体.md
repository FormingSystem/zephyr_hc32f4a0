---
id: learning.zephyr-docs.network-core-model-reference.page-7
title: ieee802154_beacon_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__beacon.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_ieee802154\_beacon\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__beacon.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信标载荷（Beacon Payload）的固定部分，即超帧规范和GTS规范。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

信标载荷（Beacon Payload）的固定部分，即超帧规范与保证时隙规范（Superframe Specification / GTS Specification）。按第7.3.1节，后面还跟有GTS列表、GTS方向和待处理地址字段，见图7-6。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a1afd2b6d448a3c1dd4dfd471068f55ed"></a>

```c
struct ieee802154_beacon_sf sf
```

相关声明：[ieee802154_beacon_sf](P008_ieee802154_beacon_sf_结构体.md)、[sf](#a1afd2b6d448a3c1dd4dfd471068f55ed)。

超帧规范字段（Superframe Specification Field）。

<a id="r_a959331440b0fcdb24b4b624b607cdf3e"></a>

```c
struct ieee802154_gts_spec gts
```

相关声明：[ieee802154_gts_spec](P022_ieee802154_gts_spec_结构体.md)、[gts](#a959331440b0fcdb24b4b624b607cdf3e)。

保证时隙规范字段（GTS Specification Field），此布局中始终存在。

## 7.2\_详细说明（Detailed Documentation）

<a id="a959331440b0fcdb24b4b624b607cdf3e"></a>

### `gts`

```c
struct ieee802154_gts_spec ieee802154_beacon::gts
```

保证时隙规范字段（GTS Specification Field），此布局中始终存在。

<a id="a1afd2b6d448a3c1dd4dfd471068f55ed"></a>

### `sf`

```c
struct ieee802154_beacon_sf ieee802154_beacon::sf
```

超帧规范字段（Superframe Specification Field）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [ieee802154_beacon_sf](P008_ieee802154_beacon_sf_结构体.md)
- [ieee802154_gts_spec](P022_ieee802154_gts_spec_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_ieee802154_aux_security_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_ieee802154_beacon_sf_结构体.md)
