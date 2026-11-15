---
id: learning.zephyr-docs.kconfig-reference.page-237
title: "`modules/libsbc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第237章\_`modules/libsbc`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/libsbc` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LIBSBC"></a>

## 237.1 `CONFIG_LIBSBC`

**提示（Prompt）**：libsbc 支持（Support）

**说明（Help）**

启用低复杂度子带编解码器（Low Complexity Subband Codec，SBC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被弱选择（Implied by）**

```text
CONFIG_BT_A2DP
```

**定义位置（Location）**：[`modules/libsbc/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/libsbc/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → libsbc（模块路径 `modules/lib/libsbc`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_A2DP)。

<!-- kconfig-navigation -->

[上一章](P236_modules_liblc3_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P238_modules_lora-basics-modem_配置项参考.md)
