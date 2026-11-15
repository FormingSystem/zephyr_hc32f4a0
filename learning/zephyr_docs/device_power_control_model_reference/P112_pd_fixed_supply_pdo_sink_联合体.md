---
id: learning.zephyr-docs.device-power-control-model-reference.page-112
title: pd_fixed_supply_pdo_sink_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__fixed__supply__pdo__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_pd\_fixed\_supply\_pdo\_sink\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__fixed__supply__pdo__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建固定供电PDO受电端（Sink）的值，见表6-14“固定供电PDO—受电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建固定供电PDO受电端（Sink）的值，见表6-14“固定供电PDO—受电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 112.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_ac681631289a36c4d68e9361c21c91051"></a>

```c
uint32_t operational_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operational_current](#a2ac4005b0cf3e28ade8f508d2c6f5e20)。

工作电流（Operational Current），以 10 mA 为单位。

<a id="r_ae87a1e4fd6c1ad44a4fcfe9e13073046"></a>

```c
uint32_t voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[voltage](#ac47dcf98dfca90eb0e6013a3e1c5eb18)。

电压，以 50 mV 为单位。

<a id="r_a859ff4d52cdee3a003da30c41feee8f3"></a>

```c
uint32_t reserved0: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#a22f9763652560dbd215324f1bb878a96)。

保留，必须设为零。

<a id="r_a71f3205037bb5a1199fbb8a1dc8eb42d"></a>

```c
uint32_t frs_required: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frs_required](#a7a26a084dd6004f9121c8493a0c520f6)。

快速角色切换（Fast Role Swap）所需的 USB Type-C 电流。

<a id="r_a651702a0229b5c23f6457a1a5c3703d6"></a>

```c
uint32_t dual_role_data: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dual_role_data](#a5c6bfb21c4d8e70a04895dd31a58885e)。

双数据角色（Dual-Role Data）。

<a id="r_a00ce2d9a4800d9386f5f1ffd2b7a4fe6"></a>

```c
uint32_t usb_comms_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comms_capable](#a0559272067e2d0c33f52274fb59ea18d)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_abf9dce4166230122d2ff834513c3f1ce"></a>

```c
uint32_t unconstrained_power: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unconstrained_power](#ab406f1f36e5fe6f7acb9abc91991a803)。

不受限电源（Unconstrained Power）。

<a id="r_a08554f880cd0bfbd6906716fc0a12e0d"></a>

```c
uint32_t higher_capability: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[higher_capability](#a3086d57313f05b8bc91fb3590e51c657)。

更高能力（Higher Capability）。

<a id="r_a0228dfd678cde7005f55f47db80edff9"></a>

```c
uint32_t dual_role_power: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dual_role_power](#aad255dbee3452bf3276464c59f113cb2)。

双电源角色（Dual-Role Power）。

<a id="r_a1ee0aff292ea07d34d4b6183d7d2f517"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#a3945768e406175b51f9c4b8c3d0e9848)。

固定供电（Fixed supply）。

<a id="r_a65a59e06174e0ad8acb90693fe131d30"></a>

```c
};
```

固定供电 PDO 的受电方字段。

<a id="r_aebdeb854bcac0d20efcbe3be56dcc9f8"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#aebdeb854bcac0d20efcbe3be56dcc9f8)。

原始 PDO 值。

## 112.2\_详细说明（Detailed Documentation）

<a id="a65a59e06174e0ad8acb90693fe131d30"></a>

### `[struct]`

```c
struct { ... } pd_fixed_supply_pdo_sink
```

固定供电 PDO 的受电方字段。

<a id="a5c6bfb21c4d8e70a04895dd31a58885e"></a>

### `dual_role_data`

```c
uint32_t pd_fixed_supply_pdo_sink::dual_role_data
```

双数据角色（Dual-Role Data）。

<a id="aad255dbee3452bf3276464c59f113cb2"></a>

### `dual_role_power`

```c
uint32_t pd_fixed_supply_pdo_sink::dual_role_power
```

双电源角色（Dual-Role Power）。

<a id="a7a26a084dd6004f9121c8493a0c520f6"></a>

### `frs_required`

```c
uint32_t pd_fixed_supply_pdo_sink::frs_required
```

快速角色切换（Fast Role Swap）所需的 USB Type-C 电流。

<a id="a3086d57313f05b8bc91fb3590e51c657"></a>

### `higher_capability`

```c
uint32_t pd_fixed_supply_pdo_sink::higher_capability
```

更高能力（Higher Capability）。

<a id="a2ac4005b0cf3e28ade8f508d2c6f5e20"></a>

### `operational_current`

```c
uint32_t pd_fixed_supply_pdo_sink::operational_current
```

工作电流（Operational Current），以 10 mA 为单位。

<a id="aebdeb854bcac0d20efcbe3be56dcc9f8"></a>

### `raw_value`

```c
uint32_t pd_fixed_supply_pdo_sink::raw_value
```

原始 PDO 值。

<a id="a22f9763652560dbd215324f1bb878a96"></a>

### `reserved0`

```c
uint32_t pd_fixed_supply_pdo_sink::reserved0
```

保留，必须设为零。

<a id="a3945768e406175b51f9c4b8c3d0e9848"></a>

### `type`

```c
uint32_t pd_fixed_supply_pdo_sink::type
```

固定供电（Fixed supply）。

设为 `PDO_FIXED`。

<a id="ab406f1f36e5fe6f7acb9abc91991a803"></a>

### `unconstrained_power`

```c
uint32_t pd_fixed_supply_pdo_sink::unconstrained_power
```

不受限电源（Unconstrained Power）。

<a id="a0559272067e2d0c33f52274fb59ea18d"></a>

### `usb_comms_capable`

```c
uint32_t pd_fixed_supply_pdo_sink::usb_comms_capable
```

具备 USB 通信能力（USB Communications Capable）。

<a id="ac47dcf98dfca90eb0e6013a3e1c5eb18"></a>

### `voltage`

```c
uint32_t pd_fixed_supply_pdo_sink::voltage
```

电压，以 50 mV 为单位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 112.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_fixed_supply_pdo_sink](P112_pd_fixed_supply_pdo_sink_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P111_pd_ext_header_联合体.md) · [返回大纲](大纲.md) · [下一章](P113_pd_fixed_supply_pdo_source_联合体.md)
