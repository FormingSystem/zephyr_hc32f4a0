---
id: learning.zephyr-docs.kconfig-reference.page-18
title: "`<module:lvgl>/zephyr`配置项参考（4/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第18章\_`<module:lvgl>/zephyr`配置项参考（4/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_OS_CUSTOM"></a>

## 18.1 `CONFIG_LV_OS_CUSTOM`

**提示（Prompt）**：自定义（Custom）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_CUSTOM_INCLUDE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:195`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_CUSTOM_INCLUDE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_CUSTOM_INCLUDE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_CUSTOM_INCLUDE`。

<a id="CONFIG_LV_OS_CUSTOM_INCLUDE"></a>

## 18.2 `CONFIG_LV_OS_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义操作系统包含头文件（Custom OS Include Header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_OS_CUSTOM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:236`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_CUSTOM`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_CUSTOM)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OS_FREERTOS"></a>

## 18.3 `CONFIG_LV_OS_FREERTOS`

**提示（Prompt）**：FreeRTOS 实时操作系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_FREERTOS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:177`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_FREERTOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_FREERTOS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_FREERTOS`。

<a id="CONFIG_LV_OS_IDLE_PERCENT_CUSTOM"></a>

## 18.4 `CONFIG_LV_OS_IDLE_PERCENT_CUSTOM`

**提示（Prompt）**：自定义空闲百分比计算（Idle Percentage Calculation）

**说明（Help）**

自行提供 `lv_os_get_idle_percent()`。这对多核系统（Multi-core System）很有用，因为默认 FreeRTOS 实现可能无法跟踪所有内核的空闲时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_OS_FREERTOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:252`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → FreeRTOS 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_FREERTOS`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_FREERTOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OS_MQX"></a>

## 18.5 `CONFIG_LV_OS_MQX`

**提示（Prompt）**：MQX 实时操作系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_MQX
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:189`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_MQX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_MQX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_MQX`。

<a id="CONFIG_LV_OS_NONE"></a>

## 18.6 `CONFIG_LV_OS_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:172`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)。

<a id="CONFIG_LV_OS_PTHREAD"></a>

## 18.7 `CONFIG_LV_OS_PTHREAD`

**提示（Prompt）**：POSIX 线程（pthread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_PTHREAD
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:174`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_PTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_PTHREAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_PTHREAD`。

<a id="CONFIG_LV_OS_RTTHREAD"></a>

## 18.8 `CONFIG_LV_OS_RTTHREAD`

**提示（Prompt）**：RT-Thread 实时操作系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_RTTHREAD
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:183`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_RTTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_RTTHREAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_RTTHREAD`。

<a id="CONFIG_LV_OS_SDL2"></a>

## 18.9 `CONFIG_LV_OS_SDL2`

**提示（Prompt）**：SDL2 多媒体库

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_SDL2
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:192`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_SDL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_SDL2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_SDL2`。

<a id="CONFIG_LV_OS_WINDOWS"></a>

## 18.10 `CONFIG_LV_OS_WINDOWS`

**提示（Prompt）**：Windows 操作系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_WINDOWS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:186`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_WINDOWS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_WINDOWS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_WINDOWS`。

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_LEFT"></a>

## 18.11 `CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_LEFT`

**提示（Prompt）**：左下（Bottom Left）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3233`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_MID"></a>

## 18.12 `CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_MID`

**提示（Prompt）**：下方居中（Bottom Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3235`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_RIGHT"></a>

## 18.13 `CONFIG_LV_PERF_MONITOR_ALIGN_BOTTOM_RIGHT`

**提示（Prompt）**：右下（Bottom Right）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3237`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_CENTER"></a>

## 18.14 `CONFIG_LV_PERF_MONITOR_ALIGN_CENTER`

**提示（Prompt）**：中央（Center）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3243`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_LEFT_MID"></a>

## 18.15 `CONFIG_LV_PERF_MONITOR_ALIGN_LEFT_MID`

