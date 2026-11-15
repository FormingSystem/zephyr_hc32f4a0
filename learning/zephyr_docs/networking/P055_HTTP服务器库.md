---
id: learning.zephyr-docs.networking.page-55
title: HTTP服务器库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/http_server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_HTTP服务器库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/http_server.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 55.1 概览（Overview）

Zephyr 的 HTTP 服务器库（HTTP Server Library）允许注册 HTTP 服务（Service），并为各服务注册资源（Resource）。服务器为已注册的服务创建监听套接字（Listening Socket），接收并处理客户端连接。它支持普通 TCP 套接字上的 HTTP，以及 TLS 套接字上的 HTTPS；支持的协议版本包括 HTTP/1.1（[RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616.html)）、HTTP/2（[RFC 9113](https://datatracker.ietf.org/doc/html/rfc9113.html)）和 HTTP/3（[RFC 9114](https://datatracker.ietf.org/doc/html/rfc9114.html)）。HTTP 是超文本传输协议（Hypertext Transfer Protocol），TCP 是传输控制协议（Transmission Control Protocol），TLS 是传输层安全（Transport Layer Security）。

> 译注：HTTP/3 使用 QUIC 传输，不能将前一句的 TCP／TLS 套接字描述套用到所有协议版本。官方 [`http_server_core.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_server_core.c) 单独建立 QUIC 监听路径，并检查 HTTP/3 配置与服务凭据。

服务器运行在后台线程（Background Thread），通常不需要应用介入日常处理；应用可通过相应 API 控制服务器活动。部分资源类型提供专用回调（Callback），用于在服务器和应用之间交换资源内容或请求载荷（Payload）。

| 资源类型 | 行为 |
| --- | --- |
| 静态资源（Static Resource），[`HTTP_RESOURCE_TYPE_STATIC`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) | 内容在编译时定义，运行时不能修改 |
| 静态文件系统资源（Static Filesystem Resource），[`HTTP_RESOURCE_TYPE_STATIC_FS`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e) | 文件系统挂载路径及对外提供资源的 URL 在构建时固定；文件内容可由 HTTP 服务器之外的代码创建、修改或删除 |
| 动态资源（Dynamic Resource），[`HTTP_RESOURCE_TYPE_DYNAMIC`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) | 通过应用回调在运行时提供内容 |
| WebSocket 资源，[`HTTP_RESOURCE_TYPE_WEBSOCKET`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) | 允许与服务器建立 WebSocket 连接 |

完整使用示例见[HTTP 服务器示例](P056_HTTP服务器示例.md#sockets-http-server)。

## 55.2 服务器准备（Server Setup）

先在应用配置文件 `prj.conf` 中启用 [`CONFIG_HTTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER)：

```kconfig
CONFIG_HTTP_SERVER=y
```

HTTP 服务和资源存放在专用链接段（Linker Section）中。服务的链接段由库预先定义；应用负责定义各服务对应的资源段。资源段名称以 `http_resource_desc_` 开头，后接服务名称。

例如，名为 `my_service` 的服务应在链接脚本 `sections-rom.ld` 中定义：

```c
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_ROM(http_resource_desc_my_service, Z_LINK_ITERABLE_SUBALIGN)
```

最后，在应用 `CMakeLists.txt` 中加入链接文件和资源段：

```cmake
zephyr_linker_sources(SECTIONS sections-rom.ld)
zephyr_linker_section(NAME http_resource_desc_my_service
                      KVMA RAM_REGION GROUP RODATA_REGION)
```

> 原文注意事项：系统每注册一个 HTTP 服务，都需要为该服务定义单独的资源链接段。

## 55.3 服务、配置与兜底资源（Services and Fallback Resources）

用 [`HTTP_SERVICE_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720) 定义一个或多个 HTTP 服务，服务名称必须与链接段使用的名称一致：

```c
#include <zephyr/net/http/service.h>

static uint16_t http_service_port = 80;

HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10, NULL, NULL, NULL);
```

也可以用 [`HTTPS_SERVICE_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b6eabec04ca31871581c382c7246765) 定义 HTTPS 服务：

