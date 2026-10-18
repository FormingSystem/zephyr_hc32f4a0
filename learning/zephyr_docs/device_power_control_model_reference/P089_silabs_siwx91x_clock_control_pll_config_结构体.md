---
id: learning.zephyr-docs.device-power-control-model-reference.page-89
title: silabs_siwx91x_clock_control_pll_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__siwx91x__clock__control__pll__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_silabs\_siwx91x\_clock\_control\_pll\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__siwx91x__clock__control__pll__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SiWx91x高性能（HP）时钟管理器的锁相环（PLL）配置。

```c
#include <zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h>
```

<a id="details"></a>

SiWx91x高性能（HP）时钟管理器的锁相环（PLL）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_ac7fa89c1dd94c0f17cc5f1de5939d89d"></a>

```c
uint32_t clkid
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clkid](#ac7fa89c1dd94c0f17cc5f1de5939d89d)。

锁相环（PLL）时钟标识符，取 `SIWX91X_CLK_PLL_*`。

<a id="r_aa474e8ff41ecd61fe1d3a99f1844d94b"></a>

```c
uint32_t ref_clkid
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ref_clkid](#aa474e8ff41ecd61fe1d3a99f1844d94b)。

PLL 参考时钟标识符。

<a id="r_a04bda8d54ed92f4103029a3a834f1ec3"></a>

```c
uint32_t frequency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frequency](#a04bda8d54ed92f4103029a3a834f1ec3)。

目标 PLL 输出频率，单位为 Hz。

## 89.2\_详细说明（Detailed Documentation）

<a id="ac7fa89c1dd94c0f17cc5f1de5939d89d"></a>

### `clkid`

```c
uint32_t silabs_siwx91x_clock_control_pll_config::clkid
```

锁相环（PLL）时钟标识符，取 `SIWX91X_CLK_PLL_*`。

<a id="a04bda8d54ed92f4103029a3a834f1ec3"></a>

### `frequency`

```c
uint32_t silabs_siwx91x_clock_control_pll_config::frequency
```

目标 PLL 输出频率，单位为 Hz。

<a id="aa474e8ff41ecd61fe1d3a99f1844d94b"></a>

### `ref_clkid`

```c
uint32_t silabs_siwx91x_clock_control_pll_config::ref_clkid
```

PLL 参考时钟标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_silabs_siwx91x.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_silabs_siwx91x_clock_control_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_st_transfer_info_结构体.md)
