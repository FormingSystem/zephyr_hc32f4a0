---
id: learning.zephyr-docs.kconfig-reference.page-15
title: "`<module:lvgl>/zephyr`配置项参考（1/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第15章\_`<module:lvgl>/zephyr`配置项参考（1/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_APRIL_STR"></a>

## 15.1 `CONFIG_LV_APRIL_STR`

**提示（Prompt）**：四月名称字符串（String for April）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"April"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2032`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ASSERT_CUSTOM_INCLUDE"></a>

## 15.2 `CONFIG_LV_ASSERT_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义断言处理程序头文件路径（Custom Assert Handler Header Path）

**说明（Help）**

可选头文件，用于覆盖断言（Assert）相关的宏。

`LV_ASSERT_HANDLER` 指定断言失败时执行的语句，例如：

```c
#define LV_ASSERT_HANDLER my_assert_failed(__FILE__, __LINE__);
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_ASSERT_USE_CUSTOM_INCLUDE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3639`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts） → 自定义断言处理程序头文件（Custom Assert Handler Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_ASSERT_USE_CUSTOM_INCLUDE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_ASSERT_USE_CUSTOM_INCLUDE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ASSERT_HANDLER_INCLUDE"></a>

## 15.3 `CONFIG_LV_ASSERT_HANDLER_INCLUDE`

**提示（Prompt）**：断言处理程序头文件（Assert Handler Header）［已弃用：使用 `LV_ASSERT_CUSTOM_INCLUDE`］

**说明（Help）**

［已弃用（Deprecated）：使用 `LV_ASSERT_CUSTOM_INCLUDE`］添加在断言（Assert）发生时执行的自定义处理程序，例如重新启动 MCU。可选头文件用于覆盖断言相关的宏。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3603`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ASSERT_USE_CUSTOM_INCLUDE"></a>

## 15.4 `CONFIG_LV_ASSERT_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义断言处理程序头文件（Custom Assert Handler Header）

**说明（Help）**

包含 `LV_ASSERT_CUSTOM_INCLUDE` 指定的头文件，其中必须定义自定义的断言处理程序宏 `LV_ASSERT_HANDLER`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3632`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ATTRIBUTE_CUSTOM_INCLUDE"></a>

## 15.5 `CONFIG_LV_ATTRIBUTE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义属性头文件路径（Custom Attributes Header Path）

**说明（Help）**

可选头文件，用于为所用平台覆盖 `LV_ATTRIBUTE_*` 宏。留空则使用默认值，即这些宏均展开为空。

创建一个头文件，并将此项设为该头文件的路径，例如 `"my_lv_attr.h"`。可在其中定义以下宏：

- `LV_ATTRIBUTE_MEM_ALIGN`：用于需要内存对齐（Memory Alignment）的位置。例如，使用 `-Os` 时，数据默认可能未对齐到所需边界。示例：`__attribute__((aligned(4)))`。
- `LV_ATTRIBUTE_TICK_INC`：应用于 `lv_tick_inc()`。该函数经常从定时器中断服务例程（ISR）调用，因此放入快速存储器可减少延迟。示例：`__attribute__((section(".itcm")))` 或 IAR 的 `__ramfunc`。
- `LV_ATTRIBUTE_TIMER_HANDLER`：应用于 `lv_timer_handler()`。示例：`__attribute__((section(".itcm")))`。
- `LV_ATTRIBUTE_FLUSH_READY`：应用于 `lv_display_flush_ready()`。该函数经常从 DMA 或显示 ISR 调用。示例：`__attribute__((section(".itcm")))`。
- `LV_ATTRIBUTE_SYNC_READY`：应用于 `lv_display_sync_ready()`。与 `FLUSH_READY` 类似，从 ISR 上下文调用时很有用。示例：`__attribute__((section(".itcm")))`。
- `LV_ATTRIBUTE_LARGE_CONST`：应用于字形位图等大型只读数组（Read-only Array），用于将它们放入特定 Flash 区域或外部存储器。示例：`__attribute__((section(".ext_flash")))`。
- `LV_ATTRIBUTE_LARGE_RAM_ARRAY`：应用于分配在 RAM 中的大型数组。示例：`__attribute__((section(".ext_ram")))`。
- `LV_ATTRIBUTE_FAST_MEM`：应用于性能关键函数（Performance-critical Function），将它们放入 ITCM 或 SRAM 等更快的存储器。示例：`__attribute__((section(".itcm")))` 或 IAR 的 `__ramfunc`。
- `LV_ATTRIBUTE_EXTERN_DATA`：所有全局外部数据声明（Global Extern Data Declaration）的前缀，可用于将共享数据放入具名段（Named Section），或应用导出属性（Export Attributes）。示例：`__attribute__((section(".shared_mem")))`。
- `LV_EXPORT_CONST_INT(int_value)`：将整数常量导出到 MicroPython 等语言绑定 API（Language Binding API）。所有形如 `LV_<CONST>` 的常量都会调用此宏。不使用语言绑定时，保持未定义。示例：`mp_rom_map_elem_t entry = {MP_ROM_QSTR(MP_QSTR_##int_value), MP_ROM_INT(int_value)}`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_ATTRIBUTE_USE_CUSTOM_INCLUDE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3739`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 编译器设置（Compiler Settings） → 自定义属性头文件（Custom Attributes Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_ATTRIBUTE_USE_CUSTOM_INCLUDE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_ATTRIBUTE_USE_CUSTOM_INCLUDE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ATTRIBUTE_FAST_MEM_USE_IRAM"></a>

## 15.6 `CONFIG_LV_ATTRIBUTE_FAST_MEM_USE_IRAM`

**提示（Prompt）**：将 `LV_ATTRIBUTE_FAST_MEM` 函数放入指令 RAM（IRAM，仅 ESP32）

**说明（Help）**

将 `LV_ATTRIBUTE_FAST_MEM` 配置为使用指令 RAM（IRAM）。此选项仅适用于 ESP32 目标。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3799`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 编译器设置（Compiler Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ATTRIBUTE_USE_CUSTOM_INCLUDE"></a>

