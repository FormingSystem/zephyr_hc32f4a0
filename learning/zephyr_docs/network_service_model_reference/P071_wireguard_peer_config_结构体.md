---
id: learning.zephyr-docs.network-service-model-reference.page-71
title: wireguard_peer_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__peer__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_wireguard\_peer\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__peer__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WireGuard对端配置（Peer Configuration）信息。

```c
#include <zephyr/net/wireguard.h>
```

<a id="details"></a>

WireGuard 对端配置（peer configuration）信息，保存 WireGuard 虚拟专用网络（VPN）对端连接信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a9ae02999964a23bdcd008648f99067b1"></a>

```c
const char * public_key
```

相关声明：[public_key](#a9ae02999964a23bdcd008648f99067b1)。

Base64 格式的公钥（public key）。

<a id="r_a9632752c8cecccee550548d9b1c3ba97"></a>

```c
const uint8_t * preshared_key
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[preshared_key](#a9632752c8cecccee550548d9b1c3ba97)。

可选的预共享密钥（pre-shared key），长度为 32 字节；不使用时设为 `NULL`。

<a id="r_a67b63a434cf1d5147dcf988e85b7b958"></a>

```c
uint8_t timestamp [(sizeof(uint64_t)+sizeof(uint32_t))]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[timestamp](#a67b63a434cf1d5147dcf988e85b7b958)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

握手期间已观察到的最大时间戳，用于防止重放（replay）。

<a id="r_ab31a019c4af3e819f06c02171237ccba"></a>

```c
struct net_sockaddr_storage endpoint_ip
```

相关声明：[endpoint_ip](#ab31a019c4af3e819f06c02171237ccba)。

端点地址（endpoint address），在连接时使用。

<a id="r_aca7a334729c726198894e22a2cdb446c"></a>

```c
struct wireguard_allowed_ip allowed_ip [WIREGUARD_MAX_SRC_IPS]
```

相关声明：[wireguard_allowed_ip](P070_wireguard_allowed_ip_结构体.md)、[allowed_ip](#aca7a334729c726198894e22a2cdb446c)。

允许的 IP 地址。

<a id="r_a8728365d722ac2bb857cbf4e9eb82d97"></a>

```c
int keepalive_interval
```

相关声明：[keepalive_interval](#a8728365d722ac2bb857cbf4e9eb82d97)。

此对端的默认保活时间（keep-alive time），单位为秒。

## 71.2\_详细说明（Detailed Documentation）

<a id="aca7a334729c726198894e22a2cdb446c"></a>

### `allowed_ip`

```c
struct wireguard_allowed_ip wireguard_peer_config::allowed_ip[WIREGUARD_MAX_SRC_IPS]
```

允许的 IP 地址。

<a id="ab31a019c4af3e819f06c02171237ccba"></a>

### `endpoint_ip`

```c
struct net_sockaddr_storage wireguard_peer_config::endpoint_ip
```

端点地址（endpoint address），在连接时使用。

<a id="a8728365d722ac2bb857cbf4e9eb82d97"></a>

### `keepalive_interval`

```c
int wireguard_peer_config::keepalive_interval
```

此对端的默认保活时间（keep-alive time），单位为秒。

设为 0 可使用默认值。

<a id="a9632752c8cecccee550548d9b1c3ba97"></a>

### `preshared_key`

```c
const uint8_t* wireguard_peer_config::preshared_key
```

可选的预共享密钥（pre-shared key），长度为 32 字节；不使用时设为 `NULL`。

<a id="a9ae02999964a23bdcd008648f99067b1"></a>

### `public_key`

```c
const char* wireguard_peer_config::public_key
```

Base64 格式的公钥（public key）。

<a id="a67b63a434cf1d5147dcf988e85b7b958"></a>

### `timestamp`

```c
uint8_t wireguard_peer_config::timestamp[(sizeof(uint64_t)+sizeof(uint32_t))]
```

握手期间已观察到的最大时间戳，用于防止重放（replay）。

本数据类型文档由以下文件生成：

- `zephyr/net/wireguard.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/net/wireguard.h](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [wireguard_allowed_ip](P070_wireguard_allowed_ip_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_wireguard_allowed_ip_结构体.md) · [返回大纲](大纲.md)
