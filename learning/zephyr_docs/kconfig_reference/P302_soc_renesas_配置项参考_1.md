---
id: learning.zephyr-docs.kconfig-reference.page-302
title: "`soc/renesas`配置项参考（1/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第302章\_`soc/renesas`配置项参考（1/4）

本章翻译官方 Kconfig 数据库中 `soc/renesas` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_HAS_RENESAS_RA_IDAU"></a>

## 302.1 `CONFIG_CPU_HAS_RENESAS_RA_IDAU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

微控制器（MCU）实现了 ARM 实现定义归属单元（Implementation-Defined Attribution Unit，IDAU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_TEE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_SOC_SERIES_RA6M4`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH"></a>

## 302.2 `CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH`

**提示（Prompt）**：强制数据缓存使用直写（write-through）

**说明（Help）**

强制数据缓存（data cache）以直写模式（write-through mode）运行。某些 SoC 可能需要这样做，以确保直接访问内存的外设正常工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_RA_HAS_DCACHE_WRITETHROUGH && <choice CONFIG_CPU_RA_DCACHE_WRITE_POLICY>
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 瑞萨 RA 数据缓存写策略（Renesas RA data cache write policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_RA_HAS_DCACHE_WRITETHROUGH`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_RA_HAS_DCACHE_WRITETHROUGH)、[`CONFIG_CPU_RA_DCACHE_WRITE_POLICY`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_RA_DCACHE_WRITE_POLICY)。

<a id="CONFIG_CPU_RA_DCACHE_WRITEBACK"></a>

## 302.3 `CONFIG_CPU_RA_DCACHE_WRITEBACK`

**提示（Prompt）**：允许数据缓存使用回写模式（write-back mode）

**说明（Help）**

允许数据缓存（data cache）以回写模式（write-back mode）运行。这可能提高性能，但需要正确管理缓存，以确保数据一致性（data consistency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_RA_DCACHE_WRITE_POLICY>
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 瑞萨 RA 数据缓存写策略（Renesas RA data cache write policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_RA_DCACHE_WRITE_POLICY`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_RA_DCACHE_WRITE_POLICY)。

<a id="CONFIG_CPU_RA_DCACHE_WRITE_POLICY"></a>

## 302.4 `CONFIG_CPU_RA_DCACHE_WRITE_POLICY`

**提示（Prompt）**：瑞萨 RA 数据缓存写策略（Renesas RA data cache write policy）

**说明（Help）**

选择数据缓存写策略（DCACHE write policy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DCACHE && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH
```

**可选项（Choices）**

```text
CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH
CONFIG_CPU_RA_DCACHE_WRITEBACK
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_RA_DCACHE_FORCE_WRITETHROUGH)、[`CONFIG_CPU_RA_DCACHE_WRITEBACK`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_RA_DCACHE_WRITEBACK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_CPU_RA_HAS_DCACHE_WRITETHROUGH"></a>

## 302.5 `CONFIG_CPU_RA_HAS_DCACHE_WRITETHROUGH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 SoC 支持强制数据缓存以直写模式（write-through mode）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DCACHE && CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T2
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_OUTPUT_RPD"></a>

## 302.6 `CONFIG_OUTPUT_RPD`

**提示（Prompt）**：以 rpd 格式生成瑞萨分区数据（Renesas Partition Data）

**说明（Help）**

在构建目录中生成分区数据（partition data）`zephyr/zephyr.rpd`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_RENESAS_RA_IDAU && CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_RENESAS_RA_IDAU`](P302_soc_renesas_配置项参考_1.md#CONFIG_CPU_HAS_RENESAS_RA_IDAU)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_SERIES_RA6M4`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_NONE_USED_PORT_INIT"></a>

## 302.7 `CONFIG_RENESAS_NONE_USED_PORT_INIT`

**提示（Prompt）**：初始化未使用端口（Initialize unused ports）

**说明（Help）**

按照 RX MCU 用户手册 PORT 章节中“未使用引脚的处理”（Handling of Unused Pins）一节，初始化 RX MCU 的未使用引脚。注意：必须在 `r_bsp_config.h` 中，将 `BSP_PACKAGE_PINS` 定义设为所用器件对应的引脚类型，否则端口可能出现非预期输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/renesas/rx/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET"></a>

## 302.8 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15984 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：仅支持经典 CAN（Classical CAN），不支持灵活数据速率（Flexible Data rate）。
- B（`0x42`）：支持经典 CAN 及灵活数据速率（Flexible Data rate）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M5 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x42 if CONFIG_SOC_R7FA6M5BH3CFC
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M5BH3CFC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M5BH3CFC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET--record-15985"></a>

## 302.9 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15985 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：不提供 MIPI 显示串行接口（DSI）。
- B（`0x42`）：提供 MIPI 显示串行接口（DSI）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x42 if CONFIG_SOC_R7FA8D1BHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8D1BHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8D1BHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET--record-15986"></a>

## 302.10 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15986 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：单核（Single Core），仅 CM85。
- J（`0x4a`）：双核（Dual Core）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x4a if CONFIG_SOC_R7KA8D2KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET--record-15987"></a>

## 302.11 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15987 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：单核（Single Core），仅 CM85。
- J（`0x4a`）：双核（Dual Core）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x4a if CONFIG_SOC_R7KA8M2JFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8M2JFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET--record-15988"></a>

