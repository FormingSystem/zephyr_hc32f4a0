---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-19
title: Renesas 事件链接控制器（ELC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Renesas 事件链接控制器（ELC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas 事件链接控制器（Event Link Controller，ELC）接口。

<a id="details"></a>

Renesas 事件链接控制器（Event Link Controller，ELC）接口。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_renesas_5Felc_2Eh"></a>

```c
file renesas_elc.h
```

相关声明：[renesas_elc.h](../api_file_clock_network_reference/P021_zephyr__drivers__misc__interconn__renesas_elc__renesas_elc.h_文件参考.md)。

Renesas事件链路控制器（ELC）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.2\_数据结构（Data Structures）

<a id="r_renesas_5Felc_5Fdt_5Fspec"></a>

```c
struct renesas_elc_dt_spec
```

相关声明：[renesas_elc_dt_spec](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md)。

设备树（Devicetree）所指定Renesas事件链路控制器（ELC）信息的容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.3\_宏定义（Macros）

<a id="r_ga32d4b23c3857552a8fe1ca6ce04f97d4"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME](#ga32d4b23c3857552a8fe1ca6ce04f97d4)。

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga79a705be3efa01b6fcc1413dd4acfec2"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX](#ga79a705be3efa01b6fcc1413dd4acfec2)。

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga996e259c97fc2511086664865b4c0e3d"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL](#ga996e259c97fc2511086664865b4c0e3d)。

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga5e79207cee205406247a972e23360110"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL](#ga5e79207cee205406247a972e23360110)。

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_gaab4d583c93f1d5990d4a6733caaded81"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME](#gaab4d583c93f1d5990d4a6733caaded81)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga788709121dbfb2db3f74ccf9a9d51002"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX](#ga788709121dbfb2db3f74ccf9a9d51002)。

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga1d58940758c664c22cb3e183e9810370"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL](#ga1d58940758c664c22cb3e183e9810370)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga65ccb580212ee15dc9329d76e810190e"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL](#ga65ccb580212ee15dc9329d76e810190e)。

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga1f196ad20380dedf193c754906c5ed14"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME](#ga1f196ad20380dedf193c754906c5ed14)。

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

<a id="r_gace33f51f3a3a2efd42932a816e05be0b"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX](#gace33f51f3a3a2efd42932a816e05be0b)。

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

<a id="r_ga35d7aef6829d74e92fa7c82306711a6c"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR](#ga35d7aef6829d74e92fa7c82306711a6c)。

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga915d2760bd3c8ecf1b689bed286035d8"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR](#ga915d2760bd3c8ecf1b689bed286035d8)。

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga3a0b277cb45636a86bf9b665fd75d133"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME](#ga3a0b277cb45636a86bf9b665fd75d133)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）。

<a id="r_gaeab186e0f09ee56ce87719a7d5566f50"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX](#gaeab186e0f09ee56ce87719a7d5566f50)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）。

<a id="r_ga0e1c393825d778fd22a9a190eaedc308"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR(inst, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR](#ga0e1c393825d778fd22a9a190eaedc308)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga360d362b3fc26afb7cc81bfd28f6fc6a"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR](#ga360d362b3fc26afb7cc81bfd28f6fc6a)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga920e3b26fb52a728ed2a3cd1ab5af7f0"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)。

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）。

<a id="r_ga6f3093b0556eb8eb1931e9b8b746245a"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX](#ga6f3093b0556eb8eb1931e9b8b746245a)。

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）。

<a id="r_ga41c5adcf8817d529b5521727d9937b42"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR](#ga41c5adcf8817d529b5521727d9937b42)。

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga2b0a12781acca4123dd7899446a94b6f"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR](#ga2b0a12781acca4123dd7899446a94b6f)。

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga86ded9427001c5d3b315b71dcbfad7d0"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME](#ga86ded9427001c5d3b315b71dcbfad7d0)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）。

<a id="r_gac5dfa5e30e1ac9ac703842e61dd3fa3b"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX](#gac5dfa5e30e1ac9ac703842e61dd3fa3b)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）。

<a id="r_ga94f2bc95761722c93019371f432da262"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR(inst, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR](#ga94f2bc95761722c93019371f432da262)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga7d57a1a3bf47feda6c2831712bfd033c"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR](#ga7d57a1a3bf47feda6c2831712bfd033c)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.4\_函数（Functions）

<a id="r_gab3b55b83b38469854aae726a71f6ad55"></a>

```c
int renesas_elc_software_event_generate (const struct device *dev, uint32_t event)
```

相关声明：[renesas_elc_software_event_generate](#gab3b55b83b38469854aae726a71f6ad55)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在事件链接控制器（Event Link Controller）中生成软件事件（Software Event）。

<a id="r_ga444e17d01310283e61bcde9a1022c47a"></a>

```c
int renesas_elc_link_set (const struct device *dev, uint32_t peripheral, uint32_t event)
```

相关声明：[renesas_elc_link_set](#ga444e17d01310283e61bcde9a1022c47a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

创建单个事件链接（Event Link）。

<a id="r_ga65c950ccf0087c514daf6d543a0a7ecf"></a>

```c
int renesas_elc_link_break (const struct device *dev, uint32_t peripheral)
```

相关声明：[renesas_elc_link_break](#ga65c950ccf0087c514daf6d543a0a7ecf)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

断开事件链接（Event Link）。

<a id="r_gafbffc029fd9482be578bd05cbdb3a03f"></a>

```c
int renesas_elc_enable (const struct device *dev)
```

相关声明：[renesas_elc_enable](#gafbffc029fd9482be578bd05cbdb3a03f)、[device](../device_reference/P002_设备对象结构.md)。

启用事件链接控制器（Event Link Controller）运行。

<a id="r_gaac75089657f841c80225aa40de9c2a93"></a>

```c
int renesas_elc_disable (const struct device *dev)
```

相关声明：[renesas_elc_disable](#gaac75089657f841c80225aa40de9c2a93)、[device](../device_reference/P002_设备对象结构.md)。

禁用事件链接控制器（Event Link Controller）运行。

## 19.5\_详细说明（Detailed Documentation）

<a id="ga79a705be3efa01b6fcc1413dd4acfec2"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE_BY_IDX(node_id, renesas_elcs, idx))
```

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）。

<a id="ga5e79207cee205406247a972e23360110"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL ( node_id, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_IDX(node_id, renesas_elcs, idx))
```

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）或 NULL。

<a id="ga32d4b23c3857552a8fe1ca6ce04f97d4"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE_BY_NAME(node_id, renesas_elcs, name))
```

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）。

<a id="ga996e259c97fc2511086664865b4c0e3d"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL ( node_id, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_NAME(node_id, renesas_elcs, name))
```

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）或 NULL。

<a id="ga788709121dbfb2db3f74ccf9a9d51002"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX ( inst, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE_BY_IDX(DT_DRV_INST(inst), renesas_elcs, idx))
```

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）。

<a id="ga65ccb580212ee15dc9329d76e810190e"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL ( inst, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_IDX(DT_DRV_INST(inst), renesas_elcs, idx))
```

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）或 NULL。

<a id="gaab4d583c93f1d5990d4a6733caaded81"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME ( inst, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE_BY_NAME(DT_DRV_INST(inst), renesas_elcs, name))
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）。

<a id="ga1d58940758c664c22cb3e183e9810370"></a>

### `RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL`

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL ( inst, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_NAME(DT_DRV_INST(inst), renesas_elcs, name))
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：设备指针（Device Pointer）或 NULL。

<a id="ga6f3093b0556eb8eb1931e9b8b746245a"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DT_PHA_BY_IDX(node_id, renesas_elcs, idx, event)
```

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）。

<a id="ga2b0a12781acca4123dd7899446a94b6f"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR ( node_id, idx, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
        (RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(node_id, idx)),                              \
        (default_value))
```

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）或 default_value。

<a id="ga920e3b26fb52a728ed2a3cd1ab5af7f0"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DT_PHA_BY_NAME(node_id, renesas_elcs, name, event)
```

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）。

<a id="ga41c5adcf8817d529b5521727d9937b42"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR ( node_id, name, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
        (RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(node_id, name)),                            \
        (default_value))
```

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）或 default_value。

<a id="gac5dfa5e30e1ac9ac703842e61dd3fa3b"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX ( inst, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）。

<a id="ga7d57a1a3bf47feda6c2831712bfd033c"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR ( inst, idx, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
```

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）或 default_value。

<a id="ga86ded9427001c5d3b315b71dcbfad7d0"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME ( inst, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(DT_DRV_INST(inst), name)
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）。

<a id="ga94f2bc95761722c93019371f432da262"></a>

### `RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR`

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR ( inst, name, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：event 单元值（Cell Value）或 default_value。

<a id="gace33f51f3a3a2efd42932a816e05be0b"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DT_PHA_BY_IDX(node_id, renesas_elcs, idx, peripheral)
```

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）。

<a id="ga915d2760bd3c8ecf1b689bed286035d8"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR ( node_id, idx, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
        (RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(node_id, idx)),                         \
        (default_value))
```

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）或 default_value。

<a id="ga1f196ad20380dedf193c754906c5ed14"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
DT_PHA_BY_NAME(node_id, renesas_elcs, name, peripheral)
```

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）。

<a id="ga35d7aef6829d74e92fa7c82306711a6c"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR ( node_id, name, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
        (RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(node_id, name)),                       \
        (default_value))
```

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）或 default_value。

<a id="gaeab186e0f09ee56ce87719a7d5566f50"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX ( inst, idx )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）。

<a id="ga360d362b3fc26afb7cc81bfd28f6fc6a"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR ( inst, idx, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
```

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | renesas-elcs 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）或 default_value。

<a id="ga3a0b277cb45636a86bf9b665fd75d133"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME ( inst, name )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(DT_DRV_INST(inst), name)
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）。

<a id="ga0e1c393825d778fd22a9a190eaedc308"></a>

### `RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR`

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR ( inst, name, default_value )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

展开值（Value）：

```c
RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
```

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `name` | renesas-elcs-names 属性中指定的名称，使用小写字母与下划线（Lowercase-and-underscores）。 |
| `default_value` | 属性不存在时返回的值。 |

**返回（Returns）**：返回值（Returns）：peripheral 单元值（Cell Value）或 default_value。

<a id="gaac75089657f841c80225aa40de9c2a93"></a>

### `renesas_elc_disable()`

```c
int renesas_elc_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

禁用事件链接控制器（Event Link Controller）运行。

禁用事件链接控制器（ELC），停止事件处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 事件链接控制器设备（Event Link Controller Device）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 errno 错误码。

<a id="gafbffc029fd9482be578bd05cbdb3a03f"></a>

### `renesas_elc_enable()`

```c
int renesas_elc_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

启用事件链接控制器（Event Link Controller）运行。

启用事件链接控制器（ELC），使其可处理事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 事件链接控制器设备（Event Link Controller Device）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 errno 错误码。

<a id="ga65c950ccf0087c514daf6d543a0a7ecf"></a>

### `renesas_elc_link_break()`

```c
int renesas_elc_link_break ( const struct device * dev, uint32_t peripheral )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

断开事件链接（Event Link）。

断开指定外设的现有事件链接（Event Link）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 事件链接控制器设备（Event Link Controller Device）。 |
| `peripheral` | 要断开其链接的外设 ID（Peripheral ID）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 errno 错误码。

<a id="ga444e17d01310283e61bcde9a1022c47a"></a>

### `renesas_elc_link_set()`

```c
int renesas_elc_link_set ( const struct device * dev, uint32_t peripheral, uint32_t event )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

创建单个事件链接（Event Link）。

将外设与特定事件信号（Event Signal）关联，以配置事件链接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 事件链接控制器设备（Event Link Controller Device）。 |
| `peripheral` | 要链接到事件信号的外设 ID（Peripheral ID）。 |
| `event` | 要与外设关联的事件信号 ID（Event Signal ID）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 errno 错误码。

<a id="gab3b55b83b38469854aae726a71f6ad55"></a>

### `renesas_elc_software_event_generate()`

```c
int renesas_elc_software_event_generate ( const struct device * dev, uint32_t event )
```

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

在事件链接控制器（Event Link Controller）中生成软件事件（Software Event）。

请求 Renesas 事件链接控制器（ELC）生成由 event 标识的软件事件（Software Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 事件链接控制器设备（Event Link Controller Device）。 |
| `event` | 要生成的软件事件 ID（Software Event ID）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 errno 错误码。


## 19.6\_原页交叉引用（Cross References）

- [renesas_elc.h](../api_file_clock_network_reference/P021_zephyr__drivers__misc__interconn__renesas_elc__renesas_elc.h_文件参考.md)
- [renesas_elc_dt_spec](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga8ff163c240878a988d29d727671671de)
- [DEVICE_DT_GET_OR_NULL](../device_reference/P001_设备模型公共接口.md#ga6ce1dbfda6847ca6c3858712e9b41989)
- [DT_PHANDLE_BY_NAME](../dt_property_reference/P001_设备树属性读取宏.md#ga65c90d2d96255b8569c5b869b637c2fd)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_PHA_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PHA_BY_NAME](../dt_property_reference/P001_设备树属性读取宏.md#gae469615356a867c49416da15bdc44a26)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga8ff163c240878a988d29d727671671de"></a>
<a id="agroup__device__model_html_ga6ce1dbfda6847ca6c3858712e9b41989"></a>
<a id="agroup__devicetree-generic-prop_html_ga65c90d2d96255b8569c5b869b637c2fd"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-generic-prop_html_ga118b63fd22c20ef940ac2fa073c126ed"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__renesas__elc__interface_html_ga6f3093b0556eb8eb1931e9b8b746245a"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__devicetree-generic-prop_html_gae469615356a867c49416da15bdc44a26"></a>
<a id="agroup__renesas__elc__interface_html_ga920e3b26fb52a728ed2a3cd1ab5af7f0"></a>
<a id="agroup__renesas__elc__interface_html_ga2b0a12781acca4123dd7899446a94b6f"></a>
<a id="agroup__renesas__elc__interface_html_ga41c5adcf8817d529b5521727d9937b42"></a>
<a id="agroup__renesas__elc__interface_html_gace33f51f3a3a2efd42932a816e05be0b"></a>
<a id="agroup__renesas__elc__interface_html_ga1f196ad20380dedf193c754906c5ed14"></a>
<a id="agroup__renesas__elc__interface_html_ga915d2760bd3c8ecf1b689bed286035d8"></a>
<a id="agroup__renesas__elc__interface_html_ga35d7aef6829d74e92fa7c82306711a6c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_网络配置库（Network Configuration Library）.md) · [返回大纲](大纲.md) · [下一章](P020_工具链抽象（Toolchain abstraction）.md)
