---
id: learning.zephyr-docs.api-protocol-topic-reference.page-10
title: Atmel SAM 电源管理控制器（PMC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Atmel SAM 电源管理控制器（PMC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_atmel_5Fsam_5Fpmc_2Eh"></a>

```c
file atmel_sam_pmc.h
```

相关声明：[atmel_sam_pmc.h](../api_file_interface_reference/P014_zephyr__drivers__clock_control__atmel_sam_pmc.h_文件参考.md)。

Atmel SAM设备的电源管理控制器（Power Management Controller，PMC）时钟辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_atmel_5Fsam_5Fpmc_5Fconfig"></a>

```c
struct atmel_sam_pmc_config
```

相关声明：[atmel_sam_pmc_config](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md)。

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.3\_宏定义（Macros）

<a id="r_ga90fa2e9a2226f7a2cb8926e9091b5eb3"></a>

```c
#define SAM_DT_PMC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(pmc))
```

相关声明：[SAM_DT_PMC_CONTROLLER](#ga90fa2e9a2226f7a2cb8926e9091b5eb3)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

指向 PMC 时钟控制器（clock controller）的设备指针。

<a id="r_gafe5b223995886a213b8e9108fdce94d5"></a>

```c
#define SAM_DT_CLOCK_PMC_CFG(clock_id, node_id)
```

相关声明：[SAM_DT_CLOCK_PMC_CFG](#gafe5b223995886a213b8e9108fdce94d5)。

使用时钟描述符（clock specifier）初始化一个 `atmel_sam_pmc_config`。

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

为节点的所有时钟初始化一个 `atmel_sam_pmc_config` 数组。

<a id="r_gaf27b70e3c0fa178c3096748bb636b704"></a>

```c
#define SAM_DT_INST_CLOCKS_PMC_CFG(inst)
```

相关声明：[SAM_DT_INST_CLOCKS_PMC_CFG](#gaf27b70e3c0fa178c3096748bb636b704)。

对设备树实例（DT Instance）执行与 `SAM_DT_CLOCKS_PMC_CFG()` 等效的操作。

## 10.4\_详细说明（Detailed Documentation）

<a id="gafe5b223995886a213b8e9108fdce94d5"></a>

### `SAM_DT_CLOCK_PMC_CFG`

```c
#define SAM_DT_CLOCK_PMC_CFG ( clock_id, node_id )
```

```c
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
```

展开值（Value）：

```c
{                                                                       \
.clock_type = DT_CLOCKS_CELL_BY_IDX(node_id, clock_id, clock_type),     \
.peripheral_id = DT_CLOCKS_CELL_BY_IDX(node_id, clock_id, peripheral_id)\
}
```

使用时钟描述符（clock specifier）初始化一个 `atmel_sam_pmc_config`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clock_id` | 时钟说明符（Clock Specifier）在节点 `clocks` 属性中的索引（Index）。 |
| `node_id` | 拥有 `clocks` 属性的设备树节点标识（Devicetree Node Identifier）。 |

<a id="gadc7b9d880d6ebcf81b47eafc223e8512"></a>

### `SAM_DT_CLOCKS_PMC_CFG`

```c
#define SAM_DT_CLOCKS_PMC_CFG ( node_id)
```

```c
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
```

展开值（Value）：

```c
{                                                                       \
        LISTIFY(DT_NUM_CLOCKS(node_id),                                 \
                SAM_DT_CLOCK_PMC_CFG, (,), node_id)                     \
}
```

为节点的所有时钟初始化一个 `atmel_sam_pmc_config` 数组。

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
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
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
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
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

<a id="ga90fa2e9a2226f7a2cb8926e9091b5eb3"></a>

### `SAM_DT_PMC_CONTROLLER`

```c
#define SAM_DT_PMC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(pmc))
```

```c
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
```

指向 PMC 时钟控制器（clock controller）的设备指针。


## 10.5\_原页交叉引用（Cross References）

- [atmel_sam_pmc.h](../api_file_interface_reference/P014_zephyr__drivers__clock_control__atmel_sam_pmc.h_文件参考.md)
- [atmel_sam_pmc_config](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_CLOCKS_CELL_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga7db765e869b8455a6c56a8f22a7cc5c8)
- [DT_NUM_CLOCKS](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga22d4e8621b5bf56ed0ac8295dd11d7e3)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-clocks_html_ga7db765e869b8455a6c56a8f22a7cc5c8"></a>
<a id="agroup__clock__control__atmel__sam__pmc_html_gafe5b223995886a213b8e9108fdce94d5"></a>
<a id="agroup__devicetree-clocks_html_ga22d4e8621b5bf56ed0ac8295dd11d7e3"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__clock__control__atmel__sam__pmc_html_gadc7b9d880d6ebcf81b47eafc223e8512"></a>

---

[上一章](P009_ARM CMSDK API主题.md) · [返回大纲](大纲.md) · [下一章](P011_乐鑫（Espressif）ESP32.md)
