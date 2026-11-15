---
id: learning.zephyr-docs.api-imaging-input-lwm2m-reference.page-5
title: 轻量级M2M（LwM2M）的高层API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_轻量级M2M（LwM2M）的高层API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

引入版本（Since）：1.9。接口版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 5.1\_主题（Topics）

<a id="r_lwm2m_5Fpath_5Fhelpers"></a>

相关声明：[轻量级M2M（LwM2M）的路径辅助宏。](../api_protocol_topic_reference/P023_轻量级M2M（LwM2M）的路径辅助宏。.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.2\_数据结构（Data Structures）

<a id="r_lwm2m_5Fobj_5Fpath"></a>

```c
struct lwm2m_obj_path
```

相关声明：[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

轻量级M2M（LwM2M）的对象路径结构。

<a id="r_lwm2m_5Fctx"></a>

```c
struct lwm2m_ctx
```

相关声明：[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

用于维护单个轻量级M2M（LwM2M）连接信息的上下文结构。

<a id="r_lwm2m_5Ftime_5Fseries_5Felem"></a>

```c
struct lwm2m_time_series_elem
```

相关声明：[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

轻量级M2M（LwM2M）的时间序列数据结构。

<a id="r_lwm2m_5Fobjlnk"></a>

```c
struct lwm2m_objlnk
```

相关声明：[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

轻量级M2M（LwM2M）的对象链接（Objlnk）资源类型结构。

<a id="r_lwm2m_5Fres_5Fitem"></a>

```c
struct lwm2m_res_item
```

相关声明：[lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)。

轻量级M2M（LwM2M）的资源项结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.3\_宏定义（Macros）

<a id="r_ga34febb0c6fb1c68b0963a6e4dd721763"></a>

```c
#define LWM2M_OBJLNK_MAX_ID USHRT_MAX
```

相关声明：[LWM2M_OBJLNK_MAX_ID](#ga34febb0c6fb1c68b0963a6e4dd721763)。

对象链接（Objlnk）资源字段的最大值。

<a id="r_ga12c2e0af3d3fc6dd5785e08c0d831a67"></a>

```c
#define LWM2M_RES_DATA_READ_ONLY 0
```

相关声明：[LWM2M_RES_DATA_READ_ONLY](#ga12c2e0af3d3fc6dd5785e08c0d831a67)。

资源只读值位（Resource Read-only Value Bit）。

<a id="r_ga1bfa5b7d83e3560828a1fb61a4d07355"></a>

```c
#define LWM2M_RES_DATA_FLAG_RO BIT(LWM2M_RES_DATA_READ_ONLY)
```

相关声明：[LWM2M_RES_DATA_FLAG_RO](#ga1bfa5b7d83e3560828a1fb61a4d07355)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[LWM2M_RES_DATA_READ_ONLY](#ga12c2e0af3d3fc6dd5785e08c0d831a67)。

资源只读标志（Resource Read-only Flag）。

<a id="r_ga49f4117dfec8cd1abe9f827e235f55b0"></a>

```c
#define LWM2M_HAS_RES_FLAG(res, f)
```

相关声明：[LWM2M_HAS_RES_FLAG](#ga49f4117dfec8cd1abe9f827e235f55b0)。

读取资源标志（Resource Flags）的辅助宏。

<a id="r_ga3a3669237762fa8c23686e5e00b7809f"></a>

```c
#define LWM2M_RD_CLIENT_FLAG_BOOTSTRAP BIT(0)
```

相关声明：[LWM2M_RD_CLIENT_FLAG_BOOTSTRAP](#ga3a3669237762fa8c23686e5e00b7809f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在当前会话（Session）中运行引导过程（Bootstrap Procedure）。

<a id="r_gab97329844cd411195add5d72ad6aa4b7"></a>

```c
#define LWM2M_MAX_PATH_STR_SIZE sizeof("/65535/65535/65535/65535")
```

相关声明：[LWM2M_MAX_PATH_STR_SIZE](#gab97329844cd411195add5d72ad6aa4b7)。

LwM2M 路径（Path）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.4\_类型定义（Typedefs）

<a id="r_gae7bf50f9abf1b82b76ac3e9175e685ac"></a>

```c
typedef void(* lwm2m_socket_fault_cb_t) (int error)
```

相关声明：[lwm2m_socket_fault_cb_t](#gae7bf50f9abf1b82b76ac3e9175e685ac)。

遇到套接字错误（Socket Error）时调用的回调函数。

<a id="r_gad7bea67e16e1e831e0f949dbf83d5afe"></a>

```c
typedef void(* lwm2m_observe_cb_t) (enum lwm2m_observe_event event, struct lwm2m_obj_path *path, void *user_data)
```

相关声明：[lwm2m_observe_cb_t](#gad7bea67e16e1e831e0f949dbf83d5afe)、[lwm2m_observe_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

观察（Observe）回调，报告观察者（Observer）的添加与删除，以及通知的确认（ACK）与超时。

<a id="r_ga38dbaf038426efc75d889c4a0666dac9"></a>

```c
typedef void(* lwm2m_ctx_event_cb_t) (struct lwm2m_ctx *ctx, enum lwm2m_rd_client_event event)
```

相关声明：[lwm2m_ctx_event_cb_t](#ga38dbaf038426efc75d889c4a0666dac9)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_rd_client_event](#gaca90ab8960a4ff01d44735dbc0405862)。

异步注册／发现客户端事件回调（Asynchronous RD Client Event Callback）。

<a id="r_ga92d2227f37e7d382bc4f1a7bae21b872"></a>

```c
typedef int(* lwm2m_set_sockopt_cb_t) (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_set_sockopt_cb_t](#ga92d2227f37e7d382bc4f1a7bae21b872)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

<a id="r_ga7a0bb9d5652f7f0fd0cc4a1139be6f37"></a>

```c
typedef bool(* lwm2m_cache_filter_cb_t) (const struct lwm2m_obj_path *path, const struct lwm2m_time_series_elem *element)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lwm2m_cache_filter_cb_t](#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

用于过滤缓存时间序列样本（Cached Time Series Samples）的回调类型。

<a id="r_ga5e531aade0537eb5e3f5756e9287e384"></a>

```c
typedef void *(* lwm2m_engine_get_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, size_t *data_len)
```

相关声明：[lwm2m_engine_get_data_cb_t](#ga5e531aade0537eb5e3f5756e9287e384)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于获取资源缓冲区（Resource Buffer）及其长度的异步回调（Asynchronous Callback）。

<a id="r_ga3afac013b0cf731f9c86dc3791131585"></a>

```c
typedef int(* lwm2m_engine_set_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, uint8_t *data, uint16_t data_len, bool last_block, size_t total_size, size_t offset)
```

相关声明：[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

数据已写入资源缓冲区（Resource Buffer）时调用的异步回调（Asynchronous Callback）。

<a id="r_gabcbca483b310e0c4cd68aef2d9cda0bf"></a>

```c
typedef int(* lwm2m_engine_user_cb_t) (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="r_gaeb32bcd4981b4c7bd891f99668ebc0fe"></a>

```c
typedef int(* lwm2m_engine_execute_cb_t) (uint16_t obj_inst_id, uint8_t *args, uint16_t args_len)
```

相关声明：[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

异步执行通知回调（Asynchronous Execute Notification Callback）。

<a id="r_gaf5394884da53edb28fe4afc92bf40e6a"></a>

```c
typedef void(* lwm2m_send_cb_t) (enum lwm2m_send_status status)
```

相关声明：[lwm2m_send_cb_t](#gaf5394884da53edb28fe4afc92bf40e6a)、[lwm2m_send_status](#ga20848e0942882e8c2cc40ee8a48b7bfd)。

返回发送状态（Send Status）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.5\_枚举（Enumerations）

<a id="r_gac8d63952ec94ca6cfb1dbe12a6c53bfb"></a>

```c
enum lwm2m_observe_event { LWM2M_OBSERVE_EVENT_OBSERVER_ADDED , LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED , LWM2M_OBSERVE_EVENT_NOTIFY_ACK , LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT }
```

相关声明：[lwm2m_observe_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb)、[LWM2M_OBSERVE_EVENT_OBSERVER_ADDED](#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3)、[LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED](#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c)、[LWM2M_OBSERVE_EVENT_NOTIFY_ACK](#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885)、[LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT](#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e)。

观察回调事件（Observe Callback Events）。

<a id="r_gaca90ab8960a4ff01d44735dbc0405862"></a>

```c
enum lwm2m_rd_client_event { LWM2M_RD_CLIENT_EVENT_NONE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE , LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE , LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE , LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT , LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE , LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE , LWM2M_RD_CLIENT_EVENT_DISCONNECT , LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF , LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED , LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR , LWM2M_RD_CLIENT_EVENT_REG_UPDATE , LWM2M_RD_CLIENT_EVENT_DEREGISTER , LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED }
```

相关声明：[lwm2m_rd_client_event](#gaca90ab8960a4ff01d44735dbc0405862)、[LWM2M_RD_CLIENT_EVENT_NONE](#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc)、[LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6)、[LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541)、[LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT](#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404)、[LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683)、[LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f)、[LWM2M_RD_CLIENT_EVENT_DISCONNECT](#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b)、[LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF](#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe)、[LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED](#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525)、[LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR](#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4)、[LWM2M_RD_CLIENT_EVENT_REG_UPDATE](#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd)、[LWM2M_RD_CLIENT_EVENT_DEREGISTER](#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13)、[LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED](#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)。

LwM2M 注册／发现客户端事件（RD Client Events）。

<a id="r_ga7611c1aebb0309ee8340e06dd8ee234d"></a>

```c
enum lwm2m_socket_states { LWM2M_SOCKET_STATE_ONGOING , LWM2M_SOCKET_STATE_ONE_RESPONSE , LWM2M_SOCKET_STATE_LAST , LWM2M_SOCKET_STATE_NO_DATA }
```

相关声明：[lwm2m_socket_states](#ga7611c1aebb0309ee8340e06dd8ee234d)、[LWM2M_SOCKET_STATE_ONGOING](#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab)、[LWM2M_SOCKET_STATE_ONE_RESPONSE](#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711)、[LWM2M_SOCKET_STATE_LAST](#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100)、[LWM2M_SOCKET_STATE_NO_DATA](#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915)。

LwM2M 套接字的不同流量状态（Traffic States）。

<a id="r_ga20848e0942882e8c2cc40ee8a48b7bfd"></a>

```c
enum lwm2m_send_status { LWM2M_SEND_STATUS_SUCCESS , LWM2M_SEND_STATUS_FAILURE , LWM2M_SEND_STATUS_TIMEOUT }
```

相关声明：[lwm2m_send_status](#ga20848e0942882e8c2cc40ee8a48b7bfd)、[LWM2M_SEND_STATUS_SUCCESS](#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4)、[LWM2M_SEND_STATUS_FAILURE](#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd)、[LWM2M_SEND_STATUS_TIMEOUT](#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a)。

LwM2M 发送状态（Send Status）。

<a id="r_ga11de8078091631cb88b26a9a460097ab"></a>

```c
enum lwm2m_security_mode_e { LWM2M_SECURITY_PSK = 0 , LWM2M_SECURITY_RAW_PK = 1 , LWM2M_SECURITY_CERT = 2 , LWM2M_SECURITY_NOSEC = 3 , LWM2M_SECURITY_CERT_EST = 4 }
```

相关声明：[lwm2m_security_mode_e](#ga11de8078091631cb88b26a9a460097ab)、[LWM2M_SECURITY_PSK](#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25)、[LWM2M_SECURITY_RAW_PK](#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716)、[LWM2M_SECURITY_CERT](#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba)、[LWM2M_SECURITY_NOSEC](#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7)、[LWM2M_SECURITY_CERT_EST](#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824)。

LwM2M 安全对象（Security Object）定义的安全模式（Security Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.6\_函数（Functions）

<a id="r_gabf8726f0438477863423947a7bb77ce2"></a>

```c
int lwm2m_device_add_err (uint8_t error_code)
```

相关声明：[lwm2m_device_add_err](#gabf8726f0438477863423947a7bb77ce2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 LwM2M 设备对象（Device Object）注册新的错误码（Error Code）。

<a id="r_ga6878ea0ebb512b19a4fb0859756f51d0"></a>

```c
void lwm2m_firmware_set_write_cb (lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_firmware_set_write_cb](#ga6878ea0ebb512b19a4fb0859756f51d0)、[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)。

设置固件分块传输（Firmware Block Transfer）的数据回调。

<a id="r_ga4bf0bbedf5573ac18a11ac4fced11284"></a>

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb (void)
```

相关声明：[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)、[lwm2m_firmware_get_write_cb](#ga4bf0bbedf5573ac18a11ac4fced11284)。

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

<a id="r_gac4e4a819e54344657d70ec479eb6ec8d"></a>

```c
void lwm2m_firmware_set_write_cb_inst (uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_firmware_set_write_cb_inst](#gac4e4a819e54344657d70ec479eb6ec8d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)。

设置固件分块传输（Firmware Block Transfer）的数据回调。

<a id="r_gad7334f06c3bdb14485597794a417152d"></a>

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)、[lwm2m_firmware_get_write_cb_inst](#gad7334f06c3bdb14485597794a417152d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

<a id="r_ga3955dca5cd6d67807ed75e61a4d84d84"></a>

```c
void lwm2m_firmware_set_cancel_cb (lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_firmware_set_cancel_cb](#ga3955dca5cd6d67807ed75e61a4d84d84)、[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置固件更新取消（Firmware Update Cancel）回调。

<a id="r_ga9561c1b8407d888f6fbe1e0ceab1c235"></a>

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb (void)
```

相关声明：[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)、[lwm2m_firmware_get_cancel_cb](#ga9561c1b8407d888f6fbe1e0ceab1c235)。

获取固件更新取消（Firmware Update Cancel）回调。

<a id="r_gaa200b524e505f64247f1e7472c5f36d4"></a>

```c
void lwm2m_firmware_set_cancel_cb_inst (uint16_t obj_inst_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_firmware_set_cancel_cb_inst](#gaa200b524e505f64247f1e7472c5f36d4)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置固件更新取消（Firmware Update Cancel）的数据回调。

<a id="r_ga6f4b3e08c7e03cff4bf31e2f2999971e"></a>

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)、[lwm2m_firmware_get_cancel_cb_inst](#ga6f4b3e08c7e03cff4bf31e2f2999971e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件更新取消（Firmware Update Cancel）回调。

<a id="r_ga61eb38e42d9e1b3f467c43a324f2fc65"></a>

```c
void lwm2m_firmware_set_update_cb (lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_firmware_set_update_cb](#ga61eb38e42d9e1b3f467c43a324f2fc65)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

<a id="r_ga1e4b8ba1b19ac9025dca3c4799bba84a"></a>

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb (void)
```

相关声明：[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[lwm2m_firmware_get_update_cb](#ga1e4b8ba1b19ac9025dca3c4799bba84a)。

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

<a id="r_ga31d0f3e40b5e3d608d16a4268b2f1b29"></a>

```c
void lwm2m_firmware_set_update_cb_inst (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_firmware_set_update_cb_inst](#ga31d0f3e40b5e3d608d16a4268b2f1b29)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

<a id="r_ga34995e902b63c4d7d37ebd709d88a72a"></a>

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[lwm2m_firmware_get_update_cb_inst](#ga34995e902b63c4d7d37ebd709d88a72a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

<a id="r_gac374d0559056ddb9cf43deae932fd128"></a>

```c
int lwm2m_swmgmt_set_activate_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_activate_cb](#gac374d0559056ddb9cf43deae932fd128)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件激活请求（Software Activation Requests）的回调。

<a id="r_ga7a2b93b918257bece819dc44804f27f5"></a>

```c
int lwm2m_swmgmt_set_deactivate_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_deactivate_cb](#ga7a2b93b918257bece819dc44804f27f5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件停用请求（Software Deactivation Requests）的回调。

<a id="r_gadfc00060c0b538ed576b5e3edd7dac80"></a>

```c
int lwm2m_swmgmt_set_install_package_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_install_package_cb](#gadfc00060c0b538ed576b5e3edd7dac80)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件安装请求（Software Install Requests）的回调。

<a id="r_gacf209563efdc5f3201152088c52d05c3"></a>

```c
int lwm2m_swmgmt_set_delete_package_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_delete_package_cb](#gacf209563efdc5f3201152088c52d05c3)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件卸载请求（Software Uninstall Requests）的回调。

<a id="r_gab59370ce4fdc94adb4903f22ab1f95b2"></a>

```c
int lwm2m_swmgmt_set_read_package_version_cb (uint16_t obj_inst_id, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_read_package_version_cb](#gab59370ce4fdc94adb4903f22ab1f95b2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_get_data_cb_t](#ga5e531aade0537eb5e3f5756e9287e384)。

设置读取软件包（Software Package）的回调。

<a id="r_ga293904118f972ae387c8aa85a1028b54"></a>

```c
int lwm2m_swmgmt_set_write_package_cb (uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_write_package_cb](#ga293904118f972ae387c8aa85a1028b54)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)。

设置软件管理分块传输（Software Management Block Transfer）的数据回调。

<a id="r_ga573e128348fb2f43a33bd09332dd677f"></a>

```c
int lwm2m_swmgmt_install_completed (uint16_t obj_inst_id, int error_code)
```

相关声明：[lwm2m_swmgmt_install_completed](#ga573e128348fb2f43a33bd09332dd677f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

软件管理对象实例（Software Management Object Instance）完成安装操作（Install Operation）时调用的函数。

<a id="r_ga950557bce8c510bcc8b0704e7bc4a9dc"></a>

```c
void lwm2m_event_log_set_read_log_data_cb (lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_event_log_set_read_log_data_cb](#ga950557bce8c510bcc8b0704e7bc4a9dc)、[lwm2m_engine_get_data_cb_t](#ga5e531aade0537eb5e3f5756e9287e384)。

设置读取日志数据（Log Data）的回调。

<a id="r_gadd163806d70713d8349a9db484ba88bf"></a>

```c
int lwm2m_update_observer_min_period (struct lwm2m_ctx *client_ctx, const struct lwm2m_obj_path *path, uint32_t period_s)
```

相关声明：[lwm2m_update_observer_min_period](#gadd163806d70713d8349a9db484ba88bf)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更改观察者（Observer）的 `pmin` 值。

<a id="r_ga6acccbcd879901574aceab53a21800fc"></a>

```c
int lwm2m_update_observer_max_period (struct lwm2m_ctx *client_ctx, const struct lwm2m_obj_path *path, uint32_t period_s)
```

相关声明：[lwm2m_update_observer_max_period](#ga6acccbcd879901574aceab53a21800fc)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更改观察者（Observer）的 `pmax` 值。

<a id="r_ga53f5b4c5967e93c7dd224fce8f416265"></a>

```c
int lwm2m_create_object_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_create_object_inst](#ga53f5b4c5967e93c7dd224fce8f416265)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

创建 LwM2M 对象实例（Object Instance）。

<a id="r_gaf921d4bc96090ef8735d90d173feab94"></a>

```c
int lwm2m_delete_object_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_delete_object_inst](#gaf921d4bc96090ef8735d90d173feab94)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

删除 LwM2M 对象实例（Object Instance）。

<a id="r_ga9a0cdcc9fc6d37462eddeb54e5d1f87a"></a>

```c
void lwm2m_registry_lock (void)
```

相关声明：[lwm2m_registry_lock](#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)。

为当前线程锁定注册表（Registry）。

<a id="r_gab09b62982c34887cdd16c30659d3349a"></a>

```c
void lwm2m_registry_unlock (void)
```

相关声明：[lwm2m_registry_unlock](#gab09b62982c34887cdd16c30659d3349a)。

解锁之前通过 `lwm2m_registry_lock()` 锁定的注册表（Registry）。

<a id="r_gaaef33bdf3f48fd91abdb50db4d5460f9"></a>

```c
int lwm2m_set_opaque (const struct lwm2m_obj_path *path, const char *data_ptr, uint16_t data_len)
```

相关声明：[lwm2m_set_opaque](#gaaef33bdf3f48fd91abdb50db4d5460f9)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

<a id="r_ga7217f33bf705011d91ba66c86a4d5747"></a>

```c
int lwm2m_set_string (const struct lwm2m_obj_path *path, const char *data_ptr)
```

相关声明：[lwm2m_set_string](#ga7217f33bf705011d91ba66c86a4d5747)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为字符串（String）。

<a id="r_ga1aa3ff424b7190d0fbd9366626b2685c"></a>

```c
int lwm2m_set_u8 (const struct lwm2m_obj_path *path, uint8_t value)
```

相关声明：[lwm2m_set_u8](#ga1aa3ff424b7190d0fbd9366626b2685c)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置资源（实例）值（Resource/Instance Value），类型为 `u8`。

<a id="r_ga1f06bb65571efee18db5d061f95399c3"></a>

```c
int lwm2m_set_u16 (const struct lwm2m_obj_path *path, uint16_t value)
```

相关声明：[lwm2m_set_u16](#ga1f06bb65571efee18db5d061f95399c3)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置资源（实例）值（Resource/Instance Value），类型为 `u16`。

<a id="r_ga9481e570b121404dc1be1ce23d904894"></a>

```c
int lwm2m_set_u32 (const struct lwm2m_obj_path *path, uint32_t value)
```

相关声明：[lwm2m_set_u32](#ga9481e570b121404dc1be1ce23d904894)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置资源（实例）值（Resource/Instance Value），类型为 `u32`。

<a id="r_ga37261a4b9e54eab3d1d855a084d082aa"></a>

```c
int lwm2m_set_s8 (const struct lwm2m_obj_path *path, int8_t value)
```

相关声明：[lwm2m_set_s8](#ga37261a4b9e54eab3d1d855a084d082aa)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置资源（实例）值（Resource/Instance Value），类型为 `s8`。

<a id="r_gad548ffedcb8328b23eb32476a97be6ee"></a>

```c
int lwm2m_set_s16 (const struct lwm2m_obj_path *path, int16_t value)
```

相关声明：[lwm2m_set_s16](#gad548ffedcb8328b23eb32476a97be6ee)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置资源（实例）值（Resource/Instance Value），类型为 `s16`。

<a id="r_ga327e086959fc5649a5ef14f1f2943e88"></a>

```c
int lwm2m_set_s32 (const struct lwm2m_obj_path *path, int32_t value)
```

相关声明：[lwm2m_set_s32](#ga327e086959fc5649a5ef14f1f2943e88)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置资源（实例）值（Resource/Instance Value），类型为 `s32`。

<a id="r_ga18fcee379640c0dda32d6e3d14827260"></a>

```c
int lwm2m_set_s64 (const struct lwm2m_obj_path *path, int64_t value)
```

相关声明：[lwm2m_set_s64](#ga18fcee379640c0dda32d6e3d14827260)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

设置资源（实例）值（Resource/Instance Value），类型为 `s64`。

<a id="r_ga9ef21d06bef8a97b7666c0aa7fa753b4"></a>

```c
int lwm2m_set_bool (const struct lwm2m_obj_path *path, bool value)
```

相关声明：[lwm2m_set_bool](#ga9ef21d06bef8a97b7666c0aa7fa753b4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

<a id="r_ga3386d3f2ad8d9713fc2283ed6921c2fc"></a>

```c
int lwm2m_set_f64 (const struct lwm2m_obj_path *path, const double value)
```

相关声明：[lwm2m_set_f64](#ga3386d3f2ad8d9713fc2283ed6921c2fc)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

<a id="r_ga04a18bd8a4eeea41a47803c16567d67b"></a>

```c
int lwm2m_set_objlnk (const struct lwm2m_obj_path *path, const struct lwm2m_objlnk *value)
```

相关声明：[lwm2m_set_objlnk](#ga04a18bd8a4eeea41a47803c16567d67b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

<a id="r_ga7194ad24842e35130d8af7f5104c0844"></a>

```c
int lwm2m_set_time (const struct lwm2m_obj_path *path, time_t value)
```

相关声明：[lwm2m_set_time](#ga7194ad24842e35130d8af7f5104c0844)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

设置资源（实例）值（Resource/Instance Value），类型为时间（Time）。

<a id="r_ga41b673986e11748b2ded8e1f8f05e0a7"></a>

```c
int lwm2m_set_bulk (const struct lwm2m_res_item res_list[], size_t res_list_size)
```

相关声明：[lwm2m_set_bulk](#ga41b673986e11748b2ded8e1f8f05e0a7)、[lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)。

设置多个资源（实例）值（Resource/Instance Values）。

<a id="r_gae245a9a1d9456af7e6283b1074944606"></a>

```c
int lwm2m_get_opaque (const struct lwm2m_obj_path *path, void *buf, uint16_t buflen)
```

相关声明：[lwm2m_get_opaque](#gae245a9a1d9456af7e6283b1074944606)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

<a id="r_ga20fc58b25468bf309175db59d67b820b"></a>

```c
int lwm2m_get_string (const struct lwm2m_obj_path *path, void *str, uint16_t buflen)
```

相关声明：[lwm2m_get_string](#ga20fc58b25468bf309175db59d67b820b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为字符串（String）。

<a id="r_gac56e804962e529799c771d81ac1fd027"></a>

```c
int lwm2m_get_u8 (const struct lwm2m_obj_path *path, uint8_t *value)
```

相关声明：[lwm2m_get_u8](#gac56e804962e529799c771d81ac1fd027)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取资源（实例）值（Resource/Instance Value），类型为 `u8`。

<a id="r_ga1b96848f96bdab9939bb2619d3e1059b"></a>

```c
int lwm2m_get_u16 (const struct lwm2m_obj_path *path, uint16_t *value)
```

相关声明：[lwm2m_get_u16](#ga1b96848f96bdab9939bb2619d3e1059b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为 `u16`。

<a id="r_ga0bc84cb39a7a537925ec7d62e54b8b48"></a>

```c
int lwm2m_get_u32 (const struct lwm2m_obj_path *path, uint32_t *value)
```

相关声明：[lwm2m_get_u32](#ga0bc84cb39a7a537925ec7d62e54b8b48)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取资源（实例）值（Resource/Instance Value），类型为 `u32`。

<a id="r_ga12817bfbf0a0cbb742568ee974a1c337"></a>

```c
int lwm2m_get_s8 (const struct lwm2m_obj_path *path, int8_t *value)
```

相关声明：[lwm2m_get_s8](#ga12817bfbf0a0cbb742568ee974a1c337)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

获取资源（实例）值（Resource/Instance Value），类型为 `s8`。

<a id="r_ga2426db6720b3f3e15e63022cabae5ece"></a>

```c
int lwm2m_get_s16 (const struct lwm2m_obj_path *path, int16_t *value)
```

相关声明：[lwm2m_get_s16](#ga2426db6720b3f3e15e63022cabae5ece)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取资源（实例）值（Resource/Instance Value），类型为 `s16`。

<a id="r_ga99d7189efa25881dbcddd99e2a795f1b"></a>

```c
int lwm2m_get_s32 (const struct lwm2m_obj_path *path, int32_t *value)
```

相关声明：[lwm2m_get_s32](#ga99d7189efa25881dbcddd99e2a795f1b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取资源（实例）值（Resource/Instance Value），类型为 `s32`。

<a id="r_gaaffe06ca9ee5302fb6e26164f250653e"></a>

```c
int lwm2m_get_s64 (const struct lwm2m_obj_path *path, int64_t *value)
```

相关声明：[lwm2m_get_s64](#gaaffe06ca9ee5302fb6e26164f250653e)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

获取资源（实例）值（Resource/Instance Value），类型为 `s64`。

<a id="r_gafdc72844ce0ca417e297d76288155aa4"></a>

```c
int lwm2m_get_bool (const struct lwm2m_obj_path *path, bool *value)
```

相关声明：[lwm2m_get_bool](#gafdc72844ce0ca417e297d76288155aa4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

<a id="r_ga03b72e96a67fcbf85feb5bf0b9df81ce"></a>

```c
int lwm2m_get_f64 (const struct lwm2m_obj_path *path, double *value)
```

相关声明：[lwm2m_get_f64](#ga03b72e96a67fcbf85feb5bf0b9df81ce)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

获取资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

<a id="r_ga4de941c36cf678e12da6e05c378a92e5"></a>

```c
int lwm2m_get_objlnk (const struct lwm2m_obj_path *path, struct lwm2m_objlnk *buf)
```

相关声明：[lwm2m_get_objlnk](#ga4de941c36cf678e12da6e05c378a92e5)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

获取资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

<a id="r_ga2e1d41866b5ea35c5aa29bca9bb43812"></a>

```c
int lwm2m_get_time (const struct lwm2m_obj_path *path, time_t *buf)
```

相关声明：[lwm2m_get_time](#ga2e1d41866b5ea35c5aa29bca9bb43812)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

获取资源（实例）值（Resource/Instance Value），类型为时间（Time）。

<a id="r_gaf33bd6a527b6d399f3d92b666ac77dfb"></a>

```c
int lwm2m_register_read_callback (const struct lwm2m_obj_path *path, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_register_read_callback](#gaf33bd6a527b6d399f3d92b666ac77dfb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_get_data_cb_t](#ga5e531aade0537eb5e3f5756e9287e384)。

设置资源（实例）读取回调（Read Callback）。

<a id="r_ga6f775837e07ba9b0032be8917a593e16"></a>

```c
int lwm2m_register_pre_write_callback (const struct lwm2m_obj_path *path, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_register_pre_write_callback](#ga6f775837e07ba9b0032be8917a593e16)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_get_data_cb_t](#ga5e531aade0537eb5e3f5756e9287e384)。

设置资源（实例）写入前回调（Pre-write Callback）。

<a id="r_gad6e5fd4815f409ad59ad631b03199333"></a>

```c
int lwm2m_register_validate_callback (const struct lwm2m_obj_path *path, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_register_validate_callback](#gad6e5fd4815f409ad59ad631b03199333)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)。

设置资源（实例）校验回调（Validation Callback）。

<a id="r_ga3dd8b38e797173dae902404fb5b7a3f4"></a>

```c
int lwm2m_register_post_write_callback (const struct lwm2m_obj_path *path, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_register_post_write_callback](#ga3dd8b38e797173dae902404fb5b7a3f4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_set_data_cb_t](#ga3afac013b0cf731f9c86dc3791131585)。

设置资源（实例）写入后回调（Post-write Callback）。

<a id="r_ga29cc5cdd697e94d7379b1fb178487916"></a>

```c
int lwm2m_register_exec_callback (const struct lwm2m_obj_path *path, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_register_exec_callback](#ga29cc5cdd697e94d7379b1fb178487916)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_execute_cb_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置资源执行事件回调（Resource Execute Event Callback）。

<a id="r_ga346d547e02bd53ee83f83b2248449e98"></a>

```c
int lwm2m_register_create_callback (uint16_t obj_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_register_create_callback](#ga346d547e02bd53ee83f83b2248449e98)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置对象实例创建事件回调（Object Instance Create Event Callback）。

<a id="r_ga92d7e6d81ef674a6c311e1717c6bf373"></a>

```c
int lwm2m_register_delete_callback (uint16_t obj_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_register_delete_callback](#ga92d7e6d81ef674a6c311e1717c6bf373)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置对象实例删除事件回调（Object Instance Delete Event Callback）。

<a id="r_ga56a2aecd38baedb5dc17258610c4780d"></a>

```c
int lwm2m_set_res_buf (const struct lwm2m_obj_path *path, void *buffer_ptr, uint16_t buffer_len, uint16_t data_len, uint8_t data_flags)
```

相关声明：[lwm2m_set_res_buf](#ga56a2aecd38baedb5dc17258610c4780d)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为资源（Resource）设置数据缓冲区（Data Buffer）。

<a id="r_ga0f2b115d231bea6622135d72b51f55ca"></a>

```c
int lwm2m_set_res_data_len (const struct lwm2m_obj_path *path, uint16_t data_len)
```

相关声明：[lwm2m_set_res_data_len](#ga0f2b115d231bea6622135d72b51f55ca)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新资源（Resource）的数据大小（Data Size）。

<a id="r_gac0b6669d8a19b03eb8b08cbbcdb0c192"></a>

```c
int lwm2m_get_res_buf (const struct lwm2m_obj_path *path, void **buffer_ptr, uint16_t *buffer_len, uint16_t *data_len, uint8_t *data_flags)
```

相关声明：[lwm2m_get_res_buf](#gac0b6669d8a19b03eb8b08cbbcdb0c192)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取资源（Resource）的数据缓冲区（Data Buffer）。

<a id="r_gac69c40474180fe14c3761185b2db1c0c"></a>

```c
int lwm2m_create_res_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_create_res_inst](#gac69c40474180fe14c3761185b2db1c0c)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

创建资源实例（Resource Instance）。

<a id="r_gacfeb63db0423e6730ffaa826a87eb262"></a>

```c
int lwm2m_delete_res_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_delete_res_inst](#gacfeb63db0423e6730ffaa826a87eb262)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

删除资源实例（Resource Instance）。

<a id="r_gab45cebf6f0b6b70974367ca453d16aeb"></a>

```c
int lwm2m_update_device_service_period (uint32_t period_ms)
```

相关声明：[lwm2m_update_device_service_period](#gab45cebf6f0b6b70974367ca453d16aeb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新设备服务（Device Service）的周期（Period）。

<a id="r_ga1065c729d5caa8ca13de7766fce77953"></a>

```c
bool lwm2m_path_is_observed (const struct lwm2m_obj_path *path)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lwm2m_path_is_observed](#ga1065c729d5caa8ca13de7766fce77953)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

检查路径（Path）是否正在被观察（Observed）。

<a id="r_ga077e1abd612d31dd33fab52b7d205c39"></a>

```c
int lwm2m_engine_stop (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_engine_stop](#ga077e1abd612d31dd33fab52b7d205c39)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

停止 LwM2M 引擎（Engine）。

<a id="r_ga9f72fbd0163b15c48ea09cf7d511e444"></a>

```c
int lwm2m_engine_start (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_engine_start](#ga9f72fbd0163b15c48ea09cf7d511e444)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

启动 LwM2M 引擎（Engine）。

<a id="r_ga919c7d6f418cda99c77fdaf54ae1a7b0"></a>

```c
void lwm2m_acknowledge (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_acknowledge](#ga919c7d6f418cda99c77fdaf54ae1a7b0)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

使用空确认（Empty ACK）确认当前处理的请求（Request）。

<a id="r_ga9dfd46b8a535b1f28e644dc18f57fd79"></a>

```c
int lwm2m_rd_client_start (struct lwm2m_ctx *client_ctx, const char *ep_name, uint32_t flags, lwm2m_ctx_event_cb_t event_cb, lwm2m_observe_cb_t observe_cb)
```

相关声明：[lwm2m_rd_client_start](#ga9dfd46b8a535b1f28e644dc18f57fd79)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[lwm2m_ctx_event_cb_t](#ga38dbaf038426efc75d889c4a0666dac9)、[lwm2m_observe_cb_t](#gad7bea67e16e1e831e0f949dbf83d5afe)。

启动 LwM2M 注册／发现客户端（Registration/Discovery Client，RD Client）。

<a id="r_gafd87e5d975c4d88973ac3e95e4d156ac"></a>

```c
int lwm2m_rd_client_stop (struct lwm2m_ctx *client_ctx, lwm2m_ctx_event_cb_t event_cb, bool deregister)
```

相关声明：[lwm2m_rd_client_stop](#gafd87e5d975c4d88973ac3e95e4d156ac)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_ctx_event_cb_t](#ga38dbaf038426efc75d889c4a0666dac9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

停止 LwM2M RD 客户端，执行注销（De-register）。

<a id="r_ga1a4dadb822a8241c5bdf339c21cc57a4"></a>

```c
int lwm2m_engine_pause (void)
```

相关声明：[lwm2m_engine_pause](#ga1a4dadb822a8241c5bdf339c21cc57a4)。

挂起 LwM2M 引擎线程（Engine Thread）。

<a id="r_ga178fea0407a5e98c4f5d5ad69688853a"></a>

```c
int lwm2m_engine_resume (void)
```

相关声明：[lwm2m_engine_resume](#ga178fea0407a5e98c4f5d5ad69688853a)。

恢复 LwM2M 引擎线程（Engine Thread）。

<a id="r_gab4ec7a22d01259b6ba9d3a7b6681e6f0"></a>

```c
void lwm2m_rd_client_update (void)
```

相关声明：[lwm2m_rd_client_update](#gab4ec7a22d01259b6ba9d3a7b6681e6f0)。

触发 LwM2M RD 客户端的注册更新（Registration Update）。

<a id="r_ga971c0636c19fe7f0a6e918622560a750"></a>

```c
char * lwm2m_path_log_buf (char *buf, struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_path_log_buf](#ga971c0636c19fe7f0a6e918622560a750)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

将路径对象（Path Objects）的内容打印到日志（Log）的辅助函数。

<a id="r_ga026cc9288d2de17ec557e08b9b987ebc"></a>

```c
int lwm2m_send_cb (struct lwm2m_ctx *ctx, const struct lwm2m_obj_path path_list[], uint8_t path_list_size, lwm2m_send_cb_t reply_cb)
```

相关声明：[lwm2m_send_cb](#ga026cc9288d2de17ec557e08b9b987ebc)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lwm2m_send_cb_t](#gaf5394884da53edb28fe4afc92bf40e6a)。

<a id="r_ga896caab5473eadff860872023d13b6c0"></a>

```c
struct lwm2m_ctx * lwm2m_rd_client_ctx (void)
```

相关声明：[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_rd_client_ctx](#ga896caab5473eadff860872023d13b6c0)。

<a id="r_ga6975c5c4825afaccc52741eb54aca4cb"></a>

```c
int lwm2m_enable_cache (const struct lwm2m_obj_path *path, struct lwm2m_time_series_elem *data_cache, size_t cache_len)
```

相关声明：[lwm2m_enable_cache](#ga6975c5c4825afaccc52741eb54aca4cb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

<a id="r_gac4e7da0353914601c3ec101415c2e110"></a>

```c
int lwm2m_set_cache_filter (const struct lwm2m_obj_path *path, lwm2m_cache_filter_cb_t filter_cb)
```

相关声明：[lwm2m_set_cache_filter](#gac4e7da0353914601c3ec101415c2e110)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_cache_filter_cb_t](#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)。

为缓存的资源样本（Cached Resource Samples）注册过滤回调（Filtering Callback）。

<a id="r_ga00d29a0c4935fc255e74b8c22ac49de1"></a>

```c
int lwm2m_cache_free_slots_get (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_cache_free_slots_get](#ga00d29a0c4935fc255e74b8c22ac49de1)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

返回缓存资源（Cached Resource）中的空闲槽位数（Free Slots）。

<a id="r_ga6c05640737cfc4da71841a77de128be0"></a>

```c
int lwm2m_security_mode (struct lwm2m_ctx *ctx)
```

相关声明：[lwm2m_security_mode](#ga6c05640737cfc4da71841a77de128be0)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

从选定的安全对象实例（Security Object Instance）读取安全模式（Security Mode）。

<a id="r_ga956c4fc742a588b7b8b95ce8481f09bf"></a>

```c
int lwm2m_set_default_sockopt (struct lwm2m_ctx *ctx)
```

相关声明：[lwm2m_set_default_sockopt](#ga956c4fc742a588b7b8b95ce8481f09bf)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

设置数据报传输层安全（DTLS）连接的默认套接字选项（Socket Options）。

<a id="r_ga647018abc15cd65c894d9acb6c866486"></a>

```c
void lwm2m_pull_context_set_sockopt_callback (lwm2m_set_sockopt_cb_t set_sockopt_cb)
```

相关声明：[lwm2m_pull_context_set_sockopt_callback](#ga647018abc15cd65c894d9acb6c866486)、[lwm2m_set_sockopt_cb_t](#ga92d2227f37e7d382bc4f1a7bae21b872)。

为拉取上下文（Pull Context）的客户端设置 `lwm2m_ctx::set_socketoptions` 回调。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.7\_由 OMA 为 LwM2M 技术规范管理的 LwM2M 对象（LwM2M Objects managed by OMA for LwM2M tech specification.）

此范围内的对象（Objects）标识符（IDs）为 `0–1023`。

<a id="r_ga785e4a647a2cf93194a249537223ab0f"></a>

```c
#define LWM2M_OBJECT_SECURITY_ID 0
```

相关声明：[LWM2M_OBJECT_SECURITY_ID](#ga785e4a647a2cf93194a249537223ab0f)。

安全对象（Security Object）。

<a id="r_gace7b2f0a1f97b6e99c0958a8382ca0d2"></a>

```c
#define LWM2M_OBJECT_SERVER_ID 1
```

相关声明：[LWM2M_OBJECT_SERVER_ID](#gace7b2f0a1f97b6e99c0958a8382ca0d2)。

服务器对象（Server Object）。

<a id="r_gaa8387c8838f952c7c60602e2952c7f55"></a>

```c
#define LWM2M_OBJECT_ACCESS_CONTROL_ID 2
```

相关声明：[LWM2M_OBJECT_ACCESS_CONTROL_ID](#gaa8387c8838f952c7c60602e2952c7f55)。

访问控制对象（Access Control Object）。

<a id="r_ga699f585b320ab5b259d4fb2bda10eb78"></a>

```c
#define LWM2M_OBJECT_DEVICE_ID 3
```

相关声明：[LWM2M_OBJECT_DEVICE_ID](#ga699f585b320ab5b259d4fb2bda10eb78)。

设备对象。

<a id="r_ga73db8616cc7dbbd04267d97a743b8ec0"></a>

```c
#define LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID 4
```

相关声明：[LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID](#ga73db8616cc7dbbd04267d97a743b8ec0)。

连接监测对象（Connectivity Monitoring Object）。

<a id="r_ga442cc51c7d0807a752ce4affe9221c5b"></a>

```c
#define LWM2M_OBJECT_FIRMWARE_ID 5
```

相关声明：[LWM2M_OBJECT_FIRMWARE_ID](#ga442cc51c7d0807a752ce4affe9221c5b)。

固件对象（Firmware Object）。

<a id="r_ga1046ec68deab3d812d7e5921fb718028"></a>

```c
#define LWM2M_OBJECT_LOCATION_ID 6
```

相关声明：[LWM2M_OBJECT_LOCATION_ID](#ga1046ec68deab3d812d7e5921fb718028)。

位置对象（Location Object）。

<a id="r_gaa6c374c401dd36b6e121ac48c91ca9cf"></a>

```c
#define LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID 7
```

相关声明：[LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID](#gaa6c374c401dd36b6e121ac48c91ca9cf)。

连接统计对象（Connectivity Statistics Object）。

<a id="r_gac2d140b4a36d6010fe93bca443a658c0"></a>

```c
#define LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID 9
```

相关声明：[LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID](#gac2d140b4a36d6010fe93bca443a658c0)。

软件管理对象（Software Management Object）。

<a id="r_ga4b4ce912a4554923974461ea3c76007e"></a>

```c
#define LWM2M_OBJECT_PORTFOLIO_ID 16
```

相关声明：[LWM2M_OBJECT_PORTFOLIO_ID](#ga4b4ce912a4554923974461ea3c76007e)。

信息组合对象（Portfolio Object）。

<a id="r_ga85eabde1900ef052064d34cf5e3a4afe"></a>

```c
#define LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID 19
```

相关声明：[LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID](#ga85eabde1900ef052064d34cf5e3a4afe)。

二进制应用数据容器对象（Binary App Data Container Object）。

<a id="r_ga4f0455fb0271c2fcbb7dadb944431ff0"></a>

```c
#define LWM2M_OBJECT_EVENT_LOG_ID 20
```

相关声明：[LWM2M_OBJECT_EVENT_LOG_ID](#ga4f0455fb0271c2fcbb7dadb944431ff0)。

事件日志对象（Event Log Object）。

<a id="r_gab13a1600a662ed1dbd8845c6d7d4549a"></a>

```c
#define LWM2M_OBJECT_OSCORE_ID 21
```

相关声明：[LWM2M_OBJECT_OSCORE_ID](#gab13a1600a662ed1dbd8845c6d7d4549a)。

受限 RESTful 环境对象安全（OSCORE）对象。

<a id="r_ga3505e9ddcd54afe86e8bd5fbc03fb565"></a>

```c
#define LWM2M_OBJECT_GATEWAY_ID 25
```

相关声明：[LWM2M_OBJECT_GATEWAY_ID](#ga3505e9ddcd54afe86e8bd5fbc03fb565)。

网关对象（Gateway Object）。

## 5.8\_由第三方标准制定方提供的 LwM2M 对象（LwM2M Objects produced by 3rd party Standards Development）

组织（Organizations）。

参见 [OMA 轻量级机器到机器通信（LwM2M）对象与资源注册表（Object and Resource Registry）原链接](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html)。译注：核验时，旧链接已重定向至 OMA 规范总入口；当前官方注册表位于 [LwM2M Objects](https://www.openmobilealliance.org/specifications/registries/objects/)，其中保留对象标识符分类及注册表入口。

<a id="r_gaeef485c23d306c93fc0f45dd58766ad9"></a>

```c
#define IPSO_OBJECT_GENERIC_SENSOR_ID 3300
```

相关声明：[IPSO_OBJECT_GENERIC_SENSOR_ID](#gaeef485c23d306c93fc0f45dd58766ad9)。

IPSO 通用传感器对象（Generic Sensor Object）。

<a id="r_ga3b0c046d93c7bcee9d4da121dd574ff0"></a>

```c
#define IPSO_OBJECT_TEMP_SENSOR_ID 3303
```

相关声明：[IPSO_OBJECT_TEMP_SENSOR_ID](#ga3b0c046d93c7bcee9d4da121dd574ff0)。

IPSO 温度传感器对象（Temperature Sensor Object）。

<a id="r_ga8075d8b7eb3b4c98f621efef673bb11f"></a>

```c
#define IPSO_OBJECT_HUMIDITY_SENSOR_ID 3304
```

相关声明：[IPSO_OBJECT_HUMIDITY_SENSOR_ID](#ga8075d8b7eb3b4c98f621efef673bb11f)。

IPSO 湿度传感器对象（Humidity Sensor Object）。

<a id="r_ga56ebac5260ee467b3763abe49ff3b8ff"></a>

```c
#define IPSO_OBJECT_LIGHT_CONTROL_ID 3311
```

相关声明：[IPSO_OBJECT_LIGHT_CONTROL_ID](#ga56ebac5260ee467b3763abe49ff3b8ff)。

IPSO 灯光控制对象（Light Control Object）。

<a id="r_ga0b3b9db806e5fe47cc08de34b5fb35fe"></a>

```c
#define IPSO_OBJECT_ACCELEROMETER_ID 3313
```

相关声明：[IPSO_OBJECT_ACCELEROMETER_ID](#ga0b3b9db806e5fe47cc08de34b5fb35fe)。

IPSO 加速度计对象（Accelerometer Object）。

<a id="r_ga6abcf3c5cf5001a4fdb7915336325ce1"></a>

```c
#define IPSO_OBJECT_MAGNETOMETER_ID 3314
```

相关声明：[IPSO_OBJECT_MAGNETOMETER_ID](#ga6abcf3c5cf5001a4fdb7915336325ce1)。

IPSO 磁力计对象（Magnetometer Object）。

<a id="r_ga270a1b5a576d72099287633b32ce909f"></a>

```c
#define IPSO_OBJECT_VOLTAGE_SENSOR_ID 3316
```

相关声明：[IPSO_OBJECT_VOLTAGE_SENSOR_ID](#ga270a1b5a576d72099287633b32ce909f)。

IPSO 电压传感器对象（Voltage Sensor Object）。

<a id="r_gae511fd54112829e63c691776750893c2"></a>

```c
#define IPSO_OBJECT_CURRENT_SENSOR_ID 3317
```

相关声明：[IPSO_OBJECT_CURRENT_SENSOR_ID](#gae511fd54112829e63c691776750893c2)。

IPSO 电流传感器对象（Current Sensor Object）。

<a id="r_ga752f81e91d0965a50ecfb0679bdea6ba"></a>

```c
#define IPSO_OBJECT_PRESSURE_ID 3323
```

相关声明：[IPSO_OBJECT_PRESSURE_ID](#ga752f81e91d0965a50ecfb0679bdea6ba)。

IPSO 压力传感器对象（Pressure Sensor Object）。

<a id="r_ga46075c78a3cd73f3313abf5ffeca697b"></a>

```c
#define IPSO_OBJECT_TIME_ID 3333
```

相关声明：[IPSO_OBJECT_TIME_ID](#ga46075c78a3cd73f3313abf5ffeca697b)。

IPSO 时间对象（Time Object）。

<a id="r_ga15d664ddbfbf4d5b25dde34a5c650e6b"></a>

```c
#define IPSO_OBJECT_BUZZER_ID 3338
```

相关声明：[IPSO_OBJECT_BUZZER_ID](#ga15d664ddbfbf4d5b25dde34a5c650e6b)。

IPSO 蜂鸣器对象（Buzzer Object）。

<a id="r_ga6c7bd5880fa22050748c2cb01981cbcb"></a>

```c
#define IPSO_OBJECT_TIMER_ID 3340
```

相关声明：[IPSO_OBJECT_TIMER_ID](#ga6c7bd5880fa22050748c2cb01981cbcb)。

IPSO 定时器对象（Timer Object）。

<a id="r_ga776a6a5e1eab3a8de0a39382f94b663a"></a>

```c
#define IPSO_OBJECT_ONOFF_SWITCH_ID 3342
```

相关声明：[IPSO_OBJECT_ONOFF_SWITCH_ID](#ga776a6a5e1eab3a8de0a39382f94b663a)。

IPSO 通断开关对象（On/Off Switch Object）。

<a id="r_ga6e3119bc8f0b9143ab384e82a5bccf7c"></a>

```c
#define IPSO_OBJECT_PUSH_BUTTON_ID 3347
```

相关声明：[IPSO_OBJECT_PUSH_BUTTON_ID](#ga6e3119bc8f0b9143ab384e82a5bccf7c)。

IPSO 按钮对象（Push Button Object）。

<a id="r_gacdd09a26ce52f36c644a89a8b89f7d32"></a>

```c
#define UCIFI_OBJECT_BATTERY_ID 3411
```

相关声明：[UCIFI_OBJECT_BATTERY_ID](#gacdd09a26ce52f36c644a89a8b89f7d32)。

uCIFI 电池对象（Battery Object）。

<a id="r_ga21f6bc6255f5f5ed28881fa797d026ca"></a>

```c
#define IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID 3435
```

相关声明：[IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID](#ga21f6bc6255f5f5ed28881fa797d026ca)。

IPSO 填充液位传感器对象（Filling Level Sensor Object）。

## 5.9\_用于“可用电源”资源的电源类型（Power source types used for the "Available Power Sources" resource of）

LwM2M 设备对象（Device Object）的 `3/0/6`。

<a id="r_gae154ca2e54ec7759dd43f2a7a275077e"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER 0
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER](#gae154ca2e54ec7759dd43f2a7a275077e)。

直流电源（DC Power）。

<a id="r_ga04ca8ac536eed7d411c1b1ea2b2a59ac"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT 1
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT](#ga04ca8ac536eed7d411c1b1ea2b2a59ac)。

内部电池（Internal Battery）。

<a id="r_gaf12052f903a688712928d036b782f621"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT 2
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT](#gaf12052f903a688712928d036b782f621)。

外部电池（External Battery）。

<a id="r_ga10c4633c97881ca7d87c748aaeec68c9"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL 3
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL](#ga10c4633c97881ca7d87c748aaeec68c9)。

燃料电池（Fuel Cell）。

<a id="r_ga72352523996e61ea93caff0bb80c42ba"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH 4
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH](#ga72352523996e61ea93caff0bb80c42ba)。

以太网供电（Power over Ethernet）。

<a id="r_ga4877877be75d3dd3c8f600b438b7ea8e"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_USB 5
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_USB](#ga4877877be75d3dd3c8f600b438b7ea8e)。

通用串行总线（USB）

<a id="r_ga97b9d38ec402478f10642f1f83a4f88a"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER 6
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER](#ga97b9d38ec402478f10642f1f83a4f88a)。

交流市电（AC Mains Power）。

<a id="r_gaa41ec1d2ca43e1385cfb11204aff729d"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR 7
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR](#gaa41ec1d2ca43e1385cfb11204aff729d)。

太阳能（Solar）。

<a id="r_gae7a580aac1804abbcf3feb57a5a30a02"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_MAX 8
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_MAX](#gae7a580aac1804abbcf3feb57a5a30a02)。

可用电源类型（Available Power Source Type）的最大值。

## 5.10\_用于 LwM2M 设备“错误码”资源的错误码（Error codes used for the "Error Code" resource of the LwM2M Device）

对象（Object）

LwM2M 客户端可以通过 `lwm2m_device_add_err()` 函数注册以下错误码（Error Codes）之一。

<a id="r_gad54ec75eb2843d5eed199ddedca6ef4f"></a>

```c
#define LWM2M_DEVICE_ERROR_NONE 0
```

相关声明：[LWM2M_DEVICE_ERROR_NONE](#gad54ec75eb2843d5eed199ddedca6ef4f)。

无错误（No Error）。

<a id="r_ga53a9ee1ae09dd32a8dc2df6018798f9f"></a>

```c
#define LWM2M_DEVICE_ERROR_LOW_POWER 1
```

相关声明：[LWM2M_DEVICE_ERROR_LOW_POWER](#ga53a9ee1ae09dd32a8dc2df6018798f9f)。

电池电量低（Low Battery Power）。

<a id="r_ga33152ea4ef497b02a12d1218d470a5a6"></a>

```c
#define LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF 2
```

相关声明：[LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF](#ga33152ea4ef497b02a12d1218d470a5a6)。

外部电源关闭（External Power Supply Off）。

<a id="r_ga3c1b7693167ff517c5cbd7bbdbfd1ea0"></a>

```c
#define LWM2M_DEVICE_ERROR_GPS_FAILURE 3
```

相关声明：[LWM2M_DEVICE_ERROR_GPS_FAILURE](#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)。

全球定位系统（GPS）模块故障。

<a id="r_ga78048382d8bc85bbabbff58f0a9860f2"></a>

```c
#define LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH 4
```

相关声明：[LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH](#ga78048382d8bc85bbabbff58f0a9860f2)。

接收信号强度低（Low Received Signal Strength）。

<a id="r_ga94ce0177c066dd43ef660b85afc83485"></a>

```c
#define LWM2M_DEVICE_ERROR_OUT_OF_MEMORY 5
```

相关声明：[LWM2M_DEVICE_ERROR_OUT_OF_MEMORY](#ga94ce0177c066dd43ef660b85afc83485)。

内存不足。

<a id="r_gabcb39cd3757ea60859984f6ad0df9e31"></a>

```c
#define LWM2M_DEVICE_ERROR_SMS_FAILURE 6
```

相关声明：[LWM2M_DEVICE_ERROR_SMS_FAILURE](#gabcb39cd3757ea60859984f6ad0df9e31)。

短信（SMS）故障。

<a id="r_ga2110d71a0c58087ff877e66b7500ba66"></a>

```c
#define LWM2M_DEVICE_ERROR_NETWORK_FAILURE 7
```

相关声明：[LWM2M_DEVICE_ERROR_NETWORK_FAILURE](#ga2110d71a0c58087ff877e66b7500ba66)。

IP 连接故障（IP Connectivity Failure）。

<a id="r_ga77e6352eace8116576c880bf7e416ba3"></a>

```c
#define LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE 8
```

相关声明：[LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE](#ga77e6352eace8116576c880bf7e416ba3)。

外设故障（Peripheral Malfunction）。

## 5.11\_用于“电池状态”资源（3/0/20）的电池状态码（Battery status codes used for the "Battery Status" resource (3/0/20)）

属于 LwM2M 设备对象（Device Object）。

电池状态（Battery Status）变化时，LwM2M 客户端可以通过 `lwm2m_set_u8("3/0/20", [battery status])` 设置以下编码之一。

<a id="r_ga4329c971f95f1c345381d1c864a9f334"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NORMAL 0
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_NORMAL](#ga4329c971f95f1c345381d1c864a9f334)。

电池工作正常，且未接入外部电源（Not on Power）。

<a id="r_gaf19da3a566782aeebebfb6ff110a9152"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGING 1
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_CHARGING](#gaf19da3a566782aeebebfb6ff110a9152)。

电池当前正在充电（Charging）。

<a id="r_ga5f7e88b52d8e6029467a2ed10585e6d4"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP 2
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP](#ga5f7e88b52d8e6029467a2ed10585e6d4)。

电池已充满（Fully Charged），充电器仍连接。

<a id="r_gaa3f81df5e4d45838922eb20a15ee3153"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_DAMAGED 3
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_DAMAGED](#gaa3f81df5e4d45838922eb20a15ee3153)。

电池存在问题（Battery Problem）。

<a id="r_ga578f6446ec1b70d2a32917abf1f5aad7"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_LOW 4
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_LOW](#ga578f6446ec1b70d2a32917abf1f5aad7)。

电池剩余电量低（Low on Charge）。

<a id="r_gacc3dfc99fc2cd9ef7048b1a0a0fd55c8"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NOT_INST 5
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_NOT_INST](#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)。

未安装电池（Battery Not Installed）。

<a id="r_ga174e118b07982b87c6c083236b79c3b7"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN 6
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN](#ga174e118b07982b87c6c083236b79c3b7)。

无法获取电池信息（Battery Information Not Available）。

## 5.12\_LwM2M 固件更新对象的状态（LwM2M Firmware Update object states）

LwM2M 客户端或 LwM2M 固件更新对象（Firmware Update Object）使用以下编码表示 LwM2M 固件更新状态（Firmware Update State），路径为 `5/0/3`。

<a id="r_gaafff27c7165f059a969fe60fee51f683"></a>

```c
#define STATE_IDLE 0
```

相关声明：[STATE_IDLE](#gaafff27c7165f059a969fe60fee51f683)。

空闲（Idle）。

<a id="r_gaeb34e88a0da4ac1274ae6b2cef010086"></a>

```c
#define STATE_DOWNLOADING 1
```

相关声明：[STATE_DOWNLOADING](#gaeb34e88a0da4ac1274ae6b2cef010086)。

正在下载（Downloading）。

<a id="r_ga009085120be71a28c1f6ebdaf7503365"></a>

```c
#define STATE_DOWNLOADED 2
```

相关声明：[STATE_DOWNLOADED](#ga009085120be71a28c1f6ebdaf7503365)。

已下载（Downloaded）。

<a id="r_gaac1dab8d1ac28bf13faeee39d1df47c5"></a>

```c
#define STATE_UPDATING 3
```

相关声明：[STATE_UPDATING](#gaac1dab8d1ac28bf13faeee39d1df47c5)。

正在更新（Updating）。

## 5.13\_LwM2M 固件更新对象的结果码（LwM2M Firmware Update object result codes）

处理固件更新后，客户端通过 `lwm2m_set_u8("5/0/5", [result code])`，使用以下结果码（Result Codes）之一设置结果。

<a id="r_ga391b47507468bbc1005903a56f80b1ea"></a>

```c
#define RESULT_DEFAULT 0
```

相关声明：[RESULT_DEFAULT](#ga391b47507468bbc1005903a56f80b1ea)。

初始值（Initial Value）。

<a id="r_ga7cc1753a05a0821f6c70dd2bccfbab5c"></a>

```c
#define RESULT_SUCCESS 1
```

相关声明：[RESULT_SUCCESS](#ga7cc1753a05a0821f6c70dd2bccfbab5c)。

固件更新成功（Firmware Updated Successfully）。

<a id="r_ga829f7bc83b67dcf16ea4775addd87343"></a>

```c
#define RESULT_NO_STORAGE 2
```

相关声明：[RESULT_NO_STORAGE](#ga829f7bc83b67dcf16ea4775addd87343)。

闪存（Flash Memory）空间不足，无法存放新的固件包（Firmware Package）。

<a id="r_gab5446111a8969aa2c66dae49f04c93cf"></a>

```c
#define RESULT_OUT_OF_MEM 3
```

相关声明：[RESULT_OUT_OF_MEM](#gab5446111a8969aa2c66dae49f04c93cf)。

下载过程中随机存取存储器（RAM）不足。

<a id="r_ga0655ba8c402d8b6c8bbd84fb36447bd4"></a>

```c
#define RESULT_CONNECTION_LOST 4
```

相关声明：[RESULT_CONNECTION_LOST](#ga0655ba8c402d8b6c8bbd84fb36447bd4)。

下载过程中连接丢失（Connection Lost）。

<a id="r_gadfd0ac7b6a3fededa2b4471dfe52d3d2"></a>

```c
#define RESULT_INTEGRITY_FAILED 5
```

相关声明：[RESULT_INTEGRITY_FAILED](#gadfd0ac7b6a3fededa2b4471dfe52d3d2)。

新下载的软件包（Package）完整性检查（Integrity Check）失败。

<a id="r_gab06dbfdac0c95f8100908a1177f3a62a"></a>

```c
#define RESULT_UNSUP_FW 6
```

相关声明：[RESULT_UNSUP_FW](#gab06dbfdac0c95f8100908a1177f3a62a)。

不支持的软件包类型（Package Type）。

<a id="r_ga268204053d7e23737283523224699979"></a>

```c
#define RESULT_INVALID_URI 7
```

相关声明：[RESULT_INVALID_URI](#ga268204053d7e23737283523224699979)。

统一资源标识符（URI）无效。

<a id="r_ga2dfdd95c2c03ccca25d855b6d6f96ed3"></a>

```c
#define RESULT_UPDATE_FAILED 8
```

相关声明：[RESULT_UPDATE_FAILED](#ga2dfdd95c2c03ccca25d855b6d6f96ed3)。

固件更新失败（Firmware Update Failed）。

<a id="r_gade3da37a44ee40292ec6344403db8d8d"></a>

```c
#define RESULT_UNSUP_PROTO 9
```

相关声明：[RESULT_UNSUP_PROTO](#gade3da37a44ee40292ec6344403db8d8d)。

不支持的协议（Protocol）。

## 5.14\_详细说明（Detailed Documentation）

<a id="ga0b3b9db806e5fe47cc08de34b5fb35fe"></a>

### `IPSO_OBJECT_ACCELEROMETER_ID`

```c
#define IPSO_OBJECT_ACCELEROMETER_ID 3313
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 加速度计对象（Accelerometer Object）。

<a id="ga15d664ddbfbf4d5b25dde34a5c650e6b"></a>

### `IPSO_OBJECT_BUZZER_ID`

```c
#define IPSO_OBJECT_BUZZER_ID 3338
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 蜂鸣器对象（Buzzer Object）。

<a id="gae511fd54112829e63c691776750893c2"></a>

### `IPSO_OBJECT_CURRENT_SENSOR_ID`

```c
#define IPSO_OBJECT_CURRENT_SENSOR_ID 3317
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 电流传感器对象（Current Sensor Object）。

<a id="ga21f6bc6255f5f5ed28881fa797d026ca"></a>

### `IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID`

```c
#define IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID 3435
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 填充液位传感器对象（Filling Level Sensor Object）。

<a id="gaeef485c23d306c93fc0f45dd58766ad9"></a>

### `IPSO_OBJECT_GENERIC_SENSOR_ID`

```c
#define IPSO_OBJECT_GENERIC_SENSOR_ID 3300
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 通用传感器对象（Generic Sensor Object）。

<a id="ga8075d8b7eb3b4c98f621efef673bb11f"></a>

### `IPSO_OBJECT_HUMIDITY_SENSOR_ID`

```c
#define IPSO_OBJECT_HUMIDITY_SENSOR_ID 3304
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 湿度传感器对象（Humidity Sensor Object）。

<a id="ga56ebac5260ee467b3763abe49ff3b8ff"></a>

### `IPSO_OBJECT_LIGHT_CONTROL_ID`

```c
#define IPSO_OBJECT_LIGHT_CONTROL_ID 3311
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 灯光控制对象（Light Control Object）。

<a id="ga6abcf3c5cf5001a4fdb7915336325ce1"></a>

### `IPSO_OBJECT_MAGNETOMETER_ID`

```c
#define IPSO_OBJECT_MAGNETOMETER_ID 3314
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 磁力计对象（Magnetometer Object）。

<a id="ga776a6a5e1eab3a8de0a39382f94b663a"></a>

### `IPSO_OBJECT_ONOFF_SWITCH_ID`

```c
#define IPSO_OBJECT_ONOFF_SWITCH_ID 3342
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 通断开关对象（On/Off Switch Object）。

<a id="ga752f81e91d0965a50ecfb0679bdea6ba"></a>

### `IPSO_OBJECT_PRESSURE_ID`

```c
#define IPSO_OBJECT_PRESSURE_ID 3323
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 压力传感器对象（Pressure Sensor Object）。

<a id="ga6e3119bc8f0b9143ab384e82a5bccf7c"></a>

### `IPSO_OBJECT_PUSH_BUTTON_ID`

```c
#define IPSO_OBJECT_PUSH_BUTTON_ID 3347
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 按钮对象（Push Button Object）。

<a id="ga3b0c046d93c7bcee9d4da121dd574ff0"></a>

### `IPSO_OBJECT_TEMP_SENSOR_ID`

```c
#define IPSO_OBJECT_TEMP_SENSOR_ID 3303
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 温度传感器对象（Temperature Sensor Object）。

<a id="ga46075c78a3cd73f3313abf5ffeca697b"></a>

### `IPSO_OBJECT_TIME_ID`

```c
#define IPSO_OBJECT_TIME_ID 3333
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 时间对象（Time Object）。

<a id="ga6c7bd5880fa22050748c2cb01981cbcb"></a>

### `IPSO_OBJECT_TIMER_ID`

```c
#define IPSO_OBJECT_TIMER_ID 3340
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 定时器对象（Timer Object）。

<a id="ga270a1b5a576d72099287633b32ce909f"></a>

### `IPSO_OBJECT_VOLTAGE_SENSOR_ID`

```c
#define IPSO_OBJECT_VOLTAGE_SENSOR_ID 3316
```

```c
#include <zephyr/net/lwm2m.h>
```

IPSO 电压传感器对象（Voltage Sensor Object）。

<a id="ga5f7e88b52d8e6029467a2ed10585e6d4"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP 2
```

```c
#include <zephyr/net/lwm2m.h>
```

电池已充满（Fully Charged），充电器仍连接。

<a id="gaf19da3a566782aeebebfb6ff110a9152"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_CHARGING`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGING 1
```

```c
#include <zephyr/net/lwm2m.h>
```

电池当前正在充电（Charging）。

<a id="gaa3f81df5e4d45838922eb20a15ee3153"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_DAMAGED`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_DAMAGED 3
```

```c
#include <zephyr/net/lwm2m.h>
```

电池存在问题（Battery Problem）。

<a id="ga578f6446ec1b70d2a32917abf1f5aad7"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_LOW`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_LOW 4
```

```c
#include <zephyr/net/lwm2m.h>
```

电池剩余电量低（Low on Charge）。

<a id="ga4329c971f95f1c345381d1c864a9f334"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_NORMAL`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NORMAL 0
```

```c
#include <zephyr/net/lwm2m.h>
```

电池工作正常，且未接入外部电源（Not on Power）。

<a id="gacc3dfc99fc2cd9ef7048b1a0a0fd55c8"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_NOT_INST`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NOT_INST 5
```

```c
#include <zephyr/net/lwm2m.h>
```

未安装电池（Battery Not Installed）。

<a id="ga174e118b07982b87c6c083236b79c3b7"></a>

### `LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN`

```c
#define LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN 6
```

```c
#include <zephyr/net/lwm2m.h>
```

无法获取电池信息（Battery Information Not Available）。

<a id="ga33152ea4ef497b02a12d1218d470a5a6"></a>

### `LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF`

```c
#define LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF 2
```

```c
#include <zephyr/net/lwm2m.h>
```

外部电源关闭（External Power Supply Off）。

<a id="ga3c1b7693167ff517c5cbd7bbdbfd1ea0"></a>

### `LWM2M_DEVICE_ERROR_GPS_FAILURE`

```c
#define LWM2M_DEVICE_ERROR_GPS_FAILURE 3
```

```c
#include <zephyr/net/lwm2m.h>
```

全球定位系统（GPS）模块故障。

<a id="ga53a9ee1ae09dd32a8dc2df6018798f9f"></a>

### `LWM2M_DEVICE_ERROR_LOW_POWER`

```c
#define LWM2M_DEVICE_ERROR_LOW_POWER 1
```

```c
#include <zephyr/net/lwm2m.h>
```

电池电量低（Low Battery Power）。

<a id="ga78048382d8bc85bbabbff58f0a9860f2"></a>

### `LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH`

```c
#define LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH 4
```

```c
#include <zephyr/net/lwm2m.h>
```

接收信号强度低（Low Received Signal Strength）。

<a id="ga2110d71a0c58087ff877e66b7500ba66"></a>

### `LWM2M_DEVICE_ERROR_NETWORK_FAILURE`

```c
#define LWM2M_DEVICE_ERROR_NETWORK_FAILURE 7
```

```c
#include <zephyr/net/lwm2m.h>
```

IP 连接故障（IP Connectivity Failure）。

<a id="gad54ec75eb2843d5eed199ddedca6ef4f"></a>

### `LWM2M_DEVICE_ERROR_NONE`

```c
#define LWM2M_DEVICE_ERROR_NONE 0
```

```c
#include <zephyr/net/lwm2m.h>
```

无错误（No Error）。

<a id="ga94ce0177c066dd43ef660b85afc83485"></a>

### `LWM2M_DEVICE_ERROR_OUT_OF_MEMORY`

```c
#define LWM2M_DEVICE_ERROR_OUT_OF_MEMORY 5
```

```c
#include <zephyr/net/lwm2m.h>
```

内存不足。

<a id="ga77e6352eace8116576c880bf7e416ba3"></a>

### `LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE`

```c
#define LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE 8
```

```c
#include <zephyr/net/lwm2m.h>
```

外设故障（Peripheral Malfunction）。

<a id="gabcb39cd3757ea60859984f6ad0df9e31"></a>

### `LWM2M_DEVICE_ERROR_SMS_FAILURE`

```c
#define LWM2M_DEVICE_ERROR_SMS_FAILURE 6
```

```c
#include <zephyr/net/lwm2m.h>
```

短信（SMS）故障。

<a id="ga97b9d38ec402478f10642f1f83a4f88a"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER 6
```

```c
#include <zephyr/net/lwm2m.h>
```

交流市电（AC Mains Power）。

<a id="gaf12052f903a688712928d036b782f621"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT 2
```

```c
#include <zephyr/net/lwm2m.h>
```

外部电池（External Battery）。

<a id="ga04ca8ac536eed7d411c1b1ea2b2a59ac"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT 1
```

```c
#include <zephyr/net/lwm2m.h>
```

内部电池（Internal Battery）。

<a id="gae154ca2e54ec7759dd43f2a7a275077e"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER 0
```

```c
#include <zephyr/net/lwm2m.h>
```

直流电源（DC Power）。

<a id="ga10c4633c97881ca7d87c748aaeec68c9"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL 3
```

```c
#include <zephyr/net/lwm2m.h>
```

燃料电池（Fuel Cell）。

<a id="gae7a580aac1804abbcf3feb57a5a30a02"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_MAX`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_MAX 8
```

```c
#include <zephyr/net/lwm2m.h>
```

可用电源类型（Available Power Source Type）的最大值。

<a id="ga72352523996e61ea93caff0bb80c42ba"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH 4
```

```c
#include <zephyr/net/lwm2m.h>
```

以太网供电（Power over Ethernet）。

<a id="gaa41ec1d2ca43e1385cfb11204aff729d"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR 7
```

```c
#include <zephyr/net/lwm2m.h>
```

太阳能（Solar）。

<a id="ga4877877be75d3dd3c8f600b438b7ea8e"></a>

### `LWM2M_DEVICE_PWR_SRC_TYPE_USB`

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_USB 5
```

```c
#include <zephyr/net/lwm2m.h>
```

通用串行总线（USB）

<a id="ga49f4117dfec8cd1abe9f827e235f55b0"></a>

### `LWM2M_HAS_RES_FLAG`

```c
#define LWM2M_HAS_RES_FLAG ( res, f )
```

```c
#include <zephyr/net/lwm2m.h>
```

展开值（Value）：

```c
((res->data_flags & f) == f)
```

读取资源标志（Resource Flags）的辅助宏。

<a id="gab97329844cd411195add5d72ad6aa4b7"></a>

### `LWM2M_MAX_PATH_STR_SIZE`

```c
#define LWM2M_MAX_PATH_STR_SIZE sizeof("/65535/65535/65535/65535")
```

```c
#include <zephyr/net/lwm2m.h>
```

LwM2M 路径（Path）的最大长度。

<a id="gaa8387c8838f952c7c60602e2952c7f55"></a>

### `LWM2M_OBJECT_ACCESS_CONTROL_ID`

```c
#define LWM2M_OBJECT_ACCESS_CONTROL_ID 2
```

```c
#include <zephyr/net/lwm2m.h>
```

访问控制对象（Access Control Object）。

<a id="ga85eabde1900ef052064d34cf5e3a4afe"></a>

### `LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID`

```c
#define LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID 19
```

```c
#include <zephyr/net/lwm2m.h>
```

二进制应用数据容器对象（Binary App Data Container Object）。

<a id="ga73db8616cc7dbbd04267d97a743b8ec0"></a>

### `LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID`

```c
#define LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID 4
```

```c
#include <zephyr/net/lwm2m.h>
```

连接监测对象（Connectivity Monitoring Object）。

<a id="gaa6c374c401dd36b6e121ac48c91ca9cf"></a>

### `LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID`

```c
#define LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID 7
```

```c
#include <zephyr/net/lwm2m.h>
```

连接统计对象（Connectivity Statistics Object）。

<a id="ga699f585b320ab5b259d4fb2bda10eb78"></a>

### `LWM2M_OBJECT_DEVICE_ID`

```c
#define LWM2M_OBJECT_DEVICE_ID 3
```

```c
#include <zephyr/net/lwm2m.h>
```

设备对象。

<a id="ga4f0455fb0271c2fcbb7dadb944431ff0"></a>

### `LWM2M_OBJECT_EVENT_LOG_ID`

```c
#define LWM2M_OBJECT_EVENT_LOG_ID 20
```

```c
#include <zephyr/net/lwm2m.h>
```

事件日志对象（Event Log Object）。

<a id="ga442cc51c7d0807a752ce4affe9221c5b"></a>

### `LWM2M_OBJECT_FIRMWARE_ID`

```c
#define LWM2M_OBJECT_FIRMWARE_ID 5
```

```c
#include <zephyr/net/lwm2m.h>
```

固件对象（Firmware Object）。

<a id="ga3505e9ddcd54afe86e8bd5fbc03fb565"></a>

### `LWM2M_OBJECT_GATEWAY_ID`

```c
#define LWM2M_OBJECT_GATEWAY_ID 25
```

```c
#include <zephyr/net/lwm2m.h>
```

网关对象（Gateway Object）。

<a id="ga1046ec68deab3d812d7e5921fb718028"></a>

### `LWM2M_OBJECT_LOCATION_ID`

```c
#define LWM2M_OBJECT_LOCATION_ID 6
```

```c
#include <zephyr/net/lwm2m.h>
```

位置对象（Location Object）。

<a id="gab13a1600a662ed1dbd8845c6d7d4549a"></a>

### `LWM2M_OBJECT_OSCORE_ID`

```c
#define LWM2M_OBJECT_OSCORE_ID 21
```

```c
#include <zephyr/net/lwm2m.h>
```

受限 RESTful 环境对象安全（OSCORE）对象。

<a id="ga4b4ce912a4554923974461ea3c76007e"></a>

### `LWM2M_OBJECT_PORTFOLIO_ID`

```c
#define LWM2M_OBJECT_PORTFOLIO_ID 16
```

```c
#include <zephyr/net/lwm2m.h>
```

信息组合对象（Portfolio Object）。

<a id="ga785e4a647a2cf93194a249537223ab0f"></a>

### `LWM2M_OBJECT_SECURITY_ID`

```c
#define LWM2M_OBJECT_SECURITY_ID 0
```

```c
#include <zephyr/net/lwm2m.h>
```

安全对象（Security Object）。

<a id="gace7b2f0a1f97b6e99c0958a8382ca0d2"></a>

### `LWM2M_OBJECT_SERVER_ID`

```c
#define LWM2M_OBJECT_SERVER_ID 1
```

```c
#include <zephyr/net/lwm2m.h>
```

服务器对象（Server Object）。

<a id="gac2d140b4a36d6010fe93bca443a658c0"></a>

### `LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID`

```c
#define LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID 9
```

```c
#include <zephyr/net/lwm2m.h>
```

软件管理对象（Software Management Object）。

<a id="ga34febb0c6fb1c68b0963a6e4dd721763"></a>

### `LWM2M_OBJLNK_MAX_ID`

```c
#define LWM2M_OBJLNK_MAX_ID USHRT_MAX
```

```c
#include <zephyr/net/lwm2m.h>
```

对象链接（Objlnk）资源字段的最大值。

<a id="ga3a3669237762fa8c23686e5e00b7809f"></a>

### `LWM2M_RD_CLIENT_FLAG_BOOTSTRAP`

```c
#define LWM2M_RD_CLIENT_FLAG_BOOTSTRAP BIT(0)
```

```c
#include <zephyr/net/lwm2m.h>
```

在当前会话（Session）中运行引导过程（Bootstrap Procedure）。

<a id="ga1bfa5b7d83e3560828a1fb61a4d07355"></a>

### `LWM2M_RES_DATA_FLAG_RO`

```c
#define LWM2M_RES_DATA_FLAG_RO BIT(LWM2M_RES_DATA_READ_ONLY)
```

```c
#include <zephyr/net/lwm2m.h>
```

资源只读标志（Resource Read-only Flag）。

<a id="ga12c2e0af3d3fc6dd5785e08c0d831a67"></a>

### `LWM2M_RES_DATA_READ_ONLY`

```c
#define LWM2M_RES_DATA_READ_ONLY 0
```

```c
#include <zephyr/net/lwm2m.h>
```

资源只读值位（Resource Read-only Value Bit）。

<a id="ga0655ba8c402d8b6c8bbd84fb36447bd4"></a>

### `RESULT_CONNECTION_LOST`

```c
#define RESULT_CONNECTION_LOST 4
```

```c
#include <zephyr/net/lwm2m.h>
```

下载过程中连接丢失（Connection Lost）。

<a id="ga391b47507468bbc1005903a56f80b1ea"></a>

### `RESULT_DEFAULT`

```c
#define RESULT_DEFAULT 0
```

```c
#include <zephyr/net/lwm2m.h>
```

初始值（Initial Value）。

<a id="gadfd0ac7b6a3fededa2b4471dfe52d3d2"></a>

### `RESULT_INTEGRITY_FAILED`

```c
#define RESULT_INTEGRITY_FAILED 5
```

```c
#include <zephyr/net/lwm2m.h>
```

新下载的软件包（Package）完整性检查（Integrity Check）失败。

<a id="ga268204053d7e23737283523224699979"></a>

### `RESULT_INVALID_URI`

```c
#define RESULT_INVALID_URI 7
```

```c
#include <zephyr/net/lwm2m.h>
```

统一资源标识符（URI）无效。

<a id="ga829f7bc83b67dcf16ea4775addd87343"></a>

### `RESULT_NO_STORAGE`

```c
#define RESULT_NO_STORAGE 2
```

```c
#include <zephyr/net/lwm2m.h>
```

闪存（Flash Memory）空间不足，无法存放新的固件包（Firmware Package）。

<a id="gab5446111a8969aa2c66dae49f04c93cf"></a>

### `RESULT_OUT_OF_MEM`

```c
#define RESULT_OUT_OF_MEM 3
```

```c
#include <zephyr/net/lwm2m.h>
```

下载过程中随机存取存储器（RAM）不足。

<a id="ga7cc1753a05a0821f6c70dd2bccfbab5c"></a>

### `RESULT_SUCCESS`

```c
#define RESULT_SUCCESS 1
```

```c
#include <zephyr/net/lwm2m.h>
```

固件更新成功（Firmware Updated Successfully）。

<a id="gab06dbfdac0c95f8100908a1177f3a62a"></a>

### `RESULT_UNSUP_FW`

```c
#define RESULT_UNSUP_FW 6
```

```c
#include <zephyr/net/lwm2m.h>
```

不支持的软件包类型（Package Type）。

<a id="gade3da37a44ee40292ec6344403db8d8d"></a>

### `RESULT_UNSUP_PROTO`

```c
#define RESULT_UNSUP_PROTO 9
```

```c
#include <zephyr/net/lwm2m.h>
```

不支持的协议（Protocol）。

<a id="ga2dfdd95c2c03ccca25d855b6d6f96ed3"></a>

### `RESULT_UPDATE_FAILED`

```c
#define RESULT_UPDATE_FAILED 8
```

```c
#include <zephyr/net/lwm2m.h>
```

固件更新失败（Firmware Update Failed）。

<a id="ga009085120be71a28c1f6ebdaf7503365"></a>

### `STATE_DOWNLOADED`

```c
#define STATE_DOWNLOADED 2
```

```c
#include <zephyr/net/lwm2m.h>
```

已下载（Downloaded）。

整个数据序列（Data Sequence）已下载完成。

<a id="gaeb34e88a0da4ac1274ae6b2cef010086"></a>

### `STATE_DOWNLOADING`

```c
#define STATE_DOWNLOADING 1
```

```c
#include <zephyr/net/lwm2m.h>
```

正在下载（Downloading）。

数据序列（Data Sequence）正在下载。

<a id="gaafff27c7165f059a969fe60fee51f683"></a>

### `STATE_IDLE`

```c
#define STATE_IDLE 0
```

```c
#include <zephyr/net/lwm2m.h>
```

空闲（Idle）。

下载前，或成功更新后（Before Downloading or After Successful Updating）。

<a id="gaac1dab8d1ac28bf13faeee39d1df47c5"></a>

### `STATE_UPDATING`

```c
#define STATE_UPDATING 3
```

```c
#include <zephyr/net/lwm2m.h>
```

正在更新（Updating）。

设备正在更新（Being Updated）。

<a id="gacdd09a26ce52f36c644a89a8b89f7d32"></a>

### `UCIFI_OBJECT_BATTERY_ID`

```c
#define UCIFI_OBJECT_BATTERY_ID 3411
```

```c
#include <zephyr/net/lwm2m.h>
```

uCIFI 电池对象（Battery Object）。

<a id="ga7a0bb9d5652f7f0fd0cc4a1139be6f37"></a>

### `lwm2m_cache_filter_cb_t`

```c
typedef bool(* lwm2m_cache_filter_cb_t) (const struct lwm2m_obj_path *path, const struct lwm2m_time_series_elem *element)
```

```c
#include <zephyr/net/lwm2m.h>
```

用于过滤缓存时间序列样本（Cached Time Series Samples）的回调类型。

返回 `false` 将跳过向轻量级机器到机器协议（LwM2M）缓存存储所提供的样本（Sample）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 缓存资源的对象路径（Object Path）。 |
| `element` | 引擎为缓存生成的样本（Sample）。 |

**返回（Returns）**：返回值（Returns）：`true` 保留样本，`false` 丢弃样本。

<a id="ga38dbaf038426efc75d889c4a0666dac9"></a>

### `lwm2m_ctx_event_cb_t`

```c
typedef void(* lwm2m_ctx_event_cb_t) (struct lwm2m_ctx *ctx, enum lwm2m_rd_client_event event)
```

```c
#include <zephyr/net/lwm2m.h>
```

异步注册／发现客户端事件回调（Asynchronous RD Client Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ctx` | 产生事件的 LwM2M 上下文（Context）。 |
| `[in] event` | LwM2M 资源目录客户端（RD Client）事件码。 |

<a id="gaeb32bcd4981b4c7bd891f99668ebc0fe"></a>

### `lwm2m_engine_execute_cb_t`

```c
typedef int(* lwm2m_engine_execute_cb_t) (uint16_t obj_inst_id, uint8_t *args, uint16_t args_len)
```

```c
#include <zephyr/net/lwm2m.h>
```

异步执行通知回调（Asynchronous Execute Notification Callback）。

资源执行操作（Resource Execute）触发此类型的回调。

通过 `lwm2m_register_exec_callback()` 注册此类型的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 产生回调的对象实例标识符（Object Instance ID）。 |
| `[in] args` | 指向执行参数载荷（Execute Arguments Payload）的指针；如果没有提供参数，可以为 `NULL`。 |
| `[in] args_len` | 参数载荷（Argument Payload）的字节长度。 |

**返回（Returns）**：返回值（Returns）：回调失败时返回负错误码，见 `errno.h`，用于指明失败原因；成功时返回 `0`。

<a id="ga5e531aade0537eb5e3f5756e9287e384"></a>

### `lwm2m_engine_get_data_cb_t`

```c
typedef void *(* lwm2m_engine_get_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, size_t *data_len)
```

```c
#include <zephyr/net/lwm2m.h>
```

用于获取资源缓冲区（Resource Buffer）及其长度的异步回调（Asynchronous Callback）。

访问资源的数据缓冲区（Data Buffer）之前，引擎可以通过此回调获取缓冲区指针及长度，从而使用回调提供的缓冲区，而不是资源原有的数据缓冲区。

客户端或 LwM2M 对象可以通过 `lwm2m_register_read_callback()`、`lwm2m_register_pre_write_callback()` 注册此类型的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 产生回调的对象实例标识符（Object Instance ID）。 |
| `[in] res_id` | 产生回调的资源标识符（Resource ID）。 |
| `[in] res_inst_id` | 产生回调的资源实例标识符（Resource Instance ID）；非多实例资源通常为 `0`。 |
| `[out] data_len` | 数据缓冲区长度（Data Buffer Length）。 |

**返回（Returns）**：返回值（Returns）：回调返回数据缓冲区的指针；失败时返回 `NULL`。

<a id="ga3afac013b0cf731f9c86dc3791131585"></a>

### `lwm2m_engine_set_data_cb_t`

```c
typedef int(* lwm2m_engine_set_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, uint8_t *data, uint16_t data_len, bool last_block, size_t total_size, size_t offset)
```

```c
#include <zephyr/net/lwm2m.h>
```

数据已写入资源缓冲区（Resource Buffer）时调用的异步回调（Asynchronous Callback）。

修改资源缓冲区的数据后，LwM2M 引擎可以使用此回调，将数据传回客户端或 LwM2M 对象。

在分块传输（Block-wise Transfer）中，处理函数会被多次调用，每次携带数据块和递增的偏移量（Offset）。最后一块的 `last_block` 标志设为 `true`；分块传输开始时，偏移量为 `0`。

可以通过 `lwm2m_register_validate_callback()`、`lwm2m_register_post_write_callback()` 注册此类型的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 产生回调的对象实例标识符（Object Instance ID）。 |
| `[in] res_id` | 产生回调的资源标识符（Resource ID）。 |
| `[in] res_inst_id` | 产生回调的资源实例标识符（Resource Instance ID）；非多实例资源通常为 `0`。 |
| `[in] data` | 数据指针。 |
| `[in] data_len` | 数据长度（Data Length）。 |
| `[in] last_block` | 分块传输（Block Transfer）期间用于指示最后一个数据块的标志。非分块传输时始终为 `false`。 |
| `[in] total_size` | 分块传输（Block Transfer）的预期数据总大小。非分块传输时为 `0`。 |
| `[in] offset` | 数据块偏移量（Offset）。非分块传输时始终为 `0`。 |

**返回（Returns）**：返回值（Returns）：回调失败时返回负错误码，见 `errno.h`，用于指明失败原因；成功时返回 `0`。

<a id="gabcbca483b310e0c4cd68aef2d9cda0bf"></a>

### `lwm2m_engine_user_cb_t`

```c
typedef int(* lwm2m_engine_user_cb_t) (uint16_t obj_inst_id)
```

```c
#include <zephyr/net/lwm2m.h>
```

异步事件通知回调（Asynchronous Event Notification Callback）。

LwM2M 引擎中基于对象实例和资源的各种事件可以触发此函数类型的回调，包括对象实例创建（Create）和对象实例删除（Delete）。

通过 `lwm2m_register_create_callback()`、`lwm2m_register_delete_callback()` 注册此类型的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 产生回调的对象实例标识符（Object Instance ID）。 |

**返回（Returns）**：返回值（Returns）：回调失败时返回负错误码，见 `errno.h`，用于指明失败原因；成功时返回 `0`。

<a id="gad7bea67e16e1e831e0f949dbf83d5afe"></a>

### `lwm2m_observe_cb_t`

```c
typedef void(* lwm2m_observe_cb_t) (enum lwm2m_observe_event event, struct lwm2m_obj_path *path, void *user_data)
```

```c
#include <zephyr/net/lwm2m.h>
```

观察（Observe）回调，报告观察者（Observer）的添加与删除，以及通知的确认（ACK）与超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] event` | 观察者添加／删除（Observer Add/Delete），或通知确认／超时（Notification ACK/Timeout）。 |
| `[in] path` | LwM2M 路径（Path）。 |
| `[in] user_data` | 指向 `send_traceable_notification()` 中提供的 `user_data` 缓冲区的指针，用于确定已确认（ACKed）或超时的通知对应哪些数据。 |

<a id="gaf5394884da53edb28fe4afc92bf40e6a"></a>

### `lwm2m_send_cb_t`

```c
typedef void(* lwm2m_send_cb_t) (enum lwm2m_send_status status)
```

```c
#include <zephyr/net/lwm2m.h>
```

返回发送状态（Send Status）的回调。

<a id="ga92d2227f37e7d382bc4f1a7bae21b872"></a>

### `lwm2m_set_sockopt_cb_t`

```c
typedef int(* lwm2m_set_sockopt_cb_t) (struct lwm2m_ctx *client_ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

<a id="gae7bf50f9abf1b82b76ac3e9175e685ac"></a>

### `lwm2m_socket_fault_cb_t`

```c
typedef void(* lwm2m_socket_fault_cb_t) (int error)
```

```c
#include <zephyr/net/lwm2m.h>
```

遇到套接字错误（Socket Error）时调用的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `error` | 错误码（Error Code）。 |

<a id="gac8d63952ec94ca6cfb1dbe12a6c53bfb"></a>

### `lwm2m_observe_event`

```c
enum lwm2m_observe_event
```

```c
#include <zephyr/net/lwm2m.h>
```

观察回调事件（Observe Callback Events）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LWM2M_OBSERVE_EVENT_OBSERVER_ADDED` | 观察者已添加（Observer Added）。 |
| `LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED` | 观察者已移除（Observer Removed）。 |
| `LWM2M_OBSERVE_EVENT_NOTIFY_ACK` | 通知已确认（Notification ACKed）。 |
| `LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT` | 通知已超时（Notification Timed Out）。 |

<a id="gaca90ab8960a4ff01d44735dbc0405862"></a>

### `lwm2m_rd_client_event`

```c
enum lwm2m_rd_client_event
```

```c
#include <zephyr/net/lwm2m.h>
```

LwM2M 注册／发现客户端事件（RD Client Events）。

LwM2M 客户端事件（Client Events）通过 `lwm2m_rd_client_start()` 中的 `event_cb` 函数回传。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LWM2M_RD_CLIENT_EVENT_NONE` | 无效事件（Invalid Event）。 |
| `LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE` | 引导注册失败（Bootstrap Registration Failure）。 |
| `LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE` | 引导注册完成（Bootstrap Registration Complete）。 |
| `LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE` | 引导传输完成（Bootstrap Transfer Complete）。 |
| `LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE` | 注册失败（Registration Failure）。 |
| `LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE` | 注册完成（Registration Complete）。 |
| `LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT` | 注册超时（Registration Timeout）。 |
| `LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE` | 注册更新完成（Registration Update Complete）。 |
| `LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE` | 注销失败（De-registration Failure）。 |
| `LWM2M_RD_CLIENT_EVENT_DISCONNECT` | 已断开连接（Disconnected）。 |
| `LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF` | 队列模式接收已关闭（Queue Mode RX Off）。 |
| `LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED` | 引擎已挂起（Engine Suspended）。 |
| `LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR` | 网络错误（Network Error）。 |
| `LWM2M_RD_CLIENT_EVENT_REG_UPDATE` | 注册更新（Registration Update）。 |
| `LWM2M_RD_CLIENT_EVENT_DEREGISTER` | 注销（De-register）。 |
| `LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED` | 服务器已禁用（Server Disabled）。 |

<a id="ga11de8078091631cb88b26a9a460097ab"></a>

### `lwm2m_security_mode_e`

```c
enum lwm2m_security_mode_e
```

```c
#include <zephyr/net/lwm2m.h>
```

LwM2M 安全对象（Security Object）定义的安全模式（Security Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LWM2M_SECURITY_PSK` | 预共享密钥模式（Pre-Shared Key Mode）。 |
| `LWM2M_SECURITY_RAW_PK` | 原始公钥模式（Raw Public Key Mode）。 |
| `LWM2M_SECURITY_CERT` | 证书模式（Certificate Mode）。 |
| `LWM2M_SECURITY_NOSEC` | 无安全保护模式（NoSec Mode）。 |
| `LWM2M_SECURITY_CERT_EST` | 使用 EST 的证书模式（Certificate Mode with EST）。 |

<a id="ga20848e0942882e8c2cc40ee8a48b7bfd"></a>

### `lwm2m_send_status`

```c
enum lwm2m_send_status
```

```c
#include <zephyr/net/lwm2m.h>
```

LwM2M 发送状态（Send Status）。

LwM2M 发送状态（Send Status）回传给 `lwm2m_send_cb()` 中的 `lwm2m_send_cb_t` 函数。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LWM2M_SEND_STATUS_SUCCESS` | 成功（Succeed）。 |
| `LWM2M_SEND_STATUS_FAILURE` | 失败（Failure）。 |
| `LWM2M_SEND_STATUS_TIMEOUT` | 超时（Timeout） |

<a id="ga7611c1aebb0309ee8340e06dd8ee234d"></a>

### `lwm2m_socket_states`

```c
enum lwm2m_socket_states
```

```c
#include <zephyr/net/lwm2m.h>
```

LwM2M 套接字的不同流量状态（Traffic States）。

此信息可为网络接口（Network Interface）提供提示，使其决定采用哪种电源管理（Power Management）方式。

这些提示来自 CoAP 层的消息，因此使用数据报传输层安全协议（DTLS）可能影响实际预期的数据报数量。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LWM2M_SOCKET_STATE_ONGOING` | 预计仍有持续流量（Ongoing Traffic）。 |
| `LWM2M_SOCKET_STATE_ONE_RESPONSE` | 预计下一条消息会收到一个响应（Response）。 |
| `LWM2M_SOCKET_STATE_LAST` | 下一条消息是最后一条（Last Message）。 |
| `LWM2M_SOCKET_STATE_NO_DATA` | 预计不再有数据（No More Data）。 |

<a id="ga919c7d6f418cda99c77fdaf54ae1a7b0"></a>

### `lwm2m_acknowledge()`

```c
void lwm2m_acknowledge ( struct lwm2m_ctx * client_ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

使用空确认（Empty ACK）确认当前处理的请求（Request）。

LwM2M 引擎默认对请求发送捎带响应（Piggybacked Response）。此函数允许应用回调提前为请求发送空确认（Empty ACK）。随后，引擎在执行全部回调后，以独立的可确认消息（CON Message）发送实际响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |

<a id="ga00d29a0c4935fc255e74b8c22ac49de1"></a>

### `lwm2m_cache_free_slots_get()`

```c
int lwm2m_cache_free_slots_get ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

返回缓存资源（Cached Resource）中的空闲槽位数（Free Slots）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 指向缓存资源的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：空闲槽位数量；出错时返回负 `errno` 错误码。

<a id="ga53f5b4c5967e93c7dd224fce8f416265"></a>

### `lwm2m_create_object_inst()`

```c
int lwm2m_create_object_inst ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

创建 LwM2M 对象实例（Object Instance）。

LwM2M 客户端使用此函数创建非默认的 LwM2M 对象。例如，创建第一个温度传感器对象（Temperature Sensor Object）：`lwm2m_create_obj_inst(&LWM2M_OBJ(3303, 0));`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gac69c40474180fe14c3761185b2db1c0c"></a>

### `lwm2m_create_res_inst()`

```c
int lwm2m_create_res_inst ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

创建资源实例（Resource Instance）。

LwM2M 客户端使用此函数创建多实例资源的实例（Multi-resource Instance）。例如，创建设备可用电源（Available Power Sources）的实例 `0`：`lwm2m_create_res_inst(&LWM2M_OBJ(3, 0, 6, 0));`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gaf921d4bc96090ef8735d90d173feab94"></a>

### `lwm2m_delete_object_inst()`

```c
int lwm2m_delete_object_inst ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

删除 LwM2M 对象实例（Object Instance）。

LwM2M 客户端使用此函数删除 LwM2M 对象（Objects）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gacfeb63db0423e6730ffaa826a87eb262"></a>

### `lwm2m_delete_res_inst()`

```c
int lwm2m_delete_res_inst ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

删除资源实例（Resource Instance）。

使用此函数移除现有资源实例（Resource Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gabf8726f0438477863423947a7bb77ce2"></a>

### `lwm2m_device_add_err()`

```c
int lwm2m_device_add_err ( uint8_t error_code)
```

```c
#include <zephyr/net/lwm2m.h>
```

向 LwM2M 设备对象（Device Object）注册新的错误码（Error Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] error_code` | 新的错误码（Error Code）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga6975c5c4825afaccc52741eb54aca4cb"></a>

### `lwm2m_enable_cache()`

```c
int lwm2m_enable_cache ( const struct lwm2m_obj_path * path, struct lwm2m_time_series_elem * data_cache, size_t cache_len )
```

```c
#include <zephyr/net/lwm2m.h>
```



为资源启用数据缓存（Data Cache）。

应用可以分配供 LwM2M 引擎使用的缓冲区，以启用资源数据缓存。缓冲区大小必须等于 `struct lwm2m_time_series_elem` 的大小乘以 `cache_len`。



**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 以结构表示的、指向资源的 LwM2M 路径（Path）。 |
| `data_cache` | 指向数据缓存数组（Data Cache Array）的指针。 |
| `cache_len` | 缓存条目数量（Number of Cached Entries）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga1a4dadb822a8241c5bdf339c21cc57a4"></a>

### `lwm2m_engine_pause()`

```c
int lwm2m_engine_pause ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

挂起 LwM2M 引擎线程（Engine Thread）。

挂起（Suspend）LwM2M 引擎，例如可用于网络连接中断的场景。引擎在挂起前通过 `LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED` 事件通知。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga178fea0407a5e98c4f5d5ad69688853a"></a>

### `lwm2m_engine_resume()`

```c
int lwm2m_engine_resume ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

恢复 LwM2M 引擎线程（Engine Thread）。

恢复（Resume）已挂起的 LwM2M 引擎。恢复调用成功后，引擎根据挂起时长执行完整注册（Full Registration）或注册更新（Registration Update）。`LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE` 或 `LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE` 事件表示客户端已连接服务器。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga9f72fbd0163b15c48ea09cf7d511e444"></a>

### `lwm2m_engine_start()`

```c
int lwm2m_engine_start ( struct lwm2m_ctx * client_ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

启动 LwM2M 引擎（Engine）。

LwM2M 客户端通常无需调用此函数，因为 `lwm2m_rd_client_start()` 会调用它。但如果客户端未采用资源目录客户端（RD Client）实现，则需要手动调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga077e1abd612d31dd33fab52b7d205c39"></a>

### `lwm2m_engine_stop()`

```c
int lwm2m_engine_stop ( struct lwm2m_ctx * client_ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

停止 LwM2M 引擎（Engine）。

LwM2M 客户端通常无需调用此函数，因为 `lwm2m_rd_client` 内部会调用它。但如果客户端未采用资源目录客户端（RD Client）实现，则需要手动调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga950557bce8c510bcc8b0704e7bc4a9dc"></a>

### `lwm2m_event_log_set_read_log_data_cb()`

```c
void lwm2m_event_log_set_read_log_data_cb ( lwm2m_engine_get_data_cb_t cb)
```

```c
#include <zephyr/net/lwm2m.h>
```

设置读取日志数据（Log Data）的回调。

当对相应对象调用 LwM2M 读取操作（Read Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 处理读取事件（Read Event）的回调函数。 |

<a id="ga9561c1b8407d888f6fbe1e0ceab1c235"></a>

### `lwm2m_firmware_get_cancel_cb()`

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件更新取消（Firmware Update Cancel）回调。

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于在取消固件更新（Firmware Update Cancel）时执行操作。

<a id="ga6f4b3e08c7e03cff4bf31e2f2999971e"></a>

### `lwm2m_firmware_get_cancel_cb_inst()`

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb_inst ( uint16_t obj_inst_id)
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件更新取消（Firmware Update Cancel）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于在取消固件更新（Firmware Update Cancel）时执行操作。

<a id="ga1e4b8ba1b19ac9025dca3c4799bba84a"></a>

### `lwm2m_firmware_get_update_cb()`

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于接收执行事件（Execute Event）。

<a id="ga34995e902b63c4d7d37ebd709d88a72a"></a>

### `lwm2m_firmware_get_update_cb_inst()`

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb_inst ( uint16_t obj_inst_id)
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于接收执行事件（Execute Event）。

<a id="ga4bf0bbedf5573ac18a11ac4fced11284"></a>

### `lwm2m_firmware_get_write_cb()`

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于接收分块传输数据（Block Transfer Data）。

<a id="gad7334f06c3bdb14485597794a417152d"></a>

### `lwm2m_firmware_get_write_cb_inst()`

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb_inst ( uint16_t obj_inst_id)
```

```c
#include <zephyr/net/lwm2m.h>
```

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |

**返回（Returns）**：返回值（Returns）：已注册的回调函数，用于接收分块传输数据（Block Transfer Data）。

<a id="ga3955dca5cd6d67807ed75e61a4d84d84"></a>

### `lwm2m_firmware_set_cancel_cb()`

```c
void lwm2m_firmware_set_cancel_cb ( lwm2m_engine_user_cb_t cb)
```

```c
#include <zephyr/net/lwm2m.h>
```

设置固件更新取消（Firmware Update Cancel）回调。

LwM2M 客户端使用此函数注册回调，以在取消固件更新（Firmware Update Cancel）时执行操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 取消固件更新（Firmware Update Cancel）时执行操作的回调函数。 |

<a id="gaa200b524e505f64247f1e7472c5f36d4"></a>

### `lwm2m_firmware_set_cancel_cb_inst()`

```c
void lwm2m_firmware_set_cancel_cb_inst ( uint16_t obj_inst_id, lwm2m_engine_user_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置固件更新取消（Firmware Update Cancel）的数据回调。

LwM2M 客户端使用此函数注册回调，以在取消固件更新（Firmware Update Cancel）时执行操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |
| `[in] cb` | 取消固件更新（Firmware Update Cancel）时执行操作的回调函数。 |

<a id="ga61eb38e42d9e1b3f467c43a324f2fc65"></a>

### `lwm2m_firmware_set_update_cb()`

```c
void lwm2m_firmware_set_update_cb ( lwm2m_engine_execute_cb_t cb)
```

```c
#include <zephyr/net/lwm2m.h>
```

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

LwM2M 客户端使用此函数注册回调，接收 LwM2M 固件更新对象（Firmware Update Object）中更新资源的“执行”（Execute）操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 接收执行事件（Execute Event）的回调函数。 |

<a id="ga31d0f3e40b5e3d608d16a4268b2f1b29"></a>

### `lwm2m_firmware_set_update_cb_inst()`

```c
void lwm2m_firmware_set_update_cb_inst ( uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

LwM2M 客户端使用此函数注册回调，接收 LwM2M 固件更新对象（Firmware Update Object）中更新资源的“执行”（Execute）操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |
| `[in] cb` | 接收执行事件（Execute Event）的回调函数。 |

<a id="ga6878ea0ebb512b19a4fb0859756f51d0"></a>

### `lwm2m_firmware_set_write_cb()`

```c
void lwm2m_firmware_set_write_cb ( lwm2m_engine_set_data_cb_t cb)
```

```c
#include <zephyr/net/lwm2m.h>
```

设置固件分块传输（Firmware Block Transfer）的数据回调。

LwM2M 客户端使用此函数注册回调，接收固件更新期间的分块传输数据（Block Transfer Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 接收分块传输数据（Block Transfer Data）的回调函数。 |

<a id="gac4e4a819e54344657d70ec479eb6ec8d"></a>

### `lwm2m_firmware_set_write_cb_inst()`

```c
void lwm2m_firmware_set_write_cb_inst ( uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置固件分块传输（Firmware Block Transfer）的数据回调。

LwM2M 客户端使用此函数注册回调，接收固件更新期间的分块传输数据（Block Transfer Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 对象实例标识（Object Instance ID）。 |
| `[in] cb` | 接收分块传输数据（Block Transfer Data）的回调函数。 |

<a id="gafdc72844ce0ca417e297d76288155aa4"></a>

### `lwm2m_get_bool()`

```c
int lwm2m_get_bool ( const struct lwm2m_obj_path * path, bool * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `bool` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga03b72e96a67fcbf85feb5bf0b9df81ce"></a>

### `lwm2m_get_f64()`

```c
int lwm2m_get_f64 ( const struct lwm2m_obj_path * path, double * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `double` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga4de941c36cf678e12da6e05c378a92e5"></a>

### `lwm2m_get_objlnk()`

```c
int lwm2m_get_objlnk ( const struct lwm2m_obj_path * path, struct lwm2m_objlnk * buf )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] buf` | 用于接收复制数据的 `lwm2m_objlnk` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gae245a9a1d9456af7e6283b1074944606"></a>

### `lwm2m_get_opaque()`

```c
int lwm2m_get_opaque ( const struct lwm2m_obj_path * path, void * buf, uint16_t buflen )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] buf` | 用于接收复制数据的数据缓冲区（Data Buffer）。 |
| `[in] buflen` | 缓冲区长度。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gac0b6669d8a19b03eb8b08cbbcdb0c192"></a>

### `lwm2m_get_res_buf()`

```c
int lwm2m_get_res_buf ( const struct lwm2m_obj_path * path, void ** buffer_ptr, uint16_t * buffer_len, uint16_t * data_len, uint8_t * data_flags )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（Resource）的数据缓冲区（Data Buffer）。

使用此函数获取指定 LwM2M 资源的数据缓冲区信息（Data Buffer Information）。

如果直接写入缓冲区，必须使用 `lwm2m_set_res_data_len()` 更新写入数据的新长度。

除 `pathstr` 外，如果不想读取某个输出值，可以将对应参数设为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] buffer_ptr` | 数据缓冲区指针（Data Buffer Pointer）。 |
| `[out] buffer_len` | 缓冲区长度。 |
| `[out] data_len` | 缓冲区中现有数据的长度（Length）。 |
| `[out] data_flags` | 数据缓冲区标志（Data Buffer Flags），例如只读等。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga2426db6720b3f3e15e63022cabae5ece"></a>

### `lwm2m_get_s16()`

```c
int lwm2m_get_s16 ( const struct lwm2m_obj_path * path, int16_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `s16`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `s16` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga99d7189efa25881dbcddd99e2a795f1b"></a>

### `lwm2m_get_s32()`

```c
int lwm2m_get_s32 ( const struct lwm2m_obj_path * path, int32_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `s32`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `s32` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gaaffe06ca9ee5302fb6e26164f250653e"></a>

### `lwm2m_get_s64()`

```c
int lwm2m_get_s64 ( const struct lwm2m_obj_path * path, int64_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `s64`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `s64` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga12817bfbf0a0cbb742568ee974a1c337"></a>

### `lwm2m_get_s8()`

```c
int lwm2m_get_s8 ( const struct lwm2m_obj_path * path, int8_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `s8`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `s8` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga20fc58b25468bf309175db59d67b820b"></a>

### `lwm2m_get_string()`

```c
int lwm2m_get_string ( const struct lwm2m_obj_path * path, void * str, uint16_t buflen )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为字符串（String）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] str` | 用于接收复制数据的字符串缓冲区（String Buffer）。 |
| `[in] buflen` | 缓冲区长度。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga2e1d41866b5ea35c5aa29bca9bb43812"></a>

### `lwm2m_get_time()`

```c
int lwm2m_get_time ( const struct lwm2m_obj_path * path, time_t * buf )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] buf` | 用于接收复制数据的 `time_t` 指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga1b96848f96bdab9939bb2619d3e1059b"></a>

### `lwm2m_get_u16()`

```c
int lwm2m_get_u16 ( const struct lwm2m_obj_path * path, uint16_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `u16`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `u16` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga0bc84cb39a7a537925ec7d62e54b8b48"></a>

### `lwm2m_get_u32()`

```c
int lwm2m_get_u32 ( const struct lwm2m_obj_path * path, uint32_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `u32`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `u32` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gac56e804962e529799c771d81ac1fd027"></a>

### `lwm2m_get_u8()`

```c
int lwm2m_get_u8 ( const struct lwm2m_obj_path * path, uint8_t * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

获取资源（实例）值（Resource/Instance Value），类型为 `u8`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[out] value` | 用于接收复制数据的 `u8` 缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga1065c729d5caa8ca13de7766fce77953"></a>

### `lwm2m_path_is_observed()`

```c
bool lwm2m_path_is_observed ( const struct lwm2m_obj_path * path)
```

```c
#include <zephyr/net/lwm2m.h>
```

检查路径（Path）是否正在被观察（Observed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 要检查的、以结构表示的 LwM2M 路径（Path）。 |

**返回（Returns）**：返回值（Returns）：存在与给定路径同级或更低级的观察（Observation）时为 `true`；不存在，或路径不是有效 LwM2M 路径时为 `false`。例如，路径指向资源且其父对象存在观察时返回 `true`，反过来则返回 `false`。译注：原文使用“same level or lower”，这里同时保留其示例，以明确父对象观察覆盖子资源的判断方向。

<a id="ga971c0636c19fe7f0a6e918622560a750"></a>

### `lwm2m_path_log_buf()`

```c
char * lwm2m_path_log_buf ( char * buf, struct lwm2m_obj_path * path )
```

```c
#include <zephyr/net/lwm2m.h>
```

将路径对象（Path Objects）的内容打印到日志（Log）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buf` | 用于格式化字符串的缓冲区（Buffer）。 |
| `[in] path` | 要转换为字符串的路径（Path）。 |

**返回（Returns）**：返回值（Returns）：格式化后的路径字符串（Path String）。

<a id="ga647018abc15cd65c894d9acb6c866486"></a>

### `lwm2m_pull_context_set_sockopt_callback()`

```c
void lwm2m_pull_context_set_sockopt_callback ( lwm2m_set_sockopt_cb_t set_sockopt_cb)
```

```c
#include <zephyr/net/lwm2m.h>
```

为拉取上下文（Pull Context）的客户端设置 `lwm2m_ctx::set_socketoptions` 回调。

允许在用于拉取固件更新的套接字（Socket）上设置特定选项。拉取上下文的套接字创建后、连接前，将调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] set_sockopt_cb` | 为拉取上下文客户端（Pull Context Client）设置套接字选项（Sockopts）的回调函数。 |

<a id="ga896caab5473eadff860872023d13b6c0"></a>

### `lwm2m_rd_client_ctx()`

```c
struct lwm2m_ctx * lwm2m_rd_client_ctx ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```



返回值（Returns）：LwM2M 客户端上下文（Client Context）。

**返回（Returns）**：返回值（Returns）：`ctx`，LwM2M 上下文（Context）。

<a id="ga9dfd46b8a535b1f28e644dc18f57fd79"></a>

### `lwm2m_rd_client_start()`

```c
int lwm2m_rd_client_start ( struct lwm2m_ctx * client_ctx, const char * ep_name, uint32_t flags, lwm2m_ctx_event_cb_t event_cb, lwm2m_observe_cb_t observe_cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

启动 LwM2M 注册／发现客户端（Registration/Discovery Client，RD Client）。

资源目录客户端（RD Client）位于 LwM2M 引擎的上一层，执行实现“注册接口”（Registration Interface）所需的操作。更多信息参见 LwM2M 技术规范（Technical Specification）的“客户端注册接口”（Client Registration Interface）一节。

注意（Note）：此函数自动调用 `lwm2m_engine_start()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |
| `[in] ep_name` | 注册的端点名称（Endpoint Name）。 |
| `[in] flags` | 用于配置当前 LwM2M 会话（Session）的标志。 |
| `[in] event_cb` | 客户端事件回调函数（Client Event Callback）。 |
| `[in] observe_cb` | 观察回调函数（Observe Callback），在添加或删除观察者，以及通知被确认或超时时调用。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；客户端已在运行时为 `-EINPROGRESS`；失败时为负错误码。

<a id="gafd87e5d975c4d88973ac3e95e4d156ac"></a>

### `lwm2m_rd_client_stop()`

```c
int lwm2m_rd_client_stop ( struct lwm2m_ctx * client_ctx, lwm2m_ctx_event_cb_t event_cb, bool deregister )
```

```c
#include <zephyr/net/lwm2m.h>
```

停止 LwM2M RD 客户端，执行注销（De-register）。

资源目录客户端（RD Client）位于 LwM2M 引擎的上一层，执行实现“注册接口”（Registration Interface）所需的操作。更多信息参见 LwM2M 技术规范（Technical Specification）的“客户端注册接口”（Client Registration Interface）一节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |
| `[in] event_cb` | 客户端事件回调函数（Client Event Callback）。 |
| `[in] deregister` | 若为 `true`，在客户端已注册的情况下将其注销（Deregister）；若为 `false`，则强制关闭连接。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gab4ec7a22d01259b6ba9d3a7b6681e6f0"></a>

### `lwm2m_rd_client_update()`

```c
void lwm2m_rd_client_update ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

触发 LwM2M RD 客户端的注册更新（Registration Update）。

<a id="ga346d547e02bd53ee83f83b2248449e98"></a>

### `lwm2m_register_create_callback()`

```c
int lwm2m_register_create_callback ( uint16_t obj_id, lwm2m_engine_user_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置对象实例创建事件回调（Object Instance Create Event Callback）。

创建对象实例（Object Instance）时触发此事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_id` | LwM2M 对象标识符（Object ID）。 |
| `[in] cb` | 创建对象实例回调（Create Object Instance Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga92d7e6d81ef674a6c311e1717c6bf373"></a>

### `lwm2m_register_delete_callback()`

```c
int lwm2m_register_delete_callback ( uint16_t obj_id, lwm2m_engine_user_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置对象实例删除事件回调（Object Instance Delete Event Callback）。

删除对象实例（Object Instance）时触发此事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_id` | LwM2M 对象标识符（Object ID）。 |
| `[in] cb` | 删除对象实例回调（Delete Object Instance Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga29cc5cdd697e94d7379b1fb178487916"></a>

### `lwm2m_register_exec_callback()`

```c
int lwm2m_register_exec_callback ( const struct lwm2m_obj_path * path, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源执行事件回调（Resource Execute Event Callback）。

启用资源的执行方法（Execute Method）时触发此事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] cb` | 执行资源回调（Execute Resource Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga3dd8b38e797173dae902404fb5b7a3f4"></a>

### `lwm2m_register_post_write_callback()`

```c
int lwm2m_register_post_write_callback ( const struct lwm2m_obj_path * path, lwm2m_engine_set_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）写入后回调（Post-write Callback）。

将资源值写入资源数据缓冲区（Resource Data Buffer）后触发此回调。

它允许 LwM2M 客户端或对象对资源值进行后处理（Post-process），或触发其他相关资源的计算。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] cb` | 资源写后回调（Post-write Resource Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga6f775837e07ba9b0032be8917a593e16"></a>

### `lwm2m_register_pre_write_callback()`

```c
int lwm2m_register_pre_write_callback ( const struct lwm2m_obj_path * path, lwm2m_engine_get_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）写入前回调（Pre-write Callback）。

设置资源值之前触发此回调。它可以向引擎提供专用数据缓冲区（Data Buffer），以便稍后计算实际资源值等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] cb` | 资源写前回调（Pre-write Resource Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gaf33bd6a527b6d399f3d92b666ac77dfb"></a>

### `lwm2m_register_read_callback()`

```c
int lwm2m_register_read_callback ( const struct lwm2m_obj_path * path, lwm2m_engine_get_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）读取回调（Read Callback）。

当需要绕过 LwM2M 引擎的数据处理时，客户端可以使用此接口设置资源读取回调（Resource Read Callback），例如从外部存储读回不透明二进制数据（Opaque Binary Data）。

对于可能被观察（Observed）的数据，通常不应使用此回调，因为引擎无法获知数据变化。

如果需要使用独立的数据缓冲区，应改用 `lwm2m_set_res_buf()` 设置存储空间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] cb` | 资源读取回调（Read Resource Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gad6e5fd4815f409ad59ad631b03199333"></a>

### `lwm2m_register_validate_callback()`

```c
int lwm2m_register_validate_callback ( const struct lwm2m_obj_path * path, lwm2m_engine_set_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）校验回调（Validation Callback）。

将资源值写入资源数据缓冲区（Resource Data Buffer）之前触发此回调。

此回调允许 LwM2M 客户端或对象在写入前验证数据（Validate Data）；如果因任何原因应当丢弃数据，则通过返回负错误码报告错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] cb` | 资源数据验证回调（Validate Resource Data Callback）。 |

**说明（Note）**：注意（Note）：对于已注册验证回调（Validation Callback）的所有资源，最初都会解码到临时验证缓冲区。请确保 `CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE` 足以分别容纳每一个待验证资源。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga9a0cdcc9fc6d37462eddeb54e5d1f87a"></a>

### `lwm2m_registry_lock()`

```c
void lwm2m_registry_lock ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

为当前线程锁定注册表（Registry）。

写入多个资源之前使用此函数。它会暂停 LwM2M 主线程（Main Thread），直到全部写操作完成。

<a id="gab09b62982c34887cdd16c30659d3349a"></a>

### `lwm2m_registry_unlock()`

```c
void lwm2m_registry_unlock ( void )
```

```c
#include <zephyr/net/lwm2m.h>
```

解锁之前通过 `lwm2m_registry_lock()` 锁定的注册表（Registry）。

<a id="ga6c05640737cfc4da71841a77de128be0"></a>

### `lwm2m_security_mode()`

```c
int lwm2m_security_mode ( struct lwm2m_ctx * ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

从选定的安全对象实例（Security Object Instance）读取安全模式（Security Mode）。

仅在资源目录客户端（RD Client）运行时，此数据才有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向客户端上下文（Client Context）的指针。 |

**返回（Returns）**：返回值（Returns）：`int`。正值表示 `lwm2m_security_mode_e`，否则为负错误码。译注：这里保留原文“Positive values”的表述。

<a id="ga026cc9288d2de17ec557e08b9b987ebc"></a>

### `lwm2m_send_cb()`

```c
int lwm2m_send_cb ( struct lwm2m_ctx * ctx, const struct lwm2m_obj_path path_list[], uint8_t path_list_size, lwm2m_send_cb_t reply_cb )
```

```c
#include <zephyr/net/lwm2m.h>
```



针对给定路径列表异步执行 LwM2M 发送操作（SEND），并使用确认回调（Confirmation Callback）。



**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | LwM2M 上下文（Context）。 |
| `path_list` | LwM2M 路径结构列表（Path Struct List）。 |
| `path_list_size` | 路径列表长度（Length）；最大值为 `CONFIG_LWM2M_COMPOSITE_PATH_LIST_SIZE`。 |
| `reply_cb` | 携带确认状态触发的回调（Callback）；不使用时为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga9ef21d06bef8a97b7666c0aa7fa753b4"></a>

### `lwm2m_set_bool()`

```c
int lwm2m_set_bool ( const struct lwm2m_obj_path * path, bool value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `bool` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga41b673986e11748b2ded8e1f8f05e0a7"></a>

### `lwm2m_set_bulk()`

```c
int lwm2m_set_bulk ( const struct lwm2m_res_item res_list[], size_t res_list_size )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置多个资源（实例）值（Resource/Instance Values）。

注意（Note）：值类型必须与目标资源匹配，因为此函数不执行任何类型转换（Type Conversion）。资源类型列表参见 `struct lwm2m_res_item`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] res_list` | LwM2M 资源条目列表（Resource Item List）。 |
| `[in] res_list_size` | 资源列表长度（Resource List Length）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gac4e7da0353914601c3ec101415c2e110"></a>

### `lwm2m_set_cache_filter()`

```c
int lwm2m_set_cache_filter ( const struct lwm2m_obj_path * path, lwm2m_cache_filter_cb_t filter_cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

为缓存的资源样本（Cached Resource Samples）注册过滤回调（Filtering Callback）。

每当 LwM2M 引擎尝试向资源缓存追加新样本（Sample）时，都会调用此回调。返回 `false` 可阻止存储该样本。传入 `NULL` 回调会移除此前注册的过滤器（Filter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 指向缓存资源的 LwM2M 路径（Path）。 |
| `filter_cb` | 用于判断样本是否应当缓存的回调（Callback）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；出错时为负 `errno` 错误码。

<a id="ga956c4fc742a588b7b8b95ce8481f09bf"></a>

### `lwm2m_set_default_sockopt()`

```c
int lwm2m_set_default_sockopt ( struct lwm2m_ctx * ctx)
```

```c
#include <zephyr/net/lwm2m.h>
```

设置数据报传输层安全（DTLS）连接的默认套接字选项（Socket Options）。

如果未覆盖 `lwm2m_ctx::set_socketoptions`，引擎会调用此函数。也可以在覆盖后的回调中调用它，从而在默认选项设置前后设置额外选项（Extra Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 客户端上下文（Client Context）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga3386d3f2ad8d9713fc2283ed6921c2fc"></a>

### `lwm2m_set_f64()`

```c
int lwm2m_set_f64 ( const struct lwm2m_obj_path * path, const double value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `double` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga04a18bd8a4eeea41a47803c16567d67b"></a>

### `lwm2m_set_objlnk()`

```c
int lwm2m_set_objlnk ( const struct lwm2m_obj_path * path, const struct lwm2m_objlnk * value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | 指向 `lwm2m_objlnk` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gaaef33bdf3f48fd91abdb50db4d5460f9"></a>

### `lwm2m_set_opaque()`

```c
int lwm2m_set_opaque ( const struct lwm2m_obj_path * path, const char * data_ptr, uint16_t data_len )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] data_ptr` | 数据缓冲区（Data Buffer） |
| `[in] data_len` | 缓冲区长度。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga56a2aecd38baedb5dc17258610c4780d"></a>

### `lwm2m_set_res_buf()`

```c
int lwm2m_set_res_buf ( const struct lwm2m_obj_path * path, void * buffer_ptr, uint16_t buffer_len, uint16_t data_len, uint8_t data_flags )
```

```c
#include <zephyr/net/lwm2m.h>
```

为资源（Resource）设置数据缓冲区（Data Buffer）。

使用此函数设置指定 LwM2M 资源的数据缓冲区（Data Buffer）及标志（Flags）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] buffer_ptr` | 数据缓冲区指针（Data Buffer Pointer）。 |
| `[in] buffer_len` | 缓冲区长度。 |
| `[in] data_len` | 缓冲区中现有数据的长度（Length）。 |
| `[in] data_flags` | 数据缓冲区标志（Data Buffer Flags），例如只读等。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga0f2b115d231bea6622135d72b51f55ca"></a>

### `lwm2m_set_res_data_len()`

```c
int lwm2m_set_res_data_len ( const struct lwm2m_obj_path * path, uint16_t data_len )
```

```c
#include <zephyr/net/lwm2m.h>
```

更新资源（Resource）的数据大小（Data Size）。

如果向通过 `lwm2m_get_res_buf()` 获得的缓冲区写入数据，使用此函数设置缓冲区中数据的新长度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] data_len` | 数据长度。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gad548ffedcb8328b23eb32476a97be6ee"></a>

### `lwm2m_set_s16()`

```c
int lwm2m_set_s16 ( const struct lwm2m_obj_path * path, int16_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `s16`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `s16` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga327e086959fc5649a5ef14f1f2943e88"></a>

### `lwm2m_set_s32()`

```c
int lwm2m_set_s32 ( const struct lwm2m_obj_path * path, int32_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `s32`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `s32` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga18fcee379640c0dda32d6e3d14827260"></a>

### `lwm2m_set_s64()`

```c
int lwm2m_set_s64 ( const struct lwm2m_obj_path * path, int64_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `s64`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `s64` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga37261a4b9e54eab3d1d855a084d082aa"></a>

### `lwm2m_set_s8()`

```c
int lwm2m_set_s8 ( const struct lwm2m_obj_path * path, int8_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `s8`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `s8` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga7217f33bf705011d91ba66c86a4d5747"></a>

### `lwm2m_set_string()`

```c
int lwm2m_set_string ( const struct lwm2m_obj_path * path, const char * data_ptr )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为字符串（String）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] data_ptr` | 以空字符结尾的字符缓冲区（NULL-terminated Char Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga7194ad24842e35130d8af7f5104c0844"></a>

### `lwm2m_set_time()`

```c
int lwm2m_set_time ( const struct lwm2m_obj_path * path, time_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | 纪元时间戳（Epoch Timestamp）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga1f06bb65571efee18db5d061f95399c3"></a>

### `lwm2m_set_u16()`

```c
int lwm2m_set_u16 ( const struct lwm2m_obj_path * path, uint16_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `u16`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `u16` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga9481e570b121404dc1be1ce23d904894"></a>

### `lwm2m_set_u32()`

```c
int lwm2m_set_u32 ( const struct lwm2m_obj_path * path, uint32_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `u32`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `u32` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga1aa3ff424b7190d0fbd9366626b2685c"></a>

### `lwm2m_set_u8()`

```c
int lwm2m_set_u8 ( const struct lwm2m_obj_path * path, uint8_t value )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置资源（实例）值（Resource/Instance Value），类型为 `u8`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] value` | `u8` 类型的值（Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga573e128348fb2f43a33bd09332dd677f"></a>

### `lwm2m_swmgmt_install_completed()`

```c
int lwm2m_swmgmt_install_completed ( uint16_t obj_inst_id, int error_code )
```

```c
#include <zephyr/net/lwm2m.h>
```

软件管理对象实例（Software Management Object Instance）完成安装操作（Install Operation）时调用的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 软件管理对象实例（Software Management Object Instance）。 |
| `[in] error_code` | 操作结果码（Result Code）。成功时为 `0`，否则应为负整数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="gac374d0559056ddb9cf43deae932fd128"></a>

### `lwm2m_swmgmt_set_activate_cb()`

```c
int lwm2m_swmgmt_set_activate_cb ( uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置处理软件激活请求（Software Activation Requests）的回调。

当对相应对象的激活资源实例（Activate Resource Instance）调用 LwM2M 执行操作（Execute Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 接收执行事件（Execute Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="ga7a2b93b918257bece819dc44804f27f5"></a>

### `lwm2m_swmgmt_set_deactivate_cb()`

```c
int lwm2m_swmgmt_set_deactivate_cb ( uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置处理软件停用请求（Software Deactivation Requests）的回调。

当对相应对象的停用资源实例（Deactivate Resource Instance）调用 LwM2M 执行操作（Execute Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 接收执行事件（Execute Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="gacf209563efdc5f3201152088c52d05c3"></a>

### `lwm2m_swmgmt_set_delete_package_cb()`

```c
int lwm2m_swmgmt_set_delete_package_cb ( uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置处理软件卸载请求（Software Uninstall Requests）的回调。

当对相应对象的卸载资源实例（Uninstall Resource Instance）调用 LwM2M 执行操作（Execute Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 处理执行事件（Execute Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="gadfc00060c0b538ed576b5e3edd7dac80"></a>

### `lwm2m_swmgmt_set_install_package_cb()`

```c
int lwm2m_swmgmt_set_install_package_cb ( uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置处理软件安装请求（Software Install Requests）的回调。

当对相应对象的安装资源实例（Install Resource Instance）调用 LwM2M 执行操作（Execute Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 接收执行事件（Execute Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="gab59370ce4fdc94adb4903f22ab1f95b2"></a>

### `lwm2m_swmgmt_set_read_package_version_cb()`

```c
int lwm2m_swmgmt_set_read_package_version_cb ( uint16_t obj_inst_id, lwm2m_engine_get_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置读取软件包（Software Package）的回调。

当对相应对象调用 LwM2M 读取操作（Read Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 处理读取事件（Read Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="ga293904118f972ae387c8aa85a1028b54"></a>

### `lwm2m_swmgmt_set_write_package_cb()`

```c
int lwm2m_swmgmt_set_write_package_cb ( uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb )
```

```c
#include <zephyr/net/lwm2m.h>
```

设置软件管理分块传输（Software Management Block Transfer）的数据回调。

当对相应对象的资源实例调用 LwM2M 分块写操作（Block Write Operation）时，将执行此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] obj_inst_id` | 要为其设置回调的实例编号（Instance Number）。 |
| `[in] cb` | 处理分块写事件（Block Write Event）的回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负整数。

<a id="gab45cebf6f0b6b70974367ca453d16aeb"></a>

### `lwm2m_update_device_service_period()`

```c
int lwm2m_update_device_service_period ( uint32_t period_ms)
```

```c
#include <zephyr/net/lwm2m.h>
```

更新设备服务（Device Service）的周期（Period）。

修改用于通报当前时间的周期性设备服务（Periodic Device Service）的周期时长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] period_ms` | 设备服务的新周期（Period），单位为毫秒。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga6acccbcd879901574aceab53a21800fc"></a>

### `lwm2m_update_observer_max_period()`

```c
int lwm2m_update_observer_max_period ( struct lwm2m_ctx * client_ctx, const struct lwm2m_obj_path * path, uint32_t period_s )
```

```c
#include <zephyr/net/lwm2m.h>
```

更改观察者（Observer）的 `pmax` 值。

LwM2M 客户端使用此函数修改当前观察（Observation）的 `pmax` 属性。例如，更新正在观察的温度传感器值的 `pmax`：`lwm2m__update_observer_max_period(client_ctx, &LWM2M_OBJ(3303, 0, 5700), 5);`。译注：原文示例中的 `lwm2m__update` 含两个下划线，此处保留原始示例；调用时请对照本节实际函数声明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] period_s` | 要设置的 `pmax` 值，单位为秒（Seconds）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gadd163806d70713d8349a9db484ba88bf"></a>

### `lwm2m_update_observer_min_period()`

```c
int lwm2m_update_observer_min_period ( struct lwm2m_ctx * client_ctx, const struct lwm2m_obj_path * path, uint32_t period_s )
```

```c
#include <zephyr/net/lwm2m.h>
```

更改观察者（Observer）的 `pmin` 值。

LwM2M 客户端使用此函数修改当前观察（Observation）的 `pmin` 属性。例如，更新正在观察的温度传感器值的 `pmin`：`lwm2m_update_observer_min_period(client_ctx, &LWM2M_OBJ(3303, 0, 5700), 5);`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client_ctx` | LwM2M 上下文（Context）。 |
| `[in] path` | 以结构表示的 LwM2M 路径（Path）。 |
| `[in] period_s` | 要设置的 `pmin` 值，单位为秒（Seconds）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。


## 5.15\_原页交叉引用（Cross References）

- [轻量级M2M（LwM2M）的路径辅助宏。](../api_protocol_topic_reference/P023_轻量级M2M（LwM2M）的路径辅助宏。.md)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)
- [lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)
- [lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)
- [lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)
- [lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lwm2m_ctx::set_socketoptions](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a8714a3ee6870515631fd75e74644d39c)
- [http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html)
- [zephyr/net/lwm2m.h](../api_file_modem_network_reference/P002_zephyr__net__lwm2m.h_文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3"></a>
<a id="ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c"></a>
<a id="ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885"></a>
<a id="ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13"></a>
<a id="ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763"></a>
<a id="gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25"></a>
<a id="gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716"></a>
<a id="gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba"></a>
<a id="gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7"></a>
<a id="gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824"></a>
<a id="gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4"></a>
<a id="gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd"></a>
<a id="gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a"></a>
<a id="gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab"></a>
<a id="gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711"></a>
<a id="gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100"></a>
<a id="gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_输入事件定义（Input Event Definitions）.md) · [返回大纲](大纲.md)
