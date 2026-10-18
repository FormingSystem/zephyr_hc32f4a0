---
id: learning.zephyr-docs.kconfig-reference.page-16
title: "`<module:lvgl>/zephyr`配置项参考（2/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第16章\_`<module:lvgl>/zephyr`配置项参考（2/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20"></a>

## 16.1 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20`

**提示（Prompt）**：Montserrat 20 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_20
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1796`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_20`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_20)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22"></a>

## 16.2 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22`

**提示（Prompt）**：Montserrat 22 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_22
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1799`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_22`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_22)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24"></a>

## 16.3 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24`

**提示（Prompt）**：Montserrat 24 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_24
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1802`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_24`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_24)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26"></a>

## 16.4 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26`

**提示（Prompt）**：Montserrat 26 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_26
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1805`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_26`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_26)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28"></a>

## 16.5 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28`

**提示（Prompt）**：Montserrat 28 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_28
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1808`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_28`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_28)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED"></a>

## 16.6 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED`

**提示（Prompt）**：Montserrat 28 字体，压缩（Compressed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_28_COMPRESSED
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1841`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_28_COMPRESSED`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_28_COMPRESSED)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30"></a>

## 16.7 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30`

**提示（Prompt）**：Montserrat 30 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_30
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1811`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_30`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_30)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32"></a>

## 16.8 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32`

**提示（Prompt）**：Montserrat 32 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1814`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_32`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_32)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34"></a>

## 16.9 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34`

**提示（Prompt）**：Montserrat 34 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_34
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1817`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_34`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_34)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36"></a>

## 16.10 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36`

**提示（Prompt）**：Montserrat 36 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_36
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1820`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_36`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_36)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38"></a>

## 16.11 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38`

**提示（Prompt）**：Montserrat 38 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_38
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1823`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_38`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_38)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40"></a>

## 16.12 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40`

**提示（Prompt）**：Montserrat 40 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_40
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1826`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_40`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_40)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42"></a>

## 16.13 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42`

**提示（Prompt）**：Montserrat 42 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_42
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1829`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_42`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_42)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44"></a>

## 16.14 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44`

**提示（Prompt）**：Montserrat 44 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_44
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1832`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_44`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_44)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46"></a>

## 16.15 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46`

**提示（Prompt）**：Montserrat 46 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_46
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1835`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_46`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_46)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48"></a>

## 16.16 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48`

**提示（Prompt）**：Montserrat 48 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_48
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1838`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_48`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_48)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8"></a>

## 16.17 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8`

**提示（Prompt）**：Montserrat 8 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1778`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_8)。

<a id="CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK"></a>

## 16.18 `CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK`

**提示（Prompt）**：SourceHanSansSC 14 字体，中日韩字符（CJK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_14_CJK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1847`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_14_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_14_CJK)。

<a id="CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK"></a>

## 16.19 `CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK`

**提示（Prompt）**：SourceHanSansSC 16 字体，中日韩字符（CJK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_16_CJK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1850`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_16_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_16_CJK)。

<a id="CONFIG_LV_FONT_DEFAULT_UNSCII_16"></a>

## 16.20 `CONFIG_LV_FONT_DEFAULT_UNSCII_16`

**提示（Prompt）**：UNSCII 16 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_UNSCII_16
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1856`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_UNSCII_16`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_UNSCII_16)。

<a id="CONFIG_LV_FONT_DEFAULT_UNSCII_8"></a>

## 16.21 `CONFIG_LV_FONT_DEFAULT_UNSCII_8`

**提示（Prompt）**：UNSCII 8 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_UNSCII_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1853`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_UNSCII_8)。

<a id="CONFIG_LV_FONT_DEJAVU_16_PERSIAN_HEBREW"></a>

## 16.22 `CONFIG_LV_FONT_DEJAVU_16_PERSIAN_HEBREW`

