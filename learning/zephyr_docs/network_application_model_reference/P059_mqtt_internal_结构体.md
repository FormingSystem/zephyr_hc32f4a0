---
id: learning.zephyr-docs.network-application-model-reference.page-59
title: mqtt_internal_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__internal.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_mqtt\_internal\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__internal.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT内部状态（Internal State）。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT内部状态（Internal State）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_af866a252b9e18496c8e1627704d8a8b2"></a>

```c
struct sys_mutex mutex
```

相关声明：[sys_mutex](../userspace_sync_reference/P004_用户模式互斥量结构.md)、[mutex](#af866a252b9e18496c8e1627704d8a8b2)。

内部使用（Internal）。

<a id="r_a8f30cb1440efecf8ae8fc448e4f462f8"></a>

```c
uint32_t last_activity
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[last_activity](#a8f30cb1440efecf8ae8fc448e4f462f8)。

内部使用（Internal）。

<a id="r_acf93a973de5a5430e767e2996f1cd048"></a>

```c
uint32_t state
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[state](#acf93a973de5a5430e767e2996f1cd048)。

内部使用（Internal）。

<a id="r_a45aeafd71dadaf1d0fd0bc3969c921de"></a>

```c
uint32_t rx_buf_datalen
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_buf_datalen](#a45aeafd71dadaf1d0fd0bc3969c921de)。

内部使用（Internal）。

<a id="r_a921477a9839447f4fe1c823911680c92"></a>

```c
uint32_t remaining_payload
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[remaining_payload](#a921477a9839447f4fe1c823911680c92)。

内部使用（Internal）。

<a id="r_a897895965adaf781b3a426dd53da10a2"></a>

```c
struct mqtt_topic_alias topic_aliases [CONFIG_MQTT_TOPIC_ALIAS_MAX]
```

相关声明：[mqtt_topic_alias](P076_mqtt_topic_alias_结构体.md)、[topic_aliases](#a897895965adaf781b3a426dd53da10a2)。

内部使用（Internal）。

<a id="r_ad41631ca4fbbae32e0a7042515c90ea9"></a>

```c
enum mqtt_disconnect_reason_code disconnect_reason
```

相关声明：[mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)、[disconnect_reason](#ad41631ca4fbbae32e0a7042515c90ea9)。

内部使用（Internal）。

## 59.2\_详细说明（Detailed Documentation）

<a id="ad41631ca4fbbae32e0a7042515c90ea9"></a>

### `disconnect_reason`

```c
enum mqtt_disconnect_reason_code mqtt_internal::disconnect_reason
```

内部使用（Internal）。

处理出错时设置的MQTT 5.0断开连接原因（Disconnect Reason）。

<a id="a8f30cb1440efecf8ae8fc448e4f462f8"></a>

### `last_activity`

```c
uint32_t mqtt_internal::last_activity
```

内部使用（Internal）。

上次活动发生的墙上时钟值（Wall Clock Value），单位为毫秒；周期性PING需要使用它。

<a id="af866a252b9e18496c8e1627704d8a8b2"></a>

### `mutex`

```c
struct sys_mutex mqtt_internal::mutex
```

内部使用（Internal）。

保护客户端实例访问的互斥锁（Mutex）。

<a id="a921477a9839447f4fe1c823911680c92"></a>

### `remaining_payload`

```c
uint32_t mqtt_internal::remaining_payload
```

内部使用（Internal）。

剩余待读取的载荷长度（Payload Length）。

<a id="a45aeafd71dadaf1d0fd0bc3969c921de"></a>

### `rx_buf_datalen`

```c
uint32_t mqtt_internal::rx_buf_datalen
```

内部使用（Internal）。

截至目前已读取的数据包长度（Packet Length）。

<a id="acf93a973de5a5430e767e2996f1cd048"></a>

### `state`

```c
uint32_t mqtt_internal::state
```

内部使用（Internal）。

客户端在连接中的状态（State）。

<a id="a897895965adaf781b3a426dd53da10a2"></a>

### `topic_aliases`

```c
struct mqtt_topic_alias mqtt_internal::topic_aliases[CONFIG_MQTT_TOPIC_ALIAS_MAX]
```

内部使用（Internal）。

MQTT 5.0主题别名映射（Topic Alias Mapping）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [sys_mutex](../userspace_sync_reference/P004_用户模式互斥量结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mqtt_topic_alias](P076_mqtt_topic_alias_结构体.md)
- [mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_mqtt_evt_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_mqtt_puback_param_结构体.md)
