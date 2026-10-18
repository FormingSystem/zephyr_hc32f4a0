---
id: learning.zephyr-docs.platform-security-model-reference.page-43
title: scmi_pd_lpm_settings_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__pd__lpm__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_scmi\_pd\_lpm\_settings\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__pd__lpm__settings.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单个电源域（Power Domain）的低功耗模式设置。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

单个电源域（Power Domain）的低功耗模式设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_ae3614c23f92717999d2058ef8636fe7c"></a>

```c
uint32_t domain_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[domain_id](#ae3614c23f92717999d2058ef8636fe7c)。

电源域的 ID。

<a id="r_a35c3e1f1f5ab7339b6ae736fb3dcde31"></a>

```c
uint32_t lpm_setting
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[lpm_setting](#a35c3e1f1f5ab7339b6ae736fb3dcde31)。

该电源域的低功耗模式设置。

<a id="r_a18de2ecf5f1d072967eacf7375d9e64c"></a>

```c
uint32_t ret_mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ret_mask](#a18de2ecf5f1d072967eacf7375d9e64c)。

在低功耗模式下应用的保持掩码（Retention mask）。

## 43.2\_详细说明（Detailed Documentation）

<a id="ae3614c23f92717999d2058ef8636fe7c"></a>

### `domain_id`

```c
uint32_t scmi_pd_lpm_settings::domain_id
```

电源域的 ID。

<a id="a35c3e1f1f5ab7339b6ae736fb3dcde31"></a>

### `lpm_setting`

```c
uint32_t scmi_pd_lpm_settings::lpm_setting
```

该电源域的低功耗模式设置。

<a id="a18de2ecf5f1d072967eacf7375d9e64c"></a>

### `ret_mask`

```c
uint32_t scmi_pd_lpm_settings::ret_mask
```

在低功耗模式下应用的保持掩码（Retention mask）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_scmi_nxp_cpu_vector_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_scmi_pinctrl_settings_结构体.md)
