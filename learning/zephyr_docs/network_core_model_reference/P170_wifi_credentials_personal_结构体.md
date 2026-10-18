---
id: learning.zephyr-docs.network-core-model-reference.page-170
title: wifi_credentials_personal_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__personal.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第170章\_wifi\_credentials\_personal\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__personal.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi个人模式凭据（Personal Credentials）的条目。

```c
#include <zephyr/net/wifi_credentials.h>
```

<a id="details"></a>

Wi‑Fi 个人凭据条目（Wi-Fi Personal credentials entry）。注意（Note）：仅包含头部和密码。对于预共享密钥（PSK）安全模式，密码连同 `NULL` 终止符最多可占 `WIFI_PSK_MAX_LEN` 字节；对于对等实体同时认证（SAE）安全模式，长度上限可达 `CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 170.1\_数据成员（Data Fields）

<a id="r_a40f13f70ee0dd797d31b643cc754440c"></a>

```c
struct wifi_credentials_header header
```

相关声明：[wifi_credentials_header](P169_wifi_credentials_header_结构体.md)、[header](#a40f13f70ee0dd797d31b643cc754440c)。

头部（Header）。

<a id="r_a4a8201ecec087203b69ade5d7547538c"></a>

```c
char password [MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)]
```

相关声明：[password](#a4a8201ecec087203b69ade5d7547538c)、[MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)、[WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)。

密码／预共享密钥（Password/PSK）。

<a id="r_a627104585a2f6d58e2f899563c2993ad"></a>

```c
size_t password_len
```

相关声明：[password_len](#a627104585a2f6d58e2f899563c2993ad)。

密码长度（Password length）。

## 170.2\_详细说明（Detailed Documentation）

<a id="a40f13f70ee0dd797d31b643cc754440c"></a>

### `header`

```c
struct wifi_credentials_header wifi_credentials_personal::header
```

头部（Header）。

<a id="a4a8201ecec087203b69ade5d7547538c"></a>

### `password`

```c
char wifi_credentials_personal::password[MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)]
```

密码／预共享密钥（Password/PSK）。

<a id="a627104585a2f6d58e2f899563c2993ad"></a>

### `password_len`

```c
size_t wifi_credentials_personal::password_len
```

密码长度（Password length）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_credentials.h`

## 170.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h_source.html)
- [wifi_credentials_header](P169_wifi_credentials_header_结构体.md)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P169_wifi_credentials_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P171_wifi_eap_cipher_config_结构体.md)
