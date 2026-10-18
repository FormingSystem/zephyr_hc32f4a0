---
id: learning.zephyr-docs.shell-remote-reference.page-5
title: 远端Shell命令行头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__cli_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_远端Shell命令行头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__cli_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P004_远端Shell命令行头文件参考.md)和[公共接口](P004_远端Shell命令行头文件参考.md)；访问语义和生命周期见本页译注。

## 5.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00051"></a>
<a id="acbprintf_8h_html"></a>
<a id="agroup__shell__api_html_ga6dcf569be711db32286fb1ef2dcf36d2"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="ashell__remote__cli_8h_html_a60806c208a7a319faf4f9467e4d55946"></a>
<a id="ashell__remote__cli_8h_html_a851c444b07279f370d3a62ab6ce71d3d"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2026 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_CLI_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_CLI_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/sys/cbprintf.h&gt;
<a id="l00017"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00031"></a>void shell_remote_cli_cbpprintf(const struct shell *sh, enum shell_vt100_color color, void *package,
<a id="l00032"></a>                                size_t len);
<a id="l00033"></a>
<a id="l00037"></a>void shell_remote_cmd_process(void);
<a id="l00038"></a>
<a id="l00040"></a>#define SHELL_REMOTE_CLI_ALIGN sizeof(long long)
<a id="l00041"></a>
<a id="l00051"></a>#define SHELL_REMOTE_CLI_FPRINTF(_sh, _color, ...)                                                 \
<a id="l00052"></a>        do {                                                                                       \
<a id="l00053"></a>                int _plen;                                                                         \
<a id="l00054"></a>                void *_pkg;                                                                        \
<a id="l00055"></a>                uint32_t _options =                                                                \
<a id="l00056"></a>                        CBPRINTF_PACKAGE_ADD_RO_STR_POS | CBPRINTF_PACKAGE_ADD_RW_STR_POS;         \
<a id="l00057"></a>                CBPRINTF_STATIC_PACKAGE(NULL, 0, _plen, SHELL_REMOTE_CLI_ALIGN, _options,          \
<a id="l00058"></a>                                        __VA_ARGS__);                                              \
<a id="l00059"></a>                _pkg = __builtin_alloca_with_align(_plen, 8);                                      \
<a id="l00060"></a>                CBPRINTF_STATIC_PACKAGE(_pkg, _plen, _plen, SHELL_REMOTE_CLI_ALIGN, _options,      \
<a id="l00061"></a>                                        __VA_ARGS__);                                              \
<a id="l00062"></a>                shell_remote_cli_cbpprintf(_sh, _color, _pkg, _plen);                              \
<a id="l00063"></a>        } while (0)
<a id="l00064"></a>
<a id="l00065"></a>#ifdef __cplusplus
<a id="l00066"></a>}
<a id="l00067"></a>#endif
<a id="l00068"></a>
<a id="l00069"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_CLI_H_ */
</code></pre>

## 5.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2026 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_CLI_H_头文件包含保护结束。

## 5.3\_原页符号提示（Symbol Descriptions）

### `cbprintf.h`

符号定位：[cbprintf.h](../cbprintf_reference/P005_回调格式化输出头文件参考.md)。

### `shell_vt100_color`

```c
shell_vt100_color
```

Shell输出可用的文本颜色（Text Colors）。

定义位置（Definition）：shell_types.h:27。

符号定位：[shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `shell_remote_cli_cbpprintf`

```c
void shell_remote_cli_cbpprintf(const struct shell *sh, enum shell_vt100_color color, void *package, size_t len)
```

向远端Shell打印格式化字符串（Formatted String）。

符号定位：[shell_remote_cli_cbpprintf](P004_远端Shell命令行头文件参考.md#a60806c208a7a319faf4f9467e4d55946)。

### `shell_remote_cmd_process`

```c
void shell_remote_cmd_process(void)
```

禁用CONFIG_MULTITHREADING时，在主执行上下文（Main Context）中处理远端消息。

符号定位：[shell_remote_cmd_process](P004_远端Shell命令行头文件参考.md#a851c444b07279f370d3a62ab6ce71d3d)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 5.4\_源码跟踪译注

> 译注——FPRINTF宏先计算包大小，在当前栈上分配空间，再静态打包并同步调用cbpprintf。包内字符串的转换与复制在发送实现中处理；不能从临时包地址推导出它可在宏结束后长期保存。

> 译注——SHELL_REMOTE_CLI_ALIGN定义为sizeof(long long)，而__builtin_alloca_with_align调用中的8是编译器内建函数的对齐参数，单位为位，见[GCC栈分配内建函数说明](https://gcc.gnu.org/onlinedocs/gcc/Stack-Allocation.html)。原始宏保留，不能将这个8直接解释为8字节对齐保证。

> 译注——禁用多线程时，shell_remote_cmd_process用于从主执行上下文处理暂存消息。启用多线程时，当前实现按配置使用工作项或专用线程；调用者应遵守接口的配置条件。

头文件定位：[include/zephyr/shell/shell_remote_cli.h](../../../include/zephyr/shell/shell_remote_cli.h)，关联实现／接口：[subsys/shell/shell_remote_cli.c](../../../subsys/shell/shell_remote_cli.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_remote_cli.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_remote_cli.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P004_远端Shell命令行头文件参考.md)
- [zephyr/sys/cbprintf.h](../cbprintf_reference/P005_回调格式化输出头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_remote_cli_cbpprintf](P004_远端Shell命令行头文件参考.md#a60806c208a7a319faf4f9467e4d55946)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)
- [shell_remote_cmd_process](P004_远端Shell命令行头文件参考.md#a851c444b07279f370d3a62ab6ce71d3d)

---

[上一章](P004_远端Shell命令行头文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_远端Shell公共头文件参考.md)
