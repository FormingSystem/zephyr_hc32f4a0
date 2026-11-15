---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-4
title: zephyr__net__ssh__common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_ssh\_\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全Shell（SSH）客户端/服务器的通用API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

安全Shell（SSH）客户端/服务器的通用API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_ga56f51b1f1c4c9d131eebc65ce5b975ee"></a>

```c
#define SSH_EXTENDED_DATA_STDERR 1
```

相关声明：[SSH_EXTENDED_DATA_STDERR](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga56f51b1f1c4c9d131eebc65ce5b975ee)。

标准错误通道数据（Standard Error Channel Data）的扩展数据类型。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga3f29b8eb5acf4b91aeb07873b2df7d56"></a>

```c
typedef int(* ssh_channel_event_callback_t) (struct ssh_channel *channel, const struct ssh_channel_event *event, void *user_data)
```

相关声明：[ssh_channel_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga3f29b8eb5acf4b91aeb07873b2df7d56)、[ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)。

安全外壳（SSH）通道事件回调（Channel Event Callback）。

<a id="r_gaed450ebb53a676fafc58bb6cfe82a448"></a>

```c
typedef int(* ssh_transport_event_callback_t) (struct ssh_transport *transport, const struct ssh_transport_event *event, void *user_data)
```

相关声明：[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)、[ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)。

安全外壳（SSH）传输事件回调（Transport Event Callback）。

<a id="r_ga9f6f03ef86ffee24da6e7fb6adc82878"></a>

```c
typedef void(* ssh_service_client_cb_t) (struct ssh_client *ssh, int instance, void *user_data)
```

相关声明：[ssh_service_client_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9f6f03ef86ffee24da6e7fb6adc82878)。

遍历 SSH 客户端连接（Client Connections）时使用的回调。

<a id="r_gaf53f661268138d4a36875fb079983c2a"></a>

```c
typedef void(* ssh_service_server_cb_t) (struct ssh_server *sshd, int instance, void *user_data)
```

相关声明：[ssh_service_server_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaf53f661268138d4a36875fb079983c2a)。

遍历 SSH 服务器连接（Server Connections）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga6c8271f6fe11a5779a7f05a232c28d84"></a>

```c
enum ssh_auth_type { SSH_AUTH_NONE , SSH_AUTH_PASSWORD , SSH_AUTH_PUBKEY }
```

相关声明：[ssh_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6c8271f6fe11a5779a7f05a232c28d84)、[SSH_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd)、[SSH_AUTH_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe)、[SSH_AUTH_PUBKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314)。

SSH 传输支持的认证方法（Authentication Methods）。

<a id="r_ga9341ecffa2ca568ed8312b7c7bd5b416"></a>

```c
enum ssh_channel_request_type { SSH_CHANNEL_REQUEST_UNKNOWN , SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL , SSH_CHANNEL_REQUEST_X11_FORWARD , SSH_CHANNEL_REQUEST_ENV_VAR , SSH_CHANNEL_REQUEST_SHELL , SSH_CHANNEL_REQUEST_EXEC , SSH_CHANNEL_REQUEST_SUBSYSTEM , SSH_CHANNEL_REQUEST_WINDOW_CHANGE , SSH_CHANNEL_REQUEST_FLOW_CONTROL , SSH_CHANNEL_REQUEST_SIGNAL , SSH_CHANNEL_REQUEST_EXIT_STATUS , SSH_CHANNEL_REQUEST_EXIT_SIGNAL }
```

相关声明：[ssh_channel_request_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9341ecffa2ca568ed8312b7c7bd5b416)、[SSH_CHANNEL_REQUEST_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f)、[SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622)、[SSH_CHANNEL_REQUEST_X11_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db)、[SSH_CHANNEL_REQUEST_ENV_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5)、[SSH_CHANNEL_REQUEST_SHELL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40)、[SSH_CHANNEL_REQUEST_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c)、[SSH_CHANNEL_REQUEST_SUBSYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d)、[SSH_CHANNEL_REQUEST_WINDOW_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952)、[SSH_CHANNEL_REQUEST_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0)、[SSH_CHANNEL_REQUEST_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0)、[SSH_CHANNEL_REQUEST_EXIT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378)、[SSH_CHANNEL_REQUEST_EXIT_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0)。

SSH 通道请求类型（Channel Request Types）。

<a id="r_gaba3db037a1fbeca22f2c3c30063788b9"></a>

```c
enum ssh_channel_event_type { SSH_CHANNEL_EVENT_OPEN_RESULT , SSH_CHANNEL_EVENT_REQUEST , SSH_CHANNEL_EVENT_REQUEST_RESULT , SSH_CHANNEL_EVENT_RX_DATA_READY , SSH_CHANNEL_EVENT_TX_DATA_READY , SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY , SSH_CHANNEL_EVENT_EOF , SSH_CHANNEL_EVENT_CLOSED }
```

