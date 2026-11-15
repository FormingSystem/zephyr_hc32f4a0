---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-1
title: zephyr__bluetooth__mesh__access.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_mesh\_\_access.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接入层（Access Layer）的API。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
#include <zephyr/settings/settings.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/mesh/msg.h>
```

查看此文件的源码。

接入层（Access Layer）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Felem"></a>

```c
struct bt_mesh_elem
```

相关声明：[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)。

描述Mesh元素（Mesh Element）的抽象。

<a id="r_bt_5Fmesh_5Felem_3A_3Abt_5Fmesh_5Felem_5Frt_5Fctx"></a>

```c
struct bt_mesh_elem::bt_mesh_elem_rt_ctx
```

相关声明：[bt_mesh_elem::bt_mesh_elem_rt_ctx](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)。

Mesh元素（Mesh Element）的运行时信息。

<a id="r_bt_5Fmesh_5Fmodel_5Fop"></a>

```c
struct bt_mesh_model_op
```

相关声明：[bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)。

模型操作码（Model Opcode）的处理程序。

<a id="r_bt_5Fmesh_5Fmodel_5Fpub"></a>

```c
struct bt_mesh_model_pub
```

相关声明：[bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)。

模型发布（Model Publication）的上下文。

<a id="r_bt_5Fmesh_5Fmodels_5Fmetadata_5Fentry"></a>

```c
struct bt_mesh_models_metadata_entry
```

相关声明：[bt_mesh_models_metadata_entry](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md)。

模型元数据条目（Models Metadata Entry）的结构。

<a id="r_bt_5Fmesh_5Fmodel_5Fcb"></a>

```c
struct bt_mesh_model_cb
```

相关声明：[bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)。

模型（Model）的回调函数。

<a id="r_bt_5Fmesh_5Fmod_5Fid_5Fvnd"></a>

```c
struct bt_mesh_mod_id_vnd
```

相关声明：[bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)。

厂商模型标识（Vendor Model ID）。

<a id="r_bt_5Fmesh_5Fmodel"></a>

```c
struct bt_mesh_model
```

相关声明：[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

描述Mesh模型（Mesh Model）实例的抽象。

<a id="r_bt_5Fmesh_5Fmodel_3A_3Abt_5Fmesh_5Fmodel_5Frt_5Fctx"></a>

```c
struct bt_mesh_model::bt_mesh_model_rt_ctx
```

相关声明：[bt_mesh_model::bt_mesh_model_rt_ctx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)。

<a id="r_bt_5Fmesh_5Fsend_5Fcb"></a>

```c
struct bt_mesh_send_cb
```

相关声明：[bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)。

监测模型消息发送的回调结构（Callback Structure）。

<a id="r_bt_5Fmesh_5Fcomp"></a>

```c
struct bt_mesh_comp
```

相关声明：[bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)。

节点组成（Node Composition）。

<a id="r_bt_5Fmesh_5Fcomp2_5Frecord"></a>

```c
struct bt_mesh_comp2_record
```

相关声明：[bt_mesh_comp2_record](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md)。

组成数据（Composition Data）的第2页记录。

<a id="r_bt_5Fmesh_5Fcomp2"></a>

```c
struct bt_mesh_comp2
```

相关声明：[bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)。

节点组成数据（Composition Data）的第2页。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ad28c5301ea6cf93f3bf2a672043cae4e"></a>

```c
#define BT_MESH_MODEL_RUNTIME_INIT(_user_data)
```

相关声明：[BT_MESH_MODEL_RUNTIME_INIT](#ad28c5301ea6cf93f3bf2a672043cae4e)。

<a id="r_ga1a4694cccf834d71f0abe2a0283cb9a8"></a>

```c
#define BT_MESH_ADDR_IS_UNICAST(addr)
```

相关声明：[BT_MESH_ADDR_IS_UNICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1a4694cccf834d71f0abe2a0283cb9a8)。

检查蓝牙 Mesh 地址是否为单播地址（Unicast Address）。

<a id="r_gab50cc8dca6f7ffd5420ef4fb38fbe224"></a>

```c
#define BT_MESH_ADDR_IS_GROUP(addr)
```

相关声明：[BT_MESH_ADDR_IS_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gab50cc8dca6f7ffd5420ef4fb38fbe224)。

检查蓝牙 Mesh 地址是否为组地址（Group Address）。

<a id="r_gaff5ff58937924a1e6297aa1b20efc30f"></a>

```c
#define BT_MESH_ADDR_IS_FIXED_GROUP(addr)
```

相关声明：[BT_MESH_ADDR_IS_FIXED_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff5ff58937924a1e6297aa1b20efc30f)。

检查蓝牙 Mesh 地址是否为固定组地址（Fixed Group Address）。

<a id="r_ga623eb2da2c880eec2107f36402ba6621"></a>

```c
#define BT_MESH_ADDR_IS_VIRTUAL(addr)
```

相关声明：[BT_MESH_ADDR_IS_VIRTUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga623eb2da2c880eec2107f36402ba6621)。

检查蓝牙 Mesh 地址是否为虚拟地址（Virtual Address）。

<a id="r_ga98ba7663259ca43cd5a38c7a9e16516d"></a>

```c
#define BT_MESH_ADDR_IS_RFU(addr)
```

相关声明：[BT_MESH_ADDR_IS_RFU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga98ba7663259ca43cd5a38c7a9e16516d)。

检查蓝牙 Mesh 地址是否为保留供未来使用的地址（Reserved for Future Use，RFU）。

<a id="r_gac4aafa0bdd24fb51d515a62e83917936"></a>

```c
#define BT_MESH_IS_DEV_KEY(key)
```

相关声明：[BT_MESH_IS_DEV_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac4aafa0bdd24fb51d515a62e83917936)。

检查蓝牙 Mesh 密钥是否为设备密钥（Device Key）。

<a id="r_gaa620c32d1dce8e4b691b7f4270016506"></a>

```c
#define BT_MESH_APP_SEG_SDU_MAX 12
```

相关声明：[BT_MESH_APP_SEG_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa620c32d1dce8e4b691b7f4270016506)。

访问消息分段（Access Message Segment）的最大大小，单位为八位组（Octets）。

<a id="r_ga64eb6a94b1db9899c4f5bbf4cc88cd9f"></a>

```c
#define BT_MESH_APP_UNSEG_SDU_MAX 15
```

相关声明：[BT_MESH_APP_UNSEG_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)。

未分段访问消息（Unsegmented Access Message）的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga18756e939ec3b312eef5c3dc9fd70270"></a>

```c
#define BT_MESH_RX_SEG_MAX 0
```

相关声明：[BT_MESH_RX_SEG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga18756e939ec3b312eef5c3dc9fd70270)。

接收消息所支持的最大分段数量（Number of Segments）。

<a id="r_ga1b2a3610ac370266578abce195e65fa2"></a>

```c
#define BT_MESH_TX_SEG_MAX 0
```

相关声明：[BT_MESH_TX_SEG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b2a3610ac370266578abce195e65fa2)。

发送消息所支持的最大分段数量（Number of Segments）。

<a id="r_ga86d7386603ecd89952b6d540ea4243c2"></a>

```c
#define BT_MESH_TX_SDU_MAX
```

相关声明：[BT_MESH_TX_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga86d7386603ecd89952b6d540ea4243c2)。

发送访问消息（Outgoing Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga36f299f2fc13892b5a7d871dad1ec9ce"></a>

```c
#define BT_MESH_RX_SDU_MAX
```

相关声明：[BT_MESH_RX_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga36f299f2fc13892b5a7d871dad1ec9ce)。

接收访问消息（Incoming Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga321a5091dabd4ec4beb5396db6cabf44"></a>

```c
#define BT_MESH_ELEM(_loc, _mods, _vnd_mods)
```

相关声明：[BT_MESH_ELEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga321a5091dabd4ec4beb5396db6cabf44)。

用于在数组中定义 Mesh 元素（Element）的辅助宏。

<a id="r_ga00915cfdff7dc0646f24d6b06e124d0d"></a>

```c
#define BT_MESH_MODEL_OP_1(b0)
```

相关声明：[BT_MESH_MODEL_OP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga00915cfdff7dc0646f24d6b06e124d0d)。

编码 1 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="r_gaa52a40ef5972c4f34cf5ff5a10e21289"></a>

```c
#define BT_MESH_MODEL_OP_2(b0, b1)
```

相关声明：[BT_MESH_MODEL_OP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa52a40ef5972c4f34cf5ff5a10e21289)。

编码 2 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="r_ga72d1d19701be52f5eac6af475f9b19a9"></a>

```c
#define BT_MESH_MODEL_OP_3(b0, cid)
```

相关声明：[BT_MESH_MODEL_OP_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga72d1d19701be52f5eac6af475f9b19a9)。

编码 3 字节操作码（Opcode）的宏，用于厂商特定消息（Vendor-Specific Message）。

<a id="r_ga637e1be0298dc681414645867b28b59f"></a>

```c
#define BT_MESH_LEN_EXACT(len)
```

相关声明：[BT_MESH_LEN_EXACT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga637e1be0298dc681414645867b28b59f)。

为定长消息编码确切消息长度（Exact Message Length）的宏。

<a id="r_ga691ed9b3ab3ddaceda0f81c4a715ab3a"></a>

```c
#define BT_MESH_LEN_MIN(len)
```

相关声明：[BT_MESH_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga691ed9b3ab3ddaceda0f81c4a715ab3a)。

为变长消息编码最小消息长度（Minimum Message Length）的宏。

<a id="r_gaf2c164506c601214c85d451747176827"></a>

```c
#define BT_MESH_MODEL_OP_END { 0, 0, NULL }
```

相关声明：[BT_MESH_MODEL_OP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf2c164506c601214c85d451747176827)。

操作码列表（Opcode List）的结束项。

<a id="r_gae6d55e0a27bb7c448affd312a2e11656"></a>

```c
#define BT_MESH_MODEL_NO_OPS
```

相关声明：[BT_MESH_MODEL_NO_OPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gae6d55e0a27bb7c448affd312a2e11656)。

用于定义空操作码列表（Empty Opcode List）的辅助宏。

<a id="r_gab0ad2aab95d49e5b60fe8dafd69132a4"></a>

```c
#define BT_MESH_MODEL_NONE ((const struct bt_mesh_model []){})
```

相关声明：[BT_MESH_MODEL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gab0ad2aab95d49e5b60fe8dafd69132a4)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

用于定义空模型数组（Empty Model Array）的辅助宏。

<a id="r_ga925da443eb15a4c1980d48a69388dc2c"></a>

```c
#define BT_MESH_MODEL_CNT_CB(_id, _op, _pub, _user_data, _keys, _grps, _cb)
```

相关声明：[BT_MESH_MODEL_CNT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga925da443eb15a4c1980d48a69388dc2c)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数，且指定密钥和组的数量。

<a id="r_ga32733dccd9329aa938dc0bd21cf9beae"></a>

```c
#define BT_MESH_MODEL_CNT_VND_CB(_company, _id, _op, _pub, _user_data, _keys, _grps, _cb)
```

相关声明：[BT_MESH_MODEL_CNT_VND_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga32733dccd9329aa938dc0bd21cf9beae)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数，且指定密钥和组的数量。

<a id="r_gac062c101b7310020e11a527de9c40d3a"></a>

```c
#define BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, _cb)
```

相关声明：[BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数。

<a id="r_ga40204b4ccaa819a487de168bcf66c98f"></a>

```c
#define BT_MESH_MODEL_METADATA_CB(_id, _op, _pub, _user_data, _cb, _metadata)
```

相关声明：[BT_MESH_MODEL_METADATA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga40204b4ccaa819a487de168bcf66c98f)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数和元数据（Metadata）。

<a id="r_gabe79d914990ba2721f5bb7081910e512"></a>

```c
#define BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, _cb)
```

相关声明：[BT_MESH_MODEL_VND_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabe79d914990ba2721f5bb7081910e512)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数。

<a id="r_gac62334962dcbe3a75a03ce5744b326d8"></a>

```c
#define BT_MESH_MODEL_VND_METADATA_CB(_company, _id, _op, _pub, _user_data, _cb, _metadata)
```

相关声明：[BT_MESH_MODEL_VND_METADATA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac62334962dcbe3a75a03ce5744b326d8)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数和元数据（Metadata）。

<a id="r_gae694f5ac7ef9f0de37aaba846443586f"></a>

```c
#define BT_MESH_MODEL(_id, _op, _pub, _user_data)
```

相关声明：[BT_MESH_MODEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gae694f5ac7ef9f0de37aaba846443586f)。

组成数据（Composition Data）中的 SIG 模型条目。

<a id="r_ga3759c8c88db48be662bf2511ff514edd"></a>

```c
#define BT_MESH_MODEL_VND(_company, _id, _op, _pub, _user_data)
```

相关声明：[BT_MESH_MODEL_VND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga3759c8c88db48be662bf2511ff514edd)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目。

<a id="r_gaff82bf652232fbce71c31f38a10577a9"></a>

```c
#define BT_MESH_TRANSMIT(count, int_ms)
```

相关声明：[BT_MESH_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff82bf652232fbce71c31f38a10577a9)。

编码发送次数（Transmission Count）和间隔步数（Interval Steps）。

<a id="r_ga62fda0d731241efbaa4827e4eb9d1795"></a>

```c
#define BT_MESH_TRANSMIT_COUNT(transmit)
```

相关声明：[BT_MESH_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga62fda0d731241efbaa4827e4eb9d1795)。

从发送值（Transmit Value）中解码发送次数（Transmit Count）。

<a id="r_ga2aa21171c5677d23ad0c472291639417"></a>

```c
#define BT_MESH_TRANSMIT_INT(transmit)
```

相关声明：[BT_MESH_TRANSMIT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga2aa21171c5677d23ad0c472291639417)。

从发送值（Transmit Value）中解码发送间隔（Transmit Interval）。

<a id="r_ga19208dea7bab9f31c2c793ef6201dd91"></a>

```c
#define BT_MESH_PUB_TRANSMIT(count, int_ms)
```

相关声明：[BT_MESH_PUB_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga19208dea7bab9f31c2c793ef6201dd91)。

编码发布重传次数（Publish Retransmit Count）和间隔步数（Interval Steps）。

<a id="r_ga13986422dda5edce4f5fb1ce387093e3"></a>

```c
#define BT_MESH_PUB_TRANSMIT_COUNT(transmit)
```

相关声明：[BT_MESH_PUB_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga13986422dda5edce4f5fb1ce387093e3)。

从给定值中解码发布重传次数（Publish Retransmit Count）。

<a id="r_gaac954956dd3913dd7ad2b93a2566afd9"></a>

```c
#define BT_MESH_PUB_TRANSMIT_INT(transmit)
```

相关声明：[BT_MESH_PUB_TRANSMIT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaac954956dd3913dd7ad2b93a2566afd9)。

从给定值中解码发布重传间隔（Publish Retransmit Interval）。

<a id="r_ga230538bb39ac3d6c8c0327d1fad77e69"></a>

```c
#define BT_MESH_PUB_MSG_TOTAL(pub)
```

相关声明：[BT_MESH_PUB_MSG_TOTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga230538bb39ac3d6c8c0327d1fad77e69)。

获取一个发布间隔（Publication Interval）内的消息总数，包括首次发布。

<a id="r_ga115ee29aba3c3e985aa11d6692ca0d83"></a>

```c
#define BT_MESH_PUB_MSG_NUM(pub)
```

相关声明：[BT_MESH_PUB_MSG_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga115ee29aba3c3e985aa11d6692ca0d83)。

获取消息在一个发布间隔（Publication Interval）内的序号。

<a id="r_ga8334ff2da1f0dc3ab2fc914059c33622"></a>

```c
#define BT_MESH_MODEL_PUB_DEFINE(_name, _update, _msg_len)
```

相关声明：[BT_MESH_MODEL_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8334ff2da1f0dc3ab2fc914059c33622)。

定义模型发布上下文（Model Publication Context）。

<a id="r_gaa2587adac719c50c311ae41c548b853c"></a>

```c
#define BT_MESH_MODELS_METADATA_ENTRY(_len, _id, _data)
```

相关声明：[BT_MESH_MODELS_METADATA_ENTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa2587adac719c50c311ae41c548b853c)。

初始化列表中的模型元数据条目结构体（Models Metadata Entry Structure）。

<a id="r_ga56b518123ab47cb3ae4a249f471ae556"></a>

```c
#define BT_MESH_MODELS_METADATA_NONE NULL
```

相关声明：[BT_MESH_MODELS_METADATA_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga56b518123ab47cb3ae4a249f471ae556)。

用于定义空模型元数据数组（Models Metadata Array）的辅助宏。

<a id="r_gaab5fe51071f6e54debd9136ac6a70a49"></a>

```c
#define BT_MESH_MODELS_METADATA_END { 0, 0, NULL }
```

相关声明：[BT_MESH_MODELS_METADATA_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaab5fe51071f6e54debd9136ac6a70a49)。

模型元数据列表（Models Metadata List）的结束项。

<a id="r_ga16516272b42420263b1c47c3ea16c0c8"></a>

```c
#define BT_MESH_TTL_DEFAULT 0xff
```

相关声明：[BT_MESH_TTL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga16516272b42420263b1c47c3ea16c0c8)。

特殊生存时间（Time To Live，TTL）值，用于请求使用已配置的默认 TTL。

<a id="r_ga071e85e929589d31bf876e2e09cf2f19"></a>

```c
#define BT_MESH_TTL_MAX 0x7f
```

相关声明：[BT_MESH_TTL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga071e85e929589d31bf876e2e09cf2f19)。

允许的最大生存时间（TTL）值。

<a id="define-members-0"></a>

### 组地址（Group Addresses）

<a id="r_ga6d11790af686e6d48f08c6f1cd65317c"></a>

```c
#define BT_MESH_ADDR_UNASSIGNED 0x0000
```

相关声明：[BT_MESH_ADDR_UNASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga6d11790af686e6d48f08c6f1cd65317c)。

未分配（Unassigned）。

<a id="r_ga27aafd100b6ccc1de060a75370184620"></a>

```c
#define BT_MESH_ADDR_ALL_NODES 0xffff
```

相关声明：[BT_MESH_ADDR_ALL_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga27aafd100b6ccc1de060a75370184620)。

所有节点（All Nodes）。

<a id="r_ga5ee81d48846de9c9c966ffe0b90ff011"></a>

```c
#define BT_MESH_ADDR_RELAYS 0xfffe
```

相关声明：[BT_MESH_ADDR_RELAYS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga5ee81d48846de9c9c966ffe0b90ff011)。

所有中继（All Relays）。

<a id="r_ga5d44892368bb7c1ecd205a81e66bd6f7"></a>

```c
#define BT_MESH_ADDR_FRIENDS 0xfffd
```

相关声明：[BT_MESH_ADDR_FRIENDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga5d44892368bb7c1ecd205a81e66bd6f7)。

所有友元节点（All Friends）。

<a id="r_ga30d4975d25c2c120da1cbfadf29c098f"></a>

```c
#define BT_MESH_ADDR_PROXIES 0xfffc
```

相关声明：[BT_MESH_ADDR_PROXIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga30d4975d25c2c120da1cbfadf29c098f)。

所有代理（All Proxies）。

<a id="r_gabf77d8365ddc278838fa450826e43243"></a>

```c
#define BT_MESH_ADDR_DFW_NODES 0xfffb
```

相关声明：[BT_MESH_ADDR_DFW_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabf77d8365ddc278838fa450826e43243)。

所有定向转发节点（All Directed Forwarding Nodes）。

<a id="r_gafd70174e5072dbbfed31156f152aeaa1"></a>

```c
#define BT_MESH_ADDR_IP_NODES 0xfffa
```

相关声明：[BT_MESH_ADDR_IP_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gafd70174e5072dbbfed31156f152aeaa1)。

所有 IPT 节点（All IPT Nodes）。

<a id="r_ga1055381438e55e953dec2e6d592ab103"></a>

```c
#define BT_MESH_ADDR_IP_BR_ROUTERS 0xfff9
```

相关声明：[BT_MESH_ADDR_IP_BR_ROUTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1055381438e55e953dec2e6d592ab103)。

所有 IPT 边界路由器（All IPT Border Routers）。

<a id="define-members-1"></a>

### 预定义密钥索引（Predefined Key Indexes）

<a id="r_gace23095bac3705c2f2afab749e48c02d"></a>

```c
#define BT_MESH_KEY_UNUSED 0xffff
```

相关声明：[BT_MESH_KEY_UNUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gace23095bac3705c2f2afab749e48c02d)。

密钥未使用（Key Unused）。

<a id="r_ga7718cce0713be98a08420c7eab1b40ee"></a>

```c
#define BT_MESH_KEY_ANY 0xffff
```

相关声明：[BT_MESH_KEY_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7718cce0713be98a08420c7eab1b40ee)。

任意密钥索引（Any Key Index）。

<a id="r_gabd37f17f3f5c3bc399ad3699df282675"></a>

```c
#define BT_MESH_KEY_DEV 0xfffe
```

相关声明：[BT_MESH_KEY_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabd37f17f3f5c3bc399ad3699df282675)。

设备密钥（Device key）。

<a id="r_ga9c64b38f2a6879f4750e3e1828e8ab7a"></a>

```c
#define BT_MESH_KEY_DEV_LOCAL BT_MESH_KEY_DEV
```

相关声明：[BT_MESH_KEY_DEV_LOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga9c64b38f2a6879f4750e3e1828e8ab7a)、[BT_MESH_KEY_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabd37f17f3f5c3bc399ad3699df282675)。

本地设备密钥（Local Device Key）。

<a id="r_gaaa6ffb62df5d6d55c831d4d9860fc7eb"></a>

```c
#define BT_MESH_KEY_DEV_REMOTE 0xfffd
```

相关声明：[BT_MESH_KEY_DEV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaaa6ffb62df5d6d55c831d4d9860fc7eb)。

远端设备密钥（Remote Device Key）。

<a id="r_gace0a526534e31e8067daf283407533fd"></a>

```c
#define BT_MESH_KEY_DEV_ANY 0xfffc
```

相关声明：[BT_MESH_KEY_DEV_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gace0a526534e31e8067daf283407533fd)。

任意设备密钥（Any Device Key）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga7cac052ef76f4b37a95343329b078e77"></a>

```c
int bt_mesh_model_send (const struct bt_mesh_model *model, struct bt_mesh_msg_ctx *ctx, struct net_buf_simple *msg, const struct bt_mesh_send_cb *cb, void *cb_data)
```

相关声明：[bt_mesh_model_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7cac052ef76f4b37a95343329b078e77)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)。

发送访问层消息（Access Layer Message）。

<a id="r_ga06644f8a5fa43351328d3f3403dbad03"></a>

```c
int bt_mesh_model_publish (const struct bt_mesh_model *model)
```

相关声明：[bt_mesh_model_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

发送模型发布消息（Model Publication Message）。

<a id="r_ga1b961d45f8b7c231c698ca229115e434"></a>

```c
static bool bt_mesh_model_pub_is_retransmission (const struct bt_mesh_model *model)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_pub_is_retransmission](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b961d45f8b7c231c698ca229115e434)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

