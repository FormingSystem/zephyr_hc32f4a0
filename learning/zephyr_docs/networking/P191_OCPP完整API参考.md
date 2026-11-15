---
id: learning.zephyr-docs.networking.api-191
title: OCPP完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ocpp__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_OCPP完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ocpp__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 191.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

开放充电桩协议（Open Charge Point Protocol，OCPP）的充电桩（Charge Point，CP）实现。

开放充电桩协议（Open Charge Point Protocol，OCPP）的充电桩（Charge Point，CP）实现。引入版本（Since）：4.3；API 版本（Version）：`0.1.0`。注意：本实现要求启用 WebSocket 模块，默认使用 OCPP 1.6。

## 191.2\_数据结构（Data Structures）

<a id="r_ocpp_5Fio_5Fvalue"></a>

```c
union ocpp_io_value
```

用于 OCPP 用户回调通知／请求的输入输出值。访问联合体（Union）成员时，应根据 `ocpp_notify_reason` 的枚举值选择对应成员。

相关声明：[ocpp_io_value](P197_OCPP回调输入输出联合体.md)。

<a id="r_ocpp_5Fcp_5Finfo"></a>

```c
struct ocpp_cp_info
```

传给 `ocpp_init` 的充电桩（Charge Point，CP）信息参数。除 `num_of_con` 外，各项均为字符串字面量（String Literal）。

相关声明：[ocpp_cp_info](P194_OCPP充电桩信息结构.md)。

<a id="r_ocpp_5Ftls_5Fcredentials"></a>

```c
struct ocpp_tls_credentials
```

中央系统（Central System，CS）的传输层安全（Transport Layer Security，TLS）凭据信息。

相关声明：[ocpp_tls_credentials](P196_OCPP的TLS凭据结构.md)。

<a id="r_ocpp_5Fcs_5Finfo"></a>

```c
struct ocpp_cs_info
```

传给 `ocpp_init` 的中央系统（Central System，CS）信息参数。

相关声明：[ocpp_cs_info](P195_OCPP中央系统信息结构.md)。

## 191.3\_宏定义（Macros）

<a id="r_gaad737e5b91eba7a972da88097f8894e9"></a>

```c
#define CISTR50 50
```

字符串字面量的最大长度，例如 `idtag`。

## 191.4\_类型定义（Typedefs）

<a id="r_ga6cbb071143791698356c7d5787151947"></a>

```c
typedef void * ocpp_session_handle_t
```

供 `ocpp_*` API 作为参数使用的不透明会话句柄（Opaque Session Handle）。

<a id="r_ga306ab09a7e1ce5eb37a25a6933fd8228"></a>

```c
typedef int(* ocpp_user_notify_callback_t) (enum ocpp_notify_reason reason, union ocpp_io_value *io, void *user_data)
```

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

相关声明：[ocpp_io_value](P197_OCPP回调输入输出联合体.md)。

## 191.5\_枚举（Enumerations）

<a id="r_ga4b2b8885d144627d43e724a3889ee1cb"></a>

```c
enum ocpp_auth_status { OCPP_AUTH_INVALID , OCPP_AUTH_ACCEPTED , OCPP_AUTH_BLOCKED , OCPP_AUTH_EXPIRED , OCPP_AUTH_CONCURRENT_TX }
```

OCPP 授权请求所返回的身份标记（IdTag）授权状态（Authorization Status）。

<a id="r_ga96b1352538137fc49587f4aad069fa66"></a>

```c
enum ocpp_notify_reason { OCPP_USR_GET_METER_VALUE , OCPP_USR_START_CHARGING , OCPP_USR_STOP_CHARGING , OCPP_USR_UNLOCK_CONNECTOR }
```



<a id="r_ga626b8c34f21c59cebdd844218a26f809"></a>

