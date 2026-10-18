---
id: learning.zephyr-docs.device-power-control-model-reference.page-78
title: sam_clk_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsam__clk__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_sam\_clk\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsam__clk__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

<a id="details"></a>

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_a267eec7843a416198edf26c31db252e7"></a>

```c
uint32_t clock_type
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clock_type](#a267eec7843a416198edf26c31db252e7)。

时钟类型，参见 `microchip_sam_pmc.h` 设备树绑定。

<a id="r_af393258d1cf2fc592970658896075b17"></a>

```c
uint32_t clock_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clock_id](#af393258d1cf2fc592970658896075b17)。

PMC 内的外设标识符。

## 78.2\_详细说明（Detailed Documentation）

<a id="af393258d1cf2fc592970658896075b17"></a>

### `clock_id`

```c
uint32_t sam_clk_cfg::clock_id
```

PMC 内的外设标识符。

<a id="a267eec7843a416198edf26c31db252e7"></a>

### `clock_type`

```c
uint32_t sam_clk_cfg::clock_type
```

时钟类型，参见 `microchip_sam_pmc.h` 设备树绑定。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_sam_pmc.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [microchip_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_rx_irq_dig_filt_s_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_sam_pmc_cfg_结构体.md)
