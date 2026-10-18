---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-17
title: bt_mesh_brg_cfg_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_bt\_mesh\_brg\_cfg\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh桥接配置客户端（Bridge Configuration Client）状态消息的回调。

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

<a id="details"></a>

Mesh桥接配置客户端（Bridge Configuration Client）状态消息的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_ac045febf91cc95982985e6de094e403b"></a>

```c
void(* bridge_status )(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, enum bt_mesh_brg_cfg_state status)
```

相关声明：[bridge_status](#ac045febf91cc95982985e6de094e403b)、[bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7bddcbe2b1196df6a1c80d8c213866f9)。

子网桥接状态消息（Subnet Bridge Status）的可选回调。

<a id="r_afe8e0a5ed681630e826ff0aa3889cd88"></a>

```c
void(* table_size_status )(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, uint16_t size)
```

相关声明：[table_size_status](#afe8e0a5ed681630e826ff0aa3889cd88)、[bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

桥接表大小状态消息（Bridging Table Size Status）的可选回调。

<a id="r_a608b74d78f2f4bb06130f40071ac93af"></a>

```c
void(* table_status )(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_table_status *rsp)
```

相关声明：[table_status](#a608b74d78f2f4bb06130f40071ac93af)、[bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_status](P022_bt_mesh_brg_cfg_table_status_结构体.md)。

桥接表状态消息（Bridging Table Status）的可选回调。

<a id="r_a947e2169ed2cb0964c082bd82c1b0943"></a>

```c
void(* subnets_list )(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_subnets_list *rsp)
```

相关声明：[subnets_list](#a947e2169ed2cb0964c082bd82c1b0943)、[bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_subnets_list](P019_bt_mesh_brg_cfg_subnets_list_结构体.md)。

已桥接子网列表消息（Bridged Subnets List）的可选回调。

<a id="r_a3817e30dd90b161a7442604207ed0ba8"></a>

```c
void(* table_list )(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_table_list *rsp)
```

相关声明：[table_list](#a3817e30dd90b161a7442604207ed0ba8)、[bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_list](P021_bt_mesh_brg_cfg_table_list_结构体.md)。

桥接表列表消息（Bridging Table List）的可选回调。

## 17.2\_详细说明（Detailed Documentation）

<a id="ac045febf91cc95982985e6de094e403b"></a>

### `bridge_status`

```c
void(* bt_mesh_brg_cfg_cli_cb::bridge_status) (struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, enum bt_mesh_brg_cfg_state status)
```

子网桥接状态消息（Subnet Bridge Status）的可选回调。

处理来自桥接配置服务器（Bridge Configuration Server）的子网桥接状态消息（Subnet Bridge Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 桥接配置客户端上下文（Bridge Configuration Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 从服务器接收的状态（Status）。 |

<a id="a947e2169ed2cb0964c082bd82c1b0943"></a>

### `subnets_list`

```c
void(* bt_mesh_brg_cfg_cli_cb::subnets_list) (struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_subnets_list *rsp)
```

已桥接子网列表消息（Bridged Subnets List）的可选回调。

处理来自桥接配置服务器（Bridge Configuration Server）的已桥接子网列表消息（Bridged Subnets List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 桥接配置客户端上下文（Bridge Configuration Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `rsp` | 从桥接配置服务器（Bridging Configuration Server）接收到的响应（Response）。 |

<a id="a3817e30dd90b161a7442604207ed0ba8"></a>

### `table_list`

```c
void(* bt_mesh_brg_cfg_cli_cb::table_list) (struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_table_list *rsp)
```

桥接表列表消息（Bridging Table List）的可选回调。

处理来自桥接配置服务器（Bridge Configuration Server）的桥接表列表消息（Bridging Table List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 桥接配置客户端上下文（Bridge Configuration Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `rsp` | 从桥接配置服务器（Bridging Configuration Server）接收到的响应（Response）。 |

<a id="afe8e0a5ed681630e826ff0aa3889cd88"></a>

### `table_size_status`

```c
void(* bt_mesh_brg_cfg_cli_cb::table_size_status) (struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, uint16_t size)
```

桥接表大小状态消息（Bridging Table Size Status）的可选回调。

处理来自桥接配置服务器（Bridge Configuration Server）的桥接表大小状态消息（Bridging Table Size Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 桥接配置客户端上下文（Bridge Configuration Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `size` | 从服务器接收的大小（Size）。 |

<a id="a608b74d78f2f4bb06130f40071ac93af"></a>

### `table_status`

```c
void(* bt_mesh_brg_cfg_cli_cb::table_status) (struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, struct bt_mesh_brg_cfg_table_status *rsp)
```

桥接表状态消息（Bridging Table Status）的可选回调。

处理来自桥接配置服务器（Bridge Configuration Server）的桥接表状态消息（Bridging Table Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 桥接配置客户端上下文（Bridge Configuration Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `rsp` | 从桥接配置服务器（Bridging Configuration Server）接收到的响应（Response）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg_cli.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h_source.html)
- [bt_mesh_brg_cfg_cli](P016_bt_mesh_brg_cfg_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_brg_cfg_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [bt_mesh_brg_cfg_table_status](P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [bt_mesh_brg_cfg_subnets_list](P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [bt_mesh_brg_cfg_table_list](P021_bt_mesh_brg_cfg_table_list_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_bt_mesh_brg_cfg_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