```c
enum ocpp_meter_measurand { OCPP_OMM_CURRENT_FROM_EV , OCPP_OMM_CURRENT_TO_EV , OCPP_OMM_CURRENT_MAX_OFFERED_TO_EV , OCPP_OMM_ACTIVE_ENERGY_FROM_EV , OCPP_OMM_ACTIVE_ENERGY_TO_EV , OCPP_OMM_REACTIVE_ENERGY_FROM_EV , OCPP_OMM_REACTIVE_ENERGY_TO_EV , OCPP_OMM_ACTIVE_POWER_FROM_EV , OCPP_OMM_ACTIVE_POWER_TO_EV , OCPP_OMM_REACTIVE_POWER_FROM_EV , OCPP_OMM_REACTIVE_POWER_TO_EV , OCPP_OMM_POWERLINE_FREQ , OCPP_OMM_POWER_FACTOR , OCPP_OMM_POWER_MAX_OFFERED_TO_EV , OCPP_OMM_FAN_SPEED , OCPP_OMM_CHARGING_PERCENT , OCPP_OMM_TEMPERATURE , OCPP_OMM_VOLTAGE_AC_RMS , OCPP_OMM_END }
```

OCPP 库通过用户回调请求填写的计量读数（Meter Readings）。

## 191.6\_函数（Functions）

<a id="r_gad6b888a526a57532feb21dcf8a6bd071"></a>

```c
int ocpp_init (struct ocpp_cp_info *cpi, struct ocpp_cs_info *csi, ocpp_user_notify_callback_t cb, void *user_data)
```

初始化 OCPP 库。

相关声明：[ocpp_cp_info](P194_OCPP充电桩信息结构.md)、[ocpp_cs_info](P195_OCPP中央系统信息结构.md)。

<a id="r_ga0cf7081249c509eb467df6147b0e6110"></a>

```c
int ocpp_session_open (ocpp_session_handle_t *hndl)
```

请求新会话（Session）的 API。

<a id="r_ga7bce1312f3e08bb9862b9162a231c9c4"></a>

```c
void ocpp_session_close (ocpp_session_handle_t hndl)
```

关闭会话的 API。

<a id="r_ga59e708015c120bba1414ff8331080e20"></a>

```c
int ocpp_authorize (ocpp_session_handle_t hndl, char *idtag, enum ocpp_auth_status *status, uint32_t timeout_ms)
```

向中央系统发送授权请求，以确定 `idtag` 是否有效。

<a id="r_gafc9982ab1d88e9af2ebe647c671876c6"></a>

```c
int ocpp_start_transaction (ocpp_session_handle_t hndl, int meter_val, uint8_t conn_id, uint32_t timeout_ms)
```

向中央系统通知交易开始（Transaction Start）。

<a id="r_ga94824d57e36cc817619523aaded8ece1"></a>

```c
int ocpp_stop_transaction (ocpp_session_handle_t hndl, int meter_val, uint32_t timeout_ms)
```

向中央系统通知交易已经停止（Transaction Stopped）。

## 191.7\_详细说明（Detailed Documentation）

<a id="gaad737e5b91eba7a972da88097f8894e9"></a>

### `CISTR50`

```c
#define CISTR50 50
```

```c
#include <zephyr/net/ocpp.h>
```

字符串字面量的最大长度，例如 `idtag`。

<a id="ga6cbb071143791698356c7d5787151947"></a>

### `ocpp_session_handle_t`

```c
typedef void* ocpp_session_handle_t
```

```c
#include <zephyr/net/ocpp.h>
```

供 `ocpp_*` API 作为参数使用的不透明会话句柄（Opaque Session Handle）。

<a id="ga306ab09a7e1ce5eb37a25a6933fd8228"></a>

### `ocpp_user_notify_callback_t`

```c
typedef int(* ocpp_user_notify_callback_t) (enum ocpp_notify_reason reason, union ocpp_io_value *io, void *user_data)
```

```c
#include <zephyr/net/ocpp.h>
```

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

