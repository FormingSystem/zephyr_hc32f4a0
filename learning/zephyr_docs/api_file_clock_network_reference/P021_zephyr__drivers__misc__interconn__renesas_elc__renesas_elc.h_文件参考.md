---
id: learning.zephyr-docs.api-file-clock-network-reference.page-21
title: zephyr__drivers__misc__interconn__renesas_elc__renesas_elc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_misc\_\_interconn\_\_renesas\_elc\_\_renesas\_elc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas事件链路控制器（ELC）驱动的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/slist.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/internal/syscall_handler.h>
#include <zephyr/syscalls/renesas_elc.h>
```

查看此文件的源码。

Renesas事件链路控制器（ELC）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_renesas_5Felc_5Fdt_5Fspec"></a>

```c
struct renesas_elc_dt_spec
```

相关声明：[renesas_elc_dt_spec](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md)。

设备树（Devicetree）所指定Renesas事件链路控制器（ELC）信息的容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga32d4b23c3857552a8fe1ca6ce04f97d4"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga32d4b23c3857552a8fe1ca6ce04f97d4)。

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga79a705be3efa01b6fcc1413dd4acfec2"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga79a705be3efa01b6fcc1413dd4acfec2)。

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga996e259c97fc2511086664865b4c0e3d"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga996e259c97fc2511086664865b4c0e3d)。

按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga5e79207cee205406247a972e23360110"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga5e79207cee205406247a972e23360110)。

按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_gaab4d583c93f1d5990d4a6733caaded81"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaab4d583c93f1d5990d4a6733caaded81)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga788709121dbfb2db3f74ccf9a9d51002"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga788709121dbfb2db3f74ccf9a9d51002)。

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）。

<a id="r_ga1d58940758c664c22cb3e183e9810370"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga1d58940758c664c22cb3e183e9810370)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga65ccb580212ee15dc9329d76e810190e"></a>

```c
#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga65ccb580212ee15dc9329d76e810190e)。

对于 DT_DRV_COMPAT 实例，按索引（Index）从 renesas-elcs 属性获取设备指针（Device Pointer）；属性不存在时返回 NULL。

<a id="r_ga1f196ad20380dedf193c754906c5ed14"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga1f196ad20380dedf193c754906c5ed14)。

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

<a id="r_gace33f51f3a3a2efd42932a816e05be0b"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gace33f51f3a3a2efd42932a816e05be0b)。

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）。

<a id="r_ga35d7aef6829d74e92fa7c82306711a6c"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga35d7aef6829d74e92fa7c82306711a6c)。

按元素名称（Element Name）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga915d2760bd3c8ecf1b689bed286035d8"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga915d2760bd3c8ecf1b689bed286035d8)。

按索引（Index）从 renesas-elcs 属性获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga3a0b277cb45636a86bf9b665fd75d133"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga3a0b277cb45636a86bf9b665fd75d133)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）。

<a id="r_gaeab186e0f09ee56ce87719a7d5566f50"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaeab186e0f09ee56ce87719a7d5566f50)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）。

<a id="r_ga0e1c393825d778fd22a9a190eaedc308"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR(inst, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga0e1c393825d778fd22a9a190eaedc308)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga360d362b3fc26afb7cc81bfd28f6fc6a"></a>

```c
#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga360d362b3fc26afb7cc81bfd28f6fc6a)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取peripheral 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga920e3b26fb52a728ed2a3cd1ab5af7f0"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(node_id, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga920e3b26fb52a728ed2a3cd1ab5af7f0)。

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）。

<a id="r_ga6f3093b0556eb8eb1931e9b8b746245a"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(node_id, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga6f3093b0556eb8eb1931e9b8b746245a)。

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）。

<a id="r_ga41c5adcf8817d529b5521727d9937b42"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga41c5adcf8817d529b5521727d9937b42)。

按元素名称（Element Name）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga2b0a12781acca4123dd7899446a94b6f"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga2b0a12781acca4123dd7899446a94b6f)。

按索引（Index）从 renesas-elcs 属性获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga86ded9427001c5d3b315b71dcbfad7d0"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME(inst, name)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga86ded9427001c5d3b315b71dcbfad7d0)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）。

<a id="r_gac5dfa5e30e1ac9ac703842e61dd3fa3b"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX(inst, idx)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gac5dfa5e30e1ac9ac703842e61dd3fa3b)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）。

<a id="r_ga94f2bc95761722c93019371f432da262"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR(inst, name, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga94f2bc95761722c93019371f432da262)。

对于 DT_DRV_COMPAT 实例，按元素名称（Element Name）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="r_ga7d57a1a3bf47feda6c2831712bfd033c"></a>

```c
#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga7d57a1a3bf47feda6c2831712bfd033c)。

