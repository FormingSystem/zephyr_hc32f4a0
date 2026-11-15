---
id: learning.zephyr-docs.modem-wireless-model-reference.page-5
title: cellular_evt_network_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__network__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_cellular\_evt\_network\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__network__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CELLULAR_EVENT_NETWORK_STATUS_CHANGED事件的载荷（Payload）。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

CELLULAR_EVENT_NETWORK_STATUS_CHANGED事件的载荷（Payload）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a05560bf076d95474ab31446dae885929"></a>

```c
enum cellular_registration_status status
```

相关声明：[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)、[status](#a05560bf076d95474ab31446dae885929)。

注册状态（Registration status）。

<a id="r_ac8192ebc31182517665b27534bffc58c"></a>

```c
enum cellular_access_technology access_tech
```

相关声明：[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[access_tech](#ac8192ebc31182517665b27534bffc58c)。

接入技术（Access technology）。

```c
union {
```

```c
struct {
```

<a id="r_a90cae3dfeee4c11e9e2f3e53a80c3fb3"></a>

```c
uint16_t mcc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcc](#aeeae2197619a01211463ee194c643f59)。

移动国家代码（Mobile Country Code，MCC）。

<a id="r_ad23c47b4f9b9f51bac3128be0b05f8ed"></a>

```c
uint16_t mnc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mnc](#a745836b09443091c3bde36c948618e88)。

移动网络代码（Mobile Network Code，MNC）。

<a id="r_a79baae437c63e301e5bfcca312422482"></a>

```c
uint32_t tac
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tac](#a91a24ffc204b5a5aa02ed06f6595dbaa)。

跟踪区代码（Tracking Area Code，TAC）。

<a id="r_a1a4285b1e328e63f98ac7c0562f7fdc9"></a>

```c
uint32_t earfcn
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[earfcn](#af1e429365b99183adc51689e04ff1079)。

演进型通用陆地无线接入网（E-UTRAN）分配的无线信道。

<a id="r_a7f7bfc27d6dfe7fc68060c2d0cc3430f"></a>

```c
uint32_t gci
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gci](#aa74bd93e515506bf39ff5a7691982092)。

E-UTRAN 小区 ID，范围为 0 至 `CELLULAR_EUTRAN_CELL_ID_MAX`。

<a id="r_a6650230da71775506ee26289b77b5e5f"></a>

```c
uint16_t phys_cell_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[phys_cell_id](#a5bc9286d12c896dafceaa360fcf0ee88)。

物理小区 ID（Physical cell ID）。

<a id="r_a51a982444e6817e8c23fc6c75a743ddb"></a>

```c
uint16_t band
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[band](#a8cbeeb2f3c189d4c88cbc9cbbe126a1a)。

频段编号，取自 3GPP TS 36.101。

<a id="r_afe27e949fc6e7c723063755a45b5d8e3"></a>

```c
int16_t rsrp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rsrp](#adbd6f936f455eff7e3b9217bd7c1d3d4)。

接收信号功率，单位为 dBm。

<a id="r_a1024ada5a01f39da977aae8c29808df2"></a>

```c
int8_t rsrq
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rsrq](#a7bcc34cb84634f0486e522d489d91ca4)。

接收信号质量，单位为 dB。

<a id="r_aa1d7fccc49993c81018dc98048c85bcd"></a>

```c
} lte
```

相关声明：[lte](#a880a490f7b9d32e281db74c8514070ce)。

长期演进（LTE）小区信息。

<a id="r_aee20974803aa32c8fd6e6f4beacc16f9"></a>

```c
} cell
```

相关声明：[cell](#aee20974803aa32c8fd6e6f4beacc16f9)。

通用小区信息（Generic Cell information）。

## 5.2\_详细说明（Detailed Documentation）

<a id="ac8192ebc31182517665b27534bffc58c"></a>

### `access_tech`

```c
enum cellular_access_technology cellular_evt_network_status::access_tech
```

接入技术（Access technology）。

<a id="a8cbeeb2f3c189d4c88cbc9cbbe126a1a"></a>

### `band`

```c
uint16_t cellular_evt_network_status::band
```

频段编号，取自 3GPP TS 36.101。

<a id="aee20974803aa32c8fd6e6f4beacc16f9"></a>

### `[union]`

```c
union { ... } cellular_evt_network_status::cell
```

通用小区信息（Generic Cell information）。

<a id="af1e429365b99183adc51689e04ff1079"></a>

### `earfcn`

```c
uint32_t cellular_evt_network_status::earfcn
```

演进型通用陆地无线接入网（E-UTRAN）分配的无线信道。

<a id="aa74bd93e515506bf39ff5a7691982092"></a>

### `gci`

```c
uint32_t cellular_evt_network_status::gci
```

E-UTRAN 小区 ID，范围为 0 至 `CELLULAR_EUTRAN_CELL_ID_MAX`。

<a id="a880a490f7b9d32e281db74c8514070ce"></a>

### `[struct]`

```c
struct { ... } cellular_evt_network_status::lte
```

长期演进（LTE）小区信息。

<a id="aeeae2197619a01211463ee194c643f59"></a>

### `mcc`

```c
uint16_t cellular_evt_network_status::mcc
```

移动国家代码（Mobile Country Code，MCC）。

<a id="a745836b09443091c3bde36c948618e88"></a>

### `mnc`

```c
uint16_t cellular_evt_network_status::mnc
```

移动网络代码（Mobile Network Code，MNC）。

<a id="a5bc9286d12c896dafceaa360fcf0ee88"></a>

### `phys_cell_id`

```c
uint16_t cellular_evt_network_status::phys_cell_id
```

物理小区 ID（Physical cell ID）。

<a id="adbd6f936f455eff7e3b9217bd7c1d3d4"></a>

### `rsrp`

```c
int16_t cellular_evt_network_status::rsrp
```

接收信号功率，单位为 dBm。

<a id="a7bcc34cb84634f0486e522d489d91ca4"></a>

### `rsrq`

```c
int8_t cellular_evt_network_status::rsrq
```

接收信号质量，单位为 dB。

<a id="a05560bf076d95474ab31446dae885929"></a>

### `status`

```c
enum cellular_registration_status cellular_evt_network_status::status
```

注册状态（Registration status）。

<a id="a91a24ffc204b5a5aa02ed06f6595dbaa"></a>

### `tac`

```c
uint32_t cellular_evt_network_status::tac
```

跟踪区代码（Tracking Area Code，TAC）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 5.3\_原页交叉引用（Cross References）

- [CELLULAR_EVENT_NETWORK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_cellular_evt_modem_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_cellular_evt_registration_status_结构体.md)
