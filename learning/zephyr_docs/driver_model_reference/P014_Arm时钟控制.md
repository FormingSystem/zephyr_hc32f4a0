---
id: learning.zephyr-docs.driver-model-reference.page-14
title: Arm时钟控制
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structarm__clock__control__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_Arm时钟控制

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structarm__clock__control__t.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ARM CMSDK 片上系统（SoC）的时钟控制子系统描述符（Clock Control Subsystem Descriptor）。

```c
#include <zephyr/drivers/clock_control/arm_clock_control.h>
```

<a id="details"></a>

ARM CMSDK 片上系统（SoC）的时钟控制子系统描述符（Clock Control Subsystem Descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ab596009f00c33d84af817c860bdb9e40"></a>

```c
enum arm_bus_type_t bus
```

相关声明：[arm_bus_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gaf000c4220627db6eee0117062c6c50ef)、[bus](#ab596009f00c33d84af817c860bdb9e40)。

设备所在的外设总线（Peripheral Bus）。

<a id="r_a46cd4433f02663f09022a71ae7fe6550"></a>

```c
enum arm_soc_state_t state
```

相关声明：[arm_soc_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ga0a2c04415a74486aa29a4d1d0d7679e1)、[state](#a46cd4433f02663f09022a71ae7fe6550)。

时钟设置适用的 CPU 状态。

<a id="r_ab2946697523620aa1f52ae69c636721e"></a>

```c
uint32_t device
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[device](#ab2946697523620aa1f52ae69c636721e)。

标识总线上的设备。

## 14.2\_详细说明（Detailed Documentation）

<a id="ab596009f00c33d84af817c860bdb9e40"></a>

### `bus`

```c
enum arm_bus_type_t arm_clock_control_t::bus
```

设备所在的外设总线（Peripheral Bus）。

<a id="ab2946697523620aa1f52ae69c636721e"></a>

### `device`

```c
uint32_t arm_clock_control_t::device
```

标识总线上的设备。

<a id="a46cd4433f02663f09022a71ae7fe6550"></a>

### `state`

```c
enum arm_soc_state_t arm_clock_control_t::state
```

时钟设置适用的 CPU 状态。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/arm_clock_control.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/arm_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h_source.html)
- [arm_bus_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gaf000c4220627db6eee0117062c6c50ef)
- [arm_soc_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ga0a2c04415a74486aa29a4d1d0d7679e1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_Andes原位执行设置参数.md) · [返回大纲](大纲.md) · [下一章](P015_Atmel_SAM电源管理时钟配置.md)
