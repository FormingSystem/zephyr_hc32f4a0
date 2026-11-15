---
id: learning.zephyr-docs.api-file-host-video-reference.page-6
title: zephyr__mgmt__ec_host_cmd__ec_host_cmd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_mgmt\_\_ec\_host\_cmd\_\_ec\_host\_cmd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入式控制器（EC）主机命令（Host Command）API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/mgmt/ec_host_cmd/backend.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

嵌入式控制器（EC）主机命令（Host Command）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_ec_5Fhost_5Fcmd"></a>

```c
struct ec_host_cmd
```

相关声明：[ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)。

主机命令（Host Command）的上下文结构。

<a id="r_ec_5Fhost_5Fcmd_5Fhandler_5Fargs"></a>

```c
struct ec_host_cmd_handler_args
```

相关声明：[ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)。

传递给每个已安装主机命令处理程序（Host Command Handler）的参数。

<a id="r_ec_5Fhost_5Fcmd_5Fhandler"></a>

```c
struct ec_host_cmd_handler
```

相关声明：[ec_host_cmd_handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md)。

用于静态注册主机命令处理程序（Host Command Handler）的结构。

<a id="r_ec_5Fhost_5Fcmd_5Frequest_5Fheader"></a>

```c
struct ec_host_cmd_request_header
```

相关声明：[ec_host_cmd_request_header](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md)。

主机发往嵌入式控制器（Embedded Controller）的请求头部。

<a id="r_ec_5Fhost_5Fcmd_5Fresponse_5Fheader"></a>

```c
struct ec_host_cmd_response_header
```

相关声明：[ec_host_cmd_response_header](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md)。

嵌入式控制器（Embedded Controller）返回主机的响应头部。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gaed5a8c4ba3648ae9e6284502f6a48dc7"></a>

```c
#define EC_HOST_CMD_HANDLER(_id, _function, _version_mask, _request_type, _response_type)
```

相关声明：[EC_HOST_CMD_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaed5a8c4ba3648ae9e6284502f6a48dc7)。

静态定义并注册主机命令处理函数（Host Command Handler）。

<a id="r_ga90213771b654eb8315834d967152fc77"></a>

```c
#define EC_HOST_CMD_HANDLER_REQ_ONLY(_id, _function, _version_mask, _request_type)
```

相关声明：[EC_HOST_CMD_HANDLER_REQ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga90213771b654eb8315834d967152fc77)。

静态定义并注册仅有请求的主机命令处理函数（Request-only Host Command Handler）。

<a id="r_ga9625e9897253d52c5ff0767b706e726d"></a>

```c
#define EC_HOST_CMD_HANDLER_RESP_ONLY(_id, _function, _version_mask, _response_type)
```

相关声明：[EC_HOST_CMD_HANDLER_RESP_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9625e9897253d52c5ff0767b706e726d)。

静态定义并注册仅有响应的主机命令处理函数（Response-only Host Command Handler）。

<a id="r_ga2dae15d1db72c7c9b5f879284a990e13"></a>

```c
#define EC_HOST_CMD_HANDLER_UNBOUND(_id, _function, _version_mask)
```

相关声明：[EC_HOST_CMD_HANDLER_UNBOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga2dae15d1db72c7c9b5f879284a990e13)。

静态定义并注册不指定大小的主机命令处理函数（Host Command Handler without Sizes）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gaa6ea251ee113cc15fd085ef12b76a573"></a>

```c
typedef void(* ec_host_cmd_user_cb_t) (const struct ec_host_cmd_rx_ctx *rx_ctx, void *user_data)
```

相关声明：[ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)、[ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)。

用于接收主机命令的用户回调函数类型（User Callback Function Type）。

<a id="r_gacf91301985634f9a12cd80db5e818821"></a>

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_in_progress_cb_t) (void *user_data)
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_in_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gacf91301985634f9a12cd80db5e818821)。

进行中回调函数类型（In-progress Callback Function Type）。

