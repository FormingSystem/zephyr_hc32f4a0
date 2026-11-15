---
id: learning.zephyr-docs.device-power-control-model-reference.page-115
title: pd_rdo_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__rdo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_pd\_rdo\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__rdo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

请求数据对象（Request Data Object，RDO）应由提出供电请求的受电端（Sink）返回。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

请求电力的受电方（Sink）必须返回请求数据对象（Request Data Object，RDO）。参见第 6.4.2 节“请求消息”（Request Message）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 115.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a179e1af07d64fd6b4138c585d8d486fd"></a>

```c
uint32_t min_or_max_operating_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_or_max_operating_current](#a41d023e9308e6d252f0bc8412a6c6184)。

工作电流，以 10 mA 为单位。注意：归还标志（Give Back Flag）为零时，此字段表示最大工作电流（Maximum Operating Current）。

<a id="r_ae8ed0edd0c4128fcc0d2c2f238cc3643"></a>

```c
uint32_t operating_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operating_current](#a8c11df4b75772cda511bd94e5a297128)。

工作电流，以 10 mA 为单位。

<a id="r_a591651e4cc543c584a52114c87171b0b"></a>

```c
uint32_t reserved0: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#ab4065aee18c3a68df38592122f607343)。

保留，必须设为零。

<a id="r_a2e40e5560de48c458281f4f8ac114b33"></a>

```c
uint32_t unchunked_ext_msg_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unchunked_ext_msg_supported](#ae71e9abde3d69211c7bcfc7b80d18c41)。

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="r_afd24f4916786c957b24ef386cf508d93"></a>

```c
uint32_t no_usb_suspend: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[no_usb_suspend](#ae90a23cc166373f7bb3c35be0c3967f2)。

不挂起 USB（No USB Suspend）。

<a id="r_aebc73a63ad5ed65011d2de6f59e4e045"></a>

```c
uint32_t usb_comm_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comm_capable](#a30f6044378cad6f277f8694df5611230)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_af1eeebaa7cf68c6b1c594d7ab1ce2d40"></a>

```c
uint32_t cap_mismatch: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cap_mismatch](#afd24863b120085c57e77b8d246effd54)。

能力不匹配（Capability Mismatch）。

<a id="r_aed8c80915a063716479876014f7ce1c7"></a>

```c
uint32_t giveback: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[giveback](#ae5ae5d3c823254ab895becc3b01761fe)。

归还标志（Give Back Flag）。

<a id="r_aaad089b6aa75715c43acf88ad67a6371"></a>

```c
uint32_t object_pos: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[object_pos](#aff1b20a6e4905ac714ab5e7af7ff9593)。

对象位置（Object Position）；`000b` 为保留值，禁止使用。

<a id="r_a0576b803435acddbe2b59c897dfb2a27"></a>

```c
uint32_t reserved1: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba)。

保留，必须设为零。

<a id="r_a0b7502c79b0976b8e0d118cae3950191"></a>

```c
} fixed
```

相关声明：[fixed](#a0b7502c79b0976b8e0d118cae3950191)。

创建固定供电 RDO 值。参见表 6-19“固定与可变请求数据对象”（Fixed and Variable Request Data Object）。

```c
struct {
```

<a id="r_a156289f23f3374f2f3bbbc33ba33802e"></a>

```c
uint32_t min_or_max_operating_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_or_max_operating_current](#a41d023e9308e6d252f0bc8412a6c6184)。

工作电流，以 10 mA 为单位。注意：归还标志（Give Back Flag）为零时，此字段表示最大工作电流（Maximum Operating Current）。

<a id="r_a6bfade7879e2a53a88593193aabe08e9"></a>

```c
uint32_t operating_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operating_current](#a8c11df4b75772cda511bd94e5a297128)。

工作电流，以 10 mA 为单位。

<a id="r_a87784d9142e542fae1453684e0146751"></a>

```c
uint32_t reserved0: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#ab4065aee18c3a68df38592122f607343)。

保留，必须设为零。

<a id="r_a3e386af4677b86c2f76e9c2e8bc776ad"></a>

```c
uint32_t unchunked_ext_msg_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unchunked_ext_msg_supported](#ae71e9abde3d69211c7bcfc7b80d18c41)。

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="r_ad9c6d42d6b4d385ee0c4c886ab8fcd78"></a>

```c
uint32_t no_usb_suspend: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[no_usb_suspend](#ae90a23cc166373f7bb3c35be0c3967f2)。

不挂起 USB（No USB Suspend）。

<a id="r_a795ce2892d58ccaac6539eac6c917a73"></a>

```c
uint32_t usb_comm_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comm_capable](#a30f6044378cad6f277f8694df5611230)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_a6861f7e114715ae776cac734a05aff68"></a>

```c
uint32_t cap_mismatch: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cap_mismatch](#afd24863b120085c57e77b8d246effd54)。

能力不匹配（Capability Mismatch）。

<a id="r_a482fd8175f7b0bd32146e4ace3c9b506"></a>

```c
uint32_t giveback: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[giveback](#ae5ae5d3c823254ab895becc3b01761fe)。

归还标志（Give Back Flag）。

<a id="r_a946e29abd5e9469354101e2a8f9092b4"></a>

```c
uint32_t object_pos: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[object_pos](#aff1b20a6e4905ac714ab5e7af7ff9593)。

对象位置（Object Position）；`000b` 为保留值，禁止使用。

<a id="r_a367d17687cf827ff88fe180ed451350d"></a>

```c
uint32_t reserved1: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba)。

保留，必须设为零。

<a id="r_a82e1adf30b6fc476b794b94cfb379214"></a>

```c
} variable
```

相关声明：[variable](#a82e1adf30b6fc476b794b94cfb379214)。

创建可变供电 RDO 值。参见表 6-19“固定与可变请求数据对象”（Fixed and Variable Request Data Object）。

```c
struct {
```

<a id="r_a443bbf1ff1062773c6aef0461f56b1ad"></a>

```c
uint32_t min_operating_power: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_operating_power](#ab59da7098c1d33c9269f66dd3ac3fc5b)。

最小工作功率，以 250 mW 为单位。

<a id="r_ae449edacf491dd7a8173d14741c166ce"></a>

```c
uint32_t operating_power: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operating_power](#a63dd2a9e94f3a61205b95efc0cf79f13)。

工作功率，以 250 mW 为单位。

<a id="r_aa46bc8f218b00e2563d046f5b8f211c5"></a>

```c
uint32_t reserved0: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#ab4065aee18c3a68df38592122f607343)。

保留，必须设为零。

<a id="r_a28f4cdce8c018e1dbd831e8e426c07c2"></a>

```c
uint32_t unchunked_ext_msg_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unchunked_ext_msg_supported](#ae71e9abde3d69211c7bcfc7b80d18c41)。

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="r_a78f902a8a77d12754e97e408f3e5adf1"></a>

```c
uint32_t no_usb_suspend: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[no_usb_suspend](#ae90a23cc166373f7bb3c35be0c3967f2)。

不挂起 USB（No USB Suspend）。

<a id="r_a7552b3d31966e9e0b99553c966c6b969"></a>

```c
uint32_t usb_comm_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comm_capable](#a30f6044378cad6f277f8694df5611230)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_ab4b040211fc339c3a128e408d678a3a9"></a>

```c
uint32_t cap_mismatch: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cap_mismatch](#afd24863b120085c57e77b8d246effd54)。

能力不匹配（Capability Mismatch）。

<a id="r_a864835b1b6586f00e7bd38d65933b3d8"></a>

```c
uint32_t giveback: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[giveback](#ae5ae5d3c823254ab895becc3b01761fe)。

归还标志（Give Back Flag）。

<a id="r_a7e69bbe541db8d7d9d2edbcbb274fb24"></a>

```c
uint32_t object_pos: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[object_pos](#aff1b20a6e4905ac714ab5e7af7ff9593)。

对象位置（Object Position）；`000b` 为保留值，禁止使用。

<a id="r_a0dcd339280f9a587611f744b062d6fff"></a>

```c
uint32_t reserved1: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba)。

保留，必须设为零。

<a id="r_a5838022e249981be50aee897c16ce56e"></a>

```c
} battery
```

相关声明：[battery](#a5838022e249981be50aee897c16ce56e)。

创建电池供电 RDO 值。参见表 6-20“电池请求数据对象”（Battery Request Data Object）。

```c
struct {
```

<a id="r_acf327be873dbd079d648ed0c8c9b8600"></a>

```c
uint32_t operating_current: 7
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operating_current](#a8c11df4b75772cda511bd94e5a297128)。

工作电流，以 50 mA 为单位。

<a id="r_af30092f633eb6a76d4d3d07d7f8fc015"></a>

```c
uint32_t reserved0: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#ab4065aee18c3a68df38592122f607343)。

保留，必须设为零。

<a id="r_acb5e1f12f28a5de2369c3e3d583bc3b2"></a>

```c
uint32_t output_voltage: 11
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[output_voltage](#ad7a98411aad054f1161b4ce32ef3ee33)。

输出电压，以 20 mV 为单位。

<a id="r_af97f02fa07fe76cc9d7733e5b4946420"></a>

```c
uint32_t reserved1: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#aa5af5685e6d9c3d8a7ec3a40d25b43ba)。

保留，必须设为零。

<a id="r_acfcfd5d7dc751b6e5ca03065b086fc34"></a>

```c
uint32_t unchunked_ext_msg_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unchunked_ext_msg_supported](#ae71e9abde3d69211c7bcfc7b80d18c41)。

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="r_a80d03570f4b2e80039a89b84ab4515a8"></a>

```c
uint32_t no_usb_suspend: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[no_usb_suspend](#ae90a23cc166373f7bb3c35be0c3967f2)。

不挂起 USB（No USB Suspend）。

<a id="r_a955ae501bfb0937961115204cb2eb50a"></a>

```c
uint32_t usb_comm_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comm_capable](#a30f6044378cad6f277f8694df5611230)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_aed756f6ed474950bd64db28888b6df75"></a>

```c
uint32_t cap_mismatch: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cap_mismatch](#afd24863b120085c57e77b8d246effd54)。

能力不匹配（Capability Mismatch）。

<a id="r_a53f95ac09cb4b2fa5cc4aaf9409c1034"></a>

```c
uint32_t reserved2: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved2](#a5f8b64ce53d9881a007405a986b6b490)。

保留，必须设为零。

<a id="r_a5f1de8c43c8fecc8c22e12c992963655"></a>

```c
uint32_t object_pos: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[object_pos](#aff1b20a6e4905ac714ab5e7af7ff9593)。

对象位置（Object Position）；`000b` 为保留值，禁止使用。

<a id="r_ac1cc4f3286638a3fd1f050b88e411bde"></a>

```c
uint32_t reserved3: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved3](#aa0ddbfb3c345b671f97d4b4e760168b4)。

保留，必须设为零。

<a id="r_ad6b45a879e689dcd05bf9e07aedc4d20"></a>

```c
} augmented
```

相关声明：[augmented](#ad6b45a879e689dcd05bf9e07aedc4d20)。

创建增强 RDO 值。参见表 6-22“可编程请求数据对象”（Programmable Request Data Object）。

<a id="r_a477cf38b68b9386e950c085a1ce4f336"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#a477cf38b68b9386e950c085a1ce4f336)。

原始 RDO 值。

## 115.2\_详细说明（Detailed Documentation）

<a id="ad6b45a879e689dcd05bf9e07aedc4d20"></a>

### `[struct]`

```c
struct { ... } pd_rdo::augmented
```

创建增强 RDO 值。参见表 6-22“可编程请求数据对象”（Programmable Request Data Object）。

<a id="a5838022e249981be50aee897c16ce56e"></a>

### `[struct]`

```c
struct { ... } pd_rdo::battery
```

创建电池供电 RDO 值。参见表 6-20“电池请求数据对象”（Battery Request Data Object）。

<a id="afd24863b120085c57e77b8d246effd54"></a>

### `cap_mismatch`

```c
uint32_t pd_rdo::cap_mismatch
```

能力不匹配（Capability Mismatch）。

<a id="a0b7502c79b0976b8e0d118cae3950191"></a>

### `[struct]`

```c
struct { ... } pd_rdo::fixed
```

创建固定供电 RDO 值。参见表 6-19“固定与可变请求数据对象”（Fixed and Variable Request Data Object）。

<a id="ae5ae5d3c823254ab895becc3b01761fe"></a>

### `giveback`

```c
uint32_t pd_rdo::giveback
```

归还标志（Give Back Flag）。

<a id="ab59da7098c1d33c9269f66dd3ac3fc5b"></a>

### `min_operating_power`

```c
uint32_t pd_rdo::min_operating_power
```

最小工作功率，以 250 mW 为单位。

<a id="a41d023e9308e6d252f0bc8412a6c6184"></a>

### `min_or_max_operating_current`

```c
uint32_t pd_rdo::min_or_max_operating_current
```

工作电流，以 10 mA 为单位。注意：归还标志（Give Back Flag）为零时，此字段表示最大工作电流（Maximum Operating Current）。

归还标志（Give Back Flag）为 `1` 时，此字段表示最小工作电流（Minimum Operating Current）。

<a id="ae90a23cc166373f7bb3c35be0c3967f2"></a>

### `no_usb_suspend`

```c
uint32_t pd_rdo::no_usb_suspend
```

不挂起 USB（No USB Suspend）。

<a id="aff1b20a6e4905ac714ab5e7af7ff9593"></a>

### `object_pos`

```c
uint32_t pd_rdo::object_pos
```

对象位置（Object Position）；`000b` 为保留值，禁止使用。

<a id="a8c11df4b75772cda511bd94e5a297128"></a>

### `operating_current`

```c
uint32_t pd_rdo::operating_current
```

工作电流，以 10 mA 为单位。

工作电流，以 50 mA 为单位。

<a id="a63dd2a9e94f3a61205b95efc0cf79f13"></a>

### `operating_power`

```c
uint32_t pd_rdo::operating_power
```

工作功率，以 250 mW 为单位。

<a id="ad7a98411aad054f1161b4ce32ef3ee33"></a>

### `output_voltage`

```c
uint32_t pd_rdo::output_voltage
```

输出电压，以 20 mV 为单位。

<a id="a477cf38b68b9386e950c085a1ce4f336"></a>

### `raw_value`

```c
uint32_t pd_rdo::raw_value
```

原始 RDO 值。

<a id="ab4065aee18c3a68df38592122f607343"></a>

### `reserved0`

```c
uint32_t pd_rdo::reserved0
```

保留，必须设为零。

<a id="aa5af5685e6d9c3d8a7ec3a40d25b43ba"></a>

### `reserved1`

```c
uint32_t pd_rdo::reserved1
```

保留，必须设为零。

<a id="a5f8b64ce53d9881a007405a986b6b490"></a>

### `reserved2`

```c
uint32_t pd_rdo::reserved2
```

保留，必须设为零。

<a id="aa0ddbfb3c345b671f97d4b4e760168b4"></a>

### `reserved3`

```c
uint32_t pd_rdo::reserved3
```

保留，必须设为零。

<a id="ae71e9abde3d69211c7bcfc7b80d18c41"></a>

### `unchunked_ext_msg_supported`

```c
uint32_t pd_rdo::unchunked_ext_msg_supported
```

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="a30f6044378cad6f277f8694df5611230"></a>

### `usb_comm_capable`

```c
uint32_t pd_rdo::usb_comm_capable
```

具备 USB 通信能力（USB Communications Capable）。

<a id="a82e1adf30b6fc476b794b94cfb379214"></a>

### `[struct]`

```c
struct { ... } pd_rdo::variable
```

创建可变供电 RDO 值。参见表 6-19“固定与可变请求数据对象”（Fixed and Variable Request Data Object）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 115.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P114_pd_header_联合体.md) · [返回大纲](大纲.md) · [下一章](P116_pd_variable_supply_pdo_sink_联合体.md)
