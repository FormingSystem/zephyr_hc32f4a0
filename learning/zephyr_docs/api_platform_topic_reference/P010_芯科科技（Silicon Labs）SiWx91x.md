---
id: learning.zephyr-docs.api-platform-topic-reference.page-10
title: 芯科科技（Silicon Labs）SiWx91x
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_芯科科技（Silicon Labs）SiWx91x

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fsilabs_5Fsiwx91x_2Eh"></a>

```c
file clock_control_silabs_siwx91x.h
```

相关声明：[clock_control_silabs_siwx91x.h](../api_file_supplement_reference/P019_zephyr__drivers__clock_control__clock_control_silabs_siwx91x.h_文件参考.md)。

Silicon Labs SiWx91x设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_silabs_5Fsiwx91x_5Fclock_5Fcontrol_5Fconfig"></a>

```c
struct silabs_siwx91x_clock_control_config
```

相关声明：[silabs_siwx91x_clock_control_config](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md)。

SiWx91x时钟管理器的多路选择/门控时钟（Mux / Gate Clock）配置。

<a id="r_silabs_5Fsiwx91x_5Fclock_5Fcontrol_5Fpll_5Fconfig"></a>

```c
struct silabs_siwx91x_clock_control_pll_config
```

相关声明：[silabs_siwx91x_clock_control_pll_config](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md)。

SiWx91x高性能（HP）时钟管理器的锁相环（PLL）配置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_gab38e7d7ff3ea5e9a12358aa4a98bd1dd"></a>

```c
const struct device * siwx91x_clock_control_get_device (uint32_t clkid)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[siwx91x_clock_control_get_device](#gab38e7d7ff3ea5e9a12358aa4a98bd1dd)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取拥有 `clkid` 的时钟控制设备（Clock Control Device）。

## 10.4\_详细说明（Detailed Documentation）

<a id="gab38e7d7ff3ea5e9a12358aa4a98bd1dd"></a>

### `siwx91x_clock_control_get_device()`

```c
const struct device * siwx91x_clock_control_get_device ( uint32_t clkid)
```

```c
#include <zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h>
```

获取拥有 `clkid` 的时钟控制设备（Clock Control Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clkid` | 时钟标识符，取 `SIWX91X_CLK_*`。 |

返回（Returns）：指向所属时钟控制设备（Owning Clock Control Device）的指针；若 `clkid` 超出范围或没有关联设备，则返回 `NULL`。


## 10.5\_原页交叉引用（Cross References）

- [clock_control_silabs_siwx91x.h](../api_file_supplement_reference/P019_zephyr__drivers__clock_control__clock_control_silabs_siwx91x.h_文件参考.md)
- [silabs_siwx91x_clock_control_config](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md)
- [silabs_siwx91x_clock_control_pll_config](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_新唐 M48x 时钟控制器设备树辅助功能（Devicetree helpers）.md) · [返回大纲](大纲.md) · [下一章](P011_新唐 NuMaker 控制器设备树辅助功能（Devicetree helpers）.md)
