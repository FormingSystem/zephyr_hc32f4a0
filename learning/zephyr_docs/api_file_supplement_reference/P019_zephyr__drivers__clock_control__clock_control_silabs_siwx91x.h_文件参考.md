---
id: learning.zephyr-docs.api-file-supplement-reference.page-19
title: zephyr__drivers__clock_control__clock_control_silabs_siwx91x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_silabs\_siwx91x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Silicon Labs SiWx91x设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

查看此文件的源码。

Silicon Labs SiWx91x设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

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

## 19.2\_函数（Functions）

<a id="r_gab38e7d7ff3ea5e9a12358aa4a98bd1dd"></a>

```c
const struct device * siwx91x_clock_control_get_device (uint32_t clkid)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[siwx91x_clock_control_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html#gab38e7d7ff3ea5e9a12358aa4a98bd1dd)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取拥有 `clkid` 的时钟控制设备（Clock Control Device）。


## 19.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/dt-bindings/clock/silabs/siwx91x-clock.h](../api_source_reference/P791_siwx91x-clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P105_clock_control_silabs_siwx91x.h_源码浏览.md)
- [silabs_siwx91x_clock_control_config](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md)
- [silabs_siwx91x_clock_control_pll_config](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [siwx91x_clock_control_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html#gab38e7d7ff3ea5e9a12358aa4a98bd1dd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P018_zephyr__drivers__clock_control__clock_control_rpi_pico.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__drivers__audio__cs35l5x.h_文件参考.md)
