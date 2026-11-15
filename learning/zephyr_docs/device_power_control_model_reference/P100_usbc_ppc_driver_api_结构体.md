---
id: learning.zephyr-docs.device-power-control-model-reference.page-100
title: usbc_ppc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbc__ppc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_usbc\_ppc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbc__ppc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：USB Type-C电源路径控制器（Power Path Controller）驱动操作。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：USB Type-C 电源路径控制器（Power Path Controller，PPC）驱动操作。这是每个 USB Type-C 电源路径控制器驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_a832320573b2adab1d748e5e761690733"></a>

```c
int(* is_dead_battery_mode )(const struct device *dev)
```

相关声明：[is_dead_battery_mode](#a832320573b2adab1d748e5e761690733)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：检查 PPC 是否处于电池耗尽模式（Dead battery mode）。

<a id="r_a4ba2f654765130d5562f56243967bf58"></a>

```c
int(* exit_dead_battery_mode )(const struct device *dev)
```

相关声明：[exit_dead_battery_mode](#a4ba2f654765130d5562f56243967bf58)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：请求 PPC 退出电池耗尽模式。此调用返回并不表示 PPC 已经退出该模式。

<a id="r_aab74a38a9c055efdfd0198143f12c9ff"></a>

```c
int(* is_vbus_source )(const struct device *dev)
```

相关声明：[is_vbus_source](#aab74a38a9c055efdfd0198143f12c9ff)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：检查 PPC 是否通过 VBUS 供电。

<a id="r_a93b91d21d4d2edda1d457f4144800f37"></a>

```c
int(* is_vbus_sink )(const struct device *dev)
```

相关声明：[is_vbus_sink](#a93b91d21d4d2edda1d457f4144800f37)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：检查 PPC 是否通过 VBUS 受电。

<a id="r_af4a66a11b66d48818123434c59553f0d"></a>

```c
int(* set_snk_ctrl )(const struct device *dev, bool enable)
```

相关声明：[set_snk_ctrl](#af4a66a11b66d48818123434c59553f0d)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

`OPT`：设置 VBUS 受电状态。

<a id="r_a20ddefaee68808414f4075cc513a8660"></a>

```c
int(* set_src_ctrl )(const struct device *dev, bool enable)
```

相关声明：[set_src_ctrl](#a20ddefaee68808414f4075cc513a8660)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

`OPT`：设置 VBUS 供电状态。

<a id="r_a1c2c21070ee18b7b5df09a6b6ed618b6"></a>

```c
int(* set_vbus_discharge )(const struct device *dev, bool enable)
```

相关声明：[set_vbus_discharge](#a1c2c21070ee18b7b5df09a6b6ed618b6)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

`OPT`：设置 VBUS 放电（Discharging）状态。

<a id="r_a8bf73dee9ba920f1b426038f62d5c9db"></a>

```c
int(* is_vbus_present )(const struct device *dev)
```

相关声明：[is_vbus_present](#a8bf73dee9ba920f1b426038f62d5c9db)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：检查 VBUS 是否存在。

<a id="r_a8f82ae3af5452d9cd0852bf15fcab573"></a>

```c
int(* set_event_handler )(const struct device *dev, usbc_ppc_event_cb_t handler, void *data)
```

相关声明：[set_event_handler](#a8f82ae3af5452d9cd0852bf15fcab573)、[device](../device_reference/P002_设备对象结构.md)、[usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)。

`OPT`：设置用于通知 PPC 事件的回调。

<a id="r_adce51ae345d5fc417f3767476af36276"></a>

```c
int(* dump_regs )(const struct device *dev)
```

相关声明：[dump_regs](#adce51ae345d5fc417f3767476af36276)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：打印 PPC 寄存器的值。译注：原文 `or PPC registers` 按上下文理解为 `of PPC registers`。

## 100.2\_详细说明（Detailed Documentation）

<a id="adce51ae345d5fc417f3767476af36276"></a>

### `dump_regs`

```c
int(* usbc_ppc_driver_api::dump_regs) (const struct device *dev)
```

`OPT`：打印 PPC 寄存器的值。译注：原文 `or PPC registers` 按上下文理解为 `of PPC registers`。

<a id="a4ba2f654765130d5562f56243967bf58"></a>

### `exit_dead_battery_mode`

```c
int(* usbc_ppc_driver_api::exit_dead_battery_mode) (const struct device *dev)
```

`OPT`：请求 PPC 退出电池耗尽模式。此调用返回并不表示 PPC 已经退出该模式。

<a id="a832320573b2adab1d748e5e761690733"></a>

### `is_dead_battery_mode`

```c
int(* usbc_ppc_driver_api::is_dead_battery_mode) (const struct device *dev)
```

`OPT`：检查 PPC 是否处于电池耗尽模式（Dead battery mode）。

<a id="a8bf73dee9ba920f1b426038f62d5c9db"></a>

### `is_vbus_present`

```c
int(* usbc_ppc_driver_api::is_vbus_present) (const struct device *dev)
```

`OPT`：检查 VBUS 是否存在。

<a id="a93b91d21d4d2edda1d457f4144800f37"></a>

### `is_vbus_sink`

```c
int(* usbc_ppc_driver_api::is_vbus_sink) (const struct device *dev)
```

`OPT`：检查 PPC 是否通过 VBUS 受电。

<a id="aab74a38a9c055efdfd0198143f12c9ff"></a>

### `is_vbus_source`

```c
int(* usbc_ppc_driver_api::is_vbus_source) (const struct device *dev)
```

`OPT`：检查 PPC 是否通过 VBUS 供电。

<a id="a8f82ae3af5452d9cd0852bf15fcab573"></a>

### `set_event_handler`

```c
int(* usbc_ppc_driver_api::set_event_handler) (const struct device *dev, usbc_ppc_event_cb_t handler, void *data)
```

`OPT`：设置用于通知 PPC 事件的回调。

<a id="af4a66a11b66d48818123434c59553f0d"></a>

### `set_snk_ctrl`

```c
int(* usbc_ppc_driver_api::set_snk_ctrl) (const struct device *dev, bool enable)
```

`OPT`：设置 VBUS 受电状态。

<a id="a20ddefaee68808414f4075cc513a8660"></a>

### `set_src_ctrl`

```c
int(* usbc_ppc_driver_api::set_src_ctrl) (const struct device *dev, bool enable)
```

`OPT`：设置 VBUS 供电状态。

<a id="a1c2c21070ee18b7b5df09a6b6ed618b6"></a>

### `set_vbus_discharge`

```c
int(* usbc_ppc_driver_api::set_vbus_discharge) (const struct device *dev, bool enable)
```

`OPT`：设置 VBUS 放电（Discharging）状态。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_ppc.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_ppc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_usb_hub_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_usbc_vbus_driver_api_结构体.md)
