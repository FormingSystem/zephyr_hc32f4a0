---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-127
title: bt_le_scan_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_bt\_le\_scan\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙（LE）扫描的监听器上下文（Listener Context）。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗扫描监听器上下文（LE scanning listener context）。注意（Note）：回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 127.1\_数据成员（Data Fields）

<a id="r_a71d73c1da28d4a27626f77d96a5b3541"></a>

```c
void(* recv )(const struct bt_le_scan_recv_info *info, struct net_buf_simple *buf)
```

相关声明：[recv](#a71d73c1da28d4a27626f77d96a5b3541)、[bt_le_scan_recv_info](P129_bt_le_scan_recv_info_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

广播数据包和扫描响应接收回调（Advertisement packet and scan response received callback）。

<a id="r_a2f57f3fee46bd137065f4c57d0cd5157"></a>

```c
void(* timeout )(void)
```

相关声明：[timeout](#a2f57f3fee46bd137065f4c57d0cd5157)。

扫描器已因扫描超时（Scan timeout）停止扫描。

<a id="r_a50dbc5e7618fd488e9acb7ad8f104a63"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a50dbc5e7618fd488e9acb7ad8f104a63)。

## 127.2\_详细说明（Detailed Documentation）

<a id="a50dbc5e7618fd488e9acb7ad8f104a63"></a>

### `node`

```c
sys_snode_t bt_le_scan_cb::node
```

<a id="a71d73c1da28d4a27626f77d96a5b3541"></a>

### `recv`

```c
void(* bt_le_scan_cb::recv) (const struct bt_le_scan_recv_info *info, struct net_buf_simple *buf)
```

广播数据包和扫描响应接收回调（Advertisement packet and scan response received callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 广播数据包和扫描响应信息（Advertiser packet and scan response information）。 |
| `buf` | 包含广播数据（Advertiser data）的缓冲区。 |

<a id="a2f57f3fee46bd137065f4c57d0cd5157"></a>

### `timeout`

```c
void(* bt_le_scan_cb::timeout) (void)
```

扫描器已因扫描超时（Scan timeout）停止扫描。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 127.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_le_scan_recv_info](P129_bt_le_scan_recv_info_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P126_bt_le_per_adv_sync_transfer_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P128_bt_le_scan_param_结构体.md)