**提示（Prompt）**：Dejavu 16 字体（波斯文 Persian、希伯来文 Hebrew、阿拉伯文 Arabic）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1719`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW)。

<a id="CONFIG_LV_FONT_FMT_TXT_LARGE"></a>

## 16.23 `CONFIG_LV_FONT_FMT_TXT_LARGE`

**提示（Prompt）**：大型字体格式（Large Font Format）

**说明（Help）**

使用更大的内部偏移量（Internal Offset），使包含大量字形（Glyph）的字体仍可被寻址。确切限制取决于字体大小、字型和格式；如果在超过大约 10000 个字符的字体上遇到问题，请启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1861`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FONT_MANAGER_NAME_MAX_LEN"></a>

## 16.24 `CONFIG_LV_FONT_MANAGER_NAME_MAX_LEN`

**提示（Prompt）**：字体名称最大长度（Font Name Max Length，字符数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FONT_MANAGER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1885`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 字体管理器（Font Manager）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FONT_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FONT_MANAGER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FONT_MONTSERRAT_10"></a>

## 16.25 `CONFIG_LV_FONT_MONTSERRAT_10`

**提示（Prompt）**：Montserrat 10 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1675`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10)。

<a id="CONFIG_LV_FONT_MONTSERRAT_12"></a>

## 16.26 `CONFIG_LV_FONT_MONTSERRAT_12`

**提示（Prompt）**：Montserrat 12 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1677`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12)。

<a id="CONFIG_LV_FONT_MONTSERRAT_14"></a>

## 16.27 `CONFIG_LV_FONT_MONTSERRAT_14`

**提示（Prompt）**：Montserrat 14 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14
CONFIG_LV_USE_DEMO_BENCHMARK
```

**被弱选择（Implied by）**

```text
CONFIG_LV_COLOR_FORMAT_RGB565
CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED
CONFIG_LV_COLOR_FORMAT_RGB888
CONFIG_LV_COLOR_FORMAT_XRGB8888
CONFIG_LV_COLOR_FORMAT_ARGB8888
CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED
CONFIG_LV_COLOR_DEPTH_32
CONFIG_LV_COLOR_DEPTH_24
CONFIG_LV_COLOR_DEPTH_16
CONFIG_LV_COLOR_DEPTH_1
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1679`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_BENCHMARK)、[`CONFIG_LV_COLOR_FORMAT_RGB565`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB565)、[`CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED)、[`CONFIG_LV_COLOR_FORMAT_RGB888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB888)、[`CONFIG_LV_COLOR_FORMAT_XRGB8888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_XRGB8888)、[`CONFIG_LV_COLOR_FORMAT_ARGB8888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_ARGB8888)、[`CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED)、[`CONFIG_LV_COLOR_DEPTH_32`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_32)、[`CONFIG_LV_COLOR_DEPTH_24`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_24)、[`CONFIG_LV_COLOR_DEPTH_16`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_16)、[`CONFIG_LV_COLOR_DEPTH_1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_1)。

<a id="CONFIG_LV_FONT_MONTSERRAT_16"></a>

## 16.28 `CONFIG_LV_FONT_MONTSERRAT_16`

**提示（Prompt）**：Montserrat 16 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1682`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16)。

<a id="CONFIG_LV_FONT_MONTSERRAT_18"></a>

## 16.29 `CONFIG_LV_FONT_MONTSERRAT_18`

**提示（Prompt）**：Montserrat 18 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1684`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18)。

<a id="CONFIG_LV_FONT_MONTSERRAT_20"></a>

## 16.30 `CONFIG_LV_FONT_MONTSERRAT_20`

**提示（Prompt）**：Montserrat 20 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1686`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_FONT_MONTSERRAT_22"></a>

## 16.31 `CONFIG_LV_FONT_MONTSERRAT_22`

**提示（Prompt）**：Montserrat 22 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1688`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22)。

<a id="CONFIG_LV_FONT_MONTSERRAT_24"></a>

## 16.32 `CONFIG_LV_FONT_MONTSERRAT_24`

**提示（Prompt）**：Montserrat 24 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1690`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_FONT_MONTSERRAT_26"></a>

## 16.33 `CONFIG_LV_FONT_MONTSERRAT_26`

**提示（Prompt）**：Montserrat 26 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1692`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_FONT_MONTSERRAT_28"></a>