```c
#include <zephyr/net/http/service.h>
#include <zephyr/net/tls_credentials.h>

#define HTTP_SERVER_CERTIFICATE_TAG 1

static uint16_t https_service_port = 443;
static const sec_tag_t sec_tag_list[] = {
    HTTP_SERVER_CERTIFICATE_TAG,
};

HTTPS_SERVICE_DEFINE(my_service, "0.0.0.0", &https_service_port, 1, 10,
                     NULL, NULL, NULL, sec_tag_list, sizeof(sec_tag_list));
```

### 按服务配置（Per-service Configuration）

服务支持单独配置。原文称 `http_service_config` 当前只包括套接字创建配置，例如设置专用套接字选项或选择自定义套接字类型。

> 源码核对译注：读取的官方 [`service.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/http/service.h) 已包含 `socket_create`、协议版本选择 `http_ver` 和 HTTP/3 配置 `h3`。因此“只包括套接字创建”是原页尚未覆盖新字段的说明；本节按原文继续演示创建回调。

自定义套接字创建示例：

```c
static int my_socket_create(const struct http_service_desc *svc, int af, int proto)
{
    int fd;

    /* Create socket with custom parameters */
    fd = zsock_socket(af, SOCK_STREAM, proto);
    if (fd < 0) {
        return fd;
    }

    /* Set custom socket options */
    /* Add any other custom socket configuration */

    return fd;
}

static const struct http_service_config my_service_config = {
    .socket_create = my_socket_create,
};

static uint16_t http_service_port = 80;

HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10,
                    NULL, NULL, &my_service_config);
```

自定义创建函数接收以下参数：

| 参数 | 含义 |
| --- | --- |
| `svc` | 服务描述符（Service Descriptor）指针 |
| `af` | 地址族（Address Family），`NET_AF_INET` 或 `NET_AF_INET6` |
| `proto` | 协议，普通连接为 `NET_IPPROTO_TCP`，HTTPS 为 `NET_IPPROTO_TLS_1_2` |

成功时返回套接字文件描述符（File Descriptor），失败时返回负错误值。不需要自定义配置时，给 `config` 参数传入 `NULL`：

```c
HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10,
                    NULL, NULL, NULL);
```

### 兜底资源（Fallback Resources）

定义 HTTP／HTTPS 服务时，`_res_fallback` 可指定兜底资源，在没有任何其他资源匹配 URL 时使用。例如，为由前端处理路由的单页应用（Single-page Application）返回索引页，或生成自定义 404 响应：

```c
static int default_handler(struct http_client_ctx *client, enum http_transaction_status status,
                   const struct http_request_ctx *request_ctx,
                   struct http_response_ctx *response_ctx, void *user_data)
{
    static const char response_404[] = "Oops, page not found!";

    if (status == HTTP_SERVER_REQUEST_DATA_FINAL) {
        response_ctx->status = 404;
        response_ctx->body = response_404;
        response_ctx->body_len = sizeof(response_404) - 1;
        response_ctx->final_chunk = true;
    }

    return 0;
}

static struct http_resource_detail_dynamic default_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_DYNAMIC,
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
    },
    .cb = default_handler,
    .user_data = NULL,
};

/* Register a fallback resource to handle any unknown path */
HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10, NULL, &default_detail, NULL);
```

> 原文注意事项：HTTPS 服务依赖事先注册好的 TLS 凭据，配置方法见[TLS 凭据子系统](P040_BSD套接字.md#sockets-tls-credentials-subsys)。

服务定义完成后，用 [`HTTP_RESOURCE_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gab177436ac7a8d6589dcfbd416ffd9200) 为它注册资源。启用 [`CONFIG_HTTP_SERVER_RESOURCE_WILDCARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_RESOURCE_WILDCARD) 后，可以让一个处理函数匹配多个路径；匹配使用 POSIX 的 [fnmatch()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fnmatch.html) 函数。

```c
HTTP_RESOURCE_DEFINE(my_resource, my_service, "/foo*", &resource_detail);
```

原文称该规则匹配以 `foo` 开始的 URL；示例中的完整路径模式是 `/foo*`，即匹配以 `/foo` 开始的路径。模式语法见[POSIX.2 第 2.13 节](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_13)。

## 55.4 静态资源（Static Resources）

静态资源内容在构建时定义，之后不可修改。下面将 gzip 压缩网页注册为静态资源：

```c
static const uint8_t index_html_gz[] = {
    #include "index.html.gz.inc"
};

struct http_resource_detail_static index_html_gz_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_STATIC,
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
        .content_encoding = "gzip",
    },
    .static_data = index_html_gz,
    .static_data_len = sizeof(index_html_gz),
};

