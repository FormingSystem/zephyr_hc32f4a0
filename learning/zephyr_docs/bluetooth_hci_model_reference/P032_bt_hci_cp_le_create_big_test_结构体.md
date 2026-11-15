---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-32
title: bt_hci_cp_le_create_big_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__big__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_hci\_cp\_le\_create\_big\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__big__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_ac202f5cee0c1d0456b200606860fd5ab"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#ac202f5cee0c1d0456b200606860fd5ab)。

<a id="r_aece09ae6264e0cc1a5548f1603a3f61a"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#aece09ae6264e0cc1a5548f1603a3f61a)。

<a id="r_a6ce270f0afd185c44fa5a2c67a7783fb"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a6ce270f0afd185c44fa5a2c67a7783fb)。

<a id="r_a331b1a8ef66804cf20d6681e1bc5aefb"></a>

```c
uint8_t sdu_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sdu_interval](#a331b1a8ef66804cf20d6681e1bc5aefb)。

<a id="r_a6475ae77af80e89bb65596bc6f907a58"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a6475ae77af80e89bb65596bc6f907a58)。

<a id="r_a402c19da1ecf273bc942ecc560730567"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#a402c19da1ecf273bc942ecc560730567)。

<a id="r_a7ebbc81306109e035f89154738900395"></a>

```c
uint16_t max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_sdu](#a7ebbc81306109e035f89154738900395)。

<a id="r_a2652e0f340f13635a5da6335ec43e801"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#a2652e0f340f13635a5da6335ec43e801)。

<a id="r_a731ca2f90c17a4f3f868660e51649ce6"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a731ca2f90c17a4f3f868660e51649ce6)。

<a id="r_a49822f8e1617e30aab9b0d7d790697a3"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a49822f8e1617e30aab9b0d7d790697a3)。

<a id="r_acc5b2c30db0c7642d12019f8241dab26"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#acc5b2c30db0c7642d12019f8241dab26)。

<a id="r_a734174187486ac760b8bf0e566166842"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#a734174187486ac760b8bf0e566166842)。

<a id="r_a66ce7ba0498053a588de9097cbbc0891"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#a66ce7ba0498053a588de9097cbbc0891)。

<a id="r_a2f2eaa258463dd51a9f6042e75ecfec6"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#a2f2eaa258463dd51a9f6042e75ecfec6)。

<a id="r_a50c4308abda01581b436b7867304e982"></a>

```c
uint8_t encryption
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[encryption](#a50c4308abda01581b436b7867304e982)。

<a id="r_a333319a03d2087067247c4f5e595b4e5"></a>

```c
uint8_t bcode [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bcode](#a333319a03d2087067247c4f5e595b4e5)。

## 32.2\_详细说明（Detailed Documentation）

<a id="aece09ae6264e0cc1a5548f1603a3f61a"></a>

### `adv_handle`

```c
uint8_t bt_hci_cp_le_create_big_test::adv_handle
```

<a id="a333319a03d2087067247c4f5e595b4e5"></a>

### `bcode`

```c
uint8_t bt_hci_cp_le_create_big_test::bcode[16]
```

<a id="ac202f5cee0c1d0456b200606860fd5ab"></a>

### `big_handle`

```c
uint8_t bt_hci_cp_le_create_big_test::big_handle
```

<a id="a734174187486ac760b8bf0e566166842"></a>

### `bn`

```c
uint8_t bt_hci_cp_le_create_big_test::bn
```

<a id="a50c4308abda01581b436b7867304e982"></a>

### `encryption`

```c
uint8_t bt_hci_cp_le_create_big_test::encryption
```

<a id="acc5b2c30db0c7642d12019f8241dab26"></a>

### `framing`

```c
uint8_t bt_hci_cp_le_create_big_test::framing
```

<a id="a66ce7ba0498053a588de9097cbbc0891"></a>

### `irc`

```c
uint8_t bt_hci_cp_le_create_big_test::irc
```

<a id="a6475ae77af80e89bb65596bc6f907a58"></a>

### `iso_interval`

```c
uint16_t bt_hci_cp_le_create_big_test::iso_interval
```

<a id="a2652e0f340f13635a5da6335ec43e801"></a>

### `max_pdu`

```c
uint16_t bt_hci_cp_le_create_big_test::max_pdu
```

<a id="a7ebbc81306109e035f89154738900395"></a>

### `max_sdu`

```c
uint16_t bt_hci_cp_le_create_big_test::max_sdu
```

<a id="a402c19da1ecf273bc942ecc560730567"></a>

### `nse`

```c
uint8_t bt_hci_cp_le_create_big_test::nse
```

<a id="a6ce270f0afd185c44fa5a2c67a7783fb"></a>

### `num_bis`

```c
uint8_t bt_hci_cp_le_create_big_test::num_bis
```

<a id="a49822f8e1617e30aab9b0d7d790697a3"></a>

### `packing`

```c
uint8_t bt_hci_cp_le_create_big_test::packing
```

<a id="a731ca2f90c17a4f3f868660e51649ce6"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_create_big_test::phy
```

<a id="a2f2eaa258463dd51a9f6042e75ecfec6"></a>

### `pto`

```c
uint8_t bt_hci_cp_le_create_big_test::pto
```

<a id="a331b1a8ef66804cf20d6681e1bc5aefb"></a>

### `sdu_interval`

```c
uint8_t bt_hci_cp_le_create_big_test::sdu_interval[3]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_hci_cp_le_create_big_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_hci_cp_le_create_cis_结构体.md)
