---
id: learning.zephyr-docs.platform-security-model-reference.page-40
title: scmi_nxp_cpu_pd_lpm_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__pd__lpm__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_scmi\_nxp\_cpu\_pd\_lpm\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__pd__lpm__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CPU电源域（Power Domain）的低功耗模式设置。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

描述CPU电源域（Power Domain）的低功耗模式设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a44654e7633e8d5705397e994ecf44f60"></a>

```c
uint32_t cpu_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cpu_id](#a44654e7633e8d5705397e994ecf44f60)。

待配置 CPU 的 ID。

<a id="r_a49f57505c116e79ca16f848662965604"></a>

```c
uint32_t num_cfg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_cfg](#a49f57505c116e79ca16f848662965604)。

`cfgs` 中有效条目的数量。

<a id="r_ac8f0fdc610b66703baaf1e177b0ef593"></a>

```c
struct scmi_pd_lpm_settings cfgs [7U]
```

相关声明：[scmi_pd_lpm_settings](P043_scmi_pd_lpm_settings_结构体.md)、[cfgs](#ac8f0fdc610b66703baaf1e177b0ef593)。

各电源域（Power domain）的低功耗模式设置。

## 40.2\_详细说明（Detailed Documentation）

<a id="ac8f0fdc610b66703baaf1e177b0ef593"></a>

### `cfgs`

```c
struct scmi_pd_lpm_settings scmi_nxp_cpu_pd_lpm_config::cfgs[7U]
```

各电源域（Power domain）的低功耗模式设置。

<a id="a44654e7633e8d5705397e994ecf44f60"></a>

### `cpu_id`

```c
uint32_t scmi_nxp_cpu_pd_lpm_config::cpu_id
```

待配置 CPU 的 ID。

<a id="a49f57505c116e79ca16f848662965604"></a>

### `num_cfg`

```c
uint32_t scmi_nxp_cpu_pd_lpm_config::num_cfg
```

`cfgs` 中有效条目的数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_pd_lpm_settings](P043_scmi_pd_lpm_settings_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_scmi_nxp_cpu_irq_mask_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_scmi_nxp_cpu_sleep_mode_config_结构体.md)