**提示（Prompt）**：左侧居中（Left Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3239`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_RIGHT_MID"></a>

## 18.16 `CONFIG_LV_PERF_MONITOR_ALIGN_RIGHT_MID`

**提示（Prompt）**：右侧居中（Right Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3241`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_TOP_LEFT"></a>

## 18.17 `CONFIG_LV_PERF_MONITOR_ALIGN_TOP_LEFT`

**提示（Prompt）**：左上（Top Left）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3227`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_TOP_MID"></a>

## 18.18 `CONFIG_LV_PERF_MONITOR_ALIGN_TOP_MID`

**提示（Prompt）**：上方居中（Top Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3229`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PERF_MONITOR_ALIGN_TOP_RIGHT"></a>

## 18.19 `CONFIG_LV_PERF_MONITOR_ALIGN_TOP_RIGHT`

**提示（Prompt）**：右上（Top Right）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3231`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor） → 性能监测器位置（Performance Monitor Position）

<a id="CONFIG_LV_PPA_BURST_LENGTH_128"></a>

## 18.20 `CONFIG_LV_PPA_BURST_LENGTH_128`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:968`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer） → PPA 突发长度（Burst Length，字节）

<a id="CONFIG_LV_PPA_BURST_LENGTH_16"></a>

## 18.21 `CONFIG_LV_PPA_BURST_LENGTH_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:962`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer） → PPA 突发长度（Burst Length，字节）

<a id="CONFIG_LV_PPA_BURST_LENGTH_32"></a>

## 18.22 `CONFIG_LV_PPA_BURST_LENGTH_32`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:964`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer） → PPA 突发长度（Burst Length，字节）

<a id="CONFIG_LV_PPA_BURST_LENGTH_64"></a>

## 18.23 `CONFIG_LV_PPA_BURST_LENGTH_64`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:966`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer） → PPA 突发长度（Burst Length，字节）

<a id="CONFIG_LV_PPA_BURST_LENGTH_8"></a>

## 18.24 `CONFIG_LV_PPA_BURST_LENGTH_8`

**提示（Prompt）**：8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:960`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer） → PPA 突发长度（Burst Length，字节）

<a id="CONFIG_LV_PROFILER_BUILTIN_BUF_SIZE"></a>

## 18.25 `CONFIG_LV_PROFILER_BUILTIN_BUF_SIZE`

**提示（Prompt）**：跟踪缓冲区大小（Trace Buffer Size，字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER_BUILTIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
16384
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3326`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 内置性能分析器（Built-in Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER_BUILTIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_BUILTIN_DEFAULT_ENABLE"></a>

## 18.26 `CONFIG_LV_PROFILER_BUILTIN_DEFAULT_ENABLE`

**提示（Prompt）**：初始化时开始性能分析（Profiling）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER_BUILTIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3330`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 内置性能分析器（Built-in Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER_BUILTIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_CACHE"></a>

## 18.27 `CONFIG_LV_PROFILER_CACHE`

**提示（Prompt）**：缓存（Cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3406`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_DECODER"></a>

## 18.28 `CONFIG_LV_PROFILER_DECODER`

**提示（Prompt）**：图像解码器（Image Decoder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3386`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_DRAW"></a>

## 18.29 `CONFIG_LV_PROFILER_DRAW`

**提示（Prompt）**：绘制（Draw）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3378`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_EVENT"></a>

## 18.30 `CONFIG_LV_PROFILER_EVENT`

**提示（Prompt）**：事件（Events）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3410`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_FONT"></a>

## 18.31 `CONFIG_LV_PROFILER_FONT`

**提示（Prompt）**：字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3390`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_FS"></a>

## 18.32 `CONFIG_LV_PROFILER_FS`

