---
id: learning.zephyr-docs.api-file-system-device-reference.page-38
title: zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_drivers\_\_pinctrl\_\_pinctrl\_rcar\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
#include <stdint.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 38.1\_数据结构（Data Structures）

<a id="r_rcar_5Fpin_5Ffunc"></a>

```c
struct rcar_pin_func
```

相关声明：[rcar_pin_func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md)。

R-Car引脚功能（Pin Function）的类型。

<a id="r_pinctrl_5Fsoc_5Fpin"></a>

```c
struct pinctrl_soc_pin
```

相关声明：[pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)。

R-Car引脚（Pin）的类型。

<a id="r_pfc_5Fdrive_5Freg_5Ffield"></a>

```c
struct pfc_drive_reg_field
```

相关声明：[pfc_drive_reg_field](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md)。

<a id="r_pfc_5Fdrive_5Freg"></a>

```c
struct pfc_drive_reg
```

相关声明：[pfc_drive_reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md)。

R-Car DRVCTRLn寄存器的类型。

<a id="r_pfc_5Fbias_5Freg"></a>

```c
struct pfc_bias_reg
```

相关声明：[pfc_bias_reg](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md)。

R-Car偏置寄存器（Bias Registers）的类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.2\_宏定义（Macros）

<a id="r_a8ac73177e56465acd4376645a2fd89b1"></a>

```c
#define RCAR_PIN_FLAGS_PULL_SET BIT(0)
```

