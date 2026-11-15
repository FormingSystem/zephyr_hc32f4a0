---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-13
title: bt_conn_le_create_synced_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__create__synced__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_conn\_le\_create\_synced\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__create__synced__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_ac5872dda4042e3ba6c161dce60784b70"></a>

```c
const bt_addr_le_t * peer
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer](#ac5872dda4042e3ba6c161dce60784b70)。

远端地址（Remote address）。

<a id="r_ac7b4e4144aaf914bdef1dc305b5e297f"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#ac7b4e4144aaf914bdef1dc305b5e297f)。

将在其中发起连接的子事件（Subevent）。

## 13.2\_详细说明（Detailed Documentation）

<a id="ac5872dda4042e3ba6c161dce60784b70"></a>

### `peer`

```c
const bt_addr_le_t* bt_conn_le_create_synced_param::peer
```

远端地址（Remote address）。

对等设备必须已同步到带响应的周期广播序列（PAwR train）。

<a id="ac7b4e4144aaf914bdef1dc305b5e297f"></a>

### `subevent`

```c
uint8_t bt_conn_le_create_synced_param::subevent
```

将在其中发起连接的子事件（Subevent）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_conn_le_create_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_conn_le_cs_capabilities_结构体.md)