**提示（Prompt）**：文件系统（File System）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3394`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_INCLUDE"></a>

## 18.33 `CONFIG_LV_PROFILER_INCLUDE`

**提示（Prompt）**：性能分析器头文件（Profiler Header）

**说明（Help）**

定义以下性能分析器钩子宏（Profiler Hook Macros）的头文件路径：

`LV_PROFILER_BEGIN`：在被分析的作用域（Profiled Scope）开始时调用。示例：

```c
#define LV_PROFILER_BEGIN  my_profiler_begin()
```

`LV_PROFILER_END`：在被分析的作用域结束时调用。示例：

```c
#define LV_PROFILER_END    my_profiler_end()
```

`LV_PROFILER_BEGIN_TAG(tag)`：在带字符串标签（String Tag）的被分析作用域开始时调用。示例：

```c
#define LV_PROFILER_BEGIN_TAG(tag)  my_profiler_begin_tag(tag)
```

`LV_PROFILER_END_TAG(tag)`：在带字符串标签的被分析作用域结束时调用。示例：

```c
#define LV_PROFILER_END_TAG(tag)    my_profiler_end_tag(tag)
```

默认头文件通过内置性能分析器提供这些宏。将此项设为自己的头文件，即可使用自定义性能分析后端（Profiler Backend）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"lvgl/debugging/profiler/lv_profiler_builtin.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3343`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_INDEV"></a>

## 18.34 `CONFIG_LV_PROFILER_INDEV`

**提示（Prompt）**：输入设备（Input Devices）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3382`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_LAYOUT"></a>

## 18.35 `CONFIG_LV_PROFILER_LAYOUT`

**提示（Prompt）**：布局（Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3370`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_REFR"></a>

## 18.36 `CONFIG_LV_PROFILER_REFR`

**提示（Prompt）**：显示刷新（Display Refresh）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3374`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_STYLE"></a>

## 18.37 `CONFIG_LV_PROFILER_STYLE`

**提示（Prompt）**：样式（Style）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3398`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_PROFILER_TIMER"></a>

## 18.38 `CONFIG_LV_PROFILER_TIMER`

**提示（Prompt）**：定时器（Timer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3402`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 进行性能分析的模块（Profiled Modules）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_PROFILER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_QNX_BUF_COUNT"></a>

## 18.39 `CONFIG_LV_QNX_BUF_COUNT`

**提示（Prompt）**：屏幕大小缓冲区数量（Number of Screen-sized Buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_QNX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2759`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → QNX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_QNX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_QNX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SATURDAY_STR"></a>

## 18.40 `CONFIG_LV_SATURDAY_STR`

**提示（Prompt）**：星期六的缩写字符串（Shortened String for Saturday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Sa"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2012`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_ACCELERATED"></a>

## 18.41 `CONFIG_LV_SDL_ACCELERATED`

**提示（Prompt）**：硬件加速（Hardware Acceleration）

**说明（Help）**

向 SDL 请求使用 GPU 的渲染器（GPU-backed Renderer），而非软件渲染器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2859`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_AUTO_BACKEND"></a>

## 18.42 `CONFIG_LV_SDL_AUTO_BACKEND`

**提示（Prompt）**：自动选择 SDL 后端（Backend，旧版行为）

**说明（Help）**

这是计划移除的旧版行为（Legacy Behavior）：按旧方式推断 EGL，即 `LV_USE_OPENGLES` 配合 OpenGL 绘制单元。请禁用此项，并在“渲染后端（Rendering Backend）”选项中显式选择后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2776`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_BACKEND_EGL"></a>

## 18.43 `CONFIG_LV_SDL_BACKEND_EGL`

**提示（Prompt）**：EGL，使用 OpenGL ES 硬件加速（Hardware-accelerated）

**说明（Help）**

通过 EGL/OpenGL ES 上下文（Context）呈现帧。需要 OpenGL ES 或 NanoVG 渲染器（Renderer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_LV_USE_DRAW_OPENGLES || CONFIG_LV_USE_DRAW_NANOVG) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_LV_SDL_USE_EGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2802`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染后端（Rendering Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_OPENGLES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_USE_DRAW_NANOVG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_SDL_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_SDL_USE_EGL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_SDL_USE_EGL`。

<a id="CONFIG_LV_SDL_BACKEND_SW"></a>

## 18.44 `CONFIG_LV_SDL_BACKEND_SW`

