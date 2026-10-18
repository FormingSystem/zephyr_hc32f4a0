---
id: learning.zephyr-docs.platform-security-model-reference.page-41
title: scmi_nxp_cpu_sleep_mode_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__sleep__mode__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_scmi\_nxp\_cpu\_sleep\_mode\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__sleep__mode__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CPU_STATE_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

描述CPU_STATE_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a016a162f5af8523cd84926f1355f62e8"></a>

```c
uint32_t cpu_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cpu_id](#a016a162f5af8523cd84926f1355f62e8)。

待配置 CPU 的 ID。

<a id="r_a24d167a783d564a2639332437c15ce21"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a24d167a783d564a2639332437c15ce21)。

睡眠标志，参见 `SCMI_NXP_CPU_SLEEP_FLAG_*`。

<a id="r_a2f34473f39d718c29209e10e4c45b14b"></a>

```c
uint32_t sleep_mode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sleep_mode](#a2f34473f39d718c29209e10e4c45b14b)。

要进入的睡眠模式。

## 41.2\_详细说明（Detailed Documentation）

<a id="a016a162f5af8523cd84926f1355f62e8"></a>

### `cpu_id`

```c
uint32_t scmi_nxp_cpu_sleep_mode_config::cpu_id
```

待配置 CPU 的 ID。

<a id="a24d167a783d564a2639332437c15ce21"></a>

### `flags`

```c
uint32_t scmi_nxp_cpu_sleep_mode_config::flags
```

睡眠标志，参见 `SCMI_NXP_CPU_SLEEP_FLAG_*`。

<a id="a2f34473f39d718c29209e10e4c45b14b"></a>

### `sleep_mode`

```c
uint32_t scmi_nxp_cpu_sleep_mode_config::sleep_mode
```

要进入的睡眠模式。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_scmi_nxp_cpu_pd_lpm_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_scmi_nxp_cpu_vector_config_结构体.md)
