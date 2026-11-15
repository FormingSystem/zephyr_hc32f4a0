---
id: learning.zephyr-docs.modem-wireless-model-reference.page-29
title: lora_modem_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_lora\_modem\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含LoRa调制解调器（Modem）配置的结构。

```c
#include <zephyr/drivers/lora.h>
```

<a id="details"></a>

包含LoRa调制解调器（Modem）配置的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a08209a2dabc5111025810fc8e141c2df"></a>

```c
uint32_t frequency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frequency](#a08209a2dabc5111025810fc8e141c2df)。

收发使用的频率，单位为 Hz。

<a id="r_a0c6a90e31b4a97d962af3dbd0ee8e885"></a>

```c
enum lora_signal_bandwidth bandwidth
```

相关声明：[lora_signal_bandwidth](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gabb5feb9d1a2bb160d9b55939efb17136)、[bandwidth](#a0c6a90e31b4a97d962af3dbd0ee8e885)。

收发使用的带宽（bandwidth）。

<a id="r_ae438c1c223f12fc6c3747d4297ec61ba"></a>

```c
enum lora_datarate datarate
```

相关声明：[lora_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga30bfeb2e6f4e35869996b597b614becb)、[datarate](#ae438c1c223f12fc6c3747d4297ec61ba)。

收发使用的数据率（data rate）。

<a id="r_a8e47a8506265562c7b118fab72cceb10"></a>

```c
enum lora_coding_rate coding_rate
```

相关声明：[lora_coding_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5af378491814d0d3a059cd6cd39265c8)、[coding_rate](#a8e47a8506265562c7b118fab72cceb10)。

收发使用的编码率（coding rate）。

<a id="r_a9d0795c5be6ae0042babaa05615cf7f2"></a>

```c
uint16_t preamble_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[preamble_len](#a9d0795c5be6ae0042babaa05615cf7f2)。

前导码（preamble）长度。

<a id="r_a41a194d62e1e3e1b142e194a75efb8a1"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a41a194d62e1e3e1b142e194a75efb8a1)。

发射使用的发送功率（TX power），单位为 dBm。

<a id="r_af5ef0c5e3443a011d2ed6af3c95cc4db"></a>

