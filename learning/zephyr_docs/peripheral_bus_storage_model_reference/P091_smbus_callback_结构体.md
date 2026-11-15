---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-91
title: smbus_callback_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_smbus\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统管理总线（SMBus）的回调结构。

```c
#include <zephyr/drivers/smbus.h>
```

<a id="details"></a>

SMBus 回调结构体（Callback structure）。用于在驱动实例的回调链表中注册回调。只要每个回调都有唯一的 `struct smbus_callback` 指针，就可以按需添加任意多个回调。注意：不应在栈上分配此结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a89fb6ad70aa53dba53aa85ebaea91f60"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a89fb6ad70aa53dba53aa85ebaea91f60)。

应由驱动用于管理回调链表。

<a id="r_a2017d57f8b1bbed10d37cb24a5212bc1"></a>

```c
smbus_callback_handler_t handler
```

相关声明：[smbus_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6d6ee9d29de5c0007d34328eb7c9f7c9)、[handler](#a2017d57f8b1bbed10d37cb24a5212bc1)。

在相关事件发生时实际调用的回调函数。

<a id="r_a707cc2c4cd2abf214343686d84cd1594"></a>

```c
uint8_t addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#a707cc2c4cd2abf214343686d84cd1594)。

外设地址。

## 91.2\_详细说明（Detailed Documentation）

<a id="a707cc2c4cd2abf214343686d84cd1594"></a>

### `addr`

```c
uint8_t smbus_callback::addr
```

外设地址。

<a id="a2017d57f8b1bbed10d37cb24a5212bc1"></a>

### `handler`

```c
smbus_callback_handler_t smbus_callback::handler
```

在相关事件发生时实际调用的回调函数。

<a id="a89fb6ad70aa53dba53aa85ebaea91f60"></a>

### `node`

```c
sys_snode_t smbus_callback::node
```

应由驱动用于管理回调链表。

本数据类型文档由以下文件生成：

- `zephyr/drivers/smbus.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/drivers/smbus.h](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [smbus_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6d6ee9d29de5c0007d34328eb7c9f7c9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smbus_callback](P091_smbus_callback_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_sent_rx_callback_configs_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_smbus_driver_api_结构体.md)
