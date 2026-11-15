---
id: learning.zephyr-docs.api-service-topic-reference.page-4
title: 微芯（Microchip）SAM 电源管理控制器（PMC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_微芯（Microchip）SAM 电源管理控制器（PMC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_mchp_5Fsam_5Fpmc_2Eh"></a>

```c
file mchp_sam_pmc.h
```

相关声明：[mchp_sam_pmc.h](../api_file_service_reference/P020_zephyr__drivers__clock_control__mchp_sam_pmc.h_文件参考.md)。

Microchip SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

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

## 4.3\_宏定义（Macros）

<a id="r_gae6ab16601edc5287a1657ff7bb1c8dbd"></a>

```c
#define SAM_DT_CLOCK_PMC_CFG(clock, node_id)
```

相关声明：[SAM_DT_CLOCK_PMC_CFG](#gae6ab16601edc5287a1657ff7bb1c8dbd)。

根据时钟说明符（Clock Specifier）初始化 `sam_clk_cfg`。

<a id="r_ga0f6e3f89dcfde77d27b2685220055109"></a>

```c
#define SAM_DT_INST_CLOCK_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCK_PMC_CFG](#ga0f6e3f89dcfde77d27b2685220055109)。

对设备树实例（DT Instance）的第一个时钟，执行与 `SAM_DT_CLOCK_PMC_CFG()` 等效的操作。

<a id="r_gadc7b9d880d6ebcf81b47eafc223e8512"></a>

```c
#define SAM_DT_CLOCKS_PMC_CFG(node_id)
```

相关声明：[SAM_DT_CLOCKS_PMC_CFG](#gadc7b9d880d6ebcf81b47eafc223e8512)。

为一个节点（Node）的所有时钟初始化 `sam_clk_cfg` 数组（Array）。

<a id="r_gaf27b70e3c0fa178c3096748bb636b704"></a>

```c
#define SAM_DT_INST_CLOCKS_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCKS_PMC_CFG](#gaf27b70e3c0fa178c3096748bb636b704)。

对设备树实例（DT Instance）执行与 `SAM_DT_CLOCKS_PMC_CFG()` 等效的操作。

## 4.4\_详细说明（Detailed Documentation）

<a id="gae6ab16601edc5287a1657ff7bb1c8dbd"></a>

### `SAM_DT_CLOCK_PMC_CFG`

```c
#define SAM_DT_CLOCK_PMC_CFG ( clock, node_id )
```

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

展开值（Value）：

```c
        {                                               \
        .clock_type = DT_CLOCKS_CELL_BY_IDX(node_id,                            \
                                            clock,                              \
                                            clock_type),                        \
        .clock_id = DT_CLOCKS_CELL_BY_IDX(node_id,                              \
                                          clock,                                \
                                          peripheral_id)                        \
}
```

根据时钟说明符（Clock Specifier）初始化 `sam_clk_cfg`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clock` | 时钟说明符（Clock Specifier）在节点 `clocks` 属性中的索引（Index）。 |
| `node_id` | 拥有 `clocks` 属性的设备树节点标识（Devicetree Node Identifier）。 |

<a id="gadc7b9d880d6ebcf81b47eafc223e8512"></a>

### `SAM_DT_CLOCKS_PMC_CFG`

```c
#define SAM_DT_CLOCKS_PMC_CFG ( node_id)
```

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

展开值（Value）：

```c
        {                                               \
        LISTIFY(DT_NUM_CLOCKS(node_id),                                         \
        SAM_DT_CLOCK_PMC_CFG, (,), node_id)                                     \
}
```

为一个节点（Node）的所有时钟初始化 `sam_clk_cfg` 数组（Array）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 拥有 `clocks` 属性的设备树节点标识（Devicetree Node Identifier）。 |

<a id="ga0f6e3f89dcfde77d27b2685220055109"></a>

### `SAM_DT_INST_CLOCK_PMC_CFG`

```c
#define SAM_DT_INST_CLOCK_PMC_CFG ( inst)
```

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

展开值（Value）：

```c
SAM_DT_CLOCK_PMC_CFG(0, DT_DRV_INST(inst))
```

对设备树实例（DT Instance）的第一个时钟，执行与 `SAM_DT_CLOCK_PMC_CFG()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |

<a id="gaf27b70e3c0fa178c3096748bb636b704"></a>

### `SAM_DT_INST_CLOCKS_PMC_CFG`

```c
#define SAM_DT_INST_CLOCKS_PMC_CFG ( inst)
```

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

展开值（Value）：

```c
SAM_DT_CLOCKS_PMC_CFG(DT_DRV_INST(inst))
```

对设备树实例（DT Instance）执行与 `SAM_DT_CLOCKS_PMC_CFG()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |


## 4.5\_原页交叉引用（Cross References）

- [mchp_sam_pmc.h](../api_file_service_reference/P020_zephyr__drivers__clock_control__mchp_sam_pmc.h_文件参考.md)
- [sam_sckc_config](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md)
- [sam_clk_cfg](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md)
- [sam_pmc_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md)
- [sam_pmc_data](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md)
- [DT_CLOCKS_CELL_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga7db765e869b8455a6c56a8f22a7cc5c8)
- [DT_NUM_CLOCKS](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga22d4e8621b5bf56ed0ac8295dd11d7e3)
- [SAM_DT_CLOCK_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gafe5b223995886a213b8e9108fdce94d5)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [SAM_DT_CLOCKS_PMC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html#gadc7b9d880d6ebcf81b47eafc223e8512)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-clocks_html_ga7db765e869b8455a6c56a8f22a7cc5c8"></a>
<a id="agroup__clock__control__atmel__sam__pmc_html_gafe5b223995886a213b8e9108fdce94d5"></a>
<a id="agroup__devicetree-clocks_html_ga22d4e8621b5bf56ed0ac8295dd11d7e3"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__clock__control__atmel__sam__pmc_html_gadc7b9d880d6ebcf81b47eafc223e8512"></a>

---

[上一章](P003_心跳（Heartbeat）.md) · [返回大纲](大纲.md) · [下一章](P005_芯科科技（Silicon Labs）.md)
