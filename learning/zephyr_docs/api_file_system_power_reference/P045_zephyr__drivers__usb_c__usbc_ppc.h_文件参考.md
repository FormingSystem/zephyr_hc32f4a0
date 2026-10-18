---
id: learning.zephyr-docs.api-file-system-power-reference.page-45
title: zephyr__drivers__usb_c__usbc_ppc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_drivers\_\_usb\_c\_\_usbc\_ppc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB Type-C电源路径控制器（Power Path Controller）的设备API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>
```

查看此文件的源码。

USB Type-C电源路径控制器（Power Path Controller）的设备API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 45.1\_数据结构（Data Structures）

<a id="r_usbc_5Fppc_5Fdriver_5Fapi"></a>

```c
struct usbc_ppc_driver_api
```

相关声明：[usbc_ppc_driver_api](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md)。

驱动操作（Driver Operations）：USB Type-C电源路径控制器（Power Path Controller）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 45.2\_类型定义（Typedefs）

<a id="r_ga8195a7a51eb5bd3cbcec985b97b84e73"></a>

```c
typedef void(* usbc_ppc_event_cb_t) (const struct device *dev, void *data, enum usbc_ppc_event ev)
```

相关声明：[usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)、[device](../device_reference/P002_设备对象结构.md)、[usbc_ppc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga3dbbb1a6701a3a79c9a1d148b239fcf9)。

用于通知电源路径控制器（PPC）事件的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 45.3\_枚举（Enumerations）

<a id="r_ga3dbbb1a6701a3a79c9a1d148b239fcf9"></a>

```c
enum usbc_ppc_event { USBC_PPC_EVENT_DEAD_BATTERY_ERROR = 0 , USBC_PPC_EVENT_SRC_OVERVOLTAGE , USBC_PPC_EVENT_SRC_REVERSE_CURRENT , USBC_PPC_EVENT_SRC_OVERCURRENT , USBC_PPC_EVENT_SRC_SHORT , USBC_PPC_EVENT_OVER_TEMPERATURE , USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED , USBC_PPC_EVENT_SNK_REVERSE_CURRENT , USBC_PPC_EVENT_SNK_SHORT , USBC_PPC_EVENT_SNK_OVERVOLTAGE }
```

相关声明：[usbc_ppc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga3dbbb1a6701a3a79c9a1d148b239fcf9)、[USBC_PPC_EVENT_DEAD_BATTERY_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e)、[USBC_PPC_EVENT_SRC_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109)、[USBC_PPC_EVENT_SRC_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6)、[USBC_PPC_EVENT_SRC_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238)、[USBC_PPC_EVENT_SRC_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4)、[USBC_PPC_EVENT_OVER_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c)、[USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94)、[USBC_PPC_EVENT_SNK_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759)、[USBC_PPC_EVENT_SNK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d)、[USBC_PPC_EVENT_SNK_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)。

电源路径控制器（Power Path Controller）通知的事件类型（Event Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 45.4\_函数（Functions）

<a id="r_ga5f70af9a0d0336c208ff4f7a90c4b665"></a>

```c
static int ppc_is_dead_battery_mode (const struct device *dev)
```

相关声明：[ppc_is_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga5f70af9a0d0336c208ff4f7a90c4b665)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否处于电池耗尽模式（Dead Battery Mode）。

<a id="r_gabcbebdf47ca1c8a9b7c2e803bb833f5a"></a>

```c
static int ppc_exit_dead_battery_mode (const struct device *dev)
```

相关声明：[ppc_exit_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gabcbebdf47ca1c8a9b7c2e803bb833f5a)、[device](../device_reference/P002_设备对象结构.md)。

请求 PPC 退出电池耗尽模式（Dead Battery Mode）。本调用返回并不代表 PPC 已经退出该模式。

<a id="r_gaab85fda6d4030c83052deb1965d814f3"></a>

```c
static int ppc_is_vbus_source (const struct device *dev)
```

相关声明：[ppc_is_vbus_source](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaab85fda6d4030c83052deb1965d814f3)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否正向 VBUS 供电（Sourcing）。

<a id="r_gaf5e3999f3a016e33adf4797b62009d6d"></a>

```c
static int ppc_is_vbus_sink (const struct device *dev)
```

相关声明：[ppc_is_vbus_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaf5e3999f3a016e33adf4797b62009d6d)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否正从 VBUS 受电（Sinking）。

<a id="r_gae157ab53326686361309f20dfe5c4e64"></a>

```c
static int ppc_set_snk_ctrl (const struct device *dev, bool enable)
```

相关声明：[ppc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae157ab53326686361309f20dfe5c4e64)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 受电状态（Sinking State）。

<a id="r_gad38e1b5b5598c23ded44b343af58b791"></a>

```c
static int ppc_set_src_ctrl (const struct device *dev, bool enable)
```

相关声明：[ppc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gad38e1b5b5598c23ded44b343af58b791)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 供电状态（Sourcing State）。

<a id="r_gae66cb0377ffefabf85bc002a2fd04a47"></a>

```c
static int ppc_set_vbus_discharge (const struct device *dev, bool enable)
```

相关声明：[ppc_set_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae66cb0377ffefabf85bc002a2fd04a47)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 放电状态（Discharging State）。

<a id="r_gacd1ac1ac4ea60f16c58f57c9df11d536"></a>

```c
static int ppc_is_vbus_present (const struct device *dev)
```

相关声明：[ppc_is_vbus_present](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gacd1ac1ac4ea60f16c58f57c9df11d536)、[device](../device_reference/P002_设备对象结构.md)。

检查 VBUS 是否存在（Present）。

<a id="r_ga1d59cc94e8d303f0125fc88e5b447a69"></a>

```c
static int ppc_set_event_handler (const struct device *dev, usbc_ppc_event_cb_t handler, void *data)
```

相关声明：[ppc_set_event_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga1d59cc94e8d303f0125fc88e5b447a69)、[device](../device_reference/P002_设备对象结构.md)、[usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)。

设置用于通知 PPC 事件（Events）的回调。

<a id="r_gaeee650c29ce524b1e4d8ef66f295c1d7"></a>

```c
static int ppc_dump_regs (const struct device *dev)
```

相关声明：[ppc_dump_regs](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaeee650c29ce524b1e4d8ef66f295c1d7)、[device](../device_reference/P002_设备对象结构.md)。

打印 PPC 寄存器值（Register Values）。原文的 `or PPC registers` 按上下文理解为 `of PPC registers`。


## 45.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P238_usbc_ppc.h_源码浏览.md)
- [usbc_ppc_driver_api](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md)
- [usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)
- [device](../device_reference/P002_设备对象结构.md)
- [usbc_ppc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga3dbbb1a6701a3a79c9a1d148b239fcf9)
- [USBC_PPC_EVENT_DEAD_BATTERY_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e)
- [USBC_PPC_EVENT_SRC_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109)
- [USBC_PPC_EVENT_SRC_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6)
- [USBC_PPC_EVENT_SRC_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238)
- [USBC_PPC_EVENT_SRC_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4)
- [USBC_PPC_EVENT_OVER_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c)
- [USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94)
- [USBC_PPC_EVENT_SNK_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759)
- [USBC_PPC_EVENT_SNK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d)
- [USBC_PPC_EVENT_SNK_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)
- [ppc_is_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga5f70af9a0d0336c208ff4f7a90c4b665)
- [ppc_exit_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gabcbebdf47ca1c8a9b7c2e803bb833f5a)
- [ppc_is_vbus_source](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaab85fda6d4030c83052deb1965d814f3)
- [ppc_is_vbus_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaf5e3999f3a016e33adf4797b62009d6d)
- [ppc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae157ab53326686361309f20dfe5c4e64)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ppc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gad38e1b5b5598c23ded44b343af58b791)
- [ppc_set_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae66cb0377ffefabf85bc002a2fd04a47)
- [ppc_is_vbus_present](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gacd1ac1ac4ea60f16c58f57c9df11d536)
- [ppc_set_event_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga1d59cc94e8d303f0125fc88e5b447a69)
- [ppc_dump_regs](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaeee650c29ce524b1e4d8ef66f295c1d7)

<a id="header-details"></a>

---

[上一章](P044_zephyr__drivers__console__uart_mcumgr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztress.h_文件参考.md)
