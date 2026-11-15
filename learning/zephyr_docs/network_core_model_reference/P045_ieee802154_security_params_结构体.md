---
id: learning.zephyr-docs.network-core-model-reference.page-45
title: ieee802154_security_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_ieee802154\_security\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全参数（Security Parameters）。

```c
#include <zephyr/net/ieee802154_mgmt.h>
```

<a id="details"></a>

安全参数（Security Parameters）。用于设置链路层安全（Link-Layer Security），见第9.5节表9-9及表9-10。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_ae47ed5df4c70bfd4a28319d35f34c940"></a>

```c
uint8_t key [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key](#ae47ed5df4c70bfd4a28319d35f34c940)。

密钥字段：secKeyDescriptor.secKey。

<a id="r_a03ba0953eaea5035346b35e0555beb9c"></a>

```c
uint8_t key_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_len](#a03ba0953eaea5035346b35e0555beb9c)。

为符合标准，密钥长度（Key Length）必须为16字节。

<a id="r_a5b6248a76d95ede67495f765d4d35b57"></a>

```c
uint8_t key_mode: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_mode](#a5b6248a76d95ede67495f765d4d35b57)。

密钥标识模式字段：secKeyIdMode。

<a id="r_a50b7b0cbb4151234747c41d41e6fd656"></a>

```c
uint8_t level: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[level](#a50b7b0cbb4151234747c41d41e6fd656)。

构造辅助安全头（Auxiliary Security Header）时，用于替代每帧专用的SecurityLevel参数。

## 45.2\_详细说明（Detailed Documentation）

<a id="ae47ed5df4c70bfd4a28319d35f34c940"></a>

### `key`

```c
uint8_t ieee802154_security_params::key[16]
```

密钥字段：secKeyDescriptor.secKey。

<a id="a03ba0953eaea5035346b35e0555beb9c"></a>

### `key_len`

```c
uint8_t ieee802154_security_params::key_len
```

为符合标准，密钥长度（Key Length）必须为16字节。

<a id="a5b6248a76d95ede67495f765d4d35b57"></a>

### `key_mode`

```c
uint8_t ieee802154_security_params::key_mode
```

密钥标识模式字段：secKeyIdMode。

<a id="a50b7b0cbb4151234747c41d41e6fd656"></a>

### `level`

```c
uint8_t ieee802154_security_params::level
```

构造辅助安全头（Auxiliary Security Header）时，用于替代每帧专用的SecurityLevel参数。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_mgmt.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_ieee802154_security_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_net_buf_结构体.md)
