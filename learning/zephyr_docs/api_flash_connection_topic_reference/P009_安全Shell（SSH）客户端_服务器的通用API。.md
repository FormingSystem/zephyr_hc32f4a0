---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-9
title: 安全Shell（SSH）客户端_服务器的通用API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_安全Shell（SSH）客户端\_服务器的通用API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 版提供（Since 4.5）；接口版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_ssh_5Fchannel_5Fevent_5Fchannel_5Frequest"></a>

```c
struct ssh_channel_event_channel_request
```

相关声明：[ssh_channel_event_channel_request](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md)。

SSH_CHANNEL_EVENT_REQUEST事件的数据。

<a id="r_ssh_5Fchannel_5Fevent_5Fchannel_5Frequest_5Fresult"></a>

```c
struct ssh_channel_event_channel_request_result
```

相关声明：[ssh_channel_event_channel_request_result](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md)。

SSH_CHANNEL_EVENT_REQUEST_RESULT事件的数据。

<a id="r_ssh_5Fchannel_5Fevent"></a>

```c
struct ssh_channel_event
```

相关声明：[ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)。

SSH通道事件信息（Channel Event Information）。

<a id="r_ssh_5Ftransport_5Fevent_5Fauthenticate_5Fresult"></a>

```c
struct ssh_transport_event_authenticate_result
```

相关声明：[ssh_transport_event_authenticate_result](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md)。

SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT事件的数据。

<a id="r_ssh_5Ftransport_5Fevent_5Fchannel_5Fopen"></a>

```c
struct ssh_transport_event_channel_open
```

相关声明：[ssh_transport_event_channel_open](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md)。

SSH_TRANSPORT_EVENT_CHANNEL_OPEN事件的数据。

<a id="r_ssh_5Ftransport_5Fevent"></a>

```c
struct ssh_transport_event
```

相关声明：[ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)。

SSH传输事件信息（Transport Event Information）。

<a id="r_ssh_5Ftransport_5Fconf"></a>

```c
struct ssh_transport_conf
```

