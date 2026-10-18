---
id: learning.zephyr-docs.modem-wireless-model-reference.page-31
title: lorawan_downlink_cb_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__downlink__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_lorawan\_downlink\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__downlink__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRaWAN下行链路（Downlink）的回调参数。

```c
#include <zephyr/lorawan/lorawan.h>
```

<a id="details"></a>

LoRaWAN下行链路（Downlink）的回调参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a0479e13faf06b99cf9023ebed8022131"></a>

```c
uint16_t port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port](#a0479e13faf06b99cf9023ebed8022131)。

要处理其消息的端口。

<a id="r_ae4f5e74bd927c650eba0d9b2f3978d8f"></a>

```c
void(* cb )(uint8_t port, uint8_t flags, int16_t rssi, int8_t snr, uint8_t len, const uint8_t *data)
```

相关声明：[cb](#ae4f5e74bd927c650eba0d9b2f3978d8f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[port](#a0479e13faf06b99cf9023ebed8022131)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

收到下行数据时执行的回调函数。

<a id="r_ad54df4a4ab38003d59f82b19fb16f5fd"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ad54df4a4ab38003d59f82b19fb16f5fd)。

回调列表节点。

## 31.2\_详细说明（Detailed Documentation）

<a id="ae4f5e74bd927c650eba0d9b2f3978d8f"></a>

### `cb`

```c
void(* lorawan_downlink_cb::cb) (uint8_t port, uint8_t flags, int16_t rssi, int8_t snr, uint8_t len, const uint8_t *data)
```

收到下行数据时执行的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 消息发送所使用的端口。 |
| `flags` | 下行数据标志，参见 `lorawan_dl_flags`。 |
| `rssi` | 接收信号强度，单位为 dBm。 |
| `snr` | 信噪比（Signal to Noise ratio），原文单位为 dBm。

译注：原页此处将信噪比单位写作 dBm；本译文保留该表述供对照。 |
| `len` | 接收数据的长度；对于确认消息（ACK）为 0。 |
| `data` | 接收的数据；对于确认消息（ACK）为 `NULL`。 |

**说明（Note）**：注意：回调在系统工作队列（system workqueue）中执行，因此应尽可能简短。

<a id="ad54df4a4ab38003d59f82b19fb16f5fd"></a>

### `node`

```c
sys_snode_t lorawan_downlink_cb::node
```

回调列表节点。

<a id="a0479e13faf06b99cf9023ebed8022131"></a>

### `port`

```c
uint16_t lorawan_downlink_cb::port
```

要处理其消息的端口。

- 端口 0：发送（TX）数据包确认。
- 端口 1 至 255：标准下行端口。
- `LW_RECV_PORT_ANY`：所有下行消息。

本数据类型文档由以下文件生成：

- `zephyr/lorawan/lorawan.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/lorawan/lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [lorawan_dl_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab28a9f22482069b2246892e4ee31660d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_lora_modem_config_gfsk_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_lorawan_join_abp_结构体.md)
