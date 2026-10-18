---
id: learning.zephyr-docs.kconfig-reference.page-19
title: "`<module:lvgl>/zephyr`配置项参考（5/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第19章\_`<module:lvgl>/zephyr`配置项参考（5/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_USE_BMP"></a>

## 19.1 `CONFIG_LV_USE_BMP`

**提示（Prompt）**：BMP 解码器（Decoder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1571`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_BUILTIN_MALLOC"></a>

## 19.2 `CONFIG_LV_USE_BUILTIN_MALLOC`

**提示（Prompt）**：LVGL 内置实现（Built-in）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_TLSF
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:30`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内存分配函数来源（Malloc Functions Source）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TLSF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_TLSF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_USE_TLSF`。

<a id="CONFIG_LV_USE_BUILTIN_SPRINTF"></a>

## 19.3 `CONFIG_LV_USE_BUILTIN_SPRINTF`

**提示（Prompt）**：LVGL 内置实现（Built-in）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:85`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 格式化输出函数来源（Sprintf Functions Source）

<a id="CONFIG_LV_USE_BUILTIN_STRING"></a>

## 19.4 `CONFIG_LV_USE_BUILTIN_STRING`

**提示（Prompt）**：LVGL 内置实现（Built-in）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:60`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 字符串函数来源（String Functions Source）

<a id="CONFIG_LV_USE_BUTTON"></a>

## 19.5 `CONFIG_LV_USE_BUTTON`

**提示（Prompt）**：按钮（Button）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1978`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_BUTTONMATRIX"></a>

## 19.6 `CONFIG_LV_USE_BUTTONMATRIX`

**提示（Prompt）**：按钮矩阵（Button Matrix）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1982`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CALENDAR"></a>

## 19.7 `CONFIG_LV_USE_CALENDAR`

**提示（Prompt）**：日历（Calendar）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1986`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CALENDAR_CHINESE"></a>

## 19.8 `CONFIG_LV_USE_CALENDAR_CHINESE`

**提示（Prompt）**：中国农历（Chinese Calendar）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2069`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CALENDAR_HEADER_ARROW"></a>

## 19.9 `CONFIG_LV_USE_CALENDAR_HEADER_ARROW`

**提示（Prompt）**：带箭头按钮的页头（Header with Arrow Buttons）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2061`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CALENDAR_HEADER_DROPDOWN"></a>

## 19.10 `CONFIG_LV_USE_CALENDAR_HEADER_DROPDOWN`

**提示（Prompt）**：带下拉列表的页头（Header with Dropdowns）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2065`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CANVAS"></a>

## 19.11 `CONFIG_LV_USE_CANVAS`

**提示（Prompt）**：画布（Canvas）

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

**主动选择（Selects）**

```text
CONFIG_LV_USE_IMAGE
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_BARCODE
CONFIG_LV_USE_QRCODE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2077`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_IMAGE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_IMAGE)、[`CONFIG_LV_USE_BARCODE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_USE_BARCODE)、[`CONFIG_LV_USE_QRCODE`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_QRCODE)。

<a id="CONFIG_LV_USE_CHART"></a>

## 19.12 `CONFIG_LV_USE_CHART`

**提示（Prompt）**：图表（Chart）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2082`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CHECKBOX"></a>

## 19.13 `CONFIG_LV_USE_CHECKBOX`

**提示（Prompt）**：复选框（Checkbox）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2086`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CHECK_ARG"></a>

## 19.14 `CONFIG_LV_USE_CHECK_ARG`

**提示（Prompt）**：运行时参数验证（Runtime Argument Validation）

**说明（Help）**

`LV_CHECK_ARG` 在运行时验证函数参数（Function Arguments）：检查失败时记录警告，并执行指定动作。禁用后，所有这些检查都会被编译为空；只有在资源极其受限且能保证不变量（Invariant）成立的环境中，这样做才安全。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3653`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CHECK_OBJ_CLASSTYPE"></a>

## 19.15 `CONFIG_LV_USE_CHECK_OBJ_CLASSTYPE`

**提示（Prompt）**：`LV_CHECK_OBJ` 中的类型检查（Class Check）

**说明（Help）**

`LV_CHECK_OBJ` 通过 `lv_obj_has_class()` 验证对象是否具有预期的类（Class）。禁用后，将跳过类检查，`LV_CHECK_OBJ` 简化为 `NULL` 检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CHECK_ARG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3699`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CHECK_ARG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CHECK_ARG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CHECK_OBJ_PARENT_LINK"></a>

## 19.16 `CONFIG_LV_USE_CHECK_OBJ_PARENT_LINK`

**提示（Prompt）**：`lv_obj_is_in_widget_tree` 中的父子链接一致性检查（Parent-link Consistency Check）