相关声明：[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

SSH传输回调（Transport Callback）的配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga56f51b1f1c4c9d131eebc65ce5b975ee"></a>

```c
#define SSH_EXTENDED_DATA_STDERR 1
```

相关声明：[SSH_EXTENDED_DATA_STDERR](#ga56f51b1f1c4c9d131eebc65ce5b975ee)。

标准错误通道数据（Standard Error Channel Data）的扩展数据类型。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_ga3f29b8eb5acf4b91aeb07873b2df7d56"></a>

```c
typedef int(* ssh_channel_event_callback_t) (struct ssh_channel *channel, const struct ssh_channel_event *event, void *user_data)
```

相关声明：[ssh_channel_event_callback_t](#ga3f29b8eb5acf4b91aeb07873b2df7d56)、[ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)。

安全外壳（SSH）通道事件回调（Channel Event Callback）。

<a id="r_gaed450ebb53a676fafc58bb6cfe82a448"></a>

```c
typedef int(* ssh_transport_event_callback_t) (struct ssh_transport *transport, const struct ssh_transport_event *event, void *user_data)
```

相关声明：[ssh_transport_event_callback_t](#gaed450ebb53a676fafc58bb6cfe82a448)、[ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)。

安全外壳（SSH）传输事件回调（Transport Event Callback）。

<a id="r_ga9f6f03ef86ffee24da6e7fb6adc82878"></a>

```c
typedef void(* ssh_service_client_cb_t) (struct ssh_client *ssh, int instance, void *user_data)
```

相关声明：[ssh_service_client_cb_t](#ga9f6f03ef86ffee24da6e7fb6adc82878)。

遍历 SSH 客户端连接（Client Connections）时使用的回调。

<a id="r_gaf53f661268138d4a36875fb079983c2a"></a>

```c
typedef void(* ssh_service_server_cb_t) (struct ssh_server *sshd, int instance, void *user_data)
```

相关声明：[ssh_service_server_cb_t](#gaf53f661268138d4a36875fb079983c2a)。

遍历 SSH 服务器连接（Server Connections）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_ga6c8271f6fe11a5779a7f05a232c28d84"></a>

```c
enum ssh_auth_type { SSH_AUTH_NONE , SSH_AUTH_PASSWORD , SSH_AUTH_PUBKEY }
```

相关声明：[ssh_auth_type](#ga6c8271f6fe11a5779a7f05a232c28d84)、[SSH_AUTH_NONE](#gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd)、[SSH_AUTH_PASSWORD](#gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe)、[SSH_AUTH_PUBKEY](#gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314)。

SSH 传输支持的认证方法（Authentication Methods）。

<a id="r_ga9341ecffa2ca568ed8312b7c7bd5b416"></a>

```c
enum ssh_channel_request_type { SSH_CHANNEL_REQUEST_UNKNOWN , SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL , SSH_CHANNEL_REQUEST_X11_FORWARD , SSH_CHANNEL_REQUEST_ENV_VAR , SSH_CHANNEL_REQUEST_SHELL , SSH_CHANNEL_REQUEST_EXEC , SSH_CHANNEL_REQUEST_SUBSYSTEM , SSH_CHANNEL_REQUEST_WINDOW_CHANGE , SSH_CHANNEL_REQUEST_FLOW_CONTROL , SSH_CHANNEL_REQUEST_SIGNAL , SSH_CHANNEL_REQUEST_EXIT_STATUS , SSH_CHANNEL_REQUEST_EXIT_SIGNAL }
```

相关声明：[ssh_channel_request_type](#ga9341ecffa2ca568ed8312b7c7bd5b416)、[SSH_CHANNEL_REQUEST_UNKNOWN](#gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f)、[SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL](#gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622)、[SSH_CHANNEL_REQUEST_X11_FORWARD](#gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db)、[SSH_CHANNEL_REQUEST_ENV_VAR](#gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5)、[SSH_CHANNEL_REQUEST_SHELL](#gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40)、[SSH_CHANNEL_REQUEST_EXEC](#gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c)、[SSH_CHANNEL_REQUEST_SUBSYSTEM](#gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d)、[SSH_CHANNEL_REQUEST_WINDOW_CHANGE](#gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952)、[SSH_CHANNEL_REQUEST_FLOW_CONTROL](#gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0)、[SSH_CHANNEL_REQUEST_SIGNAL](#gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0)、[SSH_CHANNEL_REQUEST_EXIT_STATUS](#gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378)、[SSH_CHANNEL_REQUEST_EXIT_SIGNAL](#gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0)。

SSH 通道请求类型（Channel Request Types）。

<a id="r_gaba3db037a1fbeca22f2c3c30063788b9"></a>

```c
enum ssh_channel_event_type { SSH_CHANNEL_EVENT_OPEN_RESULT , SSH_CHANNEL_EVENT_REQUEST , SSH_CHANNEL_EVENT_REQUEST_RESULT , SSH_CHANNEL_EVENT_RX_DATA_READY , SSH_CHANNEL_EVENT_TX_DATA_READY , SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY , SSH_CHANNEL_EVENT_EOF , SSH_CHANNEL_EVENT_CLOSED }
```

相关声明：[ssh_channel_event_type](#gaba3db037a1fbeca22f2c3c30063788b9)、[SSH_CHANNEL_EVENT_OPEN_RESULT](#ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced)、[SSH_CHANNEL_EVENT_REQUEST](#ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611)、[SSH_CHANNEL_EVENT_REQUEST_RESULT](#ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330)、[SSH_CHANNEL_EVENT_RX_DATA_READY](#ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f)、[SSH_CHANNEL_EVENT_TX_DATA_READY](#ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32)、[SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY](#ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249)、[SSH_CHANNEL_EVENT_EOF](#ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2)、[SSH_CHANNEL_EVENT_CLOSED](#ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e)。

安全外壳（SSH）通道所发出的事件类型。

<a id="r_ga578aed0a10600bc7a248dbb64ca13cc2"></a>

```c
enum ssh_transport_event_type { SSH_TRANSPORT_EVENT_CLOSED , SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED , SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT , SSH_TRANSPORT_EVENT_CHANNEL_OPEN }
```

相关声明：[ssh_transport_event_type](#ga578aed0a10600bc7a248dbb64ca13cc2)、[SSH_TRANSPORT_EVENT_CLOSED](#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)、[SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED](#gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3)、[SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT](#gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a)、[SSH_TRANSPORT_EVENT_CHANNEL_OPEN](#gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9)。

SSH 传输层发出的事件类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga691a9ba0d4c2bb1cf637990a4aa91f26"></a>

```c
const char * ssh_transport_client_user_name (struct ssh_transport *transport)
```

相关声明：[ssh_transport_client_user_name](#ga691a9ba0d4c2bb1cf637990a4aa91f26)。

获取某传输中已认证客户端的用户名（Authenticated Client Username）。

<a id="r_gaa3b9133aff9d5be3b258db48ba99b601"></a>

```c
int ssh_transport_auth_password (struct ssh_transport *transport, const char *user_name, const char *password)
```

相关声明：[ssh_transport_auth_password](#gaa3b9133aff9d5be3b258db48ba99b601)。

使用密码（Password）认证 SSH 传输。

<a id="r_ga1e8ec722a451a466904d077fd4b22a16"></a>

```c
int ssh_transport_channel_open (struct ssh_transport *transport, ssh_channel_event_callback_t callback, void *user_data)
```

相关声明：[ssh_transport_channel_open](#ga1e8ec722a451a466904d077fd4b22a16)、[ssh_channel_event_callback_t](#ga3f29b8eb5acf4b91aeb07873b2df7d56)。

在 SSH 传输上打开新通道（Channel）。

<a id="r_ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e"></a>

```c
int ssh_channel_open_result (struct ssh_channel *channel, bool success, ssh_channel_event_callback_t callback, void *user_data)
```

相关声明：[ssh_channel_open_result](#ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_channel_event_callback_t](#ga3f29b8eb5acf4b91aeb07873b2df7d56)。

响应通道打开请求（Channel Open Request）。

<a id="r_ga5832386d60c9fdd46c2198b45905be73"></a>

```c
int ssh_channel_request_result (struct ssh_channel *channel, bool success)
```

相关声明：[ssh_channel_request_result](#ga5832386d60c9fdd46c2198b45905be73)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

响应通道请求（Channel Request）。

<a id="r_ga52f058c2b51df404b9399f8188dcfe8d"></a>

```c
int ssh_channel_request_shell (struct ssh_channel *channel)
```

相关声明：[ssh_channel_request_shell](#ga52f058c2b51df404b9399f8188dcfe8d)。

在通道上请求交互式 Shell（Interactive Shell）。

<a id="r_ga6205c8f8d3fd6f0c457261d6cf355940"></a>

```c
int ssh_channel_read (struct ssh_channel *channel, void *data, uint32_t len)
```

相关声明：[ssh_channel_read](#ga6205c8f8d3fd6f0c457261d6cf355940)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取通道数据（Channel Data）。

<a id="r_ga658c9f84ec08797b50fb57e2415f7e3d"></a>

```c
int ssh_channel_write (struct ssh_channel *channel, const void *data, uint32_t len)
```

相关声明：[ssh_channel_write](#ga658c9f84ec08797b50fb57e2415f7e3d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入通道数据（Channel Data）。

<a id="r_ga5e0d58687f17df1f5c2480ceadcbde72"></a>

```c
int ssh_channel_read_stderr (struct ssh_channel *channel, void *data, uint32_t len)
```

相关声明：[ssh_channel_read_stderr](#ga5e0d58687f17df1f5c2480ceadcbde72)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取通道的标准错误数据（Standard Error Data）。

<a id="r_ga7fa2613a763415d19c9c6e7926ead074"></a>

```c
int ssh_channel_write_stderr (struct ssh_channel *channel, const void *data, uint32_t len)
```

相关声明：[ssh_channel_write_stderr](#ga7fa2613a763415d19c9c6e7926ead074)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入通道的标准错误数据（Standard Error Data）。

<a id="r_ga7c510e44353e7e791c8f13af3a554739"></a>

```c
int ssh_channel_close (struct ssh_channel *channel)
```

相关声明：[ssh_channel_close](#ga7c510e44353e7e791c8f13af3a554739)。

关闭 SSH 通道（Channel）。

<a id="r_gafb6780adc3007639184e634f1a7ec73a"></a>

```c
void ssh_client_foreach (ssh_service_client_cb_t cb, void *user_data)
```

相关声明：[ssh_client_foreach](#gafb6780adc3007639184e634f1a7ec73a)、[ssh_service_client_cb_t](#ga9f6f03ef86ffee24da6e7fb6adc82878)。

遍历所有 SSH 客户端连接（Client Connections）。

<a id="r_gaff36f18836543d259ee7420bdb757e1f"></a>

```c
void ssh_server_foreach (ssh_service_server_cb_t cb, void *user_data)
```

相关声明：[ssh_server_foreach](#gaff36f18836543d259ee7420bdb757e1f)、[ssh_service_server_cb_t](#gaf53f661268138d4a36875fb079983c2a)。

遍历所有 SSH 服务器连接（Server Connections）。

<a id="r_ga41ef319c12ce50fe226152eb654a6d56"></a>

```c
int ssh_transport_traverse_callbacks (bool is_server, struct ssh_transport *transport, const struct ssh_transport_event *event)
```

相关声明：[ssh_transport_traverse_callbacks](#ga41ef319c12ce50fe226152eb654a6d56)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)。

为所给传输（Transport）调用用户配置的回调。

## 9.6\_详细说明（Detailed Documentation）

<a id="ga56f51b1f1c4c9d131eebc65ce5b975ee"></a>

### `SSH_EXTENDED_DATA_STDERR`

```c
#define SSH_EXTENDED_DATA_STDERR 1
```

```c
#include <zephyr/net/ssh/common.h>
```

标准错误通道数据（Standard Error Channel Data）的扩展数据类型。

<a id="ga3f29b8eb5acf4b91aeb07873b2df7d56"></a>

### `ssh_channel_event_callback_t`

```c
typedef int(* ssh_channel_event_callback_t) (struct ssh_channel *channel, const struct ssh_channel_event *event, void *user_data)
```

```c
#include <zephyr/net/ssh/common.h>
```

安全外壳（SSH）通道事件回调（Channel Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向产生该事件的 SSH 通道（SSH Channel）的指针。 |
| `event` | 指向通道事件数据（Channel Event Data）的指针。 |
| `user_data` | 用户提供的上下文指针（Context Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga9f6f03ef86ffee24da6e7fb6adc82878"></a>

### `ssh_service_client_cb_t`

```c
typedef void(* ssh_service_client_cb_t) (struct ssh_client *ssh, int instance, void *user_data)
```

```c
#include <zephyr/net/ssh/common.h>
```

遍历 SSH 客户端连接（Client Connections）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ssh` | 指向 SSH 客户端实例（SSH Client Instance）的指针。 |
| `instance` | SSH 客户端实例标识符（SSH Client Instance ID）。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gaf53f661268138d4a36875fb079983c2a"></a>

### `ssh_service_server_cb_t`

```c
typedef void(* ssh_service_server_cb_t) (struct ssh_server *sshd, int instance, void *user_data)
```

```c
#include <zephyr/net/ssh/common.h>
```

遍历 SSH 服务器连接（Server Connections）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sshd` | 指向 SSH 服务器实例（Server Instance）的指针。 |
| `instance` | SSH 服务器实例标识符（SSH Server Instance ID）。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gaed450ebb53a676fafc58bb6cfe82a448"></a>

### `ssh_transport_event_callback_t`

```c
typedef int(* ssh_transport_event_callback_t) (struct ssh_transport *transport, const struct ssh_transport_event *event, void *user_data)
```

```c
#include <zephyr/net/ssh/common.h>
```

安全外壳（SSH）传输事件回调（Transport Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 指向产生该事件的 SSH 传输（SSH Transport）的指针。 |
| `event` | 指向传输事件数据（Transport Event Data）的指针。 |
| `user_data` | 用户提供的上下文指针（Context Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga6c8271f6fe11a5779a7f05a232c28d84"></a>

### `ssh_auth_type`

```c
enum ssh_auth_type
```

```c
#include <zephyr/net/ssh/common.h>
```

SSH 传输支持的认证方法（Authentication Methods）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_AUTH_NONE` | 未选择身份验证方法（Authentication Method）。 |
| `SSH_AUTH_PASSWORD` | 用户名和密码身份验证（Username and Password Authentication）。 |
| `SSH_AUTH_PUBKEY` | 公钥身份验证（Public Key Authentication）。 |

<a id="gaba3db037a1fbeca22f2c3c30063788b9"></a>

### `ssh_channel_event_type`

```c
enum ssh_channel_event_type
```

```c
#include <zephyr/net/ssh/common.h>
```

安全外壳（SSH）通道所发出的事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_CHANNEL_EVENT_OPEN_RESULT` | 客户端打开请求（Open Request）的结果。 |
| `SSH_CHANNEL_EVENT_REQUEST` | 服务器收到的通道请求（Incoming Channel Request）。 |
| `SSH_CHANNEL_EVENT_REQUEST_RESULT` | 客户端先前发送的通道请求（Channel Request）的结果。 |
| `SSH_CHANNEL_EVENT_RX_DATA_READY` | 有通道数据（Channel Data）可供读取。 |
| `SSH_CHANNEL_EVENT_TX_DATA_READY` | 通道可接受更多发送数据（Transmit Data）。 |
| `SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY` | 有标准错误数据（Standard Error Data）可供读取。 |
| `SSH_CHANNEL_EVENT_EOF` | 通道已收到文件结束标记（End-of-file）。 |
| `SSH_CHANNEL_EVENT_CLOSED` | 通道（Channel）已关闭。 |

<a id="ga9341ecffa2ca568ed8312b7c7bd5b416"></a>

### `ssh_channel_request_type`

```c
enum ssh_channel_request_type
```

```c
#include <zephyr/net/ssh/common.h>
```

SSH 通道请求类型（Channel Request Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_CHANNEL_REQUEST_UNKNOWN` | 未知或不支持的通道请求类型（Channel Request Type）。 |
| `SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL` | 请求伪终端（Pseudo-terminal）。 |
| `SSH_CHANNEL_REQUEST_X11_FORWARD` | 请求 X11 转发（X11 Forwarding）。 |
| `SSH_CHANNEL_REQUEST_ENV_VAR` | 设置环境变量（Environment Variable）。 |
| `SSH_CHANNEL_REQUEST_SHELL` | 启动交互式 Shell（Interactive Shell）。 |
| `SSH_CHANNEL_REQUEST_EXEC` | 执行命令（Command）。 |
| `SSH_CHANNEL_REQUEST_SUBSYSTEM` | 启动子系统（Subsystem）。 |
| `SSH_CHANNEL_REQUEST_WINDOW_CHANGE` | 通知终端窗口大小变化（Terminal Window Size Changes）。 |
| `SSH_CHANNEL_REQUEST_FLOW_CONTROL` | 请求流量控制（Flow Control）。 |
| `SSH_CHANNEL_REQUEST_SIGNAL` | 向远端进程发送信号（Signal）。 |
| `SSH_CHANNEL_REQUEST_EXIT_STATUS` | 报告进程退出状态（Process Exit Status）。 |
| `SSH_CHANNEL_REQUEST_EXIT_SIGNAL` | 报告进程退出信号（Process Exit Signal）。 |

<a id="ga578aed0a10600bc7a248dbb64ca13cc2"></a>

### `ssh_transport_event_type`

```c
enum ssh_transport_event_type
```

```c
#include <zephyr/net/ssh/common.h>
```

SSH 传输层发出的事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_TRANSPORT_EVENT_CLOSED` | 传输（Transport）已关闭。 |
| `SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED` | 请求的 SSH 服务（SSH Service）已被对端接受。 |
| `SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT` | 身份验证尝试结果（Authentication Attempt Result）。 |
| `SSH_TRANSPORT_EVENT_CHANNEL_OPEN` | 服务器收到打开通道（Open Channel）的请求。 |

<a id="ga7c510e44353e7e791c8f13af3a554739"></a>

### `ssh_channel_close()`

```c
int ssh_channel_close ( struct ssh_channel * channel)
```

```c
#include <zephyr/net/ssh/common.h>
```

关闭 SSH 通道（Channel）。

向对端发送通道关闭消息（Channel Close Message），并释放通道。成功后不得再使用该通道句柄（Channel Handle）。若存在关联的通道回调，则该回调会收到 `SSH_CHANNEL_EVENT_CLOSED` 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e"></a>

### `ssh_channel_open_result()`

```c
int ssh_channel_open_result ( struct ssh_channel * channel, bool success, ssh_channel_event_callback_t callback, void * user_data )
```

```c
#include <zephyr/net/ssh/common.h>
```

响应通道打开请求（Channel Open Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `success` | `True` 表示接受打开请求（Open Request），`false` 表示拒绝。 |
| `callback` | 要与已打开通道关联的通道事件回调（Channel Event Callback）。 |
| `user_data` | 传给回调的用户上下文指针（User-provided Context Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga6205c8f8d3fd6f0c457261d6cf355940"></a>

### `ssh_channel_read()`

```c
int ssh_channel_read ( struct ssh_channel * channel, void * data, uint32_t len )
```

```c
#include <zephyr/net/ssh/common.h>
```

读取通道数据（Channel Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `data` | 用于存储已接收数据（Received Data）的缓冲区。 |
| `len` | 最多读取的字节数。 |

**返回（Returns）**：返回值（Returns）：读取的字节数；失败时为负错误码（Negative Error Code）。

<a id="ga5e0d58687f17df1f5c2480ceadcbde72"></a>

### `ssh_channel_read_stderr()`

```c
int ssh_channel_read_stderr ( struct ssh_channel * channel, void * data, uint32_t len )
```

```c
#include <zephyr/net/ssh/common.h>
```

读取通道的标准错误数据（Standard Error Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `data` | 用于存储已接收标准错误数据（Standard Error Data）的缓冲区。 |
| `len` | 最多读取的字节数。 |

**返回（Returns）**：返回值（Returns）：读取的字节数；失败时为负错误码（Negative Error Code）。

<a id="ga5832386d60c9fdd46c2198b45905be73"></a>

### `ssh_channel_request_result()`

```c
int ssh_channel_request_result ( struct ssh_channel * channel, bool success )
```

```c
#include <zephyr/net/ssh/common.h>
```

响应通道请求（Channel Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `success` | 请求成功时为 `True`，否则为 `false`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga52f058c2b51df404b9399f8188dcfe8d"></a>

### `ssh_channel_request_shell()`

```c
int ssh_channel_request_shell ( struct ssh_channel * channel)
```

```c
#include <zephyr/net/ssh/common.h>
```

在通道上请求交互式 Shell（Interactive Shell）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga658c9f84ec08797b50fb57e2415f7e3d"></a>

### `ssh_channel_write()`

```c
int ssh_channel_write ( struct ssh_channel * channel, const void * data, uint32_t len )
```

```c
#include <zephyr/net/ssh/common.h>
```

写入通道数据（Channel Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `data` | 包含待发送数据（Data to Send）的缓冲区。 |
| `len` | 要写入的字节数。 |

**返回（Returns）**：返回值（Returns）：写入的字节数；失败时为负错误码（Negative Error Code）。

<a id="ga7fa2613a763415d19c9c6e7926ead074"></a>

### `ssh_channel_write_stderr()`

```c
int ssh_channel_write_stderr ( struct ssh_channel * channel, const void * data, uint32_t len )
```

```c
#include <zephyr/net/ssh/common.h>
```

写入通道的标准错误数据（Standard Error Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 指向 SSH 通道（SSH Channel）的指针。 |
| `data` | 包含待发送标准错误数据（Standard Error Data）的缓冲区。 |
| `len` | 要写入的字节数。 |

**返回（Returns）**：返回值（Returns）：写入的字节数；失败时为负错误码（Negative Error Code）。

<a id="gafb6780adc3007639184e634f1a7ec73a"></a>

### `ssh_client_foreach()`

```c
void ssh_client_foreach ( ssh_service_client_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/ssh/common.h>
```

遍历所有 SSH 客户端连接（Client Connections）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gaff36f18836543d259ee7420bdb757e1f"></a>

### `ssh_server_foreach()`

```c
void ssh_server_foreach ( ssh_service_server_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/ssh/common.h>
```

遍历所有 SSH 服务器连接（Server Connections）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gaa3b9133aff9d5be3b258db48ba99b601"></a>

### `ssh_transport_auth_password()`

```c
int ssh_transport_auth_password ( struct ssh_transport * transport, const char * user_name, const char * password )
```

```c
#include <zephyr/net/ssh/common.h>
```

使用密码（Password）认证 SSH 传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 指向 SSH 传输（SSH Transport）的指针。 |
| `user_name` | 用于身份验证（Authentication）的用户名（Username）。 |
| `password` | 用于身份验证（Authentication）的密码（Password）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga1e8ec722a451a466904d077fd4b22a16"></a>

### `ssh_transport_channel_open()`

```c
int ssh_transport_channel_open ( struct ssh_transport * transport, ssh_channel_event_callback_t callback, void * user_data )
```

```c
#include <zephyr/net/ssh/common.h>
```

在 SSH 传输上打开新通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 指向 SSH 传输（SSH Transport）的指针。 |
| `callback` | 新通道的通道事件回调（Channel Event Callback）。 |
| `user_data` | 传给回调的用户上下文指针（User-provided Context Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga691a9ba0d4c2bb1cf637990a4aa91f26"></a>

### `ssh_transport_client_user_name()`

```c
const char * ssh_transport_client_user_name ( struct ssh_transport * transport)
```

```c
#include <zephyr/net/ssh/common.h>
```

获取某传输中已认证客户端的用户名（Authenticated Client Username）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 指向 SSH 传输（SSH Transport）的指针。 |

**返回（Returns）**：返回值（Returns）：指向用户名字符串（Username String）的指针。

<a id="ga41ef319c12ce50fe226152eb654a6d56"></a>

### `ssh_transport_traverse_callbacks()`

```c
int ssh_transport_traverse_callbacks ( bool is_server, struct ssh_transport * transport, const struct ssh_transport_event * event )
```

```c
#include <zephyr/net/ssh/common.h>
```

为所给传输（Transport）调用用户配置的回调。

本函数调用用户为给定传输（Transport）配置的回调。SSH 传输通过本函数向用户通知身份验证结果、通道打开请求、通道数据等事件。本函数遍历已配置回调列表，并将提供的传输和事件信息传给每个回调。注意，回调不得调用传输注册或注销 API，否则可能导致死锁（Deadlock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `is_server` | 设为 `true` 时遍历已配置的服务器回调（Server Callbacks）；设为 `false` 时遍历已配置的客户端回调（Client Callbacks）。 |
| `transport` | 传给用户指定回调（Callback）的传输（Transport）。 |
| `event` | 传给用户回调（User Callback）的事件信息（Event Information）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；传输角色（Transport Role）与分派角色（Dispatch Role）不匹配，即服务器与客户端角色不匹配时，为 `-EINVAL`。


## 9.7\_原页交叉引用（Cross References）

- [ssh_channel_event_channel_request](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md)
- [ssh_channel_event_channel_request_result](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md)
- [ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)
- [ssh_transport_event_authenticate_result](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md)
- [ssh_transport_event_channel_open](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md)
- [ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/net/ssh/common.h](../api_file_serial_motion_reference/P004_zephyr__net__ssh__common.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd"></a>
<a id="gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe"></a>
<a id="gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2"></a>
<a id="ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378"></a>
<a id="gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0"></a>
<a id="gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8"></a>
<a id="gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3"></a>
<a id="gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a"></a>
<a id="gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_实时传输协议（Real-time Transport Protocol，RTP）.md) · [返回大纲](大纲.md) · [下一章](P010_USB Type-C 端口控制器驱动后端 API.md)
