---
id: learning.zephyr-docs.api-connection-topic-reference.page-2
title: 蓝牙内容控制标识符（Bluetooth Content Control Identifier）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙内容控制标识符（Bluetooth Content Control Identifier）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙内容控制标识符（Bluetooth Content Control Identifier，CCID）

<a id="details"></a>

蓝牙内容控制标识符（Bluetooth Content Control Identifier，CCID）。自 Zephyr 3.7 起提供；API 版本为 0.8.0。CCID API 管理 `BT_UUID_CCID` 特征所用的 CCID。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga1be6ef63b32f44100a77e48c88a9c126"></a>

```c
#define BT_CCID_MIN 0U
```

相关声明：[BT_CCID_MIN](#ga1be6ef63b32f44100a77e48c88a9c126)。

CCID 的最小值。

<a id="r_gaae664247d3537ab473c2f533602b2afa"></a>

```c
#define BT_CCID_MAX 255U
```

相关声明：[BT_CCID_MAX](#gaae664247d3537ab473c2f533602b2afa)。

CCID 的最大值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_gad621dd750e4b1c23791afc72785990fc"></a>

```c
int bt_ccid_alloc_value (void)
```

相关声明：[bt_ccid_alloc_value](#gad621dd750e4b1c23791afc72785990fc)。

分配一个 CCID 值。

<a id="r_ga07845fe5cc445a35448881430f528609"></a>

```c
const struct bt_gatt_attr * bt_ccid_find_attr (uint8_t ccid)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_ccid_find_attr](#ga07845fe5cc445a35448881430f528609)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 CCID 值对应的通用属性配置文件（GATT）属性。

## 2.3\_详细说明（Detailed Documentation）

<a id="gaae664247d3537ab473c2f533602b2afa"></a>

### `BT_CCID_MAX`

```c
#define BT_CCID_MAX 255U
```

```c
#include <zephyr/bluetooth/audio/ccid.h>
```

CCID 的最大值。

<a id="ga1be6ef63b32f44100a77e48c88a9c126"></a>

### `BT_CCID_MIN`

```c
#define BT_CCID_MIN 0U
```

```c
#include <zephyr/bluetooth/audio/ccid.h>
```

CCID 的最小值。

<a id="gad621dd750e4b1c23791afc72785990fc"></a>

### `bt_ccid_alloc_value()`

```c
int bt_ccid_alloc_value ( void )
```

```c
#include <zephyr/bluetooth/audio/ccid.h>
```

分配一个 CCID 值。

应始终在注册包含 `BT_UUID_CCID` 特征的 GATT 服务之前立即调用此函数。如果仅分配 CCID 而不注册该特征，在极少数情况下可能导致设备上出现重复 CCID。

要求启用 `CONFIG_BT_CONN`。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `ccid` | 成功时返回 8 位无符号 CCID 值。 |
| `-ENOMEM` | 无法再分配更多 CCID。 |

<a id="ga07845fe5cc445a35448881430f528609"></a>

### `bt_ccid_find_attr()`

```c
const struct bt_gatt_attr * bt_ccid_find_attr ( uint8_t ccid)
```

```c
#include <zephyr/bluetooth/audio/ccid.h>
```

获取 CCID 值对应的通用属性配置文件（GATT）属性。

在当前 GATT 数据库中搜索 CCID 值与所提供值相同的 CCID 特征。

要求启用 `CONFIG_BT_CONN`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ccid` | 要搜索的 CCID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 未找到任何匹配项。 |
| `attr` | 指向 GATT 属性（attribute）的指针。 |


## 2.4\_原页交叉引用（Cross References）

- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_UUID_CCID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab76981ff7b5fe1949c606e901daa33d3)
- [zephyr/bluetooth/audio/ccid.h](../api_file_interface_reference/P007_zephyr__bluetooth__audio__ccid.h_文件参考.md)
- [CONFIG_BT_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_ADXL345 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙H_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。.md)
