---
id: learning.zephyr-docs.kconfig-reference.page-289
title: "`soc/nordic`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第289章\_`soc/nordic`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `soc/nordic` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_WITH_TFM"></a>

## 289.1 `CONFIG_BUILD_WITH_TFM`

原库同名定义共 3 条；本项为数据库第 3448 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

默认情况下，如果为开发板的非安全版本（Non-Secure version）构建，则启用 TF-M 构建，将其作为安全执行环境（Secure Execution Environment）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`soc/nordic/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_DMM_HEAP_CHUNKS"></a>

## 289.2 `CONFIG_DMM_HEAP_CHUNKS`

**提示（Prompt）**：DMM 堆中的分块数量（Number of chunks in the DMM heap）

**说明（Help）**

DMM 使用简化的堆（heap），通过 32 位掩码（mask）分配由连续分块（contiguous chunks）组成的所需缓冲区。如果 DMM 使用许多小缓冲区，分配可能失败。分块数量是在性能与粒度（granularity）之间的权衡，必须为 32 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_DMM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_DMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DMM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DMM`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_DMM_STATS"></a>

## 289.3 `CONFIG_DMM_STATS`

**提示（Prompt）**：使用统计（Usage statistics）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_DMM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_DMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DMM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DMM`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_APPROTECT_APPLICATION_PROTECTED"></a>

## 289.4 `CONFIG_GEN_UICR_APPROTECT_APPLICATION_PROTECTED`

**提示（Prompt）**：保护应用域访问端口（Protect application domain access port）

**说明（Help）**

启用后，禁用对应用域处理器（application domain processor）的调试访问，阻止调试器连接到应用内存、寄存器和调试功能。禁用此项时，启用完整调试访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR.APPROTECT：访问端口保护（Access Port Protection）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_APPROTECT_CORESIGHT_PROTECTED"></a>

## 289.5 `CONFIG_GEN_UICR_APPROTECT_CORESIGHT_PROTECTED`

**提示（Prompt）**：禁用 CoreSight 子系统（Disable CoreSight subsystem）

**说明（Help）**

启用后，禁用 CoreSight 子系统，阻止使用系统级跟踪功能（system level trace features）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR.APPROTECT：访问端口保护（Access Port Protection）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_APPROTECT_RADIOCORE_PROTECTED"></a>

## 289.6 `CONFIG_GEN_UICR_APPROTECT_RADIOCORE_PROTECTED`

**提示（Prompt）**：保护无线电内核访问端口（Protect radio core access port）

**说明（Help）**

启用后，禁用对无线电内核处理器（radio core processor）的调试访问，阻止调试器连接到无线电内核内存、寄存器和调试功能。禁用此项时，启用完整调试访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR.APPROTECT：访问端口保护（Access Port Protection）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_ERASEPROTECT"></a>

## 289.7 `CONFIG_GEN_UICR_ERASEPROTECT`

**提示（Prompt）**：UICR 擦除保护（UICR.ERASEPROTECT）

**说明（Help）**

启用后，阻止 ERASEALL 全部擦除操作。此选项在 Kconfig 中与 `UICR.LOCK` 互斥，以防意外同时启用两者。如果同时启用，UICR 将无法以任何方式修改。必要时，可以直接使用 `gen_uicr.py` 创建同时启用两者的配置。调用 `gen_uicr.py` 所用的命令可在构建目录中找到：

- 基于 Ninja 的构建：`build/uicr/build.ninja`。
- 基于 Make 的构建：`build/CMakefiles/gen_uicr.dir/build.make`。

向该命令添加 `--eraseprotect` 参数，可启用本选项对应的配置。注意，烧录生成的 UICR hex 文件后，将在设备整个寿命期内完全锁定 UICR，无法再作任何修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_GEN_UICR_LOCK && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_LOCK`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_LOCK)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_GENERATE_MPCCONF"></a>

## 289.8 `CONFIG_GEN_UICR_GENERATE_MPCCONF`

**提示（Prompt）**：生成 UICR 时同时生成 MPCCONF hex 文件（Generate MPCCONF hex）

**说明（Help）**

启用后，UICR 生成器会填充 `mpcconf_partition` 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_MPCCONF && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 的 MPC 配置（UICR.MPCCONF）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_MPCCONF`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_MPCCONF)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_GENERATE_PERIPHCONF"></a>

## 289.9 `CONFIG_GEN_UICR_GENERATE_PERIPHCONF`

**提示（Prompt）**：生成 UICR 时同时生成 PERIPHCONF hex 文件（Generate PERIPHCONF hex）

**说明（Help）**

启用后，UICR 生成器会填充 `periphconf_partition` 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_PERIPHCONF && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 外设配置（UICR.PERIPHCONF）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_PERIPHCONF`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_PERIPHCONF)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_IRONSIDE_SE_PERIPHCONF_REGISTERS_FILE"></a>

## 289.10 `CONFIG_GEN_UICR_IRONSIDE_SE_PERIPHCONF_REGISTERS_FILE`

