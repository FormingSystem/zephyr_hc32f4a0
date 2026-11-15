---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-232
title: bt_hci_evt_le_cis_established_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__established__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第232章\_bt\_hci\_evt\_le\_cis\_established\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__established__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 232.1\_数据成员（Data Fields）

<a id="r_a1f43b72368227f212511bb248b4a0e22"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1f43b72368227f212511bb248b4a0e22)。

<a id="r_a7a7b8303183a916225bb0a3ea11d5480"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a7a7b8303183a916225bb0a3ea11d5480)。

<a id="r_a754ad7e68821da0bdb8da0bdeb3b4697"></a>

```c
uint8_t cig_sync_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_sync_delay](#a754ad7e68821da0bdb8da0bdeb3b4697)。

<a id="r_af134783424a77274abac44613bf61264"></a>

```c
uint8_t cis_sync_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_sync_delay](#af134783424a77274abac44613bf61264)。

<a id="r_ae580ff8c0ef4cd03365cbf1a06aed8bc"></a>

```c
uint8_t c_latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_latency](#ae580ff8c0ef4cd03365cbf1a06aed8bc)。

<a id="r_a26b25e1615991977735cbfc679d747f3"></a>

```c
uint8_t p_latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_latency](#a26b25e1615991977735cbfc679d747f3)。

<a id="r_a9b7ba96597a5131927e365b7a45f8d6f"></a>

```c
uint8_t c_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_phy](#a9b7ba96597a5131927e365b7a45f8d6f)。

<a id="r_a5a0b08098ac4e6ec93a6ecbbbf4ef587"></a>

```c
uint8_t p_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_phy](#a5a0b08098ac4e6ec93a6ecbbbf4ef587)。

<a id="r_ac3a87b20b2f10e980639d232a013f702"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#ac3a87b20b2f10e980639d232a013f702)。

<a id="r_a5f68c3cba98ed96afef0949f6b14ded9"></a>

```c
uint8_t c_bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_bn](#a5f68c3cba98ed96afef0949f6b14ded9)。

<a id="r_a64b48b20283415100fc8bdf33edf2b0e"></a>

```c
uint8_t p_bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_bn](#a64b48b20283415100fc8bdf33edf2b0e)。

<a id="r_a2de704a032ac2379528991f2d01e6979"></a>

```c
uint8_t c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_ft](#a2de704a032ac2379528991f2d01e6979)。

<a id="r_a3b1fc27cca2bc85c36e257aabd8ea612"></a>

```c
uint8_t p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_ft](#a3b1fc27cca2bc85c36e257aabd8ea612)。

<a id="r_acd8cf2d2d85b65d839256f3412a4bb43"></a>

```c
uint16_t c_max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_max_pdu](#acd8cf2d2d85b65d839256f3412a4bb43)。

<a id="r_aeea230245aa75dd7f44bf5a4a286e9a5"></a>

```c
uint16_t p_max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_max_pdu](#aeea230245aa75dd7f44bf5a4a286e9a5)。

<a id="r_a71762f8a31e20b233a252ac974f6d329"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a71762f8a31e20b233a252ac974f6d329)。

<a id="r_a353409fe069aba91c5372ee8ae6e1b79"></a>

