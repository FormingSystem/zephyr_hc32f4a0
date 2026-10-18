---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-21
title: zephyr__net__mqtt_sn.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_net\_\_mqtt\_sn.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT-SN客户端实现（Client Implementation）。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/types.h>
#include <sys/types.h>
```

查看此文件的源码。

MQTT-SN 客户端实现（Client Implementation）。本头文件定义 MQTT-SN 客户端的应用接口，面向协议版本 1.2。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_mqtt_5Fsn_5Fdata"></a>

```c
struct mqtt_sn_data
```

相关声明：[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

内存缓冲区（Memory Buffers）的抽象。

<a id="r_mqtt_5Fsn_5Fevt_5Fparam"></a>

```c
union mqtt_sn_evt_param
```

相关声明：[mqtt_sn_evt_param](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md)。

事件元数据（Event Metadata）。

<a id="r_mqtt_5Fsn_5Fevt"></a>

```c
struct mqtt_sn_evt
```

相关声明：[mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)。

由事件回调处理的MQTT-SN事件结构（Event Structure）。

<a id="r_mqtt_5Fsn_5Ftransport"></a>

```c
struct mqtt_sn_transport
```

相关声明：[mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)。

描述MQTT-SN传输（Transport）的结构。

<a id="r_mqtt_5Fsn_5Fwill_5Fupdate"></a>

```c
struct mqtt_sn_will_update
```

相关声明：[mqtt_sn_will_update](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md)。

用于存储遗嘱更新（Will Update）状态的结构。

<a id="r_mqtt_5Fsn_5Fconnect_5Fretry"></a>

```c
struct mqtt_sn_connect_retry
```

相关声明：[mqtt_sn_connect_retry](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md)。

用于存储待完成连接（CONNECT）状态的结构。

<a id="r_mqtt_5Fsn_5Fclient"></a>

```c
struct mqtt_sn_client
```

相关声明：[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

描述MQTT-SN客户端（Client）的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_gaf8223bf7e5548323c453b30be031e37e"></a>

```c
#define MQTT_SN_DATA_STRING_LITERAL(literal)
```

相关声明：[MQTT_SN_DATA_STRING_LITERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaf8223bf7e5548323c453b30be031e37e)。

使用 C 字符串字面量（Literal String）初始化内存缓冲区。

<a id="r_gabb58a0e4aa418a864f1208ff188f40bc"></a>

```c
#define MQTT_SN_DATA_BYTES(...)
```

相关声明：[MQTT_SN_DATA_BYTES](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabb58a0e4aa418a864f1208ff188f40bc)。

使用单个字节值初始化内存缓冲区（Memory Buffer）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.3\_类型定义（Typedefs）

<a id="r_gaecd8b966f3e2112261993f8a2cd5c94a"></a>

```c
typedef void(* mqtt_sn_evt_cb_t) (struct mqtt_sn_client *client, const struct mqtt_sn_evt *evt)
```

相关声明：[mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)。

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.4\_枚举（Enumerations）

<a id="r_ga8072226d2d96e184137ef40775389786"></a>

```c
enum mqtt_sn_qos { MQTT_SN_QOS_0 , MQTT_SN_QOS_1 , MQTT_SN_QOS_2 , MQTT_SN_QOS_M1 }
```

相关声明：[mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)、[MQTT_SN_QOS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)、[MQTT_SN_QOS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)、[MQTT_SN_QOS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)、[MQTT_SN_QOS_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)。

服务质量（Quality of Service，QoS）。

<a id="r_gabca9262da31b09086b0f802d15eea3fd"></a>

```c
enum mqtt_sn_topic_type { MQTT_SN_TOPIC_TYPE_NORMAL , MQTT_SN_TOPIC_TYPE_PREDEF , MQTT_SN_TOPIC_TYPE_SHORT }
```

相关声明：[mqtt_sn_topic_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabca9262da31b09086b0f802d15eea3fd)、[MQTT_SN_TOPIC_TYPE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)、[MQTT_SN_TOPIC_TYPE_PREDEF](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)、[MQTT_SN_TOPIC_TYPE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)。

MQTT-SN 主题类型（Topic Types）。

<a id="r_gaab8c9d8ddbaa2af542fdcd3e4178ea9e"></a>

```c
enum mqtt_sn_return_code { MQTT_SN_CODE_ACCEPTED = 0x00 , MQTT_SN_CODE_REJECTED_CONGESTION = 0x01 , MQTT_SN_CODE_REJECTED_TOPIC_ID = 0x02 , MQTT_SN_CODE_REJECTED_NOTSUP = 0x03 }
```

相关声明：[mqtt_sn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)、[MQTT_SN_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)、[MQTT_SN_CODE_REJECTED_CONGESTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)、[MQTT_SN_CODE_REJECTED_TOPIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)、[MQTT_SN_CODE_REJECTED_NOTSUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)。

MQTT-SN 返回码（Return Codes）。

<a id="r_gaa52518be4aa308dda9552e14d0045c42"></a>

```c
enum mqtt_sn_evt_type { MQTT_SN_EVT_CONNECTED , MQTT_SN_EVT_DISCONNECTED , MQTT_SN_EVT_ASLEEP , MQTT_SN_EVT_AWAKE , MQTT_SN_EVT_PUBLISH , MQTT_SN_EVT_PINGRESP , MQTT_SN_EVT_ADVERTISE , MQTT_SN_EVT_GWINFO , MQTT_SN_EVT_SEARCHGW }
```

相关声明：[mqtt_sn_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaa52518be4aa308dda9552e14d0045c42)、[MQTT_SN_EVT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)、[MQTT_SN_EVT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)、[MQTT_SN_EVT_ASLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)、[MQTT_SN_EVT_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)、[MQTT_SN_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)、[MQTT_SN_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)、[MQTT_SN_EVT_ADVERTISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672)、[MQTT_SN_EVT_GWINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a)、[MQTT_SN_EVT_SEARCHGW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83)。

库可以发出的事件类型（Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.5\_函数（Functions）

<a id="r_gae6a3f7a7762653474df97364ef69fc74"></a>

```c
int mqtt_sn_client_init (struct mqtt_sn_client *client, const struct mqtt_sn_data *client_id, struct mqtt_sn_transport *transport, mqtt_sn_evt_cb_t evt_cb, void *tx, size_t txsz, void *rx, size_t rxsz)
```

相关声明：[mqtt_sn_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gae6a3f7a7762653474df97364ef69fc74)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)、[mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)、[mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)。

初始化客户端（Client）。

<a id="r_ga67d69e4e3f00b31b5ea3b37fb6d653b1"></a>

```c
void mqtt_sn_client_deinit (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_client_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga67d69e4e3f00b31b5ea3b37fb6d653b1)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

