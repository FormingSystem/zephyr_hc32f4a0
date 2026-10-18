---
id: learning.zephyr-docs.network-application-model-reference.page-53
title: mqtt_binstr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__binstr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_mqtt\_binstr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__binstr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制字符串（Binary Strings）的抽象。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

二进制字符串（Binary Strings）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a1f61872edd09941155f60a242e582ff7"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a1f61872edd09941155f60a242e582ff7)。

指向二进制流（Binary Stream）的指针。

<a id="r_abcc36b6c59c3da740a6b352fe846fd5f"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#abcc36b6c59c3da740a6b352fe846fd5f)。

二进制流（Binary Stream）的长度。

## 53.2\_详细说明（Detailed Documentation）

<a id="a1f61872edd09941155f60a242e582ff7"></a>

### `data`

```c
uint8_t* mqtt_binstr::data
```

指向二进制流（Binary Stream）的指针。

<a id="abcc36b6c59c3da740a6b352fe846fd5f"></a>

### `len`

```c
uint32_t mqtt_binstr::len
```

二进制流（Binary Stream）的长度。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_mqtt_auth_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_mqtt_client_结构体.md)