## 302.12 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15988 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：单核，仅 CM85；不提供 MIPI 显示／摄像头串行接口（DSI／CSI）。
- B（`0x42`）：单核，仅 CM85；提供 MIPI DSI／CSI。
- J（`0x4a`）：双核；不提供 MIPI DSI／CSI。
- K（`0x4b`）：双核；提供 MIPI DSI／CSI。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8P1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x4b if CONFIG_SOC_R7KA8P1KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8P1KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_FEATURE_SET--record-15989"></a>

## 302.13 `CONFIG_RENESAS_PN_FEATURE_SET`

原库同名定义共 6 条；本项为数据库第 15989 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

功能集（Feature set），将功能集字符转换为其 ASCII 十六进制值：

- A（`0x41`）：单核，仅 CM85；不提供 EtherCAT 从站控制器（slave controller）。
- C（`0x43`）：单核，仅 CM85；提供 EtherCAT 从站控制器。
- L（`0x4c`）：双核；提供 EtherCAT 从站控制器。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8T2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x4c if CONFIG_SOC_R7KA8T2LFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8T2LFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_NUMBER_OF_CORES"></a>

## 302.14 `CONFIG_RENESAS_PN_NUMBER_OF_CORES`

原库同名定义共 4 条；本项为数据库第 15990 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统内核数量（Number of SoC cores）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8D2KFLCAC
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_NUMBER_OF_CORES--record-15991"></a>

## 302.15 `CONFIG_RENESAS_PN_NUMBER_OF_CORES`

原库同名定义共 4 条；本项为数据库第 15991 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统内核数量（Number of SoC cores）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8M2JFLCAC
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8M2JFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_NUMBER_OF_CORES--record-15992"></a>

## 302.16 `CONFIG_RENESAS_PN_NUMBER_OF_CORES`

原库同名定义共 4 条；本项为数据库第 15992 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统内核数量（Number of SoC cores）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8P1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8P1KFLCAC
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8P1KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_NUMBER_OF_CORES--record-15993"></a>

## 302.17 `CONFIG_RENESAS_PN_NUMBER_OF_CORES`

原库同名定义共 4 条；本项为数据库第 15993 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统内核数量（Number of SoC cores）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8T2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8T2LFLCAC
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8T2LFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE"></a>

