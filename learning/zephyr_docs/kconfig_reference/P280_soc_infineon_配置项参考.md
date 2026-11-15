---
id: learning.zephyr-docs.kconfig-reference.page-280
title: "`soc/infineon`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第280章\_`soc/infineon`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/infineon` 的 33 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_INFINEON_SECURE_LCS"></a>

## 280.1 `CONFIG_INFINEON_SECURE_LCS`

**提示（Prompt）**：安全生命周期状态阶段支持（Secure LCS stage support）

**说明（Help）**

启用安全生命周期状态阶段（SECURE LCS stage）支持。在此阶段，保护状态（protection state）设为“安全”（secure）。处于安全状态的设备，只有其 Flash 引导代码（flash boot）和应用代码通过认证后才会启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1B
```

**定义位置（Location）**：[`soc/infineon/cat1b/cyw20829/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1b/cyw20829/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1B`。

<a id="CONFIG_INFINEON_SECURE_POLICY"></a>

## 280.2 `CONFIG_INFINEON_SECURE_POLICY`

**提示（Prompt）**：策略 JSON 文件路径（policy JSON file）

**说明（Help）**

策略（Policy）是 JSON 格式的文本文件，包含一组设备配置属性，例如启用／禁用调试访问端口（debug access ports）、串行存储器接口（SMIF）配置、密钥信息等。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1B
```

**默认值（Defaults）**

```text
"default_policy.json"
```

**定义位置（Location）**：[`soc/infineon/cat1b/cyw20829/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1b/cyw20829/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1B`。

<a id="CONFIG_INFINEON_SMIF_ENCRYPTION"></a>

## 280.3 `CONFIG_INFINEON_SMIF_ENCRYPTION`

**提示（Prompt）**：串行存储器接口加密支持（SMIF encryption support）

**说明（Help）**

启用串行存储器接口加密（SMIF encryption）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INFINEON_SECURE_LCS && CONFIG_SOC_FAMILY_INFINEON_CAT1B
```

**定义位置（Location）**：[`soc/infineon/cat1b/cyw20829/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1b/cyw20829/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_INFINEON_SECURE_LCS`](P280_soc_infineon_配置项参考.md#CONFIG_INFINEON_SECURE_LCS)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1B`。

<a id="CONFIG_PSOC_EDGE_M55_SRF_SUPPORT"></a>

## 280.4 `CONFIG_PSOC_EDGE_M55_SRF_SUPPORT`

**提示（Prompt）**：选择是否在 M55 上启用 SRF 支持（SRF support）

**说明（Help）**

此选项启用 PSE84 的 M55 内核上的 SRF 支持，并在 M33／非安全侧（m33/ns）建立与之配合的基础设施。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_EDGE
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_ABSTRACTION_RTOS
```

**定义位置（Location）**：[`soc/infineon/edge/pse84/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/edge/pse84/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_USE_INFINEON_ABSTRACTION_RTOS`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_ABSTRACTION_RTOS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_EDGE`。

<a id="CONFIG_SOC_PACKAGE_PSOC4000T_16_QFN"></a>

## 280.5 `CONFIG_SOC_PACKAGE_PSOC4000T_16_QFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

16 引脚四方扁平无引线封装（QFN package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4025LQI_T411
CONFIG_SOC_CY8C4025LQI_T441
CONFIG_SOC_CY8C4025LQI_T451
CONFIG_SOC_CY8C4026LQI_T411
CONFIG_SOC_CY8C4026LQI_T441
CONFIG_SOC_CY8C4045LQI_T411
CONFIG_SOC_CY8C4045LQI_T441
CONFIG_SOC_CY8C4045LQI_T451
CONFIG_SOC_CY8C4046LQI_T411
CONFIG_SOC_CY8C4046LQI_T441
CONFIG_SOC_CY8C4046LQI_T451
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4000t/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4000t/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4025LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T411)、[`CONFIG_SOC_CY8C4025LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T441)、[`CONFIG_SOC_CY8C4025LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T451)、[`CONFIG_SOC_CY8C4026LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T411)、[`CONFIG_SOC_CY8C4026LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T441)、[`CONFIG_SOC_CY8C4045LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T411)、[`CONFIG_SOC_CY8C4045LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T441)、[`CONFIG_SOC_CY8C4045LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T451)、[`CONFIG_SOC_CY8C4046LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T411)、[`CONFIG_SOC_CY8C4046LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T441)、[`CONFIG_SOC_CY8C4046LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T451)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4025LQI_T411`、`CONFIG_SOC_CY8C4025LQI_T441`、`CONFIG_SOC_CY8C4025LQI_T451`、`CONFIG_SOC_CY8C4026LQI_T411`、`CONFIG_SOC_CY8C4026LQI_T441`、`CONFIG_SOC_CY8C4045LQI_T411`、`CONFIG_SOC_CY8C4045LQI_T441`、`CONFIG_SOC_CY8C4045LQI_T451`、`CONFIG_SOC_CY8C4046LQI_T411`、`CONFIG_SOC_CY8C4046LQI_T441`、`CONFIG_SOC_CY8C4046LQI_T451`。

<a id="CONFIG_SOC_PACKAGE_PSOC4000T_24_QFN"></a>

## 280.6 `CONFIG_SOC_PACKAGE_PSOC4000T_24_QFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

