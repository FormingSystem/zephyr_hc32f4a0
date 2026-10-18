---
id: learning.zephyr-docs.network-core-model-reference.page-53
title: net_config_ssh_key_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__config__ssh__key.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_net\_config\_ssh\_key\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__config__ssh__key.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含设备上sshd所用的密钥配置数据（Key Configuration Data）。

```c
#include <zephyr/net/net_config.h>
```

<a id="details"></a>

包含设备上sshd所用的密钥配置数据（Key Configuration Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_af44b05c8460c0657ea5c55e8860dee7e"></a>

```c
const char * key_name
```

相关声明：[key_name](#af44b05c8460c0657ea5c55e8860dee7e)。

SSH密钥名称（Key Name）。

<a id="r_a823de7fc7e367493d8d9047cceda820a"></a>

```c
uint8_t * key_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_buf](#a823de7fc7e367493d8d9047cceda820a)。

加载和保存密钥（Keys）的临时缓冲区。

<a id="r_a0c657f31a4d81cd74a86c6792372309a"></a>

```c
size_t key_buf_len
```

相关声明：[key_buf_len](#a0c657f31a4d81cd74a86c6792372309a)。

密钥缓冲区（Key Buffer）的大小，单位为字节。

<a id="r_acacf33b3c455cf690a7eee7279facb27"></a>

```c
int key_id
```

相关声明：[key_id](#acacf33b3c455cf690a7eee7279facb27)。

密钥标识（Key ID）。

<a id="r_aed44f6ce3979e24a064f26eb71186733"></a>

```c
enum ssh_host_key_type key_type
```

相关声明：[ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)、[key_type](#aed44f6ce3979e24a064f26eb71186733)。

密钥类型（Key Type）。

<a id="r_ad076498fe79bb8ecad52a78b694b17cb"></a>

```c
int key_bits
```

相关声明：[key_bits](#ad076498fe79bb8ecad52a78b694b17cb)。

密钥大小（Key Size），单位为位。

<a id="r_a38c70f14300a67b42bc452f219d35f69"></a>

```c
bool is_private
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_private](#a38c70f14300a67b42bc452f219d35f69)。

是否为私钥（Private Key）。

## 53.2\_详细说明（Detailed Documentation）

<a id="a38c70f14300a67b42bc452f219d35f69"></a>

### `is_private`

```c
bool net_config_ssh_key::is_private
```

是否为私钥（Private Key）。

<a id="ad076498fe79bb8ecad52a78b694b17cb"></a>

### `key_bits`

```c
int net_config_ssh_key::key_bits
```

密钥大小（Key Size），单位为位。

<a id="a823de7fc7e367493d8d9047cceda820a"></a>

### `key_buf`

```c
uint8_t* net_config_ssh_key::key_buf
```

加载和保存密钥（Keys）的临时缓冲区。

<a id="a0c657f31a4d81cd74a86c6792372309a"></a>

### `key_buf_len`

```c
size_t net_config_ssh_key::key_buf_len
```

密钥缓冲区（Key Buffer）的大小，单位为字节。

用于确定加载和保存密钥所需的缓冲区大小。

<a id="acacf33b3c455cf690a7eee7279facb27"></a>

### `key_id`

```c
int net_config_ssh_key::key_id
```

密钥标识（Key ID）。

<a id="af44b05c8460c0657ea5c55e8860dee7e"></a>

### `key_name`

```c
const char* net_config_ssh_key::key_name
```

SSH密钥名称（Key Name）。

保存或加载密钥时，用于识别密钥。密钥名称（Key Name）不能包含空格。

<a id="aed44f6ce3979e24a064f26eb71186733"></a>

### `key_type`

```c
enum ssh_host_key_type net_config_ssh_key::key_type
```

密钥类型（Key Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_config.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/net/net_config.h](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_net_cmsghdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_net_config_ssh_password_auth_结构体.md)