反初始化客户端（Deinitialize Client）。

<a id="r_gadd38840ebc78217a692748afb704b42b"></a>

```c
int mqtt_sn_add_gw (struct mqtt_sn_client *client, uint8_t gw_id, struct mqtt_sn_data gw_addr)
```

相关声明：[mqtt_sn_add_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd38840ebc78217a692748afb704b42b)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

手动添加网关（Gateway），跳过常规搜索过程。

<a id="r_gafdf80b1de5d1b069b2f75b2bd688416f"></a>

```c
int mqtt_sn_search (struct mqtt_sn_client *client, uint8_t radius)
```

相关声明：[mqtt_sn_search](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafdf80b1de5d1b069b2f75b2bd688416f)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 MQTT-SN 网关搜索（GW Search）过程。

<a id="r_ga8c2a525f1c30e5d5ff37180d33a76d4d"></a>

```c
int mqtt_sn_connect (struct mqtt_sn_client *client, bool will, bool clean_session)
```

相关声明：[mqtt_sn_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8c2a525f1c30e5d5ff37180d33a76d4d)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

连接客户端（Client）。

<a id="r_gab9cba16f8ce06f606ee81e0d34deb862"></a>

```c
int mqtt_sn_disconnect (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gab9cba16f8ce06f606ee81e0d34deb862)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

断开客户端（Client）连接。

<a id="r_gaf29a6339419ea02052fe53a18bb8e5ee"></a>

```c
int mqtt_sn_sleep (struct mqtt_sn_client *client, uint16_t duration)
```

相关声明：[mqtt_sn_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaf29a6339419ea02052fe53a18bb8e5ee)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将客户端置于休眠状态（Sleep State）。

<a id="r_ga9b481db6d39dee05e2c58d4c721fe0a5"></a>

```c
int mqtt_sn_subscribe (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga9b481db6d39dee05e2c58d4c721fe0a5)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

订阅给定主题（Topic）。

<a id="r_ga1bcd2a0f52610708bebb4b3b6d6cbf35"></a>