24 引脚四方扁平无引线封装（QFN package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4046LQI_T452
CONFIG_SOC_CY8C4046LQE_T1
CONFIG_SOC_CY8C4025LQI_T412
CONFIG_SOC_CY8C4025LQI_T442
CONFIG_SOC_CY8C4025LQI_T452
CONFIG_SOC_CY8C4026LQI_T412
CONFIG_SOC_CY8C4026LQI_T442
CONFIG_SOC_CY8C4045LQI_T412
CONFIG_SOC_CY8C4045LQI_T442
CONFIG_SOC_CY8C4045LQI_T452
CONFIG_SOC_CY8C4045LQE_T1
CONFIG_SOC_CY8C4045LQS_T1
CONFIG_SOC_CY8C4046LQI_T412
CONFIG_SOC_CY8C4046LQI_T442
CONFIG_SOC_CY8C4046LQS_T1
CONFIG_SOC_CY8C4046LQQ_T412
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4000t/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4000t/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4046LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T452)、[`CONFIG_SOC_CY8C4046LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQE_T1)、[`CONFIG_SOC_CY8C4025LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T412)、[`CONFIG_SOC_CY8C4025LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T442)、[`CONFIG_SOC_CY8C4025LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T452)、[`CONFIG_SOC_CY8C4026LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T412)、[`CONFIG_SOC_CY8C4026LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T442)、[`CONFIG_SOC_CY8C4045LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T412)、[`CONFIG_SOC_CY8C4045LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T442)、[`CONFIG_SOC_CY8C4045LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T452)、[`CONFIG_SOC_CY8C4045LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQE_T1)、[`CONFIG_SOC_CY8C4045LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQS_T1)、[`CONFIG_SOC_CY8C4046LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T412)、[`CONFIG_SOC_CY8C4046LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T442)、[`CONFIG_SOC_CY8C4046LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQS_T1)、[`CONFIG_SOC_CY8C4046LQQ_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQQ_T412)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4046LQI_T452`、`CONFIG_SOC_CY8C4046LQE_T1`、`CONFIG_SOC_CY8C4025LQI_T412`、`CONFIG_SOC_CY8C4025LQI_T442`、`CONFIG_SOC_CY8C4025LQI_T452`、`CONFIG_SOC_CY8C4026LQI_T412`、`CONFIG_SOC_CY8C4026LQI_T442`、`CONFIG_SOC_CY8C4045LQI_T412`、`CONFIG_SOC_CY8C4045LQI_T442`、`CONFIG_SOC_CY8C4045LQI_T452`、`CONFIG_SOC_CY8C4045LQE_T1`、`CONFIG_SOC_CY8C4045LQS_T1`、`CONFIG_SOC_CY8C4046LQI_T412`、`CONFIG_SOC_CY8C4046LQI_T442`、`CONFIG_SOC_CY8C4046LQS_T1`、`CONFIG_SOC_CY8C4046LQQ_T412`。

<a id="CONFIG_SOC_PACKAGE_PSOC4000T_25_WLCSP"></a>

## 280.7 `CONFIG_SOC_PACKAGE_PSOC4000T_25_WLCSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

25 引脚晶圆级芯片尺寸封装（WLCSP package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4025FNI_T412
CONFIG_SOC_CY8C4025FNI_T442
CONFIG_SOC_CY8C4025FNI_T452
CONFIG_SOC_CY8C4026FNI_T412
CONFIG_SOC_CY8C4026FNI_T442
CONFIG_SOC_CY8C4045FNI_T412
CONFIG_SOC_CY8C4045FNI_T442
CONFIG_SOC_CY8C4045FNI_T452
CONFIG_SOC_CY8C4046FNI_T412
CONFIG_SOC_CY8C4046FNI_T442
CONFIG_SOC_CY8C4046FNI_T452
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4000t/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4000t/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4025FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T412)、[`CONFIG_SOC_CY8C4025FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T442)、[`CONFIG_SOC_CY8C4025FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T452)、[`CONFIG_SOC_CY8C4026FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026FNI_T412)、[`CONFIG_SOC_CY8C4026FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026FNI_T442)、[`CONFIG_SOC_CY8C4045FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T412)、[`CONFIG_SOC_CY8C4045FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T442)、[`CONFIG_SOC_CY8C4045FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T452)、[`CONFIG_SOC_CY8C4046FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T412)、[`CONFIG_SOC_CY8C4046FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T442)、[`CONFIG_SOC_CY8C4046FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T452)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4025FNI_T412`、`CONFIG_SOC_CY8C4025FNI_T442`、`CONFIG_SOC_CY8C4025FNI_T452`、`CONFIG_SOC_CY8C4026FNI_T412`、`CONFIG_SOC_CY8C4026FNI_T442`、`CONFIG_SOC_CY8C4045FNI_T412`、`CONFIG_SOC_CY8C4045FNI_T442`、`CONFIG_SOC_CY8C4045FNI_T452`、`CONFIG_SOC_CY8C4046FNI_T412`、`CONFIG_SOC_CY8C4046FNI_T442`、`CONFIG_SOC_CY8C4046FNI_T452`。

<a id="CONFIG_SOC_PACKAGE_PSOC4100SMAX_100_TQFP"></a>

## 280.8 `CONFIG_SOC_PACKAGE_PSOC4100SMAX_100_TQFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

100 引脚薄型四方扁平封装（TQFP package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4149AZI_S598
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100smax/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100smax/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4149AZI_S598`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4149AZI_S598)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4149AZI_S598`。

<a id="CONFIG_SOC_PACKAGE_PSOC4100TP_44_TQFP"></a>

## 280.9 `CONFIG_SOC_PACKAGE_PSOC4100TP_44_TQFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

44 引脚薄型四方扁平封装（TQFP package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4146AXI_T403
CONFIG_SOC_CY8C4146AXI_T413
CONFIG_SOC_CY8C4146AXI_T453
CONFIG_SOC_CY8C4147AXI_T403
CONFIG_SOC_CY8C4147AXI_T413
CONFIG_SOC_CY8C4147AXI_T453
CONFIG_SOC_CY8C4147AXI_T463
CONFIG_SOC_CY8C4147AXI_T473
CONFIG_SOC_CY8C4147AXQ_T493
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4146AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T403)、[`CONFIG_SOC_CY8C4146AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T413)、[`CONFIG_SOC_CY8C4146AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T453)、[`CONFIG_SOC_CY8C4147AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T403)、[`CONFIG_SOC_CY8C4147AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T413)、[`CONFIG_SOC_CY8C4147AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T453)、[`CONFIG_SOC_CY8C4147AXI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T463)、[`CONFIG_SOC_CY8C4147AXI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T473)、[`CONFIG_SOC_CY8C4147AXQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXQ_T493)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4146AXI_T403`、`CONFIG_SOC_CY8C4146AXI_T413`、`CONFIG_SOC_CY8C4146AXI_T453`、`CONFIG_SOC_CY8C4147AXI_T403`、`CONFIG_SOC_CY8C4147AXI_T413`、`CONFIG_SOC_CY8C4147AXI_T453`、`CONFIG_SOC_CY8C4147AXI_T463`、`CONFIG_SOC_CY8C4147AXI_T473`、`CONFIG_SOC_CY8C4147AXQ_T493`。

<a id="CONFIG_SOC_PACKAGE_PSOC4100TP_48_QFN"></a>

## 280.10 `CONFIG_SOC_PACKAGE_PSOC4100TP_48_QFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

48 引脚四方扁平无引线封装（QFN package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4146LQI_T403
CONFIG_SOC_CY8C4146LQI_T413
CONFIG_SOC_CY8C4146LQI_T453
CONFIG_SOC_CY8C4147LQI_T403
CONFIG_SOC_CY8C4147LQI_T413
CONFIG_SOC_CY8C4147LQI_T453
CONFIG_SOC_CY8C4147LQI_T463
CONFIG_SOC_CY8C4147LQI_T473
CONFIG_SOC_CY8C4147LQQ_T493
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4146LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T403)、[`CONFIG_SOC_CY8C4146LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T413)、[`CONFIG_SOC_CY8C4146LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T453)、[`CONFIG_SOC_CY8C4147LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T403)、[`CONFIG_SOC_CY8C4147LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T413)、[`CONFIG_SOC_CY8C4147LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T453)、[`CONFIG_SOC_CY8C4147LQI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T463)、[`CONFIG_SOC_CY8C4147LQI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T473)、[`CONFIG_SOC_CY8C4147LQQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQQ_T493)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4146LQI_T403`、`CONFIG_SOC_CY8C4146LQI_T413`、`CONFIG_SOC_CY8C4146LQI_T453`、`CONFIG_SOC_CY8C4147LQI_T403`、`CONFIG_SOC_CY8C4147LQI_T413`、`CONFIG_SOC_CY8C4147LQI_T453`、`CONFIG_SOC_CY8C4147LQI_T463`、`CONFIG_SOC_CY8C4147LQI_T473`、`CONFIG_SOC_CY8C4147LQQ_T493`。

<a id="CONFIG_SOC_PACKAGE_PSOC4100TP_48_TQFP"></a>

## 280.11 `CONFIG_SOC_PACKAGE_PSOC4100TP_48_TQFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