## 15.7 `CONFIG_LV_ATTRIBUTE_USE_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义属性头文件（Custom Attributes Header）

**说明（Help）**

包含 `LV_ATTRIBUTE_CUSTOM_INCLUDE` 指定的头文件，为所用平台覆盖 `LV_ATTRIBUTE_*` 宏。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3732`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 编译器设置（Compiler Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_AUGUST_STR"></a>

## 15.8 `CONFIG_LV_AUGUST_STR`

**提示（Prompt）**：八月名称字符串（String for August）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"August"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2044`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_BASE_DIR_AUTO"></a>

## 15.9 `CONFIG_LV_BASE_DIR_AUTO`

**提示（Prompt）**：自动检测（Auto Detect）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_BIDI_BASE_DIR_DEF>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1660`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 双向文本（Bidirectional Text） → 默认基本方向（Default Base Direction）

**配置项引用（Symbol References）**：[`CONFIG_LV_BIDI_BASE_DIR_DEF`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BIDI_BASE_DIR_DEF)。

<a id="CONFIG_LV_BASE_DIR_LTR"></a>

## 15.10 `CONFIG_LV_BASE_DIR_LTR`

**提示（Prompt）**：从左到右（Left-to-Right）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_BIDI_BASE_DIR_DEF>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1656`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 双向文本（Bidirectional Text） → 默认基本方向（Default Base Direction）

**配置项引用（Symbol References）**：[`CONFIG_LV_BIDI_BASE_DIR_DEF`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BIDI_BASE_DIR_DEF)。

<a id="CONFIG_LV_BASE_DIR_RTL"></a>

## 15.11 `CONFIG_LV_BASE_DIR_RTL`

**提示（Prompt）**：从右到左（Right-to-Left）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_BIDI_BASE_DIR_DEF>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1658`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 双向文本（Bidirectional Text） → 默认基本方向（Default Base Direction）

**配置项引用（Symbol References）**：[`CONFIG_LV_BIDI_BASE_DIR_DEF`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BIDI_BASE_DIR_DEF)。

<a id="CONFIG_LV_BIDI_BASE_DIR_DEF"></a>

## 15.12 `CONFIG_LV_BIDI_BASE_DIR_DEF`

**提示（Prompt）**：默认基本方向（Default Base Direction）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BIDI && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_BASE_DIR_AUTO
```

**可选项（Choices）**

```text
CONFIG_LV_BASE_DIR_LTR
CONFIG_LV_BASE_DIR_RTL
CONFIG_LV_BASE_DIR_AUTO
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1651`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 双向文本（Bidirectional Text）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BIDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_BIDI)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_BASE_DIR_AUTO`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BASE_DIR_AUTO)、[`CONFIG_LV_BASE_DIR_LTR`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BASE_DIR_LTR)、[`CONFIG_LV_BASE_DIR_RTL`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BASE_DIR_RTL)。

<a id="CONFIG_LV_BIG_ENDIAN_SYSTEM"></a>

## 15.13 `CONFIG_LV_BIG_ENDIAN_SYSTEM`

**提示（Prompt）**：大端系统（Big-endian System）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3729`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 编译器设置（Compiler Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_BIN_DECODER_RAM_LOAD"></a>

## 15.14 `CONFIG_LV_BIN_DECODER_RAM_LOAD`

**提示（Prompt）**：将二进制图像（Binary Image）解码到 RAM

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1561`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_BUILD_DEMOS"></a>

## 15.15 `CONFIG_LV_BUILD_DEMOS`

**提示（Prompt）**：构建演示（Demos）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3813`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_BUILD_EXAMPLES"></a>

## 15.16 `CONFIG_LV_BUILD_EXAMPLES`

**提示（Prompt）**：构建示例（Examples）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3807`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 示例（Examples）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CACHE_DEF_SIZE"></a>

## 15.17 `CONFIG_LV_CACHE_DEF_SIZE`

**提示（Prompt）**：默认图像缓存大小（Image Cache Size，字节，0 表示禁用）

**说明（Help）**

避免反复打开和解码相同的图像，代价是消耗 RAM。仅使用内置图像格式（Built-in Image Formats）时，收益有限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1531`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CALENDAR_WEEK_STARTS_MONDAY"></a>

## 15.18 `CONFIG_LV_CALENDAR_WEEK_STARTS_MONDAY`

**提示（Prompt）**：每周从星期一开始（Week Starts on Monday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1991`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CHECK_ARG_ASSERT_ON_FAIL"></a>

## 15.19 `CONFIG_LV_CHECK_ARG_ASSERT_ON_FAIL`

**提示（Prompt）**：失败时断言（Assert on Failure）

**说明（Help）**

当 `LV_CHECK_ARG` 检查失败时，在执行相应动作之前，也调用 `LV_ASSERT_HANDLER`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CHECK_ARG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3664`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CHECK_ARG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CHECK_ARG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CHECK_ARG_LOG_MODE_MINIMAL"></a>

