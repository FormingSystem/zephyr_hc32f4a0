---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-86
title: bt_hci_cp_le_set_cig_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cig__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_bt\_hci\_cp\_le\_set\_cig\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cig__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a7dbf75c6ed92a053c4ec0d8f7268c92e"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a7dbf75c6ed92a053c4ec0d8f7268c92e)。

<a id="r_a14f5c0cf7f99ab406714501038048035"></a>

```c
uint8_t c_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_interval](#a14f5c0cf7f99ab406714501038048035)。

<a id="r_a50a260a15f3a0ceae716da6c04c5b768"></a>

```c
uint8_t p_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_interval](#a50a260a15f3a0ceae716da6c04c5b768)。

<a id="r_a46a657cdfbc7a49e6761d9f18d980c2a"></a>

```c
uint8_t sca
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sca](#a46a657cdfbc7a49e6761d9f18d980c2a)。

<a id="r_a79fc069492741f14f348650abef4c66b"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a79fc069492741f14f348650abef4c66b)。

<a id="r_a867bf5ddbcadd27dbec2c3059d67d6d6"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#a867bf5ddbcadd27dbec2c3059d67d6d6)。

<a id="r_afec8ebd17cc6ca5b3d13ef54f406df62"></a>

```c
uint16_t c_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_latency](#afec8ebd17cc6ca5b3d13ef54f406df62)。

<a id="r_a810822396b97d54988ec57561b4ee7d5"></a>

```c
uint16_t p_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_latency](#a810822396b97d54988ec57561b4ee7d5)。

<a id="r_adf468a8a195447a7bbed4dcd53d287f6"></a>

```c
uint8_t num_cis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_cis](#adf468a8a195447a7bbed4dcd53d287f6)。

<a id="r_ac922e59065920421f40468754d2ba5a2"></a>

```c
struct bt_hci_cis_params cis [0]
```

相关声明：[bt_hci_cis_params](P003_bt_hci_cis_params_结构体.md)、[cis](#ac922e59065920421f40468754d2ba5a2)。

## 86.2\_详细说明（Detailed Documentation）

<a id="a14f5c0cf7f99ab406714501038048035"></a>

### `c_interval`

```c
uint8_t bt_hci_cp_le_set_cig_params::c_interval[3]
```

<a id="afec8ebd17cc6ca5b3d13ef54f406df62"></a>

### `c_latency`

```c
uint16_t bt_hci_cp_le_set_cig_params::c_latency
```

<a id="a7dbf75c6ed92a053c4ec0d8f7268c92e"></a>

### `cig_id`

```c
uint8_t bt_hci_cp_le_set_cig_params::cig_id
```

<a id="ac922e59065920421f40468754d2ba5a2"></a>

### `cis`

```c
struct bt_hci_cis_params bt_hci_cp_le_set_cig_params::cis[0]
```

<a id="a867bf5ddbcadd27dbec2c3059d67d6d6"></a>

### `framing`

```c
uint8_t bt_hci_cp_le_set_cig_params::framing
```

<a id="adf468a8a195447a7bbed4dcd53d287f6"></a>

### `num_cis`

```c
uint8_t bt_hci_cp_le_set_cig_params::num_cis
```

<a id="a50a260a15f3a0ceae716da6c04c5b768"></a>

### `p_interval`

```c
uint8_t bt_hci_cp_le_set_cig_params::p_interval[3]
```

<a id="a810822396b97d54988ec57561b4ee7d5"></a>

### `p_latency`

```c
uint16_t bt_hci_cp_le_set_cig_params::p_latency
```

<a id="a79fc069492741f14f348650abef4c66b"></a>

### `packing`

```c
uint8_t bt_hci_cp_le_set_cig_params::packing
```

<a id="a46a657cdfbc7a49e6761d9f18d980c2a"></a>

### `sca`

```c
uint8_t bt_hci_cp_le_set_cig_params::sca
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_cis_params](P003_bt_hci_cis_params_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_bt_hci_cp_le_set_cig_params_test_结构体.md)