## 302.18 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15994 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FJ | LQFP | 32 |
| 2 | NH | HWQFN | 32 |
| 3 | NK | HWQFN | 24 |
| 4 | SC | LSSOP | 20 |
| 5 | SD | TSSOP | 20 |
| 6 | NL | HWQFN | 16 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA0E1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA0E1073CFJ || CONFIG_SOC_R7FA0E1053CFJ
2 if CONFIG_SOC_R7FA0E1073CNH || CONFIG_SOC_R7FA0E1053CNH
3 if CONFIG_SOC_R7FA0E1073CNK || CONFIG_SOC_R7FA0E1053CNK
4 if CONFIG_SOC_R7FA0E1073CSC || CONFIG_SOC_R7FA0E1053CSC
5 if CONFIG_SOC_R7FA0E1073CSD
6 if CONFIG_SOC_R7FA0E1073CNL || CONFIG_SOC_R7FA0E1053CNL
```

**取值范围（Ranges）**

```text
[1, 6]
```

**定义位置（Location）**：[`soc/renesas/ra/ra0e1/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra0e1/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA0E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA0E1073CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CFJ)、[`CONFIG_SOC_R7FA0E1053CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CFJ)、[`CONFIG_SOC_R7FA0E1073CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNH)、[`CONFIG_SOC_R7FA0E1053CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNH)、[`CONFIG_SOC_R7FA0E1073CNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNK)、[`CONFIG_SOC_R7FA0E1053CNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNK)、[`CONFIG_SOC_R7FA0E1073CSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CSC)、[`CONFIG_SOC_R7FA0E1053CSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CSC)、[`CONFIG_SOC_R7FA0E1073CSD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CSD)、[`CONFIG_SOC_R7FA0E1073CNL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNL)、[`CONFIG_SOC_R7FA0E1053CNL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7FA0E1073CFJ`、`CONFIG_SOC_R7FA0E1053CFJ`、`CONFIG_SOC_R7FA0E1073CNH`、`CONFIG_SOC_R7FA0E1053CNH`、`CONFIG_SOC_R7FA0E1073CNK`、`CONFIG_SOC_R7FA0E1053CNK`、`CONFIG_SOC_R7FA0E1073CSC`、`CONFIG_SOC_R7FA0E1053CSC`、`CONFIG_SOC_R7FA0E1073CSD`、`CONFIG_SOC_R7FA0E1073CNL`、`CONFIG_SOC_R7FA0E1053CNL`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-15995"></a>

## 302.19 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15995 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | FJ | LQFP | 32 |
| 3 | BT | BGA | 36 |
| 4 | NE | QFN | 48 |
| 5 | NF | QFN | 40 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA2A1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA2A1AB3CFM
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra2a1/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2a1/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA2A1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA2A1AB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA2A1AB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-15996"></a>

## 302.20 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15996 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FP | LQFP | 100 |
| 2 | FN | LQFP | 80 |
| 3 | FM | LQFP | 64 |
| 4 | FL | LQFP | 48 |
| 5 | NE | HWQFN | 48 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA2L1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA2L1ABXXFP || CONFIG_SOC_R7FA2L1A9XXFP
2 if CONFIG_SOC_R7FA2L1ABXXFN || CONFIG_SOC_R7FA2L1A9XXFN
3 if CONFIG_SOC_R7FA2L1ABXXFM || CONFIG_SOC_R7FA2L1A9XXFM
4 if CONFIG_SOC_R7FA2L1ABXXFL || CONFIG_SOC_R7FA2L1A9XXFL
5 if CONFIG_SOC_R7FA2L1ABXXNE || CONFIG_SOC_R7FA2L1A9XXNE
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra2l1/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2l1/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA2L1ABXXFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1ABXXFP)、[`CONFIG_SOC_R7FA2L1A9XXFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1A9XXFP)、[`CONFIG_SOC_R7FA2L1ABXXFN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1ABXXFN)、[`CONFIG_SOC_R7FA2L1A9XXFN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1A9XXFN)、[`CONFIG_SOC_R7FA2L1ABXXFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1ABXXFM)、[`CONFIG_SOC_R7FA2L1A9XXFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1A9XXFM)、[`CONFIG_SOC_R7FA2L1ABXXFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1ABXXFL)、[`CONFIG_SOC_R7FA2L1A9XXFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1A9XXFL)、[`CONFIG_SOC_R7FA2L1ABXXNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1ABXXNE)、[`CONFIG_SOC_R7FA2L1A9XXNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA2L1A9XXNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7FA2L1ABXXFP`、`CONFIG_SOC_R7FA2L1A9XXFP`、`CONFIG_SOC_R7FA2L1ABXXFN`、`CONFIG_SOC_R7FA2L1A9XXFN`、`CONFIG_SOC_R7FA2L1ABXXFM`、`CONFIG_SOC_R7FA2L1A9XXFM`、`CONFIG_SOC_R7FA2L1ABXXFL`、`CONFIG_SOC_R7FA2L1A9XXFL`、`CONFIG_SOC_R7FA2L1ABXXNE`、`CONFIG_SOC_R7FA2L1A9XXNE`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-15997"></a>

## 302.21 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15997 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4C1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7FA4C1BD3CFP
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4c1/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4c1/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4C1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4C1BD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4C1BD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-15998"></a>

## 302.22 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15998 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | NE | QFN | 48 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4E1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA4E10D2CFM
2 if CONFIG_SOC_R7FA4E10D2CNE
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4E10D2CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E10D2CFM)、[`CONFIG_SOC_R7FA4E10D2CNE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E10D2CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-15999"></a>

## 302.23 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 15999 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | NE | QFN | 48 |
| 3 | NH | QFN | 32 |
| 4 | BB | BGA | 64 |
| 5 | BC | BGA | 36 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4E2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA4E2B93CFM
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e2/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e2/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4E2B93CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E2B93CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16000"></a>

## 302.24 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16000 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FL | LQFP | 48 |
| 2 | FM | LQFP | 64 |
| 3 | FP | LQFP | 100 |
| 4 | NE | QFN | 48 |
| 5 | AH | BGA | 64 |
| 6 | AG | BGA | 100 |
| 7 | DB | WLCSP | 72 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4L1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
3 if CONFIG_SOC_R7FA4L1BD4CFP
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4l1/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4l1/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4L1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4L1BD4CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4L1BD4CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16001"></a>

## 302.25 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16001 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FP | LQFP | 100 |
| 2 | FM | LQFP | 64 |
| 3 | FL | LQFP | 48 |
| 4 | LJ | LGA | 100 |
| 5 | NB | QFN | 64 |
| 6 | NE | QFN | 48 |
| 7 | NF | QFN | 40 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4M1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA4M1AB3CFP
2 if CONFIG_SOC_R7FA4M1AB3CFM
6 if CONFIG_SOC_R7FA4M1AB3CNE
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M1AB3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CFP)、[`CONFIG_SOC_R7FA4M1AB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CFM)、[`CONFIG_SOC_R7FA4M1AB3CNE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16002"></a>

## 302.26 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16002 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FL | LQFP | 48 |
| 2 | FM | LQFP | 64 |
| 3 | FP | LQFP | 100 |
| 4 | NE | QFN | 48 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
3 if CONFIG_SOC_R7FA4M2AD3CFP
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m2/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m2/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M2AD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M2AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16003"></a>

## 302.27 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16003 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BM | FBGA | 144 |
| 2 | BQ | FBGA | 64 |
| 3 | FB | LQFP | 144 |
| 4 | FM | LQFP | 64 |
| 5 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4M3 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
3 if CONFIG_SOC_R7FA4M3AF3CFB
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m3/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m3/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M3AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M3AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16004"></a>

## 302.28 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16004 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | FL | LQFP | 48 |
| 3 | FJ | LQFP | 32 |
| 4 | NE | QFN | 48 |
| 5 | NH | QFN | 32 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4T1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA4T1BB3CFM || CONFIG_SOC_R7FA4T1B93CFM
2 if CONFIG_SOC_R7FA4T1BB3CFL || CONFIG_SOC_R7FA4T1B93CFL
3 if CONFIG_SOC_R7FA4T1BB3CFJ || CONFIG_SOC_R7FA4T1B93CFJ
4 if CONFIG_SOC_R7FA4T1BB3CNE || CONFIG_SOC_R7FA4T1B93CNE
5 if CONFIG_SOC_R7FA4T1BB3CNH || CONFIG_SOC_R7FA4T1B93CNH
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra4t1/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4t1/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4T1BB3CFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFM)、[`CONFIG_SOC_R7FA4T1B93CFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFM)、[`CONFIG_SOC_R7FA4T1BB3CFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFL)、[`CONFIG_SOC_R7FA4T1B93CFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFL)、[`CONFIG_SOC_R7FA4T1BB3CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFJ)、[`CONFIG_SOC_R7FA4T1B93CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFJ)、[`CONFIG_SOC_R7FA4T1BB3CNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CNE)、[`CONFIG_SOC_R7FA4T1B93CNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CNE)、[`CONFIG_SOC_R7FA4T1BB3CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CNH)、[`CONFIG_SOC_R7FA4T1B93CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CNH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7FA4T1BB3CFM`、`CONFIG_SOC_R7FA4T1B93CFM`、`CONFIG_SOC_R7FA4T1BB3CFL`、`CONFIG_SOC_R7FA4T1B93CFL`、`CONFIG_SOC_R7FA4T1BB3CFJ`、`CONFIG_SOC_R7FA4T1B93CFJ`、`CONFIG_SOC_R7FA4T1BB3CNE`、`CONFIG_SOC_R7FA4T1B93CNE`、`CONFIG_SOC_R7FA4T1BB3CNH`、`CONFIG_SOC_R7FA4T1B93CNH`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16005"></a>

## 302.29 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16005 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FP | LQFP | 100 |
| 2 | FM | LQFP | 64 |
| 3 | NE | QFN | 48 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6E1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA6E10F2CFP
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e1/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e1/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6E10F2CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6E10F2CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16006"></a>

## 302.30 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16006 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FM | LQFP | 64 |
| 2 | NE | QFN | 48 |
| 3 | NH | QFN | 32 |
| 4 | BB | BGA | 64 |
| 5 | BC | BGA | 36 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6E2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA6E2BB3CFM
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e2/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e2/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6E2BB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6E2BB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16007"></a>

## 302.31 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16007 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FP | LQFP | 100 |
| 2 | FM | LQFP | 64 |
| 3 | LJ | LGA | 100 |
| 4 | NB | QFN | 64 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA6M1AD3CFP
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m1/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m1/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M1AD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M1AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16008"></a>

## 302.32 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16008 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FB | LQFP | 144 |
| 2 | FP | LQFP | 100 |
| 3 | LK | LGA | 145 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA6M2AF3CFB
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m2/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m2/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M2AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M2AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16009"></a>

## 302.33 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16009 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BG | BGA | 176 |
| 2 | FC | LQFP | 176 |
| 3 | FB | LQFP | 144 |
| 4 | FP | LQFP | 100 |
| 5 | LK | LGA | 145 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M3 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA6M3AF2CBG
2 if CONFIG_SOC_R7FA6M3AH3CFC
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M3AF2CBG`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M3AF2CBG)、[`CONFIG_SOC_R7FA6M3AH3CFC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M3AH3CFC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16010"></a>

## 302.34 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16010 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BM | FBGA | 144 |
| 2 | BQ | FBGA | 64 |
| 3 | FB | LQFP | 144 |
| 4 | FM | LQFP | 64 |
| 5 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M4 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
3 if CONFIG_SOC_R7FA6M4AF3CFB
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m4/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m4/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M4`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M4AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M4AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16011"></a>

## 302.35 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16011 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BG | FBGA | 176 |
| 2 | BM | FBGA | 144 |
| 3 | FB | LQFP | 144 |
| 4 | FC | LQFP | 176 |
| 5 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA6M5 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
4 if CONFIG_SOC_R7FA6M5BH3CFC
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M5BH3CFC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M5BH3CFC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16012"></a>

## 302.36 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16012 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BD | FBGA | 224 |
| 2 | FC | LQFP | 176 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA8D1BHECBD
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8D1BHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8D1BHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16013"></a>

## 302.37 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16013 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | AB | LFBGA | 224 |
| 2 | AC | LFBGA | 289 |
| 3 | AJ | LFBGA | 303 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8D2KFLCAC
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16014"></a>

## 302.38 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16014 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | FB | LQFP | 144 |
| 2 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8E1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA8E1AFDCFB
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8E1AFDCFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8E1AFDCFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16015"></a>

## 302.39 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16015 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BD | FBGA | 224 |
| 2 | FC | LQFP | 176 |
| 3 | FB | LQFP | 144 |
| 4 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8M1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA8M1AHECBD
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8M1AHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8M1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16016"></a>

## 302.40 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16016 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | AB | LFBGA | 224 |
| 2 | AC | LFBGA | 289 |
| 3 | AJ | LFBGA | 303 |
| 4 | HC | HLQFP | 176 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8M2JFLCAC
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8M2JFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16017"></a>

## 302.41 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16017 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | AB | LFBGA | 224 |
| 2 | AC | LFBGA | 289 |
| 3 | AJ | LFBGA | 303 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8P1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8P1KFLCAC
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8P1KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16018"></a>

## 302.42 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16018 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | BD | FBGA | 224 |
| 2 | FC | LQFP | 176 |
| 3 | FB | LQFP | 144 |
| 4 | FP | LQFP | 100 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8T1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
1 if CONFIG_SOC_R7FA8T1AHECBD
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t1/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t1/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8T1AHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8T1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_PACKAGE_TYPE--record-16019"></a>

## 302.43 `CONFIG_RENESAS_PN_PACKAGE_TYPE`

原库同名定义共 26 条；本项为数据库第 16019 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

封装类型（Package type）：

| 取值（Value） | 封装代码（Code） | 封装（Package） | 引脚数（Pins） |
| --- | --- | --- | --- |
| 1 | AB | LFBGA | 224 |
| 2 | AC | LFBGA | 289 |
| 3 | AJ | LFBGA | 303 |
| 4 | HC | HLQFP | 176 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8T2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_R7KA8T2LFLCAC
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8T2LFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_ROM_SIZE"></a>

## 302.44 `CONFIG_RENESAS_PN_ROM_SIZE`

原库同名定义共 4 条；本项为数据库第 16020 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

代码磁阻 RAM 与 Flash 大小（Code MRAM and Flash size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8D2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x100000 if CONFIG_SOC_R7KA8D2KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_ROM_SIZE--record-16021"></a>

## 302.45 `CONFIG_RENESAS_PN_ROM_SIZE`

原库同名定义共 4 条；本项为数据库第 16021 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

代码磁阻 RAM 与 Flash 大小（Code MRAM and Flash size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8M2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x100000 if CONFIG_SOC_R7KA8M2JFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8M2JFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_ROM_SIZE--record-16022"></a>

## 302.46 `CONFIG_RENESAS_PN_ROM_SIZE`

原库同名定义共 4 条；本项为数据库第 16022 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

代码磁阻 RAM 与 Flash 大小（Code MRAM and Flash size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8P1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x100000 if CONFIG_SOC_R7KA8P1KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8P1KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_PN_ROM_SIZE--record-16023"></a>

## 302.47 `CONFIG_RENESAS_PN_ROM_SIZE`

原库同名定义共 4 条；本项为数据库第 16023 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

代码磁阻 RAM 与 Flash 大小（Code MRAM and Flash size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA8T2 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
0x100000 if CONFIG_SOC_R7KA8T2LFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8T2LFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_RA_BATTERY_BACKUP_MANUAL_CONFIGURE"></a>

## 302.48 `CONFIG_RENESAS_RA_BATTERY_BACKUP_MANUAL_CONFIGURE`

**提示（Prompt）**：手动切换电池供电（VBAT switching manual）

**说明（Help）**

如果此 SoC 的电池后备域（battery backup domain）允许手动切换到 VBAT，请启用此项；如果自动切换，则保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_BATTERY_BACKUP_ENABLED && n && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SERIES_SPECIFIC_SOC_INIT"></a>

## 302.49 `CONFIG_SERIES_SPECIFIC_SOC_INIT`

**提示（Prompt）**：使用系列专用初始化（series specific initialize）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_DA14695"></a>

## 302.50 `CONFIG_SOC_DA14695`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14695 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_DA1469X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_DA14695_DK_USB
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_BOARD_DA14695_DK_USB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DA14695_DK_USB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_DA14695_DK_USB`。

<a id="CONFIG_SOC_DA14697"></a>

## 302.51 `CONFIG_SOC_DA14697`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14697 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_DA1469X
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)。

