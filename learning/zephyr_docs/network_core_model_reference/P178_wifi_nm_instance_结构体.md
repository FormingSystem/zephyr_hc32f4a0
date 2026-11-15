---
id: learning.zephyr-docs.network-core-model-reference.page-178
title: wifi_nm_instance_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__nm__instance.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_wifi\_nm\_instance\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__nm__instance.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi网络管理器（Network Manager）的实例。

```c
#include <zephyr/net/wifi_nm.h>
```

<a id="details"></a>

Wi-Fi网络管理器（Network Manager）的实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 178.1\_数据成员（Data Fields）

<a id="r_a9789018a431b6c78bbbbed1bbaf634af"></a>

```c
const char * name
```

相关声明：[name](#a9789018a431b6c78bbbbed1bbaf634af)。

网络管理器实例名称（Network manager instance name）。

<a id="r_a65e73ea84dfd64dc17f0af03477362ae"></a>

```c
const struct wifi_mgmt_ops * ops
```

相关声明：[wifi_mgmt_ops](P176_wifi_mgmt_ops_结构体.md)、[ops](#a65e73ea84dfd64dc17f0af03477362ae)。

Wi‑Fi 管理操作（Wi-Fi Management operations）。

<a id="r_a02184a7739d4b9a31b6142df3e0463c0"></a>

```c
struct wifi_nm_mgd_iface mgd_ifaces [CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES]
```

相关声明：[wifi_nm_mgd_iface](P179_wifi_nm_mgd_iface_结构体.md)、[mgd_ifaces](#a02184a7739d4b9a31b6142df3e0463c0)。

受管理接口列表（Managed interfaces list）。

## 178.2\_详细说明（Detailed Documentation）

<a id="a02184a7739d4b9a31b6142df3e0463c0"></a>

### `mgd_ifaces`

```c
struct wifi_nm_mgd_iface wifi_nm_instance::mgd_ifaces[CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES]
```

受管理接口列表（Managed interfaces list）。

<a id="a9789018a431b6c78bbbbed1bbaf634af"></a>

### `name`

```c
const char* wifi_nm_instance::name
```

网络管理器实例名称（Network manager instance name）。

<a id="a65e73ea84dfd64dc17f0af03477362ae"></a>

### `ops`

```c
const struct wifi_mgmt_ops* wifi_nm_instance::ops
```

Wi‑Fi 管理操作（Wi-Fi Management operations）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_nm.h`

## 178.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_nm.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h_source.html)
- [wifi_mgmt_ops](P176_wifi_mgmt_ops_结构体.md)
- [wifi_nm_mgd_iface](P179_wifi_nm_mgd_iface_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P177_wifi_mode_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P179_wifi_nm_mgd_iface_结构体.md)
