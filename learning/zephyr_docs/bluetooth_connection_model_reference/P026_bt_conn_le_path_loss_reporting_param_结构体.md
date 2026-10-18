---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-26
title: bt_conn_le_path_loss_reporting_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__path__loss__reporting__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_bt\_conn\_le\_path\_loss\_reporting\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__path__loss__reporting__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

核心规范（Core Spec）定义的 LE 路径损耗监测参数（Path Loss Monitoring Parameters）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

低功耗路径损耗监测参数结构（LE Path Loss Monitoring Parameters Structure），由核心规范（Core Spec.）5.4 版第 4 卷 E 部分第 7.8.119 节的低功耗设置路径损耗报告参数命令（LE Set Path Loss Reporting Parameters）定义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a5cc7a17efee69d61b8f8d0c242321054"></a>

```c
uint8_t high_threshold
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[high_threshold](#a5cc7a17efee69d61b8f8d0c242321054)。

路径损耗高阈值（High path loss threshold），单位为 dB。

<a id="r_aec49adc896604d878060b03bd40ab0f4"></a>

```c
uint8_t high_hysteresis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[high_hysteresis](#aec49adc896604d878060b03bd40ab0f4)。

高阈值的滞回值（Hysteresis），单位为 dB。

<a id="r_a634c08e573cffd97a94ad681bed9239e"></a>

```c
uint8_t low_threshold
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[low_threshold](#a634c08e573cffd97a94ad681bed9239e)。

路径损耗低阈值（Low path loss threshold），单位为 dB。

<a id="r_af8e70508a39ee73b75a4769769aa303f"></a>

```c
uint8_t low_hysteresis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[low_hysteresis](#af8e70508a39ee73b75a4769769aa303f)。

低阈值的滞回值（Hysteresis），单位为 dB。

<a id="r_a6fec4497c6fd95fa6f265bd859976c9d"></a>

```c
uint16_t min_time_spent
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_time_spent](#a6fec4497c6fd95fa6f265bd859976c9d)。

路径损耗（Path loss）跨越阈值后，生成事件之前所需观察的最短时间，以连接事件数量（Connection events）表示。

## 26.2\_详细说明（Detailed Documentation）

<a id="aec49adc896604d878060b03bd40ab0f4"></a>

### `high_hysteresis`

```c
uint8_t bt_conn_le_path_loss_reporting_param::high_hysteresis
```

高阈值的滞回值（Hysteresis），单位为 dB。

<a id="a5cc7a17efee69d61b8f8d0c242321054"></a>

### `high_threshold`

```c
uint8_t bt_conn_le_path_loss_reporting_param::high_threshold
```

路径损耗高阈值（High path loss threshold），单位为 dB。

<a id="af8e70508a39ee73b75a4769769aa303f"></a>

### `low_hysteresis`

```c
uint8_t bt_conn_le_path_loss_reporting_param::low_hysteresis
```

低阈值的滞回值（Hysteresis），单位为 dB。

<a id="a634c08e573cffd97a94ad681bed9239e"></a>

### `low_threshold`

```c
uint8_t bt_conn_le_path_loss_reporting_param::low_threshold
```

路径损耗低阈值（Low path loss threshold），单位为 dB。

<a id="a6fec4497c6fd95fa6f265bd859976c9d"></a>

### `min_time_spent`

```c
uint16_t bt_conn_le_path_loss_reporting_param::min_time_spent
```

路径损耗（Path loss）跨越阈值后，生成事件之前所需观察的最短时间，以连接事件数量（Connection events）表示。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_bt_conn_le_min_conn_interval_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_bt_conn_le_path_loss_threshold_report_结构体.md)
