---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-101
title: bt_mesh_statistic_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__statistic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_bt\_mesh\_statistic\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__statistic.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存Mesh帧处理统计信息的结构。

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

<a id="details"></a>

保存Mesh帧处理统计信息的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_a5c8d77c2d32964f0a54420aafff9a4e1"></a>

```c
uint32_t rx_adv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_adv](#a5c8d77c2d32964f0a54420aafff9a4e1)。

通过基本验证和解密（Basic validation and decryption）的所有接收帧。

<a id="r_a448c73e05fd8055baaa64532275d9c69"></a>

```c
uint32_t rx_loopback
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_loopback](#a448c73e05fd8055baaa64532275d9c69)。

通过回环（Loopback）接收到的帧。

<a id="r_aa86617d0c3cfa7e2ed7e10e4c3ac8b5c"></a>

```c
uint32_t rx_proxy
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_proxy](#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c)。

通过代理（Proxy）接收到的帧。

<a id="r_af7c764c6b702957180d8b74193207a0e"></a>

```c
uint32_t rx_uknown
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_uknown](#af7c764c6b702957180d8b74193207a0e)。

通过未知接口（Unknown interface）接收的内容。

<a id="r_a1979c5798d7d015bf4cf0c30716d3e4f"></a>

```c
uint32_t tx_adv_relay_planned
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_adv_relay_planned](#a1979c5798d7d015bf4cf0c30716d3e4f)。

开始通过广播承载（Advertiser bearer）中继的帧计数。

<a id="r_a139484340d2bd3fae763b23e91648e0e"></a>

```c
uint32_t tx_adv_relay_succeeded
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_adv_relay_succeeded](#a139484340d2bd3fae763b23e91648e0e)。

成功通过广播承载（Advertiser bearer）中继的帧计数。

<a id="r_a2c47d080eac1050422d36402a9771fa6"></a>

```c
uint32_t tx_local_planned
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_local_planned](#a2c47d080eac1050422d36402a9771fa6)。

本地发起、开始通过广播承载（Advertiser bearer）发送的帧计数。

<a id="r_a9da26f6d5ad7b91b69b95e4d4a70bf71"></a>

```c
uint32_t tx_local_succeeded
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_local_succeeded](#a9da26f6d5ad7b91b69b95e4d4a70bf71)。

本地发起、成功通过广播承载（Advertiser bearer）发送的帧计数。

<a id="r_a0f60214d1f2480bc0025415064dd79e8"></a>

```c
uint32_t tx_friend_planned
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_friend_planned](#a0f60214d1f2480bc0025415064dd79e8)。

开始通过友谊承载（Friend bearer）发送的帧计数。

<a id="r_aa4d83bb57f86723899bc2fe25342423d"></a>

```c
uint32_t tx_friend_succeeded
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_friend_succeeded](#aa4d83bb57f86723899bc2fe25342423d)。

成功通过友谊承载（Friend bearer）发送的帧计数。

## 101.2\_详细说明（Detailed Documentation）

<a id="a5c8d77c2d32964f0a54420aafff9a4e1"></a>

### `rx_adv`

```c
uint32_t bt_mesh_statistic::rx_adv
```

通过基本验证和解密（Basic validation and decryption）的所有接收帧。

通过广播器（Advertiser）接收到的帧。

<a id="a448c73e05fd8055baaa64532275d9c69"></a>

### `rx_loopback`

```c
uint32_t bt_mesh_statistic::rx_loopback
```

通过回环（Loopback）接收到的帧。

<a id="aa86617d0c3cfa7e2ed7e10e4c3ac8b5c"></a>

### `rx_proxy`

```c
uint32_t bt_mesh_statistic::rx_proxy
```

通过代理（Proxy）接收到的帧。

<a id="af7c764c6b702957180d8b74193207a0e"></a>

### `rx_uknown`

```c
uint32_t bt_mesh_statistic::rx_uknown
```

通过未知接口（Unknown interface）接收的内容。

<a id="a1979c5798d7d015bf4cf0c30716d3e4f"></a>

### `tx_adv_relay_planned`

```c
uint32_t bt_mesh_statistic::tx_adv_relay_planned
```

开始通过广播承载（Advertiser bearer）中继的帧计数。

<a id="a139484340d2bd3fae763b23e91648e0e"></a>

### `tx_adv_relay_succeeded`

```c
uint32_t bt_mesh_statistic::tx_adv_relay_succeeded
```

成功通过广播承载（Advertiser bearer）中继的帧计数。

<a id="a0f60214d1f2480bc0025415064dd79e8"></a>

### `tx_friend_planned`

```c
uint32_t bt_mesh_statistic::tx_friend_planned
```

开始通过友谊承载（Friend bearer）发送的帧计数。

<a id="aa4d83bb57f86723899bc2fe25342423d"></a>

### `tx_friend_succeeded`

```c
uint32_t bt_mesh_statistic::tx_friend_succeeded
```

成功通过友谊承载（Friend bearer）发送的帧计数。

<a id="a2c47d080eac1050422d36402a9771fa6"></a>

### `tx_local_planned`

```c
uint32_t bt_mesh_statistic::tx_local_planned
```

本地发起、开始通过广播承载（Advertiser bearer）发送的帧计数。

<a id="a9da26f6d5ad7b91b69b95e4d4a70bf71"></a>

### `tx_local_succeeded`

```c
uint32_t bt_mesh_statistic::tx_local_succeeded
```

本地发起、成功通过广播承载（Advertiser bearer）发送的帧计数。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/statistic.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/statistic.h](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_bt_mesh_sol_pdu_rpl_cli_结构体.md) · [返回大纲](大纲.md)
