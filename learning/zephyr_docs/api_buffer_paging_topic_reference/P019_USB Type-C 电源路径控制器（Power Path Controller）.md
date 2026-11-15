---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-19
title: USB Type-C 电源路径控制器（Power Path Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_USB Type-C 电源路径控制器（Power Path Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB Type-C 电源路径控制器（Power Path Controller）

<a id="details"></a>

USB Type-C 电源路径控制器（Power Path Controller）

<a id="header-groups"></a>
<a id="groups"></a>

## 19.1\_主题（Topics）

<a id="r_usb_5Ftype_5Fc_5Fpower_5Fpath_5Fcontroller_5Fbackend"></a>

相关声明：[USB Type-C 电源路径控制器驱动后端 API](../api_platform_topic_reference/P124_USB Type-C 电源路径控制器驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 19.2\_文件（Files）

<a id="r_usbc_5Fppc_2Eh"></a>

```c
file usbc_ppc.h
```

相关声明：[usbc_ppc.h](../api_file_system_power_reference/P045_zephyr__drivers__usb_c__usbc_ppc.h_文件参考.md)。

USB Type-C电源路径控制器（Power Path Controller）的设备API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 19.3\_类型定义（Typedefs）

<a id="r_ga8195a7a51eb5bd3cbcec985b97b84e73"></a>

```c
typedef void(* usbc_ppc_event_cb_t) (const struct device *dev, void *data, enum usbc_ppc_event ev)
```

相关声明：[usbc_ppc_event_cb_t](#ga8195a7a51eb5bd3cbcec985b97b84e73)、[device](../device_reference/P002_设备对象结构.md)、[usbc_ppc_event](#ga3dbbb1a6701a3a79c9a1d148b239fcf9)。

用于通知电源路径控制器（PPC）事件的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.4\_枚举（Enumerations）

<a id="r_ga3dbbb1a6701a3a79c9a1d148b239fcf9"></a>

```c
enum usbc_ppc_event { USBC_PPC_EVENT_DEAD_BATTERY_ERROR = 0 , USBC_PPC_EVENT_SRC_OVERVOLTAGE , USBC_PPC_EVENT_SRC_REVERSE_CURRENT , USBC_PPC_EVENT_SRC_OVERCURRENT , USBC_PPC_EVENT_SRC_SHORT , USBC_PPC_EVENT_OVER_TEMPERATURE , USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED , USBC_PPC_EVENT_SNK_REVERSE_CURRENT , USBC_PPC_EVENT_SNK_SHORT , USBC_PPC_EVENT_SNK_OVERVOLTAGE }
```

相关声明：[usbc_ppc_event](#ga3dbbb1a6701a3a79c9a1d148b239fcf9)、[USBC_PPC_EVENT_DEAD_BATTERY_ERROR](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e)、[USBC_PPC_EVENT_SRC_OVERVOLTAGE](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109)、[USBC_PPC_EVENT_SRC_REVERSE_CURRENT](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6)、[USBC_PPC_EVENT_SRC_OVERCURRENT](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238)、[USBC_PPC_EVENT_SRC_SHORT](#gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4)、[USBC_PPC_EVENT_OVER_TEMPERATURE](#gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c)、[USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED](#gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94)、[USBC_PPC_EVENT_SNK_REVERSE_CURRENT](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759)、[USBC_PPC_EVENT_SNK_SHORT](#gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d)、[USBC_PPC_EVENT_SNK_OVERVOLTAGE](#gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)。

电源路径控制器（Power Path Controller）通知的事件类型（Event Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.5\_函数（Functions）

<a id="r_ga5f70af9a0d0336c208ff4f7a90c4b665"></a>

```c
static int ppc_is_dead_battery_mode (const struct device *dev)
```

相关声明：[ppc_is_dead_battery_mode](#ga5f70af9a0d0336c208ff4f7a90c4b665)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否处于电池耗尽模式（Dead Battery Mode）。

<a id="r_gabcbebdf47ca1c8a9b7c2e803bb833f5a"></a>

```c
static int ppc_exit_dead_battery_mode (const struct device *dev)
```

相关声明：[ppc_exit_dead_battery_mode](#gabcbebdf47ca1c8a9b7c2e803bb833f5a)、[device](../device_reference/P002_设备对象结构.md)。

请求 PPC 退出电池耗尽模式（Dead Battery Mode）。本调用返回并不代表 PPC 已经退出该模式。

<a id="r_gaab85fda6d4030c83052deb1965d814f3"></a>

```c
static int ppc_is_vbus_source (const struct device *dev)
```

相关声明：[ppc_is_vbus_source](#gaab85fda6d4030c83052deb1965d814f3)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否正向 VBUS 供电（Sourcing）。

<a id="r_gaf5e3999f3a016e33adf4797b62009d6d"></a>

```c
static int ppc_is_vbus_sink (const struct device *dev)
```

相关声明：[ppc_is_vbus_sink](#gaf5e3999f3a016e33adf4797b62009d6d)、[device](../device_reference/P002_设备对象结构.md)。

检查 PPC 是否正从 VBUS 受电（Sinking）。

<a id="r_gae157ab53326686361309f20dfe5c4e64"></a>

```c
static int ppc_set_snk_ctrl (const struct device *dev, bool enable)
```

相关声明：[ppc_set_snk_ctrl](#gae157ab53326686361309f20dfe5c4e64)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 受电状态（Sinking State）。

<a id="r_gad38e1b5b5598c23ded44b343af58b791"></a>

```c
static int ppc_set_src_ctrl (const struct device *dev, bool enable)
```

相关声明：[ppc_set_src_ctrl](#gad38e1b5b5598c23ded44b343af58b791)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 供电状态（Sourcing State）。

<a id="r_gae66cb0377ffefabf85bc002a2fd04a47"></a>

```c
static int ppc_set_vbus_discharge (const struct device *dev, bool enable)
```

相关声明：[ppc_set_vbus_discharge](#gae66cb0377ffefabf85bc002a2fd04a47)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 VBUS 放电状态（Discharging State）。

<a id="r_gacd1ac1ac4ea60f16c58f57c9df11d536"></a>

```c
static int ppc_is_vbus_present (const struct device *dev)
```

相关声明：[ppc_is_vbus_present](#gacd1ac1ac4ea60f16c58f57c9df11d536)、[device](../device_reference/P002_设备对象结构.md)。

检查 VBUS 是否存在（Present）。

<a id="r_ga1d59cc94e8d303f0125fc88e5b447a69"></a>

```c
static int ppc_set_event_handler (const struct device *dev, usbc_ppc_event_cb_t handler, void *data)
```

相关声明：[ppc_set_event_handler](#ga1d59cc94e8d303f0125fc88e5b447a69)、[device](../device_reference/P002_设备对象结构.md)、[usbc_ppc_event_cb_t](#ga8195a7a51eb5bd3cbcec985b97b84e73)。

设置用于通知 PPC 事件（Events）的回调。

<a id="r_gaeee650c29ce524b1e4d8ef66f295c1d7"></a>

```c
static int ppc_dump_regs (const struct device *dev)
```

相关声明：[ppc_dump_regs](#gaeee650c29ce524b1e4d8ef66f295c1d7)、[device](../device_reference/P002_设备对象结构.md)。

打印 PPC 寄存器值（Register Values）。原文的 `or PPC registers` 按上下文理解为 `of PPC registers`。

## 19.6\_详细说明（Detailed Documentation）

<a id="ga8195a7a51eb5bd3cbcec985b97b84e73"></a>

### `usbc_ppc_event_cb_t`

```c
typedef void(* usbc_ppc_event_cb_t) (const struct device *dev, void *data, enum usbc_ppc_event ev)
```

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

用于通知电源路径控制器（PPC）事件的回调。

通过 ppc_set_event_handler() 注册。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |
| `data` | 传给 ppc_set_event_handler() 的用户数据（User Data） |
| `ev` | 正在通知的事件（Event） |

<a id="ga3dbbb1a6701a3a79c9a1d148b239fcf9"></a>

### `usbc_ppc_event`

```c
enum usbc_ppc_event
```

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

电源路径控制器（Power Path Controller）通知的事件类型（Event Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USBC_PPC_EVENT_DEAD_BATTERY_ERROR` | 退出电池耗尽模式（Dead-battery Mode）失败。 |
| `USBC_PPC_EVENT_SRC_OVERVOLTAGE` | 处于供电方角色（Source Role）时检测到过压（Overvoltage）。 |
| `USBC_PPC_EVENT_SRC_REVERSE_CURRENT` | 处于供电方角色（Source Role）时检测到反向电流（Reverse Current）。 |
| `USBC_PPC_EVENT_SRC_OVERCURRENT` | 处于供电方角色（Source Role）时检测到过流（Overcurrent）。 |
| `USBC_PPC_EVENT_SRC_SHORT` | 处于供电方角色（Source Role）时检测到 VBUS 短路（Short）。 |
| `USBC_PPC_EVENT_OVER_TEMPERATURE` | 检测到芯片过温（Over Temperature）。 |
| `USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED` | 受电路径与供电路径（Sink and Source Paths）同时启用。 |
| `USBC_PPC_EVENT_SNK_REVERSE_CURRENT` | 处于受电方角色（Sink Role）时检测到反向电流（Reverse Current）。 |
| `USBC_PPC_EVENT_SNK_SHORT` | 处于受电方角色（Sink Role）时检测到 VBUS 短路（Short）。 |
| `USBC_PPC_EVENT_SNK_OVERVOLTAGE` | 处于受电方角色（Sink Role）时检测到过压（Overvoltage）。 |

<a id="gaeee650c29ce524b1e4d8ef66f295c1d7"></a>

### `ppc_dump_regs()`

```c
int ppc_dump_regs ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

打印 PPC 寄存器值（Register Values）。原文的 `or PPC registers` 按上下文理解为 `of PPC registers`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gabcbebdf47ca1c8a9b7c2e803bb833f5a"></a>

### `ppc_exit_dead_battery_mode()`

```c
int ppc_exit_dead_battery_mode ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

请求 PPC 退出电池耗尽模式（Dead Battery Mode）。本调用返回并不代表 PPC 已经退出该模式。

发生错误时，驱动应以 USBC_PPC_EVENT_DEAD_BATTERY_ERROR 枚举值执行回调。应调用 ppc_is_dead_battery_mode 检查 PPC 是否已禁用电池耗尽模式（Dead Battery Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功发送请求时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="ga5f70af9a0d0336c208ff4f7a90c4b665"></a>

### `ppc_is_dead_battery_mode()`

```c
int ppc_is_dead_battery_mode ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

检查 PPC 是否处于电池耗尽模式（Dead Battery Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | PPC 处于电池耗尽模式（Dead Battery Mode）时。 |
| `0` | PPC 不处于电池耗尽模式（Dead Battery Mode）时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gacd1ac1ac4ea60f16c58f57c9df11d536"></a>

### `ppc_is_vbus_present()`

```c
int ppc_is_vbus_present ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

检查 VBUS 是否存在（Present）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 存在 VBUS 电压时。 |
| `0` | 未检测到 VBUS 电压时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gaf5e3999f3a016e33adf4797b62009d6d"></a>

### `ppc_is_vbus_sink()`

```c
int ppc_is_vbus_sink ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

检查 PPC 是否正从 VBUS 受电（Sinking）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | PPC 正从 VBUS 受电（Sinking）时。 |
| `0` | PPC 未从 VBUS 受电（Sinking）时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gaab85fda6d4030c83052deb1965d814f3"></a>

### `ppc_is_vbus_source()`

```c
int ppc_is_vbus_source ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

检查 PPC 是否正向 VBUS 供电（Sourcing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | PPC 正向 VBUS 供电（Sourcing）时。 |
| `0` | PPC 未向 VBUS 供电（Sourcing）时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="ga1d59cc94e8d303f0125fc88e5b447a69"></a>

### `ppc_set_event_handler()`

```c
int ppc_set_event_handler ( const struct device * dev, usbc_ppc_event_cb_t handler, void * data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

设置用于通知 PPC 事件（Events）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |
| `handler` | 收到事件通知时调用的处理函数（Handler） |
| `data` | 用作回调参数的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gae157ab53326686361309f20dfe5c4e64"></a>

### `ppc_set_snk_ctrl()`

```c
int ppc_set_snk_ctrl ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

设置 VBUS 受电状态（Sinking State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |
| `enable` | true 表示应启用从 VBUS 受电（Sinking），false 表示应禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gad38e1b5b5598c23ded44b343af58b791"></a>

### `ppc_set_src_ctrl()`

```c
int ppc_set_src_ctrl ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

设置 VBUS 供电状态（Sourcing State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |
| `enable` | true 表示应启用向 VBUS 供电（Sourcing），false 表示应禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |

<a id="gae66cb0377ffefabf85bc002a2fd04a47"></a>

### `ppc_set_vbus_discharge()`

```c
int ppc_set_vbus_discharge ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_ppc.h>
```

设置 VBUS 放电状态（Discharging State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PPC 设备结构体（Device Structure） |
| `enable` | true 表示应启用 VBUS 放电（Discharging），false 表示应禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | I2C 通信失败时。 |
| `-ENOSYS` | 驱动不支持此函数时。 |


## 19.7\_原页交叉引用（Cross References）

- [USB Type-C 电源路径控制器驱动后端 API](../api_platform_topic_reference/P124_USB Type-C 电源路径控制器驱动后端 API.md)
- [usbc_ppc.h](../api_file_system_power_reference/P045_zephyr__drivers__usb_c__usbc_ppc.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d"></a>
<a id="gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_实用工具（Utilities）.md) · [返回大纲](大纲.md) · [下一章](P020_VEML6031 API主题.md)
