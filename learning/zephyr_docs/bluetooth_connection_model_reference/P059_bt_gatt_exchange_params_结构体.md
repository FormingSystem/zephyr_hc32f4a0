---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-59
title: bt_gatt_exchange_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__exchange__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_bt\_gatt\_exchange\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__exchange__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 最大传输单元交换（Exchange MTU）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 最大传输单元交换参数（GATT Exchange MTU parameters）。与 `bt_gatt_exchange_mtu` 函数配合使用，发起 MTU 交换。通过 `func` 回调处理响应；完成时在线程上下文（Thread context）中调用该回调，绝不会在中断服务程序（ISR）中调用，参见回调执行上下文（Callback execution contexts）。`params` 必须一直保持有效，直到回调执行。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a76f4d3e779da9c725914574ac2e22ad1"></a>

```c
void(* func )(struct bt_conn *conn, uint8_t err, struct bt_gatt_exchange_params *params)
```

相关声明：[func](#a76f4d3e779da9c725914574ac2e22ad1)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_exchange_params](P059_bt_gatt_exchange_params_结构体.md)。

最大传输单元交换响应回调（MTU exchange response callback）。

## 59.2\_详细说明（Detailed Documentation）

<a id="a76f4d3e779da9c725914574ac2e22ad1"></a>

### `func`

```c
void(* bt_gatt_exchange_params::func) (struct bt_conn *conn, uint8_t err, struct bt_gatt_exchange_params *params)
```

最大传输单元交换响应回调（MTU exchange response callback）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_gatt_exchange_params](P059_bt_gatt_exchange_params_结构体.md)
- [bt_gatt_exchange_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga0f41da23c6559a8254b04295aff8198d)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_bt_gatt_discover_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_bt_gatt_include_结构体.md)
