---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-54
title: bt_gatt_ccc_managed_user_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc__managed__user__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_bt\_gatt\_ccc\_managed\_user\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc__managed__user__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CCC 值的内部表示（Internal Representation）。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

客户端特征配置值的内部表示（Internal representation of CCC value）。注意（Note）：只能将它用作 `BT_GATT_CCC_MANAGED` 的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a44987dc5be9442436f6033c30bbb42fd"></a>

```c
struct bt_gatt_ccc_cfg cfg [0]
```

相关声明：[bt_gatt_ccc_cfg](P053_bt_gatt_ccc_cfg_结构体.md)、[cfg](#a44987dc5be9442436f6033c30bbb42fd)。

每个连接的配置（Configuration）。

<a id="r_a883177671ea068f1dcbab36197abfdfd"></a>

```c
uint16_t value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a883177671ea068f1dcbab36197abfdfd)。

所有已连接对等设备订阅值中的最大值（Highest subscription value），不计保留位。

<a id="r_a166073fca5a342b859fb42482547b80c"></a>

```c
void(* cfg_changed )(const struct bt_gatt_attr *attr, uint16_t value)
```

相关声明：[cfg_changed](#a166073fca5a342b859fb42482547b80c)、[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a883177671ea068f1dcbab36197abfdfd)。

客户端特征配置属性变化回调（CCC attribute changed callback）。

<a id="r_a7ba4c03ef2a0c2c85e17ef1147934536"></a>

```c
ssize_t(* cfg_write )(struct bt_conn *conn, const struct bt_gatt_attr *attr, uint16_t value)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[cfg_write](#a7ba4c03ef2a0c2c85e17ef1147934536)、[bt_conn](P002_bt_conn_结构体.md)、[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a883177671ea068f1dcbab36197abfdfd)。

客户端特征配置属性写入验证回调（CCC attribute write validation callback）。

<a id="r_afc0c5226be7d9b2d3d039f86960a2ed3"></a>

```c
bool(* cfg_match )(struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cfg_match](#afc0c5226be7d9b2d3d039f86960a2ed3)、[bt_conn](P002_bt_conn_结构体.md)、[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)。

客户端特征配置属性匹配处理函数（CCC attribute match handler）。

## 54.2\_详细说明（Detailed Documentation）

<a id="a44987dc5be9442436f6033c30bbb42fd"></a>

### `cfg`

```c
struct bt_gatt_ccc_cfg bt_gatt_ccc_managed_user_data::cfg[0]
```

每个连接的配置（Configuration）。

<a id="a166073fca5a342b859fb42482547b80c"></a>

### `cfg_changed`

```c
void(* bt_gatt_ccc_managed_user_data::cfg_changed) (const struct bt_gatt_attr *attr, uint16_t value)
```

客户端特征配置属性变化回调（CCC attribute changed callback）。

缓存的客户端特征配置值（CCC value）变化时调用。处理 CCC 写入时，该值为所有已连接对等设备的最大订阅值。断开连接时，仅在所有订阅均被禁用后调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 缓存值发生变化的客户端特征配置属性（CCC attribute）。 |
| `value` | 新的缓存值（Cached value）。 |

<a id="afc0c5226be7d9b2d3d039f86960a2ed3"></a>

### `cfg_match`

```c
bool(* bt_gatt_ccc_managed_user_data::cfg_match) (struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

客户端特征配置属性匹配处理函数（CCC attribute match handler）。

指明是否可以向订阅方（Subscriber）发送通知（Notification）或指示（Indication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 正在检查的连接（Connection）。 |
| `attr` | 正在检查的属性（Attribute）。 |

**返回（Returns）**：返回值（Returns）：应用批准通知／指示（Notification/indication）时为 `true`，不批准时为 `false`。

<a id="a7ba4c03ef2a0c2c85e17ef1147934536"></a>

### `cfg_write`

```c
ssize_t(* bt_gatt_ccc_managed_user_data::cfg_write) (struct bt_conn *conn, const struct bt_gatt_attr *attr, uint16_t value)
```

客户端特征配置属性写入验证回调（CCC attribute write validation callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求写入的连接（Connection）。 |
| `attr` | 正在写入的属性（Attribute）。 |
| `value` | 要写入的客户端特征配置值（CCC value）。 |

**返回（Returns）**：返回值（Returns）：要写入的字节数；发生错误时，返回带有具体错误码的 `BT_GATT_ERR()`。

<a id="a883177671ea068f1dcbab36197abfdfd"></a>

### `value`

```c
uint16_t bt_gatt_ccc_managed_user_data::value
```

所有已连接对等设备订阅值中的最大值（Highest subscription value），不计保留位。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_ccc_cfg](P053_bt_gatt_ccc_cfg_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_conn](P002_bt_conn_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_GATT_CCC_MANAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8b296ecfd1139680f21da7904b9f585)
- [BT_GATT_ERR()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaff31756c1bf8ee755e65b1e0fb689bb7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_bt_gatt_ccc_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_bt_gatt_cep_结构体.md)
