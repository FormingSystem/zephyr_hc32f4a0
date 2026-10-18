---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-19
title: zephyr__drivers__mux.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_mux.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多路复用器（Multiplexer，MUX）控制器的公共API。

<a id="details"></a>

```c
#include <errno.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/mux.h>
#include <zephyr/sys/util.h>
#include <zephyr/syscalls/mux.h>
```

查看此文件的源码。

多路复用器（Multiplexer，MUX）控制器的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

<a id="r_mux_5Fcontrol"></a>

```c
struct mux_control
```

相关声明：[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)。

单条多路复用器（MUX）控制线仅用于寻址的说明符。

<a id="r_mux_5Fstate"></a>

```c
struct mux_state
```

相关声明：[mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)。

多路复用器（MUX）控制线的寻址与默认状态对。

<a id="r_mux_5Fcontrol_5Fdriver_5Fapi"></a>

```c
struct mux_control_driver_api
```

相关声明：[mux_control_driver_api](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md)。

多路复用器（MUX）控制器驱动API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.2\_宏定义（Macros）

<a id="r_ga1fcf4fd9a94643c1b778994f76b64150"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, idx)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga1fcf4fd9a94643c1b778994f76b64150)。

根据 `mux-controls` 条目定义 `mux_control` 对象。

<a id="r_ga076e92976afbf9ecf39cf8536e6e31a6"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE(node_id)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga076e92976afbf9ecf39cf8536e6e31a6)。

等同于 `MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

<a id="r_ga332c39734d3dff70067278d29e2875b3"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME(node_id, name)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga332c39734d3dff70067278d29e2875b3)。

根据 `mux-control-names` 条目按名称定义 `mux_control` 对象。

<a id="r_gac162201caf07686e7c9c8cd736ebf7e2"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, idx)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gac162201caf07686e7c9c8cd736ebf7e2)。

根据 `mux-states` 条目定义 `mux_state` 对象。

<a id="r_gacd33ebfd1ef975152505d5ba800fd184"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE(node_id)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gacd33ebfd1ef975152505d5ba800fd184)。

等同于 `MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

<a id="r_gad42cfa2560136a306b1409c4fa64596a"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_NAME(node_id, name)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad42cfa2560136a306b1409c4fa64596a)。

根据 `mux-state-names` 条目按名称定义 `mux_state` 对象。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.3\_函数（Functions）

<a id="r_ga69b883de5e7c90f797d5a07063089bbc"></a>

```c
int mux_control_set (const struct device *dev, const struct mux_control *control, uint32_t state)
```

相关声明：[mux_control_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga69b883de5e7c90f797d5a07063089bbc)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

将 MUX 控制线驱动到给定状态。

<a id="r_gad1b56b4430fca99f03bdf2b0ad6725c5"></a>

```c
int mux_state_apply (const struct device *dev, const struct mux_state *mstate)
```

相关声明：[mux_state_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad1b56b4430fca99f03bdf2b0ad6725c5)、[device](../device_reference/P002_设备对象结构.md)、[mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)。

将设备树定义的默认状态应用于多路复用器（MUX）控制线。

<a id="r_ga188b04add235e080b95ea293e7cfd276"></a>

```c
int mux_state_get (const struct device *dev, const struct mux_control *control, uint32_t *state)
```

相关声明：[mux_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga188b04add235e080b95ea293e7cfd276)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

读回 MUX 控制线的当前状态。

<a id="r_ga0e3cbbb7ac8796c3651b56c41dd1cec5"></a>

```c
int mux_control_disconnect (const struct device *dev, const struct mux_control *control)
```

相关声明：[mux_control_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga0e3cbbb7ac8796c3651b56c41dd1cec5)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)。

物理断开 MUX 控制线。


## 19.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/devicetree/mux.h](../dt_connection_reference/P009_设备树多路复用器头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html)
- [mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)
- [mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)
- [mux_control_driver_api](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md)
- [MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga1fcf4fd9a94643c1b778994f76b64150)
- [MUX_CONTROL_DT_SPEC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga076e92976afbf9ecf39cf8536e6e31a6)
- [MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga332c39734d3dff70067278d29e2875b3)
- [MUX_STATE_DT_SPEC_DEFINE_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gac162201caf07686e7c9c8cd736ebf7e2)
- [MUX_STATE_DT_SPEC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gacd33ebfd1ef975152505d5ba800fd184)
- [MUX_STATE_DT_SPEC_DEFINE_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad42cfa2560136a306b1409c4fa64596a)
- [mux_control_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga69b883de5e7c90f797d5a07063089bbc)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [mux_state_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad1b56b4430fca99f03bdf2b0ad6725c5)
- [mux_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga188b04add235e080b95ea293e7cfd276)
- [mux_control_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga0e3cbbb7ac8796c3651b56c41dd1cec5)

<a id="header-details"></a>

---

[上一章](P018_zephyr__drivers__mspi__mspi_dw.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__mgmt__osdp.h_头文件参考.md)
