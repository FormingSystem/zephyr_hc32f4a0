---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-3
title: 通用属性配置文件（Generic Attribute Profile，GATT）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_通用属性配置文件（Generic Attribute Profile，GATT）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用属性配置文件（Generic Attribute Profile，GATT）

<a id="details"></a>

通用属性配置文件（Generic Attribute Profile，GATT）。GATT 层提供服务注册与属性声明 API，以管理服务数据库（Service Database）。更多信息参见 GATT 客户端 API（GATT Client APIs）和 GATT 服务器 API（GATT Server APIs）。自 1.0 引入，版本 1.0.1。

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_bt_5Fgatt_5Fclient"></a>

相关声明：[GATT 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html)。

<a id="r_bt_5Fgatt_5Fserver"></a>

相关声明：[GATT 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_bt_5Fgatt_5Fattr"></a>

```c
struct bt_gatt_attr
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

通用属性配置文件（GATT）属性（Attribute）。

<a id="r_bt_5Fgatt_5Fservice_5Fstatic"></a>

```c
struct bt_gatt_service_static
```

相关声明：[bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)。

静态 GATT 服务结构体。

<a id="r_bt_5Fgatt_5Fservice"></a>

```c
struct bt_gatt_service
```

相关声明：[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

GATT 服务（Service）结构体。

<a id="r_bt_5Fgatt_5Fservice_5Fval"></a>

```c
struct bt_gatt_service_val
```

相关声明：[bt_gatt_service_val](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)。

服务（Service）属性值。

<a id="r_bt_5Fgatt_5Finclude"></a>

```c
struct bt_gatt_include
```

相关声明：[bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)。

包含服务（Include）属性值。

<a id="r_bt_5Fgatt_5Fcb"></a>

```c
struct bt_gatt_cb
```

相关声明：[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

GATT 回调结构体。

<a id="r_bt_5Fgatt_5Fauthorization_5Fcb"></a>

```c
struct bt_gatt_authorization_cb
```

相关声明：[bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)。

GATT 授权（Authorization）回调结构体。

<a id="r_bt_5Fgatt_5Fchrc"></a>

```c
struct bt_gatt_chrc
```

相关声明：[bt_gatt_chrc](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)。

特征声明（Characteristic Declaration）的属性值。

<a id="r_bt_5Fgatt_5Fcep"></a>

```c
struct bt_gatt_cep
```

相关声明：[bt_gatt_cep](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)。

特征扩展属性（Characteristic Extended Properties）属性值。

<a id="r_bt_5Fgatt_5Fccc"></a>

```c
struct bt_gatt_ccc
```

相关声明：[bt_gatt_ccc](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)。

客户端特征配置（Client Characteristic Configuration，CCC）属性值。

<a id="r_bt_5Fgatt_5Fscc"></a>

```c
struct bt_gatt_scc
```

相关声明：[bt_gatt_scc](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)。

服务器特征配置（Server Characteristic Configuration）属性值。

<a id="r_bt_5Fgatt_5Fcpf"></a>

```c
struct bt_gatt_cpf
```

相关声明：[bt_gatt_cpf](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)。

GATT 特征呈现格式（Characteristic Presentation Format）属性值。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.3\_宏定义（Macros）

<a id="r_gaff31756c1bf8ee755e65b1e0fb689bb7"></a>

```c
#define BT_GATT_ERR(_att_err)
```

相关声明：[BT_GATT_ERR](#gaff31756c1bf8ee755e65b1e0fb689bb7)。

构造属性读写回调（Attribute Read/Write Callbacks）的错误返回值。

<a id="r_ga86bddd8211e7466b0457173a0dd412f0"></a>

```c
#define BT_GATT_CHRC_BROADCAST 0x01
```

相关声明：[BT_GATT_CHRC_BROADCAST](#ga86bddd8211e7466b0457173a0dd412f0)。

特征属性（Characteristic Properties）位域值。

<a id="r_gaa243a11d6d8b3e3be815c0893e0220f3"></a>

```c
#define BT_GATT_CHRC_READ 0x02
```

相关声明：[BT_GATT_CHRC_READ](#gaa243a11d6d8b3e3be815c0893e0220f3)。

特征读取属性（Characteristic Read Property）。

<a id="r_ga9c029ca574eb3c5992685b279388ac85"></a>

```c
#define BT_GATT_CHRC_WRITE_WITHOUT_RESP 0x04
```

相关声明：[BT_GATT_CHRC_WRITE_WITHOUT_RESP](#ga9c029ca574eb3c5992685b279388ac85)。

特征无响应写入属性（Characteristic Write Without Response Property）。

<a id="r_gad482d8db34707e1f9da1d8e2ddd5507e"></a>

```c
#define BT_GATT_CHRC_WRITE 0x08
```

相关声明：[BT_GATT_CHRC_WRITE](#gad482d8db34707e1f9da1d8e2ddd5507e)。

特征有响应写入属性（Characteristic Write With Response Property）。

<a id="r_gab8cd9649bdfd125a26065a8ced762a98"></a>

```c
#define BT_GATT_CHRC_NOTIFY 0x10
```

相关声明：[BT_GATT_CHRC_NOTIFY](#gab8cd9649bdfd125a26065a8ced762a98)。

特征通知属性（Characteristic Notify Property）。

<a id="r_gaa9639b9d655ea41767584b638add1f2b"></a>

```c
#define BT_GATT_CHRC_INDICATE 0x20
```

相关声明：[BT_GATT_CHRC_INDICATE](#gaa9639b9d655ea41767584b638add1f2b)。

特征指示属性（Characteristic Indicate Property）。

<a id="r_gaab3a26a00f88a6eacd36f2841004204c"></a>

```c
#define BT_GATT_CHRC_AUTH 0x40 __DEPRECATED_MACRO
```

相关声明：[BT_GATT_CHRC_AUTH](#gaab3a26a00f88a6eacd36f2841004204c)。

特征认证签名写入属性（Characteristic Authenticated Signed Writes Property）。

<a id="r_gac84d73a0ad50bfd149ad83181315de1a"></a>

```c
#define BT_GATT_CHRC_EXT_PROP 0x80
```

相关声明：[BT_GATT_CHRC_EXT_PROP](#gac84d73a0ad50bfd149ad83181315de1a)。

特征扩展属性（Characteristic Extended Properties Property）。

<a id="r_gad1825f8deafc36d7e8f09c2835884fc6"></a>

```c
#define BT_GATT_CEP_RELIABLE_WRITE 0x0001
```

相关声明：[BT_GATT_CEP_RELIABLE_WRITE](#gad1825f8deafc36d7e8f09c2835884fc6)。

特征扩展属性（Characteristic Extended Properties）位域值。

<a id="r_ga64898ec8390c89c1fc5bdf0364220a43"></a>

```c
#define BT_GATT_CEP_WRITABLE_AUX 0x0002
```

相关声明：[BT_GATT_CEP_WRITABLE_AUX](#ga64898ec8390c89c1fc5bdf0364220a43)。

特征扩展属性：可写辅助项（Writable Auxiliaries）。

<a id="r_ga240a10df32aa7a256a103ceee7211f8d"></a>

```c
#define BT_GATT_CCC_NOTIFY 0x0001
```

相关声明：[BT_GATT_CCC_NOTIFY](#ga240a10df32aa7a256a103ceee7211f8d)。

客户端特征配置值（Client Characteristic Configuration Values）。

<a id="r_ga60ff2ddcc2e3148881a2f15745ba06e8"></a>

```c
#define BT_GATT_CCC_INDICATE 0x0002
```

相关声明：[BT_GATT_CCC_INDICATE](#ga60ff2ddcc2e3148881a2f15745ba06e8)。

客户端特征配置：指示（Client Characteristic Configuration Indication）。

<a id="r_ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a"></a>

```c
#define BT_GATT_SCC_BROADCAST 0x0001
```

相关声明：[BT_GATT_SCC_BROADCAST](#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)。

服务器特征配置值（Server Characteristic Configuration Values）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.4\_类型定义（Typedefs）

<a id="r_ga57e36bf94652531964fd4237c203fe7b"></a>

```c
typedef ssize_t(* bt_gatt_attr_read_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_func_t](#ga57e36bf94652531964fd4237c203fe7b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

属性读取回调（Attribute Read Callback）。

<a id="r_ga3fd8527a0f3e8f3699dc0d3b0339eba1"></a>

```c
typedef ssize_t(* bt_gatt_attr_write_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_write_func_t](#ga3fd8527a0f3e8f3699dc0d3b0339eba1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

属性值写入实现（Attribute Value Write Implementation）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.5\_枚举（Enumerations）

<a id="r_ga96e57500d2340a45badb23701cc43833"></a>

```c
enum bt_gatt_perm { BT_GATT_PERM_NONE = 0 , BT_GATT_PERM_READ = (1UL << (0)) , BT_GATT_PERM_WRITE = (1UL << (1)) , BT_GATT_PERM_READ_ENCRYPT = (1UL << (2)) , BT_GATT_PERM_WRITE_ENCRYPT = (1UL << (3)) , BT_GATT_PERM_READ_AUTHEN = (1UL << (4)) , BT_GATT_PERM_WRITE_AUTHEN = (1UL << (5)) , BT_GATT_PERM_PREPARE_WRITE = (1UL << (6)) , BT_GATT_PERM_READ_LESC = (1UL << (7)) , BT_GATT_PERM_WRITE_LESC = (1UL << (8)) }
```

相关声明：[bt_gatt_perm](#ga96e57500d2340a45badb23701cc43833)、[BT_GATT_PERM_NONE](#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)、[BT_GATT_PERM_READ](#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)、[BT_GATT_PERM_WRITE](#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)、[BT_GATT_PERM_READ_ENCRYPT](#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)、[BT_GATT_PERM_WRITE_ENCRYPT](#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)、[BT_GATT_PERM_READ_AUTHEN](#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)、[BT_GATT_PERM_WRITE_AUTHEN](#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)、[BT_GATT_PERM_PREPARE_WRITE](#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)、[BT_GATT_PERM_READ_LESC](#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)、[BT_GATT_PERM_WRITE_LESC](#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)。

GATT 属性权限位域值（Attribute Permission Bit Field Values）。

<a id="r_ga830d437c8d0757f53af1de6aa3031906"></a>

```c
enum bt_gatt_attr_write_flag { BT_GATT_WRITE_FLAG_PREPARE = (1UL << (0)) , BT_GATT_WRITE_FLAG_CMD = (1UL << (1)) , BT_GATT_WRITE_FLAG_EXECUTE = (1UL << (2)) }
```

相关声明：[bt_gatt_attr_write_flag](#ga830d437c8d0757f53af1de6aa3031906)、[BT_GATT_WRITE_FLAG_PREPARE](#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383)、[BT_GATT_WRITE_FLAG_CMD](#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78)、[BT_GATT_WRITE_FLAG_EXECUTE](#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b)。

GATT 属性写入标志（Attribute Write Flags）。

## 3.6\_详细说明（Detailed Documentation）

<a id="ga60ff2ddcc2e3148881a2f15745ba06e8"></a>

### `BT_GATT_CCC_INDICATE`

```c
#define BT_GATT_CCC_INDICATE 0x0002
```

```c
#include <zephyr/bluetooth/gatt.h>
```

客户端特征配置：指示（Client Characteristic Configuration Indication）。

设置时，特征值（Characteristic Value）变化须通过指示（Indication）报告。

<a id="ga240a10df32aa7a256a103ceee7211f8d"></a>

### `BT_GATT_CCC_NOTIFY`

```c
#define BT_GATT_CCC_NOTIFY 0x0001
```

```c
#include <zephyr/bluetooth/gatt.h>
```

客户端特征配置值（Client Characteristic Configuration Values）。

客户端特征配置通知（Client Characteristic Configuration Notification）。

设置时，特征值（Characteristic Value）变化须通过通知（Notification）报告。

<a id="gad1825f8deafc36d7e8f09c2835884fc6"></a>

### `BT_GATT_CEP_RELIABLE_WRITE`

```c
#define BT_GATT_CEP_RELIABLE_WRITE 0x0001
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征扩展属性（Characteristic Extended Properties）位域值。

特征扩展属性：可靠写入（Characteristic Extended Property: Reliable Write）。

在特征扩展属性描述符（Characteristic Extended Properties Descriptor）中设置此位时，特征支持《蓝牙核心规范》（Bluetooth Core Specification）定义的可靠写入（Reliable Writes）。

这与 BT_GATT_PERM_PREPARE_WRITE 无关；后者是 Zephyr 专有的属性权限（Attribute Permission），控制准备写入（Prepare Writes）是否请求授权回调。

<a id="ga64898ec8390c89c1fc5bdf0364220a43"></a>

### `BT_GATT_CEP_WRITABLE_AUX`

```c
#define BT_GATT_CEP_WRITABLE_AUX 0x0002
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征扩展属性：可写辅助项（Writable Auxiliaries）。

设置时，特征用户描述描述符（Characteristic User Description Descriptor）可写。

<a id="gaab3a26a00f88a6eacd36f2841004204c"></a>

### `BT_GATT_CHRC_AUTH`

```c
#define BT_GATT_CHRC_AUTH 0x40 __DEPRECATED_MACRO
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征认证签名写入属性（Characteristic Authenticated Signed Writes Property）。

设置时，允许对特征值执行签名写入（Signed Writes）。

**已弃用（Deprecated）**：已弃用（Deprecated）：此 API 已弃用。

<a id="ga86bddd8211e7466b0457173a0dd412f0"></a>

### `BT_GATT_CHRC_BROADCAST`

```c
#define BT_GATT_CHRC_BROADCAST 0x01
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征属性（Characteristic Properties）位域值。

特征广播属性（Characteristic Broadcast Property）。

设置时，允许使用服务器特征配置描述符（Server Characteristic Configuration Descriptor）广播特征值。

<a id="gac84d73a0ad50bfd149ad83181315de1a"></a>

### `BT_GATT_CHRC_EXT_PROP`

```c
#define BT_GATT_CHRC_EXT_PROP 0x80
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征扩展属性（Characteristic Extended Properties Property）。

设置时，特征扩展属性描述符（Characteristic Extended Properties Descriptor）中定义了额外的特征属性。

<a id="gaa9639b9d655ea41767584b638add1f2b"></a>

### `BT_GATT_CHRC_INDICATE`

```c
#define BT_GATT_CHRC_INDICATE 0x20
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征指示属性（Characteristic Indicate Property）。

设置时，允许带确认的特征值指示（Indications with Acknowledgment）。

<a id="gab8cd9649bdfd125a26065a8ced762a98"></a>

### `BT_GATT_CHRC_NOTIFY`

```c
#define BT_GATT_CHRC_NOTIFY 0x10
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征通知属性（Characteristic Notify Property）。

设置时，允许不带确认的特征值通知（Notifications without Acknowledgment）。

<a id="gaa243a11d6d8b3e3be815c0893e0220f3"></a>

### `BT_GATT_CHRC_READ`

```c
#define BT_GATT_CHRC_READ 0x02
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征读取属性（Characteristic Read Property）。

设置时，允许读取特征值（Characteristic Value）。

<a id="gad482d8db34707e1f9da1d8e2ddd5507e"></a>

### `BT_GATT_CHRC_WRITE`

```c
#define BT_GATT_CHRC_WRITE 0x08
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征有响应写入属性（Characteristic Write With Response Property）。

设置时，允许有响应地写入特征值（Write with Response）。

<a id="ga9c029ca574eb3c5992685b279388ac85"></a>

### `BT_GATT_CHRC_WRITE_WITHOUT_RESP`

```c
#define BT_GATT_CHRC_WRITE_WITHOUT_RESP 0x04
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征无响应写入属性（Characteristic Write Without Response Property）。

设置时，允许无响应地写入特征值（Write without Response）。

<a id="gaff31756c1bf8ee755e65b1e0fb689bb7"></a>

### `BT_GATT_ERR`

```c
#define BT_GATT_ERR ( _att_err)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
(-(_att_err))
```

构造属性读写回调（Attribute Read/Write Callbacks）的错误返回值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_att_err` | ATT 错误码（Error Code）。 |

**返回（Returns）**：返回：适用于属性回调（Attribute Callbacks）的错误码。

<a id="ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a"></a>

### `BT_GATT_SCC_BROADCAST`

```c
#define BT_GATT_SCC_BROADCAST 0x0001
```

```c
#include <zephyr/bluetooth/gatt.h>
```

服务器特征配置值（Server Characteristic Configuration Values）。

服务器特征配置广播（Server Characteristic Configuration Broadcast）。

设置时，服务器执行广播时须在广播数据（Advertising Data）中广播该特征值。

<a id="ga57e36bf94652531964fd4237c203fe7b"></a>

### `bt_gatt_attr_read_func_t`

```c
typedef ssize_t(* bt_gatt_attr_read_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

属性读取回调（Attribute Read Callback）。

这是 bt_gatt_attr.read() 方法的类型。

此函数可假定本次读取满足属性权限（Attribute Permissions），由调用者负责保证。

调用者可设置 conn，以模拟 GATT 客户端读取；本地读取（Local Reads）可将其保留为 NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求读取的连接（Connection）。本地读取时为 NULL。 |
| `attr` | 正在读取的属性（Attribute）。 |
| `buf` | 用于存放读取结果（Read Result）的缓冲区。 |
| `len` | 要读取的数据长度（Data Length）。 |
| `offset` | 开始读取的偏移量（Offset）。 |

**说明（Note）**：注意：GATT 服务器依靠此方法处理远端 GATT 客户端的读取操作，但此方法并非服务器专用。例如，可在本地 ATT 数据库中查找属性并调用此方法。GATT 服务器将此方法的返回值传回远端客户端。协议栈为远端操作调用此方法时，始终使用由协议栈选定的线程上下文（Thread Context），不会从中断服务例程（ISR）调用；实现不应阻塞。

**返回（Returns）**：返回：读取的字节数；发生错误时，返回携带特定 BT_ATT_ERR_* 错误码的 BT_GATT_ERR()。

<a id="ga3fd8527a0f3e8f3699dc0d3b0339eba1"></a>

### `bt_gatt_attr_write_func_t`

```c
typedef ssize_t(* bt_gatt_attr_write_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

属性值写入实现（Attribute Value Write Implementation）。

这是 bt_gatt_attr.write() 方法的类型。

此函数可假定本次写入满足属性权限（Attribute Permissions），由调用者负责保证。

调用者可设置 conn，以模拟 GATT 客户端写入；本地写入（Local Writes）可将其保留为 NULL。

如果 flags 包含 BT_GATT_WRITE_FLAG_PREPARE，则此方法不得执行写入，只能检查是否获准写入，未授权时返回错误码。

属性值写入实现（Attribute Value Write Implementation）除可能存储值以外，还可以且经常会产生其他副作用（Side Effects），例如切换 LED。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求写入的连接（Connection）。 |
| `attr` | 正在写入的属性（Attribute）。 |
| `buf` | 包含待写入数据的缓冲区（Buffer）。 |
| `len` | 缓冲区内的字节数（Number of Bytes）。 |
| `offset` | 开始写入的偏移量（Offset）。 |
| `flags` | bt_gatt_attr_write_flag 类型的标志（Flags）。 |

**说明（Note）**：注意：GATT 服务器依靠此方法处理远端 GATT 客户端的写入操作，但此方法并非服务器专用。例如，可在本地 ATT 数据库中查找属性并调用此方法。GATT 服务器将此方法的返回值传回远端客户端。协议栈为远端操作调用此方法时，始终使用由协议栈选定的线程上下文（Thread Context），不会从中断服务例程（ISR）调用；实现不应阻塞。

**返回（Returns）**：返回：写入的字节数；发生错误时，返回携带特定 BT_ATT_ERR_* 错误码的 BT_GATT_ERR()。

<a id="ga830d437c8d0757f53af1de6aa3031906"></a>

### `bt_gatt_attr_write_flag`

```c
enum bt_gatt_attr_write_flag
```

```c
#include <zephyr/bluetooth/gatt.h>
```

GATT 属性写入标志（Attribute Write Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GATT_WRITE_FLAG_PREPARE` | 属性准备写入标志（Attribute Prepare Write Flag）。设置时，写回调只能检查设备是否获授权，不得写入数据。仅对设置了 BT_GATT_PERM_PREPARE_WRITE 的属性传递此标志。未设置该权限不意味着拒绝准备写入，原因参见该权限说明。 |
| `BT_GATT_WRITE_FLAG_CMD` | 属性写命令标志（Attribute Write Command Flag）。设置时，表示写操作是命令（Command），即无响应写入（Write without Response），不产生响应。 |
| `BT_GATT_WRITE_FLAG_EXECUTE` | 属性执行写入标志（Attribute Write Execute Flag）。设置时，表示写操作是执行（Execute），标志着长写入（Long Write）结束；它出现在一个或多个 BT_GATT_WRITE_FLAG_PREPARE 之后。 |

<a id="ga96e57500d2340a45badb23701cc43833"></a>

### `bt_gatt_perm`

```c
enum bt_gatt_perm
```

```c
#include <zephyr/bluetooth/gatt.h>
```

GATT 属性权限位域值（Attribute Permission Bit Field Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GATT_PERM_NONE` | 不支持任何操作（No Operations Supported），例如仅用于通知（Notify-only）。 |
| `BT_GATT_PERM_READ` | 属性读取权限（Attribute Read Permission）。 |
| `BT_GATT_PERM_WRITE` | 属性写入权限（Attribute Write Permission）。 |
| `BT_GATT_PERM_READ_ENCRYPT` | 要求加密的属性读取权限（Attribute Read Permission with Encryption）。设置时，读取访问要求加密。 |
| `BT_GATT_PERM_WRITE_ENCRYPT` | 要求加密的属性写入权限（Attribute Write Permission with Encryption）。设置时，写入访问要求加密。 |
| `BT_GATT_PERM_READ_AUTHEN` | 要求认证的属性读取权限（Attribute Read Permission with Authentication）。设置时，读取访问要求使用经过认证的链路密钥（Authenticated Link-key）加密。 |
| `BT_GATT_PERM_WRITE_AUTHEN` | 要求认证的属性写入权限（Attribute Write Permission with Authentication）。设置时，写入访问要求使用经过认证的链路密钥（Authenticated Link-key）加密。 |
| `BT_GATT_PERM_PREPARE_WRITE` | 属性准备写入权限（Attribute Prepare Write Permission）。此权限是 Zephyr 扩展，并非《蓝牙核心规范》定义的内容。设置时，准备写入（用于长写入和可靠写入）会在值加入队列之前，以 BT_GATT_WRITE_FLAG_PREPARE 调用属性写回调。回调必须返回 0 才接受准备写入，其他返回值都转换为 ATT 错误。若未设置此权限，默认接受准备写入，但仍须满足常规写权限。注意：此值与枚举的其他值不同，它不是访问检查（Access Check）；清除此位不会使 GATT 层拒绝准备写入。客户端执行写入时，每个已入队的值都会传给写回调。因此，不能接受准备写入的属性必须在写回调中拒绝它：设置此权限时，在准备阶段拒绝；未设置时，在执行阶段拒绝。不要将其与 BT_GATT_CEP_RELIABLE_WRITE 混淆；后者是规范中的特征扩展属性位（Characteristic Extended Property Bit）。 |
| `BT_GATT_PERM_READ_LESC` | 要求低功耗安全连接加密的属性读取权限（Attribute Read Permission with LE Secure Connection Encryption）。设置时，读取访问要求使用 LE Secure Connections。 |
| `BT_GATT_PERM_WRITE_LESC` | 要求低功耗安全连接加密的属性写入权限（Attribute Write Permission with LE Secure Connection Encryption）。设置时，写入访问要求使用 LE Secure Connections。 |

**说明（Note）**：注意：此值与枚举的其他值不同，它不是访问检查（Access Check）；清除此位不会使 GATT 层拒绝准备写入。客户端执行写入时，每个已入队的值都会传给写回调。因此，不能接受准备写入的属性必须在写回调中拒绝它：设置此权限时，在准备阶段拒绝；未设置时，在执行阶段拒绝。


## 3.7\_原页交叉引用（Cross References）

- [GATT 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html)
- [GATT 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [bt_gatt_service_val](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)
- [bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)
- [bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)
- [bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)
- [bt_gatt_chrc](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)
- [bt_gatt_cep](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)
- [bt_gatt_ccc](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)
- [bt_gatt_scc](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)
- [bt_gatt_cpf](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/bluetooth/gatt.h](../api_file_bluetooth_media_reference/P004_zephyr__bluetooth__gatt.h_文件参考.md)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000001)
- [bt_gatt_attr.read()](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a074abc719494ca35997a452f526e7ecc)
- [bt_gatt_attr.write()](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a1ecd78536067f4bded506e0daccefd35)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383"></a>
<a id="gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78"></a>
<a id="gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b"></a>
<a id="gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a"></a>
<a id="gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17"></a>
<a id="gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf"></a>
<a id="gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d"></a>
<a id="gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f"></a>
<a id="gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583"></a>
<a id="gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266"></a>
<a id="gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79"></a>
<a id="gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57"></a>
<a id="gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94"></a>

---

[上一章](P002_定义与分配编号（Defines and Assigned Numbers）.md) · [返回大纲](大纲.md) · [下一章](P004_信道探测（Channel Sounding，CS）.md)
