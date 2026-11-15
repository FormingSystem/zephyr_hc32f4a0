---
id: learning.zephyr-docs.device-power-control-model-reference.page-113
title: pd_fixed_supply_pdo_source_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__fixed__supply__pdo__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_pd\_fixed\_supply\_pdo\_source\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__fixed__supply__pdo__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建固定供电PDO供电端（Source）的值，见表6-9“固定供电PDO—供电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建固定供电PDO供电端（Source）的值，见表6-9“固定供电PDO—供电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 113.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a4a72f5af16b9445dcefa251da87587d0"></a>

```c
uint32_t max_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current](#a86664d945f65f19f7b96da1148700640)。

最大电流，以 10 mA 为单位。

<a id="r_a6084d4faaf694c58814034606ce882e0"></a>

```c
uint32_t voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[voltage](#a66f55e177b6f2bc76b392707e39fa4fe)。

电压，以 50 mV 为单位。

<a id="r_a82650b76b25cbe8e7df85852520cbe87"></a>

```c
uint32_t peak_current: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[peak_current](#a2c4b27407245da04b67e9524173d39bc)。

峰值电流（Peak Current）。

<a id="r_a58b3d4d134346f3b7a5969dc6c87dab2"></a>

```c
uint32_t reserved0: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#a6b0e04acd43c9b18bd1dea80508a8817)。

保留，必须设为零。

<a id="r_ad4df3585d71f7d74bd8834893522a4c7"></a>

```c
uint32_t unchunked_ext_msg_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unchunked_ext_msg_supported](#a440ff92d2bd533e3ddd6c65f9ac21772)。

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="r_a2b8ed4e592692d4e1ce5cce59ea8abd4"></a>

```c
uint32_t dual_role_data: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dual_role_data](#a7b89666e3753966001caf7602c796147)。

双数据角色（Dual-Role Data）。

<a id="r_aa53d09e13a3eb14472e42c8d06ffe769"></a>

```c
uint32_t usb_comms_capable: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_comms_capable](#a6c1bcf37a1fc9a348cf19e16fbe01dac)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_a1fe65a9adc55e4e8c7cd94d6024d6adf"></a>

```c
uint32_t unconstrained_power: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unconstrained_power](#a9fc10f3ec4126c063f5dd99e8f3e2723)。

不受限电源（Unconstrained Power）。

<a id="r_a392bf0539139a644f70106a3b2c0862c"></a>

```c
uint32_t usb_suspend_supported: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_suspend_supported](#a55003edba55a920a386cc04cbc7a72a0)。

支持 USB 挂起（USB Suspend）。

<a id="r_a5a7e1a0e66c4039d9ae0542fda061f71"></a>

```c
uint32_t dual_role_power: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dual_role_power](#af96673f1ac078436a9eca0973e1bdef9)。

双电源角色（Dual-Role Power）。

<a id="r_a543f9cc2333051dc7869ab023cc4e960"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#aff4c1e7eab502a68e80013b4010aff76)。

固定供电（Fixed supply）。

<a id="r_ad74cc67ccc7f6cfeb27fc528dc4a2258"></a>

```c
};
```

固定供电 PDO 的供电方字段。

<a id="r_a9227629f6c97357b71ea20e4e0572cf2"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#a9227629f6c97357b71ea20e4e0572cf2)。

原始 PDO 值。

## 113.2\_详细说明（Detailed Documentation）

<a id="ad74cc67ccc7f6cfeb27fc528dc4a2258"></a>

### `[struct]`

```c
struct { ... } pd_fixed_supply_pdo_source
```

固定供电 PDO 的供电方字段。

<a id="a7b89666e3753966001caf7602c796147"></a>

### `dual_role_data`

```c
uint32_t pd_fixed_supply_pdo_source::dual_role_data
```

双数据角色（Dual-Role Data）。

<a id="af96673f1ac078436a9eca0973e1bdef9"></a>

### `dual_role_power`

```c
uint32_t pd_fixed_supply_pdo_source::dual_role_power
```

双电源角色（Dual-Role Power）。

<a id="a86664d945f65f19f7b96da1148700640"></a>

### `max_current`

```c
uint32_t pd_fixed_supply_pdo_source::max_current
```

最大电流，以 10 mA 为单位。

<a id="a2c4b27407245da04b67e9524173d39bc"></a>

### `peak_current`

```c
uint32_t pd_fixed_supply_pdo_source::peak_current
```

峰值电流（Peak Current）。

<a id="a9227629f6c97357b71ea20e4e0572cf2"></a>

### `raw_value`

```c
uint32_t pd_fixed_supply_pdo_source::raw_value
```

原始 PDO 值。

<a id="a6b0e04acd43c9b18bd1dea80508a8817"></a>

### `reserved0`

```c
uint32_t pd_fixed_supply_pdo_source::reserved0
```

保留，必须设为零。

<a id="aff4c1e7eab502a68e80013b4010aff76"></a>

### `type`

```c
uint32_t pd_fixed_supply_pdo_source::type
```

固定供电（Fixed supply）。

设为 `PDO_FIXED`。

<a id="a440ff92d2bd533e3ddd6c65f9ac21772"></a>

### `unchunked_ext_msg_supported`

```c
uint32_t pd_fixed_supply_pdo_source::unchunked_ext_msg_supported
```

支持非分块扩展消息（Unchunked Extended Messages）。

<a id="a9fc10f3ec4126c063f5dd99e8f3e2723"></a>

### `unconstrained_power`

```c
uint32_t pd_fixed_supply_pdo_source::unconstrained_power
```

不受限电源（Unconstrained Power）。

<a id="a6c1bcf37a1fc9a348cf19e16fbe01dac"></a>

### `usb_comms_capable`

```c
uint32_t pd_fixed_supply_pdo_source::usb_comms_capable
```

具备 USB 通信能力（USB Communications Capable）。

<a id="a55003edba55a920a386cc04cbc7a72a0"></a>

### `usb_suspend_supported`

```c
uint32_t pd_fixed_supply_pdo_source::usb_suspend_supported
```

支持 USB 挂起（USB Suspend）。

<a id="a66f55e177b6f2bc76b392707e39fa4fe"></a>

### `voltage`

```c
uint32_t pd_fixed_supply_pdo_source::voltage
```

电压，以 50 mV 为单位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 113.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_fixed_supply_pdo_source](P113_pd_fixed_supply_pdo_source_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P112_pd_fixed_supply_pdo_sink_联合体.md) · [返回大纲](大纲.md) · [下一章](P114_pd_header_联合体.md)
