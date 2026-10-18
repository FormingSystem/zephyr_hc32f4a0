---
id: learning.zephyr-docs.platform-security-model-reference.page-42
title: scmi_nxp_cpu_vector_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__vector__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_scmi\_nxp\_cpu\_vector\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__vector__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CPU_RESET_VECTOR_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

描述CPU_RESET_VECTOR_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a4583b0c5ff44c994c612765b8b91edcc"></a>

```c
uint32_t cpu_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cpu_id](#a4583b0c5ff44c994c612765b8b91edcc)。

待配置 CPU 的 ID。

<a id="r_a02ce732308b9861367bf22be4bebe8fa"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a02ce732308b9861367bf22be4bebe8fa)。

向量标志，参见 `SCMI_NXP_CPU_VEC_FLAGS_*`。

<a id="r_a5d5d72d7ca43ac41a112822578fa3135"></a>

```c
uint32_t vector_low
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vector_low](#a5d5d72d7ca43ac41a112822578fa3135)。

复位向量地址的低 32 位。

<a id="r_a6ca9bb699b63aec9a15f3259173a07a9"></a>

```c
uint32_t vector_high
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vector_high](#a6ca9bb699b63aec9a15f3259173a07a9)。

复位向量地址的高 32 位。

## 42.2\_详细说明（Detailed Documentation）

<a id="a4583b0c5ff44c994c612765b8b91edcc"></a>

### `cpu_id`

```c
uint32_t scmi_nxp_cpu_vector_config::cpu_id
```

待配置 CPU 的 ID。

<a id="a02ce732308b9861367bf22be4bebe8fa"></a>

### `flags`

```c
uint32_t scmi_nxp_cpu_vector_config::flags
```

向量标志，参见 `SCMI_NXP_CPU_VEC_FLAGS_*`。

<a id="a6ca9bb699b63aec9a15f3259173a07a9"></a>

### `vector_high`

```c
uint32_t scmi_nxp_cpu_vector_config::vector_high
```

复位向量地址的高 32 位。

<a id="a5d5d72d7ca43ac41a112822578fa3135"></a>

### `vector_low`

```c
uint32_t scmi_nxp_cpu_vector_config::vector_low
```

复位向量地址的低 32 位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_scmi_nxp_cpu_sleep_mode_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_scmi_pd_lpm_settings_结构体.md)