## 15.20 `CONFIG_LV_CHECK_ARG_LOG_MODE_MINIMAL`

**提示（Prompt）**：最简（Minimal）：仅记录 `Check failed`，文件与行号来自 `LV_LOG_WARN`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && <choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3683`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation） → `LV_CHECK_ARG` 失败时的日志行为（Log Behavior）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)。

<a id="CONFIG_LV_CHECK_ARG_LOG_MODE_NONE"></a>

## 15.21 `CONFIG_LV_CHECK_ARG_LOG_MODE_NONE`

**提示（Prompt）**：无（None）：失败时不输出日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3680`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation） → `LV_CHECK_ARG` 失败时的日志行为（Log Behavior）

<a id="CONFIG_LV_CHECK_ARG_LOG_MODE_VERBOSE"></a>

## 15.22 `CONFIG_LV_CHECK_ARG_LOG_MODE_VERBOSE`

**提示（Prompt）**：详细（Verbose）：记录 `Check failed: <cond>` 及调用方提供的消息

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LOG && <choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3687`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 参数检查（Argument Checks） → 运行时参数验证（Runtime Argument Validation） → `LV_CHECK_ARG` 失败时的日志行为（Log Behavior）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_LOG)。

<a id="CONFIG_LV_COLOR_DEPTH_1"></a>

## 15.23 `CONFIG_LV_COLOR_DEPTH_1`

**提示（Prompt）**：1：I1，每像素 1 位（1 Bit per Pixel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:316`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_DEPTH_16"></a>

## 15.24 `CONFIG_LV_COLOR_DEPTH_16`

**提示（Prompt）**：16：RGB565 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:310`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_DEPTH_24"></a>

## 15.25 `CONFIG_LV_COLOR_DEPTH_24`

**提示（Prompt）**：24：RGB888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:307`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_DEPTH_32"></a>

## 15.26 `CONFIG_LV_COLOR_DEPTH_32`

**提示（Prompt）**：32：XRGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:304`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_DEPTH_8"></a>

## 15.27 `CONFIG_LV_COLOR_DEPTH_8`

**提示（Prompt）**：8：L8 灰度（Grayscale）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_UNSCII_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:313`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)、[`CONFIG_LV_FONT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_UNSCII_8)。

<a id="CONFIG_LV_COLOR_DEPTH_CHOICE"></a>

## 15.28 `CONFIG_LV_COLOR_DEPTH_CHOICE`

**提示（Prompt）**：颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_COLOR_DEPTH_UNSET
```

**可选项（Choices）**

```text
CONFIG_LV_COLOR_DEPTH_UNSET
CONFIG_LV_COLOR_DEPTH_32
CONFIG_LV_COLOR_DEPTH_24
CONFIG_LV_COLOR_DEPTH_16
CONFIG_LV_COLOR_DEPTH_8
CONFIG_LV_COLOR_DEPTH_1
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:299`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_COLOR_DEPTH_UNSET`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_UNSET)、[`CONFIG_LV_COLOR_DEPTH_32`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_32)、[`CONFIG_LV_COLOR_DEPTH_24`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_24)、[`CONFIG_LV_COLOR_DEPTH_16`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_16)、[`CONFIG_LV_COLOR_DEPTH_8`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_8)、[`CONFIG_LV_COLOR_DEPTH_1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_1)。

<a id="CONFIG_LV_COLOR_DEPTH_UNSET"></a>

## 15.29 `CONFIG_LV_COLOR_DEPTH_UNSET`

**提示（Prompt）**：使用 `LV_COLOR_FORMAT_DEFAULT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_DEPTH_CHOICE>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:302`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 颜色深度（Color Depth）［已弃用：使用 `LV_COLOR_FORMAT_DEFAULT`］

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_DEPTH_CHOICE`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_CHOICE)。

<a id="CONFIG_LV_COLOR_FORMAT_ARGB8888"></a>

## 15.30 `CONFIG_LV_COLOR_FORMAT_ARGB8888`

**提示（Prompt）**：ARGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:291`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED"></a>

## 15.31 `CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED`

**提示（Prompt）**：ARGB8888，预乘（Premultiplied）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:294`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_FORMAT_DEFAULT"></a>

## 15.32 `CONFIG_LV_COLOR_FORMAT_DEFAULT`

**提示（Prompt）**：默认颜色格式（Default Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_COLOR_FORMAT_I1 if CONFIG_LV_COLOR_DEPTH_1
CONFIG_LV_COLOR_FORMAT_L8 if CONFIG_LV_COLOR_DEPTH_8
CONFIG_LV_COLOR_FORMAT_RGB888 if CONFIG_LV_COLOR_DEPTH_24
CONFIG_LV_COLOR_FORMAT_XRGB8888 if CONFIG_LV_COLOR_DEPTH_32
CONFIG_LV_COLOR_FORMAT_RGB565
```

**可选项（Choices）**