## 16.34 `CONFIG_LV_FONT_MONTSERRAT_28`

**提示（Prompt）**：Montserrat 28 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1694`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28)。

<a id="CONFIG_LV_FONT_MONTSERRAT_28_COMPRESSED"></a>

## 16.35 `CONFIG_LV_FONT_MONTSERRAT_28_COMPRESSED`

**提示（Prompt）**：Montserrat 28 字体，压缩（Compressed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1717`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED)。

<a id="CONFIG_LV_FONT_MONTSERRAT_30"></a>

## 16.36 `CONFIG_LV_FONT_MONTSERRAT_30`

**提示（Prompt）**：Montserrat 30 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1696`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30)。

<a id="CONFIG_LV_FONT_MONTSERRAT_32"></a>

## 16.37 `CONFIG_LV_FONT_MONTSERRAT_32`

**提示（Prompt）**：Montserrat 32 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1698`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32)。

<a id="CONFIG_LV_FONT_MONTSERRAT_34"></a>

## 16.38 `CONFIG_LV_FONT_MONTSERRAT_34`

**提示（Prompt）**：Montserrat 34 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1700`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34)。

<a id="CONFIG_LV_FONT_MONTSERRAT_36"></a>

## 16.39 `CONFIG_LV_FONT_MONTSERRAT_36`

**提示（Prompt）**：Montserrat 36 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1702`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36)。

<a id="CONFIG_LV_FONT_MONTSERRAT_38"></a>

## 16.40 `CONFIG_LV_FONT_MONTSERRAT_38`

**提示（Prompt）**：Montserrat 38 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1704`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38)。

<a id="CONFIG_LV_FONT_MONTSERRAT_40"></a>

## 16.41 `CONFIG_LV_FONT_MONTSERRAT_40`

**提示（Prompt）**：Montserrat 40 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1706`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40)。

<a id="CONFIG_LV_FONT_MONTSERRAT_42"></a>

## 16.42 `CONFIG_LV_FONT_MONTSERRAT_42`

**提示（Prompt）**：Montserrat 42 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1708`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42)。

<a id="CONFIG_LV_FONT_MONTSERRAT_44"></a>

## 16.43 `CONFIG_LV_FONT_MONTSERRAT_44`

**提示（Prompt）**：Montserrat 44 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1710`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44)。

<a id="CONFIG_LV_FONT_MONTSERRAT_46"></a>

## 16.44 `CONFIG_LV_FONT_MONTSERRAT_46`

**提示（Prompt）**：Montserrat 46 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1712`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46)。

<a id="CONFIG_LV_FONT_MONTSERRAT_48"></a>

## 16.45 `CONFIG_LV_FONT_MONTSERRAT_48`

**提示（Prompt）**：Montserrat 48 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1714`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48)。

<a id="CONFIG_LV_FONT_MONTSERRAT_8"></a>

## 16.46 `CONFIG_LV_FONT_MONTSERRAT_8`

**提示（Prompt）**：Montserrat 8 字体（Font）

**说明（Help）**

包含 ASCII 范围字符及部分符号的 Montserrat 字体，每像素位数（bpp）为 `4`。参见 [Montserrat 字体页面](https://fonts.google.com/specimen/Montserrat)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1670`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8)。

<a id="CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_14_CJK"></a>

## 16.47 `CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_14_CJK`

**提示（Prompt）**：SourceHanSansSC 14 字体，中日韩字符（CJK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1721`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK)。

<a id="CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_16_CJK"></a>

## 16.48 `CONFIG_LV_FONT_SOURCE_HAN_SANS_SC_16_CJK`

**提示（Prompt）**：SourceHanSansSC 16 字体，中日韩字符（CJK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1723`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK)。

<a id="CONFIG_LV_FONT_UNSCII_16"></a>

## 16.49 `CONFIG_LV_FONT_UNSCII_16`

**提示（Prompt）**：UNSCII 16 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_UNSCII_16
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1730`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_UNSCII_16`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_UNSCII_16)。

<a id="CONFIG_LV_FONT_UNSCII_8"></a>

## 16.50 `CONFIG_LV_FONT_UNSCII_8`