**说明（Help）**

沿父级链向上遍历时，`lv_obj_is_in_widget_tree` 还会检查每个父对象的子对象数组是否包含对应子对象。这可以发现子对象的父指针与父对象的子对象列表不一致的数据损坏（Corruption）。代价是每一层的复杂度从 `O(1)` 变为 `O(siblings)`，发现不匹配时由 `LV_ASSERT` 报告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CHECK_OBJ_VALIDITY && CONFIG_LV_USE_ASSERT && CONFIG_LV_USE_CHECK_ARG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3715`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation） → `LV_CHECK_OBJ` 中的控件树有效性检查（Widget-tree Validity Check）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CHECK_OBJ_VALIDITY`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CHECK_OBJ_VALIDITY)、[`CONFIG_LV_USE_ASSERT`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_USE_ASSERT)、[`CONFIG_LV_USE_CHECK_ARG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CHECK_ARG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CHECK_OBJ_VALIDITY"></a>

## 19.17 `CONFIG_LV_USE_CHECK_OBJ_VALIDITY`

**提示（Prompt）**：`LV_CHECK_OBJ` 中的控件树有效性检查（Widget-tree Validity Check）

**说明（Help）**

`LV_CHECK_OBJ` 通过 `lv_obj_is_in_widget_tree()` 验证对象是否仍属于控件树（Widget Tree）。禁用后，将跳过有效性检查，仅保留类／`NULL` 检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CHECK_ARG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3707`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CHECK_ARG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CHECK_ARG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CLIB_MALLOC"></a>

## 19.18 `CONFIG_LV_USE_CLIB_MALLOC`

**提示（Prompt）**：C 标准库（C Standard Library）：`malloc/realloc/free`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内存分配函数来源（Malloc Functions Source）

<a id="CONFIG_LV_USE_CLIB_SPRINTF"></a>

## 19.19 `CONFIG_LV_USE_CLIB_SPRINTF`

**提示（Prompt）**：C 标准库（C Standard Library）：`vsnprintf`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:88`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 格式化输出函数来源（Sprintf Functions Source）

<a id="CONFIG_LV_USE_CLIB_STRING"></a>

## 19.20 `CONFIG_LV_USE_CLIB_STRING`

**提示（Prompt）**：C 标准库（C Standard Library）：`memcpy/memset/strlen/strcpy`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:63`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 字符串函数来源（String Functions Source）

<a id="CONFIG_LV_USE_COLOR_FILTER"></a>

## 19.21 `CONFIG_LV_USE_COLOR_FILTER`

**提示（Prompt）**：颜色过滤器样式（Color Filter Style）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1382`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CUSTOM_FONT_DEFAULT"></a>

## 19.22 `CONFIG_LV_USE_CUSTOM_FONT_DEFAULT`

**提示（Prompt）**：自定义默认字体（Custom Default Font）

**说明（Help）**

启用后，将 `LV_FONT_DEFAULT` 设为自己定义的字体，而不是下方某个内置字体（Built-in Font）。此时内置默认字体选择项将被隐藏，因此必须自行定义 `LV_FONT_DEFAULT`，可采用以下任一种方式：

- 从构建系统（Build System）传入，例如 `-DLV_FONT_DEFAULT='&my_font_24'`。
- 在 `LV_FONT_CUSTOM_INCLUDE` 指定的头文件中定义，例如：

```c
#define LV_FONT_CUSTOM_DECLARE  LV_FONT_DECLARE(my_font_24)
#define LV_FONT_DEFAULT         &my_font_24
```

如果未定义，`LV_FONT_DEFAULT` 会回退到一个内置字体，而该字体此时已不再被编译进来，从而导致链接错误（Link Error）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1754`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_CUSTOM_MALLOC"></a>

## 19.23 `CONFIG_LV_USE_CUSTOM_MALLOC`

**提示（Prompt）**：自定义（Custom，由外部实现）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:43`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内存分配函数来源（Malloc Functions Source）

<a id="CONFIG_LV_USE_CUSTOM_SPRINTF"></a>

## 19.24 `CONFIG_LV_USE_CUSTOM_SPRINTF`

**提示（Prompt）**：自定义（Custom，由外部实现）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:94`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 格式化输出函数来源（Sprintf Functions Source）

<a id="CONFIG_LV_USE_CUSTOM_STRING"></a>

## 19.25 `CONFIG_LV_USE_CUSTOM_STRING`

**提示（Prompt）**：自定义（Custom，由外部实现）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:69`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 字符串函数来源（String Functions Source）

<a id="CONFIG_LV_USE_DEMO_BENCHMARK"></a>

## 19.26 `CONFIG_LV_USE_DEMO_BENCHMARK`

**提示（Prompt）**：基准测试演示（Benchmark Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
CONFIG_LV_FONT_MONTSERRAT_20
CONFIG_LV_FONT_MONTSERRAT_24
CONFIG_LV_FONT_MONTSERRAT_26
CONFIG_LV_USE_DEMO_WIDGETS
```

**弱选择（Implies）**

```text
CONFIG_LV_USE_SYSMON
CONFIG_LV_USE_PERF_MONITOR
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3819`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)、[`CONFIG_LV_FONT_MONTSERRAT_20`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_20)、[`CONFIG_LV_FONT_MONTSERRAT_24`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_24)、[`CONFIG_LV_FONT_MONTSERRAT_26`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_26)、[`CONFIG_LV_USE_DEMO_WIDGETS`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_WIDGETS)、[`CONFIG_LV_USE_SYSMON`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SYSMON)、[`CONFIG_LV_USE_PERF_MONITOR`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PERF_MONITOR)。

