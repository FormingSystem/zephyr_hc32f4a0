---
id: learning.zephyr-docs.api-extension-topic-reference.page-7
title: 瑞萨（Renesas）R-Car
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_瑞萨（Renesas）R-Car

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_renesas_5Frcar_5Fgeneric_2Eh"></a>

```c
file renesas_rcar_generic.h
```

相关声明：[renesas_rcar_generic.h](../api_file_runtime_reference/P055_zephyr__drivers__clock_control__renesas_rcar_generic.h_文件参考.md)。

Renesas R-Car对时钟的通用访问（Generic Access）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga60d34a7c9572916766526b4c25433107"></a>

```c
#define RCAR_DT_INST_CLOCKS_CELL_BY_IDX(inst, idx)
```

相关声明：[RCAR_DT_INST_CLOCKS_CELL_BY_IDX](#ga60d34a7c9572916766526b4c25433107)。

与 `DT_INST_CLOCKS_CELL_BY_IDX` 类似的辅助宏（Helper）。

<a id="r_ga1148b59c97dbd4753c0d4fa8284b560f"></a>

```c
#define RCAR_CLOCK_SUBSYS(clk)
```

相关声明：[RCAR_CLOCK_SUBSYS](#ga1148b59c97dbd4753c0d4fa8284b560f)。

获取对特定时钟（Specific Clock）的访问。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_gab6254d94158b3eed9aebe694180731ee"></a>

```c
typedef struct rcar_cpg_clk rcar_generic_clk_t
```

相关声明：[rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)、[rcar_generic_clk_t](#gab6254d94158b3eed9aebe694180731ee)。

抽象实现所使用的时钟类型（Clock Type）。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga1148b59c97dbd4753c0d4fa8284b560f"></a>

### `RCAR_CLOCK_SUBSYS`

```c
#define RCAR_CLOCK_SUBSYS ( clk)
```

```c
#include <zephyr/drivers/clock_control/renesas_rcar_generic.h>
```

展开值（Value）：

```c
(clock_control_subsys_t)&(clk)
```

获取对特定时钟（Specific Clock）的访问。

获取时钟数据（Clock Data）的方式取决于平台（Platform）。

<a id="ga60d34a7c9572916766526b4c25433107"></a>

### `RCAR_DT_INST_CLOCKS_CELL_BY_IDX`

```c
#define RCAR_DT_INST_CLOCKS_CELL_BY_IDX ( inst, idx )
```

```c
#include <zephyr/drivers/clock_control/renesas_rcar_generic.h>
```

展开值（Value）：

```c
{                                                                       \
        .module = DT_INST_CLOCKS_CELL_BY_IDX(inst, idx, module),        \
        .domain = DT_INST_CLOCKS_CELL_BY_IDX(inst, idx, domain)         \
}
```

与 `DT_INST_CLOCKS_CELL_BY_IDX` 类似的辅助宏（Helper）。

根据目标平台（Target Platform）自动加载正确的时钟设置（Clock Settings）。用法与 `DT_INST_CLOCKS_CELL_BY_IDX` 相同。

<a id="gab6254d94158b3eed9aebe694180731ee"></a>

### `rcar_generic_clk_t`

```c
typedef struct rcar_cpg_clk rcar_generic_clk_t
```

```c
#include <zephyr/drivers/clock_control/renesas_rcar_generic.h>
```

抽象实现所使用的时钟类型（Clock Type）。


## 7.5\_原页交叉引用（Cross References）

- [renesas_rcar_generic.h](../api_file_runtime_reference/P055_zephyr__drivers__clock_control__renesas_rcar_generic.h_文件参考.md)
- [rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)
- [clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)
- [DT_INST_CLOCKS_CELL_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga5bee2e489f0818f0f2d1ec6d195bd3a8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__control__interface_html_gaa7d3935eaaf18902801a7d94859483db"></a>
<a id="agroup__devicetree-clocks_html_ga5bee2e489f0818f0f2d1ec6d195bd3a8"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P006_新唐（Nuvoton）NuMaker.md) · [返回大纲](大纲.md) · [下一章](P008_树莓派 Pico（Raspberry Pi Pico）.md)
