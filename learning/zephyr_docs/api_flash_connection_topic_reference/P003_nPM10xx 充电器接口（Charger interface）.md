---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-3
title: nPM10xx 充电器接口（Charger interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_nPM10xx 充电器接口（Charger interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.1\_枚举（Enumerations）

<a id="r_ga2de09557c2f7d19ad141ca8ba48e9f5d"></a>

```c
enum npm10xx_charger_prop { NPM10XX_CHARGER_PROP_TERM_CURRENT = CHARGER_PROP_CUSTOM_BEGIN , NPM10XX_CHARGER_PROP_TRICKLE_CURRENT , NPM10XX_CHARGER_PROP_THROTTLE_LVL , NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_WARM_UA , NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_COOL_UA , NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_WARM_UV , NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_COOL_UV }
```

相关声明：[npm10xx_charger_prop](#ga2de09557c2f7d19ad141ca8ba48e9f5d)、[NPM10XX_CHARGER_PROP_TERM_CURRENT](#gga2de09557c2f7d19ad141ca8ba48e9f5da43de07adf7b4c2ee51c4c415cf767e81)、[NPM10XX_CHARGER_PROP_TRICKLE_CURRENT](#gga2de09557c2f7d19ad141ca8ba48e9f5daec4b5f597aff98e289e5b826e2bf0b01)、[NPM10XX_CHARGER_PROP_THROTTLE_LVL](#gga2de09557c2f7d19ad141ca8ba48e9f5dadd0b75d418d1b9439ed16383185f7b9e)、[NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_WARM_UA](#gga2de09557c2f7d19ad141ca8ba48e9f5da5b8931185580b5f5b21adb117af0a407)、[NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_COOL_UA](#gga2de09557c2f7d19ad141ca8ba48e9f5dac1783198b9b10317142dcd3c0d614c76)、[NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_WARM_UV](#gga2de09557c2f7d19ad141ca8ba48e9f5da9bf9927db001f17b40d71665634662c4)、[NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_COOL_UV](#gga2de09557c2f7d19ad141ca8ba48e9f5da16efc7a009faff4fdecb0548cfee8e67)。

nPM10xx 充电器（Charger）的自定义属性。

<a id="r_ga0361b1ebfc18e176ed171823a38e12ab"></a>

```c
enum npm10xx_charger_iterm { NPM10XX_CHARGER_ITERM_12P5 , NPM10XX_CHARGER_ITERM_100P , NPM10XX_CHARGER_ITERM_50P , NPM10XX_CHARGER_ITERM_25P , NPM10XX_CHARGER_ITERM_6P25 , NPM10XX_CHARGER_ITERM_3P125 , NPM10XX_CHARGER_ITERM_1P56 , NPM10XX_CHARGER_ITERM_0P78 , NPM10XX_CHARGER_CURRENT_PERCENT_MAX }
```

相关声明：[npm10xx_charger_iterm](#ga0361b1ebfc18e176ed171823a38e12ab)、[NPM10XX_CHARGER_ITERM_12P5](#gga0361b1ebfc18e176ed171823a38e12aba0959a4ef28fcfd44de6f4c852744e197)、[NPM10XX_CHARGER_ITERM_100P](#gga0361b1ebfc18e176ed171823a38e12abad6f6c26c8759613c05a10592ac628d15)、[NPM10XX_CHARGER_ITERM_50P](#gga0361b1ebfc18e176ed171823a38e12aba44ed6f6aea9feee4577635fffc480dfb)、[NPM10XX_CHARGER_ITERM_25P](#gga0361b1ebfc18e176ed171823a38e12abab7aaa32e285208f86889cc7d7a0060c0)、[NPM10XX_CHARGER_ITERM_6P25](#gga0361b1ebfc18e176ed171823a38e12aba25a044f38b048ff0451e556b42534b67)、[NPM10XX_CHARGER_ITERM_3P125](#gga0361b1ebfc18e176ed171823a38e12abae981727f782b8459d41757151b0cdcf7)、[NPM10XX_CHARGER_ITERM_1P56](#gga0361b1ebfc18e176ed171823a38e12abafa68639f27c5366ad45db5c56f2268af)、[NPM10XX_CHARGER_ITERM_0P78](#gga0361b1ebfc18e176ed171823a38e12aba8ca1895fc6fe1a8660f2e2b2452c5f59)、[NPM10XX_CHARGER_CURRENT_PERCENT_MAX](#gga0361b1ebfc18e176ed171823a38e12aba911e517245594be44d2c4cc971cee1bd)。

nPM10xx 充电器终止电流（termination current），以百分比表示。

<a id="r_ga645f680cc19e3d6f0c777dfa41b3abae"></a>

```c
enum npm10xx_charger_itrickle { NPM10XX_CHARGER_ITRICKLE_12P5 , NPM10XX_CHARGER_ITRICKLE_100P , NPM10XX_CHARGER_ITRICKLE_50P , NPM10XX_CHARGER_ITRICKLE_25P , NPM10XX_CHARGER_ITRICKLE_6P25 , NPM10XX_CHARGER_ITRICKLE_3P125 , NPM10XX_CHARGER_ITRICKLE_1P56 , NPM10XX_CHARGER_ITRICKLE_0P78 }
```

相关声明：[npm10xx_charger_itrickle](#ga645f680cc19e3d6f0c777dfa41b3abae)、[NPM10XX_CHARGER_ITRICKLE_12P5](#gga645f680cc19e3d6f0c777dfa41b3abaea7b97b37ac08b922c7382d92ce2c22890)、[NPM10XX_CHARGER_ITRICKLE_100P](#gga645f680cc19e3d6f0c777dfa41b3abaea870a1db010506badc4f1579d3d1a7d74)、[NPM10XX_CHARGER_ITRICKLE_50P](#gga645f680cc19e3d6f0c777dfa41b3abaea25c61182f513f6da143e5c77954bece4)、[NPM10XX_CHARGER_ITRICKLE_25P](#gga645f680cc19e3d6f0c777dfa41b3abaeaccdcdd78cd8ba973a1a74ba1a629b609)、[NPM10XX_CHARGER_ITRICKLE_6P25](#gga645f680cc19e3d6f0c777dfa41b3abaea2158df739371f0cd8dfadb37b56356c7)、[NPM10XX_CHARGER_ITRICKLE_3P125](#gga645f680cc19e3d6f0c777dfa41b3abaea634f230faf1547e0ae7a396be6bc4bcb)、[NPM10XX_CHARGER_ITRICKLE_1P56](#gga645f680cc19e3d6f0c777dfa41b3abaeadb4f86e7b444dd47b417489ce074acf1)、[NPM10XX_CHARGER_ITRICKLE_0P78](#gga645f680cc19e3d6f0c777dfa41b3abaea9bff02ec00c10b480cbeda27c8e78c8f)。

nPM10xx 充电器涓流电流（trickle current），以百分比表示。

<a id="r_ga2e2382e875599723272916c8eda7e693"></a>

```c
enum npm10xx_charger_ithrottle { NPM10XX_CHARGER_ITHROTTLE_100P = 0x00U , NPM10XX_CHARGER_ITHROTTLE_87P5 = 0x10U , NPM10XX_CHARGER_ITHROTTLE_75P = 0x20U , NPM10XX_CHARGER_ITHROTTLE_62P5 = 0x30U , NPM10XX_CHARGER_ITHROTTLE_50P = 0x40U , NPM10XX_CHARGER_ITHROTTLE_37P5 = 0x50U , NPM10XX_CHARGER_ITHROTTLE_25P = 0x60U , NPM10XX_CHARGER_ITHROTTLE_12P5 = 0x70U }
```

相关声明：[npm10xx_charger_ithrottle](#ga2e2382e875599723272916c8eda7e693)、[NPM10XX_CHARGER_ITHROTTLE_100P](#gga2e2382e875599723272916c8eda7e693ac91db4439de44f8137eb8a723491e0cf)、[NPM10XX_CHARGER_ITHROTTLE_87P5](#gga2e2382e875599723272916c8eda7e693af9c1e0e4bb3dbf2a3f59a6dc07e61756)、[NPM10XX_CHARGER_ITHROTTLE_75P](#gga2e2382e875599723272916c8eda7e693a24a0a5e7f1ab78f0ac8245a59ee4c1b8)、[NPM10XX_CHARGER_ITHROTTLE_62P5](#gga2e2382e875599723272916c8eda7e693a556ac103ce88c27b2e134570f131006f)、[NPM10XX_CHARGER_ITHROTTLE_50P](#gga2e2382e875599723272916c8eda7e693a6b73937a3b83e16c6d2829a35d950312)、[NPM10XX_CHARGER_ITHROTTLE_37P5](#gga2e2382e875599723272916c8eda7e693a498a1b6c5493c7bd649b6039a1c95c99)、[NPM10XX_CHARGER_ITHROTTLE_25P](#gga2e2382e875599723272916c8eda7e693a608716ba46dc88ed9728aee15ae878aa)、[NPM10XX_CHARGER_ITHROTTLE_12P5](#gga2e2382e875599723272916c8eda7e693a92a054648b92527a1e40e7373808c398)。

nPM10xx 充电器限流电流（throttle current），以百分比表示。

<a id="r_ga51fc3e1a4aa657d030209b1e2f640b88"></a>

```c
enum npm10xx_charger_vthrottle { NPM10XX_CHARGER_VTHROTTLE_25MV , NPM10XX_CHARGER_VTHROTTLE_50MV , NPM10XX_CHARGER_VTHROTTLE_75MV , NPM10XX_CHARGER_VTHROTTLE_100MV , NPM10XX_CHARGER_VTHROTTLE_125MV , NPM10XX_CHARGER_VTHROTTLE_150MV , NPM10XX_CHARGER_VTHROTTLE_175MV , NPM10XX_CHARGER_VTHROTTLE_200MV , NPM10XX_CHARGER_VTHROTTLE_225MV , NPM10XX_CHARGER_VTHROTTLE_250MV , NPM10XX_CHARGER_VTHROTTLE_275MV , NPM10XX_CHARGER_VTHROTTLE_300MV , NPM10XX_CHARGER_VTHROTTLE_325MV , NPM10XX_CHARGER_VTHROTTLE_350MV , NPM10XX_CHARGER_VTHROTTLE_375MV , NPM10XX_CHARGER_VTHROTTLE_400MV }
```

相关声明：[npm10xx_charger_vthrottle](#ga51fc3e1a4aa657d030209b1e2f640b88)、[NPM10XX_CHARGER_VTHROTTLE_25MV](#gga51fc3e1a4aa657d030209b1e2f640b88a8d7fdc23a114a55170c4ae555381fe5b)、[NPM10XX_CHARGER_VTHROTTLE_50MV](#gga51fc3e1a4aa657d030209b1e2f640b88a9d09acf1922030fb519ca092a7527e62)、[NPM10XX_CHARGER_VTHROTTLE_75MV](#gga51fc3e1a4aa657d030209b1e2f640b88aa2f1d279f26a3225fc198e491ff7fcf6)、[NPM10XX_CHARGER_VTHROTTLE_100MV](#gga51fc3e1a4aa657d030209b1e2f640b88a4e45618b333920e65dfe988db66c0f04)、[NPM10XX_CHARGER_VTHROTTLE_125MV](#gga51fc3e1a4aa657d030209b1e2f640b88a67b674f960d97d7e089d6b3d37270e68)、[NPM10XX_CHARGER_VTHROTTLE_150MV](#gga51fc3e1a4aa657d030209b1e2f640b88ae47eecdc5eb8efa490afb99e495ef054)、[NPM10XX_CHARGER_VTHROTTLE_175MV](#gga51fc3e1a4aa657d030209b1e2f640b88a85a31b2555549cccb5089e58fa0e37ed)、[NPM10XX_CHARGER_VTHROTTLE_200MV](#gga51fc3e1a4aa657d030209b1e2f640b88a3eb7141403396386412f6f50f778dd48)、[NPM10XX_CHARGER_VTHROTTLE_225MV](#gga51fc3e1a4aa657d030209b1e2f640b88a2a95bf55e11ce8daad49ada9cf7e051f)、[NPM10XX_CHARGER_VTHROTTLE_250MV](#gga51fc3e1a4aa657d030209b1e2f640b88a04e8c6f6ca79ef3ce3980ef47c58baa8)、[NPM10XX_CHARGER_VTHROTTLE_275MV](#gga51fc3e1a4aa657d030209b1e2f640b88aab2570493e5da1ba860d5a23859163e7)、[NPM10XX_CHARGER_VTHROTTLE_300MV](#gga51fc3e1a4aa657d030209b1e2f640b88ad0c98d2cd315171789da2e1c9d77aae0)、[NPM10XX_CHARGER_VTHROTTLE_325MV](#gga51fc3e1a4aa657d030209b1e2f640b88a7ede8e6af663b49ed5949cc33b1839a3)、[NPM10XX_CHARGER_VTHROTTLE_350MV](#gga51fc3e1a4aa657d030209b1e2f640b88afa5083a75c161410ec281111574b6d18)、[NPM10XX_CHARGER_VTHROTTLE_375MV](#gga51fc3e1a4aa657d030209b1e2f640b88a9def6f7f3b2ec46ae1d500541f9f40ee)、[NPM10XX_CHARGER_VTHROTTLE_400MV](#gga51fc3e1a4aa657d030209b1e2f640b88acb6321aef264d44040f077bdad150f3f)。

nPM10xx 充电器相对于终止电压（termination voltage）的限流电压档位（throttle voltage levels）。

## 3.2\_详细说明（Detailed Documentation）

<a id="ga0361b1ebfc18e176ed171823a38e12ab"></a>

### `npm10xx_charger_iterm`

```c
enum npm10xx_charger_iterm
```

```c
#include <zephyr/drivers/charger/npm10xx.h>
```

nPM10xx 充电器终止电流（termination current），以百分比表示。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_CHARGER_ITERM_12P5` | 终止电流（Termination Current）等于充电电流（Charge Current）的 12.5%。 |
| `NPM10XX_CHARGER_ITERM_100P` | 终止电流（Termination Current）等于充电电流（Charge Current）的 100%。 |
| `NPM10XX_CHARGER_ITERM_50P` | 终止电流（Termination Current）等于充电电流（Charge Current）的 50%。 |
| `NPM10XX_CHARGER_ITERM_25P` | 终止电流（Termination Current）等于充电电流（Charge Current）的 25%。 |
| `NPM10XX_CHARGER_ITERM_6P25` | 终止电流（Termination Current）等于充电电流（Charge Current）的 6.25%。 |
| `NPM10XX_CHARGER_ITERM_3P125` | 终止电流（Termination Current）等于充电电流（Charge Current）的 3.125%。 |
| `NPM10XX_CHARGER_ITERM_1P56` | 终止电流（Termination Current）等于充电电流（Charge Current）的 1.56%。 |
| `NPM10XX_CHARGER_ITERM_0P78` | 终止电流（Termination Current）等于充电电流（Charge Current）的 0.78%。 |
| `NPM10XX_CHARGER_CURRENT_PERCENT_MAX` | 标记有效枚举值（Valid Enum Values）的结束。 |

<a id="ga2e2382e875599723272916c8eda7e693"></a>

### `npm10xx_charger_ithrottle`

```c
enum npm10xx_charger_ithrottle
```

```c
#include <zephyr/drivers/charger/npm10xx.h>
```

nPM10xx 充电器限流电流（throttle current），以百分比表示。

与一个 `enum npm10xx_charger_vthrottle` 值组合，用于配置充电限流（Charge Throttling）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_CHARGER_ITHROTTLE_100P` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 100%。 |
| `NPM10XX_CHARGER_ITHROTTLE_87P5` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 87.5%。 |
| `NPM10XX_CHARGER_ITHROTTLE_75P` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 75%。 |
| `NPM10XX_CHARGER_ITHROTTLE_62P5` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 62.5%。 |
| `NPM10XX_CHARGER_ITHROTTLE_50P` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 50%。 |
| `NPM10XX_CHARGER_ITHROTTLE_37P5` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 37.5%。 |
| `NPM10XX_CHARGER_ITHROTTLE_25P` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 25%。 |
| `NPM10XX_CHARGER_ITHROTTLE_12P5` | 限流电流（Throttle Current）等于充电电流（Charge Current）的 12.5%。 |

<a id="ga645f680cc19e3d6f0c777dfa41b3abae"></a>

### `npm10xx_charger_itrickle`

```c
enum npm10xx_charger_itrickle
```

```c
#include <zephyr/drivers/charger/npm10xx.h>
```

nPM10xx 充电器涓流电流（trickle current），以百分比表示。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_CHARGER_ITRICKLE_12P5` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 12.5%。 |
| `NPM10XX_CHARGER_ITRICKLE_100P` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 100%。 |
| `NPM10XX_CHARGER_ITRICKLE_50P` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 50%。 |
| `NPM10XX_CHARGER_ITRICKLE_25P` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 25%。 |
| `NPM10XX_CHARGER_ITRICKLE_6P25` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 6.25%。 |
| `NPM10XX_CHARGER_ITRICKLE_3P125` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 3.125%。 |
| `NPM10XX_CHARGER_ITRICKLE_1P56` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 1.56%。 |
| `NPM10XX_CHARGER_ITRICKLE_0P78` | 涓流电流（Trickle Current）等于充电电流（Charge Current）的 0.78%。 |

<a id="ga2de09557c2f7d19ad141ca8ba48e9f5d"></a>

### `npm10xx_charger_prop`

```c
enum npm10xx_charger_prop
```

```c
#include <zephyr/drivers/charger/npm10xx.h>
```

nPM10xx 充电器（Charger）的自定义属性。

扩展 `enum charger_property`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_CHARGER_PROP_TERM_CURRENT` | 充电终止电流（Charging Termination Current），以恒定充电电流（Constant Charging Current）的百分比表示。值的类型应为 `enum npm10xx_charger_iterm`。 |
| `NPM10XX_CHARGER_PROP_TRICKLE_CURRENT` | 充电涓流电流（Charging Trickle Current），以恒定充电电流（Constant Charging Current）的百分比表示。值的类型应为 `enum npm10xx_charger_itrickle`。 |
| `NPM10XX_CHARGER_PROP_THROTTLE_LVL` | 充电限流配置（Charge Throttling Configuration）。值应由一个 `enum npm10xx_charger_ithrottle` 值与一个 `enum npm10xx_charger_vthrottle` 值按位或（Bitwise OR）组成，例如 `NPM10XX_CHARGER_ITHROTTLE_75P \| NPM10XX_CHARGER_VTHROTTLE_100MV`。 |
| `NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_WARM_UA` | NTC 温暖区（Warm Region）的充电电流目标值（Charge Current Target），以 μA 为单位。 |
| `NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_COOL_UA` | NTC 偏冷区（Cool Region）的充电电流目标值（Charge Current Target），以 μA 为单位。 |
| `NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_WARM_UV` | NTC 温暖区（Warm Region）的充电电压调节目标值（Charge Voltage Regulation Target），以 μV 为单位。 |
| `NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_COOL_UV` | NTC 偏冷区（Cool Region）的充电电压调节目标值（Charge Voltage Regulation Target），以 μV 为单位。 |

<a id="ga51fc3e1a4aa657d030209b1e2f640b88"></a>

### `npm10xx_charger_vthrottle`

```c
enum npm10xx_charger_vthrottle
```

```c
#include <zephyr/drivers/charger/npm10xx.h>
```

nPM10xx 充电器相对于终止电压（termination voltage）的限流电压档位（throttle voltage levels）。

与一个 `enum npm10xx_charger_ithrottle` 值组合，用于配置充电限流（Charge Throttling）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_CHARGER_VTHROTTLE_25MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 25 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_50MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 50 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_75MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 75 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_100MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 100 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_125MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 125 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_150MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 150 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_175MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 175 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_200MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 200 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_225MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 225 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_250MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 250 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_275MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 275 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_300MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 300 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_325MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 325 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_350MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 350 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_375MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 375 mV。 |
| `NPM10XX_CHARGER_VTHROTTLE_400MV` | 限流电压（Throttle Voltage）比终止电压（Termination Voltage）低 400 mV。 |


## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/charger/npm10xx.h](../api_file_interface_reference/P013_zephyr__drivers__charger__npm10xx.h_文件参考.md)
- [charger_property](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga6eb3b4cc76e4f1e34732b7853eb860b7)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12aba0959a4ef28fcfd44de6f4c852744e197"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12abad6f6c26c8759613c05a10592ac628d15"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12aba44ed6f6aea9feee4577635fffc480dfb"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12abab7aaa32e285208f86889cc7d7a0060c0"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12aba25a044f38b048ff0451e556b42534b67"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12abae981727f782b8459d41757151b0cdcf7"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12abafa68639f27c5366ad45db5c56f2268af"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12aba8ca1895fc6fe1a8660f2e2b2452c5f59"></a>
<a id="gga0361b1ebfc18e176ed171823a38e12aba911e517245594be44d2c4cc971cee1bd"></a>
<a id="gga2e2382e875599723272916c8eda7e693ac91db4439de44f8137eb8a723491e0cf"></a>
<a id="gga2e2382e875599723272916c8eda7e693af9c1e0e4bb3dbf2a3f59a6dc07e61756"></a>
<a id="gga2e2382e875599723272916c8eda7e693a24a0a5e7f1ab78f0ac8245a59ee4c1b8"></a>
<a id="gga2e2382e875599723272916c8eda7e693a556ac103ce88c27b2e134570f131006f"></a>
<a id="gga2e2382e875599723272916c8eda7e693a6b73937a3b83e16c6d2829a35d950312"></a>
<a id="gga2e2382e875599723272916c8eda7e693a498a1b6c5493c7bd649b6039a1c95c99"></a>
<a id="gga2e2382e875599723272916c8eda7e693a608716ba46dc88ed9728aee15ae878aa"></a>
<a id="gga2e2382e875599723272916c8eda7e693a92a054648b92527a1e40e7373808c398"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea7b97b37ac08b922c7382d92ce2c22890"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea870a1db010506badc4f1579d3d1a7d74"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea25c61182f513f6da143e5c77954bece4"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaeaccdcdd78cd8ba973a1a74ba1a629b609"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea2158df739371f0cd8dfadb37b56356c7"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea634f230faf1547e0ae7a396be6bc4bcb"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaeadb4f86e7b444dd47b417489ce074acf1"></a>
<a id="gga645f680cc19e3d6f0c777dfa41b3abaea9bff02ec00c10b480cbeda27c8e78c8f"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5da43de07adf7b4c2ee51c4c415cf767e81"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5daec4b5f597aff98e289e5b826e2bf0b01"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5dadd0b75d418d1b9439ed16383185f7b9e"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5da5b8931185580b5f5b21adb117af0a407"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5dac1783198b9b10317142dcd3c0d614c76"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5da9bf9927db001f17b40d71665634662c4"></a>
<a id="gga2de09557c2f7d19ad141ca8ba48e9f5da16efc7a009faff4fdecb0548cfee8e67"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a8d7fdc23a114a55170c4ae555381fe5b"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a9d09acf1922030fb519ca092a7527e62"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88aa2f1d279f26a3225fc198e491ff7fcf6"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a4e45618b333920e65dfe988db66c0f04"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a67b674f960d97d7e089d6b3d37270e68"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88ae47eecdc5eb8efa490afb99e495ef054"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a85a31b2555549cccb5089e58fa0e37ed"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a3eb7141403396386412f6f50f778dd48"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a2a95bf55e11ce8daad49ada9cf7e051f"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a04e8c6f6ca79ef3ce3980ef47c58baa8"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88aab2570493e5da1ba860d5a23859163e7"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88ad0c98d2cd315171789da2e1c9d77aae0"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a7ede8e6af663b49ed5949cc33b1839a3"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88afa5083a75c161410ec281111574b6d18"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88a9def6f7f3b2ec46ae1d500541f9f40ee"></a>
<a id="gga51fc3e1a4aa657d030209b1e2f640b88acb6321aef264d44040f077bdad150f3f"></a>

---

[上一章](P002_蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）.md) · [返回大纲](大纲.md) · [下一章](P004_连接管理器连接性 API（Connectivity API）.md)