<a id="CONFIG_LV_USE_DEMO_EBIKE"></a>

## 19.27 `CONFIG_LV_USE_DEMO_EBIKE`

**提示（Prompt）**：电动自行车演示（E-bike Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3901`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_FLEX_LAYOUT"></a>

## 19.28 `CONFIG_LV_USE_DEMO_FLEX_LAYOUT`

**提示（Prompt）**：弹性布局演示（Flex Layout Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3891`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_GLTF"></a>

## 19.29 `CONFIG_LV_USE_DEMO_GLTF`

**提示（Prompt）**：glTF 演示（Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_GLTF && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3837`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_GLTF`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GLTF)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_HIGH_RES"></a>

## 19.30 `CONFIG_LV_USE_DEMO_HIGH_RES`

**提示（Prompt）**：高分辨率演示（High Resolution Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3909`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_KEYPAD_AND_ENCODER"></a>

## 19.31 `CONFIG_LV_USE_DEMO_KEYPAD_AND_ENCODER`

**提示（Prompt）**：键盘与编码器演示（Keypad and Encoder Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3841`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_MULTILANG"></a>

## 19.32 `CONFIG_LV_USE_DEMO_MULTILANG`

**提示（Prompt）**：多语言演示（Multi-language Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3894`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_MUSIC"></a>

## 19.33 `CONFIG_LV_USE_DEMO_MUSIC`

**提示（Prompt）**：音乐播放器演示（Music Player Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3845`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_RENDER"></a>

## 19.34 `CONFIG_LV_USE_DEMO_RENDER`

**提示（Prompt）**：渲染演示（Render Demo）

**说明（Help）**

渲染每种绘制图元（Drawing Primitive），以进行视觉比较。需要至少 480×272 的显示器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GRID
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3871`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GRID`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GRID)。

<a id="CONFIG_LV_USE_DEMO_SMARTWATCH"></a>

## 19.35 `CONFIG_LV_USE_DEMO_SMARTWATCH`

**提示（Prompt）**：智能手表演示（Smartwatch Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3898`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_STRESS"></a>

## 19.36 `CONFIG_LV_USE_DEMO_STRESS`

**提示（Prompt）**：压力测试演示（Stress Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3879`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DEMO_VECTOR_GRAPHIC"></a>

## 19.37 `CONFIG_LV_USE_DEMO_VECTOR_GRAPHIC`

**提示（Prompt）**：矢量图形演示（Vector Graphic Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_VECTOR_GRAPHIC
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3882`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_VECTOR_GRAPHIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_VECTOR_GRAPHIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_DEMO_WIDGETS"></a>

## 19.38 `CONFIG_LV_USE_DEMO_WIDGETS`

**提示（Prompt）**：控件演示（Widgets Demo）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3887`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_USE_DRAW_ARM2D_SYNC"></a>

## 19.39 `CONFIG_LV_USE_DRAW_ARM2D_SYNC`

**提示（Prompt）**：Arm-2D 加速（Acceleration，Cortex-M）

**说明（Help）**

要求项目中具有 Arm-2D 库，并提供 `arm_2d.h` 的包含路径（Include Path）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:534`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_DAVE2D"></a>

## 19.40 `CONFIG_LV_USE_DRAW_DAVE2D`

**提示（Prompt）**：Dave2D 渲染器（Renderer）

**说明（Help）**

使用 Renesas RA 平台上的 Dave2D 图形处理器（GPU）加速绘制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:773`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → Dave2D 图形引擎

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_DMA2D"></a>

## 19.41 `CONFIG_LV_USE_DRAW_DMA2D`

**提示（Prompt）**：DMA2D 渲染器（Renderer）

**说明（Help）**

