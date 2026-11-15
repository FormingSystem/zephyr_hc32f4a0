---
id: learning.zephyr-docs.kconfig-reference.page-269
title: "`soc/cdns`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第269章\_`soc/cdns`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/cdns` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_CDNS_SWERV_BOOT_MRAC"></a>

## 269.1 `CONFIG_SOC_CDNS_SWERV_BOOT_MRAC`

**提示（Prompt）**：启动时设置 MRAC 控制与状态寄存器值（MRAC CSR value）

**说明（Help）**

设置 MRAC 控制与状态寄存器（CSR），为区域访问控制配置缓存（caching）和副作用（side effect）属性。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_S400 || CONFIG_SOC_S420) && CONFIG_SOC_FAMILY_CDNS_SWERV
```

**定义位置（Location）**：[`soc/cdns/swerv/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/cdns/swerv/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_S400`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S400)、[`CONFIG_SOC_S420`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S420)、[`CONFIG_SOC_FAMILY_CDNS_SWERV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CDNS_SWERV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_S400`、`CONFIG_SOC_S420`、`CONFIG_SOC_FAMILY_CDNS_SWERV`。

<!-- kconfig-navigation -->

[上一章](P268_soc_cdac_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P270_soc_common_配置项参考.md)