```c
uint8_t sub_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub_interval](#a353409fe069aba91c5372ee8ae6e1b79)。

<a id="r_ad054af39ddad854423379b3cc7aafc26"></a>

```c
uint16_t c_max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_max_sdu](#ad054af39ddad854423379b3cc7aafc26)。

<a id="r_a2a060c0bb2831eb3df0dc8ffb74ecebd"></a>

```c
uint16_t p_max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_max_sdu](#a2a060c0bb2831eb3df0dc8ffb74ecebd)。

<a id="r_a926a5faeb98a99333310d860da37f6f5"></a>

```c
uint8_t c_sdu_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_sdu_interval](#a926a5faeb98a99333310d860da37f6f5)。

<a id="r_acf30d6a745803fd4e984d66548ceff58"></a>

```c
uint8_t p_sdu_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_sdu_interval](#acf30d6a745803fd4e984d66548ceff58)。

<a id="r_af59ca6d54ca770ef8334ea091bcc53f6"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#af59ca6d54ca770ef8334ea091bcc53f6)。

## 232.2\_详细说明（Detailed Documentation）

<a id="a5f68c3cba98ed96afef0949f6b14ded9"></a>

### `c_bn`

```c
uint8_t bt_hci_evt_le_cis_established_v2::c_bn
```

<a id="a2de704a032ac2379528991f2d01e6979"></a>

### `c_ft`

```c
uint8_t bt_hci_evt_le_cis_established_v2::c_ft
```

<a id="ae580ff8c0ef4cd03365cbf1a06aed8bc"></a>

### `c_latency`

```c
uint8_t bt_hci_evt_le_cis_established_v2::c_latency[3]
```

<a id="acd8cf2d2d85b65d839256f3412a4bb43"></a>

### `c_max_pdu`

```c
uint16_t bt_hci_evt_le_cis_established_v2::c_max_pdu
```

<a id="ad054af39ddad854423379b3cc7aafc26"></a>

### `c_max_sdu`

```c
uint16_t bt_hci_evt_le_cis_established_v2::c_max_sdu
```

<a id="a9b7ba96597a5131927e365b7a45f8d6f"></a>

### `c_phy`

```c
uint8_t bt_hci_evt_le_cis_established_v2::c_phy
```

<a id="a926a5faeb98a99333310d860da37f6f5"></a>

### `c_sdu_interval`

```c
uint8_t bt_hci_evt_le_cis_established_v2::c_sdu_interval[3]
```

<a id="a754ad7e68821da0bdb8da0bdeb3b4697"></a>

### `cig_sync_delay`

```c
uint8_t bt_hci_evt_le_cis_established_v2::cig_sync_delay[3]
```

<a id="af134783424a77274abac44613bf61264"></a>

### `cis_sync_delay`

```c
uint8_t bt_hci_evt_le_cis_established_v2::cis_sync_delay[3]
```

<a id="a7a7b8303183a916225bb0a3ea11d5480"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cis_established_v2::conn_handle
```

<a id="af59ca6d54ca770ef8334ea091bcc53f6"></a>

### `framing`

```c
uint8_t bt_hci_evt_le_cis_established_v2::framing
```

<a id="a71762f8a31e20b233a252ac974f6d329"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_cis_established_v2::interval
```

<a id="ac3a87b20b2f10e980639d232a013f702"></a>

### `nse`

```c
uint8_t bt_hci_evt_le_cis_established_v2::nse
```

<a id="a64b48b20283415100fc8bdf33edf2b0e"></a>

### `p_bn`

```c
uint8_t bt_hci_evt_le_cis_established_v2::p_bn
```

<a id="a3b1fc27cca2bc85c36e257aabd8ea612"></a>

### `p_ft`

```c
uint8_t bt_hci_evt_le_cis_established_v2::p_ft
```

<a id="a26b25e1615991977735cbfc679d747f3"></a>

### `p_latency`

```c
uint8_t bt_hci_evt_le_cis_established_v2::p_latency[3]
```

<a id="aeea230245aa75dd7f44bf5a4a286e9a5"></a>

### `p_max_pdu`

```c
uint16_t bt_hci_evt_le_cis_established_v2::p_max_pdu
```

<a id="a2a060c0bb2831eb3df0dc8ffb74ecebd"></a>

### `p_max_sdu`

```c
uint16_t bt_hci_evt_le_cis_established_v2::p_max_sdu
```

<a id="a5a0b08098ac4e6ec93a6ecbbbf4ef587"></a>

### `p_phy`

```c
uint8_t bt_hci_evt_le_cis_established_v2::p_phy
```

<a id="acf30d6a745803fd4e984d66548ceff58"></a>

### `p_sdu_interval`

```c
uint8_t bt_hci_evt_le_cis_established_v2::p_sdu_interval[3]
```

<a id="a1f43b72368227f212511bb248b4a0e22"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cis_established_v2::status
```

<a id="a353409fe069aba91c5372ee8ae6e1b79"></a>

### `sub_interval`

```c
uint8_t bt_hci_evt_le_cis_established_v2::sub_interval[3]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 232.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P231_bt_hci_evt_le_cis_established_结构体.md) · [返回大纲](大纲.md) · [下一章](P233_bt_hci_evt_le_cis_req_结构体.md)
