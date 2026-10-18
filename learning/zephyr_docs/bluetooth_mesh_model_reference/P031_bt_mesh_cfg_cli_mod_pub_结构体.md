---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-31
title: bt_mesh_cfg_cli_mod_pub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__mod__pub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_mesh\_cfg\_cli\_mod\_pub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__mod__pub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模型发布（Model Publication）的配置参数。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

模型发布（Model Publication）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_ab52dd35df271ae5bd70a4640e6f3bea8"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#ab52dd35df271ae5bd70a4640e6f3bea8)。

发布目的地址（Publication destination address）。

<a id="r_a29cbd50ad33f25ad3b98b4ec7ac56a6c"></a>

```c
const uint8_t * uuid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#a29cbd50ad33f25ad3b98b4ec7ac56a6c)。

虚拟地址通用唯一标识符（Virtual address UUID）；若不是虚拟地址，则为 `NULL`。

<a id="r_aefbe5449a10379b064dea054300cb9a0"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#aefbe5449a10379b064dea054300cb9a0)。

发布时使用的应用索引（Application index）。

<a id="r_aa7452f697410fdf8a63808bcb29c53ee"></a>

```c
bool cred_flag
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cred_flag](#aa7452f697410fdf8a63808bcb29c53ee)。

友谊关系凭据标志（Friendship credential flag）。

<a id="r_a9513db038ec4f51734892bd1ce7d08f3"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a9513db038ec4f51734892bd1ce7d08f3)。

发布时使用的生存时间（Time To Live，TTL）。

<a id="r_a104afe2b8d9766e037293b09c0c1b91c"></a>

```c
uint8_t period
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[period](#a104afe2b8d9766e037293b09c0c1b91c)。

编码后的发布周期（Encoded publish period）。

<a id="r_a2a5a0ead8155bf971c84f73dfa4ec282"></a>

```c
uint8_t transmit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit](#a2a5a0ead8155bf971c84f73dfa4ec282)。

编码后的传输参数（Encoded transmit parameters）。

## 31.2\_详细说明（Detailed Documentation）

<a id="ab52dd35df271ae5bd70a4640e6f3bea8"></a>

### `addr`

```c
uint16_t bt_mesh_cfg_cli_mod_pub::addr
```

发布目的地址（Publication destination address）。

<a id="aefbe5449a10379b064dea054300cb9a0"></a>

### `app_idx`

```c
uint16_t bt_mesh_cfg_cli_mod_pub::app_idx
```

发布时使用的应用索引（Application index）。

<a id="aa7452f697410fdf8a63808bcb29c53ee"></a>

### `cred_flag`

```c
bool bt_mesh_cfg_cli_mod_pub::cred_flag
```

友谊关系凭据标志（Friendship credential flag）。

<a id="a104afe2b8d9766e037293b09c0c1b91c"></a>

### `period`

```c
uint8_t bt_mesh_cfg_cli_mod_pub::period
```

编码后的发布周期（Encoded publish period）。

**参阅（See Also）**：另见（See also）：`BT_MESH_PUB_PERIOD_100MS`、`BT_MESH_PUB_PERIOD_SEC`、`BT_MESH_PUB_PERIOD_10SEC`、`BT_MESH_PUB_PERIOD_10MIN`。

<a id="a2a5a0ead8155bf971c84f73dfa4ec282"></a>

### `transmit`

```c
uint8_t bt_mesh_cfg_cli_mod_pub::transmit
```

编码后的传输参数（Encoded transmit parameters）。

**参阅（See Also）**：另见（See also）：`BT_MESH_TRANSMIT`。

<a id="a9513db038ec4f51734892bd1ce7d08f3"></a>

### `ttl`

```c
uint8_t bt_mesh_cfg_cli_mod_pub::ttl
```

发布时使用的生存时间（Time To Live，TTL）。

<a id="a29cbd50ad33f25ad3b98b4ec7ac56a6c"></a>

### `uuid`

```c
const uint8_t* bt_mesh_cfg_cli_mod_pub::uuid
```

虚拟地址通用唯一标识符（Virtual address UUID）；若不是虚拟地址，则为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_MESH_PUB_PERIOD_100MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab542c707fb5bad0a15088fefda775a42)
- [BT_MESH_PUB_PERIOD_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga29435e527a73ff6e19339b773c8eb79e)
- [BT_MESH_PUB_PERIOD_10SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga654204077adaa08259d1afbfe92e070e)
- [BT_MESH_PUB_PERIOD_10MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36c37f644ee39ad91b6167f68c806b7e)
- [BT_MESH_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff82bf652232fbce71c31f38a10577a9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_mesh_cfg_cli_hb_sub_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_mesh_comp_结构体.md)