```text
CONFIG_LV_COLOR_FORMAT_I1
CONFIG_LV_COLOR_FORMAT_L8
CONFIG_LV_COLOR_FORMAT_RGB565
CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED
CONFIG_LV_COLOR_FORMAT_RGB888
CONFIG_LV_COLOR_FORMAT_XRGB8888
CONFIG_LV_COLOR_FORMAT_ARGB8888
CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:265`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_COLOR_FORMAT_I1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_I1)、[`CONFIG_LV_COLOR_DEPTH_1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_1)、[`CONFIG_LV_COLOR_FORMAT_L8`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_L8)、[`CONFIG_LV_COLOR_DEPTH_8`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_8)、[`CONFIG_LV_COLOR_FORMAT_RGB888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB888)、[`CONFIG_LV_COLOR_DEPTH_24`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_24)、[`CONFIG_LV_COLOR_FORMAT_XRGB8888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_XRGB8888)、[`CONFIG_LV_COLOR_DEPTH_32`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_DEPTH_32)、[`CONFIG_LV_COLOR_FORMAT_RGB565`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB565)、[`CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED)、[`CONFIG_LV_COLOR_FORMAT_ARGB8888`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_ARGB8888)、[`CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_ARGB8888_PREMULTIPLIED)。

<a id="CONFIG_LV_COLOR_FORMAT_I1"></a>

## 15.33 `CONFIG_LV_COLOR_FORMAT_I1`

**提示（Prompt）**：I1 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_UNSCII_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:273`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_UNSCII_8)。

<a id="CONFIG_LV_COLOR_FORMAT_L8"></a>

## 15.34 `CONFIG_LV_COLOR_FORMAT_L8`

**提示（Prompt）**：L8 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_UNSCII_8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:276`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_UNSCII_8)。

<a id="CONFIG_LV_COLOR_FORMAT_RGB565"></a>

## 15.35 `CONFIG_LV_COLOR_FORMAT_RGB565`

**提示（Prompt）**：RGB565 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:279`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED"></a>

## 15.36 `CONFIG_LV_COLOR_FORMAT_RGB565_SWAPPED`

**提示（Prompt）**：RGB565，大端（Big-endian）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:282`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_FORMAT_RGB888"></a>

## 15.37 `CONFIG_LV_COLOR_FORMAT_RGB888`

**提示（Prompt）**：RGB888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:285`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_FORMAT_XRGB8888"></a>

## 15.38 `CONFIG_LV_COLOR_FORMAT_XRGB8888`

**提示（Prompt）**：XRGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_COLOR_FORMAT_DEFAULT>
```

**弱选择（Implies）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:288`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings） → 默认颜色格式（Default Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_COLOR_FORMAT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_COLOR_FORMAT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_COLOR_MIX_ROUND_OFS"></a>

## 15.39 `CONFIG_LV_COLOR_MIX_ROUND_OFS`

**提示（Prompt）**：颜色混合舍入偏移量（Color Mix Rounding Offset）

**说明（Help）**

`0`：不作调整，取结果的整数部分，即向下舍入（Round Down）。

`64`：从 `x.75` 起向上舍入。

`128`：从半值起向上舍入。

`192`：从 `x.25` 起向上舍入。

`254`：向上舍入（Round Up）。

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
[0, 254]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:329`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 颜色设置（Color Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CONF_MINIMAL"></a>

## 15.40 `CONFIG_LV_CONF_MINIMAL`

**提示（Prompt）**：最小配置（Minimal Configuration）［已弃用：使用最小 defconfig］

**说明（Help）**

已弃用且不再起作用。最小预设（Minimal Preset）现在是 defconfig 文件 `configs/defconfigs/minimal.defconfig`。设置此项不会影响生成的配置，并会触发构建警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3524`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_CONF_SKIP"></a>

## 15.41 `CONFIG_LV_CONF_SKIP`

**提示（Prompt）**：跳过 `lv_conf.h`

**说明（Help）**

不包含 `lv_conf.h`，而从此 Kconfig 树（Kconfig Tree）及内置默认值获取配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3517`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DECEMBER_STR"></a>

## 15.42 `CONFIG_LV_DECEMBER_STR`

**提示（Prompt）**：十二月名称字符串（String for December）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"December"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2056`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEF_REFR_PERIOD"></a>

## 15.43 `CONFIG_LV_DEF_REFR_PERIOD`

**提示（Prompt）**：默认刷新周期（Default Refresh Period，ms）

**说明（Help）**

显示刷新（Display Refresh）、输入设备读取（Input Device Read）和动画步进（Animation Step）的默认周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
33
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:353`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_BENCHMARK_ALIGNED_FONTS"></a>

## 15.44 `CONFIG_LV_DEMO_BENCHMARK_ALIGNED_FONTS`

**提示（Prompt）**：对齐字体（Aligned Fonts）

**说明（Help）**

使用演示自带、字形位图（Glyph Bitmap）经过对齐的 Montserrat 字体，代替 `LV_FONT_MONTSERRAT_*` 字体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_BENCHMARK && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3830`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 基准测试演示（Benchmark Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_BENCHMARK)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_EBIKE_PORTRAIT"></a>

## 15.45 `CONFIG_LV_DEMO_EBIKE_PORTRAIT`

**提示（Prompt）**：纵向布局（Portrait Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_EBIKE && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3904`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 电动自行车演示（E-bike Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_EBIKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_EBIKE)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_MUSIC_AUTO_PLAY"></a>

## 15.46 `CONFIG_LV_DEMO_MUSIC_AUTO_PLAY`

**提示（Prompt）**：自动播放（Auto Play）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_MUSIC && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3866`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 音乐播放器演示（Music Player Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_MUSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_MUSIC)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_MUSIC_LANDSCAPE"></a>

## 15.47 `CONFIG_LV_DEMO_MUSIC_LANDSCAPE`

**提示（Prompt）**：横向布局（Landscape Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_MUSIC && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3854`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 音乐播放器演示（Music Player Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_MUSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_MUSIC)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_MUSIC_LARGE"></a>

## 15.48 `CONFIG_LV_DEMO_MUSIC_LARGE`

**提示（Prompt）**：大型布局（Large Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_MUSIC && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3862`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 音乐播放器演示（Music Player Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_MUSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_MUSIC)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_MUSIC_ROUND"></a>