建议回调不要长时间占用执行上下文，以免阻塞 OCPP 协议栈／库。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] reason` | 此次调用回调的原因。 |
| `[in] io` | 根据 `reason` 访问相应的输入输出成员。 |
| `[in] user_data` | 调用 `ocpp_init` 时传入的用户数据。 |

**返回（Returns）**：返回 `0` 或负错误码，错误码定义见 `errno.h`。

> 译注（源码核对）：原参数表将 `io` 标为输入（`[in]`），但这并不表示联合体的所有成员只读。读取电表时，库先给出 `meter_val.id_con` 和 `meter_val.mes`，应用必须填写 `meter_val.val` 后返回。当前内部处理线程直接调用该回调；“异步事件”不表示库会为每次回调创建独立线程。长操作应按应用需要转交其他执行上下文，详见[联合体参考](P197_OCPP回调输入输出联合体.md)。

<a id="ga4b2b8885d144627d43e724a3889ee1cb"></a>

### `ocpp_auth_status`

```c
enum ocpp_auth_status
```

```c
#include <zephyr/net/ocpp.h>
```

OCPP 授权请求所返回的身份标记（IdTag）授权状态（Authorization Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OCPP_AUTH_INVALID` | 身份标记（IdTag）无效。 |
| `OCPP_AUTH_ACCEPTED` | 已接受，允许充电。 |
| `OCPP_AUTH_BLOCKED` | 被阻止充电。 |
| `OCPP_AUTH_EXPIRED` | 身份标记已过期，不允许充电。 |
| `OCPP_AUTH_CONCURRENT_TX` | 同一身份标记正被并发使用。 |

<a id="ga626b8c34f21c59cebdd844218a26f809"></a>

### `ocpp_meter_measurand`

```c
enum ocpp_meter_measurand
```

```c
#include <zephyr/net/ocpp.h>
```

OCPP 库通过用户回调请求填写的计量读数（Meter Readings）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OCPP_OMM_CURRENT_FROM_EV` | 来自电动汽车（Electric Vehicle，EV）的电流，单位为安培（A）。 |
| `OCPP_OMM_CURRENT_TO_EV` | 流向电动汽车（EV）的电流，单位为安培（A）。 |
| `OCPP_OMM_CURRENT_MAX_OFFERED_TO_EV` | 可向电动汽车提供的最大电流，单位为安培（A）。 |
| `OCPP_OMM_ACTIVE_ENERGY_FROM_EV` | 来自电动汽车的有功电能（Active Energy），单位为瓦时（Wh）。 |
| `OCPP_OMM_ACTIVE_ENERGY_TO_EV` | 输送给电动汽车的有功电能，单位为瓦时（Wh）。 |
| `OCPP_OMM_REACTIVE_ENERGY_FROM_EV` | 来自电动汽车的无功电能（Reactive Energy），单位为乏时（varh）。 |
| `OCPP_OMM_REACTIVE_ENERGY_TO_EV` | 输送给电动汽车的无功电能，单位为乏时（varh）。 |
| `OCPP_OMM_ACTIVE_POWER_FROM_EV` | 来自电动汽车的有功功率（Active Power），单位为瓦特（W）。 |
| `OCPP_OMM_ACTIVE_POWER_TO_EV` | 输送给电动汽车的有功功率，单位为瓦特（W）。 |
| `OCPP_OMM_REACTIVE_POWER_FROM_EV` | 来自电动汽车的无功功率（Reactive Power），单位为乏（var）。 |
| `OCPP_OMM_REACTIVE_POWER_TO_EV` | 输送给电动汽车的无功功率，单位为乏（var）。 |
| `OCPP_OMM_POWERLINE_FREQ` | 电力线频率（Powerline Frequency），单位为赫兹（Hz）。 |
| `OCPP_OMM_POWER_FACTOR` | 供电功率因数（Power Factor）。 |
| `OCPP_OMM_POWER_MAX_OFFERED_TO_EV` | 可向电动汽车提供的最大功率，单位为瓦特（W）。 |
| `OCPP_OMM_FAN_SPEED` | 风扇转速，单位为转每分钟（rpm）。 |
| `OCPP_OMM_CHARGING_PERCENT` | 充电百分比（Charging Percentage）。 |
| `OCPP_OMM_TEMPERATURE` | 充电桩内部温度，单位为摄氏度（Celsius）。 |
| `OCPP_OMM_VOLTAGE_AC_RMS` | 交流供电电压的均方根值（Root Mean Square，RMS），单位为伏特（V）。 |
| `OCPP_OMM_END` |  |

<a id="ga96b1352538137fc49587f4aad069fa66"></a>

### `ocpp_notify_reason`

```c
enum ocpp_notify_reason
```

```c
#include <zephyr/net/ocpp.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OCPP_USR_GET_METER_VALUE` | 用户必须填写当前读数。 |
| `OCPP_USR_START_CHARGING` | 按本地收到身份标记时的流程处理开始充电请求，例如进行授权等。 |
| `OCPP_USR_STOP_CHARGING` | 执行停止充电流程。 |
| `OCPP_USR_UNLOCK_CONNECTOR` | 解锁充电桩的机械连接器（Mechanical Connector）。 |

