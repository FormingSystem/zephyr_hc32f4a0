---
id: learning.zephyr-docs.device-power-control-model-reference.page-87
title: silabs_clock_control_cmu_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__clock__control__cmu__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_silabs\_clock\_control\_cmu\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsilabs__clock__control__cmu__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设的时钟管理单元（Clock Management Unit，CMU）时钟配置。

```c
#include <zephyr/drivers/clock_control/clock_control_silabs.h>
```

<a id="details"></a>

外设的时钟管理单元（Clock Management Unit，CMU）时钟配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_a5792da0cf4363d3127cff97562763f45"></a>

```c
uint32_t bus_clock
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bus_clock](#a5792da0cf4363d3127cff97562763f45)。

总线时钟使能标识符。

<a id="r_a8e9a65a261eae1fefcf0d697a8a59bf9"></a>

```c
uint8_t branch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[branch](#a8e9a65a261eae1fefcf0d697a8a59bf9)。

外设时钟所来自的时钟分支（Clock branch）。

## 87.2\_详细说明（Detailed Documentation）

<a id="a8e9a65a261eae1fefcf0d697a8a59bf9"></a>

### `branch`

```c
uint8_t silabs_clock_control_cmu_config::branch
```

外设时钟所来自的时钟分支（Clock branch）。

<a id="a5792da0cf4363d3127cff97562763f45"></a>

### `bus_clock`

```c
uint32_t silabs_clock_control_cmu_config::bus_clock
```

总线时钟使能标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_silabs.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_silabs.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_sf32lb_dma_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_silabs_siwx91x_clock_control_config_结构体.md)