## 15.49 `CONFIG_LV_DEMO_MUSIC_ROUND`

**提示（Prompt）**：圆形布局（Round Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_MUSIC && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3858`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 音乐播放器演示（Music Player Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_MUSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_MUSIC)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DEMO_MUSIC_SQUARE"></a>

## 15.50 `CONFIG_LV_DEMO_MUSIC_SQUARE`

**提示（Prompt）**：方形布局（Square Layout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DEMO_MUSIC && CONFIG_LV_BUILD_DEMOS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3850`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 演示（Demos） → 构建演示（Demos） → 音乐播放器演示（Music Player Demo）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DEMO_MUSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DEMO_MUSIC)、[`CONFIG_LV_BUILD_DEMOS`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_BUILD_DEMOS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DISABLE_ASSERT_HANDLER_INCLUDE_WARNING"></a>

## 15.51 `CONFIG_LV_DISABLE_ASSERT_HANDLER_INCLUDE_WARNING`

**提示（Prompt）**：禁用 `LV_ASSERT_HANDLER_INCLUDE` 弃用警告（Deprecated Warning）

**说明（Help）**

禁用提示 `LV_ASSERT_HANDLER_INCLUDE` 已弃用（Deprecated）的警告。此设置允许继续使用依赖 `LV_ASSERT_HANDLER_INCLUDE` 的旧版 LVGL，而不触发编译器警告。该选项已被新方式取代：将头文件路径定义为 `LV_ASSERT_CUSTOM_INCLUDE`，并将 `LV_ASSERT_HANDLER` 宏定义放在该头文件中。仅在需要兼容使用 `LV_ASSERT_HANDLER_INCLUDE` 的现有代码且无法立即迁移时启用。新项目应直接使用 `LV_ASSERT_CUSTOM_INCLUDE` 和 `LV_ASSERT_HANDLER`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3615`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build） → 断言（Asserts）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DPI_DEF"></a>

## 15.52 `CONFIG_LV_DPI_DEF`

**提示（Prompt）**：默认每英寸像素数（DPI，px/inch）

**说明（Help）**

用于初始化控件大小（Widget Size）、样式内边距（Style Padding）等默认尺寸。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
130
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:359`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_BUF_ALIGN"></a>

## 15.53 `CONFIG_LV_DRAW_BUF_ALIGN`

**提示（Prompt）**：绘制缓冲区地址对齐（Draw Buffer Address Alignment，字节）

**说明（Help）**

将 `draw_buf` 的起始地址按指定字节数对齐（Align）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:371`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_BUF_STRIDE_ALIGN"></a>

## 15.54 `CONFIG_LV_DRAW_BUF_STRIDE_ALIGN`

**提示（Prompt）**：绘制缓冲区步幅对齐（Draw Buffer Stride Alignment，字节）

**说明（Help）**

将所有图层（Layer）和图像（Image）的步幅（Stride）按指定字节数对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:365`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_DMA2D_HAL_INCLUDE"></a>

## 15.55 `CONFIG_LV_DRAW_DMA2D_HAL_INCLUDE`

**提示（Prompt）**：STM32 HAL 头文件（Header）

**说明（Help）**

声明目标 STM32 系列 DMA2D 硬件抽象层（HAL）API 的头文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_DMA2D && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"stm32h7xx_hal.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:991`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 二维直接存储器访问（DMA2D） → DMA2D 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_DMA2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_DMA2D)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_EVE_EVE_GENERATION"></a>

## 15.56 `CONFIG_LV_DRAW_EVE_EVE_GENERATION`

**提示（Prompt）**：嵌入式视频引擎（EVE）代次

**说明（Help）**

所连接控制器的代次（Generation）：`2` 表示 FT81x，`3` 表示 BT815/BT816，`4` 表示 BT817/BT818。更高代次提供更多命令和寄存器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_EVE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 4]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1045`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 嵌入式视频引擎（EVE） → EVE 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_EVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_EVE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_EVE_WRITE_BUFFER_SIZE"></a>

## 15.57 `CONFIG_LV_DRAW_EVE_WRITE_BUFFER_SIZE`

**提示（Prompt）**：SPI 写缓冲区大小（Write Buffer Size，字节）

**说明（Help）**

每次 SPI 传输之前缓冲的字节数。`0` 禁用缓冲（Buffering），小于 `4` 的值按 `0` 处理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_EVE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1053`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 嵌入式视频引擎（EVE） → EVE 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_EVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_EVE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_LAYER_MAX_MEMORY"></a>

## 15.58 `CONFIG_LV_DRAW_LAYER_MAX_MEMORY`

**提示（Prompt）**：最大图层内存（Maximum Layer Memory，字节）

**说明（Help）**

简单图层（Simple Layer）与变换图层（Transformed Layer）合计的内存上限；`0` 表示不限。必须至少为 `LV_DRAW_LAYER_SIMPLE_BUF_SIZE`；若使用变换图层，还必须足以容纳最大的控件，即 `width x height x 4`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:399`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_LAYER_SIMPLE_BUF_SIZE"></a>

## 15.59 `CONFIG_LV_DRAW_LAYER_SIMPLE_BUF_SIZE`

**提示（Prompt）**：简单图层缓冲区大小（Simple Layer Buffer Size，字节）

**说明（Help）**

对于 `style_opa < 255` 的控件，此处不是指 `bg_opa`、`text_opa` 等属性，或采用非 NORMAL 混合模式（Blend Mode）的控件，会按此大小分块缓冲到“简单图层（Simple Layer）”。设置了 `transform_angle/zoom` 时使用的“变换图层（Transformed Layer）”需要更大的缓冲区，且不能分块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
24576
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:391`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_OPENGLES_TEXTURE_CACHE_COUNT"></a>

