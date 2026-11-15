---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-6
title: clock_control_rx_root_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__root__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_clock\_control\_rx\_root\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__root__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

根时钟配置（Root Clock Configuration）。

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

<a id="details"></a>

根时钟配置（Root Clock Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a3c551c54867d14793fc67b1321f93a92"></a>

```c
uint32_t rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rate](#a3c551c54867d14793fc67b1321f93a92)。

目标时钟频率，单位为 Hz。

## 6.2\_详细说明（Detailed Documentation）

<a id="a3c551c54867d14793fc67b1321f93a92"></a>

### `rate`

```c
uint32_t clock_control_rx_root_cfg::rate
```

目标时钟频率，单位为 Hz。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_rx_cgc.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_rx_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_clock_control_rx_pll_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_clock_control_rx_subsys_cfg_结构体.md)
