---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-88
title: bt_mesh_prov_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_bt\_mesh\_prov\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配网（Provisioning）的属性与能力。

```c
#include <zephyr/bluetooth/mesh/main.h>
```

<a id="details"></a>

配网（Provisioning）的属性与能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_a1152d77c4c4d9271bbd72514d94052f2"></a>

```c
const uint8_t * uuid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#a1152d77c4c4d9271bbd72514d94052f2)。

以未配网状态（Unprovisioned）广播时使用的通用唯一标识符（UUID）。

<a id="r_a6a11cc0d36ca2f4c5aee67a023c295a2"></a>

```c
const char * uri
```

相关声明：[uri](#a6a11cc0d36ca2f4c5aee67a023c295a2)。

可选的统一资源标识符（URI）。

<a id="r_a6ed61556291f7f9d9a32062d588b8f2a"></a>

```c
bt_mesh_prov_oob_info_t oob_info
```

相关声明：[bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)、[oob_info](#a6ed61556291f7f9d9a32062d588b8f2a)。

带外信息字段（Out of Band information field）。

<a id="r_a1261ba69e785f005d5834ac49da00778"></a>

```c
const uint8_t * public_key_be
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[public_key_be](#a1261ba69e785f005d5834ac49da00778)。

指向大端格式公钥（Public Key in big-endian）的指针，用于支持带外公钥类型（OOB public key type）。

<a id="r_a1ab714e9be35242e02099884c3af45f5"></a>

```c
const uint8_t * private_key_be
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[private_key_be](#a1ab714e9be35242e02099884c3af45f5)。

指向大端格式私钥（Private Key in big-endian）的指针，用于支持带外公钥类型（OOB public key type）。

<a id="r_a97cf41cf857479c8eefee640f7b66788"></a>

```c
const uint8_t * static_val
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[static_val](#a97cf41cf857479c8eefee640f7b66788)。

静态带外值（Static OOB value）。

<a id="r_a97394dded5fd55b553364a566a2441e8"></a>

```c
uint8_t static_val_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[static_val_len](#a97394dded5fd55b553364a566a2441e8)。

静态带外值长度（Static OOB value length）。

<a id="r_a4c51aa8e5887b3364d9480c92da3a0a0"></a>

```c
uint8_t output_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_size](#a4c51aa8e5887b3364d9480c92da3a0a0)。

支持的输出带外数据最大大小（Maximum Output OOB size）。

<a id="r_a8b88959c5eef7f47591468e9c9768b7c"></a>

```c
uint16_t output_actions
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[output_actions](#a8b88959c5eef7f47591468e9c9768b7c)。

支持的输出带外操作（Output OOB Actions）。

<a id="r_ab9044f6dbf9780b3237f18270b2c8582"></a>

```c
uint8_t input_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[input_size](#ab9044f6dbf9780b3237f18270b2c8582)。

支持的输入带外数据最大大小（Maximum Input OOB size）。

<a id="r_af928a9419f684bcbda0563dda2c34d76"></a>

```c
uint16_t input_actions
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[input_actions](#af928a9419f684bcbda0563dda2c34d76)。

支持的输入带外操作（Input OOB Actions）。

<a id="r_afbc65bb8be99f7dc37ecc911f4ac2151"></a>

```c
void(* capabilities )(const struct bt_mesh_dev_capabilities *cap)
```

相关声明：[capabilities](#afbc65bb8be99f7dc37ecc911f4ac2151)、[bt_mesh_dev_capabilities](P043_bt_mesh_dev_capabilities_结构体.md)。

配网能力（Provisioning Capabilities）。

<a id="r_ae7aec4a89f4260a99696bb46207c4338"></a>

```c
int(* output_numeric )(bt_mesh_output_action_t act, uint8_t *numeric, size_t size)
```

相关声明：[output_numeric](#ae7aec4a89f4260a99696bb46207c4338)、[bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求输出一个数值（Numeric value）。

<a id="r_a28284efee6478637446702d7839f6b8c"></a>

```c
int(* output_string )(const char *str)
```

相关声明：[output_string](#a28284efee6478637446702d7839f6b8c)。

请求输出一个字符串（String）。

<a id="r_a31eff9c903ac721bbca7ab586dda9e80"></a>

```c
int(* input )(bt_mesh_input_action_t act, uint8_t size)
```

相关声明：[input](#a31eff9c903ac721bbca7ab586dda9e80)、[bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求输入（Input）。

<a id="r_a2717ddf38465b95452724078f780f9e5"></a>

```c
void(* input_complete )(void)
```

相关声明：[input_complete](#a2717ddf38465b95452724078f780f9e5)。

另一台设备已完成带外输入（OOB input）。

<a id="r_a8142a3b8120b1686f68513caeac09497"></a>

```c
void(* unprovisioned_beacon )(uint8_t uuid[16], bt_mesh_prov_oob_info_t oob_info, uint32_t *uri_hash)
```

相关声明：[unprovisioned_beacon](#a8142a3b8120b1686f68513caeac09497)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)、[oob_info](#a6ed61556291f7f9d9a32062d588b8f2a)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

已收到未配网信标（Unprovisioned beacon）。

<a id="r_a7eddf1f088264f8b6e3fb86dce4c108e"></a>

```c
void(* unprovisioned_beacon_gatt )(uint8_t uuid[16], bt_mesh_prov_oob_info_t oob_info)
```

相关声明：[unprovisioned_beacon_gatt](#a7eddf1f088264f8b6e3fb86dce4c108e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)、[oob_info](#a6ed61556291f7f9d9a32062d588b8f2a)。

已收到基于 GATT 的配网承载未配网广播（PB-GATT Unprovisioned Advertising）。

<a id="r_a44efea3e9221c182cbcacce8219ef6b7"></a>

```c
void(* link_open )(bt_mesh_prov_bearer_t bearer)
```

相关声明：[link_open](#a44efea3e9221c182cbcacce8219ef6b7)、[bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)。

配网链路（Provisioning link）已打开。

<a id="r_a0183cef77dda3978ef8a40ce7aad043a"></a>

```c
void(* link_close )(bt_mesh_prov_bearer_t bearer)
```

相关声明：[link_close](#a0183cef77dda3978ef8a40ce7aad043a)、[bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)。

配网链路（Provisioning link）已关闭。

<a id="r_ad55abc2b1632455bb23fbd8b03df85ea"></a>

```c
void(* complete )(uint16_t net_idx, uint16_t addr)
```

相关声明：[complete](#ad55abc2b1632455bb23fbd8b03df85ea)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

配网（Provisioning）已完成。

<a id="r_ac131476cdeb002f0027407b4cf80c2b5"></a>

```c
void(* reprovisioned )(uint16_t addr)
```

相关声明：[reprovisioned](#ac131476cdeb002f0027407b4cf80c2b5)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

本地节点已重新配网（Reprovisioned）。

<a id="r_aaa49675e358ea4cba7552b3e855befba"></a>

```c
void(* node_added )(uint16_t net_idx, uint8_t uuid[16], uint16_t addr, uint8_t num_elem)
```

相关声明：[node_added](#aaa49675e358ea4cba7552b3e855befba)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

新节点已添加到配网数据库（Provisioning database）。

<a id="r_ae87570de25c89e74bece2516ff957779"></a>

```c
void(* reset )(void)
```

相关声明：[reset](#ae87570de25c89e74bece2516ff957779)。

节点已重置（Reset）。

## 88.2\_详细说明（Detailed Documentation）

<a id="afbc65bb8be99f7dc37ecc911f4ac2151"></a>

### `capabilities`

```c
void(* bt_mesh_prov::capabilities) (const struct bt_mesh_dev_capabilities *cap)
```

配网能力（Provisioning Capabilities）。

此回调通知应用，已收到未配网设备（Unprovisioned device）的配网能力（Provisioning capabilities）。

随后，应用可调用 `bt_mesh_auth_method_set_<*>` 选择合适的配网带外认证方法（Provisioning OOB authentication method）。

此回调返回后，配网器（Provisioner）将使用选定的方法开始认证。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cap` | 设备支持的能力（Capabilities）。 |

<a id="ad55abc2b1632455bb23fbd8b03df85ea"></a>

### `complete`

```c
void(* bt_mesh_prov::complete) (uint16_t net_idx, uint16_t addr)
```

配网（Provisioning）已完成。

此回调通知应用，配网（Provisioning）已成功完成，且本地节点已被分配指定的网络密钥索引（NetKeyIndex）和主元素地址（Primary element address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 配网（Provisioning）期间提供的网络密钥索引（NetKeyIndex）。 |
| `addr` | 主元素地址（Primary element address）。 |

<a id="a31eff9c903ac721bbca7ab586dda9e80"></a>

### `input`

```c
int(* bt_mesh_prov::input) (bt_mesh_input_action_t act, uint8_t size)
```

请求输入（Input）。

此回调通知应用，应使用指定动作向用户请求输入。请求的输入为字符串或数值；应用从用户处获得数据后，需要相应调用 `bt_mesh_input_string()` 或 `bt_mesh_input_numeric()` 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `act` | 输入数据的动作（Input action）。 |
| `size` | 输入数据的最大大小（Maximum input data size）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="af928a9419f684bcbda0563dda2c34d76"></a>

### `input_actions`

```c
uint16_t bt_mesh_prov::input_actions
```

支持的输入带外操作（Input OOB Actions）。

<a id="a2717ddf38465b95452724078f780f9e5"></a>

### `input_complete`

```c
void(* bt_mesh_prov::input_complete) (void)
```

另一台设备已完成带外输入（OOB input）。

此回调通知应用，另一方已完成带外输入（OOB input），因此应停止显示自身的输出带外值（Output OOB value）。

<a id="ab9044f6dbf9780b3237f18270b2c8582"></a>

### `input_size`

```c
uint8_t bt_mesh_prov::input_size
```

支持的输入带外数据最大大小（Maximum Input OOB size）。

<a id="a0183cef77dda3978ef8a40ce7aad043a"></a>

### `link_close`

```c
void(* bt_mesh_prov::link_close) (bt_mesh_prov_bearer_t bearer)
```

配网链路（Provisioning link）已关闭。

此回调通知应用，指定配网承载（Provisioning bearer）上的配网链路（Provisioning link）已关闭。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 配网承载（Provisioning bearer）。 |

<a id="a44efea3e9221c182cbcacce8219ef6b7"></a>

### `link_open`

```c
void(* bt_mesh_prov::link_open) (bt_mesh_prov_bearer_t bearer)
```

配网链路（Provisioning link）已打开。

此回调通知应用，指定配网承载（Provisioning bearer）上的配网链路（Provisioning link）已打开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 配网承载（Provisioning bearer）。 |

<a id="aaa49675e358ea4cba7552b3e855befba"></a>

### `node_added`

```c
void(* bt_mesh_prov::node_added) (uint16_t net_idx, uint8_t uuid[16], uint16_t addr, uint8_t num_elem)
```

新节点已添加到配网数据库（Provisioning database）。

此回调通知应用，配网（Provisioning）已成功完成，且某个节点已被分配指定的网络密钥索引（NetKeyIndex）和主元素地址（Primary element address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 配网（Provisioning）期间提供的网络密钥索引（NetKeyIndex）。 |
| `uuid` | 新增节点的通用唯一标识符（UUID）。 |
| `addr` | 主元素地址（Primary element address）。 |
| `num_elem` | 此节点的元素数量（Number of elements）。 |

<a id="a6ed61556291f7f9d9a32062d588b8f2a"></a>

### `oob_info`

```c
bt_mesh_prov_oob_info_t bt_mesh_prov::oob_info
```

带外信息字段（Out of Band information field）。

<a id="a8b88959c5eef7f47591468e9c9768b7c"></a>

### `output_actions`

```c
uint16_t bt_mesh_prov::output_actions
```

支持的输出带外操作（Output OOB Actions）。

<a id="ae7aec4a89f4260a99696bb46207c4338"></a>

### `output_numeric`

```c
int(* bt_mesh_prov::output_numeric) (bt_mesh_output_action_t act, uint8_t *numeric, size_t size)
```

请求输出一个数值（Numeric value）。

此回调通知应用，应使用指定动作输出给定数值（Numeric value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `act` | 输出数值的动作（Numeric output action）。 |
| `numeric` | 保存待输出数值的内存，数值采用小端格式（Little endian）。 |
| `size` | 数值大小（Numeric value size），单位为字节。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="a4c51aa8e5887b3364d9480c92da3a0a0"></a>

### `output_size`

```c
uint8_t bt_mesh_prov::output_size
```

支持的输出带外数据最大大小（Maximum Output OOB size）。

<a id="a28284efee6478637446702d7839f6b8c"></a>

### `output_string`

```c
int(* bt_mesh_prov::output_string) (const char *str)
```

请求输出一个字符串（String）。

此回调通知应用，应向用户显示给定字符串（String）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 待显示的字符串（String）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="a1ab714e9be35242e02099884c3af45f5"></a>

### `private_key_be`

```c
const uint8_t* bt_mesh_prov::private_key_be
```

指向大端格式私钥（Private Key in big-endian）的指针，用于支持带外公钥类型（OOB public key type）。

初始化此参数时，记得启用 `CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY`。

必须与 `bt_mesh_prov::public_key_be` 一起使用。

<a id="a1261ba69e785f005d5834ac49da00778"></a>

### `public_key_be`

```c
const uint8_t* bt_mesh_prov::public_key_be
```

指向大端格式公钥（Public Key in big-endian）的指针，用于支持带外公钥类型（OOB public key type）。

初始化此参数时，记得启用 `CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY`。

必须与 `bt_mesh_prov::private_key_be` 一起使用。

<a id="ac131476cdeb002f0027407b4cf80c2b5"></a>

### `reprovisioned`

```c
void(* bt_mesh_prov::reprovisioned) (uint16_t addr)
```

本地节点已重新配网（Reprovisioned）。

此回调通知应用，重新配网（Reprovisioning）已成功完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 新的主元素地址（Primary element address）。 |

<a id="ae87570de25c89e74bece2516ff957779"></a>

### `reset`

```c
void(* bt_mesh_prov::reset) (void)
```

节点已重置（Reset）。

此回调通知应用，本地节点已重置，需要重新配网（Provisioning）。节点不会自动广播未配网状态；必须调用 `bt_mesh_prov_enable()` API，才能在一个或多个配网承载（Provisioning bearers）上启用未配网广播（Unprovisioned advertising）。

<a id="a97cf41cf857479c8eefee640f7b66788"></a>

### `static_val`

```c
const uint8_t* bt_mesh_prov::static_val
```

静态带外值（Static OOB value）。

<a id="a97394dded5fd55b553364a566a2441e8"></a>

### `static_val_len`

```c
uint8_t bt_mesh_prov::static_val_len
```

静态带外值长度（Static OOB value length）。

<a id="a8142a3b8120b1686f68513caeac09497"></a>

### `unprovisioned_beacon`

```c
void(* bt_mesh_prov::unprovisioned_beacon) (uint8_t uuid[16], bt_mesh_prov_oob_info_t oob_info, uint32_t *uri_hash)
```

已收到未配网信标（Unprovisioned beacon）。

此回调通知应用，已收到未配网信标（Unprovisioned beacon）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | 通用唯一标识符（UUID）。 |
| `oob_info` | 带外信息（OOB Information）。 |
| `uri_hash` | 指向统一资源标识符哈希值（URI Hash）的指针。若信标中没有哈希值，则为 `NULL`。 |

<a id="a7eddf1f088264f8b6e3fb86dce4c108e"></a>

### `unprovisioned_beacon_gatt`

```c
void(* bt_mesh_prov::unprovisioned_beacon_gatt) (uint8_t uuid[16], bt_mesh_prov_oob_info_t oob_info)
```

已收到基于 GATT 的配网承载未配网广播（PB-GATT Unprovisioned Advertising）。

此回调通知应用，已收到基于 GATT 的配网承载未配网广播（PB-GATT Unprovisioned Advertising）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | 通用唯一标识符（UUID）。 |
| `oob_info` | 带外信息（OOB Information）。 |

<a id="a6a11cc0d36ca2f4c5aee67a023c295a2"></a>

### `uri`

```c
const char* bt_mesh_prov::uri
```

可选的统一资源标识符（URI）。

此内容与未配网信标（Unprovisioned beacon）分别广播，但未配网信标包含它的哈希值（Hash），使配网器（Provisioner）能够将二者关联起来。

<a id="a1152d77c4c4d9271bbd72514d94052f2"></a>

### `uuid`

```c
const uint8_t* bt_mesh_prov::uuid
```

以未配网状态（Unprovisioned）广播时使用的通用唯一标识符（UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/main.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_dev_capabilities](P043_bt_mesh_dev_capabilities_结构体.md)
- [bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)
- [bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)
- [bt_mesh_input_string()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga2592abf429b40ef9242bce26f5bd085e)
- [bt_mesh_input_numeric()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)
- [CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY)
- [bt_mesh_prov_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_bt_mesh_priv_node_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_bt_mesh_proxy_cb_结构体.md)
