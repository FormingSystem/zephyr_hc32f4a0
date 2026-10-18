---
id: learning.zephyr-docs.device-power-control-model-reference.page-85
title: sf32lb_clock_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsf32lb__clock__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_sf32lb\_clock\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsf32lb__clock__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SF32LB时钟的设备树规格（Clock DT Spec）。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

<a id="details"></a>

SF32LB时钟的设备树规格（Clock DT Spec）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_af16b29caf2839be48eb2da372177a614"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#af16b29caf2839be48eb2da372177a614)。

复位与时钟控制器（RCC）。

<a id="r_a42c0ab2e23e96efad24e27c7d490818f"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a42c0ab2e23e96efad24e27c7d490818f)。

时钟 ID。

## 85.2\_详细说明（Detailed Documentation）

<a id="af16b29caf2839be48eb2da372177a614"></a>

### `dev`

```c
const struct device* sf32lb_clock_dt_spec::dev
```

复位与时钟控制器（RCC）。

<a id="a42c0ab2e23e96efad24e27c7d490818f"></a>

### `id`

```c
uint16_t sf32lb_clock_dt_spec::id
```

时钟 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/sf32lb.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/sf32lb.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control_2sf32lb_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_sbs_gauge_manufacturer_name_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_sf32lb_dma_dt_spec_结构体.md)