**提示（Prompt）**：IronSide SE 外设配置寄存器文件（PERIPHCONF registers file）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
"${IRONSIDE_SUPPORT_DIR}/se/resources/periphconf_registers-nrf54h20_xxaa-v23.4.0+27.json" if CONFIG_SOC_NRF54H20
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:448`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L448)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_LOCK"></a>

## 289.11 `CONFIG_GEN_UICR_LOCK`

**提示（Prompt）**：UICR 锁定（UICR.LOCK）

**说明（Help）**

启用后，锁定 MRAM10 中 NVR0 页的全部内容，包括用户信息配置寄存器（UICR）和开发板信息配置寄存器（Board Information Configuration Registers，BICR）的所有值。锁定后，只能通过执行 ERASEALL 全部擦除操作修改 UICR。仅应在生产设备中启用此项，以防止未经授权的修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_MPCCONF"></a>

## 289.12 `CONFIG_GEN_UICR_MPCCONF`

**提示（Prompt）**：UICR 的 MPC 配置（UICR.MPCCONF）

**说明（Help）**

启用后，UICR 生成器会根据设备树中的 `mpcconf_partition` 配置 MPC 配置数据的位置。启用此项会使生成的 UICR 格式版本设为不低于 2.2，因此要求安装 IronSide SE v23.4.0+27 或更高版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

<a id="CONFIG_GEN_UICR_PERIPHCONF"></a>

## 289.13 `CONFIG_GEN_UICR_PERIPHCONF`

**提示（Prompt）**：UICR 外设配置（UICR.PERIPHCONF）

**说明（Help）**

启用后，UICR 生成器会根据设备树中的 `periphconf_partition` 配置外设配置数据（peripheral configuration data）的位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

<a id="CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE"></a>

## 289.14 `CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE`

**提示（Prompt）**：UICR 的 MPC 配置阶段策略（UICR.POLICY_MPCCONFSTAGE）

**说明（Help）**

设置 IronSide SE MPCCONF 服务 API 在启动时的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL
```

**可选项（Choices）**

```text
CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL
CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_INIT
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL)、[`CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_INIT`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_INIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_INIT"></a>

## 289.15 `CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_INIT`

**提示（Prompt）**：初始化阶段（Initialization stage）

**说明（Help）**

API 从初始化阶段（initialization stage）开始，此阶段允许更新全局域（global domain）的 MPC 配置。应用必须通过 `ironside_se_mpcconf_finish_init()` API 通知 IronSide SE，才能结束初始化。启用此策略选项会使生成的 UICR 格式版本设为不低于 2.2，因此要求安装 IronSide SE v23.4.0+27 或更高版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L398)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 的 MPC 配置阶段策略（UICR.POLICY_MPCCONFSTAGE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE)。

<a id="CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL"></a>

## 289.16 `CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE_NORMAL`

**提示（Prompt）**：正常运行阶段（Normal operation stage）

**说明（Help）**

API 从正常运行阶段（normal operation stage）开始，因此无需显式调用 API 来结束初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 的 MPC 配置阶段策略（UICR.POLICY_MPCCONFSTAGE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_MPCCONF_STAGE)。

<a id="CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE"></a>

## 289.17 `CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE`

**提示（Prompt）**：UICR 外设配置阶段策略（UICR.POLICY_PERIPHCONFSTAGE）

**说明（Help）**

设置 IronSide SE PERIPHCONF 服务 API 在启动时的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL
```

**可选项（Choices）**

```text
CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL
CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_INIT
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL)、[`CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_INIT`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_INIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_INIT"></a>

## 289.18 `CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_INIT`

**提示（Prompt）**：初始化阶段（Initialization stage）

**说明（Help）**

API 从初始化阶段（initialization stage）开始，此阶段允许写入 UICR PERIPHCONF 数据块（blob）支持的任意寄存器，不受基于 CPU 的限制。应用必须通过 `ironside_se_periphconf_finish_init()` API 通知 IronSide SE，才能结束初始化。启用此策略选项会使生成的 UICR 格式版本设为不低于 2.1，因此要求安装 IronSide SE v23.3.0+26 或更高版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 外设配置阶段策略（UICR.POLICY_PERIPHCONFSTAGE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE)。

<a id="CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL"></a>

## 289.19 `CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE_NORMAL`

**提示（Prompt）**：正常运行阶段（Normal operation stage）

**说明（Help）**

API 从正常运行阶段（normal operation stage）开始，因此无需显式调用 API 来结束初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 外设配置阶段策略（UICR.POLICY_PERIPHCONFSTAGE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_POLICY_PERIPHCONF_STAGE)。

<a id="CONFIG_GEN_UICR_PROTECTEDMEM"></a>

## 289.20 `CONFIG_GEN_UICR_PROTECTEDMEM`

**提示（Prompt）**：UICR 受保护内存（UICR.PROTECTEDMEM）

**说明（Help）**

启用后，UICR 生成器会配置受保护内存区域（protected memory region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_PROTECTEDMEM_SIZE_BYTES"></a>

## 289.21 `CONFIG_GEN_UICR_PROTECTEDMEM_SIZE_BYTES`

**提示（Prompt）**：受保护内存大小，单位为字节（Protected memory size）

**说明（Help）**

受保护内存区域（protected memory region）的大小，单位为字节。此值必须能被 4096（4 kiB）整除。如果定义了标签为 `protectedmem_partition` 的设备树节点，则从该节点获取大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_PROTECTEDMEM && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0 if n
4096
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 受保护内存（UICR.PROTECTEDMEM）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_PROTECTEDMEM`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_PROTECTEDMEM)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY"></a>

## 289.22 `CONFIG_GEN_UICR_SECONDARY`

**提示（Prompt）**：UICR 次级固件启用（UICR.SECONDARY.ENABLE）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

<a id="CONFIG_GEN_UICR_SECONDARY_GENERATE_MPCCONF"></a>

## 289.23 `CONFIG_GEN_UICR_SECONDARY_GENERATE_MPCCONF`

**提示（Prompt）**：生成 UICR 时同时生成 SECONDARY.MPCCONF hex 文件

**说明（Help）**

启用后，UICR 生成器会填充 `secondary_mpcconf_partition` 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_MPCCONF && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件 MPC 配置（UICR.SECONDARY.MPCCONF）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_MPCCONF`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_MPCCONF)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_GENERATE_PERIPHCONF"></a>

## 289.24 `CONFIG_GEN_UICR_SECONDARY_GENERATE_PERIPHCONF`

**提示（Prompt）**：生成 UICR 时同时生成 SECONDARY.PERIPHCONF hex 文件

**说明（Help）**

启用后，UICR 生成器会填充 `secondary_periphconf_partition` 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_PERIPHCONF && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件外设配置（UICR.SECONDARY.PERIPHCONF）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_PERIPHCONF`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PERIPHCONF)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_MPCCONF"></a>

