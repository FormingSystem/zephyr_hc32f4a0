---
id: learning.zephyr-docs.api-file-clock-network-reference.page-18
title: zephyr__net__mqtt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_net\_\_mqtt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT客户端实现（Client Implementation）。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/tls_credentials.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/sys/mutex.h>
#include <zephyr/net/websocket.h>
```

查看此文件的源码。

MQTT 客户端实现（Client Implementation）。注意（Note）：实现假定 TCP 模块已启用，默认使用 MQTT 3.1.1 版本。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

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

## 18.2\_宏定义（Macros）

<a id="r_gaeaa4fcf581c7d6be755f9a053a3b488c"></a>

```c
#define MQTT_UTF8_LITERAL(literal)
```

相关声明：[MQTT_UTF8_LITERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaeaa4fcf581c7d6be755f9a053a3b488c)。

根据 C 字符串字面量（Literal String）初始化 UTF-8 编码字符串。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.3\_类型定义（Typedefs）

<a id="r_gabdf01ededb62ceb4c1608a64cb718a8c"></a>

```c
typedef void(* mqtt_evt_cb_t) (struct mqtt_client *client, const struct mqtt_evt *evt)
```

相关声明：[mqtt_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gabdf01ededb62ceb4c1608a64cb718a8c)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_evt](../network_application_model_reference/P058_mqtt_evt_结构体.md)。

由应用注册的异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.4\_枚举（Enumerations）

<a id="r_ga0071fe013b9920711456ef51cc3e6d91"></a>

```c
enum mqtt_evt_type { MQTT_EVT_CONNACK , MQTT_EVT_DISCONNECT , MQTT_EVT_PUBLISH , MQTT_EVT_PUBACK , MQTT_EVT_PUBREC , MQTT_EVT_PUBREL , MQTT_EVT_PUBCOMP , MQTT_EVT_SUBACK , MQTT_EVT_UNSUBACK , MQTT_EVT_PINGRESP , MQTT_EVT_AUTH }
```

相关声明：[mqtt_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0071fe013b9920711456ef51cc3e6d91)、[MQTT_EVT_CONNACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3)、[MQTT_EVT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032)、[MQTT_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9)、[MQTT_EVT_PUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de)、[MQTT_EVT_PUBREC](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87)、[MQTT_EVT_PUBREL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2)、[MQTT_EVT_PUBCOMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8)、[MQTT_EVT_SUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb)、[MQTT_EVT_UNSUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2)、[MQTT_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)、[MQTT_EVT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde)。

模块通过应用注册的回调，向应用通知 MQTT 异步事件（Asynchronous Events）。

<a id="r_ga90d152a4b0986e9a07a12c7c56f5e2a0"></a>

```c
enum mqtt_version { MQTT_VERSION_3_1_0 = 3 , MQTT_VERSION_3_1_1 = 4 , MQTT_VERSION_5_0 = 5 }
```

相关声明：[mqtt_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga90d152a4b0986e9a07a12c7c56f5e2a0)、[MQTT_VERSION_3_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7)、[MQTT_VERSION_3_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e)、[MQTT_VERSION_5_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f)。

MQTT 版本协议级别（Version Protocol Level）。

<a id="r_ga396015e492b0fee8da37c7168d9cdb33"></a>

```c
enum mqtt_qos { MQTT_QOS_0_AT_MOST_ONCE = 0x00 , MQTT_QOS_1_AT_LEAST_ONCE = 0x01 , MQTT_QOS_2_EXACTLY_ONCE = 0x02 }
```

相关声明：[mqtt_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga396015e492b0fee8da37c7168d9cdb33)、[MQTT_QOS_0_AT_MOST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e)、[MQTT_QOS_1_AT_LEAST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d)、[MQTT_QOS_2_EXACTLY_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117)。

MQTT 服务质量类型（Quality of Service，QoS）。

<a id="r_ga25ba4f0870fc2c01ee5fc2c06bd898c8"></a>

```c
enum mqtt_retain_handling { MQTT_RH_0_SEND_AT_SUBSCRIBE = 0x00 , MQTT_RH_1_SEND_IF_NEW = 0x01 , MQTT_RH_2_DO_NOT_SEND = 0x02 }
```

相关声明：[mqtt_retain_handling](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga25ba4f0870fc2c01ee5fc2c06bd898c8)、[MQTT_RH_0_SEND_AT_SUBSCRIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc)、[MQTT_RH_1_SEND_IF_NEW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d)、[MQTT_RH_2_DO_NOT_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4)。

MQTT 5.0 保留消息处理选项（Retain Handling Options）。

<a id="r_gaa17b38ed9c7e65f3e01ad906b24bb618"></a>

```c
enum mqtt_conn_return_code { MQTT_CONNECTION_ACCEPTED = 0x00 , MQTT_UNACCEPTABLE_PROTOCOL_VERSION = 0x01 , MQTT_IDENTIFIER_REJECTED = 0x02 , MQTT_SERVER_UNAVAILABLE = 0x03 , MQTT_BAD_USER_NAME_OR_PASSWORD = 0x04 , MQTT_NOT_AUTHORIZED = 0x05 }
```

相关声明：[mqtt_conn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa17b38ed9c7e65f3e01ad906b24bb618)、[MQTT_CONNECTION_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050)、[MQTT_UNACCEPTABLE_PROTOCOL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744)、[MQTT_IDENTIFIER_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141)、[MQTT_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3)、[MQTT_BAD_USER_NAME_OR_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134)、[MQTT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb)。

MQTT 3.1 连接确认（CONNACK）返回码。

<a id="r_gae4c3fb5313addb72961ff578113d183a"></a>

```c
enum mqtt_connack_reason_code { MQTT_CONNACK_SUCCESS = 0 , MQTT_CONNACK_UNSPECIFIED_ERROR = 128 , MQTT_CONNACK_MALFORMED_PACKET = 129 , MQTT_CONNACK_PROTOCOL_ERROR = 130 , MQTT_CONNACK_IMPL_SPECIFIC_ERROR = 131 , MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR = 132 , MQTT_CONNACK_CLIENT_ID_NOT_VALID = 133 , MQTT_CONNACK_BAD_USERNAME_OR_PASS = 134 , MQTT_CONNACK_NOT_AUTHORIZED = 135 , MQTT_CONNACK_SERVER_UNAVAILABLE = 136 , MQTT_CONNACK_SERVER_BUSY = 137 , MQTT_CONNACK_BANNED = 138 , MQTT_CONNACK_BAD_AUTH_METHOD = 140 , MQTT_CONNACK_TOPIC_NAME_INVALID = 144 , MQTT_CONNACK_PACKET_TOO_LARGE = 149 , MQTT_CONNACK_QUOTA_EXCEEDED = 151 , MQTT_CONNACK_PAYLOAD_FORMAT_INVALID = 153 , MQTT_CONNACK_RETAIN_NOT_SUPPORTED = 154 , MQTT_CONNACK_QOS_NOT_SUPPORTED = 155 , MQTT_CONNACK_USE_ANOTHER_SERVER = 156 , MQTT_CONNACK_SERVER_MOVED = 157 , MQTT_CONNACK_CONNECTION_RATE_EXCEEDED = 159 }
```

相关声明：[mqtt_connack_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae4c3fb5313addb72961ff578113d183a)、[MQTT_CONNACK_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7)、[MQTT_CONNACK_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989)、[MQTT_CONNACK_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0)、[MQTT_CONNACK_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc)、[MQTT_CONNACK_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee)、[MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816)、[MQTT_CONNACK_CLIENT_ID_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f)、[MQTT_CONNACK_BAD_USERNAME_OR_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd)、[MQTT_CONNACK_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e)、[MQTT_CONNACK_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa)、[MQTT_CONNACK_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8)、[MQTT_CONNACK_BANNED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33)、[MQTT_CONNACK_BAD_AUTH_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4)、[MQTT_CONNACK_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5)、[MQTT_CONNACK_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040)、[MQTT_CONNACK_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f)、[MQTT_CONNACK_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c)、[MQTT_CONNACK_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956)、[MQTT_CONNACK_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0)、[MQTT_CONNACK_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c)、[MQTT_CONNACK_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa)、[MQTT_CONNACK_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e)。

MQTT 5.0 连接确认原因码（CONNACK Reason Codes），见 MQTT 5.0 第 3.2.2.2 节。

<a id="r_gaca1e61c8b14b75544e253cea355274a8"></a>

```c
enum mqtt_suback_return_code { MQTT_SUBACK_SUCCESS_QoS_0 = 0x00 , MQTT_SUBACK_SUCCESS_QoS_1 = 0x01 , MQTT_SUBACK_SUCCESS_QoS_2 = 0x02 , MQTT_SUBACK_FAILURE = 0x80 }
```

相关声明：[mqtt_suback_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaca1e61c8b14b75544e253cea355274a8)、[MQTT_SUBACK_SUCCESS_QoS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01)、[MQTT_SUBACK_SUCCESS_QoS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c)、[MQTT_SUBACK_SUCCESS_QoS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b)、[MQTT_SUBACK_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7)。

MQTT 订阅确认（SUBACK）返回码。

<a id="r_gaaf563f26ca66841145643a657119d780"></a>

```c
enum mqtt_disconnect_reason_code { MQTT_DISCONNECT_NORMAL = 0 , MQTT_DISCONNECT_WITH_WILL_MSG = 4 , MQTT_DISCONNECT_UNSPECIFIED_ERROR = 128 , MQTT_DISCONNECT_MALFORMED_PACKET = 129 , MQTT_DISCONNECT_PROTOCOL_ERROR = 130 , MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR = 131 , MQTT_DISCONNECT_NOT_AUTHORIZED = 135 , MQTT_DISCONNECT_SERVER_BUSY = 137 , MQTT_DISCONNECT_SERVER_SHUTTING_DOWN = 139 , MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT = 141 , MQTT_DISCONNECT_SESSION_TAKE_OVER = 142 , MQTT_DISCONNECT_TOPIC_FILTER_INVALID = 143 , MQTT_DISCONNECT_TOPIC_NAME_INVALID = 144 , MQTT_DISCONNECT_RECV_MAX_EXCEEDED = 147 , MQTT_DISCONNECT_TOPIC_ALIAS_INVALID = 148 , MQTT_DISCONNECT_PACKET_TOO_LARGE = 149 , MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH = 150 , MQTT_DISCONNECT_QUOTA_EXCEEDED = 151 , MQTT_DISCONNECT_ADMIN_ACTION = 152 , MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID = 153 , MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED = 154 , MQTT_DISCONNECT_QOS_NOT_SUPPORTED = 155 , MQTT_DISCONNECT_USE_ANOTHER_SERVER = 156 , MQTT_DISCONNECT_SERVER_MOVED = 157 , MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED = 158 , MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED = 159 , MQTT_DISCONNECT_MAX_CONNECT_TIME = 160 , MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED = 161 , MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED = 162 }
```

相关声明：[mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)、[MQTT_DISCONNECT_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a)、[MQTT_DISCONNECT_WITH_WILL_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b)、[MQTT_DISCONNECT_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c)、[MQTT_DISCONNECT_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa)、[MQTT_DISCONNECT_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec)、[MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c)、[MQTT_DISCONNECT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78)、[MQTT_DISCONNECT_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86)、[MQTT_DISCONNECT_SERVER_SHUTTING_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d)、[MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603)、[MQTT_DISCONNECT_SESSION_TAKE_OVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf)、[MQTT_DISCONNECT_TOPIC_FILTER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a)、[MQTT_DISCONNECT_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610)、[MQTT_DISCONNECT_RECV_MAX_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0)、[MQTT_DISCONNECT_TOPIC_ALIAS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c)、[MQTT_DISCONNECT_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b)、[MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194)、[MQTT_DISCONNECT_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5)、[MQTT_DISCONNECT_ADMIN_ACTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173)、[MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a)、[MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65)、[MQTT_DISCONNECT_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d)、[MQTT_DISCONNECT_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6)、[MQTT_DISCONNECT_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1)、[MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98)、[MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293)、[MQTT_DISCONNECT_MAX_CONNECT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c)、[MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4)、[MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4)。

MQTT 断开原因码（Disconnect Reason Codes），见 MQTT 5.0 第 3.14.2.1 节。

<a id="r_gacdbeff0450bbcd438cdf35cd543fc6d6"></a>

```c
enum mqtt_auth_reason_code { MQTT_AUTH_SUCCESS = 0 , MQTT_AUTH_CONTINUE_AUTHENTICATION = 24 , MQTT_AUTH_RE_AUTHENTICATE = 25 }
```

相关声明：[mqtt_auth_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacdbeff0450bbcd438cdf35cd543fc6d6)、[MQTT_AUTH_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60)、[MQTT_AUTH_CONTINUE_AUTHENTICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863)、[MQTT_AUTH_RE_AUTHENTICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a)。

MQTT 认证原因码（Authenticate Reason Codes），见 MQTT 5.0 第 3.15.2.1 节。

<a id="r_gaffc2c3078004cf8d24935be086ad63b4"></a>

```c
enum mqtt_transport_type { MQTT_TRANSPORT_NON_SECURE , MQTT_TRANSPORT_NUM }
```

相关声明：[mqtt_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaffc2c3078004cf8d24935be086ad63b4)、[MQTT_TRANSPORT_NON_SECURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a)、[MQTT_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)。

MQTT 传输类型（Transport Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.5\_函数（Functions）

<a id="r_gad1376509ae7c946c840d103d8b59e9a1"></a>

```c
void mqtt_client_init (struct mqtt_client *client)
```

相关声明：[mqtt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1376509ae7c946c840d103d8b59e9a1)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

初始化客户端实例（Client Instance）。

<a id="r_gad936f28553cb2e771a843512b0a315fa"></a>

```c
int mqtt_connect (struct mqtt_client *client)
```

相关声明：[mqtt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad936f28553cb2e771a843512b0a315fa)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

请求新的 MQTT 客户端连接（Client Connection）的 API。

<a id="r_ga57745efa1bf6fbdf7eb1b3f01623e4c7"></a>

```c
int mqtt_publish (struct mqtt_client *client, const struct mqtt_publish_param *param)
```

相关声明：[mqtt_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_publish_param](../network_application_model_reference/P063_mqtt_publish_param_结构体.md)。

向主题（Topics）发布消息的 API。

<a id="r_gae9069fceec2c018e64cc6beb16aa055c"></a>

```c
int mqtt_publish_qos1_ack (struct mqtt_client *client, const struct mqtt_puback_param *param)
```

相关声明：[mqtt_publish_qos1_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae9069fceec2c018e64cc6beb16aa055c)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_puback_param](../network_application_model_reference/P060_mqtt_puback_param_结构体.md)。

客户端收到 QoS1 发布消息（Publish Message）后发送确认的 API。

<a id="r_gacbe41b83d9c0676d0d4cf01dd91765eb"></a>

```c
int mqtt_publish_qos2_receive (struct mqtt_client *client, const struct mqtt_pubrec_param *param)
```

相关声明：[mqtt_publish_qos2_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacbe41b83d9c0676d0d4cf01dd91765eb)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubrec_param](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md)。

客户端收到 QoS2 发布消息（Publish Message）后发送确认的 API。

<a id="r_ga6c952ed014f78774096bfb6099794803"></a>

```c
int mqtt_publish_qos2_release (struct mqtt_client *client, const struct mqtt_pubrel_param *param)
```

相关声明：[mqtt_publish_qos2_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga6c952ed014f78774096bfb6099794803)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubrel_param](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md)。

客户端请求释放 QoS2 发布消息（Publish Message）的 API。

<a id="r_ga2b17999e845d613f5b0b20015b8204f3"></a>

```c
int mqtt_publish_qos2_complete (struct mqtt_client *client, const struct mqtt_pubcomp_param *param)
```

相关声明：[mqtt_publish_qos2_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2b17999e845d613f5b0b20015b8204f3)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_pubcomp_param](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md)。

客户端收到 QoS2 发布释放消息（Publish Release Message）后发送确认的 API。

<a id="r_ga40d226b891b8f62f2c486bbb11ce9678"></a>

```c
int mqtt_subscribe (struct mqtt_client *client, const struct mqtt_subscription_list *param)
```

相关声明：[mqtt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga40d226b891b8f62f2c486bbb11ce9678)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)。

在连接上请求订阅一个或多个主题（Topics）的 API。

<a id="r_ga4ff43a198e93e332b5553a4d0b59261d"></a>

```c
int mqtt_unsubscribe (struct mqtt_client *client, const struct mqtt_subscription_list *param)
```

相关声明：[mqtt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga4ff43a198e93e332b5553a4d0b59261d)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)。

在连接上请求取消订阅一个或多个主题（Topics）的 API。

<a id="r_gad1d549d37b69a61e1bf8d9d213e02ca8"></a>

```c
int mqtt_ping (struct mqtt_client *client)
```

相关声明：[mqtt_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1d549d37b69a61e1bf8d9d213e02ca8)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

发送 MQTT ping 的 API。

<a id="r_ga0bc7d91da88c2fbc25108d89ce4318c4"></a>

```c
int mqtt_disconnect (struct mqtt_client *client, const struct mqtt_disconnect_param *param)
```

相关声明：[mqtt_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0bc7d91da88c2fbc25108d89ce4318c4)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_disconnect_param](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md)。

断开 MQTT 连接（Connection）的 API。

<a id="r_gad4d870f91a7d594c3a7325ab6de87a02"></a>

```c
int mqtt_auth (struct mqtt_client *client, const struct mqtt_auth_param *param)
```

相关声明：[mqtt_auth](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad4d870f91a7d594c3a7325ab6de87a02)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[mqtt_auth_param](../network_application_model_reference/P052_mqtt_auth_param_结构体.md)。

向服务器发送认证数据包（Authentication Packet）的 API。

<a id="r_gafb2df41fad7c318f9fe75919919139bd"></a>

```c
int mqtt_abort (struct mqtt_client *client)
```

相关声明：[mqtt_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gafb2df41fad7c318f9fe75919919139bd)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

中止 MQTT 连接（Abort Connection）的 API。

<a id="r_ga8b87710d01076c8e51b1a75634168269"></a>

```c
int mqtt_live (struct mqtt_client *client)
```

相关声明：[mqtt_live](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga8b87710d01076c8e51b1a75634168269)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

应定期调用此 API，使客户端能够在需要时发送 ping 请求（Ping Requests）以保持连接存活。

<a id="r_gaa16bf7b0597ad00c4a3943235579e86b"></a>

```c
int mqtt_keepalive_time_left (const struct mqtt_client *client)
```

相关声明：[mqtt_keepalive_time_left](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa16bf7b0597ad00c4a3943235579e86b)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

确定何时应发送下一条保活消息（Keep Alive Message）的辅助函数。

<a id="r_ga2dbc3c158d63a6f57b362be94c22660a"></a>

```c
int mqtt_input (struct mqtt_client *client)
```

相关声明：[mqtt_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2dbc3c158d63a6f57b362be94c22660a)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

接收入站 MQTT 数据包（Incoming MQTT Packet）。

<a id="r_ga3559cdd6093d75c6fe6792ec2a453172"></a>

```c
int mqtt_read_publish_payload (struct mqtt_client *client, void *buffer, size_t length)
```

相关声明：[mqtt_read_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga3559cdd6093d75c6fe6792ec2a453172)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

读取所收到 PUBLISH 消息的载荷（Payload）。

<a id="r_ga05213aceaa9e9cbbfaa9bab7a78b3d25"></a>

```c
int mqtt_read_publish_payload_blocking (struct mqtt_client *client, void *buffer, size_t length)
```

相关声明：[mqtt_read_publish_payload_blocking](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga05213aceaa9e9cbbfaa9bab7a78b3d25)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)。

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version）。

<a id="r_ga31823965ec34a253793b40b50e800417"></a>

```c
int mqtt_readall_publish_payload (struct mqtt_client *client, uint8_t *buffer, size_t length)
```

相关声明：[mqtt_readall_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga31823965ec34a253793b40b50e800417)、[mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

mqtt_read_publish_payload 函数的阻塞版本（Blocking Version），运行直到读取到所需字节数。


## 18.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/tls_credentials.h](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/sys/mutex.h](../userspace_sync_reference/P006_用户模式互斥量头文件源码.md)
- [zephyr/net/websocket.h](../api_source_reference/P916_websocket.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P020_mqtt.h_源码浏览.md)
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
- [MQTT_UTF8_LITERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaeaa4fcf581c7d6be755f9a053a3b488c)
- [mqtt_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gabdf01ededb62ceb4c1608a64cb718a8c)
- [mqtt_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0071fe013b9920711456ef51cc3e6d91)
- [MQTT_EVT_CONNACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3)
- [MQTT_EVT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032)
- [MQTT_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9)
- [MQTT_EVT_PUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de)
- [MQTT_EVT_PUBREC](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87)
- [MQTT_EVT_PUBREL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2)
- [MQTT_EVT_PUBCOMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8)
- [MQTT_EVT_SUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb)
- [MQTT_EVT_UNSUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2)
- [MQTT_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)
- [MQTT_EVT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde)
- [mqtt_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga90d152a4b0986e9a07a12c7c56f5e2a0)
- [MQTT_VERSION_3_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7)
- [MQTT_VERSION_3_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e)
- [MQTT_VERSION_5_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f)
- [mqtt_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga396015e492b0fee8da37c7168d9cdb33)
- [MQTT_QOS_0_AT_MOST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e)
- [MQTT_QOS_1_AT_LEAST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d)
- [MQTT_QOS_2_EXACTLY_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117)
- [mqtt_retain_handling](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga25ba4f0870fc2c01ee5fc2c06bd898c8)
- [MQTT_RH_0_SEND_AT_SUBSCRIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc)
- [MQTT_RH_1_SEND_IF_NEW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d)
- [MQTT_RH_2_DO_NOT_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4)
- [mqtt_conn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa17b38ed9c7e65f3e01ad906b24bb618)
- [MQTT_CONNECTION_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050)
- [MQTT_UNACCEPTABLE_PROTOCOL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744)
- [MQTT_IDENTIFIER_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141)
- [MQTT_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3)
- [MQTT_BAD_USER_NAME_OR_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134)
- [MQTT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb)
- [mqtt_connack_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae4c3fb5313addb72961ff578113d183a)
- [MQTT_CONNACK_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7)
- [MQTT_CONNACK_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989)
- [MQTT_CONNACK_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0)
- [MQTT_CONNACK_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc)
- [MQTT_CONNACK_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee)
- [MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816)
- [MQTT_CONNACK_CLIENT_ID_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f)
- [MQTT_CONNACK_BAD_USERNAME_OR_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd)
- [MQTT_CONNACK_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e)
- [MQTT_CONNACK_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa)
- [MQTT_CONNACK_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8)
- [MQTT_CONNACK_BANNED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33)
- [MQTT_CONNACK_BAD_AUTH_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4)
- [MQTT_CONNACK_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5)
- [MQTT_CONNACK_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040)
- [MQTT_CONNACK_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f)
- [MQTT_CONNACK_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c)
- [MQTT_CONNACK_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956)
- [MQTT_CONNACK_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0)
- [MQTT_CONNACK_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c)
- [MQTT_CONNACK_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa)
- [MQTT_CONNACK_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e)
- [mqtt_suback_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaca1e61c8b14b75544e253cea355274a8)
- [MQTT_SUBACK_SUCCESS_QoS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01)
- [MQTT_SUBACK_SUCCESS_QoS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c)
- [MQTT_SUBACK_SUCCESS_QoS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b)
- [MQTT_SUBACK_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7)
- [mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)
- [MQTT_DISCONNECT_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a)
- [MQTT_DISCONNECT_WITH_WILL_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b)
- [MQTT_DISCONNECT_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c)
- [MQTT_DISCONNECT_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa)
- [MQTT_DISCONNECT_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec)
- [MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c)
- [MQTT_DISCONNECT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78)
- [MQTT_DISCONNECT_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86)
- [MQTT_DISCONNECT_SERVER_SHUTTING_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d)
- [MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603)
- [MQTT_DISCONNECT_SESSION_TAKE_OVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf)
- [MQTT_DISCONNECT_TOPIC_FILTER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a)
- [MQTT_DISCONNECT_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610)
- [MQTT_DISCONNECT_RECV_MAX_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0)
- [MQTT_DISCONNECT_TOPIC_ALIAS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c)
- [MQTT_DISCONNECT_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b)
- [MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194)
- [MQTT_DISCONNECT_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5)
- [MQTT_DISCONNECT_ADMIN_ACTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173)
- [MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a)
- [MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65)
- [MQTT_DISCONNECT_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d)
- [MQTT_DISCONNECT_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6)
- [MQTT_DISCONNECT_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1)
- [MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98)
- [MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293)
- [MQTT_DISCONNECT_MAX_CONNECT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c)
- [MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4)
- [MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4)
- [mqtt_auth_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacdbeff0450bbcd438cdf35cd543fc6d6)
- [MQTT_AUTH_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60)
- [MQTT_AUTH_CONTINUE_AUTHENTICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863)
- [MQTT_AUTH_RE_AUTHENTICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a)
- [mqtt_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaffc2c3078004cf8d24935be086ad63b4)
- [MQTT_TRANSPORT_NON_SECURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a)
- [MQTT_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)
- [mqtt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1376509ae7c946c840d103d8b59e9a1)
- [mqtt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad936f28553cb2e771a843512b0a315fa)
- [mqtt_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7)
- [mqtt_publish_qos1_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae9069fceec2c018e64cc6beb16aa055c)
- [mqtt_publish_qos2_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacbe41b83d9c0676d0d4cf01dd91765eb)
- [mqtt_publish_qos2_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga6c952ed014f78774096bfb6099794803)
- [mqtt_publish_qos2_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2b17999e845d613f5b0b20015b8204f3)
- [mqtt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga40d226b891b8f62f2c486bbb11ce9678)
- [mqtt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga4ff43a198e93e332b5553a4d0b59261d)
- [mqtt_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1d549d37b69a61e1bf8d9d213e02ca8)
- [mqtt_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0bc7d91da88c2fbc25108d89ce4318c4)
- [mqtt_auth](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad4d870f91a7d594c3a7325ab6de87a02)
- [mqtt_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gafb2df41fad7c318f9fe75919919139bd)
- [mqtt_live](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga8b87710d01076c8e51b1a75634168269)
- [mqtt_keepalive_time_left](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa16bf7b0597ad00c4a3943235579e86b)
- [mqtt_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2dbc3c158d63a6f57b362be94c22660a)
- [mqtt_read_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga3559cdd6093d75c6fe6792ec2a453172)
- [mqtt_read_publish_payload_blocking](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga05213aceaa9e9cbbfaa9bab7a78b3d25)
- [mqtt_readall_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga31823965ec34a253793b40b50e800417)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P017_zephyr__drivers__lora.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__sys__printk.h_文件参考.md)