检查消息是否正在重传（Retransmitted）。

<a id="r_ga8edba04af103fb11994d4d3e558ec4fb"></a>

```c
const struct bt_mesh_elem * bt_mesh_model_elem (const struct bt_mesh_model *mod)
```

相关声明：[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[bt_mesh_model_elem](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8edba04af103fb11994d4d3e558ec4fb)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

获取模型所属的元素（Element）。

<a id="r_gaf0510f9511d72f1d4fd07f865753a50a"></a>

```c
const struct bt_mesh_model * bt_mesh_model_find (const struct bt_mesh_elem *elem, uint16_t id)
```

相关声明：[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model_find](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf0510f9511d72f1d4fd07f865753a50a)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找 SIG 模型（SIG Model）。

<a id="r_gadfb473db4b23902a192e12d322ff1fd2"></a>

```c
const struct bt_mesh_model * bt_mesh_model_find_vnd (const struct bt_mesh_elem *elem, uint16_t company, uint16_t id)
```

相关声明：[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model_find_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadfb473db4b23902a192e12d322ff1fd2)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找厂商模型（Vendor Model）。

<a id="r_gaa8694fdab3f514d8051dad1cc7362ac9"></a>

```c
static bool bt_mesh_model_in_primary (const struct bt_mesh_model *mod)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_in_primary](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa8694fdab3f514d8051dad1cc7362ac9)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

获取模型是否位于设备的主元素（Primary Element）中。

<a id="r_gadff0895c5c34928d778fa615512b3d85"></a>

```c
int bt_mesh_model_data_store (const struct bt_mesh_model *mod, bool vnd, const char *name, const void *data, size_t data_len)
```

相关声明：[bt_mesh_model_data_store](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

立即将模型的用户数据保存到持久存储（Persistent Storage）。

<a id="r_ga762896dd2e806b5be061b220d53ce4db"></a>

```c
void bt_mesh_model_data_store_schedule (const struct bt_mesh_model *mod)
```

相关声明：[bt_mesh_model_data_store_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

安排将模型的用户数据保存到持久存储（Persistent Storage）。

<a id="r_gaf6356f715c8968151b8d539f2dd1880c"></a>

```c
int bt_mesh_model_extend (const struct bt_mesh_model *extending_mod, const struct bt_mesh_model *base_mod)
```

相关声明：[bt_mesh_model_extend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

使一个模型扩展（Extend）另一个模型。

<a id="r_ga03ce9f6f9ccf734ea72beede09288923"></a>

```c
int bt_mesh_model_correspond (const struct bt_mesh_model *corresponding_mod, const struct bt_mesh_model *base_mod)
```

相关声明：[bt_mesh_model_correspond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga03ce9f6f9ccf734ea72beede09288923)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

使一个模型与另一个模型建立对应关系（Correspond）。

<a id="r_ga10603a5846210a397f306b227ce10c2e"></a>

```c
bool bt_mesh_model_is_extended (const struct bt_mesh_model *model)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_is_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga10603a5846210a397f306b227ce10c2e)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