**提示（Prompt）**：软件（Software，SDL 表面）

**说明（Help）**

使用软件渲染（Software Rendering），并通过 SDL 表面（Surface）上传。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2791`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染后端（Rendering Backend）

<a id="CONFIG_LV_SDL_BACKEND_TEXTURE"></a>

## 18.45 `CONFIG_LV_SDL_BACKEND_TEXTURE`

**提示（Prompt）**：缓存的 SDL 纹理（Cached SDL Textures）

**说明（Help）**

渲染到缓存的 SDL 纹理（Texture）中。此项启用 SDL 渲染器（Renderer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_SDL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2796`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染后端（Rendering Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SDL)。

<a id="CONFIG_LV_SDL_BUF_COUNT"></a>

## 18.46 `CONFIG_LV_SDL_BUF_COUNT`

**提示（Prompt）**：屏幕大小缓冲区数量（Number of Screen-sized Buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2843`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_DIRECT_EXIT"></a>

## 18.47 `CONFIG_LV_SDL_DIRECT_EXIT`

**提示（Prompt）**：关闭所有窗口时退出（Exit When All Windows Are Closed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2869`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_DOUBLE_BUFFER"></a>

## 18.48 `CONFIG_LV_SDL_DOUBLE_BUFFER`

**提示（Prompt）**：两个屏幕大小的缓冲区（Screen-sized Buffers）［已弃用：将 `LV_SDL_BUF_COUNT` 设为 2］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2855`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → SDL 缓冲区数量（Buffer Count）［已弃用：使用 `LV_SDL_BUF_COUNT`］

<a id="CONFIG_LV_SDL_FULLSCREEN"></a>

## 18.49 `CONFIG_LV_SDL_FULLSCREEN`

**提示（Prompt）**：全屏（Fullscreen）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2865`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_INCLUDE_PATH"></a>

## 18.50 `CONFIG_LV_SDL_INCLUDE_PATH`

**提示（Prompt）**：SDL 包含路径（Include Path）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SDL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"SDL2/SDL.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2772`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SDL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SDL_MOUSEWHEEL_MODE_CROWN"></a>

## 18.51 `CONFIG_LV_SDL_MOUSEWHEEL_MODE_CROWN`

**提示（Prompt）**：智能手表表冠（Smart Watch Crown）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2880`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → SDL 鼠标滚轮模式（Mousewheel Mode）

<a id="CONFIG_LV_SDL_MOUSEWHEEL_MODE_ENCODER"></a>

## 18.52 `CONFIG_LV_SDL_MOUSEWHEEL_MODE_ENCODER`

**提示（Prompt）**：编码器输入设备（Encoder Input Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2877`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → SDL 鼠标滚轮模式（Mousewheel Mode）

<a id="CONFIG_LV_SDL_RENDER_MODE_DIRECT"></a>

## 18.53 `CONFIG_LV_SDL_RENDER_MODE_DIRECT`

**提示（Prompt）**：直接模式（Direct Mode）

**说明（Help）**

将内容渲染到屏幕大小缓冲区中的正确位置，使缓冲区始终保存完整图像，并仅刷新变化区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2832`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染模式（Render Mode）

<a id="CONFIG_LV_SDL_RENDER_MODE_FULL"></a>

## 18.54 `CONFIG_LV_SDL_RENDER_MODE_FULL`

**提示（Prompt）**：全屏模式（Full Mode）

**说明（Help）**

即使只有一个像素发生变化，也始终重绘整个屏幕。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2837`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染模式（Render Mode）

<a id="CONFIG_LV_SDL_RENDER_MODE_PARTIAL"></a>

## 18.55 `CONFIG_LV_SDL_RENDER_MODE_PARTIAL`

**提示（Prompt）**：局部模式（Partial Mode）

**说明（Help）**

