---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-36
title: bt_conn_le_tx_power_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__tx__power__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_bt\_conn\_le\_tx\_power\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__tx__power__report.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 发射功率报告（Transmit Power Reporting）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 发射功率报告（Transmit Power Reporting）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_aa5606925229784af8ae90542432cf200"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#aa5606925229784af8ae90542432cf200)。

核心规范（Core Spec.）中定义的发射功率报告原因（Reason for Transmit power reporting）。

<a id="r_a5b1f67537fbe945f2f258b47082723b4"></a>

```c
enum bt_conn_le_tx_power_phy phy
```

相关声明：[bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)、[phy](#a5b1f67537fbe945f2f258b47082723b4)。

发射功率报告的物理层（PHY）。

<a id="r_ace830ddb7ae662c9759babed87f1b6f3"></a>

```c
int8_t tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_level](#ace830ddb7ae662c9759babed87f1b6f3)。

发射功率等级（Transmit power level）。

<a id="r_ae7a4f77c6f7af1a459896d25cf661eb8"></a>

```c
uint8_t tx_power_level_flag
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_power_level_flag](#ae7a4f77c6f7af1a459896d25cf661eb8)。

位 0：发射功率等级处于最低等级（Minimum level）。

<a id="r_a7c681c7b9f77d994b2de1febea7c5dc9"></a>

```c
int8_t delta
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[delta](#a7c681c7b9f77d994b2de1febea7c5dc9)。

发射功率等级变化量（Change in transmit power level）。

## 36.2\_详细说明（Detailed Documentation）

<a id="a7c681c7b9f77d994b2de1febea7c5dc9"></a>

### `delta`

```c
int8_t bt_conn_le_tx_power_report::delta
```

发射功率等级变化量（Change in transmit power level）。

- `0xXX`：发射功率等级变化量（Change in transmit power level）；正数表示增加，负数表示降低，零表示不变。单位为 dB。
- `0x7F`：变化量不可用或超出范围（Out of range）。

<a id="a5b1f67537fbe945f2f258b47082723b4"></a>

### `phy`

```c
enum bt_conn_le_tx_power_phy bt_conn_le_tx_power_report::phy
```

发射功率报告的物理层（PHY）。

<a id="aa5606925229784af8ae90542432cf200"></a>

### `reason`

```c
uint8_t bt_conn_le_tx_power_report::reason
```

核心规范（Core Spec.）中定义的发射功率报告原因（Reason for Transmit power reporting）。

5.4 版第 4 卷 E 部分第 7.7.65.33 节。

<a id="ace830ddb7ae662c9759babed87f1b6f3"></a>

### `tx_power_level`

```c
int8_t bt_conn_le_tx_power_report::tx_power_level
```

发射功率等级（Transmit power level）。

- `0xXX`：发射功率等级（Transmit power level），范围为 -127–20，单位为 dBm。
- 范围（Range）：-127–20。
- 单位（Units）：dBm。
- `0x7E`：远端设备不管理此物理层（PHY）的功率等级（Power levels）。
- `0x7F`：发射功率等级（Transmit power level）不可用。

<a id="ae7a4f77c6f7af1a459896d25cf661eb8"></a>

### `tx_power_level_flag`

```c
uint8_t bt_conn_le_tx_power_report::tx_power_level_flag
```

位 0：发射功率等级处于最低等级（Minimum level）。

位 1：发射功率等级处于最高等级（Maximum level）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_bt_conn_le_tx_power_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_bt_conn_oob_info_结构体.md)
