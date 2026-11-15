---
id: learning.zephyr-docs.kconfig-reference.page-346
title: "`subsys/input`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第346章\_`subsys/input`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/input` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_INPUT"></a>

## 346.1 `CONFIG_INPUT`

**提示（Prompt）**：`input`（输入）。

**说明（Help）**

将输入子系统（input subsystem）及其驱动纳入系统配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/arduino_giga_display_shield/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/arduino_giga_display_shield/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/g1120b0mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/lcd_par_s035/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/m5stack_cardputer/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/m5stack_cardputer/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/seeed_xiao_round_display/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_round_display/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`subsys/input/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<a id="CONFIG_INPUT_DOUBLE_TAP"></a>

## 346.2 `CONFIG_INPUT_DOUBLE_TAP`

**提示（Prompt）**：输入双击（Input double tap）

**说明（Help）**

启用输入双击驱动（input double tap driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_INPUT_DOUBLE_TAP_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/input/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_EVENT_DUMP"></a>

## 346.3 `CONFIG_INPUT_EVENT_DUMP`

**提示（Prompt）**：记录所有输入事件（input events）

**说明（Help）**

以 info 级别日志输出所有输入事件（input events）。使用 `INPUT_SHELL` 时，还必须通过 `input dump on` 启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_INPUT
```

**定义位置（Location）**：[`subsys/input/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_INIT_PRIORITY"></a>

## 346.4 `CONFIG_INPUT_INIT_PRIORITY`

**提示（Prompt）**：输入子系统及驱动的初始化优先级（init priority）

**说明（Help）**

输入子系统（input subsystem）及驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT
```

**默认值（Defaults）**

```text
90
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtkmipilcdb00000be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/Kconfig.defconfig)。

```text
89
```

**定义位置（Location）**：[`subsys/input/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KEYMAP"></a>

## 346.5 `CONFIG_INPUT_KEYMAP`

**提示（Prompt）**：输入键映射（Input keymap）

**说明（Help）**

启用输入键映射驱动（input keymap driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INPUT_KEYMAP_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/input/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_LONGPRESS"></a>

## 346.6 `CONFIG_INPUT_LONGPRESS`

**提示（Prompt）**：输入长按（Input longpress）

**说明（Help）**

启用输入长按驱动（input longpress driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_INPUT_LONGPRESS_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/input/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_MODE"></a>

## 346.7 `CONFIG_INPUT_MODE`

**提示（Prompt）**：输入事件处理模式（Input event processing mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT
```

**默认值（Defaults）**

```text
CONFIG_INPUT_MODE_THREAD
```

**可选项（Choices）**

```text
CONFIG_INPUT_MODE_SYNCHRONOUS
CONFIG_INPUT_MODE_THREAD
```

**定义位置（Location）**：[`subsys/input/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)、[`CONFIG_INPUT_MODE_THREAD`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_THREAD)、[`CONFIG_INPUT_MODE_SYNCHRONOUS`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_SYNCHRONOUS)。

<a id="CONFIG_INPUT_MODE_SYNCHRONOUS"></a>

## 346.8 `CONFIG_INPUT_MODE_SYNCHRONOUS`

**提示（Prompt）**：同步处理输入事件（synchronously）

**说明（Help）**

在报告事件的代码上下文（context）中同步执行输入事件回调（callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_MODE>
```

**定义位置（Location）**：[`subsys/input/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入事件处理模式（Input event processing mode）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_MODE`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE)。

<a id="CONFIG_INPUT_MODE_THREAD"></a>

## 346.9 `CONFIG_INPUT_MODE_THREAD`

**提示（Prompt）**：在专用线程中处理输入事件

**说明（Help）**

将输入事件加入消息队列（message queue），并在专用线程中异步处理回调（callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && <choice CONFIG_INPUT_MODE>
```

**定义位置（Location）**：[`subsys/input/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入事件处理模式（Input event processing mode）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_INPUT_MODE`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE)。

<a id="CONFIG_INPUT_QUEUE_MAX_MSGS"></a>

## 346.10 `CONFIG_INPUT_QUEUE_MAX_MSGS`

**提示（Prompt）**：输入队列消息数量上限（max messages）

**说明（Help）**

输入事件队列（input event queue）中的消息数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_MODE_THREAD && CONFIG_INPUT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/input/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT_MODE_THREAD`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_THREAD)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SHELL"></a>

## 346.11 `CONFIG_INPUT_SHELL`

**提示（Prompt）**：输入命令行（Input shell）

**说明（Help）**

启用输入命令行（input shell），通过命令行接口与输入子系统交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_INPUT
```

**定义位置（Location）**：[`subsys/input/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_THREAD_PRIORITY"></a>

## 346.12 `CONFIG_INPUT_THREAD_PRIORITY`

**提示（Prompt）**：输入线程优先级（Input thread priority）

**说明（Help）**

设置输入线程的优先级（thread priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE && CONFIG_INPUT_MODE_THREAD && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/input/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 覆盖默认输入线程优先级

**配置项引用（Symbol References）**：[`CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE)、[`CONFIG_INPUT_MODE_THREAD`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_THREAD)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE"></a>

## 346.13 `CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE`

**提示（Prompt）**：覆盖默认输入线程优先级

**说明（Help）**

允许更改输入线程默认优先级（priority）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_MODE_THREAD && CONFIG_INPUT
```

**定义位置（Location）**：[`subsys/input/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT_MODE_THREAD`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_THREAD)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)。

<a id="CONFIG_INPUT_THREAD_STACK_SIZE"></a>

## 346.14 `CONFIG_INPUT_THREAD_STACK_SIZE`

**提示（Prompt）**：输入线程栈大小（stack size）

**说明（Help）**

处理输入事件的线程栈大小，必须有足够空间执行已注册的回调（callbacks）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_MODE_THREAD && CONFIG_INPUT
```

**默认值（Defaults）**

```text
2048 if CONFIG_64BIT
1024
```

**定义位置（Location）**：[`subsys/input/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT_MODE_THREAD`](P346_subsys_input_配置项参考.md#CONFIG_INPUT_MODE_THREAD)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<!-- kconfig-navigation -->

[上一章](P345_subsys_gnss_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P347_subsys_instrumentation_配置项参考.md)