**提示（Prompt）**：UNSCII 8 字体（Font）

**说明（Help）**

像素精确的等宽字体（Pixel-perfect Monospaced Fonts）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_FONT_DEFAULT_UNSCII_8
```

**被弱选择（Implied by）**

```text
CONFIG_LV_COLOR_FORMAT_I1
CONFIG_LV_COLOR_FORMAT_L8
CONFIG_LV_COLOR_DEPTH_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1726`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 内置字体（Built-in Fonts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_UNSCII_8)、[`CONFIG_LV_COLOR_FORMAT_I1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_I1)、[`CONFIG_LV_COLOR_FORMAT_L8`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_L8)、[`CONFIG_LV_COLOR_DEPTH_8`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_8)。

<a id="CONFIG_LV_FONT_USE_CUSTOM_INCLUDE"></a>

## 16.51 `CONFIG_LV_FONT_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义字体声明头文件（Custom Font Declaration Header）

**说明（Help）**

包含 `LV_FONT_CUSTOM_INCLUDE` 指定的头文件，以声明自定义字体（`LV_FONT_CUSTOM_DECLARE`）或覆盖字体相关的宏。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1734`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FREETYPE_CACHE_FT_GLYPH_CNT"></a>

## 16.52 `CONFIG_LV_FREETYPE_CACHE_FT_GLYPH_CNT`

**提示（Prompt）**：字形缓存大小（Glyph Cache Size，字形数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FREETYPE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1910`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → FreeType 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FREETYPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FREETYPE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FREETYPE_CACHE_FT_GLYPH_L1"></a>

## 16.53 `CONFIG_LV_FREETYPE_CACHE_FT_GLYPH_L1`

**提示（Prompt）**：L1 字形度量缓存（Glyph Metrics Cache，无锁，仅限单线程）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_OS_NONE && CONFIG_LV_USE_FREETYPE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1914`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → FreeType 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_NONE)、[`CONFIG_LV_USE_FREETYPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FREETYPE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FREETYPE_USE_LVGL_PORT"></a>

## 16.54 `CONFIG_LV_FREETYPE_USE_LVGL_PORT`

**提示（Prompt）**：LVGL 内存与文件系统移植层（Memory and File System Port）

**说明（Help）**

启用后，FreeType 将使用 LVGL 的内存分配器（Memory Allocator）和文件系统抽象（File System Abstraction），代替平台默认实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FREETYPE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1903`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → FreeType 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FREETYPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FREETYPE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FRIDAY_STR"></a>

## 16.55 `CONFIG_LV_FRIDAY_STR`

**提示（Prompt）**：星期五的缩写字符串（Shortened String for Friday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Fr"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2009`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_ARDUINO_ESP_LITTLEFS_LETTER"></a>

## 16.56 `CONFIG_LV_FS_ARDUINO_ESP_LITTLEFS_LETTER`

**提示（Prompt）**：Arduino ESP littlefs 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3137`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Arduino ESP littlefs 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_ARDUINO_ESP_LITTLEFS_PATH"></a>

## 16.57 `CONFIG_LV_FS_ARDUINO_ESP_LITTLEFS_PATH`

**提示（Prompt）**：Arduino ESP littlefs 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3142`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Arduino ESP littlefs 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_ARDUINO_SD_LETTER"></a>

## 16.58 `CONFIG_LV_FS_ARDUINO_SD_LETTER`

**提示（Prompt）**：Arduino SD 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_ARDUINO_SD && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3153`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Arduino SD 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_ARDUINO_SD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_ARDUINO_SD)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_ARDUINO_SD_PATH"></a>

## 16.59 `CONFIG_LV_FS_ARDUINO_SD_PATH`

**提示（Prompt）**：Arduino SD 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_ARDUINO_SD && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3158`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Arduino SD 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_ARDUINO_SD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_ARDUINO_SD)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_DEFAULT_DRIVER_LETTER"></a>

## 16.60 `CONFIG_LV_FS_DEFAULT_DRIVER_LETTER`

**提示（Prompt）**：默认驱动器字母（Default Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**