使用 STM32 DMA2D 外设加速混合（Blend）、填充（Fill）和图像解码（Image Decoding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:983`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维直接存储器访问（DMA2D）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_DMA2D_INTERRUPT"></a>

## 19.42 `CONFIG_LV_USE_DRAW_DMA2D_INTERRUPT`

**提示（Prompt）**：传输完成中断（Transfer Complete Interrupt）

**说明（Help）**

异步运行 DMA2D 传输，而不等待其完成，需要操作系统（OS）。从 DMA2D 全局中断服务例程（ISR）调用 `lv_draw_dma2d_transfer_complete_interrupt_handler()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_DMA2D && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:997`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维直接存储器访问（DMA2D） → DMA2D 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_DMA2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_DMA2D)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_EVE"></a>

## 19.43 `CONFIG_LV_USE_DRAW_EVE`

**提示（Prompt）**：EVE 渲染器（Renderer）

**说明（Help）**

通过 SPI 将绘制工作卸载（Offload）到外部 EVE（FT81X/BT81X）图形控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1037`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 嵌入式视频引擎（EVE）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_G2D"></a>

## 19.44 `CONFIG_LV_USE_DRAW_G2D`

**提示（Prompt）**：G2D 渲染器（Renderer）

**说明（Help）**

使用 NXP G2D API，即 i.MX 二维 GPU，加速混合（Blend）、填充（Fill）和图像块传送（Blit）。需要 g2d 库及其头文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_SW
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_G2D
CONFIG_LV_WAYLAND_USE_G2D
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1071`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维图形（G2D）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LV_USE_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_G2D)、[`CONFIG_LV_WAYLAND_USE_G2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_WAYLAND_USE_G2D)。

<a id="CONFIG_LV_USE_DRAW_NANOVG"></a>

## 19.45 `CONFIG_LV_USE_DRAW_NANOVG`

**提示（Prompt）**：NanoVG 渲染器（Renderer）

**说明（Help）**

使用基于 OpenGL / OpenGL ES 着色器（Shader）的 NanoVG 矢量库（Vector Library）进行绘制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_NANOVG
CONFIG_LV_USE_OPENGLES
CONFIG_LV_USE_MATRIX
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT
CONFIG_LV_DRAW_HAS_3D_SUPPORT
CONFIG_LV_DRAW_DISABLE_TILED_RENDERING
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1108`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NanoVG 矢量图形库

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_NANOVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NANOVG)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)、[`CONFIG_LV_USE_MATRIX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MATRIX)、[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)、[`CONFIG_LV_DRAW_HAS_3D_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_3D_SUPPORT)、[`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_DISABLE_TILED_RENDERING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`、`CONFIG_LV_DRAW_HAS_3D_SUPPORT`、`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`。

<a id="CONFIG_LV_USE_DRAW_OPENGLES"></a>

## 19.46 `CONFIG_LV_USE_DRAW_OPENGLES`

**提示（Prompt）**：OpenGL ES 渲染器（Renderer）

**说明（Help）**

使用 OpenGL ES 绘制，将已渲染控件和图像保留为 GPU 纹理（Texture）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_OPENGLES
CONFIG_LV_DRAW_HAS_3D_SUPPORT
CONFIG_LV_DRAW_DISABLE_TILED_RENDERING
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1162`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → OpenGL ES 图形 API

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)、[`CONFIG_LV_DRAW_HAS_3D_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_3D_SUPPORT)、[`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_DISABLE_TILED_RENDERING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_3D_SUPPORT`、`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`。

<a id="CONFIG_LV_USE_DRAW_PXP"></a>

## 19.47 `CONFIG_LV_USE_DRAW_PXP`

**提示（Prompt）**：PXP 渲染器（Renderer）

**说明（Help）**

使用 NXP i.MX RT SoC 的像素流水线（Pixel Pipeline，PXP）引擎加速混合（Blend）、填充（Fill）和变换（Transform）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_PXP
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:904`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素流水线（PXP）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_PXP`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PXP)。

<a id="CONFIG_LV_USE_DRAW_SDL"></a>

## 19.48 `CONFIG_LV_USE_DRAW_SDL`

**提示（Prompt）**：SDL 渲染器（Renderer）

**说明（Help）**

使用 SDL 渲染器 API（Renderer API）进行渲染，将控件和图像缓存为 SDL 纹理（Texture）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_SW
CONFIG_LV_DRAW_DISABLE_TILED_RENDERING
```

**被选择（Selected by）**

```text
CONFIG_LV_SDL_BACKEND_TEXTURE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1184`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → SDL 多媒体库

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_DISABLE_TILED_RENDERING)、[`CONFIG_LV_SDL_BACKEND_TEXTURE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_SDL_BACKEND_TEXTURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_DISABLE_TILED_RENDERING`。

<a id="CONFIG_LV_USE_DRAW_SW"></a>

## 19.49 `CONFIG_LV_USE_DRAW_SW`

**提示（Prompt）**：软件渲染器（SW Renderer）

**说明（Help）**

在屏幕上绘制任何内容都需要此功能。

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
CONFIG_LV_USE_PPA
CONFIG_LV_USE_SIFLI_EPIC
CONFIG_LV_USE_DRAW_G2D
CONFIG_LV_USE_DRAW_SDL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:462`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_PPA`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PPA)、[`CONFIG_LV_USE_SIFLI_EPIC`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SIFLI_EPIC)、[`CONFIG_LV_USE_DRAW_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_G2D)、[`CONFIG_LV_USE_DRAW_SDL`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SDL)。

<a id="CONFIG_LV_USE_DRAW_SW_ASM"></a>

## 19.50 `CONFIG_LV_USE_DRAW_SW_ASM`

**提示（Prompt）**：软件汇编优化（SW Assembly Optimization）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_DRAW_SW_ASM_NONE
```

**可选项（Choices）**

```text
CONFIG_LV_DRAW_SW_ASM_NONE
CONFIG_LV_DRAW_SW_ASM_NEON
CONFIG_LV_DRAW_SW_ASM_HELIUM
CONFIG_LV_DRAW_SW_ASM_RISCV_V
CONFIG_LV_DRAW_SW_ASM_SVE2
CONFIG_LV_DRAW_SW_ASM_CUSTOM
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:582`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_DRAW_SW_ASM_NONE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_NONE)、[`CONFIG_LV_DRAW_SW_ASM_NEON`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_NEON)、[`CONFIG_LV_DRAW_SW_ASM_HELIUM`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_HELIUM)、[`CONFIG_LV_DRAW_SW_ASM_RISCV_V`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_RISCV_V)、[`CONFIG_LV_DRAW_SW_ASM_SVE2`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_SVE2)、[`CONFIG_LV_DRAW_SW_ASM_CUSTOM`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_CUSTOM)。

