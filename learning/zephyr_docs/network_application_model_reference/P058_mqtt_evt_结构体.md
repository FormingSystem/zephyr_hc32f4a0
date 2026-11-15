---
id: learning.zephyr-docs.network-application-model-reference.page-58
title: mqtt_evt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__evt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_mqtt\_evt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__evt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

定义通知应用的MQTT异步事件（Asynchronous Event）。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

定义通知应用的MQTT异步事件（Asynchronous Event）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a79d7a198d8ed9959bb7aae835b6301c2"></a>

```c
enum mqtt_evt_type type
```

相关声明：[mqtt_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0071fe013b9920711456ef51cc3e6d91)、[type](#a79d7a198d8ed9959bb7aae835b6301c2)。

标识事件（Event）。

<a id="r_aca1085171667c46b2438f66d9227e07c"></a>

```c
union mqtt_evt_param param
```

相关声明：[mqtt_evt_param](P091_mqtt_evt_param_联合体.md)、[param](#aca1085171667c46b2438f66d9227e07c)。

包含随事件提供的参数（Parameters），如有。

<a id="r_aa1a4304d4aa70440ba630f3fe5e76d2f"></a>

```c
int result
```

相关声明：[result](#aa1a4304d4aa70440ba630f3fe5e76d2f)。

事件结果（Event Result）。

## 58.2\_详细说明（Detailed Documentation）

<a id="aca1085171667c46b2438f66d9227e07c"></a>

### `param`

```c
union mqtt_evt_param mqtt_evt::param
```

包含随事件提供的参数（Parameters），如有。

<a id="aa1a4304d4aa70440ba630f3fe5e76d2f"></a>

### `result`

```c
int mqtt_evt::result
```

事件结果（Event Result）。

0或表示失败原因的负错误码，见errno.h。

<a id="a79d7a198d8ed9959bb7aae835b6301c2"></a>

### `type`

```c
enum mqtt_evt_type mqtt_evt::type
```

标识事件（Event）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0071fe013b9920711456ef51cc3e6d91)
- [mqtt_evt_param](P091_mqtt_evt_param_联合体.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_mqtt_disconnect_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_mqtt_internal_结构体.md)
