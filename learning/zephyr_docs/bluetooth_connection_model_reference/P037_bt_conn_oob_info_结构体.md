---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-37
title: bt_conn_oob_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_conn\_oob\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

带外（Out-of-Band，OOB）配对信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

带外（Out-of-Band，OOB）配对信息结构体。

<a id="header-pub-types"></a>
<a id="pub-types"></a>

## 37.1\_公开类型（Public Types）

<a id="r_aaec69b732a4bd8baf10c8b66bc73db89"></a>

```c
enum { BT_CONN_OOB_LE_LEGACY , BT_CONN_OOB_LE_SC }
```

相关声明：[BT_CONN_OOB_LE_LEGACY](#aaec69b732a4bd8baf10c8b66bc73db89a4c33ea839306256a198c29ea783c659b)、[BT_CONN_OOB_LE_SC](#aaec69b732a4bd8baf10c8b66bc73db89acd02773beb42df3fb6cbaa2fa2abda1e)。

带外配对方法类型（OOB pairing method type）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.2\_数据成员（Data Fields）

<a id="r_a2117d76f495304753bc028afc66fc6b0"></a>

```c
enum bt_conn_oob_info:: { ... } type
```

相关声明：[type](#a2117d76f495304753bc028afc66fc6b0)。

带外配对方法类型（OOB pairing method type）。

```c
union {
```

```c
struct {
```

<a id="r_ad70497b2a86e5fbd5a7ab40bbcbbde82"></a>

```c
enum { BT_CONN_OOB_LOCAL_ONLY , BT_CONN_OOB_REMOTE_ONLY , BT_CONN_OOB_BOTH_PEERS , BT_CONN_OOB_NO_DATA }
```

相关声明：[BT_CONN_OOB_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02861)、[BT_CONN_OOB_REMOTE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02864)、[BT_CONN_OOB_BOTH_PEERS](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02867)、[BT_CONN_OOB_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02870)。

带外数据配置（OOB data configuration）。

<a id="r_abd119a29389dcf4da3bb96db8f511b42"></a>

```c
enum bt_conn_oob_info:: { ... } oob_config
```

相关声明：[oob_config](#a9c71633c3fc8c0a16edde7e6f1a832db)。

带外数据配置（OOB data configuration）。

<a id="r_a024a27f7675610723985c5e93d55b92a"></a>

```c
} lesc
```

相关声明：[lesc](#a49c2473beac84e2ea21b1299352beee6)。

低功耗安全连接带外配对参数（LE Secure Connections OOB pairing parameters）。

<a id="r_a53d98a02ed3b5c23e8110d904a237345"></a>

```c
};
```

## 37.3\_详细说明（Detailed Documentation）

<a id="aaec69b732a4bd8baf10c8b66bc73db89"></a>

### `anonymous enum`

```c
anonymous enum
```

带外配对方法类型（OOB pairing method type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_OOB_LE_LEGACY` | 低功耗传统配对（LE legacy pairing）。 |
| `BT_CONN_OOB_LE_SC` | 低功耗安全连接配对（LE SC pairing）。 |

<a id="a53d98a02ed3b5c23e8110d904a237345"></a>

### `[union]`

```c
union { ... } bt_conn_oob_info
```

<a id="a49c2473beac84e2ea21b1299352beee6"></a>

### `[struct]`

```c
struct { ... } bt_conn_oob_info::lesc
```

低功耗安全连接带外配对参数（LE Secure Connections OOB pairing parameters）。

<a id="a9c71633c3fc8c0a16edde7e6f1a832db"></a>

### `[]`

```c
enum { ... } bt_conn_oob_info::oob_config
```

带外数据配置（OOB data configuration）。

<a id="a2117d76f495304753bc028afc66fc6b0"></a>

### `[]`

```c
enum { ... } bt_conn_oob_info::type
```

带外配对方法类型（OOB pairing method type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 37.4\_原页交叉引用（Cross References）

> 译注：原页四个带外配对枚举值的匿名类型链接返回404；以下入口改为已核对的官方头文件源码声明位置，枚举名称保持原样。

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [BT_CONN_OOB_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02861)
- [BT_CONN_OOB_REMOTE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02864)
- [BT_CONN_OOB_BOTH_PEERS](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02867)
- [BT_CONN_OOB_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02870)
- [bt_conn_oob_info](P037_bt_conn_oob_info_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aaec69b732a4bd8baf10c8b66bc73db89a4c33ea839306256a198c29ea783c659b"></a>
<a id="aaec69b732a4bd8baf10c8b66bc73db89acd02773beb42df3fb6cbaa2fa2abda1e"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_conn_le_tx_power_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_conn_pairing_feat_结构体.md)
