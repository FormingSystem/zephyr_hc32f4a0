---
id: learning.zephyr-docs.network-core-model-reference.page-157
title: net_wifi_mgmt_offload_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__wifi__mgmt__offload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第157章\_net\_wifi\_mgmt\_offload\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__wifi__mgmt__offload.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi管理卸载（Management Offload）API。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi管理卸载（Management Offload）API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 157.1\_数据成员（Data Fields）

<a id="r_a1d34a954a2f16d29f51dc51dd6fbb845"></a>

```c
struct ethernet_api wifi_iface
```

相关声明：[ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)、[wifi_iface](#a1d34a954a2f16d29f51dc51dd6fbb845)。

必须位于第一个位置（First position）。

<a id="r_a98fcc053d9820d2d981ed659520c9b3b"></a>

```c
const struct wifi_mgmt_ops *const wifi_mgmt_api
```

相关声明：[wifi_mgmt_ops](P176_wifi_mgmt_ops_结构体.md)、[wifi_mgmt_api](#a98fcc053d9820d2d981ed659520c9b3b)。

Wi-Fi管理（Management）API。

<a id="r_a991e0bc6247578a3d1c9d2d3ab0b63d7"></a>

```c
const void * wifi_drv_ops
```

相关声明：[wifi_drv_ops](#a991e0bc6247578a3d1c9d2d3ab0b63d7)。

Wi‑Fi 认证请求端驱动 API（Wi-Fi supplicant driver API）。

## 157.2\_详细说明（Detailed Documentation）

<a id="a991e0bc6247578a3d1c9d2d3ab0b63d7"></a>

### `wifi_drv_ops`

```c
const void* net_wifi_mgmt_offload::wifi_drv_ops
```

Wi‑Fi 认证请求端驱动 API（Wi-Fi supplicant driver API）。

<a id="a1d34a954a2f16d29f51dc51dd6fbb845"></a>

### `wifi_iface`

```c
struct ethernet_api net_wifi_mgmt_offload::wifi_iface
```

必须位于第一个位置（First position）。

网络设备应提供指向这种 `net_if_api` 结构的指针。因此，当前结构的指针应能强制转换为 `net_if_api` 结构指针。参见以太网 API（Ethernet API）。

<a id="a98fcc053d9820d2d981ed659520c9b3b"></a>

### `wifi_mgmt_api`

```c
const struct wifi_mgmt_ops* const net_wifi_mgmt_offload::wifi_mgmt_api
```

Wi-Fi管理（Management）API。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 157.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)
- [wifi_mgmt_ops](P176_wifi_mgmt_ops_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P156_net_tuple_结构体.md) · [返回大纲](大纲.md) · [下一章](P158_wifi_11k_params_结构体.md)
