---
id: learning.zephyr-docs.shell-transport-reference.page-9
title: Shell_Telnet后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__telnet_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Shell\_Telnet后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__telnet_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P008_Shell_Telnet后端头文件参考.md)和[公共接口](P007_Shell_Telnet后端接口.md)；访问语义和生命周期见本页译注。

## 9.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00087"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__telnet_html_ga628b99d20ef08a0b1165af07aee4888c"></a>
<a id="anet_2socket_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_TELNET_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_TELNET_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/net/socket.h&gt;
<a id="l00017"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00024"></a>extern const struct shell_transport_api shell_telnet_transport_api;
<a id="l00025"></a>
<a id="l00026"></a>#define SHELL_TELNET_POLLFD_COUNT 3
<a id="l00027"></a>#define SHELL_TELNET_MAX_CMD_SIZE 3
<a id="l00028"></a>
<a id="l00030"></a>struct shell_telnet_line_buf {
<a id="l00032"></a>        char buf[CONFIG_SHELL_TELNET_LINE_BUF_SIZE];
<a id="l00033"></a>
<a id="l00035"></a>        uint16_t len;
<a id="l00036"></a>};
<a id="l00037"></a>
<a id="l00039"></a>struct shell_telnet {
<a id="l00041"></a>        shell_transport_handler_t shell_handler;
<a id="l00042"></a>
<a id="l00044"></a>        void *shell_context;
<a id="l00045"></a>
<a id="l00047"></a>        struct shell_telnet_line_buf line_out;
<a id="l00048"></a>
<a id="l00050"></a>        struct zsock_pollfd fds[SHELL_TELNET_POLLFD_COUNT];
<a id="l00051"></a>
<a id="l00053"></a>        uint8_t rx_buf[CONFIG_SHELL_CMD_BUFF_SIZE];
<a id="l00054"></a>
<a id="l00056"></a>        size_t rx_len;
<a id="l00057"></a>
<a id="l00059"></a>        struct k_mutex rx_lock;
<a id="l00060"></a>        uint8_t cmd_buf[SHELL_TELNET_MAX_CMD_SIZE];
<a id="l00061"></a>        uint8_t cmd_len;
<a id="l00062"></a>
<a id="l00067"></a>        struct k_work_delayable send_work;
<a id="l00068"></a>        struct k_work_sync work_sync;
<a id="l00069"></a>
<a id="l00071"></a>        bool output_lock;
<a id="l00072"></a>};
<a id="l00074"></a>
<a id="l00081"></a>
<a id="l00087"></a>#define SHELL_TELNET_DEFINE(_name)                                      \
<a id="l00088"></a>        static struct shell_telnet _name##_shell_telnet;                \
<a id="l00089"></a>        struct shell_transport _name = {                                \
<a id="l00090"></a>                .api = &amp;shell_telnet_transport_api,                     \
<a id="l00091"></a>                .ctx = (struct shell_telnet *)&amp;_name##_shell_telnet     \
<a id="l00092"></a>        }
<a id="l00093"></a>
<a id="l00102"></a>const struct shell *shell_backend_telnet_get_ptr(void);
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>#ifdef __cplusplus
<a id="l00107"></a>}
<a id="l00108"></a>#endif
<a id="l00109"></a>
<a id="l00110"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_TELNET_H_ */
</code></pre>

## 9.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2019 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_TELNET_H_头文件包含保护结束。

## 9.3\_原页符号提示（Symbol Descriptions）

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_backend_telnet_get_ptr`

```c
const struct shell * shell_backend_telnet_get_ptr(void)
```

此函数提供Shell Telnet后端实例的指针。

符号定位：[shell_backend_telnet_get_ptr](P007_Shell_Telnet后端接口.md#ga628b99d20ef08a0b1165af07aee4888c)。

### `socket.h`

兼容BSD套接字（BSD Sockets）的API定义。

符号定位：[socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

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

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 9.4\_源码跟踪译注

> 译注——DEFINE宏创建传输对象及静态上下文，get_ptr取得配置好的Shell实例。返回实例地址并不表示已有Telnet客户端连接；连接及输入输出由传输实现负责。

头文件定位：[include/zephyr/shell/shell_telnet.h](../../../include/zephyr/shell/shell_telnet.h)，关联实现／接口：[subsys/shell/backends/shell_telnet.c](../../../subsys/shell/backends/shell_telnet.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_telnet.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_telnet.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P008_Shell_Telnet后端头文件参考.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_telnet_get_ptr](P007_Shell_Telnet后端接口.md#ga628b99d20ef08a0b1165af07aee4888c)

---

[上一章](P008_Shell_Telnet后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_Shell_WebSocket后端接口.md)
