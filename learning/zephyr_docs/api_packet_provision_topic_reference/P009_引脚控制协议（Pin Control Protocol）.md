---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-9
title: 引脚控制协议（Pin Control Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_引脚控制协议（Pin Control Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 进行引脚配置与控制。

<a id="details"></a>

通过 SCMI 进行引脚配置与控制。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_pinctrl_2Eh"></a>

```c
file pinctrl.h
```

相关声明：[pinctrl.h](../api_file_transfer_device_reference/P006_zephyr__drivers__firmware__scmi__pinctrl.h_文件参考.md)。

系统控制与管理接口（SCMI）引脚控制协议（Pin Control Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_scmi_5Fpinctrl_5Fsettings"></a>

```c
struct scmi_pinctrl_settings
```

相关声明：[scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)。

描述PINCTRL_SETTINGS_CONFIGURE命令的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.3\_宏定义（Macros）

<a id="r_ga5856f69a41daebeb67bc675549a94082"></a>

```c
#define ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE (10 * 2)
```

相关声明：[ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE](#ga5856f69a41daebeb67bc675549a94082)。

`PINCTRL_SETTINGS_CONFIGURE` 命令携带的配置字（Configuration Word）数量上限。

<a id="r_gad3e2c57ca0d05f266c13ad5efda5f822"></a>

```c
#define SCMI_PINCTRL_NO_FUNCTION 0xFFFFFFFF
```

相关声明：[SCMI_PINCTRL_NO_FUNCTION](#gad3e2c57ca0d05f266c13ad5efda5f822)。

`scmi_pinctrl_settings::function` 的哨兵值（Sentinel Value），表示“无功能”（No Function）。

<a id="r_ga8a504f804ca89f1fc7c7c2f8298f5b9e"></a>

```c
#define SCMI_PINCTRL_CONFIG_ATTRIBUTES(fid_valid, cfg_num, selector)
```

相关声明：[SCMI_PINCTRL_CONFIG_ATTRIBUTES](#ga8a504f804ca89f1fc7c7c2f8298f5b9e)。

构造 `PINCTRL_SETTINGS_CONFIGURE` 命令的属性字（Attributes Word）。

<a id="r_ga563b6183eda65630c1883af094585095"></a>

```c
#define SCMI_PINCTRL_SELECTOR_PIN 0x0
```

相关声明：[SCMI_PINCTRL_SELECTOR_PIN](#ga563b6183eda65630c1883af094585095)。

选择器值（Selector Value）：设置应用于单个引脚（Pin）。

<a id="r_ga2d4fff080b1f6c62d3afb6de24c925ae"></a>

```c
#define SCMI_PINCTRL_SELECTOR_GROUP 0x1
```

相关声明：[SCMI_PINCTRL_SELECTOR_GROUP](#ga2d4fff080b1f6c62d3afb6de24c925ae)。

选择器值（Selector Value）：设置应用于一组引脚（Group of Pins）。

<a id="r_gadd032f5989f91f734db10ca382cb6c11"></a>

```c
#define SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM(attributes)
```

相关声明：[SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM](#gadd032f5989f91f734db10ca382cb6c11)。

从属性字（Attributes Word）中提取配置数量（Number of Configurations）。

<a id="r_ga9b673f726491bf302b74f34574274340"></a>

```c
#define SCMI_PINCTRL_ATTRIBUTES_FID_VALID(attributes)
```

相关声明：[SCMI_PINCTRL_ATTRIBUTES_FID_VALID](#ga9b673f726491bf302b74f34574274340)。

从属性字（Attributes Word）中提取 `fid_valid`：功能 ID 字段有效时为 `1`，否则为 `0`。

<a id="r_ga26ceba36b1f07c6314a4ddedbe3785d1"></a>

```c
#define SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION 0x10000
```

相关声明：[SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION](#ga26ceba36b1f07c6314a4ddedbe3785d1)。

本驱动支持的 SCMI 引脚控制协议（Pin Control Protocol）版本。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_gab5208b8108578e82acfa5dd0c8a2a96b"></a>

```c
enum scmi_pinctrl_config { SCMI_PINCTRL_DEFAULT = 0 , SCMI_PINCTRL_BIAS_BUS_HOLD = 1 , SCMI_PINCTRL_BIAS_DISABLE = 2 , SCMI_PINCTRL_BIAS_HIGH_Z = 3 , SCMI_PINCTRL_BIAS_PULL_UP = 4 , SCMI_PINCTRL_BIAS_PULL_DEFAULT = 5 , SCMI_PINCTRL_BIAS_PULL_DOWN = 6 , SCMI_PINCTRL_DRIVE_OPEN_DRAIN = 7 , SCMI_PINCTRL_DRIVE_OPEN_SOURCE = 8 , SCMI_PCINTRL_DRIVE_PUSH_PULL = 9 , SCMI_PCINTRL_DRIVE_STRENGTH = 10 , SCMI_PINCTRL_INPUT_DEBOUNCE = 11 , SCMI_PINCTRL_INPUT_MODE = 12 , SCMI_PINCTRL_PULL_MODE = 13 , SCMI_PINCTRL_INPUT_VALUE = 14 , SCMI_PINCTRL_INPUT_SCHMITT = 15 , SCMI_PINCTRL_LP_MODE = 16 , SCMI_PINCTRL_OUTPUT_MODE = 17 , SCMI_PINCTRL_OUTPUT_VALUE = 18 , SCMI_PINCTRL_POWER_SOURCE = 19 , SCMI_PINCTRL_SLEW_RATE = 20 , SCMI_PINCTRL_RESERVED_START = 21 , SCMI_PINCTRL_RESERVED_END = 191 , SCMI_PINCTRL_VENDOR_START = 192 }
```

相关声明：[scmi_pinctrl_config](#gab5208b8108578e82acfa5dd0c8a2a96b)、[SCMI_PINCTRL_DEFAULT](#ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b)、[SCMI_PINCTRL_BIAS_BUS_HOLD](#ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55)、[SCMI_PINCTRL_BIAS_DISABLE](#ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8)、[SCMI_PINCTRL_BIAS_HIGH_Z](#ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432)、[SCMI_PINCTRL_BIAS_PULL_UP](#ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e)、[SCMI_PINCTRL_BIAS_PULL_DEFAULT](#ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2)、[SCMI_PINCTRL_BIAS_PULL_DOWN](#ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692)、[SCMI_PINCTRL_DRIVE_OPEN_DRAIN](#ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d)、[SCMI_PINCTRL_DRIVE_OPEN_SOURCE](#ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54)、[SCMI_PCINTRL_DRIVE_PUSH_PULL](#ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227)、[SCMI_PCINTRL_DRIVE_STRENGTH](#ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3)、[SCMI_PINCTRL_INPUT_DEBOUNCE](#ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4)、[SCMI_PINCTRL_INPUT_MODE](#ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4)、[SCMI_PINCTRL_PULL_MODE](#ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65)、[SCMI_PINCTRL_INPUT_VALUE](#ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5)、[SCMI_PINCTRL_INPUT_SCHMITT](#ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be)、[SCMI_PINCTRL_LP_MODE](#ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691)、[SCMI_PINCTRL_OUTPUT_MODE](#ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378)、[SCMI_PINCTRL_OUTPUT_VALUE](#ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359)、[SCMI_PINCTRL_POWER_SOURCE](#ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905)、[SCMI_PINCTRL_SLEW_RATE](#ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629)、[SCMI_PINCTRL_RESERVED_START](#ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727)、[SCMI_PINCTRL_RESERVED_END](#ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171)、[SCMI_PINCTRL_VENDOR_START](#ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696)。

引脚控制配置（Pinctrl Configurations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_gad7d9ca78b75cc32edefc1ea8e0e0c09e"></a>

```c
int scmi_pinctrl_settings_configure (struct scmi_pinctrl_settings *settings)
```

相关声明：[scmi_pinctrl_settings_configure](#gad7d9ca78b75cc32edefc1ea8e0e0c09e)、[scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)。

发送 `PINCTRL_SETTINGS_CONFIGURE` 命令并获取回复（Reply）。

## 9.6\_详细说明（Detailed Documentation）

<a id="ga5856f69a41daebeb67bc675549a94082"></a>

### `ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE`

```c
#define ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE (10 * 2)
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

`PINCTRL_SETTINGS_CONFIGURE` 命令携带的配置字（Configuration Word）数量上限。

<a id="ga26ceba36b1f07c6314a4ddedbe3785d1"></a>

### `SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION 0x10000
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

本驱动支持的 SCMI 引脚控制协议（Pin Control Protocol）版本。

<a id="gadd032f5989f91f734db10ca382cb6c11"></a>

### `SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM`

```c
#define SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM ( attributes)
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

展开值（Value）：

```c
(((attributes) & GENMASK(9, 2)) >> 2)
```

从属性字（Attributes Word）中提取配置数量（Number of Configurations）。

<a id="ga9b673f726491bf302b74f34574274340"></a>

### `SCMI_PINCTRL_ATTRIBUTES_FID_VALID`

```c
#define SCMI_PINCTRL_ATTRIBUTES_FID_VALID ( attributes)
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

展开值（Value）：

```c
FIELD_GET(BIT(10), attributes)
```

从属性字（Attributes Word）中提取 `fid_valid`：功能 ID 字段有效时为 `1`，否则为 `0`。

<a id="ga8a504f804ca89f1fc7c7c2f8298f5b9e"></a>

### `SCMI_PINCTRL_CONFIG_ATTRIBUTES`

```c
#define SCMI_PINCTRL_CONFIG_ATTRIBUTES ( fid_valid, cfg_num, selector )
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

展开值（Value）：

```c
(SCMI_FIELD_MAKE(fid_valid, BIT(0), 10) |                       \
 SCMI_FIELD_MAKE(cfg_num, GENMASK(7, 0), 2) |                   \
 SCMI_FIELD_MAKE(selector, GENMASK(1, 0), 0))
```

构造 `PINCTRL_SETTINGS_CONFIGURE` 命令的属性字（Attributes Word）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fid_valid` | 函数 ID 字段有效时为 1，否则为 0。 |
| `cfg_num` | 命令携带的配置数量（Number of Configurations）。 |
| `selector` | 选择要配置的内容，参见 `SCMI_PINCTRL_SELECTOR_*`。 |

<a id="gad3e2c57ca0d05f266c13ad5efda5f822"></a>

### `SCMI_PINCTRL_NO_FUNCTION`

```c
#define SCMI_PINCTRL_NO_FUNCTION 0xFFFFFFFF
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

`scmi_pinctrl_settings::function` 的哨兵值（Sentinel Value），表示“无功能”（No Function）。

<a id="ga2d4fff080b1f6c62d3afb6de24c925ae"></a>

### `SCMI_PINCTRL_SELECTOR_GROUP`

```c
#define SCMI_PINCTRL_SELECTOR_GROUP 0x1
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

选择器值（Selector Value）：设置应用于一组引脚（Group of Pins）。

<a id="ga563b6183eda65630c1883af094585095"></a>

### `SCMI_PINCTRL_SELECTOR_PIN`

```c
#define SCMI_PINCTRL_SELECTOR_PIN 0x0
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

选择器值（Selector Value）：设置应用于单个引脚（Pin）。

<a id="gab5208b8108578e82acfa5dd0c8a2a96b"></a>

### `scmi_pinctrl_config`

```c
enum scmi_pinctrl_config
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

引脚控制配置（Pinctrl Configurations）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SCMI_PINCTRL_DEFAULT` | 默认配置（Default Configuration）。 |
| `SCMI_PINCTRL_BIAS_BUS_HOLD` | 使用总线保持电路（Bus Hold/Keeper Circuit）对引脚施加偏置（Bias）。 |
| `SCMI_PINCTRL_BIAS_DISABLE` | 禁用所有偏置（Biasing）。 |
| `SCMI_PINCTRL_BIAS_HIGH_Z` | 高阻态，即悬空偏置（High-impedance/Floating Bias）。 |
| `SCMI_PINCTRL_BIAS_PULL_UP` | 将引脚上拉（Pull Up）。 |
| `SCMI_PINCTRL_BIAS_PULL_DEFAULT` | 应用默认的上下拉偏置（Default Pull Bias）。 |
| `SCMI_PINCTRL_BIAS_PULL_DOWN` | 将引脚下拉（Pull Down）。 |
| `SCMI_PINCTRL_DRIVE_OPEN_DRAIN` | 开漏输出驱动（Open-drain Output Drive）。 |
| `SCMI_PINCTRL_DRIVE_OPEN_SOURCE` | 开源输出驱动（Open-source Output Drive）。 |
| `SCMI_PCINTRL_DRIVE_PUSH_PULL` | 推挽输出驱动（Push-pull Output Drive）。注意：为保持应用二进制接口（ABI）兼容性，保留原名称。 |
| `SCMI_PCINTRL_DRIVE_STRENGTH` | 输出驱动强度（Output Drive Strength）。注意：为保持应用二进制接口（ABI）兼容性，保留原名称。 |
| `SCMI_PINCTRL_INPUT_DEBOUNCE` | 输入去抖时间（Input Debounce Time）。 |
| `SCMI_PINCTRL_INPUT_MODE` | 输入模式使能（Input Mode Enable）。 |
| `SCMI_PINCTRL_PULL_MODE` | 上下拉模式选择（Pull Mode Selection）。 |
| `SCMI_PINCTRL_INPUT_VALUE` | 输入值。 |
| `SCMI_PINCTRL_INPUT_SCHMITT` | 输入施密特触发器使能（Input Schmitt-trigger Enable）。 |
| `SCMI_PINCTRL_LP_MODE` | 低功耗模式（Low-power Mode）。 |
| `SCMI_PINCTRL_OUTPUT_MODE` | 输出模式使能（Output Mode Enable）。 |
| `SCMI_PINCTRL_OUTPUT_VALUE` | 输出值（Output Value）。 |
| `SCMI_PINCTRL_POWER_SOURCE` | 电源选择（Power Source Selection）。 |
| `SCMI_PINCTRL_SLEW_RATE` | 输出转换速率（Output Slew Rate）。 |
| `SCMI_PINCTRL_RESERVED_START` | 第一个保留配置类型（Reserved Configuration Type）。 |
| `SCMI_PINCTRL_RESERVED_END` | 最后一个保留配置类型（Reserved Configuration Type）。 |
| `SCMI_PINCTRL_VENDOR_START` | 第一个厂商专用配置类型（Vendor-specific Configuration Type）。 |

<a id="gad7d9ca78b75cc32edefc1ea8e0e0c09e"></a>

### `scmi_pinctrl_settings_configure()`

```c
int scmi_pinctrl_settings_configure ( struct scmi_pinctrl_settings * settings)
```

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

发送 `PINCTRL_SETTINGS_CONFIGURE` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Settings` | 指向要应用的设置（Settings）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 9.7\_原页交叉引用（Cross References）

- [pinctrl.h](../api_file_transfer_device_reference/P006_zephyr__drivers__firmware__scmi__pinctrl.h_文件参考.md)
- [scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)
- [scmi_pinctrl_settings::function](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#ade79b6c3efc5b069f74ad6e12088d6c2)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SCMI_FIELD_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga21b369f9fa6d1a965ece4a589df88581)
- [设置（Settings）。](../storage/P063_设置子系统接口.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="agroup__scmi__util_html_ga21b369f9fa6d1a965ece4a589df88581"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171"></a>
<a id="ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_PCIe 控制器（PCIe Controller）.md) · [返回大纲](大纲.md) · [下一章](P010_安全外壳（SSH）服务器库.md)
