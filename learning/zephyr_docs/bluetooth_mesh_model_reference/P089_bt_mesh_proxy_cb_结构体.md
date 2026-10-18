---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-89
title: bt_mesh_proxy_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__proxy__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_bt\_mesh\_proxy\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__proxy__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

代理功能（Proxy Feature）的回调。

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

<a id="details"></a>

代理特性（Proxy feature）的回调。应使用 `BT_MESH_PROXY_CB_DEFINE` 实例化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_ae6f129ae511681d2f1fccafedba47918"></a>

```c
void(* identity_enabled )(uint16_t net_idx)
```

相关声明：[identity_enabled](#ae6f129ae511681d2f1fccafedba47918)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

已开始在指定子网上发送节点身份信标（Node Identity beacons）。

<a id="r_a207ebf7e3f1f1e732d4540af000bf2ef"></a>

```c
void(* identity_disabled )(uint16_t net_idx)
```

相关声明：[identity_disabled](#a207ebf7e3f1f1e732d4540af000bf2ef)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

已停止在指定子网上发送节点身份信标（Node Identity beacons）。

## 89.2\_详细说明（Detailed Documentation）

<a id="a207ebf7e3f1f1e732d4540af000bf2ef"></a>

### `identity_disabled`

```c
void(* bt_mesh_proxy_cb::identity_disabled) (uint16_t net_idx)
```

已停止在指定子网上发送节点身份信标（Node Identity beacons）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 此前运行节点身份信标（Node Identity beacons）所用的网络索引（Network index）。 |

<a id="ae6f129ae511681d2f1fccafedba47918"></a>

### `identity_enabled`

```c
void(* bt_mesh_proxy_cb::identity_enabled) (uint16_t net_idx)
```

已开始在指定子网上发送节点身份信标（Node Identity beacons）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 当前运行节点身份信标（Node Identity beacons）所用的网络索引（Network index）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/proxy.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_MESH_PROXY_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga325b71c3d7ed69952bf760c0288b28ef)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_bt_mesh_prov_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_bt_mesh_rpr_caps_结构体.md)
