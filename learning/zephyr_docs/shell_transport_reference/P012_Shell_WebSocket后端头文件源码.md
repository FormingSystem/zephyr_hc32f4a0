---
id: learning.zephyr-docs.shell-transport-reference.page-12
title: Shell_WebSocket后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__websocket_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_Shell\_WebSocket后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__websocket_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P011_Shell_WebSocket后端头文件参考.md)和[公共接口](P010_Shell_WebSocket后端接口.md)；访问语义和生命周期见本页译注。

## 12.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00174"></a>
<a id="foldopen00192"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="ahttp_2server_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="aservice_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhttp__request__ctx_html"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_WEBSOCKET_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_WEBSOCKET_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/net/socket.h&gt;
<a id="l00017"></a>#include &lt;zephyr/net/http/server.h&gt;
<a id="l00018"></a>#include &lt;zephyr/net/http/service.h&gt;
<a id="l00019"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#ifdef __cplusplus
<a id="l00022"></a>extern "C" {
<a id="l00023"></a>#endif
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>#define SHELL_WEBSOCKET_SERVICE_COUNT CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT
<a id="l00028"></a>
<a id="l00030"></a>struct shell_websocket_line_buf {
<a id="l00032"></a>        char buf[CONFIG_SHELL_WEBSOCKET_LINE_BUF_SIZE];
<a id="l00033"></a>
<a id="l00035"></a>        uint16_t len;
<a id="l00036"></a>};
<a id="l00037"></a>
<a id="l00039"></a>struct shell_websocket {
<a id="l00041"></a>        shell_transport_handler_t shell_handler;
<a id="l00042"></a>
<a id="l00044"></a>        void *shell_context;
<a id="l00045"></a>
<a id="l00047"></a>        struct shell_websocket_line_buf line_out;
<a id="l00048"></a>
<a id="l00050"></a>        struct zsock_pollfd fds[1];
<a id="l00051"></a>
<a id="l00053"></a>        struct k_mutex socket_lock;
<a id="l00054"></a>
<a id="l00056"></a>        uint8_t rx_buf[CONFIG_SHELL_CMD_BUFF_SIZE];
<a id="l00057"></a>
<a id="l00059"></a>        size_t rx_len;
<a id="l00060"></a>
<a id="l00062"></a>        struct k_mutex rx_lock;
<a id="l00063"></a>
<a id="l00068"></a>        struct k_work_delayable send_work;
<a id="l00069"></a>        struct k_work_sync work_sync;
<a id="l00070"></a>
<a id="l00072"></a>        bool output_lock;
<a id="l00073"></a>};
<a id="l00074"></a>
<a id="l00075"></a>extern const struct shell_transport_api shell_websocket_transport_api;
<a id="l00076"></a>int shell_websocket_setup(int ws_socket, struct http_request_ctx *request_ctx, void *user_data);
<a id="l00077"></a>int shell_websocket_enable(const struct shell *sh);
<a id="l00078"></a>
<a id="l00079"></a>#define GET_WS_NAME(_service) ws_ctx_##_service
<a id="l00080"></a>#define GET_WS_SHELL_NAME(_name) shell_websocket_##_name
<a id="l00081"></a>#define GET_WS_TRANSPORT_NAME(_service) transport_shell_ws_##_service
<a id="l00082"></a>#define GET_WS_DETAIL_NAME(_service) ws_res_detail_##_service
<a id="l00083"></a>
<a id="l00084"></a>#define SHELL_WEBSOCKET_DEFINE(_service)                                        \
<a id="l00085"></a>        static struct shell_websocket GET_WS_NAME(_service);                    \
<a id="l00086"></a>        static struct shell_transport GET_WS_TRANSPORT_NAME(_service) = {       \
<a id="l00087"></a>                .api = &amp;shell_websocket_transport_api,                          \
<a id="l00088"></a>                .ctx = &amp;GET_WS_NAME(_service),                                  \
<a id="l00089"></a>        }
<a id="l00090"></a>
<a id="l00091"></a>#define SHELL_WS_PORT_NAME(_service)    http_service_##_service
<a id="l00092"></a>#define SHELL_WS_BUF_NAME(_service)     ws_recv_buffer_##_service
<a id="l00093"></a>#define SHELL_WS_TEMP_RECV_BUF_SIZE 256
<a id="l00094"></a>
<a id="l00095"></a>#define DEFINE_WEBSOCKET_HTTP_SERVICE(_service)                                 \
<a id="l00096"></a>        uint8_t SHELL_WS_BUF_NAME(_service)[SHELL_WS_TEMP_RECV_BUF_SIZE];       \
<a id="l00097"></a>        struct http_resource_detail_websocket                                   \
<a id="l00098"></a>            GET_WS_DETAIL_NAME(_service) = {                                    \
<a id="l00099"></a>                .common = {                                                     \
<a id="l00100"></a>                        .type = HTTP_RESOURCE_TYPE_WEBSOCKET,                   \
<a id="l00101"></a>                                                                                \
<a id="l00102"></a>                        /* We need HTTP/1.1 GET method for upgrading */         \
<a id="l00103"></a>                        .bitmask_of_supported_http_methods = BIT(HTTP_GET),     \
<a id="l00104"></a>                },                                                              \
<a id="l00105"></a>                .cb = shell_websocket_setup,                                    \
<a id="l00106"></a>                .data_buffer = SHELL_WS_BUF_NAME(_service),                     \
<a id="l00107"></a>                .data_buffer_len = sizeof(SHELL_WS_BUF_NAME(_service)),         \
<a id="l00108"></a>                .user_data = &amp;GET_WS_NAME(_service),                            \
<a id="l00109"></a>        };                                                                      \
<a id="l00110"></a>        HTTP_RESOURCE_DEFINE(ws_resource_##_service, _service,                  \
<a id="l00111"></a>                             "/" CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL,           \
<a id="l00112"></a>                             &amp;GET_WS_DETAIL_NAME(_service))
<a id="l00113"></a>
<a id="l00114"></a>#define DEFINE_WEBSOCKET_SERVICE(_service)                                      \
<a id="l00115"></a>        SHELL_WEBSOCKET_DEFINE(_service);                                       \
<a id="l00116"></a>        SHELL_DEFINE(shell_websocket_##_service,                                \
<a id="l00117"></a>                     CONFIG_SHELL_WEBSOCKET_PROMPT,                             \
<a id="l00118"></a>                     &amp;GET_WS_TRANSPORT_NAME(_service),                          \
<a id="l00119"></a>                     CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_SIZE,             \
<a id="l00120"></a>                     CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_TIMEOUT,          \
<a id="l00121"></a>                     SHELL_FLAG_OLF_CRLF);                                      \
<a id="l00122"></a>        DEFINE_WEBSOCKET_HTTP_SERVICE(_service)
<a id="l00124"></a>
<a id="l00131"></a>
<a id="l00132"></a>#if defined(CONFIG_NET_SOCKETS_SOCKOPT_TLS)
<a id="l00133"></a>/* Use a secure connection only for Websocket. */
<a id="l00145"></a>#define WEBSOCKET_CONSOLE_DEFINE(_service, _sec_tag_list, _sec_tag_list_size) \
<a id="l00146"></a>        static uint16_t SHELL_WS_PORT_NAME(_service) =                    \
<a id="l00147"></a>                CONFIG_SHELL_WEBSOCKET_PORT;                              \
<a id="l00148"></a>        HTTPS_SERVICE_DEFINE(_service,                                    \
<a id="l00149"></a>                             CONFIG_SHELL_WEBSOCKET_IP_ADDR,              \
<a id="l00150"></a>                             &amp;SHELL_WS_PORT_NAME(_service),               \
<a id="l00151"></a>                             SHELL_WEBSOCKET_SERVICE_COUNT,               \
<a id="l00152"></a>                             SHELL_WEBSOCKET_SERVICE_COUNT,               \
<a id="l00153"></a>                             NULL,                                        \
<a id="l00154"></a>                             NULL,                                        \
<a id="l00155"></a>                             NULL,                                        \
<a id="l00156"></a>                             _sec_tag_list,                               \
<a id="l00157"></a>                             _sec_tag_list_size);                         \
<a id="l00158"></a>        DEFINE_WEBSOCKET_SERVICE(_service);                               \
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>#else /* CONFIG_NET_SOCKETS_SOCKOPT_TLS */
<a id="l00162"></a>/* TLS not possible so define only normal HTTP service */
<a id="l00174"></a>#define WEBSOCKET_CONSOLE_DEFINE(_service, _sec_tag_list, _sec_tag_list_size) \
<a id="l00175"></a>        static uint16_t SHELL_WS_PORT_NAME(_service) =                  \
<a id="l00176"></a>                CONFIG_SHELL_WEBSOCKET_PORT;                            \
<a id="l00177"></a>        HTTP_SERVICE_DEFINE(_service,                                   \
<a id="l00178"></a>                            CONFIG_SHELL_WEBSOCKET_IP_ADDR,             \
<a id="l00179"></a>                            &amp;SHELL_WS_PORT_NAME(_service),              \
<a id="l00180"></a>                            SHELL_WEBSOCKET_SERVICE_COUNT,              \
<a id="l00181"></a>                            SHELL_WEBSOCKET_SERVICE_COUNT,              \
<a id="l00182"></a>                            NULL, NULL, NULL);                          \
<a id="l00183"></a>        DEFINE_WEBSOCKET_SERVICE(_service)
<a id="l00184"></a>
<a id="l00185"></a>#endif /* CONFIG_NET_SOCKETS_SOCKOPT_TLS */
<a id="l00186"></a>
<a id="l00192"></a>#define WEBSOCKET_CONSOLE_ENABLE(_service)                              \
<a id="l00193"></a>        (void)shell_websocket_enable(&amp;GET_WS_SHELL_NAME(_service))
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>#ifdef __cplusplus
<a id="l00198"></a>}
<a id="l00199"></a>#endif
<a id="l00200"></a>
<a id="l00201"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_WEBSOCKET_H_ */
</code></pre>

