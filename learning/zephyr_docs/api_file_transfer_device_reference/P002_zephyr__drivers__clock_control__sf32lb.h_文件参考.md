---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-2
title: zephyr__drivers__clock_control__sf32lb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control_2sf32lb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_clock\_control\_\_sf32lb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control_2sf32lb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Core Devices SF32LB设备的时钟控制辅助接口（Clock Control Helpers）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/clocks.h>
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

Core Devices SF32LB设备的时钟控制辅助接口（Clock Control Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_sf32lb_5Fclock_5Fdt_5Fspec"></a>

```c
struct sf32lb_clock_dt_spec
```

相关声明：[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

SF32LB时钟的设备树规格（Clock DT Spec）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga918cb283440e5ddf0ced958f55477b34"></a>

```c
#define SF32LB_CLOCK_DT_SPEC_GET(node_id)
```

相关声明：[SF32LB_CLOCK_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga918cb283440e5ddf0ced958f55477b34)。

根据设备树节点（DT Node）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_ga0f499e84570bfc26292d37a955b66d65"></a>

```c
#define SF32LB_CLOCK_DT_SPEC_GET_OR(node_id, default_spec)
```

相关声明：[SF32LB_CLOCK_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga0f499e84570bfc26292d37a955b66d65)。

与 `SF32LB_CLOCK_DT_SPEC_GET` 相同，但提供默认值（Default Value）。

<a id="r_gad3b3a613c2fa2606dfaf725d437d3b04"></a>

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET(index)
```

相关声明：[SF32LB_CLOCK_DT_INST_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gad3b3a613c2fa2606dfaf725d437d3b04)。

根据设备树实例（DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_ga7dfb5fb6a26ecf5785a83ce97cbf72dd"></a>

```c
#define SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET(index)
```

相关声明：[SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga7dfb5fb6a26ecf5785a83ce97cbf72dd)。

根据父设备树实例（Parent DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_gaa1ff407097f3bec82c389c128317503b"></a>

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET_OR(index, default_spec)
```

相关声明：[SF32LB_CLOCK_DT_INST_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gaa1ff407097f3bec82c389c128317503b)。

与 `SF32LB_CLOCK_DT_INST_SPEC_GET` 相同，但提供默认值（Default Value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gafb7a2391a9bb9b4a3e0f5bb528195358"></a>

```c
static bool sf32lb_clock_is_ready_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sf32lb_clock_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gafb7a2391a9bb9b4a3e0f5bb528195358)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

检查时钟设备（Clock Device）是否就绪。

<a id="r_ga4eed096f4161bce08fa721a762834edf"></a>

```c
static int sf32lb_clock_control_on_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[sf32lb_clock_control_on_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga4eed096f4161bce08fa721a762834edf)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体开启时钟（Clock）。

<a id="r_ga25d996cf39360f4d51a79856d9498247"></a>

```c
static int sf32lb_clock_control_off_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[sf32lb_clock_control_off_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga25d996cf39360f4d51a79856d9498247)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体关闭时钟（Clock）。

<a id="r_ga6287285db98a2df028a761742896bbd3"></a>

```c
static enum clock_control_status sf32lb_clock_control_get_status_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[clock_control_status](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gad12829335f0c954ab6d586549db45e09)、[sf32lb_clock_control_get_status_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga6287285db98a2df028a761742896bbd3)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体获取时钟状态（Clock Status）。

<a id="r_gaa15f0fb2a5304a9782b9dfb5ff1ddb93"></a>

```c
static uint32_t sf32lb_clock_control_get_rate_dt (const struct sf32lb_clock_dt_spec *spec, uint32_t *rate)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sf32lb_clock_control_get_rate_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gaa15f0fb2a5304a9782b9dfb5ff1ddb93)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用 `sf32lb_clock_dt_spec` 结构体获取时钟速率（Clock Rate）。


## 2.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/devicetree/clocks.h](../timer_reference/P109_设备树时钟完整头文件.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_reference/P097_sf32lb.h_源码浏览.md)
- [sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)
- [SF32LB_CLOCK_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga918cb283440e5ddf0ced958f55477b34)
- [SF32LB_CLOCK_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga0f499e84570bfc26292d37a955b66d65)
- [SF32LB_CLOCK_DT_INST_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gad3b3a613c2fa2606dfaf725d437d3b04)
- [SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga7dfb5fb6a26ecf5785a83ce97cbf72dd)
- [SF32LB_CLOCK_DT_INST_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gaa1ff407097f3bec82c389c128317503b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [sf32lb_clock_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gafb7a2391a9bb9b4a3e0f5bb528195358)
- [sf32lb_clock_control_on_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga4eed096f4161bce08fa721a762834edf)
- [sf32lb_clock_control_off_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga25d996cf39360f4d51a79856d9498247)
- [clock_control_status](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gad12829335f0c954ab6d586549db45e09)
- [sf32lb_clock_control_get_status_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#ga6287285db98a2df028a761742896bbd3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sf32lb_clock_control_get_rate_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html#gaa15f0fb2a5304a9782b9dfb5ff1ddb93)

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__mesh__blob_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__net__dhcpv4.h_文件参考.md)