```c
uint8_t sync_word
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sync_word](#af5ef0c5e3443a011d2ed6af3c95cc4db)。

使用显式同步字（sync word）覆盖 `public_network`。

<a id="r_a10b12a2092712050bdd64c6250c8731f"></a>

```c
bool tx
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tx](#a10b12a2092712050bdd64c6250c8731f)。

发送时设为 `true`，接收时设为 `false`。

<a id="r_a5737749b3bd29515887bb0b8c48c8bd1"></a>

```c
bool iq_inverted
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[iq_inverted](#a5737749b3bd29515887bb0b8c48c8bd1)。

反转同相与正交（In-Phase and Quadrature，IQ）信号。

<a id="r_af97fde1f5f40a4d702c0140872728e86"></a>

```c
bool public_network
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[public_network](#af97fde1f5f40a4d702c0140872728e86)。

设置要使用的同步字节（sync-byte）：

<a id="r_a3c9f32935f253df5e1ee67c5aab7795c"></a>

```c
bool packet_crc_disable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[packet_crc_disable](#a3c9f32935f253df5e1ee67c5aab7795c)。

设为 `true` 可禁用载荷的 16 位循环冗余校验（CRC）。

```c
struct {
```

<a id="r_ae1d607435f586e179c3012e9c57306b0"></a>

```c
enum lora_cad_mode mode
```

相关声明：[lora_cad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga22c381e69be5cc630e283e8f5dfa940a)、[mode](#adc1f228bbba786608fbb66df2b34aa51)。

信道活动检测（CAD）模式。

<a id="r_a267864a8c209345b01463ab67c4e6ad0"></a>

```c
enum lora_cad_symbol_num symbol_num
```

相关声明：[lora_cad_symbol_num](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga0b6af528164f65b590295882590e7c7f)、[symbol_num](#ad12a48ff7aaa815a34e888aff839c389)。

CAD 检测使用的符号数量。

<a id="r_a717160f90397a9b82d14377c2f4ce7c7"></a>

```c
uint8_t detection_peak
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[detection_peak](#a43d01b02bfc4e1a801ea04aa3d0f0518)。

检测峰值阈值（detection peak threshold），与硬件相关，无量纲。

<a id="r_ab87d9927864f0fd1930ffc51e90b20b1"></a>

```c
uint8_t detection_minimum
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[detection_minimum](#ae9442b595916150367086e93e833aa68)。

最小检测阈值（minimum detection threshold），与硬件相关，无量纲。

<a id="r_a05681aa7e1423be4b0582164bc1b02a6"></a>

```c
} cad
```

相关声明：[cad](#a05681aa7e1423be4b0582164bc1b02a6)。

信道活动检测（Channel Activity Detection）参数。

## 29.2\_详细说明（Detailed Documentation）

<a id="a0c6a90e31b4a97d962af3dbd0ee8e885"></a>

### `bandwidth`

```c
enum lora_signal_bandwidth lora_modem_config::bandwidth
```

收发使用的带宽（bandwidth）。

<a id="a05681aa7e1423be4b0582164bc1b02a6"></a>

### `[struct]`

```c
struct { ... } lora_modem_config::cad
```

信道活动检测（Channel Activity Detection）参数。

<a id="a8e47a8506265562c7b118fab72cceb10"></a>

### `coding_rate`

```c
enum lora_coding_rate lora_modem_config::coding_rate
```

收发使用的编码率（coding rate）。

<a id="ae438c1c223f12fc6c3747d4297ec61ba"></a>

### `datarate`

```c
enum lora_datarate lora_modem_config::datarate
```

收发使用的数据率（data rate）。

<a id="ae9442b595916150367086e93e833aa68"></a>

### `detection_minimum`

```c
uint8_t lora_modem_config::detection_minimum
```

最小检测阈值（minimum detection threshold），与硬件相关，无量纲。

直接传给无线收发器。0 表示根据扩频因子和带宽（SF/BW）自动推导。

<a id="a43d01b02bfc4e1a801ea04aa3d0f0518"></a>

### `detection_peak`

```c
uint8_t lora_modem_config::detection_peak
```

检测峰值阈值（detection peak threshold），与硬件相关，无量纲。

直接传给无线收发器。0 表示根据扩频因子和带宽（SF/BW）自动推导。

<a id="a08209a2dabc5111025810fc8e141c2df"></a>

### `frequency`

```c
uint32_t lora_modem_config::frequency
```

收发使用的频率，单位为 Hz。

<a id="a5737749b3bd29515887bb0b8c48c8bd1"></a>

### `iq_inverted`

```c
bool lora_modem_config::iq_inverted
```

反转同相与正交（In-Phase and Quadrature，IQ）信号。

通常应设为 `false`。在需要区分上行和下行流量的高级用例中，可反转 IQ，在同一频率上创建两个不同的信道。

<a id="adc1f228bbba786608fbb66df2b34aa51"></a>

### `mode`

```c
enum lora_cad_mode lora_modem_config::mode
```

信道活动检测（CAD）模式。

详情参见 `lora_cad_mode`。

<a id="a3c9f32935f253df5e1ee67c5aab7795c"></a>

### `packet_crc_disable`

```c
bool lora_modem_config::packet_crc_disable
```

设为 `true` 可禁用载荷的 16 位循环冗余校验（CRC）。

<a id="a9d0795c5be6ae0042babaa05615cf7f2"></a>

### `preamble_len`

```c
uint16_t lora_modem_config::preamble_len
```

前导码（preamble）长度。

<a id="af97fde1f5f40a4d702c0140872728e86"></a>

### `public_network`

```c
bool lora_modem_config::public_network
```

设置要使用的同步字节（sync-byte）：

- `false`：使用私有网络同步字节（private network sync-byte）。
- `true`：使用公共网络同步字节（public network sync-byte）。公共网络同步字节仅供高级用法使用。通常，点对点通信应使用私有网络同步字节，与公共网络交互应使用 LoRaWAN API。

<a id="ad12a48ff7aaa815a34e888aff839c389"></a>

### `symbol_num`

```c
enum lora_cad_symbol_num lora_modem_config::symbol_num
```

CAD 检测使用的符号数量。

0 表示使用驱动默认值。

<a id="af5ef0c5e3443a011d2ed6af3c95cc4db"></a>

### `sync_word`

```c
uint8_t lora_modem_config::sync_word
```

使用显式同步字（sync word）覆盖 `public_network`。

对旧版 `loramac-node` 后端无效。必须是 `0x00` 以外的值。

<a id="a10b12a2092712050bdd64c6250c8731f"></a>

### `tx`

```c
bool lora_modem_config::tx
```

发送时设为 `true`，接收时设为 `false`。

<a id="a41a194d62e1e3e1b142e194a75efb8a1"></a>

### `tx_power`

```c
int8_t lora_modem_config::tx_power
```

发射使用的发送功率（TX power），单位为 dBm。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lora.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lora.h](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lora_signal_bandwidth](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gabb5feb9d1a2bb160d9b55939efb17136)
- [lora_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga30bfeb2e6f4e35869996b597b614becb)
- [lora_coding_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5af378491814d0d3a059cd6cd39265c8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [lora_cad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga22c381e69be5cc630e283e8f5dfa940a)
- [lora_cad_symbol_num](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga0b6af528164f65b590295882590e7c7f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_lora_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_lora_modem_config_gfsk_结构体.md)