<a id="CONFIG_LV_USE_DRAW_SW_COMPLEX_GRADIENTS"></a>

## 19.51 `CONFIG_LV_USE_DRAW_SW_COMPLEX_GRADIENTS`

**提示（Prompt）**：复杂渐变（Complex Gradients）

**说明（Help）**

增加带角度的线性渐变（Linear Gradient）、径向渐变（Radial Gradient）和锥形渐变（Conical Gradient）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:559`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_DRAW_VG_LITE"></a>

## 19.52 `CONFIG_LV_USE_DRAW_VG_LITE`

**提示（Prompt）**：VG-Lite 渲染器（Renderer）

**说明（Help）**

使用 VG-Lite GPU 渲染。需要 VG-Lite 驱动或下方的 VG-Lite 模拟器（Simulator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_MATRIX
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:622`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_MATRIX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MATRIX)、[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_DROPDOWN"></a>

## 19.53 `CONFIG_LV_USE_DROPDOWN`

**提示（Prompt）**：下拉列表（Dropdown）

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

**主动选择（Selects）**

```text
CONFIG_LV_USE_LABEL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2090`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_LABEL`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_LABEL)。

<a id="CONFIG_LV_USE_EVDEV"></a>

## 19.54 `CONFIG_LV_USE_EVDEV`

**提示（Prompt）**：事件设备（evdev）

**说明（Help）**

从 Linux 的 `/dev/input` 事件设备（Event Device）读取触摸屏、鼠标和键盘输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2549`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_EXT_DATA"></a>

## 19.55 `CONFIG_LV_USE_EXT_DATA`

**提示（Prompt）**：外部数据与析构函数（External Data and Destructor）

**说明（Help）**

为事件（Event）、控件（Widget）、观察者（Observer）、动画（Animation）、定时器（Timer）、组（Group）、显示器（Display）、输入设备（Input Device）和主题（Theme）附加自己的数据及析构回调（Destructor Callback），使 LVGL 释放它们时，也清理你的资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1357`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FFMPEG"></a>

## 19.56 `CONFIG_LV_USE_FFMPEG`

**提示（Prompt）**：FFmpeg 播放器（Player）

**说明（Help）**

使用 FFmpeg 解码图像并播放视频。它支持所有主要图像格式，因此不要同时启用其他图像解码器（Image Decoder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2095`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FILE_EXPLORER"></a>

## 19.57 `CONFIG_LV_USE_FILE_EXPLORER`

**提示（Prompt）**：文件浏览器（File Explorer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_TABLE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3485`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 其他（Others）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_TABLE`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_TABLE)。

