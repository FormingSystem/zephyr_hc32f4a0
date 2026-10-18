---
id: learning.zephyr-docs.networking.api-192
title: OCPP头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ocpp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第192章\_OCPP头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ocpp_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 192.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

```c
#include <stdio.h>
```

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/net/net_ip.h>
```

```c
#include <zephyr/net/tls_credentials.h>
```

## 192.2\_数据结构（Data Structures）

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

## 192.3\_宏定义（Macros）

<a id="r_gaad737e5b91eba7a972da88097f8894e9"></a>

```c
#define CISTR50 50
```

字符串字面量的最大长度，例如 `idtag`。

相关声明：[CISTR50](P191_OCPP完整API参考.md#gaad737e5b91eba7a972da88097f8894e9)。

## 192.4\_类型定义（Typedefs）

<a id="r_ga6cbb071143791698356c7d5787151947"></a>

```c
typedef void * ocpp_session_handle_t
```

供 `ocpp_*` API 作为参数使用的不透明会话句柄（Opaque Session Handle）。

相关声明：[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)。

<a id="r_ga306ab09a7e1ce5eb37a25a6933fd8228"></a>

```c
typedef int(* ocpp_user_notify_callback_t) (enum ocpp_notify_reason reason, union ocpp_io_value *io, void *user_data)
```

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

相关声明：[ocpp_user_notify_callback_t](P191_OCPP完整API参考.md#ga306ab09a7e1ce5eb37a25a6933fd8228)、[ocpp_notify_reason](P191_OCPP完整API参考.md#ga96b1352538137fc49587f4aad069fa66)、[ocpp_io_value](P197_OCPP回调输入输出联合体.md)。

## 192.5\_枚举（Enumerations）

<a id="r_ga4b2b8885d144627d43e724a3889ee1cb"></a>

```c
enum ocpp_auth_status { OCPP_AUTH_INVALID , OCPP_AUTH_ACCEPTED , OCPP_AUTH_BLOCKED , OCPP_AUTH_EXPIRED , OCPP_AUTH_CONCURRENT_TX }
```

OCPP 授权请求所返回的身份标记（IdTag）授权状态（Authorization Status）。

相关声明：[ocpp_auth_status](P191_OCPP完整API参考.md#ga4b2b8885d144627d43e724a3889ee1cb)、[OCPP_AUTH_INVALID](P191_OCPP完整API参考.md#gga4b2b8885d144627d43e724a3889ee1cba15b29195fc077bd2cf58a1fda047a5c3)、[OCPP_AUTH_ACCEPTED](P191_OCPP完整API参考.md#gga4b2b8885d144627d43e724a3889ee1cba1345c54c53dd0088aa5de6763dd15cc2)、[OCPP_AUTH_BLOCKED](P191_OCPP完整API参考.md#gga4b2b8885d144627d43e724a3889ee1cba23198c5ad01a58694a5f42593f97d026)、[OCPP_AUTH_EXPIRED](P191_OCPP完整API参考.md#gga4b2b8885d144627d43e724a3889ee1cbae90129c78fda6c9f21aaadba45a11959)、[OCPP_AUTH_CONCURRENT_TX](P191_OCPP完整API参考.md#gga4b2b8885d144627d43e724a3889ee1cbac4064ac7c1f2ed004965e9441d19b88d)。

<a id="r_ga96b1352538137fc49587f4aad069fa66"></a>

```c
enum ocpp_notify_reason { OCPP_USR_GET_METER_VALUE , OCPP_USR_START_CHARGING , OCPP_USR_STOP_CHARGING , OCPP_USR_UNLOCK_CONNECTOR }
```



相关声明：[ocpp_notify_reason](P191_OCPP完整API参考.md#ga96b1352538137fc49587f4aad069fa66)、[OCPP_USR_GET_METER_VALUE](P191_OCPP完整API参考.md#gga96b1352538137fc49587f4aad069fa66a93ad1eb3396e70cfc25c76393175c0ab)、[OCPP_USR_START_CHARGING](P191_OCPP完整API参考.md#gga96b1352538137fc49587f4aad069fa66a08926167e33944dac03db3bb07d45a00)、[OCPP_USR_STOP_CHARGING](P191_OCPP完整API参考.md#gga96b1352538137fc49587f4aad069fa66a502f9e4a4ef623f5e669747fcf22b6fd)、[OCPP_USR_UNLOCK_CONNECTOR](P191_OCPP完整API参考.md#gga96b1352538137fc49587f4aad069fa66a3570d5e28bc4efc360da47d0f31787b8)。

<a id="r_ga626b8c34f21c59cebdd844218a26f809"></a>

```c
enum ocpp_meter_measurand { OCPP_OMM_CURRENT_FROM_EV , OCPP_OMM_CURRENT_TO_EV , OCPP_OMM_CURRENT_MAX_OFFERED_TO_EV , OCPP_OMM_ACTIVE_ENERGY_FROM_EV , OCPP_OMM_ACTIVE_ENERGY_TO_EV , OCPP_OMM_REACTIVE_ENERGY_FROM_EV , OCPP_OMM_REACTIVE_ENERGY_TO_EV , OCPP_OMM_ACTIVE_POWER_FROM_EV , OCPP_OMM_ACTIVE_POWER_TO_EV , OCPP_OMM_REACTIVE_POWER_FROM_EV , OCPP_OMM_REACTIVE_POWER_TO_EV , OCPP_OMM_POWERLINE_FREQ , OCPP_OMM_POWER_FACTOR , OCPP_OMM_POWER_MAX_OFFERED_TO_EV , OCPP_OMM_FAN_SPEED , OCPP_OMM_CHARGING_PERCENT , OCPP_OMM_TEMPERATURE , OCPP_OMM_VOLTAGE_AC_RMS , OCPP_OMM_END }
```

OCPP 库通过用户回调请求填写的计量读数（Meter Readings）。

相关声明：[ocpp_meter_measurand](P191_OCPP完整API参考.md#ga626b8c34f21c59cebdd844218a26f809)、[OCPP_OMM_CURRENT_FROM_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809aed5d3d42b3927cab608c4dc3a16e3724)、[OCPP_OMM_CURRENT_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a4fa1401134fe057b051a7131049e8e44)、[OCPP_OMM_CURRENT_MAX_OFFERED_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a933787dfcec73082ebd4c0144fdd0cd9)、[OCPP_OMM_ACTIVE_ENERGY_FROM_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809ace0bd2c98033300135471c5f1fea1c06)、[OCPP_OMM_ACTIVE_ENERGY_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a66ccc789070a28f21fd8e4521b967d83)、[OCPP_OMM_REACTIVE_ENERGY_FROM_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a36bb5a1d957b77c8b6d65042f2c589ac)、[OCPP_OMM_REACTIVE_ENERGY_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a01fb33e7bc399d4b685d396720b698c1)、[OCPP_OMM_ACTIVE_POWER_FROM_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a35a9bb9bf371166906479455c1c9178a)、[OCPP_OMM_ACTIVE_POWER_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a5b720f10cb8518951c8dc7f209e22490)、[OCPP_OMM_REACTIVE_POWER_FROM_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809ab379992411707f5eec45287163d288fc)、[OCPP_OMM_REACTIVE_POWER_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a91b3027a78c2bb5069ac655b614f3e6e)、[OCPP_OMM_POWERLINE_FREQ](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809accddeeb3811744536e7f280610c748a0)、[OCPP_OMM_POWER_FACTOR](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809ae9e74f6c45265912220d9a3758a2df0c)、[OCPP_OMM_POWER_MAX_OFFERED_TO_EV](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a224d2d25d57886c8200fd0a447e5faae)、[OCPP_OMM_FAN_SPEED](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809affb62430884b2c8976fdd2c21fc383eb)、[OCPP_OMM_CHARGING_PERCENT](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809aeb80f2a3820318120d9ae62f11bbb15d)、[OCPP_OMM_TEMPERATURE](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a40a3b80da74a8645f6bb50be64b23ace)、[OCPP_OMM_VOLTAGE_AC_RMS](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a06e0a29177bc5b0d920de921e10b7186)、[OCPP_OMM_END](P191_OCPP完整API参考.md#gga626b8c34f21c59cebdd844218a26f809a6aaf34eb8cd7a9c538f70f7c2909e9b0)。

## 192.6\_函数（Functions）

<a id="r_gad6b888a526a57532feb21dcf8a6bd071"></a>

```c
int ocpp_init (struct ocpp_cp_info *cpi, struct ocpp_cs_info *csi, ocpp_user_notify_callback_t cb, void *user_data)
```

初始化 OCPP 库。

相关声明：[ocpp_init](P191_OCPP完整API参考.md#gad6b888a526a57532feb21dcf8a6bd071)、[ocpp_cp_info](P194_OCPP充电桩信息结构.md)、[ocpp_cs_info](P195_OCPP中央系统信息结构.md)、[ocpp_user_notify_callback_t](P191_OCPP完整API参考.md#ga306ab09a7e1ce5eb37a25a6933fd8228)。

<a id="r_ga0cf7081249c509eb467df6147b0e6110"></a>

```c
int ocpp_session_open (ocpp_session_handle_t *hndl)
```

请求新会话（Session）的 API。

相关声明：[ocpp_session_open](P191_OCPP完整API参考.md#ga0cf7081249c509eb467df6147b0e6110)、[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)。

<a id="r_ga7bce1312f3e08bb9862b9162a231c9c4"></a>

```c
void ocpp_session_close (ocpp_session_handle_t hndl)
```

关闭会话的 API。

相关声明：[ocpp_session_close](P191_OCPP完整API参考.md#ga7bce1312f3e08bb9862b9162a231c9c4)、[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)。

<a id="r_ga59e708015c120bba1414ff8331080e20"></a>

```c
int ocpp_authorize (ocpp_session_handle_t hndl, char *idtag, enum ocpp_auth_status *status, uint32_t timeout_ms)
```

向中央系统发送授权请求，以确定 `idtag` 是否有效。

相关声明：[ocpp_authorize](P191_OCPP完整API参考.md#ga59e708015c120bba1414ff8331080e20)、[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)、[ocpp_auth_status](P191_OCPP完整API参考.md#ga4b2b8885d144627d43e724a3889ee1cb)。

<a id="r_gafc9982ab1d88e9af2ebe647c671876c6"></a>

```c
int ocpp_start_transaction (ocpp_session_handle_t hndl, int meter_val, uint8_t conn_id, uint32_t timeout_ms)
```

向中央系统通知交易开始（Transaction Start）。

相关声明：[ocpp_start_transaction](P191_OCPP完整API参考.md#gafc9982ab1d88e9af2ebe647c671876c6)、[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)。

<a id="r_ga94824d57e36cc817619523aaded8ece1"></a>

```c
int ocpp_stop_transaction (ocpp_session_handle_t hndl, int meter_val, uint32_t timeout_ms)
```

向中央系统通知交易已经停止（Transaction Stopped）。

相关声明：[ocpp_stop_transaction](P191_OCPP完整API参考.md#ga94824d57e36cc817619523aaded8ece1)、[ocpp_session_handle_t](P191_OCPP完整API参考.md#ga6cbb071143791698356c7d5787151947)。

## 192.7\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

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

[上一章](P191_OCPP完整API参考.md) · [返回大纲](大纲.md) · [下一章](P193_OCPP头文件源码.md)
