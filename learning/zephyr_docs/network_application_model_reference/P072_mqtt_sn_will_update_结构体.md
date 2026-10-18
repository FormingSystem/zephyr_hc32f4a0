---
id: learning.zephyr-docs.network-application-model-reference.page-72
title: mqtt_sn_will_update_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__will__update.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_mqtt\_sn\_will\_update\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__will__update.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于存储遗嘱更新（Will Update）状态的结构。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

用于存储遗嘱更新（Will Update）状态的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a4d154a06ee21a2ac606642443b8aab98"></a>

```c
bool in_progress
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[in_progress](#a4d154a06ee21a2ac606642443b8aab98)。

需要发送一条更新消息（Update Message）。

<a id="r_a5563460ce89861a00f4f2a8056c67068"></a>

```c
uint8_t retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retries](#a5563460ce89861a00f4f2a8056c67068)。

更新尝试失败后的重试次数（Retries）。

<a id="r_a329934f8b34ccea260e429c815fe8ea6"></a>

```c
int64_t last_attempt
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[last_attempt](#a329934f8b34ccea260e429c815fe8ea6)。

上次更新尝试的时间戳（Timestamp）。

## 72.2\_详细说明（Detailed Documentation）

<a id="a4d154a06ee21a2ac606642443b8aab98"></a>

### `in_progress`

```c
bool mqtt_sn_will_update::in_progress
```

需要发送一条更新消息（Update Message）。

<a id="a329934f8b34ccea260e429c815fe8ea6"></a>

### `last_attempt`

```c
int64_t mqtt_sn_will_update::last_attempt
```

上次更新尝试的时间戳（Timestamp）。

<a id="a5563460ce89861a00f4f2a8056c67068"></a>

### `retries`

```c
uint8_t mqtt_sn_will_update::retries
```

更新尝试失败后的重试次数（Retries）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_mqtt_sn_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_mqtt_suback_param_结构体.md)
