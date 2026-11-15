---
id: learning.zephyr-docs.platform-security-model-reference.page-39
title: scmi_nxp_cpu_irq_mask_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__irq__mask__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_scmi\_nxp\_cpu\_irq\_mask\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__nxp__cpu__irq__mask__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CPU_IRQ_WAKE_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

<a id="details"></a>

描述CPU_IRQ_WAKE_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a53fb756537e3dd3c997371726b11a3f1"></a>

```c
uint32_t cpu_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cpu_id](#a53fb756537e3dd3c997371726b11a3f1)。

待配置 CPU 的 ID。

<a id="r_a75f9b3c94bef32627ca92af1c90ca032"></a>

```c
uint32_t mask_idx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mask_idx](#a75f9b3c94bef32627ca92af1c90ca032)。

要写入的第一个掩码字（Mask word）的索引。

<a id="r_a5ffe5fae57289b1d53b8a19ca676f6e9"></a>

```c
uint32_t num_mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_mask](#a5ffe5fae57289b1d53b8a19ca676f6e9)。

`mask` 中有效条目的数量。

<a id="r_a416a9df0f67c107d490725d2eeff8623"></a>

```c
uint32_t mask [22U]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mask](#a416a9df0f67c107d490725d2eeff8623)。

IRQ 唤醒掩码字。

## 39.2\_详细说明（Detailed Documentation）

<a id="a53fb756537e3dd3c997371726b11a3f1"></a>

### `cpu_id`

```c
uint32_t scmi_nxp_cpu_irq_mask_config::cpu_id
```

待配置 CPU 的 ID。

<a id="a416a9df0f67c107d490725d2eeff8623"></a>

### `mask`

```c
uint32_t scmi_nxp_cpu_irq_mask_config::mask[22U]
```

IRQ 唤醒掩码字。

<a id="a75f9b3c94bef32627ca92af1c90ca032"></a>

### `mask_idx`

```c
uint32_t scmi_nxp_cpu_irq_mask_config::mask_idx
```

要写入的第一个掩码字（Mask word）的索引。

<a id="a5ffe5fae57289b1d53b8a19ca676f6e9"></a>

### `num_mask`

```c
uint32_t scmi_nxp_cpu_irq_mask_config::num_mask
```

`mask` 中有效条目的数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/nxp/cpu.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/nxp/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_scmi_nxp_cpu_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_scmi_nxp_cpu_pd_lpm_config_结构体.md)
