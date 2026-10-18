---
id: learning.zephyr-docs.platform-security-model-reference.page-11
title: fido2_transport_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__transport__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_fido2\_transport\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__transport__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传输驱动（Transport Driver）的API回调。

```c
#include <zephyr/authentication/fido2/fido2_transport.h>
```

<a id="details"></a>

传输驱动（Transport Driver）的API回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_abd7cdffe93a80e3f0ac16550b6edf4d3"></a>

```c
int(* init )(fido2_transport_recv_cb_t cb, fido2_transport_cancel_cb_t cancel_cb)
```

相关声明：[init](#abd7cdffe93a80e3f0ac16550b6edf4d3)、[fido2_transport_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#af8365317181d301d3f44fd3eb9416475)、[fido2_transport_cancel_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a081a49ee568a0939254bc640b509c3f8)。

初始化传输层（Transport）。

<a id="r_a79bd5f4a1556c5ee451b8b62f674a861"></a>

```c
int(* send )(uint32_t cid, const uint8_t *data, size_t len)
```

相关声明：[send](#a79bd5f4a1556c5ee451b8b62f674a861)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向主机发送响应数据。

<a id="r_af9ded3aefb0c8c43337ba3d133a34555"></a>

```c
void(* notify )(uint32_t cid, enum fido2_wire_status status)
```

相关声明：[notify](#af9ded3aefb0c8c43337ba3d133a34555)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fido2_wire_status](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720b)。

通知传输层：操作进度发生变化。

<a id="r_aade11fc3660d148850816f7de6f6810d"></a>

```c
void(* shutdown )(void)
```

相关声明：[shutdown](#aade11fc3660d148850816f7de6f6810d)。

关闭传输层。

## 11.2\_详细说明（Detailed Documentation）

<a id="abd7cdffe93a80e3f0ac16550b6edf4d3"></a>

### `init`

```c
int(* fido2_transport_api::init) (fido2_transport_recv_cb_t cb, fido2_transport_cancel_cb_t cancel_cb)
```

初始化传输层（Transport）。

子系统启动期间调用一次。传输层必须保存这些回调，并在每次收到 CBOR 消息或取消命令时调用相应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 收到 CBOR 消息时调用的回调。 |
| `cancel_cb` | 收到取消命令时调用的回调。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENODEV` | 硬件不可用时。 |

<a id="af9ded3aefb0c8c43337ba3d133a34555"></a>

### `notify`

```c
void(* fido2_transport_api::notify) (uint32_t cid, enum fido2_wire_status status)
```

通知传输层：操作进度发生变化。

由 FIDO2 核心调用，用于通知长时间操作期间的状态转换。各传输层将其转换成相应的线路协议信令（wire-protocol signaling）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cid` | 通道或连接标识符。 |
| `status` | 表明核心当前操作的进度状态。 |

<a id="a79bd5f4a1556c5ee451b8b62f674a861"></a>

### `send`

```c
int(* fido2_transport_api::send) (uint32_t cid, const uint8_t *data, size_t len)
```

向主机发送响应数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cid` | 用于发送响应的传输通道 ID。 |
| `data` | 响应载荷字节。 |
| `len` | 数据长度，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 传输发生错误时。 |

<a id="aade11fc3660d148850816f7de6f6810d"></a>

### `shutdown`

```c
void(* fido2_transport_api::shutdown) (void)
```

关闭传输层。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_transport.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_transport.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h_source.html)
- [fido2_transport_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#af8365317181d301d3f44fd3eb9416475)
- [fido2_transport_cancel_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a081a49ee568a0939254bc640b509c3f8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fido2_wire_status](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_fido2_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_intel_adsp_mic_priv_cfg_结构体.md)
