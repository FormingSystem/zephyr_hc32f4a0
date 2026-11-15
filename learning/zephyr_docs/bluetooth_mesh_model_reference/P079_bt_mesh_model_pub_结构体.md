---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-79
title: bt_mesh_model_pub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_bt\_mesh\_model\_pub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模型发布（Model Publication）的上下文。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

模型发布上下文（Model publication context）。主要应使用 `BT_MESH_MODEL_PUB_DEFINE` 宏创建此上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_aa5026299082b3013740c7e36c01f91f5"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#aa5026299082b3013740c7e36c01f91f5)。

此上下文所属的模型（Model）。

<a id="r_a408c9185168b962f7e7314f9a429fe8c"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a408c9185168b962f7e7314f9a429fe8c)。

发布地址（Publish Address）。

<a id="r_abea9c2085c9d2e1e2fc71f03dd323ee7"></a>

```c
const uint8_t * uuid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#abea9c2085c9d2e1e2fc71f03dd323ee7)。

发布地址为虚拟地址（Virtual Address）时使用的标签通用唯一标识符（Label UUID）。

<a id="r_a0ad1809fe74930c9b36b32516a8d146f"></a>

```c
uint16_t key:12
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[key](#a0ad1809fe74930c9b36b32516a8d146f)。

发布所用的应用密钥索引（Publish AppKey Index）。

<a id="r_a3617adb0c1192419bdac2ad0f37199ac"></a>

```c
uint16_t cred:1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cred](#a3617adb0c1192419bdac2ad0f37199ac)。

友谊关系凭据标志（Friendship Credentials Flag）。

<a id="r_ab704aedcfd06d374615ef18c6ecc84a9"></a>

```c
uint16_t send_rel:1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[send_rel](#ab704aedcfd06d374615ef18c6ecc84a9)。

强制可靠发送（Reliable sending），即使用分段确认（Segment acknowledgments）。

<a id="r_abdbdc3bbc5d4ac5a5d606b55bb2d50ee"></a>

```c
uint16_t fast_period:1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fast_period](#abdbdc3bbc5d4ac5a5d606b55bb2d50ee)。

使用快速周期除数（FastPeriodDivisor）。

<a id="r_a16c13e46c012ab836acd02b8fe5f05e3"></a>

```c
uint16_t retr_update:1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[retr_update](#a16c13e46c012ab836acd02b8fe5f05e3)。

每次重传（Retransmission）时调用更新回调（Update callback）。

<a id="r_a820b713aaa1e0c33a4a59c80f805e854"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a820b713aaa1e0c33a4a59c80f805e854)。

发布生存时间（Publish Time to Live）。

<a id="r_a3d93d44ff85243dc94e7b4d36cde5b97"></a>

```c
uint8_t retransmit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retransmit](#a3d93d44ff85243dc94e7b4d36cde5b97)。

重传次数及间隔步数（Retransmit Count & Interval Steps）。

<a id="r_ae550510e9ca45f8c9fd9802e4e7e0f3d"></a>

```c
uint8_t period
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[period](#ae550510e9ca45f8c9fd9802e4e7e0f3d)。

发布周期（Publish Period）。

<a id="r_a4f2ce8727ffb44f564d1dc0615ebcadf"></a>

```c
uint8_t period_div:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[period_div](#a4f2ce8727ffb44f564d1dc0615ebcadf)。

周期除数（Period Divisor）。

<a id="r_a4e211c851bf91a9b43f035d435e9c93c"></a>

```c
uint8_t count:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[count](#a4e211c851bf91a9b43f035d435e9c93c)。

剩余发送次数（Transmissions left）。

<a id="r_a23a865dbd2dce5c1af074097864611e9"></a>

```c
uint8_t delayable:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[delayable](#a23a865dbd2dce5c1af074097864611e9)。

发布时使用随机延迟（Random delay）。

<a id="r_ab6e00714ea899eb32873d10b0908d278"></a>

```c
uint32_t period_start
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[period_start](#ab6e00714ea899eb32873d10b0908d278)。

当前周期的开始时刻（Start of current period）。

<a id="r_a5f5639c01d3704ec3d527c418d35f827"></a>

```c
struct net_buf_simple * msg
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[msg](#a5f5639c01d3704ec3d527c418d35f827)。

包含发布消息的发布缓冲区（Publication buffer）。

<a id="r_a0354344e08e633dc4d6c0b4e7b169080"></a>

```c
int(* update )(const struct bt_mesh_model *mod)
```

相关声明：[update](#a0354344e08e633dc4d6c0b4e7b169080)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#aa5026299082b3013740c7e36c01f91f5)。

用于更新发布缓冲区（Publication buffer）的回调。

<a id="r_af3771432d13805710e94f013332e8214"></a>

```c
struct k_work_delayable timer
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[timer](#af3771432d13805710e94f013332e8214)。

发布周期定时器（Publish Period Timer）。

## 79.2\_详细说明（Detailed Documentation）

<a id="a408c9185168b962f7e7314f9a429fe8c"></a>

### `addr`

```c
uint16_t bt_mesh_model_pub::addr
```

发布地址（Publish Address）。

<a id="a4e211c851bf91a9b43f035d435e9c93c"></a>

### `count`

```c
uint8_t bt_mesh_model_pub::count
```

剩余发送次数（Transmissions left）。

<a id="a3617adb0c1192419bdac2ad0f37199ac"></a>

### `cred`

```c
uint16_t bt_mesh_model_pub::cred
```

友谊关系凭据标志（Friendship Credentials Flag）。

<a id="a23a865dbd2dce5c1af074097864611e9"></a>

### `delayable`

```c
uint8_t bt_mesh_model_pub::delayable
```

发布时使用随机延迟（Random delay）。

<a id="abdbdc3bbc5d4ac5a5d606b55bb2d50ee"></a>

### `fast_period`

```c
uint16_t bt_mesh_model_pub::fast_period
```

使用快速周期除数（FastPeriodDivisor）。

<a id="a0ad1809fe74930c9b36b32516a8d146f"></a>

### `key`

```c
uint16_t bt_mesh_model_pub::key
```

发布所用的应用密钥索引（Publish AppKey Index）。

<a id="aa5026299082b3013740c7e36c01f91f5"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_model_pub::mod
```

此上下文所属的模型（Model）。

由协议栈（Stack）初始化。

<a id="a5f5639c01d3704ec3d527c418d35f827"></a>

### `msg`

```c
struct net_buf_simple* bt_mesh_model_pub::msg
```

包含发布消息的发布缓冲区（Publication buffer）。

使用 `BT_MESH_MODEL_PUB_DEFINE` 宏定义发布上下文（Publication context）时，会正确创建此项。

原始示例（Example）：

```c
BT_MESH_MODEL_PUB_DEFINE(name, update, size);
```

<a id="ae550510e9ca45f8c9fd9802e4e7e0f3d"></a>

### `period`

```c
uint8_t bt_mesh_model_pub::period
```

发布周期（Publish Period）。

<a id="a4f2ce8727ffb44f564d1dc0615ebcadf"></a>

### `period_div`

```c
uint8_t bt_mesh_model_pub::period_div
```

周期除数（Period Divisor）。

<a id="ab6e00714ea899eb32873d10b0908d278"></a>

### `period_start`

```c
uint32_t bt_mesh_model_pub::period_start
```

当前周期的开始时刻（Start of current period）。

<a id="a16c13e46c012ab836acd02b8fe5f05e3"></a>

### `retr_update`

```c
uint16_t bt_mesh_model_pub::retr_update
```

每次重传（Retransmission）时调用更新回调（Update callback）。

<a id="a3d93d44ff85243dc94e7b4d36cde5b97"></a>

### `retransmit`

```c
uint8_t bt_mesh_model_pub::retransmit
```

重传次数及间隔步数（Retransmit Count & Interval Steps）。

<a id="ab704aedcfd06d374615ef18c6ecc84a9"></a>

### `send_rel`

```c
uint16_t bt_mesh_model_pub::send_rel
```

强制可靠发送（Reliable sending），即使用分段确认（Segment acknowledgments）。

<a id="af3771432d13805710e94f013332e8214"></a>

### `timer`

```c
struct k_work_delayable bt_mesh_model_pub::timer
```

发布周期定时器（Publish Period Timer）。

仅供协议栈内部使用（Stack-internal use）。

<a id="a820b713aaa1e0c33a4a59c80f805e854"></a>

### `ttl`

```c
uint8_t bt_mesh_model_pub::ttl
```

发布生存时间（Publish Time to Live）。

<a id="a0354344e08e633dc4d6c0b4e7b169080"></a>

### `update`

```c
int(* bt_mesh_model_pub::update) (const struct bt_mesh_model *mod)
```

用于更新发布缓冲区（Publication buffer）的回调。

设为 `NULL` 时，视为该模型不支持周期发布（Periodic publishing）。设为非 `NULL` 时，将周期性调用此回调；回调应使用有效的发布消息更新 `bt_mesh_model_pub::msg`。

若回调返回非零值，则跳过本次发布，并在下一个周期发布间隔（Periodic publishing interval）恢复。

当 `bt_mesh_model_pub::retr_update` 设为 `1` 时，每次重传（Retransmission）都会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mod` | 发布上下文（Publication Context）所属的模型（Model）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="abea9c2085c9d2e1e2fc71f03dd323ee7"></a>

### `uuid`

```c
const uint8_t* bt_mesh_model_pub::uuid
```

发布地址为虚拟地址（Virtual Address）时使用的标签通用唯一标识符（Label UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_bt_mesh_model_op_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_bt_mesh_models_metadata_entry_结构体.md)
