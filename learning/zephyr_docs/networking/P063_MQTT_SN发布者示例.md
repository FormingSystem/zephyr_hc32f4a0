---
id: learning.zephyr-docs.networking.page-63
title: MQTT_SN发布者示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/mqtt_sn_publisher/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_MQTT_SN发布者示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/mqtt_sn_publisher/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 63.1 概览（Overview）

[MQTT](http://mqtt.org/) 是为小型传感器和移动设备优化的轻量级发布／订阅（Publish/Subscribe）消息协议。面向传感器网络的 MQTT（MQTT for Sensor Networks，MQTT-SN）针对无线通信环境作了调整。

MQTT 要求可靠的 TCP/IP 传输；MQTT-SN 可以使用基于数据报（Datagram）的传输，例如用户数据报协议（User Datagram Protocol，UDP）、ZigBee，甚至配有额外分帧协议（Framing Protocol）的通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

Zephyr MQTT-SN 发布者（Publisher）是 v1.2 客户端，向 MQTT-SN 网关发送 `PUBLISH` 消息，同时通过 `SUBSCRIBE` 订阅主题。规范见[MQTT-SN v1.2 规范](https://www.oasis-open.org/committees/download.php/66091/MQTT-SN_spec_v1.2.pdf)。

源码位于[samples/net/mqtt_sn_publisher](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/mqtt_sn_publisher/README.rst/..)。

## 63.2 运行要求（Requirements）

需要 Linux 主机、MQTT-SN 网关（例如 Eclipse Paho）、支持 MQTT v3.1.1 的 Mosquitto 服务器、Mosquitto 订阅客户端及用于测试的以太网局域网（Local Area Network，LAN）。原文使用 Mosquitto 1.6 测试过，这是历史记录。

## 63.3 构建与运行（Build and Running）

示例支持静态 IP 与网关发现（Gateway Discovery）。在[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher/prj.conf)中按局域网设置地址，通过 [`CONFIG_NET_SAMPLE_MQTT_SN_STATIC_GATEWAY`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher/Kconfig) 选择静态网关或发现流程。

同时需要启动 MQTT-SN 网关。示例提供[Docker Compose 配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher/compose/compose.yaml)。先在[net-tools](https://github.com/zephyrproject-rtos/net-tools)目录启动其网络配置：

```shell
$ ./net-setup.sh --config docker.conf
```

再在另一个终端启动 Docker 环境：

```shell
$ cd ./compose
$ docker compose up
```

> 源码核对译注：第二组命令的 `./compose` 相对于 [`samples/net/mqtt_sn_publisher`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher)，不是 net-tools 目录。官方 [`compose.yaml`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher/compose/compose.yaml) 依赖已经建立的外部网络 `net-tools0`，其中网关为 `192.0.2.2`，Mosquitto 为 `192.0.2.3`。这解释了原文先运行 net-tools、再启动 Compose 的顺序；不要求仓库位于固定盘符。

也可以手工搭建。Paho 可以按[Paho MQTT-SN 网关文档](https://www.eclipse.org/paho/index.php?page=components/mqtt-sn-transparent-gateway/index.php)从源码构建，或使用原文提到的非官方容器镜像[kyberpunk/paho](https://hub.docker.com/r/kyberpunk/paho)。

在 Linux 主机打开三个终端。第一个启动 Mosquitto：

```shell
$ sudo mosquitto -v -p 1883
```

第二个启动网关，例如：

```shell
$ docker run -it -p 10000:10000 -p 10000:10000/udp --name paho -v $PWD/gateway.conf:/etc/paho/gateway.conf:ro kyberpunk/paho
```

> 译注：`$PWD/gateway.conf` 是当前目录中的配置，挂载到容器的 `/etc/paho/gateway.conf`，后者是容器系统路径。官方 [Compose 网关配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_sn_publisher/compose/gateway.conf) 默认使用 `BrokerName=mosquitto`，依赖 Compose 服务名解析；若拿它用于手工部署，应改成该容器实际能访问的代理地址。Mosquitto 2.0 及以上还需配置相应监听器与访问规则，可参照[MQTT 发布者示例](P060_MQTT发布者示例.md)。两套部署方式是原文提供的替代方案，不需要同时启动两套代理和网关。

第三个终端进入 Zephyr 源码根目录，构建并运行：

```shell
west build -b native_sim/native/64 samples/net/mqtt_sn_publisher
west build -t run
```

也可以用任意 MQTT 浏览工具连接代理观察消息。

## 63.4 Wi-Fi

通过[Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)启用 IPv4 Wi-Fi 支持。

## 63.5 示例输出（Sample Output）

原文应用输出：

```text
WARNING: Using a test - not safe - entropy source
*** Booting Zephyr OS build zephyr-v3.2.0-279-gc7fa387cea81  ***
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 172.18.0.20
[00:00:00.000,000] <inf> mqtt_sn_publisher_sample: MQTT-SN sample
[00:00:00.000,000] <inf> mqtt_sn_publisher_sample: Network connected
[00:00:00.000,000] <inf> mqtt_sn_publisher_sample: Waiting for connection...
[00:00:00.000,000] <inf> mqtt_sn_publisher_sample: Connecting client
[00:00:00.510,000] <inf> net_mqtt_sn: Decoding message type: 5
[00:00:00.510,000] <inf> net_mqtt_sn: Got message of type 5
[00:00:00.510,000] <inf> net_mqtt_sn: MQTT_SN client connected
[00:00:00.510,000] <inf> mqtt_sn_publisher_sample: MQTT-SN event EVT_CONNECTED
[00:00:01.020,000] <inf> net_mqtt_sn: Decoding message type: 19
[00:00:01.020,000] <inf> net_mqtt_sn: Got message of type 19
[00:00:10.200,000] <inf> mqtt_sn_publisher_sample: Publishing timestamp
[00:00:10.200,000] <inf> net_mqtt_sn: Registering topic
                                                                        2f 75 70 74 69 6d 65                             |/uptime
[00:00:10.200,000] <inf> net_mqtt_sn: Can't publish; topic is not ready
[00:00:10.710,000] <inf> net_mqtt_sn: Decoding message type: 11
[00:00:10.710,000] <inf> net_mqtt_sn: Got message of type 11
[00:00:10.710,000] <inf> net_mqtt_sn: Publishing to topic ID 14
[00:00:20.400,000] <inf> mqtt_sn_publisher_sample: Publishing timestamp
[00:00:20.400,000] <inf> net_mqtt_sn: Publishing to topic ID 14
```

MQTT-SN 网关输出：

```text
20221024 140210.191   CONNECT           <---  ZEPHYR                              0C 04 04 01 00 3C 5A 45 50 48 59 52
20221024 140210.192   CONNECT           ===>  ZEPHYR                              10 12 00 04 4D 51 54 54 04 02 00 3C 00 06 5A 45 50 48 59 52
20221024 140210.192   CONNACK           <===  ZEPHYR                              20 02 00 00
20221024 140210.192   CONNACK           --->  ZEPHYR                              03 05 00

20221024 140210.643   SUBSCRIBE   0001  <---  ZEPHYR                              0C 12 00 00 01 2F 6E 75 6D 62 65 72
20221024 140210.648   SUBSCRIBE   0001  ===>  ZEPHYR                              82 0C 00 01 00 07 2F 6E 75 6D 62 65 72 00
20221024 140210.660   SUBACK      0001  <===  ZEPHYR                              90 03 00 01 00
20221024 140210.661   SUBACK      0001  --->  ZEPHYR                              08 13 00 00 0D 00 01 00

20221024 140220.338   REGISTER    0002  <---  ZEPHYR                              0D 0A 00 00 00 02 2F 75 70 74 69 6D 65
20221024 140220.348   REGACK      0002  --->  ZEPHYR                              07 0B 00 0E 00 02 00

20221024 140220.848   PUBLISH           <---  ZEPHYR                              0C 0C 00 00 0E 00 00 31 30 32 30 30
20221024 140220.850   PUBLISH           ===>  ZEPHYR                              30 0E 00 07 2F 75 70 74 69 6D 65 31 30 32 30 30

20221024 140230.539   PUBLISH           <---  ZEPHYR                              0C 0C 00 00 0E 00 00 32 30 34 30 30
20221024 140230.542   PUBLISH           ===>  ZEPHYR                              30 0E 00 07 2F 75 70 74 69 6D 65 32 30 34 30 30
```

以上日志为官方原页示例，包含原始版本、时间戳和协议数据；本轮未运行 Docker、建立网桥、启动代理／网关或实际发布消息。

## 63.6 相关参考（See Also）

参见[MQTT-SN 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html)与[MQTT-SN 指南](P062_MQTT_SN客户端库.md)。


<a id="mqtt-sn-publisher"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="build-and-running"></a>
<a id="wi-fi"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P062_MQTT_SN客户端库.md) · [返回大纲](大纲.md) · [下一章](P064_CoAP协议库.md)
