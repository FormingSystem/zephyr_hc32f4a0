---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-4
title: 麦克风控制配置文件（Microphone Control Profile，MICP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_麦克风控制配置文件（Microphone Control Profile，MICP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

麦克风控制配置文件（Microphone Control Profile，MICP）

<a id="details"></a>

麦克风控制配置文件（Microphone Control Profile，MICP）。自 2.7 起提供，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fmicp_5Fmic_5Fdev_5Fregister_5Fparam"></a>

```c
struct bt_micp_mic_dev_register_param
```

相关声明：[bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)。

麦克风控制服务（Microphone Control Service）的注册参数结构。

<a id="r_bt_5Fmicp_5Fincluded"></a>

```c
struct bt_micp_included
```

相关声明：[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

麦克风控制配置文件（Microphone Control Profile）包含的服务。

<a id="r_bt_5Fmicp_5Fmic_5Fdev_5Fcb"></a>

```c
struct bt_micp_mic_dev_cb
```

相关声明：[bt_micp_mic_dev_cb](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md)。

保存麦克风设备（Microphone Device）回调的结构。

<a id="r_bt_5Fmicp_5Fmic_5Fctlr_5Fcb"></a>

```c
struct bt_micp_mic_ctlr_cb
```

相关声明：[bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)。

保存麦克风控制器（Microphone Controller）回调的结构。

<a id="r_bt_5Fmicp_5Fmic_5Fctlr"></a>

```c
struct bt_micp_mic_ctlr
```

相关声明：[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

不透明的麦克风控制器（Microphone Controller）实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga46cc0362c55cd9bdaf331de834a5fef5"></a>

```c
#define BT_MICP_MIC_DEV_AICS_CNT 0U
```

相关声明：[BT_MICP_MIC_DEV_AICS_CNT](#ga46cc0362c55cd9bdaf331de834a5fef5)。

定义麦克风控制配置文件（Microphone Control Profile）中麦克风设备（Microphone Device）可具有的麦克风控制服务（Microphone Control Service）实例最大数量。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga5dee6c7a1115bffbea39ba0575f369fc"></a>

```c
int bt_micp_mic_dev_register (struct bt_micp_mic_dev_register_param *param)
```

相关声明：[bt_micp_mic_dev_register](#ga5dee6c7a1115bffbea39ba0575f369fc)、[bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)。

初始化麦克风控制配置文件（Microphone Control Profile）的麦克风设备（Microphone Device）。

<a id="r_ga0541a36655024d9eadcff2d3e0c877f6"></a>

```c
int bt_micp_mic_dev_included_get (struct bt_micp_included *included)
```

相关声明：[bt_micp_mic_dev_included_get](#ga0541a36655024d9eadcff2d3e0c877f6)、[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

获取麦克风设备的包含服务（Included Services）。

<a id="r_ga19ec08afa7784b80fce039fe84a4e33c"></a>

```c
int bt_micp_mic_dev_unmute (void)
```

相关声明：[bt_micp_mic_dev_unmute](#ga19ec08afa7784b80fce039fe84a4e33c)。

取消麦克风设备的静音（Unmute）。

<a id="r_ga47f971c9c259e43504d586a55cf22c4e"></a>

```c
int bt_micp_mic_dev_mute (void)
```

相关声明：[bt_micp_mic_dev_mute](#ga47f971c9c259e43504d586a55cf22c4e)。

将麦克风设备静音（Mute）。

<a id="r_ga525c5d694f7d510d33f088e848733af6"></a>

```c
int bt_micp_mic_dev_mute_disable (void)
```

相关声明：[bt_micp_mic_dev_mute_disable](#ga525c5d694f7d510d33f088e848733af6)。

禁用麦克风设备的静音功能（Mute Functionality）。

<a id="r_ga263bf5cf51e4ef8d7e6986f0d8358da3"></a>

```c
int bt_micp_mic_dev_mute_get (void)
```

相关声明：[bt_micp_mic_dev_mute_get](#ga263bf5cf51e4ef8d7e6986f0d8358da3)。

读取麦克风设备的静音状态（Mute State）。

<a id="r_ga21e04942da32b15e75a0b0de3fb84167"></a>

```c
int bt_micp_mic_ctlr_included_get (struct bt_micp_mic_ctlr *mic_ctlr, struct bt_micp_included *included)
```

相关声明：[bt_micp_mic_ctlr_included_get](#ga21e04942da32b15e75a0b0de3fb84167)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

获取麦克风控制配置文件（Microphone Control Profile）的包含服务（Included Services）。

<a id="r_ga4b564e6b315a3861f1c3ba6098eabfe1"></a>

```c
int bt_micp_mic_ctlr_conn_get (const struct bt_micp_mic_ctlr *mic_ctlr, struct bt_conn **conn)
```

相关声明：[bt_micp_mic_ctlr_conn_get](#ga4b564e6b315a3861f1c3ba6098eabfe1)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取麦克风控制端实例（Microphone Controller Instance）的连接指针。

<a id="r_ga863030e1b836c01a1be964bce0c72025"></a>

```c
struct bt_micp_mic_ctlr * bt_micp_mic_ctlr_get_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_micp_mic_ctlr_get_by_conn](#ga863030e1b836c01a1be964bce0c72025)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

从连接指针获取麦克风控制端（Microphone Controller）。

<a id="r_ga26187007ebf35ba2a5c57a076a3a7212"></a>

```c
int bt_micp_mic_ctlr_discover (struct bt_conn *conn, struct bt_micp_mic_ctlr **mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_discover](#ga26187007ebf35ba2a5c57a076a3a7212)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

发现麦克风控制服务（Microphone Control Service）。

<a id="r_ga6248c90bb94cd138c5bf9c68cffda4fe"></a>

```c
int bt_micp_mic_ctlr_unmute (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_unmute](#ga6248c90bb94cd138c5bf9c68cffda4fe)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

取消远端麦克风设备的静音（Unmute）。

<a id="r_ga2d50f432703233c0f03cb139b6119faa"></a>

```c
int bt_micp_mic_ctlr_mute (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_mute](#ga2d50f432703233c0f03cb139b6119faa)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

将远端麦克风设备静音（Mute）。

<a id="r_ga5148e78053a3052d27677a1fa24e3847"></a>

```c
int bt_micp_mic_ctlr_mute_get (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_mute_get](#ga5148e78053a3052d27677a1fa24e3847)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

读取远端麦克风设备的静音状态（Mute State）。

<a id="r_ga148ffcd0672adff9ccfaf35c522897c4"></a>

```c
int bt_micp_mic_ctlr_cb_register (struct bt_micp_mic_ctlr_cb *cb)
```

相关声明：[bt_micp_mic_ctlr_cb_register](#ga148ffcd0672adff9ccfaf35c522897c4)、[bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)。

注册麦克风控制端（Microphone Controller）所用的回调。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.4\_应用错误码（Application Error Codes）

<a id="r_ga31ce5cce4aa28662de82735241ee49d8"></a>

```c
#define BT_MICP_ERR_MUTE_DISABLED 0x80U
```

相关声明：[BT_MICP_ERR_MUTE_DISABLED](#ga31ce5cce4aa28662de82735241ee49d8)。

静音／取消静音命令（Mute/Unmute Commands）已禁用。

## 4.5\_麦克风控制配置文件静音状态（Microphone Control Profile Mute States）

<a id="r_gaaf0327be66ebf4b0dd23282d4a46aa54"></a>

```c
#define BT_MICP_MUTE_UNMUTED 0x00U
```

相关声明：[BT_MICP_MUTE_UNMUTED](#gaaf0327be66ebf4b0dd23282d4a46aa54)。

麦克风处于非静音状态（Unmuted）。

<a id="r_ga5718e29fefc336fbee1875aa5b81f233"></a>

```c
#define BT_MICP_MUTE_MUTED 0x01U
```

相关声明：[BT_MICP_MUTE_MUTED](#ga5718e29fefc336fbee1875aa5b81f233)。

麦克风处于静音状态（Muted）。

<a id="r_gafc7ed719d471ca27aeb96aaa638c05cb"></a>

```c
#define BT_MICP_MUTE_DISABLED 0x02U
```

相关声明：[BT_MICP_MUTE_DISABLED](#gafc7ed719d471ca27aeb96aaa638c05cb)。

麦克风状态为禁用（Disabled），无法静音或取消静音。

## 4.6\_详细说明（Detailed Documentation）

<a id="ga31ce5cce4aa28662de82735241ee49d8"></a>

### `BT_MICP_ERR_MUTE_DISABLED`

```c
#define BT_MICP_ERR_MUTE_DISABLED 0x80U
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

静音／取消静音命令（Mute/Unmute Commands）已禁用。

<a id="ga46cc0362c55cd9bdaf331de834a5fef5"></a>

### `BT_MICP_MIC_DEV_AICS_CNT`

```c
#define BT_MICP_MIC_DEV_AICS_CNT 0U
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

定义麦克风控制配置文件（Microphone Control Profile）中麦克风设备（Microphone Device）可具有的麦克风控制服务（Microphone Control Service）实例最大数量。

<a id="gafc7ed719d471ca27aeb96aaa638c05cb"></a>

### `BT_MICP_MUTE_DISABLED`

```c
#define BT_MICP_MUTE_DISABLED 0x02U
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

麦克风状态为禁用（Disabled），无法静音或取消静音。

<a id="ga5718e29fefc336fbee1875aa5b81f233"></a>

### `BT_MICP_MUTE_MUTED`

```c
#define BT_MICP_MUTE_MUTED 0x01U
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

麦克风处于静音状态（Muted）。

<a id="gaaf0327be66ebf4b0dd23282d4a46aa54"></a>

### `BT_MICP_MUTE_UNMUTED`

```c
#define BT_MICP_MUTE_UNMUTED 0x00U
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

麦克风处于非静音状态（Unmuted）。

<a id="ga148ffcd0672adff9ccfaf35c522897c4"></a>

### `bt_micp_mic_ctlr_cb_register()`

```c
int bt_micp_mic_ctlr_cb_register ( struct bt_micp_mic_ctlr_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

注册麦克风控制端（Microphone Controller）所用的回调。

只能以客户端（Client）身份执行此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga4b564e6b315a3861f1c3ba6098eabfe1"></a>

### `bt_micp_mic_ctlr_conn_get()`

```c
int bt_micp_mic_ctlr_conn_get ( const struct bt_micp_mic_ctlr * mic_ctlr, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

获取麦克风控制端实例（Microphone Controller Instance）的连接指针。

获取麦克风控制端实例（Microphone Controller Instance）的蓝牙连接指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `conn` | 连接指针（Connection Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga26187007ebf35ba2a5c57a076a3a7212"></a>

### `bt_micp_mic_ctlr_discover()`

```c
int bt_micp_mic_ctlr_discover ( struct bt_conn * conn, struct bt_micp_mic_ctlr ** mic_ctlr )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

发现麦克风控制服务（Microphone Control Service）。

启动通用属性配置文件（GATT）发现，并设置句柄和订阅（Handles and Subscriptions）。在对对端设备执行任何其他操作之前，必须先调用一次；`bt_micp_mic_ctlr_cb::discover` 回调会通知何时可以开始远端操作。

- 参数（Parameters）：`conn` 为要为其初始化此配置文件的连接；`[out] mic_ctlr` 在成功时得到有效远端实例对象。返回值：成功返回 0，失败返回 GATT 错误值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` conn` | 要为其初始化此配置文件（Profile）的连接。 |
| `[out] mic_ctlr` | 成功时的有效远端实例对象（Remote Instance Object）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga863030e1b836c01a1be964bce0c72025"></a>

### `bt_micp_mic_ctlr_get_by_conn()`

```c
struct bt_micp_mic_ctlr * bt_micp_mic_ctlr_get_by_conn ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

从连接指针获取麦克风控制端（Microphone Controller）。

根据连接指针获取麦克风控制配置文件（Microphone Control Profile）的麦克风控制端指针。只能获取通过 `bt_micp_mic_ctlr_discover()` 初始化过的控制端。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接指针（Connection Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Pointer` | 指向麦克风控制配置文件（Microphone Control Profile）的麦克风控制端实例（Microphone Controller Instance）。 |
| `NULL` | `conn` 为 `NULL`，或者连接尚未完成发现（Discovery）时。 |

<a id="ga21e04942da32b15e75a0b0de3fb84167"></a>

### `bt_micp_mic_ctlr_included_get()`

```c
int bt_micp_mic_ctlr_included_get ( struct bt_micp_mic_ctlr * mic_ctlr, struct bt_micp_included * included )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

获取麦克风控制配置文件（Microphone Control Profile）的包含服务（Included Services）。

返回结构体指针，该结构体包含麦克风控制配置文件（Microphone Control Profile）中包含服务实例（Included Service Instances）的信息，例如指向音频输入控制服务（Audio Input Control Service）实例的指针。

要求启用 `CONFIG_BT_MICP_MIC_CTLR_AICS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `[out] included` | 用于保存结果的指针（Result Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2d50f432703233c0f03cb139b6119faa"></a>

### `bt_micp_mic_ctlr_mute()`

```c
int bt_micp_mic_ctlr_mute ( struct bt_micp_mic_ctlr * mic_ctlr)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

将远端麦克风设备静音（Mute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga5148e78053a3052d27677a1fa24e3847"></a>

### `bt_micp_mic_ctlr_mute_get()`

```c
int bt_micp_mic_ctlr_mute_get ( struct bt_micp_mic_ctlr * mic_ctlr)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

读取远端麦克风设备的静音状态（Mute State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga6248c90bb94cd138c5bf9c68cffda4fe"></a>

### `bt_micp_mic_ctlr_unmute()`

```c
int bt_micp_mic_ctlr_unmute ( struct bt_micp_mic_ctlr * mic_ctlr)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

取消远端麦克风设备的静音（Unmute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga0541a36655024d9eadcff2d3e0c877f6"></a>

### `bt_micp_mic_dev_included_get()`

```c
int bt_micp_mic_dev_included_get ( struct bt_micp_included * included)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

获取麦克风设备的包含服务（Included Services）。

返回结构体指针，该结构体包含麦克风设备（Microphone Device）所包含的音频输入控制服务（Audio Input Control Service）实例信息。

要求启用 `CONFIG_BT_MICP_MIC_DEV_AICS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `included` | 用于保存结果的指针（Result Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga47f971c9c259e43504d586a55cf22c4e"></a>

### `bt_micp_mic_dev_mute()`

```c
int bt_micp_mic_dev_mute ( void )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

将麦克风设备静音（Mute）。

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga525c5d694f7d510d33f088e848733af6"></a>

### `bt_micp_mic_dev_mute_disable()`

```c
int bt_micp_mic_dev_mute_disable ( void )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

禁用麦克风设备的静音功能（Mute Functionality）。

可通过调用 `bt_micp_mic_dev_mute` 或 `bt_micp_mic_dev_unmute` 重新使能。

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga263bf5cf51e4ef8d7e6986f0d8358da3"></a>

### `bt_micp_mic_dev_mute_get()`

```c
int bt_micp_mic_dev_mute_get ( void )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

读取麦克风设备的静音状态（Mute State）。

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga5dee6c7a1115bffbea39ba0575f369fc"></a>

### `bt_micp_mic_dev_register()`

```c
int bt_micp_mic_dev_register ( struct bt_micp_mic_dev_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

初始化麦克风控制配置文件（Microphone Control Profile）的麦克风设备（Microphone Device）。

使能麦克风控制服务实例（Microphone Control Service Instance），使麦克风控制端（Microphone Controllers）能够发现它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 指向初始化结构体（Initialization Structure）的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga19ec08afa7784b80fce039fe84a4e33c"></a>

### `bt_micp_mic_dev_unmute()`

```c
int bt_micp_mic_dev_unmute ( void )
```

```c
#include <zephyr/bluetooth/audio/micp.h>
```

取消麦克风设备的静音（Unmute）。

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。


## 4.7\_原页交叉引用（Cross References）

- [bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)
- [bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)
- [bt_micp_mic_dev_cb](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md)
- [bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)
- [bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/micp.h](../api_file_display_management_reference/P013_zephyr__bluetooth__audio__micp.h_文件参考.md)
- [bt_micp_mic_ctlr_cb::discover](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a2359b88344bf36c3a491b0126dac006b)
- [CONFIG_BT_MICP_MIC_CTLR_AICS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MICP_MIC_CTLR_AICS)
- [CONFIG_BT_MICP_MIC_DEV_AICS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MICP_MIC_DEV_AICS)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_固件分发模型（Firmware Distribution models）.md) · [返回大纲](大纲.md) · [下一章](P005_IT8XXX2 电压比较器（Voltage comparator）.md)
