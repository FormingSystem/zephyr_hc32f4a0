---
id: learning.zephyr-docs.network-application-model-reference.page-70
title: mqtt_sn_evt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__evt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_mqtt\_sn\_evt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__evt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由事件回调处理的MQTT-SN事件结构（Event Structure）。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

由事件回调处理的MQTT-SN事件结构（Event Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_aef636c6acdc17831acb44095fbef1885"></a>

```c
enum mqtt_sn_evt_type type
```

相关声明：[mqtt_sn_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaa52518be4aa308dda9552e14d0045c42)、[type](#aef636c6acdc17831acb44095fbef1885)。

事件类型（Event Type）。

<a id="r_a8e75d71d1b38e1b84bf1ad20063ec4e8"></a>

```c
union mqtt_sn_evt_param param
```

相关声明：[mqtt_sn_evt_param](P092_mqtt_sn_evt_param_联合体.md)、[param](#a8e75d71d1b38e1b84bf1ad20063ec4e8)。

事件参数（Event Parameters）。

## 70.2\_详细说明（Detailed Documentation）

<a id="a8e75d71d1b38e1b84bf1ad20063ec4e8"></a>

### `param`

```c
union mqtt_sn_evt_param mqtt_sn_evt::param
```

事件参数（Event Parameters）。

<a id="aef636c6acdc17831acb44095fbef1885"></a>

### `type`

```c
enum mqtt_sn_evt_type mqtt_sn_evt::type
```

事件类型（Event Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [mqtt_sn_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaa52518be4aa308dda9552e14d0045c42)
- [mqtt_sn_evt_param](P092_mqtt_sn_evt_param_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_mqtt_sn_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_mqtt_sn_transport_结构体.md)
