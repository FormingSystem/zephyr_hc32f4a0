---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-16
title: Renesas R-Car 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_Renesas R-Car 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas R-Car Gen3/Gen4/Gen5 片上系统（SoC）的引脚宏和功能宏。

<a id="details"></a>

Renesas R-Car Gen3/Gen4/Gen5 SoC 的引脚和功能宏（Pin and Function Macros）。R-Car 引脚功能控制器（Pin Function Controller，PFC）通过将引脚标识符与要路由到该引脚的复用功能（Alternate Function）配对来配置。二者在对应 SoC 的头文件中定义：`pinctrl-r8a77951.h` 对应 R-Car H3；`pinctrl-r8a77961.h` 对应 R-Car M3-W；`pinctrl-r8a779f0.h` 对应 R-Car S4；`pinctrl-r8a779g0.h` 对应 R-Car V4H；`pinctrl-r8a78000.h` 对应 R-Car Gen5。

各头文件提供 `PIN_<NAME>` 引脚标识符和 `FUNC_<NAME>` 复用功能值，其中 `<NAME>` 为 SoC 数据手册中的信号名称，例如 `PIN_RD` 和 `FUNC_CAN0_TX_A`。二者均由此处定义的编码辅助宏（Encoding Helpers）构造：引脚使用 `RCAR_GP_PIN()` 和 `RCAR_NOGP_PIN()`；功能使用 Gen3/4 的 `IPSR()`／`IPnSR()` 或 Gen5 的 `RCAR_ALTSEL_FUNC()`。原始示例如下。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-r8a77951.h>

