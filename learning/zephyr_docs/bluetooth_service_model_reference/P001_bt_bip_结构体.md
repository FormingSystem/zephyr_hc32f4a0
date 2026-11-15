---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-1
title: bt_bip_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_bt\_bip\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本图像配置文件（BIP）实例结构体。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范实例结构（BIP instance structure）。表示基本成像规范会话（BIP session）的主要结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a245296151dcf59b69822e3122488c2c2"></a>

```c
struct bt_goep_transport goep_transport
```

相关声明：[bt_goep_transport](P071_bt_goep_transport_结构体.md)、[goep_transport](#a245296151dcf59b69822e3122488c2c2)。

底层通用对象交换规范传输实例（GOEP transport instance）。

<a id="r_adba3573d8d8250c015cb5adca9bd77bb"></a>

```c
struct bt_goep goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#adba3573d8d8250c015cb5adca9bd77bb)。

底层通用对象交换规范实例（GOEP instance）。

<a id="r_a9cee12abb9b8efadb1b7c3e21803f349"></a>

```c
enum bt_bip_role role
```

相关声明：[bt_bip_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30d9309cbbd88b54508551285b21e575)、[role](#a9cee12abb9b8efadb1b7c3e21803f349)。

连接中的角色（Role）。

<a id="r_ac5b8a3fd23216a0894a47ac487835bc0"></a>

```c
const struct bt_bip_transport_ops * ops
```

相关声明：[bt_bip_transport_ops](P008_bt_bip_transport_ops_结构体.md)、[ops](#ac5b8a3fd23216a0894a47ac487835bc0)。

传输操作回调（Transport operation callbacks）。

## 1.2\_详细说明（Detailed Documentation）

<a id="adba3573d8d8250c015cb5adca9bd77bb"></a>

### `goep`

```c
struct bt_goep bt_bip::goep
```

底层通用对象交换规范实例（GOEP instance）。

<a id="a245296151dcf59b69822e3122488c2c2"></a>

### `goep_transport`

```c
struct bt_goep_transport bt_bip::goep_transport
```

底层通用对象交换规范传输实例（GOEP transport instance）。

<a id="ac5b8a3fd23216a0894a47ac487835bc0"></a>

### `ops`

```c
const struct bt_bip_transport_ops* bt_bip::ops
```

传输操作回调（Transport operation callbacks）。

<a id="a9cee12abb9b8efadb1b7c3e21803f349"></a>

### `role`

```c
enum bt_bip_role bt_bip::role
```

连接中的角色（Role）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_goep_transport](P071_bt_goep_transport_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)
- [bt_bip_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30d9309cbbd88b54508551285b21e575)
- [bt_bip_transport_ops](P008_bt_bip_transport_ops_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_bt_bip_client_结构体.md)
