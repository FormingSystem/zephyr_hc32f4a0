---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-68
title: bt_gatt_subscribe_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__subscribe__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_bt\_gatt\_subscribe\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__subscribe__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 订阅（Subscribe）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 订阅（Subscribe）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_acf237ef097e8b847eb049fb0a5d4b759"></a>

```c
bt_gatt_notify_func_t notify
```

相关声明：[bt_gatt_notify_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gab3e53eb5f9bb1eda7bf612ef95755b4d)、[notify](#acf237ef097e8b847eb049fb0a5d4b759)。

通知值回调（Notification value callback）。

<a id="r_a91595407b8de4e862652e41100668f0a"></a>

```c
bt_gatt_subscribe_func_t subscribe
```

相关声明：[bt_gatt_subscribe_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2e914e63b4b91fa56bc3295283c43714)、[subscribe](#a91595407b8de4e862652e41100668f0a)。

订阅客户端特征配置写请求的响应回调（Subscribe CCC write request response callback）。若提供此回调，则调用时传入订阅时给定的订阅参数。

<a id="r_a9248418eb04a5b7a0faed5077c40bf22"></a>

```c
uint16_t value_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value_handle](#a9248418eb04a5b7a0faed5077c40bf22)。

订阅值句柄（Subscribe value handle）。

<a id="r_a77c53cdfd4143483b33a8ecf6061561e"></a>

```c
uint16_t ccc_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ccc_handle](#a77c53cdfd4143483b33a8ecf6061561e)。

订阅客户端特征配置句柄（Subscribe CCC handle）。

<a id="r_af806d24aa97db1f2e9a021e719598a6d"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#af806d24aa97db1f2e9a021e719598a6d)。

订阅结束句柄（Subscribe End handle），用于自动发现（Automatic discovery）。

<a id="r_ad3a3b9335b85777d65bdf875486e292a"></a>

```c
struct bt_gatt_discover_params * disc_params
```

相关声明：[bt_gatt_discover_params](P058_bt_gatt_discover_params_结构体.md)、[disc_params](#ad3a3b9335b85777d65bdf875486e292a)。

当 `ccc_handle = BT_GATT_AUTO_DISCOVER_CCC_HANDLE` 时使用的发现参数（Discover parameters）。

<a id="r_a3bff1209b7a0b5908408a568622d0150"></a>

```c
uint16_t value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a3bff1209b7a0b5908408a568622d0150)。

订阅值（Subscribe value）。

<a id="r_a5b34bad1cf39bb3efd5faf516473dd4a"></a>

```c
bt_security_t min_security
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[min_security](#a5b34bad1cf39bb3efd5faf516473dd4a)。

接收通知所要求的最低安全等级（Minimum required security）。

<a id="r_aedd24024881e22372505355024cd716b"></a>

```c
atomic_t flags [ATOMIC_BITMAP_SIZE(BT_GATT_SUBSCRIBE_NUM_FLAGS)]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flags](#aedd24024881e22372505355024cd716b)、[ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)、[BT_GATT_SUBSCRIBE_NUM_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)。

订阅标志（Subscription flags），参见 `bt_gatt_sub_flag`。

<a id="r_ae139848da09705d37fe7c9de4c1a4087"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#ae139848da09705d37fe7c9de4c1a4087)。

属性协议通道选项（ATT channel options）。

## 68.2\_详细说明（Detailed Documentation）

<a id="a77c53cdfd4143483b33a8ecf6061561e"></a>

### `ccc_handle`

```c
uint16_t bt_gatt_subscribe_params::ccc_handle
```

订阅客户端特征配置句柄（Subscribe CCC handle）。

<a id="ae139848da09705d37fe7c9de4c1a4087"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_subscribe_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="ad3a3b9335b85777d65bdf875486e292a"></a>

### `disc_params`

```c
struct bt_gatt_discover_params* bt_gatt_subscribe_params::disc_params
```

当 `ccc_handle = BT_GATT_AUTO_DISCOVER_CCC_HANDLE` 时使用的发现参数（Discover parameters）。

<a id="af806d24aa97db1f2e9a021e719598a6d"></a>

### `end_handle`

```c
uint16_t bt_gatt_subscribe_params::end_handle
```

订阅结束句柄（Subscribe End handle），用于自动发现（Automatic discovery）。

<a id="aedd24024881e22372505355024cd716b"></a>

### `flags`

```c
atomic_t bt_gatt_subscribe_params::flags[ATOMIC_BITMAP_SIZE(BT_GATT_SUBSCRIBE_NUM_FLAGS)]
```

订阅标志（Subscription flags），参见 `bt_gatt_sub_flag`。

<a id="a5b34bad1cf39bb3efd5faf516473dd4a"></a>

### `min_security`

```c
bt_security_t bt_gatt_subscribe_params::min_security
```

接收通知所要求的最低安全等级（Minimum required security）。

通过较低安全等级连接收到的通知（Notifications）和指示（Indications）将被静默丢弃。

<a id="acf237ef097e8b847eb049fb0a5d4b759"></a>

### `notify`

```c
bt_gatt_notify_func_t bt_gatt_subscribe_params::notify
```

通知值回调（Notification value callback）。

<a id="a91595407b8de4e862652e41100668f0a"></a>

### `subscribe`

```c
bt_gatt_subscribe_func_t bt_gatt_subscribe_params::subscribe
```

订阅客户端特征配置写请求的响应回调（Subscribe CCC write request response callback）。若提供此回调，则调用时传入订阅时给定的订阅参数。

<a id="a3bff1209b7a0b5908408a568622d0150"></a>

### `value`

```c
uint16_t bt_gatt_subscribe_params::value
```

订阅值（Subscribe value）。

<a id="a9248418eb04a5b7a0faed5077c40bf22"></a>

### `value_handle`

```c
uint16_t bt_gatt_subscribe_params::value_handle
```

订阅值句柄（Subscribe value handle）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_notify_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gab3e53eb5f9bb1eda7bf612ef95755b4d)
- [bt_gatt_subscribe_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2e914e63b4b91fa56bc3295283c43714)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_discover_params](P058_bt_gatt_discover_params_结构体.md)
- [BT_GATT_AUTO_DISCOVER_CCC_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7ca44e95989a143ae0b21e4a5316561d)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)
- [BT_GATT_SUBSCRIBE_NUM_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)
- [bt_gatt_sub_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaa43f45658809908baa72bf4e0ea745ac)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_bt_gatt_service_val_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_bt_gatt_write_params_结构体.md)
