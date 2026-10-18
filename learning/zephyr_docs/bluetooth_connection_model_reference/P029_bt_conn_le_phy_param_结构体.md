---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-29
title: bt_conn_le_phy_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__phy__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_bt\_conn\_le\_phy\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__phy__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的首选 PHY 参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的首选 PHY 参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a889dae2cdc2fba43f9f1194d26c4b737"></a>

```c
uint16_t options
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[options](#a889dae2cdc2fba43f9f1194d26c4b737)。

连接物理层选项（Connection PHY options）。

<a id="r_ace64d2181ecc25ecdfa374f7f4bcf664"></a>

```c
uint8_t pref_tx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pref_tx_phy](#ace64d2181ecc25ecdfa374f7f4bcf664)。

首选发送物理层的位掩码（Preferred transmit PHYs）。

<a id="r_a8d576bed5d9dfe9ca9a694d6d295afbc"></a>

```c
uint8_t pref_rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pref_rx_phy](#a8d576bed5d9dfe9ca9a694d6d295afbc)。

首选接收物理层的位掩码（Preferred receive PHYs）。

## 29.2\_详细说明（Detailed Documentation）

<a id="a889dae2cdc2fba43f9f1194d26c4b737"></a>

### `options`

```c
uint16_t bt_conn_le_phy_param::options
```

连接物理层选项（Connection PHY options）。

<a id="a8d576bed5d9dfe9ca9a694d6d295afbc"></a>

### `pref_rx_phy`

```c
uint8_t bt_conn_le_phy_param::pref_rx_phy
```

首选接收物理层的位掩码（Preferred receive PHYs）。

<a id="ace64d2181ecc25ecdfa374f7f4bcf664"></a>

### `pref_tx_phy`

```c
uint8_t bt_conn_le_phy_param::pref_tx_phy
```

首选发送物理层的位掩码（Preferred transmit PHYs）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_bt_conn_le_phy_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)
