---
id: learning.zephyr-docs.shell-backend-reference.page-6
title: Shell虚拟后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__dummy_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell虚拟后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__dummy_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P005_Shell虚拟后端头文件参考.md)和[公共接口](P004_Shell虚拟后端接口.md)；访问语义和生命周期见本页译注。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00065"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__dummy_html_ga12827fc2f644eb4748408807d763419e"></a>
<a id="agroup__shell__dummy_html_ga8eb6e736190c11fe4a6eb6a02a48f44f"></a>
<a id="agroup__shell__dummy_html_ga8f830aaae69ab4bb7ab5115a27566e6d"></a>
<a id="agroup__shell__dummy_html_gaa48156ae134db73dce185be3b461071d"></a>
<a id="agroup__shell__dummy_html_gaa93489d27aab568d3ca04640e9d18391"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Shell backend used for testing
<a id="l00003"></a> *
<a id="l00004"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_DUMMY_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_DUMMY_H_
<a id="l00017"></a>
<a id="l00018"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00019"></a>
<a id="l00020"></a>#ifdef __cplusplus
<a id="l00021"></a>extern "C" {
<a id="l00022"></a>#endif
<a id="l00023"></a>
<a id="l00025"></a>extern const struct shell_transport_api shell_dummy_transport_api;
<a id="l00026"></a>
<a id="l00027"></a>struct shell_dummy {
<a id="l00028"></a>        bool initialized;
<a id="l00029"></a>
<a id="l00031"></a>        size_t len;
<a id="l00032"></a>
<a id="l00034"></a>        char buf[CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE];
<a id="l00035"></a>
<a id="l00037"></a>        size_t input_len;
<a id="l00038"></a>
<a id="l00040"></a>        size_t input_pos;
<a id="l00041"></a>
<a id="l00043"></a>        char input_buf[CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE];
<a id="l00044"></a>
<a id="l00046"></a>        shell_transport_handler_t handler;
<a id="l00047"></a>
<a id="l00049"></a>        void *context;
<a id="l00050"></a>};
<a id="l00052"></a>
<a id="l00059"></a>
<a id="l00065"></a>#define SHELL_DUMMY_DEFINE(_name)                                       \
<a id="l00066"></a>        static struct shell_dummy _name##_shell_dummy;                  \
<a id="l00067"></a>        struct shell_transport _name = {                                \
<a id="l00068"></a>                .api = &amp;shell_dummy_transport_api,                      \
<a id="l00069"></a>                .ctx = (struct shell_dummy *)&amp;_name##_shell_dummy       \
<a id="l00070"></a>        }
<a id="l00071"></a>
<a id="l00081"></a>const struct shell *shell_backend_dummy_get_ptr(void);
<a id="l00082"></a>
<a id="l00092"></a>const char *shell_backend_dummy_get_output(const struct shell *sh,
<a id="l00093"></a>                                           size_t *sizep);
<a id="l00094"></a>
<a id="l00100"></a>void shell_backend_dummy_clear_output(const struct shell *sh);
<a id="l00101"></a>
<a id="l00113"></a>int shell_backend_dummy_push_input(const struct shell *sh, const char *data, size_t len);
<a id="l00114"></a>
<a id="l00120"></a>void shell_backend_dummy_clear_input(const struct shell *sh);
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>#ifdef __cplusplus
<a id="l00125"></a>}
<a id="l00126"></a>#endif
<a id="l00127"></a>
<a id="l00128"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_DUMMY_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 用于测试的Shell后端（Shell Backend）。版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_DUMMY_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_backend_dummy_get_ptr`

```c
const struct shell * shell_backend_dummy_get_ptr(void)
```

不应直接使用此函数。

符号定位：[shell_backend_dummy_get_ptr](P004_Shell虚拟后端接口.md#ga12827fc2f644eb4748408807d763419e)。

### `shell_backend_dummy_clear_output`

```c
void shell_backend_dummy_clear_output(const struct shell *sh)
```

清空Shell后端的输出缓冲区（Output Buffer）。

符号定位：[shell_backend_dummy_clear_output](P004_Shell虚拟后端接口.md#ga8eb6e736190c11fe4a6eb6a02a48f44f)。

### `shell_backend_dummy_push_input`

```c
int shell_backend_dummy_push_input(const struct shell *sh, const char *data, size_t len)
```

向Shell虚拟后端推入输入数据（Input Data）。

符号定位：[shell_backend_dummy_push_input](P004_Shell虚拟后端接口.md#ga8f830aaae69ab4bb7ab5115a27566e6d)。

### `shell_backend_dummy_clear_input`

```c
void shell_backend_dummy_clear_input(const struct shell *sh)
```

清空Shell后端的输入缓冲区（Input Buffer）。

符号定位：[shell_backend_dummy_clear_input](P004_Shell虚拟后端接口.md#gaa48156ae134db73dce185be3b461071d)。

### `shell_backend_dummy_get_output`

```c
const char * shell_backend_dummy_get_output(const struct shell *sh, size_t *sizep)
```

返回Shell中缓存的输出，并重置指针。

符号定位：[shell_backend_dummy_get_output](P004_Shell虚拟后端接口.md#gaa93489d27aab568d3ca04640e9d18391)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 6.4\_源码跟踪译注

> 译注——虚拟后端（Dummy Backend）将输出存于内部缓冲。get_output写入NUL终止字符、返回当前长度并把内部长度清零，返回值仍指向同一内部数组。后续输出可能覆盖内容；需长期保存时应在读取后复制。

> 译注——当前输出写入会为终止字符保留空间，容量不足时只保存可容纳的部分，但仍向传输调用方报告原请求长度已处理。测试不能只凭写入成功就认定全部输出已保存。

> 译注——push_input空间不足时返回-ENOMEM且不追加数据；成功后可通知RX_RDY。读取推进input_pos，而输入已使用总长度直到clear_input才被清零。多轮测试需要按场景清理输入，不能把已经读过误当作容量自动回收。

头文件定位：[include/zephyr/shell/shell_dummy.h](../../../include/zephyr/shell/shell_dummy.h)，关联实现／接口：[subsys/shell/backends/shell_dummy.c](../../../subsys/shell/backends/shell_dummy.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_dummy.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_dummy.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_Shell虚拟后端头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_dummy_get_ptr](P004_Shell虚拟后端接口.md#ga12827fc2f644eb4748408807d763419e)
- [shell_backend_dummy_get_output](P004_Shell虚拟后端接口.md#gaa93489d27aab568d3ca04640e9d18391)
- [shell_backend_dummy_clear_output](P004_Shell虚拟后端接口.md#ga8eb6e736190c11fe4a6eb6a02a48f44f)
- [shell_backend_dummy_push_input](P004_Shell虚拟后端接口.md#ga8f830aaae69ab4bb7ab5115a27566e6d)
- [shell_backend_dummy_clear_input](P004_Shell虚拟后端接口.md#gaa48156ae134db73dce185be3b461071d)

---

[上一章](P005_Shell虚拟后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_Shell_RTT后端接口.md)
