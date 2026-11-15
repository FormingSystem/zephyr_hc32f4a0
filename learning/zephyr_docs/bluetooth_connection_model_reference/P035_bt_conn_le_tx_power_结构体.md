---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-35
title: bt_conn_le_tx_power_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__tx__power.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_conn\_le\_tx\_power\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__tx__power.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 发射功率等级（Transmit Power Level）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 发射功率等级（Transmit Power Level）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a8702c4ff5082b8f90decdfabfb8253fe"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a8702c4ff5082b8f90decdfabfb8253fe)。

输入（Input）：1M、2M、编码 S2（Coded S2）或编码 S8（Coded S8）。

<a id="r_a6d2e5a5215fa5d60630e74928a67fc04"></a>

```c
int8_t current_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[current_level](#a6d2e5a5215fa5d60630e74928a67fc04)。

输出（Output）：当前发射功率等级（Transmit power level），单位为 dBm。

<a id="r_a1674247c511906fa6f0193653ed0b71a"></a>

```c
int8_t max_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_level](#a1674247c511906fa6f0193653ed0b71a)。

输出（Output）：最大发射功率等级（Maximum transmit power level），单位为 dBm。

## 35.2\_详细说明（Detailed Documentation）

<a id="a6d2e5a5215fa5d60630e74928a67fc04"></a>

### `current_level`

```c
int8_t bt_conn_le_tx_power::current_level
```

输出（Output）：当前发射功率等级（Transmit power level），单位为 dBm。

取值范围取决于所使用的主机控制器接口命令（HCI command）：

- `phy` 为 `0` 时，范围为 -30 至 +20，使用 `HCI_Read_Transmit_Power_Level`。
- `phy` 非零时，范围为 -127 至 +20，使用 `HCI_LE_Enhanced_Read_Transmit_Power_Level`。

<a id="a1674247c511906fa6f0193653ed0b71a"></a>

### `max_level`

```c
int8_t bt_conn_le_tx_power::max_level
```

输出（Output）：最大发射功率等级（Maximum transmit power level），单位为 dBm。

取值范围取决于所使用的主机控制器接口命令（HCI command）：

- `phy` 为 `0` 时，范围为 -30 至 +20，使用 `HCI_Read_Transmit_Power_Level`。
- `phy` 非零时，范围为 -127 至 +20，使用 `HCI_LE_Enhanced_Read_Transmit_Power_Level`。

<a id="a8702c4ff5082b8f90decdfabfb8253fe"></a>

### `phy`

```c
uint8_t bt_conn_le_tx_power::phy
```

输入（Input）：1M、2M、编码 S2（Coded S2）或编码 S8（Coded S8）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_bt_conn_le_subrating_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_conn_le_tx_power_report_结构体.md)