HTTP_RESOURCE_DEFINE(index_html_gz_resource, my_service, "/",
                     &index_html_gz_resource_detail);
```

资源内容及内容编码（Content Encoding）由应用决定。上述例子可在应用 `CMakeLists.txt` 加入以下内容，在构建时生成 gzip 数据：

```cmake
set(gen_dir ${ZEPHYR_BINARY_DIR}/include/generated/)
set(source_file_index src/index.html)
generate_inc_file_for_target(app ${source_file_index} ${gen_dir}/index.html.gz.inc --gzip)
```

`src/index.html` 是待压缩网页的位置；生成的 `index.html.gz.inc` 被包含进静态字节数组。

## 55.5 静态文件系统资源（Static Filesystem Resources）

原文本节开头称此类资源内容“在构建时定义且不可修改”，并说明它只支持 `GET`，用户不能通过该资源向文件系统上传文件。路径定义示例如下：

```c
struct http_resource_detail_static_fs static_fs_resource_detail = {
    .common = {
        .type                              = HTTP_RESOURCE_TYPE_STATIC_FS,
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
    },
    .fs_path = "/lfs1/www",
};

HTTP_RESOURCE_DEFINE(static_fs_resource, my_service, "*", &static_fs_resource_detail);
```

> 源码核对译注：这里“内容不可修改”的措辞与原页概览不一致。固定的是资源路径映射，文件可由其他代码修改；官方 [`handle_http1_static_fs_resource()`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_server_http1.c) 实际从文件系统打开并读取文件。HTTP 服务只提供读取，不意味着文件系统内容永久不可变。`/lfs1/www` 是设备文件系统的挂载路径，不是作者电脑的仓库路径。

`/lfs1/www` 下的文件向客户端开放。gzip 压缩文件须加 `.gz` 后缀，例如 `index.html.gz`；当客户端请求 `index.html` 时，服务器返回压缩文件，并添加 gzip 内容编码头部。

内容类型（Content Type）按扩展名判断。服务器支持 `.html`、`.js`、`.css`、`.jpg`、`.png` 和 `.svg`；可以用 [`HTTP_SERVER_CONTENT_TYPE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga709ddfe3f5ae5605b3399687f8be8c47) 增加类型，其他文件默认按 `text/html` 提供。例如：

```c
HTTP_SERVER_CONTENT_TYPE(json, "application/json")
```

[`CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE) 配置从静态文件系统向客户端传输内容时，每块响应数据的大小。

## 55.6 动态资源（Dynamic Resources）

动态资源通过注册资源回调，在服务器与应用之间交换数据。下面的处理函数将收到的数据回送给客户端：

```c
static int dyn_handler(struct http_client_ctx *client, enum http_transaction_status status,
                       const struct http_request_ctx *request_ctx,
                       struct http_response_ctx *response_ctx, void *user_data)
{
#define MAX_TEMP_PRINT_LEN 32
    static char print_str[MAX_TEMP_PRINT_LEN];
    enum http_method method = client->method;
    static size_t processed;

    __ASSERT_NO_MSG(request_ctx->data != NULL);

    if (status == HTTP_SERVER_TRANSACTION_ABORTED ||
        status == HTTP_SERVER_TRANSACTION_COMPLETE) {
        if (status == HTTP_SERVER_TRANSACTION_ABORTED) {
            LOG_DBG("Transaction aborted after %zd bytes.", processed);
        }
        processed = 0;
        return 0;
    }

    processed += request_ctx->data_len;

    snprintf(print_str, sizeof(print_str), "%s received (%zd bytes)",
             http_method_str(method), request_ctx->data_len);
    LOG_HEXDUMP_DBG(request_ctx->data, request_ctx->data_len, print_str);

    if (status == HTTP_SERVER_REQUEST_DATA_FINAL) {
        LOG_DBG("All data received (%zd bytes).", processed);
        processed = 0;
    }

    /* Echo data back to client */
    response_ctx->body = request_ctx->data;
    response_ctx->body_len = request_ctx->data_len;
    response_ctx->final_chunk = (status == HTTP_SERVER_REQUEST_DATA_FINAL);

    return 0;
}

struct http_resource_detail_dynamic dyn_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_DYNAMIC,
        .bitmask_of_supported_http_methods =
            BIT(HTTP_GET) | BIT(HTTP_POST),
    },
    .cb = dyn_handler,
    .user_data = NULL,
};

