---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-308
title: bt_hci_ext_conn_phy_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__ext__conn__phy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第308章\_bt\_hci\_ext\_conn\_phy\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__ext__conn__phy.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 308.1\_数据成员（Data Fields）

<a id="r_a4f78503fe42ee81fea740ba1643a732e"></a>

```c
uint16_t scan_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[scan_interval](#a4f78503fe42ee81fea740ba1643a732e)。

<a id="r_ae0e950c8004bd595631f95a289a5c871"></a>

```c
uint16_t scan_window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[scan_window](#ae0e950c8004bd595631f95a289a5c871)。

<a id="r_a7fc06c1a458aedb6b29381450a5a4df0"></a>

```c
uint16_t conn_interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_min](#a7fc06c1a458aedb6b29381450a5a4df0)。

<a id="r_a7bcf66a3372d92c809d8427796915b88"></a>

```c
uint16_t conn_interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_max](#a7bcf66a3372d92c809d8427796915b88)。

<a id="r_a7dd57b7ef0b13b15da47e92076f87d79"></a>

```c
uint16_t conn_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_latency](#a7dd57b7ef0b13b15da47e92076f87d79)。

<a id="r_aaec54c0743dfc08923b5ccd8fc1a4015"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#aaec54c0743dfc08923b5ccd8fc1a4015)。

<a id="r_af48212961ce21f5222e57f70ffeb811b"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#af48212961ce21f5222e57f70ffeb811b)。

<a id="r_a3c3ccb93014758b3215718d2672ce7f3"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#a3c3ccb93014758b3215718d2672ce7f3)。

## 308.2\_详细说明（Detailed Documentation）

<a id="a7bcf66a3372d92c809d8427796915b88"></a>

### `conn_interval_max`

```c
uint16_t bt_hci_ext_conn_phy::conn_interval_max
```

<a id="a7fc06c1a458aedb6b29381450a5a4df0"></a>

### `conn_interval_min`

```c
uint16_t bt_hci_ext_conn_phy::conn_interval_min
```

<a id="a7dd57b7ef0b13b15da47e92076f87d79"></a>

### `conn_latency`

```c
uint16_t bt_hci_ext_conn_phy::conn_latency
```

<a id="a3c3ccb93014758b3215718d2672ce7f3"></a>

### `max_ce_len`

```c
uint16_t bt_hci_ext_conn_phy::max_ce_len
```

<a id="af48212961ce21f5222e57f70ffeb811b"></a>

### `min_ce_len`

```c
uint16_t bt_hci_ext_conn_phy::min_ce_len
```

<a id="a4f78503fe42ee81fea740ba1643a732e"></a>

### `scan_interval`

```c
uint16_t bt_hci_ext_conn_phy::scan_interval
```

<a id="ae0e950c8004bd595631f95a289a5c871"></a>

### `scan_window`

```c
uint16_t bt_hci_ext_conn_phy::scan_window
```

<a id="aaec54c0743dfc08923b5ccd8fc1a4015"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_ext_conn_phy::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 308.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P307_bt_hci_ext_adv_set_结构体.md) · [返回大纲](大纲.md) · [下一章](P309_bt_hci_ext_scan_phy_结构体.md)