## 15.60 `CONFIG_LV_DRAW_OPENGLES_TEXTURE_CACHE_COUNT`

**提示（Prompt）**：纹理缓存大小（Texture Cache Size，条目数）

**说明（Help）**

缓存中保留的纹理（Texture）数量。条目越多，重绘次数越少，但消耗的 GPU 内存越多。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_OPENGLES && CONFIG_LVGL
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1173`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → OpenGL ES 图形 API → OpenGL ES 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_OPENGLES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_ASM_CUSTOM"></a>

## 15.61 `CONFIG_LV_DRAW_SW_ASM_CUSTOM`

**提示（Prompt）**：255：自定义（Custom）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**主动选择（Selects）**

```text
CONFIG_LV_DRAW_SW_ASM_USE_CUSTOM_INCLUDE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:596`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)、[`CONFIG_LV_DRAW_SW_ASM_USE_CUSTOM_INCLUDE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_SW_ASM_USE_CUSTOM_INCLUDE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_SW_ASM_USE_CUSTOM_INCLUDE`。

<a id="CONFIG_LV_DRAW_SW_ASM_CUSTOM_INCLUDE"></a>

## 15.62 `CONFIG_LV_DRAW_SW_ASM_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义汇编包含文件（Custom Assembly Include File）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_SW_ASM_CUSTOM && CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:613`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_SW_ASM_CUSTOM`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_ASM_CUSTOM)、[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_ASM_HELIUM"></a>

## 15.63 `CONFIG_LV_DRAW_SW_ASM_HELIUM`

**提示（Prompt）**：2：Helium 扩展

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:590`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)。

<a id="CONFIG_LV_DRAW_SW_ASM_NEON"></a>

## 15.64 `CONFIG_LV_DRAW_SW_ASM_NEON`

**提示（Prompt）**：1：NEON 扩展

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:588`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)。

<a id="CONFIG_LV_DRAW_SW_ASM_NONE"></a>

## 15.65 `CONFIG_LV_DRAW_SW_ASM_NONE`

**提示（Prompt）**：0：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:586`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)。

<a id="CONFIG_LV_DRAW_SW_ASM_RISCV_V"></a>

## 15.66 `CONFIG_LV_DRAW_SW_ASM_RISCV_V`

**提示（Prompt）**：3：RISC-V 向量扩展（Vector）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:592`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)。

<a id="CONFIG_LV_DRAW_SW_ASM_SVE2"></a>

## 15.67 `CONFIG_LV_DRAW_SW_ASM_SVE2`

**提示（Prompt）**：4：SVE2 扩展

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_USE_DRAW_SW_ASM>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:594`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 软件汇编优化（SW Assembly Optimization）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW_ASM)。

<a id="CONFIG_LV_DRAW_SW_CIRCLE_CACHE_SIZE"></a>

## 15.68 `CONFIG_LV_DRAW_SW_CIRCLE_CACHE_SIZE`

**提示（Prompt）**：圆形缓存大小（Circle Cache Size）

**说明（Help）**

为抗锯齿（Anti-aliasing）缓存四分之一圆的圆周，每个圆消耗 `radius * 4` 字节。设为 `0` 禁用缓存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_SW_COMPLEX && CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:574`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_SW_COMPLEX`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_COMPLEX)、[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_COMPLEX"></a>

## 15.69 `CONFIG_LV_DRAW_SW_COMPLEX`

**提示（Prompt）**：复杂绘制引擎（Complex Draw Engine）

**说明（Help）**

增加圆角（Rounded Corner）、阴影（Shadow）、斜线（Skewed Line）和圆弧（Arc）支持。没有它时，只能绘制带渐变的矩形、图像、文本和直线。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:546`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_DRAW_UNIT_CNT"></a>

## 15.70 `CONFIG_LV_DRAW_SW_DRAW_UNIT_CNT`

**提示（Prompt）**：绘制单元数量（Number of Draw Units）

**说明（Help）**

用于并行渲染一帧的线程（Thread）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:526`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_NONE)、[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_I1_LUM_THRESHOLD"></a>

## 15.71 `CONFIG_LV_DRAW_SW_I1_LUM_THRESHOLD`

**提示（Prompt）**：I1 亮度阈值（Luminance Threshold）

**说明（Help）**

渲染到 I1 时，亮度超过此值的像素（Pixel）将成为有效像素，即对应位被置位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_SW_SUPPORT_I1 && CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
127
```

**取值范围（Ranges）**

```text
[0, 254]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:516`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats） → I1 颜色格式（Color Format）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_SW_SUPPORT_I1`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_SUPPORT_I1)、[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SHADOW_CACHE_SIZE"></a>

## 15.72 `CONFIG_LV_DRAW_SW_SHADOW_CACHE_SIZE`

**提示（Prompt）**：阴影缓存大小（Shadow Cache Size）

**说明（Help）**

要缓冲的最大阴影大小（Shadow Size），其中阴影大小为 `shadow_width + radius`。消耗的 RAM 大小为此值的平方；`0` 禁用缓存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_SW_COMPLEX && CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:566`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_SW_COMPLEX`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_DRAW_SW_COMPLEX)、[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_A8"></a>

## 15.73 `CONFIG_LV_DRAW_SW_SUPPORT_A8`

**提示（Prompt）**：A8 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:508`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_AL88"></a>

