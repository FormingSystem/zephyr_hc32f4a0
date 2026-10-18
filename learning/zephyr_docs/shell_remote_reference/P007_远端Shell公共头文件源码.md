---
id: learning.zephyr-docs.shell-remote-reference.page-7
title: 远端Shell公共头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__common_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_远端Shell公共头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__common_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P006_远端Shell公共头文件参考.md)和[公共接口](P001_远端Shell接口.md)；访问语义和生命周期见本页译注。

## 7.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00046"></a>
<a id="foldopen00052"></a>
<a id="foldopen00062"></a>
<a id="foldopen00076"></a>
<a id="foldopen00084"></a>
<a id="foldopen00094"></a>
<a id="foldopen00110"></a>
<a id="agroup__shell__api_html_ga331e7d19b9b0755486596f5ffc598338"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructshell__remote__msg__cmd__get_html"></a>
<a id="astructshell__remote__msg__cmd__get_html_a205b1bce49334b83ccc669d68720d69c"></a>
<a id="astructshell__remote__msg__cmd__get_html_a7f8cd91270137df8995e3a5913eb1b00"></a>
<a id="astructshell__remote__msg__cmd__get_html_a89bed24f4000096cc53f259d2a2d183e"></a>
<a id="astructshell__remote__msg__cmd_html"></a>
<a id="astructshell__remote__msg__cmd_html_a04251b73dbc44e09f8dc386fd5128af9"></a>
<a id="astructshell__remote__msg__cmd_html_a39ed2f88f0bf01a68b327be6067f0818"></a>
<a id="astructshell__remote__msg__cmd_html_a400f454b15a9f69463bc79ccfee9a904"></a>
<a id="astructshell__remote__msg__cmd_html_a45f35f76aac5f6a29e5b7bbcfc312d2b"></a>
<a id="astructshell__remote__msg__cmd_html_aadc28558b4ecbf31c42d886b6f42b2a9"></a>
<a id="astructshell__remote__msg__cmd_html_afdaf8c8fd47440d0c487d75ae072d468"></a>
<a id="astructshell__remote__msg__exec_html"></a>
<a id="astructshell__remote__msg__exec_html_a6c661488016ddf91df201e5971ef9919"></a>
<a id="astructshell__remote__msg__exec_html_ad87d1ba0997fec825264a2a822fa5c3a"></a>
<a id="astructshell__remote__msg__exec_html_aefd3b2714922ef9185ace6afe651632a"></a>
<a id="astructshell__remote__msg__exec_html_af37fa4562d03647fc9f3d1600ab64500"></a>
<a id="astructshell__remote__msg__exec_html_af4d04a35c0f33572b0723b41a1bca453"></a>
<a id="astructshell__remote__msg__generic_html"></a>
<a id="astructshell__remote__msg__generic_html_a8e020f1dd46da8efecc8b3d362fda0e1"></a>
<a id="astructshell__remote__msg__print_html"></a>
<a id="astructshell__remote__msg__print_html_a58ecd5cbe3bb9d44e6f38285b09cd857"></a>
<a id="astructshell__remote__msg__print_html_aa6156ad4d41eeab87030a6238d67633b"></a>
<a id="astructshell__remote__msg__print_html_ad6746a9530f0d7b86593d7ac1d4844d7"></a>
<a id="astructshell__remote__msg__result_html"></a>
<a id="astructshell__remote__msg__result_html_a28203656bb169c8795c8df0700349484"></a>
<a id="astructshell__remote__msg__result_html_aafb3c21e82956cbc465b5a75fe045cd6"></a>
<a id="astructshell__static__args_html"></a>
<a id="astructshell__static__entry_html"></a>
<a id="aunionshell__cmd__entry_html"></a>
<a id="aunionshell__remote__msg_html"></a>
<a id="aunionshell__remote__msg_html_a119a705c8f8221dce1f8030ab0f3a66a"></a>
<a id="aunionshell__remote__msg_html_a1ecdbe4c2e7f7a080839a5d56fd029ba"></a>
<a id="aunionshell__remote__msg_html_a33e93c0e2a28c62c3481d201d54d6ef7"></a>
<a id="aunionshell__remote__msg_html_a766c60920a68b0dd29e2c5bb0cce3b09"></a>
<a id="aunionshell__remote__msg_html_a8de3d7b63d61e8f1bcd1642254c7cda6"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2026 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_COMMON_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_COMMON_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00027"></a>
<a id="l00029"></a>#define SHELL_REMOTE_MSG_PRINT      1
<a id="l00030"></a>
<a id="l00032"></a>#define SHELL_REMOTE_MSG_CMD_GET    2
<a id="l00033"></a>
<a id="l00035"></a>#define SHELL_REMOTE_MSG_CMD        3
<a id="l00036"></a>
<a id="l00038"></a>#define SHELL_REMOTE_MSG_EXEC       4
<a id="l00039"></a>
<a id="l00041"></a>#define SHELL_REMOTE_MSG_RESULT     5
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>struct shell_remote_msg_generic {
<a id="l00048"></a>        uint8_t id;
<a id="l00049"></a>};
<a id="l00050"></a>
<a id="l00052"></a>struct shell_remote_msg_print {
<a id="l00054"></a>        uint8_t id;
<a id="l00056"></a>        uint8_t color;
<a id="l00058"></a>        uint8_t data[0];
<a id="l00059"></a>};
<a id="l00060"></a>
<a id="l00062"></a>struct shell_remote_msg_exec {
<a id="l00064"></a>        uint8_t id;
<a id="l00066"></a>        uint8_t argc;
<a id="l00068"></a>        uint8_t cmd_lvl;
<a id="l00070"></a>        shell_cmd_handler handler;
<a id="l00072"></a>        uint8_t data[0];
<a id="l00073"></a>};
<a id="l00074"></a>
<a id="l00076"></a>struct shell_remote_msg_result {
<a id="l00078"></a>        uint8_t id;
<a id="l00080"></a>        int result;
<a id="l00081"></a>};
<a id="l00082"></a>
<a id="l00084"></a>struct shell_remote_msg_cmd_get {
<a id="l00086"></a>        uint8_t id;
<a id="l00088"></a>        const struct shell_static_entry *parent;
<a id="l00090"></a>        size_t idx;
<a id="l00091"></a>};
<a id="l00092"></a>
<a id="l00094"></a>struct shell_remote_msg_cmd {
<a id="l00096"></a>        uint8_t id;
<a id="l00098"></a>        const union shell_cmd_entry *subcmd;
<a id="l00100"></a>        const struct shell_static_entry *entry;
<a id="l00102"></a>        shell_cmd_handler handler;
<a id="l00104"></a>        struct shell_static_args args;
<a id="l00106"></a>        char data[0];
<a id="l00107"></a>};
<a id="l00108"></a>
<a id="l00110"></a>union shell_remote_msg {
<a id="l00112"></a>        struct shell_remote_msg_generic *generic;
<a id="l00114"></a>        struct shell_remote_msg_print *print;
<a id="l00116"></a>        struct shell_remote_msg_cmd *cmd;
<a id="l00118"></a>        struct shell_remote_msg_cmd_get *cmd_get;
<a id="l00120"></a>        struct shell_remote_msg_exec *exec;
<a id="l00122"></a>        struct shell_remote_msg_result *result;
<a id="l00123"></a>};
<a id="l00124"></a>
<a id="l00125"></a>#ifdef __cplusplus
<a id="l00126"></a>}
<a id="l00127"></a>#endif
<a id="l00128"></a>
<a id="l00129"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_COMMON_H_ */
</code></pre>

