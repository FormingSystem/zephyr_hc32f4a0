---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-137
title: bt_ots_client_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_bt\_ots\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）的客户端实例。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）的客户端实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 137.1\_数据成员（Data Fields）

<a id="r_a39818a4d776056212e82c4ba0626d0f1"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#a39818a4d776056212e82c4ba0626d0f1)。

<a id="r_a99727a6d064d79c3078a04b1d6d046db"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#a99727a6d064d79c3078a04b1d6d046db)。

<a id="r_a65608146d1a3e141635a015eb5092ab1"></a>

```c
uint16_t feature_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feature_handle](#a65608146d1a3e141635a015eb5092ab1)。

<a id="r_ae902c29051540141852869dd94edf7e0"></a>

```c
uint16_t obj_name_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_name_handle](#ae902c29051540141852869dd94edf7e0)。

<a id="r_ae2eebd727fd908ef2b2074c9c0b2ab4f"></a>

```c
uint16_t obj_type_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_type_handle](#ae2eebd727fd908ef2b2074c9c0b2ab4f)。

<a id="r_a83c5d653692dc3d7dbcfd5c8e2361f96"></a>

```c
uint16_t obj_size_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_size_handle](#a83c5d653692dc3d7dbcfd5c8e2361f96)。

<a id="r_aabd4a625a341b4f7bdcdcff03e7ae76f"></a>

```c
uint16_t obj_properties_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_properties_handle](#aabd4a625a341b4f7bdcdcff03e7ae76f)。

<a id="r_aff756cfa5f9431ed288563a95877cb53"></a>

```c
uint16_t obj_created_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_created_handle](#aff756cfa5f9431ed288563a95877cb53)。

<a id="r_a83cf53f6f7737620ea39dccbebe26dd4"></a>

```c
uint16_t obj_modified_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_modified_handle](#a83cf53f6f7737620ea39dccbebe26dd4)。

<a id="r_a6ff62fb7570269358888c9ab865a5ec6"></a>

```c
uint16_t obj_id_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_id_handle](#a6ff62fb7570269358888c9ab865a5ec6)。

<a id="r_ad56aaee2630d75a1bb5faf0f56486c0a"></a>

```c
uint16_t oacp_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[oacp_handle](#ad56aaee2630d75a1bb5faf0f56486c0a)。

<a id="r_aa98ae5a468c46f1ffbfd08a6e82f420d"></a>

```c
uint16_t olcp_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[olcp_handle](#aa98ae5a468c46f1ffbfd08a6e82f420d)。

<a id="r_a98a75a8ed52a2b97be1ea273a21b8775"></a>

```c
struct bt_gatt_subscribe_params oacp_sub_params
```

相关声明：[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)、[oacp_sub_params](#a98a75a8ed52a2b97be1ea273a21b8775)。

<a id="r_a8913d240d90b77ea72612ddbf816f528"></a>

```c
struct bt_gatt_discover_params oacp_sub_disc_params
```

相关声明：[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)、[oacp_sub_disc_params](#a8913d240d90b77ea72612ddbf816f528)。

<a id="r_a787b4851389e5da47a93969db6b3edcf"></a>

```c
struct bt_gatt_subscribe_params olcp_sub_params
```

相关声明：[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)、[olcp_sub_params](#a787b4851389e5da47a93969db6b3edcf)。

<a id="r_acbee05e7b1cd5c325a6982c6b32a732d"></a>

```c
struct bt_gatt_discover_params olcp_sub_disc_params
```

相关声明：[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)、[olcp_sub_disc_params](#acbee05e7b1cd5c325a6982c6b32a732d)。

<a id="r_a0e6a0d97a1b8edc7a282aec12d95b0dc"></a>

```c
struct bt_gatt_write_params write_params
```

相关声明：[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)、[write_params](#a0e6a0d97a1b8edc7a282aec12d95b0dc)。

<a id="r_a87d273e283941a3b9f1402e2b514134b"></a>

```c
struct bt_gatt_read_params read_proc
```

相关声明：[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)、[read_proc](#a87d273e283941a3b9f1402e2b514134b)。

<a id="r_a3aded7f58deb7f13c1c5adaa073f45f8"></a>

```c
struct bt_ots_client_cb * cb
```

相关声明：[bt_ots_client_cb](P138_bt_ots_client_cb_结构体.md)、[cb](#a3aded7f58deb7f13c1c5adaa073f45f8)。

<a id="r_a8a6d138d506a5e2732f4c51971533ce9"></a>

```c
struct bt_ots_feat features
```

相关声明：[bt_ots_feat](P140_bt_ots_feat_结构体.md)、[features](#a8a6d138d506a5e2732f4c51971533ce9)。

<a id="r_ac0fac55db40bf66aff358ce906fc8172"></a>

```c
struct bt_ots_obj_metadata cur_object
```

相关声明：[bt_ots_obj_metadata](P144_bt_ots_obj_metadata_结构体.md)、[cur_object](#ac0fac55db40bf66aff358ce906fc8172)。

## 137.2\_详细说明（Detailed Documentation）

<a id="a3aded7f58deb7f13c1c5adaa073f45f8"></a>

### `cb`

```c
struct bt_ots_client_cb* bt_ots_client::cb
```

<a id="ac0fac55db40bf66aff358ce906fc8172"></a>

### `cur_object`

```c
struct bt_ots_obj_metadata bt_ots_client::cur_object
```

<a id="a99727a6d064d79c3078a04b1d6d046db"></a>

### `end_handle`

```c
uint16_t bt_ots_client::end_handle
```

<a id="a65608146d1a3e141635a015eb5092ab1"></a>

### `feature_handle`

```c
uint16_t bt_ots_client::feature_handle
```

<a id="a8a6d138d506a5e2732f4c51971533ce9"></a>

### `features`

```c
struct bt_ots_feat bt_ots_client::features
```

<a id="ad56aaee2630d75a1bb5faf0f56486c0a"></a>

### `oacp_handle`

```c
uint16_t bt_ots_client::oacp_handle
```

<a id="a8913d240d90b77ea72612ddbf816f528"></a>

### `oacp_sub_disc_params`

```c
struct bt_gatt_discover_params bt_ots_client::oacp_sub_disc_params
```

<a id="a98a75a8ed52a2b97be1ea273a21b8775"></a>

### `oacp_sub_params`

```c
struct bt_gatt_subscribe_params bt_ots_client::oacp_sub_params
```

<a id="aff756cfa5f9431ed288563a95877cb53"></a>

### `obj_created_handle`

```c
uint16_t bt_ots_client::obj_created_handle
```

<a id="a6ff62fb7570269358888c9ab865a5ec6"></a>

### `obj_id_handle`

```c
uint16_t bt_ots_client::obj_id_handle
```

<a id="a83cf53f6f7737620ea39dccbebe26dd4"></a>

### `obj_modified_handle`

```c
uint16_t bt_ots_client::obj_modified_handle
```

<a id="ae902c29051540141852869dd94edf7e0"></a>

### `obj_name_handle`

```c
uint16_t bt_ots_client::obj_name_handle
```

<a id="aabd4a625a341b4f7bdcdcff03e7ae76f"></a>

### `obj_properties_handle`

```c
uint16_t bt_ots_client::obj_properties_handle
```

<a id="a83c5d653692dc3d7dbcfd5c8e2361f96"></a>

### `obj_size_handle`

```c
uint16_t bt_ots_client::obj_size_handle
```

<a id="ae2eebd727fd908ef2b2074c9c0b2ab4f"></a>

### `obj_type_handle`

```c
uint16_t bt_ots_client::obj_type_handle
```

<a id="aa98ae5a468c46f1ffbfd08a6e82f420d"></a>

### `olcp_handle`

```c
uint16_t bt_ots_client::olcp_handle
```

<a id="acbee05e7b1cd5c325a6982c6b32a732d"></a>

### `olcp_sub_disc_params`

```c
struct bt_gatt_discover_params bt_ots_client::olcp_sub_disc_params
```

<a id="a787b4851389e5da47a93969db6b3edcf"></a>

### `olcp_sub_params`

```c
struct bt_gatt_subscribe_params bt_ots_client::olcp_sub_params
```

<a id="a87d273e283941a3b9f1402e2b514134b"></a>

### `read_proc`

```c
struct bt_gatt_read_params bt_ots_client::read_proc
```

<a id="a39818a4d776056212e82c4ba0626d0f1"></a>

### `start_handle`

```c
uint16_t bt_ots_client::start_handle
```

<a id="a0e6a0d97a1b8edc7a282aec12d95b0dc"></a>

### `write_params`

```c
struct bt_gatt_write_params bt_ots_client::write_params
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 137.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)
- [bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)
- [bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)
- [bt_ots_client_cb](P138_bt_ots_client_cb_结构体.md)
- [bt_ots_feat](P140_bt_ots_feat_结构体.md)
- [bt_ots_obj_metadata](P144_bt_ots_obj_metadata_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P136_bt_ots_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P138_bt_ots_client_cb_结构体.md)
