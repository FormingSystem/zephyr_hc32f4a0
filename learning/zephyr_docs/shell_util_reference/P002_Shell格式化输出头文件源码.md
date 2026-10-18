---
id: learning.zephyr-docs.shell-util-reference.page-2
title: Shell格式化输出头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__fprintf_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Shell格式化输出头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__fprintf_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P001_Shell格式化输出头文件参考.md)和[公共接口](P001_Shell格式化输出头文件参考.md)；访问语义和生命周期见本页译注。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__shell__api_html_ga1fd1671311b112f0c87ab2dafd801105"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdio_8h_html_a610723ed7ffdf7b802f6093d45ffa09d"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_FPRINTF_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_FPRINTF_H_
<a id="l00014"></a>
<a id="l00015"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00016"></a>#include &lt;stdbool.h&gt;
<a id="l00017"></a>#include &lt;stddef.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>typedef void (*shell_fprintf_fwrite)(const void *user_ctx,
<a id="l00026"></a>                                     const char *data,
<a id="l00027"></a>                                     size_t length);
<a id="l00028"></a>
<a id="l00029"></a>struct shell_fprintf_control_block {
<a id="l00030"></a>        size_t buffer_cnt;
<a id="l00031"></a>        bool autoflush;
<a id="l00032"></a>};
<a id="l00036"></a>struct shell_fprintf {
<a id="l00037"></a>        uint8_t *buffer;
<a id="l00038"></a>        size_t buffer_size;
<a id="l00039"></a>        shell_fprintf_fwrite fwrite;
<a id="l00040"></a>        const void *user_ctx;
<a id="l00041"></a>        struct shell_fprintf_control_block *ctrl_blk;
<a id="l00042"></a>};
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00056"></a>#define Z_SHELL_FPRINTF_DEFINE(_name, _user_ctx, _buf, _size,   \
<a id="l00057"></a>                            _autoflush, _fwrite)                \
<a id="l00058"></a>        static struct shell_fprintf_control_block               \
<a id="l00059"></a>                                _name##_shell_fprintf_ctx = {   \
<a id="l00060"></a>                .autoflush = _autoflush,                        \
<a id="l00061"></a>                .buffer_cnt = 0                                 \
<a id="l00062"></a>        };                                                      \
<a id="l00063"></a>        static const struct shell_fprintf _name = {             \
<a id="l00064"></a>                .buffer = _buf,                                 \
<a id="l00065"></a>                .buffer_size = _size,                           \
<a id="l00066"></a>                .fwrite = _fwrite,                              \
<a id="l00067"></a>                .user_ctx = _user_ctx,                          \
<a id="l00068"></a>                .ctrl_blk = &amp;_name##_shell_fprintf_ctx          \
<a id="l00069"></a>        }
<a id="l00070"></a>
<a id="l00078"></a>void z_shell_fprintf_fmt(const struct shell_fprintf *sh_fprintf,
<a id="l00079"></a>                         char const *fmt, va_list args);
<a id="l00080"></a>
<a id="l00087"></a>void z_shell_cbpprintf_fmt(const struct shell_fprintf *sh_fprintf, void *package);
<a id="l00088"></a>
<a id="l00094"></a>void z_shell_fprintf_buffer_flush(const struct shell_fprintf *sh_fprintf);
<a id="l00095"></a>
<a id="l00096"></a>#ifdef __cplusplus
<a id="l00097"></a>}
<a id="l00098"></a>#endif
<a id="l00099"></a>
<a id="l00100"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_FPRINTF_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_FPRINTF_H_头文件包含保护结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `shell_fprintf`

```c
#define shell_fprintf(sh, color, fmt,...)
```

类似printf的函数，向Shell发送格式化数据流（Formatted Data Stream）。

定义位置（Definition）：shell.h:1303。

符号定位：[shell_fprintf](../shell_core_reference/P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `fwrite`

```c
size_t fwrite(const void *ZRESTRICT ptr, size_t size, size_t nitems, FILE *ZRESTRICT stream)
```

符号定位：[fwrite](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html#a610723ed7ffdf7b802f6093d45ffa09d)。

## 2.4\_源码跟踪译注

> 译注——格式化辅助函数的参考页没有列出内部z_shell_*接口详细说明；源码页仍完整保留它们的可见声明、宏和控制结构。输出缓冲区与用户上下文由调用方提供，不由DEFINE宏复制其内容。

> 译注——当前flush调用fwrite传出已有缓冲内容，随后把buffer_cnt清零。fwrite回调返回void，不能从这次刷新推断串口、网络或远端终端已确认接收。autoflush控制一次格式化结束后的刷新，缓冲区满时也会刷新。

头文件定位：[include/zephyr/shell/shell_fprintf.h](../../../include/zephyr/shell/shell_fprintf.h)，关联实现／接口：[subsys/shell/shell_fprintf.c](../../../subsys/shell/shell_fprintf.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_fprintf.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_fprintf.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_Shell格式化输出头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [shell_fprintf](../shell_core_reference/P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fwrite](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html#a610723ed7ffdf7b802f6093d45ffa09d)

---

[上一章](P001_Shell格式化输出头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_Shell命令历史头文件参考.md)