<a id="ga59e708015c120bba1414ff8331080e20"></a>

### `ocpp_authorize()`

```c
int ocpp_authorize ( ocpp_session_handle_t hndl, char * idtag, enum ocpp_auth_status * status, uint32_t timeout_ms )
```

```c
#include <zephyr/net/ocpp.h>
```

向中央系统发送授权请求，以确定 `idtag` 是否有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] hndl` | 会话句柄。 |
| `[in] idtag` | 待查询授权有效性的身份标记，字符串字面量。 |
| `[out] status` | 授权状态。 |
| `[in] timeout_ms` | 超时时间，单位为毫秒（ms）。 |

**返回（Returns）**：成功返回 `0`；失败返回 `errno.h` 中的负错误码，以指明失败原因。

> 译注（源码核对）：当前官方实现成功收取并处理响应后，将授权结果写入 `status` 并返回 `0`。因此 `0` 只表示这次 API 操作成功，允许充电还需检查 `status == OCPP_AUTH_ACCEPTED`。尚未准备好时可能返回 `-EAGAIN`；错误返回时不能直接使用输出状态作授权判断。

<a id="gad6b888a526a57532feb21dcf8a6bd071"></a>

### `ocpp_init()`

```c
int ocpp_init ( struct ocpp_cp_info * cpi, struct ocpp_cs_info * csi, ocpp_user_notify_callback_t cb, void * user_data )
```

```c
#include <zephyr/net/ocpp.h>
```

初始化 OCPP 库。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cpi` | 充电桩信息。 |
| `[in] csi` | 中央系统信息。 |
| `[in] cb` | 用户注册的回调。 |
| `[in] user_data` | 回调时会传入同一份引用。 |

**返回（Returns）**：成功返回 `0`；失败返回 `errno.h` 中的负错误码，以指明失败原因。

**注意（Note）**：必须先调用此函数，再调用其他 OCPP API。

> 译注（源码核对）：当前实现检查必需信息和回调后创建内部上下文、网络读取线程和内部处理线程。返回 `0` 不等于中央系统已经接受启动通知（BootNotification），后续请求仍可能因状态未就绪返回 `-EAGAIN`。应保持初始化、每连接器独立会话、授权与交易调用的次序。

<a id="ga7bce1312f3e08bb9862b9162a231c9c4"></a>

### `ocpp_session_close()`

```c
void ocpp_session_close ( ocpp_session_handle_t hndl)
```

```c
#include <zephyr/net/ocpp.h>
```

关闭会话的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] hndl` | 调用会话打开接口时获得的句柄。 |

<a id="ga0cf7081249c509eb467df6147b0e6110"></a>

### `ocpp_session_open()`

```c
int ocpp_session_open ( ocpp_session_handle_t * hndl)
```

```c
#include <zephyr/net/ocpp.h>
```

请求新会话（Session）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] hndl` | 有效的不透明句柄。 |

**返回（Returns）**：成功返回 `0`；失败返回 `errno.h` 中的负错误码，以指明失败原因。

**注意（Note）**：每个连接器都应在 `ocpp_init` 之后、其他 `ocpp_*` 请求消息 API 之前，打开自己的独立会话。

<a id="gafc9982ab1d88e9af2ebe647c671876c6"></a>

### `ocpp_start_transaction()`

```c
int ocpp_start_transaction ( ocpp_session_handle_t hndl, int meter_val, uint8_t conn_id, uint32_t timeout_ms )
```

```c
#include <zephyr/net/ocpp.h>
```

