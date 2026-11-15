---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-19
title: zephyr__bluetooth__services__nus.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_bluetooth\_\_services\_\_nus.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/services/nus/inst.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

<a id="r_bt_5Fnus_5Fcb"></a>

```c
struct bt_nus_cb
```

相关声明：[bt_nus_cb](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md)。

用于接收NUS服务（NUS Service）事件通知的回调。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.2\_宏定义（Macros）

<a id="r_a8da4aaa9c77a537805c7b5bff7fc4aa6"></a>

```c
#define BT_UUID_NUS_SRV_VAL BT_UUID_128_ENCODE(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

相关声明：[BT_UUID_NUS_SRV_VAL](#a8da4aaa9c77a537805c7b5bff7fc4aa6)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

Nordic UART 通用属性配置文件服务（GATT Service）的通用唯一标识符（UUIDs）。

<a id="r_ada90c739cf936ec52008fcc4f272e207"></a>

```c
#define BT_UUID_NUS_RX_CHAR_VAL BT_UUID_128_ENCODE(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

相关声明：[BT_UUID_NUS_RX_CHAR_VAL](#ada90c739cf936ec52008fcc4f272e207)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

<a id="r_a7636b61879884e6f6fc8e871ae09160b"></a>

```c
#define BT_UUID_NUS_TX_CHAR_VAL BT_UUID_128_ENCODE(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

相关声明：[BT_UUID_NUS_TX_CHAR_VAL](#a7636b61879884e6f6fc8e871ae09160b)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

<a id="r_a54ba967101dc2a5515b9cfd1272c569b"></a>

```c
#define BT_NUS_INST_DEFINE(_name)
```

相关声明：[BT_NUS_INST_DEFINE](#a54ba967101dc2a5515b9cfd1272c569b)。

用于定义 Nordic UART 服务（NUS）实例的宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.3\_函数（Functions）

<a id="r_a84cb19f07f861963c73614a04c0a375f"></a>

```c
int bt_nus_inst_cb_register (struct bt_nus_inst *inst, struct bt_nus_cb *cb, void *ctx)
```

相关声明：[bt_nus_inst_cb_register](#a84cb19f07f861963c73614a04c0a375f)、[bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)、[bt_nus_cb](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md)。

注册 NUS 服务端实例回调（Server Instance Callback）。

<a id="r_a997453fc8108f64a95186b130ea68076"></a>

```c
int bt_nus_inst_send (struct bt_conn *conn, struct bt_nus_inst *inst, const void *data, uint16_t len)
```

相关声明：[bt_nus_inst_send](#a997453fc8108f64a95186b130ea68076)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 NUS 实例发送数据（Send Data）。

<a id="r_a1a28f3d267b34856450f60803eed485f"></a>

```c
static int bt_nus_cb_register (struct bt_nus_cb *cb, void *ctx)
```

相关声明：[bt_nus_cb_register](#a1a28f3d267b34856450f60803eed485f)、[bt_nus_cb](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md)。

注册 NUS 服务端回调（Server Callback）。

<a id="r_a950188897461f1c1f78ffbabeae1180a"></a>

```c
static int bt_nus_send (struct bt_conn *conn, const void *data, uint16_t len)
```

相关声明：[bt_nus_send](#a950188897461f1c1f78ffbabeae1180a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 NUS 发送数据（Send Data）。

## 19.4\_详细说明（Detailed Documentation）

<a id="a54ba967101dc2a5515b9cfd1272c569b"></a>

### `BT_NUS_INST_DEFINE`

```c
#define BT_NUS_INST_DEFINE ( _name)
```

展开值（Value）：

```c
Z_INTERNAL_BT_NUS_INST_DEFINE(_name)
```

用于定义 Nordic UART 服务（NUS）实例的宏。

允许用户定义多个 NUS 实例，类似于串行端点（Serial Endpoints），并将各实例用于不同目的。可通过 Kconfig 定义默认 NUS 实例。

<a id="ada90c739cf936ec52008fcc4f272e207"></a>

### `BT_UUID_NUS_RX_CHAR_VAL`

```c
#define BT_UUID_NUS_RX_CHAR_VAL BT_UUID_128_ENCODE(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

<a id="a8da4aaa9c77a537805c7b5bff7fc4aa6"></a>

### `BT_UUID_NUS_SRV_VAL`

```c
#define BT_UUID_NUS_SRV_VAL BT_UUID_128_ENCODE(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

Nordic UART 通用属性配置文件服务（GATT Service）的通用唯一标识符（UUIDs）。

服务（Service）：`6e400001-b5a3-f393-e0a9-e50e24dcca9e`；接收特征（RX Characteristic）：`6e400002-b5a3-f393-e0a9-e50e24dcca9e`；发送特征（TX Characteristic）：`6e400003-b5a3-f393-e0a9-e50e24dcca9e`。

<a id="a7636b61879884e6f6fc8e871ae09160b"></a>

### `BT_UUID_NUS_TX_CHAR_VAL`

```c
#define BT_UUID_NUS_TX_CHAR_VAL BT_UUID_128_ENCODE(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
```

<a id="a1a28f3d267b34856450f60803eed485f"></a>

### `bt_nus_cb_register()`

```c
int bt_nus_cb_register ( struct bt_nus_cb * cb, void * ctx )
```

声明属性：`inline`、`static`。

注册 NUS 服务端回调（Server Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callbacks Structure）的指针。必须在应用的整个生命周期内保持有效。 |
| `ctx` | 通过回调函数传递的用户上下文（User Context）。 |

**返回（Returns）**：返回值：成功返回 0；失败返回负错误码。`cb` 为 `NULL` 时返回 `-EINVAL`。

<a id="a84cb19f07f861963c73614a04c0a375f"></a>

### `bt_nus_inst_cb_register()`

```c
int bt_nus_inst_cb_register ( struct bt_nus_inst * inst, struct bt_nus_cb * cb, void * ctx )
```

注册 NUS 服务端实例回调（Server Instance Callback）。

此函数注册回调函数（Callbacks），它们会在发生与 NUS 有关的特定事件时被调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向 NUS 服务实例（Service Instance）的指针。使用默认实例时为 `NULL`。 |
| `cb` | 指向回调结构体（Callbacks Structure）的指针。必须在应用的整个生命周期内保持有效。 |
| `ctx` | 通过回调函数传递的用户上下文（User Context）。 |

**返回（Returns）**：返回值：成功时返回 0；`cb` 为 `NULL` 时返回 `-EINVAL`。

<a id="a997453fc8108f64a95186b130ea68076"></a>

### `bt_nus_inst_send()`

```c
int bt_nus_inst_send ( struct bt_conn * conn, struct bt_nus_inst * inst, const void * data, uint16_t len )
```

向 NUS 实例发送数据（Send Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要向其发送数据的连接对象（Connection Object）。通知所有对端时为 `NULL`。 |
| `inst` | 指向 NUS 服务实例（Service Instance）的指针。使用默认实例时为 `NULL`。 |
| `data` | 指向包含待发送字节的缓冲区（Buffer）的指针。 |
| `len` | 待发送数据的长度，单位为字节（Bytes）。 |

**说明（Note）**：注意：此 API 向指定对端（Peer）发送数据。

**返回（Returns）**：返回值：成功返回 0；失败返回负错误码。蓝牙协议栈（Bluetooth Stack）尚未启用时返回 `-EAGAIN`；尚未建立连接，或没有任何对端订阅时返回 `-ENOTCONN`。

<a id="a950188897461f1c1f78ffbabeae1180a"></a>

### `bt_nus_send()`

```c
int bt_nus_send ( struct bt_conn * conn, const void * data, uint16_t len )
```

声明属性：`inline`、`static`。

通过 NUS 发送数据（Send Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要向其发送数据的连接对象（Connection Object）。通知所有对端时为 `NULL`。 |
| `data` | 指向包含待发送字节的缓冲区（Buffer）的指针。 |
| `len` | 待发送数据的长度，单位为字节（Bytes）。 |

**说明（Note）**：注意：此 API 向指定对端（Peer）发送数据。

**返回（Returns）**：返回值：成功返回 0；失败返回负错误码。蓝牙协议栈（Bluetooth Stack）尚未启用时返回 `-EAGAIN`；尚未建立连接，或没有任何对端订阅时返回 `-ENOTCONN`。


## 19.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/bluetooth/services/nus/inst.h](../api_source_reference/P390_inst.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P609_nus.h_源码浏览.md)
- [bt_nus_cb](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__drivers__comparator__nrf_lpcomp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__display__panel.h_文件参考.md)
