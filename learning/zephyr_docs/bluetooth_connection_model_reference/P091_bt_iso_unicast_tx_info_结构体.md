---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-91
title: bt_iso_unicast_tx_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__unicast__tx__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_bt\_iso\_unicast\_tx\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__unicast__tx__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时单播发送（ISO Unicast TX）的信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时单播发送（ISO Unicast TX）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a14548ee24fad8a26287aa0daba451a47"></a>

```c
uint32_t latency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[latency](#a14548ee24fad8a26287aa0daba451a47)。

传输延迟（Transport latency），单位为微秒。

<a id="r_aaf1f623eac2f84ca06082776179b71c5"></a>

```c
uint32_t flush_timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flush_timeout](#aaf1f623eac2f84ca06082776179b71c5)。

刷新超时（Flush timeout），为 N × 1.25 毫秒。

<a id="r_afe7dce9255613e5e2939d3719c720822"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#afe7dce9255613e5e2939d3719c720822)。

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="r_a3134e0bdb663ad7184e23531504233a5"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a3134e0bdb663ad7184e23531504233a5)。

传输物理层（Transport PHY）。

<a id="r_ab4ea9d5bb535d29ae9406e948d8707a9"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#ab4ea9d5bb535d29ae9406e948d8707a9)。

突发数量（Burst number）。

<a id="r_a7bed74a67bb73f6919d2817d82bcf996"></a>

```c
uint16_t max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_sdu](#a7bed74a67bb73f6919d2817d82bcf996)。

最大服务数据单元大小（Maximum SDU size），以八位组（Octets）为单位。

<a id="r_adc91f9c200199400a84322a58d28a933"></a>

```c
uint32_t sdu_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sdu_interval](#adc91f9c200199400a84322a58d28a933)。

服务数据单元间隔（SDU interval），单位为微秒。

## 91.2\_详细说明（Detailed Documentation）

<a id="ab4ea9d5bb535d29ae9406e948d8707a9"></a>

### `bn`

```c
uint8_t bt_iso_unicast_tx_info::bn
```

突发数量（Burst number）。

<a id="aaf1f623eac2f84ca06082776179b71c5"></a>

### `flush_timeout`

```c
uint32_t bt_iso_unicast_tx_info::flush_timeout
```

刷新超时（Flush timeout），为 N × 1.25 毫秒。

<a id="a14548ee24fad8a26287aa0daba451a47"></a>

### `latency`

```c
uint32_t bt_iso_unicast_tx_info::latency
```

传输延迟（Transport latency），单位为微秒。

<a id="afe7dce9255613e5e2939d3719c720822"></a>

### `max_pdu`

```c
uint16_t bt_iso_unicast_tx_info::max_pdu
```

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="a7bed74a67bb73f6919d2817d82bcf996"></a>

### `max_sdu`

```c
uint16_t bt_iso_unicast_tx_info::max_sdu
```

最大服务数据单元大小（Maximum SDU size），以八位组（Octets）为单位。

对于外设（Peripherals），若未知，可设为 `bt_iso_unicast_tx_info::max_pdu`。

<a id="a3134e0bdb663ad7184e23531504233a5"></a>

### `phy`

```c
uint8_t bt_iso_unicast_tx_info::phy
```

传输物理层（Transport PHY）。

<a id="adc91f9c200199400a84322a58d28a933"></a>

### `sdu_interval`

```c
uint32_t bt_iso_unicast_tx_info::sdu_interval
```

服务数据单元间隔（SDU interval），单位为微秒。

若未知，可设为 `BT_ISO_SDU_INTERVAL_UNKNOWN`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_SDU_INTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4f0cc6262171fbee9d0ef173123b8f3d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_bt_iso_unicast_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_bt_le_adv_param_结构体.md)