## 289.25 `CONFIG_GEN_UICR_SECONDARY_MPCCONF`

**提示（Prompt）**：UICR 次级固件 MPC 配置（UICR.SECONDARY.MPCCONF）

**说明（Help）**

启用后，UICR 生成器会根据设备树中的 `secondary_mpcconf_partition` 配置次级固件（secondary firmware）的 MPC 配置数据位置。启用此项会使生成的 UICR 格式版本设为不低于 2.2，因此要求安装 IronSide SE v23.4.0+27 或更高版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE）

<a id="CONFIG_GEN_UICR_SECONDARY_PERIPHCONF"></a>

## 289.26 `CONFIG_GEN_UICR_SECONDARY_PERIPHCONF`

**提示（Prompt）**：UICR 次级固件外设配置（UICR.SECONDARY.PERIPHCONF）

**说明（Help）**

启用后，UICR 生成器会根据设备树中的 `secondary_periphconf_partition` 配置次级固件（secondary firmware）的外设配置数据位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE）

<a id="CONFIG_GEN_UICR_SECONDARY_PROCESSOR"></a>

## 289.27 `CONFIG_GEN_UICR_SECONDARY_PROCESSOR`

**提示（Prompt）**：次级处理器选择（Secondary processor selection）

**说明（Help）**

用于启动次级固件（secondary firmware）的处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION
```

**可选项（Choices）**

```text
CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION
CONFIG_GEN_UICR_SECONDARY_PROCESSOR_RADIOCORE
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION)、[`CONFIG_GEN_UICR_SECONDARY_PROCESSOR_RADIOCORE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PROCESSOR_RADIOCORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION"></a>

## 289.28 `CONFIG_GEN_UICR_SECONDARY_PROCESSOR_APPLICATION`

**提示（Prompt）**：应用处理器（APPLICATION processor）

**说明（Help）**

在应用处理器（APPLICATION processor）上启动次级固件（secondary firmware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_SECONDARY_PROCESSOR>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → 次级处理器选择（Secondary processor selection）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_PROCESSOR`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PROCESSOR)。

<a id="CONFIG_GEN_UICR_SECONDARY_PROCESSOR_RADIOCORE"></a>

## 289.29 `CONFIG_GEN_UICR_SECONDARY_PROCESSOR_RADIOCORE`

**提示（Prompt）**：无线电内核处理器（RADIOCORE processor）

**说明（Help）**

在无线电内核处理器（RADIOCORE processor）上启动次级固件（secondary firmware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_SECONDARY_PROCESSOR>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → 次级处理器选择（Secondary processor selection）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_PROCESSOR`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PROCESSOR)。

<a id="CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM"></a>

## 289.30 `CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM`

**提示（Prompt）**：UICR 次级固件受保护内存（UICR.SECONDARY.PROTECTEDMEM）

**说明（Help）**

启用后，UICR 生成器会配置次级固件（secondary firmware）的受保护内存区域（protected memory region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM_SIZE_BYTES"></a>

## 289.31 `CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM_SIZE_BYTES`

**提示（Prompt）**：次级受保护内存大小，单位为字节（Secondary protected memory size）

**说明（Help）**

次级受保护内存区域（secondary protected memory region）的大小，单位为字节。此值必须能被 4096（4 kiB）整除。如果定义了标签为 `secondary_protectedmem_partition` 的设备树节点，则从该节点获取大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0 if n
4096
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件受保护内存（UICR.SECONDARY.PROTECTEDMEM）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_PROTECTEDMEM)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER"></a>

## 289.32 `CONFIG_GEN_UICR_SECONDARY_TRIGGER`

**提示（Prompt）**：UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**说明（Help）**

启用后，配置自动触发条件（automatic triggers），使 IronSide SE 根据特定复位原因启动次级固件（secondary firmware），而非主固件（primary firmware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONLOCKUP"></a>

## 289.33 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONLOCKUP`

**提示（Prompt）**：应用域 CPU 锁死复位触发（Application domain CPU lockup reset）

**说明（Help）**

当应用域（Application domain）CPU 锁死（lockup）导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONWDT0"></a>

## 289.34 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONWDT0`

**提示（Prompt）**：应用域看门狗 0 复位触发（Application domain watchdog 0 reset）

**说明（Help）**

当应用域（Application domain）看门狗 0 导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:283`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L283)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONWDT1"></a>

## 289.35 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_APPLICATIONWDT1`

**提示（Prompt）**：应用域看门狗 1 复位触发（Application domain watchdog 1 reset）

**说明（Help）**

当应用域（Application domain）看门狗 1 导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCORELOCKUP"></a>

## 289.36 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCORELOCKUP`

**提示（Prompt）**：无线电内核 CPU 锁死复位触发（Radio core CPU lockup reset）

**说明（Help）**

当无线电内核（Radio core）CPU 锁死（lockup）导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L308)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCOREWDT0"></a>

## 289.37 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCOREWDT0`

**提示（Prompt）**：无线电内核看门狗 0 复位触发（Radio core watchdog 0 reset）

**说明（Help）**

当无线电内核（Radio core）看门狗 0 导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCOREWDT1"></a>

## 289.38 `CONFIG_GEN_UICR_SECONDARY_TRIGGER_RADIOCOREWDT1`

**提示（Prompt）**：无线电内核看门狗 1 复位触发（Radio core watchdog 1 reset）

**说明（Help）**

