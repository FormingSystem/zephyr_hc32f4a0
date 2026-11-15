---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-126
title: bt_nus_inst_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__nus__inst.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_bt\_nus\_inst\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__nus__inst.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/services/nus/inst.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 126.1\_数据成员（Data Fields）

<a id="r_a3a3dd0e1f20e47a39124f10982a6be59"></a>

```c
const struct bt_gatt_service_static * svc
```

相关声明：[bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)、[svc](#a3a3dd0e1f20e47a39124f10982a6be59)。

指向 Nordic UART 服务（NUS）实例的指针。

<a id="r_a47c7d47a0cbad0e5696c64e3592de776"></a>

```c
sys_slist_t * cbs
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[cbs](#a47c7d47a0cbad0e5696c64e3592de776)。

订阅者列表，用于在异步事件发生时调用回调。

## 126.2\_详细说明（Detailed Documentation）

<a id="a47c7d47a0cbad0e5696c64e3592de776"></a>

### `cbs`

```c
sys_slist_t* bt_nus_inst::cbs
```

订阅者列表，用于在异步事件发生时调用回调。

<a id="a3a3dd0e1f20e47a39124f10982a6be59"></a>

### `svc`

```c
const struct bt_gatt_service_static* bt_nus_inst::svc
```

指向 Nordic UART 服务（NUS）实例的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/nus/inst.h`

## 126.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/nus/inst.h](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h_source.html)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P125_bt_nus_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P127_bt_obex_结构体.md)
