---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-30
title: bt_mesh_cfg_cli_hb_sub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__hb__sub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_mesh\_cfg\_cli\_hb\_sub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__hb__sub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳订阅（Heartbeat Subscription）的配置参数。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

心跳订阅（Heartbeat Subscription）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a01ec0c3cab7bb7ed76d7728390eb4f25"></a>

```c
uint16_t src
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src](#a01ec0c3cab7bb7ed76d7728390eb4f25)。

要从中接收心跳消息（Heartbeat messages）的源地址（Source address）。

<a id="r_abc9ea18fbe86c260d6cf5d53c26a0248"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#abc9ea18fbe86c260d6cf5d53c26a0248)。

用于接收心跳消息（Heartbeat messages）的目的地址（Destination address）。

<a id="r_a5a75c924f0868c664652503335b1b012"></a>

```c
uint8_t period
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[period](#a5a75c924f0868c664652503335b1b012)。

以对数表示的持续监听订阅周期（Logarithmic subscription period）。

<a id="r_a93624ab6c8a0c15c0b50490e0fcd3675"></a>

```c
uint8_t count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[count](#a93624ab6c8a0c15c0b50490e0fcd3675)。

以对数表示的心跳订阅接收次数（Heartbeat subscription receive count）。

<a id="r_a480b214e0e1974a6a54426c49e5d62d1"></a>

```c
uint8_t min
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min](#a480b214e0e1974a6a54426c49e5d62d1)。

接收消息中的最小跳数（Minimum hops），即从发布节点到订阅节点记录到的最短路径。

<a id="r_aac96c2ab606e38f412e94539795c5594"></a>

```c
uint8_t max
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max](#aac96c2ab606e38f412e94539795c5594)。

接收消息中的最大跳数（Maximum hops），即从发布节点到订阅节点记录到的最长路径。

## 30.2\_详细说明（Detailed Documentation）

<a id="a93624ab6c8a0c15c0b50490e0fcd3675"></a>

### `count`

```c
uint8_t bt_mesh_cfg_cli_hb_sub::count
```

以对数表示的心跳订阅接收次数（Heartbeat subscription receive count）。

`count` 在 `1` 到 `0xfe` 之间时，解码后的心跳次数为 `(1 << (count - 1))`；`count` 为 `0` 时为 `0`；`count` 为 `0xff` 时为 `0xffff`。

设置心跳订阅（Heartbeat subscription set）时忽略此项。

<a id="abc9ea18fbe86c260d6cf5d53c26a0248"></a>

### `dst`

```c
uint16_t bt_mesh_cfg_cli_hb_sub::dst
```

用于接收心跳消息（Heartbeat messages）的目的地址（Destination address）。

<a id="aac96c2ab606e38f412e94539795c5594"></a>

### `max`

```c
uint8_t bt_mesh_cfg_cli_hb_sub::max
```

接收消息中的最大跳数（Maximum hops），即从发布节点到订阅节点记录到的最长路径。

从直接邻居（Immediate neighbor）收到的心跳，其跳数（Hop count）为 `1`。

设置心跳订阅（Heartbeat subscription set）时忽略此项。

<a id="a480b214e0e1974a6a54426c49e5d62d1"></a>

### `min`

```c
uint8_t bt_mesh_cfg_cli_hb_sub::min
```

接收消息中的最小跳数（Minimum hops），即从发布节点到订阅节点记录到的最短路径。

从直接邻居（Immediate neighbor）收到的心跳，其跳数（Hop count）为 `1`。

设置心跳订阅（Heartbeat subscription set）时忽略此项。

<a id="a5a75c924f0868c664652503335b1b012"></a>

### `period`

```c
uint8_t bt_mesh_cfg_cli_hb_sub::period
```

以对数表示的持续监听订阅周期（Logarithmic subscription period）。

解码后的订阅周期（Subscription period）为 `(1 << (period - 1))` 秒；`period` 为 `0` 时为 `0` 秒。

<a id="a01ec0c3cab7bb7ed76d7728390eb4f25"></a>

### `src`

```c
uint16_t bt_mesh_cfg_cli_hb_sub::src
```

要从中接收心跳消息（Heartbeat messages）的源地址（Source address）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_mesh_cfg_cli_hb_pub_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_mesh_cfg_cli_mod_pub_结构体.md)
