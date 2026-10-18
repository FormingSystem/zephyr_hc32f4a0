---
id: learning.zephyr-docs.networking.page-62
title: MQTT_SN客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mqtt_sn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_MQTT_SN客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mqtt_sn.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 62.1 概览（Overview）

面向传感器网络的 MQTT（MQTT for Sensor Networks，MQTT-SN）是 [MQTT](P059_MQTT客户端库.md#mqtt-socket-interface) 协议的一种变体。与 MQTT 不同，它不要求传输控制协议（Transmission Control Protocol，TCP），可以运行在任何基于消息的传输（Message-based Transport）之上。最初主要考虑 ZigBee，也可以使用蓝牙（Bluetooth）、用户数据报协议（User Datagram Protocol，UDP），甚至通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

Zephyr 提供基于 BSD 套接字 API 的 MQTT-SN 客户端库，通过 [`CONFIG_MQTT_SN_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_SN_LIB) 启用。可以逐客户端配置，支持 MQTT-SN 1.2。实现允许适配各种基于消息的传输，并已内置 UDP 支持。

客户端连接 MQTT-SN 网关（Gateway），由它在 MQTT-SN 与 MQTT 之间转换。Eclipse Paho 提供一种[MQTT-SN 网关实现](https://www.eclipse.org/paho/index.php?page=components/mqtt-sn-transparent-gateway/index.php)，也存在其他实现。规范见[MQTT-SN v1.2](https://www.oasis-open.org/committees/download.php/66091/MQTT-SN_spec_v1.2.pdf)。

## 62.2 客户端与传输初始化（Sample Usage）

先定义客户端上下文（Client Context）和缓冲区：

```c
/* Buffers for MQTT client. */
static uint8_t rx_buffer[256];
static uint8_t tx_buffer[256];

/* MQTT-SN client context */
static struct mqtt_sn_client client;
```

应用可以创建并独立管理多个实例。还需要传输结构体；库提供 UDP 实现。原文定义如下：

```c
/* MQTT Broker address information. */
static struct mqtt_sn_transport tp;
```

库通过回调（Callback）通知事件：

```c
static void evt_cb(struct mqtt_sn_client *client,
                   const struct mqtt_sn_evt *evt)
{
   switch(evt->type) {
   {
      /* Handle events here. */
   }
}
```

> 译注：原文回调的 `switch` 内多写了一个左花括号，不能直接作为完整 C 程序编译。应补齐各事件分支并保持括号配对。可能的事件见[MQTT-SN 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html)。

使用前初始化并配置上下文，原文 UDP 示例为：

```c
struct mqtt_sn_data client_id = MQTT_SN_DATA_STRING_LITERAL("ZEPHYR");
struct net_sockaddr_in gateway = {0};

uint8_t tx_buf[256];
uint8_t rx_buf[256];

mqtt_sn_transport_udp_init(&tp, (struct net_sockaddr*)&gateway, sizeof((gateway)));

mqtt_sn_client_init(&client, &client_id, &tp.tp, evt_cb, tx_buf, sizeof(tx_buf), rx_buf, sizeof(rx_buf));
```

> 源码核对译注：官方 [`mqtt_sn.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/mqtt_sn.h) 中，`mqtt_sn_transport_udp_init()` 接收 `struct mqtt_sn_transport_udp *`，其中的 `tp` 成员才是通用 `struct mqtt_sn_transport`。因此前面的声明应为 `static struct mqtt_sn_transport_udp tp;`，才能与这里的 `&tp`、`&tp.tp` 配合。`gateway` 也应预先填好地址族、地址和端口，不能仅保留清零值。客户端、传输对象和缓冲区须在使用期间保持有效。

## 62.3 查找网关并连接（Gateway Discovery and Connection）

配置后，必须确定网关地址。MQTT-SN 提供通告（Advertisement）和搜索（Search）机制，应用至少采用以下一种方式：

1. 调用 [`mqtt_sn_add_gw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd38840ebc78217a692748afb704b42b) 手动登记网关地址。
2. 等待 [`MQTT_SN_EVT_ADVERTISE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672) 事件。
3. 调用 [`mqtt_sn_search()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafdf80b1de5d1b069b2f75b2bd688416f)，等待 [`MQTT_SN_EVT_GWINFO`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a) 回调，并定期调用 [`mqtt_sn_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49) 处理接收消息。

搜索示例：

```c
err = mqtt_sn_search(&mqtt_client, 1);
k_sleep(K_SECONDS(10));
err = mqtt_sn_input(&mqtt_client);
__ASSERT(err == 0, "mqtt_sn_search() failed %d", err);
```

> 译注：这个片段使用 `mqtt_client`，前面的客户端变量叫 `client`；实际应用应统一名称。原例在搜索后休眠十秒，再调用输入函数，并用同一 `err` 覆盖前一步结果；正式代码应分别检查每次调用，不能把最后的断言当成已验证搜索和网关发现成功。

地址已登记或发现后，通过 [`mqtt_sn_connect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8c2a525f1c30e5d5ff37180d33a76d4d) 发送 MQTT-SN `CONNECT` 消息。应用应定期调用 [`mqtt_sn_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49) 处理响应；如果能确认没有数据，例如某些蓝牙传输场景，可以不调用。原文说明，传输结构包含兼容 [`poll()`](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html#afa7e83ddea0ab5b08fcf614b89ac48ba) 的函数指针时，[`mqtt_sn_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49) 为非阻塞（Non-blocking）操作。连接成功后，回调通知 [`MQTT_SN_EVT_CONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)。

```c
err = mqtt_sn_connect(&client, false, true);
__ASSERT(err == 0, "mqtt_sn_connect() failed %d", err);

while (1) {
        mqtt_sn_input(&client);
        if (connected) {
                mqtt_sn_publish(&client, MQTT_SN_QOS_0, &topic_p, false, &pubdata);
        }
        k_sleep(K_MSEC(500));
}
```

该片段先建立网关连接，再发布消息；`connected` 应由成功连接事件更新。MQTT 层连接失败或超时会中止连接并报告错误。

连接后，需要周期性处理接收数据；连接保活由 `k_work` 工作项（Work Item）自动完成，收到消息后回调报告相应事件。

> 源码核对译注：原文这一段误写为调用 [`mqtt_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2dbc3c158d63a6f57b362be94c22660a)，那是 MQTT 客户端接口。这里应继续调用 [`mqtt_sn_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49)；官方 [`mqtt_sn.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/mqtt_sn.c) 实现了 MQTT-SN 输入与保活工作项。传输接口头文件还要求：即使未提供 `poll` 指针，接收实现也不应阻塞，不能因为省略轮询函数就任意改成阻塞接收。

用 [`mqtt_sn_disconnect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gab9cba16f8ce06f606ee81e0d34deb862) 关闭协议连接，但它不会影响传输本身。若还要关闭套接字等底层传输，应调用 [`mqtt_sn_client_deinit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga67d69e4e3f00b31b5ea3b37fb6d653b1)，它也会反初始化传输。

完整示例见[MQTT-SN 发布者](P063_MQTT_SN发布者示例.md#mqtt-sn-publisher)。

## 62.4 与标准的差异（Deviations from the Standard）

原文列出的尚未支持部分是转发器封装（Forwarder Encapsulation）。

## 62.5 API 参考（API Reference）

完整接口见[MQTT-SN 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html)。相关的[MQTT-SN 发布者示例](P063_MQTT_SN发布者示例.md#mqtt-sn-publisher)向网关发送 `PUBLISH` 消息。指南与详细 API 参考分别跟踪；本轮未运行网关搜索、连接或发布测试。


<a id="mqtt-sn"></a>
<a id="mqtt-sn-socket-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="deviations-from-the-standard"></a>
<a id="api-reference"></a>
<a id="mqtt-sn-api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MQTT客户端库](P059_MQTT客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：CoAP协议库](P064_CoAP协议库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P061_安全MQTT传感器与执行器示例.md) · [返回大纲](大纲.md) · [下一章](P063_MQTT_SN发布者示例.md)

</details>

<!-- reading-navigation:end -->
