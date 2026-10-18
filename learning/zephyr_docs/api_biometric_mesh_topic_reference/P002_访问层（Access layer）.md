---
id: learning.zephyr-docs.api-biometric-mesh-topic-reference.page-2
title: 访问层（Access layer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_访问层（Access layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

访问层（Access layer）

<a id="details"></a>

访问层（Access layer）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Felem"></a>

```c
struct bt_mesh_elem
```

相关声明：[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)。

描述Mesh元素（Mesh Element）的抽象。

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

## 2.2\_宏定义（Macros）

<a id="r_ga1a4694cccf834d71f0abe2a0283cb9a8"></a>

```c
#define BT_MESH_ADDR_IS_UNICAST(addr)
```

相关声明：[BT_MESH_ADDR_IS_UNICAST](#ga1a4694cccf834d71f0abe2a0283cb9a8)。

检查蓝牙 Mesh 地址是否为单播地址（Unicast Address）。

<a id="r_gab50cc8dca6f7ffd5420ef4fb38fbe224"></a>

```c
#define BT_MESH_ADDR_IS_GROUP(addr)
```

相关声明：[BT_MESH_ADDR_IS_GROUP](#gab50cc8dca6f7ffd5420ef4fb38fbe224)。

检查蓝牙 Mesh 地址是否为组地址（Group Address）。

<a id="r_gaff5ff58937924a1e6297aa1b20efc30f"></a>

```c
#define BT_MESH_ADDR_IS_FIXED_GROUP(addr)
```

相关声明：[BT_MESH_ADDR_IS_FIXED_GROUP](#gaff5ff58937924a1e6297aa1b20efc30f)。

检查蓝牙 Mesh 地址是否为固定组地址（Fixed Group Address）。

<a id="r_ga623eb2da2c880eec2107f36402ba6621"></a>

```c
#define BT_MESH_ADDR_IS_VIRTUAL(addr)
```

相关声明：[BT_MESH_ADDR_IS_VIRTUAL](#ga623eb2da2c880eec2107f36402ba6621)。

检查蓝牙 Mesh 地址是否为虚拟地址（Virtual Address）。

<a id="r_ga98ba7663259ca43cd5a38c7a9e16516d"></a>

```c
#define BT_MESH_ADDR_IS_RFU(addr)
```

相关声明：[BT_MESH_ADDR_IS_RFU](#ga98ba7663259ca43cd5a38c7a9e16516d)。

检查蓝牙 Mesh 地址是否为保留供未来使用的地址（Reserved for Future Use，RFU）。

<a id="r_gac4aafa0bdd24fb51d515a62e83917936"></a>

```c
#define BT_MESH_IS_DEV_KEY(key)
```

相关声明：[BT_MESH_IS_DEV_KEY](#gac4aafa0bdd24fb51d515a62e83917936)。

检查蓝牙 Mesh 密钥是否为设备密钥（Device Key）。

<a id="r_gaa620c32d1dce8e4b691b7f4270016506"></a>

```c
#define BT_MESH_APP_SEG_SDU_MAX 12
```

相关声明：[BT_MESH_APP_SEG_SDU_MAX](#gaa620c32d1dce8e4b691b7f4270016506)。

访问消息分段（Access Message Segment）的最大大小，单位为八位组（Octets）。

<a id="r_ga64eb6a94b1db9899c4f5bbf4cc88cd9f"></a>

```c
#define BT_MESH_APP_UNSEG_SDU_MAX 15
```

相关声明：[BT_MESH_APP_UNSEG_SDU_MAX](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)。

未分段访问消息（Unsegmented Access Message）的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga18756e939ec3b312eef5c3dc9fd70270"></a>

```c
#define BT_MESH_RX_SEG_MAX 0
```

相关声明：[BT_MESH_RX_SEG_MAX](#ga18756e939ec3b312eef5c3dc9fd70270)。

接收消息所支持的最大分段数量（Number of Segments）。

<a id="r_ga1b2a3610ac370266578abce195e65fa2"></a>

```c
#define BT_MESH_TX_SEG_MAX 0
```

相关声明：[BT_MESH_TX_SEG_MAX](#ga1b2a3610ac370266578abce195e65fa2)。

发送消息所支持的最大分段数量（Number of Segments）。

<a id="r_ga86d7386603ecd89952b6d540ea4243c2"></a>

```c
#define BT_MESH_TX_SDU_MAX
```

相关声明：[BT_MESH_TX_SDU_MAX](#ga86d7386603ecd89952b6d540ea4243c2)。

发送访问消息（Outgoing Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga36f299f2fc13892b5a7d871dad1ec9ce"></a>

```c
#define BT_MESH_RX_SDU_MAX
```

相关声明：[BT_MESH_RX_SDU_MAX](#ga36f299f2fc13892b5a7d871dad1ec9ce)。

接收访问消息（Incoming Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="r_ga321a5091dabd4ec4beb5396db6cabf44"></a>

```c
#define BT_MESH_ELEM(_loc, _mods, _vnd_mods)
```

相关声明：[BT_MESH_ELEM](#ga321a5091dabd4ec4beb5396db6cabf44)。

用于在数组中定义 Mesh 元素（Element）的辅助宏。

<a id="r_ga00915cfdff7dc0646f24d6b06e124d0d"></a>

```c
#define BT_MESH_MODEL_OP_1(b0)
```

相关声明：[BT_MESH_MODEL_OP_1](#ga00915cfdff7dc0646f24d6b06e124d0d)。

编码 1 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="r_gaa52a40ef5972c4f34cf5ff5a10e21289"></a>

```c
#define BT_MESH_MODEL_OP_2(b0, b1)
```

相关声明：[BT_MESH_MODEL_OP_2](#gaa52a40ef5972c4f34cf5ff5a10e21289)。

编码 2 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="r_ga72d1d19701be52f5eac6af475f9b19a9"></a>

```c
#define BT_MESH_MODEL_OP_3(b0, cid)
```

相关声明：[BT_MESH_MODEL_OP_3](#ga72d1d19701be52f5eac6af475f9b19a9)。

编码 3 字节操作码（Opcode）的宏，用于厂商特定消息（Vendor-Specific Message）。

<a id="r_ga637e1be0298dc681414645867b28b59f"></a>

```c
#define BT_MESH_LEN_EXACT(len)
```

相关声明：[BT_MESH_LEN_EXACT](#ga637e1be0298dc681414645867b28b59f)。

为定长消息编码确切消息长度（Exact Message Length）的宏。

<a id="r_ga691ed9b3ab3ddaceda0f81c4a715ab3a"></a>

```c
#define BT_MESH_LEN_MIN(len)
```

相关声明：[BT_MESH_LEN_MIN](#ga691ed9b3ab3ddaceda0f81c4a715ab3a)。

为变长消息编码最小消息长度（Minimum Message Length）的宏。

<a id="r_gaf2c164506c601214c85d451747176827"></a>

```c
#define BT_MESH_MODEL_OP_END { 0, 0, NULL }
```

相关声明：[BT_MESH_MODEL_OP_END](#gaf2c164506c601214c85d451747176827)。

操作码列表（Opcode List）的结束项。

<a id="r_gae6d55e0a27bb7c448affd312a2e11656"></a>

```c
#define BT_MESH_MODEL_NO_OPS
```

相关声明：[BT_MESH_MODEL_NO_OPS](#gae6d55e0a27bb7c448affd312a2e11656)。

用于定义空操作码列表（Empty Opcode List）的辅助宏。

<a id="r_gab0ad2aab95d49e5b60fe8dafd69132a4"></a>

```c
#define BT_MESH_MODEL_NONE ((const struct bt_mesh_model []){})
```

相关声明：[BT_MESH_MODEL_NONE](#gab0ad2aab95d49e5b60fe8dafd69132a4)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

用于定义空模型数组（Empty Model Array）的辅助宏。

<a id="r_ga925da443eb15a4c1980d48a69388dc2c"></a>

```c
#define BT_MESH_MODEL_CNT_CB(_id, _op, _pub, _user_data, _keys, _grps, _cb)
```

相关声明：[BT_MESH_MODEL_CNT_CB](#ga925da443eb15a4c1980d48a69388dc2c)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数，且指定密钥和组的数量。

<a id="r_ga32733dccd9329aa938dc0bd21cf9beae"></a>

```c
#define BT_MESH_MODEL_CNT_VND_CB(_company, _id, _op, _pub, _user_data, _keys, _grps, _cb)
```

相关声明：[BT_MESH_MODEL_CNT_VND_CB](#ga32733dccd9329aa938dc0bd21cf9beae)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数，且指定密钥和组的数量。

<a id="r_gac062c101b7310020e11a527de9c40d3a"></a>

```c
#define BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, _cb)
```

相关声明：[BT_MESH_MODEL_CB](#gac062c101b7310020e11a527de9c40d3a)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数。

<a id="r_ga40204b4ccaa819a487de168bcf66c98f"></a>

```c
#define BT_MESH_MODEL_METADATA_CB(_id, _op, _pub, _user_data, _cb, _metadata)
```

相关声明：[BT_MESH_MODEL_METADATA_CB](#ga40204b4ccaa819a487de168bcf66c98f)。

组成数据（Composition Data）中的 SIG 模型条目，带回调函数和元数据（Metadata）。

<a id="r_gabe79d914990ba2721f5bb7081910e512"></a>

```c
#define BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, _cb)
```

相关声明：[BT_MESH_MODEL_VND_CB](#gabe79d914990ba2721f5bb7081910e512)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数。

<a id="r_gac62334962dcbe3a75a03ce5744b326d8"></a>

```c
#define BT_MESH_MODEL_VND_METADATA_CB(_company, _id, _op, _pub, _user_data, _cb, _metadata)
```

相关声明：[BT_MESH_MODEL_VND_METADATA_CB](#gac62334962dcbe3a75a03ce5744b326d8)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数和元数据（Metadata）。

<a id="r_gae694f5ac7ef9f0de37aaba846443586f"></a>

```c
#define BT_MESH_MODEL(_id, _op, _pub, _user_data)
```

相关声明：[BT_MESH_MODEL](#gae694f5ac7ef9f0de37aaba846443586f)。

组成数据（Composition Data）中的 SIG 模型条目。

<a id="r_ga3759c8c88db48be662bf2511ff514edd"></a>

```c
#define BT_MESH_MODEL_VND(_company, _id, _op, _pub, _user_data)
```

相关声明：[BT_MESH_MODEL_VND](#ga3759c8c88db48be662bf2511ff514edd)。

组成数据（Composition Data）中的厂商模型（Vendor Model）条目。

<a id="r_gaff82bf652232fbce71c31f38a10577a9"></a>

```c
#define BT_MESH_TRANSMIT(count, int_ms)
```

相关声明：[BT_MESH_TRANSMIT](#gaff82bf652232fbce71c31f38a10577a9)。

编码发送次数（Transmission Count）和间隔步数（Interval Steps）。

<a id="r_ga62fda0d731241efbaa4827e4eb9d1795"></a>

```c
#define BT_MESH_TRANSMIT_COUNT(transmit)
```

相关声明：[BT_MESH_TRANSMIT_COUNT](#ga62fda0d731241efbaa4827e4eb9d1795)。

从发送值（Transmit Value）中解码发送次数（Transmit Count）。

<a id="r_ga2aa21171c5677d23ad0c472291639417"></a>

```c
#define BT_MESH_TRANSMIT_INT(transmit)
```

相关声明：[BT_MESH_TRANSMIT_INT](#ga2aa21171c5677d23ad0c472291639417)。

从发送值（Transmit Value）中解码发送间隔（Transmit Interval）。

<a id="r_ga19208dea7bab9f31c2c793ef6201dd91"></a>

```c
#define BT_MESH_PUB_TRANSMIT(count, int_ms)
```

相关声明：[BT_MESH_PUB_TRANSMIT](#ga19208dea7bab9f31c2c793ef6201dd91)。

编码发布重传次数（Publish Retransmit Count）和间隔步数（Interval Steps）。

<a id="r_ga13986422dda5edce4f5fb1ce387093e3"></a>

```c
#define BT_MESH_PUB_TRANSMIT_COUNT(transmit)
```

相关声明：[BT_MESH_PUB_TRANSMIT_COUNT](#ga13986422dda5edce4f5fb1ce387093e3)。

从给定值中解码发布重传次数（Publish Retransmit Count）。

<a id="r_gaac954956dd3913dd7ad2b93a2566afd9"></a>

```c
#define BT_MESH_PUB_TRANSMIT_INT(transmit)
```

相关声明：[BT_MESH_PUB_TRANSMIT_INT](#gaac954956dd3913dd7ad2b93a2566afd9)。

从给定值中解码发布重传间隔（Publish Retransmit Interval）。

<a id="r_ga230538bb39ac3d6c8c0327d1fad77e69"></a>

```c
#define BT_MESH_PUB_MSG_TOTAL(pub)
```

相关声明：[BT_MESH_PUB_MSG_TOTAL](#ga230538bb39ac3d6c8c0327d1fad77e69)。

获取一个发布间隔（Publication Interval）内的消息总数，包括首次发布。

<a id="r_ga115ee29aba3c3e985aa11d6692ca0d83"></a>

```c
#define BT_MESH_PUB_MSG_NUM(pub)
```

相关声明：[BT_MESH_PUB_MSG_NUM](#ga115ee29aba3c3e985aa11d6692ca0d83)。

获取消息在一个发布间隔（Publication Interval）内的序号。

<a id="r_ga8334ff2da1f0dc3ab2fc914059c33622"></a>

```c
#define BT_MESH_MODEL_PUB_DEFINE(_name, _update, _msg_len)
```

相关声明：[BT_MESH_MODEL_PUB_DEFINE](#ga8334ff2da1f0dc3ab2fc914059c33622)。

定义模型发布上下文（Model Publication Context）。

<a id="r_gaa2587adac719c50c311ae41c548b853c"></a>

```c
#define BT_MESH_MODELS_METADATA_ENTRY(_len, _id, _data)
```

相关声明：[BT_MESH_MODELS_METADATA_ENTRY](#gaa2587adac719c50c311ae41c548b853c)。

初始化列表中的模型元数据条目结构体（Models Metadata Entry Structure）。

<a id="r_ga56b518123ab47cb3ae4a249f471ae556"></a>

```c
#define BT_MESH_MODELS_METADATA_NONE NULL
```

相关声明：[BT_MESH_MODELS_METADATA_NONE](#ga56b518123ab47cb3ae4a249f471ae556)。

用于定义空模型元数据数组（Models Metadata Array）的辅助宏。

<a id="r_gaab5fe51071f6e54debd9136ac6a70a49"></a>

```c
#define BT_MESH_MODELS_METADATA_END { 0, 0, NULL }
```

相关声明：[BT_MESH_MODELS_METADATA_END](#gaab5fe51071f6e54debd9136ac6a70a49)。

模型元数据列表（Models Metadata List）的结束项。

<a id="r_ga16516272b42420263b1c47c3ea16c0c8"></a>

```c
#define BT_MESH_TTL_DEFAULT 0xff
```

相关声明：[BT_MESH_TTL_DEFAULT](#ga16516272b42420263b1c47c3ea16c0c8)。

特殊生存时间（Time To Live，TTL）值，用于请求使用已配置的默认 TTL。

<a id="r_ga071e85e929589d31bf876e2e09cf2f19"></a>

```c
#define BT_MESH_TTL_MAX 0x7f
```

相关声明：[BT_MESH_TTL_MAX](#ga071e85e929589d31bf876e2e09cf2f19)。

允许的最大生存时间（TTL）值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga7cac052ef76f4b37a95343329b078e77"></a>

```c
int bt_mesh_model_send (const struct bt_mesh_model *model, struct bt_mesh_msg_ctx *ctx, struct net_buf_simple *msg, const struct bt_mesh_send_cb *cb, void *cb_data)
```

相关声明：[bt_mesh_model_send](#ga7cac052ef76f4b37a95343329b078e77)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)。

发送访问层消息（Access Layer Message）。

<a id="r_ga06644f8a5fa43351328d3f3403dbad03"></a>

```c
int bt_mesh_model_publish (const struct bt_mesh_model *model)
```

相关声明：[bt_mesh_model_publish](#ga06644f8a5fa43351328d3f3403dbad03)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

发送模型发布消息（Model Publication Message）。

<a id="r_ga1b961d45f8b7c231c698ca229115e434"></a>

```c
static bool bt_mesh_model_pub_is_retransmission (const struct bt_mesh_model *model)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_pub_is_retransmission](#ga1b961d45f8b7c231c698ca229115e434)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

检查消息是否正在重传（Retransmitted）。

<a id="r_ga8edba04af103fb11994d4d3e558ec4fb"></a>

```c
const struct bt_mesh_elem * bt_mesh_model_elem (const struct bt_mesh_model *mod)
```

相关声明：[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[bt_mesh_model_elem](#ga8edba04af103fb11994d4d3e558ec4fb)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

获取模型所属的元素（Element）。

<a id="r_gaf0510f9511d72f1d4fd07f865753a50a"></a>

```c
const struct bt_mesh_model * bt_mesh_model_find (const struct bt_mesh_elem *elem, uint16_t id)
```

相关声明：[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model_find](#gaf0510f9511d72f1d4fd07f865753a50a)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找 SIG 模型（SIG Model）。

<a id="r_gadfb473db4b23902a192e12d322ff1fd2"></a>

```c
const struct bt_mesh_model * bt_mesh_model_find_vnd (const struct bt_mesh_elem *elem, uint16_t company, uint16_t id)
```

相关声明：[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model_find_vnd](#gadfb473db4b23902a192e12d322ff1fd2)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找厂商模型（Vendor Model）。

<a id="r_gaa8694fdab3f514d8051dad1cc7362ac9"></a>

```c
static bool bt_mesh_model_in_primary (const struct bt_mesh_model *mod)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_in_primary](#gaa8694fdab3f514d8051dad1cc7362ac9)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

获取模型是否位于设备的主元素（Primary Element）中。

<a id="r_gadff0895c5c34928d778fa615512b3d85"></a>

```c
int bt_mesh_model_data_store (const struct bt_mesh_model *mod, bool vnd, const char *name, const void *data, size_t data_len)
```

相关声明：[bt_mesh_model_data_store](#gadff0895c5c34928d778fa615512b3d85)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

立即将模型的用户数据保存到持久存储（Persistent Storage）。

<a id="r_ga762896dd2e806b5be061b220d53ce4db"></a>

```c
void bt_mesh_model_data_store_schedule (const struct bt_mesh_model *mod)
```

相关声明：[bt_mesh_model_data_store_schedule](#ga762896dd2e806b5be061b220d53ce4db)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

安排将模型的用户数据保存到持久存储（Persistent Storage）。

<a id="r_gaf6356f715c8968151b8d539f2dd1880c"></a>

```c
int bt_mesh_model_extend (const struct bt_mesh_model *extending_mod, const struct bt_mesh_model *base_mod)
```

相关声明：[bt_mesh_model_extend](#gaf6356f715c8968151b8d539f2dd1880c)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

使一个模型扩展（Extend）另一个模型。

<a id="r_ga03ce9f6f9ccf734ea72beede09288923"></a>

```c
int bt_mesh_model_correspond (const struct bt_mesh_model *corresponding_mod, const struct bt_mesh_model *base_mod)
```

相关声明：[bt_mesh_model_correspond](#ga03ce9f6f9ccf734ea72beede09288923)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

使一个模型与另一个模型建立对应关系（Correspond）。

<a id="r_ga10603a5846210a397f306b227ce10c2e"></a>

```c
bool bt_mesh_model_is_extended (const struct bt_mesh_model *model)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_model_is_extended](#ga10603a5846210a397f306b227ce10c2e)、[bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)。

检查模型是否被另一个模型扩展（Extended）。

<a id="r_ga8575f680e77d86d6c85cac27985b9f3c"></a>

```c
int bt_mesh_comp_change_prepare (void)
```

相关声明：[bt_mesh_comp_change_prepare](#ga8575f680e77d86d6c85cac27985b9f3c)。

指示组成数据（Composition Data）将在下次启动时改变。

<a id="r_ga26ac86bdd32d27e0091735d98670687a"></a>

```c
int bt_mesh_models_metadata_change_prepare (void)
```

相关声明：[bt_mesh_models_metadata_change_prepare](#ga26ac86bdd32d27e0091735d98670687a)。

指示元数据（Metadata）将在下次启动时改变。

<a id="r_ga8445c550a47dba16e3fa6fea36d6d9fc"></a>

```c
int bt_mesh_comp2_register (const struct bt_mesh_comp2 *comp2)
```

相关声明：[bt_mesh_comp2_register](#ga8445c550a47dba16e3fa6fea36d6d9fc)、[bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)。

注册设备的组成数据（Composition Data）第 2 页。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 2.4\_组地址（Group Addresses）

<a id="r_ga6d11790af686e6d48f08c6f1cd65317c"></a>

```c
#define BT_MESH_ADDR_UNASSIGNED 0x0000
```

相关声明：[BT_MESH_ADDR_UNASSIGNED](#ga6d11790af686e6d48f08c6f1cd65317c)。

未分配（Unassigned）。

<a id="r_ga27aafd100b6ccc1de060a75370184620"></a>

```c
#define BT_MESH_ADDR_ALL_NODES 0xffff
```

相关声明：[BT_MESH_ADDR_ALL_NODES](#ga27aafd100b6ccc1de060a75370184620)。

所有节点（All Nodes）。

<a id="r_ga5ee81d48846de9c9c966ffe0b90ff011"></a>

```c
#define BT_MESH_ADDR_RELAYS 0xfffe
```

相关声明：[BT_MESH_ADDR_RELAYS](#ga5ee81d48846de9c9c966ffe0b90ff011)。

所有中继（All Relays）。

<a id="r_ga5d44892368bb7c1ecd205a81e66bd6f7"></a>

```c
#define BT_MESH_ADDR_FRIENDS 0xfffd
```

相关声明：[BT_MESH_ADDR_FRIENDS](#ga5d44892368bb7c1ecd205a81e66bd6f7)。

所有友元节点（All Friends）。

<a id="r_ga30d4975d25c2c120da1cbfadf29c098f"></a>

```c
#define BT_MESH_ADDR_PROXIES 0xfffc
```

相关声明：[BT_MESH_ADDR_PROXIES](#ga30d4975d25c2c120da1cbfadf29c098f)。

所有代理（All Proxies）。

<a id="r_gabf77d8365ddc278838fa450826e43243"></a>

```c
#define BT_MESH_ADDR_DFW_NODES 0xfffb
```

相关声明：[BT_MESH_ADDR_DFW_NODES](#gabf77d8365ddc278838fa450826e43243)。

所有定向转发节点（All Directed Forwarding Nodes）。

<a id="r_gafd70174e5072dbbfed31156f152aeaa1"></a>

```c
#define BT_MESH_ADDR_IP_NODES 0xfffa
```

相关声明：[BT_MESH_ADDR_IP_NODES](#gafd70174e5072dbbfed31156f152aeaa1)。

所有 IPT 节点（All IPT Nodes）。

<a id="r_ga1055381438e55e953dec2e6d592ab103"></a>

```c
#define BT_MESH_ADDR_IP_BR_ROUTERS 0xfff9
```

相关声明：[BT_MESH_ADDR_IP_BR_ROUTERS](#ga1055381438e55e953dec2e6d592ab103)。

所有 IPT 边界路由器（All IPT Border Routers）。

## 2.5\_预定义密钥索引（Predefined Key Indexes）

<a id="r_gace23095bac3705c2f2afab749e48c02d"></a>

```c
#define BT_MESH_KEY_UNUSED 0xffff
```

相关声明：[BT_MESH_KEY_UNUSED](#gace23095bac3705c2f2afab749e48c02d)。

密钥未使用（Key Unused）。

<a id="r_ga7718cce0713be98a08420c7eab1b40ee"></a>

```c
#define BT_MESH_KEY_ANY 0xffff
```

相关声明：[BT_MESH_KEY_ANY](#ga7718cce0713be98a08420c7eab1b40ee)。

任意密钥索引（Any Key Index）。

<a id="r_gabd37f17f3f5c3bc399ad3699df282675"></a>

```c
#define BT_MESH_KEY_DEV 0xfffe
```

相关声明：[BT_MESH_KEY_DEV](#gabd37f17f3f5c3bc399ad3699df282675)。

设备密钥（Device key）。

<a id="r_ga9c64b38f2a6879f4750e3e1828e8ab7a"></a>

```c
#define BT_MESH_KEY_DEV_LOCAL BT_MESH_KEY_DEV
```

相关声明：[BT_MESH_KEY_DEV_LOCAL](#ga9c64b38f2a6879f4750e3e1828e8ab7a)、[BT_MESH_KEY_DEV](#gabd37f17f3f5c3bc399ad3699df282675)。

本地设备密钥（Local Device Key）。

<a id="r_gaaa6ffb62df5d6d55c831d4d9860fc7eb"></a>

```c
#define BT_MESH_KEY_DEV_REMOTE 0xfffd
```

相关声明：[BT_MESH_KEY_DEV_REMOTE](#gaaa6ffb62df5d6d55c831d4d9860fc7eb)。

远端设备密钥（Remote Device Key）。

<a id="r_gace0a526534e31e8067daf283407533fd"></a>

```c
#define BT_MESH_KEY_DEV_ANY 0xfffc
```

相关声明：[BT_MESH_KEY_DEV_ANY](#gace0a526534e31e8067daf283407533fd)。

任意设备密钥（Any Device Key）。

## 2.6\_详细说明（Detailed Documentation）

<a id="ga27aafd100b6ccc1de060a75370184620"></a>

### `BT_MESH_ADDR_ALL_NODES`

```c
#define BT_MESH_ADDR_ALL_NODES 0xffff
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有节点（All Nodes）。

<a id="gabf77d8365ddc278838fa450826e43243"></a>

### `BT_MESH_ADDR_DFW_NODES`

```c
#define BT_MESH_ADDR_DFW_NODES 0xfffb
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有定向转发节点（All Directed Forwarding Nodes）。

<a id="ga5d44892368bb7c1ecd205a81e66bd6f7"></a>

### `BT_MESH_ADDR_FRIENDS`

```c
#define BT_MESH_ADDR_FRIENDS 0xfffd
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有友元节点（All Friends）。

<a id="ga1055381438e55e953dec2e6d592ab103"></a>

### `BT_MESH_ADDR_IP_BR_ROUTERS`

```c
#define BT_MESH_ADDR_IP_BR_ROUTERS 0xfff9
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有 IPT 边界路由器（All IPT Border Routers）。

<a id="gafd70174e5072dbbfed31156f152aeaa1"></a>

### `BT_MESH_ADDR_IP_NODES`

```c
#define BT_MESH_ADDR_IP_NODES 0xfffa
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有 IPT 节点（All IPT Nodes）。

<a id="gaff5ff58937924a1e6297aa1b20efc30f"></a>

### `BT_MESH_ADDR_IS_FIXED_GROUP`

```c
#define BT_MESH_ADDR_IS_FIXED_GROUP ( addr)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((addr) >= 0xff00 && (addr) < 0xffff)
```

检查蓝牙 Mesh 地址是否为固定组地址（Fixed Group Address）。

<a id="gab50cc8dca6f7ffd5420ef4fb38fbe224"></a>

### `BT_MESH_ADDR_IS_GROUP`

```c
#define BT_MESH_ADDR_IS_GROUP ( addr)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((addr) >= 0xc000 && (addr) < 0xff00)
```

检查蓝牙 Mesh 地址是否为组地址（Group Address）。

<a id="ga98ba7663259ca43cd5a38c7a9e16516d"></a>

### `BT_MESH_ADDR_IS_RFU`

```c
#define BT_MESH_ADDR_IS_RFU ( addr)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((addr) >= 0xff00 && (addr) <= 0xfff8)
```

检查蓝牙 Mesh 地址是否为保留供未来使用的地址（Reserved for Future Use，RFU）。

<a id="ga1a4694cccf834d71f0abe2a0283cb9a8"></a>

### `BT_MESH_ADDR_IS_UNICAST`

```c
#define BT_MESH_ADDR_IS_UNICAST ( addr)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((addr) && (addr) < 0x8000)
```

检查蓝牙 Mesh 地址是否为单播地址（Unicast Address）。

<a id="ga623eb2da2c880eec2107f36402ba6621"></a>

### `BT_MESH_ADDR_IS_VIRTUAL`

```c
#define BT_MESH_ADDR_IS_VIRTUAL ( addr)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((addr) >= 0x8000 && (addr) < 0xc000)
```

检查蓝牙 Mesh 地址是否为虚拟地址（Virtual Address）。

<a id="ga30d4975d25c2c120da1cbfadf29c098f"></a>

### `BT_MESH_ADDR_PROXIES`

```c
#define BT_MESH_ADDR_PROXIES 0xfffc
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有代理（All Proxies）。

<a id="ga5ee81d48846de9c9c966ffe0b90ff011"></a>

### `BT_MESH_ADDR_RELAYS`

```c
#define BT_MESH_ADDR_RELAYS 0xfffe
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

所有中继（All Relays）。

<a id="ga6d11790af686e6d48f08c6f1cd65317c"></a>

### `BT_MESH_ADDR_UNASSIGNED`

```c
#define BT_MESH_ADDR_UNASSIGNED 0x0000
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

未分配（Unassigned）。

<a id="gaa620c32d1dce8e4b691b7f4270016506"></a>

### `BT_MESH_APP_SEG_SDU_MAX`

```c
#define BT_MESH_APP_SEG_SDU_MAX 12
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

访问消息分段（Access Message Segment）的最大大小，单位为八位组（Octets）。

<a id="ga64eb6a94b1db9899c4f5bbf4cc88cd9f"></a>

### `BT_MESH_APP_UNSEG_SDU_MAX`

```c
#define BT_MESH_APP_UNSEG_SDU_MAX 15
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

未分段访问消息（Unsegmented Access Message）的最大载荷大小，单位为八位组（Octets）。

<a id="ga321a5091dabd4ec4beb5396db6cabf44"></a>

### `BT_MESH_ELEM`

```c
#define BT_MESH_ELEM ( _loc, _mods, _vnd_mods )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
{                                                                       \
        .rt               = &(struct bt_mesh_elem_rt_ctx) { 0 },        \
        .loc              = (_loc),                                     \
        .model_count      = ARRAY_SIZE(_mods),                          \
        .vnd_model_count  = ARRAY_SIZE(_vnd_mods),                      \
        .models           = (_mods),                                    \
        .vnd_models       = (_vnd_mods),                                \
}
```

用于在数组中定义 Mesh 元素（Element）的辅助宏。

若元素没有 SIG 模型或厂商模型（Vendor Model），可改用辅助宏 `BT_MESH_MODEL_NONE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 位置描述符（Location Descriptor）。 |
| `_mods` | 模型数组（Array of Models）。 |
| `_vnd_mods` | 厂商模型数组（Array of Vendor Models）。 |

<a id="gac4aafa0bdd24fb51d515a62e83917936"></a>

### `BT_MESH_IS_DEV_KEY`

```c
#define BT_MESH_IS_DEV_KEY ( key)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(key == BT_MESH_KEY_DEV_LOCAL || \
key == BT_MESH_KEY_DEV_REMOTE)
```

检查蓝牙 Mesh 密钥是否为设备密钥（Device Key）。

<a id="ga7718cce0713be98a08420c7eab1b40ee"></a>

### `BT_MESH_KEY_ANY`

```c
#define BT_MESH_KEY_ANY 0xffff
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

任意密钥索引（Any Key Index）。

<a id="gabd37f17f3f5c3bc399ad3699df282675"></a>

### `BT_MESH_KEY_DEV`

```c
#define BT_MESH_KEY_DEV 0xfffe
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

设备密钥（Device key）。

<a id="gace0a526534e31e8067daf283407533fd"></a>

### `BT_MESH_KEY_DEV_ANY`

```c
#define BT_MESH_KEY_DEV_ANY 0xfffc
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

任意设备密钥（Any Device Key）。

<a id="ga9c64b38f2a6879f4750e3e1828e8ab7a"></a>

### `BT_MESH_KEY_DEV_LOCAL`

```c
#define BT_MESH_KEY_DEV_LOCAL BT_MESH_KEY_DEV
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

本地设备密钥（Local Device Key）。

<a id="gaaa6ffb62df5d6d55c831d4d9860fc7eb"></a>

### `BT_MESH_KEY_DEV_REMOTE`

```c
#define BT_MESH_KEY_DEV_REMOTE 0xfffd
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

远端设备密钥（Remote Device Key）。

<a id="gace23095bac3705c2f2afab749e48c02d"></a>

### `BT_MESH_KEY_UNUSED`

```c
#define BT_MESH_KEY_UNUSED 0xffff
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

密钥未使用（Key Unused）。

<a id="ga637e1be0298dc681414645867b28b59f"></a>

### `BT_MESH_LEN_EXACT`

```c
#define BT_MESH_LEN_EXACT ( len)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(-len)
```

为定长消息编码确切消息长度（Exact Message Length）的宏。

<a id="ga691ed9b3ab3ddaceda0f81c4a715ab3a"></a>

### `BT_MESH_LEN_MIN`

```c
#define BT_MESH_LEN_MIN ( len)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(len)
```

为变长消息编码最小消息长度（Minimum Message Length）的宏。

<a id="gae694f5ac7ef9f0de37aaba846443586f"></a>

### `BT_MESH_MODEL`

```c
#define BT_MESH_MODEL ( _id, _op, _pub, _user_data )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, NULL)
```

组成数据（Composition Data）中的 SIG 模型条目。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |

<a id="gac062c101b7310020e11a527de9c40d3a"></a>

### `BT_MESH_MODEL_CB`

```c
#define BT_MESH_MODEL_CB ( _id, _op, _pub, _user_data, _cb )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CNT_CB(_id, _op, _pub, _user_data,        \
                     CONFIG_BT_MESH_MODEL_KEY_COUNT,    \
                     CONFIG_BT_MESH_MODEL_GROUP_COUNT, _cb)
```

组成数据（Composition Data）中的 SIG 模型条目，带回调函数。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |

<a id="ga925da443eb15a4c1980d48a69388dc2c"></a>

### `BT_MESH_MODEL_CNT_CB`

```c
#define BT_MESH_MODEL_CNT_CB ( _id, _op, _pub, _user_data, _keys, _grps, _cb )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
{                                                                               \
        .id = (_id),                                                            \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                                  \
        .pub = _pub,                                                            \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(_keys),                 \
        .keys_cnt = _keys,                                                      \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(_grps),         \
        .groups_cnt = _grps,                                                    \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                        \
        .op = _op,                                                              \
        .cb = _cb,                                                              \
}
```

组成数据（Composition Data）中的 SIG 模型条目，带回调函数，且指定密钥和组的数量。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_keys` | 可绑定到模型的密钥数量，不得超过 `CONFIG_BT_MESH_MODEL_KEY_COUNT`。 |
| `_grps` | 模型可订阅的地址数量，不得超过 `CONFIG_BT_MESH_MODEL_GROUP_COUNT`。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |

<a id="ga32733dccd9329aa938dc0bd21cf9beae"></a>

### `BT_MESH_MODEL_CNT_VND_CB`

```c
#define BT_MESH_MODEL_CNT_VND_CB ( _company, _id, _op, _pub, _user_data, _keys, _grps, _cb )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
{                                                                                               \
        .vnd.company = (_company),                                                              \
        .vnd.id = (_id),                                                                        \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                                                  \
        .op = _op,                                                                              \
        .pub = _pub,                                                                            \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(_keys),                                 \
        .keys_cnt = _keys,                                                                      \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(_grps),                         \
        .groups_cnt = _grps,                                                                    \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                                        \
        .cb = _cb,                                                                              \
}
```

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数，且指定密钥和组的数量。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_company` | 公司标识符（Company ID）。 |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_keys` | 可绑定到模型的密钥数量，不得超过 `CONFIG_BT_MESH_MODEL_KEY_COUNT`。 |
| `_grps` | 模型可订阅的地址数量，不得超过 `CONFIG_BT_MESH_MODEL_GROUP_COUNT`。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |

<a id="ga40204b4ccaa819a487de168bcf66c98f"></a>

### `BT_MESH_MODEL_METADATA_CB`

```c
#define BT_MESH_MODEL_METADATA_CB ( _id, _op, _pub, _user_data, _cb, _metadata )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, _cb)
```

组成数据（Composition Data）中的 SIG 模型条目，带回调函数和元数据（Metadata）。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |
| `_metadata` | 元数据结构体（Metadata Structure）。启用 `CONFIG_BT_MESH_LARGE_COMP_DATA_SRV` 时使用。 |

<a id="gae6d55e0a27bb7c448affd312a2e11656"></a>

### `BT_MESH_MODEL_NO_OPS`

```c
#define BT_MESH_MODEL_NO_OPS
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((struct bt_mesh_model_op []) \
{ BT_MESH_MODEL_OP_END })
```

用于定义空操作码列表（Empty Opcode List）的辅助宏。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

<a id="gab0ad2aab95d49e5b60fe8dafd69132a4"></a>

### `BT_MESH_MODEL_NONE`

```c
#define BT_MESH_MODEL_NONE ((const struct bt_mesh_model []){})
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

用于定义空模型数组（Empty Model Array）的辅助宏。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

<a id="ga00915cfdff7dc0646f24d6b06e124d0d"></a>

### `BT_MESH_MODEL_OP_1`

```c
#define BT_MESH_MODEL_OP_1 ( b0)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(b0)
```

编码 1 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="gaa52a40ef5972c4f34cf5ff5a10e21289"></a>

### `BT_MESH_MODEL_OP_2`

```c
#define BT_MESH_MODEL_OP_2 ( b0, b1 )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(((b0) << 8) | (b1))
```

编码 2 字节操作码（Opcode）的宏，用于蓝牙 SIG 定义的模型。

<a id="ga72d1d19701be52f5eac6af475f9b19a9"></a>

### `BT_MESH_MODEL_OP_3`

```c
#define BT_MESH_MODEL_OP_3 ( b0, cid )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((((b0) << 16) | 0xc00000) | (cid))
```

编码 3 字节操作码（Opcode）的宏，用于厂商特定消息（Vendor-Specific Message）。

<a id="gaf2c164506c601214c85d451747176827"></a>

### `BT_MESH_MODEL_OP_END`

```c
#define BT_MESH_MODEL_OP_END { 0, 0, NULL }
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

操作码列表（Opcode List）的结束项。

必须始终存在。

<a id="ga8334ff2da1f0dc3ab2fc914059c33622"></a>

### `BT_MESH_MODEL_PUB_DEFINE`

```c
#define BT_MESH_MODEL_PUB_DEFINE ( _name, _update, _msg_len )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
NET_BUF_SIMPLE_DEFINE_STATIC(bt_mesh_pub_msg_##_name, _msg_len); \
static struct bt_mesh_model_pub _name = { \
        .msg = &bt_mesh_pub_msg_##_name, \
        .update = _update, \
}
```

定义模型发布上下文（Model Publication Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 为上下文（Context）指定的变量名。 |
| `_update` | 可选的消息更新回调（Message Update Callback），可为 `NULL`。 |
| `_msg_len` | 发布消息（Publication Message）的长度。 |

<a id="ga3759c8c88db48be662bf2511ff514edd"></a>

### `BT_MESH_MODEL_VND`

```c
#define BT_MESH_MODEL_VND ( _company, _id, _op, _pub, _user_data )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, NULL)
```

组成数据（Composition Data）中的厂商模型（Vendor Model）条目。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_company` | 公司标识符（Company ID）。 |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |

<a id="gabe79d914990ba2721f5bb7081910e512"></a>

### `BT_MESH_MODEL_VND_CB`

```c
#define BT_MESH_MODEL_VND_CB ( _company, _id, _op, _pub, _user_data, _cb )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CNT_VND_CB(_company, _id, _op, _pub, _user_data,  \
                         CONFIG_BT_MESH_MODEL_KEY_COUNT,        \
                         CONFIG_BT_MESH_MODEL_GROUP_COUNT, _cb)
```

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_company` | 公司标识符（Company ID）。 |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |

<a id="gac62334962dcbe3a75a03ce5744b326d8"></a>

### `BT_MESH_MODEL_VND_METADATA_CB`

```c
#define BT_MESH_MODEL_VND_METADATA_CB ( _company, _id, _op, _pub, _user_data, _cb, _metadata )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, _cb)
```

组成数据（Composition Data）中的厂商模型（Vendor Model）条目，带回调函数和元数据（Metadata）。

此宏使用 C99 标准的复合字面量（Compound Literal）功能，因此仅可用于 C，不能用于 C++。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_company` | 公司标识符（Company ID）。 |
| `_id` | 模型标识符（Model ID）。 |
| `_op` | 模型操作码处理函数数组（Model Opcode Handlers）。 |
| `_pub` | 模型发布参数（Model Publish Parameters）。 |
| `_user_data` | 模型的用户数据（User Data）。 |
| `_cb` | 回调结构体（Callback Structure）；设为 `NULL` 则不保留回调。 |
| `_metadata` | 元数据结构体（Metadata Structure）。启用 `CONFIG_BT_MESH_LARGE_COMP_DATA_SRV` 时使用。 |

<a id="gaab5fe51071f6e54debd9136ac6a70a49"></a>

### `BT_MESH_MODELS_METADATA_END`

```c
#define BT_MESH_MODELS_METADATA_END { 0, 0, NULL }
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

模型元数据列表（Models Metadata List）的结束项。

必须始终存在。

<a id="gaa2587adac719c50c311ae41c548b853c"></a>

### `BT_MESH_MODELS_METADATA_ENTRY`

```c
#define BT_MESH_MODELS_METADATA_ENTRY ( _len, _id, _data )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
{                                                                      \
        .len = (_len), .id = _id, .data = _data,                       \
}
```

初始化列表中的模型元数据条目结构体（Models Metadata Entry Structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_len` | 元数据条目（Metadata Entry）的长度。 |
| `_id` | 模型元数据条目（Models Metadata Entry）的 ID。 |
| `_data` | 指向包含元数据（Metadata）的连续内存的指针。 |

<a id="ga56b518123ab47cb3ae4a249f471ae556"></a>

### `BT_MESH_MODELS_METADATA_NONE`

```c
#define BT_MESH_MODELS_METADATA_NONE NULL
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

用于定义空模型元数据数组（Models Metadata Array）的辅助宏。

<a id="ga115ee29aba3c3e985aa11d6692ca0d83"></a>

### `BT_MESH_PUB_MSG_NUM`

```c
#define BT_MESH_PUB_MSG_NUM ( pub)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(BT_MESH_PUB_TRANSMIT_COUNT((pub)->retransmit) + 1 - (pub)->count)
```

获取消息在一个发布间隔（Publication Interval）内的序号。

预期在 `bt_mesh_model_pub::update` 中使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pub` | 模型发布（Model Publication）的上下文。 |

**返回（Returns）**：返回值（Returns）：从 1 开始的消息序号。

<a id="ga230538bb39ac3d6c8c0327d1fad77e69"></a>

### `BT_MESH_PUB_MSG_TOTAL`

```c
#define BT_MESH_PUB_MSG_TOTAL ( pub)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(BT_MESH_PUB_TRANSMIT_COUNT((pub)->retransmit) + 1)
```

获取一个发布间隔（Publication Interval）内的消息总数，包括首次发布。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pub` | 模型发布（Model Publication）的上下文。 |

**返回（Returns）**：返回值（Returns）：消息总数。

<a id="ga19208dea7bab9f31c2c793ef6201dd91"></a>

### `BT_MESH_PUB_TRANSMIT`

```c
#define BT_MESH_PUB_TRANSMIT ( count, int_ms )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_TRANSMIT(count,           \
(int_ms) / 5)
```

编码发布重传次数（Publish Retransmit Count）和间隔步数（Interval Steps）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `count` | 重传次数（Number of Retransmissions），不包括首次发送。 |
| `int_ms` | 间隔步长（Interval Steps），单位为毫秒。必须大于 0，且为 50 的整数倍。 |

**返回（Returns）**：返回值（Returns）：Mesh 发送值（Transmit Value），例如可用于配置模型数据的默认值。

<a id="ga13986422dda5edce4f5fb1ce387093e3"></a>

### `BT_MESH_PUB_TRANSMIT_COUNT`

```c
#define BT_MESH_PUB_TRANSMIT_COUNT ( transmit)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
BT_MESH_TRANSMIT_COUNT(transmit)
```

从给定值中解码发布重传次数（Publish Retransmit Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transmit` | 已编码的发布重传次数与间隔值（Publish Retransmit Count and Interval Value）。 |

**返回（Returns）**：返回值（Returns）：重传次数；实际发送次数为 `N + 1`。

<a id="gaac954956dd3913dd7ad2b93a2566afd9"></a>

### `BT_MESH_PUB_TRANSMIT_INT`

```c
#define BT_MESH_PUB_TRANSMIT_INT ( transmit)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((((transmit) >> 3) + 1) * 50)
```

从给定值中解码发布重传间隔（Publish Retransmit Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transmit` | 已编码的发布重传次数与间隔值（Publish Retransmit Count and Interval Value）。 |

**返回（Returns）**：返回值（Returns）：发送间隔（Transmission Interval），单位为毫秒。

<a id="ga36f299f2fc13892b5a7d871dad1ec9ce"></a>

### `BT_MESH_RX_SDU_MAX`

```c
#define BT_MESH_RX_SDU_MAX
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
 MAX((BT_MESH_RX_SEG_MAX *                \
 BT_MESH_APP_SEG_SDU_MAX),        \
BT_MESH_APP_UNSEG_SDU_MAX)
```

接收访问消息（Incoming Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="ga18756e939ec3b312eef5c3dc9fd70270"></a>

### `BT_MESH_RX_SEG_MAX`

```c
#define BT_MESH_RX_SEG_MAX 0
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

接收消息所支持的最大分段数量（Number of Segments）。

<a id="gaff82bf652232fbce71c31f38a10577a9"></a>

### `BT_MESH_TRANSMIT`

```c
#define BT_MESH_TRANSMIT ( count, int_ms )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((uint8_t)((count) | (((int_ms / 10) - 1) << 3)))
```

编码发送次数（Transmission Count）和间隔步数（Interval Steps）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `count` | 重传次数（Number of Retransmissions），不包括首次发送。 |
| `int_ms` | 间隔步长（Interval Steps），单位为毫秒。必须大于 0、小于或等于 320，且为 10 的整数倍。 |

**返回（Returns）**：返回值（Returns）：Mesh 发送值（Transmit Value），例如可用于配置模型数据的默认值。

<a id="ga62fda0d731241efbaa4827e4eb9d1795"></a>

### `BT_MESH_TRANSMIT_COUNT`

```c
#define BT_MESH_TRANSMIT_COUNT ( transmit)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
(((transmit) & (uint8_t)BIT_MASK(3)))
```

从发送值（Transmit Value）中解码发送次数（Transmit Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transmit` | 已编码的发送次数与间隔值（Transmit Count and Interval Value）。 |

**返回（Returns）**：返回值（Returns）：发送计数；实际发送次数为 `N + 1`。

<a id="ga2aa21171c5677d23ad0c472291639417"></a>

### `BT_MESH_TRANSMIT_INT`

```c
#define BT_MESH_TRANSMIT_INT ( transmit)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
((((transmit) >> 3) + 1) * 10)
```

从发送值（Transmit Value）中解码发送间隔（Transmit Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transmit` | 已编码的发送次数与间隔值（Transmit Count and Interval Value）。 |

**返回（Returns）**：返回值（Returns）：发送间隔（Transmission Interval），单位为毫秒。

<a id="ga16516272b42420263b1c47c3ea16c0c8"></a>

### `BT_MESH_TTL_DEFAULT`

```c
#define BT_MESH_TTL_DEFAULT 0xff
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

特殊生存时间（Time To Live，TTL）值，用于请求使用已配置的默认 TTL。

<a id="ga071e85e929589d31bf876e2e09cf2f19"></a>

### `BT_MESH_TTL_MAX`

```c
#define BT_MESH_TTL_MAX 0x7f
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

允许的最大生存时间（TTL）值。

<a id="ga86d7386603ecd89952b6d540ea4243c2"></a>

### `BT_MESH_TX_SDU_MAX`

```c
#define BT_MESH_TX_SDU_MAX
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

展开值（Value）：

```c
 MAX((BT_MESH_TX_SEG_MAX *                \
 BT_MESH_APP_SEG_SDU_MAX),        \
BT_MESH_APP_UNSEG_SDU_MAX)
```

发送访问消息（Outgoing Access Message）可能具有的最大载荷大小，单位为八位组（Octets）。

<a id="ga1b2a3610ac370266578abce195e65fa2"></a>

### `BT_MESH_TX_SEG_MAX`

```c
#define BT_MESH_TX_SEG_MAX 0
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

发送消息所支持的最大分段数量（Number of Segments）。

<a id="ga8445c550a47dba16e3fa6fea36d6d9fc"></a>

### `bt_mesh_comp2_register()`

```c
int bt_mesh_comp2_register ( const struct bt_mesh_comp2 * comp2)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

注册设备的组成数据（Composition Data）第 2 页。

为设备的组成数据第 2 页（Composition Data Page 2）注册 Mesh 配置文件信息（Mesh Profiles），参见 Bluetooth SIG Assigned Numbers 第 3.12 节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `comp2` | 指向组成数据第 2 页（Composition Data Page 2）的指针。 |

**说明（Note）**：注（Note）：`comp2` 中必须至少存在一条记录。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga8575f680e77d86d6c85cac27985b9f3c"></a>

### `bt_mesh_comp_change_prepare()`

```c
int bt_mesh_comp_change_prepare ( void )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

指示组成数据（Composition Data）将在下次启动时改变。

告知配置服务器（Config Server），组成数据（Composition Data）预期将在下次启动时改变，因此应备份当前组成数据。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga03ce9f6f9ccf734ea72beede09288923"></a>

### `bt_mesh_model_correspond()`

```c
int bt_mesh_model_correspond ( const struct bt_mesh_model * corresponding_mod, const struct bt_mesh_model * base_mod )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

使一个模型与另一个模型建立对应关系（Correspond）。

Mesh 模型可互相对应（Correspondence），即其中一个模型存在时，另一个也必须存在。一个 Mesh 模型可与任意元素中的任意数量模型对应。通过对应关系连接在一起的所有模型形成一个对应组（Correspondence Group），该组具有唯一的对应 ID（Correspondence ID）。对应关系信息用于构建组成数据第 1 页（Composition Data Page 1）。

调用此函数时，`base_mod` 必须已经初始化。由于此函数设计为在 `corresponding_mod` 的初始化器中调用，因此 `base_mod` 必须先于 `corresponding_mod` 初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `corresponding_mod` | 与基础模型（Base Model）相对应的 Mesh 模型。 |
| `base_mod` | 作为对应目标的模型。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功保存与 `base_mod` 模型的对应关系（Correspondence）。 |
| `-ENOMEM` | 没有更多空间保存此关系。 |
| `-ENOTSUP` | 不支持组成数据第 1 页（Composition Data Page 1）。 |

<a id="gadff0895c5c34928d778fa615512b3d85"></a>

### `bt_mesh_model_data_store()`

```c
int bt_mesh_model_data_store ( const struct bt_mesh_model * mod, bool vnd, const char * name, const void * data, size_t data_len )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

立即将模型的用户数据保存到持久存储（Persistent Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mod` | Mesh 模型（Model）。 |
| `vnd` | 这是厂商模型（Vendor Model）。 |
| `name` | 设置项（Settings Item）的名称／键。最多仅使用 `SETTINGS_MAX_DIR_DEPTH` 字节。 |
| `data` | 要存储的模型数据（Model Data）；传入 `NULL` 可删除模型数据。 |
| `data_len` | 模型数据的长度。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga762896dd2e806b5be061b220d53ce4db"></a>

### `bt_mesh_model_data_store_schedule()`

```c
void bt_mesh_model_data_store_schedule ( const struct bt_mesh_model * mod)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

安排将模型的用户数据保存到持久存储（Persistent Storage）。

此函数在 `CONFIG_BT_MESH_STORE_TIMEOUT` 定义的延迟之后，触发对应模型的 `bt_mesh_model_cb::pending_store` 回调。

此延迟对所有模型全局共享。一旦安排了回调，在上一次安排完成前就不能重新安排。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mod` | Mesh 模型（Model）。 |

<a id="ga8edba04af103fb11994d4d3e558ec4fb"></a>

### `bt_mesh_model_elem()`

```c
const struct bt_mesh_elem * bt_mesh_model_elem ( const struct bt_mesh_model * mod)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

获取模型所属的元素（Element）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mod` | Mesh 模型（Model）。 |

**返回（Returns）**：返回值（Returns）：指向给定模型所属元素（Element）的指针。

<a id="gaf6356f715c8968151b8d539f2dd1880c"></a>

### `bt_mesh_model_extend()`

```c
int bt_mesh_model_extend ( const struct bt_mesh_model * extending_mod, const struct bt_mesh_model * base_mod )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

使一个模型扩展（Extend）另一个模型。

可以通过扩展（Extend）Mesh 模型来复用其功能，形成更复杂的模型。一个 Mesh 模型可扩展任意元素中的任意数量模型。扩展还可以嵌套，即扩展了其他模型的模型本身也可被扩展。

一组互相扩展的模型形成模型扩展列表（Model Extension List）。

扩展列表中的所有模型在每个元素内共享一个订阅列表（Subscription List）。访问层（Access Layer）将利用同一扩展列表、同一元素中所有模型合并后的订阅列表，从而扩大这些模型的订阅列表容量。

若启用 `CONFIG_BT_MESH_COMP_PAGE_1`，在两个模型的 `bt_mesh_model_cb::init` 回调均被调用之前，不允许调用此函数；但在最后一个初始化回调内部调用除外。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `extending_mod` | 正在扩展基础模型（Base Model）的 Mesh 模型。 |
| `base_mod` | 被扩展的模型。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功扩展 `base_mod` 模型。 |

<a id="gaf0510f9511d72f1d4fd07f865753a50a"></a>

### `bt_mesh_model_find()`

```c
const struct bt_mesh_model * bt_mesh_model_find ( const struct bt_mesh_elem * elem, uint16_t id )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

查找 SIG 模型（SIG Model）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 要在其中查找模型的元素（Element）。 |
| `id` | 模型的模型 ID（Model ID）。 |

**返回（Returns）**：返回值（Returns）：指向与给定参数匹配的 Mesh 模型的指针；给定元素中不存在指定 ID 的 SIG 模型时，为 `NULL`。

<a id="gadfb473db4b23902a192e12d322ff1fd2"></a>

### `bt_mesh_model_find_vnd()`

```c
const struct bt_mesh_model * bt_mesh_model_find_vnd ( const struct bt_mesh_elem * elem, uint16_t company, uint16_t id )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

查找厂商模型（Vendor Model）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 要在其中查找模型的元素（Element）。 |
| `company` | 模型的公司 ID（Company ID）。 |
| `id` | 模型的模型 ID（Model ID）。 |

**返回（Returns）**：返回值（Returns）：指向与给定参数匹配的 Mesh 模型的指针；给定元素中不存在指定 ID 的厂商模型（Vendor Model）时，为 `NULL`。

<a id="gaa8694fdab3f514d8051dad1cc7362ac9"></a>

### `bt_mesh_model_in_primary()`

```c
bool bt_mesh_model_in_primary ( const struct bt_mesh_model * mod)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

获取模型是否位于设备的主元素（Primary Element）中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mod` | Mesh 模型（Model）。 |

**返回（Returns）**：返回值（Returns）：模型位于主元素（Primary Element）时为 `true`，否则为 `false`。

<a id="ga10603a5846210a397f306b227ce10c2e"></a>

### `bt_mesh_model_is_extended()`

```c
bool bt_mesh_model_is_extended ( const struct bt_mesh_model * model)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

检查模型是否被另一个模型扩展（Extended）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要检查的模型（Model）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 模型被另一个模型扩展时为真，否则为 `false`。 |

<a id="ga1b961d45f8b7c231c698ca229115e434"></a>

### `bt_mesh_model_pub_is_retransmission()`

```c
bool bt_mesh_model_pub_is_retransmission ( const struct bt_mesh_model * model)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

检查消息是否正在重传（Retransmitted）。

预期在 `bt_mesh_model_pub::update` 回调中使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 支持发布（Publication）的 Mesh 模型。 |

**返回（Returns）**：返回值（Returns）：此次是重传（Retransmission）时为 `true`；首次发布时为 `false`。

<a id="ga06644f8a5fa43351328d3f3403dbad03"></a>

### `bt_mesh_model_publish()`

```c
int bt_mesh_model_publish ( const struct bt_mesh_model * model)
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

发送模型发布消息（Model Publication Message）。

调用此函数之前，用户须确保模型发布消息 `bt_mesh_model_pub::msg` 中包含有效的待发送消息。注意，此 API 仅用于非周期性发布（Non-Periodic Publishing）。对于周期性发布（Periodic Publishing），应用只需确保每次调用 `bt_mesh_model_pub::update` 回调时，`bt_mesh_model_pub::msg` 都包含有效消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 正在发布消息的 Mesh 客户端模型（Client Model）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga7cac052ef76f4b37a95343329b078e77"></a>

### `bt_mesh_model_send()`

```c
int bt_mesh_model_send ( const struct bt_mesh_model * model, struct bt_mesh_msg_ctx * ctx, struct net_buf_simple * msg, const struct bt_mesh_send_cb * cb, void * cb_data )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

发送访问层消息（Access Layer Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 消息所属的 Mesh 客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context），包括密钥、TTL 等。 |
| `msg` | 访问层载荷（Access Layer Payload），即实际要发送的消息。 |
| `cb` | 可选的“消息已发送”回调（Message Sent Callback）。 |
| `cb_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga26ac86bdd32d27e0091735d98670687a"></a>

### `bt_mesh_models_metadata_change_prepare()`

```c
int bt_mesh_models_metadata_change_prepare ( void )
```

```c
#include <zephyr/bluetooth/mesh/access.h>
```

指示元数据（Metadata）将在下次启动时改变。

告知配置服务器（Config Server），模型元数据（Models Metadata）预期将在下次启动时改变，因此应备份当前模型元数据。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 2.7\_原页交叉引用（Cross References）

- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)
- [bt_mesh_models_metadata_entry](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)
- [bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)
- [bt_mesh_comp2_record](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md)
- [bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/mesh/access.h](../api_file_mesh_acpi_reference/P001_zephyr__bluetooth__mesh__access.h_文件参考.md)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [BT_MESH_MODEL_RUNTIME_INIT](../api_file_mesh_acpi_reference/P001_zephyr__bluetooth__mesh__access.h_文件参考.md#ad28c5301ea6cf93f3bf2a672043cae4e)
- [CONFIG_BT_MESH_MODEL_KEY_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_KEY_COUNT)
- [CONFIG_BT_MESH_MODEL_GROUP_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_GROUP_COUNT)
- [CONFIG_BT_MESH_LARGE_COMP_DATA_SRV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV)
- [NET_BUF_SIMPLE_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga21ced8b3082d57bf071008de5fffc0f4)
- [update](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a0354344e08e633dc4d6c0b4e7b169080)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [SETTINGS_MAX_DIR_DEPTH](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga2afa32b032e88a188c5263156d9e73e1)
- [bt_mesh_model_cb::pending_store](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#ae28f875dffc7f5f2ce99abe590369f43)
- [CONFIG_BT_MESH_STORE_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_STORE_TIMEOUT)
- [CONFIG_BT_MESH_COMP_PAGE_1](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_COMP_PAGE_1)
- [bt_mesh_model_cb::init](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a1688a2c6d7b3b17ba49a0975b6f4f68e)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [bt_mesh_model_pub::msg](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a5f5639c01d3704ec3d527c418d35f827)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__bt__mesh__access_html_ga9c64b38f2a6879f4750e3e1828e8ab7a"></a>
<a id="agroup__bt__mesh__access_html_gaaa6ffb62df5d6d55c831d4d9860fc7eb"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="agroup__bt__mesh__access_html_ga925da443eb15a4c1980d48a69388dc2c"></a>
<a id="aaccess_8h_html_ad28c5301ea6cf93f3bf2a672043cae4e"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="agroup__bt__mesh__access_html_gaf2c164506c601214c85d451747176827"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="agroup__net__buf_html_ga21ced8b3082d57bf071008de5fffc0f4"></a>
<a id="astructbt__mesh__model__pub_html"></a>
<a id="astructbt__mesh__model__pub_html_a0354344e08e633dc4d6c0b4e7b169080"></a>
<a id="agroup__bt__mesh__access_html_gabe79d914990ba2721f5bb7081910e512"></a>
<a id="agroup__bt__mesh__access_html_ga32733dccd9329aa938dc0bd21cf9beae"></a>
<a id="agroup__bt__mesh__access_html_ga13986422dda5edce4f5fb1ce387093e3"></a>
<a id="agroup__bt__mesh__access_html_gaff82bf652232fbce71c31f38a10577a9"></a>
<a id="agroup__bt__mesh__access_html_ga62fda0d731241efbaa4827e4eb9d1795"></a>
<a id="agroup__bt__mesh__access_html_ga18756e939ec3b312eef5c3dc9fd70270"></a>
<a id="agroup__bt__mesh__access_html_ga64eb6a94b1db9899c4f5bbf4cc88cd9f"></a>
<a id="agroup__bt__mesh__access_html_gaa620c32d1dce8e4b691b7f4270016506"></a>
<a id="agroup__sys-util_html_gafa99ec4acc4ecb2dc3c2d05da15d0e3f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="agroup__bt__mesh__access_html_ga1b2a3610ac370266578abce195e65fa2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_生物识别（Biometrics）.md) · [返回大纲](大纲.md) · [下一章](P003_LSM9DS1 API主题.md)
