---
id: learning.zephyr-docs.modem-wireless-model-reference.page-70
title: sim7080_ue_sys_info_lte_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info__lte.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_sim7080\_ue\_sys\_info\_lte\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info__lte.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sim7080用户设备（UE）的LTE系统信息结构。

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

<a id="details"></a>

Sim7080用户设备（UE）的LTE系统信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a110fae03ebc62ef7ec83bd885d920f8a"></a>

```c
uint16_t mcc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcc](#a110fae03ebc62ef7ec83bd885d920f8a)。

移动国家代码（Mobile country code，MCC）。

<a id="r_a2978455bb41a4d1ae888aaa0e2242807"></a>

```c
uint16_t mcn
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcn](#a2978455bb41a4d1ae888aaa0e2242807)。

移动网络代码（Mobile network code，MNC）。

<a id="r_aed7ef4908901397958bc121138807c1e"></a>

```c
uint16_t tac
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tac](#aed7ef4908901397958bc121138807c1e)。

跟踪区代码（原文为 Tracing area code）。

<a id="r_aadfaabd5692fd42619edaf8c16c4efef"></a>

```c
uint32_t sci
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sci](#aadfaabd5692fd42619edaf8c16c4efef)。

服务小区 ID（Serving Cell ID）。

<a id="r_af0072ee8fa216a544b9b762672279ebd"></a>

```c
uint16_t pci
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pci](#af0072ee8fa216a544b9b762672279ebd)。

物理小区 ID（Physical Cell ID）。

<a id="r_ada937e5906995e3b0c1487bf572e30e5"></a>

```c
uint8_t band [32+1]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[band](#ada937e5906995e3b0c1487bf572e30e5)。

频段（Frequency band）。

<a id="r_adce93c6c4192d090c06622aaebaa87e0"></a>

```c
uint16_t earfcn
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[earfcn](#adce93c6c4192d090c06622aaebaa87e0)。

E-UTRA 绝对射频信道号（absolute radio frequency channel number）。

<a id="r_a0f6a10da2ac1b67f29cf3307597764ed"></a>

```c
uint16_t dlbw
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dlbw](#a0f6a10da2ac1b67f29cf3307597764ed)。

下行带宽，单位为 MHz。

<a id="r_acce77829b8bcc16d16367c1aec7d4323"></a>

```c
uint16_t ulbw
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ulbw](#acce77829b8bcc16d16367c1aec7d4323)。

上行带宽，单位为 MHz。

<a id="r_af3f5afa6ba5bc07de4f01886c7083a44"></a>

```c
int16_t rsrq
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rsrq](#af3f5afa6ba5bc07de4f01886c7083a44)。

参考信号接收质量（RSRQ），单位为 dB。

<a id="r_ae398efdcfd7c31e42ea135b334c51946"></a>

```c
int16_t rsrp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rsrp](#ae398efdcfd7c31e42ea135b334c51946)。

参考信号接收功率（RSRP），单位为 dBm。

<a id="r_a243f34e1ccd63716883f8246feeeb1b8"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a243f34e1ccd63716883f8246feeeb1b8)。

接收信号强度指示（RSSI），单位为 dBm。

<a id="r_a30b6a65590be8198f57baf54191c2d97"></a>

```c
int16_t rssnr
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssnr](#a30b6a65590be8198f57baf54191c2d97)。

参考信号信噪比（SNR），单位为 dB。

<a id="r_a2b230db49b10f285fded288664d25d9f"></a>

```c
int16_t sinr
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[sinr](#a2b230db49b10f285fded288664d25d9f)。

信号与干扰加噪声比（SINR），单位为 dB。

## 70.2\_详细说明（Detailed Documentation）

<a id="ada937e5906995e3b0c1487bf572e30e5"></a>

### `band`

```c
uint8_t sim7080_ue_sys_info_lte::band[32+1]
```

频段（Frequency band）。

<a id="a0f6a10da2ac1b67f29cf3307597764ed"></a>

### `dlbw`

```c
uint16_t sim7080_ue_sys_info_lte::dlbw
```

下行带宽，单位为 MHz。

<a id="adce93c6c4192d090c06622aaebaa87e0"></a>

### `earfcn`

```c
uint16_t sim7080_ue_sys_info_lte::earfcn
```

E-UTRA 绝对射频信道号（absolute radio frequency channel number）。

<a id="a110fae03ebc62ef7ec83bd885d920f8a"></a>

### `mcc`

```c
uint16_t sim7080_ue_sys_info_lte::mcc
```

移动国家代码（Mobile country code，MCC）。

<a id="a2978455bb41a4d1ae888aaa0e2242807"></a>

### `mcn`

```c
uint16_t sim7080_ue_sys_info_lte::mcn
```

移动网络代码（Mobile network code，MNC）。

<a id="af0072ee8fa216a544b9b762672279ebd"></a>

### `pci`

```c
uint16_t sim7080_ue_sys_info_lte::pci
```

物理小区 ID（Physical Cell ID）。

<a id="ae398efdcfd7c31e42ea135b334c51946"></a>

### `rsrp`

```c
int16_t sim7080_ue_sys_info_lte::rsrp
```

参考信号接收功率（RSRP），单位为 dBm。

<a id="af3f5afa6ba5bc07de4f01886c7083a44"></a>

### `rsrq`

```c
int16_t sim7080_ue_sys_info_lte::rsrq
```

参考信号接收质量（RSRQ），单位为 dB。

<a id="a243f34e1ccd63716883f8246feeeb1b8"></a>

### `rssi`

```c
int16_t sim7080_ue_sys_info_lte::rssi
```

接收信号强度指示（RSSI），单位为 dBm。

<a id="a30b6a65590be8198f57baf54191c2d97"></a>

### `rssnr`

```c
int16_t sim7080_ue_sys_info_lte::rssnr
```

参考信号信噪比（SNR），单位为 dB。

<a id="aadfaabd5692fd42619edaf8c16c4efef"></a>

### `sci`

```c
uint32_t sim7080_ue_sys_info_lte::sci
```

服务小区 ID（Serving Cell ID）。

<a id="a2b230db49b10f285fded288664d25d9f"></a>

### `sinr`

```c
int16_t sim7080_ue_sys_info_lte::sinr
```

信号与干扰加噪声比（SINR），单位为 dB。

<a id="aed7ef4908901397958bc121138807c1e"></a>

### `tac`

```c
uint16_t sim7080_ue_sys_info_lte::tac
```

跟踪区代码（原文为 Tracing area code）。

<a id="acce77829b8bcc16d16367c1aec7d4323"></a>

### `ulbw`

```c
uint16_t sim7080_ue_sys_info_lte::ulbw
```

上行带宽，单位为 MHz。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/simcom-sim7080.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/simcom-sim7080.h](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_sim7080_ue_sys_info_gsm_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_st87mxx_wifiscan_params_结构体.md)
