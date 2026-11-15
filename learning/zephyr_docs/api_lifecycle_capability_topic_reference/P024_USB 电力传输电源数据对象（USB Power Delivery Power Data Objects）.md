---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-24
title: USB 电力传输电源数据对象（USB Power Delivery Power Data Objects）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_USB 电力传输电源数据对象（USB Power Delivery Power Data Objects）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

构建 USB 电力传输电源数据对象（Power Data Object，PDO）的宏。

<a id="details"></a>

构造 USB 电力传输（USB Power Delivery）电源数据对象（Power Data Objects，PDO）的宏。辅助宏用于构造 USB Power Delivery 规范定义的 32 位 PDO，供供电端／受电端（Source/Sink）能力协商时交换。它们主要用于设备树（Devicetree），描述 USB-C 端口的能力，例如下方原始示例。

```c
source-pdos = <PDO_FIXED(5000, 100, PDO_FIXED_DUAL_ROLE)>;
```

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="r_ga9fa615ab7f38385c21277d4e9e6a1441"></a>

```c
#define PDO_FIXED(mv, ma, flags)
```

相关声明：[PDO_FIXED](#ga9fa615ab7f38385c21277d4e9e6a1441)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

构造固定供电电源数据对象（Fixed Supply PDO）。

<a id="r_gae3c4f39fb7ff5b00bdc25676af3b88f7"></a>

```c
#define VSAFE5V 5000
```

相关声明：[VSAFE5V](#gae3c4f39fb7ff5b00bdc25676af3b88f7)。

`vSafe5V`：默认 5 V 供电，单位为毫伏（Millivolts）。

<a id="r_ga37daa9cc2b8482e127d31c2f3ea4e7ed"></a>

```c
#define PDO_BATT(min_mv, max_mv, max_mw)
```

相关声明：[PDO_BATT](#ga37daa9cc2b8482e127d31c2f3ea4e7ed)。

构造电池供电电源数据对象（Battery Supply PDO）。

<a id="r_ga359cf8ce52c69924cd2962b2a766f794"></a>

```c
#define PDO_VAR(min_mv, max_mv, max_ma)
```

相关声明：[PDO_VAR](#ga359cf8ce52c69924cd2962b2a766f794)。

构造可变供电、非电池类电源数据对象（Variable Supply, Non-Battery PDO）。

<a id="r_ga48f8ae89ab76eae6f27585b389f2b33b"></a>

```c
#define PDO_PPS_APDO(min_mv, max_mv, max_ma)
```

相关声明：[PDO_PPS_APDO](#ga48f8ae89ab76eae6f27585b389f2b33b)。

构造可编程电源（Programmable Power Supply，PPS）增强型电源数据对象（Augmented PDO）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 24.2\_固定供电 PDO 能力标志（Fixed Supply PDO Capability Flags）

<a id="r_ga06df29b5b810f22013ad2135cb0238ea"></a>

```c
#define PDO_FIXED_DUAL_ROLE (1 << 29)
```

相关声明：[PDO_FIXED_DUAL_ROLE](#ga06df29b5b810f22013ad2135cb0238ea)。

支持供电角色交换（Power Role Swap）。

<a id="r_ga869842bccecddf1941826fba3399f735"></a>

```c
#define PDO_FIXED_SUSPEND (1 << 28)
```

相关声明：[PDO_FIXED_SUSPEND](#ga869842bccecddf1941826fba3399f735)。

支持 USB 挂起（USB Suspend），适用于供电端（Source）。

<a id="r_gae7692e9c32e7c6ee2cf8e4c84d0752d8"></a>

```c
#define PDO_FIXED_HIGHER_CAP (1 << 28)
```

相关声明：[PDO_FIXED_HIGHER_CAP](#gae7692e9c32e7c6ee2cf8e4c84d0752d8)。

需要高于 `vSafe5V` 的供电，适用于受电端（Sink）。

<a id="r_ga9e098ecbd9e7b74052fcbf302a0f6a41"></a>

```c
#define PDO_FIXED_EXTPOWER (1 << 27)
```

相关声明：[PDO_FIXED_EXTPOWER](#ga9e098ecbd9e7b74052fcbf302a0f6a41)。

由外部供电（Externally Powered）。

<a id="r_ga398ebc832c89bd8cbccd08b3def758dd"></a>

```c
#define PDO_FIXED_USB_COMM (1 << 26)
```

相关声明：[PDO_FIXED_USB_COMM](#ga398ebc832c89bd8cbccd08b3def758dd)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_ga17760e6fb2761a8d14d41f1f44993c3b"></a>

```c
#define PDO_FIXED_DATA_SWAP (1 << 25)
```

相关声明：[PDO_FIXED_DATA_SWAP](#ga17760e6fb2761a8d14d41f1f44993c3b)。

支持数据角色交换（Data Role Swap）。

## 24.3\_详细说明（Detailed Documentation）

<a id="ga37daa9cc2b8482e127d31c2f3ea4e7ed"></a>

### `PDO_BATT`

```c
#define PDO_BATT ( min_mv, max_mv, max_mw )
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

展开值（Value）：

```c
(PDO_TYPE(PDO_TYPE_BATT) | PDO_BATT_MIN_VOLT(min_mv) |  \
 PDO_BATT_MAX_VOLT(max_mv) | PDO_BATT_MAX_POWER(max_mw))
```

构造电池供电电源数据对象（Battery Supply PDO）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_mv` | 最低电压（Minimum Voltage），单位为毫伏。 |
| `max_mv` | 最高电压（Maximum Voltage），单位为毫伏。 |
| `max_mw` | 最大功率（Maximum Power），单位为毫瓦。 |

**返回（Returns）**：**返回值（Returns）：**32 位电池供电 PDO（Battery Supply PDO）。

<a id="ga9fa615ab7f38385c21277d4e9e6a1441"></a>

### `PDO_FIXED`

```c
#define PDO_FIXED ( mv, ma, flags )
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

展开值（Value）：

```c
(PDO_TYPE(PDO_TYPE_FIXED) | (flags) |           \
 PDO_FIXED_VOLT(mv) | PDO_FIXED_CURR(ma))
```

构造固定供电电源数据对象（Fixed Supply PDO）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mv` | 输出电压（Output Voltage），单位为毫伏。 |
| `ma` | 最大输出电流（Maximum Output Current），单位为毫安。 |
| `flags` | 对 `PDO_FIXED_*` 能力标志（Capability Flags）进行按位或（Bitwise OR）。 |

**返回（Returns）**：**返回值（Returns）：**32 位固定供电 PDO（Fixed Supply PDO）。

<a id="ga17760e6fb2761a8d14d41f1f44993c3b"></a>

### `PDO_FIXED_DATA_SWAP`

```c
#define PDO_FIXED_DATA_SWAP (1 << 25)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

支持数据角色交换（Data Role Swap）。

<a id="ga06df29b5b810f22013ad2135cb0238ea"></a>

### `PDO_FIXED_DUAL_ROLE`

```c
#define PDO_FIXED_DUAL_ROLE (1 << 29)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

支持供电角色交换（Power Role Swap）。

<a id="ga9e098ecbd9e7b74052fcbf302a0f6a41"></a>

### `PDO_FIXED_EXTPOWER`

```c
#define PDO_FIXED_EXTPOWER (1 << 27)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

由外部供电（Externally Powered）。

<a id="gae7692e9c32e7c6ee2cf8e4c84d0752d8"></a>

### `PDO_FIXED_HIGHER_CAP`

```c
#define PDO_FIXED_HIGHER_CAP (1 << 28)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

需要高于 `vSafe5V` 的供电，适用于受电端（Sink）。

<a id="ga869842bccecddf1941826fba3399f735"></a>

### `PDO_FIXED_SUSPEND`

```c
#define PDO_FIXED_SUSPEND (1 << 28)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

支持 USB 挂起（USB Suspend），适用于供电端（Source）。

<a id="ga398ebc832c89bd8cbccd08b3def758dd"></a>

### `PDO_FIXED_USB_COMM`

```c
#define PDO_FIXED_USB_COMM (1 << 26)
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

具备 USB 通信能力（USB Communications Capable）。

<a id="ga48f8ae89ab76eae6f27585b389f2b33b"></a>

### `PDO_PPS_APDO`

```c
#define PDO_PPS_APDO ( min_mv, max_mv, max_ma )
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

展开值（Value）：

```c
(PDO_TYPE(PDO_TYPE_APDO) | PDO_APDO_TYPE(APDO_TYPE_PPS) |               \
 PDO_PPS_APDO_MIN_VOLT(min_mv) | PDO_PPS_APDO_MAX_VOLT(max_mv) |        \
 PDO_PPS_APDO_MAX_CURR(max_ma))
```

构造可编程电源（Programmable Power Supply，PPS）增强型电源数据对象（Augmented PDO）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_mv` | 最低电压（Minimum Voltage），单位为毫伏。 |
| `max_mv` | 最高电压（Maximum Voltage），单位为毫伏。 |
| `max_ma` | 最大电流（Maximum Current），单位为毫安。 |

**返回（Returns）**：**返回值（Returns）：**32 位可编程电源增强型 PDO（PPS APDO）。

<a id="ga359cf8ce52c69924cd2962b2a766f794"></a>

### `PDO_VAR`

```c
#define PDO_VAR ( min_mv, max_mv, max_ma )
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

展开值（Value）：

```c
(PDO_TYPE(PDO_TYPE_VAR) | PDO_VAR_MIN_VOLT(min_mv) |    \
 PDO_VAR_MAX_VOLT(max_mv) | PDO_VAR_MAX_CURR(max_ma))
```

构造可变供电、非电池类电源数据对象（Variable Supply, Non-Battery PDO）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_mv` | 最低电压（Minimum Voltage），单位为毫伏。 |
| `max_mv` | 最高电压（Maximum Voltage），单位为毫伏。 |
| `max_ma` | 最大电流（Maximum Current），单位为毫安。 |

**返回（Returns）**：**返回值（Returns）：**32 位可变供电 PDO（Variable Supply PDO）。

<a id="gae3c4f39fb7ff5b00bdc25676af3b88f7"></a>

### `VSAFE5V`

```c
#define VSAFE5V 5000
```

```c
#include <zephyr/dt-bindings/usb-c/pd.h>
```

`vSafe5V`：默认 5 V 供电，单位为毫伏（Millivolts）。


## 24.4\_原页交叉引用（Cross References）

- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/dt-bindings/usb-c/pd.h](../api_file_system_power_reference/P033_zephyr__dt-bindings__usb-c__pd.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

---

[上一章](P023_ST87Mxx API主题.md) · [返回大纲](大纲.md) · [下一章](P025_VEML60XX API主题.md)