HTTP_RESOURCE_DEFINE(dyn_resource, my_service, "/dynamic",
                     &dyn_resource_detail);
```

> 源码核对译注：原例在检查事务终止状态之前断言 `request_ctx->data != NULL`。但官方 [`http_server_core.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_server_core.c) 的中止通知会提供空数据指针和零长度；因此实际处理时应先处理终止通知，也不能把空请求体误判为错误。本章保留原代码，未将其记作已构建验证的完整程序。

一个请求可能触发多次回调，应用必须记录已收到数据的进度。`status` 表示处理阶段：

| 状态 | 含义及处理 |
| --- | --- |
| [`HTTP_SERVER_REQUEST_DATA_MORE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474) | 还有请求载荷，后续回调会继续提供 |
| [`HTTP_SERVER_REQUEST_DATA_FINAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2) | 所有请求载荷都已交给应用 |
| [`HTTP_SERVER_TRANSACTION_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521) | 处理发生通信错误，例如完整载荷收到前客户端就关闭连接 |
| [`HTTP_SERVER_TRANSACTION_COMPLETE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb) | 整个响应已发送给客户端 |

中止或完成状态都表示该请求处理结束。应用应重置此资源记录的进度，等待新请求。服务器保证同一资源一次只由一个客户端访问。

`request_ctx` 用于向应用提供请求数据：

| 字段 | 含义 |
| --- | --- |
| `data`、`data_len` | 当前请求数据及长度 |
| `headers`、`header_count`、`headers_status` | 启用 [`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_CAPTURE_HEADERS) 后捕获的请求头；只在本次请求的首次回调中填充，详见[访问请求头](#accessing-request-headers) |

应用填写 `response_ctx`，向服务器提供响应数据：

| 字段 | 含义 |
| --- | --- |
| `status` | HTTP 响应状态码；未填写时默认为 `200` |
| `headers`、`header_count` | 应用提供的任意响应头；未填写时默认发送 `Transfer-Encoding` 和 `Content-Type`，回调可覆盖 `Content-Type` |
| `body`、`body_len` | 响应体（Response Body）及长度 |
| `final_chunk` | 标明应用没有更多响应数据需要发送 |

响应头和状态码只能在首次填充的 `response_ctx` 中提供。之后的回调只能继续提供响应体数据。服务器会持续调用回调，直到请求数据全部交给应用，并且应用声明没有更多响应数据。

## 55.7 WebSocket 资源（WebSocket Resources）

WebSocket 资源注册一个应用回调，在连接升级（Connection Upgrade）时调用。原文将传入的描述符描述为对应底层 TCP／TLS 连接的套接字。回调调用后，应用接管该连接，负责在使用结束后释放它。

```c
static int ws_socket;
static uint8_t ws_recv_buffer[1024];

int ws_setup(int sock, struct http_request_ctx *request_ctx, void *user_data)
{
    ws_socket = sock;
    return 0;
}

struct http_resource_detail_websocket ws_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_WEBSOCKET,
        /* We need HTTP/1.1 Get method for upgrading */
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
    },
    .cb = ws_setup,
    .data_buffer = ws_recv_buffer,
    .data_buffer_len = sizeof(ws_recv_buffer),
    .user_data = NULL, /* Fill this for any user specific data */
};

HTTP_RESOURCE_DEFINE(ws_resource, my_service, "/", &ws_resource_detail);
```

这个最小示例仅保存传入的套接字描述符，后续连接处理由应用决定，超出本指南范围。完整 WebSocket 回显服务见[HTTP 服务器示例](P056_HTTP服务器示例.md#sockets-http-server)。

> 源码核对译注：当前官方 [`http_server_ws.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_server_ws.c) 先调用 `websocket_register()` 包装底层连接，再把返回的 WebSocket 描述符传给回调；不能把它当成未经封装的 TCP 数据流直接处理。释放时应遵循 WebSocket 服务端连接的管理接口，而不是套用普通 TCP 描述符的假设。

