---
id: learning.zephyr-docs.kconfig-reference.page-17
title: "`<module:lvgl>/zephyr`配置项参考（3/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第17章\_`<module:lvgl>/zephyr`配置项参考（3/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_INDEV_DEF_SCROLL_LIMIT"></a>

## 17.1 `CONFIG_LV_INDEV_DEF_SCROLL_LIMIT`

**提示（Prompt）**：滚动阈值（Scroll Threshold，px）

**说明（Help）**

开始滚动（Scrolling）之前，指针需要移动的距离。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1195`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INDEV_DEF_SCROLL_THROW"></a>

## 17.2 `CONFIG_LV_INDEV_DEF_SCROLL_THROW`

**提示（Prompt）**：惯性滚动减速比例（Scroll Throw Slow-down，%）

**说明（Help）**

松开滚动后施加的减速（Slow-down）。数值越大，减速越快。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1202`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_INTTYPES_INCLUDE"></a>

## 17.3 `CONFIG_LV_INTTYPES_INCLUDE`

**提示（Prompt）**：固定宽度整数格式宏（Fixed-width Integer Format Macros）的头文件 `inttypes`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"inttypes.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:151`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_JANUARY_STR"></a>

## 17.4 `CONFIG_LV_JANUARY_STR`

**提示（Prompt）**：一月名称字符串（String for January）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"January"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2023`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_JULY_STR"></a>

## 17.5 `CONFIG_LV_JULY_STR`

**提示（Prompt）**：七月名称字符串（String for July）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"July"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2041`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_JUNE_STR"></a>

## 17.6 `CONFIG_LV_JUNE_STR`

**提示（Prompt）**：六月名称字符串（String for June）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"June"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2038`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LABEL_LONG_TXT_HINT"></a>

## 17.7 `CONFIG_LV_LABEL_LONG_TXT_HINT`

**提示（Prompt）**：长文本绘制提示（Long Text Draw Hint）

**说明（Help）**

为每个标签（Label）额外存储 12 字节，以加快超长文本的绘制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LABEL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2214`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 标签（Label）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LABEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LABEL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LABEL_TEXT_SELECTION"></a>

## 17.8 `CONFIG_LV_LABEL_TEXT_SELECTION`

**提示（Prompt）**：文本选择（Text Selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LABEL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2210`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 标签（Label）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LABEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LABEL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LABEL_WAIT_CHAR_COUNT"></a>

## 17.9 `CONFIG_LV_LABEL_WAIT_CHAR_COUNT`

**提示（Prompt）**：循环滚动间隔（Circular Scroll Gap，字符数）

**说明（Help）**

循环滚动文本的末尾与重新开始处之间的间隔，以空格字符宽度为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LABEL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2220`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 标签（Label）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LABEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LABEL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LGFX_USER_INCLUDE"></a>

## 17.10 `CONFIG_LV_LGFX_USER_INCLUDE`

**提示（Prompt）**：LovyanGFX 用户配置头文件（User Configuration Header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOVYAN_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"lv_lgfx_user.hpp"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2480`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → LovyanGFX 图形库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOVYAN_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOVYAN_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_BSD"></a>

## 17.11 `CONFIG_LV_LIBINPUT_BSD`

**提示（Prompt）**：libinput 的 BSD 变体（BSD Variant）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2562`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB"></a>

## 17.12 `CONFIG_LV_LIBINPUT_XKB`

**提示（Prompt）**：通过 XKB 提供完整键盘支持（Full Keyboard Support）

**说明（Help）**

使用 XKB 布局（Layout）将按键事件映射为字符，使修饰键（Modifier）和非美国布局正常工作。需要使用 `-lxkbcommon` 链接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2566`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_LAYOUT"></a>

## 17.13 `CONFIG_LV_LIBINPUT_XKB_LAYOUT`

**提示（Prompt）**：XKB 布局（Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"us"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2585`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_MODEL"></a>

## 17.14 `CONFIG_LV_LIBINPUT_XKB_MODEL`

