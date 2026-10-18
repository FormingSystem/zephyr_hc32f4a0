---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-3
title: 嵌入式控制器主机命令接口（EC Host Command Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_嵌入式控制器主机命令接口（EC Host Command Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入式控制器主机命令接口（EC Host Command Interface）

<a id="details"></a>

嵌入式控制器主机命令接口（EC Host Command Interface）。自（Since）2.4 起提供，版本（Version）0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_ec_5Fhost_5Fcmd_5Finterface_5Fbackend"></a>

相关声明：[主机命令驱动后端 API（Host Command Driver Backend API）](../api_power_policy_topic_reference/P004_主机命令驱动后端 API（Host Command Driver Backend API）.md)。

<a id="r_ec_5Fhost_5Fcmd_5Fsimulator"></a>

相关声明：[模拟器（Simulator）](../api_auxiliary_topic_reference/P005_模拟器（Simulator）.md)。

EC 主机命令模拟器接口。

<a id="header-files"></a>
<a id="files"></a>

## 3.2\_文件（Files）

<a id="r_ec_5Fhost_5Fcmd_2Eh"></a>

```c
file ec_host_cmd.h
```

相关声明：[ec_host_cmd.h](../api_file_host_video_reference/P006_zephyr__mgmt__ec_host_cmd__ec_host_cmd.h_文件参考.md)。

嵌入式控制器（EC）主机命令（Host Command）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.3\_数据结构（Data Structures）

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

## 3.4\_宏定义（Macros）

<a id="r_gaed5a8c4ba3648ae9e6284502f6a48dc7"></a>

```c
#define EC_HOST_CMD_HANDLER(_id, _function, _version_mask, _request_type, _response_type)
```

