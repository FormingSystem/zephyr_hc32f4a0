---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-28
title: bt_conn_le_phy_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__phy__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_conn\_le\_phy\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__phy__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的物理层（PHY）信息。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的物理层（PHY）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_ac65912cc2a7997c0f886886783ea5b11"></a>

```c
uint8_t tx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_phy](#ac65912cc2a7997c0f886886783ea5b11)。

<a id="r_abf029b63958d86eef7bf15218238783b"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#abf029b63958d86eef7bf15218238783b)。

连接发送物理层（Connection transmit PHY）。

## 28.2\_详细说明（Detailed Documentation）

<a id="abf029b63958d86eef7bf15218238783b"></a>

### `rx_phy`

```c
uint8_t bt_conn_le_phy_info::rx_phy
```

连接发送物理层（Connection transmit PHY）。

<a id="ac65912cc2a7997c0f886886783ea5b11"></a>

### `tx_phy`

```c
uint8_t bt_conn_le_phy_info::tx_phy
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_conn_le_path_loss_threshold_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_conn_le_phy_param_结构体.md)
