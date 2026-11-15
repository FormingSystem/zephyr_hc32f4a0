---
id: learning.zephyr-docs.network-core-model-reference.page-20
title: ieee802154_gts_dir_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__dir.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_ieee802154\_gts\_dir\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__dir.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信标载荷中的保证时隙方向（GTS Direction）字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

信标载荷（Beacon Payload）中的保证时隙方向（GTS Direction）字段。见第7.3.1.5节及图7-10。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a8f3e09bed02abb0b69234b10fb9604f7"></a>

```c
uint8_t reserved: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a8f3e09bed02abb0b69234b10fb9604f7)。

保留字段（Reserved），应为0。

<a id="r_abdff100f062a94d5c1c90f2590e69053"></a>

```c
uint8_t mask: 7
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mask](#abdff100f062a94d5c1c90f2590e69053)。

保证时隙（GTS）描述符的方向掩码（Direction Mask），每个描述符占一位。

## 20.2\_详细说明（Detailed Documentation）

<a id="abdff100f062a94d5c1c90f2590e69053"></a>

### `mask`

```c
uint8_t ieee802154_gts_dir::mask
```

保证时隙（GTS）描述符的方向掩码（Direction Mask），每个描述符占一位。

<a id="a8f3e09bed02abb0b69234b10fb9604f7"></a>

### `reserved`

```c
uint8_t ieee802154_gts_dir::reserved
```

保留字段（Reserved），应为0。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_ieee802154_gts_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_ieee802154_gts_request_结构体.md)