<a id="CONFIG_LV_USE_FLEX"></a>

## 19.58 `CONFIG_LV_USE_FLEX`

**提示（Prompt）**：弹性布局（Flex）

**说明（Help）**

将子对象排列在可换行、可扩展的行或列中，类似 CSS 的弹性盒布局（Flexbox）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1517`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 布局（Layouts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FLOAT"></a>

## 19.59 `CONFIG_LV_USE_FLOAT`

**提示（Prompt）**：使用浮点数（Float）作为 `lv_value_precise_t`

**说明（Help）**

对于需要亚像素精度（Sub-pixel Precision）的坐标和值，使用 `float` 代替 `int32_t`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_MATRIX
CONFIG_LV_USE_GESTURE_RECOGNITION
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1365`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_MATRIX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MATRIX)、[`CONFIG_LV_USE_GESTURE_RECOGNITION`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GESTURE_RECOGNITION)。

<a id="CONFIG_LV_USE_FONT_COMPRESSED"></a>

## 19.60 `CONFIG_LV_USE_FONT_COMPRESSED`

**提示（Prompt）**：压缩字体（Compressed Fonts）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1868`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FONT_MANAGER"></a>

## 19.61 `CONFIG_LV_USE_FONT_MANAGER`

**提示（Prompt）**：字体管理器（Font Manager）

**说明（Help）**

按名称加载字体，在控件之间共享字体，并通过引用计数（Reference Counting）释放字体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1878`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FONT_PLACEHOLDER"></a>

## 19.62 `CONFIG_LV_USE_FONT_PLACEHOLDER`

**提示（Prompt）**：字形占位符（Glyph Placeholders）

**说明（Help）**

字体缺少某个字形（Glyph）时，绘制占位矩形（Placeholder Rectangle），而不是不显示任何内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1871`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FRAGMENT"></a>

## 19.63 `CONFIG_LV_USE_FRAGMENT`

**提示（Prompt）**：片段（Fragment）

**说明（Help）**

管理具有独立生命周期（Lifecycle）和返回栈（Back Stack）的控件子树（Widget Subtree），类似 Android 片段（Fragment）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3479`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 其他（Others）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FREERTOS_TASK_NOTIFY"></a>

## 19.64 `CONFIG_LV_USE_FREERTOS_TASK_NOTIFY`

**提示（Prompt）**：直接任务通知（Direct Task Notifications）

**说明（Help）**

使用直接任务通知（Direct Task Notification）而不是二值信号量（Binary Semaphore）等中间对象进行同步：速度提高 45%，且使用更少 RAM，但仅适用于单个任务可作为事件接收者的情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_OS_FREERTOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:244`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS） → FreeRTOS 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_FREERTOS`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_FREERTOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FREETYPE"></a>

## 19.65 `CONFIG_LV_USE_FREETYPE`

**提示（Prompt）**：FreeType 字体引擎

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1897`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS"></a>

## 19.66 `CONFIG_LV_USE_FS_ARDUINO_ESP_LITTLEFS`

**提示（Prompt）**：Arduino ESP littlefs 文件系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3132`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_ARDUINO_SD"></a>

## 19.67 `CONFIG_LV_USE_FS_ARDUINO_SD`

**提示（Prompt）**：Arduino SD 文件系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3148`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_FATFS"></a>

## 19.68 `CONFIG_LV_USE_FS_FATFS`

**提示（Prompt）**：FatFS 文件系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3095`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_FROGFS"></a>

## 19.69 `CONFIG_LV_USE_FS_FROGFS`

**提示（Prompt）**：FrogFS 文件系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3174`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_LITTLEFS"></a>

## 19.70 `CONFIG_LV_USE_FS_LITTLEFS`

**提示（Prompt）**：littlefs 文件系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3116`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_MEMFS"></a>

## 19.71 `CONFIG_LV_USE_FS_MEMFS`

**提示（Prompt）**：内存映射（Memory-mapped）

**说明（Help）**

通过 `lv_fs` API 访问已在内存中的数据，而无需实际文件系统（File System）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3184`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_POSIX"></a>

## 19.72 `CONFIG_LV_USE_FS_POSIX`

**提示（Prompt）**：POSIX 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3053`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_STDIO"></a>

## 19.73 `CONFIG_LV_USE_FS_STDIO`

**提示（Prompt）**：标准输入／输出（stdio）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3032`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_UEFI"></a>

## 19.74 `CONFIG_LV_USE_FS_UEFI`

**提示（Prompt）**：统一可扩展固件接口（UEFI）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3164`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FS_WIN32"></a>

## 19.75 `CONFIG_LV_USE_FS_WIN32`