## 12.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 升级（Upgrade）需要使用HTTP/1.1的GET方法。

3. 仅对WebSocket使用安全连接（Secure Connection）。

4. CONFIG_NET_SOCKETS_SOCKOPT_TLS条件的else分支标记。

5. 无法使用TLS，因此只定义普通HTTP服务。

6. CONFIG_NET_SOCKETS_SOCKOPT_TLS条件编译结束标记。

7. ZEPHYR_INCLUDE_SHELL_SHELL_WEBSOCKET_H_头文件包含保护结束。

## 12.3\_原页符号提示（Symbol Descriptions）

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `server.h`

HTTP服务器API（HTTP Server API）。

符号定位：[server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)。

### `socket.h`

兼容BSD套接字（BSD Sockets）的API定义。

符号定位：[socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。

### `service.h`

HTTP服务API（HTTP Service API）。

符号定位：[service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html)。

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

### `http_request_ctx`

HTTP请求上下文（HTTP Request Context）。

定义位置（Definition）：server.h:210。

符号定位：[http_request_ctx](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request__ctx.html)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 12.4\_源码跟踪译注

> 译注——WEBSOCKET_CONSOLE_DEFINE在编译期同时定义Shell传输、Shell实例与HTTP资源。CONFIG_NET_SOCKETS_SOCKOPT_TLS选择HTTPS或普通HTTP分支；未启用TLS时安全标签参数不参与普通HTTP服务定义。

> 译注——资源只支持HTTP GET用于WebSocket升级（Upgrade），路径由斜杠和CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL组成。不要把HTTP资源定义理解成已经建立了客户端会话。

> 译注——WEBSOCKET_CONSOLE_ENABLE调用shell_websocket_enable，但宏显式丢弃其返回值。底层函数返回shell_init结果；宏调用结束本身不提供可检查的初始化成功状态。

> 译注——源码中的输入缓冲、套接字锁和延迟工作属于实现内部结构。原始源码页可见它们不代表官方为全部内部字段提供独立的公共API契约。

头文件定位：[include/zephyr/shell/shell_websocket.h](../../../include/zephyr/shell/shell_websocket.h)，关联实现／接口：[subsys/shell/backends/shell_websocket.c](../../../subsys/shell/backends/shell_websocket.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_websocket.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_websocket.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 12.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P011_Shell_WebSocket后端头文件参考.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)
- [zephyr/net/http/service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [http_request_ctx](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request__ctx.html)
- [shell](../shell_core_reference/P004_Shell实例结构.md)

---

[上一章](P011_Shell_WebSocket后端头文件参考.md) · [返回大纲](大纲.md)
