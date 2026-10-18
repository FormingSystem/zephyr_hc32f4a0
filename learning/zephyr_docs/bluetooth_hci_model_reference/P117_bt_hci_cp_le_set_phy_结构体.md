---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-117
title: bt_hci_cp_le_set_phy_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__phy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_bt\_hci\_cp\_le\_set\_phy\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__phy.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 117.1\_数据成员（Data Fields）

<a id="r_ad0759eea02017674459d4ce0af0e526e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ad0759eea02017674459d4ce0af0e526e)。

<a id="r_afb8d056dc7d8824eec0ef16fdf9ce924"></a>

```c
uint8_t all_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[all_phys](#afb8d056dc7d8824eec0ef16fdf9ce924)。

<a id="r_a06880062ff486b532ebeb789adb57d1e"></a>

```c
uint8_t tx_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_phys](#a06880062ff486b532ebeb789adb57d1e)。

<a id="r_ab30eb68920a0578b16794250e592b12a"></a>

```c
uint8_t rx_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phys](#ab30eb68920a0578b16794250e592b12a)。

<a id="r_a458ab90f83b60fafa66167f474c0800d"></a>

```c
uint16_t phy_opts
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[phy_opts](#a458ab90f83b60fafa66167f474c0800d)。

## 117.2\_详细说明（Detailed Documentation）

<a id="afb8d056dc7d8824eec0ef16fdf9ce924"></a>

### `all_phys`

```c
uint8_t bt_hci_cp_le_set_phy::all_phys
```

<a id="ad0759eea02017674459d4ce0af0e526e"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_phy::handle
```

<a id="a458ab90f83b60fafa66167f474c0800d"></a>

### `phy_opts`

```c
uint16_t bt_hci_cp_le_set_phy::phy_opts
```

<a id="ab30eb68920a0578b16794250e592b12a"></a>

### `rx_phys`

```c
uint8_t bt_hci_cp_le_set_phy::rx_phys
```

<a id="a06880062ff486b532ebeb789adb57d1e"></a>

### `tx_phys`

```c
uint8_t bt_hci_cp_le_set_phy::tx_phys
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 117.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P118_bt_hci_cp_le_set_privacy_mode_结构体.md)
