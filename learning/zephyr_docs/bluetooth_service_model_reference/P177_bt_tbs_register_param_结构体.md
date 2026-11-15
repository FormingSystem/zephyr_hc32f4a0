---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-177
title: bt_tbs_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_bt\_tbs\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

注册电话承载服务（Telephone Bearer Service）的参数。

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

<a id="details"></a>

注册电话承载服务（Telephone Bearer Service）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 177.1\_数据成员（Data Fields）

<a id="r_a8cf7713269e8bb193c61be01d6971922"></a>

```c
char * provider_name
```

相关声明：[provider_name](#a8cf7713269e8bb193c61be01d6971922)。

提供方名称，例如蜂窝服务提供商的名称。

<a id="r_ab7a0dc41a9e4c898ffd1afaffdfae51d"></a>

```c
char * uci
```

相关声明：[uci](#ab7a0dc41a9e4c898ffd1afaffdfae51d)。

承载的统一呼叫方标识符（Uniform Caller Identifier，UCI）。

<a id="r_a4ffe59cd6d00b9b45db304b17efa22b0"></a>

```c
char * uri_schemes_supported
```

相关声明：[uri_schemes_supported](#a4ffe59cd6d00b9b45db304b17efa22b0)。

此承载支持的统一资源标识符（Uniform Resource Identifier，URI）方案，以 UTF-8 字符串表示。

<a id="r_a54352a512eeb209d0254a8f395647f87"></a>

```c
enum bt_bearer_tech technology
```

相关声明：[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)、[technology](#a54352a512eeb209d0254a8f395647f87)。

承载使用的技术（technology）。

<a id="r_aa38a646b7121b555846f7acea9bc9365"></a>

```c
bool gtbs
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gtbs](#aa38a646b7121b555846f7acea9bc9365)。

是否将此承载注册为通用电话承载（Generic Telephone Bearer）服务器。

<a id="r_af88bfd0ac0e83f94e9e467064b4c6c32"></a>

```c
bool authorization_required
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[authorization_required](#af88bfd0ac0e83f94e9e467064b4c6c32)。

应用是否需要对通话的变更进行授权。

<a id="r_a004fc8f70cff59acf0122135bdd27065"></a>

```c
uint16_t optional_opcodes
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[optional_opcodes](#a004fc8f70cff59acf0122135bdd27065)。

承载支持的可选操作码（optional supported opcodes）。

## 177.2\_详细说明（Detailed Documentation）

<a id="af88bfd0ac0e83f94e9e467064b4c6c32"></a>

### `authorization_required`

```c
bool bt_tbs_register_param::authorization_required
```

应用是否需要对通话的变更进行授权。

如果设为 `false`，服务将自动接受客户端的写入请求。

<a id="aa38a646b7121b555846f7acea9bc9365"></a>

### `gtbs`

```c
bool bt_tbs_register_param::gtbs
```

是否将此承载注册为通用电话承载（Generic Telephone Bearer）服务器。

必须先注册通用电话承载服务（GTBS），然后才能注册任何非 GTBS 服务。只能注册一个 GTBS。

<a id="a004fc8f70cff59acf0122135bdd27065"></a>

### `optional_opcodes`

```c
uint16_t bt_tbs_register_param::optional_opcodes
```

承载支持的可选操作码（optional supported opcodes）。

参见 `BT_TBS_OPTIONAL_OPCODE_*` 取值。

<a id="a8cf7713269e8bb193c61be01d6971922"></a>

### `provider_name`

```c
char* bt_tbs_register_param::provider_name
```

提供方名称，例如蜂窝服务提供商的名称。

<a id="a54352a512eeb209d0254a8f395647f87"></a>

### `technology`

```c
enum bt_bearer_tech bt_tbs_register_param::technology
```

承载使用的技术（technology）。

<a id="ab7a0dc41a9e4c898ffd1afaffdfae51d"></a>

### `uci`

```c
char* bt_tbs_register_param::uci
```

承载的统一呼叫方标识符（Uniform Caller Identifier，UCI）。

参见蓝牙已分配编号（Bluetooth Assigned Numbers）中的统一呼叫方标识符（Uniform Caller Identifiers）表。

<a id="a4ffe59cd6d00b9b45db304b17efa22b0"></a>

### `uri_schemes_supported`

```c
char* bt_tbs_register_param::uri_schemes_supported
```

此承载支持的统一资源标识符（Uniform Resource Identifier，URI）方案，以 UTF-8 字符串表示。

可能的取值参见 https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml 。若使用多个值，必须用逗号分隔，例如 `"tel,skype"`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tbs.h`

## 177.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P176_bt_tbs_instance_结构体.md) · [返回大纲](大纲.md) · [下一章](P178_bt_tmap_cb_结构体.md)