相关声明：[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求上拉（pull-up）、下拉（pull-down）或禁用偏置（bias disable）。

<a id="r_acdaea04a569eaec56c706bd311e1cadd"></a>

```c
#define RCAR_PIN_FLAGS_PUEN BIT(1)
```

相关声明：[RCAR_PIN_FLAGS_PUEN](#acdaea04a569eaec56c706bd311e1cadd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制上下拉电阻的启用／关闭。

<a id="r_a6df27aa417055266a299e964bb92fd44"></a>

```c
#define RCAR_PIN_FLAGS_PUD BIT(2)
```

相关声明：[RCAR_PIN_FLAGS_PUD](#a6df27aa417055266a299e964bb92fd44)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

置位时选择上拉电阻，否则选择下拉电阻。

<a id="r_aabcc781206d861b19d24bd82ad1150b0"></a>

```c
#define RCAR_PIN_FLAGS_FUNC_SET BIT(3)
```

相关声明：[RCAR_PIN_FLAGS_FUNC_SET](#aabcc781206d861b19d24bd82ad1150b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求该引脚的复用功能（alternate function）。

<a id="r_a44b7efa931db5d11e5b7c9cb8a94bbf9"></a>

```c
#define RCAR_PIN_FLAGS_FUNC_DUMMY BIT(4)
```

相关声明：[RCAR_PIN_FLAGS_FUNC_DUMMY](#a44b7efa931db5d11e5b7c9cb8a94bbf9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对复用功能引脚忽略 IPSR 设置。

<a id="r_a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>

```c
#define RCAR_PIN_PULL_UP (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
```

相关声明：[RCAR_PIN_PULL_UP](#a5ac9cbd536534bf5e4edb3b76f0a2f60)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)、[RCAR_PIN_FLAGS_PUEN](#acdaea04a569eaec56c706bd311e1cadd)、[RCAR_PIN_FLAGS_PUD](#a6df27aa417055266a299e964bb92fd44)。

<a id="r_a53d33b579bb9c498fdd09ed9bb35c0e1"></a>

```c
#define RCAR_PIN_PULL_DOWN (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
```

相关声明：[RCAR_PIN_PULL_DOWN](#a53d33b579bb9c498fdd09ed9bb35c0e1)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)、[RCAR_PIN_FLAGS_PUEN](#acdaea04a569eaec56c706bd311e1cadd)。

<a id="r_a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>

```c
#define RCAR_PIN_PULL_DISABLE RCAR_PIN_FLAGS_PULL_SET
```

相关声明：[RCAR_PIN_PULL_DISABLE](#a6d4c259adbd0cd5fd6065fdd4a57cda7)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)。

<a id="r_a2c260d5b989251d6dc533f835df76772"></a>

```c
#define RCAR_HAS_IPSR(node_id)
```

相关声明：[RCAR_HAS_IPSR](#a2c260d5b989251d6dc533f835df76772)。

<a id="r_af89135625acaec60f328c703a7d1823b"></a>

```c
#define RCAR_IPSR(node_id)
```

相关声明：[RCAR_IPSR](#af89135625acaec60f328c703a7d1823b)。

<a id="r_a7f0e2d8e2d84035326685c1e2c56d181"></a>

```c
#define RCAR_PIN_FUNC(node_id)
```

相关声明：[RCAR_PIN_FUNC](#a7f0e2d8e2d84035326685c1e2c56d181)。

<a id="r_a718e93760aba13e5c883ce133760e197"></a>

```c
#define RCAR_PIN_IS_FUNC_DUMMY(node_id)
```

相关声明：[RCAR_PIN_IS_FUNC_DUMMY](#a718e93760aba13e5c883ce133760e197)。

<a id="r_ab94ca6630b8bddbf7325b5ae01ee969d"></a>

```c
#define RCAR_PIN_FLAGS(node_id)
```

相关声明：[RCAR_PIN_FLAGS](#ab94ca6630b8bddbf7325b5ae01ee969d)。

<a id="r_a3f524c2e190008ea866d3e9e114a5f18"></a>

```c
#define RCAR_DT_PIN(node_id)
```

相关声明：[RCAR_DT_PIN](#a3f524c2e190008ea866d3e9e114a5f18)。

<a id="r_af231b8fe5b02c023bf068b8c7565d4c4"></a>

```c
#define RCAR_IS_GP_PIN(pin)
```

相关声明：[RCAR_IS_GP_PIN](#af231b8fe5b02c023bf068b8c7565d4c4)。

用于检查引脚是否具备 GPIO 能力的工具宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 38.3\_类型定义（Typedefs）

<a id="r_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>

```c
typedef struct pinctrl_soc_pin pinctrl_soc_pin_t
```

相关声明：[pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)、[pinctrl_soc_pin_t](#a022eeb1c811e7ef94d3a7a99cbda0e2d)。

R-Car引脚（Pin）的类型。

## 38.4\_详细说明（Detailed Documentation）

<a id="a3f524c2e190008ea866d3e9e114a5f18"></a>

### `RCAR_DT_PIN`

```c
#define RCAR_DT_PIN ( node_id)
```

展开值（Value）：

```c
{                                                                      \
        .pin = DT_PROP_BY_IDX(node_id, pin, 0),                        \
        .func = COND_CODE_1(RCAR_HAS_IPSR(node_id),                    \
                            (RCAR_PIN_FUNC(node_id)), ({0})),          \
        .flags = RCAR_PIN_FLAGS(node_id),                              \
        .drive_strength =                                              \
                COND_CODE_1(DT_NODE_HAS_PROP(node_id, drive_strength), \
                            (DT_PROP(node_id, drive_strength)), (0)),  \
        .voltage = COND_CODE_1(DT_NODE_HAS_PROP(node_id,               \
                                                power_source),         \
                               (DT_PROP(node_id, power_source)),       \
                               (PIN_VOLTAGE_NONE)),                    \
},
```

<a id="a2c260d5b989251d6dc533f835df76772"></a>

### `RCAR_HAS_IPSR`

```c
#define RCAR_HAS_IPSR ( node_id)
```

展开值（Value）：

```c
DT_PROP_HAS_IDX(node_id, pin, 1)
```

<a id="af89135625acaec60f328c703a7d1823b"></a>

### `RCAR_IPSR`

```c
#define RCAR_IPSR ( node_id)
```

展开值（Value）：

```c
COND_CODE_1(RCAR_HAS_IPSR(node_id), (DT_PROP_BY_IDX(node_id, pin, 1)), \
(0))
```

<a id="af231b8fe5b02c023bf068b8c7565d4c4"></a>

### `RCAR_IS_GP_PIN`

```c
#define RCAR_IS_GP_PIN ( pin)
```

展开值（Value）：

```c
(pin < PIN_NOGPSR_START)
```

用于检查引脚是否具备 GPIO 能力的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` |  |

**返回（Returns）**：返回值：引脚具备 GPIO 能力时为 true，否则为 false。

<a id="ab94ca6630b8bddbf7325b5ae01ee969d"></a>

### `RCAR_PIN_FLAGS`

```c
#define RCAR_PIN_FLAGS ( node_id)
```

展开值（Value）：

```c
DT_PROP(node_id, bias_pull_up)   * RCAR_PIN_PULL_UP |                  \
DT_PROP(node_id, bias_pull_down) * RCAR_PIN_PULL_DOWN |                \
DT_PROP(node_id, bias_disable)   * RCAR_PIN_PULL_DISABLE |             \
RCAR_HAS_IPSR(node_id) * RCAR_PIN_FLAGS_FUNC_SET |                     \
RCAR_PIN_IS_FUNC_DUMMY(node_id) * RCAR_PIN_FLAGS_FUNC_DUMMY
```

<a id="a44b7efa931db5d11e5b7c9cb8a94bbf9"></a>

### `RCAR_PIN_FLAGS_FUNC_DUMMY`

```c
#define RCAR_PIN_FLAGS_FUNC_DUMMY BIT(4)
```

对复用功能引脚忽略 IPSR 设置。

<a id="aabcc781206d861b19d24bd82ad1150b0"></a>

### `RCAR_PIN_FLAGS_FUNC_SET`

```c
#define RCAR_PIN_FLAGS_FUNC_SET BIT(3)
```

请求该引脚的复用功能（alternate function）。

<a id="a6df27aa417055266a299e964bb92fd44"></a>

### `RCAR_PIN_FLAGS_PUD`

```c
#define RCAR_PIN_FLAGS_PUD BIT(2)
```

置位时选择上拉电阻，否则选择下拉电阻。

<a id="acdaea04a569eaec56c706bd311e1cadd"></a>

### `RCAR_PIN_FLAGS_PUEN`

```c
#define RCAR_PIN_FLAGS_PUEN BIT(1)
```

控制上下拉电阻的启用／关闭。

<a id="a8ac73177e56465acd4376645a2fd89b1"></a>

### `RCAR_PIN_FLAGS_PULL_SET`

```c
#define RCAR_PIN_FLAGS_PULL_SET BIT(0)
```

请求上拉（pull-up）、下拉（pull-down）或禁用偏置（bias disable）。

<a id="a7f0e2d8e2d84035326685c1e2c56d181"></a>

### `RCAR_PIN_FUNC`

```c
#define RCAR_PIN_FUNC ( node_id)
```

展开值（Value）：

```c
{                                              \
        ((RCAR_IPSR(node_id) >> 10U) & 0x1FU), \
        ((RCAR_IPSR(node_id) >> 4U) & 0x1FU),  \
        ((RCAR_IPSR(node_id) & 0xFU))          \
}
```

<a id="a718e93760aba13e5c883ce133760e197"></a>

### `RCAR_PIN_IS_FUNC_DUMMY`

```c
#define RCAR_PIN_IS_FUNC_DUMMY ( node_id)
```

展开值（Value）：

```c
((((RCAR_IPSR(node_id) >> 10U) & 0x1FU) == 0x1F) &&                    \
 (((RCAR_IPSR(node_id) >> 4U) & 0x1FU) == 0x1F) &&                     \
 ((RCAR_IPSR(node_id) & 0xFU) == 0xF))
```

<a id="a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>

### `RCAR_PIN_PULL_DISABLE`

```c
#define RCAR_PIN_PULL_DISABLE RCAR_PIN_FLAGS_PULL_SET
```

<a id="a53d33b579bb9c498fdd09ed9bb35c0e1"></a>

### `RCAR_PIN_PULL_DOWN`

```c
#define RCAR_PIN_PULL_DOWN (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
```

<a id="a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>

### `RCAR_PIN_PULL_UP`

```c
#define RCAR_PIN_PULL_UP (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
```

<a id="a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>

### `pinctrl_soc_pin_t`

```c
typedef struct pinctrl_soc_pin pinctrl_soc_pin_t
```

R-Car引脚（Pin）的类型。


## 38.5\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h](../api_source_supplement_reference/P143_pinctrl-rcar-common.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_device_reference/P030_pinctrl_rcar_common.h_源码浏览.md)
- [rcar_pin_func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md)
- [pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)
- [pfc_drive_reg_field](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md)
- [pfc_drive_reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md)
- [pfc_bias_reg](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [PIN_VOLTAGE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga866ef498674c60a51c56decc15421e25)
- [DT_PROP_HAS_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__pinctrl__rcar_html_ga866ef498674c60a51c56decc15421e25"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="apinctrl__rcar__common_8h_html_a2c260d5b989251d6dc533f835df76772"></a>
<a id="apinctrl__rcar__common_8h_html_a7f0e2d8e2d84035326685c1e2c56d181"></a>
<a id="apinctrl__rcar__common_8h_html_ab94ca6630b8bddbf7325b5ae01ee969d"></a>
<a id="agroup__devicetree-generic-prop_html_ga479dfc704087eea7e7c5af42ae98576c"></a>
<a id="apinctrl__rcar__common_8h_html_a44b7efa931db5d11e5b7c9cb8a94bbf9"></a>
<a id="apinctrl__rcar__common_8h_html_a53d33b579bb9c498fdd09ed9bb35c0e1"></a>
<a id="apinctrl__rcar__common_8h_html_a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>
<a id="apinctrl__rcar__common_8h_html_a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>
<a id="apinctrl__rcar__common_8h_html_aabcc781206d861b19d24bd82ad1150b0"></a>
<a id="apinctrl__rcar__common_8h_html_af89135625acaec60f328c703a7d1823b"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P037_zephyr__drivers__sensor__pcnt_esp32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__bluetooth__mesh__priv_beacon_cli.h_文件参考.md)
