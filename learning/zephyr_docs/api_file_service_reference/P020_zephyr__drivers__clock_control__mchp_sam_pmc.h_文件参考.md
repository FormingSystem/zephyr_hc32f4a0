---
id: learning.zephyr-docs.api-file-service-reference.page-20
title: zephyr__drivers__clock_control__mchp_sam_pmc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_drivers\_\_clock\_control\_\_mchp\_sam\_pmc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="details"></a>

```c
#include <soc.h>
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/microchip_sam_pmc.h>
```

查看此文件的源码。

Microchip SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_sam_5Fsckc_5Fconfig"></a>

```c
struct sam_sckc_config
```

相关声明：[sam_sckc_config](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md)。

慢时钟控制器（Slow Clock Controller，SCKC）的配置。

<a id="r_sam_5Fclk_5Fcfg"></a>

```c
struct sam_clk_cfg
```

相关声明：[sam_clk_cfg](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md)。

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

<a id="r_sam_5Fpmc_5Fcfg"></a>

```c
struct sam_pmc_cfg
```

相关声明：[sam_pmc_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md)。

电源管理控制器（PMC）设备的恒定配置参数。

<a id="r_sam_5Fpmc_5Fdata"></a>

```c
struct sam_pmc_data
```

相关声明：[sam_pmc_data](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md)。

电源管理控制器（PMC）设备的运行时数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_gae6ab16601edc5287a1657ff7bb1c8dbd"></a>

```c
#define SAM_DT_CLOCK_PMC_CFG(clock, node_id)
```

相关声明：[SAM_DT_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gae6ab16601edc5287a1657ff7bb1c8dbd)。

根据时钟说明符（Clock Specifier）初始化 `sam_clk_cfg`。

<a id="r_ga0f6e3f89dcfde77d27b2685220055109"></a>

```c
#define SAM_DT_INST_CLOCK_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#ga0f6e3f89dcfde77d27b2685220055109)。

对设备树实例（DT Instance）的第一个时钟，执行与 `SAM_DT_CLOCK_PMC_CFG()` 等效的操作。

<a id="r_gadc7b9d880d6ebcf81b47eafc223e8512"></a>

```c
#define SAM_DT_CLOCKS_PMC_CFG(node_id)
```

相关声明：[SAM_DT_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gadc7b9d880d6ebcf81b47eafc223e8512)。

为一个节点（Node）的所有时钟初始化 `sam_clk_cfg` 数组（Array）。

<a id="r_gaf27b70e3c0fa178c3096748bb636b704"></a>

```c
#define SAM_DT_INST_CLOCKS_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gaf27b70e3c0fa178c3096748bb636b704)。

对设备树实例（DT Instance）执行与 `SAM_DT_CLOCKS_PMC_CFG()` 等效的操作。


## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [zephyr/dt-bindings/clock/microchip_sam_pmc.h](../api_source_configuration_reference/P056_microchip_sam_pmc.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P505_mchp_sam_pmc.h_源码浏览.md)
- [sam_sckc_config](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md)
- [sam_clk_cfg](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md)
- [sam_pmc_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md)
- [sam_pmc_data](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md)
- [SAM_DT_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gae6ab16601edc5287a1657ff7bb1c8dbd)
- [SAM_DT_INST_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#ga0f6e3f89dcfde77d27b2685220055109)
- [SAM_DT_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gadc7b9d880d6ebcf81b47eafc223e8512)
- [SAM_DT_INST_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html#gaf27b70e3c0fa178c3096748bb636b704)

<a id="header-details"></a>

---

[上一章](P019_zephyr__dt-bindings__gpio__ite-it8xxx2-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__mfd__mfd_maxq10xx.h_文件参考.md)
