---
id: learning.zephyr-docs.system-service-model-reference.page-82
title: smp_transport_api_t_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__api__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_smp\_transport\_api\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__api__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单管理协议（SMP）传输函数的函数指针；处理函数为NULL表示不支持或尚未实现。

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

<a id="details"></a>

简单管理协议（SMP）传输函数的函数指针；处理函数为NULL表示不支持或尚未实现。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_aa779d7dcea55385963a0c0054b95f9da"></a>

```c
smp_transport_out_fn output
```

相关声明：[smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)、[output](#aa779d7dcea55385963a0c0054b95f9da)。

传输层的发送函数。

<a id="r_acfeec0f2b18fa4d8518e96d10b2e879a"></a>

```c
uint16_t(* get_mtu )(const struct net_buf *nb)
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[get_mtu](#acfeec0f2b18fa4d8518e96d10b2e879a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

传输层获取最大传输单元（MTU）的函数。

<a id="r_ae3153c9a27123de510e4ee83cc9c0c62"></a>

```c
smp_transport_ud_copy_fn ud_copy
```

相关声明：[smp_transport_ud_copy_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga840da7e00d590459b656dcbe0dd6f6f4)、[ud_copy](#ae3153c9a27123de510e4ee83cc9c0c62)。

传输缓冲区 `user_data` 的复制函数。

<a id="r_acc98fb8a8e7e674ec907939831de1809"></a>

```c
smp_transport_ud_free_fn ud_free
```

相关声明：[smp_transport_ud_free_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0f249aa3fed3044d9bad811e92e4135c)、[ud_free](#acc98fb8a8e7e674ec907939831de1809)。

传输缓冲区 `user_data` 的释放函数。

<a id="r_a811fefe5287c7050701705f8db51f16d"></a>

```c
smp_transport_query_valid_check_fn query_valid_check
```

相关声明：[smp_transport_query_valid_check_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga77d54c0bd6afc69f73613575b671e089)、[query_valid_check](#a811fefe5287c7050701705f8db51f16d)。

传输层用于检查查询是否有效的函数。

<a id="r_a3b7000867da67eacaf122963e79bb500"></a>

```c
smp_transport_ud_req_init_fn ud_init
```

相关声明：[smp_transport_ud_req_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga095edd916780b458e8cbd701969c0640)、[ud_init](#a3b7000867da67eacaf122963e79bb500)。

传输层的请求缓冲区初始化函数。

<a id="r_a5c8ab9d564d8cc013d28155763f8b20e"></a>

```c
smp_transport_bridge_connect_fn bridge_connect
```

相关声明：[smp_transport_bridge_connect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga032db1c1b6f4d4212e6dc67fbd28c115)、[bridge_connect](#a5c8ab9d564d8cc013d28155763f8b20e)。

将传输层桥接连接到另一传输层的函数。

<a id="r_aaea5ecb91fc45c3dd4c4785e733fbfa1"></a>

```c
smp_transport_bridge_disconnect_fn bridge_disconnect
```

相关声明：[smp_transport_bridge_disconnect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga50fcdcef18ae4c937ced9f323715e1e1)、[bridge_disconnect](#aaea5ecb91fc45c3dd4c4785e733fbfa1)。

断开传输桥接的函数。

<a id="r_aa408fcddf2262cd6eef52c5b451b7f08"></a>

```c
smp_transport_bridge_out_fn bridge_output
```

相关声明：[smp_transport_bridge_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gadadf97eb50e871f5942b4774c643eba2)、[bridge_output](#aa408fcddf2262cd6eef52c5b451b7f08)。

通过桥接连接发送数据的函数。

<a id="r_a68a94fa4f1a1e5e5bea3c1a2d58ef08e"></a>

```c
smp_transport_bridge_modes_fn bridge_modes
```

相关声明：[smp_transport_bridge_modes_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4570f81d545ae51e68f5a2c3ede4f170)、[bridge_modes](#a68a94fa4f1a1e5e5bea3c1a2d58ef08e)。

获取传输模式的函数。

<a id="r_a3da771527b2ab8c63ddb7920405fca8c"></a>

```c
smp_transport_bridge_config_details_fn bridge_config_details
```

相关声明：[smp_transport_bridge_config_details_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0d8277e9da18c896749e2392c7ea1ac7)、[bridge_config_details](#a3da771527b2ab8c63ddb7920405fca8c)。

获取传输配置详情的函数。

## 82.2\_详细说明（Detailed Documentation）

<a id="a3da771527b2ab8c63ddb7920405fca8c"></a>

### `bridge_config_details`

```c
smp_transport_bridge_config_details_fn smp_transport_api_t::bridge_config_details
```

获取传输配置详情的函数。

<a id="a5c8ab9d564d8cc013d28155763f8b20e"></a>

### `bridge_connect`

```c
smp_transport_bridge_connect_fn smp_transport_api_t::bridge_connect
```

将传输层桥接连接到另一传输层的函数。

<a id="aaea5ecb91fc45c3dd4c4785e733fbfa1"></a>

### `bridge_disconnect`

```c
smp_transport_bridge_disconnect_fn smp_transport_api_t::bridge_disconnect
```

断开传输桥接的函数。

<a id="a68a94fa4f1a1e5e5bea3c1a2d58ef08e"></a>

### `bridge_modes`

```c
smp_transport_bridge_modes_fn smp_transport_api_t::bridge_modes
```

获取传输模式的函数。

<a id="aa408fcddf2262cd6eef52c5b451b7f08"></a>

### `bridge_output`

```c
smp_transport_bridge_out_fn smp_transport_api_t::bridge_output
```

通过桥接连接发送数据的函数。

<a id="acfeec0f2b18fa4d8518e96d10b2e879a"></a>

### `get_mtu`

```c
uint16_t(* smp_transport_api_t::get_mtu) (const struct net_buf *nb)
```

传输层获取最大传输单元（MTU）的函数。

**已弃用（Deprecated）**：已弃用（Deprecated）：SMP 层不会调用此函数，参见 `smp_transport_get_mtu_fn`。

<a id="aa779d7dcea55385963a0c0054b95f9da"></a>

### `output`

```c
smp_transport_out_fn smp_transport_api_t::output
```

传输层的发送函数。

<a id="a811fefe5287c7050701705f8db51f16d"></a>

### `query_valid_check`

```c
smp_transport_query_valid_check_fn smp_transport_api_t::query_valid_check
```

传输层用于检查查询是否有效的函数。

<a id="ae3153c9a27123de510e4ee83cc9c0c62"></a>

### `ud_copy`

```c
smp_transport_ud_copy_fn smp_transport_api_t::ud_copy
```

传输缓冲区 `user_data` 的复制函数。

<a id="acc98fb8a8e7e674ec907939831de1809"></a>

### `ud_free`

```c
smp_transport_ud_free_fn smp_transport_api_t::ud_free
```

传输缓冲区 `user_data` 的释放函数。

<a id="a3b7000867da67eacaf122963e79bb500"></a>

### `ud_init`

```c
smp_transport_ud_req_init_fn smp_transport_api_t::ud_init
```

传输层的请求缓冲区初始化函数。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/transport/smp.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html)
- [smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_transport_ud_copy_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga840da7e00d590459b656dcbe0dd6f6f4)
- [smp_transport_ud_free_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0f249aa3fed3044d9bad811e92e4135c)
- [smp_transport_query_valid_check_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga77d54c0bd6afc69f73613575b671e089)
- [smp_transport_ud_req_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga095edd916780b458e8cbd701969c0640)
- [smp_transport_bridge_connect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga032db1c1b6f4d4212e6dc67fbd28c115)
- [smp_transport_bridge_disconnect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga50fcdcef18ae4c937ced9f323715e1e1)
- [smp_transport_bridge_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gadadf97eb50e871f5942b4774c643eba2)
- [smp_transport_bridge_modes_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4570f81d545ae51e68f5a2c3ede4f170)
- [smp_transport_bridge_config_details_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0d8277e9da18c896749e2392c7ea1ac7)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000097)
- [smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_smp_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_smp_transport_bridge_结构体.md)
