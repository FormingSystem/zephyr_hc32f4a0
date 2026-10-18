---
id: learning.zephyr-docs.network-core-model-reference.page-166
title: wifi_config_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__config__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_wifi\_config\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__config__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi站点（STA）的配置参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi站点（STA）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 166.1\_数据成员（Data Fields）

<a id="r_aada77f3f6f5909ebefb699d7252bb74c"></a>

```c
enum wifi_config_param type
```

相关声明：[wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)、[type](#aada77f3f6f5909ebefb699d7252bb74c)。

用于标识不同站点参数（STA parameters）的参数。

<a id="r_a3a05f8b09eb2a74913c394f28fe7ab79"></a>

```c
int okc
```

相关声明：[okc](#a3a05f8b09eb2a74913c394f28fe7ab79)。

用于机会式密钥缓存（Opportunistic key caching）的参数。

## 166.2\_详细说明（Detailed Documentation）

<a id="a3a05f8b09eb2a74913c394f28fe7ab79"></a>

### `okc`

```c
int wifi_config_params::okc
```

用于机会式密钥缓存（Opportunistic key caching）的参数。

<a id="aada77f3f6f5909ebefb699d7252bb74c"></a>

### `type`

```c
enum wifi_config_param wifi_config_params::type
```

用于标识不同站点参数（STA parameters）的参数。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 166.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P165_wifi_cipher_desc_结构体.md) · [返回大纲](大纲.md) · [下一章](P167_wifi_connect_req_params_结构体.md)