向中央系统通知交易开始（Transaction Start）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] hndl` | 会话句柄。 |
| `[in] meter_val` | 该连接器的电能表读数，单位为瓦时（Wh）。 |
| `[in] conn_id` | 连接器标识应为大于 `0` 的连续编号。 |
| `[in] timeout_ms` | 超时时间，单位为毫秒（ms）。 |

**返回（Returns）**：成功返回 `0`。`EACCES` 表示未获授权，应进入停止充电流程；也可能返回 `errno.h` 中表示失败原因的负错误码。原文此处写作 `EACCES`，具体正负号见下方源码核对译注。

> 译注（源码核对）：原返回说明写作 `EACCES`，当前核心实现实际返回 `-EACCES`。`meter_val` 是电能表读数（Wh），不是瓦特数（W）或耗时。当前离线分支直接返回 `0`，旁边仍有保存交易／电表数据的 TODO；不能据此声称服务端已经接受交易或离线持久化补报已经完整实现。

<a id="ga94824d57e36cc817619523aaded8ece1"></a>

### `ocpp_stop_transaction()`

```c
int ocpp_stop_transaction ( ocpp_session_handle_t hndl, int meter_val, uint32_t timeout_ms )
```

```c
#include <zephyr/net/ocpp.h>
```

向中央系统通知交易已经停止（Transaction Stopped）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] hndl` | 会话句柄。 |
| `[in] meter_val` | 该连接器的电能表读数，单位为瓦时（Wh）。 |
| `[in] timeout_ms` | 超时时间，单位为毫秒（ms）。 |

**返回（Returns）**：成功返回 `0`；失败返回 `errno.h` 中的负错误码，以指明失败原因。

## 191.8\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

> 译注——条件成员（Conditional Member）：本批中央系统结构的 Doxygen 页面只展示 `cs_ip`、`ws_url`、`port` 与 `sa_family`。原始头文件在 `CONFIG_NET_SOCKETS_SOCKOPT_TLS` 启用时，还声明 `struct ocpp_tls_credentials creds`，保存中央系统 TLS 凭据；该成员不在所有配置下都存在。详见[TLS 凭据结构](P196_OCPP的TLS凭据结构.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4b2b8885d144627d43e724a3889ee1cba15b29195fc077bd2cf58a1fda047a5c3"></a>
<a id="gga4b2b8885d144627d43e724a3889ee1cba1345c54c53dd0088aa5de6763dd15cc2"></a>
<a id="gga4b2b8885d144627d43e724a3889ee1cba23198c5ad01a58694a5f42593f97d026"></a>
<a id="gga4b2b8885d144627d43e724a3889ee1cbae90129c78fda6c9f21aaadba45a11959"></a>
<a id="gga4b2b8885d144627d43e724a3889ee1cbac4064ac7c1f2ed004965e9441d19b88d"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809aed5d3d42b3927cab608c4dc3a16e3724"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a4fa1401134fe057b051a7131049e8e44"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a933787dfcec73082ebd4c0144fdd0cd9"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809ace0bd2c98033300135471c5f1fea1c06"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a66ccc789070a28f21fd8e4521b967d83"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a36bb5a1d957b77c8b6d65042f2c589ac"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a01fb33e7bc399d4b685d396720b698c1"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a35a9bb9bf371166906479455c1c9178a"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a5b720f10cb8518951c8dc7f209e22490"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809ab379992411707f5eec45287163d288fc"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a91b3027a78c2bb5069ac655b614f3e6e"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809accddeeb3811744536e7f280610c748a0"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809ae9e74f6c45265912220d9a3758a2df0c"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a224d2d25d57886c8200fd0a447e5faae"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809affb62430884b2c8976fdd2c21fc383eb"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809aeb80f2a3820318120d9ae62f11bbb15d"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a40a3b80da74a8645f6bb50be64b23ace"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a06e0a29177bc5b0d920de921e10b7186"></a>
<a id="gga626b8c34f21c59cebdd844218a26f809a6aaf34eb8cd7a9c538f70f7c2909e9b0"></a>
<a id="gga96b1352538137fc49587f4aad069fa66a93ad1eb3396e70cfc25c76393175c0ab"></a>
<a id="gga96b1352538137fc49587f4aad069fa66a08926167e33944dac03db3bb07d45a00"></a>
<a id="gga96b1352538137fc49587f4aad069fa66a502f9e4a4ef623f5e669747fcf22b6fd"></a>
<a id="gga96b1352538137fc49587f4aad069fa66a3570d5e28bc4efc360da47d0f31787b8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P190_MCP工具记录结构.md) · [返回大纲](大纲.md) · [下一章](P192_OCPP头文件参考.md)