<a id="r_ga027ae23ea11a0ec7711725d1b28125d7"></a>

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_handler_cb) (struct ec_host_cmd_handler_args *args)
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga027ae23ea11a0ec7711725d1b28125d7)、[ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)。

主机命令处理回调函数类型（Host Command Handler Callback Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga9b0b87983dcc92ea55ebfa1aecf82a8f"></a>

```c
enum ec_host_cmd_status { EC_HOST_CMD_SUCCESS = 0 , EC_HOST_CMD_INVALID_COMMAND = 1 , EC_HOST_CMD_ERROR = 2 , EC_HOST_CMD_INVALID_PARAM = 3 , EC_HOST_CMD_ACCESS_DENIED = 4 , EC_HOST_CMD_INVALID_RESPONSE = 5 , EC_HOST_CMD_INVALID_VERSION = 6 , EC_HOST_CMD_INVALID_CHECKSUM = 7 , EC_HOST_CMD_IN_PROGRESS = 8 , EC_HOST_CMD_UNAVAILABLE = 9 , EC_HOST_CMD_TIMEOUT = 10 , EC_HOST_CMD_OVERFLOW = 11 , EC_HOST_CMD_INVALID_HEADER = 12 , EC_HOST_CMD_REQUEST_TRUNCATED = 13 , EC_HOST_CMD_RESPONSE_TOO_BIG = 14 , EC_HOST_CMD_BUS_ERROR = 15 , EC_HOST_CMD_BUSY = 16 , EC_HOST_CMD_INVALID_HEADER_VERSION = 17 , EC_HOST_CMD_INVALID_HEADER_CRC = 18 , EC_HOST_CMD_INVALID_DATA_CRC = 19 , EC_HOST_CMD_DUP_UNAVAILABLE = 20 }
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[EC_HOST_CMD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e)、[EC_HOST_CMD_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432)、[EC_HOST_CMD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201)、[EC_HOST_CMD_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d)、[EC_HOST_CMD_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c)、[EC_HOST_CMD_INVALID_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9)、[EC_HOST_CMD_INVALID_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39)、[EC_HOST_CMD_INVALID_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301)、[EC_HOST_CMD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e)、[EC_HOST_CMD_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996)、[EC_HOST_CMD_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26)、[EC_HOST_CMD_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443)、[EC_HOST_CMD_INVALID_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b)、[EC_HOST_CMD_REQUEST_TRUNCATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00)、[EC_HOST_CMD_RESPONSE_TOO_BIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5)、[EC_HOST_CMD_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2)、[EC_HOST_CMD_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1)、[EC_HOST_CMD_INVALID_HEADER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5)、[EC_HOST_CMD_INVALID_HEADER_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e)、[EC_HOST_CMD_INVALID_DATA_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985)、[EC_HOST_CMD_DUP_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80)。

主机命令响应码（Host Command Response Codes），16 位。

<a id="r_ga70cbd55129ef589688c6d2f5999337c9"></a>

```c
enum ec_host_cmd_log_level { EC_HOST_CMD_DEBUG_OFF , EC_HOST_CMD_DEBUG_NORMAL , EC_HOST_CMD_DEBUG_EVERY , EC_HOST_CMD_DEBUG_PARAMS , EC_HOST_CMD_DEBUG_MODES }
```

相关声明：[ec_host_cmd_log_level](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga70cbd55129ef589688c6d2f5999337c9)、[EC_HOST_CMD_DEBUG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38)、[EC_HOST_CMD_DEBUG_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81)、[EC_HOST_CMD_DEBUG_EVERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6)、[EC_HOST_CMD_DEBUG_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1)、[EC_HOST_CMD_DEBUG_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)。

主机命令日志级别（Host Command Log Levels）。

<a id="r_gabf0f1243bf55cb70078f2a9fd0a755ec"></a>

```c
enum ec_host_cmd_state { EC_HOST_CMD_STATE_DISABLED = 0 , EC_HOST_CMD_STATE_RECEIVING , EC_HOST_CMD_STATE_PROCESSING , EC_HOST_CMD_STATE_SENDING }
```

相关声明：[ec_host_cmd_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gabf0f1243bf55cb70078f2a9fd0a755ec)、[EC_HOST_CMD_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af)、[EC_HOST_CMD_STATE_RECEIVING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20)、[EC_HOST_CMD_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8)、[EC_HOST_CMD_STATE_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46)。

主机命令状态（Host Command State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gaab1fdcb0fd13a19447d262d496b8aed9"></a>

```c
int ec_host_cmd_init (struct ec_host_cmd_backend *backend)
```

相关声明：[ec_host_cmd_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaab1fdcb0fd13a19447d262d496b8aed9)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)。

初始化主机命令子系统（Host Command Subsystem）。

<a id="r_ga95f36f8cf2d21ea73bd8a36f3f7303e8"></a>

```c
int ec_host_cmd_send_response (enum ec_host_cmd_status status, const struct ec_host_cmd_handler_args *args)
```

相关声明：[ec_host_cmd_send_response](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga95f36f8cf2d21ea73bd8a36f3f7303e8)、[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)。

发送主机命令响应（Host Command Response）。

<a id="r_gadbee4a2588abeb6db63f70a90b67a8fb"></a>

```c
void ec_host_cmd_rx_notify (void)
```

相关声明：[ec_host_cmd_rx_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gadbee4a2588abeb6db63f70a90b67a8fb)。

发出新主机命令的通知（Signal）。

<a id="r_gaaf267a44816e5f856db2092fca681d3e"></a>

```c
void ec_host_cmd_set_user_cb (ec_host_cmd_user_cb_t cb, void *user_data)
```

相关声明：[ec_host_cmd_set_user_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaf267a44816e5f856db2092fca681d3e)、[ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)。

安装用于接收主机命令（Host Command）的用户回调。

<a id="r_gaf3b87533037c4d865641643736904d02"></a>

```c
const struct ec_host_cmd * ec_host_cmd_get_hc (void)
```

相关声明：[ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)、[ec_host_cmd_get_hc](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaf3b87533037c4d865641643736904d02)。

获取嵌入式控制器（EC）主机命令的主结构体。

<a id="r_gaaa3dc6c413b9637a3817cf82e138b27a"></a>

```c
FUNC_NORETURN void ec_host_cmd_task (void)
```

相关声明：[ec_host_cmd_task](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaa3dc6c413b9637a3817cf82e138b27a)。

主机命令子系统（Host Command Subsystem）的线程函数。

<a id="r_ga9a234157f85e06413b60682055d44fd3"></a>

```c
bool ec_host_cmd_send_in_progress_ended (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ec_host_cmd_send_in_progress_ended](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9a234157f85e06413b60682055d44fd3)。

