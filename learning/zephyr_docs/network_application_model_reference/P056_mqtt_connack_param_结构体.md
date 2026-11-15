---
id: learning.zephyr-docs.network-application-model-reference.page-56
title: mqtt_connack_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__connack__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_mqtt\_connack\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__connack__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接确认（CONNACK）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

连接确认（CONNACK）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_ab123a8236804082667ad93ddd7e40e7a"></a>

```c
uint8_t session_present_flag
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[session_present_flag](#ab123a8236804082667ad93ddd7e40e7a)。

会话存在标志（Session Present Flag）使客户端能够判断：客户端与服务器对于是否已有存储的会话状态，是否持有一致认识。

<a id="r_aae7a54dd6f62887b618f652f260ed6bd"></a>

```c
uint8_t return_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[return_code](#aae7a54dd6f62887b618f652f260ed6bd)。

服务器因某种原因无法处理连接请求时，用相应的非零连接返回码（Connect Return Code）表示。

```c
struct {
```

<a id="r_a5cc1ea7f34232646f71032e05a40b21e"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a29eed1a34902519380aa59757bde501c)。

MQTT 5.0第3.2.2.3.10节：用户属性（User Property）。

<a id="r_aecdedda28efea2f89bc75d907ee0ebde"></a>

```c
struct mqtt_utf8 assigned_client_id
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[assigned_client_id](#a7f275e22d6cdf808b1f0a19c3f78f517)。

MQTT 5.0第3.2.2.3.7节：分配的客户端标识符（Assigned Client Identifier）。

<a id="r_ae1d22c27d218950b855587727655dddf"></a>

```c
struct mqtt_utf8 reason_string
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[reason_string](#a5fbdc09eff6fef2f06a98c8f9faf0a03)。

MQTT 5.0第3.2.2.3.9节：原因字符串（Reason String）。

<a id="r_a3cbb4829aaa407284d4e4a505647b086"></a>

```c
struct mqtt_utf8 response_information
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[response_information](#a1314e5735f128b905bd3d78beaee956e)。

MQTT 5.0第3.2.2.3.15节：响应信息（Response Information）。

<a id="r_a27fdb99f1b0cb2268ba6094e2c46ce77"></a>

```c
struct mqtt_utf8 server_reference
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[server_reference](#a0426044dfe84d5160d1116018265eda3)。

MQTT 5.0第3.2.2.3.16节：服务器引用（Server Reference）。

<a id="r_a0bdfc9684999ede9837e46b675e37f4d"></a>

```c
struct mqtt_utf8 auth_method
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[auth_method](#abbd4490c94846009f79c741e3067c743)。

MQTT 5.0第3.2.2.3.17节：认证方法（Authentication Method）。

<a id="r_aa884430ab2dcdc67e7ecd1fe7533a6df"></a>

```c
struct mqtt_binstr auth_data
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[auth_data](#ad45d67943848406b290fee98e5d4d3ba)。

MQTT 5.0第3.2.2.3.18节：认证数据（Authentication Data）。

<a id="r_a85a75946761313b32e7e23847a8c7c0f"></a>

```c
uint32_t session_expiry_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[session_expiry_interval](#a7e47864579e36ea469d198ceb9cdd3f4)。

MQTT 5.0第3.2.2.3.2节：会话过期间隔（Session Expiry Interval）。

<a id="r_aa3626978b7d122fd3bc95f3ed6b09e61"></a>

```c
uint32_t maximum_packet_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[maximum_packet_size](#a8e5cab6b3479fc9e902feb622008386a)。

MQTT 5.0第3.2.2.3.6节：最大数据包大小（Maximum Packet Size）。

<a id="r_aad435d1ae53dd3c9a7f293732e927058"></a>

```c
uint16_t receive_maximum
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_maximum](#a9eecd31595fa1332a1cf4b661cedeae2)。

MQTT 5.0第3.3.2.3.3节：接收最大值（Receive Maximum）。

<a id="r_aca47ab0c99d4ee4418d5ea44e5ffcb7f"></a>

```c
uint16_t topic_alias_maximum
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[topic_alias_maximum](#a09cdb8430a3ced98055b564716201bf1)。

MQTT 5.0第3.2.2.3.8节：主题别名最大值（Topic Alias Maximum）。

<a id="r_a4e09bd54f824666fe0e3bd337b511ccc"></a>

```c
uint16_t server_keep_alive
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[server_keep_alive](#af21ff08751c63f17423500c33191fcdf)。

MQTT 5.0第3.2.2.3.14节：服务器保活时间（Server Keep Alive）。

<a id="r_a3f0842ed7912ad06cab8bce4f9731082"></a>

```c
uint8_t maximum_qos
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[maximum_qos](#a9c400f66c3a7eade5df879b328f4cb42)。

MQTT 5.0第3.2.2.3.4节：最大服务质量（Maximum QoS）。

<a id="r_a54e6d91c2615f93c344f9cc05a5372be"></a>

```c
uint8_t retain_available
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retain_available](#af0810d9762a46f0ac7376becb631a9f7)。

MQTT 5.0第3.2.2.3.5节：保留消息可用性（Retain Available）。

<a id="r_ab76064bbc14910e06f74696c96348338"></a>

```c
uint8_t wildcard_sub_available
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wildcard_sub_available](#a1802487e00937da8e4261083b7229219)。

MQTT 5.0第3.2.2.3.11节：通配符订阅可用性（Wildcard Subscription Available）。

<a id="r_ab39c61bfa13809fb15da228abfdbf84b"></a>

```c
uint8_t subscription_ids_available
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subscription_ids_available](#ac3815c5ecaaeb8cea860ccd75f1d460a)。

MQTT 5.0第3.2.2.3.12节：订阅标识符可用性（Subscription Identifiers Available）。

<a id="r_a83d5671a3bcdfdeeb4c7ec8e875dd51d"></a>

```c
uint8_t shared_sub_available
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[shared_sub_available](#a3a21965017d0e9d15ed046eb0cfb461f)。

MQTT 5.0第3.2.2.3.13节：共享订阅可用性（Shared Subscription Available）。

```c
struct {
```

<a id="r_a8dfc271a7f503067341ecb7900ff361f"></a>

```c
bool has_session_expiry_interval
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_session_expiry_interval](#ae2c5b667e0e050611791160c8b7755ef)。

包含会话过期间隔（Session Expiry Interval）属性。

<a id="r_afc2eace087534c581ca410cddf2e141a"></a>

```c
bool has_receive_maximum
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_receive_maximum](#a1c37aaf9f6cde9f251b79af7144a099e)。

包含接收最大值（Receive Maximum）属性。

<a id="r_a6f929887bc5845f9694da1d911ecae7b"></a>

```c
bool has_maximum_qos
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_maximum_qos](#a0f02175c92a22ad05f370dd944ad6b1a)。

包含最大服务质量（Maximum QoS）属性。

<a id="r_a9807db465077900210f7838cd5602b72"></a>

```c
bool has_retain_available
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_retain_available](#a7df963cce8b5ba99efe9888f742fad4f)。

包含保留消息可用性（Retain Available）属性。

<a id="r_a83f3ed392044cde3e9bb53b716fe1bbc"></a>

```c
bool has_maximum_packet_size
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_maximum_packet_size](#a80932b53f13d5cb5c299f384c176e1af)。

包含最大数据包大小（Maximum Packet Size）属性。

<a id="r_a775e1401a6b950de33a3de6e7dbb2455"></a>

```c
bool has_assigned_client_id
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_assigned_client_id](#af2655b3164805704e68d8ed69621a168)。

包含分配的客户端标识符（Assigned Client Identifier）属性。

<a id="r_afabe134619524e225a523abd2aa352c0"></a>

```c
bool has_topic_alias_maximum
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_topic_alias_maximum](#ac3f6a6b22fcf1ed55dc46d4b9b2079e6)。

包含主题别名最大值（Topic Alias Maximum）属性。

<a id="r_aaeccc6155961ac60ff44992a5b6e080a"></a>

```c
bool has_reason_string
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_reason_string](#a4f8092dc562fe27396c21e1329e19262)。

包含原因字符串（Reason String）属性。

<a id="r_a8f15934a1fd9725f19311c0b30b0b76d"></a>

```c
bool has_user_prop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_user_prop](#a4d1b50d148189053879ec80aa2688a2b)。

包含用户属性（User Property）属性。

<a id="r_aaa8524b98af91f35de778fdf3113fcdc"></a>

```c
bool has_wildcard_sub_available
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_wildcard_sub_available](#a3a6f8b9f79f81c34bda7aca99fa0682f)。

包含通配符订阅可用性（Wildcard Subscription Available）属性。

<a id="r_a5543fa83cf5d47b2df43fccb7b5cb4bb"></a>

```c
bool has_subscription_ids_available
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_subscription_ids_available](#a43ada81fd7746aab783a0d1cb4d4d645)。

包含订阅标识符可用性（Subscription Identifiers Available）属性。

<a id="r_a13546f69ce9cdc9ff5a0a3e80f78543c"></a>

```c
bool has_shared_sub_available
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_shared_sub_available](#a78dad1593aaa64c27263cafc61791a03)。

包含共享订阅可用性（Shared Subscription Available）属性。

<a id="r_abd2c84a128ee593c2790c8b3395ead56"></a>

```c
bool has_server_keep_alive
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_server_keep_alive](#a0d11efb926df6a0d65e879fee878bda0)。

包含服务器保活时间（Server Keep Alive）属性。

<a id="r_a6719a78e2ace89bf83de0b52937825f9"></a>

```c
bool has_response_information
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_response_information](#a0f03ee47ace97ccaa841df5353e49f26)。

包含响应信息（Response Information）属性。

<a id="r_a5564fd53a86400befb8a84efc613dfa9"></a>

```c
bool has_server_reference
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_server_reference](#a351717d25bf8bc2d915506b5bc354214)。

包含服务器引用（Server Reference）属性。

<a id="r_a595f9df36757b16030344a090ef4a3b6"></a>

```c
bool has_auth_method
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_auth_method](#a7134eddbb0d497c6cfe85b6fcfc9efa1)。

包含认证方法（Authentication Method）属性。

<a id="r_a41ead56be72857211e59f2d1ed6d0981"></a>

```c
bool has_auth_data
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_auth_data](#a6d7423e5c7234e97f79db2dd9e592d85)。

包含认证数据（Authentication Data）属性。

<a id="r_a00b77574cd9ab96f52615f88654fe722"></a>

```c
} rx
```

相关声明：[rx](#a3a7a8a6dbef8d5026717b98b4e949c4e)。

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="r_a54ae953abeec2d31e7c82869302b492e"></a>

```c
} prop
```

相关声明：[prop](#a54ae953abeec2d31e7c82869302b492e)。

## 56.2\_详细说明（Detailed Documentation）

<a id="a7f275e22d6cdf808b1f0a19c3f78f517"></a>

### `assigned_client_id`

```c
struct mqtt_utf8 mqtt_connack_param::assigned_client_id
```

MQTT 5.0第3.2.2.3.7节：分配的客户端标识符（Assigned Client Identifier）。

<a id="ad45d67943848406b290fee98e5d4d3ba"></a>

### `auth_data`

```c
struct mqtt_binstr mqtt_connack_param::auth_data
```

MQTT 5.0第3.2.2.3.18节：认证数据（Authentication Data）。

<a id="abbd4490c94846009f79c741e3067c743"></a>

### `auth_method`

```c
struct mqtt_utf8 mqtt_connack_param::auth_method
```

MQTT 5.0第3.2.2.3.17节：认证方法（Authentication Method）。

<a id="af2655b3164805704e68d8ed69621a168"></a>

### `has_assigned_client_id`

```c
bool mqtt_connack_param::has_assigned_client_id
```

包含分配的客户端标识符（Assigned Client Identifier）属性。

<a id="a6d7423e5c7234e97f79db2dd9e592d85"></a>

### `has_auth_data`

```c
bool mqtt_connack_param::has_auth_data
```

包含认证数据（Authentication Data）属性。

<a id="a7134eddbb0d497c6cfe85b6fcfc9efa1"></a>

### `has_auth_method`

```c
bool mqtt_connack_param::has_auth_method
```

包含认证方法（Authentication Method）属性。

<a id="a80932b53f13d5cb5c299f384c176e1af"></a>

### `has_maximum_packet_size`

```c
bool mqtt_connack_param::has_maximum_packet_size
```

包含最大数据包大小（Maximum Packet Size）属性。

<a id="a0f02175c92a22ad05f370dd944ad6b1a"></a>

### `has_maximum_qos`

```c
bool mqtt_connack_param::has_maximum_qos
```

包含最大服务质量（Maximum QoS）属性。

<a id="a4f8092dc562fe27396c21e1329e19262"></a>

### `has_reason_string`

```c
bool mqtt_connack_param::has_reason_string
```

包含原因字符串（Reason String）属性。

<a id="a1c37aaf9f6cde9f251b79af7144a099e"></a>

### `has_receive_maximum`

```c
bool mqtt_connack_param::has_receive_maximum
```

包含接收最大值（Receive Maximum）属性。

<a id="a0f03ee47ace97ccaa841df5353e49f26"></a>

### `has_response_information`

```c
bool mqtt_connack_param::has_response_information
```

包含响应信息（Response Information）属性。

<a id="a7df963cce8b5ba99efe9888f742fad4f"></a>

### `has_retain_available`

```c
bool mqtt_connack_param::has_retain_available
```

包含保留消息可用性（Retain Available）属性。

<a id="a0d11efb926df6a0d65e879fee878bda0"></a>

### `has_server_keep_alive`

```c
bool mqtt_connack_param::has_server_keep_alive
```

包含服务器保活时间（Server Keep Alive）属性。

<a id="a351717d25bf8bc2d915506b5bc354214"></a>

### `has_server_reference`

```c
bool mqtt_connack_param::has_server_reference
```

包含服务器引用（Server Reference）属性。

<a id="ae2c5b667e0e050611791160c8b7755ef"></a>

### `has_session_expiry_interval`

```c
bool mqtt_connack_param::has_session_expiry_interval
```

包含会话过期间隔（Session Expiry Interval）属性。

<a id="a78dad1593aaa64c27263cafc61791a03"></a>

### `has_shared_sub_available`

```c
bool mqtt_connack_param::has_shared_sub_available
```

包含共享订阅可用性（Shared Subscription Available）属性。

<a id="a43ada81fd7746aab783a0d1cb4d4d645"></a>

### `has_subscription_ids_available`

```c
bool mqtt_connack_param::has_subscription_ids_available
```

包含订阅标识符可用性（Subscription Identifiers Available）属性。

<a id="ac3f6a6b22fcf1ed55dc46d4b9b2079e6"></a>

### `has_topic_alias_maximum`

```c
bool mqtt_connack_param::has_topic_alias_maximum
```

包含主题别名最大值（Topic Alias Maximum）属性。

<a id="a4d1b50d148189053879ec80aa2688a2b"></a>

### `has_user_prop`

```c
bool mqtt_connack_param::has_user_prop
```

包含用户属性（User Property）属性。

<a id="a3a6f8b9f79f81c34bda7aca99fa0682f"></a>

### `has_wildcard_sub_available`

```c
bool mqtt_connack_param::has_wildcard_sub_available
```

包含通配符订阅可用性（Wildcard Subscription Available）属性。

<a id="a8e5cab6b3479fc9e902feb622008386a"></a>

### `maximum_packet_size`

```c
uint32_t mqtt_connack_param::maximum_packet_size
```

MQTT 5.0第3.2.2.3.6节：最大数据包大小（Maximum Packet Size）。

<a id="a9c400f66c3a7eade5df879b328f4cb42"></a>

### `maximum_qos`

```c
uint8_t mqtt_connack_param::maximum_qos
```

MQTT 5.0第3.2.2.3.4节：最大服务质量（Maximum QoS）。

<a id="a54ae953abeec2d31e7c82869302b492e"></a>

### `[struct]`

```c
struct { ... } mqtt_connack_param::prop
```

<a id="a5fbdc09eff6fef2f06a98c8f9faf0a03"></a>

### `reason_string`

```c
struct mqtt_utf8 mqtt_connack_param::reason_string
```

MQTT 5.0第3.2.2.3.9节：原因字符串（Reason String）。

<a id="a9eecd31595fa1332a1cf4b661cedeae2"></a>

### `receive_maximum`

```c
uint16_t mqtt_connack_param::receive_maximum
```

MQTT 5.0第3.3.2.3.3节：接收最大值（Receive Maximum）。

<a id="a1314e5735f128b905bd3d78beaee956e"></a>

### `response_information`

```c
struct mqtt_utf8 mqtt_connack_param::response_information
```

MQTT 5.0第3.2.2.3.15节：响应信息（Response Information）。

<a id="af0810d9762a46f0ac7376becb631a9f7"></a>

### `retain_available`

```c
uint8_t mqtt_connack_param::retain_available
```

MQTT 5.0第3.2.2.3.5节：保留消息可用性（Retain Available）。

<a id="aae7a54dd6f62887b618f652f260ed6bd"></a>

### `return_code`

```c
uint8_t mqtt_connack_param::return_code
```

服务器因某种原因无法处理连接请求时，用相应的非零连接返回码（Connect Return Code）表示。

MQTT 3.1的返回码由mqtt_conn_return_code定义；MQTT 5.0的原因码由mqtt_connack_reason_code定义。

<a id="a3a7a8a6dbef8d5026717b98b4e949c4e"></a>

### `[struct]`

```c
struct { ... } mqtt_connack_param::rx
```

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="af21ff08751c63f17423500c33191fcdf"></a>

### `server_keep_alive`

```c
uint16_t mqtt_connack_param::server_keep_alive
```

MQTT 5.0第3.2.2.3.14节：服务器保活时间（Server Keep Alive）。

<a id="a0426044dfe84d5160d1116018265eda3"></a>

### `server_reference`

```c
struct mqtt_utf8 mqtt_connack_param::server_reference
```

MQTT 5.0第3.2.2.3.16节：服务器引用（Server Reference）。

<a id="a7e47864579e36ea469d198ceb9cdd3f4"></a>

### `session_expiry_interval`

```c
uint32_t mqtt_connack_param::session_expiry_interval
```

MQTT 5.0第3.2.2.3.2节：会话过期间隔（Session Expiry Interval）。

<a id="ab123a8236804082667ad93ddd7e40e7a"></a>

### `session_present_flag`

```c
uint8_t mqtt_connack_param::session_present_flag
```

会话存在标志（Session Present Flag）使客户端能够判断：客户端与服务器对于是否已有存储的会话状态，是否持有一致认识。

<a id="a3a21965017d0e9d15ed046eb0cfb461f"></a>

### `shared_sub_available`

```c
uint8_t mqtt_connack_param::shared_sub_available
```

MQTT 5.0第3.2.2.3.13节：共享订阅可用性（Shared Subscription Available）。

<a id="ac3815c5ecaaeb8cea860ccd75f1d460a"></a>

### `subscription_ids_available`

```c
uint8_t mqtt_connack_param::subscription_ids_available
```

MQTT 5.0第3.2.2.3.12节：订阅标识符可用性（Subscription Identifiers Available）。

<a id="a09cdb8430a3ced98055b564716201bf1"></a>

### `topic_alias_maximum`

```c
uint16_t mqtt_connack_param::topic_alias_maximum
```

MQTT 5.0第3.2.2.3.8节：主题别名最大值（Topic Alias Maximum）。

<a id="a29eed1a34902519380aa59757bde501c"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_connack_param::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.2.2.3.10节：用户属性（User Property）。

<a id="a1802487e00937da8e4261083b7229219"></a>

### `wildcard_sub_available`

```c
uint8_t mqtt_connack_param::wildcard_sub_available
```

MQTT 5.0第3.2.2.3.11节：通配符订阅可用性（Wildcard Subscription Available）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mqtt_conn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa17b38ed9c7e65f3e01ad906b24bb618)
- [mqtt_connack_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae4c3fb5313addb72961ff578113d183a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_mqtt_common_ack_properties_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_mqtt_disconnect_param_结构体.md)