## 15.74 `CONFIG_LV_DRAW_SW_SUPPORT_AL88`

**提示（Prompt）**：AL88 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:504`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_ARGB8888"></a>

## 15.75 `CONFIG_LV_DRAW_SW_SUPPORT_ARGB8888`

**提示（Prompt）**：ARGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:492`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_ARGB8888_PREMULTIPLIED"></a>

## 15.76 `CONFIG_LV_DRAW_SW_SUPPORT_ARGB8888_PREMULTIPLIED`

**提示（Prompt）**：预乘 ARGB8888（Premultiplied）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:496`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_I1"></a>

## 15.77 `CONFIG_LV_DRAW_SW_SUPPORT_I1`

**提示（Prompt）**：I1 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:512`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_L8"></a>

## 15.78 `CONFIG_LV_DRAW_SW_SUPPORT_L8`

**提示（Prompt）**：L8 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:500`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_RGB565"></a>

## 15.79 `CONFIG_LV_DRAW_SW_SUPPORT_RGB565`

**提示（Prompt）**：RGB565 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:472`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_RGB565A8"></a>

## 15.80 `CONFIG_LV_DRAW_SW_SUPPORT_RGB565A8`

**提示（Prompt）**：RGB565A8 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:480`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_RGB565_SWAPPED"></a>

## 15.81 `CONFIG_LV_DRAW_SW_SUPPORT_RGB565_SWAPPED`

**提示（Prompt）**：字节交换的 RGB565（Swapped）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:476`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_RGB888"></a>

## 15.82 `CONFIG_LV_DRAW_SW_SUPPORT_RGB888`

**提示（Prompt）**：RGB888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:484`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_SW_SUPPORT_XRGB8888"></a>

## 15.83 `CONFIG_LV_DRAW_SW_SUPPORT_XRGB8888`

**提示（Prompt）**：XRGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:488`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer） → 支持的颜色格式（Supported Color Formats）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_THREAD_PRIO"></a>

## 15.84 `CONFIG_LV_DRAW_THREAD_PRIO`

**提示（Prompt）**：绘制线程优先级（Draw Thread Priority）

**说明（Help）**

线程优先级（Thread Priority）控制绘制线程的相对重要程度，数值对应 `lv_os.h` 中的 `lv_thread_prio_t` 枚举：

- `0`：`LV_THREAD_PRIO_LOWEST`。
- `1`：`LV_THREAD_PRIO_LOW`。
- `2`：`LV_THREAD_PRIO_MID`，默认值。
- `3`：`LV_THREAD_PRIO_HIGH`。
- `4`：`LV_THREAD_PRIO_HIGHEST`。

提高优先级可改善渲染性能，但可能使低优先级任务发生饥饿（Starvation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:414`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_NONE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_THREAD_STACK_SIZE"></a>

## 15.85 `CONFIG_LV_DRAW_THREAD_STACK_SIZE`

**提示（Prompt）**：绘制线程栈大小（Draw Thread Stack Size，字节）

**说明（Help）**

如果启用 FreeType 或 ThorVG，建议将此值设为 32 KB 或更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:407`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_OS_NONE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_DRAW_TRANSFORM_USE_MATRIX"></a>

## 15.86 `CONFIG_LV_DRAW_TRANSFORM_USE_MATRIX`

**提示（Prompt）**：基于矩阵的变换（Matrix-based Transformations）

**说明（Help）**

渲染引擎（Rendering Engine）必须支持 3×3 矩阵变换（Matrix Transformation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_MATRIX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:384`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 矩阵（Matrix）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_MATRIX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_ENABLE_GLOBAL_CUSTOM"></a>

## 15.87 `CONFIG_LV_ENABLE_GLOBAL_CUSTOM`

**提示（Prompt）**：自定义 `lv_global`（Customization）

**说明（Help）**

默认情况下，LVGL 将所有运行时状态（Runtime State）存储在单个静态 `lv_global_t` 变量中，这足以满足大多数单显示器、单线程应用。如果需要在同一进程中运行多个独立的 LVGL 实例，请启用此选项，例如：

- 多个物理显示器，分别具有独立渲染循环（Render Loop）。
- 实时操作系统（RTOS，例如 FreeRTOS、Zephyr 等）中各线程独立的 LVGL 上下文（Context）。
- 可热插拔或沙箱隔离的用户界面实例（UI Instance）。

启用后，LVGL 内部对全局状态的每次访问都通过 `LV_GLOBAL_CUSTOM()`，而不使用静态变量。必须实现 `lv_global_t *lv_global_default(void)`，返回当前上下文的正确实例，例如通过线程局部存储（Thread-local Storage）或受保护的指针切换实现。从该函数返回 `NULL` 是安全的；LVGL 会将此上下文中的库视为尚未初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3539`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FEBRUARY_STR"></a>

## 15.88 `CONFIG_LV_FEBRUARY_STR`

**提示（Prompt）**：二月名称字符串（String for February）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"February"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2026`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 月份名称配置（Month Names Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FFMPEG_DUMP_FORMAT"></a>

## 15.89 `CONFIG_LV_FFMPEG_DUMP_FORMAT`

**提示（Prompt）**：输出格式信息（Dump Format）

**说明（Help）**

将输入流信息打印到标准错误（stderr），并保持 FFmpeg 日志启用；否则会关闭其日志输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FFMPEG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2104`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → FFmpeg 播放器（Player）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FFMPEG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FFMPEG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FFMPEG_PLAYER_USE_LV_FS"></a>