检查模型是否被另一个模型扩展（Extended）。

<a id="r_ga8575f680e77d86d6c85cac27985b9f3c"></a>

```c
int bt_mesh_comp_change_prepare (void)
```

相关声明：[bt_mesh_comp_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8575f680e77d86d6c85cac27985b9f3c)。

指示组成数据（Composition Data）将在下次启动时改变。

<a id="r_ga26ac86bdd32d27e0091735d98670687a"></a>

```c
int bt_mesh_models_metadata_change_prepare (void)
```

相关声明：[bt_mesh_models_metadata_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga26ac86bdd32d27e0091735d98670687a)。

指示元数据（Metadata）将在下次启动时改变。

<a id="r_ga8445c550a47dba16e3fa6fea36d6d9fc"></a>

```c
int bt_mesh_comp2_register (const struct bt_mesh_comp2 *comp2)
```

相关声明：[bt_mesh_comp2_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8445c550a47dba16e3fa6fea36d6d9fc)、[bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)。

注册设备的组成数据（Composition Data）第 2 页。

## 1.4\_详细说明（Detailed Documentation）

<a id="ad28c5301ea6cf93f3bf2a672043cae4e"></a>

### `BT_MESH_MODEL_RUNTIME_INIT`

```c
#define BT_MESH_MODEL_RUNTIME_INIT ( _user_data)
```