48 引脚薄型四方扁平封装（TQFP package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4146AZI_T403
CONFIG_SOC_CY8C4146AZI_T413
CONFIG_SOC_CY8C4146AZI_T453
CONFIG_SOC_CY8C4147AZI_T403
CONFIG_SOC_CY8C4147AZI_T413
CONFIG_SOC_CY8C4147AZI_T453
CONFIG_SOC_CY8C4147AZI_T463
CONFIG_SOC_CY8C4147AZI_T473
CONFIG_SOC_CY8C4147AZQ_T493
CONFIG_SOC_CY8C4146AZQ_T413
CONFIG_SOC_CY8C4146AZQ_T453
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4146AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T403)、[`CONFIG_SOC_CY8C4146AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T413)、[`CONFIG_SOC_CY8C4146AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T453)、[`CONFIG_SOC_CY8C4147AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T403)、[`CONFIG_SOC_CY8C4147AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T413)、[`CONFIG_SOC_CY8C4147AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T453)、[`CONFIG_SOC_CY8C4147AZI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T463)、[`CONFIG_SOC_CY8C4147AZI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T473)、[`CONFIG_SOC_CY8C4147AZQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T493)、[`CONFIG_SOC_CY8C4146AZQ_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZQ_T413)、[`CONFIG_SOC_CY8C4146AZQ_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZQ_T453)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4146AZI_T403`、`CONFIG_SOC_CY8C4146AZI_T413`、`CONFIG_SOC_CY8C4146AZI_T453`、`CONFIG_SOC_CY8C4147AZI_T403`、`CONFIG_SOC_CY8C4147AZI_T413`、`CONFIG_SOC_CY8C4147AZI_T453`、`CONFIG_SOC_CY8C4147AZI_T463`、`CONFIG_SOC_CY8C4147AZI_T473`、`CONFIG_SOC_CY8C4147AZQ_T493`、`CONFIG_SOC_CY8C4146AZQ_T413`、`CONFIG_SOC_CY8C4146AZQ_T453`。

<a id="CONFIG_SOC_PACKAGE_PSOC4100TP_64_TQFP"></a>

## 280.12 `CONFIG_SOC_PACKAGE_PSOC4100TP_64_TQFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