<a id="CONFIG_SOC_DA14699"></a>

## 302.52 `CONFIG_SOC_DA14699`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14699 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_DA1469X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_DA1469X_DK_PRO
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_BOARD_DA1469X_DK_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DA1469X_DK_PRO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_DA1469X_DK_PRO`。

<a id="CONFIG_SOC_OPTION_SETTING_MEMORY"></a>

## 302.53 `CONFIG_SOC_OPTION_SETTING_MEMORY`

**提示（Prompt）**：选项设置存储器（Option Setting Memory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RA4M1 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_WDT_RENESAS_RA
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_WDT_RENESAS_RA`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_R5F51308AXFP"></a>

## 302.54 `CONFIG_SOC_R5F51308AXFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51308AXFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX130
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RSK_RX130
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX130`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX130)、[`CONFIG_BOARD_RSK_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RSK_RX130)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RSK_RX130`。

<a id="CONFIG_SOC_R5F51406BDFN"></a>

## 302.55 `CONFIG_SOC_R5F51406BDFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51406BDFN`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX140
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RSK_RX140
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX140`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX140)、[`CONFIG_BOARD_RSK_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RSK_RX140)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RSK_RX140`。

<a id="CONFIG_SOC_R5F51406BGFN"></a>

## 302.56 `CONFIG_SOC_R5F51406BGFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51406BGFN`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX140
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RX140
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX140`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX140)、[`CONFIG_BOARD_FPB_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RX140)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RX140`。

<a id="CONFIG_SOC_R5F514T5AMFM"></a>

## 302.57 `CONFIG_SOC_R5F514T5AMFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`SOC_R5F514T5AMFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX14T
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MCB_RX14T
CONFIG_BOARD_FPB_RX14T
```

