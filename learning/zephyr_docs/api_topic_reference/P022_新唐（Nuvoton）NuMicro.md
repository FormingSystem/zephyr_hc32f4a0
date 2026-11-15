---
id: learning.zephyr-docs.api-topic-reference.page-22
title: 新唐（Nuvoton）NuMicro
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_新唐（Nuvoton）NuMicro

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 22.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fnumicro_2Eh"></a>

```c
file clock_control_numicro.h
```

相关声明：[clock_control_numicro.h](../api_file_runtime_reference/P006_zephyr__drivers__clock_control__clock_control_numicro.h_文件参考.md)。

Nuvoton NuMicro系列的时钟控制（Clock Control）头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 22.2\_数据结构（Data Structures）

<a id="r_numicro_5Fscc_5Fsubsys_5Fpcc"></a>

```c
struct numicro_scc_subsys_pcc
```

相关声明：[numicro_scc_subsys_pcc](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md)。

外设时钟控制（Peripheral Clock Control）的配置结构。

<a id="r_numicro_5Fscc_5Fsubsys"></a>

```c
struct numicro_scc_subsys
```

相关声明：[numicro_scc_subsys](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md)。

Numicro外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.3\_宏定义（Macros）

<a id="r_gafc2d65af18944d55ab57cc75b281aa99"></a>

```c
#define NUMICRO_SCC_SUBSYS_ID_PCC 1
```

相关声明：[NUMICRO_SCC_SUBSYS_ID_PCC](#gafc2d65af18944d55ab57cc75b281aa99)。

外设时钟控制（Peripheral Clock Control，PCC）使用的 SCC 子系统标识（Subsystem ID）。

<a id="r_ga07e3998b15407f2724b1902825ea84a4"></a>

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM(dev)
```

相关声明：[DT_NUMICRO_CLOCK_PCC_SUBSYSTEM](#ga07e3998b15407f2724b1902825ea84a4)。

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="r_ga67a68984d536fcb9c7f00d6c6eed6b9e"></a>

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST(inst)
```

相关声明：[DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST](#ga67a68984d536fcb9c7f00d6c6eed6b9e)。

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

## 22.4\_详细说明（Detailed Documentation）

<a id="ga07e3998b15407f2724b1902825ea84a4"></a>

### `DT_NUMICRO_CLOCK_PCC_SUBSYSTEM`

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM ( dev)
```

```c
#include <zephyr/drivers/clock_control/clock_control_numicro.h>
```

展开值（Value）：

```c
{                                                                                          \
        .subsys_id = NUMICRO_SCC_SUBSYS_ID_PCC,                                            \
        .pcc =                                                                             \
                {                                                                          \
                        .clk_mod = DT_CLOCKS_CELL(dev, clock_module_index),                \
                        .clk_src = DT_CLOCKS_CELL(dev, clock_source),                      \
                        .clk_div = DT_CLOCKS_CELL(dev, clock_divider),                     \
                },                                                                         \
}
```

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="ga67a68984d536fcb9c7f00d6c6eed6b9e"></a>

### `DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST`

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST ( inst)
```

```c
#include <zephyr/drivers/clock_control/clock_control_numicro.h>
```

展开值（Value）：

```c
DT_NUMICRO_CLOCK_PCC_SUBSYSTEM(DT_DRV_INST(inst))
```

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="gafc2d65af18944d55ab57cc75b281aa99"></a>

### `NUMICRO_SCC_SUBSYS_ID_PCC`

```c
#define NUMICRO_SCC_SUBSYS_ID_PCC 1
```

```c
#include <zephyr/drivers/clock_control/clock_control_numicro.h>
```

外设时钟控制（Peripheral Clock Control，PCC）使用的 SCC 子系统标识（Subsystem ID）。


## 22.5\_原页交叉引用（Cross References）

- [clock_control_numicro.h](../api_file_runtime_reference/P006_zephyr__drivers__clock_control__clock_control_numicro.h_文件参考.md)
- [numicro_scc_subsys_pcc](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md)
- [numicro_scc_subsys](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md)
- [DT_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga211bc385cbbb1d8b8fa52e2e0a52d23d)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__control__numicro_html_gafc2d65af18944d55ab57cc75b281aa99"></a>
<a id="agroup__devicetree-clocks_html_ga211bc385cbbb1d8b8fa52e2e0a52d23d"></a>
<a id="agroup__clock__control__numicro_html_ga07e3998b15407f2724b1902825ea84a4"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>

---

[上一章](P021_微芯（Microchip）XEC.md) · [返回大纲](大纲.md) · [下一章](P023_恩智浦（NXP）.md)