设置默认驱动器字母（Default Drive Letter）后，可在文件路径中省略驱动前缀（Driver Prefix）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3024`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_FATFS_CACHE_SIZE"></a>

## 16.61 `CONFIG_LV_FS_FATFS_CACHE_SIZE`

**提示（Prompt）**：FatFS 读取缓存大小（Read Cache Size，字节，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_FATFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3109`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → FatFS 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_FATFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_FATFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_FATFS_LETTER"></a>

## 16.62 `CONFIG_LV_FS_FATFS_LETTER`

**提示（Prompt）**：FatFS 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_FATFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3100`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → FatFS 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_FATFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_FATFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_FATFS_PATH"></a>

## 16.63 `CONFIG_LV_FS_FATFS_PATH`

**提示（Prompt）**：FatFS 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_FATFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3105`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → FatFS 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_FATFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_FATFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_FROGFS_LETTER"></a>

## 16.64 `CONFIG_LV_FS_FROGFS_LETTER`

**提示（Prompt）**：FrogFS 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_FROGFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3178`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → FrogFS 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_FROGFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_FROGFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_LITTLEFS_LETTER"></a>

## 16.65 `CONFIG_LV_FS_LITTLEFS_LETTER`

**提示（Prompt）**：littlefs 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_LITTLEFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3121`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → littlefs 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_LITTLEFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_LITTLEFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_LITTLEFS_PATH"></a>

## 16.66 `CONFIG_LV_FS_LITTLEFS_PATH`

**提示（Prompt）**：littlefs 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_LITTLEFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3126`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → littlefs 文件系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_LITTLEFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_LITTLEFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_MEMFS_LETTER"></a>

## 16.67 `CONFIG_LV_FS_MEMFS_LETTER`

**提示（Prompt）**：memfs 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_MEMFS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3191`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → 内存映射（Memory-mapped）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_MEMFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_MEMFS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_POSIX_CACHE_SIZE"></a>

## 16.68 `CONFIG_LV_FS_POSIX_CACHE_SIZE`

**提示（Prompt）**：POSIX 读取缓存大小（Read Cache Size，字节，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_POSIX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3067`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → POSIX 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_POSIX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_POSIX_LETTER"></a>

## 16.69 `CONFIG_LV_FS_POSIX_LETTER`

**提示（Prompt）**：POSIX 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_POSIX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3058`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → POSIX 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_POSIX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_POSIX_PATH"></a>

## 16.70 `CONFIG_LV_FS_POSIX_PATH`

**提示（Prompt）**：POSIX 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_POSIX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3063`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → POSIX 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_POSIX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_STDIO_CACHE_SIZE"></a>

## 16.71 `CONFIG_LV_FS_STDIO_CACHE_SIZE`

**提示（Prompt）**：stdio 读取缓存大小（Read Cache Size，字节，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_STDIO && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3046`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → 标准输入／输出（stdio）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_STDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_STDIO)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_STDIO_LETTER"></a>

## 16.72 `CONFIG_LV_FS_STDIO_LETTER`

**提示（Prompt）**：stdio 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_STDIO && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3037`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → 标准输入／输出（stdio）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_STDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_STDIO)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_STDIO_PATH"></a>

## 16.73 `CONFIG_LV_FS_STDIO_PATH`

**提示（Prompt）**：stdio 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_STDIO && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3042`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → 标准输入／输出（stdio）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_STDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_STDIO)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_UEFI_LETTER"></a>

## 16.74 `CONFIG_LV_FS_UEFI_LETTER`

**提示（Prompt）**：UEFI 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_UEFI && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3168`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → 统一可扩展固件接口（UEFI）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_UEFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_UEFI)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_WIN32_CACHE_SIZE"></a>

## 16.75 `CONFIG_LV_FS_WIN32_CACHE_SIZE`

**提示（Prompt）**：Win32 读取缓存大小（Read Cache Size，字节，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_WIN32 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3088`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Win32 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_WIN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_WIN32)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_WIN32_LETTER"></a>

## 16.76 `CONFIG_LV_FS_WIN32_LETTER`

