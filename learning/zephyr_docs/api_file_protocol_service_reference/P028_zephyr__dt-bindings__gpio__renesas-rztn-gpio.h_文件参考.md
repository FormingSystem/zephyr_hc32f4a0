---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-28
title: zephyr__dt-bindings__gpio__renesas-rztn-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_dt-bindings\_\_gpio\_\_renesas-rztn-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr使用的Renesas RZ/T、RZ/N GPIO标志（Flags）。

查看此文件的源码。

<a id="details"></a>

供 Zephyr 使用的 Renesas RZ/T、RZ/N GPIO 标志（Flags）。附加标志编码在 `gpio_dt_flags_t` 的高 8 位中：位 `[9:8]` 为驱动能力控制（Driving Ability Control，`0=低`、`1=中`、`2=高`、`3=超高`）；位 `[12]` 为施密特触发器控制（Schmitt Trigger Control，`0=禁用`、`1=启用`）；位 `[13]` 为转换速率控制（Slew Rate Control，`0=慢`、`1=快`）；位 `[14]` 为安全区域（Safety Region，`0=安全`、`1=非安全`）。下方设备树示例采用中等驱动能力、启用施密特触发器、慢转换速率和非安全区域。

```c
gpio-consumer {
    out-gpios = <&port8 2 (GPIO_PULL_UP | RZTN_GPIO_CFG_SET(1, 1, 0) | RZTN_GPIO_NONSAFETY)>;
};
```

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="define-members-0"></a>

### Renesas RZ/T、RZ/N 区域选择选项（Region Select Options）

设置 I/O 端口的安全属性（Safety Attribute，RSELP）。

<a id="r_a0c99733184752624d93b9c2858367619"></a>

```c
#define RZTN_GPIO_SAFETY 0U
```

相关声明：[RZTN_GPIO_SAFETY](#a0c99733184752624d93b9c2858367619)。

安全区域（Safety Region）。

<a id="r_af34338935c720ac24f38b49936716e71"></a>

```c
#define RZTN_GPIO_NONSAFETY BIT(14)
```

相关声明：[RZTN_GPIO_NONSAFETY](#af34338935c720ac24f38b49936716e71)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

非安全区域（Non-safety Region）。

<a id="define-members-1"></a>

<a id="r_a74666258b9d1c0bc26c00cc30bbfb489"></a>

```c
#define RZTN_GPIO_DRCTL_SET(drive_ability, schmitt_trig, slew_rate)
```

相关声明：[RZTN_GPIO_DRCTL_SET](#a74666258b9d1c0bc26c00cc30bbfb489)。

将 DRCTL 寄存器设置（Register Settings）编码为一个配置值（Configuration Value）。

## 28.2\_详细说明（Detailed Documentation）

<a id="a74666258b9d1c0bc26c00cc30bbfb489"></a>

### `RZTN_GPIO_DRCTL_SET`

```c
#define RZTN_GPIO_DRCTL_SET ( drive_ability, schmitt_trig, slew_rate )
```

展开值（Value）：

```c
(((drive_ability) | ((schmitt_trig) << RZTN_GPIO_SCHMITT_TRIG_SHIFT) |                     \
  ((slew_rate) << RZTN_GPIO_SLEW_RATE_SHIFT))                                              \
 << RZTN_GPIO_DRCTL_SHIFT)
```

将 DRCTL 寄存器设置（Register Settings）编码为一个配置值（Configuration Value）。

编码方式（Encodings）：

- 位 `[9:8]`：驱动能力控制（Driving Ability Control），`0=低（Low）`、`1=中（Middle）`、`2=高（High）`、`3=超高（Ultra High）`。
- 位 `[12]`：施密特触发器控制（Schmitt Trigger Control），`0=禁用（Disable）`、`1=启用（Enable）`。
- 位 `[13]`：转换速率控制（Slew Rate Control），`0=慢（Slow）`、`1=快（Fast）`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `drive_ability` | 驱动能力控制（Driving Ability Control）：`0=低（Low）`、`1=中（Middle）`、`2=高（High）`、`3=超高（Ultra High）`。 |
| `schmitt_trig` | 施密特触发器控制（Schmitt Trigger Control）：`0=禁用（Disable）`、`1=启用（Enable）`。 |
| `slew_rate` | 转换速率控制（Slew Rate Control）：`0=慢（Slow）`、`1=快（Fast）`。 |

**返回（Returns）**：**返回值（Returns）：**DRCTL 寄存器编码后的配置值（Encoded Configuration Value）。

<a id="af34338935c720ac24f38b49936716e71"></a>

### `RZTN_GPIO_NONSAFETY`

```c
#define RZTN_GPIO_NONSAFETY BIT(14)
```

非安全区域（Non-safety Region）。

<a id="a0c99733184752624d93b9c2858367619"></a>

### `RZTN_GPIO_SAFETY`

```c
#define RZTN_GPIO_SAFETY 0U
```

安全区域（Safety Region）。


## 28.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P161_renesas-rztn-gpio.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P027_zephyr__dt-bindings__sensor__qdec_stm32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__interrupt_controller__riscv_aplic_direct.h_文件参考.md)
