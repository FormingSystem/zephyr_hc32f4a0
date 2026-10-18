---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-34
title: bt_cap_handover_unicast_to_broadcast_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__unicast__to__broadcast__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_cap\_handover\_unicast\_to\_broadcast\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__unicast__to__broadcast__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_handover_unicast_to_broadcast()` 的参数（Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_handover_unicast_to_broadcast()` 的参数（Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a079b91898031113b6126465307bed6d0"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a079b91898031113b6126465307bed6d0)。

集合类型（Set type）。

<a id="r_abf15dec430b51c9c5e83ea4cb56b7845"></a>

```c
struct bt_cap_unicast_group * unicast_group
```

相关声明：[bt_cap_unicast_group](P045_bt_cap_unicast_group_结构体.md)、[unicast_group](#abf15dec430b51c9c5e83ea4cb56b7845)。

包含这些流的源单播组（Source unicast group）。

<a id="r_a399a28aa6eb43f892ae0810c5e90d6e6"></a>

```c
struct bt_le_ext_adv * ext_adv
```

相关声明：[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[ext_adv](#a399a28aa6eb43f892ae0810c5e90d6e6)。

广播源使用的广播集（Advertising set）。

<a id="r_a0d8ccf04a751e775581c07e89b956b6c"></a>

```c
uint16_t pa_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pa_interval](#a0d8ccf04a751e775581c07e89b956b6c)。

为广播集配置的周期广播间隔（Periodic advertising interval）。

<a id="r_acb23afa394cd883b444ece27b1784adf"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#acb23afa394cd883b444ece27b1784adf)。

广播集当前使用或将要使用的广播标识符（Broadcast ID）。

<a id="r_a58442e418a8fb01d67560aa68bfbd2cc"></a>

```c
struct bt_cap_initiator_broadcast_create_param * broadcast_create_param
```

相关声明：[bt_cap_initiator_broadcast_create_param](P035_bt_cap_initiator_broadcast_create_param_结构体.md)、[broadcast_create_param](#a58442e418a8fb01d67560aa68bfbd2cc)。

广播源参数（Broadcast source parameters）。

## 34.2\_详细说明（Detailed Documentation）

<a id="a58442e418a8fb01d67560aa68bfbd2cc"></a>

### `broadcast_create_param`

```c
struct bt_cap_initiator_broadcast_create_param* bt_cap_handover_unicast_to_broadcast_param::broadcast_create_param
```

广播源参数（Broadcast source parameters）。

这些参数必须一直保持有效，直到过程（Procedure）完成。

<a id="acb23afa394cd883b444ece27b1784adf"></a>

### `broadcast_id`

```c
uint32_t bt_cap_handover_unicast_to_broadcast_param::broadcast_id
```

广播集当前使用或将要使用的广播标识符（Broadcast ID）。

<a id="a399a28aa6eb43f892ae0810c5e90d6e6"></a>

### `ext_adv`

```c
struct bt_le_ext_adv* bt_cap_handover_unicast_to_broadcast_param::ext_adv
```

广播源使用的广播集（Advertising set）。

此项必须一直保持有效，直到过程（Procedure）完成。如果调用 `bt_cap_handover_unicast_to_broadcast()` 时广播集尚未启动，该过程会使用 `BT_LE_EXT_ADV_START_DEFAULT` 启动广播集。

<a id="a0d8ccf04a751e775581c07e89b956b6c"></a>

### `pa_interval`

```c
uint16_t bt_cap_handover_unicast_to_broadcast_param::pa_interval
```

为广播集配置的周期广播间隔（Periodic advertising interval）。

<a id="a079b91898031113b6126465307bed6d0"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_handover_unicast_to_broadcast_param::type
```

集合类型（Set type）。

<a id="abf15dec430b51c9c5e83ea4cb56b7845"></a>

### `unicast_group`

```c
struct bt_cap_unicast_group* bt_cap_handover_unicast_to_broadcast_param::unicast_group
```

包含这些流的源单播组（Source unicast group）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 34.3\_原页交叉引用（Cross References）

- [bt_cap_handover_unicast_to_broadcast()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_unicast_group](P045_bt_cap_unicast_group_结构体.md)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_cap_initiator_broadcast_create_param](P035_bt_cap_initiator_broadcast_create_param_结构体.md)
- [BT_LE_EXT_ADV_START_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8c83a6f322a479bc24a576a7f091312e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_cap_handover_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_cap_initiator_broadcast_create_param_结构体.md)