**提示（Prompt）**：Win32 驱动器字母（Drive Letter，65 表示 A，0 表示禁用）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_WIN32 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3079`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Win32 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_WIN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_WIN32)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FS_WIN32_PATH"></a>

## 16.77 `CONFIG_LV_FS_WIN32_PATH`

**提示（Prompt）**：Win32 工作目录（Working Directory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FS_WIN32 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3084`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System） → Win32 接口

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FS_WIN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FS_WIN32)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_G2D_HASH_TABLE_SIZE"></a>

## 16.78 `CONFIG_LV_G2D_HASH_TABLE_SIZE`

**提示（Prompt）**：缓冲区哈希表大小（Buffer Hash Table Size，条目数）

**说明（Help）**

为 G2D 绘制单元（Draw Unit）映射的最大缓冲区数量，包括帧缓冲区（Frame Buffer）和资源（Asset）。表满后，绘制将触发断言（Assert）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_G2D && CONFIG_LVGL
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1081`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维图形（G2D） → G2D 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_G2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_G2D)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GIF_CACHE_DECODE_DATA"></a>

## 16.79 `CONFIG_LV_GIF_CACHE_DECODE_DATA`

**提示（Prompt）**：缓存解码数据（Cache Decoded Data）

**说明（Help）**

加快播放速度，代价是额外占用 16 KB RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GIF && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2123`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → GIF 解码器（Decoder）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GIF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GIF_MAX_HEIGHT"></a>

## 16.80 `CONFIG_LV_GIF_MAX_HEIGHT`

**提示（Prompt）**：GIF 画布最大高度（Maximum Canvas Height，像素）

**说明（Help）**

拒绝高度超过此值的 GIF；该值不影响内存使用量（Memory Usage）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GIF && CONFIG_LVGL
```

**默认值（Defaults）**

```text
32768
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2136`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → GIF 解码器（Decoder）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GIF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GIF_MAX_WIDTH"></a>

## 16.81 `CONFIG_LV_GIF_MAX_WIDTH`

**提示（Prompt）**：GIF 画布最大宽度（Maximum Canvas Width，像素）

**说明（Help）**

拒绝宽度超过此值的 GIF；增大该值会增加内存使用量（Memory Usage）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GIF && CONFIG_LVGL
```

**默认值（Defaults）**

```text
480
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2129`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → GIF 解码器（Decoder）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GIF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GLOBAL_CUSTOM_INCLUDE"></a>

## 16.82 `CONFIG_LV_GLOBAL_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义 `lv_global` 头文件路径（Header Path）

**说明（Help）**

声明 `lv_global_t *lv_global_default(void);` 的头文件路径。凡是 LVGL 需要解析 `LV_GLOBAL_DEFAULT()` 宏的位置，都会包含此头文件。它会用于性能关键路径（Performance-critical Path），因此应保持轻量。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_GLOBAL_USE_CUSTOM_INCLUDE && CONFIG_LV_ENABLE_GLOBAL_CUSTOM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"lv_global.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3570`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 自定义 `lv_global`（Customization） → 自定义 `lv_global_default()` 头文件（Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_GLOBAL_USE_CUSTOM_INCLUDE`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_GLOBAL_USE_CUSTOM_INCLUDE)、[`CONFIG_LV_ENABLE_GLOBAL_CUSTOM`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_ENABLE_GLOBAL_CUSTOM)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GLOBAL_USE_CUSTOM_INCLUDE"></a>

## 16.83 `CONFIG_LV_GLOBAL_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义 `lv_global_default()` 头文件（Header）

**说明（Help）**

使用自定义头文件声明 `lv_global_t *lv_global_default(void);`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_ENABLE_GLOBAL_CUSTOM && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3564`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 自定义 `lv_global`（Customization）

**配置项引用（Symbol References）**：[`CONFIG_LV_ENABLE_GLOBAL_CUSTOM`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_ENABLE_GLOBAL_CUSTOM)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_GRADIENT_MAX_STOPS"></a>

## 16.84 `CONFIG_LV_GRADIENT_MAX_STOPS`

**提示（Prompt）**：最大渐变色标数量（Maximum Gradient Stops）

**说明（Help）**

每增加一个渐变色标（Gradient Stop），消耗 `sizeof(lv_color_t) + 1` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:553`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_IMAGE_HEADER_CACHE_DEF_CNT"></a>

