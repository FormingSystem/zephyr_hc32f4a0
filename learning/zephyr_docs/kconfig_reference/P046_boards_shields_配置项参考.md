---
id: learning.zephyr-docs.kconfig-reference.page-46
title: "`boards/shields`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第46章\_`boards/shields`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/shields` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SHIELD_AD_APARDPFW_SL"></a>

## 46.1 `CONFIG_SHIELD_AD_APARDPFW_SL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

带有 ADIN2111 以太网交换机（Ethernet Switch）的 AD-APARDPFW-SL 10BASE-T1L 电源转发扩展板（Power Forwarder Shield）。需要开发板专用的 SPI 配置，示例见 `boards/apard32690_max32690_m4.overlay`。此扩展板不兼容 Arduino R3 开发板。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIN2111_ENABLED
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`boards/shields/ad_apardpfw_sl/Kconfig.shield:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ad_apardpfw_sl/Kconfig.shield#L4)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_SHIELD_LCD_PAR_S035_INIT_PRIORITY"></a>

## 46.2 `CONFIG_SHIELD_LCD_PAR_S035_INIT_PRIORITY`

**提示（Prompt）**：LCD_PAR_S035 扩展板初始化优先级（Shield Init Priority）

**说明（Help）**

用于初始化扩展板（Shield）的 `SYSINIT()` 优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHIELD_LCD_PAR_S035
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`boards/shields/lcd_par_s035/Kconfig.shield:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/Kconfig.shield#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SHIELD_LCD_PAR_S035`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_LCD_PAR_S035)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_LCD_PAR_S035`。

<!-- kconfig-navigation -->

[上一章](P045_boards_lilygo_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P047_drivers_adc_配置项参考_1.md)