64 引脚薄型四方扁平封装（TQFP package）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4146AZI_T405
CONFIG_SOC_CY8C4146AZI_T415
CONFIG_SOC_CY8C4146AZI_T455
CONFIG_SOC_CY8C4147AZI_T405
CONFIG_SOC_CY8C4147AZI_T415
CONFIG_SOC_CY8C4147AZI_T455
CONFIG_SOC_CY8C4147AZI_T465
CONFIG_SOC_CY8C4147AZI_T475
CONFIG_SOC_CY8C4147AZQ_T495
CONFIG_SOC_CY8C4147AZQ_T415
CONFIG_SOC_CY8C4147AZQ_T455
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CY8C4146AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T405)、[`CONFIG_SOC_CY8C4146AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T415)、[`CONFIG_SOC_CY8C4146AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T455)、[`CONFIG_SOC_CY8C4147AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T405)、[`CONFIG_SOC_CY8C4147AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T415)、[`CONFIG_SOC_CY8C4147AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T455)、[`CONFIG_SOC_CY8C4147AZI_T465`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T465)、[`CONFIG_SOC_CY8C4147AZI_T475`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T475)、[`CONFIG_SOC_CY8C4147AZQ_T495`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T495)、[`CONFIG_SOC_CY8C4147AZQ_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T415)、[`CONFIG_SOC_CY8C4147AZQ_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T455)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CY8C4146AZI_T405`、`CONFIG_SOC_CY8C4146AZI_T415`、`CONFIG_SOC_CY8C4146AZI_T455`、`CONFIG_SOC_CY8C4147AZI_T405`、`CONFIG_SOC_CY8C4147AZI_T415`、`CONFIG_SOC_CY8C4147AZI_T455`、`CONFIG_SOC_CY8C4147AZI_T465`、`CONFIG_SOC_CY8C4147AZI_T475`、`CONFIG_SOC_CY8C4147AZQ_T495`、`CONFIG_SOC_CY8C4147AZQ_T415`、`CONFIG_SOC_CY8C4147AZQ_T455`。

<a id="CONFIG_SOC_PSC3_LPM_TIMER"></a>

## 280.13 `CONFIG_SOC_PSC3_LPM_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用多计数器看门狗定时器（MCWDT），作为 SysTick 的低功耗配套定时器。MCWDT 由 32 kHz 晶体振荡器（WCO）驱动，在深度睡眠（deepsleep）期间，高频时钟（HF clocks）及 SysTick 停止时提供计时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1B
```

**默认值（Defaults）**

```text
y if CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_LPTIMER
```

**定义位置（Location）**：[`soc/infineon/cat1b/psc3/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1b/psc3/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1B)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS)、[`CONFIG_USE_INFINEON_LPTIMER`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_LPTIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1B`。

<a id="CONFIG_SOC_PSE84_LPM_TIMER"></a>

## 280.14 `CONFIG_SOC_PSE84_LPM_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用多计数器看门狗定时器（MCWDT），作为 SysTick 的低功耗配套定时器。MCWDT 由 32 kHz 精密内部低速振荡器（PILO）驱动，在深度睡眠（deepsleep）期间，高频时钟（HF clocks）及 SysTick 停止时提供计时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_EDGE
```

**默认值（Defaults）**

```text
y if CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_LPTIMER
```

**定义位置（Location）**：[`soc/infineon/edge/pse84/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/edge/pse84/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS)、[`CONFIG_USE_INFINEON_LPTIMER`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_LPTIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_EDGE`。

<a id="CONFIG_SOC_PSE84_M55_ENABLE"></a>

## 280.15 `CONFIG_SOC_PSE84_M55_ENABLE`

**提示（Prompt）**：设置期间启用 PSE84 M55 内核（m55 core enabled during setup）

**说明（Help）**

此选项由 M33 内核启用 PSE84 上的 M55 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_PSE84_M33 && CONFIG_SOC_FAMILY_INFINEON_EDGE
```

**定义位置（Location）**：[`soc/infineon/edge/pse84/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/edge/pse84/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_PSE84_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M33)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_PSE84_M33`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`。

<a id="CONFIG_SOC_PSOC6_CM0P_IMAGE_SLEEP"></a>

## 280.16 `CONFIG_SOC_PSOC6_CM0P_IMAGE_SLEEP`

**提示（Prompt）**：深度睡眠（DeepSleep）

**说明（Help）**

深度睡眠（DeepSleep）预构建应用镜像在 PSOC™ 6 BLE 双核 MCU 的 Cortex-M0+ 内核上执行。此镜像以 C 数组形式提供，可直接作为 Cortex-M4 应用的一部分编译。Cortex-M4 链接器脚本会将 Cortex-M0+ 应用代码放入内部 Flash。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/infineon/cat1a/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1a/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → PSOC™ 6 Cortex-M0+ 预构建镜像（prebuilt images）

<a id="CONFIG_SOC_PSOC6_M0_ENABLES_M4"></a>

## 280.17 `CONFIG_SOC_PSOC6_M0_ENABLES_M4`

**提示（Prompt）**：双核支持，激活 Cortex-M4（Dual-core support）

**说明（Help）**

Cortex-M0 CPU 应启动 Cortex-M4

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0
```

**定义位置（Location）**：[`soc/infineon/cat1a/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1a/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`。

<a id="CONFIG_SOC_SERIES_CYT4DN_START_M7_0"></a>

## 280.18 `CONFIG_SOC_SERIES_CYT4DN_START_M7_0`

**提示（Prompt）**：M0+ 启动期间的 CYT4DN M7 内核 0（M7 Core 0）

**说明（Help）**

允许从 M0+ 内核启动 M7 内核 0。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CYT4DN && CONFIG_SOC_SERIES_CYT4DN && CONFIG_SOC_FAMILY_INFINEON_CAT1C
```

**定义位置（Location）**：[`soc/infineon/cat1c/cyt4dn/m0p/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1c/cyt4dn/m0p/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CYT4DN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYT4DN)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_CYT4DN`、`CONFIG_SOC_FAMILY_INFINEON_CAT1C`。

<a id="CONFIG_SOC_SERIES_CYT4DN_START_M7_1"></a>

## 280.19 `CONFIG_SOC_SERIES_CYT4DN_START_M7_1`

**提示（Prompt）**：M0+ 启动期间的 CYT4DN M7 内核 1（M7 Core 1）

**说明（Help）**

允许从 M0+ 内核启动 M7 内核 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CYT4DN && CONFIG_SOC_SERIES_CYT4DN && CONFIG_SOC_FAMILY_INFINEON_CAT1C
```

**定义位置（Location）**：[`soc/infineon/cat1c/cyt4dn/m0p/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat1c/cyt4dn/m0p/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CYT4DN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYT4DN)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_CYT4DN`、`CONFIG_SOC_FAMILY_INFINEON_CAT1C`。

<a id="CONFIG_SOC_SERIES_PSOC4000T"></a>

## 280.20 `CONFIG_SOC_SERIES_PSOC4000T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4000T 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4046LQI_T452
CONFIG_SOC_CY8C4046LQE_T1
CONFIG_SOC_CY8C4025LQI_T411
CONFIG_SOC_CY8C4025LQI_T441
CONFIG_SOC_CY8C4025LQI_T451
CONFIG_SOC_CY8C4026LQI_T411
CONFIG_SOC_CY8C4026LQI_T441
CONFIG_SOC_CY8C4045LQI_T411
CONFIG_SOC_CY8C4045LQI_T441
CONFIG_SOC_CY8C4045LQI_T451
CONFIG_SOC_CY8C4046LQI_T411
CONFIG_SOC_CY8C4046LQI_T441
CONFIG_SOC_CY8C4046LQI_T451
CONFIG_SOC_CY8C4025LQI_T412
CONFIG_SOC_CY8C4025LQI_T442
CONFIG_SOC_CY8C4025LQI_T452
CONFIG_SOC_CY8C4026LQI_T412
CONFIG_SOC_CY8C4026LQI_T442
CONFIG_SOC_CY8C4045LQI_T412
CONFIG_SOC_CY8C4045LQI_T442
CONFIG_SOC_CY8C4045LQI_T452
CONFIG_SOC_CY8C4045LQE_T1
CONFIG_SOC_CY8C4045LQS_T1
CONFIG_SOC_CY8C4046LQI_T412
CONFIG_SOC_CY8C4046LQI_T442
CONFIG_SOC_CY8C4046LQS_T1
CONFIG_SOC_CY8C4046LQQ_T412
CONFIG_SOC_CY8C4025FNI_T412
CONFIG_SOC_CY8C4025FNI_T442
CONFIG_SOC_CY8C4025FNI_T452
CONFIG_SOC_CY8C4026FNI_T412
CONFIG_SOC_CY8C4026FNI_T442
CONFIG_SOC_CY8C4045FNI_T412
CONFIG_SOC_CY8C4045FNI_T442
CONFIG_SOC_CY8C4045FNI_T452
CONFIG_SOC_CY8C4046FNI_T412
CONFIG_SOC_CY8C4046FNI_T442
CONFIG_SOC_CY8C4046FNI_T452
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4000t/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4000t/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_CY8C4046LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T452)、[`CONFIG_SOC_CY8C4046LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQE_T1)、[`CONFIG_SOC_CY8C4025LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T411)、[`CONFIG_SOC_CY8C4025LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T441)、[`CONFIG_SOC_CY8C4025LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T451)、[`CONFIG_SOC_CY8C4026LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T411)、[`CONFIG_SOC_CY8C4026LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T441)、[`CONFIG_SOC_CY8C4045LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T411)、[`CONFIG_SOC_CY8C4045LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T441)、[`CONFIG_SOC_CY8C4045LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T451)、[`CONFIG_SOC_CY8C4046LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T411)、[`CONFIG_SOC_CY8C4046LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T441)、[`CONFIG_SOC_CY8C4046LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T451)、[`CONFIG_SOC_CY8C4025LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T412)、[`CONFIG_SOC_CY8C4025LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T442)、[`CONFIG_SOC_CY8C4025LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025LQI_T452)、[`CONFIG_SOC_CY8C4026LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T412)、[`CONFIG_SOC_CY8C4026LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026LQI_T442)、[`CONFIG_SOC_CY8C4045LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T412)、[`CONFIG_SOC_CY8C4045LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T442)、[`CONFIG_SOC_CY8C4045LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQI_T452)、[`CONFIG_SOC_CY8C4045LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQE_T1)、[`CONFIG_SOC_CY8C4045LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045LQS_T1)、[`CONFIG_SOC_CY8C4046LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T412)、[`CONFIG_SOC_CY8C4046LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQI_T442)、[`CONFIG_SOC_CY8C4046LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQS_T1)、[`CONFIG_SOC_CY8C4046LQQ_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046LQQ_T412)、[`CONFIG_SOC_CY8C4025FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T412)、[`CONFIG_SOC_CY8C4025FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T442)、[`CONFIG_SOC_CY8C4025FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4025FNI_T452)、[`CONFIG_SOC_CY8C4026FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026FNI_T412)、[`CONFIG_SOC_CY8C4026FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4026FNI_T442)、[`CONFIG_SOC_CY8C4045FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T412)、[`CONFIG_SOC_CY8C4045FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T442)、[`CONFIG_SOC_CY8C4045FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4045FNI_T452)、[`CONFIG_SOC_CY8C4046FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T412)、[`CONFIG_SOC_CY8C4046FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T442)、[`CONFIG_SOC_CY8C4046FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4046FNI_T452)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`CONFIG_SOC_CY8C4046LQI_T452`、`CONFIG_SOC_CY8C4046LQE_T1`、`CONFIG_SOC_CY8C4025LQI_T411`、`CONFIG_SOC_CY8C4025LQI_T441`、`CONFIG_SOC_CY8C4025LQI_T451`、`CONFIG_SOC_CY8C4026LQI_T411`、`CONFIG_SOC_CY8C4026LQI_T441`、`CONFIG_SOC_CY8C4045LQI_T411`、`CONFIG_SOC_CY8C4045LQI_T441`、`CONFIG_SOC_CY8C4045LQI_T451`、`CONFIG_SOC_CY8C4046LQI_T411`、`CONFIG_SOC_CY8C4046LQI_T441`、`CONFIG_SOC_CY8C4046LQI_T451`、`CONFIG_SOC_CY8C4025LQI_T412`、`CONFIG_SOC_CY8C4025LQI_T442`、`CONFIG_SOC_CY8C4025LQI_T452`、`CONFIG_SOC_CY8C4026LQI_T412`、`CONFIG_SOC_CY8C4026LQI_T442`、`CONFIG_SOC_CY8C4045LQI_T412`、`CONFIG_SOC_CY8C4045LQI_T442`、`CONFIG_SOC_CY8C4045LQI_T452`、`CONFIG_SOC_CY8C4045LQE_T1`、`CONFIG_SOC_CY8C4045LQS_T1`、`CONFIG_SOC_CY8C4046LQI_T412`、`CONFIG_SOC_CY8C4046LQI_T442`、`CONFIG_SOC_CY8C4046LQS_T1`、`CONFIG_SOC_CY8C4046LQQ_T412`、`CONFIG_SOC_CY8C4025FNI_T412`、`CONFIG_SOC_CY8C4025FNI_T442`、`CONFIG_SOC_CY8C4025FNI_T452`、`CONFIG_SOC_CY8C4026FNI_T412`、`CONFIG_SOC_CY8C4026FNI_T442`、`CONFIG_SOC_CY8C4045FNI_T412`、`CONFIG_SOC_CY8C4045FNI_T442`、`CONFIG_SOC_CY8C4045FNI_T452`、`CONFIG_SOC_CY8C4046FNI_T412`、`CONFIG_SOC_CY8C4046FNI_T442`、`CONFIG_SOC_CY8C4046FNI_T452`。

<a id="CONFIG_SOC_SERIES_PSOC4100SMAX"></a>

## 280.21 `CONFIG_SOC_SERIES_PSOC4100SMAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4100Smax 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4149AZI_S598
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100smax/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100smax/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_CY8C4149AZI_S598`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4149AZI_S598)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`CONFIG_SOC_CY8C4149AZI_S598`。

<a id="CONFIG_SOC_SERIES_PSOC4100TP"></a>

## 280.22 `CONFIG_SOC_SERIES_PSOC4100TP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4100tp 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_CY8C4146LQI_T403
CONFIG_SOC_CY8C4146AXI_T403
CONFIG_SOC_CY8C4146AZI_T403
CONFIG_SOC_CY8C4146AZI_T405
CONFIG_SOC_CY8C4146LQI_T413
CONFIG_SOC_CY8C4146AXI_T413
CONFIG_SOC_CY8C4146AZI_T413
CONFIG_SOC_CY8C4146AZI_T415
CONFIG_SOC_CY8C4146LQI_T453
CONFIG_SOC_CY8C4146AXI_T453
CONFIG_SOC_CY8C4146AZI_T453
CONFIG_SOC_CY8C4146AZI_T455
CONFIG_SOC_CY8C4147LQI_T403
CONFIG_SOC_CY8C4147AXI_T403
CONFIG_SOC_CY8C4147AZI_T403
CONFIG_SOC_CY8C4147AZI_T405
CONFIG_SOC_CY8C4147LQI_T413
CONFIG_SOC_CY8C4147AXI_T413
CONFIG_SOC_CY8C4147AZI_T413
CONFIG_SOC_CY8C4147AZI_T415
CONFIG_SOC_CY8C4147LQI_T453
CONFIG_SOC_CY8C4147AXI_T453
CONFIG_SOC_CY8C4147AZI_T453
CONFIG_SOC_CY8C4147AZI_T455
CONFIG_SOC_CY8C4147LQI_T463
CONFIG_SOC_CY8C4147AXI_T463
CONFIG_SOC_CY8C4147AZI_T463
CONFIG_SOC_CY8C4147AZI_T465
CONFIG_SOC_CY8C4147LQI_T473
CONFIG_SOC_CY8C4147AXI_T473
CONFIG_SOC_CY8C4147AZI_T473
CONFIG_SOC_CY8C4147AZI_T475
CONFIG_SOC_CY8C4147LQQ_T493
CONFIG_SOC_CY8C4147AXQ_T493
CONFIG_SOC_CY8C4147AZQ_T493
CONFIG_SOC_CY8C4147AZQ_T495
CONFIG_SOC_CY8C4146AZQ_T413
CONFIG_SOC_CY8C4146AZQ_T453
CONFIG_SOC_CY8C4147AZQ_T415
CONFIG_SOC_CY8C4147AZQ_T455
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_CY8C4146LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T403)、[`CONFIG_SOC_CY8C4146AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T403)、[`CONFIG_SOC_CY8C4146AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T403)、[`CONFIG_SOC_CY8C4146AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T405)、[`CONFIG_SOC_CY8C4146LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T413)、[`CONFIG_SOC_CY8C4146AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T413)、[`CONFIG_SOC_CY8C4146AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T413)、[`CONFIG_SOC_CY8C4146AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T415)、[`CONFIG_SOC_CY8C4146LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146LQI_T453)、[`CONFIG_SOC_CY8C4146AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AXI_T453)、[`CONFIG_SOC_CY8C4146AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T453)、[`CONFIG_SOC_CY8C4146AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZI_T455)、[`CONFIG_SOC_CY8C4147LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T403)、[`CONFIG_SOC_CY8C4147AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T403)、[`CONFIG_SOC_CY8C4147AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T403)、[`CONFIG_SOC_CY8C4147AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T405)、[`CONFIG_SOC_CY8C4147LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T413)、[`CONFIG_SOC_CY8C4147AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T413)、[`CONFIG_SOC_CY8C4147AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T413)、[`CONFIG_SOC_CY8C4147AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T415)、[`CONFIG_SOC_CY8C4147LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T453)、[`CONFIG_SOC_CY8C4147AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T453)、[`CONFIG_SOC_CY8C4147AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T453)、[`CONFIG_SOC_CY8C4147AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T455)、[`CONFIG_SOC_CY8C4147LQI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T463)、[`CONFIG_SOC_CY8C4147AXI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T463)、[`CONFIG_SOC_CY8C4147AZI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T463)、[`CONFIG_SOC_CY8C4147AZI_T465`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T465)、[`CONFIG_SOC_CY8C4147LQI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQI_T473)、[`CONFIG_SOC_CY8C4147AXI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXI_T473)、[`CONFIG_SOC_CY8C4147AZI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T473)、[`CONFIG_SOC_CY8C4147AZI_T475`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZI_T475)、[`CONFIG_SOC_CY8C4147LQQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147LQQ_T493)、[`CONFIG_SOC_CY8C4147AXQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AXQ_T493)、[`CONFIG_SOC_CY8C4147AZQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T493)、[`CONFIG_SOC_CY8C4147AZQ_T495`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T495)、[`CONFIG_SOC_CY8C4146AZQ_T413`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZQ_T413)、[`CONFIG_SOC_CY8C4146AZQ_T453`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4146AZQ_T453)、[`CONFIG_SOC_CY8C4147AZQ_T415`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T415)、[`CONFIG_SOC_CY8C4147AZQ_T455`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C4147AZQ_T455)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`CONFIG_SOC_CY8C4146LQI_T403`、`CONFIG_SOC_CY8C4146AXI_T403`、`CONFIG_SOC_CY8C4146AZI_T403`、`CONFIG_SOC_CY8C4146AZI_T405`、`CONFIG_SOC_CY8C4146LQI_T413`、`CONFIG_SOC_CY8C4146AXI_T413`、`CONFIG_SOC_CY8C4146AZI_T413`、`CONFIG_SOC_CY8C4146AZI_T415`、`CONFIG_SOC_CY8C4146LQI_T453`、`CONFIG_SOC_CY8C4146AXI_T453`、`CONFIG_SOC_CY8C4146AZI_T453`、`CONFIG_SOC_CY8C4146AZI_T455`、`CONFIG_SOC_CY8C4147LQI_T403`、`CONFIG_SOC_CY8C4147AXI_T403`、`CONFIG_SOC_CY8C4147AZI_T403`、`CONFIG_SOC_CY8C4147AZI_T405`、`CONFIG_SOC_CY8C4147LQI_T413`、`CONFIG_SOC_CY8C4147AXI_T413`、`CONFIG_SOC_CY8C4147AZI_T413`、`CONFIG_SOC_CY8C4147AZI_T415`、`CONFIG_SOC_CY8C4147LQI_T453`、`CONFIG_SOC_CY8C4147AXI_T453`、`CONFIG_SOC_CY8C4147AZI_T453`、`CONFIG_SOC_CY8C4147AZI_T455`、`CONFIG_SOC_CY8C4147LQI_T463`、`CONFIG_SOC_CY8C4147AXI_T463`、`CONFIG_SOC_CY8C4147AZI_T463`、`CONFIG_SOC_CY8C4147AZI_T465`、`CONFIG_SOC_CY8C4147LQI_T473`、`CONFIG_SOC_CY8C4147AXI_T473`、`CONFIG_SOC_CY8C4147AZI_T473`、`CONFIG_SOC_CY8C4147AZI_T475`、`CONFIG_SOC_CY8C4147LQQ_T493`、`CONFIG_SOC_CY8C4147AXQ_T493`、`CONFIG_SOC_CY8C4147AZQ_T493`、`CONFIG_SOC_CY8C4147AZQ_T495`、`CONFIG_SOC_CY8C4146AZQ_T413`、`CONFIG_SOC_CY8C4146AZQ_T453`、`CONFIG_SOC_CY8C4147AZQ_T415`、`CONFIG_SOC_CY8C4147AZQ_T455`。

<a id="CONFIG_SOC_SERIES_XMC4XXX"></a>

## 280.23 `CONFIG_SOC_SERIES_XMC4XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC 4xxx 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INFINEON_XMC
```

**被选择（Selected by）**

```text
CONFIG_SOC_XMC4500
CONFIG_SOC_XMC4700
CONFIG_SOC_XMC4800
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_XMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_XMC)、[`CONFIG_SOC_XMC4500`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_XMC4500)、[`CONFIG_SOC_XMC4700`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_XMC4700)、[`CONFIG_SOC_XMC4800`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_XMC4800)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_XMC`。

<a id="CONFIG_SOC_XMC4500"></a>

## 280.24 `CONFIG_SOC_XMC4500`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4500 片上系统配置（SoC）：`SOC_XMC4500`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_XMC45_RELAX_KIT
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_BOARD_XMC45_RELAX_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XMC45_RELAX_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XMC45_RELAX_KIT`。

<a id="CONFIG_SOC_XMC4700"></a>

## 280.25 `CONFIG_SOC_XMC4700`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4700 片上系统配置（SoC）：`SOC_XMC4700`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_XMC47_RELAX_KIT
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_BOARD_XMC47_RELAX_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XMC47_RELAX_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XMC47_RELAX_KIT`。

<a id="CONFIG_SOC_XMC4800"></a>

## 280.26 `CONFIG_SOC_XMC4800`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4800 片上系统配置（SoC）：`SOC_XMC4800`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_SERIES_XMC4XXX)。

<a id="SB_CONFIG_SOC_SERIES_PSOC4000T"></a>

## 280.27 `SB_CONFIG_SOC_SERIES_PSOC4000T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4000T 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CY8C4046LQI_T452
SB_CONFIG_SOC_CY8C4046LQE_T1
SB_CONFIG_SOC_CY8C4025LQI_T411
SB_CONFIG_SOC_CY8C4025LQI_T441
SB_CONFIG_SOC_CY8C4025LQI_T451
SB_CONFIG_SOC_CY8C4026LQI_T411
SB_CONFIG_SOC_CY8C4026LQI_T441
SB_CONFIG_SOC_CY8C4045LQI_T411
SB_CONFIG_SOC_CY8C4045LQI_T441
SB_CONFIG_SOC_CY8C4045LQI_T451
SB_CONFIG_SOC_CY8C4046LQI_T411
SB_CONFIG_SOC_CY8C4046LQI_T441
SB_CONFIG_SOC_CY8C4046LQI_T451
SB_CONFIG_SOC_CY8C4025LQI_T412
SB_CONFIG_SOC_CY8C4025LQI_T442
SB_CONFIG_SOC_CY8C4025LQI_T452
SB_CONFIG_SOC_CY8C4026LQI_T412
SB_CONFIG_SOC_CY8C4026LQI_T442
SB_CONFIG_SOC_CY8C4045LQI_T412
SB_CONFIG_SOC_CY8C4045LQI_T442
SB_CONFIG_SOC_CY8C4045LQI_T452
SB_CONFIG_SOC_CY8C4045LQE_T1
SB_CONFIG_SOC_CY8C4045LQS_T1
SB_CONFIG_SOC_CY8C4046LQI_T412
SB_CONFIG_SOC_CY8C4046LQI_T442
SB_CONFIG_SOC_CY8C4046LQS_T1
SB_CONFIG_SOC_CY8C4046LQQ_T412
SB_CONFIG_SOC_CY8C4025FNI_T412
SB_CONFIG_SOC_CY8C4025FNI_T442
SB_CONFIG_SOC_CY8C4025FNI_T452
SB_CONFIG_SOC_CY8C4026FNI_T412
SB_CONFIG_SOC_CY8C4026FNI_T442
SB_CONFIG_SOC_CY8C4045FNI_T412
SB_CONFIG_SOC_CY8C4045FNI_T442
SB_CONFIG_SOC_CY8C4045FNI_T452
SB_CONFIG_SOC_CY8C4046FNI_T412
SB_CONFIG_SOC_CY8C4046FNI_T442
SB_CONFIG_SOC_CY8C4046FNI_T452
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4000t/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4000t/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`SB_CONFIG_SOC_CY8C4046LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T452)、[`SB_CONFIG_SOC_CY8C4046LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQE_T1)、[`SB_CONFIG_SOC_CY8C4025LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T411)、[`SB_CONFIG_SOC_CY8C4025LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T441)、[`SB_CONFIG_SOC_CY8C4025LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T451)、[`SB_CONFIG_SOC_CY8C4026LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026LQI_T411)、[`SB_CONFIG_SOC_CY8C4026LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026LQI_T441)、[`SB_CONFIG_SOC_CY8C4045LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T411)、[`SB_CONFIG_SOC_CY8C4045LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T441)、[`SB_CONFIG_SOC_CY8C4045LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T451)、[`SB_CONFIG_SOC_CY8C4046LQI_T411`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T411)、[`SB_CONFIG_SOC_CY8C4046LQI_T441`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T441)、[`SB_CONFIG_SOC_CY8C4046LQI_T451`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T451)、[`SB_CONFIG_SOC_CY8C4025LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T412)、[`SB_CONFIG_SOC_CY8C4025LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T442)、[`SB_CONFIG_SOC_CY8C4025LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025LQI_T452)、[`SB_CONFIG_SOC_CY8C4026LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026LQI_T412)、[`SB_CONFIG_SOC_CY8C4026LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026LQI_T442)、[`SB_CONFIG_SOC_CY8C4045LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T412)、[`SB_CONFIG_SOC_CY8C4045LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T442)、[`SB_CONFIG_SOC_CY8C4045LQI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQI_T452)、[`SB_CONFIG_SOC_CY8C4045LQE_T1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQE_T1)、[`SB_CONFIG_SOC_CY8C4045LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045LQS_T1)、[`SB_CONFIG_SOC_CY8C4046LQI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T412)、[`SB_CONFIG_SOC_CY8C4046LQI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQI_T442)、[`SB_CONFIG_SOC_CY8C4046LQS_T1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQS_T1)、[`SB_CONFIG_SOC_CY8C4046LQQ_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046LQQ_T412)、[`SB_CONFIG_SOC_CY8C4025FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025FNI_T412)、[`SB_CONFIG_SOC_CY8C4025FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025FNI_T442)、[`SB_CONFIG_SOC_CY8C4025FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4025FNI_T452)、[`SB_CONFIG_SOC_CY8C4026FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026FNI_T412)、[`SB_CONFIG_SOC_CY8C4026FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4026FNI_T442)、[`SB_CONFIG_SOC_CY8C4045FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045FNI_T412)、[`SB_CONFIG_SOC_CY8C4045FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045FNI_T442)、[`SB_CONFIG_SOC_CY8C4045FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4045FNI_T452)、[`SB_CONFIG_SOC_CY8C4046FNI_T412`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046FNI_T412)、[`SB_CONFIG_SOC_CY8C4046FNI_T442`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046FNI_T442)、[`SB_CONFIG_SOC_CY8C4046FNI_T452`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4046FNI_T452)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`SB_CONFIG_SOC_CY8C4046LQI_T452`、`SB_CONFIG_SOC_CY8C4046LQE_T1`、`SB_CONFIG_SOC_CY8C4025LQI_T411`、`SB_CONFIG_SOC_CY8C4025LQI_T441`、`SB_CONFIG_SOC_CY8C4025LQI_T451`、`SB_CONFIG_SOC_CY8C4026LQI_T411`、`SB_CONFIG_SOC_CY8C4026LQI_T441`、`SB_CONFIG_SOC_CY8C4045LQI_T411`、`SB_CONFIG_SOC_CY8C4045LQI_T441`、`SB_CONFIG_SOC_CY8C4045LQI_T451`、`SB_CONFIG_SOC_CY8C4046LQI_T411`、`SB_CONFIG_SOC_CY8C4046LQI_T441`、`SB_CONFIG_SOC_CY8C4046LQI_T451`、`SB_CONFIG_SOC_CY8C4025LQI_T412`、`SB_CONFIG_SOC_CY8C4025LQI_T442`、`SB_CONFIG_SOC_CY8C4025LQI_T452`、`SB_CONFIG_SOC_CY8C4026LQI_T412`、`SB_CONFIG_SOC_CY8C4026LQI_T442`、`SB_CONFIG_SOC_CY8C4045LQI_T412`、`SB_CONFIG_SOC_CY8C4045LQI_T442`、`SB_CONFIG_SOC_CY8C4045LQI_T452`、`SB_CONFIG_SOC_CY8C4045LQE_T1`、`SB_CONFIG_SOC_CY8C4045LQS_T1`、`SB_CONFIG_SOC_CY8C4046LQI_T412`、`SB_CONFIG_SOC_CY8C4046LQI_T442`、`SB_CONFIG_SOC_CY8C4046LQS_T1`、`SB_CONFIG_SOC_CY8C4046LQQ_T412`、`SB_CONFIG_SOC_CY8C4025FNI_T412`、`SB_CONFIG_SOC_CY8C4025FNI_T442`、`SB_CONFIG_SOC_CY8C4025FNI_T452`、`SB_CONFIG_SOC_CY8C4026FNI_T412`、`SB_CONFIG_SOC_CY8C4026FNI_T442`、`SB_CONFIG_SOC_CY8C4045FNI_T412`、`SB_CONFIG_SOC_CY8C4045FNI_T442`、`SB_CONFIG_SOC_CY8C4045FNI_T452`、`SB_CONFIG_SOC_CY8C4046FNI_T412`、`SB_CONFIG_SOC_CY8C4046FNI_T442`、`SB_CONFIG_SOC_CY8C4046FNI_T452`。

