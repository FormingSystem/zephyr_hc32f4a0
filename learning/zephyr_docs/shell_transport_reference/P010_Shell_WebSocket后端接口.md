---
id: learning.zephyr-docs.shell-transport-reference.page-10
title: Shell_WebSocket后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__websocket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Shell\_WebSocket后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__websocket.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

通过WebSocket连接访问Shell。

<a id="details"></a>

通过WebSocket连接访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_shell_5Fwebsocket_2Eh"></a>

```c
file shell_websocket.h
```

相关声明：[shell_websocket.h](P011_Shell_WebSocket后端头文件参考.md)。

Shell WebSocket后端（WebSocket Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga726a23776948ff246176c1ac2c88daa6"></a>

```c
#define WEBSOCKET_CONSOLE_DEFINE(_service, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[WEBSOCKET_CONSOLE_DEFINE](#ga726a23776948ff246176c1ac2c88daa6)。

定义WebSocket Shell服务（Service）。

<a id="r_ga134a7de93ded994b49fd781fb289e876"></a>

```c
#define WEBSOCKET_CONSOLE_ENABLE(_service)
```

相关声明：[WEBSOCKET_CONSOLE_ENABLE](#ga134a7de93ded994b49fd781fb289e876)。

启用使用WEBSOCKET_CONSOLE_DEFINE定义的WebSocket Shell服务。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga726a23776948ff246176c1ac2c88daa6"></a>

### `WEBSOCKET_CONSOLE_DEFINE`

```c
#define WEBSOCKET_CONSOLE_DEFINE ( _service, _sec_tag_list, _sec_tag_list_size )
```

```c
#include <zephyr/shell/shell_websocket.h>
```

展开值（Value）：

```c
static uint16_t SHELL_WS_PORT_NAME(_service) =                  \
        CONFIG_SHELL_WEBSOCKET_PORT;                            \
HTTP_SERVICE_DEFINE(_service,                                   \
                    CONFIG_SHELL_WEBSOCKET_IP_ADDR,             \
                    &SHELL_WS_PORT_NAME(_service),              \
                    SHELL_WEBSOCKET_SERVICE_COUNT,              \
                    SHELL_WEBSOCKET_SERVICE_COUNT,              \
                    NULL, NULL, NULL);                          \
DEFINE_WEBSOCKET_SERVICE(_service)
```

定义WebSocket Shell服务（Service）。

定义WebSocket Shell传输对象、对应Shell实例，以及在CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL端点暴露该实例的HTTP(S)服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | WebSocket服务实例的名称。 |
| `_sec_tag_list` | 用于安全HTTPS连接的传输层安全（TLS）安全标签列表（Security Tag List）。未启用TLS时忽略。 |
| `_sec_tag_list_size` | _sec_tag_list中的条目数。 |

<a id="ga134a7de93ded994b49fd781fb289e876"></a>

### `WEBSOCKET_CONSOLE_ENABLE`

```c
#define WEBSOCKET_CONSOLE_ENABLE ( _service)
```

```c
#include <zephyr/shell/shell_websocket.h>
```

展开值（Value）：

```c
(void)shell_websocket_enable(&GET_WS_SHELL_NAME(_service))
```

启用使用WEBSOCKET_CONSOLE_DEFINE定义的WebSocket Shell服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | WebSocket服务实例的名称。 |

## 10.4\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_websocket.h](../../../include/zephyr/shell/shell_websocket.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：WEBSOCKET_CONSOLE_DEFINE在编译期同时定义Shell传输、Shell实例与HTTP资源。CONFIG_NET_SOCKETS_SOCKOPT_TLS选择HTTPS或普通HTTP分支；未启用TLS时安全标签参数不参与普通HTTP服务定义。

> 译注——源码核对：资源只支持HTTP GET用于WebSocket升级（Upgrade），路径由斜杠和CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL组成。不要把HTTP资源定义理解成已经建立了客户端会话。

> 译注——源码核对：WEBSOCKET_CONSOLE_ENABLE调用shell_websocket_enable，但宏显式丢弃其返回值。底层函数返回shell_init结果；宏调用结束本身不提供可检查的初始化成功状态。

> 译注——源码核对：源码中的输入缓冲、套接字锁和延迟工作属于实现内部结构。原始源码页可见它们不代表官方为全部内部字段提供独立的公共API契约。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.5\_原页交叉引用（Cross References）

- [shell_websocket.h](P011_Shell_WebSocket后端头文件参考.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

---

[上一章](P009_Shell_Telnet后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P011_Shell_WebSocket后端头文件参考.md)
