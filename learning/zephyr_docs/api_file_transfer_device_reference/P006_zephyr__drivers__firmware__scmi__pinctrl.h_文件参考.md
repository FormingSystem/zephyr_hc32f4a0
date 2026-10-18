---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-6
title: zephyr__drivers__firmware__scmi__pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）引脚控制协议（Pin Control Protocol）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）引脚控制协议（Pin Control Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_scmi_5Fpinctrl_5Fsettings"></a>

```c
struct scmi_pinctrl_settings
```

相关声明：[scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)。

描述PINCTRL_SETTINGS_CONFIGURE命令的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga5856f69a41daebeb67bc675549a94082"></a>

```c
#define ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE (10 * 2)
```

相关声明：[ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga5856f69a41daebeb67bc675549a94082)。

`PINCTRL_SETTINGS_CONFIGURE` 命令携带的配置字（Configuration Word）数量上限。

<a id="r_gad3e2c57ca0d05f266c13ad5efda5f822"></a>

```c
#define SCMI_PINCTRL_NO_FUNCTION 0xFFFFFFFF
```

相关声明：[SCMI_PINCTRL_NO_FUNCTION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad3e2c57ca0d05f266c13ad5efda5f822)。

`scmi_pinctrl_settings::function` 的哨兵值（Sentinel Value），表示“无功能”（No Function）。

<a id="r_ga8a504f804ca89f1fc7c7c2f8298f5b9e"></a>

```c
#define SCMI_PINCTRL_CONFIG_ATTRIBUTES(fid_valid, cfg_num, selector)
```

相关声明：[SCMI_PINCTRL_CONFIG_ATTRIBUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga8a504f804ca89f1fc7c7c2f8298f5b9e)。

构造 `PINCTRL_SETTINGS_CONFIGURE` 命令的属性字（Attributes Word）。

<a id="r_ga563b6183eda65630c1883af094585095"></a>

```c
#define SCMI_PINCTRL_SELECTOR_PIN 0x0
```

相关声明：[SCMI_PINCTRL_SELECTOR_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga563b6183eda65630c1883af094585095)。

选择器值（Selector Value）：设置应用于单个引脚（Pin）。

<a id="r_ga2d4fff080b1f6c62d3afb6de24c925ae"></a>

```c
#define SCMI_PINCTRL_SELECTOR_GROUP 0x1
```

相关声明：[SCMI_PINCTRL_SELECTOR_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga2d4fff080b1f6c62d3afb6de24c925ae)。

选择器值（Selector Value）：设置应用于一组引脚（Group of Pins）。

<a id="r_gadd032f5989f91f734db10ca382cb6c11"></a>

```c
#define SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM(attributes)
```

相关声明：[SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gadd032f5989f91f734db10ca382cb6c11)。

从属性字（Attributes Word）中提取配置数量（Number of Configurations）。

<a id="r_ga9b673f726491bf302b74f34574274340"></a>

```c
#define SCMI_PINCTRL_ATTRIBUTES_FID_VALID(attributes)
```

相关声明：[SCMI_PINCTRL_ATTRIBUTES_FID_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga9b673f726491bf302b74f34574274340)。

从属性字（Attributes Word）中提取 `fid_valid`：功能 ID 字段有效时为 `1`，否则为 `0`。

<a id="r_ga26ceba36b1f07c6314a4ddedbe3785d1"></a>

```c
#define SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION 0x10000
```

相关声明：[SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga26ceba36b1f07c6314a4ddedbe3785d1)。

本驱动支持的 SCMI 引脚控制协议（Pin Control Protocol）版本。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_gab5208b8108578e82acfa5dd0c8a2a96b"></a>

```c
enum scmi_pinctrl_config { SCMI_PINCTRL_DEFAULT = 0 , SCMI_PINCTRL_BIAS_BUS_HOLD = 1 , SCMI_PINCTRL_BIAS_DISABLE = 2 , SCMI_PINCTRL_BIAS_HIGH_Z = 3 , SCMI_PINCTRL_BIAS_PULL_UP = 4 , SCMI_PINCTRL_BIAS_PULL_DEFAULT = 5 , SCMI_PINCTRL_BIAS_PULL_DOWN = 6 , SCMI_PINCTRL_DRIVE_OPEN_DRAIN = 7 , SCMI_PINCTRL_DRIVE_OPEN_SOURCE = 8 , SCMI_PCINTRL_DRIVE_PUSH_PULL = 9 , SCMI_PCINTRL_DRIVE_STRENGTH = 10 , SCMI_PINCTRL_INPUT_DEBOUNCE = 11 , SCMI_PINCTRL_INPUT_MODE = 12 , SCMI_PINCTRL_PULL_MODE = 13 , SCMI_PINCTRL_INPUT_VALUE = 14 , SCMI_PINCTRL_INPUT_SCHMITT = 15 , SCMI_PINCTRL_LP_MODE = 16 , SCMI_PINCTRL_OUTPUT_MODE = 17 , SCMI_PINCTRL_OUTPUT_VALUE = 18 , SCMI_PINCTRL_POWER_SOURCE = 19 , SCMI_PINCTRL_SLEW_RATE = 20 , SCMI_PINCTRL_RESERVED_START = 21 , SCMI_PINCTRL_RESERVED_END = 191 , SCMI_PINCTRL_VENDOR_START = 192 }
```

