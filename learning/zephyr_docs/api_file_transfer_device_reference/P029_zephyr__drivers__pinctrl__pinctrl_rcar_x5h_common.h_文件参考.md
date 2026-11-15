---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-29
title: zephyr__drivers__pinctrl__pinctrl_rcar_x5h_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_drivers\_\_pinctrl\_\_pinctrl\_rcar\_x5h\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas R-Car Gen5引脚控制（Pinctrl）的通用定义。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

Renesas R-Car Gen5引脚控制（Pinctrl）的通用定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 29.1\_数据结构（Data Structures）

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

## 29.2\_宏定义（Macros）

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

控制上拉／下拉电阻（Pull Resistors）的开关。

<a id="r_a6df27aa417055266a299e964bb92fd44"></a>

```c
#define RCAR_PIN_FLAGS_PUD BIT(2)
```

相关声明：[RCAR_PIN_FLAGS_PUD](#a6df27aa417055266a299e964bb92fd44)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

置位时选择上拉电阻（Pull-up Resistor），否则选择下拉电阻（Pull-down Resistor）。

<a id="r_aabcc781206d861b19d24bd82ad1150b0"></a>

```c
#define RCAR_PIN_FLAGS_FUNC_SET BIT(3)
```

相关声明：[RCAR_PIN_FLAGS_FUNC_SET](#aabcc781206d861b19d24bd82ad1150b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求该引脚的复用功能（alternate function）。

<a id="r_a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>

```c
#define RCAR_PIN_PULL_UP (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
```

相关声明：[RCAR_PIN_PULL_UP](#a5ac9cbd536534bf5e4edb3b76f0a2f60)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)、[RCAR_PIN_FLAGS_PUEN](#acdaea04a569eaec56c706bd311e1cadd)、[RCAR_PIN_FLAGS_PUD](#a6df27aa417055266a299e964bb92fd44)。

启用上拉（Pull-up）。

<a id="r_a53d33b579bb9c498fdd09ed9bb35c0e1"></a>

```c
#define RCAR_PIN_PULL_DOWN (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
```

相关声明：[RCAR_PIN_PULL_DOWN](#a53d33b579bb9c498fdd09ed9bb35c0e1)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)、[RCAR_PIN_FLAGS_PUEN](#acdaea04a569eaec56c706bd311e1cadd)。

启用下拉（Pull-down）。

<a id="r_a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>

```c
#define RCAR_PIN_PULL_DISABLE RCAR_PIN_FLAGS_PULL_SET
```

相关声明：[RCAR_PIN_PULL_DISABLE](#a6d4c259adbd0cd5fd6065fdd4a57cda7)、[RCAR_PIN_FLAGS_PULL_SET](#a8ac73177e56465acd4376645a2fd89b1)。

禁用上拉／下拉（Pull Disabled）。

<a id="r_a9deede1d4ed63423aa956a5738ef9209"></a>

```c
#define RCAR_ALTSEL(node_id)
```

相关声明：[RCAR_ALTSEL](#a9deede1d4ed63423aa956a5738ef9209)。

获取复用功能 ID（Alternate Function ID）的工具宏。

<a id="r_a3dfee622a2f36cd4081aae415fd7756a"></a>

```c
#define RCAR_HAS_ALTSEL(node_id)
```

相关声明：[RCAR_HAS_ALTSEL](#a3dfee622a2f36cd4081aae415fd7756a)。

检查是否选择了复用功能（Alternate Function）的工具宏。

<a id="r_a7f0e2d8e2d84035326685c1e2c56d181"></a>

```c
#define RCAR_PIN_FUNC(node_id)
```

相关声明：[RCAR_PIN_FUNC](#a7f0e2d8e2d84035326685c1e2c56d181)。

初始化 R-Car 引脚功能（Pin Function）的工具宏。

<a id="r_ab94ca6630b8bddbf7325b5ae01ee969d"></a>

```c
#define RCAR_PIN_FLAGS(node_id)
```

相关声明：[RCAR_PIN_FLAGS](#ab94ca6630b8bddbf7325b5ae01ee969d)。

初始化 R-Car 引脚标志（Pin Flags）的工具宏，包含偏置（Bias）和引脚模式（Pin Mode）。

<a id="r_a3f524c2e190008ea866d3e9e114a5f18"></a>

```c
#define RCAR_DT_PIN(node_id)
```

相关声明：[RCAR_DT_PIN](#a3f524c2e190008ea866d3e9e114a5f18)。

初始化 R-Car 引脚（Pin）的工具宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 29.3\_类型定义（Typedefs）

<a id="r_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>

```c
typedef struct pinctrl_soc_pin pinctrl_soc_pin_t
```

相关声明：[pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)、[pinctrl_soc_pin_t](#a022eeb1c811e7ef94d3a7a99cbda0e2d)。

R-Car引脚（Pin）的类型。

## 29.4\_详细说明（Detailed Documentation）

<a id="a9deede1d4ed63423aa956a5738ef9209"></a>

### `RCAR_ALTSEL`

```c
#define RCAR_ALTSEL ( node_id)
```

展开值（Value）：

```c
DT_PROP_BY_IDX(node_id, pin, 1)
```

获取复用功能 ID（Alternate Function ID）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="a3f524c2e190008ea866d3e9e114a5f18"></a>

### `RCAR_DT_PIN`

```c
#define RCAR_DT_PIN ( node_id)
```

展开值（Value）：

```c
{                                                  \
.pin = DT_PROP_BY_IDX(node_id, pin, 0),                                 \
.func = COND_CODE_1(RCAR_HAS_ALTSEL(node_id),                           \
                    (RCAR_PIN_FUNC(node_id)), ({0})),                   \
.flags = RCAR_PIN_FLAGS(node_id),                                       \
.drive_strength_microamp =                                              \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, drive_strength_microamp), \
                    (DT_PROP(node_id, drive_strength_microamp)), (0))},
```

初始化 R-Car 引脚（Pin）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="a3dfee622a2f36cd4081aae415fd7756a"></a>

### `RCAR_HAS_ALTSEL`

```c
#define RCAR_HAS_ALTSEL ( node_id)
```

展开值（Value）：

```c
DT_PROP_HAS_IDX(node_id, pin, 1)
```

检查是否选择了复用功能（Alternate Function）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="ab94ca6630b8bddbf7325b5ae01ee969d"></a>

### `RCAR_PIN_FLAGS`

```c
#define RCAR_PIN_FLAGS ( node_id)
```

展开值（Value）：

```c
DT_PROP(node_id, bias_pull_up) * RCAR_PIN_PULL_UP |      \
DT_PROP(node_id, bias_pull_down) * RCAR_PIN_PULL_DOWN |  \
DT_PROP(node_id, bias_disable) * RCAR_PIN_PULL_DISABLE | \
RCAR_HAS_ALTSEL(node_id) * RCAR_PIN_FLAGS_FUNC_SET
```

初始化 R-Car 引脚标志（Pin Flags）的工具宏，包含偏置（Bias）和引脚模式（Pin Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

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

置位时选择上拉电阻（Pull-up Resistor），否则选择下拉电阻（Pull-down Resistor）。

<a id="acdaea04a569eaec56c706bd311e1cadd"></a>

### `RCAR_PIN_FLAGS_PUEN`

```c
#define RCAR_PIN_FLAGS_PUEN BIT(1)
```

控制上拉／下拉电阻（Pull Resistors）的开关。

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
{                 \
((RCAR_ALTSEL(node_id) >> 10U) & 0xFU),  \
((RCAR_ALTSEL(node_id) >> 14U) & 0x1FU), \
((RCAR_ALTSEL(node_id) & 0xFU))}
```

初始化 R-Car 引脚功能（Pin Function）的工具宏。

偏移（Offsets）在设备树绑定（DT Bindings）的 `pinctrl-rcar-common.h` 中定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>

### `RCAR_PIN_PULL_DISABLE`

```c
#define RCAR_PIN_PULL_DISABLE RCAR_PIN_FLAGS_PULL_SET
```

禁用上拉／下拉（Pull Disabled）。

<a id="a53d33b579bb9c498fdd09ed9bb35c0e1"></a>

### `RCAR_PIN_PULL_DOWN`

```c
#define RCAR_PIN_PULL_DOWN (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
```

启用下拉（Pull-down）。

<a id="a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>

### `RCAR_PIN_PULL_UP`

```c
#define RCAR_PIN_PULL_UP (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
```

启用上拉（Pull-up）。

<a id="a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>

### `pinctrl_soc_pin_t`

```c
typedef struct pinctrl_soc_pin pinctrl_soc_pin_t
```

R-Car引脚（Pin）的类型。


## 29.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P658_pinctrl_rcar_x5h_common.h_源码浏览.md)
- [rcar_pin_func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md)
- [pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)
- [pfc_drive_reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md)
- [pfc_bias_reg](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [RCAR_PIN_FUNC](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a7f0e2d8e2d84035326685c1e2c56d181)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [RCAR_PIN_FLAGS](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#ab94ca6630b8bddbf7325b5ae01ee969d)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_PROP_HAS_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c)
- [RCAR_PIN_PULL_UP](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a5ac9cbd536534bf5e4edb3b76f0a2f60)
- [RCAR_PIN_PULL_DOWN](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a53d33b579bb9c498fdd09ed9bb35c0e1)
- [RCAR_PIN_PULL_DISABLE](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a6d4c259adbd0cd5fd6065fdd4a57cda7)
- [RCAR_PIN_FLAGS_FUNC_SET](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#aabcc781206d861b19d24bd82ad1150b0)
- [pinctrl-rcar-common.h](../api_file_network_device_reference/P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考.md)
- [pinctrl_soc_pin_t](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="apinctrl__rcar__common_8h_html_a7f0e2d8e2d84035326685c1e2c56d181"></a>
<a id="apinctrl__rcar__common_8h_html_ab94ca6630b8bddbf7325b5ae01ee969d"></a>
<a id="apinctrl__rcar__x5h__common_8h_html_a3dfee622a2f36cd4081aae415fd7756a"></a>
<a id="agroup__devicetree-generic-prop_html_ga479dfc704087eea7e7c5af42ae98576c"></a>
<a id="apinctrl__rcar__common_8h_html_a53d33b579bb9c498fdd09ed9bb35c0e1"></a>
<a id="apinctrl__rcar__common_8h_html_a5ac9cbd536534bf5e4edb3b76f0a2f60"></a>
<a id="apinctrl__rcar__common_8h_html_a6d4c259adbd0cd5fd6065fdd4a57cda7"></a>
<a id="apinctrl__rcar__common_8h_html_aabcc781206d861b19d24bd82ad1150b0"></a>
<a id="apinctrl__rcar__x5h__common_8h_html_a9deede1d4ed63423aa956a5738ef9209"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P028_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__modem__pipe.h_文件参考.md)
