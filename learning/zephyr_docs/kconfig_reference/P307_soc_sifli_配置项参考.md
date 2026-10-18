---
id: learning.zephyr-docs.kconfig-reference.page-307
title: "`soc/sifli`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第307章\_`soc/sifli`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/sifli` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SF32LB52X_BOOTROM_FLASH_OFF_DELAY_MS"></a>

## 307.1 `CONFIG_SF32LB52X_BOOTROM_FLASH_OFF_DELAY_MS`

**提示（Prompt）**：启动 ROM 的 Flash 断电延迟，单位为毫秒（flash off delay）

**说明（Help）**

配置启动 ROM 的 Flash 断电延迟（PA21），单位为毫秒。更多细节请参阅 `SF32LB52X_BOOTROM_FLASH_ON_DELAY_MS` 的帮助。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_SOC_FAMILY_SF32
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`soc/sifli/sf32/sf32lb52x/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/sifli/sf32/sf32lb52x/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_FAMILY_SF32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SF32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_FAMILY_SF32`。

<a id="CONFIG_SF32LB52X_BOOTROM_FLASH_ON_DELAY_MS"></a>

## 307.2 `CONFIG_SF32LB52X_BOOTROM_FLASH_ON_DELAY_MS`

**提示（Prompt）**：启动 ROM 的 Flash 上电延迟，单位为毫秒（flash on delay）

**说明（Help）**

配置启动 ROM 的 Flash 上电延迟（PA21），单位为毫秒。默认情况下，启动 ROM 会在跳转到固件前将上电／断电延迟设为 0ms。启用此项可以将这些延迟配置为非零值。对 Flash 重新断电再上电（power cycle），可保证从外部 Flash 执行代码之前，使其进入已知状态。如果外部 Flash 使用 4 字节地址模式，则必须这样做，因为启动 ROM 从外部 Flash 读取时始终使用 3 字节地址模式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_SOC_FAMILY_SF32
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4095]
```

**定义位置（Location）**：[`soc/sifli/sf32/sf32lb52x/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/sifli/sf32/sf32lb52x/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_FAMILY_SF32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SF32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_FAMILY_SF32`。

<!-- kconfig-navigation -->

[上一章](P306_soc_renode_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P308_soc_silabs_配置项参考_1.md)
