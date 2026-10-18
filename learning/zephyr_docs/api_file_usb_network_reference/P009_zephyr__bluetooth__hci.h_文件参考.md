---
id: learning.zephyr-docs.api-file-usb-network-reference.page-9
title: zephyr__bluetooth__hci.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_bluetooth\_\_hci.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.1\_类型定义（Typedefs）

<a id="r_a061c7eee0b02021da072d9859ef838a6"></a>

```c
typedef bool bt_hci_vnd_evt_cb_t(struct net_buf_simple *buf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_hci_vnd_evt_cb_t](#a061c7eee0b02021da072d9859ef838a6)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于厂商处理 HCI 厂商特定事件（HCI Vendor-Specific Event）的回调类型（Callback Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.2\_函数（Functions）

<a id="r_a31f7876c1a3e5dc7f1e1b2949b08139f"></a>

```c
static const char * bt_hci_err_to_str (uint8_t hci_err)
```

相关声明：[bt_hci_err_to_str](#a31f7876c1a3e5dc7f1e1b2949b08139f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 HCI 错误（HCI Error）转换为字符串。

<a id="r_a974e6e9262601e73537cbdcba7a7c93c"></a>

```c
struct net_buf * bt_hci_cmd_alloc (k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hci_cmd_alloc](#a974e6e9262601e73537cbdcba7a7c93c)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配 HCI 命令缓冲区（HCI Command Buffer）。

<a id="r_af2eed9d93da45185aad9c2edc0001a54"></a>

```c
int bt_hci_cmd_send (uint16_t opcode, struct net_buf *buf)
```

相关声明：[bt_hci_cmd_send](#af2eed9d93da45185aad9c2edc0001a54)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

异步发送 HCI 命令（HCI Command）。

<a id="r_a8d306b5b56afdece1cadbbf0eecfe5a7"></a>

```c
int bt_hci_cmd_send_sync (uint16_t opcode, struct net_buf *buf, struct net_buf **rsp)
```

相关声明：[bt_hci_cmd_send_sync](#a8d306b5b56afdece1cadbbf0eecfe5a7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

同步发送 HCI 命令（HCI Command）。

<a id="r_ac223ac9cddf8696d853c0942f9f148e0"></a>

```c
int bt_hci_get_conn_handle (const struct bt_conn *conn, uint16_t *conn_handle)
```

相关声明：[bt_hci_get_conn_handle](#ac223ac9cddf8696d853c0942f9f148e0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取连接的连接句柄（Connection Handle）。

<a id="r_a73ba00112117da9ce60c850fa4cb4722"></a>

```c
struct bt_conn * bt_hci_conn_lookup_handle (uint16_t handle)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hci_conn_lookup_handle](#a73ba00112117da9ce60c850fa4cb4722)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据连接句柄（Connection Handle）获取连接。

<a id="r_a27f6cd853c079e4412adbe4a1b32f8e6"></a>

```c
int bt_hci_get_adv_handle (const struct bt_le_ext_adv *adv, uint8_t *adv_handle)
```

相关声明：[bt_hci_get_adv_handle](#a27f6cd853c079e4412adbe4a1b32f8e6)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取广播集的广播句柄（Advertising Handle）。

<a id="r_a8bf5e3e8b55633350a4cb34c928bce4d"></a>

```c
struct bt_le_ext_adv * bt_hci_adv_lookup_handle (uint8_t handle)
```

相关声明：[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_hci_adv_lookup_handle](#a8bf5e3e8b55633350a4cb34c928bce4d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据广播句柄（Advertising Handle）获取广播集。

<a id="r_a73fa69c6e4faea073433f3f73d327c46"></a>

```c
int bt_hci_get_adv_sync_handle (const struct bt_le_per_adv_sync *sync, uint16_t *sync_handle)
```

相关声明：[bt_hci_get_adv_sync_handle](#a73fa69c6e4faea073433f3f73d327c46)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取周期广播同步句柄（Periodic Advertising Sync Handle）。

<a id="r_a425f0cee74f061bb7f11e73da3ac627d"></a>

```c
struct bt_le_per_adv_sync * bt_hci_per_adv_sync_lookup_handle (uint16_t handle)
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_hci_per_adv_sync_lookup_handle](#a425f0cee74f061bb7f11e73da3ac627d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据周期广播同步句柄（Periodic Advertising Sync Handle）获取周期广播同步对象。

<a id="r_a9931a6d4e55140e741b78656cb43e88c"></a>

```c
const char * bt_hci_get_ver_str (uint8_t core_version)
```

相关声明：[bt_hci_get_ver_str](#a9931a6d4e55140e741b78656cb43e88c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据核心版本号（Core Version Number）获取版本字符串。

<a id="r_ae41be6f3dd87016bbb92f004adeb6ece"></a>

```c
int bt_hci_register_vnd_evt_cb (bt_hci_vnd_evt_cb_t cb)
```

相关声明：[bt_hci_register_vnd_evt_cb](#ae41be6f3dd87016bbb92f004adeb6ece)、[bt_hci_vnd_evt_cb_t](#a061c7eee0b02021da072d9859ef838a6)。

注册用于 HCI 厂商特定事件（HCI Vendor-Specific Event）的用户回调（User Callback）。

<a id="r_a50f4a8808c26a7b4e288e650b2325883"></a>

```c
int bt_hci_le_rand (void *buffer, size_t len)
```

相关声明：[bt_hci_le_rand](#a50f4a8808c26a7b4e288e650b2325883)。

从低功耗控制器（LE Controller）获取随机字节。

## 9.3\_详细说明（Detailed Documentation）

<a id="a061c7eee0b02021da072d9859ef838a6"></a>

### `bt_hci_vnd_evt_cb_t`

```c
typedef bool bt_hci_vnd_evt_cb_t(struct net_buf_simple *buf)
```

用于厂商处理 HCI 厂商特定事件（HCI Vendor-Specific Event）的回调类型（Callback Type）。

通过 `bt_hci_register_vnd_evt_cb()` 注册此类型的函数，并在发生任何 HCI 厂商特定事件（HCI Vendor-Specific Event）时调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含事件参数（Event Parameters）的缓冲区。 |

**返回（Returns）**：返回值（Returns）：如果函数已处理该事件，则为 `true`；如果将该事件交回协议栈（Stack）处理，则为 `false`。

<a id="a8bf5e3e8b55633350a4cb34c928bce4d"></a>

### `bt_hci_adv_lookup_handle()`

```c
struct bt_le_ext_adv * bt_hci_adv_lookup_handle ( uint8_t handle)
```

根据广播句柄（Advertising Handle）获取广播集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 广播句柄（Advertising Handle）。 |

**返回（Returns）**：返回值（Returns）：成功时为对应的广播集（Advertising Set）；若不存在，则为 `NULL`。

<a id="a974e6e9262601e73537cbdcba7a7c93c"></a>

### `bt_hci_cmd_alloc()`

```c
struct net_buf * bt_hci_cmd_alloc ( k_timeout_t timeout)
```

分配 HCI 命令缓冲区（HCI Command Buffer）。

本函数为 HCI 命令分配新缓冲区（Buffer）。成功返回后，即可向该缓冲区编码命令参数。缓冲区会自动预留足够的头部空间（Headroom），以便稍后在调用 `bt_hci_cmd_send()` 或 `bt_hci_cmd_send_sync()` 时编码实际命令头和 H:4 头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 分配操作的超时（Allocation Timeout）。 |

**返回（Returns）**：返回值（Returns）：新分配的缓冲区（Buffer）；分配失败时为 `NULL`。

<a id="af2eed9d93da45185aad9c2edc0001a54"></a>

### `bt_hci_cmd_send()`

```c
int bt_hci_cmd_send ( uint16_t opcode, struct net_buf * buf )
```

异步发送 HCI 命令（HCI Command）。

本函数用于异步发送 HCI 命令（HCI Command）。可传入由 `bt_hci_cmd_alloc()` 创建的缓冲区；如果命令没有参数，也可传入 `NULL`。命令以异步方式发送，因此本函数成功返回时，调用者只能确定命令已成功入队（Queued）。

如果需要同步行为（Synchronous Behavior），并获取命令完成（Command Complete）参数，应改用 `bt_hci_cmd_send_sync()` API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `opcode` | 命令操作码（Command OpCode）。 |
| `buf` | 命令缓冲区（Command Buffer）；没有参数时为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EHOSTDOWN` | HCI 传输（HCI Transport）尚未打开，即蓝牙（Bluetooth）尚未启用。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，表示命令已入队；失败时为负的 `errno` 值。

<a id="a8d306b5b56afdece1cadbbf0eecfe5a7"></a>

### `bt_hci_cmd_send_sync()`

```c
int bt_hci_cmd_send_sync ( uint16_t opcode, struct net_buf * buf, struct net_buf ** rsp )
```

同步发送 HCI 命令（HCI Command）。

本函数用于同步发送 HCI 命令（HCI Command）。可传入由 `bt_hci_cmd_alloc()` 创建的缓冲区；如果命令没有参数，也可传入 `NULL`。

本函数会阻塞，直至收到命令状态（Command Status）或命令完成（Command Complete）事件。如果任一事件的状态非零，则函数返回负错误码，且不会设置响应引用（Response Reference）。如果命令成功完成，并且传入了非 `NULL` 的 `rsp` 参数，则将该参数设为指向包含响应参数的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `opcode` | 命令操作码（Command OpCode）。 |
| `buf` | 命令缓冲区（Command Buffer）；没有参数时为 `NULL`。 |
| `rsp` | 用于存储命令响应引用（Command Response Reference）的位置。如果调用者不关心响应参数，可为 `NULL`。如果传入非 `NULL`，调用者须负责在完成解析后对该缓冲区调用 `net_buf_unref()`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EHOSTDOWN` | HCI 传输（HCI Transport）尚未打开，即蓝牙（Bluetooth）尚未启用。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，表示命令已完成；失败时为负的 `errno` 值。

<a id="a73ba00112117da9ce60c850fa4cb4722"></a>

### `bt_hci_conn_lookup_handle()`

```c
struct bt_conn * bt_hci_conn_lookup_handle ( uint16_t handle)
```

根据连接句柄（Connection Handle）获取连接。

调用者获得连接对象（Connection Object）的一个新引用；使用完该对象后，必须通过 bt_conn_unref() 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 连接句柄（Connection Handle）。 |

**返回（Returns）**：返回值（Returns）：成功时为对应的连接对象（Connection Object）；若不存在，则为 `NULL`。

<a id="a31f7876c1a3e5dc7f1e1b2949b08139f"></a>

### `bt_hci_err_to_str()`

```c
const char * bt_hci_err_to_str ( uint8_t hci_err)
```

声明属性：`inline`、`static`。

将 HCI 错误（HCI Error）转换为字符串。

错误码（Error Code）在蓝牙核心规范（Bluetooth Core Specification）第 1 卷 F 部分第 2 节中描述。

第 4 卷 E 部分的 HCI 文档说明各错误码（Error Code）的使用情形。

另请参见已定义的 `BT_HCI_ERR_*` 宏。

**返回（Returns）**：返回值（Returns）：HCI 错误码的字符串表示。如果未启用 `CONFIG_BT_HCI_ERR_TO_STR`，则仅返回空字符串。

<a id="a27f6cd853c079e4412adbe4a1b32f8e6"></a>

### `bt_hci_get_adv_handle()`

```c
int bt_hci_get_adv_handle ( const struct bt_le_ext_adv * adv, uint8_t * adv_handle )
```

获取广播集的广播句柄（Advertising Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集（Advertising Set）。 |
| `adv_handle` | 用于存储广播句柄（Advertising Handle）的位置。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="a73fa69c6e4faea073433f3f73d327c46"></a>

### `bt_hci_get_adv_sync_handle()`

```c
int bt_hci_get_adv_sync_handle ( const struct bt_le_per_adv_sync * sync, uint16_t * sync_handle )
```

获取周期广播同步句柄（Periodic Advertising Sync Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步集（Periodic Advertising Sync Set）。 |
| `sync_handle` | 用于存储周期广播同步句柄（Periodic Advertising Sync Handle）的位置。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ac223ac9cddf8696d853c0942f9f148e0"></a>

### `bt_hci_get_conn_handle()`

```c
int bt_hci_get_conn_handle ( const struct bt_conn * conn, uint16_t * conn_handle )
```

获取连接的连接句柄（Connection Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `conn_handle` | 用于存储连接句柄（Connection Handle）的位置。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="a9931a6d4e55140e741b78656cb43e88c"></a>

### `bt_hci_get_ver_str()`

```c
const char * bt_hci_get_ver_str ( uint8_t core_version)
```

根据核心版本号（Core Version Number）获取版本字符串。

可以通过发出 HCI 读取本地版本信息命令（HCI Read Local Version Information）获取控制器的核心版本（Core Version）。

另请参见以 `BT_HCI_VERSION_` 为前缀的定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `core_version` | 核心版本（Core Version）。 |

**返回（Returns）**：返回值（Returns）：与核心版本号（Core Version Number）对应的版本字符串。

<a id="a50f4a8808c26a7b4e288e650b2325883"></a>

### `bt_hci_le_rand()`

```c
int bt_hci_le_rand ( void * buffer, size_t len )
```

从低功耗控制器（LE Controller）获取随机字节。

根据需要，多次向低功耗控制器（LE Controller）发送 `HCI_LE_Rand`，直至填满提供的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buffer` | 用于填入随机字节（Random Bytes）的缓冲区。 |
| `len` | 缓冲区长度，单位为字节。 |

**说明（Note）**：注意（Note）：本函数是一个辅助函数，通过 `HCI_LE_Rand` 命令从低功耗控制器（LE Controller）收集任意数量的随机字节。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="a425f0cee74f061bb7f11e73da3ac627d"></a>

### `bt_hci_per_adv_sync_lookup_handle()`

```c
struct bt_le_per_adv_sync * bt_hci_per_adv_sync_lookup_handle ( uint16_t handle)
```

根据周期广播同步句柄（Periodic Advertising Sync Handle）获取周期广播同步对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 周期同步集句柄（Periodic Sync Set Handle）。 |

**返回（Returns）**：返回值（Returns）：成功时为对应的周期广播同步集对象（Periodic Advertising Sync Set Object）；若不存在，则为 `NULL`。

<a id="ae41be6f3dd87016bbb92f004adeb6ece"></a>

### `bt_hci_register_vnd_evt_cb()`

```c
int bt_hci_register_vnd_evt_cb ( bt_hci_vnd_evt_cb_t cb)
```

注册用于 HCI 厂商特定事件（HCI Vendor-Specific Event）的用户回调（User Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 协议栈（Stack）收到 HCI 厂商特定事件（HCI Vendor-Specific Event）时调用的回调。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。


## 9.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [net_buf_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [CONFIG_BT_HCI_ERR_TO_STR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_ERR_TO_STR)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_zephyr__net__ethernet.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__bluetooth__mesh__health_faults.h_文件参考.md)