检查曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令（Host Command）是否已结束。

<a id="r_ga9d8349220771fd9570432c3e3bea3066"></a>

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_status (void)
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_send_in_progress_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9d8349220771fd9570432c3e3bea3066)。

获取最近一次曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令的最终结果（Final Result）。

<a id="r_ga0af800c7a27eb6d0a35179f472a3c37e"></a>

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_continue (ec_host_cmd_in_progress_cb_t cb, void *user_data)
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_send_in_progress_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga0af800c7a27eb6d0a35179f472a3c37e)、[ec_host_cmd_in_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gacf91301985634f9a12cd80db5e818821)。

返回 `EC_HOST_CMD_IN_PROGRESS` 后，在回调中继续执行处理函数（Handler）。

<a id="r_ga9f734642958684ca654a3c786b2ceb74"></a>

```c
int ec_host_cmd_add_suppressed (uint16_t cmd_id)
```

相关声明：[ec_host_cmd_add_suppressed](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9f734642958684ca654a3c786b2ceb74)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

添加一个被抑制的命令（Suppressed Command）。


## 6.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/mgmt/ec_host_cmd/backend.h](../api_source_reference/P050_backend.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P049_ec_host_cmd.h_源码浏览.md)
- [ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)
- [ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)
- [ec_host_cmd_handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md)
- [ec_host_cmd_request_header](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md)
- [ec_host_cmd_response_header](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md)
- [EC_HOST_CMD_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaed5a8c4ba3648ae9e6284502f6a48dc7)
- [EC_HOST_CMD_HANDLER_REQ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga90213771b654eb8315834d967152fc77)
- [EC_HOST_CMD_HANDLER_RESP_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9625e9897253d52c5ff0767b706e726d)
- [EC_HOST_CMD_HANDLER_UNBOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga2dae15d1db72c7c9b5f879284a990e13)
- [ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)
- [ec_host_cmd_in_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gacf91301985634f9a12cd80db5e818821)
- [ec_host_cmd_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga027ae23ea11a0ec7711725d1b28125d7)
- [EC_HOST_CMD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e)
- [EC_HOST_CMD_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432)
- [EC_HOST_CMD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201)
- [EC_HOST_CMD_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d)
- [EC_HOST_CMD_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c)
- [EC_HOST_CMD_INVALID_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9)
- [EC_HOST_CMD_INVALID_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39)
- [EC_HOST_CMD_INVALID_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301)
- [EC_HOST_CMD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e)
- [EC_HOST_CMD_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996)
- [EC_HOST_CMD_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26)
- [EC_HOST_CMD_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443)
- [EC_HOST_CMD_INVALID_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b)
- [EC_HOST_CMD_REQUEST_TRUNCATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00)
- [EC_HOST_CMD_RESPONSE_TOO_BIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5)
- [EC_HOST_CMD_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2)
- [EC_HOST_CMD_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1)
- [EC_HOST_CMD_INVALID_HEADER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5)
- [EC_HOST_CMD_INVALID_HEADER_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e)
- [EC_HOST_CMD_INVALID_DATA_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985)
- [EC_HOST_CMD_DUP_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80)
- [ec_host_cmd_log_level](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga70cbd55129ef589688c6d2f5999337c9)
- [EC_HOST_CMD_DEBUG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38)
- [EC_HOST_CMD_DEBUG_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81)
- [EC_HOST_CMD_DEBUG_EVERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6)
- [EC_HOST_CMD_DEBUG_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1)
- [EC_HOST_CMD_DEBUG_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)
- [ec_host_cmd_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gabf0f1243bf55cb70078f2a9fd0a755ec)
- [EC_HOST_CMD_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af)
- [EC_HOST_CMD_STATE_RECEIVING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20)
- [EC_HOST_CMD_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8)
- [EC_HOST_CMD_STATE_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46)
- [ec_host_cmd_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaab1fdcb0fd13a19447d262d496b8aed9)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [ec_host_cmd_send_response](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga95f36f8cf2d21ea73bd8a36f3f7303e8)
- [ec_host_cmd_rx_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gadbee4a2588abeb6db63f70a90b67a8fb)
- [ec_host_cmd_set_user_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaf267a44816e5f856db2092fca681d3e)
- [ec_host_cmd_get_hc](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaf3b87533037c4d865641643736904d02)
- [ec_host_cmd_task](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaa3dc6c413b9637a3817cf82e138b27a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ec_host_cmd_send_in_progress_ended](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9a234157f85e06413b60682055d44fd3)
- [ec_host_cmd_send_in_progress_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9d8349220771fd9570432c3e3bea3066)
- [ec_host_cmd_send_in_progress_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga0af800c7a27eb6d0a35179f472a3c37e)
- [ec_host_cmd_add_suppressed](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9f734642958684ca654a3c786b2ceb74)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__sensor__it8xxx2_vcmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__interrupt_controller__gpio_intc_stm32.h_文件参考.md)
