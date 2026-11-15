---
id: learning.zephyr-docs.shell-util-reference.page-6
title: Shell字符串转换头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__string__conv_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell字符串转换头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__string__conv_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P005_Shell字符串转换头文件参考.md)和[公共接口](P005_Shell字符串转换头文件参考.md)；访问语义和生命周期见本页译注。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__shell__api_html_ga2a3fc802d8a4d13e49024ee5546d62a6"></a>
<a id="agroup__shell__api_html_ga635c05cc9a2e84b6438402334587d537"></a>
<a id="agroup__shell__api_html_gaabc3fbdfdc2c3cbd4cd41dc97309aea4"></a>
<a id="agroup__shell__api_html_gac7928525a22e053d1dea44995c8198b9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2022 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_STRING_CONV_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_STRING_CONV_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;stdbool.h&gt;
<a id="l00017"></a>#include &lt;stdint.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00027"></a>
<a id="l00043"></a>long shell_strtol(const char *str, int base, int *err);
<a id="l00044"></a>
<a id="l00060"></a>unsigned long shell_strtoul(const char *str, int base, int *err);
<a id="l00061"></a>
<a id="l00077"></a>unsigned long long shell_strtoull(const char *str, int base, int *err);
<a id="l00078"></a>
<a id="l00094"></a>bool shell_strtobool(const char *str, int base, int *err);
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>#ifdef __cplusplus
<a id="l00099"></a>}
<a id="l00100"></a>#endif
<a id="l00101"></a>
<a id="l00102"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_STRING_CONV_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2022 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_STRING_CONV_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `shell_strtol`

```c
long shell_strtol(const char *str, int base, int *err)
```

将字符串转换为long，并检查错误（Error Check）。

符号定位：[shell_strtol](../shell_core_reference/P001_Shell核心接口.md#ga2a3fc802d8a4d13e49024ee5546d62a6)。

### `shell_strtoull`

```c
unsigned long long shell_strtoull(const char *str, int base, int *err)
```

将字符串转换为unsigned long long，并检查错误（Error Check）。

符号定位：[shell_strtoull](../shell_core_reference/P001_Shell核心接口.md#ga635c05cc9a2e84b6438402334587d537)。

### `shell_strtobool`

```c
bool shell_strtobool(const char *str, int base, int *err)
```

将字符串转换为布尔值（Boolean），并检查错误。

符号定位：[shell_strtobool](../shell_core_reference/P001_Shell核心接口.md#gaabc3fbdfdc2c3cbd4cd41dc97309aea4)。

### `shell_strtoul`

```c
unsigned long shell_strtoul(const char *str, int base, int *err)
```

将字符串转换为unsigned long，并检查错误（Error Check）。

符号定位：[shell_strtoul](../shell_core_reference/P001_Shell核心接口.md#gac7928525a22e053d1dea44995c8198b9)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

## 6.4\_源码跟踪译注

> 译注——原始头文件规定err在成功时保持原值，应由调用方预先初始化为0。当前转换函数发生错误返回0或false，并通过err提供-EINVAL或-ERANGE；零本身也可能是有效结果，判断时需同时查看err。

> 译注——当前布尔转换精确匹配小写on、enable、true以及off、disable、false；其他文本交给无符号整数转换，非零数转为true。它不是对任意大小写文本进行宽松匹配的函数。

> 译注——数值转换检查是否实际读取了字符以及结尾是否还有未消费字符。无符号版本首先拒绝首字符为减号的输入；不要把这个具体判断扩大解释为自行实现了所有字符形式的负号规范化。

头文件定位：[include/zephyr/shell/shell_string_conv.h](../../../include/zephyr/shell/shell_string_conv.h)，关联实现／接口：[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_string_conv.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_utils.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_Shell字符串转换头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [shell_strtol](../shell_core_reference/P001_Shell核心接口.md#ga2a3fc802d8a4d13e49024ee5546d62a6)
- [shell_strtoul](../shell_core_reference/P001_Shell核心接口.md#gac7928525a22e053d1dea44995c8198b9)
- [shell_strtoull](../shell_core_reference/P001_Shell核心接口.md#ga635c05cc9a2e84b6438402334587d537)
- [shell_strtobool](../shell_core_reference/P001_Shell核心接口.md#gaabc3fbdfdc2c3cbd4cd41dc97309aea4)

---

[上一章](P005_Shell字符串转换头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_Shell类型头文件参考.md)