## 7.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2026 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_COMMON_H_头文件包含保护结束。

## 7.3\_原页符号提示（Symbol Descriptions）

### `shell_cmd_handler`

```c
int(* shell_cmd_handler)(const struct shell *sh, size_t argc, char **argv)
```

Shell命令处理函数原型（Command Handler Prototype）。

定义位置（Definition）：shell.h:267。

符号定位：[shell_cmd_handler](../shell_core_reference/P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `shell_remote_msg_cmd_get`

获取命令（Get Command）。

定义位置（Definition）：shell_remote_common.h:84。

符号定位：[shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)。

### `shell_remote_msg_cmd_get::parent`

```c
const struct shell_static_entry * parent
```

父命令（Parent Command）。

定义位置（Definition）：shell_remote_common.h:88。

符号定位：[shell_remote_msg_cmd_get::parent](P012_远端Shell获取命令消息.md#a205b1bce49334b83ccc669d68720d69c)。

### `shell_remote_msg_cmd_get::idx`

```c
size_t idx
```

索引（Index）。

定义位置（Definition）：shell_remote_common.h:90。

符号定位：[shell_remote_msg_cmd_get::idx](P012_远端Shell获取命令消息.md#a7f8cd91270137df8995e3a5913eb1b00)。

### `shell_remote_msg_cmd_get::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:86。

符号定位：[shell_remote_msg_cmd_get::id](P012_远端Shell获取命令消息.md#a89bed24f4000096cc53f259d2a2d183e)。

### `shell_remote_msg_cmd`

获取命令请求的响应（Response to Get Command）。

定义位置（Definition）：shell_remote_common.h:94。

符号定位：[shell_remote_msg_cmd](P011_远端Shell命令消息.md)。

### `shell_remote_msg_cmd::handler`

```c
shell_cmd_handler handler
```

命令处理函数（Command Handler）。

定义位置（Definition）：shell_remote_common.h:102。

符号定位：[shell_remote_msg_cmd::handler](P011_远端Shell命令消息.md#a04251b73dbc44e09f8dc386fd5128af9)。

### `shell_remote_msg_cmd::entry`

```c
const struct shell_static_entry * entry
```

条目（Entry）。

定义位置（Definition）：shell_remote_common.h:100。

符号定位：[shell_remote_msg_cmd::entry](P011_远端Shell命令消息.md#a39ed2f88f0bf01a68b327be6067f0818)。

### `shell_remote_msg_cmd::data`

```c
char data[0]
```

数据：以空字符（NUL）结尾的命令语法文本，后接可选的帮助文本。

定义位置（Definition）：shell_remote_common.h:106。

符号定位：[shell_remote_msg_cmd::data](P011_远端Shell命令消息.md#a400f454b15a9f69463bc79ccfee9a904)。

### `shell_remote_msg_cmd::args`

```c
struct shell_static_args args
```

命令参数（Command Parameters）。

定义位置（Definition）：shell_remote_common.h:104。

符号定位：[shell_remote_msg_cmd::args](P011_远端Shell命令消息.md#a45f35f76aac5f6a29e5b7bbcfc312d2b)。

### `shell_remote_msg_cmd::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:96。

符号定位：[shell_remote_msg_cmd::id](P011_远端Shell命令消息.md#aadc28558b4ecbf31c42d886b6f42b2a9)。

### `shell_remote_msg_cmd::subcmd`

```c
const union shell_cmd_entry * subcmd
```

子命令（Subcommand）。

定义位置（Definition）：shell_remote_common.h:98。

符号定位：[shell_remote_msg_cmd::subcmd](P011_远端Shell命令消息.md#afdaf8c8fd47440d0c487d75ae072d468)。

### `shell_remote_msg_exec`

执行命令（Execute Command）。

定义位置（Definition）：shell_remote_common.h:62。

符号定位：[shell_remote_msg_exec](P013_远端Shell执行消息.md)。

### `shell_remote_msg_exec::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:64。

符号定位：[shell_remote_msg_exec::id](P013_远端Shell执行消息.md#a6c661488016ddf91df201e5971ef9919)。

### `shell_remote_msg_exec::cmd_lvl`

```c
uint8_t cmd_lvl
```

命令层级（Command Level）。

定义位置（Definition）：shell_remote_common.h:68。

符号定位：[shell_remote_msg_exec::cmd_lvl](P013_远端Shell执行消息.md#ad87d1ba0997fec825264a2a822fa5c3a)。

### `shell_remote_msg_exec::handler`

```c
shell_cmd_handler handler
```

命令处理函数（Command Handler）。

定义位置（Definition）：shell_remote_common.h:70。

符号定位：[shell_remote_msg_exec::handler](P013_远端Shell执行消息.md#aefd3b2714922ef9185ace6afe651632a)。

### `shell_remote_msg_exec::argc`

```c
uint8_t argc
```

参数数量（Argument Count）。

定义位置（Definition）：shell_remote_common.h:66。

符号定位：[shell_remote_msg_exec::argc](P013_远端Shell执行消息.md#af37fa4562d03647fc9f3d1600ab64500)。

### `shell_remote_msg_exec::data`

```c
uint8_t data[0]
```

命令实参（Command Arguments）。

定义位置（Definition）：shell_remote_common.h:72。

符号定位：[shell_remote_msg_exec::data](P013_远端Shell执行消息.md#af4d04a35c0f33572b0723b41a1bca453)。

### `shell_remote_msg_generic`

通用消息（Generic Message）。

定义位置（Definition）：shell_remote_common.h:46。

符号定位：[shell_remote_msg_generic](P014_远端Shell通用消息.md)。

### `shell_remote_msg_generic::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:48。

符号定位：[shell_remote_msg_generic::id](P014_远端Shell通用消息.md#a8e020f1dd46da8efecc8b3d362fda0e1)。

### `shell_remote_msg_print`

打印消息（Print Message）。

定义位置（Definition）：shell_remote_common.h:52。

符号定位：[shell_remote_msg_print](P015_远端Shell打印消息.md)。

### `shell_remote_msg_print::color`

```c
uint8_t color
```

颜色（Color）。

定义位置（Definition）：shell_remote_common.h:56。

符号定位：[shell_remote_msg_print::color](P015_远端Shell打印消息.md#a58ecd5cbe3bb9d44e6f38285b09cd857)。

### `shell_remote_msg_print::data`

```c
uint8_t data[0]
```

cbprintf包，已预先填充以满足8字节对齐（8-byte Alignment）。

定义位置（Definition）：shell_remote_common.h:58。

符号定位：[shell_remote_msg_print::data](P015_远端Shell打印消息.md#aa6156ad4d41eeab87030a6238d67633b)。

### `shell_remote_msg_print::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:54。

符号定位：[shell_remote_msg_print::id](P015_远端Shell打印消息.md#ad6746a9530f0d7b86593d7ac1d4844d7)。

### `shell_remote_msg_result`

结果（Result）。

定义位置（Definition）：shell_remote_common.h:76。

符号定位：[shell_remote_msg_result](P016_远端Shell结果消息.md)。

### `shell_remote_msg_result::id`

```c
uint8_t id
```

消息编号（Message ID）。

定义位置（Definition）：shell_remote_common.h:78。

符号定位：[shell_remote_msg_result::id](P016_远端Shell结果消息.md#a28203656bb169c8795c8df0700349484)。

### `shell_remote_msg_result::result`

```c
int result
```

结果（Result）。

定义位置（Definition）：shell_remote_common.h:80。

符号定位：[shell_remote_msg_result::result](P016_远端Shell结果消息.md#aafb3c21e82956cbc465b5a75fe045cd6)。

### `shell_static_args`

Shell命令的参数数量约束（Argument Count Constraints）与远端路由（Remote Routing）。

定义位置（Definition）：shell.h:120。

符号定位：[shell_static_args](../shell_core_reference/P007_Shell命令参数约束.md)。

### `shell_static_entry`

Shell静态命令描述符（Static Command Descriptor）。

定义位置（Definition）：shell.h:299。

符号定位：[shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)。

### `shell_cmd_entry`

Shell命令描述符（Command Descriptor）。

定义位置（Definition）：shell.h:109。

符号定位：[shell_cmd_entry](../shell_core_reference/P011_Shell命令条目联合体.md)。

### `shell_remote_msg`

远端Shell消息联合体（Message Union）。

定义位置（Definition）：shell_remote_common.h:110。

符号定位：[shell_remote_msg](P017_远端Shell消息联合体.md)。

### `shell_remote_msg::print`

```c
struct shell_remote_msg_print * print
```

打印消息（Print Message）。

定义位置（Definition）：shell_remote_common.h:114。

符号定位：[shell_remote_msg::print](P017_远端Shell消息联合体.md#a119a705c8f8221dce1f8030ab0f3a66a)。

### `shell_remote_msg::exec`

```c
struct shell_remote_msg_exec * exec
```

执行命令（Execute Command）。

定义位置（Definition）：shell_remote_common.h:120。

符号定位：[shell_remote_msg::exec](P017_远端Shell消息联合体.md#a1ecdbe4c2e7f7a080839a5d56fd029ba)。

### `shell_remote_msg::cmd_get`

```c
struct shell_remote_msg_cmd_get * cmd_get
```

获取命令（Get Command）。

定义位置（Definition）：shell_remote_common.h:118。

符号定位：[shell_remote_msg::cmd_get](P017_远端Shell消息联合体.md#a33e93c0e2a28c62c3481d201d54d6ef7)。

### `shell_remote_msg::result`

```c
struct shell_remote_msg_result * result
```

结果（Result）。

定义位置（Definition）：shell_remote_common.h:122。

符号定位：[shell_remote_msg::result](P017_远端Shell消息联合体.md#a766c60920a68b0dd29e2c5bb0cce3b09)。

### `shell_remote_msg::cmd`

```c
struct shell_remote_msg_cmd * cmd
```

命令（Command）。

定义位置（Definition）：shell_remote_common.h:116。

符号定位：[shell_remote_msg::cmd](P017_远端Shell消息联合体.md#a8de3d7b63d61e8f1bcd1642254c7cda6)。

## 7.4\_源码跟踪译注

> 译注——消息结构含size_t、int、函数指针和其他对象指针，不能把这些C结构当成天然跨位宽、跨字节序的通用网络格式。指针字段是对应远端命令对象或处理函数的值，不能在错误的地址空间中直接解引用。

> 译注——data[0]在原始声明中表示头部后的变长数据位置；它不自带存储容量。命令响应数据依次保存NUL结尾的语法和可选帮助文本，实际长度来自消息，不应由零长数组的sizeof推算。

> 译注——消息联合体的成员是各消息类型的指针。应先根据通用头中的消息编号选择成员，再按对应消息格式解析；这不是同时容纳所有消息正文的内嵌结构。

头文件定位：[include/zephyr/shell/shell_remote_common.h](../../../include/zephyr/shell/shell_remote_common.h)，关联实现／接口：[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_remote_common.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_remote.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P006_远端Shell公共头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_remote_msg_generic](P014_远端Shell通用消息.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](P014_远端Shell通用消息.md#a8e020f1dd46da8efecc8b3d362fda0e1)
- [shell_remote_msg_print](P015_远端Shell打印消息.md)
- [id](P015_远端Shell打印消息.md#ad6746a9530f0d7b86593d7ac1d4844d7)
- [color](P015_远端Shell打印消息.md#a58ecd5cbe3bb9d44e6f38285b09cd857)
- [data](P015_远端Shell打印消息.md#aa6156ad4d41eeab87030a6238d67633b)
- [shell_remote_msg_exec](P013_远端Shell执行消息.md)
- [id](P013_远端Shell执行消息.md#a6c661488016ddf91df201e5971ef9919)
- [argc](P013_远端Shell执行消息.md#af37fa4562d03647fc9f3d1600ab64500)
- [cmd_lvl](P013_远端Shell执行消息.md#ad87d1ba0997fec825264a2a822fa5c3a)
- [shell_cmd_handler](../shell_core_reference/P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)
- [handler](P013_远端Shell执行消息.md#aefd3b2714922ef9185ace6afe651632a)
- [data](P013_远端Shell执行消息.md#af4d04a35c0f33572b0723b41a1bca453)
- [shell_remote_msg_result](P016_远端Shell结果消息.md)
- [id](P016_远端Shell结果消息.md#a28203656bb169c8795c8df0700349484)
- [result](P016_远端Shell结果消息.md#aafb3c21e82956cbc465b5a75fe045cd6)
- [shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)
- [id](P012_远端Shell获取命令消息.md#a89bed24f4000096cc53f259d2a2d183e)
- [shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)
- [parent](P012_远端Shell获取命令消息.md#a205b1bce49334b83ccc669d68720d69c)
- [idx](P012_远端Shell获取命令消息.md#a7f8cd91270137df8995e3a5913eb1b00)
- [shell_remote_msg_cmd](P011_远端Shell命令消息.md)
- [id](P011_远端Shell命令消息.md#aadc28558b4ecbf31c42d886b6f42b2a9)
- [shell_cmd_entry](../shell_core_reference/P011_Shell命令条目联合体.md)
- [subcmd](P011_远端Shell命令消息.md#afdaf8c8fd47440d0c487d75ae072d468)
- [entry](P011_远端Shell命令消息.md#a39ed2f88f0bf01a68b327be6067f0818)
- [handler](P011_远端Shell命令消息.md#a04251b73dbc44e09f8dc386fd5128af9)
- [shell_static_args](../shell_core_reference/P007_Shell命令参数约束.md)
- [args](P011_远端Shell命令消息.md#a45f35f76aac5f6a29e5b7bbcfc312d2b)
- [data](P011_远端Shell命令消息.md#a400f454b15a9f69463bc79ccfee9a904)
- [shell_remote_msg](P017_远端Shell消息联合体.md)
- [print](P017_远端Shell消息联合体.md#a119a705c8f8221dce1f8030ab0f3a66a)
- [cmd](P017_远端Shell消息联合体.md#a8de3d7b63d61e8f1bcd1642254c7cda6)
- [cmd_get](P017_远端Shell消息联合体.md#a33e93c0e2a28c62c3481d201d54d6ef7)
- [exec](P017_远端Shell消息联合体.md#a1ecdbe4c2e7f7a080839a5d56fd029ba)
- [result](P017_远端Shell消息联合体.md#a766c60920a68b0dd29e2c5bb0cce3b09)

---

[上一章](P006_远端Shell公共头文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_远端Shell实例.md)
