---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-6
title: MQTT-SN 客户端库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_MQTT-SN 客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自（Since）3.3 起提供，版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

## 6.2\_宏定义（Macros）

<a id="r_gaf8223bf7e5548323c453b30be031e37e"></a>

```c
#define MQTT_SN_DATA_STRING_LITERAL(literal)
```

相关声明：[MQTT_SN_DATA_STRING_LITERAL](#gaf8223bf7e5548323c453b30be031e37e)。

使用 C 字符串字面量（Literal String）初始化内存缓冲区。

<a id="r_gabb58a0e4aa418a864f1208ff188f40bc"></a>

```c
#define MQTT_SN_DATA_BYTES(...)
```

相关声明：[MQTT_SN_DATA_BYTES](#gabb58a0e4aa418a864f1208ff188f40bc)。

使用单个字节值初始化内存缓冲区（Memory Buffer）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gaecd8b966f3e2112261993f8a2cd5c94a"></a>

```c
typedef void(* mqtt_sn_evt_cb_t) (struct mqtt_sn_client *client, const struct mqtt_sn_evt *evt)
```

相关声明：[mqtt_sn_evt_cb_t](#gaecd8b966f3e2112261993f8a2cd5c94a)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)。

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga8072226d2d96e184137ef40775389786"></a>

```c
enum mqtt_sn_qos { MQTT_SN_QOS_0 , MQTT_SN_QOS_1 , MQTT_SN_QOS_2 , MQTT_SN_QOS_M1 }
```

相关声明：[mqtt_sn_qos](#ga8072226d2d96e184137ef40775389786)、[MQTT_SN_QOS_0](#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)、[MQTT_SN_QOS_1](#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)、[MQTT_SN_QOS_2](#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)、[MQTT_SN_QOS_M1](#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)。

服务质量（Quality of Service，QoS）。

<a id="r_gabca9262da31b09086b0f802d15eea3fd"></a>

```c
enum mqtt_sn_topic_type { MQTT_SN_TOPIC_TYPE_NORMAL , MQTT_SN_TOPIC_TYPE_PREDEF , MQTT_SN_TOPIC_TYPE_SHORT }
```

相关声明：[mqtt_sn_topic_type](#gabca9262da31b09086b0f802d15eea3fd)、[MQTT_SN_TOPIC_TYPE_NORMAL](#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)、[MQTT_SN_TOPIC_TYPE_PREDEF](#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)、[MQTT_SN_TOPIC_TYPE_SHORT](#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)。

MQTT-SN 主题类型（Topic Types）。

<a id="r_gaab8c9d8ddbaa2af542fdcd3e4178ea9e"></a>

```c
enum mqtt_sn_return_code { MQTT_SN_CODE_ACCEPTED = 0x00 , MQTT_SN_CODE_REJECTED_CONGESTION = 0x01 , MQTT_SN_CODE_REJECTED_TOPIC_ID = 0x02 , MQTT_SN_CODE_REJECTED_NOTSUP = 0x03 }
```

相关声明：[mqtt_sn_return_code](#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)、[MQTT_SN_CODE_ACCEPTED](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)、[MQTT_SN_CODE_REJECTED_CONGESTION](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)、[MQTT_SN_CODE_REJECTED_TOPIC_ID](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)、[MQTT_SN_CODE_REJECTED_NOTSUP](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)。

MQTT-SN 返回码（Return Codes）。

<a id="r_gaa52518be4aa308dda9552e14d0045c42"></a>

```c
enum mqtt_sn_evt_type { MQTT_SN_EVT_CONNECTED , MQTT_SN_EVT_DISCONNECTED , MQTT_SN_EVT_ASLEEP , MQTT_SN_EVT_AWAKE , MQTT_SN_EVT_PUBLISH , MQTT_SN_EVT_PINGRESP , MQTT_SN_EVT_ADVERTISE , MQTT_SN_EVT_GWINFO , MQTT_SN_EVT_SEARCHGW }
```

相关声明：[mqtt_sn_evt_type](#gaa52518be4aa308dda9552e14d0045c42)、[MQTT_SN_EVT_CONNECTED](#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)、[MQTT_SN_EVT_DISCONNECTED](#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)、[MQTT_SN_EVT_ASLEEP](#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)、[MQTT_SN_EVT_AWAKE](#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)、[MQTT_SN_EVT_PUBLISH](#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)、[MQTT_SN_EVT_PINGRESP](#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)、[MQTT_SN_EVT_ADVERTISE](#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672)、[MQTT_SN_EVT_GWINFO](#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a)、[MQTT_SN_EVT_SEARCHGW](#ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83)。

库可以发出的事件类型（Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gae6a3f7a7762653474df97364ef69fc74"></a>

```c
int mqtt_sn_client_init (struct mqtt_sn_client *client, const struct mqtt_sn_data *client_id, struct mqtt_sn_transport *transport, mqtt_sn_evt_cb_t evt_cb, void *tx, size_t txsz, void *rx, size_t rxsz)
```

相关声明：[mqtt_sn_client_init](#gae6a3f7a7762653474df97364ef69fc74)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)、[mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)、[mqtt_sn_evt_cb_t](#gaecd8b966f3e2112261993f8a2cd5c94a)。

初始化客户端（Client）。

<a id="r_ga67d69e4e3f00b31b5ea3b37fb6d653b1"></a>

```c
void mqtt_sn_client_deinit (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_client_deinit](#ga67d69e4e3f00b31b5ea3b37fb6d653b1)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

反初始化客户端（Deinitialize Client）。

<a id="r_gadd38840ebc78217a692748afb704b42b"></a>

```c
int mqtt_sn_add_gw (struct mqtt_sn_client *client, uint8_t gw_id, struct mqtt_sn_data gw_addr)
```

相关声明：[mqtt_sn_add_gw](#gadd38840ebc78217a692748afb704b42b)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

手动添加网关（Gateway），跳过常规搜索过程。

<a id="r_gafdf80b1de5d1b069b2f75b2bd688416f"></a>

```c
int mqtt_sn_search (struct mqtt_sn_client *client, uint8_t radius)
```

相关声明：[mqtt_sn_search](#gafdf80b1de5d1b069b2f75b2bd688416f)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 MQTT-SN 网关搜索（GW Search）过程。

<a id="r_ga8c2a525f1c30e5d5ff37180d33a76d4d"></a>

```c
int mqtt_sn_connect (struct mqtt_sn_client *client, bool will, bool clean_session)
```

相关声明：[mqtt_sn_connect](#ga8c2a525f1c30e5d5ff37180d33a76d4d)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

连接客户端（Client）。

<a id="r_gab9cba16f8ce06f606ee81e0d34deb862"></a>

```c
int mqtt_sn_disconnect (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_disconnect](#gab9cba16f8ce06f606ee81e0d34deb862)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

断开客户端（Client）连接。

<a id="r_gaf29a6339419ea02052fe53a18bb8e5ee"></a>

```c
int mqtt_sn_sleep (struct mqtt_sn_client *client, uint16_t duration)
```

相关声明：[mqtt_sn_sleep](#gaf29a6339419ea02052fe53a18bb8e5ee)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将客户端置于休眠状态（Sleep State）。

<a id="r_ga9b481db6d39dee05e2c58d4c721fe0a5"></a>

```c
int mqtt_sn_subscribe (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_subscribe](#ga9b481db6d39dee05e2c58d4c721fe0a5)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

订阅给定主题（Topic）。

<a id="r_ga1bcd2a0f52610708bebb4b3b6d6cbf35"></a>

```c
int mqtt_sn_unsubscribe (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_unsubscribe](#ga1bcd2a0f52610708bebb4b3b6d6cbf35)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

取消订阅主题（Topic）。

<a id="r_ga434c3626ceaf3a9b60c5ffb75e9b5b56"></a>

```c
int mqtt_sn_publish (struct mqtt_sn_client *client, enum mqtt_sn_qos qos, struct mqtt_sn_data *topic_name, bool retain, struct mqtt_sn_data *data)
```

相关声明：[mqtt_sn_publish](#ga434c3626ceaf3a9b60c5ffb75e9b5b56)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_qos](#ga8072226d2d96e184137ef40775389786)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

发布一个值（Publish a Value）。

<a id="r_gafa1f81168d44152ad72c5f3d1c744b49"></a>

```c
int mqtt_sn_input (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_input](#gafa1f81168d44152ad72c5f3d1c744b49)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

检查传输通道（Transport）是否有新入站数据。

<a id="r_gade962a4da5311a403893ba24714dc332"></a>

```c
int mqtt_sn_get_topic_name (struct mqtt_sn_client *client, uint16_t id, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_get_topic_name](#gade962a4da5311a403893ba24714dc332)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

根据主题 ID（Topic ID）获取主题名称。

<a id="r_gadd0a809d7e451df55540fb7ea227fd50"></a>

```c
int mqtt_sn_predefine_topic (struct mqtt_sn_client *client, uint16_t topic_id, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_predefine_topic](#gadd0a809d7e451df55540fb7ea227fd50)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

预定义主题（Predefine Topic）。

<a id="r_ga1a6b39984ef047f0089cea43f5378d0f"></a>

```c
int mqtt_sn_define_short_topic (struct mqtt_sn_client *client, struct mqtt_sn_data *topic_name)
```

相关声明：[mqtt_sn_define_short_topic](#ga1a6b39984ef047f0089cea43f5378d0f)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)、[mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)。

定义短主题（Short Topic）。

<a id="r_ga90ced79565deb9a92be8cd3a99d808b7"></a>

```c
int mqtt_sn_update_will_topic (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_update_will_topic](#ga90ced79565deb9a92be8cd3a99d808b7)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

向服务器发送遗嘱主题更新（Will Topic Update）。

<a id="r_ga0850d89af7dd6b5d3ec2b1e1abe01d19"></a>

```c
int mqtt_sn_update_will_message (struct mqtt_sn_client *client)
```

相关声明：[mqtt_sn_update_will_message](#ga0850d89af7dd6b5d3ec2b1e1abe01d19)、[mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)。

向服务器发送遗嘱消息更新（Will Message Update）。

## 6.6\_详细说明（Detailed Documentation）

<a id="gabb58a0e4aa418a864f1208ff188f40bc"></a>

### `MQTT_SN_DATA_BYTES`

```c
#define MQTT_SN_DATA_BYTES ( ...)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

展开值（Value）：

```c
((struct mqtt_sn_data){(uint8_t[]){__VA_ARGS__}, sizeof((uint8_t[]){__VA_ARGS__})})
```

使用单个字节值初始化内存缓冲区（Memory Buffer）。

用法如下：

```c
struct mqtt_sn_data data = MQTT_SN_DATA_BYTES(0x13, 0x37);
```

<a id="gaf8223bf7e5548323c453b30be031e37e"></a>

### `MQTT_SN_DATA_STRING_LITERAL`

```c
#define MQTT_SN_DATA_STRING_LITERAL ( literal)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

展开值（Value）：

```c
((struct mqtt_sn_data){literal, sizeof(literal) - 1})
```

使用 C 字符串字面量（Literal String）初始化内存缓冲区。

用法如下：

```c
struct mqtt_sn_data topic = MQTT_SN_DATA_STRING_LITERAL("/zephyr");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] literal` | 用于生成 `mqtt_sn_data` 对象的字符串字面量（Literal String）。 |

<a id="gaecd8b966f3e2112261993f8a2cd5c94a"></a>

### `mqtt_sn_evt_cb_t`

```c
typedef void(* mqtt_sn_evt_cb_t) (struct mqtt_sn_client *client, const struct mqtt_sn_evt *evt)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识接收此事件通知的客户端（Client）。 |
| `[in] evt` | 事件说明，以及结果和关联参数（如有）。 |

<a id="gaa52518be4aa308dda9552e14d0045c42"></a>

### `mqtt_sn_evt_type`

```c
enum mqtt_sn_evt_type
```

```c
#include <zephyr/net/mqtt_sn.h>
```

库可以发出的事件类型（Event Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_SN_EVT_CONNECTED` | 已连接到网关（Gateway）。 |
| `MQTT_SN_EVT_DISCONNECTED` | 已断开连接（Disconnected）。 |
| `MQTT_SN_EVT_ASLEEP` | 已进入睡眠状态（ASLEEP）。 |
| `MQTT_SN_EVT_AWAKE` | 已进入唤醒状态（AWAKE）。 |
| `MQTT_SN_EVT_PUBLISH` | 收到 PUBLISH 消息。 |
| `MQTT_SN_EVT_PINGRESP` | 收到 PINGRESP 消息。 |
| `MQTT_SN_EVT_ADVERTISE` | 收到 ADVERTISE 消息。 |
| `MQTT_SN_EVT_GWINFO` | 收到 GWINFO 消息。 |
| `MQTT_SN_EVT_SEARCHGW` | 收到 SEARCHGW 消息。 |

<a id="ga8072226d2d96e184137ef40775389786"></a>

### `mqtt_sn_qos`

```c
enum mqtt_sn_qos
```

```c
#include <zephyr/net/mqtt_sn.h>
```

服务质量（Quality of Service，QoS）。

QoS 0–2 的行为与基本 MQTT 相同，QoS -1 是 MQTT-SN 增加的级别。目前尚不支持 QoS -1。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_SN_QOS_0` | 服务质量（QoS）0。 |
| `MQTT_SN_QOS_1` | 服务质量（QoS）1。 |
| `MQTT_SN_QOS_2` | 服务质量（QoS）2。 |
| `MQTT_SN_QOS_M1` | 服务质量（QoS）-1。 |

<a id="gaab8c9d8ddbaa2af542fdcd3e4178ea9e"></a>

### `mqtt_sn_return_code`

```c
enum mqtt_sn_return_code
```

```c
#include <zephyr/net/mqtt_sn.h>
```

MQTT-SN 返回码（Return Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_SN_CODE_ACCEPTED` | 已接受（Accepted）。 |
| `MQTT_SN_CODE_REJECTED_CONGESTION` | 拒绝：拥塞（Congestion）。 |
| `MQTT_SN_CODE_REJECTED_TOPIC_ID` | 拒绝：主题 ID 无效（Invalid Topic ID）。 |
| `MQTT_SN_CODE_REJECTED_NOTSUP` | 拒绝：不支持（Not Supported）。 |

<a id="gabca9262da31b09086b0f802d15eea3fd"></a>

### `mqtt_sn_topic_type`

```c
enum mqtt_sn_topic_type
```

```c
#include <zephyr/net/mqtt_sn.h>
```

MQTT-SN 主题类型（Topic Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_SN_TOPIC_TYPE_NORMAL` | 普通主题（Normal Topic）。允许使用任何有效的 UTF-8 字符串作为主题名称。 |
| `MQTT_SN_TOPIC_TYPE_PREDEF` | 预定义主题（Pre-Defined Topic）。允许使用一个双字节标识符表示主题名称，对应名称由客户端和网关／服务器双方事先知晓。 |
| `MQTT_SN_TOPIC_TYPE_SHORT` | 短主题（Short Topic）。允许使用一个双字节字符串作为主题名称。 |

<a id="gadd38840ebc78217a692748afb704b42b"></a>

### `mqtt_sn_add_gw()`

```c
int mqtt_sn_add_gw ( struct mqtt_sn_client * client, uint8_t gw_id, struct mqtt_sn_data gw_addr )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

手动添加网关（Gateway），跳过常规搜索过程。

此函数手动创建一个网关（Gateway），并将其保存在库内部。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要连接的 MQTT-SN 客户端（Client）。 |
| `gw_id` | 单字节网关标识符（Gateway Identifier）。 |
| `gw_addr` | 供传输层（Transport Layer）使用的地址数据结构。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga67d69e4e3f00b31b5ea3b37fb6d653b1"></a>

### `mqtt_sn_client_deinit()`

```c
void mqtt_sn_client_deinit ( struct mqtt_sn_client * client)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

反初始化客户端（Deinitialize Client）。

这会移除所有主题（Topics）和发布项（Publishes），并反初始化传输（Transport）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要反初始化的 MQTT-SN 客户端（Client）。 |

<a id="gae6a3f7a7762653474df97364ef69fc74"></a>

### `mqtt_sn_client_init()`

```c
int mqtt_sn_client_init ( struct mqtt_sn_client * client, const struct mqtt_sn_data * client_id, struct mqtt_sn_transport * transport, mqtt_sn_evt_cb_t evt_cb, void * tx, size_t txsz, void * rx, size_t rxsz )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

初始化客户端（Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要初始化的 MQTT-SN 客户端（Client）。 |
| `client_id` | 客户端要使用的 ID。 |
| `transport` | 客户端要使用的传输（Transport）。 |
| `evt_cb` | 客户端的事件回调函数（Event Callback）。 |
| `tx` | 指向发送缓冲区（Transmit Buffer）的指针。 |
| `txsz` | 发送缓冲区（Transmit Buffer）的大小。 |
| `rx` | 指向接收缓冲区（Receive Buffer）的指针。 |
| `rxsz` | 接收缓冲区（Receive Buffer）的大小。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga8c2a525f1c30e5d5ff37180d33a76d4d"></a>

### `mqtt_sn_connect()`

```c
int mqtt_sn_connect ( struct mqtt_sn_client * client, bool will, bool clean_session )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

连接客户端（Client）。

发送失败时会重试。只能通过 `MQTT_SN_EVT_CONNECTED` 或 `MQTT_SN_EVT_DISCONNECTED` 观察结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要连接的 MQTT-SN 客户端（Client）。 |
| `will` | 指示是否发送遗嘱消息（Will Message）的标志。 |
| `clean_session` | 指示是否开始清洁会话（Clean Session）的标志。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；参数无效时为 `-EINVAL`；已有 CONNECT 正在进行时为 `-EALREADY`。

<a id="ga1a6b39984ef047f0089cea43f5378d0f"></a>

### `mqtt_sn_define_short_topic()`

```c
int mqtt_sn_define_short_topic ( struct mqtt_sn_client * client, struct mqtt_sn_data * topic_name )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

定义短主题（Short Topic）。

可在 `mqtt_sn_connect` 之前调用，因为短主题（Short Topics）永远不会被清除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 要在其上定义主题的 MQTT-SN 客户端（Client）。 |
| `[in] topic_name` | 主题名称（Topic Name），长度必须恰好为 2 字节。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gab9cba16f8ce06f606ee81e0d34deb862"></a>

### `mqtt_sn_disconnect()`

```c
int mqtt_sn_disconnect ( struct mqtt_sn_client * client)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

断开客户端（Client）连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要断开连接的 MQTT-SN 客户端（Client）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gade962a4da5311a403893ba24714dc332"></a>

### `mqtt_sn_get_topic_name()`

```c
int mqtt_sn_get_topic_name ( struct mqtt_sn_client * client, uint16_t id, struct mqtt_sn_data * topic_name )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

根据主题 ID（Topic ID）获取主题名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 使用此主题的 MQTT-SN 客户端（Client）。 |
| `[in] id` | 主题标识符（Topic Identifier）。 |
| `[out] topic_name` | 将被赋值为主题名称（Topic Name）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；主题 ID 不存在时为 `-ENOENT`；参数无效时为 `-EINVAL`。

<a id="gafa1f81168d44152ad72c5f3d1c744b49"></a>

### `mqtt_sn_input()`

```c
int mqtt_sn_input ( struct mqtt_sn_client * client)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

检查传输通道（Transport）是否有新入站数据。

应定期调用此函数，或在有充分理由认为已有数据时调用。如果客户端的传输结构体（Transport Struct）包含轮询函数（Poll Function），则此函数为非阻塞调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要检查其入站数据的 MQTT-SN 客户端（Client）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gadd0a809d7e451df55540fb7ea227fd50"></a>

### `mqtt_sn_predefine_topic()`

```c
int mqtt_sn_predefine_topic ( struct mqtt_sn_client * client, uint16_t topic_id, struct mqtt_sn_data * topic_name )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

预定义主题（Predefine Topic）。

可在 `mqtt_sn_connect` 之前调用，因为预定义主题（Predefined Topics）永远不会被清除。若在连接之后调用，则必须早于连接后首次调用 `mqtt_sn_input`，以免出现接收到的发布消息使用了尚未定义的预定义主题的竞态条件（Race Conditions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 要在其上定义主题的 MQTT-SN 客户端（Client）。 |
| `[in] topic_id` | 主题标识符（Topic Identifier）。 |
| `[in] topic_name` | 主题名称（Topic Name）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga434c3626ceaf3a9b60c5ffb75e9b5b56"></a>

### `mqtt_sn_publish()`

```c
int mqtt_sn_publish ( struct mqtt_sn_client * client, enum mqtt_sn_qos qos, struct mqtt_sn_data * topic_name, bool retain, struct mqtt_sn_data * data )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

发布一个值（Publish a Value）。

如果主题尚未向网关（Gateway）注册，库会负责注册。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要执行发布（Publish）的 MQTT-SN 客户端。 |
| `qos` | 本次发布期望的服务质量（Quality of Service，QoS）。 |
| `topic_name` | 要发布到的主题名称（Topic Name）。 |
| `retain` | 指示消息是否应由消息代理（Broker）保留（Retained）的标志。 |
| `data` | 要发布的数据。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gafdf80b1de5d1b069b2f75b2bd688416f"></a>

### `mqtt_sn_search()`

```c
int mqtt_sn_search ( struct mqtt_sn_client * client, uint8_t radius )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

启动 MQTT-SN 网关搜索（GW Search）过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要连接的 MQTT-SN 客户端（Client）。 |
| `radius` | 搜索消息（Search Message）的广播半径（Broadcast Radius）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gaf29a6339419ea02052fe53a18bb8e5ee"></a>

### `mqtt_sn_sleep()`

```c
int mqtt_sn_sleep ( struct mqtt_sn_client * client, uint16_t duration )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

将客户端置于休眠状态（Sleep State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要置于睡眠状态的 MQTT-SN 客户端。 |
| `duration` | 睡眠时长（Sleep Duration），单位为秒。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga9b481db6d39dee05e2c58d4c721fe0a5"></a>

### `mqtt_sn_subscribe()`

```c
int mqtt_sn_subscribe ( struct mqtt_sn_client * client, enum mqtt_sn_qos qos, struct mqtt_sn_data * topic_name )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

订阅给定主题（Topic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要执行订阅（Subscribe）的 MQTT-SN 客户端。 |
| `qos` | 本次订阅期望的服务质量（Quality of Service，QoS）。 |
| `topic_name` | 要订阅的主题名称（Topic Name）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga1bcd2a0f52610708bebb4b3b6d6cbf35"></a>

### `mqtt_sn_unsubscribe()`

```c
int mqtt_sn_unsubscribe ( struct mqtt_sn_client * client, enum mqtt_sn_qos qos, struct mqtt_sn_data * topic_name )
```

```c
#include <zephyr/net/mqtt_sn.h>
```

取消订阅主题（Topic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 要取消订阅（Unsubscribe）的 MQTT-SN 客户端。 |
| `qos` | 订阅时使用的服务质量（Quality of Service，QoS）。 |
| `topic_name` | 要取消订阅的主题名称（Topic Name）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga0850d89af7dd6b5d3ec2b1e1abe01d19"></a>

### `mqtt_sn_update_will_message()`

```c
int mqtt_sn_update_will_message ( struct mqtt_sn_client * client)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

向服务器发送遗嘱消息更新（Will Message Update）。

调用此函数，将 `client->will_msg` 中保存的遗嘱消息（Will Message）发送给服务器。若连接后更改了该值，应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 用于发送更新的 MQTT-SN 客户端。 |

**警告（Warning）**：警告（Warning）：遗嘱消息更新消息（Will Message Update Message）中没有消息 ID，因此无法避免竞态条件（Race Conditions）。若希望改变这一点，请参与更新版本规范的制定。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga90ced79565deb9a92be8cd3a99d808b7"></a>

### `mqtt_sn_update_will_topic()`

```c
int mqtt_sn_update_will_topic ( struct mqtt_sn_client * client)
```

```c
#include <zephyr/net/mqtt_sn.h>
```

向服务器发送遗嘱主题更新（Will Topic Update）。

调用此函数，将 `client->will_topic` 中保存的遗嘱主题（Will Topic）发送给服务器。若连接后更改了该值，应调用此函数。`client->will_retain` 和 `client->will_qos` 也将作为更新的一部分发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 用于发送更新的 MQTT-SN 客户端。 |

**警告（Warning）**：警告（Warning）：遗嘱主题更新消息（Will Topic Update Message）中没有消息 ID，因此无法避免竞态条件（Race Conditions）。若希望改变这一点，请参与更新版本规范的制定。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。


## 6.7\_原页交叉引用（Cross References）

- [mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)
- [mqtt_sn_evt_param](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md)
- [mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)
- [mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)
- [mqtt_sn_will_update](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md)
- [mqtt_sn_connect_retry](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md)
- [mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/net/mqtt_sn.h](../api_file_audio_gateway_reference/P021_zephyr__net__mqtt_sn.h_文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmqtt__sn__data_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a"></a>
<a id="ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83"></a>
<a id="gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389"></a>
<a id="gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da"></a>
<a id="gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4"></a>
<a id="gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9"></a>
<a id="ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c"></a>
<a id="ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7"></a>
<a id="ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3"></a>
<a id="ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5"></a>
<a id="ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b"></a>
<a id="ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b"></a>
<a id="ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_MFD NPM10XX 接口.md) · [返回大纲](大纲.md) · [下一章](P007_MQTT 客户端库.md)
