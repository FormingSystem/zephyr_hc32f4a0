---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-87
title: bt_hci_cp_le_set_cig_params_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cig__params__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_bt\_hci\_cp\_le\_set\_cig\_params\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cig__params__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_a161ae960cbd4f7833815285d04f87e46"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a161ae960cbd4f7833815285d04f87e46)。

<a id="r_aa392cbac058beefd0e410fcc9821a0c3"></a>

```c
uint8_t c_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_interval](#aa392cbac058beefd0e410fcc9821a0c3)。

<a id="r_a0cf0f3f7c10b29d74ab64aa30a4969de"></a>

```c
uint8_t p_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_interval](#a0cf0f3f7c10b29d74ab64aa30a4969de)。

<a id="r_a1eae50a97188304852589fd95e994150"></a>

```c
uint8_t c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_ft](#a1eae50a97188304852589fd95e994150)。

<a id="r_af2ed1bf1a6beaff884c3ce3faf26bfb2"></a>

```c
uint8_t p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_ft](#af2ed1bf1a6beaff884c3ce3faf26bfb2)。

<a id="r_aa77765d90fde67c52e4f2d483f0a3ee0"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#aa77765d90fde67c52e4f2d483f0a3ee0)。

<a id="r_a1d060539ff26677c1326a6ed3394fb6e"></a>

```c
uint8_t sca
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sca](#a1d060539ff26677c1326a6ed3394fb6e)。

<a id="r_a7275312e8b1c8ebc2af7992f765b392c"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a7275312e8b1c8ebc2af7992f765b392c)。

<a id="r_a2cb6745b8f908cd2e7d5f12a092c3b69"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#a2cb6745b8f908cd2e7d5f12a092c3b69)。

<a id="r_a50c345ef03c669f476e143728f42cd6d"></a>

```c
uint8_t num_cis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_cis](#a50c345ef03c669f476e143728f42cd6d)。

<a id="r_a5e07eb0d7d13e57be457d1b77a5dba12"></a>

```c
struct bt_hci_cis_params_test cis [0]
```

相关声明：[bt_hci_cis_params_test](P004_bt_hci_cis_params_test_结构体.md)、[cis](#a5e07eb0d7d13e57be457d1b77a5dba12)。

## 87.2\_详细说明（Detailed Documentation）

<a id="a1eae50a97188304852589fd95e994150"></a>

### `c_ft`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::c_ft
```

<a id="aa392cbac058beefd0e410fcc9821a0c3"></a>

### `c_interval`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::c_interval[3]
```

<a id="a161ae960cbd4f7833815285d04f87e46"></a>

### `cig_id`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::cig_id
```

<a id="a5e07eb0d7d13e57be457d1b77a5dba12"></a>

### `cis`

```c
struct bt_hci_cis_params_test bt_hci_cp_le_set_cig_params_test::cis[0]
```

<a id="a2cb6745b8f908cd2e7d5f12a092c3b69"></a>

### `framing`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::framing
```

<a id="aa77765d90fde67c52e4f2d483f0a3ee0"></a>

### `iso_interval`

```c
uint16_t bt_hci_cp_le_set_cig_params_test::iso_interval
```

<a id="a50c345ef03c669f476e143728f42cd6d"></a>

### `num_cis`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::num_cis
```

<a id="af2ed1bf1a6beaff884c3ce3faf26bfb2"></a>

### `p_ft`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::p_ft
```

<a id="a0cf0f3f7c10b29d74ab64aa30a4969de"></a>

### `p_interval`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::p_interval[3]
```

<a id="a7275312e8b1c8ebc2af7992f765b392c"></a>

### `packing`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::packing
```

<a id="a1d060539ff26677c1326a6ed3394fb6e"></a>

### `sca`

```c
uint8_t bt_hci_cp_le_set_cig_params_test::sca
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_cis_params_test](P004_bt_hci_cis_params_test_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_bt_hci_cp_le_set_cig_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md)