将屏幕拆成较小部分进行渲染，使缓冲区可以小于显示区域，从而节省 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2827`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → 渲染模式（Render Mode）

<a id="CONFIG_LV_SDL_SINGLE_BUFFER"></a>

## 18.56 `CONFIG_LV_SDL_SINGLE_BUFFER`

**提示（Prompt）**：一个屏幕大小的缓冲区（Screen-sized Buffer）［已弃用：将 `LV_SDL_BUF_COUNT` 设为 1］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2852`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → SDL 多媒体库 → SDL 缓冲区数量（Buffer Count）［已弃用：使用 `LV_SDL_BUF_COUNT`］

<a id="CONFIG_LV_SEPTEMBER_STR"></a>

## 18.57 `CONFIG_LV_SEPTEMBER_STR`

**提示（Prompt）**：九月名称字符串（String for September）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"September"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2047`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SPAN_SNIPPET_STACK_SIZE"></a>

## 18.58 `CONFIG_LV_SPAN_SNIPPET_STACK_SIZE`

**提示（Prompt）**：最大文本片段描述符数量（Maximum Number of Span Descriptors）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SPAN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2287`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 文本片段（Span）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SPAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SPAN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_STDARG_INCLUDE"></a>

## 18.59 `CONFIG_LV_STDARG_INCLUDE`

**提示（Prompt）**：可变参数处理（Variadic Argument Handling）的头文件 `stdarg`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stdarg.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:159`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_STDBOOL_INCLUDE"></a>

## 18.60 `CONFIG_LV_STDBOOL_INCLUDE`

**提示（Prompt）**：布尔类型（Boolean Types）的头文件 `stdbool`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stdbool.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:147`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_STDDEF_INCLUDE"></a>

## 18.61 `CONFIG_LV_STDDEF_INCLUDE`

**提示（Prompt）**：标准定义（Standard Definitions）的头文件 `stddef`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stddef.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:143`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_STDINT_INCLUDE"></a>

## 18.62 `CONFIG_LV_STDINT_INCLUDE`

**提示（Prompt）**：整数类型（Integer Types）的头文件 `stdint`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stdint.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:139`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ST_LTDC_USE_DMA2D_FLUSH"></a>

## 18.63 `CONFIG_LV_ST_LTDC_USE_DMA2D_FLUSH`

**提示（Prompt）**：局部模式显示器的 DMA2D 刷新（Flush）

**说明（Help）**

使用 DMA2D 刷新局部模式（Partial Mode）的 LTDC 显示器，与渲染并行执行。仅在 DMA2D 渲染器（Renderer）禁用时可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_DRAW_DMA2D && CONFIG_LV_USE_ST_LTDC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2535`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → ST LCD-TFT 显示控制器（LTDC）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_DMA2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_DMA2D)、[`CONFIG_LV_USE_ST_LTDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_ST_LTDC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SUNDAY_STR"></a>

## 18.64 `CONFIG_LV_SUNDAY_STR`

**提示（Prompt）**：星期日的缩写字符串（Shortened String for Sunday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Su"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2015`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SYSMON_CUSTOM_INCLUDE"></a>

## 18.65 `CONFIG_LV_SYSMON_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义系统监测头文件路径（Sysmon Header Path）

**说明（Help）**

可选头文件，用于覆盖系统监测器（System Monitor）的空闲测量宏（Idle Measurement Macros）。

`LV_SYSMON_GET_IDLE`：返回自上次调用以来 CPU 空闲百分比（0～100）的表达式，例如 `my_rtos_get_idle_percent()`。

`LV_SYSMON_GET_PROC_IDLE`：如果实时操作系统（RTOS）支持，返回每进程空闲百分比（Per-process Idle Percentage）的表达式。需要启用 `LV_SYSMON_PROC_IDLE_AVAILABLE`，例如 `my_rtos_get_proc_idle_percent()`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_SYSMON_USE_CUSTOM_INCLUDE && CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3293`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 自定义系统监测头文件（Sysmon Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_SYSMON_USE_CUSTOM_INCLUDE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_SYSMON_USE_CUSTOM_INCLUDE)、[`CONFIG_LV_USE_SYSMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SYSMON_PROC_IDLE_AVAILABLE"></a>

