---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-57
title: bt_gatt_cpf_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cpf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_bt\_gatt\_cpf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cpf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 特征呈现格式（Characteristic Presentation Format）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 特征表示格式属性值（Characteristic Presentation Format Attribute Value）。用于发现标准特征描述符值。可与 `BT_GATT_CPF` 宏配合使用，声明特征表示格式描述符（CPF descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_ab0ca135a75130b3ffc0c5bf375f3528f"></a>

```c
uint8_t format
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[format](#ab0ca135a75130b3ffc0c5bf375f3528f)。

特征值格式（Characteristic value format）。

<a id="r_a3690a86c942badb2d2698481b03e436d"></a>

```c
int8_t exponent
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[exponent](#a3690a86c942badb2d2698481b03e436d)。

用于值格式化的指数字段（Exponent field）。

<a id="r_a2a9f3d3f72b9acb1ef7f2dc765e5a231"></a>

```c
uint16_t unit
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[unit](#a2a9f3d3f72b9acb1ef7f2dc765e5a231)。

特征单位的通用唯一标识符（Unit UUID）。

<a id="r_a1dfbb9fc1e1397d2abec04b216d7ae33"></a>

```c
uint8_t name_space
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name_space](#a1dfbb9fc1e1397d2abec04b216d7ae33)。

描述的命名空间（Name space）。

<a id="r_a3c48dd5ea717fbaf510d13c64a370c06"></a>

```c
uint16_t description
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[description](#a3c48dd5ea717fbaf510d13c64a370c06)。

上层配置规范（Higher layer profile）定义的特征描述（Characteristic description）。

## 57.2\_详细说明（Detailed Documentation）

<a id="a3c48dd5ea717fbaf510d13c64a370c06"></a>

### `description`

```c
uint16_t bt_gatt_cpf::description
```

上层配置规范（Higher layer profile）定义的特征描述（Characteristic description）。

由 `name_space` 字段所标识的组织定义的枚举值（Enumerated value）。参见蓝牙技术联盟已分配编号文档（Bluetooth SIG Assigned Numbers）第 2.4.2.1 节。

<a id="a3690a86c942badb2d2698481b03e436d"></a>

### `exponent`

```c
int8_t bt_gatt_cpf::exponent
```

用于值格式化的指数字段（Exponent field）。

仅用于整数格式类型（Integer format types）。实际值（Actual value）＝特征值（Characteristic Value）× 10^指数（Exponent）。

<a id="ab0ca135a75130b3ffc0c5bf375f3528f"></a>

### `format`

```c
uint8_t bt_gatt_cpf::format
```

特征值格式（Characteristic value format）。

格式类型（Format types）见蓝牙技术联盟已分配编号文档（Bluetooth SIG Assigned Numbers）第 2.4.1 节。

<a id="a1dfbb9fc1e1397d2abec04b216d7ae33"></a>

### `name_space`

```c
uint8_t bt_gatt_cpf::name_space
```

描述的命名空间（Name space）。

用于标识负责定义 `description` 字段枚举值的组织。参见蓝牙技术联盟已分配编号文档（Bluetooth SIG Assigned Numbers）第 2.4.2 节。

<a id="a2a9f3d3f72b9acb1ef7f2dc765e5a231"></a>

### `unit`

```c
uint16_t bt_gatt_cpf::unit
```

特征单位的通用唯一标识符（Unit UUID）。

单位（Units）见蓝牙技术联盟已分配编号文档（Bluetooth SIG Assigned Numbers）第 3.5 节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_GATT_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga3835fcfdf7a5f917e21c9d17e75162be)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_bt_gatt_chrc_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_bt_gatt_discover_params_结构体.md)
