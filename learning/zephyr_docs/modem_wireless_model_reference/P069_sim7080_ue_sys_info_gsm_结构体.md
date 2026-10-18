---
id: learning.zephyr-docs.modem-wireless-model-reference.page-69
title: sim7080_ue_sys_info_gsm_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info__gsm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_sim7080\_ue\_sys\_info\_gsm\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info__gsm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sim7080用户设备（UE）的GSM系统信息结构。

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

<a id="details"></a>

Sim7080用户设备（UE）的GSM系统信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_ae12054693fa10b41be19ebcad14f1683"></a>

```c
uint16_t mcc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcc](#ae12054693fa10b41be19ebcad14f1683)。

移动国家代码（Mobile country code，MCC）。

<a id="r_a481f9b9426f6deebeb019bf7f7d61e03"></a>

```c
uint16_t mcn
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcn](#a481f9b9426f6deebeb019bf7f7d61e03)。

移动网络代码（Mobile network code，MNC）。

<a id="r_a6514320e087362edf623e1b35ac2f4ec"></a>

```c
uint16_t lac
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[lac](#a6514320e087362edf623e1b35ac2f4ec)。

位置区代码（Location area code，LAC）。

<a id="r_a7109571a82f669173c0dffbfc91e6706"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a7109571a82f669173c0dffbfc91e6706)。

小区 ID（Cell ID）。

<a id="r_a84678a3a6dbdbf0f4e2cecfd7ebfe96a"></a>

```c
uint8_t arfcn [32+1]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[arfcn](#a84678a3a6dbdbf0f4e2cecfd7ebfe96a)。

绝对射频信道号（Absolute radio frequency channel number，ARFCN）。

<a id="r_ac15deea095cc6316bb56505be968ad92"></a>

```c
int16_t rx_lvl
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rx_lvl](#ac15deea095cc6316bb56505be968ad92)。

接收电平（RX level），单位为 dBm。

<a id="r_a91dc051575f95177042aa63fbea8b409"></a>

```c
int16_t track_lo_adjust
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[track_lo_adjust](#a91dc051575f95177042aa63fbea8b409)。

跟踪本地振荡器调整值（Track LO adjust）。

<a id="r_a7566a16cdd2a7ffbcbb575cce97c0dd8"></a>

```c
uint16_t c1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c1](#a7566a16cdd2a7ffbcbb575cce97c0dd8)。

C1 系数（coefficient）。

<a id="r_a60b655f5dd03137c67f3990d9584f579"></a>

```c
uint16_t c2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c2](#a60b655f5dd03137c67f3990d9584f579)。

C2 系数（coefficient）。

## 69.2\_详细说明（Detailed Documentation）

<a id="a84678a3a6dbdbf0f4e2cecfd7ebfe96a"></a>

### `arfcn`

```c
uint8_t sim7080_ue_sys_info_gsm::arfcn[32+1]
```

绝对射频信道号（Absolute radio frequency channel number，ARFCN）。

<a id="a7566a16cdd2a7ffbcbb575cce97c0dd8"></a>

### `c1`

```c
uint16_t sim7080_ue_sys_info_gsm::c1
```

C1 系数（coefficient）。

<a id="a60b655f5dd03137c67f3990d9584f579"></a>

### `c2`

```c
uint16_t sim7080_ue_sys_info_gsm::c2
```

C2 系数（coefficient）。

<a id="a7109571a82f669173c0dffbfc91e6706"></a>

### `cid`

```c
uint16_t sim7080_ue_sys_info_gsm::cid
```

小区 ID（Cell ID）。

<a id="a6514320e087362edf623e1b35ac2f4ec"></a>

### `lac`

```c
uint16_t sim7080_ue_sys_info_gsm::lac
```

位置区代码（Location area code，LAC）。

<a id="ae12054693fa10b41be19ebcad14f1683"></a>

### `mcc`

```c
uint16_t sim7080_ue_sys_info_gsm::mcc
```

移动国家代码（Mobile country code，MCC）。

<a id="a481f9b9426f6deebeb019bf7f7d61e03"></a>

### `mcn`

```c
uint16_t sim7080_ue_sys_info_gsm::mcn
```

移动网络代码（Mobile network code，MNC）。

<a id="ac15deea095cc6316bb56505be968ad92"></a>

### `rx_lvl`

```c
int16_t sim7080_ue_sys_info_gsm::rx_lvl
```

接收电平（RX level），单位为 dBm。

<a id="a91dc051575f95177042aa63fbea8b409"></a>

### `track_lo_adjust`

```c
int16_t sim7080_ue_sys_info_gsm::track_lo_adjust
```

跟踪本地振荡器调整值（Track LO adjust）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/simcom-sim7080.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/simcom-sim7080.h](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_sim7080_ue_sys_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_sim7080_ue_sys_info_lte_结构体.md)
