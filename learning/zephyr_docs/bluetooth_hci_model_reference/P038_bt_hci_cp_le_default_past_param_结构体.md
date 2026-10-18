---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-38
title: bt_hci_cp_le_default_past_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__default__past__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_hci\_cp\_le\_default\_past\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__default__past__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a2ef92304264ad0bf1560accf306bb6d9"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#a2ef92304264ad0bf1560accf306bb6d9)。

<a id="r_a214cb0597d0065bc2c056fe9c51a2220"></a>

```c
uint16_t skip
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[skip](#a214cb0597d0065bc2c056fe9c51a2220)。

<a id="r_a159f5245f86b27198264bdcf394d719f"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a159f5245f86b27198264bdcf394d719f)。

<a id="r_af18f679f5833c1d782b4e474af5d819c"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#af18f679f5833c1d782b4e474af5d819c)。

## 38.2\_详细说明（Detailed Documentation）

<a id="af18f679f5833c1d782b4e474af5d819c"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_default_past_param::cte_type
```

<a id="a2ef92304264ad0bf1560accf306bb6d9"></a>

### `mode`

```c
uint8_t bt_hci_cp_le_default_past_param::mode
```

<a id="a214cb0597d0065bc2c056fe9c51a2220"></a>

### `skip`

```c
uint16_t bt_hci_cp_le_default_past_param::skip
```

<a id="a159f5245f86b27198264bdcf394d719f"></a>

### `timeout`

```c
uint16_t bt_hci_cp_le_default_past_param::timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_hci_cp_le_cs_set_default_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_hci_cp_le_encrypt_结构体.md)
