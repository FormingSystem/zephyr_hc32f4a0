---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-53
title: bt_gatt_ccc_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_bt\_gatt\_ccc\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT CCC 配置条目。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 客户端特征配置条目（CCC configuration entry）。`bt_gatt_attr_read_ccc` 和 `bt_gatt_attr_write_ccc` 分别使用 `bt_gatt_ccc_cfg` 读取与写入 CCC 配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_ac17ddefe7ca6dbac921ee4c6f44fbf51"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ac17ddefe7ca6dbac921ee4c6f44fbf51)。

本地身份（Local identity），多数情况下为 `BT_ID_DEFAULT`。

<a id="r_ab316080693b2c4daf5fd45e2c0501c70"></a>

```c
bt_addr_le_t peer
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer](#ab316080693b2c4daf5fd45e2c0501c70)。

远端对等设备地址（Remote peer address）。

<a id="r_a92acf7329f66638ac6c657c8eaa795ac"></a>

```c
uint16_t value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value](#a92acf7329f66638ac6c657c8eaa795ac)。

配置值（Configuration value），用于启用或禁用某个特定特征（Characteristic）的通知（Notifications）或指示（Indications）。

## 53.2\_详细说明（Detailed Documentation）

<a id="ac17ddefe7ca6dbac921ee4c6f44fbf51"></a>

### `id`

```c
uint8_t bt_gatt_ccc_cfg::id
```

本地身份（Local identity），多数情况下为 `BT_ID_DEFAULT`。

<a id="ab316080693b2c4daf5fd45e2c0501c70"></a>

### `peer`

```c
bt_addr_le_t bt_gatt_ccc_cfg::peer
```

远端对等设备地址（Remote peer address）。

<a id="a92acf7329f66638ac6c657c8eaa795ac"></a>

### `value`

```c
uint16_t bt_gatt_ccc_cfg::value
```

配置值（Configuration value），用于启用或禁用某个特定特征（Characteristic）的通知（Notifications）或指示（Indications）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_ccc_cfg](P053_bt_gatt_ccc_cfg_结构体.md)
- [bt_gatt_attr_read_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2e85b42136e2c6a4cb5b7ad8a2532573)
- [bt_gatt_attr_write_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabba965b676650a55cb9934072b34c75e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_bt_gatt_ccc_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_bt_gatt_ccc_managed_user_data_结构体.md)
