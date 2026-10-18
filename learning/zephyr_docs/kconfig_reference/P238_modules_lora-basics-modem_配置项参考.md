---
id: learning.zephyr-docs.kconfig-reference.page-238
title: "`modules/lora-basics-modem`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第238章\_`modules/lora-basics-modem`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/lora-basics-modem` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LORA_BASICS_MODEM_HAL"></a>

## 238.1 `CONFIG_LORA_BASICS_MODEM_HAL`

**提示（Prompt）**：LoRa Basics Modem 硬件抽象层（HAL）实现

**说明（Help）**

编译 LoRa Basics Modem 的 `smtc_modem_hal` 实现，供移植测试（porting tests）和完整调制解调器功能使用。目前仅支持 SX126x 无线电（radios）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_LORA_BASICS_MODEM_DRIVERS && CONFIG_LORA_SX126X
```

**定义位置（Location）**：[`modules/lora-basics-modem/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lora-basics-modem/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → lora-basics-modem（模块路径 `modules/lib/lora-basics-modem`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_USE_LORA_BASICS_MODEM_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_LORA_BASICS_MODEM_DRIVERS)、[`CONFIG_LORA_SX126X`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_LORA_BASICS_MODEM_DRIVERS`。

<!-- kconfig-navigation -->

[上一章](P237_modules_libsbc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P239_modules_loramac-node_配置项参考.md)
