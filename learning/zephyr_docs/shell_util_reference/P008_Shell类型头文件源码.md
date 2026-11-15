---
id: learning.zephyr-docs.shell-util-reference.page-8
title: Shell类型头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__types_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Shell类型头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__types_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P007_Shell类型头文件参考.md)和[公共接口](P007_Shell类型头文件参考.md)；访问语义和生命周期见本页译注。

## 8.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00027"></a>
<a id="agroup__shell__api_html_ga6dcf569be711db32286fb1ef2dcf36d2"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d"></a>
<a id="agroup__shell__api_html_gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_TYPES_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_TYPES_H_
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>#ifdef __cplusplus
<a id="l00018"></a>extern "C" {
<a id="l00019"></a>#endif
<a id="l00020"></a>
<a id="l00025"></a>
<a id="l00027"></a>enum shell_vt100_color {
<a id="l00028"></a>        SHELL_VT100_COLOR_BLACK,
<a id="l00029"></a>        SHELL_VT100_COLOR_RED,
<a id="l00030"></a>        SHELL_VT100_COLOR_GREEN,
<a id="l00031"></a>        SHELL_VT100_COLOR_YELLOW,
<a id="l00032"></a>        SHELL_VT100_COLOR_BLUE,
<a id="l00033"></a>        SHELL_VT100_COLOR_MAGENTA,
<a id="l00034"></a>        SHELL_VT100_COLOR_CYAN,
<a id="l00035"></a>        SHELL_VT100_COLOR_WHITE,
<a id="l00036"></a>
<a id="l00037"></a>        SHELL_VT100_COLOR_DEFAULT,
<a id="l00038"></a>
<a id="l00040"></a>        VT100_COLOR_END
<a id="l00042"></a>};
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>struct shell_vt100_colors {
<a id="l00049"></a>        enum shell_vt100_color col;
<a id="l00050"></a>        enum shell_vt100_color bgcol;
<a id="l00051"></a>};
<a id="l00052"></a>
<a id="l00053"></a>struct shell_multiline_cons {
<a id="l00054"></a>        uint16_t cur_x;
<a id="l00055"></a>        uint16_t cur_x_end;
<a id="l00056"></a>        uint16_t cur_y;
<a id="l00057"></a>        uint16_t cur_y_end;
<a id="l00058"></a>        uint16_t terminal_hei;
<a id="l00059"></a>        uint16_t terminal_wid;
<a id="l00060"></a>        uint8_t name_len;
<a id="l00061"></a>};
<a id="l00062"></a>
<a id="l00063"></a>struct shell_vt100_ctx {
<a id="l00064"></a>        struct shell_multiline_cons cons;
<a id="l00065"></a>        struct shell_vt100_colors col;
<a id="l00066"></a>        uint16_t printed_cmd;
<a id="l00067"></a>};
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>#ifdef __cplusplus
<a id="l00072"></a>}
<a id="l00073"></a>#endif
<a id="l00074"></a>
<a id="l00075"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_TYPES_H_ */
</code></pre>

## 8.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_TYPES_H_头文件包含保护结束。

## 8.3\_原页符号提示（Symbol Descriptions）

### `shell_vt100_color`

```c
shell_vt100_color
```

Shell输出可用的文本颜色（Text Colors）。

定义位置（Definition）：shell_types.h:27。

符号定位：[shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

### `SHELL_VT100_COLOR_WHITE`

```c
@ SHELL_VT100_COLOR_WHITE
```

白色（White）。

定义位置（Definition）：shell_types.h:35。

符号定位：[SHELL_VT100_COLOR_WHITE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c)。

### `SHELL_VT100_COLOR_DEFAULT`

```c
@ SHELL_VT100_COLOR_DEFAULT
```

终端默认前景色（Default Foreground Color）。

定义位置（Definition）：shell_types.h:37。

符号定位：[SHELL_VT100_COLOR_DEFAULT](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)。

### `SHELL_VT100_COLOR_BLACK`

```c
@ SHELL_VT100_COLOR_BLACK
```

黑色（Black）。

定义位置（Definition）：shell_types.h:28。

符号定位：[SHELL_VT100_COLOR_BLACK](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6)。

### `SHELL_VT100_COLOR_CYAN`

```c
@ SHELL_VT100_COLOR_CYAN
```

青色（Cyan）。

定义位置（Definition）：shell_types.h:34。

符号定位：[SHELL_VT100_COLOR_CYAN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)。

### `SHELL_VT100_COLOR_RED`

```c
@ SHELL_VT100_COLOR_RED
```

红色（Red）。

定义位置（Definition）：shell_types.h:29。

符号定位：[SHELL_VT100_COLOR_RED](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)。

### `SHELL_VT100_COLOR_MAGENTA`

```c
@ SHELL_VT100_COLOR_MAGENTA
```

品红色（Magenta）。

定义位置（Definition）：shell_types.h:33。

符号定位：[SHELL_VT100_COLOR_MAGENTA](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a)。

### `SHELL_VT100_COLOR_GREEN`

```c
@ SHELL_VT100_COLOR_GREEN
```

绿色（Green）。

定义位置（Definition）：shell_types.h:30。

符号定位：[SHELL_VT100_COLOR_GREEN](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)。

### `SHELL_VT100_COLOR_BLUE`

```c
@ SHELL_VT100_COLOR_BLUE
```

蓝色（Blue）。

定义位置（Definition）：shell_types.h:32。

符号定位：[SHELL_VT100_COLOR_BLUE](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d)。

### `SHELL_VT100_COLOR_YELLOW`

```c
@ SHELL_VT100_COLOR_YELLOW
```

黄色（Yellow）。

定义位置（Definition）：shell_types.h:31。

符号定位：[SHELL_VT100_COLOR_YELLOW](../shell_core_reference/P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

## 8.4\_源码跟踪译注

> 译注——shell_vt100_color是终端文本颜色枚举，包含默认前景色（Default Foreground Color）；它不是RGB像素值数组。源码页还显示颜色上下文和多行编辑光标状态等内部结构，公共参考页只列出原文公开的类型。

头文件定位：[include/zephyr/shell/shell_types.h](../../../include/zephyr/shell/shell_types.h)，关联实现／接口：[include/zephyr/shell/shell_types.h](../../../include/zephyr/shell/shell_types.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_types.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_types.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 8.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P007_Shell类型头文件参考.md)
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
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

---

[上一章](P007_Shell类型头文件参考.md) · [返回大纲](大纲.md)
