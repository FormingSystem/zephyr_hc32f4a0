---
id: learning.zephyr-docs.network-application-model-reference.page-91
title: mqtt_evt_param_联合体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmqtt__evt__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_mqtt\_evt\_param\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionmqtt__evt__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

定义随异步事件一起通知应用的事件参数（Event Parameters）。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

定义随异步事件一起通知应用的事件参数（Event Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_aa99a77bbade75b3f450088b32131f87a"></a>

```c
struct mqtt_connack_param connack
```

相关声明：[mqtt_connack_param](P056_mqtt_connack_param_结构体.md)、[connack](#aa99a77bbade75b3f450088b32131f87a)。

随MQTT_EVT_CONNACK事件提供的参数。

<a id="r_a41be40873e1ebb9bf6fbf6dc9566d6ff"></a>

```c
struct mqtt_publish_param publish
```

相关声明：[mqtt_publish_param](P063_mqtt_publish_param_结构体.md)、[publish](#a41be40873e1ebb9bf6fbf6dc9566d6ff)。

随MQTT_EVT_PUBLISH事件提供的参数。

<a id="r_a24bf756db9fa8cc67c0b02c4e2cb602c"></a>

```c
struct mqtt_puback_param puback
```

相关声明：[mqtt_puback_param](P060_mqtt_puback_param_结构体.md)、[puback](#a24bf756db9fa8cc67c0b02c4e2cb602c)。

随MQTT_EVT_PUBACK事件提供的参数。

<a id="r_a3b31e1d94c480b8d0244cc12d1c25524"></a>

```c
struct mqtt_pubrec_param pubrec
```

相关声明：[mqtt_pubrec_param](P064_mqtt_pubrec_param_结构体.md)、[pubrec](#a3b31e1d94c480b8d0244cc12d1c25524)。

随MQTT_EVT_PUBREC事件提供的参数。

<a id="r_a2269e07f580fb65df5f3d0832aa6b3af"></a>

```c
struct mqtt_pubrel_param pubrel
```

相关声明：[mqtt_pubrel_param](P065_mqtt_pubrel_param_结构体.md)、[pubrel](#a2269e07f580fb65df5f3d0832aa6b3af)。

随MQTT_EVT_PUBREL事件提供的参数。

<a id="r_ac3d564095019ccf57c10678a433bc31a"></a>

```c
struct mqtt_pubcomp_param pubcomp
```

相关声明：[mqtt_pubcomp_param](P061_mqtt_pubcomp_param_结构体.md)、[pubcomp](#ac3d564095019ccf57c10678a433bc31a)。

随MQTT_EVT_PUBCOMP事件提供的参数。

<a id="r_af6ce2426884d2faa443b3dfdaa45594c"></a>

```c
struct mqtt_suback_param suback
```

相关声明：[mqtt_suback_param](P073_mqtt_suback_param_结构体.md)、[suback](#af6ce2426884d2faa443b3dfdaa45594c)。

随MQTT_EVT_SUBACK事件提供的参数。

<a id="r_ad040b028ed0aaabcaddedc204fb709d8"></a>

```c
struct mqtt_unsuback_param unsuback
```

相关声明：[mqtt_unsuback_param](P078_mqtt_unsuback_param_结构体.md)、[unsuback](#ad040b028ed0aaabcaddedc204fb709d8)。

随MQTT_EVT_UNSUBACK事件提供的参数。

<a id="r_a6967703ed8a9f58eda8e9a94b5bc1f5f"></a>

```c
struct mqtt_disconnect_param disconnect
```

相关声明：[mqtt_disconnect_param](P057_mqtt_disconnect_param_结构体.md)、[disconnect](#a6967703ed8a9f58eda8e9a94b5bc1f5f)。

随MQTT_EVT_DISCONNECT事件提供的参数。

<a id="r_ad1bb0a46bab0442404e22627bcc6a0ef"></a>

```c
struct mqtt_auth_param auth
```

相关声明：[mqtt_auth_param](P052_mqtt_auth_param_结构体.md)、[auth](#ad1bb0a46bab0442404e22627bcc6a0ef)。

随MQTT_EVT_AUTH事件提供的参数。

## 91.2\_详细说明（Detailed Documentation）

<a id="ad1bb0a46bab0442404e22627bcc6a0ef"></a>

### `auth`

```c
struct mqtt_auth_param mqtt_evt_param::auth
```

随MQTT_EVT_AUTH事件提供的参数。

<a id="aa99a77bbade75b3f450088b32131f87a"></a>

### `connack`

```c
struct mqtt_connack_param mqtt_evt_param::connack
```

随MQTT_EVT_CONNACK事件提供的参数。

<a id="a6967703ed8a9f58eda8e9a94b5bc1f5f"></a>

### `disconnect`

```c
struct mqtt_disconnect_param mqtt_evt_param::disconnect
```

随MQTT_EVT_DISCONNECT事件提供的参数。

<a id="a24bf756db9fa8cc67c0b02c4e2cb602c"></a>

### `puback`

```c
struct mqtt_puback_param mqtt_evt_param::puback
```

随MQTT_EVT_PUBACK事件提供的参数。

<a id="ac3d564095019ccf57c10678a433bc31a"></a>

### `pubcomp`

```c
struct mqtt_pubcomp_param mqtt_evt_param::pubcomp
```

随MQTT_EVT_PUBCOMP事件提供的参数。

<a id="a41be40873e1ebb9bf6fbf6dc9566d6ff"></a>

### `publish`

```c
struct mqtt_publish_param mqtt_evt_param::publish
```

随MQTT_EVT_PUBLISH事件提供的参数。

说明（Note）：PUBLISH事件结构仅包含载荷大小，应忽略载荷数据参数。必须使用mqtt_read_publish_payload函数手动读取载荷内容（Payload Content）。

<a id="a3b31e1d94c480b8d0244cc12d1c25524"></a>

### `pubrec`

```c
struct mqtt_pubrec_param mqtt_evt_param::pubrec
```

随MQTT_EVT_PUBREC事件提供的参数。

<a id="a2269e07f580fb65df5f3d0832aa6b3af"></a>

### `pubrel`

```c
struct mqtt_pubrel_param mqtt_evt_param::pubrel
```

随MQTT_EVT_PUBREL事件提供的参数。

<a id="af6ce2426884d2faa443b3dfdaa45594c"></a>

### `suback`

```c
struct mqtt_suback_param mqtt_evt_param::suback
```

随MQTT_EVT_SUBACK事件提供的参数。

<a id="ad040b028ed0aaabcaddedc204fb709d8"></a>

### `unsuback`

```c
struct mqtt_unsuback_param mqtt_evt_param::unsuback
```

随MQTT_EVT_UNSUBACK事件提供的参数。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_connack_param](P056_mqtt_connack_param_结构体.md)
- [mqtt_publish_param](P063_mqtt_publish_param_结构体.md)
- [mqtt_puback_param](P060_mqtt_puback_param_结构体.md)
- [mqtt_pubrec_param](P064_mqtt_pubrec_param_结构体.md)
- [mqtt_pubrel_param](P065_mqtt_pubrel_param_结构体.md)
- [mqtt_pubcomp_param](P061_mqtt_pubcomp_param_结构体.md)
- [mqtt_suback_param](P073_mqtt_suback_param_结构体.md)
- [mqtt_unsuback_param](P078_mqtt_unsuback_param_结构体.md)
- [mqtt_disconnect_param](P057_mqtt_disconnect_param_结构体.md)
- [mqtt_auth_param](P052_mqtt_auth_param_结构体.md)
- [mqtt_read_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga3559cdd6093d75c6fe6792ec2a453172)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_coap_client_tcp_event_data_联合体.md) · [返回大纲](大纲.md) · [下一章](P092_mqtt_sn_evt_param_联合体.md)
