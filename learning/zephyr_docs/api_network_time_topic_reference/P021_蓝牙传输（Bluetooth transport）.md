---
id: learning.zephyr-docs.api-network-time-topic-reference.page-21
title: 蓝牙传输（Bluetooth transport）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_蓝牙传输（Bluetooth transport）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

允许通过蓝牙使用 MCUmgr SMP 协议。

<a id="details"></a>

允许通过蓝牙使用 MCUmgr SMP 协议。

<a id="header-files"></a>
<a id="files"></a>

## 21.1\_文件（Files）

<a id="r_smp_5Fbt_2Eh"></a>

```c
file smp_bt.h
```

相关声明：[smp_bt.h](../api_file_system_device_reference/P046_zephyr__mgmt__mcumgr__transport__smp_bt.h_文件参考.md)。

mcumgr简单管理协议（SMP）的蓝牙传输。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga35a151d8a3e9fb6f5e2e355c0c23f17c"></a>

```c
#define SMP_BT_SVC_UUID_VAL BT_UUID_128_ENCODE(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84)
```

相关声明：[SMP_BT_SVC_UUID_VAL](#ga35a151d8a3e9fb6f5e2e355c0c23f17c)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

简单管理协议（SMP）服务的通用唯一标识符（UUID）值。

<a id="r_gafa04c341a4ed3b5a10c07d268266acc3"></a>

```c
#define SMP_BT_SVC_UUID BT_UUID_DECLARE_128(SMP_BT_SVC_UUID_VAL)
```

相关声明：[SMP_BT_SVC_UUID](#gafa04c341a4ed3b5a10c07d268266acc3)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[SMP_BT_SVC_UUID_VAL](#ga35a151d8a3e9fb6f5e2e355c0c23f17c)。

SMP 服务 UUID。

<a id="r_ga3f75f06a2f437008ecbe87474971a4ec"></a>

```c
#define SMP_BT_CHR_UUID_VAL BT_UUID_128_ENCODE(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48)
```

相关声明：[SMP_BT_CHR_UUID_VAL](#ga3f75f06a2f437008ecbe87474971a4ec)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

SMP 特征（characteristic）的 UUID 值。

<a id="r_gaa42455942e31ddafc6174c5eca6f85ac"></a>

```c
#define SMP_BT_CHR_UUID BT_UUID_DECLARE_128(SMP_BT_CHR_UUID_VAL)
```

相关声明：[SMP_BT_CHR_UUID](#gaa42455942e31ddafc6174c5eca6f85ac)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[SMP_BT_CHR_UUID_VAL](#ga3f75f06a2f437008ecbe87474971a4ec)。

SMP 特征 UUID，同时用于请求和响应。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_ga9ceedfe6c84f194ff103356a4c30331f"></a>

```c
int smp_bt_register (void)
```

相关声明：[smp_bt_register](#ga9ceedfe6c84f194ff103356a4c30331f)。

注册 SMP 蓝牙服务。

<a id="r_gad19e1e1ba3ed59f13b5953bfda53ac15"></a>

```c
int smp_bt_unregister (void)
```

相关声明：[smp_bt_unregister](#gad19e1e1ba3ed59f13b5953bfda53ac15)。

注销 SMP 蓝牙服务。

<a id="r_ga8f52f0fda08b308dd7f1272b5ce5ba84"></a>

```c
int smp_bt_notify (struct bt_conn *conn, const void *data, uint16_t len)
```

相关声明：[smp_bt_notify](#ga8f52f0fda08b308dd7f1272b5ce5ba84)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过指定蓝牙连接，以通知（notification）形式传输 SMP 命令／响应。

## 21.4\_详细说明（Detailed Documentation）

<a id="gaa42455942e31ddafc6174c5eca6f85ac"></a>

### `SMP_BT_CHR_UUID`

```c
#define SMP_BT_CHR_UUID BT_UUID_DECLARE_128(SMP_BT_CHR_UUID_VAL)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

SMP 特征 UUID，同时用于请求和响应。

<a id="ga3f75f06a2f437008ecbe87474971a4ec"></a>

### `SMP_BT_CHR_UUID_VAL`

```c
#define SMP_BT_CHR_UUID_VAL BT_UUID_128_ENCODE(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

SMP 特征（characteristic）的 UUID 值。

<a id="gafa04c341a4ed3b5a10c07d268266acc3"></a>

### `SMP_BT_SVC_UUID`

```c
#define SMP_BT_SVC_UUID BT_UUID_DECLARE_128(SMP_BT_SVC_UUID_VAL)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

SMP 服务 UUID。

<a id="ga35a151d8a3e9fb6f5e2e355c0c23f17c"></a>

### `SMP_BT_SVC_UUID_VAL`

```c
#define SMP_BT_SVC_UUID_VAL BT_UUID_128_ENCODE(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

简单管理协议（SMP）服务的通用唯一标识符（UUID）值。

<a id="ga8f52f0fda08b308dd7f1272b5ce5ba84"></a>

### `smp_bt_notify()`

```c
int smp_bt_notify ( struct bt_conn * conn, const void * data, uint16_t len )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

通过指定蓝牙连接，以通知（notification）形式传输 SMP 命令／响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `data` | 指向简单管理协议（SMP）消息的指针。 |
| `len` | 数据长度（Data Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga9ceedfe6c84f194ff103356a4c30331f"></a>

### `smp_bt_register()`

```c
int smp_bt_register ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

注册 SMP 蓝牙服务。

只有先通过 `smp_bt_unregister()` 注销蓝牙传输层后，才应调用。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gad19e1e1ba3ed59f13b5953bfda53ac15"></a>

### `smp_bt_unregister()`

```c
int smp_bt_unregister ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_bt.h>
```

注销 SMP 蓝牙服务。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 21.5\_原页交叉引用（Cross References）

- [smp_bt.h](../api_file_system_device_reference/P046_zephyr__mgmt__mcumgr__transport__smp_bt.h_文件参考.md)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_向量绝对值（Vector Absolute Value）.md) · [返回大纲](大纲.md) · [下一章](P022_网络时间表示（Network time representation）。.md)