**提示（Prompt）**：XKB 型号（Model）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"pc101"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2581`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_OPTIONS"></a>

## 17.15 `CONFIG_LV_LIBINPUT_XKB_OPTIONS`

**提示（Prompt）**：XKB 选项（Options）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_LIBINPUT_XKB_OPTIONS_USE_DEFAULT && CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2600`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB_OPTIONS_USE_DEFAULT`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB_OPTIONS_USE_DEFAULT)、[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_OPTIONS_USE_DEFAULT"></a>

## 17.16 `CONFIG_LV_LIBINPUT_XKB_OPTIONS_USE_DEFAULT`

**提示（Prompt）**：系统默认 XKB 选项（System Default Options）

**说明（Help）**

将 XKB 选项参数传为 `NULL`，以应用系统默认值，例如来自环境变量 `XKB_DEFAULT_OPTIONS` 的值。否则使用 `LV_LIBINPUT_XKB_OPTIONS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2593`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_RULES"></a>

## 17.17 `CONFIG_LV_LIBINPUT_XKB_RULES`

**提示（Prompt）**：XKB 规则（Rules）

**说明（Help）**

运行 `setxkbmap -query`，查找适合所用键盘的值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2575`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIBINPUT_XKB_VARIANT"></a>

## 17.18 `CONFIG_LV_LIBINPUT_XKB_VARIANT`

**提示（Prompt）**：XKB 变体（Variant）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LIBINPUT_XKB && CONFIG_LV_USE_LIBINPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2589`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → libinput 输入库 → 通过 XKB 提供完整键盘支持（Full Keyboard Support）

**配置项引用（Symbol References）**：[`CONFIG_LV_LIBINPUT_XKB`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LIBINPUT_XKB)、[`CONFIG_LV_USE_LIBINPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LIBINPUT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LIMITS_INCLUDE"></a>

## 17.19 `CONFIG_LV_LIMITS_INCLUDE`

**提示（Prompt）**：实现限制（Implementation Limits）的头文件 `limits`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
"limits.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:155`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LINUX_DRM_AUTO_BACKEND"></a>

## 17.20 `CONFIG_LV_LINUX_DRM_AUTO_BACKEND`

**提示（Prompt）**：自动选择 DRM 后端（Backend，旧版行为）

**说明（Help）**