展开值（Value）：

```c
.rt = &(struct bt_mesh_model_rt_ctx){ .user_data = (_user_data) },
```


## 1.5\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/settings/settings.h](../api_source_configuration_reference/P035_settings.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/mesh/msg.h](../api_source_reference/P566_msg.h_源码浏览.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)
- [bt_mesh_elem::bt_mesh_elem_rt_ctx](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)
- [bt_mesh_models_metadata_entry](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [bt_mesh_model::bt_mesh_model_rt_ctx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)
- [bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)
- [bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)
- [bt_mesh_comp2_record](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md)
- [bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)
- [BT_MESH_ADDR_IS_UNICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1a4694cccf834d71f0abe2a0283cb9a8)
- [BT_MESH_ADDR_IS_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gab50cc8dca6f7ffd5420ef4fb38fbe224)
- [BT_MESH_ADDR_IS_FIXED_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff5ff58937924a1e6297aa1b20efc30f)
- [BT_MESH_ADDR_IS_VIRTUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga623eb2da2c880eec2107f36402ba6621)
- [BT_MESH_ADDR_IS_RFU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga98ba7663259ca43cd5a38c7a9e16516d)
- [BT_MESH_IS_DEV_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac4aafa0bdd24fb51d515a62e83917936)
- [BT_MESH_APP_SEG_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa620c32d1dce8e4b691b7f4270016506)
- [BT_MESH_APP_UNSEG_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)
- [BT_MESH_RX_SEG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga18756e939ec3b312eef5c3dc9fd70270)
- [BT_MESH_TX_SEG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b2a3610ac370266578abce195e65fa2)
- [BT_MESH_TX_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga86d7386603ecd89952b6d540ea4243c2)
- [BT_MESH_RX_SDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga36f299f2fc13892b5a7d871dad1ec9ce)
- [BT_MESH_ELEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga321a5091dabd4ec4beb5396db6cabf44)
- [BT_MESH_MODEL_OP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga00915cfdff7dc0646f24d6b06e124d0d)
- [BT_MESH_MODEL_OP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa52a40ef5972c4f34cf5ff5a10e21289)
- [BT_MESH_MODEL_OP_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga72d1d19701be52f5eac6af475f9b19a9)
- [BT_MESH_LEN_EXACT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga637e1be0298dc681414645867b28b59f)
- [BT_MESH_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga691ed9b3ab3ddaceda0f81c4a715ab3a)
- [BT_MESH_MODEL_OP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf2c164506c601214c85d451747176827)
- [BT_MESH_MODEL_NO_OPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gae6d55e0a27bb7c448affd312a2e11656)
- [BT_MESH_MODEL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gab0ad2aab95d49e5b60fe8dafd69132a4)
- [BT_MESH_MODEL_CNT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga925da443eb15a4c1980d48a69388dc2c)
- [BT_MESH_MODEL_CNT_VND_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga32733dccd9329aa938dc0bd21cf9beae)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_METADATA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga40204b4ccaa819a487de168bcf66c98f)
- [BT_MESH_MODEL_VND_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabe79d914990ba2721f5bb7081910e512)
- [BT_MESH_MODEL_VND_METADATA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac62334962dcbe3a75a03ce5744b326d8)
- [BT_MESH_MODEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gae694f5ac7ef9f0de37aaba846443586f)
- [BT_MESH_MODEL_VND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga3759c8c88db48be662bf2511ff514edd)
- [BT_MESH_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff82bf652232fbce71c31f38a10577a9)
- [BT_MESH_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga62fda0d731241efbaa4827e4eb9d1795)
- [BT_MESH_TRANSMIT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga2aa21171c5677d23ad0c472291639417)
- [BT_MESH_PUB_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga19208dea7bab9f31c2c793ef6201dd91)
- [BT_MESH_PUB_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga13986422dda5edce4f5fb1ce387093e3)
- [BT_MESH_PUB_TRANSMIT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaac954956dd3913dd7ad2b93a2566afd9)
- [BT_MESH_PUB_MSG_TOTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga230538bb39ac3d6c8c0327d1fad77e69)
- [BT_MESH_PUB_MSG_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga115ee29aba3c3e985aa11d6692ca0d83)
- [BT_MESH_MODEL_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8334ff2da1f0dc3ab2fc914059c33622)
- [BT_MESH_MODELS_METADATA_ENTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa2587adac719c50c311ae41c548b853c)
- [BT_MESH_MODELS_METADATA_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga56b518123ab47cb3ae4a249f471ae556)
- [BT_MESH_MODELS_METADATA_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaab5fe51071f6e54debd9136ac6a70a49)
- [BT_MESH_TTL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga16516272b42420263b1c47c3ea16c0c8)
- [BT_MESH_TTL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga071e85e929589d31bf876e2e09cf2f19)
- [BT_MESH_ADDR_UNASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga6d11790af686e6d48f08c6f1cd65317c)
- [BT_MESH_ADDR_ALL_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga27aafd100b6ccc1de060a75370184620)
- [BT_MESH_ADDR_RELAYS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga5ee81d48846de9c9c966ffe0b90ff011)
- [BT_MESH_ADDR_FRIENDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga5d44892368bb7c1ecd205a81e66bd6f7)
- [BT_MESH_ADDR_PROXIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga30d4975d25c2c120da1cbfadf29c098f)
- [BT_MESH_ADDR_DFW_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabf77d8365ddc278838fa450826e43243)
- [BT_MESH_ADDR_IP_NODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gafd70174e5072dbbfed31156f152aeaa1)
- [BT_MESH_ADDR_IP_BR_ROUTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1055381438e55e953dec2e6d592ab103)
- [BT_MESH_KEY_UNUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gace23095bac3705c2f2afab749e48c02d)
- [BT_MESH_KEY_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7718cce0713be98a08420c7eab1b40ee)
- [BT_MESH_KEY_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gabd37f17f3f5c3bc399ad3699df282675)
- [BT_MESH_KEY_DEV_LOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga9c64b38f2a6879f4750e3e1828e8ab7a)
- [BT_MESH_KEY_DEV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaaa6ffb62df5d6d55c831d4d9860fc7eb)
- [BT_MESH_KEY_DEV_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gace0a526534e31e8067daf283407533fd)
- [bt_mesh_model_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7cac052ef76f4b37a95343329b078e77)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_model_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_model_pub_is_retransmission](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b961d45f8b7c231c698ca229115e434)
- [bt_mesh_model_elem](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8edba04af103fb11994d4d3e558ec4fb)
- [bt_mesh_model_find](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf0510f9511d72f1d4fd07f865753a50a)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_model_find_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadfb473db4b23902a192e12d322ff1fd2)
- [bt_mesh_model_in_primary](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa8694fdab3f514d8051dad1cc7362ac9)
- [bt_mesh_model_data_store](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85)
- [bt_mesh_model_data_store_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db)
- [bt_mesh_model_extend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c)
- [bt_mesh_model_correspond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga03ce9f6f9ccf734ea72beede09288923)
- [bt_mesh_model_is_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga10603a5846210a397f306b227ce10c2e)
- [bt_mesh_comp_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8575f680e77d86d6c85cac27985b9f3c)
- [bt_mesh_models_metadata_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga26ac86bdd32d27e0091735d98670687a)
- [bt_mesh_comp2_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8445c550a47dba16e3fa6fea36d6d9fc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__acpi__acpi.h_文件参考.md)
