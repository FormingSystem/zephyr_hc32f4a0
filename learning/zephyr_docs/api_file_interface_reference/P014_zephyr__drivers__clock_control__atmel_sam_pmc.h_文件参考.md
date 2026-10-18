---
id: learning.zephyr-docs.api-file-interface-reference.page-14
title: zephyr__drivers__clock_control__atmel_sam_pmc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_clock\_control\_\_atmel\_sam\_pmc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Atmel SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/atmel_sam_pmc.h>
```

查看此文件的源码。

Atmel SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_atmel_5Fsam_5Fpmc_5Fconfig"></a>

```c
struct atmel_sam_pmc_config
```

相关声明：[atmel_sam_pmc_config](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md)。

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga90fa2e9a2226f7a2cb8926e9091b5eb3"></a>

```c
#define SAM_DT_PMC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(pmc))
```

相关声明：[SAM_DT_PMC_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#ga90fa2e9a2226f7a2cb8926e9091b5eb3)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

指向 PMC 时钟控制器（clock controller）的设备指针。

<a id="r_gafe5b223995886a213b8e9108fdce94d5"></a>

```c
#define SAM_DT_CLOCK_PMC_CFG(clock_id, node_id)
```

相关声明：[SAM_DT_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gafe5b223995886a213b8e9108fdce94d5)。

使用时钟描述符（clock specifier）初始化一个 `atmel_sam_pmc_config`。

<a id="r_ga0f6e3f89dcfde77d27b2685220055109"></a>

```c
#define SAM_DT_INST_CLOCK_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#ga0f6e3f89dcfde77d27b2685220055109)。

对设备树实例（DT Instance）的第一个时钟，执行与 `SAM_DT_CLOCK_PMC_CFG()` 等效的操作。

<a id="r_gadc7b9d880d6ebcf81b47eafc223e8512"></a>

```c
#define SAM_DT_CLOCKS_PMC_CFG(node_id)
```

相关声明：[SAM_DT_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gadc7b9d880d6ebcf81b47eafc223e8512)。

为节点的所有时钟初始化一个 `atmel_sam_pmc_config` 数组。

<a id="r_gaf27b70e3c0fa178c3096748bb636b704"></a>

```c
#define SAM_DT_INST_CLOCKS_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gaf27b70e3c0fa178c3096748bb636b704)。

对设备树实例（DT Instance）执行与 `SAM_DT_CLOCKS_PMC_CFG()` 等效的操作。


## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [zephyr/dt-bindings/clock/atmel_sam_pmc.h](../api_source_reference/P189_atmel_sam_pmc.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P149_atmel_sam_pmc.h_源码浏览.md)
- [atmel_sam_pmc_config](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md)
- [SAM_DT_PMC_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#ga90fa2e9a2226f7a2cb8926e9091b5eb3)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [SAM_DT_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gafe5b223995886a213b8e9108fdce94d5)
- [SAM_DT_INST_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#ga0f6e3f89dcfde77d27b2685220055109)
- [SAM_DT_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gadc7b9d880d6ebcf81b47eafc223e8512)
- [SAM_DT_INST_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gaf27b70e3c0fa178c3096748bb636b704)

<a id="header-details"></a>

---

[上一章](P013_zephyr__drivers__charger__npm10xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__console__console.h_文件参考.md)