**定义位置（Location）**：[`soc/renesas/rx/rx14t/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx14t/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX14T`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_BOARD_MCB_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MCB_RX14T)、[`CONFIG_BOARD_FPB_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RX14T)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MCB_RX14T`、`CONFIG_BOARD_FPB_RX14T`。

<a id="CONFIG_SOC_R5F52618BGFP"></a>

## 302.58 `CONFIG_SOC_R5F52618BGFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R5F52618BGFP 微控制器片上系统（microcontroller SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX261
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RX261
CONFIG_BOARD_EK_RX261
```

**定义位置（Location）**：[`soc/renesas/rx/rx261/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx261/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX261`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX261)、[`CONFIG_BOARD_FPB_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RX261)、[`CONFIG_BOARD_EK_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RX261)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RX261`、`CONFIG_BOARD_EK_RX261`。

<a id="CONFIG_SOC_R5F526TFDDFP"></a>

## 302.59 `CONFIG_SOC_R5F526TFDDFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`SOC_R5F526TFDDFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX26T
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MCB_RX26T
```

**定义位置（Location）**：[`soc/renesas/rx/rx26t/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx26t/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX26T`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_BOARD_MCB_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MCB_RX26T)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MCB_RX26T`。

<a id="CONFIG_SOC_R5F562N8"></a>

## 302.60 `CONFIG_SOC_R5F562N8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F562N8`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX62N
```

**被选择（Selected by）**

```text
CONFIG_BOARD_QEMU_RX
```

**定义位置（Location）**：[`soc/renesas/rx/rx62n/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx62n/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX62N`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX62N)、[`CONFIG_BOARD_QEMU_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_RX`。

<a id="CONFIG_SOC_R5K574MCB4AE"></a>

## 302.61 `CONFIG_SOC_R5K574MCB4AE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5K574MCB4AE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX74M
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RX74M
```

**定义位置（Location）**：[`soc/renesas/rx/rx74m/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74m/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX74M`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_BOARD_EK_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RX74M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RX74M`。

<a id="CONFIG_SOC_R5K574NCB4AE"></a>

## 302.62 `CONFIG_SOC_R5K574NCB4AE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5K574NCB4AE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RX74N
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RX74N
```

**定义位置（Location）**：[`soc/renesas/rx/rx74n/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74n/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX74N`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX74N)、[`CONFIG_BOARD_EK_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RX74N)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RX74N`。

<a id="CONFIG_SOC_R7FA2A1AB3CFM"></a>

## 302.63 `CONFIG_SOC_R7FA2A1AB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA2A1AB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA2A1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA2A1
```

**定义位置（Location）**：[`soc/renesas/ra/ra2a1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2a1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA2A1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_BOARD_EK_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA2A1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA2A1`。

<a id="CONFIG_SOC_R7FA4C1BD3CFP"></a>

## 302.64 `CONFIG_SOC_R7FA4C1BD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4C1BD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4C1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4C1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4c1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4c1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4C1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_BOARD_EK_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4C1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4C1`。

<a id="CONFIG_SOC_R7FA4E10D2CFM"></a>

## 302.65 `CONFIG_SOC_R7FA4E10D2CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E10D2CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4E1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RA4E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_BOARD_FPB_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RA4E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RA4E1`。

<a id="CONFIG_SOC_R7FA4E10D2CNE"></a>

## 302.66 `CONFIG_SOC_R7FA4E10D2CNE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E10D2CNE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4E1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VOICE_RA4E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_BOARD_VOICE_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VOICE_RA4E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_VOICE_RA4E1`。

<a id="CONFIG_SOC_R7FA4E2B93CFM"></a>

## 302.67 `CONFIG_SOC_R7FA4E2B93CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E2B93CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4E2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4E2
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_BOARD_EK_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4E2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4E2`。

<a id="CONFIG_SOC_R7FA4L1BD4CFP"></a>

## 302.68 `CONFIG_SOC_R7FA4L1BD4CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4L1BD4CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4L1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4L1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4l1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4l1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4L1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_BOARD_EK_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4L1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4L1`。

<a id="CONFIG_SOC_R7FA4M1AB3CFM"></a>

## 302.69 `CONFIG_SOC_R7FA4M1AB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARDUINO_UNO_R4
CONFIG_BOARD_ARDUINO_NANO_R4
CONFIG_BOARD_MIKROE_CLICKER_RA4M1
CONFIG_BOARD_WEACT_RA4M1_CORE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_BOARD_ARDUINO_UNO_R4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARDUINO_UNO_R4)、[`CONFIG_BOARD_ARDUINO_NANO_R4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARDUINO_NANO_R4)、[`CONFIG_BOARD_MIKROE_CLICKER_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MIKROE_CLICKER_RA4M1)、[`CONFIG_BOARD_WEACT_RA4M1_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_RA4M1_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ARDUINO_UNO_R4`、`CONFIG_BOARD_ARDUINO_NANO_R4`、`CONFIG_BOARD_MIKROE_CLICKER_RA4M1`、`CONFIG_BOARD_WEACT_RA4M1_CORE`。

<a id="CONFIG_SOC_R7FA4M1AB3CFP"></a>

## 302.70 `CONFIG_SOC_R7FA4M1AB3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_BOARD_EK_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4M1`。

<a id="CONFIG_SOC_R7FA4M1AB3CNE"></a>

## 302.71 `CONFIG_SOC_R7FA4M1AB3CNE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CNE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_XIAO_RA4M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_BOARD_XIAO_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_RA4M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XIAO_RA4M1`。

<a id="CONFIG_SOC_R7FA4M2AD3CFP"></a>

## 302.72 `CONFIG_SOC_R7FA4M2AD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M2AD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4M2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4M2
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_BOARD_EK_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4M2`。

<a id="CONFIG_SOC_R7FA4M3AF3CFB"></a>

## 302.73 `CONFIG_SOC_R7FA4M3AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M3AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4M3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_BOARD_EK_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4M3`。

<a id="CONFIG_SOC_R7FA4W1AD2CNG"></a>

## 302.74 `CONFIG_SOC_R7FA4W1AD2CNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4W1AD2CNG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA4W1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA4W1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4w1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4w1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA4W1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_BOARD_EK_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA4W1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA4W1`。

<a id="CONFIG_SOC_R7FA6E10F2CFP"></a>

## 302.75 `CONFIG_SOC_R7FA6E10F2CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6E10F2CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6E1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RA6E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_BOARD_FPB_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RA6E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RA6E1`。

<a id="CONFIG_SOC_R7FA6E2BB3CFM"></a>

## 302.76 `CONFIG_SOC_R7FA6E2BB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6E2BB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6E2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RA6E2
CONFIG_BOARD_EK_RA6E2
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_BOARD_FPB_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RA6E2)、[`CONFIG_BOARD_EK_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6E2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RA6E2`、`CONFIG_BOARD_EK_RA6E2`。

<a id="CONFIG_SOC_R7FA6M1AD3CFP"></a>

## 302.77 `CONFIG_SOC_R7FA6M1AD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M1AD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA6M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_BOARD_EK_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA6M1`。

<a id="CONFIG_SOC_R7FA6M2AF3CFB"></a>

## 302.78 `CONFIG_SOC_R7FA6M2AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M2AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA6M2
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_BOARD_EK_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA6M2`。

<a id="CONFIG_SOC_R7FA6M3AF2CBG"></a>

## 302.79 `CONFIG_SOC_R7FA6M3AF2CBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M3AF2CBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M3)。