## 15.90 `CONFIG_LV_FFMPEG_PLAYER_USE_LV_FS`

**提示（Prompt）**：播放器中的 LVGL 文件系统路径（File System Paths）

**说明（Help）**

启用后将无法再打开 URL。无论此选项如何设置，FFmpeg 图像解码器（Image Decoder）始终使用 LVGL 文件系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FFMPEG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2111`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → FFmpeg 播放器（Player）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FFMPEG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FFMPEG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FILE_EXPLORER_PATH_MAX_LEN"></a>

## 15.91 `CONFIG_LV_FILE_EXPLORER_PATH_MAX_LEN`

**提示（Prompt）**：最大路径长度（Maximum Path Length，字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FILE_EXPLORER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3491`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 其他（Others） → 文件浏览器（File Explorer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FILE_EXPLORER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FILE_EXPLORER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FILE_EXPLORER_QUICK_ACCESS"></a>

## 15.92 `CONFIG_LV_FILE_EXPLORER_QUICK_ACCESS`

**提示（Prompt）**：快速访问栏（Quick Access Bar）

**说明（Help）**

添加侧边栏（Sidebar），提供常用位置的快捷入口。点击浏览区域左上角的按钮可隐藏该栏，这对小屏幕很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_FILE_EXPLORER && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3495`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 其他（Others） → 文件浏览器（File Explorer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_FILE_EXPLORER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_FILE_EXPLORER)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FONT_CUSTOM_INCLUDE"></a>

## 15.93 `CONFIG_LV_FONT_CUSTOM_INCLUDE`

**提示（Prompt）**：自定义字体声明头文件路径（Custom Font Declaration Header Path）

**说明（Help）**

可选头文件，用于覆盖字体（Font）相关的宏。典型用途是通过 `LV_FONT_CUSTOM_DECLARE` 声明额外字体：

```c
#define LV_FONT_CUSTOM_DECLARE  LV_FONT_DECLARE(my_font_24)
```

也可以将默认字体覆盖为自定义字体：

```c
#define LV_FONT_DEFAULT         &my_font_24
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_FONT_USE_CUSTOM_INCLUDE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1741`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 自定义字体声明头文件（Custom Font Declaration Header）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_USE_CUSTOM_INCLUDE`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_USE_CUSTOM_INCLUDE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_FONT_DEFAULT"></a>

## 15.94 `CONFIG_LV_FONT_DEFAULT`

**提示（Prompt）**：默认字体（Default Font）

**说明（Help）**

主题（Theme）和未显式指定字体的控件（Widget）使用的字体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_CUSTOM_FONT_DEFAULT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14
```

**可选项（Choices）**

```text
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48
CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED
CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW
CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK
CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK
CONFIG_LV_FONT_DEFAULT_UNSCII_8
CONFIG_LV_FONT_DEFAULT_UNSCII_16
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1771`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CUSTOM_FONT_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_CUSTOM_FONT_DEFAULT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_8)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_20)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_22)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_24)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_26)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_30)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_32)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_34)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_36)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_38)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_40)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_42)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_44)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_46)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_48)、[`CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_MONTSERRAT_28_COMPRESSED)、[`CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW)、[`CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_14_CJK)、[`CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_SOURCE_HAN_SANS_SC_16_CJK)、[`CONFIG_LV_FONT_DEFAULT_UNSCII_8`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_UNSCII_8)、[`CONFIG_LV_FONT_DEFAULT_UNSCII_16`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEFAULT_UNSCII_16)。

<a id="CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW"></a>

## 15.95 `CONFIG_LV_FONT_DEFAULT_DEJAVU_16_PERSIAN_HEBREW`

**提示（Prompt）**：Dejavu 16 字体（波斯文 Persian、希伯来文 Hebrew、阿拉伯文 Arabic）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_DEJAVU_16_PERSIAN_HEBREW
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1844`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_DEJAVU_16_PERSIAN_HEBREW`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_DEJAVU_16_PERSIAN_HEBREW)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10"></a>

## 15.96 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_10`

**提示（Prompt）**：Montserrat 10 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_10
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1781`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_10`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_10)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12"></a>

## 15.97 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_12`

**提示（Prompt）**：Montserrat 12 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_12
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1784`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_12`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_12)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14"></a>

## 15.98 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_14`

**提示（Prompt）**：Montserrat 14 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_14
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1787`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_14`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_14)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16"></a>

## 15.99 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_16`

**提示（Prompt）**：Montserrat 16 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_16
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1790`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_16`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_16)。

<a id="CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18"></a>

## 15.100 `CONFIG_LV_FONT_DEFAULT_MONTSERRAT_18`

**提示（Prompt）**：Montserrat 18 字体（Font）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_FONT_DEFAULT>
```

**主动选择（Selects）**

```text
CONFIG_LV_FONT_MONTSERRAT_18
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1793`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings） → 默认字体（Default Font）

**配置项引用（Symbol References）**：[`CONFIG_LV_FONT_DEFAULT`](P015_module_lvgl_zephyr_配置项参考_1.md#CONFIG_LV_FONT_DEFAULT)、[`CONFIG_LV_FONT_MONTSERRAT_18`](P016_module_lvgl_zephyr_配置项参考_2.md#CONFIG_LV_FONT_MONTSERRAT_18)。

<!-- kconfig-navigation -->

[上一章](P014_module_hal_realtek_bee_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P016_module_lvgl_zephyr_配置项参考_2.md)
