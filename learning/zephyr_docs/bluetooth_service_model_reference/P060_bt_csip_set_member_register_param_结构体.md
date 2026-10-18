---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-60
title: bt_csip_set_member_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_bt\_csip\_set\_member\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

协调集合标识服务（CSIS）的注册结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

协调集合标识服务（CSIS）的注册结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_af8814b6e0695001e0a70025f5c2b4e83"></a>

```c
uint8_t set_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[set_size](#af8814b6e0695001e0a70025f5c2b4e83)。

集合大小（Set size）。

<a id="r_aeba89480776db362a9c9406dc3a9a945"></a>

```c
uint8_t sirk [16U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sirk](#aeba89480776db362a9c9406dc3a9a945)。

唯一的集合身份解析密钥（Set Identity Resolving Key，SIRK）。

<a id="r_abc87df6590e3c55a2cd860f86398346d"></a>

```c
bool lockable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[lockable](#abc87df6590e3c55a2cd860f86398346d)。

布尔值，用于设置客户端是否可以锁定此集合（Lockable）。

<a id="r_af38436c47f52ec285cadb5d23c67ea0a"></a>

```c
uint8_t rank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rank](#af38436c47f52ec285cadb5d23c67ea0a)。

此设备在此集合中的排序值（Rank）。

<a id="r_a1878a8d50ab190920435aaef611b69f1"></a>

```c
struct bt_csip_set_member_cb * cb
```

相关声明：[bt_csip_set_member_cb](P059_bt_csip_set_member_cb_结构体.md)、[cb](#a1878a8d50ab190920435aaef611b69f1)。

指向回调结构体（Callback Structure）的指针。

<a id="r_a7b74ebf8608ba0a9c50d83d414ff15b2"></a>

```c
const struct bt_gatt_service * parent
```

相关声明：[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)、[parent](#a7b74ebf8608ba0a9c50d83d414ff15b2)。

父服务指针（Parent service pointer）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a1878a8d50ab190920435aaef611b69f1"></a>

### `cb`

```c
struct bt_csip_set_member_cb* bt_csip_set_member_register_param::cb
```

指向回调结构体（Callback Structure）的指针。

<a id="abc87df6590e3c55a2cd860f86398346d"></a>

### `lockable`

```c
bool bt_csip_set_member_register_param::lockable
```

布尔值，用于设置客户端是否可以锁定此集合（Lockable）。

设为 `false` 时，禁用锁特征（Lock characteristic）。若未启用 `CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT`，则忽略此项。

<a id="a7b74ebf8608ba0a9c50d83d414ff15b2"></a>

### `parent`

```c
const struct bt_gatt_service* bt_csip_set_member_register_param::parent
```

父服务指针（Parent service pointer）。

若此协调集合标识服务实例（CSIS instance）由其他服务包含，则必须提供父服务指针（Parent service pointer）。根据协调集合标识规范（CSIP），当 `CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT` 大于 `1` 时，所有 CSIS 实例都必须由另一个服务包含。

<a id="af38436c47f52ec285cadb5d23c67ea0a"></a>

### `rank`

```c
uint8_t bt_csip_set_member_register_param::rank
```

此设备在此集合中的排序值（Rank）。

若 `lockable` 设为 `true`，此值必须大于 `0`；若启用了集合大小支持，还必须小于或等于 `set_size`。若 `lockable` 为 `false`，可将此值设为 `0`，以禁用排序特征（Rank characteristic）。

未启用 `CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT` 时，忽略此项。

<a id="af8814b6e0695001e0a70025f5c2b4e83"></a>

### `set_size`

```c
uint8_t bt_csip_set_member_register_param::set_size
```

集合大小（Set size）。

设为 `0` 时，不初始化集合大小特征（Set size characteristic）。未启用 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT` 时，忽略此项。

<a id="aeba89480776db362a9c9406dc3a9a945"></a>

### `sirk`

```c
uint8_t bt_csip_set_member_register_param::sirk[16U]
```

唯一的集合身份解析密钥（Set Identity Resolving Key，SIRK）。

此值必须在不同集合之间唯一，并且同一个集合的所有成员必须使用相同值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_csip_set_member_cb](P059_bt_csip_set_member_cb_结构体.md)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT)
- [CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_bt_csip_set_member_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_bt_csip_set_member_set_info_结构体.md)
