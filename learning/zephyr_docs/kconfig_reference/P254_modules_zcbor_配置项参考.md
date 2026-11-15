---
id: learning.zephyr-docs.kconfig-reference.page-254
title: "`modules/zcbor`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第254章\_`modules/zcbor`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/zcbor` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ZCBOR"></a>

## 254.1 `CONFIG_ZCBOR`

**提示（Prompt）**：zcbor 简洁二进制对象表示库（CBOR library）

**说明（Help）**

zcbor CBOR 编码器／解码器库（encoder/decoder library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_ZCBOR_MODULE
```

**被选择（Selected by）**

```text
CONFIG_FIDO2
```

**被弱选择（Implied by）**

```text
CONFIG_LWM2M_VERSION_1_1
```

**定义位置（Location）**：[`modules/zcbor/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/zcbor/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → zcbor（模块路径 `modules/lib/zcbor`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_ZCBOR_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_ZCBOR_MODULE)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_LWM2M_VERSION_1_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_VERSION_1_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_ZCBOR_MODULE`。

<a id="CONFIG_ZCBOR_CANONICAL"></a>

## 254.2 `CONFIG_ZCBOR_CANONICAL`

**提示（Prompt）**：生成规范形式的 CBOR（canonical CBOR）

**说明（Help）**

启用此项会阻止 zcbor 以不定长度数组（indefinite-length array）形式创建列表（list）和映射（map）。同时会在所有 zcbor 状态中启用 `state->constant_state->enforce_canonical` 标志；该标志控制解码时对规范形式数据（canonical data）的验证。如果只需要规范形式编码，请在初始化后将所有新状态结构中的 `enforce_canonical` 标志设为 `false`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR
```

**被选择（Selected by）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`modules/zcbor/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/zcbor/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → zcbor（模块路径 `modules/lib/zcbor`，相对于 west 工作区顶层目录） → zcbor 简洁二进制对象表示库（CBOR library）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)。

<a id="CONFIG_ZCBOR_MAX_STR_LEN"></a>

## 254.3 `CONFIG_ZCBOR_MAX_STR_LEN`

**提示（Prompt）**：调用 zcbor_tstr_put_term() 时的默认最大长度（Default max length）

**说明（Help）**

没有现成的其他值时，可以手动使用此值，但不建议这样做。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`modules/zcbor/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/zcbor/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → zcbor（模块路径 `modules/lib/zcbor`，相对于 west 工作区顶层目录） → zcbor 简洁二进制对象表示库（CBOR library）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)。

<a id="CONFIG_ZCBOR_STOP_ON_ERROR"></a>

## 254.4 `CONFIG_ZCBOR_STOP_ON_ERROR`

**提示（Prompt）**：处理时遇错停止，也必须在状态变量中启用（Stop on error）

**说明（Help）**

提供遇错停止功能（`stop_on_error`）。注意，仍需在状态变量 `state->constant_state->stop_on_error` 中启用它。启用后，如果调用函数时已经发生错误，所有函数都会中止执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR
```

**定义位置（Location）**：[`modules/zcbor/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/zcbor/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → zcbor（模块路径 `modules/lib/zcbor`，相对于 west 工作区顶层目录） → zcbor 简洁二进制对象表示库（CBOR library）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)。

<a id="CONFIG_ZCBOR_VERBOSE"></a>

## 254.5 `CONFIG_ZCBOR_VERBOSE`

**提示（Prompt）**：使 zcbor 代码通过 printf 打印消息（print messages via printf）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR
```

**定义位置（Location）**：[`modules/zcbor/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/zcbor/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → zcbor（模块路径 `modules/lib/zcbor`，相对于 west 工作区顶层目录） → zcbor 简洁二进制对象表示库（CBOR library）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)。

<!-- kconfig-navigation -->

[上一章](P253_modules_uoscore-uedhoc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P255_share_配置项参考.md)