## 55.8 访问请求头（Accessing Request Headers）

应用可注册需要关注的特定 HTTP 请求头（Request Header）。服务器为每个请求捕获这些头部，动态资源回调可读取它们。

> 原文重要说明：捕获的请求头只在该请求的第一次回调中提供。同一请求的后续回调中，`request_ctx` 的 `headers`、`header_count` 和 `headers_status` 会清空，`headers_status` 变为 [`HTTP_HEADER_STATUS_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)。应用必须在首次回调中复制后续要用的头部值。

第一次回调可能包含请求体，也可能不包含，这取决于请求方法及传输分帧（Transport Framing）。不能以“有无请求体”为条件决定是否处理请求头；应始终检查 `headers_status`，只要它不是 [`HTTP_HEADER_STATUS_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)，就保存需要的字段。

先启用 [`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_CAPTURE_HEADERS)，再注册要捕获的头部，并在动态资源回调中读取。推荐首次回调时复制头部，完整请求体到达后再一起处理：

```c
HTTP_SERVER_REGISTER_HEADER_CAPTURE(capture_user_agent, "User-Agent");

static char user_agent[64];

static int dyn_handler(struct http_client_ctx *client, enum http_transaction_status status,
                       const struct http_request_ctx *request_ctx,
                       struct http_response_ctx *response_ctx, void *user_data)
{
    /* Request headers are only present in the first callback, so copy out
     * any values needed later before they are gone.
     */
    if (request_ctx->headers_status != HTTP_HEADER_STATUS_NONE) {
        for (size_t i = 0; i < request_ctx->header_count; i++) {
            const struct http_header *hdr = &request_ctx->headers[i];

            LOG_INF("Captured header: '%s: %s'", hdr->name, hdr->value);

            if (strcasecmp(hdr->name, "User-Agent") == 0) {
                strncpy(user_agent, hdr->value, sizeof(user_agent) - 1);
            }
        }
    }

    /* Process request body data (may be empty in the first callback). */

    if (status == HTTP_SERVER_REQUEST_DATA_FINAL) {
        /* Full request received: act on the body together with the header
         * values stashed above (e.g. user_agent).
         */
    }

    return 0;
}
```

示例捕获 `User-Agent` 并复制到应用缓冲区。译注：该片段用静态 `user_agent` 保存状态；实际应用须在事务边界清理自己的缓存，避免新请求没有该头部时误用上一次的值。该提示是对示例状态生命周期的补充，不改变原文代码。

## 55.9 API 参考与相关示例（API Reference）

完整参考分别见[HTTP 服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html)和[HTTP 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html)。这两组参考页均列出以下示例：

| 示例 | 用途 |
| --- | --- |
| [HTTP 服务器](P056_HTTP服务器示例.md#sockets-http-server) | 展示 HTTP(S) 服务器和各种资源类型 |
| [Prometheus 示例](P220_Prometheus指标示例.md#prometheus) | 实现展示多种指标类型（Metric Type）的 Prometheus 指标服务器 |

本指南不代替详细 API 页的翻译。本轮未构建服务、进行 HTTP 协议或资源并发测试。


<a id="http-server"></a>
<a id="http-server-interface"></a>
<a id="contents"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="id12"></a>
<a id="id13"></a>
<a id="id14"></a>
<a id="id15"></a>
<a id="id16"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="server-setup"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="sample-usage"></a>
<a id="services"></a>
<a id="per-service-configuration"></a>
<a id="fallback-resources"></a>
<a id="static-resources"></a>
<a id="id4"></a>
<a id="static-filesystem-resources"></a>
<a id="dynamic-resources"></a>
<a id="websocket-resources"></a>
<a id="accessing-request-headers"></a>
<a id="http-server-interface-accessing-request-headers"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：WebSocket客户端](P053_WebSocket客户端.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：MQTT客户端库](P059_MQTT客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P054_WebSocket客户端示例.md) · [返回大纲](大纲.md) · [下一章](P056_HTTP服务器示例.md)

</details>

<!-- reading-navigation:end -->
