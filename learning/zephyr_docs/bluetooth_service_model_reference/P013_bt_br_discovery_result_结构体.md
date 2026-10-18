---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-13
title: bt_br_discovery_result_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_br\_discovery\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 发现结果结构体。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="details"></a>

BR/EDR 发现结果结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a833b05883132a0c20690f71b2c14a62a"></a>

```c
bt_addr_t addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[addr](#a833b05883132a0c20690f71b2c14a62a)。

远端设备地址（Remote device address）。

<a id="r_ad1f6bbfc27796e998ed30e307a251841"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#ad1f6bbfc27796e998ed30e307a251841)。

查询所得的接收信号强度指示（RSSI），单位为 dBm。

<a id="r_aec239cbb82436ace39c8928a3baa0cf6"></a>

```c
uint8_t cod [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cod](#aec239cbb82436ace39c8928a3baa0cf6)。

设备类别（Class of Device）。

<a id="r_a6bfe9a421257e2460eb9b4381252f9cc"></a>

```c
uint8_t eir [240]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eir](#a6bfe9a421257e2460eb9b4381252f9cc)。

扩展查询响应（Extended Inquiry Response）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a833b05883132a0c20690f71b2c14a62a"></a>

### `addr`

```c
bt_addr_t bt_br_discovery_result::addr
```

远端设备地址（Remote device address）。

<a id="aec239cbb82436ace39c8928a3baa0cf6"></a>

### `cod`

```c
uint8_t bt_br_discovery_result::cod[3]
```

设备类别（Class of Device）。

<a id="a6bfe9a421257e2460eb9b4381252f9cc"></a>

### `eir`

```c
uint8_t bt_br_discovery_result::eir[240]
```

扩展查询响应（Extended Inquiry Response）。

<a id="ad1f6bbfc27796e998ed30e307a251841"></a>

### `rssi`

```c
int8_t bt_br_discovery_result::rssi
```

查询所得的接收信号强度指示（RSSI），单位为 dBm。

范围（Range）：-127 至 +20。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_br_discovery_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_br_inquiry_scan_param_结构体.md)
