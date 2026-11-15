---
id: learning.zephyr-docs.log-transport-reference.page-6
title: MQTT日志后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__mqtt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_MQTT日志后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__mqtt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_MQTT日志后端头文件参考.md)和[公共API](P004_MQTT日志后端接口.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__log__backend__mqtt_html_ga75e1b3fb99bb8211eaa684fcaa41882a"></a>
<a id="agroup__log__backend__mqtt_html_gaad9f9b8fe0c67093e41732b525922bee"></a>
<a id="amqtt_8h_html"></a>
<a id="astructmqtt__client_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Arif Balik &lt;arifbalik@outlook.com&gt;
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_MQTT_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_MQTT_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/net/mqtt.h&gt;
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00028"></a>
<a id="l00048"></a>int log_backend_mqtt_client_set(struct mqtt_client *client);
<a id="l00049"></a>
<a id="l00064"></a>int log_backend_mqtt_topic_set(const char *topic);
<a id="l00065"></a>
<a id="l00069"></a>
<a id="l00070"></a>#ifdef __cplusplus
<a id="l00071"></a>}
<a id="l00072"></a>#endif
<a id="l00073"></a>
<a id="l00074"></a>#endif /* ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_MQTT_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Arif Balik <arifbalik@outlook.com>；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_MQTT_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `log_backend_mqtt_client_set`

```c
int log_backend_mqtt_client_set(struct mqtt_client *client)
```

设置MQTT客户端实例，以便向代理发布应用的日志消息。

符号定位：[log_backend_mqtt_client_set](P004_MQTT日志后端接口.md#ga75e1b3fb99bb8211eaa684fcaa41882a)。

### `log_backend_mqtt_topic_set`

```c
int log_backend_mqtt_topic_set(const char *topic)
```

设置用于发布日志消息的MQTT主题（Topic）。

符号定位：[log_backend_mqtt_topic_set](P004_MQTT日志后端接口.md#gaad9f9b8fe0c67093e41732b525922bee)。

### `mqtt.h`

MQTT客户端实现（MQTT Client Implementation）。

符号定位：[mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)。

### `mqtt_client`

用于维护客户端相关信息的MQTT客户端定义。

定义位置（Definition）：mqtt.h:954。

符号定位：[mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)。

## 6.4\_源码跟踪译注

> 译注——客户端连接（Client Connection）由应用建立和维护，后端只借用客户端指针发布日志；client_set不会进行连接握手，也不会处理网络输入、保活或重连。客户端对象必须在使用期间持续有效。

> 译注——当前client_set先停用后端，非NULL时再以所给客户端上下文启用，返回0；传NULL会保持停用。源码未在此验证连接状态，返回0不能证明代理可达或客户端已完成连接。

> 译注——主题（Topic）设置保存传入指针，不复制字符串；当前实现只拒绝NULL或空字符串，并不在此完整校验UTF-8与代理长度限制。原文中的有效UTF-8和长度要求仍由调用者满足，不能用临时栈字符串作为长期主题。

> 译注——当前发送路径忽略mqtt_publish返回值并返回已处理长度，所以一次日志调用没有提供MQTT交付确认。panic回调设置标志后停止本后端继续处理消息；这不等于自动切换到可靠的同步网络发送。

头文件定位：[include/zephyr/logging/log_backend_mqtt.h](../../../include/zephyr/logging/log_backend_mqtt.h)，关联实现／接口：[subsys/logging/backends/log_backend_mqtt.c](../../../subsys/logging/backends/log_backend_mqtt.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_backend_mqtt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/log_backend_mqtt.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_MQTT日志后端头文件参考.md)
- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)
- [log_backend_mqtt_client_set](P004_MQTT日志后端接口.md#ga75e1b3fb99bb8211eaa684fcaa41882a)
- [mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)
- [log_backend_mqtt_topic_set](P004_MQTT日志后端接口.md#gaad9f9b8fe0c67093e41732b525922bee)

---

[上一章](P005_MQTT日志后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_网络日志后端接口.md)
