---
id: learning.zephyr-docs.platform-security-model-reference.page-38
title: scmi_nxp_cpu_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_scmi\_nxp\_cpu\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CPU_INFO_GET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

描述CPU_INFO_GET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a9e8ef984d7613ef2893cd0fe42dc750b"></a>

```c
uint32_t run_mode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[run_mode](#a9e8ef984d7613ef2893cd0fe42dc750b)。

CPU 当前的运行模式（Run mode）。

<a id="r_a53cab503c7619e68a5a7b6ddc71bcad8"></a>

```c
uint32_t sleep_mode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sleep_mode](#a53cab503c7619e68a5a7b6ddc71bcad8)。

CPU 当前的睡眠模式（Sleep mode）。

<a id="r_a7642f805dd7a70bfc216c1526c3e3e7d"></a>

```c
uint32_t vector_low
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vector_low](#a7642f805dd7a70bfc216c1526c3e3e7d)。

CPU 复位向量（Reset vector）地址的低 32 位。

<a id="r_ab817f075da09dea4359ae39a351fc966"></a>

```c
uint32_t vector_high
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vector_high](#ab817f075da09dea4359ae39a351fc966)。

CPU 复位向量地址的高 32 位。

## 38.2\_详细说明（Detailed Documentation）

<a id="a9e8ef984d7613ef2893cd0fe42dc750b"></a>

### `run_mode`

```c
uint32_t scmi_nxp_cpu_info::run_mode
```

CPU 当前的运行模式（Run mode）。

<a id="a53cab503c7619e68a5a7b6ddc71bcad8"></a>

### `sleep_mode`

```c
uint32_t scmi_nxp_cpu_info::sleep_mode
```

CPU 当前的睡眠模式（Sleep mode）。

<a id="ab817f075da09dea4359ae39a351fc966"></a>

### `vector_high`

```c
uint32_t scmi_nxp_cpu_info::vector_high
```

CPU 复位向量地址的高 32 位。

<a id="a7642f805dd7a70bfc216c1526c3e3e7d"></a>

### `vector_low`

```c
uint32_t scmi_nxp_cpu_info::vector_low
```

CPU 复位向量（Reset vector）地址的低 32 位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_scmi_message_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_scmi_nxp_cpu_irq_mask_config_结构体.md)