## 16.85 `CONFIG_LV_IMAGE_HEADER_CACHE_DEF_CNT`

**提示（Prompt）**：默认图像头缓存大小（Image Header Cache Size，条目数，0 表示禁用）

**说明（Help）**

避免反复读取图像头（Image Header），代价是消耗 RAM。仅使用内置图像格式（Built-in Image Formats）时，收益有限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1538`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_IME_PINYIN_CAND_TEXT_NUM"></a>

## 16.86 `CONFIG_LV_IME_PINYIN_CAND_TEXT_NUM`

**提示（Prompt）**：最大候选面板数量（Maximum Number of Candidate Panels）

**说明（Help）**

根据屏幕大小调整此值，因为所有候选面板（Candidate Panel）都必须容纳在屏幕中。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_IME_PINYIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2192`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 拼音输入法（Pinyin Input Method）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_IME_PINYIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_IME_PINYIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_IME_PINYIN_K9_CAND_TEXT_NUM"></a>

## 16.87 `CONFIG_LV_IME_PINYIN_K9_CAND_TEXT_NUM`

**提示（Prompt）**：九键输入模式（9-key Input Mode）的最大候选面板数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_IME_PINYIN_USE_K9_MODE && CONFIG_LV_USE_IME_PINYIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2180`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 拼音输入法（Pinyin Input Method） → 九键输入模式（9-key Input Mode）

**配置项引用（Symbol References）**：[`CONFIG_LV_IME_PINYIN_USE_K9_MODE`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_IME_PINYIN_USE_K9_MODE)、[`CONFIG_LV_USE_IME_PINYIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_IME_PINYIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_IME_PINYIN_USE_DEFAULT_DICT"></a>

## 16.88 `CONFIG_LV_IME_PINYIN_USE_DEFAULT_DICT`

**提示（Prompt）**：内置词典（Built-in Dictionary）

**说明（Help）**

如果不使用内置词典，必须在使用输入法（IME）之前通过 `lv_ime_pinyin_set_dict()` 设置词典。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_IME_PINYIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2185`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 拼音输入法（Pinyin Input Method）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_IME_PINYIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_IME_PINYIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_IME_PINYIN_USE_K9_MODE"></a>

## 16.89 `CONFIG_LV_IME_PINYIN_USE_K9_MODE`

**提示（Prompt）**：九键输入模式（9-key Input Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_IME_PINYIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2176`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 拼音输入法（Pinyin Input Method）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_IME_PINYIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_IME_PINYIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_DOUBLE_CLICK_TIME"></a>

## 16.90 `CONFIG_LV_INDEV_DEF_DOUBLE_CLICK_TIME`

**提示（Prompt）**：多次点击时间（Multi-click Time，ms）

**说明（Help）**

连续点击被计为双击或三击时，点击之间允许的最大时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
400
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1230`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_LIMIT"></a>

## 16.91 `CONFIG_LV_INDEV_DEF_GESTURE_LIMIT`

**提示（Prompt）**：手势阈值（Gesture Threshold，px）

**说明（Help）**

检测到手势（Gesture）之前，指针需要移动的距离。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1237`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_MIN_VELOCITY"></a>

## 16.92 `CONFIG_LV_INDEV_DEF_GESTURE_MIN_VELOCITY`

**提示（Prompt）**：手势最小速度（Gesture Minimum Velocity，px）

**说明（Help）**

松开时报告滑动（Swipe）所需的最小指针速度（Pointer Velocity）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1244`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_PINCH_DOWN_THRESHOLD"></a>

## 16.93 `CONFIG_LV_INDEV_DEF_GESTURE_PINCH_DOWN_THRESHOLD`

**提示（Prompt）**：捏合缩小阈值（Pinch-in Threshold，%）

**说明（Help）**

发送捏合事件（Pinch Event）之前，手指需要捏合缩小到的比例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GESTURE_RECOGNITION && CONFIG_LVGL
```

