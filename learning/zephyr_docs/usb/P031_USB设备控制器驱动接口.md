---
id: learning.zephyr-docs.usb.api-31
title: USB设备控制器驱动接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_USB设备控制器驱动接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 31.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

UDC 驱动 API。任何 USB 设备控制器驱动都必须提供这些 API，但 device_speed() 和 test_mode() 仅对高速（HS）控制器为必需。

```c
#include <zephyr/drivers/usb/udc.h>
```

UDC 驱动 API。任何 USB 设备控制器驱动都必须提供这些 API，但 device_speed() 和 test_mode() 仅对高速（HS）控制器为必需。

## 31.2\_数据成员（Data Fields）

<a id="r_adf2b8f76158d7bd2d3918628c8a9fc22"></a>

```c
enum udc_bus_speed(* device_speed )(const struct device *dev)
```



相关声明：[udc_bus_speed](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1b)、[device_speed](P031_USB设备控制器驱动接口.md#adf2b8f76158d7bd2d3918628c8a9fc22)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_aa1d3dadf63cb156ce5346712e1c65069"></a>

```c
int(* ep_enqueue )(const struct device *dev, struct udc_ep_config *const cfg, struct net_buf *const buf)
```



相关声明：[ep_enqueue](P031_USB设备控制器驱动接口.md#aa1d3dadf63cb156ce5346712e1c65069)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_a023fcfa0fa251dcadcb379347fe7531a"></a>

```c
int(* ep_dequeue )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_dequeue](P031_USB设备控制器驱动接口.md#a023fcfa0fa251dcadcb379347fe7531a)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_adf2adaea90b53999d1e98756062a2050"></a>

```c
int(* ep_set_halt )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_set_halt](P031_USB设备控制器驱动接口.md#adf2adaea90b53999d1e98756062a2050)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_a923a684868721d0b7232c86eed15e121"></a>

```c
int(* ep_clear_halt )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_clear_halt](P031_USB设备控制器驱动接口.md#a923a684868721d0b7232c86eed15e121)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_a775a18f5555f1c518762ff7dc016559c"></a>

```c
int(* ep_try_config )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_try_config](P031_USB设备控制器驱动接口.md#a775a18f5555f1c518762ff7dc016559c)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_a27291ab4d2acda207f6a6a2313d50793"></a>

```c
int(* ep_enable )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_enable](P031_USB设备控制器驱动接口.md#a27291ab4d2acda207f6a6a2313d50793)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_a1af05b484e9c9d1f2a0dbfb822f09c98"></a>

```c
int(* ep_disable )(const struct device *dev, struct udc_ep_config *const cfg)
```



相关声明：[ep_disable](P031_USB设备控制器驱动接口.md#a1af05b484e9c9d1f2a0dbfb822f09c98)、[device](../device_reference/P002_设备对象结构.md)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

<a id="r_aeca6c3a8a6b7af469d96bec8c9a8e5eb"></a>

```c
int(* host_wakeup )(const struct device *dev)
```



相关声明：[host_wakeup](P031_USB设备控制器驱动接口.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a2e8b88743ab56144a199b3ad0618755f"></a>

```c
int(* set_address )(const struct device *dev, const uint8_t addr)
```



相关声明：[set_address](P031_USB设备控制器驱动接口.md#a2e8b88743ab56144a199b3ad0618755f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ab06839ded48cbc671b2b915fe0010959"></a>

```c
int(* test_mode )(const struct device *dev, const uint8_t mode, const bool dryrun)
```



相关声明：[test_mode](P031_USB设备控制器驱动接口.md#ab06839ded48cbc671b2b915fe0010959)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_af8b916f6b8c211ad82ddcfdaa12de5ae"></a>

```c
int(* enable )(const struct device *dev)
```



相关声明：[enable](P031_USB设备控制器驱动接口.md#af8b916f6b8c211ad82ddcfdaa12de5ae)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a8997bba956d264463b71aae0b1a4e3dc"></a>

```c
int(* disable )(const struct device *dev)
```



相关声明：[disable](P031_USB设备控制器驱动接口.md#a8997bba956d264463b71aae0b1a4e3dc)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a01f803a2d258072df102b831cf184b27"></a>

```c
int(* init )(const struct device *dev)
```



相关声明：[init](P031_USB设备控制器驱动接口.md#a01f803a2d258072df102b831cf184b27)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ad7135abf78eb372730dddbba7dc6a75d"></a>

```c
int(* shutdown )(const struct device *dev)
```



相关声明：[shutdown](P031_USB设备控制器驱动接口.md#ad7135abf78eb372730dddbba7dc6a75d)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a1e3d733665cd609381e02929907c9837"></a>

```c
void(* lock )(const struct device *dev)
```



相关声明：[lock](P031_USB设备控制器驱动接口.md#a1e3d733665cd609381e02929907c9837)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a2be8523215fd255112bb03d9cd54c26b"></a>

```c
void(* unlock )(const struct device *dev)
```



相关声明：[unlock](P031_USB设备控制器驱动接口.md#a2be8523215fd255112bb03d9cd54c26b)、[device](../device_reference/P002_设备对象结构.md)。

## 31.3\_详细说明（Detailed Documentation）

<a id="adf2b8f76158d7bd2d3918628c8a9fc22"></a>

### `device_speed`

```c
enum udc_bus_speed(* udc_api::device_speed) (const struct device *dev)
```

<a id="a8997bba956d264463b71aae0b1a4e3dc"></a>

### `disable`

```c
int(* udc_api::disable) (const struct device *dev)
```

<a id="af8b916f6b8c211ad82ddcfdaa12de5ae"></a>

### `enable`

```c
int(* udc_api::enable) (const struct device *dev)
```

<a id="a923a684868721d0b7232c86eed15e121"></a>

### `ep_clear_halt`

```c
int(* udc_api::ep_clear_halt) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="a023fcfa0fa251dcadcb379347fe7531a"></a>

### `ep_dequeue`

```c
int(* udc_api::ep_dequeue) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="a1af05b484e9c9d1f2a0dbfb822f09c98"></a>

### `ep_disable`

```c
int(* udc_api::ep_disable) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="a27291ab4d2acda207f6a6a2313d50793"></a>

### `ep_enable`

```c
int(* udc_api::ep_enable) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="aa1d3dadf63cb156ce5346712e1c65069"></a>

### `ep_enqueue`

```c
int(* udc_api::ep_enqueue) (const struct device *dev, struct udc_ep_config *const cfg, struct net_buf *const buf)
```

<a id="adf2adaea90b53999d1e98756062a2050"></a>

### `ep_set_halt`

```c
int(* udc_api::ep_set_halt) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="a775a18f5555f1c518762ff7dc016559c"></a>

### `ep_try_config`

```c
int(* udc_api::ep_try_config) (const struct device *dev, struct udc_ep_config *const cfg)
```

<a id="aeca6c3a8a6b7af469d96bec8c9a8e5eb"></a>

### `host_wakeup`

```c
int(* udc_api::host_wakeup) (const struct device *dev)
```

<a id="a01f803a2d258072df102b831cf184b27"></a>

### `init`

```c
int(* udc_api::init) (const struct device *dev)
```

<a id="a1e3d733665cd609381e02929907c9837"></a>

### `lock`

```c
void(* udc_api::lock) (const struct device *dev)
```

> 译注（源码核对）：这是驱动函数表的锁入口，配套 unlock；公共UDC层在调用许多硬件操作前后使用它们。官方骨架通过 udc_lock_internal()/udc_unlock_internal() 接入互斥量，并非只有应用才需要考虑同步。

<a id="a2e8b88743ab56144a199b3ad0618755f"></a>

### `set_address`

```c
int(* udc_api::set_address) (const struct device *dev, const uint8_t addr)
```

<a id="ad7135abf78eb372730dddbba7dc6a75d"></a>

### `shutdown`

```c
int(* udc_api::shutdown) (const struct device *dev)
```

<a id="ab06839ded48cbc671b2b915fe0010959"></a>

### `test_mode`

```c
int(* udc_api::test_mode) (const struct device *dev, const uint8_t mode, const bool dryrun)
```

<a id="a2be8523215fd255112bb03d9cd54c26b"></a>

### `unlock`

```c
void(* udc_api::unlock) (const struct device *dev)
```

## 31.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P030_USB设备控制器API.md) · [返回大纲](大纲.md) · [下一章](P032_USB设备控制器缓冲区信息.md)