当无线电内核（Radio core）看门狗 1 导致复位时，启动次级固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_TRIGGER && CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件启用（UICR.SECONDARY.ENABLE） → UICR 次级固件触发条件（UICR.SECONDARY.TRIGGER）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_TRIGGER`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_TRIGGER)、[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_WDTSTART"></a>

## 289.39 `CONFIG_GEN_UICR_SECONDARY_WDTSTART`

**提示（Prompt）**：UICR 次级固件看门狗启动（UICR.SECONDARY.WDTSTART）

**说明（Help）**

启用后，UICR 生成器会配置看门狗定时器（watchdog timer），使其在次级固件启动前自动开始运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_WDTSTART_CRV"></a>

## 289.40 `CONFIG_GEN_UICR_SECONDARY_WDTSTART_CRV`

**提示（Prompt）**：次级看门狗初始计数器重载值（Counter Reload Value，CRV）

**说明（Help）**

次级看门狗定时器（secondary watchdog timer）的初始计数器重载值（Counter Reload Value，CRV）。此值决定看门狗超时周期。为确保看门狗正常工作，必须至少为 15（`0xF`）。默认值 65535 产生 2 秒超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_WDTSTART && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
65535
```

**取值范围（Ranges）**

```text
[15, 4294967295]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件看门狗启动（UICR.SECONDARY.WDTSTART）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_WDTSTART`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE"></a>

## 289.41 `CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE`

**提示（Prompt）**：次级看门狗定时器实例（Secondary watchdog timer instance）

**说明（Help）**

选择供次级固件（secondary firmware）使用的看门狗定时器实例（watchdog timer instance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SECONDARY_WDTSTART && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0
```

**可选项（Choices）**

```text
CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0
CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT1
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件看门狗启动（UICR.SECONDARY.WDTSTART）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_WDTSTART`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0)、[`CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT1`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0"></a>

## 289.42 `CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT0`

**提示（Prompt）**：看门狗定时器 0（WDT0）

**说明（Help）**

为次级固件使用看门狗定时器实例 0（watchdog timer instance 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件看门狗启动（UICR.SECONDARY.WDTSTART） → 次级看门狗定时器实例（Secondary watchdog timer instance）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE)。

<a id="CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT1"></a>

## 289.43 `CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE_WDT1`

**提示（Prompt）**：看门狗定时器 1（WDT1）

**说明（Help）**

为次级固件使用看门狗定时器实例 1（watchdog timer instance 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 次级固件看门狗启动（UICR.SECONDARY.WDTSTART） → 次级看门狗定时器实例（Secondary watchdog timer instance）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SECONDARY_WDTSTART_INSTANCE)。

<a id="CONFIG_GEN_UICR_SECURESTORAGE"></a>

## 289.44 `CONFIG_GEN_UICR_SECURESTORAGE`

**提示（Prompt）**：UICR 安全存储（UICR.SECURESTORAGE）

**说明（Help）**

启用后，UICR 生成器会根据设备树分区配置安全存储区域（secure storage region）。使用以下设备树分区：

- `secure_storage_partition`：主安全存储分区，必需。
- `cpuapp_crypto_partition`：应用处理器加密存储，可选。
- `cpurad_crypto_partition`：无线电内核加密存储，可选。
- `cpuapp_its_partition`：应用处理器内部可信存储，可选。
- `cpurad_its_partition`：无线电内核内部可信存储，可选。

要求：

- `secure_storage_partition` 的地址和大小必须按 4KB 对齐。
- 所有子分区必须为 1KB 的整数倍，并连续布局、不留空隙。
- 必须至少定义一个子分区。
- 子分区大小之和必须等于 `secure_storage_partition` 的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGIONS"></a>

## 289.45 `CONFIG_GEN_UICR_SNAPSHOT_REGIONS`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**说明（Help）**

启用后，UICR 生成器会配置 Kconfig 指定的快照区域（snapshot regions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54H && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_0"></a>

## 289.46 `CONFIG_GEN_UICR_SNAPSHOT_REGION_0`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_0_ADDRESS"></a>

## 289.47 `CONFIG_GEN_UICR_SNAPSHOT_REGION_0_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_0 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_0`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_0)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_0_SIZE_BYTES"></a>

## 289.48 `CONFIG_GEN_UICR_SNAPSHOT_REGION_0_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_0 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_0`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_0)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_1"></a>

## 289.49 `CONFIG_GEN_UICR_SNAPSHOT_REGION_1`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_1_ADDRESS"></a>

## 289.50 `CONFIG_GEN_UICR_SNAPSHOT_REGION_1_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_1 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_1`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_1)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_1_SIZE_BYTES"></a>

## 289.51 `CONFIG_GEN_UICR_SNAPSHOT_REGION_1_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_1 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_1`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_1)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_2"></a>

## 289.52 `CONFIG_GEN_UICR_SNAPSHOT_REGION_2`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_2_ADDRESS"></a>

## 289.53 `CONFIG_GEN_UICR_SNAPSHOT_REGION_2_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_2 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_2`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_2)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_2_SIZE_BYTES"></a>

## 289.54 `CONFIG_GEN_UICR_SNAPSHOT_REGION_2_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_2 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_2`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_2)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_3"></a>

## 289.55 `CONFIG_GEN_UICR_SNAPSHOT_REGION_3`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_3_ADDRESS"></a>

## 289.56 `CONFIG_GEN_UICR_SNAPSHOT_REGION_3_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_3 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_3`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_3)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_3_SIZE_BYTES"></a>

## 289.57 `CONFIG_GEN_UICR_SNAPSHOT_REGION_3_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_3 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_3`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_3)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_4"></a>

## 289.58 `CONFIG_GEN_UICR_SNAPSHOT_REGION_4`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_4_ADDRESS"></a>

## 289.59 `CONFIG_GEN_UICR_SNAPSHOT_REGION_4_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_4 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_4`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_4)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_4_SIZE_BYTES"></a>

## 289.60 `CONFIG_GEN_UICR_SNAPSHOT_REGION_4_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_4 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_4`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_4)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_5"></a>

## 289.61 `CONFIG_GEN_UICR_SNAPSHOT_REGION_5`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_5_ADDRESS"></a>

## 289.62 `CONFIG_GEN_UICR_SNAPSHOT_REGION_5_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_5 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_5`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_5)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_5_SIZE_BYTES"></a>

## 289.63 `CONFIG_GEN_UICR_SNAPSHOT_REGION_5_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_5 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_5`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_5)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_6"></a>

## 289.64 `CONFIG_GEN_UICR_SNAPSHOT_REGION_6`

**提示（Prompt）**：UICR 快照区域（UICR.SNAPSHOT region）

**说明（Help）**

启用后，配置一个 UICR 快照区域（UICR.SNAPSHOT region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_6_ADDRESS"></a>

## 289.65 `CONFIG_GEN_UICR_SNAPSHOT_REGION_6_ADDRESS`

**提示（Prompt）**：UICR 快照区域起始地址（UICR.SNAPSHOT region start address）

**说明（Help）**

UICR 快照区域（UICR.SNAPSHOT region）的起始地址，必须按 1 KB 边界对齐。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_6 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[0x0e030000, 0x0e1ff000]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_6`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_6)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_SNAPSHOT_REGION_6_SIZE_BYTES"></a>

