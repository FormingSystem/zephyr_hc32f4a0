---
id: learning.zephyr-docs.network-application-model-reference.page-68
title: mqtt_sn_connect_retry_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__connect__retry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_mqtt\_sn\_connect\_retry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__connect__retry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于存储待完成连接（CONNECT）状态的结构。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

用于存储待完成连接（CONNECT）状态的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a63ad57a516060561cdb8368fc39b95bf"></a>

```c
atomic_t state
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[state](#a63ad57a516060561cdb8368fc39b95bf)。

待处理CONNECT的状态，类型为enum mqtt_sn_connect_state。

<a id="r_a0bc18dbe3eeb1d0f40df40c7043e30dd"></a>

```c
uint8_t retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retries](#a0bc18dbe3eeb1d0f40df40c7043e30dd)。

CONNECT尝试失败后的重试次数（Retries）。

<a id="r_adc9e9a043233d291ce6a5cd02e22e16f"></a>

```c
int64_t last_attempt
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[last_attempt](#adc9e9a043233d291ce6a5cd02e22e16f)。

上次CONNECT尝试的时间戳（Timestamp）。

<a id="r_a5224c27cbd657bae4e1dbbbc01bac2bd"></a>

```c
bool will
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[will](#a5224c27cbd657bae4e1dbbbc01bac2bd)。

待处理mqtt_sn_connect()调用中的遗嘱标志（Will Flag），重试时再次发送。

<a id="r_ad863eef56bb80ea87a3924d4b00995a6"></a>

```c
bool clean_session
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[clean_session](#ad863eef56bb80ea87a3924d4b00995a6)。

待处理mqtt_sn_connect()调用中的清理会话标志（Clean Session Flag），重试时再次发送。

## 68.2\_详细说明（Detailed Documentation）

<a id="ad863eef56bb80ea87a3924d4b00995a6"></a>

### `clean_session`

```c
bool mqtt_sn_connect_retry::clean_session
```

待处理mqtt_sn_connect()调用中的清理会话标志（Clean Session Flag），重试时再次发送。

<a id="adc9e9a043233d291ce6a5cd02e22e16f"></a>

### `last_attempt`

```c
int64_t mqtt_sn_connect_retry::last_attempt
```

上次CONNECT尝试的时间戳（Timestamp）。

<a id="a0bc18dbe3eeb1d0f40df40c7043e30dd"></a>

### `retries`

```c
uint8_t mqtt_sn_connect_retry::retries
```

CONNECT尝试失败后的重试次数（Retries）。

<a id="a63ad57a516060561cdb8368fc39b95bf"></a>

### `state`

```c
atomic_t mqtt_sn_connect_retry::state
```

待处理CONNECT的状态，类型为enum mqtt_sn_connect_state。

<a id="a5224c27cbd657bae4e1dbbbc01bac2bd"></a>

### `will`

```c
bool mqtt_sn_connect_retry::will
```

待处理mqtt_sn_connect()调用中的遗嘱标志（Will Flag），重试时再次发送。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mqtt_sn_connect()](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8c2a525f1c30e5d5ff37180d33a76d4d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_mqtt_sn_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_mqtt_sn_data_结构体.md)
