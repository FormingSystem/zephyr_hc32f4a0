---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-75
title: bt_goep_transport_v1_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__v1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_bt\_goep\_transport\_v1\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__v1.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用对象交换配置文件（GOEP）v1.1结构。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

通用对象交换配置文件（GOEP）v1.1结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_a5e3a3cfd380d2001a156949177e1ca38"></a>

```c
struct bt_rfcomm_dlc dlc
```

相关声明：[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)、[dlc](#a5e3a3cfd380d2001a156949177e1ca38)。

用于传输的串口仿真协议数据链路连接（RFCOMM DLC）。

<a id="r_a82ed6f11432432f051c705bddfd7a53b"></a>

```c
struct bt_goep * goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#a82ed6f11432432f051c705bddfd7a53b)。

指向父通用对象交换规范对象（GOEP object）的反向指针（Back-pointer）。

## 75.2\_详细说明（Detailed Documentation）

<a id="a5e3a3cfd380d2001a156949177e1ca38"></a>

### `dlc`

```c
struct bt_rfcomm_dlc bt_goep_transport_v1::dlc
```

用于传输的串口仿真协议数据链路连接（RFCOMM DLC）。

<a id="a82ed6f11432432f051c705bddfd7a53b"></a>

### `goep`

```c
struct bt_goep* bt_goep_transport_v1::goep
```

指向父通用对象交换规范对象（GOEP object）的反向指针（Back-pointer）。

调用任何 GOEP 传输连接或注册 API 之前，必须将此项初始化为指向父通用对象交换规范结构（GOEP structure）。对于有效的 GOEP v1.1 会话，父 GOEP 对象的 `bt_goep::v1` 字段必须指向此结构，并且 `bt_goep::v2` 必须为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_goep::v1](P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep::v2](P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_bt_goep_transport_rfcomm_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_bt_goep_transport_v2_结构体.md)