## 289.66 `CONFIG_GEN_UICR_SNAPSHOT_REGION_6_SIZE_BYTES`

**提示（Prompt）**：UICR 快照区域大小，单位为字节（UICR.SNAPSHOT region size）

**说明（Help）**

快照区域（snapshot region）的大小，单位为字节，必须为 1024 的倍数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_SNAPSHOT_REGION_6 && CONFIG_GEN_UICR_SNAPSHOT_REGIONS && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[1024, 1048576]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.template.gen_uicr_snapshot_region#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 快照区域（UICR.SNAPSHOT.REGIONS） → UICR 快照区域（UICR.SNAPSHOT region）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_SNAPSHOT_REGION_6`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGION_6)、[`CONFIG_GEN_UICR_SNAPSHOT_REGIONS`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_SNAPSHOT_REGIONS)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_WDTSTART"></a>

## 289.67 `CONFIG_GEN_UICR_WDTSTART`

**提示（Prompt）**：UICR 看门狗启动（UICR.WDTSTART）

**说明（Help）**

启用后，UICR 生成器会配置应用域看门狗定时器（application domain watchdog timer），使其在应用内核启动前自动开始运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options）

**配置项引用（Symbol References）**：[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_WDTSTART_CRV"></a>

## 289.68 `CONFIG_GEN_UICR_WDTSTART_CRV`

**提示（Prompt）**：初始计数器重载值（Counter Reload Value，CRV）

**说明（Help）**

看门狗定时器（watchdog timer）的初始计数器重载值（Counter Reload Value，CRV）。此值决定看门狗超时周期。为确保看门狗正常工作，必须至少为 15（`0xF`）。默认值 65535 产生 2 秒超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_WDTSTART && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
65535
```

**取值范围（Ranges）**

```text
[15, 4294967295]
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 看门狗启动（UICR.WDTSTART）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_WDTSTART`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_WDTSTART_INSTANCE"></a>

## 289.69 `CONFIG_GEN_UICR_WDTSTART_INSTANCE`

**提示（Prompt）**：看门狗定时器实例（Watchdog timer instance）

**说明（Help）**

选择要使用的看门狗定时器实例（watchdog timer instance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_UICR_WDTSTART && CONFIG_IS_GEN_UICR_IMAGE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0
```

**可选项（Choices）**

```text
CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0
CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT1
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 看门狗启动（UICR.WDTSTART）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_WDTSTART`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART)、[`CONFIG_IS_GEN_UICR_IMAGE`](P289_soc_nordic_配置项参考_1.md#CONFIG_IS_GEN_UICR_IMAGE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0)、[`CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT1`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0"></a>

## 289.70 `CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT0`

**提示（Prompt）**：看门狗定时器 0（WDT0）

**说明（Help）**

使用看门狗定时器实例 0（watchdog timer instance 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_WDTSTART_INSTANCE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 看门狗启动（UICR.WDTSTART） → 看门狗定时器实例（Watchdog timer instance）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_WDTSTART_INSTANCE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART_INSTANCE)。

<a id="CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT1"></a>

## 289.71 `CONFIG_GEN_UICR_WDTSTART_INSTANCE_WDT1`

**提示（Prompt）**：看门狗定时器 1（WDT1）

**说明（Help）**

使用看门狗定时器实例 1（watchdog timer instance 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_UICR_WDTSTART_INSTANCE>
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig.gen_uicr:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig.gen_uicr#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → UICR 生成器镜像标识，仅供参考，请勿更改（image indicator） → 用户信息配置寄存器生成器选项（UICR generator options） → UICR 看门狗启动（UICR.WDTSTART） → 看门狗定时器实例（Watchdog timer instance）

