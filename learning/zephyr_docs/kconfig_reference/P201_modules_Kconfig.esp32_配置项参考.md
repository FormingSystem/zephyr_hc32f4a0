---
id: learning.zephyr-docs.kconfig-reference.page-201
title: "`modules/Kconfig.esp32`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第201章\_`modules/Kconfig.esp32`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.esp32` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP_HAL_EARLY_LOG_LEVEL"></a>

## 201.1 `CONFIG_ESP_HAL_EARLY_LOG_LEVEL`

**提示（Prompt）**：ESP 硬件抽象层（HAL）的早期启动日志级别

**说明（Help）**

控制在 Zephyr 日志子系统初始化之前运行的 `ESP_EARLY_LOGx` 和 `ESP_DRAM_LOGx` 宏的日志输出。它们使用 `esp_rom_printf`，独立于 `CONFIG_LOG`。级别为：`0` 关闭（Off），`1` 错误（Error），`2` 警告（Warning），`3` 信息（Info），`4` 调试（Debug）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`modules/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<!-- kconfig-navigation -->

[上一章](P200_modules_Kconfig_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P202_modules_Kconfig.infineon_配置项参考.md)