相关声明：[ssh_channel_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaba3db037a1fbeca22f2c3c30063788b9)、[SSH_CHANNEL_EVENT_OPEN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced)、[SSH_CHANNEL_EVENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611)、[SSH_CHANNEL_EVENT_REQUEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330)、[SSH_CHANNEL_EVENT_RX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f)、[SSH_CHANNEL_EVENT_TX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32)、[SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249)、[SSH_CHANNEL_EVENT_EOF](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2)、[SSH_CHANNEL_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e)。

安全外壳（SSH）通道所发出的事件类型。

<a id="r_ga578aed0a10600bc7a248dbb64ca13cc2"></a>

```c
enum ssh_transport_event_type { SSH_TRANSPORT_EVENT_CLOSED , SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED , SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT , SSH_TRANSPORT_EVENT_CHANNEL_OPEN }
```

相关声明：[ssh_transport_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga578aed0a10600bc7a248dbb64ca13cc2)、[SSH_TRANSPORT_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)、[SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3)、[SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a)、[SSH_TRANSPORT_EVENT_CHANNEL_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9)。

SSH 传输层发出的事件类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga691a9ba0d4c2bb1cf637990a4aa91f26"></a>

```c
const char * ssh_transport_client_user_name (struct ssh_transport *transport)
```

相关声明：[ssh_transport_client_user_name](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga691a9ba0d4c2bb1cf637990a4aa91f26)。

获取某传输中已认证客户端的用户名（Authenticated Client Username）。

<a id="r_gaa3b9133aff9d5be3b258db48ba99b601"></a>

```c
int ssh_transport_auth_password (struct ssh_transport *transport, const char *user_name, const char *password)
```

相关声明：[ssh_transport_auth_password](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaa3b9133aff9d5be3b258db48ba99b601)。

使用密码（Password）认证 SSH 传输。

<a id="r_ga1e8ec722a451a466904d077fd4b22a16"></a>

```c
int ssh_transport_channel_open (struct ssh_transport *transport, ssh_channel_event_callback_t callback, void *user_data)
```

相关声明：[ssh_transport_channel_open](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga1e8ec722a451a466904d077fd4b22a16)、[ssh_channel_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga3f29b8eb5acf4b91aeb07873b2df7d56)。

在 SSH 传输上打开新通道（Channel）。

<a id="r_ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e"></a>

```c
int ssh_channel_open_result (struct ssh_channel *channel, bool success, ssh_channel_event_callback_t callback, void *user_data)
```

相关声明：[ssh_channel_open_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_channel_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga3f29b8eb5acf4b91aeb07873b2df7d56)。

响应通道打开请求（Channel Open Request）。

<a id="r_ga5832386d60c9fdd46c2198b45905be73"></a>

```c
int ssh_channel_request_result (struct ssh_channel *channel, bool success)
```

相关声明：[ssh_channel_request_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5832386d60c9fdd46c2198b45905be73)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

响应通道请求（Channel Request）。

<a id="r_ga52f058c2b51df404b9399f8188dcfe8d"></a>

```c
int ssh_channel_request_shell (struct ssh_channel *channel)
```

相关声明：[ssh_channel_request_shell](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga52f058c2b51df404b9399f8188dcfe8d)。

在通道上请求交互式 Shell（Interactive Shell）。

<a id="r_ga6205c8f8d3fd6f0c457261d6cf355940"></a>

```c
int ssh_channel_read (struct ssh_channel *channel, void *data, uint32_t len)
```

相关声明：[ssh_channel_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6205c8f8d3fd6f0c457261d6cf355940)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取通道数据（Channel Data）。

<a id="r_ga658c9f84ec08797b50fb57e2415f7e3d"></a>

```c
int ssh_channel_write (struct ssh_channel *channel, const void *data, uint32_t len)
```

