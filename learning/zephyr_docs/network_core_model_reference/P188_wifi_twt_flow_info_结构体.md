---
id: learning.zephyr-docs.network-core-model-reference.page-188
title: wifi_twt_flow_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__twt__flow__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_wifi\_twt\_flow\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__twt__flow__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi目标唤醒时间流（TWT Flow）的信息。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi目标唤醒时间流（TWT Flow）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 188.1\_数据成员（Data Fields）

<a id="r_ae15ba49fa54f82cc6a1fb0d4572114b7"></a>

```c
uint64_t twt_interval
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[twt_interval](#ae15ba49fa54f82cc6a1fb0d4572114b7)。

间隔（Interval）＝唤醒时间（Wake up time）＋睡眠时间（Sleeping time）。

<a id="r_a123ce10bed8b62b01919a7ea7644a0ba"></a>

```c
uint8_t dialog_token
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dialog_token](#a123ce10bed8b62b01919a7ea7644a0ba)。

对话令牌（Dialog token），用于将请求映射到响应。

<a id="r_acb0c618f1cebcb172f342cfe222683be"></a>

```c
uint8_t flow_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flow_id](#acb0c618f1cebcb172f342cfe222683be)。

流标识符（Flow ID），用于将建立操作（Setup）与拆除操作（Teardown）对应起来。

<a id="r_a620ae8ba546e4091d74280cb1553b2cf"></a>

```c
enum wifi_twt_negotiation_type negotiation_type
```

相关声明：[wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)、[negotiation_type](#a620ae8ba546e4091d74280cb1553b2cf)。

目标唤醒时间协商类型（TWT negotiation type），参见枚举 `wifi_twt_negotiation_type`。

<a id="r_ac82e4de8ffc82f851061f8ba8d217dc1"></a>

```c
bool responder
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[responder](#ac82e4de8ffc82f851061f8ba8d217dc1)。

请求方或响应方（Requestor or responder）。

<a id="r_a952a67bd092c5dadba387bb13449c6f3"></a>

```c
bool trigger
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[trigger](#a952a67bd092c5dadba387bb13449c6f3)。

启用或禁用触发（Trigger enabled or disabled）。

<a id="r_afb480be82d1c6f351bd634fd83bfa5c7"></a>

```c
bool implicit
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[implicit](#afb480be82d1c6f351bd634fd83bfa5c7)。

隐式或显式（Implicit or explicit）。

<a id="r_afc81a5111c265fd9bb2aca5f9510bfa8"></a>

```c
bool announce
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[announce](#afc81a5111c265fd9bb2aca5f9510bfa8)。

通告或不通告（Announced or unannounced）。

<a id="r_aede6cb0cfc999fac8ded49e2981a3762"></a>

```c
uint32_t twt_wake_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[twt_wake_interval](#aede6cb0cfc999fac8ded49e2981a3762)。

唤醒时间（Wake up time）。

<a id="r_a6384d3829d54a58a53eafcb74c64a658"></a>

```c
uint32_t twt_wake_ahead_duration
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[twt_wake_ahead_duration](#a6384d3829d54a58a53eafcb74c64a658)。

提前唤醒时长（Wake ahead duration）。

## 188.2\_详细说明（Detailed Documentation）

<a id="afc81a5111c265fd9bb2aca5f9510bfa8"></a>

### `announce`

```c
bool wifi_twt_flow_info::announce
```

通告或不通告（Announced or unannounced）。

<a id="a123ce10bed8b62b01919a7ea7644a0ba"></a>

### `dialog_token`

```c
uint8_t wifi_twt_flow_info::dialog_token
```

对话令牌（Dialog token），用于将请求映射到响应。

<a id="acb0c618f1cebcb172f342cfe222683be"></a>

### `flow_id`

```c
uint8_t wifi_twt_flow_info::flow_id
```

流标识符（Flow ID），用于将建立操作（Setup）与拆除操作（Teardown）对应起来。

<a id="afb480be82d1c6f351bd634fd83bfa5c7"></a>

### `implicit`

```c
bool wifi_twt_flow_info::implicit
```

隐式或显式（Implicit or explicit）。

<a id="a620ae8ba546e4091d74280cb1553b2cf"></a>

### `negotiation_type`

```c
enum wifi_twt_negotiation_type wifi_twt_flow_info::negotiation_type
```

目标唤醒时间协商类型（TWT negotiation type），参见枚举 `wifi_twt_negotiation_type`。

<a id="ac82e4de8ffc82f851061f8ba8d217dc1"></a>

### `responder`

```c
bool wifi_twt_flow_info::responder
```

请求方或响应方（Requestor or responder）。

<a id="a952a67bd092c5dadba387bb13449c6f3"></a>

### `trigger`

```c
bool wifi_twt_flow_info::trigger
```

启用或禁用触发（Trigger enabled or disabled）。

<a id="ae15ba49fa54f82cc6a1fb0d4572114b7"></a>

### `twt_interval`

```c
uint64_t wifi_twt_flow_info::twt_interval
```

间隔（Interval）＝唤醒时间（Wake up time）＋睡眠时间（Sleeping time）。

<a id="a6384d3829d54a58a53eafcb74c64a658"></a>

### `twt_wake_ahead_duration`

```c
uint32_t wifi_twt_flow_info::twt_wake_ahead_duration
```

提前唤醒时长（Wake ahead duration）。

<a id="aede6cb0cfc999fac8ded49e2981a3762"></a>

### `twt_wake_interval`

```c
uint32_t wifi_twt_flow_info::twt_wake_interval
```

唤醒时间（Wake up time）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 188.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P187_wifi_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P189_wifi_twt_params_结构体.md)