这是计划移除的旧版行为（Legacy Behavior）：根据 `LV_USE_OPENGLES` 推断后端（Backend），启用它时采用 EGL。请禁用此项，并在“渲染后端（Rendering Backend）”选项中显式选择后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LINUX_DRM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2339`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 直接渲染管理器（DRM）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LINUX_DRM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_DRM)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LINUX_DRM_BACKEND_EGL"></a>

## 17.21 `CONFIG_LV_LINUX_DRM_BACKEND_EGL`

**提示（Prompt）**：EGL，使用 OpenGL ES 硬件加速（Hardware-accelerated）

**说明（Help）**

通过 OpenGL ES 2.0 和 EGL 进行硬件加速渲染（Hardware-accelerated Rendering），兼容 LVGL 3D/glTF 渲染。要求目标硬件支持 OpenGL ES 2.0，并通过 `-lEGL` 链接；会弱选择（Imply）GBM 缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LV_LINUX_DRM_USE_EGL
CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS
CONFIG_LV_USE_OPENGLES
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2365`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 直接渲染管理器（DRM） → 渲染后端（Rendering Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_LINUX_DRM_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_LINUX_DRM_USE_EGL)、[`CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS)、[`CONFIG_LV_USE_OPENGLES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OPENGLES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_LINUX_DRM_USE_EGL`、`CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS`。

<a id="CONFIG_LV_LINUX_DRM_BACKEND_FBDEV"></a>

## 17.22 `CONFIG_LV_LINUX_DRM_BACKEND_FBDEV`

**提示（Prompt）**：简单缓冲区（Dumb Buffers，无 GPU）

**说明（Help）**

将软件渲染（Software Rendering）结果写入 DRM/KMS 简单缓冲区（Dumb Buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2354`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 直接渲染管理器（DRM） → 渲染后端（Rendering Backend）

<a id="CONFIG_LV_LINUX_DRM_BACKEND_GBM"></a>

## 17.23 `CONFIG_LV_LINUX_DRM_BACKEND_GBM`

**提示（Prompt）**：通用缓冲区管理（GBM）DMA 缓冲区

**说明（Help）**

为 Linux DRM DMA 缓冲区使用 MESA 通用缓冲区管理（GBM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2359`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 直接渲染管理器（DRM） → 渲染后端（Rendering Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_USE_LINUX_DRM_GBM_BUFFERS`。

<a id="CONFIG_LV_LINUX_FBDEV_BSD"></a>

## 17.24 `CONFIG_LV_LINUX_FBDEV_BSD`

**提示（Prompt）**：BSD 风格的帧缓冲设备（Framebuffer Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LINUX_FBDEV && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2398`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LINUX_FBDEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_FBDEV)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LINUX_FBDEV_BUFFER_SIZE"></a>

## 17.25 `CONFIG_LV_LINUX_FBDEV_BUFFER_SIZE`

**提示（Prompt）**：自定义局部缓冲区大小（Partial Buffer Size，行数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LINUX_FBDEV_CUSTOM_BUFFER && CONFIG_LV_USE_LINUX_FBDEV && CONFIG_LVGL
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2449`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev）

**配置项引用（Symbol References）**：[`CONFIG_LV_LINUX_FBDEV_CUSTOM_BUFFER`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LINUX_FBDEV_CUSTOM_BUFFER)、[`CONFIG_LV_USE_LINUX_FBDEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_FBDEV)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LINUX_FBDEV_CUSTOM_BUFFER"></a>

## 17.26 `CONFIG_LV_LINUX_FBDEV_CUSTOM_BUFFER`

**提示（Prompt）**：自定义大小的缓冲区（Custom-sized Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL && <choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2437`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 帧缓冲大小（Framebuffer Size）

**配置项引用（Symbol References）**：[`CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL)。

<a id="CONFIG_LV_LINUX_FBDEV_DOUBLE_BUFFER"></a>

## 17.27 `CONFIG_LV_LINUX_FBDEV_DOUBLE_BUFFER`

**提示（Prompt）**：两个屏幕大小的缓冲区（Screen-sized Buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL && <choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2433`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 帧缓冲大小（Framebuffer Size）

**配置项引用（Symbol References）**：[`CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL)。

<a id="CONFIG_LV_LINUX_FBDEV_MMAP"></a>

## 17.28 `CONFIG_LV_LINUX_FBDEV_MMAP`

**提示（Prompt）**：帧缓冲设备支持内存映射（mmap）

**说明（Help）**

通过 `mmap()` 访问帧缓冲（Framebuffer），而不调用 `write()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LINUX_FBDEV && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2454`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LINUX_FBDEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_FBDEV)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LINUX_FBDEV_RENDER_MODE_DIRECT"></a>

## 17.29 `CONFIG_LV_LINUX_FBDEV_RENDER_MODE_DIRECT`

**提示（Prompt）**：直接模式（Direct Mode）

**说明（Help）**

将内容渲染到屏幕大小缓冲区中的正确位置，使缓冲区始终保存完整图像，仅刷新变化区域。使用两个缓冲区时，它们的内容会自动保持同步，`flush_cb` 只需更改地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2412`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 渲染模式（Render Mode）

<a id="CONFIG_LV_LINUX_FBDEV_RENDER_MODE_FULL"></a>

## 17.30 `CONFIG_LV_LINUX_FBDEV_RENDER_MODE_FULL`

**提示（Prompt）**：全屏模式（Full Mode）

**说明（Help）**

即使只有一个像素发生变化，也始终重绘整个屏幕。使用两个缓冲区时，`flush_cb` 只需更改地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2418`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 渲染模式（Render Mode）

<a id="CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL"></a>

## 17.31 `CONFIG_LV_LINUX_FBDEV_RENDER_MODE_PARTIAL`

**提示（Prompt）**：局部模式（Partial Mode）

**说明（Help）**

将屏幕拆成较小部分进行渲染，使缓冲区可以小于显示区域，从而节省 RAM。建议缓冲区至少为屏幕大小的十分之一。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2406`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 渲染模式（Render Mode）

<a id="CONFIG_LV_LINUX_FBDEV_SINGLE_BUFFER"></a>

## 17.32 `CONFIG_LV_LINUX_FBDEV_SINGLE_BUFFER`

**提示（Prompt）**：一个屏幕大小的缓冲区（Screen-sized Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2430`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev） → 帧缓冲大小（Framebuffer Size）

<a id="CONFIG_LV_LINUX_FBDEV_VSYNC"></a>

## 17.33 `CONFIG_LV_LINUX_FBDEV_VSYNC`

**提示（Prompt）**：将刷新与垂直同步（Vsync）同步

**说明（Help）**

写入帧缓冲（Framebuffer）前等待垂直同步（Vsync），以减少画面撕裂（Tearing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LINUX_FBDEV && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2460`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Linux 帧缓冲（Framebuffer，fbdev）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LINUX_FBDEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LINUX_FBDEV)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_LEVEL_ERROR"></a>

## 17.34 `CONFIG_LV_LOG_LEVEL_ERROR`

**提示（Prompt）**：错误（Error）：可能使系统失效的严重问题

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1403`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_LEVEL_INFO"></a>

## 17.35 `CONFIG_LV_LOG_LEVEL_INFO`

**提示（Prompt）**：信息（Info）：重要事件

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1399`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_LEVEL_NONE"></a>

## 17.36 `CONFIG_LV_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）：不记录任何日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1407`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_LEVEL_TRACE"></a>

## 17.37 `CONFIG_LV_LOG_LEVEL_TRACE`

**提示（Prompt）**：跟踪（Trace）：所有方面的详细信息

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1397`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_LEVEL_USER"></a>

## 17.38 `CONFIG_LV_LOG_LEVEL_USER`

**提示（Prompt）**：用户（User）：仅记录用户添加的日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1405`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_LEVEL_WARN"></a>

## 17.39 `CONFIG_LV_LOG_LEVEL_WARN`

**提示（Prompt）**：警告（Warn）：发生了不期望的情况，但尚未造成问题

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1401`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 默认日志详细程度（Default Log Verbosity）

<a id="CONFIG_LV_LOG_PRINTF"></a>

## 17.40 `CONFIG_LV_LOG_PRINTF`

**提示（Prompt）**：使用 `printf` 打印日志（Log）

**说明（Help）**

如果未设置，用户需要通过 `lv_log_register_print_cb()` 注册回调（Callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1424`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_ANIM"></a>

## 17.41 `CONFIG_LV_LOG_TRACE_ANIM`

**提示（Prompt）**：动画（Animations）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1468`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_CACHE"></a>

## 17.42 `CONFIG_LV_LOG_TRACE_CACHE`

**提示（Prompt）**：缓存（Cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1472`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_DISP_REFR"></a>

## 17.43 `CONFIG_LV_LOG_TRACE_DISP_REFR`

**提示（Prompt）**：显示刷新（Display Refresh）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1452`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_EVENT"></a>

## 17.44 `CONFIG_LV_LOG_TRACE_EVENT`

**提示（Prompt）**：事件（Events）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1456`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_INDEV"></a>

## 17.45 `CONFIG_LV_LOG_TRACE_INDEV`

**提示（Prompt）**：输入设备（Input Devices）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1448`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_LAYOUT"></a>

## 17.46 `CONFIG_LV_LOG_TRACE_LAYOUT`

**提示（Prompt）**：布局（Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1464`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_MEM"></a>

## 17.47 `CONFIG_LV_LOG_TRACE_MEM`

**提示（Prompt）**：内存（Memory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1440`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_OBJ_CREATE"></a>

## 17.48 `CONFIG_LV_LOG_TRACE_OBJ_CREATE`

**提示（Prompt）**：控件创建（Widget Creation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1460`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_TRACE_TIMER"></a>

## 17.49 `CONFIG_LV_LOG_TRACE_TIMER`

**提示（Prompt）**：定时器（Timer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1444`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。 → 各模块的跟踪日志（Trace Logs per Module）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_USE_FILE_LINE"></a>

## 17.50 `CONFIG_LV_LOG_USE_FILE_LINE`

**提示（Prompt）**：在每条日志中加入文件名和行号（File Name and Line Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1434`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_LOG_USE_TIMESTAMP"></a>

## 17.51 `CONFIG_LV_LOG_USE_TIMESTAMP`

**提示（Prompt）**：在每条日志中加入时间戳（Timestamp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1430`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MARCH_STR"></a>

## 17.52 `CONFIG_LV_MARCH_STR`

**提示（Prompt）**：三月名称字符串（String for March）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"March"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2029`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MAY_STR"></a>

## 17.53 `CONFIG_LV_MAY_STR`

**提示（Prompt）**：五月名称字符串（String for May）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"May"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2035`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MEM_ADR"></a>

## 17.54 `CONFIG_LV_MEM_ADR`

**提示（Prompt）**：内存池地址（Memory Pool Address）

**说明（Help）**

将内存池（Memory Pool）放在固定地址，而不是按普通数组分配。`0` 表示不使用。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BUILTIN_MALLOC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:128`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内置内存分配设置（Builtin Malloc Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BUILTIN_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_BUILTIN_MALLOC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_LEFT"></a>

## 17.55 `CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_LEFT`

**提示（Prompt）**：左下（Bottom Left）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3272`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_MID"></a>

## 17.56 `CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_MID`

**提示（Prompt）**：下方居中（Bottom Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3274`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_RIGHT"></a>

## 17.57 `CONFIG_LV_MEM_MONITOR_ALIGN_BOTTOM_RIGHT`

**提示（Prompt）**：右下（Bottom Right）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3276`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_CENTER"></a>

## 17.58 `CONFIG_LV_MEM_MONITOR_ALIGN_CENTER`

**提示（Prompt）**：中央（Center）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3282`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_LEFT_MID"></a>

## 17.59 `CONFIG_LV_MEM_MONITOR_ALIGN_LEFT_MID`

**提示（Prompt）**：左侧居中（Left Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3278`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_RIGHT_MID"></a>

## 17.60 `CONFIG_LV_MEM_MONITOR_ALIGN_RIGHT_MID`

**提示（Prompt）**：右侧居中（Right Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3280`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_TOP_LEFT"></a>

## 17.61 `CONFIG_LV_MEM_MONITOR_ALIGN_TOP_LEFT`

**提示（Prompt）**：左上（Top Left）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3266`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_TOP_MID"></a>

## 17.62 `CONFIG_LV_MEM_MONITOR_ALIGN_TOP_MID`

**提示（Prompt）**：上方居中（Top Middle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3268`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_MONITOR_ALIGN_TOP_RIGHT"></a>

## 17.63 `CONFIG_LV_MEM_MONITOR_ALIGN_TOP_RIGHT`

**提示（Prompt）**：右上（Top Right）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3270`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 内存监测器（Memory Monitor） → 内存监测器位置（Memory Monitor Position）

<a id="CONFIG_LV_MEM_POOL_EXPAND_SIZE_KILOBYTES"></a>

## 17.64 `CONFIG_LV_MEM_POOL_EXPAND_SIZE_KILOBYTES`

**提示（Prompt）**：内存池扩展大小（Memory Pool Expand Size，KB）［已弃用：直接使用 `LV_MEM_SIZE`］

**说明（Help）**

已弃用（Deprecated）。请直接修改以字节为单位的 `LV_MEM_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BUILTIN_MALLOC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:122`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内置内存分配设置（Builtin Malloc Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BUILTIN_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_BUILTIN_MALLOC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MEM_SIZE"></a>

## 17.65 `CONFIG_LV_MEM_SIZE`

**提示（Prompt）**：内存大小（Memory Size，字节）

**说明（Help）**

供 `lv_malloc()` 分配的内存池（Memory Pool）大小，至少需要 2 kB，即 2048 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BUILTIN_MALLOC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:110`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内置内存分配设置（Builtin Malloc Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BUILTIN_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_BUILTIN_MALLOC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MEM_SIZE_KILOBYTES"></a>

## 17.66 `CONFIG_LV_MEM_SIZE_KILOBYTES`

**提示（Prompt）**：内存大小（Memory Size，KB）［已弃用：使用 `LV_MEM_SIZE`］

**说明（Help）**

已弃用（Deprecated）。请改用以字节为单位的 `LV_MEM_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BUILTIN_MALLOC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:116`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内置内存分配设置（Builtin Malloc Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BUILTIN_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_BUILTIN_MALLOC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_MONDAY_STR"></a>

## 17.67 `CONFIG_LV_MONDAY_STR`

**提示（Prompt）**：星期一的缩写字符串（Shortened String for Monday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"Mo"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1997`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NANOVG_BACKEND"></a>

## 17.68 `CONFIG_LV_NANOVG_BACKEND`

**提示（Prompt）**：NanoVG OpenGL 后端（Backend）

**说明（Help）**

要编译的 NanoVG 着色器变体（Shader Flavor），必须与显示驱动创建的 OpenGL 上下文（Context）匹配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_NANOVG_BACKEND_GLES2
```

**可选项（Choices）**

```text
CONFIG_LV_NANOVG_BACKEND_GL2
CONFIG_LV_NANOVG_BACKEND_GL3
CONFIG_LV_NANOVG_BACKEND_GLES2
CONFIG_LV_NANOVG_BACKEND_GLES3
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1122`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_NANOVG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_NANOVG_BACKEND_GLES2`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND_GLES2)、[`CONFIG_LV_NANOVG_BACKEND_GL2`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND_GL2)、[`CONFIG_LV_NANOVG_BACKEND_GL3`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND_GL3)、[`CONFIG_LV_NANOVG_BACKEND_GLES3`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND_GLES3)。

<a id="CONFIG_LV_NANOVG_BACKEND_GL2"></a>

## 17.69 `CONFIG_LV_NANOVG_BACKEND_GL2`

**提示（Prompt）**：OpenGL 2.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_NANOVG_BACKEND>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1129`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer） → NanoVG OpenGL 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_NANOVG_BACKEND`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND)。

<a id="CONFIG_LV_NANOVG_BACKEND_GL3"></a>

## 17.70 `CONFIG_LV_NANOVG_BACKEND_GL3`

**提示（Prompt）**：OpenGL 3.0 及以上（3.0+）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_NANOVG_BACKEND>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1131`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer） → NanoVG OpenGL 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_NANOVG_BACKEND`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND)。

<a id="CONFIG_LV_NANOVG_BACKEND_GLES2"></a>

## 17.71 `CONFIG_LV_NANOVG_BACKEND_GLES2`

**提示（Prompt）**：OpenGL ES 2.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_NANOVG_BACKEND>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1133`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer） → NanoVG OpenGL 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_NANOVG_BACKEND`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND)。

<a id="CONFIG_LV_NANOVG_BACKEND_GLES3"></a>

## 17.72 `CONFIG_LV_NANOVG_BACKEND_GLES3`

**提示（Prompt）**：OpenGL ES 3.0 及以上（3.0+）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_NANOVG_BACKEND>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1135`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer） → NanoVG OpenGL 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_LV_NANOVG_BACKEND`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NANOVG_BACKEND)。

<a id="CONFIG_LV_NANOVG_IMAGE_CACHE_CNT"></a>

## 17.73 `CONFIG_LV_NANOVG_IMAGE_CACHE_CNT`

**提示（Prompt）**：图像纹理缓存大小（Image Texture Cache Size，条目数）

**说明（Help）**

以 GPU 纹理（Texture）形式保留的已解码图像数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1146`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_NANOVG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NANOVG_LETTER_CACHE_CNT"></a>

## 17.74 `CONFIG_LV_NANOVG_LETTER_CACHE_CNT`

**提示（Prompt）**：字符缓存大小（Letter Cache Size，条目数）

**说明（Help）**

为文本绘制保留的已渲染字形（Glyph）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1152`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库 → NanoVG 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_NANOVG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_CACHE_HAL_INCLUDE"></a>

## 17.75 `CONFIG_LV_NEMA_CACHE_HAL_INCLUDE`

**提示（Prompt）**：缓存 HAL 头文件（Cache HAL Header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_NEMA_USE_CACHE && CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stm32u5xx_hal.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:796`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → 缓存维护（Cache Maintenance）

**配置项引用（Symbol References）**：[`CONFIG_LV_NEMA_USE_CACHE`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_USE_CACHE)、[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_CUSTOM_INCLUDE"></a>

## 17.76 `CONFIG_LV_NEMA_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义 NemaGFX 属性头文件路径（Attribute Header Path）

**说明（Help）**

可选头文件，用于覆盖 NemaGFX/STM32 HAL 专用宏。

`LV_NEMA_STM32_HAL_ATTRIBUTE_POOL_MEM` 是应用于 STM32 目标上 NemaGFX 内存池（Memory Pool）的属性，用于将内存池放入 NemaGFX DMA 可以访问的特定 RAM 区域。示例：`__attribute__((section(".nema_pool")))`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_NEMA_USE_CUSTOM_INCLUDE && CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:860`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → 自定义属性头文件（Custom Attribute Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_NEMA_USE_CUSTOM_INCLUDE`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_USE_CUSTOM_INCLUDE)、[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_GFX_MAX_RESX"></a>

## 17.77 `CONFIG_LV_NEMA_GFX_MAX_RESX`

**提示（Prompt）**：NemaVG 最大水平分辨率（Max Horizontal Resolution，px）

**说明（Help）**

初始化 NemaVG 时采用的画布宽度（Canvas Width）。它与垂直分辨率一起决定 STM32 上 NemaGFX 内存池的大小，即 `RESX * RESY + 10KB`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:880`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_GFX_MAX_RESY"></a>

## 17.78 `CONFIG_LV_NEMA_GFX_MAX_RESY`

**提示（Prompt）**：NemaVG 最大垂直分辨率（Max Vertical Resolution，px）

**说明（Help）**

初始化 NemaVG 时采用的画布高度（Canvas Height）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
600
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:887`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_HAL_CUSTOM"></a>

## 17.79 `CONFIG_LV_NEMA_HAL_CUSTOM`

**提示（Prompt）**：自定义（Custom）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_HAL>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:835`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_HAL)。

<a id="CONFIG_LV_NEMA_HAL_STM32"></a>

## 17.80 `CONFIG_LV_NEMA_HAL_STM32`

**提示（Prompt）**：STM32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_HAL>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:837`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_HAL)。

<a id="CONFIG_LV_NEMA_LIB_M33_NEMAPVG"></a>

## 17.81 `CONFIG_LV_NEMA_LIB_M33_NEMAPVG`

**提示（Prompt）**：Cortex-M33（NemaPVG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_LIB>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:812`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 静态库（Static Library）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_LIB)。

<a id="CONFIG_LV_NEMA_LIB_M33_REVC"></a>

## 17.82 `CONFIG_LV_NEMA_LIB_M33_REVC`

**提示（Prompt）**：Cortex-M33（修订版 C，Rev C）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_LIB>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:810`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 静态库（Static Library）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_LIB)。

<a id="CONFIG_LV_NEMA_LIB_M55"></a>

## 17.83 `CONFIG_LV_NEMA_LIB_M55`

**提示（Prompt）**：Cortex-M55

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_LIB>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:814`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 静态库（Static Library）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_LIB)。

<a id="CONFIG_LV_NEMA_LIB_M7"></a>

## 17.84 `CONFIG_LV_NEMA_LIB_M7`

**提示（Prompt）**：Cortex-M7

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_LIB>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:816`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 静态库（Static Library）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_LIB)。

<a id="CONFIG_LV_NEMA_LIB_NONE"></a>

## 17.85 `CONFIG_LV_NEMA_LIB_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_NEMA_LIB>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:808`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer） → NemaGFX 静态库（Static Library）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_LIB)。

<a id="CONFIG_LV_NEMA_STM32_HAL_INCLUDE"></a>

## 17.86 `CONFIG_LV_NEMA_STM32_HAL_INCLUDE`

**提示（Prompt）**：STM32 HAL 头文件（Header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_NEMA_HAL_STM32 && CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stm32u5xx_hal.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:846`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_NEMA_HAL_STM32`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_HAL_STM32)、[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_USE_CACHE"></a>

## 17.87 `CONFIG_LV_NEMA_USE_CACHE`

**提示（Prompt）**：缓存维护（Cache Maintenance）

**说明（Help）**

围绕绘制缓冲区（Draw Buffer）执行 CPU 缓存清理（Clean）与失效（Invalidate），使 GPU 能看到一致的数据。具有数据缓存（Data Cache）的内核需要此操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:789`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NEMA_USE_CUSTOM_INCLUDE"></a>

## 17.88 `CONFIG_LV_NEMA_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义属性头文件（Custom Attribute Header）

**说明（Help）**

包含 `LV_NEMA_CUSTOM_INCLUDE` 指定的头文件，以覆盖 `LV_NEMA_STM32_HAL_ATTRIBUTE_POOL_MEM` 等 NemaGFX/STM32 HAL 专用宏。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_NEMA_HAL_STM32 && CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:851`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_NEMA_HAL_STM32`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_HAL_STM32)、[`CONFIG_LV_USE_NEMA_GFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NOVEMBER_STR"></a>

## 17.89 `CONFIG_LV_NOVEMBER_STR`

**提示（Prompt）**：十一月名称字符串（String for November）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"November"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2053`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NUTTX_DEFAULT_DRAW_BUF_USE_INDEPENDENT_IMAGE_HEAP"></a>

## 17.90 `CONFIG_LV_NUTTX_DEFAULT_DRAW_BUF_USE_INDEPENDENT_IMAGE_HEAP`

**提示（Prompt）**：为默认绘制缓冲区（Default Draw Buffer）使用独立图像堆（Independent Image Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX_INDEPENDENT_IMAGE_HEAP && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2622`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 独立图像堆（Independent Image Heap）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX_INDEPENDENT_IMAGE_HEAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX_INDEPENDENT_IMAGE_HEAP)、[`CONFIG_LV_USE_NUTTX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NUTTX_LCD_BUFFER_SIZE"></a>

## 17.91 `CONFIG_LV_NUTTX_LCD_BUFFER_SIZE`

**提示（Prompt）**：自定义局部缓冲区大小（Partial Buffer Size，行数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_NUTTX_LCD_CUSTOM_BUFFER && CONFIG_LV_USE_NUTTX_LCD && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2667`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_NUTTX_LCD_CUSTOM_BUFFER`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NUTTX_LCD_CUSTOM_BUFFER)、[`CONFIG_LV_USE_NUTTX_LCD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX_LCD)、[`CONFIG_LV_USE_NUTTX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NUTTX_LCD_CUSTOM_BUFFER"></a>

## 17.92 `CONFIG_LV_NUTTX_LCD_CUSTOM_BUFFER`

**提示（Prompt）**：自定义大小的缓冲区（Custom-sized Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2656`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 液晶显示设备（LCD Device） → 液晶显示缓冲区大小（LCD Buffer Size）

<a id="CONFIG_LV_NUTTX_LCD_DOUBLE_BUFFER"></a>

## 17.93 `CONFIG_LV_NUTTX_LCD_DOUBLE_BUFFER`

**提示（Prompt）**：两个屏幕大小的缓冲区（Screen-sized Buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2653`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 液晶显示设备（LCD Device） → 液晶显示缓冲区大小（LCD Buffer Size）

<a id="CONFIG_LV_NUTTX_LCD_SINGLE_BUFFER"></a>

## 17.94 `CONFIG_LV_NUTTX_LCD_SINGLE_BUFFER`

**提示（Prompt）**：一个屏幕大小的缓冲区（Screen-sized Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2650`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 液晶显示设备（LCD Device） → 液晶显示缓冲区大小（LCD Buffer Size）

<a id="CONFIG_LV_NUTTX_TOUCHSCREEN_CURSOR_SIZE"></a>

## 17.95 `CONFIG_LV_NUTTX_TOUCHSCREEN_CURSOR_SIZE`

**提示（Prompt）**：触摸屏光标大小（Touchscreen Cursor Size，px）

**说明（Help）**

`0` 禁用光标（Cursor）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX_TOUCHSCREEN && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2678`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 触摸屏（Touchscreen）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX_TOUCHSCREEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX_TOUCHSCREEN)、[`CONFIG_LV_USE_NUTTX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_NUTTX_TRACE_FILE_PATH"></a>

## 17.96 `CONFIG_LV_NUTTX_TRACE_FILE_PATH`

**提示（Prompt）**：性能分析跟踪文件路径（Profiler Trace File Path）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX_TRACE_FILE && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"/data/lvgl-trace.log"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2702`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 性能分析跟踪文件（Profiler Trace File）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX_TRACE_FILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX_TRACE_FILE)、[`CONFIG_LV_USE_NUTTX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OBJ_ID_AUTO_ASSIGN"></a>

## 17.97 `CONFIG_LV_OBJ_ID_AUTO_ASSIGN`

**提示（Prompt）**：创建控件时自动分配 ID（Automatic ID Assignment）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_OBJ_ID && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1323`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core） → 控件 ID（Widget ID，`lv_obj_set_id`）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OBJ_ID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OBJ_ID)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OBJ_STYLE_CACHE"></a>

## 17.98 `CONFIG_LV_OBJ_STYLE_CACHE`

**提示（Prompt）**：样式缓存（Style Cache）

**说明（Help）**

为每个 `lv_obj_t` 增加两个 32 位变量，以加快样式属性查找（Style Property Lookup）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1307`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OCTOBER_STR"></a>

## 17.99 `CONFIG_LV_OCTOBER_STR`

**提示（Prompt）**：十月名称字符串（String for October）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"October"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2050`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_OS_CMSIS_RTOS2"></a>

## 17.100 `CONFIG_LV_OS_CMSIS_RTOS2`

**提示（Prompt）**：CMSIS-RTOS2 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_OS>
```

**主动选择（Selects）**

```text
CONFIG_LV_OS_USE_CMSIS_RTOS2
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:180`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → 操作系统（Operating System）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_OS)、[`CONFIG_LV_OS_USE_CMSIS_RTOS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_USE_CMSIS_RTOS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_OS_USE_CMSIS_RTOS2`。

<!-- kconfig-navigation -->

[上一章](P016_module_lvgl_zephyr_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P018_module_lvgl_zephyr_配置项参考_4.md)