## 18.66 `CONFIG_LV_SYSMON_PROC_IDLE_AVAILABLE`

**提示（Prompt）**：每进程空闲测量（Per-process Idle Measurement）

**说明（Help）**

除系统整体空闲百分比外，移植层（Port）还通过 `lv_os_get_proc_idle_percent` 提供每进程空闲百分比（Per-process Idle Percentage）。LVGL 为 Linux 系统提供默认实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3209`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SYSMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_SYSMON_USE_CUSTOM_INCLUDE"></a>

## 18.67 `CONFIG_LV_SYSMON_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义系统监测头文件（Sysmon Header）

**说明（Help）**

包含 `LV_SYSMON_CUSTOM_INCLUDE` 指定的头文件，以覆盖 `LV_SYSMON_GET_IDLE` 等系统监测器宏（System Monitor Macros）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3286`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SYSMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TEST_SCREENSHOT_CREATE_REFERENCE_IMAGE"></a>

## 18.68 `CONFIG_LV_TEST_SCREENSHOT_CREATE_REFERENCE_IMAGE`

**提示（Prompt）**：创建缺失的参考图像（Reference Images）

**说明（Help）**

如果参考图像（Reference Image）尚不存在，则根据渲染后的屏幕创建该图像，而不是让比较失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE && CONFIG_LV_USE_TEST && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3433`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 测试工具（Test Utilities） → 测试工具（Test Utilities） → 截图比较（Screenshot Compare）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE)、[`CONFIG_LV_USE_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TEST)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TEXTAREA_DEF_PWD_SHOW_TIME"></a>

## 18.69 `CONFIG_LV_TEXTAREA_DEF_PWD_SHOW_TIME`

**提示（Prompt）**：默认密码显示时间（Password Show Time，ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TEXTAREA && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2309`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 文本区域（Text Area）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TEXTAREA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TEXTAREA)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_THEME_DEFAULT_DARK"></a>

## 18.70 `CONFIG_LV_THEME_DEFAULT_DARK`

**提示（Prompt）**：深色模式（Dark Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_THEME_DEFAULT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1489`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes） → 默认主题（Default Theme）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_THEME_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_THEME_DEFAULT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_THEME_DEFAULT_GROW"></a>

## 18.71 `CONFIG_LV_THEME_DEFAULT_GROW`

**提示（Prompt）**：按下时放大（Grow on Press）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_THEME_DEFAULT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1493`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes） → 默认主题（Default Theme）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_THEME_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_THEME_DEFAULT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_THEME_DEFAULT_TRANSITION_TIME"></a>

## 18.72 `CONFIG_LV_THEME_DEFAULT_TRANSITION_TIME`

**提示（Prompt）**：过渡时间（Transition Time，ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_THEME_DEFAULT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1497`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes） → 默认主题（Default Theme）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_THEME_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_THEME_DEFAULT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_THURSDAY_STR"></a>

## 18.73 `CONFIG_LV_THURSDAY_STR`

**提示（Prompt）**：星期四的缩写字符串（Shortened String for Thursday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Th"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2006`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TINY_TTF_CACHE_GLYPH_CNT"></a>

## 18.74 `CONFIG_LV_TINY_TTF_CACHE_GLYPH_CNT`

**提示（Prompt）**：字形缓存大小（Glyph Cache Size，字形数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TINY_TTF && CONFIG_LVGL
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1929`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → Tiny TTF 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TINY_TTF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TINY_TTF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TINY_TTF_CACHE_KERNING_CNT"></a>

## 18.75 `CONFIG_LV_TINY_TTF_CACHE_KERNING_CNT`

**提示（Prompt）**：字偶距缓存大小（Kerning Cache Size，条目数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TINY_TTF && CONFIG_LVGL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1933`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → Tiny TTF 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TINY_TTF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TINY_TTF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TINY_TTF_FILE_SUPPORT"></a>

## 18.76 `CONFIG_LV_TINY_TTF_FILE_SUPPORT`