相关声明：[scmi_pinctrl_config](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gab5208b8108578e82acfa5dd0c8a2a96b)、[SCMI_PINCTRL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b)、[SCMI_PINCTRL_BIAS_BUS_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55)、[SCMI_PINCTRL_BIAS_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8)、[SCMI_PINCTRL_BIAS_HIGH_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432)、[SCMI_PINCTRL_BIAS_PULL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e)、[SCMI_PINCTRL_BIAS_PULL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2)、[SCMI_PINCTRL_BIAS_PULL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692)、[SCMI_PINCTRL_DRIVE_OPEN_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d)、[SCMI_PINCTRL_DRIVE_OPEN_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54)、[SCMI_PCINTRL_DRIVE_PUSH_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227)、[SCMI_PCINTRL_DRIVE_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3)、[SCMI_PINCTRL_INPUT_DEBOUNCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4)、[SCMI_PINCTRL_INPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4)、[SCMI_PINCTRL_PULL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65)、[SCMI_PINCTRL_INPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5)、[SCMI_PINCTRL_INPUT_SCHMITT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be)、[SCMI_PINCTRL_LP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691)、[SCMI_PINCTRL_OUTPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378)、[SCMI_PINCTRL_OUTPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359)、[SCMI_PINCTRL_POWER_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905)、[SCMI_PINCTRL_SLEW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629)、[SCMI_PINCTRL_RESERVED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727)、[SCMI_PINCTRL_RESERVED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171)、[SCMI_PINCTRL_VENDOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696)。

引脚控制配置（Pinctrl Configurations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gad7d9ca78b75cc32edefc1ea8e0e0c09e"></a>

```c
int scmi_pinctrl_settings_configure (struct scmi_pinctrl_settings *settings)
```

相关声明：[scmi_pinctrl_settings_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad7d9ca78b75cc32edefc1ea8e0e0c09e)、[scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)。

发送 `PINCTRL_SETTINGS_CONFIGURE` 命令并获取回复（Reply）。


## 6.5\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](../api_source_reference/P156_protocol.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P155_pinctrl.h_源码浏览.md)
- [scmi_pinctrl_settings](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md)
- [ARM_SCMI_PINCTRL_MAX_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga5856f69a41daebeb67bc675549a94082)
- [SCMI_PINCTRL_NO_FUNCTION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad3e2c57ca0d05f266c13ad5efda5f822)
- [scmi_pinctrl_settings::function](../platform_security_model_reference/P044_scmi_pinctrl_settings_结构体.md#ade79b6c3efc5b069f74ad6e12088d6c2)
- [SCMI_PINCTRL_CONFIG_ATTRIBUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga8a504f804ca89f1fc7c7c2f8298f5b9e)
- [SCMI_PINCTRL_SELECTOR_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga563b6183eda65630c1883af094585095)
- [SCMI_PINCTRL_SELECTOR_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga2d4fff080b1f6c62d3afb6de24c925ae)
- [SCMI_PINCTRL_ATTRIBUTES_CONFIG_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gadd032f5989f91f734db10ca382cb6c11)
- [SCMI_PINCTRL_ATTRIBUTES_FID_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga9b673f726491bf302b74f34574274340)
- [SCMI_PIN_CONTROL_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga26ceba36b1f07c6314a4ddedbe3785d1)
- [scmi_pinctrl_config](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gab5208b8108578e82acfa5dd0c8a2a96b)
- [SCMI_PINCTRL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b)
- [SCMI_PINCTRL_BIAS_BUS_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55)
- [SCMI_PINCTRL_BIAS_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8)
- [SCMI_PINCTRL_BIAS_HIGH_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432)
- [SCMI_PINCTRL_BIAS_PULL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e)
- [SCMI_PINCTRL_BIAS_PULL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2)
- [SCMI_PINCTRL_BIAS_PULL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692)
- [SCMI_PINCTRL_DRIVE_OPEN_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d)
- [SCMI_PINCTRL_DRIVE_OPEN_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54)
- [SCMI_PCINTRL_DRIVE_PUSH_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227)
- [SCMI_PCINTRL_DRIVE_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3)
- [SCMI_PINCTRL_INPUT_DEBOUNCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4)
- [SCMI_PINCTRL_INPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4)
- [SCMI_PINCTRL_PULL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65)
- [SCMI_PINCTRL_INPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5)
- [SCMI_PINCTRL_INPUT_SCHMITT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be)
- [SCMI_PINCTRL_LP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691)
- [SCMI_PINCTRL_OUTPUT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378)
- [SCMI_PINCTRL_OUTPUT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359)
- [SCMI_PINCTRL_POWER_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905)
- [SCMI_PINCTRL_SLEW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629)
- [SCMI_PINCTRL_RESERVED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727)
- [SCMI_PINCTRL_RESERVED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171)
- [SCMI_PINCTRL_VENDOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ggab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696)
- [scmi_pinctrl_settings_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad7d9ca78b75cc32edefc1ea8e0e0c09e)

<a id="header-details"></a>

---

[上一章](P005_zephyr__drivers__firmware__scmi__nxp__cpu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__mfd__axp192.h_文件参考.md)
