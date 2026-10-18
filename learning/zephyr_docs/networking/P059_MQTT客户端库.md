---
id: learning.zephyr-docs.networking.page-59
title: MQTT客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mqtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_MQTT客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mqtt.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 59.1 概览（Overview）

消息队列遥测传输（Message Queuing Telemetry Transport，MQTT）是运行在 TCP/IP 协议栈之上的应用层协议，为机器间通信（Machine-to-Machine Communication）提供轻量级发布／订阅（Publish/Subscribe）消息传输。协议介绍见[MQTT 官方网站](https://mqtt.org/)。

Zephyr 的 MQTT 客户端库建立在 BSD 套接字 API（BSD Sockets API）之上，通过 [`CONFIG_MQTT_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_LIB) 启用。可以逐个客户端配置，支持 MQTT 3.1.0、3.1.1 和 5.0。既可以使用普通 TCP 套接字，也可以使用 TLS 安全套接字。TCP 是传输控制协议（Transmission Control Protocol），TLS 是传输层安全（Transport Layer Security），接口说明见[BSD 套接字指南](P040_BSD套接字.md#bsd-sockets-interface)。

MQTT 客户端连接的服务器称为消息代理（MQTT Broker），负责管理客户端订阅并分发客户端发布的消息。代理有多种实现，其中之一是 Eclipse Mosquitto，详见[Mosquitto 官方网站](https://mosquitto.org/)。

## 59.2 使用示例（Sample Usage）

先定义客户端上下文（Client Context）及缓冲区（Buffer）：

```c
/* Buffers for MQTT client. */
static uint8_t rx_buffer[256];
static uint8_t tx_buffer[256];

/* MQTT client context */
static struct mqtt_client client_ctx;
```

应用可以创建多个客户端实例，分别管理。还需要保存代理地址的结构体；它必须在客户端整个生命周期内保持有效，可以由多个客户端共享：

```c
/* MQTT Broker address information. */
static struct net_sockaddr_storage broker;
```

客户端库通过回调函数（Callback）向应用通知 MQTT 事件：

```c
void mqtt_evt_handler(struct mqtt_client *client,
                      const struct mqtt_evt *evt)
{
   switch (evt->type) {
      /* Handle events here. */
   }
}
```

可能的事件见[MQTT 客户端 API 参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)。使用之前，需要初始化并配置上下文。下面是普通 TCP 传输的配置：

```c
mqtt_client_init(&client_ctx);

/* MQTT client configuration */
client_ctx.broker = &broker;
client_ctx.evt_cb = mqtt_evt_handler;
client_ctx.client_id.utf8 = (uint8_t *)"zephyr_mqtt_client";
client_ctx.client_id.size = sizeof("zephyr_mqtt_client") - 1;
client_ctx.password = NULL;
client_ctx.user_name = NULL;
client_ctx.protocol_version = MQTT_VERSION_3_1_1;
client_ctx.transport.type = MQTT_TRANSPORT_NON_SECURE;

/* MQTT buffers configuration */
client_ctx.rx_buf = rx_buffer;
client_ctx.rx_buf_size = sizeof(rx_buffer);
client_ctx.tx_buf = tx_buffer;
client_ctx.tx_buf_size = sizeof(tx_buffer);
```

配置完成后，调用 `mqtt_connect`。它创建相应套接字，建立 TCP／TLS 连接并发送 `MQTT CONNECT` 消息。收到响应后，应用调用 `mqtt_input` 处理；由于它是非阻塞（Non-blocking）函数，应使用套接字 `poll` 等待数据到达。连接成功时，通过回调报告 `MQTT_EVT_CONNACK`：

```c
rc = mqtt_connect(&client_ctx);
if (rc != 0) {
   return rc;
}

fds[0].fd = client_ctx.transport.tcp.sock;
fds[0].events = ZSOCK_POLLIN;
poll(fds, 1, 5000);

mqtt_input(&client_ctx);

if (!connected) {
   mqtt_abort(&client_ctx);
}
```

回调应在连接成功时设置 `connected` 标志。如果 MQTT 层连接失败或等待超时，例子调用 `mqtt_abort` 中止连接并关闭底层套接字。

> 译注：这是说明片段，代理地址的实际填写、`fds` 与 `connected` 的定义以及回调中的成功判断由应用补齐。这里访问 `client_ctx.transport.tcp.sock`，对应前面的普通 TCP 配置；TLS 配置应使用相应的传输描述符。官方[发布者源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_publisher/src/main.c)分别处理 TCP 和 TLS 套接字。实际应用还应检查 `poll()` 与输入处理返回值，不能把“已发送 CONNECT”当作“代理已接受连接”。

连接建立后，应用需定期调用 `mqtt_input` 处理接收数据，并调用 `mqtt_live` 维持连接。收到 MQTT 消息时，库调用回调报告相应事件。通过 `mqtt_disconnect` 关闭连接。

完整用法见[MQTT 发布者示例](P060_MQTT发布者示例.md#mqtt-publisher)。

## 59.3 使用 TLS（Using MQTT with TLS）

选择安全传输类型 `MQTT_TRANSPORT_SECURE`，并补充 TLS 配置：

```c
client_ctx.transport.type = MQTT_TRANSPORT_SECURE;

struct mqtt_sec_config *tls_config = &client_ctx.transport.tls.config;

tls_config->peer_verify = TLS_PEER_VERIFY_REQUIRED;
tls_config->cipher_list = NULL;
tls_config->sec_tag_list = m_sec_tags;
tls_config->sec_tag_count = ARRAY_SIZE(m_sec_tags);
tls_config->hostname = MQTT_BROKER_HOSTNAME;
tls_config->set_native_tls = true;
```

其中，`m_sec_tags` 是安全标签（Security Tag）数组，引用用于身份验证的 TLS 凭据。`cipher_list` 设为 `NULL`，表示允许使用系统中可用的全部密码套件（Cipher Suite）。`hostname` 设置为代理主机名，用于服务器身份验证；`peer_verify` 要求校验对端证书（Peer Certificate）。

`m_sec_tags` 引用的凭据必须事先注册到系统，方法见[安全套接字文档](P040_BSD套接字.md#secure-sockets-interface)。

还可以设置 `set_native_tls`，启用原生 TLS（Native TLS），由 Zephyr 处理 TLS，而不是将它交给卸载套接字（Offloaded Socket）。[MQTT 发布者示例](P060_MQTT发布者示例.md#mqtt-publisher)也包含 TLS 用法。

## 59.4 API 参考与相关示例（API Reference）

完整参考见[MQTT 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)；本指南与详细参考页分别跟踪翻译状态。

| 示例 | 用途 |
| --- | --- |
| [AWS IoT Core MQTT](P216_AWS物联网MQTT示例.md#aws-iot-mqtt) | 连接 AWS IoT Core，通过 MQTT 发布消息 |
| [Microsoft Azure IoT Hub MQTT](P217_Azure物联网MQTT示例.md#mqtt-azure) | 连接 Azure IoT Hub，通过 MQTT 发布消息 |
| [MQTT 发布者](P060_MQTT发布者示例.md#mqtt-publisher) | 向 MQTT 服务器发送 `PUBLISH` 消息 |
| [安全 MQTT 传感器／执行器](P061_安全MQTT传感器与执行器示例.md#secure-mqtt-sensor-actuator) | 实现基于 MQTT 的物联网（Internet of Things，IoT）传感器／执行器设备 |

本轮未连接消息代理、发布消息或验证 TLS 通信。


<a id="mqtt"></a>
<a id="mqtt-socket-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="using-mqtt-with-tls"></a>
<a id="api-reference"></a>
<a id="mqtt-api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HTTP服务器库](P055_HTTP服务器库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：MQTT_SN客户端库](P062_MQTT_SN客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P058_多线程HTTP服务器示例.md) · [返回大纲](大纲.md) · [下一章](P060_MQTT发布者示例.md)

</details>

<!-- reading-navigation:end -->
