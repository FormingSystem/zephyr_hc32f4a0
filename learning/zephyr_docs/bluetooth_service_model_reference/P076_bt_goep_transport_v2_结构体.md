---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-76
title: bt_goep_transport_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_bt\_goep\_transport\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__v2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用对象交换配置文件（GOEP）v2结构。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

通用对象交换配置文件（GOEP）v2结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_a8a273966650ed88693c9de1213f2088d"></a>

```c
struct bt_l2cap_br_chan chan
```

相关声明：[bt_l2cap_br_chan](P096_bt_l2cap_br_chan_结构体.md)、[chan](#a8a273966650ed88693c9de1213f2088d)。

用于传输的 L2CAP 基本速率／增强数据率通道（L2CAP BR/EDR channel）。

<a id="r_a5d3086e35bd244810e87d4bd0023e7bc"></a>

```c
struct bt_goep * goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#a5d3086e35bd244810e87d4bd0023e7bc)。

指向父通用对象交换规范对象（GOEP object）的反向指针（Back-pointer）。

## 76.2\_详细说明（Detailed Documentation）

<a id="a8a273966650ed88693c9de1213f2088d"></a>

### `chan`

```c
struct bt_l2cap_br_chan bt_goep_transport_v2::chan
```

用于传输的 L2CAP 基本速率／增强数据率通道（L2CAP BR/EDR channel）。

<a id="a5d3086e35bd244810e87d4bd0023e7bc"></a>

### `goep`

```c
struct bt_goep* bt_goep_transport_v2::goep
```

指向父通用对象交换规范对象（GOEP object）的反向指针（Back-pointer）。

调用任何 GOEP 传输连接或注册 API 之前，必须将此项初始化为指向父通用对象交换规范结构（GOEP structure）。对于有效的 GOEP v2.0 会话，父 GOEP 对象的 `bt_goep::v2` 字段必须指向此结构，并且 `bt_goep::v1` 必须为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_l2cap_br_chan](P096_bt_l2cap_br_chan_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_goep::v2](P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep::v1](P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_bt_goep_transport_v1_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_bt_has_结构体.md)
