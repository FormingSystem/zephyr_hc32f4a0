---
id: learning.zephyr-docs.modem-wireless-model-reference.page-30
title: lora_modem_config_gfsk_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config__gfsk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_lora\_modem\_config\_gfsk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config__gfsk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含高斯频移键控（GFSK）调制解调器配置的结构。

```c
#include <zephyr/drivers/lora.h>
```

<a id="details"></a>

包含高斯频移键控（GFSK）调制解调器配置的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a9dd764760623f5ee04ea608cbc180c00"></a>

```c
uint32_t frequency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frequency](#a9dd764760623f5ee04ea608cbc180c00)。

收发使用的频率，单位为 Hz。

<a id="r_a24e0dd59c6b63672c546a52a54066186"></a>

```c
uint32_t bitrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bitrate](#a24e0dd59c6b63672c546a52a54066186)。

比特率（Bit rate），单位为 bit/s。

<a id="r_a2a8b2df70532bb82920431e2e013b5b0"></a>

```c
uint32_t freq_deviation
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[freq_deviation](#a2a8b2df70532bb82920431e2e013b5b0)。

发射频偏（frequency deviation），单位为 Hz。

<a id="r_a9fdc015f243dfe7bae02c69ae4028258"></a>

```c
uint32_t bandwidth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bandwidth](#a9fdc015f243dfe7bae02c69ae4028258)。

接收带宽，单位为 Hz，按覆盖两个边带的总宽度计算。

<a id="r_ab290c324797465c551e903df15a8eee3"></a>

```c
enum lora_gfsk_pulse_shape pulse_shape
```

相关声明：[lora_gfsk_pulse_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga6b74d80debd5a629af29aedc7b174118)、[pulse_shape](#ab290c324797465c551e903df15a8eee3)。

脉冲成形滤波器（Pulse shaping filter）。

<a id="r_aee3775468ec73b8cfa8347996a897445"></a>

```c
uint8_t sync_word [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sync_word](#aee3775468ec73b8cfa8347996a897445)。

要发送及用于匹配的同步字（sync word）。

<a id="r_a5c6b50a264eef09a4198e2116908f8b8"></a>

```c
uint8_t sync_word_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sync_word_len](#a5c6b50a264eef09a4198e2116908f8b8)。

同步字长度，单位为字节；0 表示不包含同步字。

<a id="r_a9b816ff8b4f215761399b5f7cd3b9f1e"></a>

```c
uint16_t preamble_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[preamble_len](#a9b816ff8b4f215761399b5f7cd3b9f1e)。

前导码长度，单位为字节，最大为 `LORA_GFSK_PREAMBLE_MAX`。

<a id="r_aadc6d35654c3158932080d4e7b5b5f9f"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#aadc6d35654c3158932080d4e7b5b5f9f)。

发射使用的发送功率（TX power），单位为 dBm。

<a id="r_a93b6c16da78ca973ba20549bc5ca833e"></a>

```c
bool tx
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tx](#a93b6c16da78ca973ba20549bc5ca833e)。

发送时设为 `true`，接收时设为 `false`。

<a id="r_a2868bdf2650e0e1082bac10357d8ab67"></a>

```c
bool whitening
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[whitening](#a2868bdf2650e0e1082bac10357d8ab67)。

对载荷进行白化（whitening），使发射频谱保持平坦。

<a id="r_afd0fe3012874bfb460283dbd6cba0a72"></a>

```c
bool fixed_len
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[fixed_len](#afd0fe3012874bfb460283dbd6cba0a72)。

发送并期望固定长度的载荷，而不在载荷前放置长度字节。

<a id="r_a5ae2b2c3e7e12db26a7ebc95b8146dcd"></a>

```c
uint8_t payload_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_len](#a5ae2b2c3e7e12db26a7ebc95b8146dcd)。

载荷长度，单位为字节，仅在设置了 `fixed_len` 时使用。

<a id="r_ad5ba923fe733374b23e1e67918d1fc5a"></a>

```c
bool packet_crc_disable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[packet_crc_disable](#ad5ba923fe733374b23e1e67918d1fc5a)。

设为 `true` 可禁用载荷的 CRC-16-CCITT 校验。

## 30.2\_详细说明（Detailed Documentation）

<a id="a9fdc015f243dfe7bae02c69ae4028258"></a>

### `bandwidth`

```c
uint32_t lora_modem_config_gfsk::bandwidth
```

接收带宽，单位为 Hz，按覆盖两个边带的总宽度计算。

无线收发器数据手册以这种方式描述信道滤波器，因此从手册复制的数值无需转换。如果规定给出的是单边带数值，则需要转换，因为它是这里所用总带宽的一半。

无线收发器提供一组固定的滤波器，因此驱动选择带宽至少达到此值的最窄滤波器；如果没有足够宽的滤波器，则拒绝该配置。

<a id="a24e0dd59c6b63672c546a52a54066186"></a>

### `bitrate`

```c
uint32_t lora_modem_config_gfsk::bitrate
```

比特率（Bit rate），单位为 bit/s。

<a id="afd0fe3012874bfb460283dbd6cba0a72"></a>

### `fixed_len`

```c
bool lora_modem_config_gfsk::fixed_len
```

发送并期望固定长度的载荷，而不在载荷前放置长度字节。

<a id="a2a8b2df70532bb82920431e2e013b5b0"></a>

### `freq_deviation`

```c
uint32_t lora_modem_config_gfsk::freq_deviation
```

发射频偏（frequency deviation），单位为 Hz。

<a id="a9dd764760623f5ee04ea608cbc180c00"></a>

### `frequency`

```c
uint32_t lora_modem_config_gfsk::frequency
```

收发使用的频率，单位为 Hz。

<a id="ad5ba923fe733374b23e1e67918d1fc5a"></a>

### `packet_crc_disable`

```c
bool lora_modem_config_gfsk::packet_crc_disable
```

设为 `true` 可禁用载荷的 CRC-16-CCITT 校验。

<a id="a5ae2b2c3e7e12db26a7ebc95b8146dcd"></a>

### `payload_len`

```c
uint8_t lora_modem_config_gfsk::payload_len
```

载荷长度，单位为字节，仅在设置了 `fixed_len` 时使用。

帧不携带长度字节，因此无线收发器恰好按时钟输出这么多字节；发送其他长度的数据会被拒绝。

<a id="a9b816ff8b4f215761399b5f7cd3b9f1e"></a>

### `preamble_len`

```c
uint16_t lora_modem_config_gfsk::preamble_len
```

前导码长度，单位为字节，最大为 `LORA_GFSK_PREAMBLE_MAX`。

<a id="ab290c324797465c551e903df15a8eee3"></a>

### `pulse_shape`

```c
enum lora_gfsk_pulse_shape lora_modem_config_gfsk::pulse_shape
```

脉冲成形滤波器（Pulse shaping filter）。

<a id="aee3775468ec73b8cfa8347996a897445"></a>

### `sync_word`

```c
uint8_t lora_modem_config_gfsk::sync_word[8]
```

要发送及用于匹配的同步字（sync word）。

<a id="a5c6b50a264eef09a4198e2116908f8b8"></a>

### `sync_word_len`

```c
uint8_t lora_modem_config_gfsk::sync_word_len
```

同步字长度，单位为字节；0 表示不包含同步字。

<a id="a93b6c16da78ca973ba20549bc5ca833e"></a>

### `tx`

```c
bool lora_modem_config_gfsk::tx
```

发送时设为 `true`，接收时设为 `false`。

<a id="aadc6d35654c3158932080d4e7b5b5f9f"></a>

### `tx_power`

```c
int8_t lora_modem_config_gfsk::tx_power
```

发射使用的发送功率（TX power），单位为 dBm。

<a id="a2868bdf2650e0e1082bac10357d8ab67"></a>

### `whitening`

```c
bool lora_modem_config_gfsk::whitening
```

对载荷进行白化（whitening），使发射频谱保持平坦。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lora.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lora.h](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lora_gfsk_pulse_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga6b74d80debd5a629af29aedc7b174118)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [LORA_GFSK_PREAMBLE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad59648fafcde1b76d7eb4d7c70b3a6af)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_lora_modem_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_lorawan_downlink_cb_结构体.md)
