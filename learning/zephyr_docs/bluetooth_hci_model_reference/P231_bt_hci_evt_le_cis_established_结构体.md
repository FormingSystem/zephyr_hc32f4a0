---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-231
title: bt_hci_evt_le_cis_established_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__established.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第231章\_bt\_hci\_evt\_le\_cis\_established\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__established.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 231.1\_数据成员（Data Fields）

<a id="r_a4d90dbeda130a6142ff0b7f9e2ee7c16"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a4d90dbeda130a6142ff0b7f9e2ee7c16)。

<a id="r_a932e8df0222eb3bcf7bee753414d529e"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a932e8df0222eb3bcf7bee753414d529e)。

<a id="r_ac4e5a2535e3e8d3782adac63a4c5a8d9"></a>

```c
uint8_t cig_sync_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_sync_delay](#ac4e5a2535e3e8d3782adac63a4c5a8d9)。

<a id="r_ae71d6753849ae3c57327c8763cab1802"></a>

```c
uint8_t cis_sync_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_sync_delay](#ae71d6753849ae3c57327c8763cab1802)。

<a id="r_a877913bb4b9016c64793458de94d84a0"></a>

```c
uint8_t c_latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_latency](#a877913bb4b9016c64793458de94d84a0)。

<a id="r_aefb2d4e0458cbe990903a9f449189c30"></a>

```c
uint8_t p_latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_latency](#aefb2d4e0458cbe990903a9f449189c30)。

<a id="r_a53ea1da3f31313ab73b511c72912bd33"></a>

```c
uint8_t c_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_phy](#a53ea1da3f31313ab73b511c72912bd33)。

<a id="r_a25b84cf026775b582c7944e265ffb0b2"></a>

```c
uint8_t p_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_phy](#a25b84cf026775b582c7944e265ffb0b2)。

<a id="r_a683856418764b1110d5c5fea0494fe1e"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#a683856418764b1110d5c5fea0494fe1e)。

<a id="r_ab6b2d892e3c1e4f6aedee722049b75d3"></a>

```c
uint8_t c_bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_bn](#ab6b2d892e3c1e4f6aedee722049b75d3)。

<a id="r_ad0a79bfadd413bf572b697069695c0a5"></a>

```c
uint8_t p_bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_bn](#ad0a79bfadd413bf572b697069695c0a5)。

<a id="r_ad0f3bd5f81b660afbc4927a777c2c18e"></a>

```c
uint8_t c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_ft](#ad0f3bd5f81b660afbc4927a777c2c18e)。

<a id="r_a200afaff044b9eea653d8aee13297dc2"></a>

```c
uint8_t p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_ft](#a200afaff044b9eea653d8aee13297dc2)。

<a id="r_ae9fdecff4342f25de30165a4531ad703"></a>

```c
uint16_t c_max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_max_pdu](#ae9fdecff4342f25de30165a4531ad703)。

<a id="r_ae8b195f433570e28e42a5f9d321964de"></a>

```c
uint16_t p_max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_max_pdu](#ae8b195f433570e28e42a5f9d321964de)。

<a id="r_a0bcdc0d8b3b776660d2e51427f9634dd"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a0bcdc0d8b3b776660d2e51427f9634dd)。

## 231.2\_详细说明（Detailed Documentation）

<a id="ab6b2d892e3c1e4f6aedee722049b75d3"></a>

### `c_bn`

```c
uint8_t bt_hci_evt_le_cis_established::c_bn
```

<a id="ad0f3bd5f81b660afbc4927a777c2c18e"></a>

### `c_ft`

```c
uint8_t bt_hci_evt_le_cis_established::c_ft
```

<a id="a877913bb4b9016c64793458de94d84a0"></a>

### `c_latency`

```c
uint8_t bt_hci_evt_le_cis_established::c_latency[3]
```

<a id="ae9fdecff4342f25de30165a4531ad703"></a>

### `c_max_pdu`

```c
uint16_t bt_hci_evt_le_cis_established::c_max_pdu
```

<a id="a53ea1da3f31313ab73b511c72912bd33"></a>

### `c_phy`

```c
uint8_t bt_hci_evt_le_cis_established::c_phy
```

<a id="ac4e5a2535e3e8d3782adac63a4c5a8d9"></a>

### `cig_sync_delay`

```c
uint8_t bt_hci_evt_le_cis_established::cig_sync_delay[3]
```

<a id="ae71d6753849ae3c57327c8763cab1802"></a>

### `cis_sync_delay`

```c
uint8_t bt_hci_evt_le_cis_established::cis_sync_delay[3]
```

<a id="a932e8df0222eb3bcf7bee753414d529e"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cis_established::conn_handle
```

<a id="a0bcdc0d8b3b776660d2e51427f9634dd"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_cis_established::interval
```

<a id="a683856418764b1110d5c5fea0494fe1e"></a>

### `nse`

```c
uint8_t bt_hci_evt_le_cis_established::nse
```

<a id="ad0a79bfadd413bf572b697069695c0a5"></a>

### `p_bn`

```c
uint8_t bt_hci_evt_le_cis_established::p_bn
```

<a id="a200afaff044b9eea653d8aee13297dc2"></a>

### `p_ft`

```c
uint8_t bt_hci_evt_le_cis_established::p_ft
```

<a id="aefb2d4e0458cbe990903a9f449189c30"></a>

### `p_latency`

```c
uint8_t bt_hci_evt_le_cis_established::p_latency[3]
```

<a id="ae8b195f433570e28e42a5f9d321964de"></a>

### `p_max_pdu`

```c
uint16_t bt_hci_evt_le_cis_established::p_max_pdu
```

<a id="a25b84cf026775b582c7944e265ffb0b2"></a>

### `p_phy`

```c
uint8_t bt_hci_evt_le_cis_established::p_phy
```

<a id="a4d90dbeda130a6142ff0b7f9e2ee7c16"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cis_established::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 231.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P230_bt_hci_evt_le_chan_sel_algo_结构体.md) · [返回大纲](大纲.md) · [下一章](P232_bt_hci_evt_le_cis_established_v2_结构体.md)
