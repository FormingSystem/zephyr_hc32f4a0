---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-29
title: bt_mesh_cfg_cli_hb_pub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__hb__pub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_bt\_mesh\_cfg\_cli\_hb\_pub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__hb__pub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳发布（Heartbeat Publication）的配置参数。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

心跳发布（Heartbeat Publication）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a473df7dd958683d7502dcc983c4ceb8a"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#a473df7dd958683d7502dcc983c4ceb8a)。

心跳目的地址（Heartbeat destination address）。

<a id="r_a13c7c155f30ca94d30090a25df50e4b2"></a>

```c
uint8_t count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[count](#a13c7c155f30ca94d30090a25df50e4b2)。

以对数表示的心跳次数（Logarithmic Heartbeat count）。

<a id="r_a8d17dd2df4be23cadad4b5746ddb50ad"></a>

```c
uint8_t period
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[period](#a8d17dd2df4be23cadad4b5746ddb50ad)。

以对数表示的心跳发布发送间隔（Heartbeat publication transmit interval），单位为秒。

<a id="r_ac7f24f7bf942587ef83ca47d9ee4e7fb"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#ac7f24f7bf942587ef83ca47d9ee4e7fb)。

发布消息的生存时间值（Time To Live，TTL）。

<a id="r_a94598c9b733075abe22d70f62293b5a1"></a>

```c
uint16_t feat
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feat](#a94598c9b733075abe22d70f62293b5a1)。

触发心跳发布（Heartbeat publications）的特性位图（Feature bitmap）。

<a id="r_a90a79d8b7ea91c6ba872dca15d87b356"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#a90a79d8b7ea91c6ba872dca15d87b356)。

发布时使用的网络索引（Network index）。

## 29.2\_详细说明（Detailed Documentation）

<a id="a13c7c155f30ca94d30090a25df50e4b2"></a>

### `count`

```c
uint8_t bt_mesh_cfg_cli_hb_pub::count
```

以对数表示的心跳次数（Logarithmic Heartbeat count）。

`count` 在 `1` 到 `0x11` 之间时，解码为 `(1 << (count - 1))`；`count` 为 `0` 时解码为 `0`；`count` 为 `0xff` 时表示无限次（Indefinitely）。

用于设置心跳发布（Heartbeat publication set）时，此参数表示要发送的心跳消息数量。

由获取心跳发布（Heartbeat publication get）操作返回时，此参数表示尚待发送的心跳消息数量。

<a id="a473df7dd958683d7502dcc983c4ceb8a"></a>

### `dst`

```c
uint16_t bt_mesh_cfg_cli_hb_pub::dst
```

心跳目的地址（Heartbeat destination address）。

<a id="a94598c9b733075abe22d70f62293b5a1"></a>

### `feat`

```c
uint16_t bt_mesh_cfg_cli_hb_pub::feat
```

触发心跳发布（Heartbeat publications）的特性位图（Feature bitmap）。

合法值为 `BT_MESH_FEAT_RELAY`、`BT_MESH_FEAT_PROXY`、`BT_MESH_FEAT_FRIEND` 和 `BT_MESH_FEAT_LOW_POWER`。

<a id="a90a79d8b7ea91c6ba872dca15d87b356"></a>

### `net_idx`

```c
uint16_t bt_mesh_cfg_cli_hb_pub::net_idx
```

发布时使用的网络索引（Network index）。

<a id="a8d17dd2df4be23cadad4b5746ddb50ad"></a>

### `period`

```c
uint8_t bt_mesh_cfg_cli_hb_pub::period
```

以对数表示的心跳发布发送间隔（Heartbeat publication transmit interval），单位为秒。

`period` 在 `1` 到 `0x11` 之间时，解码为 `(1 << (period - 1))`。`period` 为 `0` 时，禁用心跳发布（Heartbeat publication）。

<a id="ac7f24f7bf942587ef83ca47d9ee4e7fb"></a>

### `ttl`

```c
uint8_t bt_mesh_cfg_cli_hb_pub::ttl
```

发布消息的生存时间值（Time To Live，TTL）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_MESH_FEAT_RELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gac588eefe83db94784a420ce063f02b55)
- [BT_MESH_FEAT_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaee648ce202316c56d4d588cb0ad5aeb4)
- [BT_MESH_FEAT_FRIEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga8f27086b3bc3c4a6e14621836f9f8e80)
- [BT_MESH_FEAT_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaad71a36c82b4e4d3fa334ecff5cc0171)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_bt_mesh_cfg_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_bt_mesh_cfg_cli_hb_sub_结构体.md)
