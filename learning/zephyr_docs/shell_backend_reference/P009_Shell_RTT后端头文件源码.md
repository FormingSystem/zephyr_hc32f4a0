---
id: learning.zephyr-docs.shell-backend-reference.page-9
title: Shell_RTT后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__rtt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Shell\_RTT后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__rtt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P008_Shell_RTT后端头文件参考.md)和[公共接口](P007_Shell_RTT后端接口.md)；访问语义和生命周期见本页译注。

## 9.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00044"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__rtt_html_ga74ccc10cf40cd54f6d4d28f5e62f3091"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Makaio GmbH
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_RTT_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_RTT_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00023"></a>extern const struct shell_transport_api shell_rtt_transport_api;
<a id="l00024"></a>
<a id="l00025"></a>struct shell_rtt {
<a id="l00026"></a>        shell_transport_handler_t handler;
<a id="l00027"></a>        struct k_timer timer;
<a id="l00028"></a>        void *context;
<a id="l00029"></a>};
<a id="l00031"></a>
<a id="l00038"></a>
<a id="l00044"></a>#define SHELL_RTT_DEFINE(_name)                                 \
<a id="l00045"></a>        static struct shell_rtt _name##_shell_rtt;                      \
<a id="l00046"></a>        struct shell_transport _name = {                                \
<a id="l00047"></a>                .api = &amp;shell_rtt_transport_api,                        \
<a id="l00048"></a>                .ctx = (struct shell_rtt *)&amp;_name##_shell_rtt           \
<a id="l00049"></a>        }
<a id="l00050"></a>
<a id="l00059"></a>const struct shell *shell_backend_rtt_get_ptr(void);
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>#ifdef __cplusplus
<a id="l00064"></a>}
<a id="l00065"></a>#endif
<a id="l00066"></a>
<a id="l00067"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_RTT_H_ */
</code></pre>

## 9.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Makaio GmbH；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_RTT_H_头文件包含保护结束。

## 9.3\_原页符号提示（Symbol Descriptions）

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_backend_rtt_get_ptr`

```c
const struct shell * shell_backend_rtt_get_ptr(void)
```

提供Shell RTT后端实例的指针。

符号定位：[shell_backend_rtt_get_ptr](P007_Shell_RTT后端接口.md#ga74ccc10cf40cd54f6d4d28f5e62f3091)。

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

## 9.4\_源码跟踪译注

> 译注——RTT（Real Time Transfer）通过调试通道传输数据；get_ptr取得已定义的Shell实例地址，不负责建立调试探针连接。DEFINE宏创建传输对象及其上下文，Shell实例和传输实例不要混为一谈。

头文件定位：[include/zephyr/shell/shell_rtt.h](../../../include/zephyr/shell/shell_rtt.h)，关联实现／接口：[subsys/shell/backends/shell_rtt.c](../../../subsys/shell/backends/shell_rtt.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_rtt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_rtt.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P008_Shell_RTT后端头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_rtt_get_ptr](P007_Shell_RTT后端接口.md#ga74ccc10cf40cd54f6d4d28f5e62f3091)

---

[上一章](P008_Shell_RTT后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_Shell_UART后端接口.md)
