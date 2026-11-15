---
id: learning.zephyr-docs.log-transport-reference.page-5
title: MQTT日志后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__mqtt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_MQTT日志后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__mqtt_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙低功耗、MQTT、网络与WebSocket后端的接口和头文件源码。源码跟踪译注与官方原文分开标示。

MQTT日志后端的头文件。

<a id="details"></a>

```c
#include <zephyr/net/mqtt.h>
```

查看此文件的源码。

MQTT日志后端的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga75e1b3fb99bb8211eaa684fcaa41882a"></a>

```c
int log_backend_mqtt_client_set (struct mqtt_client *client)
```

相关声明：[log_backend_mqtt_client_set](P004_MQTT日志后端接口.md#ga75e1b3fb99bb8211eaa684fcaa41882a)、[mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)。

设置MQTT客户端实例，以便向代理发布应用的日志消息。

<a id="r_gaad9f9b8fe0c67093e41732b525922bee"></a>

```c
int log_backend_mqtt_topic_set (const char *topic)
```

相关声明：[log_backend_mqtt_topic_set](P004_MQTT日志后端接口.md#gaad9f9b8fe0c67093e41732b525922bee)。

设置用于发布日志消息的MQTT主题（Topic）。

## 5.2\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_mqtt.h](../../../include/zephyr/logging/log_backend_mqtt.h)、[subsys/logging/backends/log_backend_mqtt.c](../../../subsys/logging/backends/log_backend_mqtt.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中的官方main文件；所有本地链接均为相对路径。

> 译注——源码核对：客户端连接（Client Connection）由应用建立和维护，后端只借用客户端指针发布日志；client_set不会进行连接握手，也不会处理网络输入、保活或重连。客户端对象必须在使用期间持续有效。

> 译注——源码核对：当前client_set先停用后端，非NULL时再以所给客户端上下文启用，返回0；传NULL会保持停用。源码未在此验证连接状态，返回0不能证明代理可达或客户端已完成连接。

> 译注——源码核对：主题（Topic）设置保存传入指针，不复制字符串；当前实现只拒绝NULL或空字符串，并不在此完整校验UTF-8与代理长度限制。原文中的有效UTF-8和长度要求仍由调用者满足，不能用临时栈字符串作为长期主题。

> 译注——源码核对：当前发送路径忽略mqtt_publish返回值并返回已处理长度，所以一次日志调用没有提供MQTT交付确认。panic回调设置标志后停止本后端继续处理消息；这不等于自动切换到可靠的同步网络发送。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [查看此文件的源码](P006_MQTT日志后端头文件源码.md)
- [log_backend_mqtt_client_set](P004_MQTT日志后端接口.md#ga75e1b3fb99bb8211eaa684fcaa41882a)
- [mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)
- [log_backend_mqtt_topic_set](P004_MQTT日志后端接口.md#gaad9f9b8fe0c67093e41732b525922bee)

<a id="header-details"></a>

---

[上一章](P004_MQTT日志后端接口.md) · [返回大纲](大纲.md) · [下一章](P006_MQTT日志后端头文件源码.md)
