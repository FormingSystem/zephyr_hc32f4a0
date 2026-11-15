---
id: learning.zephyr-docs.device-power-control-model-reference.page-43
title: mspm0_sys_clock_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspm0__sys__clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_mspm0\_sys\_clock\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspm0__sys__clock.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPM0系统时钟子系统选择器（Subsystem Selector）。

```c
#include <zephyr/drivers/clock_control/mspm0_clock_control.h>
```

<a id="details"></a>

MSPM0系统时钟子系统选择器（Subsystem Selector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_ac48292bef828c08f7da17a376e491c79"></a>

```c
uint32_t clk
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk](#ac48292bef828c08f7da17a376e491c79)。

时钟标识符，参见 `mspm0_clock.h` 设备树（DT）绑定。

## 43.2\_详细说明（Detailed Documentation）

<a id="ac48292bef828c08f7da17a376e491c79"></a>

### `clk`

```c
uint32_t mspm0_sys_clock::clk
```

时钟标识符，参见 `mspm0_clock.h` 设备树（DT）绑定。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mspm0_clock_control.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mspm0_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mspm0_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_msosv2_vendor_revision_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_npcx_ex_ops_gdma_in_结构体.md)
