---
id: learning.zephyr-docs.network-application-model-reference.page-54
title: mqtt_client_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_mqtt\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于维护客户端相关信息的MQTT客户端（Client）定义。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

用于维护客户端相关信息的MQTT客户端（Client）定义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a41cc1d3c5e5180af1d6376f88598678a"></a>

```c
struct mqtt_internal internal
```

相关声明：[mqtt_internal](P059_mqtt_internal_结构体.md)、[internal](#a41cc1d3c5e5180af1d6376f88598678a)。

MQTT客户端内部状态（Internal State）。

<a id="r_ac31a2ea9d67886f83fd3af88f33f36d9"></a>

```c
struct mqtt_transport transport
```

相关声明：[mqtt_transport](P077_mqtt_transport_结构体.md)、[transport](#ac31a2ea9d67886f83fd3af88f33f36d9)。

MQTT传输配置和数据（Transport Configuration and Data）。

<a id="r_aabd419115c8637e4e4c0e6d23a5a984d"></a>

```c
struct mqtt_utf8 client_id
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[client_id](#aabd419115c8637e4e4c0e6d23a5a984d)。

用于连接的唯一客户端标识（Client Identification）。

<a id="r_a72d61d9c0e717010ff90c2ed7fcddf5c"></a>

```c
const void * broker
```

相关声明：[broker](#a72d61d9c0e717010ff90c2ed7fcddf5c)。

消息代理（Broker）的详细信息，例如地址、端口。

<a id="r_ab271f2061fe3c9e3c1a76158a1c00449"></a>

```c
struct mqtt_utf8 * user_name
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[user_name](#ab271f2061fe3c9e3c1a76158a1c00449)。

连接所用的用户名（User Name），如有。

<a id="r_aef6da1db6f600a2bfd1c7dd0d78d1b6d"></a>

```c
struct mqtt_utf8 * password
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[password](#aef6da1db6f600a2bfd1c7dd0d78d1b6d)。

连接所用的口令（Password），如有。

```c
struct {
```

<a id="r_a1edf14d04d514e89d47443e49576bf8e"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a726f5a806458d7dc9d6072dff74508fc)。

MQTT 5.0第3.1.3.2.8节：用户属性（User Property）。

<a id="r_ae1e018f283f472f4d998e7945517e886"></a>

```c
struct mqtt_utf8 content_type
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[content_type](#a89ce07fe536a502c051e4082b708155e)。

MQTT 5.0第3.1.3.2.5节：内容类型（Content Type）。

<a id="r_a471e20d78a82c778afc6b4ed7bc27243"></a>

```c
struct mqtt_utf8 response_topic
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[response_topic](#ac6c53bf95f311a4df29d7db5f4c20b45)。

MQTT 5.0第3.1.3.2.6节：响应主题（Response Topic）。

<a id="r_aa327085539e068aa16fa5259f1ccb86e"></a>

```c
struct mqtt_binstr correlation_data
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[correlation_data](#aac856189cedecf059f4ba723b06edda6)。

MQTT 5.0第3.1.3.2.7节：关联数据（Correlation Data）。

<a id="r_a50b0443ee47afd1463d3e55d7bc3bac6"></a>

```c
uint32_t will_delay_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[will_delay_interval](#a253bee13043ffe1ebe9c46299f8a238e)。

MQTT 5.0第3.1.3.2.2节：遗嘱延迟间隔（Will Delay Interval）。

<a id="r_a7451ae50f34d26385fe836f03c296984"></a>

```c
uint32_t message_expiry_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[message_expiry_interval](#a485855e9b09d0c48fb09c5673f38b5ee)。

MQTT 5.0第3.1.3.2.4节：消息过期间隔（Message Expiry Interval）。

<a id="r_a15cf4701e6b9f02a15ad50bf9946d6c9"></a>

```c
uint8_t payload_format_indicator
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_format_indicator](#abdf2c45264ba77d584655b0cb6562c6b)。

MQTT 5.0第3.1.3.2.3节：载荷格式指示符（Payload Format Indicator）。

<a id="r_a0a1669a8be16d37819704ac60911de73"></a>

```c
} will_prop
```

相关声明：[will_prop](#a0a1669a8be16d37819704ac60911de73)。

MQTT 5.0遗嘱属性（Will Properties）。

<a id="r_a4b23a72831697b78dc4019a4b6ac97e4"></a>

```c
struct mqtt_topic * will_topic
```

相关声明：[mqtt_topic](P075_mqtt_topic_结构体.md)、[will_topic](#a4b23a72831697b78dc4019a4b6ac97e4)。

遗嘱主题（Will Topic）和服务质量（QoS）。

<a id="r_a7f4e9547b1d91edf21589334db711499"></a>

```c
struct mqtt_utf8 * will_message
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[will_message](#a7f4e9547b1d91edf21589334db711499)。

遗嘱消息（Will Message）。

<a id="r_a44c515b8b25d59554990f6193217d83f"></a>

```c
mqtt_evt_cb_t evt_cb
```

相关声明：[mqtt_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gabdf01ededb62ceb4c1608a64cb718a8c)、[evt_cb](#a44c515b8b25d59554990f6193217d83f)。

应用向模块注册的回调（Callback），用于获取MQTT事件。

<a id="r_a9f63fb54f8557135c1aa38a60bb7053c"></a>

```c
uint8_t * rx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_buf](#a9f63fb54f8557135c1aa38a60bb7053c)。

接收路径（RX Path）中用于接收MQTT数据包的接收缓冲区。

<a id="r_a66335741e991a2985ab5d4d7765651d2"></a>

```c
uint32_t rx_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_buf_size](#a66335741e991a2985ab5d4d7765651d2)。

接收缓冲区（Receive Buffer）的大小。

<a id="r_ae582274bf396caa0a3427f1aeace639c"></a>

```c
uint8_t * tx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_buf](#ae582274bf396caa0a3427f1aeace639c)。

发送路径（TX Path）中用于创建MQTT数据包的发送缓冲区。

<a id="r_a4c456f4065e3bc20752d908f2d805667"></a>

```c
uint32_t tx_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_buf_size](#a4c456f4065e3bc20752d908f2d805667)。

发送缓冲区（Transmit Buffer）的大小。

<a id="r_aa65a4af5952634e4ff5c4bf700ccccd7"></a>

```c
uint16_t keepalive
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[keepalive](#aa65a4af5952634e4ff5c4bf700ccccd7)。

此客户端的保活间隔（Keepalive Interval），单位为秒。

<a id="r_a63e3c1b470a7de9d179b1c0686504a68"></a>

```c
uint8_t protocol_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[protocol_version](#a63e3c1b470a7de9d179b1c0686504a68)。

MQTT协议版本（Protocol Version）。

<a id="r_a67f76cd0feadf8ae11ed232dcc9ac1d1"></a>

```c
int8_t unacked_ping
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[unacked_ping](#a67f76cd0feadf8ae11ed232dcc9ac1d1)。

此连接上尚未得到应答的PINGREQ数量。

```c
struct {
```

<a id="r_a47a36b17ae44db26f9ea757374569109"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a726f5a806458d7dc9d6072dff74508fc)。

MQTT 5.0第3.1.2.11.8节：用户属性（User Property）。

<a id="r_a5a25d3c9ba5aec1fa2ca32d3d8f05972"></a>

```c
struct mqtt_utf8 auth_method
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[auth_method](#ac899284f06f581cac0b647381c757287)。

MQTT 5.0第3.1.2.11.9节：认证方法（Authentication Method）。

<a id="r_a03551ea7bf5b253c1c447859582c5c34"></a>

```c
struct mqtt_binstr auth_data
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[auth_data](#ae46c6695e9dfbf13cb895d8acad12d58)。

MQTT 5.0第3.1.2.11.10节：认证数据（Authentication Data）。

<a id="r_ad4c9e5ef3aedf6e72656592ca4c01b6e"></a>

```c
uint32_t session_expiry_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[session_expiry_interval](#a1d0587f7b2be63eb74f9cba271c337fb)。

MQTT 5.0第3.1.2.11.2节：会话过期间隔（Session Expiry Interval）。

<a id="r_a14f56c6482a95d7719243842679dea33"></a>

```c
uint32_t maximum_packet_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[maximum_packet_size](#a2d9fc66f26284f6ab90f79a4d7aef6d7)。

MQTT 5.0第3.1.2.11.4节：最大数据包大小（Maximum Packet Size）。

<a id="r_afe13021dc5022462d53588feb31bc9a2"></a>

```c
uint16_t receive_maximum
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_maximum](#a6700818bb78880e8b10878f31680f3d3)。

MQTT 5.0第3.1.2.11.3节：接收最大值（Receive Maximum）。

<a id="r_acc0a6138851a99fb7820a61f9d637469"></a>

```c
bool request_response_info
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[request_response_info](#a1c5a0e00803a745b2569452ed127440a)。

MQTT 5.0第3.1.2.11.6节：请求响应信息（Request Response Information）。

<a id="r_a73bec8294552fd58f7c7e7ae26e19111"></a>

```c
bool request_problem_info
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[request_problem_info](#a1a8f71b8756219a20404782c9aeff431)。

MQTT 5.0第3.1.2.11.7节：请求响应信息（Request Response Information）。

<a id="r_a8c48cec6d0f895d05a8f933240348818"></a>

```c
} prop
```

相关声明：[prop](#a8c48cec6d0f895d05a8f933240348818)。

MQTT 5.0属性（Properties）。

<a id="r_ac96879e15ccd829fbcf9b88913161c0d"></a>

```c
uint8_t will_retain: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[will_retain](#ac96879e15ccd829fbcf9b88913161c0d)。

遗嘱保留标志（Will Retain Flag）；若应持久保留遗嘱消息，则为1。

<a id="r_aae9ecb0faf8dc4337579e0713d065184"></a>

```c
uint8_t clean_session: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clean_session](#aae9ecb0faf8dc4337579e0713d065184)。

清理会话标志（Clean Session Flag），表示新会话（1）或保留会话（0）。

<a id="r_afe138435d59720cc2c8c4b2756134a49"></a>

```c
void * user_data
```

相关声明：[user_data](#afe138435d59720cc2c8c4b2756134a49)。

用户专用的不透明数据（Opaque Data）。

## 54.2\_详细说明（Detailed Documentation）

<a id="ae46c6695e9dfbf13cb895d8acad12d58"></a>

### `auth_data`

```c
struct mqtt_binstr mqtt_client::auth_data
```

MQTT 5.0第3.1.2.11.10节：认证数据（Authentication Data）。

<a id="ac899284f06f581cac0b647381c757287"></a>

### `auth_method`

```c
struct mqtt_utf8 mqtt_client::auth_method
```

MQTT 5.0第3.1.2.11.9节：认证方法（Authentication Method）。

<a id="a72d61d9c0e717010ff90c2ed7fcddf5c"></a>

### `broker`

```c
const void* mqtt_client::broker
```

消息代理（Broker）的详细信息，例如地址、端口。

地址类型（Address Type）应与使用的传输方式兼容。

<a id="aae9ecb0faf8dc4337579e0713d065184"></a>

### `clean_session`

```c
uint8_t mqtt_client::clean_session
```

清理会话标志（Clean Session Flag），表示新会话（1）或保留会话（0）。

默认值为CONFIG_MQTT_CLEAN_SESSION。

<a id="aabd419115c8637e4e4c0e6d23a5a984d"></a>

### `client_id`

```c
struct mqtt_utf8 mqtt_client::client_id
```

用于连接的唯一客户端标识（Client Identification）。

<a id="a89ce07fe536a502c051e4082b708155e"></a>

### `content_type`

```c
struct mqtt_utf8 mqtt_client::content_type
```

MQTT 5.0第3.1.3.2.5节：内容类型（Content Type）。

<a id="aac856189cedecf059f4ba723b06edda6"></a>

### `correlation_data`

```c
struct mqtt_binstr mqtt_client::correlation_data
```

MQTT 5.0第3.1.3.2.7节：关联数据（Correlation Data）。

<a id="a44c515b8b25d59554990f6193217d83f"></a>

### `evt_cb`

```c
mqtt_evt_cb_t mqtt_client::evt_cb
```

应用向模块注册的回调（Callback），用于获取MQTT事件。

<a id="a41cc1d3c5e5180af1d6376f88598678a"></a>

### `internal`

```c
struct mqtt_internal mqtt_client::internal
```

MQTT客户端内部状态（Internal State）。

<a id="aa65a4af5952634e4ff5c4bf700ccccd7"></a>

### `keepalive`

```c
uint16_t mqtt_client::keepalive
```

此客户端的保活间隔（Keepalive Interval），单位为秒。

默认值为CONFIG_MQTT_KEEPALIVE。

<a id="a2d9fc66f26284f6ab90f79a4d7aef6d7"></a>

### `maximum_packet_size`

```c
uint32_t mqtt_client::maximum_packet_size
```

MQTT 5.0第3.1.2.11.4节：最大数据包大小（Maximum Packet Size）。

<a id="a485855e9b09d0c48fb09c5673f38b5ee"></a>

### `message_expiry_interval`

```c
uint32_t mqtt_client::message_expiry_interval
```

MQTT 5.0第3.1.3.2.4节：消息过期间隔（Message Expiry Interval）。

<a id="aef6da1db6f600a2bfd1c7dd0d78d1b6d"></a>

### `password`

```c
struct mqtt_utf8* mqtt_client::password
```

连接所用的口令（Password），如有。

注意，提供口令（Password）时也必须提供用户名。NULL表示没有口令。

<a id="abdf2c45264ba77d584655b0cb6562c6b"></a>

### `payload_format_indicator`

```c
uint8_t mqtt_client::payload_format_indicator
```

MQTT 5.0第3.1.3.2.3节：载荷格式指示符（Payload Format Indicator）。

<a id="a8c48cec6d0f895d05a8f933240348818"></a>

### `[struct]`

```c
struct { ... } mqtt_client::prop
```

MQTT 5.0属性（Properties）。

<a id="a63e3c1b470a7de9d179b1c0686504a68"></a>

### `protocol_version`

```c
uint8_t mqtt_client::protocol_version
```

MQTT协议版本（Protocol Version）。

<a id="a6700818bb78880e8b10878f31680f3d3"></a>

### `receive_maximum`

```c
uint16_t mqtt_client::receive_maximum
```

MQTT 5.0第3.1.2.11.3节：接收最大值（Receive Maximum）。

<a id="a1a8f71b8756219a20404782c9aeff431"></a>

### `request_problem_info`

```c
bool mqtt_client::request_problem_info
```

MQTT 5.0第3.1.2.11.7节：请求响应信息（Request Response Information）。

<a id="a1c5a0e00803a745b2569452ed127440a"></a>

### `request_response_info`

```c
bool mqtt_client::request_response_info
```

MQTT 5.0第3.1.2.11.6节：请求响应信息（Request Response Information）。

<a id="ac6c53bf95f311a4df29d7db5f4c20b45"></a>

### `response_topic`

```c
struct mqtt_utf8 mqtt_client::response_topic
```

MQTT 5.0第3.1.3.2.6节：响应主题（Response Topic）。

<a id="a9f63fb54f8557135c1aa38a60bb7053c"></a>

### `rx_buf`

```c
uint8_t* mqtt_client::rx_buf
```

接收路径（RX Path）中用于接收MQTT数据包的接收缓冲区。

<a id="a66335741e991a2985ab5d4d7765651d2"></a>

### `rx_buf_size`

```c
uint32_t mqtt_client::rx_buf_size
```

接收缓冲区（Receive Buffer）的大小。

<a id="a1d0587f7b2be63eb74f9cba271c337fb"></a>

### `session_expiry_interval`

```c
uint32_t mqtt_client::session_expiry_interval
```

MQTT 5.0第3.1.2.11.2节：会话过期间隔（Session Expiry Interval）。

<a id="ac31a2ea9d67886f83fd3af88f33f36d9"></a>

### `transport`

```c
struct mqtt_transport mqtt_client::transport
```

MQTT传输配置和数据（Transport Configuration and Data）。

<a id="ae582274bf396caa0a3427f1aeace639c"></a>

### `tx_buf`

```c
uint8_t* mqtt_client::tx_buf
```

发送路径（TX Path）中用于创建MQTT数据包的发送缓冲区。

<a id="a4c456f4065e3bc20752d908f2d805667"></a>

### `tx_buf_size`

```c
uint32_t mqtt_client::tx_buf_size
```

发送缓冲区（Transmit Buffer）的大小。

<a id="a67f76cd0feadf8ae11ed232dcc9ac1d1"></a>

### `unacked_ping`

```c
int8_t mqtt_client::unacked_ping
```

此连接上尚未得到应答的PINGREQ数量。

<a id="afe138435d59720cc2c8c4b2756134a49"></a>

### `user_data`

```c
void* mqtt_client::user_data
```

用户专用的不透明数据（Opaque Data）。

<a id="ab271f2061fe3c9e3c1a76158a1c00449"></a>

### `user_name`

```c
struct mqtt_utf8* mqtt_client::user_name
```

连接所用的用户名（User Name），如有。

NULL表示没有用户名（User Name）。

<a id="a726f5a806458d7dc9d6072dff74508fc"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_client::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.1.3.2.8节：用户属性（User Property）。

MQTT 5.0第3.1.2.11.8节：用户属性（User Property）。

<a id="a253bee13043ffe1ebe9c46299f8a238e"></a>

### `will_delay_interval`

```c
uint32_t mqtt_client::will_delay_interval
```

MQTT 5.0第3.1.3.2.2节：遗嘱延迟间隔（Will Delay Interval）。

<a id="a7f4e9547b1d91edf21589334db711499"></a>

### `will_message`

```c
struct mqtt_utf8* mqtt_client::will_message
```

遗嘱消息（Will Message）。

可为NULL。非NULL值仅在遗嘱主题（Will Topic）不为NULL时有效。

<a id="a0a1669a8be16d37819704ac60911de73"></a>

### `[struct]`

```c
struct { ... } mqtt_client::will_prop
```

MQTT 5.0遗嘱属性（Will Properties）。

<a id="ac96879e15ccd829fbcf9b88913161c0d"></a>

### `will_retain`

```c
uint8_t mqtt_client::will_retain
```

遗嘱保留标志（Will Retain Flag）；若应持久保留遗嘱消息，则为1。

<a id="a4b23a72831697b78dc4019a4b6ac97e4"></a>

### `will_topic`

```c
struct mqtt_topic* mqtt_client::will_topic
```

遗嘱主题（Will Topic）和服务质量（QoS）。

可为NULL。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_internal](P059_mqtt_internal_结构体.md)
- [mqtt_transport](P077_mqtt_transport_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_topic](P075_mqtt_topic_结构体.md)
- [mqtt_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gabdf01ededb62ceb4c1608a64cb718a8c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_mqtt_binstr_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_mqtt_common_ack_properties_结构体.md)