对于 DT_DRV_COMPAT 实例，按索引（Index）获取event 单元值（Cell Value）；属性不存在时返回默认值（Default Value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_gab3b55b83b38469854aae726a71f6ad55"></a>

```c
int renesas_elc_software_event_generate (const struct device *dev, uint32_t event)
```

相关声明：[renesas_elc_software_event_generate](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gab3b55b83b38469854aae726a71f6ad55)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在事件链接控制器（Event Link Controller）中生成软件事件（Software Event）。

<a id="r_ga444e17d01310283e61bcde9a1022c47a"></a>

```c
int renesas_elc_link_set (const struct device *dev, uint32_t peripheral, uint32_t event)
```

相关声明：[renesas_elc_link_set](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga444e17d01310283e61bcde9a1022c47a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

创建单个事件链接（Event Link）。

<a id="r_ga65c950ccf0087c514daf6d543a0a7ecf"></a>

```c
int renesas_elc_link_break (const struct device *dev, uint32_t peripheral)
```

相关声明：[renesas_elc_link_break](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga65c950ccf0087c514daf6d543a0a7ecf)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

断开事件链接（Event Link）。

<a id="r_gafbffc029fd9482be578bd05cbdb3a03f"></a>

```c
int renesas_elc_enable (const struct device *dev)
```

相关声明：[renesas_elc_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gafbffc029fd9482be578bd05cbdb3a03f)、[device](../device_reference/P002_设备对象结构.md)。

启用事件链接控制器（Event Link Controller）运行。

<a id="r_gaac75089657f841c80225aa40de9c2a93"></a>

```c
int renesas_elc_disable (const struct device *dev)
```

相关声明：[renesas_elc_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaac75089657f841c80225aa40de9c2a93)、[device](../device_reference/P002_设备对象结构.md)。

禁用事件链接控制器（Event Link Controller）运行。


## 21.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/internal/syscall_handler.h](../syscall_boot_reference/P005_系统调用处理头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P708_renesas_elc.h_源码浏览.md)
- [renesas_elc_dt_spec](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md)
- [RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga32d4b23c3857552a8fe1ca6ce04f97d4)
- [RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga79a705be3efa01b6fcc1413dd4acfec2)
- [RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga996e259c97fc2511086664865b4c0e3d)
- [RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga5e79207cee205406247a972e23360110)
- [RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaab4d583c93f1d5990d4a6733caaded81)
- [RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga788709121dbfb2db3f74ccf9a9d51002)
- [RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga1d58940758c664c22cb3e183e9810370)
- [RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga65ccb580212ee15dc9329d76e810190e)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga1f196ad20380dedf193c754906c5ed14)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gace33f51f3a3a2efd42932a816e05be0b)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga35d7aef6829d74e92fa7c82306711a6c)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga915d2760bd3c8ecf1b689bed286035d8)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga3a0b277cb45636a86bf9b665fd75d133)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaeab186e0f09ee56ce87719a7d5566f50)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga0e1c393825d778fd22a9a190eaedc308)
- [RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga360d362b3fc26afb7cc81bfd28f6fc6a)
- [RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga920e3b26fb52a728ed2a3cd1ab5af7f0)
- [RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga6f3093b0556eb8eb1931e9b8b746245a)
- [RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga41c5adcf8817d529b5521727d9937b42)
- [RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga2b0a12781acca4123dd7899446a94b6f)
- [RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga86ded9427001c5d3b315b71dcbfad7d0)
- [RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gac5dfa5e30e1ac9ac703842e61dd3fa3b)
- [RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga94f2bc95761722c93019371f432da262)
- [RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga7d57a1a3bf47feda6c2831712bfd033c)
- [renesas_elc_software_event_generate](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gab3b55b83b38469854aae726a71f6ad55)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [renesas_elc_link_set](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga444e17d01310283e61bcde9a1022c47a)
- [renesas_elc_link_break](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga65c950ccf0087c514daf6d543a0a7ecf)
- [renesas_elc_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gafbffc029fd9482be578bd05cbdb3a03f)
- [renesas_elc_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaac75089657f841c80225aa40de9c2a93)

<a id="header-details"></a>

---

[上一章](P020_zephyr__dt-bindings__gpio__realtek-rts5817-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__dt-bindings__clock__rtl8752h-clocks.h_文件参考.md)