<a id="SB_CONFIG_SOC_SERIES_PSOC4100SMAX"></a>

## 280.28 `SB_CONFIG_SOC_SERIES_PSOC4100SMAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4100Smax 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CY8C4149AZI_S598
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100smax/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100smax/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`SB_CONFIG_SOC_CY8C4149AZI_S598`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4149AZI_S598)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`SB_CONFIG_SOC_CY8C4149AZI_S598`。

<a id="SB_CONFIG_SOC_SERIES_PSOC4100TP"></a>

## 280.29 `SB_CONFIG_SOC_SERIES_PSOC4100TP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC4100tp 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CY8C4146LQI_T403
SB_CONFIG_SOC_CY8C4146AXI_T403
SB_CONFIG_SOC_CY8C4146AZI_T403
SB_CONFIG_SOC_CY8C4146AZI_T405
SB_CONFIG_SOC_CY8C4146LQI_T413
SB_CONFIG_SOC_CY8C4146AXI_T413
SB_CONFIG_SOC_CY8C4146AZI_T413
SB_CONFIG_SOC_CY8C4146AZI_T415
SB_CONFIG_SOC_CY8C4146LQI_T453
SB_CONFIG_SOC_CY8C4146AXI_T453
SB_CONFIG_SOC_CY8C4146AZI_T453
SB_CONFIG_SOC_CY8C4146AZI_T455
SB_CONFIG_SOC_CY8C4147LQI_T403
SB_CONFIG_SOC_CY8C4147AXI_T403
SB_CONFIG_SOC_CY8C4147AZI_T403
SB_CONFIG_SOC_CY8C4147AZI_T405
SB_CONFIG_SOC_CY8C4147LQI_T413
SB_CONFIG_SOC_CY8C4147AXI_T413
SB_CONFIG_SOC_CY8C4147AZI_T413
SB_CONFIG_SOC_CY8C4147AZI_T415
SB_CONFIG_SOC_CY8C4147LQI_T453
SB_CONFIG_SOC_CY8C4147AXI_T453
SB_CONFIG_SOC_CY8C4147AZI_T453
SB_CONFIG_SOC_CY8C4147AZI_T455
SB_CONFIG_SOC_CY8C4147LQI_T463
SB_CONFIG_SOC_CY8C4147AXI_T463
SB_CONFIG_SOC_CY8C4147AZI_T463
SB_CONFIG_SOC_CY8C4147AZI_T465
SB_CONFIG_SOC_CY8C4147LQI_T473
SB_CONFIG_SOC_CY8C4147AXI_T473
SB_CONFIG_SOC_CY8C4147AZI_T473
SB_CONFIG_SOC_CY8C4147AZI_T475
SB_CONFIG_SOC_CY8C4147LQQ_T493
SB_CONFIG_SOC_CY8C4147AXQ_T493
SB_CONFIG_SOC_CY8C4147AZQ_T493
SB_CONFIG_SOC_CY8C4147AZQ_T495
SB_CONFIG_SOC_CY8C4146AZQ_T413
SB_CONFIG_SOC_CY8C4146AZQ_T453
SB_CONFIG_SOC_CY8C4147AZQ_T415
SB_CONFIG_SOC_CY8C4147AZQ_T455
```

**定义位置（Location）**：[`soc/infineon/psoc4/psoc4100tp/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/psoc4/psoc4100tp/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`SB_CONFIG_SOC_CY8C4146LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146LQI_T403)、[`SB_CONFIG_SOC_CY8C4146AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AXI_T403)、[`SB_CONFIG_SOC_CY8C4146AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T403)、[`SB_CONFIG_SOC_CY8C4146AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T405)、[`SB_CONFIG_SOC_CY8C4146LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146LQI_T413)、[`SB_CONFIG_SOC_CY8C4146AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AXI_T413)、[`SB_CONFIG_SOC_CY8C4146AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T413)、[`SB_CONFIG_SOC_CY8C4146AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T415)、[`SB_CONFIG_SOC_CY8C4146LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146LQI_T453)、[`SB_CONFIG_SOC_CY8C4146AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AXI_T453)、[`SB_CONFIG_SOC_CY8C4146AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T453)、[`SB_CONFIG_SOC_CY8C4146AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZI_T455)、[`SB_CONFIG_SOC_CY8C4147LQI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQI_T403)、[`SB_CONFIG_SOC_CY8C4147AXI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXI_T403)、[`SB_CONFIG_SOC_CY8C4147AZI_T403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T403)、[`SB_CONFIG_SOC_CY8C4147AZI_T405`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T405)、[`SB_CONFIG_SOC_CY8C4147LQI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQI_T413)、[`SB_CONFIG_SOC_CY8C4147AXI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXI_T413)、[`SB_CONFIG_SOC_CY8C4147AZI_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T413)、[`SB_CONFIG_SOC_CY8C4147AZI_T415`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T415)、[`SB_CONFIG_SOC_CY8C4147LQI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQI_T453)、[`SB_CONFIG_SOC_CY8C4147AXI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXI_T453)、[`SB_CONFIG_SOC_CY8C4147AZI_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T453)、[`SB_CONFIG_SOC_CY8C4147AZI_T455`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T455)、[`SB_CONFIG_SOC_CY8C4147LQI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQI_T463)、[`SB_CONFIG_SOC_CY8C4147AXI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXI_T463)、[`SB_CONFIG_SOC_CY8C4147AZI_T463`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T463)、[`SB_CONFIG_SOC_CY8C4147AZI_T465`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T465)、[`SB_CONFIG_SOC_CY8C4147LQI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQI_T473)、[`SB_CONFIG_SOC_CY8C4147AXI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXI_T473)、[`SB_CONFIG_SOC_CY8C4147AZI_T473`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T473)、[`SB_CONFIG_SOC_CY8C4147AZI_T475`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZI_T475)、[`SB_CONFIG_SOC_CY8C4147LQQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147LQQ_T493)、[`SB_CONFIG_SOC_CY8C4147AXQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AXQ_T493)、[`SB_CONFIG_SOC_CY8C4147AZQ_T493`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZQ_T493)、[`SB_CONFIG_SOC_CY8C4147AZQ_T495`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZQ_T495)、[`SB_CONFIG_SOC_CY8C4146AZQ_T413`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZQ_T413)、[`SB_CONFIG_SOC_CY8C4146AZQ_T453`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4146AZQ_T453)、[`SB_CONFIG_SOC_CY8C4147AZQ_T415`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZQ_T415)、[`SB_CONFIG_SOC_CY8C4147AZQ_T455`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CY8C4147AZQ_T455)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`SB_CONFIG_SOC_CY8C4146LQI_T403`、`SB_CONFIG_SOC_CY8C4146AXI_T403`、`SB_CONFIG_SOC_CY8C4146AZI_T403`、`SB_CONFIG_SOC_CY8C4146AZI_T405`、`SB_CONFIG_SOC_CY8C4146LQI_T413`、`SB_CONFIG_SOC_CY8C4146AXI_T413`、`SB_CONFIG_SOC_CY8C4146AZI_T413`、`SB_CONFIG_SOC_CY8C4146AZI_T415`、`SB_CONFIG_SOC_CY8C4146LQI_T453`、`SB_CONFIG_SOC_CY8C4146AXI_T453`、`SB_CONFIG_SOC_CY8C4146AZI_T453`、`SB_CONFIG_SOC_CY8C4146AZI_T455`、`SB_CONFIG_SOC_CY8C4147LQI_T403`、`SB_CONFIG_SOC_CY8C4147AXI_T403`、`SB_CONFIG_SOC_CY8C4147AZI_T403`、`SB_CONFIG_SOC_CY8C4147AZI_T405`、`SB_CONFIG_SOC_CY8C4147LQI_T413`、`SB_CONFIG_SOC_CY8C4147AXI_T413`、`SB_CONFIG_SOC_CY8C4147AZI_T413`、`SB_CONFIG_SOC_CY8C4147AZI_T415`、`SB_CONFIG_SOC_CY8C4147LQI_T453`、`SB_CONFIG_SOC_CY8C4147AXI_T453`、`SB_CONFIG_SOC_CY8C4147AZI_T453`、`SB_CONFIG_SOC_CY8C4147AZI_T455`、`SB_CONFIG_SOC_CY8C4147LQI_T463`、`SB_CONFIG_SOC_CY8C4147AXI_T463`、`SB_CONFIG_SOC_CY8C4147AZI_T463`、`SB_CONFIG_SOC_CY8C4147AZI_T465`、`SB_CONFIG_SOC_CY8C4147LQI_T473`、`SB_CONFIG_SOC_CY8C4147AXI_T473`、`SB_CONFIG_SOC_CY8C4147AZI_T473`、`SB_CONFIG_SOC_CY8C4147AZI_T475`、`SB_CONFIG_SOC_CY8C4147LQQ_T493`、`SB_CONFIG_SOC_CY8C4147AXQ_T493`、`SB_CONFIG_SOC_CY8C4147AZQ_T493`、`SB_CONFIG_SOC_CY8C4147AZQ_T495`、`SB_CONFIG_SOC_CY8C4146AZQ_T413`、`SB_CONFIG_SOC_CY8C4146AZQ_T453`、`SB_CONFIG_SOC_CY8C4147AZQ_T415`、`SB_CONFIG_SOC_CY8C4147AZQ_T455`。

<a id="SB_CONFIG_SOC_SERIES_XMC4XXX"></a>

## 280.30 `SB_CONFIG_SOC_SERIES_XMC4XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC 4xxx 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INFINEON_XMC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_XMC4500
SB_CONFIG_SOC_XMC4700
SB_CONFIG_SOC_XMC4800
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INFINEON_XMC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INFINEON_XMC)、[`SB_CONFIG_SOC_XMC4500`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_XMC4500)、[`SB_CONFIG_SOC_XMC4700`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_XMC4700)、[`SB_CONFIG_SOC_XMC4800`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_XMC4800)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INFINEON_XMC`。

<a id="SB_CONFIG_SOC_XMC4500"></a>

## 280.31 `SB_CONFIG_SOC_XMC4500`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4500 片上系统配置（SoC）：`SOC_XMC4500`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XMC4XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_XMC45_RELAX_KIT
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_SERIES_XMC4XXX)、[`SB_CONFIG_BOARD_XMC45_RELAX_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XMC45_RELAX_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_XMC45_RELAX_KIT`。

<a id="SB_CONFIG_SOC_XMC4700"></a>

## 280.32 `SB_CONFIG_SOC_XMC4700`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4700 片上系统配置（SoC）：`SOC_XMC4700`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XMC4XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_XMC47_RELAX_KIT
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_SERIES_XMC4XXX)、[`SB_CONFIG_BOARD_XMC47_RELAX_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XMC47_RELAX_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_XMC47_RELAX_KIT`。

<a id="SB_CONFIG_SOC_XMC4800"></a>

## 280.33 `SB_CONFIG_SOC_XMC4800`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XMC4800 片上系统配置（SoC）：`SOC_XMC4800`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`soc/infineon/cat3/xmc4xxx/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/infineon/cat3/xmc4xxx/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XMC4XXX`](P280_soc_infineon_配置项参考.md#SB_CONFIG_SOC_SERIES_XMC4XXX)。

<!-- kconfig-navigation -->

[上一章](P279_soc_gd_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P281_soc_intel_配置项参考.md)
