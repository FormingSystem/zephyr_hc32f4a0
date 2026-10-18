---
id: learning.zephyr-docs.network-application-model-reference.page-67
title: mqtt_sn_client_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_mqtt\_sn\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述MQTT-SN客户端（Client）的结构。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

描述MQTT-SN客户端（Client）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a9cbf86052061b55a93356346cae75e8b"></a>

```c
struct mqtt_sn_data client_id
```

相关声明：[mqtt_sn_data](P069_mqtt_sn_data_结构体.md)、[client_id](#a9cbf86052061b55a93356346cae75e8b)。

长度为1至23个字符的唯一客户端标识（Client ID）。

<a id="r_af70196b9800123e2f9c36362cfb8b6be"></a>

```c
struct mqtt_sn_data will_topic
```

相关声明：[mqtt_sn_data](P069_mqtt_sn_data_结构体.md)、[will_topic](#af70196b9800123e2f9c36362cfb8b6be)。

遗嘱消息（Will Message）的主题。

<a id="r_a9d2397f5ff59a51630f5b82f94c92327"></a>

```c
struct mqtt_sn_data will_msg
```

相关声明：[mqtt_sn_data](P069_mqtt_sn_data_结构体.md)、[will_msg](#a9d2397f5ff59a51630f5b82f94c92327)。

遗嘱消息（Will Message）。

<a id="r_a42d76db9cbcc9770246241283bb65486"></a>

```c
enum mqtt_sn_qos will_qos
```

相关声明：[mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)、[will_qos](#a42d76db9cbcc9770246241283bb65486)。

遗嘱消息（Will Message）的服务质量（QoS）。

<a id="r_ad8f5b3b7815033cfecda7519ca657724"></a>

```c
bool will_retain
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[will_retain](#ad8f5b3b7815033cfecda7519ca657724)。

表示消息代理（Broker）是否应保留遗嘱消息的标志。

<a id="r_aec0d4d3f436d7c7d40e2548d7c6575c1"></a>

```c
struct mqtt_sn_transport * transport
```

相关声明：[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)、[transport](#aec0d4d3f436d7c7d40e2548d7c6575c1)。

客户端所用的底层传输（Underlying Transport）。

<a id="r_a3802bd92a42e421a5d733c64b53473db"></a>

```c
struct net_buf_simple tx
```

相关声明：[net_buf_simple](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html)、[tx](#a3802bd92a42e421a5d733c64b53473db)。

传出数据（Outgoing Data）的缓冲区。

<a id="r_aec40ceeac5a4160b058ee6a7676ec68f"></a>

```c
struct net_buf_simple rx
```

相关声明：[net_buf_simple](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html)、[rx](#aec40ceeac5a4160b058ee6a7676ec68f)。

传入数据（Incoming Data）的缓冲区。

<a id="r_a306887539a950e2f0b3ad6da40519ba3"></a>

```c
struct net_buf_simple rx_addr
```

相关声明：[net_buf_simple](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html)、[rx_addr](#a306887539a950e2f0b3ad6da40519ba3)。

传入数据发送方地址（Sender Address）的缓冲区。

<a id="r_ac2b8e9d7d4c246c5d5538922a1e9887b"></a>

```c
mqtt_sn_evt_cb_t evt_cb
```

相关声明：[mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)、[evt_cb](#ac2b8e9d7d4c246c5d5538922a1e9887b)。

事件回调（Event Callback）。

<a id="r_a05b83c732ed9199dac0110cfb1e56563"></a>

```c
uint16_t next_msg_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[next_msg_id](#a05b83c732ed9199dac0110cfb1e56563)。

下一条待发送消息的消息标识（Message ID）。

<a id="r_a32efbccbf7b1820ff5092896130e6b7e"></a>

```c
sys_slist_t publish
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[publish](#a32efbccbf7b1820ff5092896130e6b7e)。

待处理发布消息（Pending Publish Messages）的列表。

<a id="r_aa47e6426ca7e8434734377a85f586b84"></a>

```c
sys_slist_t topic
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[topic](#aa47e6426ca7e8434734377a85f586b84)。

已注册主题（Registered Topics）的列表。

<a id="r_a96748b082edf64987a867f9a2e32dca2"></a>

```c
sys_slist_t gateways
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[gateways](#a96748b082edf64987a867f9a2e32dca2)。

已发现网关（Found Gateways）的列表。

<a id="r_a02a38427caa60c51f85661efe58813f6"></a>

```c
int state
```

相关声明：[state](#a02a38427caa60c51f85661efe58813f6)。

MQTT-SN客户端的当前状态（Current State）。

<a id="r_af400a2f993c27e0f25a4325daeacee28"></a>

```c
int64_t last_ping
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[last_ping](#af400a2f993c27e0f25a4325daeacee28)。

上次ping请求的时间戳（Timestamp）。

<a id="r_a2be2f7d041f325dda14007864e03fb70"></a>

```c
uint8_t ping_retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ping_retries](#a2be2f7d041f325dda14007864e03fb70)。

ping尝试失败后的重试次数（Retries）。

<a id="r_aa1501b32ef99547d99a1c03a29433748"></a>

```c
int64_t ts_searchgw
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[ts_searchgw](#aa1501b32ef99547d99a1c03a29433748)。

下一次SEARCHGW传输的时间戳（Timestamp）。

<a id="r_a1b2ceae7b3fe37ebd2f3ecd8387565d3"></a>

```c
int64_t ts_gwinfo
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[ts_gwinfo](#a1b2ceae7b3fe37ebd2f3ecd8387565d3)。

下一次GWINFO传输的时间戳（Timestamp）。

<a id="r_a9ec4ff19f5cfef074ad9f5a34dd35eff"></a>

```c
uint8_t radius_gwinfo
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[radius_gwinfo](#a9ec4ff19f5cfef074ad9f5a34dd35eff)。

下一次GWINFO传输的半径（Radius）。

<a id="r_ae79d55b3148233cf44afe97e810f9fad"></a>

```c
struct mqtt_sn_connect_retry connect
```

相关声明：[mqtt_sn_connect_retry](P068_mqtt_sn_connect_retry_结构体.md)、[connect](#ae79d55b3148233cf44afe97e810f9fad)。

待处理CONNECT重试的状态。

<a id="r_af6e609481e40f4382898b53d12b4aa88"></a>

```c
struct mqtt_sn_will_update will_topic_update
```

相关声明：[mqtt_sn_will_update](P072_mqtt_sn_will_update_结构体.md)、[will_topic_update](#af6e609481e40f4382898b53d12b4aa88)。

遗嘱主题更新（Will Topic Updates）的状态。

<a id="r_a7d5aa6955be3c30a5569cf9730a2f3f3"></a>

```c
struct mqtt_sn_will_update will_message_update
```

相关声明：[mqtt_sn_will_update](P072_mqtt_sn_will_update_结构体.md)、[will_message_update](#a7d5aa6955be3c30a5569cf9730a2f3f3)。

遗嘱消息更新（Will Message Updates）的状态。

<a id="r_a65bb52c8a5ecbd81e743fdc7c213b43a"></a>

```c
struct k_work_delayable process_work
```

相关声明：[k_work_delayable](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__delayable.html)、[process_work](#a65bb52c8a5ecbd81e743fdc7c213b43a)。

用于处理MQTT-SN事件的可延迟工作（Delayable Work）结构。

## 67.2\_详细说明（Detailed Documentation）

<a id="a9cbf86052061b55a93356346cae75e8b"></a>

### `client_id`

```c
struct mqtt_sn_data mqtt_sn_client::client_id
```

长度为1至23个字符的唯一客户端标识（Client ID）。

<a id="ae79d55b3148233cf44afe97e810f9fad"></a>

### `connect`

```c
struct mqtt_sn_connect_retry mqtt_sn_client::connect
```

待处理CONNECT重试的状态。

<a id="ac2b8e9d7d4c246c5d5538922a1e9887b"></a>

### `evt_cb`

```c
mqtt_sn_evt_cb_t mqtt_sn_client::evt_cb
```

事件回调（Event Callback）。

<a id="a96748b082edf64987a867f9a2e32dca2"></a>

### `gateways`

```c
sys_slist_t mqtt_sn_client::gateways
```

已发现网关（Found Gateways）的列表。

<a id="af400a2f993c27e0f25a4325daeacee28"></a>

### `last_ping`

```c
int64_t mqtt_sn_client::last_ping
```

上次ping请求的时间戳（Timestamp）。

<a id="a05b83c732ed9199dac0110cfb1e56563"></a>

### `next_msg_id`

```c
uint16_t mqtt_sn_client::next_msg_id
```

下一条待发送消息的消息标识（Message ID）。

<a id="a2be2f7d041f325dda14007864e03fb70"></a>

### `ping_retries`

```c
uint8_t mqtt_sn_client::ping_retries
```

ping尝试失败后的重试次数（Retries）。

<a id="a65bb52c8a5ecbd81e743fdc7c213b43a"></a>

### `process_work`

```c
struct k_work_delayable mqtt_sn_client::process_work
```

用于处理MQTT-SN事件的可延迟工作（Delayable Work）结构。

<a id="a32efbccbf7b1820ff5092896130e6b7e"></a>

### `publish`

```c
sys_slist_t mqtt_sn_client::publish
```

待处理发布消息（Pending Publish Messages）的列表。

<a id="a9ec4ff19f5cfef074ad9f5a34dd35eff"></a>

### `radius_gwinfo`

```c
uint8_t mqtt_sn_client::radius_gwinfo
```

下一次GWINFO传输的半径（Radius）。

<a id="aec40ceeac5a4160b058ee6a7676ec68f"></a>

### `rx`

```c
struct net_buf_simple mqtt_sn_client::rx
```

传入数据（Incoming Data）的缓冲区。

<a id="a306887539a950e2f0b3ad6da40519ba3"></a>

### `rx_addr`

```c
struct net_buf_simple mqtt_sn_client::rx_addr
```

传入数据发送方地址（Sender Address）的缓冲区。

<a id="a02a38427caa60c51f85661efe58813f6"></a>

### `state`

```c
int mqtt_sn_client::state
```

MQTT-SN客户端的当前状态（Current State）。

<a id="aa47e6426ca7e8434734377a85f586b84"></a>

### `topic`

```c
sys_slist_t mqtt_sn_client::topic
```

已注册主题（Registered Topics）的列表。

<a id="aec0d4d3f436d7c7d40e2548d7c6575c1"></a>

### `transport`

```c
struct mqtt_sn_transport* mqtt_sn_client::transport
```

客户端所用的底层传输（Underlying Transport）。

<a id="a1b2ceae7b3fe37ebd2f3ecd8387565d3"></a>

### `ts_gwinfo`

```c
int64_t mqtt_sn_client::ts_gwinfo
```

下一次GWINFO传输的时间戳（Timestamp）。

<a id="aa1501b32ef99547d99a1c03a29433748"></a>

### `ts_searchgw`

```c
int64_t mqtt_sn_client::ts_searchgw
```

下一次SEARCHGW传输的时间戳（Timestamp）。

<a id="a3802bd92a42e421a5d733c64b53473db"></a>

### `tx`

```c
struct net_buf_simple mqtt_sn_client::tx
```

传出数据（Outgoing Data）的缓冲区。

<a id="a7d5aa6955be3c30a5569cf9730a2f3f3"></a>

### `will_message_update`

```c
struct mqtt_sn_will_update mqtt_sn_client::will_message_update
```

遗嘱消息更新（Will Message Updates）的状态。

<a id="a9d2397f5ff59a51630f5b82f94c92327"></a>

### `will_msg`

```c
struct mqtt_sn_data mqtt_sn_client::will_msg
```

遗嘱消息（Will Message）。

以will=true连接之前必须初始化。

<a id="a42d76db9cbcc9770246241283bb65486"></a>

### `will_qos`

```c
enum mqtt_sn_qos mqtt_sn_client::will_qos
```

遗嘱消息（Will Message）的服务质量（QoS）。

<a id="ad8f5b3b7815033cfecda7519ca657724"></a>

### `will_retain`

```c
bool mqtt_sn_client::will_retain
```

表示消息代理（Broker）是否应保留遗嘱消息的标志。

<a id="af70196b9800123e2f9c36362cfb8b6be"></a>

### `will_topic`

```c
struct mqtt_sn_data mqtt_sn_client::will_topic
```

遗嘱消息（Will Message）的主题。

以will=true连接之前必须初始化。

<a id="af6e609481e40f4382898b53d12b4aa88"></a>

### `will_topic_update`

```c
struct mqtt_sn_will_update mqtt_sn_client::will_topic_update
```

遗嘱主题更新（Will Topic Updates）的状态。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [mqtt_sn_data](P069_mqtt_sn_data_结构体.md)
- [mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)
- [net_buf_simple](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html)
- [mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_sn_connect_retry](P068_mqtt_sn_connect_retry_结构体.md)
- [mqtt_sn_will_update](P072_mqtt_sn_will_update_结构体.md)
- [k_work_delayable](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__delayable.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_mqtt_sec_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_mqtt_sn_connect_retry_结构体.md)
