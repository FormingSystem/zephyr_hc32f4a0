---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-24
title: bt_avrcp_cover_art_tg_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__tg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_bt\_avrcp\_cover\_art\_tg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__tg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 目标端封面图（Target Cover Art）结构体。

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

<a id="details"></a>

AVRCP 目标端封面图（Target Cover Art）结构体。该结构体表示 AVRCP 目标端封面图实例，为 AVRCP 控制端设备提供封面图。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_acdd5b50f1f5f8f21738e5723441b4b8c"></a>

```c
struct bt_bip bip
```

相关声明：[bt_bip](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html)、[bip](#acdd5b50f1f5f8f21738e5723441b4b8c)。

基本图像配置文件（Basic Image Profile，BIP）实例。

<a id="r_a08644473b1f4c425e7dfb5e8dc64bc0a"></a>

```c
struct bt_bip_server server
```

相关声明：[bt_bip_server](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__server.html)、[server](#a08644473b1f4c425e7dfb5e8dc64bc0a)。

BIP 服务器实例。

<a id="r_aedc07dd496bebcfef110c1e2c2bacb93"></a>

```c
struct bt_avrcp_tg * tg
```

相关声明：[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[tg](#aedc07dd496bebcfef110c1e2c2bacb93)。

关联的 AVRCP 目标端（Target）。

<a id="r_a41e8025b600c057b1fe47c5e74f0a658"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[conn](#a41e8025b600c057b1fe47c5e74f0a658)。

蓝牙连接（Bluetooth Connection）。

## 24.2\_详细说明（Detailed Documentation）

<a id="acdd5b50f1f5f8f21738e5723441b4b8c"></a>

### `bip`

```c
struct bt_bip bt_avrcp_cover_art_tg::bip
```

基本图像配置文件（Basic Image Profile，BIP）实例。

<a id="a41e8025b600c057b1fe47c5e74f0a658"></a>

### `conn`

```c
struct bt_conn* bt_avrcp_cover_art_tg::conn
```

蓝牙连接（Bluetooth Connection）。

<a id="a08644473b1f4c425e7dfb5e8dc64bc0a"></a>

### `server`

```c
struct bt_bip_server bt_avrcp_cover_art_tg::server
```

BIP 服务器实例。

<a id="aedc07dd496bebcfef110c1e2c2bacb93"></a>

### `tg`

```c
struct bt_avrcp_tg* bt_avrcp_cover_art_tg::tg
```

关联的 AVRCP 目标端（Target）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp_cover_art.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp_cover_art.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html)
- [bt_bip](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html)
- [bt_bip_server](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__server.html)
- [bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_bt_avrcp_cover_art_ct_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_bt_avrcp_cover_art_tg_cb_结构体.md)
