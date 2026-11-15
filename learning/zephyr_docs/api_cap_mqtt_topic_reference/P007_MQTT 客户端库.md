---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-7
title: MQTT 客户端库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_MQTT 客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自（Since）1.14 起提供，版本（Version）0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_mqtt_5Futf8"></a>

```c
struct mqtt_utf8
```

相关声明：[mqtt_utf8](../network_application_model_reference/P079_mqtt_utf8_结构体.md)。

UTF-8编码字符串（Strings）的抽象。

<a id="r_mqtt_5Fbinstr"></a>

```c
struct mqtt_binstr
```

相关声明：[mqtt_binstr](../network_application_model_reference/P053_mqtt_binstr_结构体.md)。

二进制字符串（Binary Strings）的抽象。

<a id="r_mqtt_5Ftopic_5Falias"></a>

```c
struct mqtt_topic_alias
```

相关声明：[mqtt_topic_alias](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md)。

别名主题（Aliased Topic）的抽象。

<a id="r_mqtt_5Ftopic"></a>

```c
struct mqtt_topic
```

相关声明：[mqtt_topic](../network_application_model_reference/P075_mqtt_topic_结构体.md)。

可订阅或发布的UTF-8编码MQTT主题（Topic）的抽象。

<a id="r_mqtt_5Futf8_5Fpair"></a>

```c
struct mqtt_utf8_pair
```

相关声明：[mqtt_utf8_pair](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md)。

UTF-8编码的MQTT字符串对（String Pair）的抽象。

<a id="r_mqtt_5Fpublish_5Fmessage"></a>

```c
struct mqtt_publish_message
```

相关声明：[mqtt_publish_message](../network_application_model_reference/P062_mqtt_publish_message_结构体.md)。

发布消息（Publish Message）的参数。

<a id="r_mqtt_5Fconnack_5Fparam"></a>

```c
struct mqtt_connack_param
```

相关声明：[mqtt_connack_param](../network_application_model_reference/P056_mqtt_connack_param_结构体.md)。

连接确认（CONNACK）的参数。

<a id="r_mqtt_5Fcommon_5Fack_5Fproperties"></a>

```c
struct mqtt_common_ack_properties
```

相关声明：[mqtt_common_ack_properties](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md)。

所有确认类型消息（ACK-Type Messages）共享的通用MQTT 5.0属性。

<a id="r_mqtt_5Fpuback_5Fparam"></a>

```c
struct mqtt_puback_param
```

相关声明：[mqtt_puback_param](../network_application_model_reference/P060_mqtt_puback_param_结构体.md)。

MQTT发布确认（PUBACK）的参数。

<a id="r_mqtt_5Fpubrec_5Fparam"></a>

```c
struct mqtt_pubrec_param
```

相关声明：[mqtt_pubrec_param](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md)。

MQTT发布已接收（PUBREC）的参数。

<a id="r_mqtt_5Fpubrel_5Fparam"></a>

```c
struct mqtt_pubrel_param
```

相关声明：[mqtt_pubrel_param](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md)。

MQTT发布释放（PUBREL）的参数。

<a id="r_mqtt_5Fpubcomp_5Fparam"></a>

```c
struct mqtt_pubcomp_param
```

相关声明：[mqtt_pubcomp_param](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md)。

MQTT发布完成（PUBCOMP）的参数。

<a id="r_mqtt_5Fsuback_5Fparam"></a>

```c
struct mqtt_suback_param
```

相关声明：[mqtt_suback_param](../network_application_model_reference/P073_mqtt_suback_param_结构体.md)。

MQTT订阅确认（SUBACK）的参数。

<a id="r_mqtt_5Funsuback_5Fparam"></a>

```c
struct mqtt_unsuback_param
```

相关声明：[mqtt_unsuback_param](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md)。

MQTT取消订阅确认（UNSUBACK）的参数。

<a id="r_mqtt_5Fpublish_5Fparam"></a>

```c
struct mqtt_publish_param
```

相关声明：[mqtt_publish_param](../network_application_model_reference/P063_mqtt_publish_param_结构体.md)。

发布消息（PUBLISH）的参数。

<a id="r_mqtt_5Fsubscription_5Flist"></a>

```c
struct mqtt_subscription_list
```

相关声明：[mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)。

订阅/取消订阅消息（Subscribe / Unsubscribe Message）的参数。

<a id="r_mqtt_5Fdisconnect_5Fparam"></a>

```c
struct mqtt_disconnect_param
```

相关声明：[mqtt_disconnect_param](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md)。

断开连接消息（Disconnect Message）的参数。

<a id="r_mqtt_5Fauth_5Fparam"></a>

```c
struct mqtt_auth_param
```

相关声明：[mqtt_auth_param](../network_application_model_reference/P052_mqtt_auth_param_结构体.md)。

认证消息（Auth Message）的参数。

<a id="r_mqtt_5Fevt_5Fparam"></a>

```c
union mqtt_evt_param
```

相关声明：[mqtt_evt_param](../network_application_model_reference/P091_mqtt_evt_param_联合体.md)。

定义随异步事件一起通知应用的事件参数（Event Parameters）。

<a id="r_mqtt_5Fevt"></a>

```c
struct mqtt_evt
```

相关声明：[mqtt_evt](../network_application_model_reference/P058_mqtt_evt_结构体.md)。

定义通知应用的MQTT异步事件（Asynchronous Event）。

<a id="r_mqtt_5Fsec_5Fconfig"></a>

```c
struct mqtt_sec_config
```

相关声明：[mqtt_sec_config](../network_application_model_reference/P066_mqtt_sec_config_结构体.md)。

安全MQTT传输（Secure MQTT Transports）的TLS配置。

<a id="r_mqtt_5Ftransport"></a>

```c
struct mqtt_transport
```

相关声明：[mqtt_transport](../network_application_model_reference/P077_mqtt_transport_结构体.md)。

MQTT传输专用数据（Transport Specific Data）。

<a id="r_mqtt_5Finternal"></a>

```c
struct mqtt_internal
```

相关声明：[mqtt_internal](../network_application_model_reference/P059_mqtt_internal_结构体.md)。

MQTT内部状态（Internal State）。

<a id="r_mqtt_5Fclient"></a>

```c
struct mqtt_client
```

