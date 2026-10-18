---
id: learning.zephyr-docs.kconfig-reference.page-244
title: "`modules/nanopb`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第244章\_`modules/nanopb`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/nanopb` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NANOPB"></a>

## 244.1 `CONFIG_NANOPB`

**提示（Prompt）**：Nanopb 支持（Nanopb Support）

**说明（Help）**

此选项启用 Nanopb 库和生成器（generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ESP_HOSTED_MCU
CONFIG_WIFI_ESP_HOSTED
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)。

<a id="CONFIG_NANOPB_BUFFER_ONLY"></a>

## 244.2 `CONFIG_NANOPB_BUFFER_ONLY`

**提示（Prompt）**：仅使用缓冲区（Buffers only）

**说明（Help）**

禁用自定义流（custom stream）支持，仅支持通过内存缓冲区进行编码和解码。这会加快执行速度，并略微减小代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<a id="CONFIG_NANOPB_ENABLE_MALLOC"></a>

## 244.3 `CONFIG_NANOPB_ENABLE_MALLOC`

**提示（Prompt）**：malloc 使用（Malloc usage）

**说明（Help）**

此选项在解码器（decoder）中启用动态分配（dynamic allocation）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**被选择（Selected by）**

```text
CONFIG_ESP_HOSTED_MCU
CONFIG_WIFI_ESP_HOSTED
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)、[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)。

<a id="CONFIG_NANOPB_ENCODE_ARRAYS_UNPACKED"></a>

## 244.4 `CONFIG_NANOPB_ENCODE_ARRAYS_UNPACKED`

**提示（Prompt）**：以非打包形式编码数组（Encode arrays unpacked）

**说明（Help）**

以非打包格式（unpacked format）编码标量数组，这会占用更多空间。仅当接收端的解码器无法处理打包数组（packed array）时使用，例如 2020 年以前的 protobuf.js 版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<a id="CONFIG_NANOPB_MAX_REQUIRED_FIELDS"></a>

## 244.5 `CONFIG_NANOPB_MAX_REQUIRED_FIELDS`

**提示（Prompt）**：必需字段的最大数量（Max number of required fields）

**说明（Help）**

需要检查是否存在的 proto2 必需字段（required field）的最大数量。默认值和最小值均为 64。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<a id="CONFIG_NANOPB_NO_ERRMSG"></a>

## 244.6 `CONFIG_NANOPB_NO_ERRMSG`

**提示（Prompt）**：禁用错误消息（Disable error messages）

**说明（Help）**

禁用错误消息（error message）支持，以节省代码空间。唯一的错误信息是 true／false 返回值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<a id="CONFIG_NANOPB_VALIDATE_UTF8"></a>

## 244.7 `CONFIG_NANOPB_VALIDATE_UTF8`

**提示（Prompt）**：验证 UTF-8（Validate UTF-8）

**说明（Help）**

检查输入字符串是否为有效的 UTF-8 序列。这会带来少量性能开销和代码体积增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<a id="CONFIG_NANOPB_WITHOUT_64BIT"></a>

## 244.8 `CONFIG_NANOPB_WITHOUT_64BIT`

**提示（Prompt）**：禁用 64 位整数字段（Disable 64-bit integer fields）

**说明（Help）**

禁用 64 位整数字段（64-bit integer field）支持，适用于旧编译器，或用于略微提高 8 位平台上的执行速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NANOPB
```

**定义位置（Location）**：[`modules/nanopb/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nanopb/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nanopb（模块路径 `modules/lib/nanopb`，相对于 west 工作区顶层目录） → Nanopb 支持（Nanopb Support）

**配置项引用（Symbol References）**：[`CONFIG_NANOPB`](P244_modules_nanopb_配置项参考.md#CONFIG_NANOPB)。

<!-- kconfig-navigation -->

[上一章](P243_modules_mbedtls_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P245_modules_nrf_wifi_配置项参考.md)