**默认值（Defaults）**

```text
75
```

**取值范围（Ranges）**

```text
[1, 99]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1273`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices） → 多点触控手势识别（Multi-touch Gesture Recognition）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GESTURE_RECOGNITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GESTURE_RECOGNITION)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_PINCH_MAX_INITIAL_SCALE"></a>

## 16.94 `CONFIG_LV_INDEV_DEF_GESTURE_PINCH_MAX_INITIAL_SCALE`

**提示（Prompt）**：捏合最大初始比例（Pinch Maximum Initial Scale，%）

**说明（Help）**

初始比例高于此值的捏合（Pinch）将被丢弃。该值必须大于捏合放大阈值（Pinch-out Threshold）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GESTURE_RECOGNITION && CONFIG_LVGL
```

**默认值（Defaults）**

```text
250
```

**取值范围（Ranges）**

```text
[101, 1000]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1287`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices） → 多点触控手势识别（Multi-touch Gesture Recognition）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GESTURE_RECOGNITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GESTURE_RECOGNITION)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_PINCH_UP_THRESHOLD"></a>

## 16.95 `CONFIG_LV_INDEV_DEF_GESTURE_PINCH_UP_THRESHOLD`

**提示（Prompt）**：捏合放大阈值（Pinch-out Threshold，%）

**说明（Help）**

发送捏合事件（Pinch Event）之前，手指需要张开放大到的比例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GESTURE_RECOGNITION && CONFIG_LVGL
```

**默认值（Defaults）**

```text
150
```

**取值范围（Ranges）**

```text
[101, 1000]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1280`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices） → 多点触控手势识别（Multi-touch Gesture Recognition）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GESTURE_RECOGNITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GESTURE_RECOGNITION)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_GESTURE_ROTATION_THRESHOLD"></a>

## 16.96 `CONFIG_LV_INDEV_DEF_GESTURE_ROTATION_THRESHOLD`

**提示（Prompt）**：旋转阈值（Rotation Threshold，mrad）

**说明（Help）**

发送旋转事件（Rotation Event）之前，手指需要旋转的角度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GESTURE_RECOGNITION && CONFIG_LVGL
```

**默认值（Defaults）**

```text
200
```

**取值范围（Ranges）**

```text
[1, 3141]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1295`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices） → 多点触控手势识别（Multi-touch Gesture Recognition）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GESTURE_RECOGNITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GESTURE_RECOGNITION)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_LONG_PRESS_REP_TIME"></a>

## 16.97 `CONFIG_LV_INDEV_DEF_LONG_PRESS_REP_TIME`

**提示（Prompt）**：长按重复周期（Long Press Repeat Period，ms）

**说明（Help）**

`LV_EVENT_LONG_PRESSED_REPEAT` 事件之间的时间间隔。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1223`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_LONG_PRESS_TIME"></a>

## 16.98 `CONFIG_LV_INDEV_DEF_LONG_PRESS_TIME`

**提示（Prompt）**：长按时间（Long Press Time，ms）

**说明（Help）**

按住达到该时长后，发送 `LV_EVENT_LONG_PRESSED` 事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
400
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1216`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_ROTARY_SENSITIVITY"></a>

## 16.99 `CONFIG_LV_INDEV_DEF_ROTARY_SENSITIVITY`

**提示（Prompt）**：旋转灵敏度（Rotary Sensitivity）

**说明（Help）**

编码器增量（Encoder Diff）乘以此值后再除以 `256`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1251`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_SCROLL_ELASTIC_FACTOR"></a>

## 16.100 `CONFIG_LV_INDEV_DEF_SCROLL_ELASTIC_FACTOR`

**提示（Prompt）**：弹性滚动减速系数（Elastic Scroll Slow-down Factor）

**说明（Help）**

滚动超过可滚动控件（Scrollable Widget）的边缘时，按此系数减慢滚动速度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1209`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<!-- kconfig-navigation -->

[上一章](P015_module_lvgl_zephyr_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P017_module_lvgl_zephyr_配置项参考_3.md)