**配置项引用（Symbol References）**：[`CONFIG_GEN_UICR_WDTSTART_INSTANCE`](P289_soc_nordic_配置项参考_1.md#CONFIG_GEN_UICR_WDTSTART_INSTANCE)。

<a id="CONFIG_GPPI_EXT_ALLOCATOR"></a>

## 289.72 `CONFIG_GPPI_EXT_ALLOCATOR`

**提示（Prompt）**：通用可编程外设互连外部分配器（GPPI external allocator）

**说明（Help）**

启用 GPPI 外部分配器的服务器角色（server role）。服务器会注册一个进程间通信端点（IPC endpoint），用于跨内核 GPPI 资源分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE && CONFIG_NRFX_GPPI && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE)、[`CONFIG_NRFX_GPPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GPPI_EXT_ALLOCATOR_CLI"></a>

## 289.73 `CONFIG_GPPI_EXT_ALLOCATOR_CLI`

**提示（Prompt）**：GPPI 外部分配器客户端（external allocator client）

**说明（Help）**

启用 GPPI 外部分配器的客户端角色（client role）。客户端内核提供外部 GPPI 分配函数，通过进程间通信（IPC）将请求委托给服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE && CONFIG_NRFX_GPPI && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI_EXT_ALLOCATOR
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE)、[`CONFIG_NRFX_GPPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRFX_GPPI_EXT_ALLOCATOR`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI_EXT_ALLOCATOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_GPPI_EXT_ALLOCATOR_TIMEOUT"></a>

## 289.74 `CONFIG_GPPI_EXT_ALLOCATOR_TIMEOUT`

**提示（Prompt）**：GPPI 外部分配器 IPC 超时，单位为毫秒（IPC timeout）

**说明（Help）**

GPPI 外部分配器的 IPC 信号量（semaphore）和互斥锁（mutex）操作超时，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_GPPI_EXT_ALLOCATOR || CONFIG_GPPI_EXT_ALLOCATOR_CLI) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GPPI_EXT_ALLOCATOR`](P289_soc_nordic_配置项参考_1.md#CONFIG_GPPI_EXT_ALLOCATOR)、[`CONFIG_GPPI_EXT_ALLOCATOR_CLI`](P289_soc_nordic_配置项参考_1.md#CONFIG_GPPI_EXT_ALLOCATOR_CLI)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_IS_GEN_UICR_IMAGE"></a>

## 289.75 `CONFIG_IS_GEN_UICR_IMAGE`

**提示（Prompt）**：UICR 生成器镜像标识，仅供参考，请勿更改（image indicator）

**说明（Help）**

构建 `gen_uicr` 镜像时自动设置此 Kconfig。它表示这是 UICR 生成器工具镜像（generator utility image），并启用 UICR 生成器配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_IS_IRONSIDE_SE_SECONDARY_IMAGE"></a>

## 289.76 `CONFIG_IS_IRONSIDE_SE_SECONDARY_IMAGE`

**提示（Prompt）**：IronSide SE 次级镜像标识，仅供参考，请勿更改（secondary image indicator）

**说明（Help）**

此 Kconfig 由 Sysbuild 设置，表示该镜像是 IronSide SE 的次级固件（secondary firmware）。UICR 生成系统使用此信息确定要采用哪个 PERIPHCONF 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/uicr/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/uicr/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_MRAM_LATENCY"></a>

## 289.77 `CONFIG_MRAM_LATENCY`

**提示（Prompt）**：磁阻 RAM 延迟管理器（MRAM latency manager）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_MRAM_SERVICE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_ONOFF
CONFIG_NRFS_MRAM_SERVICE_ENABLED
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_FLASH_NRF_MRAM
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_MRAM_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_MRAM_SERVICE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_ONOFF`](P198_lib_配置项参考_2.md#CONFIG_ONOFF)、[`CONFIG_NRFS_MRAM_SERVICE_ENABLED`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_MRAM_SERVICE_ENABLED)、[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_MRAM_SERVICE`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_MRAM_LATENCY_AUTO_REQ"></a>

## 289.78 `CONFIG_MRAM_LATENCY_AUTO_REQ`

**提示（Prompt）**：启动时请求无延迟 MRAM（MRAM without latency）

**说明（Help）**

启用后，在初始化期间请求无延迟 MRAM 配置（MRAM configuration without latency），并一直保持启用，直到 `mram_latency` API 的使用者调用 `mram_no_latency_sync_release()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MRAM_LATENCY && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY`](P289_soc_nordic_配置项参考_1.md#CONFIG_MRAM_LATENCY)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_MRAM_LATENCY_SYNC_TIMEOUT"></a>

## 289.79 `CONFIG_MRAM_LATENCY_SYNC_TIMEOUT`

**提示（Prompt）**：同步请求超时（Timeout in synchronous request）

**说明（Help）**

超时时间（timeout）以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MRAM_LATENCY && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY`](P289_soc_nordic_配置项参考_1.md#CONFIG_MRAM_LATENCY)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NORDIC_VPR_DEEPSLEEP"></a>

## 289.80 `CONFIG_NORDIC_VPR_DEEPSLEEP`

**提示（Prompt）**：深度睡眠（Deep sleep）

**说明（Help）**

仅在 nRF54H20 上，深度睡眠（deep sleep）可使系统开启但空闲状态（system-on-idle）的电流低于 5 uA。唤醒时间与睡眠模式（sleep mode）相近。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPUPPR && <choice CONFIG_NORDIC_VPR_SLEEP_MODE>
```

**定义位置（Location）**：[`soc/nordic/common/vpr/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/vpr/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 默认睡眠模式（Default sleep mode）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_NORDIC_VPR_SLEEP_MODE`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_SLEEP_MODE)。

<a id="CONFIG_NORDIC_VPR_HIBERNATE"></a>

## 289.81 `CONFIG_NORDIC_VPR_HIBERNATE`

**提示（Prompt）**：休眠（Hibernation）

**说明（Help）**

此模式功耗最低；在 nRF54H20 以外的目标上，要使系统开启但空闲状态（system-on-idle）的电流低于 5 uA，必须使用此模式。唤醒时间略长，额外增加 1 us。休眠（Hibernation）使用一个 RAM 块存储 VPR 状态，父内核（parent core）必须配置该内存，使其保持供电并保留内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF54H && !CONFIG_SOC_SERIES_NRF92 && <choice CONFIG_NORDIC_VPR_SLEEP_MODE>
```

**定义位置（Location）**：[`soc/nordic/common/vpr/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/vpr/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 默认睡眠模式（Default sleep mode）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_NORDIC_VPR_SLEEP_MODE`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_SLEEP_MODE)。

<a id="CONFIG_NORDIC_VPR_SLEEP"></a>

## 289.82 `CONFIG_NORDIC_VPR_SLEEP`

**提示（Prompt）**：睡眠（Sleep）

**说明（Help）**

功耗明显更高，但唤醒时间（wake up time）很短。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_SLEEP_MODE>
```

**定义位置（Location）**：[`soc/nordic/common/vpr/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/vpr/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 默认睡眠模式（Default sleep mode）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_SLEEP_MODE`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_SLEEP_MODE)。

<a id="CONFIG_NORDIC_VPR_SLEEP_MODE"></a>

## 289.83 `CONFIG_NORDIC_VPR_SLEEP_MODE`

**提示（Prompt）**：默认睡眠模式（Default sleep mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_CORE_NORDIC_VPR && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_NORDIC_VPR_SLEEP if CONFIG_SOC_NRF54H20_CPUFLPR
CONFIG_NORDIC_VPR_DEEPSLEEP if CONFIG_SOC_NRF54H20_CPUPPR
CONFIG_NORDIC_VPR_HIBERNATE
```

**可选项（Choices）**

```text
CONFIG_NORDIC_VPR_SLEEP
CONFIG_NORDIC_VPR_DEEPSLEEP
CONFIG_NORDIC_VPR_HIBERNATE
```

**定义位置（Location）**：[`soc/nordic/common/vpr/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/vpr/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CORE_NORDIC_VPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NORDIC_VPR_SLEEP`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_SLEEP)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUFLPR)、[`CONFIG_NORDIC_VPR_DEEPSLEEP`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_DEEPSLEEP)、[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_NORDIC_VPR_HIBERNATE`](P289_soc_nordic_配置项参考_1.md#CONFIG_NORDIC_VPR_HIBERNATE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF52_ANOMALY_109_WORKAROUND"></a>

## 289.84 `CONFIG_NRF52_ANOMALY_109_WORKAROUND`

**提示（Prompt）**：异常 109 规避措施（Anomaly 109 workaround）

**说明（Help）**

由于异常 109（Anomaly 109），这些外设发送的第一个字节有时不正确。当系统进入 IDLE 状态并停止 64MHz 时钟，同时使用 DMA 的外设启动时，会发生此问题。此异常适用于直到修订版“3”为止的 IC 修订版；原文将“3”称为最新修订版。译注：修订版范围按本次官方文档快照保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF52832 && (CONFIG_NRFX_SPIS || CONFIG_NRFX_SPIM || CONFIG_NRFX_TWIM || CONFIG_NRFX_PWM) && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_NRFX_SPIS`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPIS)、[`CONFIG_NRFX_SPIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPIM)、[`CONFIG_NRFX_TWIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWIM)、[`CONFIG_NRFX_PWM`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_PWM)、[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF52832`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF52_ANOMALY_109_WORKAROUND_EGU_INSTANCE"></a>

## 289.85 `CONFIG_NRF52_ANOMALY_109_WORKAROUND_EGU_INSTANCE`

**提示（Prompt）**：异常 109 规避措施使用的事件发生器实例（EGU instance）

**说明（Help）**

nRF52 异常 109 的 PWM 规避措施所使用的事件发生器（EGU）实例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF52_ANOMALY_109_WORKAROUND && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 5]
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 异常 109 规避措施（Anomaly 109 workaround）

