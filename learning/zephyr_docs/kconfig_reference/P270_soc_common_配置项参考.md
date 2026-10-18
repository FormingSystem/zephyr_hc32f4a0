---
id: learning.zephyr-docs.kconfig-reference.page-270
title: "`soc/common`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第270章\_`soc/common`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/common` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RISCV_VECTORED_MODE"></a>

## 270.1 `CONFIG_RISCV_VECTORED_MODE`

**提示（Prompt）**：SoC 是否使用向量模式（vectored mode）

**说明（Help）**

SoC 是否使用向量模式（vectored mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PRIVILEGED && CONFIG_RISCV_PRIVILEGED
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENTITAN
CONFIG_GEN_IRQ_VECTOR_TABLE
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`soc/common/riscv-privileged/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/common/riscv-privileged/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PRIVILEGED`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PRIVILEGED)、[`CONFIG_SOC_SERIES_BL60X`](P266_soc_bflb_配置项参考.md#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](P266_soc_bflb_配置项参考.md#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](P266_soc_bflb_配置项参考.md#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_GEN_IRQ_VECTOR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_IRQ_VECTOR_TABLE)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_OPENTITAN`、`CONFIG_CPU_XUANTIE_E907`。

<!-- kconfig-navigation -->

[上一章](P269_soc_cdns_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P271_soc_efinix_配置项参考.md)
