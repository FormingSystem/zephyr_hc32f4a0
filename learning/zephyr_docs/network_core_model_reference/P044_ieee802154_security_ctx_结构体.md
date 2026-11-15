---
id: learning.zephyr-docs.network-core-model-reference.page-44
title: ieee802154_security_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_ieee802154\_security\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接口级安全属性（Interface-Level Security Attributes），见第9.5节。

```c
#include <zephyr/net/ieee802154.h>
```

<a id="details"></a>

接口级安全属性（Interface-Level Security Attributes），见第9.5节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_adc4ce1ddf15b8b0bc4f283747b858b02"></a>

```c
uint32_t frame_counter
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frame_counter](#adc4ce1ddf15b8b0bc4f283747b858b02)。

接口级出站帧计数器（Outgoing Frame Counter），见第9.5节表9-8的secFrameCounter。

<a id="r_a3478b9a5430e12ca2c5641e1417a43d4"></a>

```c
uint8_t key [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key](#a3478b9a5430e12ca2c5641e1417a43d4)。

接口级帧加密安全密钥材料（Security Key Material）。

<a id="r_a1665374abce017c4b60e5c2085b19d8f"></a>

```c
uint8_t key_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_len](#a1665374abce017c4b60e5c2085b19d8f)。

接口级安全密钥材料（Security Key Material）的长度，单位为字节。

<a id="r_a65d1ca01bf7ed917a008591c8be0ca19"></a>

```c
uint8_t level: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[level](#a65d1ca01bf7ed917a008591c8be0ca19)。

帧安全等级（Frame Security Level），可能值定义见第9.4.2.2节表9-6。

<a id="r_afc41da04241f4fcc11e9d9f7728315d9"></a>

```c
uint8_t key_mode: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_mode](#afc41da04241f4fcc11e9d9f7728315d9)。

帧安全密钥模式（Frame Security Key Mode）。

## 44.2\_详细说明（Detailed Documentation）

<a id="adc4ce1ddf15b8b0bc4f283747b858b02"></a>

### `frame_counter`

```c
uint32_t ieee802154_security_ctx::frame_counter
```

接口级出站帧计数器（Outgoing Frame Counter），见第9.5节表9-8的secFrameCounter。

仅在驱动没有实现逐密钥帧计数器（Key-Specific Frame Counters）时使用。

<a id="a3478b9a5430e12ca2c5641e1417a43d4"></a>

### `key`

```c
uint8_t ieee802154_security_ctx::key[16]
```

接口级帧加密安全密钥材料（Security Key Material）。

当前原生第二层（Native L2）仅支持单个secKeySource，见第9.5节表9-9，并配合secKeyMode为0的隐式密钥模式（Implicit Key Mode）使用，见第9.4.2.3节表9-7。

**警告（Warning）**：警告（Warning）：这已不符合2015年及更新版本的标准；未来需要扩展，才能完全符合安全过程要求（Security Procedure Compliance）。

<a id="a1665374abce017c4b60e5c2085b19d8f"></a>

### `key_len`

```c
uint8_t ieee802154_security_ctx::key_len
```

接口级安全密钥材料（Security Key Material）的长度，单位为字节。

<a id="afc41da04241f4fcc11e9d9f7728315d9"></a>

### `key_mode`

```c
uint8_t ieee802154_security_ctx::key_mode
```

帧安全密钥模式（Frame Security Key Mode）。

目前仅部分支持隐式密钥模式（Implicit Key Mode），见第9.4.2.3节表9-7的secKeyMode。

**警告（Warning）**：警告（Warning）：这已不符合2015年及更新版本的标准；未来需要扩展，才能完全符合安全过程要求（Security Procedure Compliance）。

<a id="a65d1ca01bf7ed917a008591c8be0ca19"></a>

### `level`

```c
uint8_t ieee802154_security_ctx::level
```

帧安全等级（Frame Security Level），可能值定义见第9.4.2.2节表9-6。

**警告（Warning）**：警告（Warning）：当前原生第二层（Native L2）允许为全部帧类型、命令和信息元素配置一个共同的安全等级。这已不符合2015年及更新版本的标准；未来需要扩展，才能完全符合安全过程要求（Security Procedure Compliance）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_ieee802154_security_control_field_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_ieee802154_security_params_结构体.md)
