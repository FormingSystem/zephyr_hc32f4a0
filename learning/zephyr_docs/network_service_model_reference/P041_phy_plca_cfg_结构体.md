---
id: learning.zephyr-docs.network-service-model-reference.page-41
title: phy_plca_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structphy__plca__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_phy\_plca\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structphy__plca__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

物理层冲突避免（PLCA）协调子层（Reconciliation Sublayer）的配置。

```c
#include <zephyr/net/phy.h>
```

<a id="details"></a>

物理层冲突避免（PLCA）协调子层（Reconciliation Sublayer）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a2c5eafc46d4869f11336094657978879"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#a2c5eafc46d4869f11336094657978879)。

物理层冲突避免（PLCA）寄存器映射版本。

<a id="r_a3f8580797874684e64fed0bd9bf25a94"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#a3f8580797874684e64fed0bd9bf25a94)。

PLCA 配置模式：启用或禁用（enable/disable）。

<a id="r_a7b98e4e26e7571aa7e4d1a99d81ea84a"></a>

```c
uint8_t node_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[node_id](#a7b98e4e26e7571aa7e4d1a99d81ea84a)。

PLCA 本地节点标识符。

<a id="r_a22346f28e7959b87038e938b169e670a"></a>

```c
uint8_t node_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[node_count](#a22346f28e7959b87038e938b169e670a)。

PLCA 节点数量。

<a id="r_a841b0ab053ea1903e8d0756f2ec6be87"></a>

```c
uint8_t burst_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[burst_count](#a841b0ab053ea1903e8d0756f2ec6be87)。

单次发送机会（Transmit Opportunity，TO）内允许节点发送的额外帧数。

<a id="r_aed0ad2e0da7dd1f7fb9e90dcd9d206ca"></a>

```c
uint8_t burst_timer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[burst_timer](#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)。

中断突发传输（burst）之前，等待 MAC 发送新帧的时间。

<a id="r_a0be4e9b562c9baabff0fb8c91868e549"></a>

```c
uint8_t to_timer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[to_timer](#a0be4e9b562c9baabff0fb8c91868e549)。

PLCA 的 `to_timer`，单位为比特时间（bit-time），用于决定 PLCA 发送机会。

## 41.2\_详细说明（Detailed Documentation）

<a id="a841b0ab053ea1903e8d0756f2ec6be87"></a>

### `burst_count`

```c
uint8_t phy_plca_cfg::burst_count
```

单次发送机会（Transmit Opportunity，TO）内允许节点发送的额外帧数。

<a id="aed0ad2e0da7dd1f7fb9e90dcd9d206ca"></a>

### `burst_timer`

```c
uint8_t phy_plca_cfg::burst_timer
```

中断突发传输（burst）之前，等待 MAC 发送新帧的时间。

<a id="a3f8580797874684e64fed0bd9bf25a94"></a>

### `enable`

```c
bool phy_plca_cfg::enable
```

PLCA 配置模式：启用或禁用（enable/disable）。

<a id="a22346f28e7959b87038e938b169e670a"></a>

### `node_count`

```c
uint8_t phy_plca_cfg::node_count
```

PLCA 节点数量。

<a id="a7b98e4e26e7571aa7e4d1a99d81ea84a"></a>

### `node_id`

```c
uint8_t phy_plca_cfg::node_id
```

PLCA 本地节点标识符。

<a id="a0be4e9b562c9baabff0fb8c91868e549"></a>

### `to_timer`

```c
uint8_t phy_plca_cfg::to_timer
```

PLCA 的 `to_timer`，单位为比特时间（bit-time），用于决定 PLCA 发送机会。

<a id="a2c5eafc46d4869f11336094657978879"></a>

### `version`

```c
uint8_t phy_plca_cfg::version
```

物理层冲突避免（PLCA）寄存器映射版本。

本数据类型文档由以下文件生成：

- `zephyr/net/phy.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/net/phy.h](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_phy_link_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_ppp_api_结构体.md)