**提示（Prompt）**：Win32 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3074`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文件系统（File System）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_FT81X"></a>

## 19.76 `CONFIG_LV_USE_FT81X`

**提示（Prompt）**：FT81X 图形控制器

**说明（Help）**

通过 SPI 连接的 FT81X EVE 图形控制器（Graphics Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2467`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_G2D"></a>

## 19.77 `CONFIG_LV_USE_G2D`

**提示（Prompt）**：G2D，旧版（Legacy）

**说明（Help）**

请改用 `LV_USE_DRAW_G2D`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_G2D
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1064`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维图形（G2D）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_G2D)。

<a id="CONFIG_LV_USE_G2D_ASSERT"></a>

## 19.78 `CONFIG_LV_USE_G2D_ASSERT`

**提示（Prompt）**：断言（Asserts）

**说明（Help）**

检查每次 G2D 调用的状态，失败时触发断言（Assert）。这对开发板初始调试（Bring-up）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_G2D && CONFIG_LV_USE_DRAW_G2D && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1096`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维图形（G2D） → G2D 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_G2D)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_G2D_DRAW_THREAD"></a>

## 19.79 `CONFIG_LV_USE_G2D_DRAW_THREAD`

**提示（Prompt）**：专用绘制线程（Dedicated Draw Thread）

**说明（Help）**

通过独立线程分派 G2D 操作，使 CPU 能继续并行渲染。需要操作系统（OS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LV_USE_DRAW_G2D && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1088`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维图形（G2D） → G2D 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_NONE)、[`CONFIG_LV_USE_DRAW_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_G2D)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_GENERIC_MIPI"></a>

## 19.80 `CONFIG_LV_USE_GENERIC_MIPI`

**提示（Prompt）**：通用 MIPI（Generic MIPI）

**说明（Help）**

通过 SPI 或并行端口（Parallel Port）连接的 LCD 设备驱动。如果 LCD 控制器未列在下方专用驱动中，请使用此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_ST7735
CONFIG_LV_USE_ST7789
CONFIG_LV_USE_ST7796
CONFIG_LV_USE_ILI9341
CONFIG_LV_USE_NV3007
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2485`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_ST7735`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_ST7735)、[`CONFIG_LV_USE_ST7789`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_ST7789)、[`CONFIG_LV_USE_ST7796`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_ST7796)、[`CONFIG_LV_USE_ILI9341`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_ILI9341)、[`CONFIG_LV_USE_NV3007`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NV3007)。

<a id="CONFIG_LV_USE_GESTURE_RECOGNITION"></a>

## 19.81 `CONFIG_LV_USE_GESTURE_RECOGNITION`

**提示（Prompt）**：多点触控手势识别（Multi-touch Gesture Recognition）

**说明（Help）**

从多点触控输入（Multi-touch Input）检测捏合（Pinch）与旋转（Rotate）手势，需要浮点支持（Float Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_FLOAT
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1264`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_FLOAT`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_FLOAT)。

<a id="CONFIG_LV_USE_GIF"></a>

## 19.82 `CONFIG_LV_USE_GIF`

**提示（Prompt）**：GIF 解码器（Decoder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2120`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_GLFW"></a>

## 19.83 `CONFIG_LV_USE_GLFW`

**提示（Prompt）**：GLFW 窗口库

**说明（Help）**

通过 GLFW 在 PC 桌面打开窗口，并读取鼠标和键盘输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_EGL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_OPENGLES
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2743`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_EGL)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_USE_EGL`。

<a id="CONFIG_LV_USE_GLTF"></a>

## 19.84 `CONFIG_LV_USE_GLTF`

**提示（Prompt）**：glTF 三维资产格式

**说明（Help）**

解析并渲染三维模型（3D Model），支持 `.gltf/.glb`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_HAS_3D_SUPPORT && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_3DTEXTURE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2143`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_HAS_3D_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_3D_SUPPORT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_3DTEXTURE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_USE_3DTEXTURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_3D_SUPPORT`。

<a id="CONFIG_LV_USE_GRID"></a>

## 19.85 `CONFIG_LV_USE_GRID`

**提示（Prompt）**：网格布局（Grid）

**说明（Help）**

将子对象排列成行和列，类似 CSS 的网格布局（Grid）。

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
CONFIG_LV_USE_DEMO_RENDER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1523`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 布局（Layouts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DEMO_RENDER`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_RENDER)。

<a id="CONFIG_LV_USE_GRIDNAV"></a>

## 19.86 `CONFIG_LV_USE_GRIDNAV`

**提示（Prompt）**：网格导航（Grid Navigation）

**说明（Help）**

根据子对象的位置，使用方向键在容器（Container）的子对象之间移动焦点（Focus）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1258`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 输入设备（Input Devices）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_GSTREAMER"></a>