相关声明：[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

用于维护客户端相关信息的MQTT客户端（Client）定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaeaa4fcf581c7d6be755f9a053a3b488c"></a>

```c
#define MQTT_UTF8_LITERAL(literal)
```

相关声明：[MQTT_UTF8_LITERAL](#gaeaa4fcf581c7d6be755f9a053a3b488c)。

根据 C 字符串字面量（Literal String）初始化 UTF-8 编码字符串。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_gabdf01ededb62ceb4c1608a64cb718a8c"></a>

```c
typedef void(* mqtt_evt_cb_t) (struct mqtt_client *client, const struct mqtt_evt *evt)
```

相关声明：[mqtt_evt_cb_t](#gabdf01ededb62ceb4c1608a64cb718a8c)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_evt](../network_application_model_reference/P058_mqtt_evt_结构体.md)。

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga0071fe013b9920711456ef51cc3e6d91"></a>

```c
enum mqtt_evt_type { MQTT_EVT_CONNACK , MQTT_EVT_DISCONNECT , MQTT_EVT_PUBLISH , MQTT_EVT_PUBACK , MQTT_EVT_PUBREC , MQTT_EVT_PUBREL , MQTT_EVT_PUBCOMP , MQTT_EVT_SUBACK , MQTT_EVT_UNSUBACK , MQTT_EVT_PINGRESP , MQTT_EVT_AUTH }
```

相关声明：[mqtt_evt_type](#ga0071fe013b9920711456ef51cc3e6d91)、[MQTT_EVT_CONNACK](#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3)、[MQTT_EVT_DISCONNECT](#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032)、[MQTT_EVT_PUBLISH](#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9)、[MQTT_EVT_PUBACK](#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de)、[MQTT_EVT_PUBREC](#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87)、[MQTT_EVT_PUBREL](#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2)、[MQTT_EVT_PUBCOMP](#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8)、[MQTT_EVT_SUBACK](#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb)、[MQTT_EVT_UNSUBACK](#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2)、[MQTT_EVT_PINGRESP](#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)、[MQTT_EVT_AUTH](#gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde)。

模块通过应用注册的回调，向应用通知 MQTT 异步事件（Asynchronous Events）。

<a id="r_ga90d152a4b0986e9a07a12c7c56f5e2a0"></a>

```c
enum mqtt_version { MQTT_VERSION_3_1_0 = 3 , MQTT_VERSION_3_1_1 = 4 , MQTT_VERSION_5_0 = 5 }
```

相关声明：[mqtt_version](#ga90d152a4b0986e9a07a12c7c56f5e2a0)、[MQTT_VERSION_3_1_0](#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7)、[MQTT_VERSION_3_1_1](#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e)、[MQTT_VERSION_5_0](#gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f)。

MQTT 版本协议级别（Version Protocol Level）。

<a id="r_ga396015e492b0fee8da37c7168d9cdb33"></a>

```c
enum mqtt_qos { MQTT_QOS_0_AT_MOST_ONCE = 0x00 , MQTT_QOS_1_AT_LEAST_ONCE = 0x01 , MQTT_QOS_2_EXACTLY_ONCE = 0x02 }
```

相关声明：[mqtt_qos](#ga396015e492b0fee8da37c7168d9cdb33)、[MQTT_QOS_0_AT_MOST_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e)、[MQTT_QOS_1_AT_LEAST_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d)、[MQTT_QOS_2_EXACTLY_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117)。

MQTT 服务质量类型（Quality of Service，QoS）。

<a id="r_ga25ba4f0870fc2c01ee5fc2c06bd898c8"></a>

```c
enum mqtt_retain_handling { MQTT_RH_0_SEND_AT_SUBSCRIBE = 0x00 , MQTT_RH_1_SEND_IF_NEW = 0x01 , MQTT_RH_2_DO_NOT_SEND = 0x02 }
```

相关声明：[mqtt_retain_handling](#ga25ba4f0870fc2c01ee5fc2c06bd898c8)、[MQTT_RH_0_SEND_AT_SUBSCRIBE](#gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc)、[MQTT_RH_1_SEND_IF_NEW](#gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d)、[MQTT_RH_2_DO_NOT_SEND](#gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4)。

MQTT 5.0 保留消息处理选项（Retain Handling Options）。

<a id="r_gaa17b38ed9c7e65f3e01ad906b24bb618"></a>

```c
enum mqtt_conn_return_code { MQTT_CONNECTION_ACCEPTED = 0x00 , MQTT_UNACCEPTABLE_PROTOCOL_VERSION = 0x01 , MQTT_IDENTIFIER_REJECTED = 0x02 , MQTT_SERVER_UNAVAILABLE = 0x03 , MQTT_BAD_USER_NAME_OR_PASSWORD = 0x04 , MQTT_NOT_AUTHORIZED = 0x05 }
```

相关声明：[mqtt_conn_return_code](#gaa17b38ed9c7e65f3e01ad906b24bb618)、[MQTT_CONNECTION_ACCEPTED](#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050)、[MQTT_UNACCEPTABLE_PROTOCOL_VERSION](#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744)、[MQTT_IDENTIFIER_REJECTED](#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141)、[MQTT_SERVER_UNAVAILABLE](#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3)、[MQTT_BAD_USER_NAME_OR_PASSWORD](#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134)、[MQTT_NOT_AUTHORIZED](#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb)。

MQTT 3.1 连接确认（CONNACK）返回码。

<a id="r_gae4c3fb5313addb72961ff578113d183a"></a>

```c
enum mqtt_connack_reason_code { MQTT_CONNACK_SUCCESS = 0 , MQTT_CONNACK_UNSPECIFIED_ERROR = 128 , MQTT_CONNACK_MALFORMED_PACKET = 129 , MQTT_CONNACK_PROTOCOL_ERROR = 130 , MQTT_CONNACK_IMPL_SPECIFIC_ERROR = 131 , MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR = 132 , MQTT_CONNACK_CLIENT_ID_NOT_VALID = 133 , MQTT_CONNACK_BAD_USERNAME_OR_PASS = 134 , MQTT_CONNACK_NOT_AUTHORIZED = 135 , MQTT_CONNACK_SERVER_UNAVAILABLE = 136 , MQTT_CONNACK_SERVER_BUSY = 137 , MQTT_CONNACK_BANNED = 138 , MQTT_CONNACK_BAD_AUTH_METHOD = 140 , MQTT_CONNACK_TOPIC_NAME_INVALID = 144 , MQTT_CONNACK_PACKET_TOO_LARGE = 149 , MQTT_CONNACK_QUOTA_EXCEEDED = 151 , MQTT_CONNACK_PAYLOAD_FORMAT_INVALID = 153 , MQTT_CONNACK_RETAIN_NOT_SUPPORTED = 154 , MQTT_CONNACK_QOS_NOT_SUPPORTED = 155 , MQTT_CONNACK_USE_ANOTHER_SERVER = 156 , MQTT_CONNACK_SERVER_MOVED = 157 , MQTT_CONNACK_CONNECTION_RATE_EXCEEDED = 159 }
```

相关声明：[mqtt_connack_reason_code](#gae4c3fb5313addb72961ff578113d183a)、[MQTT_CONNACK_SUCCESS](#ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7)、[MQTT_CONNACK_UNSPECIFIED_ERROR](#ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989)、[MQTT_CONNACK_MALFORMED_PACKET](#ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0)、[MQTT_CONNACK_PROTOCOL_ERROR](#ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc)、[MQTT_CONNACK_IMPL_SPECIFIC_ERROR](#ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee)、[MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR](#ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816)、[MQTT_CONNACK_CLIENT_ID_NOT_VALID](#ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f)、[MQTT_CONNACK_BAD_USERNAME_OR_PASS](#ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd)、[MQTT_CONNACK_NOT_AUTHORIZED](#ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e)、[MQTT_CONNACK_SERVER_UNAVAILABLE](#ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa)、[MQTT_CONNACK_SERVER_BUSY](#ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8)、[MQTT_CONNACK_BANNED](#ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33)、[MQTT_CONNACK_BAD_AUTH_METHOD](#ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4)、[MQTT_CONNACK_TOPIC_NAME_INVALID](#ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5)、[MQTT_CONNACK_PACKET_TOO_LARGE](#ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040)、[MQTT_CONNACK_QUOTA_EXCEEDED](#ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f)、[MQTT_CONNACK_PAYLOAD_FORMAT_INVALID](#ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c)、[MQTT_CONNACK_RETAIN_NOT_SUPPORTED](#ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956)、[MQTT_CONNACK_QOS_NOT_SUPPORTED](#ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0)、[MQTT_CONNACK_USE_ANOTHER_SERVER](#ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c)、[MQTT_CONNACK_SERVER_MOVED](#ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa)、[MQTT_CONNACK_CONNECTION_RATE_EXCEEDED](#ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e)。

MQTT 5.0 连接确认原因码（CONNACK Reason Codes），见 MQTT 5.0 第 3.2.2.2 节。

<a id="r_gaca1e61c8b14b75544e253cea355274a8"></a>

```c
enum mqtt_suback_return_code { MQTT_SUBACK_SUCCESS_QoS_0 = 0x00 , MQTT_SUBACK_SUCCESS_QoS_1 = 0x01 , MQTT_SUBACK_SUCCESS_QoS_2 = 0x02 , MQTT_SUBACK_FAILURE = 0x80 }
```

相关声明：[mqtt_suback_return_code](#gaca1e61c8b14b75544e253cea355274a8)、[MQTT_SUBACK_SUCCESS_QoS_0](#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01)、[MQTT_SUBACK_SUCCESS_QoS_1](#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c)、[MQTT_SUBACK_SUCCESS_QoS_2](#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b)、[MQTT_SUBACK_FAILURE](#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7)。

MQTT 订阅确认（SUBACK）返回码。

<a id="r_gaaf563f26ca66841145643a657119d780"></a>

```c
enum mqtt_disconnect_reason_code { MQTT_DISCONNECT_NORMAL = 0 , MQTT_DISCONNECT_WITH_WILL_MSG = 4 , MQTT_DISCONNECT_UNSPECIFIED_ERROR = 128 , MQTT_DISCONNECT_MALFORMED_PACKET = 129 , MQTT_DISCONNECT_PROTOCOL_ERROR = 130 , MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR = 131 , MQTT_DISCONNECT_NOT_AUTHORIZED = 135 , MQTT_DISCONNECT_SERVER_BUSY = 137 , MQTT_DISCONNECT_SERVER_SHUTTING_DOWN = 139 , MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT = 141 , MQTT_DISCONNECT_SESSION_TAKE_OVER = 142 , MQTT_DISCONNECT_TOPIC_FILTER_INVALID = 143 , MQTT_DISCONNECT_TOPIC_NAME_INVALID = 144 , MQTT_DISCONNECT_RECV_MAX_EXCEEDED = 147 , MQTT_DISCONNECT_TOPIC_ALIAS_INVALID = 148 , MQTT_DISCONNECT_PACKET_TOO_LARGE = 149 , MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH = 150 , MQTT_DISCONNECT_QUOTA_EXCEEDED = 151 , MQTT_DISCONNECT_ADMIN_ACTION = 152 , MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID = 153 , MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED = 154 , MQTT_DISCONNECT_QOS_NOT_SUPPORTED = 155 , MQTT_DISCONNECT_USE_ANOTHER_SERVER = 156 , MQTT_DISCONNECT_SERVER_MOVED = 157 , MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED = 158 , MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED = 159 , MQTT_DISCONNECT_MAX_CONNECT_TIME = 160 , MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED = 161 , MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED = 162 }
```

相关声明：[mqtt_disconnect_reason_code](#gaaf563f26ca66841145643a657119d780)、[MQTT_DISCONNECT_NORMAL](#ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a)、[MQTT_DISCONNECT_WITH_WILL_MSG](#ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b)、[MQTT_DISCONNECT_UNSPECIFIED_ERROR](#ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c)、[MQTT_DISCONNECT_MALFORMED_PACKET](#ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa)、[MQTT_DISCONNECT_PROTOCOL_ERROR](#ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec)、[MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR](#ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c)、[MQTT_DISCONNECT_NOT_AUTHORIZED](#ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78)、[MQTT_DISCONNECT_SERVER_BUSY](#ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86)、[MQTT_DISCONNECT_SERVER_SHUTTING_DOWN](#ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d)、[MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT](#ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603)、[MQTT_DISCONNECT_SESSION_TAKE_OVER](#ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf)、[MQTT_DISCONNECT_TOPIC_FILTER_INVALID](#ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a)、[MQTT_DISCONNECT_TOPIC_NAME_INVALID](#ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610)、[MQTT_DISCONNECT_RECV_MAX_EXCEEDED](#ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0)、[MQTT_DISCONNECT_TOPIC_ALIAS_INVALID](#ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c)、[MQTT_DISCONNECT_PACKET_TOO_LARGE](#ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b)、[MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH](#ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194)、[MQTT_DISCONNECT_QUOTA_EXCEEDED](#ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5)、[MQTT_DISCONNECT_ADMIN_ACTION](#ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173)、[MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID](#ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a)、[MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED](#ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65)、[MQTT_DISCONNECT_QOS_NOT_SUPPORTED](#ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d)、[MQTT_DISCONNECT_USE_ANOTHER_SERVER](#ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6)、[MQTT_DISCONNECT_SERVER_MOVED](#ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1)、[MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED](#ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98)、[MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED](#ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293)、[MQTT_DISCONNECT_MAX_CONNECT_TIME](#ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c)、[MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED](#ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4)、[MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED](#ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4)。

MQTT 断开原因码（Disconnect Reason Codes），见 MQTT 5.0 第 3.14.2.1 节。

<a id="r_gacdbeff0450bbcd438cdf35cd543fc6d6"></a>

```c
enum mqtt_auth_reason_code { MQTT_AUTH_SUCCESS = 0 , MQTT_AUTH_CONTINUE_AUTHENTICATION = 24 , MQTT_AUTH_RE_AUTHENTICATE = 25 }
```

相关声明：[mqtt_auth_reason_code](#gacdbeff0450bbcd438cdf35cd543fc6d6)、[MQTT_AUTH_SUCCESS](#ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60)、[MQTT_AUTH_CONTINUE_AUTHENTICATION](#ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863)、[MQTT_AUTH_RE_AUTHENTICATE](#ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a)。

MQTT 认证原因码（Authenticate Reason Codes），见 MQTT 5.0 第 3.15.2.1 节。

<a id="r_gaffc2c3078004cf8d24935be086ad63b4"></a>

```c
enum mqtt_transport_type { MQTT_TRANSPORT_NON_SECURE , MQTT_TRANSPORT_NUM }
```

相关声明：[mqtt_transport_type](#gaffc2c3078004cf8d24935be086ad63b4)、[MQTT_TRANSPORT_NON_SECURE](#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a)、[MQTT_TRANSPORT_NUM](#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)。

MQTT 传输类型（Transport Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gad1376509ae7c946c840d103d8b59e9a1"></a>

```c
void mqtt_client_init (struct mqtt_client *client)
```

相关声明：[mqtt_client_init](#gad1376509ae7c946c840d103d8b59e9a1)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

初始化客户端实例（Client Instance）。

<a id="r_gad936f28553cb2e771a843512b0a315fa"></a>

```c
int mqtt_connect (struct mqtt_client *client)
```

相关声明：[mqtt_connect](#gad936f28553cb2e771a843512b0a315fa)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

请求新的 MQTT 客户端连接（Client Connection）的 API。

<a id="r_ga57745efa1bf6fbdf7eb1b3f01623e4c7"></a>

```c
int mqtt_publish (struct mqtt_client *client, const struct mqtt_publish_param *param)
```

相关声明：[mqtt_publish](#ga57745efa1bf6fbdf7eb1b3f01623e4c7)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_publish_param](../network_application_model_reference/P063_mqtt_publish_param_结构体.md)。

向主题（Topics）发布消息的 API。

<a id="r_gae9069fceec2c018e64cc6beb16aa055c"></a>

```c
int mqtt_publish_qos1_ack (struct mqtt_client *client, const struct mqtt_puback_param *param)
```

相关声明：[mqtt_publish_qos1_ack](#gae9069fceec2c018e64cc6beb16aa055c)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_puback_param](../network_application_model_reference/P060_mqtt_puback_param_结构体.md)。

客户端收到 QoS1 发布消息（Publish Message）后发送确认的 API。

<a id="r_gacbe41b83d9c0676d0d4cf01dd91765eb"></a>

```c
int mqtt_publish_qos2_receive (struct mqtt_client *client, const struct mqtt_pubrec_param *param)
```

相关声明：[mqtt_publish_qos2_receive](#gacbe41b83d9c0676d0d4cf01dd91765eb)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubrec_param](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md)。

客户端收到 QoS2 发布消息（Publish Message）后发送确认的 API。

<a id="r_ga6c952ed014f78774096bfb6099794803"></a>

```c
int mqtt_publish_qos2_release (struct mqtt_client *client, const struct mqtt_pubrel_param *param)
```

相关声明：[mqtt_publish_qos2_release](#ga6c952ed014f78774096bfb6099794803)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubrel_param](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md)。

客户端请求释放 QoS2 发布消息（Publish Message）的 API。

<a id="r_ga2b17999e845d613f5b0b20015b8204f3"></a>

```c
int mqtt_publish_qos2_complete (struct mqtt_client *client, const struct mqtt_pubcomp_param *param)
```

相关声明：[mqtt_publish_qos2_complete](#ga2b17999e845d613f5b0b20015b8204f3)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubcomp_param](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md)。

客户端收到 QoS2 发布释放消息（Publish Release Message）后发送确认的 API。

<a id="r_ga40d226b891b8f62f2c486bbb11ce9678"></a>

```c
int mqtt_subscribe (struct mqtt_client *client, const struct mqtt_subscription_list *param)
```

相关声明：[mqtt_subscribe](#ga40d226b891b8f62f2c486bbb11ce9678)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)。

在连接上请求订阅一个或多个主题（Topics）的 API。

<a id="r_ga4ff43a198e93e332b5553a4d0b59261d"></a>

```c
int mqtt_unsubscribe (struct mqtt_client *client, const struct mqtt_subscription_list *param)
```

相关声明：[mqtt_unsubscribe](#ga4ff43a198e93e332b5553a4d0b59261d)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)。

在连接上请求取消订阅一个或多个主题（Topics）的 API。

<a id="r_gad1d549d37b69a61e1bf8d9d213e02ca8"></a>

```c
int mqtt_ping (struct mqtt_client *client)
```

相关声明：[mqtt_ping](#gad1d549d37b69a61e1bf8d9d213e02ca8)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

发送 MQTT ping 的 API。

<a id="r_ga0bc7d91da88c2fbc25108d89ce4318c4"></a>

```c
int mqtt_disconnect (struct mqtt_client *client, const struct mqtt_disconnect_param *param)
```

相关声明：[mqtt_disconnect](#ga0bc7d91da88c2fbc25108d89ce4318c4)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_disconnect_param](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md)。

断开 MQTT 连接（Connection）的 API。

<a id="r_gad4d870f91a7d594c3a7325ab6de87a02"></a>

```c
int mqtt_auth (struct mqtt_client *client, const struct mqtt_auth_param *param)
```

相关声明：[mqtt_auth](#gad4d870f91a7d594c3a7325ab6de87a02)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_auth_param](../network_application_model_reference/P052_mqtt_auth_param_结构体.md)。

向服务器发送认证数据包（Authentication Packet）的 API。

<a id="r_gafb2df41fad7c318f9fe75919919139bd"></a>

```c
int mqtt_abort (struct mqtt_client *client)
```

相关声明：[mqtt_abort](#gafb2df41fad7c318f9fe75919919139bd)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

中止 MQTT 连接（Abort Connection）的 API。

<a id="r_ga8b87710d01076c8e51b1a75634168269"></a>

```c
int mqtt_live (struct mqtt_client *client)
```

相关声明：[mqtt_live](#ga8b87710d01076c8e51b1a75634168269)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

应定期调用此 API，使客户端能够在需要时发送 ping 请求（Ping Requests）以保持连接存活。

<a id="r_gaa16bf7b0597ad00c4a3943235579e86b"></a>

```c
int mqtt_keepalive_time_left (const struct mqtt_client *client)
```

相关声明：[mqtt_keepalive_time_left](#gaa16bf7b0597ad00c4a3943235579e86b)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

确定何时应发送下一条保活消息（Keep Alive Message）的辅助函数。

<a id="r_ga2dbc3c158d63a6f57b362be94c22660a"></a>

```c
int mqtt_input (struct mqtt_client *client)
```

相关声明：[mqtt_input](#ga2dbc3c158d63a6f57b362be94c22660a)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

接收入站 MQTT 数据包（Incoming MQTT Packet）。

<a id="r_ga3559cdd6093d75c6fe6792ec2a453172"></a>

```c
int mqtt_read_publish_payload (struct mqtt_client *client, void *buffer, size_t length)
```

相关声明：[mqtt_read_publish_payload](#ga3559cdd6093d75c6fe6792ec2a453172)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

读取所收到 PUBLISH 消息的载荷（Payload）。

<a id="r_ga05213aceaa9e9cbbfaa9bab7a78b3d25"></a>

```c
int mqtt_read_publish_payload_blocking (struct mqtt_client *client, void *buffer, size_t length)
```

相关声明：[mqtt_read_publish_payload_blocking](#ga05213aceaa9e9cbbfaa9bab7a78b3d25)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version）。

<a id="r_ga31823965ec34a253793b40b50e800417"></a>

```c
int mqtt_readall_publish_payload (struct mqtt_client *client, uint8_t *buffer, size_t length)
```

相关声明：[mqtt_readall_publish_payload](#ga31823965ec34a253793b40b50e800417)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version），运行直到读取到所需字节数。

## 7.6\_详细说明（Detailed Documentation）

<a id="gaeaa4fcf581c7d6be755f9a053a3b488c"></a>

### `MQTT_UTF8_LITERAL`

```c
#define MQTT_UTF8_LITERAL ( literal)
```

```c
#include <zephyr/net/mqtt.h>
```

展开值（Value）：

```c
((struct mqtt_utf8) {literal, sizeof(literal) - 1})
```

根据 C 字符串字面量（Literal String）初始化 UTF-8 编码字符串。

用法如下：

```c
struct mqtt_utf8 password = MQTT_UTF8_LITERAL("my_pass");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] literal` | 用于生成 `mqtt_utf8` 对象的字符串字面量（Literal String）。 |

<a id="gabdf01ededb62ceb4c1608a64cb718a8c"></a>

### `mqtt_evt_cb_t`

```c
typedef void(* mqtt_evt_cb_t) (struct mqtt_client *client, const struct mqtt_evt *evt)
```

```c
#include <zephyr/net/mqtt.h>
```

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识接收此事件通知的客户端（Client）。 |
| `[in] evt` | 事件说明，以及结果和关联参数（如有）。 |

<a id="gacdbeff0450bbcd438cdf35cd543fc6d6"></a>

### `mqtt_auth_reason_code`

```c
enum mqtt_auth_reason_code
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 认证原因码（Authenticate Reason Codes），见 MQTT 5.0 第 3.15.2.1 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_AUTH_SUCCESS` |  |
| `MQTT_AUTH_CONTINUE_AUTHENTICATION` |  |
| `MQTT_AUTH_RE_AUTHENTICATE` |  |

<a id="gaa17b38ed9c7e65f3e01ad906b24bb618"></a>

### `mqtt_conn_return_code`

```c
enum mqtt_conn_return_code
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 3.1 连接确认（CONNACK）返回码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_CONNECTION_ACCEPTED` | 连接已接受（Connection Accepted）。 |
| `MQTT_UNACCEPTABLE_PROTOCOL_VERSION` | 服务器不支持客户端请求的 MQTT 协议级别（Protocol Level）。 |
| `MQTT_IDENTIFIER_REJECTED` | 客户端标识符（Client Identifier）是正确的 UTF-8，但服务器不允许使用。 |
| `MQTT_SERVER_UNAVAILABLE` | 网络连接已建立，但 MQTT 服务不可用。 |
| `MQTT_BAD_USER_NAME_OR_PASSWORD` | 用户名或密码中的数据格式错误（Malformed）。 |
| `MQTT_NOT_AUTHORIZED` | 客户端未获准连接（Not Authorized）。 |

<a id="gae4c3fb5313addb72961ff578113d183a"></a>

### `mqtt_connack_reason_code`

```c
enum mqtt_connack_reason_code
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 5.0 连接确认原因码（CONNACK Reason Codes），见 MQTT 5.0 第 3.2.2.2 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_CONNACK_SUCCESS` |  |
| `MQTT_CONNACK_UNSPECIFIED_ERROR` |  |
| `MQTT_CONNACK_MALFORMED_PACKET` |  |
| `MQTT_CONNACK_PROTOCOL_ERROR` |  |
| `MQTT_CONNACK_IMPL_SPECIFIC_ERROR` |  |
| `MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR` |  |
| `MQTT_CONNACK_CLIENT_ID_NOT_VALID` |  |
| `MQTT_CONNACK_BAD_USERNAME_OR_PASS` |  |
| `MQTT_CONNACK_NOT_AUTHORIZED` |  |
| `MQTT_CONNACK_SERVER_UNAVAILABLE` |  |
| `MQTT_CONNACK_SERVER_BUSY` |  |
| `MQTT_CONNACK_BANNED` |  |
| `MQTT_CONNACK_BAD_AUTH_METHOD` |  |
| `MQTT_CONNACK_TOPIC_NAME_INVALID` |  |
| `MQTT_CONNACK_PACKET_TOO_LARGE` |  |
| `MQTT_CONNACK_QUOTA_EXCEEDED` |  |
| `MQTT_CONNACK_PAYLOAD_FORMAT_INVALID` |  |
| `MQTT_CONNACK_RETAIN_NOT_SUPPORTED` |  |
| `MQTT_CONNACK_QOS_NOT_SUPPORTED` |  |
| `MQTT_CONNACK_USE_ANOTHER_SERVER` |  |
| `MQTT_CONNACK_SERVER_MOVED` |  |
| `MQTT_CONNACK_CONNECTION_RATE_EXCEEDED` |  |

<a id="gaaf563f26ca66841145643a657119d780"></a>

### `mqtt_disconnect_reason_code`

```c
enum mqtt_disconnect_reason_code
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 断开原因码（Disconnect Reason Codes），见 MQTT 5.0 第 3.14.2.1 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_DISCONNECT_NORMAL` |  |
| `MQTT_DISCONNECT_WITH_WILL_MSG` |  |
| `MQTT_DISCONNECT_UNSPECIFIED_ERROR` |  |
| `MQTT_DISCONNECT_MALFORMED_PACKET` |  |
| `MQTT_DISCONNECT_PROTOCOL_ERROR` |  |
| `MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR` |  |
| `MQTT_DISCONNECT_NOT_AUTHORIZED` |  |
| `MQTT_DISCONNECT_SERVER_BUSY` |  |
| `MQTT_DISCONNECT_SERVER_SHUTTING_DOWN` |  |
| `MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT` |  |
| `MQTT_DISCONNECT_SESSION_TAKE_OVER` |  |
| `MQTT_DISCONNECT_TOPIC_FILTER_INVALID` |  |
| `MQTT_DISCONNECT_TOPIC_NAME_INVALID` |  |
| `MQTT_DISCONNECT_RECV_MAX_EXCEEDED` |  |
| `MQTT_DISCONNECT_TOPIC_ALIAS_INVALID` |  |
| `MQTT_DISCONNECT_PACKET_TOO_LARGE` |  |
| `MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH` |  |
| `MQTT_DISCONNECT_QUOTA_EXCEEDED` |  |
| `MQTT_DISCONNECT_ADMIN_ACTION` |  |
| `MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID` |  |
| `MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED` |  |
| `MQTT_DISCONNECT_QOS_NOT_SUPPORTED` |  |
| `MQTT_DISCONNECT_USE_ANOTHER_SERVER` |  |
| `MQTT_DISCONNECT_SERVER_MOVED` |  |
| `MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED` |  |
| `MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED` |  |
| `MQTT_DISCONNECT_MAX_CONNECT_TIME` |  |
| `MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED` |  |
| `MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED` |  |

<a id="ga0071fe013b9920711456ef51cc3e6d91"></a>

### `mqtt_evt_type`

```c
enum mqtt_evt_type
```

```c
#include <zephyr/net/mqtt.h>
```

模块通过应用注册的回调，向应用通知 MQTT 异步事件（Asynchronous Events）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_EVT_CONNACK` | 连接请求确认（Acknowledgment of Connection Request）。随事件提供的结果表示连接失败还是成功。 |
| `MQTT_EVT_DISCONNECT` | 断开连接事件（Disconnection Event）。收到客户端的此事件后，MQTT 客户端引用（Client Reference）不再有效。 |
| `MQTT_EVT_PUBLISH` | 当消息发布到客户端已订阅的主题（Topic）时，收到发布事件（Publish Event）。注（Note）：PUBLISH 事件结构体只包含载荷大小，应忽略载荷数据参数。必须使用 `mqtt_read_publish_payload` 函数手动读取载荷内容。 |
| `MQTT_EVT_PUBACK` | 对 QoS 1 已发布消息的确认（Acknowledgment）。 |
| `MQTT_EVT_PUBREC` | 对 QoS 2 已发布消息的接收确认（Reception Confirmation）。 |
| `MQTT_EVT_PUBREL` | QoS 2 已发布消息的释放（Release）。 |
| `MQTT_EVT_PUBCOMP` | 对 QoS 2 发布释放消息（Publish Release Message）的确认。 |
| `MQTT_EVT_SUBACK` | 对订阅请求（Subscribe Request）的确认。 |
| `MQTT_EVT_UNSUBACK` | 对取消订阅请求（Unsubscribe Request）的确认。 |
| `MQTT_EVT_PINGRESP` | 来自服务器的 Ping 响应（Ping Response）。 |
| `MQTT_EVT_AUTH` | 从服务器收到认证分组（Authentication Packet）。仅适用于 MQTT 5.0。 |

说明（Note）：PUBLISH事件结构仅包含载荷大小，应忽略载荷数据参数。必须使用mqtt_read_publish_payload函数手动读取载荷内容（Payload Content）。

<a id="ga396015e492b0fee8da37c7168d9cdb33"></a>

### `mqtt_qos`

```c
enum mqtt_qos
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 服务质量类型（Quality of Service，QoS）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_QOS_0_AT_MOST_ONCE` | 最低服务质量（Quality of Service，QoS）；发布消息无需确认。 |
| `MQTT_QOS_1_AT_LEAST_ONCE` | 中等服务质量（QoS）；期望对发布消息进行确认，允许重复消息。 |
| `MQTT_QOS_2_EXACTLY_ONCE` | 最高服务质量（QoS）；期望进行确认，且消息只能发布一次。客户端发出 `PUBREL` 之前，不会向关注该消息的接收方发布消息。 |

<a id="ga25ba4f0870fc2c01ee5fc2c06bd898c8"></a>

### `mqtt_retain_handling`

```c
enum mqtt_retain_handling
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 5.0 保留消息处理选项（Retain Handling Options）。

MQTT 5.0，第 3.3.1.3 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_RH_0_SEND_AT_SUBSCRIBE` | 订阅时，向客户端发送与订阅主题过滤器（Topic Filter）匹配的保留消息（Retained Messages）。 |
| `MQTT_RH_1_SEND_IF_NEW` | 如果此前不存在该订阅，则向客户端发送与其主题过滤器（Topic Filter）匹配的所有保留消息（Retained Messages）；如果该订阅已存在，则不发送保留消息。 |
| `MQTT_RH_2_DO_NOT_SEND` | 订阅时不发送保留消息（Retained Messages）。 |

<a id="gaca1e61c8b14b75544e253cea355274a8"></a>

### `mqtt_suback_return_code`

```c
enum mqtt_suback_return_code
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 订阅确认（SUBACK）返回码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_SUBACK_SUCCESS_QoS_0` | QoS 0 订阅成功。 |
| `MQTT_SUBACK_SUCCESS_QoS_1` | QoS 1 订阅成功。 |
| `MQTT_SUBACK_SUCCESS_QoS_2` | QoS 2 订阅成功。 |
| `MQTT_SUBACK_FAILURE` | 主题（Topic）订阅失败。 |

<a id="gaffc2c3078004cf8d24935be086ad63b4"></a>

### `mqtt_transport_type`

```c
enum mqtt_transport_type
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 传输类型（Transport Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_TRANSPORT_NON_SECURE` | MQTT 连接使用非安全 TCP 传输（Non-Secure TCP Transport）。 |
| `MQTT_TRANSPORT_NUM` | 不得用作传输类型（Transport Type）。用于标记可能的传输类型最大数量（Maximum Transport Types）。 |

<a id="ga90d152a4b0986e9a07a12c7c56f5e2a0"></a>

### `mqtt_version`

```c
enum mqtt_version
```

```c
#include <zephyr/net/mqtt.h>
```

MQTT 版本协议级别（Version Protocol Level）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MQTT_VERSION_3_1_0` | 3.1.0 版本的协议级别（Protocol Level）。 |
| `MQTT_VERSION_3_1_1` | 3.1.1 版本的协议级别（Protocol Level）。 |
| `MQTT_VERSION_5_0` | 5.0 版本的协议级别（Protocol Level）。 |

<a id="gafb2df41fad7c318f9fe75919919139bd"></a>

### `mqtt_abort()`

```c
int mqtt_abort ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

中止 MQTT 连接（Abort Connection）的 API。

这会关闭对应传输，而不会在 MQTT 层通过断开连接消息（Disconnect Message）优雅关闭连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gad4d870f91a7d594c3a7325ab6de87a02"></a>

### `mqtt_auth()`

```c
int mqtt_auth ( struct mqtt_client * client, const struct mqtt_auth_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

向服务器发送认证数据包（Authentication Packet）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 认证消息（Auth Message）所用参数，不得为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gad1376509ae7c946c840d103d8b59e9a1"></a>

### `mqtt_client_init()`

```c
void mqtt_client_init ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

初始化客户端实例（Client Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |

**说明（Note）**：注（Note）：在设置任何客户端参数及连接消息代理（Broker）之前，必须调用此函数初始化客户端结构体。

<a id="gad936f28553cb2e771a843512b0a315fa"></a>

### `mqtt_connect()`

```c
int mqtt_connect ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

请求新的 MQTT 客户端连接（Client Connection）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |

**说明（Note）**：注（Note）：假定此内存在调用 `mqtt_disconnect` 前一直驻留有效。MQTT 连接建立后，对代理地址、用户名、设备 ID 等参数的后续更改均无效。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

**说明（Note）**：注（Note）：连接请求默认使用协议修订版 3.1.1。使用协议 3.1.0 时，请设置 `client.protocol_version = MQTT_VERSION_3_1_0`。若要覆盖默认的 1 分钟保活时间，请修改 `CONFIG_MQTT_KEEPALIVE`。

<a id="ga0bc7d91da88c2fbc25108d89ce4318c4"></a>

### `mqtt_disconnect()`

```c
int mqtt_disconnect ( struct mqtt_client * client, const struct mqtt_disconnect_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

断开 MQTT 连接（Connection）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance）。 |
| `[in] param` | 可选的断开连接参数（Disconnect Parameters），可为 `NULL`。使用 MQTT 3.1.1 时忽略。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga2dbc3c158d63a6f57b362be94c22660a"></a>

### `mqtt_input()`

```c
int mqtt_input ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

接收入站 MQTT 数据包（Incoming MQTT Packet）。

将调用已注册的回调，并传入分组内容（Packet Content）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |

**说明（Note）**：注（Note）：对于 PUBLISH 消息，须使用 `mqtt_read_publish_payload` 函数单独读取载荷（Payload）。发布事件结构体提供要读取的载荷大小。这是非阻塞调用。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gaa16bf7b0597ad00c4a3943235579e86b"></a>

### `mqtt_keepalive_time_left()`

```c
int mqtt_keepalive_time_left ( const struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

确定何时应发送下一条保活消息（Keep Alive Message）的辅助函数。

例如可用作 `poll` 超时的取值来源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance）。 |

**返回（Returns）**：返回值（Returns）：距离预计发送下一条保活消息（Keep Alive Message）的时间，单位为毫秒。未启用保活消息时返回 -1。

<a id="ga8b87710d01076c8e51b1a75634168269"></a>

### `mqtt_live()`

```c
int mqtt_live ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

应定期调用此 API，使客户端能够在需要时发送 ping 请求（Ping Requests）以保持连接存活。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |

**说明（Note）**：注（Note）：应用必须确保调用此函数的周期足以遵守连接时与消息代理（Broker）约定的保活时间（Keep Alive Time）。保活时间的详细信息参见 `mqtt_connect`。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gad1d549d37b69a61e1bf8d9d213e02ca8"></a>

### `mqtt_ping()`

```c
int mqtt_ping ( struct mqtt_client * client)
```

```c
#include <zephyr/net/mqtt.h>
```

发送 MQTT ping 的 API。

此 API 为可选项，因为库会自行处理连接保活（Keep-Alive），参见 `mqtt_live`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance）。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga57745efa1bf6fbdf7eb1b3f01623e4c7"></a>

### `mqtt_publish()`

```c
int mqtt_publish ( struct mqtt_client * client, const struct mqtt_publish_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

向主题（Topics）发布消息的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 发布消息（Publish Message）所用参数，不得为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gae9069fceec2c018e64cc6beb16aa055c"></a>

### `mqtt_publish_qos1_ack()`

```c
int mqtt_publish_qos1_ack ( struct mqtt_client * client, const struct mqtt_puback_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

客户端收到 QoS1 发布消息（Publish Message）后发送确认的 API。

收到 QoS 级别为 `MQTT_QOS_1_AT_LEAST_ONCE` 的 `MQTT_EVT_PUBLISH` 时应调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 标识正在确认的消息。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga2b17999e845d613f5b0b20015b8204f3"></a>

### `mqtt_publish_qos2_complete()`

```c
int mqtt_publish_qos2_complete ( struct mqtt_client * client, const struct mqtt_pubcomp_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

客户端收到 QoS2 发布释放消息（Publish Release Message）后发送确认的 API。

收到 `MQTT_EVT_PUBREL` 时应调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 标识正在完成的消息。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="gacbe41b83d9c0676d0d4cf01dd91765eb"></a>

### `mqtt_publish_qos2_receive()`

```c
int mqtt_publish_qos2_receive ( struct mqtt_client * client, const struct mqtt_pubrec_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

客户端收到 QoS2 发布消息（Publish Message）后发送确认的 API。

收到 QoS 级别为 `MQTT_QOS_2_EXACTLY_ONCE` 的 `MQTT_EVT_PUBLISH` 时应调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 标识正在确认的消息。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga6c952ed014f78774096bfb6099794803"></a>

### `mqtt_publish_qos2_release()`

```c
int mqtt_publish_qos2_release ( struct mqtt_client * client, const struct mqtt_pubrel_param * param )
```

```c
#include <zephyr/net/mqtt.h>
```

客户端请求释放 QoS2 发布消息（Publish Message）的 API。

收到 `MQTT_EVT_PUBREC` 时应调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 标识正在释放的消息。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga3559cdd6093d75c6fe6792ec2a453172"></a>

### `mqtt_read_publish_payload()`

```c
int mqtt_read_publish_payload ( struct mqtt_client * client, void * buffer, size_t length )
```

```c
#include <zephyr/net/mqtt.h>
```

读取所收到 PUBLISH 消息的载荷（Payload）。

在收到 MQTT PUBLISH 消息通知时，应在 MQTT 事件处理函数（Event Handler）内部调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[out] buffer` | 用于存储载荷（Payload）的缓冲区。 |
| `[in] length` | 缓冲区长度（Buffer Length），单位为字节。 |

**说明（Note）**：注（Note）：这是非阻塞调用（Non-Blocking Call）。

**返回（Returns）**：返回值（Returns）：已读字节数，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga05213aceaa9e9cbbfaa9bab7a78b3d25"></a>

### `mqtt_read_publish_payload_blocking()`

```c
int mqtt_read_publish_payload_blocking ( struct mqtt_client * client, void * buffer, size_t length )
```

```c
#include <zephyr/net/mqtt.h>
```

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[out] buffer` | 用于存储载荷（Payload）的缓冲区。 |
| `[in] length` | 缓冲区长度（Buffer Length），单位为字节。 |

**返回（Returns）**：返回值（Returns）：已读字节数，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga31823965ec34a253793b40b50e800417"></a>

### `mqtt_readall_publish_payload()`

```c
int mqtt_readall_publish_payload ( struct mqtt_client * client, uint8_t * buffer, size_t length )
```

```c
#include <zephyr/net/mqtt.h>
```

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version），运行直到读取到所需字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[out] buffer` | 用于存储载荷（Payload）的缓冲区。 |
| `[in] length` | 要读取的字节数。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为表示失败原因的负错误码，参见 `errno.h`。

<a id="ga40d226b891b8f62f2c486bbb11ce9678"></a>

### `mqtt_subscribe()`

```c
int mqtt_subscribe ( struct mqtt_client * client, const struct mqtt_subscription_list * param )
```

```c
#include <zephyr/net/mqtt.h>
```

在连接上请求订阅一个或多个主题（Topics）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 订阅参数（Subscription Parameters），不得为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。

<a id="ga4ff43a198e93e332b5553a4d0b59261d"></a>

### `mqtt_unsubscribe()`

```c
int mqtt_unsubscribe ( struct mqtt_client * client, const struct mqtt_subscription_list * param )
```

```c
#include <zephyr/net/mqtt.h>
```

在连接上请求取消订阅一个或多个主题（Topics）的 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 标识请求执行此流程的客户端实例（Client Instance），不得为 `NULL`。 |
| `[in] param` | 描述要取消订阅的主题（Topics）的参数，不得为 `NULL`。 |

**说明（Note）**：注（Note）：此 API 不使用主题描述中的 QoS。

**返回（Returns）**：返回值（Returns）：0，或表示失败原因的负错误码，参见 `errno.h`。


## 7.7\_原页交叉引用（Cross References）

- [mqtt_utf8](../network_application_model_reference/P079_mqtt_utf8_结构体.md)
- [mqtt_binstr](../network_application_model_reference/P053_mqtt_binstr_结构体.md)
- [mqtt_topic_alias](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md)
- [mqtt_topic](../network_application_model_reference/P075_mqtt_topic_结构体.md)
- [mqtt_utf8_pair](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md)
- [mqtt_publish_message](../network_application_model_reference/P062_mqtt_publish_message_结构体.md)
- [mqtt_connack_param](../network_application_model_reference/P056_mqtt_connack_param_结构体.md)
- [mqtt_common_ack_properties](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md)
- [mqtt_puback_param](../network_application_model_reference/P060_mqtt_puback_param_结构体.md)
- [mqtt_pubrec_param](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md)
- [mqtt_pubrel_param](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md)
- [mqtt_pubcomp_param](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md)
- [mqtt_suback_param](../network_application_model_reference/P073_mqtt_suback_param_结构体.md)
- [mqtt_unsuback_param](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md)
- [mqtt_publish_param](../network_application_model_reference/P063_mqtt_publish_param_结构体.md)
- [mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)
- [mqtt_disconnect_param](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md)
- [mqtt_auth_param](../network_application_model_reference/P052_mqtt_auth_param_结构体.md)
- [mqtt_evt_param](../network_application_model_reference/P091_mqtt_evt_param_联合体.md)
- [mqtt_evt](../network_application_model_reference/P058_mqtt_evt_结构体.md)
- [mqtt_sec_config](../network_application_model_reference/P066_mqtt_sec_config_结构体.md)
- [mqtt_transport](../network_application_model_reference/P077_mqtt_transport_结构体.md)
- [mqtt_internal](../network_application_model_reference/P059_mqtt_internal_结构体.md)
- [mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/mqtt.h](../api_file_clock_network_reference/P018_zephyr__net__mqtt.h_文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [CONFIG_MQTT_KEEPALIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_KEEPALIVE)
- [poll](../api_file_reference/P306_zephyr__posix__poll.h_文件参考.md#afa7e83ddea0ab5b08fcf614b89ac48ba)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructmqtt__utf8_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60"></a>
<a id="ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863"></a>
<a id="ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134"></a>
<a id="ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa"></a>
<a id="ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e"></a>
<a id="ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a"></a>
<a id="ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b"></a>
<a id="ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c"></a>
<a id="ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa"></a>
<a id="ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec"></a>
<a id="ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c"></a>
<a id="ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78"></a>
<a id="ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86"></a>
<a id="ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d"></a>
<a id="ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603"></a>
<a id="ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf"></a>
<a id="ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a"></a>
<a id="ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610"></a>
<a id="ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0"></a>
<a id="ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c"></a>
<a id="ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b"></a>
<a id="ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194"></a>
<a id="ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5"></a>
<a id="ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173"></a>
<a id="ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a"></a>
<a id="ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65"></a>
<a id="ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d"></a>
<a id="ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6"></a>
<a id="ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1"></a>
<a id="ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98"></a>
<a id="ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293"></a>
<a id="ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c"></a>
<a id="ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4"></a>
<a id="ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5"></a>
<a id="gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde"></a>
<a id="gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e"></a>
<a id="gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d"></a>
<a id="gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117"></a>
<a id="gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc"></a>
<a id="gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d"></a>
<a id="gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4"></a>
<a id="ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01"></a>
<a id="ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c"></a>
<a id="ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b"></a>
<a id="ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7"></a>
<a id="ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a"></a>
<a id="ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df"></a>
<a id="gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7"></a>
<a id="gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e"></a>
<a id="gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_MQTT-SN 客户端库.md) · [返回大纲](大纲.md) · [下一章](P008_USB Type-C 端口控制器 API（Port Controller API）.md)
