---
id: learning.zephyr-docs.kconfig-reference.page-217
title: "`modules/Kconfig.xtensa`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第217章\_`modules/Kconfig.xtensa`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.xtensa` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_XTENSA_HAL"></a>

## 217.1 `CONFIG_XTENSA_HAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在构建过程中构建 Xtensa 硬件抽象层（HAL）模块。此项由 Xtensa 架构（ARCH）Kconfig 自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT595S_F1
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_HIFI1
CONFIG_SOC_MIMXRT758S_HIFI1
CONFIG_SOC_MIMXRT735S_HIFI1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER
CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_ACP_7_X
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_SOC_XTENSA_DC233C
CONFIG_SOC_ACP_7_0
CONFIG_SOC_ACP_6_0
```

**定义位置（Location）**：[`modules/Kconfig.xtensa:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.xtensa#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT595S_F1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_F1)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER)、[`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_ACP_7_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_X)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)、[`CONFIG_SOC_ACP_7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_0)、[`CONFIG_SOC_ACP_6_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_6_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER`、`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`、`CONFIG_SOC_ACP_7_X`、`CONFIG_SOC_XTENSA_DC233C`、`CONFIG_SOC_ACP_7_0`、`CONFIG_SOC_ACP_6_0`。

<!-- kconfig-navigation -->

[上一章](P216_modules_Kconfig.vega_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P218_modules_acpica_配置项参考.md)
