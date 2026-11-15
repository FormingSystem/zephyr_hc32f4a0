---
id: learning.zephyr-docs.modem-wireless-model-reference.page-9
title: conn_mgr_conn_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_conn\_mgr\_conn\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器（Connectivity Manager）的连接API结构。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

<a id="details"></a>

连接管理器（Connectivity Manager）的连接 API 结构体，用于以通用方式访问网络关联参数和过程。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a2490ac680ca52c93ab0c7f48c04f673c"></a>

```c
bool(* has_connection_config )(struct conn_mgr_conn_binding *const binding)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_connection_config](#a2490ac680ca52c93ab0c7f48c04f673c)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

调用时，连接实现应返回它是否已具备尝试连接所需的配置。

<a id="r_a92064a4752f0c9621c5c6a745708a66e"></a>

```c
int(* connect )(struct conn_mgr_conn_binding *const binding)
```

相关声明：[connect](#a92064a4752f0c9621c5c6a745708a66e)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

调用时，连接实现应开始尝试为 `if_conn->iface` 指向的已绑定网络接口（iface）建立连接，即关联到网络。

<a id="r_aee0d0fc9ef3361c8859b69128a087ba5"></a>

```c
int(* disconnect )(struct conn_mgr_conn_binding *const binding)
```

相关声明：[disconnect](#aee0d0fc9ef3361c8859b69128a087ba5)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

调用时，连接实现应断开 `if_conn->iface` 指向的已绑定接口与网络的关联，或停止该接口当前正在进行的网络关联尝试。

<a id="r_ad2bb08d518e2f797002ca5257889a59e"></a>

```c
void(* init )(struct conn_mgr_conn_binding *const binding)
```

相关声明：[init](#ad2bb08d518e2f797002ca5257889a59e)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

对通过此 API 绑定到连接实现的每个接口，调用一次。

<a id="r_a5636cced185825bd6c6997b427fd6121"></a>

```c
int(* set_opt )(struct conn_mgr_conn_binding *const binding, int optname, const void *optval, size_t optlen)
```

相关声明：[set_opt](#a5636cced185825bd6c6997b427fd6121)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

`conn_mgr_if_set_opt` 的实现回调。

<a id="r_a15d4bd909af1a2d3348fdec822bca7b7"></a>

```c
int(* get_opt )(struct conn_mgr_conn_binding *const binding, int optname, void *optval, size_t *optlen)
```

相关声明：[get_opt](#a15d4bd909af1a2d3348fdec822bca7b7)、[conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)。

`conn_mgr_if_get_opt` 的实现回调。

## 9.2\_详细说明（Detailed Documentation）

<a id="a92064a4752f0c9621c5c6a745708a66e"></a>

### `connect`

```c
int(* conn_mgr_conn_api::connect) (struct conn_mgr_conn_binding *const binding)
```

调用时，连接实现应开始尝试为 `if_conn->iface` 指向的已绑定网络接口（iface）建立连接，即关联到网络。

必须为非阻塞（non-blocking）操作。

由 `conn_mgr_if_connect` 调用。

<a id="aee0d0fc9ef3361c8859b69128a087ba5"></a>

### `disconnect`

```c
int(* conn_mgr_conn_api::disconnect) (struct conn_mgr_conn_binding *const binding)
```

调用时，连接实现应断开 `if_conn->iface` 指向的已绑定接口与网络的关联，或停止该接口当前正在进行的网络关联尝试。

由 `conn_mgr_if_disconnect` 调用。

<a id="a15d4bd909af1a2d3348fdec822bca7b7"></a>

### `get_opt`

```c
int(* conn_mgr_conn_api::get_opt) (struct conn_mgr_conn_binding *const binding, int optname, void *optval, size_t *optlen)
```

`conn_mgr_if_get_opt` 的实现回调。

用于获取实现专用的连接设置。

对接口调用 `conn_mgr_if_get_opt` 时，会调用此回调，并传入绑定到该接口的 `conn_mgr_conn_binding` 结构体。

`optname` 的含义由连接实现解释。选项可以仅适用于 `if_conn->iface` 指向的已绑定接口，也可以适用于整个连接实现。

更多详情参见 `conn_mgr_if_get_opt` 的说明。`get_opt` 实现应遵守该说明。

<a id="a2490ac680ca52c93ab0c7f48c04f673c"></a>

### `has_connection_config`

```c
bool(* conn_mgr_conn_api::has_connection_config) (struct conn_mgr_conn_binding *const binding)
```

调用时，连接实现应返回它是否已具备尝试连接所需的配置。

如果非持久连接（non-persistent connection）未通过此检查，则接口不会启用，也不会调用 `connect`。

例如，此检查可以判断 Wi-Fi 连接绑定是否已配置要连接的服务集标识符（SSID）。

必须为非阻塞（non-blocking）操作。

由 `conn_mgr_if_connect` 调用。

<a id="ad2bb08d518e2f797002ca5257889a59e"></a>

### `init`

```c
void(* conn_mgr_conn_api::init) (struct conn_mgr_conn_binding *const binding)
```

对通过此 API 绑定到连接实现的每个接口，调用一次。

连接实现应使用此回调，对每个已绑定接口执行必要的初始化。

如果合适，实现可以通过部分写入妥善处理无效的缓冲区长度，而不是直接报错。

<a id="a5636cced185825bd6c6997b427fd6121"></a>

### `set_opt`

```c
int(* conn_mgr_conn_api::set_opt) (struct conn_mgr_conn_binding *const binding, int optname, const void *optval, size_t optlen)
```

`conn_mgr_if_set_opt` 的实现回调。

用于设置实现专用的连接配置。

对接口调用 `conn_mgr_if_set_opt` 时，会调用此回调，并传入绑定到该接口的 `conn_mgr_conn_binding` 结构体。

`optname` 的含义由连接实现解释。选项可以仅适用于 `if_conn->iface` 指向的已绑定接口，也可以适用于整个连接实现。

更多详情参见 `conn_mgr_if_set_opt` 的说明。`set_opt` 实现应遵守该说明。

如果合适，实现可以通过部分读取妥善处理无效的缓冲区长度，而不是直接报错。

本数据类型文档由以下文件生成：

- `zephyr/net/conn_mgr_connectivity_impl.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/conn_mgr_connectivity_impl.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [conn_mgr_conn_binding](P010_conn_mgr_conn_binding_结构体.md)
- [conn_mgr_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga575d367c95592fd9f4ead694ff94543f)
- [conn_mgr_if_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada2b5271b3e5dbcab629e1538b3d8eb4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_cellular_stats_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_conn_mgr_conn_binding_结构体.md)
