---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-31
title: bt_hci_cp_le_create_big_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__big.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_hci\_cp\_le\_create\_big\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__big.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_af5412e4a69c05a09b2e818322636a98a"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#af5412e4a69c05a09b2e818322636a98a)。

<a id="r_aa686eec31ca4c831262dd34d41f9a1fb"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#aa686eec31ca4c831262dd34d41f9a1fb)。

<a id="r_ad8491c970417e63c6a98c12278a89c86"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#ad8491c970417e63c6a98c12278a89c86)。

<a id="r_a2960a9891b827529c9fa1b68a747e2d5"></a>

```c
uint8_t sdu_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sdu_interval](#a2960a9891b827529c9fa1b68a747e2d5)。

<a id="r_a06fd74e9a5f172060835524da5851c71"></a>

```c
uint16_t max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_sdu](#a06fd74e9a5f172060835524da5851c71)。

<a id="r_a15018e5ebc124bbe90644b38fe3e7e76"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a15018e5ebc124bbe90644b38fe3e7e76)。

<a id="r_a1cb0dd106bf4a1a0c473333d089c95e7"></a>

```c
uint8_t rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtn](#a1cb0dd106bf4a1a0c473333d089c95e7)。

<a id="r_a56cb773a03e4927c3b6bf4d2a6ed6ed9"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a56cb773a03e4927c3b6bf4d2a6ed6ed9)。

<a id="r_ac027390db21320fb9d1002161c4c2f67"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#ac027390db21320fb9d1002161c4c2f67)。

<a id="r_a330916d60c05ec2ef7a71933b62c203a"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#a330916d60c05ec2ef7a71933b62c203a)。

<a id="r_a490bd68d137f8cf60ea2ccd5ea4495e9"></a>

```c
uint8_t encryption
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[encryption](#a490bd68d137f8cf60ea2ccd5ea4495e9)。

<a id="r_a0b4b2d77cd0f579aab190336b14597c5"></a>

```c
uint8_t bcode [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bcode](#a0b4b2d77cd0f579aab190336b14597c5)。

## 31.2\_详细说明（Detailed Documentation）

<a id="aa686eec31ca4c831262dd34d41f9a1fb"></a>

### `adv_handle`

```c
uint8_t bt_hci_cp_le_create_big::adv_handle
```

<a id="a0b4b2d77cd0f579aab190336b14597c5"></a>

### `bcode`

```c
uint8_t bt_hci_cp_le_create_big::bcode[16]
```

<a id="af5412e4a69c05a09b2e818322636a98a"></a>

### `big_handle`

```c
uint8_t bt_hci_cp_le_create_big::big_handle
```

<a id="a490bd68d137f8cf60ea2ccd5ea4495e9"></a>

### `encryption`

```c
uint8_t bt_hci_cp_le_create_big::encryption
```

<a id="a330916d60c05ec2ef7a71933b62c203a"></a>

### `framing`

```c
uint8_t bt_hci_cp_le_create_big::framing
```

<a id="a15018e5ebc124bbe90644b38fe3e7e76"></a>

### `max_latency`

```c
uint16_t bt_hci_cp_le_create_big::max_latency
```

<a id="a06fd74e9a5f172060835524da5851c71"></a>

### `max_sdu`

```c
uint16_t bt_hci_cp_le_create_big::max_sdu
```

<a id="ad8491c970417e63c6a98c12278a89c86"></a>

### `num_bis`

```c
uint8_t bt_hci_cp_le_create_big::num_bis
```

<a id="ac027390db21320fb9d1002161c4c2f67"></a>

### `packing`

```c
uint8_t bt_hci_cp_le_create_big::packing
```

<a id="a56cb773a03e4927c3b6bf4d2a6ed6ed9"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_create_big::phy
```

<a id="a1cb0dd106bf4a1a0c473333d089c95e7"></a>

### `rtn`

```c
uint8_t bt_hci_cp_le_create_big::rtn
```

<a id="a2960a9891b827529c9fa1b68a747e2d5"></a>

### `sdu_interval`

```c
uint8_t bt_hci_cp_le_create_big::sdu_interval[3]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_hci_cp_le_conn_param_req_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_hci_cp_le_create_big_test_结构体.md)
