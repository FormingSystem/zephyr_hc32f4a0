---
id: learning.zephyr-docs.driver-trace-reference.page-2
title: GPIO跟踪接口
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__gpio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GPIO跟踪接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__gpio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO、GPIO、电源管理与工作项的跟踪接口，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

GPIO事件的跟踪钩子（Tracing Hooks）。

<a id="details"></a>

GPIO事件的跟踪钩子（Tracing Hooks）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga136247e36d2f518d15bf332d8ba5d035"></a>

```c
#define sys_port_trace_gpio_pin_interrupt_configure_enter(port, pin, flags)
```

相关声明：[sys_port_trace_gpio_pin_interrupt_configure_enter](#ga136247e36d2f518d15bf332d8ba5d035)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

跟踪GPIO引脚中断配置调用的入口。

<a id="r_ga78b6201756dc8889aed4dbe2f5e5df08"></a>

```c
#define sys_port_trace_gpio_pin_interrupt_configure_exit(port, pin, ret)
```

相关声明：[sys_port_trace_gpio_pin_interrupt_configure_exit](#ga78b6201756dc8889aed4dbe2f5e5df08)。

跟踪GPIO引脚中断配置调用的出口。

<a id="r_ga9975f3c53f4cfa2fb4b699691811289d"></a>

```c
#define sys_port_trace_gpio_pin_configure_enter(port, pin, flags)
```

相关声明：[sys_port_trace_gpio_pin_configure_enter](#ga9975f3c53f4cfa2fb4b699691811289d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

跟踪GPIO单个引脚配置调用的入口。

<a id="r_gad116e0fee008064fa859fcb660735420"></a>

```c
#define sys_port_trace_gpio_pin_configure_exit(port, pin, ret)
```

相关声明：[sys_port_trace_gpio_pin_configure_exit](#gad116e0fee008064fa859fcb660735420)。

跟踪GPIO单个引脚配置调用的出口。

<a id="r_ga20672a060ed09777729bc417eb4ac726"></a>

```c
#define sys_port_trace_gpio_port_get_direction_enter(port, map, inputs, outputs)
```

相关声明：[sys_port_trace_gpio_port_get_direction_enter](#ga20672a060ed09777729bc417eb4ac726)。

跟踪GPIO端口方向获取调用的入口。

<a id="r_gade6194699050e060dc48fa0de50fc930"></a>

```c
#define sys_port_trace_gpio_port_get_direction_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_get_direction_exit](#gade6194699050e060dc48fa0de50fc930)。

跟踪GPIO端口方向获取调用的出口。

<a id="r_gac5592dce31daf0c8cfcfa09db50fc9e4"></a>

```c
#define sys_port_trace_gpio_pin_get_config_enter(port, pin, flags)
```

相关声明：[sys_port_trace_gpio_pin_get_config_enter](#gac5592dce31daf0c8cfcfa09db50fc9e4)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

跟踪GPIO引脚配置获取调用的入口。

<a id="r_ga92ada0c9043f9b00803e33c5537abe05"></a>

```c
#define sys_port_trace_gpio_pin_get_config_exit(port, pin, ret)
```

相关声明：[sys_port_trace_gpio_pin_get_config_exit](#ga92ada0c9043f9b00803e33c5537abe05)。

跟踪GPIO引脚配置获取调用的出口。

<a id="r_gabeea324bb6ee389a6f4f739918e43328"></a>

```c
#define sys_port_trace_gpio_port_get_raw_enter(port, value)
```

相关声明：[sys_port_trace_gpio_port_get_raw_enter](#gabeea324bb6ee389a6f4f739918e43328)。

跟踪GPIO端口原始值获取（Get Raw）调用的入口。

<a id="r_ga1cbebfa0804f10c410622bb17c02bdb5"></a>

```c
#define sys_port_trace_gpio_port_get_raw_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_get_raw_exit](#ga1cbebfa0804f10c410622bb17c02bdb5)。

跟踪GPIO端口原始值获取（Get Raw）调用的出口。

<a id="r_ga6ddcc9a973b2c938fa67ba9d9de90b43"></a>

```c
#define sys_port_trace_gpio_port_set_masked_raw_enter(port, mask, value)
```

相关声明：[sys_port_trace_gpio_port_set_masked_raw_enter](#ga6ddcc9a973b2c938fa67ba9d9de90b43)。

跟踪GPIO端口按掩码设置原始值（Set Masked Raw）调用的入口。

<a id="r_gacc4328675df61fc4d6aea6406328fec6"></a>

```c
#define sys_port_trace_gpio_port_set_masked_raw_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_set_masked_raw_exit](#gacc4328675df61fc4d6aea6406328fec6)。

跟踪GPIO端口按掩码设置原始值（Set Masked Raw）调用的出口。

<a id="r_gae312b54e7983e48519e60be101d2f6cb"></a>

```c
#define sys_port_trace_gpio_port_set_bits_raw_enter(port, pins)
```

相关声明：[sys_port_trace_gpio_port_set_bits_raw_enter](#gae312b54e7983e48519e60be101d2f6cb)。

跟踪GPIO端口原始位设置（Set Bits Raw）调用的入口。

<a id="r_ga273a91c09bb777d3f436eab91ae69969"></a>

```c
#define sys_port_trace_gpio_port_set_bits_raw_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_set_bits_raw_exit](#ga273a91c09bb777d3f436eab91ae69969)。

跟踪GPIO端口原始位设置（Set Bits Raw）调用的出口。

<a id="r_ga8873f6d6af038b43a9f37c0912775608"></a>

```c
#define sys_port_trace_gpio_port_clear_bits_raw_enter(port, pins)
```

相关声明：[sys_port_trace_gpio_port_clear_bits_raw_enter](#ga8873f6d6af038b43a9f37c0912775608)。

跟踪GPIO端口原始位清除（Clear Bits Raw）调用的入口。

<a id="r_ga4a4b88d5a585c0f772dbc8892b801efd"></a>

```c
#define sys_port_trace_gpio_port_clear_bits_raw_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_clear_bits_raw_exit](#ga4a4b88d5a585c0f772dbc8892b801efd)。

跟踪GPIO端口原始位清除（Clear Bits Raw）调用的出口。

<a id="r_gaf5d4ac1b95410aa6ba7e543868e59928"></a>

```c
#define sys_port_trace_gpio_port_toggle_bits_enter(port, pins)
```

相关声明：[sys_port_trace_gpio_port_toggle_bits_enter](#gaf5d4ac1b95410aa6ba7e543868e59928)。

跟踪GPIO端口位翻转（Toggle Bits）调用的入口。

<a id="r_ga70f76ddf530aafa81488ca30d6ea4fb7"></a>

```c
#define sys_port_trace_gpio_port_toggle_bits_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_port_toggle_bits_exit](#ga70f76ddf530aafa81488ca30d6ea4fb7)。

跟踪GPIO端口位翻转（Toggle Bits）调用的出口。

<a id="r_ga3c173c0b612671a9f44fd54efd288ac2"></a>

```c
#define sys_port_trace_gpio_init_callback_enter(callback, handler, pin_mask)
```

相关声明：[sys_port_trace_gpio_init_callback_enter](#ga3c173c0b612671a9f44fd54efd288ac2)。

跟踪GPIO回调初始化调用的入口。

<a id="r_ga4c130cd12803687e6b8dde1d82aa1d37"></a>

```c
#define sys_port_trace_gpio_init_callback_exit(callback)
```

相关声明：[sys_port_trace_gpio_init_callback_exit](#ga4c130cd12803687e6b8dde1d82aa1d37)。

跟踪GPIO回调初始化调用的出口。

<a id="r_ga70cacc72e4696340ed8d53578a13a325"></a>

```c
#define sys_port_trace_gpio_add_callback_enter(port, callback)
```

相关声明：[sys_port_trace_gpio_add_callback_enter](#ga70cacc72e4696340ed8d53578a13a325)。

跟踪GPIO添加回调调用的入口。

<a id="r_gaadca093d8a88c53f7f23ef80300b455a"></a>

```c
#define sys_port_trace_gpio_add_callback_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_add_callback_exit](#gaadca093d8a88c53f7f23ef80300b455a)。

跟踪GPIO添加回调调用的出口。

<a id="r_ga2a756f3d1c60c51708492cbb08c9c3b3"></a>

```c
#define sys_port_trace_gpio_remove_callback_enter(port, callback)
```

相关声明：[sys_port_trace_gpio_remove_callback_enter](#ga2a756f3d1c60c51708492cbb08c9c3b3)。

跟踪GPIO移除回调调用的入口。

<a id="r_gaa7cb1d5a8b2205e610df66ee51dee39b"></a>

```c
#define sys_port_trace_gpio_remove_callback_exit(port, ret)
```

相关声明：[sys_port_trace_gpio_remove_callback_exit](#gaa7cb1d5a8b2205e610df66ee51dee39b)。

跟踪GPIO移除回调调用的出口。

<a id="r_ga29d20db6e85ac27181b697eeff1a405c"></a>

```c
#define sys_port_trace_gpio_get_pending_int_enter(dev)
```

相关声明：[sys_port_trace_gpio_get_pending_int_enter](#ga29d20db6e85ac27181b697eeff1a405c)。

跟踪GPIO待处理中断获取调用的入口。

<a id="r_ga118077a21a3037e353fa9ff4ba404be6"></a>

```c
#define sys_port_trace_gpio_get_pending_int_exit(dev, ret)
```

相关声明：[sys_port_trace_gpio_get_pending_int_exit](#ga118077a21a3037e353fa9ff4ba404be6)。

跟踪GPIO待处理中断获取调用的出口。

<a id="r_ga9cf081771e5f4724b02de3a89eec339c"></a>

```c
#define sys_port_trace_gpio_fire_callbacks_enter(list, port, pins)
```

相关声明：[sys_port_trace_gpio_fire_callbacks_enter](#ga9cf081771e5f4724b02de3a89eec339c)。

<a id="r_gaed3026e592853a9a97c0900a0687974b"></a>

```c
#define sys_port_trace_gpio_fire_callback(port, callback)
```

相关声明：[sys_port_trace_gpio_fire_callback](#gaed3026e592853a9a97c0900a0687974b)。

## 2.2\_详细说明（Detailed Documentation）

<a id="ga70cacc72e4696340ed8d53578a13a325"></a>

### `sys_port_trace_gpio_add_callback_enter`

```c
#define sys_port_trace_gpio_add_callback_enter ( port, callback )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO添加回调调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `callback` | 有效的应用回调结构体指针。 |

<a id="gaadca093d8a88c53f7f23ef80300b455a"></a>

### `sys_port_trace_gpio_add_callback_exit`

```c
#define sys_port_trace_gpio_add_callback_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO添加回调调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="gaed3026e592853a9a97c0900a0687974b"></a>

### `sys_port_trace_gpio_fire_callback`

```c
#define sys_port_trace_gpio_fire_callback ( port, callback )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 表示GPIO端口的设备。 |
| `callback` | `gpio_callback`：有效的应用回调结构体指针。 |

<a id="ga9cf081771e5f4724b02de3a89eec339c"></a>

### `sys_port_trace_gpio_fire_callbacks_enter`

```c
#define sys_port_trace_gpio_fire_callbacks_enter ( list, port, pins )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `list` | `sys_slist_t`：表示`gpio_callback`指针列表。 |
| `port` | 表示GPIO端口的设备。 |
| `pins` | `gpio_pin_t`：表示引脚。 |

<a id="ga29d20db6e85ac27181b697eeff1a405c"></a>

### `sys_port_trace_gpio_get_pending_int_enter`

```c
#define sys_port_trace_gpio_get_pending_int_enter ( dev)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO待处理中断获取调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备实例的设备结构体的指针。 |

<a id="ga118077a21a3037e353fa9ff4ba404be6"></a>

### `sys_port_trace_gpio_get_pending_int_exit`

```c
#define sys_port_trace_gpio_get_pending_int_exit ( dev, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO待处理中断获取调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备实例的设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga3c173c0b612671a9f44fd54efd288ac2"></a>

### `sys_port_trace_gpio_init_callback_enter`

```c
#define sys_port_trace_gpio_init_callback_enter ( callback, handler, pin_mask )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO回调初始化调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `pin_mask` | 表示处理函数相关引脚的位掩码（Bit Mask）。 |

<a id="ga4c130cd12803687e6b8dde1d82aa1d37"></a>

### `sys_port_trace_gpio_init_callback_exit`

```c
#define sys_port_trace_gpio_init_callback_exit ( callback)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO回调初始化调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针。 |

<a id="ga9975f3c53f4cfa2fb4b699691811289d"></a>

### `sys_port_trace_gpio_pin_configure_enter`

```c
#define sys_port_trace_gpio_pin_configure_enter ( port, pin, flags )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO单个引脚配置调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | 要配置的GPIO引脚编号。 |
| `flags` | GPIO引脚配置标志（Configuration Flags）。 |

<a id="gad116e0fee008064fa859fcb660735420"></a>

### `sys_port_trace_gpio_pin_configure_exit`

```c
#define sys_port_trace_gpio_pin_configure_exit ( port, pin, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO单个引脚配置调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | 要配置的GPIO引脚编号。 |
| `ret` | 返回值（Return Value）。 |

<a id="gac5592dce31daf0c8cfcfa09db50fc9e4"></a>

### `sys_port_trace_gpio_pin_get_config_enter`

```c
#define sys_port_trace_gpio_pin_get_config_enter ( port, pin, flags )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO引脚配置获取调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | 要配置的GPIO引脚编号。 |
| `flags` | GPIO引脚配置标志（Configuration Flags）。 |

<a id="ga92ada0c9043f9b00803e33c5537abe05"></a>

### `sys_port_trace_gpio_pin_get_config_exit`

```c
#define sys_port_trace_gpio_pin_get_config_exit ( port, pin, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO引脚配置获取调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | 要配置的GPIO引脚编号。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga136247e36d2f518d15bf332d8ba5d035"></a>

### `sys_port_trace_gpio_pin_interrupt_configure_enter`

```c
#define sys_port_trace_gpio_pin_interrupt_configure_enter ( port, pin, flags )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO引脚中断配置调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | GPIO引脚编号。 |
| `flags` | 由`GPIO_INT_*`定义的中断配置标志。 |

<a id="ga78b6201756dc8889aed4dbe2f5e5df08"></a>

### `sys_port_trace_gpio_pin_interrupt_configure_exit`

```c
#define sys_port_trace_gpio_pin_interrupt_configure_exit ( port, pin, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO引脚中断配置调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pin` | GPIO引脚编号。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga8873f6d6af038b43a9f37c0912775608"></a>

### `sys_port_trace_gpio_port_clear_bits_raw_enter`

```c
#define sys_port_trace_gpio_port_clear_bits_raw_enter ( port, pins )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始位清除（Clear Bits Raw）调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pins` | 表示将修改哪些引脚的值。 |

<a id="ga4a4b88d5a585c0f772dbc8892b801efd"></a>

### `sys_port_trace_gpio_port_clear_bits_raw_exit`

```c
#define sys_port_trace_gpio_port_clear_bits_raw_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始位清除（Clear Bits Raw）调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga20672a060ed09777729bc417eb4ac726"></a>

### `sys_port_trace_gpio_port_get_direction_enter`

```c
#define sys_port_trace_gpio_port_get_direction_enter ( port, map, inputs, outputs )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口方向获取调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `map` | 要查询方向的引脚位图（Bitmap）。 |
| `inputs` | 指向用于存储输入方向的变量的指针。 |
| `outputs` | 指向用于存储输出方向的变量的指针。 |

<a id="gade6194699050e060dc48fa0de50fc930"></a>

### `sys_port_trace_gpio_port_get_direction_exit`

```c
#define sys_port_trace_gpio_port_get_direction_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口方向获取调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="gabeea324bb6ee389a6f4f739918e43328"></a>

### `sys_port_trace_gpio_port_get_raw_enter`

```c
#define sys_port_trace_gpio_port_get_raw_enter ( port, value )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始值获取（Get Raw）调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `value` | 指向用于存储原始值（Raw Value）的变量的指针。 |

<a id="ga1cbebfa0804f10c410622bb17c02bdb5"></a>

### `sys_port_trace_gpio_port_get_raw_exit`

```c
#define sys_port_trace_gpio_port_get_raw_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始值获取（Get Raw）调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="gae312b54e7983e48519e60be101d2f6cb"></a>

### `sys_port_trace_gpio_port_set_bits_raw_enter`

```c
#define sys_port_trace_gpio_port_set_bits_raw_enter ( port, pins )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始位设置（Set Bits Raw）调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pins` | 表示将修改哪些引脚的值。 |

<a id="ga273a91c09bb777d3f436eab91ae69969"></a>

### `sys_port_trace_gpio_port_set_bits_raw_exit`

```c
#define sys_port_trace_gpio_port_set_bits_raw_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口原始位设置（Set Bits Raw）调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga6ddcc9a973b2c938fa67ba9d9de90b43"></a>

### `sys_port_trace_gpio_port_set_masked_raw_enter`

```c
#define sys_port_trace_gpio_port_set_masked_raw_enter ( port, mask, value )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口按掩码设置原始值（Set Masked Raw）调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `mask` | 表示将修改哪些引脚的掩码。 |
| `value` | 要写入输出引脚的值。 |

<a id="gacc4328675df61fc4d6aea6406328fec6"></a>

### `sys_port_trace_gpio_port_set_masked_raw_exit`

```c
#define sys_port_trace_gpio_port_set_masked_raw_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口按掩码设置原始值（Set Masked Raw）调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="gaf5d4ac1b95410aa6ba7e543868e59928"></a>

### `sys_port_trace_gpio_port_toggle_bits_enter`

```c
#define sys_port_trace_gpio_port_toggle_bits_enter ( port, pins )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口位翻转（Toggle Bits）调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `pins` | 表示将修改哪些引脚的值。 |

<a id="ga70f76ddf530aafa81488ca30d6ea4fb7"></a>

### `sys_port_trace_gpio_port_toggle_bits_exit`

```c
#define sys_port_trace_gpio_port_toggle_bits_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO端口位翻转（Toggle Bits）调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

<a id="ga2a756f3d1c60c51708492cbb08c9c3b3"></a>

### `sys_port_trace_gpio_remove_callback_enter`

```c
#define sys_port_trace_gpio_remove_callback_enter ( port, callback )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO移除回调调用的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `callback` | 有效的应用回调结构体指针。 |

<a id="gaa7cb1d5a8b2205e610df66ee51dee39b"></a>

### `sys_port_trace_gpio_remove_callback_exit`

```c
#define sys_port_trace_gpio_remove_callback_exit ( port, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪GPIO移除回调调用的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向驱动实例设备结构体的指针。 |
| `ret` | 返回值（Return Value）。 |

## 2.3\_源码定位与版本边界

相对源码定位：[跟踪入口](../../../include/zephyr/tracing/tracing.h)、[钩子声明](../../../include/zephyr/tracing/tracing_hooks.h)、[包装宏](../../../include/zephyr/tracing/tracing_macros.h)、[跟踪配置](../../../subsys/tracing/Kconfig)、[RTIO核心](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)、[GPIO接口](../../../include/zephyr/drivers/gpio.h)、[GPIO回调分派](../../../include/zephyr/drivers/gpio/gpio_utils.h)、[工作队列](../../../kernel/work.c)、[轮询工作](../../../kernel/poll.c)、[设备运行时电源管理](../../../subsys/pm/device_runtime.c)及[系统电源管理](../../../subsys/pm/pm.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：本页是跟踪钩子（Tracing Hooks）的接口约定，不是替代原功能API的操作入口。tracing_hooks.h为尚未由后端定义的钩子提供空宏，并用#ifndef保留后端已有定义。仅有宏声明或开启功能模块，不等于已经生成可导出的事件数据；具体记录由所选跟踪格式与后端实现。

> 译注——源码核对：跟踪包装宏在原调用位置执行，不自动转到独立工作线程。CONFIG_TRACING关闭时，SYS_PORT_TRACING系列编译为空操作；对象类钩子还受相应类型开关控制。钩子可能位于中断、锁保护或调度敏感路径，后端实现应遵守实际调用上下文，不能把宏参数求值当作业务必需的副作用。

> 译注——源码核对：Enter、Blocking、Exit分别表示调用入口、某处阻塞标记与调用出口；它们不天然组成每条路径都一一配对的记录，也不自动表示外设完成或回调已执行。返回值按所属API解释，不能把所有ret都当成同一种errno或成功布尔值。

> 译注——源码核对：raw端口操作记录物理位值，不自动转换成逻辑有效电平。pin是引脚编号，pins、map、mask通常表示位图或掩码，不能互换；get_raw入口参数value是输出变量指针，应按对应操作的时序解读，不能在入口就把指针所指内容当作新读值。

> 译注——源码核对：原文pin_get_config_enter摘要把get拼作gent，译文按声明译为获取配置。本次gpio.h在入口钩子传入的是*flags当时的值，随后才执行查询，所以该事件中的flags不能当成成功返回后的配置；出口宏仅带port、pin、ret。

> 译注——源码核对：gpio_fire_callbacks_enter在遍历回调链表前执行；每个匹配回调的gpio_fire_callback位于应用handler返回之后。后者没有独立的enter／exit配对，也没有直接传入触发引脚掩码。原参数说明把pins写为gpio_pin_t，本次gpio_utils.h调用点实际传入uint32_t引脚掩码，不能当作单一引脚序号。

> 译注——源码核对：GPIO辅助函数直接调用sys_port_trace_gpio_*钩子，驱动API中的许多位置则通过SYS_PORT_TRACING包装。是否输出记录仍取决于实际后端定义；不能仅检查一种包装宏，就认为已经覆盖所有GPIO跟踪点。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界，本仓库同名文件通过相对链接定位；未配置跟踪硬件、运行采集或验证事件时序。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/tracing/tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_RTIO跟踪接口.md) · [返回大纲](大纲.md) · [下一章](P003_设备运行时电源管理跟踪.md)
