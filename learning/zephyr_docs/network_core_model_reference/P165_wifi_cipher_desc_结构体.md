---
id: learning.zephyr-docs.network-core-model-reference.page-165
title: wifi_cipher_desc_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__cipher__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_wifi\_cipher\_desc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__cipher__desc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

密码算法能力与名称说明（Cipher Capability and Name Description）。

```c
#include <zephyr/net/wifi.h>
```

<a id="details"></a>

密码算法能力与名称说明（Cipher Capability and Name Description）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 165.1\_数据成员（Data Fields）

<a id="r_a6751019bb6da3032ca2f7bc42a3469e3"></a>

```c
unsigned int capa
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[capa](#a6751019bb6da3032ca2f7bc42a3469e3)。

密码算法能力（Cipher capability）。

<a id="r_a9396239f38613b151232a4c5f3d66a8f"></a>

```c
char * name
```

相关声明：[name](#a9396239f38613b151232a4c5f3d66a8f)。

密码算法名称字符串（Cipher name string）。

## 165.2\_详细说明（Detailed Documentation）

<a id="a6751019bb6da3032ca2f7bc42a3469e3"></a>

### `capa`

```c
unsigned int wifi_cipher_desc::capa
```

密码算法能力（Cipher capability）。

<a id="a9396239f38613b151232a4c5f3d66a8f"></a>

### `name`

```c
char* wifi_cipher_desc::name
```

密码算法名称字符串（Cipher name string）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi.h`

## 165.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P164_wifi_channel_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P166_wifi_config_params_结构体.md)
