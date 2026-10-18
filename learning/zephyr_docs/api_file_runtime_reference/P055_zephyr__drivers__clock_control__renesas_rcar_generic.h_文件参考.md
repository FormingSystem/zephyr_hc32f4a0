---
id: learning.zephyr-docs.api-file-runtime-reference.page-55
title: zephyr__drivers__clock_control__renesas_rcar_generic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_drivers\_\_clock\_control\_\_renesas\_rcar\_generic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas R-Car对时钟的通用访问（Generic Access）。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control/renesas_cpg_mssr.h>
```

查看此文件的源码。

Renesas R-Car对时钟的通用访问（Generic Access）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 55.1\_宏定义（Macros）

<a id="r_ga60d34a7c9572916766526b4c25433107"></a>

```c
#define RCAR_DT_INST_CLOCKS_CELL_BY_IDX(inst, idx)
```

相关声明：[RCAR_DT_INST_CLOCKS_CELL_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#ga60d34a7c9572916766526b4c25433107)。

与 `DT_INST_CLOCKS_CELL_BY_IDX` 类似的辅助宏（Helper）。

<a id="r_ga1148b59c97dbd4753c0d4fa8284b560f"></a>

```c
#define RCAR_CLOCK_SUBSYS(clk)
```

相关声明：[RCAR_CLOCK_SUBSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#ga1148b59c97dbd4753c0d4fa8284b560f)。

获取对特定时钟（Specific Clock）的访问。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 55.2\_类型定义（Typedefs）

<a id="r_gab6254d94158b3eed9aebe694180731ee"></a>

```c
typedef struct rcar_cpg_clk rcar_generic_clk_t
```

相关声明：[rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)、[rcar_generic_clk_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#gab6254d94158b3eed9aebe694180731ee)。

抽象实现所使用的时钟类型（Clock Type）。


## 55.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_cpg_mssr.h](../api_source_reference/P150_renesas_cpg_mssr.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P095_renesas_rcar_generic.h_源码浏览.md)
- [RCAR_DT_INST_CLOCKS_CELL_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#ga60d34a7c9572916766526b4c25433107)
- [RCAR_CLOCK_SUBSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#ga1148b59c97dbd4753c0d4fa8284b560f)
- [rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)
- [rcar_generic_clk_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#gab6254d94158b3eed9aebe694180731ee)

<a id="header-details"></a>

---

[上一章](P054_zephyr__dt-bindings__gpio__renesas-rzt2m-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__dt-bindings__clock__renesas_rzg_clock.h_文件参考.md)