## 19.87 `CONFIG_LV_USE_GSTREAMER`

**提示（Prompt）**：GStreamer 播放器（Player）

**说明（Help）**

需要 `gstreamer-1.0`、`gstreamer-video-1.0` 和 `gstreamer-app-1.0` 开发库（Development Libraries）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_IMAGE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2150`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_IMAGE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_IMAGE)。

<a id="CONFIG_LV_USE_ILI9341"></a>

## 19.88 `CONFIG_LV_USE_ILI9341`

**提示（Prompt）**：ILI9341 显示控制器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GENERIC_MIPI
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2507`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GENERIC_MIPI`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GENERIC_MIPI)。

<a id="CONFIG_LV_USE_IMAGE"></a>

## 19.89 `CONFIG_LV_USE_IMAGE`

**提示（Prompt）**：图像（Image）

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
CONFIG_LV_USE_CANVAS
CONFIG_LV_USE_GSTREAMER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2158`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_CANVAS`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CANVAS)、[`CONFIG_LV_USE_GSTREAMER`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GSTREAMER)。

<a id="CONFIG_LV_USE_IMAGEBUTTON"></a>

## 19.90 `CONFIG_LV_USE_IMAGEBUTTON`

**提示（Prompt）**：图像按钮（Image Button）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2162`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_IME_PINYIN"></a>

## 19.91 `CONFIG_LV_USE_IME_PINYIN`

**提示（Prompt）**：拼音输入法（Pinyin Input Method）

**说明（Help）**

中文输入法（Chinese Input Method），将键盘控件上输入的拼音（Pinyin）转换为汉字。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_KEYBOARD
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2166`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_KEYBOARD`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_KEYBOARD)。

<a id="CONFIG_LV_USE_IMGFONT"></a>

## 19.92 `CONFIG_LV_USE_IMGFONT`

**提示（Prompt）**：图像字体（Image Font）

**说明（Help）**

在标签（Label）和文本片段（Span）控件中将图像用作字形（Glyph），例如渲染表情符号（Emoji）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1890`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_KEYBOARD"></a>

## 19.93 `CONFIG_LV_USE_KEYBOARD`

**提示（Prompt）**：键盘（Keyboard）

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
CONFIG_LV_USE_IME_PINYIN
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2200`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_IME_PINYIN`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_IME_PINYIN)。

<a id="CONFIG_LV_USE_LABEL"></a>

## 19.94 `CONFIG_LV_USE_LABEL`

**提示（Prompt）**：标签（Label）

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
CONFIG_LV_USE_DROPDOWN
CONFIG_LV_USE_MSGBOX
CONFIG_LV_USE_ROLLER
CONFIG_LV_USE_TEXTAREA
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2204`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DROPDOWN`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DROPDOWN)、[`CONFIG_LV_USE_MSGBOX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MSGBOX)、[`CONFIG_LV_USE_ROLLER`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_ROLLER)、[`CONFIG_LV_USE_TEXTAREA`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_TEXTAREA)。

<a id="CONFIG_LV_USE_LAYER_DEBUG"></a>

## 19.95 `CONFIG_LV_USE_LAYER_DEBUG`

**提示（Prompt）**：图层类型覆盖层（Layer Type Overlay）

**说明（Help）**

在 ARGB 图层上绘制红色覆盖层（Overlay），在 RGB 图层上绘制绿色覆盖层。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3466`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 调试渲染（Debug Rendering）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LED"></a>

## 19.96 `CONFIG_LV_USE_LED`

**提示（Prompt）**：发光二极管（LED）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2229`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LIBINPUT"></a>

## 19.97 `CONFIG_LV_USE_LIBINPUT`

**提示（Prompt）**：libinput 输入库

**说明（Help）**

通过 libinput 读取指针、触摸和键盘输入；构建中必须提供 libinput。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2554`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LIBJPEG_TURBO"></a>

## 19.98 `CONFIG_LV_USE_LIBJPEG_TURBO`

**提示（Prompt）**：JPEG 解码器（Decoder，libjpeg-turbo）

**说明（Help）**

支持完整 JPEG 规范（Specifications）的高性能解码器（Decoder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1579`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LIBPNG"></a>

## 19.99 `CONFIG_LV_USE_LIBPNG`

**提示（Prompt）**：PNG 解码器（Decoder，libpng）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1568`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LIBWEBP"></a>

## 19.100 `CONFIG_LV_USE_LIBWEBP`

**提示（Prompt）**：WebP 解码器（Decoder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1584`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<!-- kconfig-navigation -->

[上一章](P018_module_lvgl_zephyr_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P020_module_lvgl_zephyr_配置项参考_6.md)
