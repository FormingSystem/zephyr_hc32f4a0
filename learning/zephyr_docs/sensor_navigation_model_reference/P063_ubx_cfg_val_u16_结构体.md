---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-63
title: ubx_cfg_val_u16_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u16.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_ubx\_cfg\_val\_u16\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u16.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_a32e877f1e2f60b209fbcdd057aa82c4f"></a>

```c
struct ubx_cfg_val_hdr hdr
```

相关声明：[ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)、[hdr](#a32e877f1e2f60b209fbcdd057aa82c4f)。

<a id="r_a87a9c181318e297935bb1eb65093d4a8"></a>

```c
uint32_t key
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[key](#a87a9c181318e297935bb1eb65093d4a8)。

<a id="r_a6226f1b8f4cb89cb318c07ff8ddcbbde"></a>

```c
uint16_t value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a6226f1b8f4cb89cb318c07ff8ddcbbde)。

## 63.2\_详细说明（Detailed Documentation）

<a id="a32e877f1e2f60b209fbcdd057aa82c4f"></a>

### `hdr`

```c
struct ubx_cfg_val_hdr ubx_cfg_val_u16::hdr
```

<a id="a87a9c181318e297935bb1eb65093d4a8"></a>

### `key`

```c
uint32_t ubx_cfg_val_u16::key
```

<a id="a6226f1b8f4cb89cb318c07ff8ddcbbde"></a>

### `value`

```c
uint16_t ubx_cfg_val_u16::value
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_ubx_cfg_val_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_ubx_cfg_val_u32_结构体.md)
