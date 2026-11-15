---
id: learning.zephyr-docs.shell-util-reference.page-5
title: Shell字符串转换头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__string__conv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Shell字符串转换头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__string__conv_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell格式化输出、命令历史、字符串转换和终端类型的参考与源码。源码跟踪译注与官方原文分开标示。

Shell字符串转换辅助函数（String Conversion Helpers）的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
```

查看此文件的源码。

Shell字符串转换辅助函数（String Conversion Helpers）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga2a3fc802d8a4d13e49024ee5546d62a6"></a>

```c
long shell_strtol (const char *str, int base, int *err)
```

相关声明：[shell_strtol](../shell_core_reference/P001_Shell核心接口.md#ga2a3fc802d8a4d13e49024ee5546d62a6)。

将字符串转换为long，并检查错误（Error Check）。

<a id="r_gac7928525a22e053d1dea44995c8198b9"></a>

```c
unsigned long shell_strtoul (const char *str, int base, int *err)
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[shell_strtoul](../shell_core_reference/P001_Shell核心接口.md#gac7928525a22e053d1dea44995c8198b9)。

将字符串转换为unsigned long，并检查错误（Error Check）。

<a id="r_ga635c05cc9a2e84b6438402334587d537"></a>

```c
unsigned long long shell_strtoull (const char *str, int base, int *err)
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[shell_strtoull](../shell_core_reference/P001_Shell核心接口.md#ga635c05cc9a2e84b6438402334587d537)。

将字符串转换为unsigned long long，并检查错误（Error Check）。

<a id="r_gaabc3fbdfdc2c3cbd4cd41dc97309aea4"></a>

```c
bool shell_strtobool (const char *str, int base, int *err)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_strtobool](../shell_core_reference/P001_Shell核心接口.md#gaabc3fbdfdc2c3cbd4cd41dc97309aea4)。

将字符串转换为布尔值（Boolean），并检查错误。

## 5.2\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_string_conv.h](../../../include/zephyr/shell/shell_string_conv.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：原始头文件规定err在成功时保持原值，应由调用方预先初始化为0。当前转换函数发生错误返回0或false，并通过err提供-EINVAL或-ERANGE；零本身也可能是有效结果，判断时需同时查看err。

> 译注——源码核对：当前布尔转换精确匹配小写on、enable、true以及off、disable、false；其他文本交给无符号整数转换，非零数转为true。它不是对任意大小写文本进行宽松匹配的函数。

> 译注——源码核对：数值转换检查是否实际读取了字符以及结尾是否还有未消费字符。无符号版本首先拒绝首字符为减号的输入；不要把这个具体判断扩大解释为自行实现了所有字符形式的负号规范化。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.3\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码](P006_Shell字符串转换头文件源码.md)
- [shell_strtol](../shell_core_reference/P001_Shell核心接口.md#ga2a3fc802d8a4d13e49024ee5546d62a6)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [shell_strtoul](../shell_core_reference/P001_Shell核心接口.md#gac7928525a22e053d1dea44995c8198b9)
- [shell_strtoull](../shell_core_reference/P001_Shell核心接口.md#ga635c05cc9a2e84b6438402334587d537)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [shell_strtobool](../shell_core_reference/P001_Shell核心接口.md#gaabc3fbdfdc2c3cbd4cd41dc97309aea4)

<a id="header-details"></a>

---

[上一章](P004_Shell命令历史头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_Shell字符串转换头文件源码.md)
