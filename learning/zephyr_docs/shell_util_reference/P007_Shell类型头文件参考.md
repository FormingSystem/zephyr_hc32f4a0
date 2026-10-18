---
id: learning.zephyr-docs.shell-util-reference.page-7
title: Shell类型头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Shell类型头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__types_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell格式化输出、命令历史、字符串转换和终端类型的参考与源码。源码跟踪译注与官方原文分开标示。

Shell终端类型与颜色（Terminal Types and Colors）的头文件。

查看此文件的源码。

<a id="details"></a>

Shell终端类型与颜色（Terminal Types and Colors）的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.1\_枚举（Enumerations）

<a id="r_ga6dcf569be711db32286fb1ef2dcf36d2"></a>

```c
enum shell_vt100_color { SHELL_VT100_COLOR_BLACK , SHELL_VT100_COLOR_RED , SHELL_VT100_COLOR_GREEN , SHELL_VT100_COLOR_YELLOW , SHELL_VT100_COLOR_BLUE , SHELL_VT100_COLOR_MAGENTA , SHELL_VT100_COLOR_CYAN , SHELL_VT100_COLOR_WHITE , SHELL_VT100_COLOR_DEFAULT }
```

相关声明：[shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)、[SHELL_VT100_COLOR_BLACK](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6)、[SHELL_VT100_COLOR_RED](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)、[SHELL_VT100_COLOR_GREEN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)、[SHELL_VT100_COLOR_YELLOW](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)、[SHELL_VT100_COLOR_BLUE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d)、[SHELL_VT100_COLOR_MAGENTA](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a)、[SHELL_VT100_COLOR_CYAN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)、[SHELL_VT100_COLOR_WHITE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c)、[SHELL_VT100_COLOR_DEFAULT](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)。

Shell输出可用的文本颜色（Text Colors）。

## 7.2\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_types.h](../../../include/zephyr/shell/shell_types.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：shell_vt100_color是终端文本颜色枚举，包含默认前景色（Default Foreground Color）；它不是RGB像素值数组。源码页还显示颜色上下文和多行编辑光标状态等内部结构，公共参考页只列出原文公开的类型。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P008_Shell类型头文件源码.md)
- [shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)
- [SHELL_VT100_COLOR_BLACK](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6)
- [SHELL_VT100_COLOR_RED](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)
- [SHELL_VT100_COLOR_GREEN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)
- [SHELL_VT100_COLOR_YELLOW](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)
- [SHELL_VT100_COLOR_BLUE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d)
- [SHELL_VT100_COLOR_MAGENTA](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a)
- [SHELL_VT100_COLOR_CYAN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)
- [SHELL_VT100_COLOR_WHITE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c)
- [SHELL_VT100_COLOR_DEFAULT](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)

<a id="header-details"></a>

---

[上一章](P006_Shell字符串转换头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_Shell类型头文件源码.md)