相关声明：[EC_HOST_CMD_HANDLER](#gaed5a8c4ba3648ae9e6284502f6a48dc7)。

静态定义并注册主机命令处理函数（Host Command Handler）。

<a id="r_ga90213771b654eb8315834d967152fc77"></a>

```c
#define EC_HOST_CMD_HANDLER_REQ_ONLY(_id, _function, _version_mask, _request_type)
```

相关声明：[EC_HOST_CMD_HANDLER_REQ_ONLY](#ga90213771b654eb8315834d967152fc77)。

静态定义并注册仅有请求的主机命令处理函数（Request-only Host Command Handler）。

<a id="r_ga9625e9897253d52c5ff0767b706e726d"></a>

```c
#define EC_HOST_CMD_HANDLER_RESP_ONLY(_id, _function, _version_mask, _response_type)
```

相关声明：[EC_HOST_CMD_HANDLER_RESP_ONLY](#ga9625e9897253d52c5ff0767b706e726d)。

静态定义并注册仅有响应的主机命令处理函数（Response-only Host Command Handler）。

<a id="r_ga2dae15d1db72c7c9b5f879284a990e13"></a>

```c
#define EC_HOST_CMD_HANDLER_UNBOUND(_id, _function, _version_mask)
```

相关声明：[EC_HOST_CMD_HANDLER_UNBOUND](#ga2dae15d1db72c7c9b5f879284a990e13)。

静态定义并注册不指定大小的主机命令处理函数（Host Command Handler without Sizes）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.5\_类型定义（Typedefs）

<a id="r_gaa6ea251ee113cc15fd085ef12b76a573"></a>

```c
typedef void(* ec_host_cmd_user_cb_t) (const struct ec_host_cmd_rx_ctx *rx_ctx, void *user_data)
```

相关声明：[ec_host_cmd_user_cb_t](#gaa6ea251ee113cc15fd085ef12b76a573)、[ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)。

用于接收主机命令的用户回调函数类型（User Callback Function Type）。

<a id="r_gacf91301985634f9a12cd80db5e818821"></a>

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_in_progress_cb_t) (void *user_data)
```

相关声明：[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_in_progress_cb_t](#gacf91301985634f9a12cd80db5e818821)。

进行中回调函数类型（In-progress Callback Function Type）。

<a id="r_ga027ae23ea11a0ec7711725d1b28125d7"></a>

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_handler_cb) (struct ec_host_cmd_handler_args *args)
```

相关声明：[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_handler_cb](#ga027ae23ea11a0ec7711725d1b28125d7)、[ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)。

主机命令处理回调函数类型（Host Command Handler Callback Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.6\_枚举（Enumerations）

<a id="r_ga9b0b87983dcc92ea55ebfa1aecf82a8f"></a>

```c
enum ec_host_cmd_status { EC_HOST_CMD_SUCCESS = 0 , EC_HOST_CMD_INVALID_COMMAND = 1 , EC_HOST_CMD_ERROR = 2 , EC_HOST_CMD_INVALID_PARAM = 3 , EC_HOST_CMD_ACCESS_DENIED = 4 , EC_HOST_CMD_INVALID_RESPONSE = 5 , EC_HOST_CMD_INVALID_VERSION = 6 , EC_HOST_CMD_INVALID_CHECKSUM = 7 , EC_HOST_CMD_IN_PROGRESS = 8 , EC_HOST_CMD_UNAVAILABLE = 9 , EC_HOST_CMD_TIMEOUT = 10 , EC_HOST_CMD_OVERFLOW = 11 , EC_HOST_CMD_INVALID_HEADER = 12 , EC_HOST_CMD_REQUEST_TRUNCATED = 13 , EC_HOST_CMD_RESPONSE_TOO_BIG = 14 , EC_HOST_CMD_BUS_ERROR = 15 , EC_HOST_CMD_BUSY = 16 , EC_HOST_CMD_INVALID_HEADER_VERSION = 17 , EC_HOST_CMD_INVALID_HEADER_CRC = 18 , EC_HOST_CMD_INVALID_DATA_CRC = 19 , EC_HOST_CMD_DUP_UNAVAILABLE = 20 }
```

相关声明：[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[EC_HOST_CMD_SUCCESS](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e)、[EC_HOST_CMD_INVALID_COMMAND](#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432)、[EC_HOST_CMD_ERROR](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201)、[EC_HOST_CMD_INVALID_PARAM](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d)、[EC_HOST_CMD_ACCESS_DENIED](#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c)、[EC_HOST_CMD_INVALID_RESPONSE](#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9)、[EC_HOST_CMD_INVALID_VERSION](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39)、[EC_HOST_CMD_INVALID_CHECKSUM](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301)、[EC_HOST_CMD_IN_PROGRESS](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e)、[EC_HOST_CMD_UNAVAILABLE](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996)、[EC_HOST_CMD_TIMEOUT](#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26)、[EC_HOST_CMD_OVERFLOW](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443)、[EC_HOST_CMD_INVALID_HEADER](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b)、[EC_HOST_CMD_REQUEST_TRUNCATED](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00)、[EC_HOST_CMD_RESPONSE_TOO_BIG](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5)、[EC_HOST_CMD_BUS_ERROR](#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2)、[EC_HOST_CMD_BUSY](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1)、[EC_HOST_CMD_INVALID_HEADER_VERSION](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5)、[EC_HOST_CMD_INVALID_HEADER_CRC](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e)、[EC_HOST_CMD_INVALID_DATA_CRC](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985)、[EC_HOST_CMD_DUP_UNAVAILABLE](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80)。

主机命令响应码（Host Command Response Codes），16 位。

<a id="r_ga70cbd55129ef589688c6d2f5999337c9"></a>

```c
enum ec_host_cmd_log_level { EC_HOST_CMD_DEBUG_OFF , EC_HOST_CMD_DEBUG_NORMAL , EC_HOST_CMD_DEBUG_EVERY , EC_HOST_CMD_DEBUG_PARAMS , EC_HOST_CMD_DEBUG_MODES }
```

相关声明：[ec_host_cmd_log_level](#ga70cbd55129ef589688c6d2f5999337c9)、[EC_HOST_CMD_DEBUG_OFF](#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38)、[EC_HOST_CMD_DEBUG_NORMAL](#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81)、[EC_HOST_CMD_DEBUG_EVERY](#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6)、[EC_HOST_CMD_DEBUG_PARAMS](#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1)、[EC_HOST_CMD_DEBUG_MODES](#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)。

主机命令日志级别（Host Command Log Levels）。

<a id="r_gabf0f1243bf55cb70078f2a9fd0a755ec"></a>

```c
enum ec_host_cmd_state { EC_HOST_CMD_STATE_DISABLED = 0 , EC_HOST_CMD_STATE_RECEIVING , EC_HOST_CMD_STATE_PROCESSING , EC_HOST_CMD_STATE_SENDING }
```

相关声明：[ec_host_cmd_state](#gabf0f1243bf55cb70078f2a9fd0a755ec)、[EC_HOST_CMD_STATE_DISABLED](#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af)、[EC_HOST_CMD_STATE_RECEIVING](#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20)、[EC_HOST_CMD_STATE_PROCESSING](#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8)、[EC_HOST_CMD_STATE_SENDING](#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46)。

主机命令状态（Host Command State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.7\_函数（Functions）

<a id="r_gaab1fdcb0fd13a19447d262d496b8aed9"></a>

```c
int ec_host_cmd_init (struct ec_host_cmd_backend *backend)
```

相关声明：[ec_host_cmd_init](#gaab1fdcb0fd13a19447d262d496b8aed9)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)。

初始化主机命令子系统（Host Command Subsystem）。

<a id="r_ga95f36f8cf2d21ea73bd8a36f3f7303e8"></a>

```c
int ec_host_cmd_send_response (enum ec_host_cmd_status status, const struct ec_host_cmd_handler_args *args)
```

相关声明：[ec_host_cmd_send_response](#ga95f36f8cf2d21ea73bd8a36f3f7303e8)、[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)。

发送主机命令响应（Host Command Response）。

<a id="r_gadbee4a2588abeb6db63f70a90b67a8fb"></a>

```c
void ec_host_cmd_rx_notify (void)
```

相关声明：[ec_host_cmd_rx_notify](#gadbee4a2588abeb6db63f70a90b67a8fb)。

发出新主机命令的通知（Signal）。

<a id="r_gaaf267a44816e5f856db2092fca681d3e"></a>

```c
void ec_host_cmd_set_user_cb (ec_host_cmd_user_cb_t cb, void *user_data)
```

相关声明：[ec_host_cmd_set_user_cb](#gaaf267a44816e5f856db2092fca681d3e)、[ec_host_cmd_user_cb_t](#gaa6ea251ee113cc15fd085ef12b76a573)。

安装用于接收主机命令（Host Command）的用户回调。

<a id="r_gaf3b87533037c4d865641643736904d02"></a>

```c
const struct ec_host_cmd * ec_host_cmd_get_hc (void)
```

相关声明：[ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)、[ec_host_cmd_get_hc](#gaf3b87533037c4d865641643736904d02)。

获取嵌入式控制器（EC）主机命令的主结构体。

<a id="r_gaaa3dc6c413b9637a3817cf82e138b27a"></a>

```c
FUNC_NORETURN void ec_host_cmd_task (void)
```

相关声明：[ec_host_cmd_task](#gaaa3dc6c413b9637a3817cf82e138b27a)。

主机命令子系统（Host Command Subsystem）的线程函数。

<a id="r_ga9a234157f85e06413b60682055d44fd3"></a>

```c
bool ec_host_cmd_send_in_progress_ended (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ec_host_cmd_send_in_progress_ended](#ga9a234157f85e06413b60682055d44fd3)。

检查曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令（Host Command）是否已结束。

<a id="r_ga9d8349220771fd9570432c3e3bea3066"></a>

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_status (void)
```

相关声明：[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_send_in_progress_status](#ga9d8349220771fd9570432c3e3bea3066)。

获取最近一次曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令的最终结果（Final Result）。

<a id="r_ga0af800c7a27eb6d0a35179f472a3c37e"></a>

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_continue (ec_host_cmd_in_progress_cb_t cb, void *user_data)
```

相关声明：[ec_host_cmd_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[ec_host_cmd_send_in_progress_continue](#ga0af800c7a27eb6d0a35179f472a3c37e)、[ec_host_cmd_in_progress_cb_t](#gacf91301985634f9a12cd80db5e818821)。

返回 `EC_HOST_CMD_IN_PROGRESS` 后，在回调中继续执行处理函数（Handler）。

<a id="r_ga9f734642958684ca654a3c786b2ceb74"></a>

```c
int ec_host_cmd_add_suppressed (uint16_t cmd_id)
```

相关声明：[ec_host_cmd_add_suppressed](#ga9f734642958684ca654a3c786b2ceb74)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

添加一个被抑制的命令（Suppressed Command）。

## 3.8\_详细说明（Detailed Documentation）

<a id="gaed5a8c4ba3648ae9e6284502f6a48dc7"></a>

### `EC_HOST_CMD_HANDLER`

```c
#define EC_HOST_CMD_HANDLER ( _id, _function, _version_mask, _request_type, _response_type )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
        .handler = _function,                                                              \
        .id = _id,                                                                         \
        .version_mask = _version_mask,                                                     \
        .min_rqt_size = sizeof(_request_type),                                             \
        .min_rsp_size = sizeof(_response_type),                                            \
}
```

静态定义并注册主机命令处理函数（Host Command Handler）。

辅助宏，用于静态定义并注册主机命令处理函数（Host Command Handler）；其请求和响应结构体的大小都在编译时固定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 要处理其请求的主机命令 ID（Host Command ID）。 |
| `_function` | 处理函数（Handler Function）的名称。 |
| `_version_mask` | `_function` 支持的所有版本组成的位字段（Bitfield）。例如，`BIT(0)` 对应版本 0。 |
| `_request_type` | `_function` 请求参数的数据类型（Datatype）。 |
| `_response_type` | `_function` 响应参数的数据类型（Datatype）。 |

<a id="ga90213771b654eb8315834d967152fc77"></a>

### `EC_HOST_CMD_HANDLER_REQ_ONLY`

```c
#define EC_HOST_CMD_HANDLER_REQ_ONLY ( _id, _function, _version_mask, _request_type )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
        .handler = _function,                                                              \
        .id = _id,                                                                         \
        .version_mask = _version_mask,                                                     \
        .min_rqt_size = sizeof(_request_type),                                             \
        .min_rsp_size = 0,                                                                 \
}
```

静态定义并注册仅有请求的主机命令处理函数（Request-only Host Command Handler）。

辅助宏，用于静态定义并注册主机命令处理函数（Host Command Handler）；其请求结构体的大小在编译时固定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 要处理其请求的主机命令 ID（Host Command ID）。 |
| `_function` | 处理函数（Handler Function）的名称。 |
| `_version_mask` | `_function` 支持的所有版本组成的位字段（Bitfield）。例如，`BIT(0)` 对应版本 0。 |
| `_request_type` | `_function` 请求参数的数据类型（Datatype）。 |

<a id="ga9625e9897253d52c5ff0767b706e726d"></a>

### `EC_HOST_CMD_HANDLER_RESP_ONLY`

```c
#define EC_HOST_CMD_HANDLER_RESP_ONLY ( _id, _function, _version_mask, _response_type )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
        .handler = _function,                                                              \
        .id = _id,                                                                         \
        .version_mask = _version_mask,                                                     \
        .min_rqt_size = 0,                                                                 \
        .min_rsp_size = sizeof(_response_type),                                            \
}
```

静态定义并注册仅有响应的主机命令处理函数（Response-only Host Command Handler）。

辅助宏，用于静态定义并注册主机命令处理函数（Host Command Handler）；其响应结构体的大小在编译时固定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 要处理其请求的主机命令 ID（Host Command ID）。 |
| `_function` | 处理函数（Handler Function）的名称。 |
| `_version_mask` | `_function` 支持的所有版本组成的位字段（Bitfield）。例如，`BIT(0)` 对应版本 0。 |
| `_response_type` | `_function` 响应参数的数据类型（Datatype）。 |

<a id="ga2dae15d1db72c7c9b5f879284a990e13"></a>

### `EC_HOST_CMD_HANDLER_UNBOUND`

```c
#define EC_HOST_CMD_HANDLER_UNBOUND ( _id, _function, _version_mask )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
        .handler = _function,                                                              \
        .id = _id,                                                                         \
        .version_mask = _version_mask,                                                     \
        .min_rqt_size = 0,                                                                 \
        .min_rsp_size = 0,                                                                 \
}
```

静态定义并注册不指定大小的主机命令处理函数（Host Command Handler without Sizes）。

辅助宏，用于静态定义并注册主机命令处理函数（Host Command Handler）；其请求或响应结构体的大小在编译时未知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 要处理其请求的主机命令 ID（Host Command ID）。 |
| `_function` | 处理函数（Handler Function）的名称。 |
| `_version_mask` | `_function` 支持的所有版本组成的位字段（Bitfield）。例如，`BIT(0)` 对应版本 0。 |

<a id="ga027ae23ea11a0ec7711725d1b28125d7"></a>

### `ec_host_cmd_handler_cb`

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_handler_cb) (struct ec_host_cmd_handler_args *args)
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

主机命令处理回调函数类型（Host Command Handler Callback Function Type）。

当主机命令与处理函数的命令 ID 和版本匹配时，调用此回调进行处理。处理函数处理传入的命令数据并生成响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `args` | 指向包含命令数据与缓冲区的 `ec_host_cmd_handler_args` 结构体的指针。 |

**返回（Returns）**：返回值（Returns）：表示命令处理结果的状态码（Status Code）。

<a id="gacf91301985634f9a12cd80db5e818821"></a>

### `ec_host_cmd_in_progress_cb_t`

```c
typedef enum ec_host_cmd_status(* ec_host_cmd_in_progress_cb_t) (void *user_data)
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

进行中回调函数类型（In-progress Callback Function Type）。

对于返回 `EC_HOST_CMD_IN_PROGRESS` 状态的命令，此回调异步执行，使耗时操作能够在后台完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_data` | 传给回调的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：命令的最终状态码（Final Status Code）。

<a id="gaa6ea251ee113cc15fd085ef12b76a573"></a>

### `ec_host_cmd_user_cb_t`

```c
typedef void(* ec_host_cmd_user_cb_t) (const struct ec_host_cmd_rx_ctx *rx_ctx, void *user_data)
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

用于接收主机命令的用户回调函数类型（User Callback Function Type）。

收到主机命令并完成验证后、开始处理命令之前，调用此回调。它允许用户代码根据收到的命令执行自定义操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx_ctx` | 指向包含命令数据的接收上下文（Receive Context）的指针。 |
| `user_data` | 注册回调时传入的用户定义数据指针。 |

<a id="ga70cbd55129ef589688c6d2f5999337c9"></a>

### `ec_host_cmd_log_level`

```c
enum ec_host_cmd_log_level
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

主机命令日志级别（Host Command Log Levels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `EC_HOST_CMD_DEBUG_OFF` | 不输出主机命令调试信息（Host Command Debug Output）。 |
| `EC_HOST_CMD_DEBUG_NORMAL` | 正常输出模式（Normal Output Mode），跳过重复命令。 |
| `EC_HOST_CMD_DEBUG_EVERY` | 打印每条命令。 |
| `EC_HOST_CMD_DEBUG_PARAMS` | ……并打印请求／响应参数（Request/Response Parameters）。 |
| `EC_HOST_CMD_DEBUG_MODES` | 主机命令调试模式（Debug Modes）的数量。 |

<a id="gabf0f1243bf55cb70078f2a9fd0a755ec"></a>

### `ec_host_cmd_state`

```c
enum ec_host_cmd_state
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

主机命令状态（Host Command State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `EC_HOST_CMD_STATE_DISABLED` | 主机命令子系统（Host Command Subsystem）已禁用。 |
| `EC_HOST_CMD_STATE_RECEIVING` | 正在从主机接收命令数据。 |
| `EC_HOST_CMD_STATE_PROCESSING` | 正在处理收到的命令。 |
| `EC_HOST_CMD_STATE_SENDING` | 正在向主机发送响应。 |

<a id="ga9b0b87983dcc92ea55ebfa1aecf82a8f"></a>

### `ec_host_cmd_status`

```c
enum ec_host_cmd_status
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

主机命令响应码（Host Command Response Codes），16 位。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `EC_HOST_CMD_SUCCESS` | 主机命令成功。 |
| `EC_HOST_CMD_INVALID_COMMAND` | 指定的命令 ID 无法识别或不受支持。 |
| `EC_HOST_CMD_ERROR` | 通用错误（Generic Error）。 |
| `EC_HOST_CMD_INVALID_PARAM` | 一个或多个输入请求参数无效。 |
| `EC_HOST_CMD_ACCESS_DENIED` | 不允许执行该主机命令。 |
| `EC_HOST_CMD_INVALID_RESPONSE` | 响应无效，例如头部版本不是 3。 |
| `EC_HOST_CMD_INVALID_VERSION` | 不支持该主机命令 ID 的版本。 |
| `EC_HOST_CMD_INVALID_CHECKSUM` | 校验和（Checksum）不匹配。 |
| `EC_HOST_CMD_IN_PROGRESS` | 当前正在处理一个主机命令。 |
| `EC_HOST_CMD_UNAVAILABLE` | 所请求的信息当前不可用。 |
| `EC_HOST_CMD_TIMEOUT` | 处理期间超时。 |
| `EC_HOST_CMD_OVERFLOW` | 数据或表溢出（Overflow）。 |
| `EC_HOST_CMD_INVALID_HEADER` | 头部无效或不受支持，例如头部版本不是 3。 |
| `EC_HOST_CMD_REQUEST_TRUNCATED` | 未收到全部预期的请求数据。 |
| `EC_HOST_CMD_RESPONSE_TOO_BIG` | 响应过大，无法在一个响应分组（Response Packet）内发送。 |
| `EC_HOST_CMD_BUS_ERROR` | 底层通信总线（Communication Bus）发生错误。 |
| `EC_HOST_CMD_BUSY` | 系统忙（System Busy），应稍后重试。 |
| `EC_HOST_CMD_INVALID_HEADER_VERSION` | 头部版本（Header Version）无效。 |
| `EC_HOST_CMD_INVALID_HEADER_CRC` | 头部 CRC（Header CRC）无效。 |
| `EC_HOST_CMD_INVALID_DATA_CRC` | 数据 CRC（Data CRC）无效。 |
| `EC_HOST_CMD_DUP_UNAVAILABLE` | 无法重新发送响应。 |

<a id="ga9f734642958684ca654a3c786b2ceb74"></a>

### `ec_host_cmd_add_suppressed()`

```c
int ec_host_cmd_add_suppressed ( uint16_t cmd_id)
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

添加一个被抑制的命令（Suppressed Command）。

被抑制的命令（Suppressed Commands）不会记入日志。添加一个要抑制记录的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cmd_id` | 要抑制记录的命令 ID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；若超出可抑制命令的最大数量，则返回 `-EIO`。 |

<a id="gaf3b87533037c4d865641643736904d02"></a>

### `ec_host_cmd_get_hc()`

```c
const struct ec_host_cmd * ec_host_cmd_get_hc ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

获取嵌入式控制器（EC）主机命令的主结构体。

此例程返回指向主机命令主结构体（Main Host Command Structure）的指针，允许应用代码按需获取内部信息，例如主机命令线程 ID。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `A` | 指向主机命令主结构体（Main Host Command Structure）的指针。 |

<a id="gaab1fdcb0fd13a19447d262d496b8aed9"></a>

### `ec_host_cmd_init()`

```c
int ec_host_cmd_init ( struct ec_host_cmd_backend * backend)
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

初始化主机命令子系统（Host Command Subsystem）。

此例程初始化主机命令子系统（Host Command Subsystem），包括后端（Backend）与处理函数的初始化。当应用配置了 `zephyr,host-cmd-espi-backend`、`zephyr,host-cmd-shi-backend` 或 `zephyr,host-cmd-uart-backend` 的 chosen 节点，并设置 `CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT` 时，所选后端按 `CONFIG_EC_HOST_CMD_INIT_PRIORITY` 自动调用此例程。需要在运行时选择后端的应用必须将 `CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT` 设为 `n`，并显式调用此例程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] backend` | 指向要初始化的后端结构体（Backend Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="gadbee4a2588abeb6db63f70a90b67a8fb"></a>

### `ec_host_cmd_rx_notify()`

```c
void ec_host_cmd_rx_notify ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

发出新主机命令的通知（Signal）。

发出已收到新主机命令的信号。后端将数据复制到 RX 缓冲区并设置长度后，应调用此函数。

<a id="ga0af800c7a27eb6d0a35179f472a3c37e"></a>

### `ec_host_cmd_send_in_progress_continue()`

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_continue ( ec_host_cmd_in_progress_cb_t cb, void * user_data )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

返回 `EC_HOST_CMD_IN_PROGRESS` 后，在回调中继续执行处理函数（Handler）。

主机命令处理函数可返回 `EC_HOST_CMD_IN_PROGRESS`，同时仍需继续处理。在返回此状态之前，应调用本函数并提供之后要执行的回调。回调返回的状态将被保存，可通过 `ec_host_cmd_send_in_progress_status` 获取。可使用 `ec_host_cmd_send_in_progress_ended` 检查回调是否结束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 从命令处理函数返回后要调用的回调（Callback）。 |
| `[in] user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `EC_HOST_CMD_BUSY` | 已有任一命令正在进行时；否则为 `EC_HOST_CMD_SUCCESS`。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS`。

<a id="ga9a234157f85e06413b60682055d44fd3"></a>

### `ec_host_cmd_send_in_progress_ended()`

```c
bool ec_host_cmd_send_in_progress_ended ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

检查曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令（Host Command）是否已结束。

发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令不会发送最终结果。可通过 `ec_host_cmd_send_in_progress_status` 函数获取最终结果。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 主机命令已结束时。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS`。

<a id="ga9d8349220771fd9570432c3e3bea3066"></a>

### `ec_host_cmd_send_in_progress_status()`

```c
enum ec_host_cmd_status ec_host_cmd_send_in_progress_status ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

获取最近一次曾发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令的最终结果（Final Result）。

发送 `EC_HOST_CMD_IN_PROGRESS` 状态的主机命令不会发送最终结果。使用此函数获取保存的状态。状态只能获取一次，后续调用返回 `EC_HOST_CMD_UNAVAILABLE`。

不支持为发送响应数据的主机命令保存状态。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | 最终状态；若不可用，则为 `EC_HOST_CMD_UNAVAILABLE`。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS`。

<a id="ga95f36f8cf2d21ea73bd8a36f3f7303e8"></a>

### `ec_host_cmd_send_response()`

```c
int ec_host_cmd_send_response ( enum ec_host_cmd_status status, const struct ec_host_cmd_handler_args * args )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

发送主机命令响应（Host Command Response）。

此例程发送主机命令响应。应使用它发送 `IN_PROGRESS` 状态，或在主机命令处理函数不返回时（例如重启命令）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] status` | 要发送的主机命令状态（Host Command Status）。 |
| `[in] args` | 指向传给处理函数的结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="gaaf267a44816e5f856db2092fca681d3e"></a>

### `ec_host_cmd_set_user_cb()`

```c
void ec_host_cmd_set_user_cb ( ec_host_cmd_user_cb_t cb, void * user_data )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

安装用于接收主机命令（Host Command）的用户回调。

允许安装用户在收到命令后需要执行的自定义处理流程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 要安装的回调（Callback）。 |
| `[in] user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

<a id="gaaa3dc6c413b9637a3817cf82e138b27a"></a>

### `ec_host_cmd_task()`

```c
FUNC_NORETURN void ec_host_cmd_task ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

主机命令子系统（Host Command Subsystem）的线程函数。

此例程调用主机命令线程入口函数（Thread Entry Function）。未定义 `CONFIG_EC_HOST_CMD_DEDICATED_THREAD` 时，不创建新线程，必须由应用代码调用此函数。此函数不会返回。


## 3.9\_原页交叉引用（Cross References）

- [主机命令驱动后端 API（Host Command Driver Backend API）](../api_power_policy_topic_reference/P004_主机命令驱动后端 API（Host Command Driver Backend API）.md)
- [模拟器（Simulator）](../api_auxiliary_topic_reference/P005_模拟器（Simulator）.md)
- [ec_host_cmd.h](../api_file_host_video_reference/P006_zephyr__mgmt__ec_host_cmd__ec_host_cmd.h_文件参考.md)
- [ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)
- [ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)
- [ec_host_cmd_handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md)
- [ec_host_cmd_request_header](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md)
- [ec_host_cmd_response_header](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [BIT(0)](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT)
- [CONFIG_EC_HOST_CMD_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EC_HOST_CMD_INIT_PRIORITY)
- [CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [CONFIG_EC_HOST_CMD_DEDICATED_THREAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EC_HOST_CMD_DEDICATED_THREAD)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructec__host__cmd__handler_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38"></a>
<a id="gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81"></a>
<a id="gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6"></a>
<a id="gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1"></a>
<a id="gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b"></a>
<a id="ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af"></a>
<a id="ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20"></a>
<a id="ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8"></a>
<a id="ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985"></a>
<a id="gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_通用音频配置文件（Common Audio Profile，CAP）.md) · [返回大纲](大纲.md) · [下一章](P004_多功能设备（MFD）MAX2221X.md)