**提示（Prompt）**：从文件加载 TTF 数据（Data）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TINY_TTF && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1926`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → Tiny TTF 字体引擎

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TINY_TTF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TINY_TTF)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TUESDAY_STR"></a>

## 18.77 `CONFIG_LV_TUESDAY_STR`

**提示（Prompt）**：星期二的缩写字符串（Shortened String for Tuesday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Tu"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2000`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TXT_BREAK_CHARS"></a>

## 18.78 `CONFIG_LV_TXT_BREAK_CHARS`

**提示（Prompt）**：用于文本断行／换行的字符（Text Break/Wrap Characters）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
" ,.;:-_)]}"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1615`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TXT_COLOR_CMD"></a>

## 18.79 `CONFIG_LV_TXT_COLOR_CMD`

**提示（Prompt）**：文本重新着色控制字符（Text Recoloring Control Character）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"#"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1640`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TXT_ENC"></a>

## 18.80 `CONFIG_LV_TXT_ENC`

**提示（Prompt）**：字符串字符编码（Character Encoding）

**说明（Help）**

集成开发环境（IDE）或编辑器应设置为相同的字符编码（Character Encoding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_TXT_ENC_UTF8
```

**可选项（Choices）**

```text
CONFIG_LV_TXT_ENC_UTF8
CONFIG_LV_TXT_ENC_ASCII
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1603`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_TXT_ENC_UTF8`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_ENC_UTF8)、[`CONFIG_LV_TXT_ENC_ASCII`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_ENC_ASCII)。

<a id="CONFIG_LV_TXT_ENC_ASCII"></a>

## 18.81 `CONFIG_LV_TXT_ENC_ASCII`

**提示（Prompt）**：ASCII 字符编码

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_TXT_ENC>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1611`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 字符串字符编码（Character Encoding）

**配置项引用（Symbol References）**：[`CONFIG_LV_TXT_ENC`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_ENC)。

<a id="CONFIG_LV_TXT_ENC_UTF8"></a>

## 18.82 `CONFIG_LV_TXT_ENC_UTF8`

**提示（Prompt）**：UTF-8 字符编码

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_TXT_ENC>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1609`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 字符串字符编码（Character Encoding）

**配置项引用（Symbol References）**：[`CONFIG_LV_TXT_ENC`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_ENC)。

<a id="CONFIG_LV_TXT_LINE_BREAK_LONG_LEN"></a>

## 18.83 `CONFIG_LV_TXT_LINE_BREAK_LONG_LEN`

**提示（Prompt）**：长单词断行长度（Line Break Long Length）

**说明（Help）**

如果单词至少达到此长度，将在视觉上“最合适”的位置断行（Break）。设为小于或等于 `0` 的值可禁用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1619`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TXT_LINE_BREAK_LONG_POST_MIN_LEN"></a>

## 18.84 `CONFIG_LV_TXT_LINE_BREAK_LONG_POST_MIN_LEN`

**提示（Prompt）**：断行后最少字符数（Min Characters After Break）

**说明（Help）**

长单词断行（Break）后放在下一行上的最少字符数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_TXT_LINE_BREAK_LONG_LEN > 0 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1633`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_TXT_LINE_BREAK_LONG_LEN`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_LINE_BREAK_LONG_LEN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_TXT_LINE_BREAK_LONG_PRE_MIN_LEN"></a>

## 18.85 `CONFIG_LV_TXT_LINE_BREAK_LONG_PRE_MIN_LEN`

**提示（Prompt）**：断行前最少字符数（Min Characters Before Break）

**说明（Help）**

长单词断行（Break）前保留在当前行上的最少字符数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_TXT_LINE_BREAK_LONG_LEN > 0 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1626`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_TXT_LINE_BREAK_LONG_LEN`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_TXT_LINE_BREAK_LONG_LEN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_UEFI_USE_MEMORY_SERVICES"></a>

## 18.86 `CONFIG_LV_UEFI_USE_MEMORY_SERVICES`

**提示（Prompt）**：使用启动服务表中的内存服务（Memory Services from Boot Services Table）

**说明（Help）**

使用 UEFI 启动服务（Boot Services）而非 C 库分配内存。仅对自定义标准库内存分配实现（Custom Stdlib Malloc Implementation）生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_UEFI && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2903`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → 统一可扩展固件接口（UEFI）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_UEFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_UEFI)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_3DTEXTURE"></a>