**配置项引用（Symbol References）**：[`CONFIG_NRF52_ANOMALY_109_WORKAROUND`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF52_ANOMALY_109_WORKAROUND)、[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF52_ANOMALY_132_DELAY_US"></a>

## 289.86 `CONFIG_NRF52_ANOMALY_132_DELAY_US`

**提示（Prompt）**：异常 132 规避延迟，单位为微秒（Anomaly 132 workaround delay）

**说明（Help）**

由于异常 132（Anomaly 132），低频 RC 时钟源（LF RC source）停止后，如果在特定时间窗口内（230 us～330 us）重新启动，可能无法启动。软件复位也会停止时钟，因此若在该窗口内初始化时钟，重启时也可能无法启动。在启动低频时钟前加入延迟，可确保不满足异常触发条件。延迟应足够长，使时钟在复位后超过 330 us 才启动。

使用晶体振荡器（XO）时，低频时钟最初由 RC 启动，然后无缝切换到启动时间更长的 XO，因此仍可能需要此规避措施，具体取决于应用。其他驱动初始化会增加总初始化时间，因此可相应缩短此延迟。将延迟设为 0 可禁用规避措施。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
NRF52_ANOMALY_132_WORKAROUND && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
330
```

**取值范围（Ranges）**

```text
[0, 330]
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF52_ANOMALY_198_WORKAROUND"></a>

## 289.87 `CONFIG_NRF52_ANOMALY_198_WORKAROUND`

**提示（Prompt）**：异常 198 规避措施（Anomaly 198 workaround）

**说明（Help）**

此异常适用于从“Engineering B”到“3”的 IC 修订版；原文将“3”称为最新修订版。译注：修订版范围按本次官方文档快照保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_NRF52_ANOMALY_219_WORKAROUND"></a>

## 289.88 `CONFIG_NRF52_ANOMALY_219_WORKAROUND`

**提示（Prompt）**：异常 219 规避措施（Anomaly 219 workaround）

**说明（Help）**

由于异常 219（Anomaly 219），在 400 kHz 下 SCL 时钟的低电平持续时间过短，无法满足 I2C 规范。此规避措施将 I2C 频率改为 390 kHz，而非 400 kHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TWIM && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TWIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWIM)、[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF52_ANOMALY_58_WORKAROUND"></a>

## 289.89 `CONFIG_NRF52_ANOMALY_58_WORKAROUND`

**提示（Prompt）**：异常 58 规避措施（Anomaly 58 workaround）

**说明（Help）**

此异常会使 SPI 主机外设（SPIM）在请求传输 1 字节时，时钟输出 2 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF52832 && CONFIG_NRFX_SPIM && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_NRFX_SPIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPIM)、[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF52832`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF53_SYNC_RTC"></a>

## 289.90 `CONFIG_NRF53_SYNC_RTC`

**提示（Prompt）**：实时时钟同步（RTC clock synchronization）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_RTC_TIMER && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && !CONFIG_IS_BOOTLOADER && (CONFIG_SOC_NRF53_CPUNET_ENABLE || CONFIG_SOC_NRF5340_CPUNET)
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
CONFIG_MBOX if !CONFIG_IPM
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.sync_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.sync_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_IS_BOOTLOADER`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_IS_BOOTLOADER)、[`CONFIG_SOC_NRF53_CPUNET_ENABLE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_CPUNET_ENABLE)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_NRFX_GPPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_NRF53_SYNC_RTC_INIT_PRIORITY"></a>

## 289.91 `CONFIG_NRF53_SYNC_RTC_INIT_PRIORITY`

**提示（Prompt）**：nRF53 同步 RTC 初始化优先级（Synchronized RTC init priority）

**说明（Help）**

nRF53 同步实时时钟（Synchronized RTC）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF53_SYNC_RTC && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.sync_rtc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.sync_rtc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization）

**配置项引用（Symbol References）**：[`CONFIG_NRF53_SYNC_RTC`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF53_SYNC_RTC_IPM_IN"></a>

## 289.92 `CONFIG_NRF53_SYNC_RTC_IPM_IN`

**提示（Prompt）**：从应用内核到网络内核的处理器间消息通道（IPM channel from APP to NET）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF53_SYNC_RTC && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
8 if CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP
7
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.sync_rtc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.sync_rtc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization）

**配置项引用（Symbol References）**：[`CONFIG_NRF53_SYNC_RTC`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP`。

<a id="CONFIG_NRF53_SYNC_RTC_IPM_OUT"></a>

## 289.93 `CONFIG_NRF53_SYNC_RTC_IPM_OUT`

**提示（Prompt）**：从应用内核到网络内核的处理器间消息通道（IPM channel from APP to NET）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF53_SYNC_RTC && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
7 if CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP
8
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.sync_rtc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.sync_rtc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization）

**配置项引用（Symbol References）**：[`CONFIG_NRF53_SYNC_RTC`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_COMPATIBLE_NRF5340_CPUAPP`。

<a id="CONFIG_NRF53_SYNC_RTC_LOG_TIMESTAMP"></a>

## 289.94 `CONFIG_NRF53_SYNC_RTC_LOG_TIMESTAMP`

**提示（Prompt）**：使用同步 RTC 作为日志时间戳（logging timestamp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF53_SYNC_RTC && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.sync_rtc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.sync_rtc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization）

**配置项引用（Symbol References）**：[`CONFIG_NRF53_SYNC_RTC`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF91_ANOMALY_36_WORKAROUND"></a>

## 289.95 `CONFIG_NRF91_ANOMALY_36_WORKAROUND`

**提示（Prompt）**：异常 36 规避措施（Anomaly 36 workaround）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF91 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_ACL_FLASH_REGION_SIZE"></a>

## 289.96 `CONFIG_NRF_ACL_FLASH_REGION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_ACL 外设的 Flash 区域大小（FLASH region size）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_ACL && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`soc/nordic/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_ACL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_ACL)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_ACL`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_APPROTECT_DISABLE"></a>

## 289.97 `CONFIG_NRF_APPROTECT_DISABLE`

**提示（Prompt）**：禁用（Disable）

**说明（Help）**

选择此项时，`SystemInit()` 禁用访问端口保护机制（AP-Protect），允许调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54L_CPUAPP_COMMON && <choice CONFIG_NRF_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 访问端口保护处理（AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_NRF_APPROTECT_HANDLING`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_HANDLING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF54L_CPUAPP_COMMON`。

<a id="CONFIG_NRF_APPROTECT_HANDLING"></a>

## 289.98 `CONFIG_NRF_APPROTECT_HANDLING`

**提示（Prompt）**：访问端口保护处理（AP-Protect handling）

**说明（Help）**

指定 `SystemInit()` 函数如何处理访问端口保护机制（AP-Protect）。此选择不适用于 nRF9160 及采用较旧硬件构建代码（HW build codes）的 nRF52 系列器件；这些器件的 AP-Protect 完全由硬件控制，即由 `UICR.APPROTECT` 寄存器控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF52 || CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_NRF54L_CPUAPP_COMMON || CONFIG_SOC_SERIES_NRF91) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_NRF_APPROTECT_DISABLE if CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_NRF_APPROTECT_USE_UICR
```

**可选项（Choices）**

```text
CONFIG_NRF_APPROTECT_DISABLE
CONFIG_NRF_APPROTECT_USE_UICR
CONFIG_NRF_APPROTECT_LOCK
CONFIG_NRF_APPROTECT_USER_HANDLING
```

**定义位置（Location）**：[`soc/nordic/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_APPROTECT_DISABLE`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_DISABLE)、[`CONFIG_NRF_APPROTECT_USE_UICR`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_APPROTECT_USE_UICR)、[`CONFIG_NRF_APPROTECT_LOCK`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_LOCK)、[`CONFIG_NRF_APPROTECT_USER_HANDLING`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_USER_HANDLING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_APPROTECT_LOCK"></a>

## 289.99 `CONFIG_NRF_APPROTECT_LOCK`

**提示（Prompt）**：锁定（Lock）

**说明（Help）**

选择此项时，`SystemInit()` 锁定访问端口保护机制（AP-Protect），使调试器持续无法访问设备。只有通过控制访问端口（CTRL-AP）执行 ERASEALL 全部擦除操作，才能恢复访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 访问端口保护处理（AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_NRF_APPROTECT_HANDLING`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_HANDLING)。

<a id="CONFIG_NRF_APPROTECT_USER_HANDLING"></a>

## 289.100 `CONFIG_NRF_APPROTECT_USER_HANDLING`

**提示（Prompt）**：允许用户处理（Allow user handling）

**说明（Help）**

选择此项时，`SystemInit()` 不触碰访问端口保护机制（AP-Protect）。用户代码可以在后续阶段处理它，例如实现经过认证的调试（authenticated debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF52 && <choice CONFIG_NRF_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 访问端口保护处理（AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_NRF_APPROTECT_HANDLING`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_HANDLING)。

<!-- kconfig-navigation -->

[上一章](P288_soc_neorv32_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P290_soc_nordic_配置项参考_2.md)