相关声明：[ssh_channel_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga658c9f84ec08797b50fb57e2415f7e3d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入通道数据（Channel Data）。

<a id="r_ga5e0d58687f17df1f5c2480ceadcbde72"></a>

```c
int ssh_channel_read_stderr (struct ssh_channel *channel, void *data, uint32_t len)
```

相关声明：[ssh_channel_read_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5e0d58687f17df1f5c2480ceadcbde72)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取通道的标准错误数据（Standard Error Data）。

<a id="r_ga7fa2613a763415d19c9c6e7926ead074"></a>

```c
int ssh_channel_write_stderr (struct ssh_channel *channel, const void *data, uint32_t len)
```

相关声明：[ssh_channel_write_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7fa2613a763415d19c9c6e7926ead074)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入通道的标准错误数据（Standard Error Data）。

<a id="r_ga7c510e44353e7e791c8f13af3a554739"></a>

```c
int ssh_channel_close (struct ssh_channel *channel)
```

相关声明：[ssh_channel_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7c510e44353e7e791c8f13af3a554739)。

关闭 SSH 通道（Channel）。

<a id="r_gafb6780adc3007639184e634f1a7ec73a"></a>

```c
void ssh_client_foreach (ssh_service_client_cb_t cb, void *user_data)
```

相关声明：[ssh_client_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gafb6780adc3007639184e634f1a7ec73a)、[ssh_service_client_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9f6f03ef86ffee24da6e7fb6adc82878)。

遍历所有 SSH 客户端连接（Client Connections）。

<a id="r_gaff36f18836543d259ee7420bdb757e1f"></a>

```c
void ssh_server_foreach (ssh_service_server_cb_t cb, void *user_data)
```

相关声明：[ssh_server_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaff36f18836543d259ee7420bdb757e1f)、[ssh_service_server_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaf53f661268138d4a36875fb079983c2a)。

遍历所有 SSH 服务器连接（Server Connections）。

<a id="r_ga41ef319c12ce50fe226152eb654a6d56"></a>

```c
int ssh_transport_traverse_callbacks (bool is_server, struct ssh_transport *transport, const struct ssh_transport_event *event)
```

相关声明：[ssh_transport_traverse_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga41ef319c12ce50fe226152eb654a6d56)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)。

为所给传输（Transport）调用用户配置的回调。


## 4.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_architecture_reference/P010_common.h_源码浏览.md)
- [ssh_channel_event_channel_request](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md)
- [ssh_channel_event_channel_request_result](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md)
- [ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)
- [ssh_transport_event_authenticate_result](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md)
- [ssh_transport_event_channel_open](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md)
- [ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [SSH_EXTENDED_DATA_STDERR](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga56f51b1f1c4c9d131eebc65ce5b975ee)
- [ssh_channel_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga3f29b8eb5acf4b91aeb07873b2df7d56)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_service_client_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9f6f03ef86ffee24da6e7fb6adc82878)
- [ssh_service_server_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaf53f661268138d4a36875fb079983c2a)
- [ssh_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6c8271f6fe11a5779a7f05a232c28d84)
- [SSH_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd)
- [SSH_AUTH_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe)
- [SSH_AUTH_PUBKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314)
- [ssh_channel_request_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9341ecffa2ca568ed8312b7c7bd5b416)
- [SSH_CHANNEL_REQUEST_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f)
- [SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622)
- [SSH_CHANNEL_REQUEST_X11_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db)
- [SSH_CHANNEL_REQUEST_ENV_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5)
- [SSH_CHANNEL_REQUEST_SHELL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40)
- [SSH_CHANNEL_REQUEST_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c)
- [SSH_CHANNEL_REQUEST_SUBSYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d)
- [SSH_CHANNEL_REQUEST_WINDOW_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952)
- [SSH_CHANNEL_REQUEST_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0)
- [SSH_CHANNEL_REQUEST_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0)
- [SSH_CHANNEL_REQUEST_EXIT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378)
- [SSH_CHANNEL_REQUEST_EXIT_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0)
- [ssh_channel_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaba3db037a1fbeca22f2c3c30063788b9)
- [SSH_CHANNEL_EVENT_OPEN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced)
- [SSH_CHANNEL_EVENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611)
- [SSH_CHANNEL_EVENT_REQUEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330)
- [SSH_CHANNEL_EVENT_RX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f)
- [SSH_CHANNEL_EVENT_TX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32)
- [SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249)
- [SSH_CHANNEL_EVENT_EOF](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2)
- [SSH_CHANNEL_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e)
- [ssh_transport_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga578aed0a10600bc7a248dbb64ca13cc2)
- [SSH_TRANSPORT_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)
- [SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3)
- [SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a)
- [SSH_TRANSPORT_EVENT_CHANNEL_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9)
- [ssh_transport_client_user_name](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga691a9ba0d4c2bb1cf637990a4aa91f26)
- [ssh_transport_auth_password](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaa3b9133aff9d5be3b258db48ba99b601)
- [ssh_transport_channel_open](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga1e8ec722a451a466904d077fd4b22a16)
- [ssh_channel_open_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ssh_channel_request_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5832386d60c9fdd46c2198b45905be73)
- [ssh_channel_request_shell](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga52f058c2b51df404b9399f8188dcfe8d)
- [ssh_channel_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6205c8f8d3fd6f0c457261d6cf355940)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ssh_channel_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga658c9f84ec08797b50fb57e2415f7e3d)
- [ssh_channel_read_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5e0d58687f17df1f5c2480ceadcbde72)
- [ssh_channel_write_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7fa2613a763415d19c9c6e7926ead074)
- [ssh_channel_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7c510e44353e7e791c8f13af3a554739)
- [ssh_client_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gafb6780adc3007639184e634f1a7ec73a)
- [ssh_server_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaff36f18836543d259ee7420bdb757e1f)
- [ssh_transport_traverse_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga41ef319c12ce50fe226152eb654a6d56)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__gnss.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__input__input_kbd_matrix.h_文件参考.md)