<a id="CONFIG_SOC_R7FA6M3AH3CFC"></a>

## 302.80 `CONFIG_SOC_R7FA6M3AH3CFC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M3AH3CFC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA6M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_BOARD_EK_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA6M3`。

<a id="CONFIG_SOC_R7FA6M4AF3CFB"></a>

## 302.81 `CONFIG_SOC_R7FA6M4AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M4AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA6M4
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m4/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m4/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M4`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_BOARD_EK_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA6M4`。

<a id="CONFIG_SOC_R7FA6M5BH3CFC"></a>

## 302.82 `CONFIG_SOC_R7FA6M5BH3CFC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M5BH3CFC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA6M5
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARDUINO_PORTENTA_C33
CONFIG_BOARD_EK_RA6M5
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_BOARD_ARDUINO_PORTENTA_C33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARDUINO_PORTENTA_C33)、[`CONFIG_BOARD_EK_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA6M5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ARDUINO_PORTENTA_C33`、`CONFIG_BOARD_EK_RA6M5`。

<a id="CONFIG_SOC_R7FA8D1BHECBD"></a>

## 302.83 `CONFIG_SOC_R7FA8D1BHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8D1BHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8D1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RA8D1_VISION_BOARD
CONFIG_BOARD_EK_RA8D1
CONFIG_BOARD_CPKCOR_RA8D1B
CONFIG_BOARD_AIK_RA8D1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_BOARD_RA8D1_VISION_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RA8D1_VISION_BOARD)、[`CONFIG_BOARD_EK_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA8D1)、[`CONFIG_BOARD_CPKCOR_RA8D1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CPKCOR_RA8D1B)、[`CONFIG_BOARD_AIK_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_AIK_RA8D1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RA8D1_VISION_BOARD`、`CONFIG_BOARD_EK_RA8D1`、`CONFIG_BOARD_CPKCOR_RA8D1B`、`CONFIG_BOARD_AIK_RA8D1`。

<a id="CONFIG_SOC_R7FA8E1AFDCFB"></a>

## 302.84 `CONFIG_SOC_R7FA8E1AFDCFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8E1AFDCFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8E1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FPB_RA8E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_BOARD_FPB_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FPB_RA8E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_FPB_RA8E1`。

<a id="CONFIG_SOC_R7FA8E1AFDCFP"></a>

## 302.85 `CONFIG_SOC_R7FA8E1AFDCFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8E1AFDCFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8E1)。

<a id="CONFIG_SOC_R7FA8M1AHECBD"></a>

## 302.86 `CONFIG_SOC_R7FA8M1AHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8M1AHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EK_RA8M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_BOARD_EK_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EK_RA8M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EK_RA8M1`。

<a id="CONFIG_SOC_R7FA8T1AHECBD"></a>

## 302.87 `CONFIG_SOC_R7FA8T1AHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8T1AHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8T1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MCK_RA8T1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t1/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t1/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_BOARD_MCK_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MCK_RA8T1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MCK_RA8T1`。

<a id="CONFIG_SOC_R7KA8D2KFLCAC"></a>

## 302.88 `CONFIG_SOC_R7KA8D2KFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8D2KFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8D2
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8D2KFLCAC_CM85
CONFIG_SOC_R7KA8D2KFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM85)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8D2KFLCAC_CM85`、`CONFIG_SOC_R7KA8D2KFLCAC_CM33`。

<a id="CONFIG_SOC_R7KA8M2JFLCAC"></a>

## 302.89 `CONFIG_SOC_R7KA8M2JFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8M2JFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8M2
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8M2JFLCAC_CM85
CONFIG_SOC_R7KA8M2JFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM85)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8M2JFLCAC_CM85`、`CONFIG_SOC_R7KA8M2JFLCAC_CM33`。

<a id="CONFIG_SOC_R7KA8P1KFLCAC"></a>

## 302.90 `CONFIG_SOC_R7KA8P1KFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8P1KFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8P1
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8P1KFLCAC_CM85
CONFIG_SOC_R7KA8P1KFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`CONFIG_SOC_R7KA8P1KFLCAC_CM33`。

