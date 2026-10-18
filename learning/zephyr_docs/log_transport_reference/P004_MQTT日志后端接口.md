---
id: learning.zephyr-docs.log-transport-reference.page-4
title: MQTT日志后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__mqtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_MQTT日志后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__mqtt.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙低功耗、MQTT、网络与WebSocket后端的接口和头文件源码。源码跟踪译注与官方原文分开标示。

向MQTT代理（MQTT Broker）发布消息的日志后端。

<a id="details"></a>

向MQTT代理（MQTT Broker）发布消息的日志后端。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_log_5Fbackend_5Fmqtt_2Eh"></a>

```c
file log_backend_mqtt.h
```

相关声明：[log_backend_mqtt.h](P005_MQTT日志后端头文件参考.md)。

MQTT日志后端的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.2\_函数（Functions）

<a id="r_ga75e1b3fb99bb8211eaa684fcaa41882a"></a>

```c
int log_backend_mqtt_client_set (struct mqtt_client *client)
```

相关声明：[log_backend_mqtt_client_set](#ga75e1b3fb99bb8211eaa684fcaa41882a)、[mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)。

设置MQTT客户端实例，以便向代理发布应用的日志消息。

<a id="r_gaad9f9b8fe0c67093e41732b525922bee"></a>

```c
int log_backend_mqtt_topic_set (const char *topic)
```

相关声明：[log_backend_mqtt_topic_set](#gaad9f9b8fe0c67093e41732b525922bee)。

设置用于发布日志消息的MQTT主题（Topic）。

## 4.3\_详细说明（Detailed Documentation）

<a id="ga75e1b3fb99bb8211eaa684fcaa41882a"></a>

### `log_backend_mqtt_client_set()`

```c
int log_backend_mqtt_client_set ( struct mqtt_client * client)
```

```c
#include <zephyr/logging/log_backend_mqtt.h>
```

设置MQTT客户端实例，以便向代理发布应用的日志消息。

此函数允许应用向日志后端提供由应用自己初始化的MQTT客户端。后端仅使用此客户端通过mqtt_publish()发布日志消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向已初始化并已连接的MQTT客户端的指针。在日志后端的整个使用期间，该客户端必须始终有效。传入NULL可禁用MQTT日志。 |

返回（Returns）：成功时为0，失败时为负错误码。

说明（Note）：调用本函数前，MQTT客户端必须已连接。后端不管理客户端连接，这由应用负责。后端只会使用mqtt_publish()，不会对客户端执行其他操作。

<a id="gaad9f9b8fe0c67093e41732b525922bee"></a>

### `log_backend_mqtt_topic_set()`

```c
int log_backend_mqtt_topic_set ( const char * topic)
```

```c
#include <zephyr/logging/log_backend_mqtt.h>
```

设置用于发布日志消息的MQTT主题（Topic）。

允许应用指定日志后端发布日志消息所使用的MQTT主题（Topic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `topic` | 指向以空字符结尾、包含MQTT主题的字符串的指针。在日志后端的整个使用期间，该主题必须始终有效。 |

返回（Returns）：成功时为0，失败时为负错误码。

说明（Note）：主题必须是有效的UTF-8字符串，以空字符结尾，且不应超过MQTT代理所支持的最大长度。

## 4.4\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_mqtt.h](../../../include/zephyr/logging/log_backend_mqtt.h)、[subsys/logging/backends/log_backend_mqtt.c](../../../subsys/logging/backends/log_backend_mqtt.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中的官方main文件；所有本地链接均为相对路径。

> 译注——源码核对：客户端连接（Client Connection）由应用建立和维护，后端只借用客户端指针发布日志；client_set不会进行连接握手，也不会处理网络输入、保活或重连。客户端对象必须在使用期间持续有效。

> 译注——源码核对：当前client_set先停用后端，非NULL时再以所给客户端上下文启用，返回0；传NULL会保持停用。源码未在此验证连接状态，返回0不能证明代理可达或客户端已完成连接。

> 译注——源码核对：主题（Topic）设置保存传入指针，不复制字符串；当前实现只拒绝NULL或空字符串，并不在此完整校验UTF-8与代理长度限制。原文中的有效UTF-8和长度要求仍由调用者满足，不能用临时栈字符串作为长期主题。

> 译注——源码核对：当前发送路径忽略mqtt_publish返回值并返回已处理长度，所以一次日志调用没有提供MQTT交付确认。panic回调设置标志后停止本后端继续处理消息；这不等于自动切换到可靠的同步网络发送。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [log_backend_mqtt.h](P005_MQTT日志后端头文件参考.md)
- [mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)
- [mqtt_publish()](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙低功耗日志后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_MQTT日志后端头文件参考.md)