&pfc {
        can0_data_a_tx_default: can0_data_a_tx_default {
                pin = <PIN_RD FUNC_CAN0_TX_A>;
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_pinctrl-r8a77951_2Eh"></a>

```c
file pinctrl-r8a77951.h
```

相关声明：[pinctrl-r8a77951.h](../api_file_reference/P293_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a77951.h_文件参考.md)。

Renesas R-Car H3 (R8A77951)的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-r8a77961_2Eh"></a>

```c
file pinctrl-r8a77961.h
```

相关声明：[pinctrl-r8a77961.h](../api_file_reference/P294_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a77961.h_文件参考.md)。

Renesas R-Car M3-W (R8A77961)的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-r8a779f0_2Eh"></a>

```c
file pinctrl-r8a779f0.h
```

相关声明：[pinctrl-r8a779f0.h](../api_file_reference/P295_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a779f0.h_文件参考.md)。

Renesas R-Car S4 (R8A779F0)的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-r8a779g0_2Eh"></a>

```c
file pinctrl-r8a779g0.h
```

相关声明：[pinctrl-r8a779g0.h](../api_file_supplement_reference/P085_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a779g0.h_文件参考.md)。

Renesas R-Car V4H (R8A779G0)的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-r8a78000_2Eh"></a>

```c
file pinctrl-r8a78000.h
```

相关声明：[pinctrl-r8a78000.h](../api_file_reference/P296_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a78000.h_文件参考.md)。

Renesas R-Car Gen5 (R8A78000)的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-rcar-common_2Eh"></a>

```c
file pinctrl-rcar-common.h
```

相关声明：[pinctrl-rcar-common.h](../api_file_network_device_reference/P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考.md)。

Renesas R-Car的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.2\_宏定义（Macros）

<a id="r_gadbde593c77123c64c2f63e4e8f508ccb"></a>

```c
#define IPSR(bank, shift, func)
```

相关声明：[IPSR](#gadbde593c77123c64c2f63e4e8f508ccb)。

构造 IPSR 属性条目（Property Entry）的辅助宏，仅适用于 Gen3/4。

<a id="r_ga840b9b9f9f5513088896bbb960724d8f"></a>

```c
#define RCAR_GP_PIN(bank, pin)
```

相关声明：[RCAR_GP_PIN](#ga840b9b9f9f5513088896bbb960724d8f)。

编码具备 GPIO 能力的引脚的辅助宏。

<a id="r_ga6e8b18f9578375cb325e9e5b204b6c66"></a>

```c
#define RCAR_NOGP_PIN(pin)
```

相关声明：[RCAR_NOGP_PIN](#ga6e8b18f9578375cb325e9e5b204b6c66)。

编码不具备 GPIO 能力的引脚的辅助宏。

<a id="r_ga0d4d66df6e1565e2d9f3cfdca9aa5362"></a>

```c
#define IPnSR(bank, reg, shift, func)
```

相关声明：[IPnSR](#ga0d4d66df6e1565e2d9f3cfdca9aa5362)。

为 Gen4 片上系统（SoC）构造 IPSR 属性条目的辅助宏。

<a id="r_ga66425dcd41fb8297e87a13d2c597d1b5"></a>

```c
#define IPSR_DUMMY IPnSR(0x1f, 7, 0x1f, 0xf)
```

相关声明：[IPSR_DUMMY](#ga66425dcd41fb8297e87a13d2c597d1b5)、[IPnSR](#ga0d4d66df6e1565e2d9f3cfdca9aa5362)。

为引脚定义占位 IPSR 标志（Dummy IPSR Flag）的宏。

<a id="r_ga5109d4c9a0f6625194c2e4d940805be7"></a>

```c
#define RCAR_ALTSEL_FUNC(group, pin, func)
```

相关声明：[RCAR_ALTSEL_FUNC](#ga5109d4c9a0f6625194c2e4d940805be7)、[group](../posix_system_model_reference/P003_group_结构体.md)。

构造 ALTSEL 属性条目（Property Entry）的辅助宏，仅适用于 Gen5。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 16.3\_R-Car 引脚输入输出电压电平（I/O Voltage Levels）

<a id="r_ga866ef498674c60a51c56decc15421e25"></a>

```c
#define PIN_VOLTAGE_NONE 0
```

相关声明：[PIN_VOLTAGE_NONE](#ga866ef498674c60a51c56decc15421e25)。

不选择输入输出电压（I/O Voltage）。

<a id="r_gaeb4cb1a9f61be2a30c5b11bec746b839"></a>

```c
#define PIN_VOLTAGE_1P8V 1
```

相关声明：[PIN_VOLTAGE_1P8V](#gaeb4cb1a9f61be2a30c5b11bec746b839)。

1.8 V 输入输出电压（I/O Voltage）。

<a id="r_gacc995ebea352dc5bf5042e29cd1e15d0"></a>

```c
#define PIN_VOLTAGE_3P3V 2
```

相关声明：[PIN_VOLTAGE_3P3V](#gacc995ebea352dc5bf5042e29cd1e15d0)。

3.3 V 输入输出电压（I/O Voltage）。

## 16.4\_详细说明（Detailed Documentation）

<a id="ga0d4d66df6e1565e2d9f3cfdca9aa5362"></a>

### `IPnSR`

```c
#define IPnSR ( bank, reg, shift, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

展开值（Value）：

```c
IPSR(((reg) << 5U) | (bank), shift, func)
```

为 Gen4 片上系统（SoC）构造 IPSR 属性条目的辅助宏。

Renesas Gen4 的 IPSR 寄存器位于不同基地址（Base Addresses）；`reg` 是基地址索引。每个基地址包含 4 个 IPSR 寄存器组（Banks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bank` | IPSR 寄存器组（Register Bank）。 |
| `reg` | IPSR 基地址索引（Base Address Index）。 |
| `shift` | 此复用功能（Alternate Function）的位移。 |
| `func` | 以 4 位编码的复用功能（Alternate Function）。 |

<a id="gadbde593c77123c64c2f63e4e8f508ccb"></a>

### `IPSR`

```c
#define IPSR ( bank, shift, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

展开值（Value）：

```c
(((bank) << 10U) | ((shift) << 4U) | (func))
```

构造 IPSR 属性条目（Property Entry）的辅助宏，仅适用于 Gen3/4。

IPSR：外设功能选择寄存器（Peripheral Function Select Register）。每个 IPSR 寄存器组（Bank）可容纳 8 个以 4 位编码功能的单元。

功能编码（Function Code）`[0:3]`；功能位移（Function Shift）`[4:8]`；空位（Empty）`[9]`；IPSR 组（Bank）`[10:14]`；寄存器索引（Register Index）`[15:17]`，仅 S4 使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bank` | IPSR 寄存器组（Register Bank）。 |
| `shift` | 此复用功能（Alternate Function）的位移。 |
| `func` | 以 4 位编码的复用功能（Alternate Function）。 |

<a id="ga66425dcd41fb8297e87a13d2c597d1b5"></a>

### `IPSR_DUMMY`

```c
#define IPSR_DUMMY IPnSR(0x1f, 7, 0x1f, 0xf)
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

为引脚定义占位 IPSR 标志（Dummy IPSR Flag）的宏。

此宏在 R-Car PFC 驱动中为引脚定义虚拟 IPSR 标志（Dummy IPSR Flag）。适用于未在 IPSR 中定义特定功能、但始终作为外设使用的引脚。此虚拟标志确保驱动为这些引脚设置“外设”（Peripheral）位。

**参阅（See Also）**：**另见（See Also）：**`RCAR_PIN_FLAGS_FUNC_DUMMY`。

<a id="gaeb4cb1a9f61be2a30c5b11bec746b839"></a>

### `PIN_VOLTAGE_1P8V`

```c
#define PIN_VOLTAGE_1P8V 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

1.8 V 输入输出电压（I/O Voltage）。

<a id="gacc995ebea352dc5bf5042e29cd1e15d0"></a>

### `PIN_VOLTAGE_3P3V`

```c
#define PIN_VOLTAGE_3P3V 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

3.3 V 输入输出电压（I/O Voltage）。

<a id="ga866ef498674c60a51c56decc15421e25"></a>

### `PIN_VOLTAGE_NONE`

```c
#define PIN_VOLTAGE_NONE 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

不选择输入输出电压（I/O Voltage）。

<a id="ga5109d4c9a0f6625194c2e4d940805be7"></a>

### `RCAR_ALTSEL_FUNC`

```c
#define RCAR_ALTSEL_FUNC ( group, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

展开值（Value）：

```c
(((pin) << 14U) | ((group) << 10U) | (func))
```

构造 ALTSEL 属性条目（Property Entry）的辅助宏，仅适用于 Gen5。

`ALTSELn`（`n=0..3`）：复用外设功能选择寄存器（Alternative Peripheral Function Select Registers）。每种功能由 ALTSELn 寄存器保存的 4 位编码，每个 ALTSELn 寄存器提供 1 位。

功能编码（Function Code）`[0:3]`；空位（Empty）`[4:9]`；GPIO 组（Group）`[10:13]`；引脚（Pin）`[14:18]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | GPIO 组（Group），范围 `0–10`。 |
| `pin` | 引脚（Pin），即范围 `0–31` 的位。 |
| `func` | 以 4 位编码的复用功能（Alternate Function）。 |

<a id="ga840b9b9f9f5513088896bbb960724d8f"></a>

### `RCAR_GP_PIN`

```c
#define RCAR_GP_PIN ( bank, pin )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

展开值（Value）：

```c
(((bank) * 32U) + (pin))
```

编码具备 GPIO 能力的引脚的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bank` | GPIO 组（Bank）。 |
| `pin` | GPIO 组（Bank）内的引脚（Pin），范围 `0..31`。 |

<a id="ga6e8b18f9578375cb325e9e5b204b6c66"></a>

### `RCAR_NOGP_PIN`

```c
#define RCAR_NOGP_PIN ( pin)
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
```

展开值（Value）：

```c
(PIN_NOGPSR_START + pin)
```

编码不具备 GPIO 能力的引脚的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 编码后的引脚编号（Encoded Pin Number）。 |


## 16.5\_原页交叉引用（Cross References）

- [pinctrl-r8a77951.h](../api_file_reference/P293_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a77951.h_文件参考.md)
- [pinctrl-r8a77961.h](../api_file_reference/P294_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a77961.h_文件参考.md)
- [pinctrl-r8a779f0.h](../api_file_reference/P295_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a779f0.h_文件参考.md)
- [pinctrl-r8a779g0.h](../api_file_supplement_reference/P085_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a779g0.h_文件参考.md)
- [pinctrl-r8a78000.h](../api_file_reference/P296_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a78000.h_文件参考.md)
- [pinctrl-rcar-common.h](../api_file_network_device_reference/P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考.md)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [RCAR_PIN_FLAGS_FUNC_DUMMY](../api_file_system_device_reference/P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md#a44b7efa931db5d11e5b7c9cb8a94bbf9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__pinctrl__rcar_html_gadbde593c77123c64c2f63e4e8f508ccb"></a>
<a id="astructgroup_html"></a>

---

[上一章](P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P017_Raspberry Pi Pico 可编程 I_O（PIO）.md)