```c
int mqtt_sn_unsubscribe (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1bcd2a0f52610708bebb4b3b6d6cbf35)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

取消订阅主题（Topic）。

<a id="r_ga434c3626ceaf3a9b60c5ffb75e9b5b56"></a>

```c
int mqtt_sn_publish (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name, bool retain, struct mqtt_sn_data *data)
```

相关声明：[mqtt_sn_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga434c3626ceaf3a9b60c5ffb75e9b5b56)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

发布一个值（Publish a Value）。

<a id="r_gafa1f81168d44152ad72c5f3d1c744b49"></a>

```c
int mqtt_sn_input (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

检查传输通道（Transport）是否有新入站数据。

<a id="r_gade962a4da5311a403893ba24714dc332"></a>

```c
int mqtt_sn_get_topic_name (struct mqtt_sn_client *client, uint16_t id, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_get_topic_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gade962a4da5311a403893ba24714dc332)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

根据主题 ID（Topic ID）获取主题名称。

<a id="r_gadd0a809d7e451df55540fb7ea227fd50"></a>

```c
int mqtt_sn_predefine_topic (struct mqtt_sn_client *client, uint16_t topic_id, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_predefine_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd0a809d7e451df55540fb7ea227fd50)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

预定义主题（Predefine Topic）。

<a id="r_ga1a6b39984ef047f0089cea43f5378d0f"></a>

```c
int mqtt_sn_define_short_topic (struct mqtt_sn_client *client, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_define_short_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1a6b39984ef047f0089cea43f5378d0f)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

定义短主题（Short Topic）。

<a id="r_ga90ced79565deb9a92be8cd3a99d808b7"></a>

```c
int mqtt_sn_update_will_topic (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_update_will_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga90ced79565deb9a92be8cd3a99d808b7)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

向服务器发送遗嘱主题更新（Will Topic Update）。

<a id="r_ga0850d89af7dd6b5d3ec2b1e1abe01d19"></a>

```c
int mqtt_sn_update_will_message (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_update_will_message](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga0850d89af7dd6b5d3ec2b1e1abe01d19)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

向服务器发送遗嘱消息更新（Will Message Update）。


## 21.6\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P118_mqtt_sn.h_源码浏览.md)
- [mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)
- [mqtt_sn_evt_param](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md)
- [mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)
- [mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)
- [mqtt_sn_will_update](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md)
- [mqtt_sn_connect_retry](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md)
- [mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)
- [MQTT_SN_DATA_STRING_LITERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaf8223bf7e5548323c453b30be031e37e)
- [MQTT_SN_DATA_BYTES](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabb58a0e4aa418a864f1208ff188f40bc)
- [mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)
- [mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)
- [MQTT_SN_QOS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)
- [MQTT_SN_QOS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)
- [MQTT_SN_QOS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)
- [MQTT_SN_QOS_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)
- [mqtt_sn_topic_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabca9262da31b09086b0f802d15eea3fd)
- [MQTT_SN_TOPIC_TYPE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)
- [MQTT_SN_TOPIC_TYPE_PREDEF](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)
- [MQTT_SN_TOPIC_TYPE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)
- [mqtt_sn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)
- [MQTT_SN_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)
- [MQTT_SN_CODE_REJECTED_CONGESTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)
- [MQTT_SN_CODE_REJECTED_TOPIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)
- [MQTT_SN_CODE_REJECTED_NOTSUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)
- [mqtt_sn_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaa52518be4aa308dda9552e14d0045c42)
- [MQTT_SN_EVT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)
- [MQTT_SN_EVT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)
- [MQTT_SN_EVT_ASLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)
- [MQTT_SN_EVT_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)
- [MQTT_SN_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)
- [MQTT_SN_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)
- [MQTT_SN_EVT_ADVERTISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672)
- [MQTT_SN_EVT_GWINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a)
- [MQTT_SN_EVT_SEARCHGW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83)
- [mqtt_sn_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gae6a3f7a7762653474df97364ef69fc74)
- [mqtt_sn_client_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga67d69e4e3f00b31b5ea3b37fb6d653b1)
- [mqtt_sn_add_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd38840ebc78217a692748afb704b42b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_sn_search](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafdf80b1de5d1b069b2f75b2bd688416f)
- [mqtt_sn_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8c2a525f1c30e5d5ff37180d33a76d4d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mqtt_sn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gab9cba16f8ce06f606ee81e0d34deb862)
- [mqtt_sn_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaf29a6339419ea02052fe53a18bb8e5ee)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mqtt_sn_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga9b481db6d39dee05e2c58d4c721fe0a5)
- [mqtt_sn_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1bcd2a0f52610708bebb4b3b6d6cbf35)
- [mqtt_sn_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga434c3626ceaf3a9b60c5ffb75e9b5b56)
- [mqtt_sn_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49)
- [mqtt_sn_get_topic_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gade962a4da5311a403893ba24714dc332)
- [mqtt_sn_predefine_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd0a809d7e451df55540fb7ea227fd50)
- [mqtt_sn_define_short_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1a6b39984ef047f0089cea43f5378d0f)
- [mqtt_sn_update_will_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga90ced79565deb9a92be8cd3a99d808b7)
- [mqtt_sn_update_will_message](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga0850d89af7dd6b5d3ec2b1e1abe01d19)

<a id="header-details"></a>

---

[上一章](P020_zephyr__sd__mmc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__dt-bindings__clock-monitor__nxp-fmeas.h_文件参考.md)
