---
id: learning.zephyr-docs.log-transport-reference.page-12
title: WebSocket日志后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__ws_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_WebSocket日志后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__ws_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P011_WebSocket日志后端头文件参考.md)和[公共API](P010_WebSocket日志后端接口.md)。

## 12.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__log__backend__ws_html_ga5501764d7eefda59e35990671be58387"></a>
<a id="agroup__log__backend__ws_html_ga6026cf4df6ba455708ca58867dd66b72"></a>
<a id="agroup__log__backend__ws_html_gabf3157cb42022eeea46cbe43c3824de0"></a>
<a id="agroup__log__backend__ws_html_gac502c554b139ba774bf1716126e36110"></a>
<a id="astdbool_8h_html"></a>
<a id="astructlog__backend_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_WS_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_WS_H_
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>#include &lt;stdbool.h&gt;
<a id="l00024"></a>
<a id="l00025"></a>#ifdef __cplusplus
<a id="l00026"></a>extern "C" {
<a id="l00027"></a>#endif
<a id="l00028"></a>
<a id="l00036"></a>int log_backend_ws_register(int fd);
<a id="l00037"></a>
<a id="l00047"></a>int log_backend_ws_unregister(int fd);
<a id="l00048"></a>
<a id="l00056"></a>const struct log_backend *log_backend_ws_get(void);
<a id="l00057"></a>
<a id="l00063"></a>void log_backend_ws_start(void);
<a id="l00064"></a>
<a id="l00065"></a>#ifdef __cplusplus
<a id="l00066"></a>}
<a id="l00067"></a>#endif
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>#endif /* ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_WS_H_ */
</code></pre>

## 12.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_WS_H_头文件包含保护结束。

## 12.3\_原页符号提示（Symbol Descriptions）

### `log_backend_ws_start`

```c
void log_backend_ws_start(void)
```

启动WebSocket日志后端。

符号定位：[log_backend_ws_start](P010_WebSocket日志后端接口.md#ga5501764d7eefda59e35990671be58387)。

### `log_backend_ws_unregister`

```c
int log_backend_ws_unregister(int fd)
```

注销曾用于发送日志输出的WebSocket套接字（Socket）。

符号定位：[log_backend_ws_unregister](P010_WebSocket日志后端接口.md#ga6026cf4df6ba455708ca58867dd66b72)。

### `log_backend_ws_register`

```c
int log_backend_ws_register(int fd)
```

注册日志输出要发送到的WebSocket套接字（Socket）。

符号定位：[log_backend_ws_register](P010_WebSocket日志后端接口.md#gabf3157cb42022eeea46cbe43c3824de0)。

### `log_backend_ws_get`

```c
const struct log_backend * log_backend_ws_get(void)
```

取得WebSocket日志后端。

符号定位：[log_backend_ws_get](P010_WebSocket日志后端接口.md#gac502c554b139ba774bf1716126e36110)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `log_backend`

日志后端结构（Logger Backend Structure）。

定义位置（Definition）：log_backend.h:118。

符号定位：[log_backend](../log_backend_reference/P004_日志后端结构.md)。

## 12.4\_源码跟踪译注

> 译注——WebSocket套接字（WebSocket Socket）的创建与连接由调用者负责。register保存给定描述符，start激活日志后端；这两个操作本身都不建立WebSocket握手。

> 译注——当前register与unregister直接访问输出控制块的ctx，而设置该ctx的do_ws_init位于首次process路径。源码中没有在注册处检查空ctx；不能从这两个API的简短说明推断可在任意初始化阶段调用。使用时需结合实际初始化顺序核对上下文已经建立。

> 译注——当前unregister即使传入描述符与已保存值不一致，也只记录一条调试信息，然后把保存值设为-1并返回0。它不会关闭套接字；描述符的关闭与连接资源回收仍由持有者处理。

> 译注——输出按换行或缓冲区满触发发送，遇到EAGAIN时按配置重试。持续失败时可能丢弃缓冲内容；处理字节数不是远端接收确认。panic路径停止继续处理消息，不提供故障状态下的网络发送保证。

头文件定位：[include/zephyr/logging/log_backend_ws.h](../../../include/zephyr/logging/log_backend_ws.h)，关联实现／接口：[subsys/logging/backends/log_backend_ws.c](../../../subsys/logging/backends/log_backend_ws.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_backend_ws.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/log_backend_ws.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 12.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P011_WebSocket日志后端头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [log_backend_ws_register](P010_WebSocket日志后端接口.md#gabf3157cb42022eeea46cbe43c3824de0)
- [log_backend_ws_unregister](P010_WebSocket日志后端接口.md#ga6026cf4df6ba455708ca58867dd66b72)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [log_backend_ws_get](P010_WebSocket日志后端接口.md#gac502c554b139ba774bf1716126e36110)
- [log_backend_ws_start](P010_WebSocket日志后端接口.md#ga5501764d7eefda59e35990671be58387)

---

[上一章](P011_WebSocket日志后端头文件参考.md) · [返回大纲](大纲.md)