## 18.87 `CONFIG_LV_USE_3DTEXTURE`

**提示（Prompt）**：三维纹理（3D Texture）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_HAS_3D_SUPPORT && CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_GLTF
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1952`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_HAS_3D_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_3D_SUPPORT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GLTF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_GLTF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_3D_SUPPORT`。

<a id="CONFIG_LV_USE_ANIMIMG"></a>

## 18.88 `CONFIG_LV_USE_ANIMIMG`

**提示（Prompt）**：动画图像（Animated Image）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1956`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ARABIC_PERSIAN_CHARS"></a>

## 18.89 `CONFIG_LV_USE_ARABIC_PERSIAN_CHARS`

**提示（Prompt）**：阿拉伯文／波斯文字符整形（Arabic/Persian Character Shaping）

**说明（Help）**

在这些语言中，应根据字符在文本中的位置，将字符替换为另一种形态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1664`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ARC"></a>

## 18.90 `CONFIG_LV_USE_ARC`

**提示（Prompt）**：圆弧（Arc）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1960`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ARCLABEL"></a>

## 18.91 `CONFIG_LV_USE_ARCLABEL`

**提示（Prompt）**：圆弧标签（Arc Label）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1964`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT"></a>

## 18.92 `CONFIG_LV_USE_ASSERT`

**提示（Prompt）**：断言宏 `LV_ASSERT` / `LV_ASSERT_MSG` / `LV_ASSERT_FORMAT_MSG`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3585`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT_MALLOC"></a>

## 18.93 `CONFIG_LV_USE_ASSERT_MALLOC`

**提示（Prompt）**：内存分配断言宏 `LV_ASSERT_MALLOC`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3588`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT_MEM_INTEGRITY"></a>

## 18.94 `CONFIG_LV_USE_ASSERT_MEM_INTEGRITY`

**提示（Prompt）**：内存完整性断言宏 `LV_ASSERT_MEM_INTEGRITY`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3597`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT_NULL"></a>

## 18.95 `CONFIG_LV_USE_ASSERT_NULL`

**提示（Prompt）**：空指针断言宏 `LV_ASSERT_NULL`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3591`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT_OBJ"></a>

## 18.96 `CONFIG_LV_USE_ASSERT_OBJ`

**提示（Prompt）**：对象断言宏 `LV_ASSERT_OBJ`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3600`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ASSERT_STYLE"></a>

## 18.97 `CONFIG_LV_USE_ASSERT_STYLE`

**提示（Prompt）**：样式断言宏 `LV_ASSERT_STYLE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3594`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_BAR"></a>

## 18.98 `CONFIG_LV_USE_BAR`

**提示（Prompt）**：条形指示器（Bar）

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
CONFIG_LV_USE_SLIDER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1968`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_SLIDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_SLIDER)。

<a id="CONFIG_LV_USE_BARCODE"></a>

## 18.99 `CONFIG_LV_USE_BARCODE`

**提示（Prompt）**：条形码（Barcode）

**说明（Help）**

生成 Code 128 条形码（Barcode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_CANVAS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1972`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_CANVAS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CANVAS)。

<a id="CONFIG_LV_USE_BIDI"></a>

## 18.100 `CONFIG_LV_USE_BIDI`

**提示（Prompt）**：双向文本（Bidirectional Text）

**说明（Help）**

允许混合从左到右（Left-to-Right）和从右到左（Right-to-Left）的文本。方向将按照 Unicode 双向算法（Unicode Bidirectional Algorithm）处理，参见 [Unicode 双向算法基础](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1644`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<!-- kconfig-navigation -->

[上一章](P017_module_lvgl_zephyr_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P019_module_lvgl_zephyr_配置项参考_5.md)
