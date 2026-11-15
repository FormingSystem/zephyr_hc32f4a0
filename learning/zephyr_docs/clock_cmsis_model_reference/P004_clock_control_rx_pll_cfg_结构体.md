---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-4
title: clock_control_rx_pll_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__pll__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_clock\_control\_rx\_pll\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__pll__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

锁相环（Phase-Locked Loop，PLL）配置结构体。

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

<a id="details"></a>

锁相环（Phase-Locked Loop，PLL）配置结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a06f3394bdaadb0f06cce23cd90c95061"></a>

```c
const struct device * clock_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[clock_dev](#a06f3394bdaadb0f06cce23cd90c95061)。

提供 PLL 时钟源的设备。

## 4.2\_详细说明（Detailed Documentation）

<a id="a06f3394bdaadb0f06cce23cd90c95061"></a>

### `clock_dev`

```c
const struct device* clock_control_rx_pll_cfg::clock_dev
```

提供 PLL 时钟源的设备。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_rx_cgc.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_rx_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_clock_control_rx_pclk_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_clock_control_rx_pll_data_结构体.md)
