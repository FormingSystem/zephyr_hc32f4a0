---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-4
title: zephyr__drivers__dma__sf32lb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma_2sf32lb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_dma\_\_sf32lb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma_2sf32lb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/dma.h>
#include <zephyr/dt-bindings/dma/sf32lb-dma-config.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_sf32lb_5Fdma_5Fdt_5Fspec"></a>

```c
struct sf32lb_dma_dt_spec
```

相关声明：[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

SF32LB直接内存访问的设备树规格（DMA DT Spec）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gafe8cf86b36b9741dd069b296bf2dfbdf"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET(node_id)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gafe8cf86b36b9741dd069b296bf2dfbdf)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_gaf9f8a7a13b1c806aa182e917c99cacaf"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME(node_id, name)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gaf9f8a7a13b1c806aa182e917c99cacaf)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_gacb66db47cfc3b7bf06ca1323de291611"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gacb66db47cfc3b7bf06ca1323de291611)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体，必要时回退到默认值（Default Values）。

<a id="r_gafac07cb5115b1e38d3894a9d63267b94"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET(index)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gafac07cb5115b1e38d3894a9d63267b94)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_ga81ecab737bf1dbe44c4ec49dc7a42cb4"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME(index, name)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga81ecab737bf1dbe44c4ec49dc7a42cb4)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_ga0acc6ba43d7b7e77218110b0e3fb5777"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR(index, name, default_value)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga0acc6ba43d7b7e77218110b0e3fb5777)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga6a55283d1c080695e9b6130bd86da8b2"></a>

```c
static bool sf32lb_dma_is_ready_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sf32lb_dma_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga6a55283d1c080695e9b6130bd86da8b2)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

检查 DMA 控制器（Controller）是否就绪。

<a id="r_ga15960e506ac44ea925a84b29730f94dd"></a>

```c
static void sf32lb_dma_config_init_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_config *config)
```

相关声明：[sf32lb_dma_config_init_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga15960e506ac44ea925a84b29730f94dd)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_config](../dma_reference/P004_DMA通道配置.md)。

根据设备树规格（DT Spec）初始化 DMA 配置结构体。

<a id="r_ga4e70429d274e376e6152291aa6815e56"></a>

```c
static int sf32lb_dma_config_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_config *config)
```

相关声明：[sf32lb_dma_config_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga4e70429d274e376e6152291aa6815e56)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_config](../dma_reference/P004_DMA通道配置.md)。

根据设备树规格（DT Spec）配置 DMA 通道（Channel）。

<a id="r_ga4aac7edfd591224b08956a1aab6e4c7c"></a>

```c
static int sf32lb_dma_start_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[sf32lb_dma_start_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga4aac7edfd591224b08956a1aab6e4c7c)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

根据设备树规格（DT Spec）启动 DMA 传输（Transfer）。

<a id="r_ga7d9763ae4042d855718a855955faef78"></a>

```c
static int sf32lb_dma_stop_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[sf32lb_dma_stop_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga7d9763ae4042d855718a855955faef78)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

根据设备树规格（DT Spec）停止 DMA 传输（Transfer）。

<a id="r_gab6dd22ab9a477e8fb450d8197c15a280"></a>

```c
static int sf32lb_dma_reload_dt (const struct sf32lb_dma_dt_spec *spec, uintptr_t src, uintptr_t dst, size_t size)
```

相关声明：[sf32lb_dma_reload_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gab6dd22ab9a477e8fb450d8197c15a280)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据设备树规格（DT Spec）重新装载 DMA 传输（Reload Transfer）。

<a id="r_ga6ca2f3a9b69b930552d0704bc562f01f"></a>

```c
static int sf32lb_dma_get_status_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_status *status)
```

相关声明：[sf32lb_dma_get_status_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga6ca2f3a9b69b930552d0704bc562f01f)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_status](../dma_reference/P005_DMA运行状态.md)。

根据设备树规格（DT Spec）获取 DMA 传输状态（Transfer Status）。


## 4.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/drivers/dma.h](../dma_reference/P010_DMA驱动头文件源码.md)
- [zephyr/dt-bindings/dma/sf32lb-dma-config.h](../api_source_reference/P775_sf32lb-dma-config.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P136_sf32lb.h_源码浏览.md)
- [sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)
- [SF32LB_DMA_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gafe8cf86b36b9741dd069b296bf2dfbdf)
- [SF32LB_DMA_DT_SPEC_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gaf9f8a7a13b1c806aa182e917c99cacaf)
- [SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gacb66db47cfc3b7bf06ca1323de291611)
- [SF32LB_DMA_DT_INST_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gafac07cb5115b1e38d3894a9d63267b94)
- [SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga81ecab737bf1dbe44c4ec49dc7a42cb4)
- [SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga0acc6ba43d7b7e77218110b0e3fb5777)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [sf32lb_dma_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga6a55283d1c080695e9b6130bd86da8b2)
- [sf32lb_dma_config_init_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga15960e506ac44ea925a84b29730f94dd)
- [dma_config](../dma_reference/P004_DMA通道配置.md)
- [sf32lb_dma_config_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga4e70429d274e376e6152291aa6815e56)
- [sf32lb_dma_start_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga4aac7edfd591224b08956a1aab6e4c7c)
- [sf32lb_dma_stop_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga7d9763ae4042d855718a855955faef78)
- [sf32lb_dma_reload_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#gab6dd22ab9a477e8fb450d8197c15a280)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [sf32lb_dma_get_status_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html#ga6ca2f3a9b69b930552d0704bc562f01f)
- [dma_status](../dma_reference/P005_DMA运行状态.md)

---

[上一章](P003_zephyr__net__dhcpv4.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__firmware__scmi__nxp__cpu.h_文件参考.md)
