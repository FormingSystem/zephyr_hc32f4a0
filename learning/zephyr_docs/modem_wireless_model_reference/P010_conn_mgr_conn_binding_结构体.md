---
id: learning.zephyr-docs.modem-wireless-model-reference.page-10
title: conn_mgr_conn_binding_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__binding.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_conn\_mgr\_conn\_binding\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__binding.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器（Connectivity Manager）的网络接口绑定结构。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

<a id="details"></a>

连接管理器的网络接口绑定（network interface binding）结构体。将一个 `conn_mgr` 连接实现绑定到接口或网络设备，并为连接实现保存各接口独立的状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a59bd71867b19e002c310d85496833e8f"></a>

```c
struct net_if * iface
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface](#a59bd71867b19e002c310d85496833e8f)。

连接实现所绑定的网络接口。

<a id="r_a288749353194206b8d8766f8f17aff48"></a>

```c
const struct conn_mgr_conn_impl * impl
```

相关声明：[conn_mgr_conn_impl](P011_conn_mgr_conn_impl_结构体.md)、[impl](#a288749353194206b8d8766f8f17aff48)。

网络设备所绑定的连接实现。

<a id="r_ad9102e2cf44b5940b21b1d160fea7611"></a>

```c
void * ctx
```

相关声明：[ctx](#ad9102e2cf44b5940b21b1d160fea7611)。

指向私有、按接口独立保存的连接上下文的指针。

<a id="pub-attribs-0"></a>

### 通用连接状态（Generic connectivity state）

<a id="r_a9b842340ebe872f30935b8f7e75d3605"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a9b842340ebe872f30935b8f7e75d3605)。

连接标志（Connectivity flags）。

<a id="r_a8474461cf7b00132441227aae07511ab"></a>

```c
int timeout
```

相关声明：[timeout](#a8474461cf7b00132441227aae07511ab)。

超时时间，单位为秒。

<a id="r_a50a8484896227f81aaf62f7f9a913985"></a>

```c
int idle_timeout
```

相关声明：[idle_timeout](#a50a8484896227f81aaf62f7f9a913985)。

使用超时（Usage timeout），单位为秒。

## 10.2\_详细说明（Detailed Documentation）

<a id="ad9102e2cf44b5940b21b1d160fea7611"></a>

### `ctx`

```c
void* conn_mgr_conn_binding::ctx
```

指向私有、按接口独立保存的连接上下文的指针。

<a id="a9b842340ebe872f30935b8f7e75d3605"></a>

### `flags`

```c
uint32_t conn_mgr_conn_binding::flags
```

连接标志（Connectivity flags）。

所有绑定都支持的公共布尔状态及配置值。可用选项参见 `conn_mgr_if_flag`。

<a id="a50a8484896227f81aaf62f7f9a913985"></a>

### `idle_timeout`

```c
int conn_mgr_conn_binding::idle_timeout
```

使用超时（Usage timeout），单位为秒。

告诉连接实现：接口最多可以空闲多久，超过后应自动关闭接口。

设为 `CONN_MGR_IF_NO_TIMEOUT` 表示不使用空闲超时。

<a id="a59bd71867b19e002c310d85496833e8f"></a>

### `iface`

```c
struct net_if* conn_mgr_conn_binding::iface
```

连接实现所绑定的网络接口。

<a id="a288749353194206b8d8766f8f17aff48"></a>

### `impl`

```c
const struct conn_mgr_conn_impl* conn_mgr_conn_binding::impl
```

网络设备所绑定的连接实现。

<a id="a8474461cf7b00132441227aae07511ab"></a>

### `timeout`

```c
int conn_mgr_conn_binding::timeout
```

超时时间，单位为秒。

告诉连接实现：一次连接尝试中，应尝试建立连接多久后放弃。

此超时到期后，即使启用了持久连接，连接实现也应放弃建立连接。

设为 `CONN_MGR_IF_NO_TIMEOUT` 表示不使用超时。

本数据类型文档由以下文件生成：

- `zephyr/net/conn_mgr_connectivity_impl.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/net/conn_mgr_connectivity_impl.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_conn_impl](P011_conn_mgr_conn_impl_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [CONN_MGR_IF_NO_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga605eee24f4419b5cd6a50a0272979da7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_conn_mgr_conn_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_conn_mgr_conn_impl_结构体.md)
