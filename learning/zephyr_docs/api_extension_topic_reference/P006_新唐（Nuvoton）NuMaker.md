---
id: learning.zephyr-docs.api-extension-topic-reference.page-6
title: 新唐（Nuvoton）NuMaker
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numaker.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_新唐（Nuvoton）NuMaker

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numaker.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fnumaker_2Eh"></a>

```c
file clock_control_numaker.h
```

相关声明：[clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h.html)。

Nuvoton NuMaker设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_numaker_5Fscc_5Fsubsys_5Fpcc"></a>

```c
struct numaker_scc_subsys_pcc
```

相关声明：[numaker_scc_subsys_pcc](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md)。

外设时钟控制配置（Peripheral Clock Control Configuration）。

<a id="r_numaker_5Fscc_5Fsubsys_5Fpcc_5Frate"></a>

```c
struct numaker_scc_subsys_pcc_rate
```

相关声明：[numaker_scc_subsys_pcc_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md)。

外设时钟控制频率信息（Peripheral Clock Control Rate Information）。

<a id="r_numaker_5Fscc_5Fsubsys"></a>

```c
struct numaker_scc_subsys
```

相关声明：[numaker_scc_subsys](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md)。

NuMaker时钟子系统选择器（Clock Subsystem Selector）。

<a id="r_numaker_5Fscc_5Fsubsys_5Frate"></a>

```c
struct numaker_scc_subsys_rate
```

相关声明：[numaker_scc_subsys_rate](../device_power_control_model_reference/P052_numaker_scc_subsys_rate_结构体.md)。

NuMaker时钟子系统频率选择器（Rate Selector）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga276ba4e34017fda5c4b77f4abb82a7af"></a>

```c
#define NUMAKER_SCC_SUBSYS_ID_PCC 1
```

相关声明：[NUMAKER_SCC_SUBSYS_ID_PCC](#ga276ba4e34017fda5c4b77f4abb82a7af)。

外设时钟控制（Peripheral Clock Control，PCC）使用的 SCC 子系统标识（Subsystem ID）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.4\_振荡器／时钟切换操作（Oscillator / Clock Switch Actions）

<a id="r_ga45da36b4d2240d67426c24173c418244"></a>

```c
#define NUMAKER_SCC_CLKSW_UNTOUCHED 0
```

相关声明：[NUMAKER_SCC_CLKSW_UNTOUCHED](#ga45da36b4d2240d67426c24173c418244)。

保持时钟开关（Clock Switch）不变。

<a id="r_gadf1d45b58eba1825231c031b993562c7"></a>

```c
#define NUMAKER_SCC_CLKSW_ENABLE 1
```

相关声明：[NUMAKER_SCC_CLKSW_ENABLE](#gadf1d45b58eba1825231c031b993562c7)。

启用振荡器／时钟（Oscillator / Clock）。

<a id="r_ga35485fa37bb7eeac9d761cf5c98d5177"></a>

```c
#define NUMAKER_SCC_CLKSW_DISABLE 2
```

相关声明：[NUMAKER_SCC_CLKSW_DISABLE](#ga35485fa37bb7eeac9d761cf5c98d5177)。

禁用振荡器／时钟（Oscillator / Clock）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga35485fa37bb7eeac9d761cf5c98d5177"></a>

### `NUMAKER_SCC_CLKSW_DISABLE`

```c
#define NUMAKER_SCC_CLKSW_DISABLE 2
```

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

禁用振荡器／时钟（Oscillator / Clock）。

<a id="gadf1d45b58eba1825231c031b993562c7"></a>

### `NUMAKER_SCC_CLKSW_ENABLE`

```c
#define NUMAKER_SCC_CLKSW_ENABLE 1
```

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

启用振荡器／时钟（Oscillator / Clock）。

<a id="ga45da36b4d2240d67426c24173c418244"></a>

### `NUMAKER_SCC_CLKSW_UNTOUCHED`

```c
#define NUMAKER_SCC_CLKSW_UNTOUCHED 0
```

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

保持时钟开关（Clock Switch）不变。

<a id="ga276ba4e34017fda5c4b77f4abb82a7af"></a>

### `NUMAKER_SCC_SUBSYS_ID_PCC`

```c
#define NUMAKER_SCC_SUBSYS_ID_PCC 1
```

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

外设时钟控制（Peripheral Clock Control，PCC）使用的 SCC 子系统标识（Subsystem ID）。


## 6.6\_原页交叉引用（Cross References）

- [clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h.html)
- [numaker_scc_subsys_pcc](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md)
- [numaker_scc_subsys_pcc_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md)
- [numaker_scc_subsys](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md)
- [numaker_scc_subsys_rate](../device_power_control_model_reference/P052_numaker_scc_subsys_rate_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_瑞昱（Realtek）BEE.md) · [返回大纲](大纲.md) · [下一章](P007_瑞萨（Renesas）R-Car.md)