<a id="CONFIG_SOC_R7KA8T2LFLCAC"></a>

## 302.91 `CONFIG_SOC_R7KA8T2LFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8T2LFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RA8T2
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8T2LFLCAC_CM85
CONFIG_SOC_R7KA8T2LFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM85)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8T2LFLCAC_CM85`、`CONFIG_SOC_R7KA8T2LFLCAC_CM33`。

<a id="CONFIG_SOC_R7S921053VCBG"></a>

## 302.92 `CONFIG_SOC_R7S921053VCBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7S921053VCBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZA2M
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZA2M_EVK
CONFIG_SOC_R7S921053VCBG_CA9
```

**定义位置（Location）**：[`soc/renesas/rz/rza2m/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza2m/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZA2M`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZA2M)、[`CONFIG_BOARD_RZA2M_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZA2M_EVK)、[`CONFIG_SOC_R7S921053VCBG_CA9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7S921053VCBG_CA9)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZA2M_EVK`、`CONFIG_SOC_R7S921053VCBG_CA9`。

<a id="CONFIG_SOC_R8A77951_A57"></a>

## 302.93 `CONFIG_SOC_R8A77951_A57`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R8A77951 A57 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_H3ULCB
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN3)、[`CONFIG_BOARD_RCAR_H3ULCB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_H3ULCB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RCAR_GEN3`、`CONFIG_BOARD_RCAR_H3ULCB`。

<a id="CONFIG_SOC_R8A77951_R7"></a>

## 302.94 `CONFIG_SOC_R8A77951_R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R8A77951 R7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_SALVATOR_X
CONFIG_BOARD_RCAR_H3ULCB
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN3)、[`CONFIG_BOARD_RCAR_SALVATOR_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_SALVATOR_X)、[`CONFIG_BOARD_RCAR_H3ULCB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_H3ULCB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RCAR_GEN3`、`CONFIG_BOARD_RCAR_SALVATOR_X`、`CONFIG_BOARD_RCAR_H3ULCB`。

<a id="CONFIG_SOC_R8A77961"></a>

## 302.95 `CONFIG_SOC_R8A77961`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R8A77961`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_SALVATOR_XS
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN3)、[`CONFIG_BOARD_RCAR_SALVATOR_XS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_SALVATOR_XS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RCAR_GEN3`、`CONFIG_BOARD_RCAR_SALVATOR_XS`。

<a id="CONFIG_SOC_R8A779F0_A55"></a>

## 302.96 `CONFIG_SOC_R8A779F0_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

r8a779f0 a55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_SPIDER_S4
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen4/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen4/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN4)、[`CONFIG_BOARD_RCAR_SPIDER_S4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_SPIDER_S4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RCAR_GEN4`、`CONFIG_BOARD_RCAR_SPIDER_S4`。

<a id="CONFIG_SOC_R8A779F0_R52"></a>

## 302.97 `CONFIG_SOC_R8A779F0_R52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

r8a779f0 r52 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_SPIDER_S4
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen4/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen4/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN4)、[`CONFIG_BOARD_RCAR_SPIDER_S4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_SPIDER_S4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RCAR_GEN4`、`CONFIG_BOARD_RCAR_SPIDER_S4`。

<a id="CONFIG_SOC_R8A78000_A720"></a>

## 302.98 `CONFIG_SOC_R8A78000_A720`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持 R8A78000 A720 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN5
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_IRONHIDE_X5H
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RCAR_GEN5)、[`CONFIG_BOARD_RCAR_IRONHIDE_X5H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_IRONHIDE_X5H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RCAR_IRONHIDE_X5H`。

<a id="CONFIG_SOC_R8A78000_R52"></a>

## 302.99 `CONFIG_SOC_R8A78000_R52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持 R8A78000 R52 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RCAR_GEN5
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RCAR_IRONHIDE_X5H
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RCAR_GEN5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RCAR_GEN5)、[`CONFIG_BOARD_RCAR_IRONHIDE_X5H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RCAR_IRONHIDE_X5H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RCAR_IRONHIDE_X5H`。

<a id="CONFIG_SOC_R9A07G043U11GBG"></a>

## 302.100 `CONFIG_SOC_R9A07G043U11GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G043U11GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZG2UL
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZG2UL_SMARC
CONFIG_SOC_R9A07G043U11GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2ul/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2ul/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG2UL`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_BOARD_RZG2UL_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZG2UL_SMARC)、[`CONFIG_SOC_R9A07G043U11GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A07G043U11GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZG2UL_SMARC`、`CONFIG_SOC_R9A07G043U11GBG_CM33`。

<!-- kconfig-navigation -->

[上一章](P301_soc_realtek_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P303_soc_renesas_配置项参考_2.md)
