---
id: learning.zephyr-docs.networking.page-60
title: MQTT发布者示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/mqtt_publisher/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_MQTT发布者示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/mqtt_publisher/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 60.1 概览（Overview）

[MQTT](http://mqtt.org/) 是面向小型传感器和移动设备优化的轻量级发布／订阅（Publish/Subscribe）消息协议。原页使用名称 MQ Telemetry Transport，本译文与库指南统一称为消息队列遥测传输（Message Queuing Telemetry Transport，MQTT）。

Zephyr MQTT 发布者（Publisher）示例向消息代理（MQTT Broker）发送 `PUBLISH` 消息，默认支持 MQTT v3.1.1，也可使用 v5.0。规范分别见[MQTT v3.1.1 规范](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html)和[MQTT v5.0 规范](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)。

源码位于[samples/net/mqtt_publisher](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_publisher)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/mqtt_publisher/README.rst/..)。

## 60.2 运行要求（Requirements）

原文测试环境包括 Linux 主机、Freedom 开发板（FRDM-K64F）、支持 MQTT v3.1.1 的 Mosquitto 服务器、Mosquitto 订阅客户端（Subscriber），以及用于测试的以太网局域网（Local Area Network，LAN）。原文验证过的服务器版本为 Mosquitto 1.3.4；这是上游历史测试记录，不是本轮结果。

## 60.3 配置、构建与运行（Build and Running）

原文称示例目前只支持静态 IP 地址。打开 `src/config.h`，按局域网环境设置 IP；也可在 `prj.conf` 中设置。后文 `cc3220sf_launchxl` 分支另行说明它可以使用 DHCP 动态地址。

`src/config.h` 中还可调整下列参数。MQTT 代理 TCP 端口：

```c
#define SERVER_PORT             1883
```

应用休眠时间（毫秒）：

```c
#define APP_SLEEP_MSECS         500
```

最大连接尝试次数：

```c
#define APP_CONNECT_TRIES       10
```

MQTT 客户端标识（Client Identifier）：

```c
#define MQTT_CLIENTID           "zephyr_publisher"
```

示例支持 IBM Bluemix Watson 主题格式（Topic Format），把 `APP_BLUEMIX_TOPIC` 从默认的 `0` 改为 `1` 可启用：

```c
#define APP_BLUEMIX_TOPIC       1
```

主题可以包含设备类型、设备标识、事件类型和消息格式，分别用以下宏指定：

```c
#define BLUEMIX_DEVTYPE         "sensor"
#define BLUEMIX_DEVID           "carbon"
#define BLUEMIX_EVENT           "status"
#define BLUEMIX_FORMAT          "json"
```

MQTT `PUBLISH` 最大迭代次数在 Kconfig 中配置：

```kconfig
CONFIG_NET_SAMPLE_APP_MAX_ITERATIONS=5
```

> 源码核对译注：官方 [`config.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mqtt_publisher/src/config.h) 在启用网络配置库时，从 `CONFIG_NET_CONFIG_PEER_IPV4_ADDR`／`CONFIG_NET_CONFIG_PEER_IPV6_ADDR` 获取 `SERVER_ADDR`。端口也按配置区分：普通 MQTT 默认 `1883`，TLS 默认 `8883`，WebSocket 分支默认 `9001`。上方 `1883` 不是所有传输方式的固定端口。Bluemix 部分保留的是原文主题拼接格式，不表示本轮验证了相应云服务可用。

在 Linux 主机终端找到示例后，构建并烧录：

```shell
west build -b frdm_k64f samples/net/mqtt_publisher
west flash
```

命令中的应用路径相对于 Zephyr 源码根目录。如果开发板通过网线直接连接 Linux 主机，配置对应网卡：

```shell
$ IFACE=eth0 # Change this to the interface to which the LAN cable is connected

$ IPV4_ADDR_1="192.0.2.2/24"
$ IPV4_ROUTE_1="192.0.2.0/24"

$ sudo ip address add $IPV4_ADDR_1 dev $IFACE
$ sudo ip route add $IPV4_ROUTE_1 dev $IFACE
$ sudo ip link set dev $IFACE up
```

`IFACE` 应换成实际接线网卡名称。原文说可通过 `sudo ip addr flush dev $IFACE` 撤销前面的配置。

> 译注：`flush` 会清空指定接口上的地址，并不只撤销本例添加的一项。若只删除本例地址，应针对该地址使用 `ip address del`，并单独处理本例路由。这里保留原命令说明其作用范围，本轮没有更改主机网卡或路由。

对于 Mosquitto 2.0 及以上版本，原文要求在 `mosquitto.conf` 中加入以下配置，以允许示例使用未认证访问（Unauthenticated Access）：

```conf
listener 1883
allow_anonymous true
bind_interface eth0
```

其中 `bind_interface eth0` 也应与实际接口一致。另开终端启动代理，根据版本选择对应命令：

```shell
$ sudo mosquitto -v -p 1883             # For mosquitto < 2.0
$ sudo mosquitto -v -c mosquitto.conf   # For mosquitto >= 2.0
```

再开终端订阅 `sensors` 主题：

```shell
$ mosquitto_sub -t sensors
```

## 60.4 MQTT v5.0 支持（MQTT v5.0 Support）

构建时加入 `-DEXTRA_CONF_FILE=overlay-mqtt-5.conf`，即可使用 v5.0 代替 v3.1.1。示例应可用于支持 v5.0 的代理，原文特别测试过 Mosquitto 2.0.21；该场景的服务器配置与 v3.1.1 相同。

v5.0 模式使用主题别名（Topic Alias）。若代理报告支持主题别名，客户端为默认的 `sensors` 主题注册别名，并在后续 `PUBLISH` 中使用它。可用 Wireshark 观察：完整主题只出现在首条发布消息中，之后消息只携带主题别名属性，体积更小。

## 60.5 TLS 安全连接（Connecting Securely using TLS）

可以自己搭建安全 MQTT 服务器，但需要生成证书并配置服务器。原文还提供通过[公共 Mosquitto 测试代理](https://test.mosquitto.org/)快速试用 TLS 的步骤：

1. 从[测试服务网站](https://test.mosquitto.org)下载 DER 格式的 CA 证书。CA 是证书颁发机构（Certificate Authority），DER 是可辨别编码规则（Distinguished Encoding Rules）。
2. 在 `src/test_certs.h` 中，将证书内容写入 `ca_certificate[]`。若平台使用套接字卸载且 `CONFIG_TLS_CREDENTIAL_FILENAMES=y`，则可设为证书文件名。
3. 在 `src/config.h` 设置 `SERVER_ADDR`。原文给出的 `test.mosquitto.org` IP 是 `"37.187.106.16"`；它是原页示例值，使用前应按实际 DNS 解析结果确认。
4. 在 `src/main.c` 将 `TLS_SNI_HOSTNAME` 设为 `"test.mosquitto.org"`。原文称要与下载证书的通用名称（Common Name，CN）匹配。
5. 构建时加入 `-DEXTRA_CONF_FILE=overlay-tls.conf`；若平台使用 TLS 卸载，见下一节。

> 译注：服务器名称应当对应目标服务器证书中的身份，而不是把 CA 证书自身的 CN 当作目标主机名。Mosquitto 的[官方 TLS 说明](https://mosquitto.org/man/mosquitto-tls-7.html)区分 CA、服务器与客户端证书，并要求服务器证书对应代理主机名。服务器名称指示（Server Name Indication，SNI）与 CA 信任材料承担不同职责。

将生成的固件烧录到设备：

```shell
$ west flash
```

### TLS 卸载（TLS Offloading）

支持卸载的开发板可在 `west build` 或 `cmake` 中指定 `-DEXTRA_CONF_FILE=overlay-tls-offload.conf`。这样启用 TLS，而不把 Mbed TLS 软件实现编入应用。

### SOCKS5 代理（SOCKS5 Proxy）

通过 `-DEXTRA_CONF_FILE=overlay-socks5.conf` 启用 SOCKS5 代理连接。为方便测试，默认假定代理与 MQTT Broker 在同一主机。可使用安全 Shell（Secure Shell，SSH）启动代理：

```shell
$ ssh -N -D 0.0.0.0:1080 localhost
```

代理使用不同 IP 或端口时，修改：

```c
#define SOCKS5_PROXY_ADDR    SERVER_ADDR
#define SOCKS5_PROXY_PORT    1080
```

## 60.6 MQTT 日志后端（MQTT Logging Backend）

示例可以把应用日志发布到 MQTT Broker，并与主应用共用同一个 MQTT 客户端实例。通过 [`log_backend_mqtt_client_set()`](../log_transport_reference/P004_MQTT日志后端接口.md#ga75e1b3fb99bb8211eaa684fcaa41882a) 注册用于发送日志的客户端。

后端只调用客户端的 [`mqtt_publish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7)，不会管理连接生命周期；建立、维护和断开连接仍由应用负责。构建时加入 `-DEXTRA_CONF_FILE=overlay-log-backend-mqtt.conf` 启用。

| 配置 | 含义与原文默认值 |
| --- | --- |
| [`CONFIG_LOG_BACKEND_MQTT_TOPIC_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_MQTT_TOPIC_DEFAULT) | 日志发布主题，默认 `zephyr/logs` |
| [`CONFIG_LOG_BACKEND_MQTT_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_MQTT_QOS) | 日志服务质量（Quality of Service，QoS）级别，默认 `0` |
| [`CONFIG_LOG_BACKEND_MQTT_RETAIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_MQTT_RETAIN) | 是否保留消息（Retain），默认关闭 |
| [`CONFIG_LOG_BACKEND_MQTT_MAX_MSG_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_MQTT_MAX_MSG_SIZE) | 最大日志消息长度，默认 256 字节 |

## 60.7 在 cc3220sf_launchxl 上运行

该板的卸载实现还提供动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）服务，所以示例在该板上使用动态 IP 地址。

默认连接 `config.h` 中 `SERVER_ADDR` 指定的代理。若代理使用 TLS，应启用 TLS 卸载，并用 TI Uniflash 将 DER 格式的 CA 证书写入设备文件系统，文件名为 `ca_cert.der`。

原文还要求在 `main.c` 设置 `TLS_SNI_HOSTNAME`，使 TLS 域名验证匹配证书中的 CN；CA 与服务器身份的区别见前面的译注。参见[CC3220SF LaunchXL](https://docs.zephyrproject.org/latest/boards/ti/cc3220sf_launchxl/doc/index.html#cc3220sf_launchxl)的配网（Provisioning）、快速连接（Fast Connect）及安全套接字卸载（Secure Socket Offload）章节，其中说明了证书烧写。然后按前述方法测试。

## 60.8 示例输出（Sample Output）

以下是原文 FRDM 串口输出，配置为：

```kconfig
CONFIG_NET_SAMPLE_APP_MAX_ITERATIONS=5
```

```text
[dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
[dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:3e:1a:0a
[publisher:233] network_setup: 0 <OK>
[publisher:258] mqtt_init: 0 <OK>
[connect_cb:81] user_data: CONNECTED
[try_to_connect:212] mqtt_tx_connect: 0 <OK>
[publisher:276] try_to_connect: 0 <OK>
[publisher:285] mqtt_tx_pingreq: 0 <OK>
[publisher:290] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBACK> packet id: 1888, user_data: PUBLISH
[publisher:295] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBREC> packet id: 16356, user_data: PUBLISH
[publish_cb:149] <MQTT_PUBCOMP> packet id: 16356, user_data: PUBLISH
[publisher:300] mqtt_tx_publish: 0 <OK>
[publisher:285] mqtt_tx_pingreq: 0 <OK>
[publisher:290] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBACK> packet id: 45861, user_data: PUBLISH
[publisher:295] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBREC> packet id: 53870, user_data: PUBLISH
[publish_cb:149] <MQTT_PUBCOMP> packet id: 53870, user_data: PUBLISH
[publisher:300] mqtt_tx_publish: 0 <OK>
[publisher:285] mqtt_tx_pingreq: 0 <OK>
[publisher:290] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBACK> packet id: 60144, user_data: PUBLISH
[publisher:295] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBREC> packet id: 6561, user_data: PUBLISH
[publish_cb:149] <MQTT_PUBCOMP> packet id: 6561, user_data: PUBLISH
[publisher:300] mqtt_tx_publish: 0 <OK>
[publisher:285] mqtt_tx_pingreq: 0 <OK>
[publisher:290] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBACK> packet id: 38355, user_data: PUBLISH
[publisher:295] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBREC> packet id: 60656, user_data: PUBLISH
[publish_cb:149] <MQTT_PUBCOMP> packet id: 60656, user_data: PUBLISH
[publisher:300] mqtt_tx_publish: 0 <OK>
[publisher:285] mqtt_tx_pingreq: 0 <OK>
[publisher:290] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBACK> packet id: 28420, user_data: PUBLISH
[publisher:295] mqtt_tx_publish: 0 <OK>
[publish_cb:149] <MQTT_PUBREC> packet id: 49829, user_data: PUBLISH
[publish_cb:149] <MQTT_PUBCOMP> packet id: 49829, user_data: PUBLISH
[publisher:300] mqtt_tx_publish: 0 <OK>
[disconnect_cb:101] user_data: DISCONNECTED
[publisher:304] mqtt_tx_disconnect: 0 <OK>

Bye!
```

其中这一行表示检测到错误，随后会发送新的连接消息：

```text
[try_to_connect:220] mqtt_connect: -5 <ERROR>
```

MQTT API 为异步（Asynchronous）接口，输出会随着回调执行而出现。订阅者收到：

```text
$ mosquitto_sub -t sensors
DOORS:OPEN_QoS0
DOORS:OPEN_QoS1
DOORS:OPEN_QoS2
DOORS:OPEN_QoS0
DOORS:OPEN_QoS1
DOORS:OPEN_QoS2
DOORS:OPEN_QoS0
DOORS:OPEN_QoS1
DOORS:OPEN_QoS2
DOORS:OPEN_QoS0
DOORS:OPEN_QoS1
DOORS:OPEN_QoS2
DOORS:OPEN_QoS0
DOORS:OPEN_QoS1
DOORS:OPEN_QoS2
```

MQTT Broker 的输出为：

```text
$ sudo mosquitto -v
1485663791: mosquitto version 1.3.4 (build date 2014-08-17 00:14:52-0300) starting
1485663791: Using default config.
1485663791: Opening ipv4 listen socket on port 1883.
1485663791: Opening ipv6 listen socket on port 1883.
1485663797: New connection from 192.168.1.101 on port 1883.
1485663797: New client connected from 192.168.1.101 as zephyr_publisher (c1, k0).
1485663797: Sending CONNACK to zephyr_publisher (0)
1485663798: Received PINGREQ from zephyr_publisher
1485663798: Sending PINGRESP to zephyr_publisher
1485663798: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
1485663799: Received PUBLISH from zephyr_publisher (d0, q1, r0, m1888, 'sensors', ... (15 bytes))
1485663799: Sending PUBACK to zephyr_publisher (Mid: 1888)
1485663799: Received PUBLISH from zephyr_publisher (d0, q2, r0, m16356, 'sensors', ... (15 bytes))
1485663799: Sending PUBREC to zephyr_publisher (Mid: 16356)
1485663799: Received PUBREL from zephyr_publisher (Mid: 16356)
1485663799: Sending PUBCOMP to zephyr_publisher (Mid: 16356)
1485663800: Received PINGREQ from zephyr_publisher
1485663800: Sending PINGRESP to zephyr_publisher
1485663800: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
1485663801: Received PUBLISH from zephyr_publisher (d0, q1, r0, m45861, 'sensors', ... (15 bytes))
1485663801: Sending PUBACK to zephyr_publisher (Mid: 45861)
1485663801: Received PUBLISH from zephyr_publisher (d0, q2, r0, m53870, 'sensors', ... (15 bytes))
1485663801: Sending PUBREC to zephyr_publisher (Mid: 53870)
1485663801: Received PUBREL from zephyr_publisher (Mid: 53870)
1485663801: Sending PUBCOMP to zephyr_publisher (Mid: 53870)
1485663802: Received PINGREQ from zephyr_publisher
1485663802: Sending PINGRESP to zephyr_publisher
1485663802: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
1485663803: Received PUBLISH from zephyr_publisher (d0, q1, r0, m60144, 'sensors', ... (15 bytes))
1485663803: Sending PUBACK to zephyr_publisher (Mid: 60144)
1485663803: Received PUBLISH from zephyr_publisher (d0, q2, r0, m6561, 'sensors', ... (15 bytes))
1485663803: Sending PUBREC to zephyr_publisher (Mid: 6561)
1485663803: Received PUBREL from zephyr_publisher (Mid: 6561)
1485663803: Sending PUBCOMP to zephyr_publisher (Mid: 6561)
1485663804: Received PINGREQ from zephyr_publisher
1485663804: Sending PINGRESP to zephyr_publisher
1485663804: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
1485663805: Received PUBLISH from zephyr_publisher (d0, q1, r0, m38355, 'sensors', ... (15 bytes))
1485663805: Sending PUBACK to zephyr_publisher (Mid: 38355)
1485663805: Received PUBLISH from zephyr_publisher (d0, q2, r0, m60656, 'sensors', ... (15 bytes))
1485663805: Sending PUBREC to zephyr_publisher (Mid: 60656)
1485663805: Received PUBREL from zephyr_publisher (Mid: 60656)
1485663805: Sending PUBCOMP to zephyr_publisher (Mid: 60656)
1485663806: Received PINGREQ from zephyr_publisher
1485663806: Sending PINGRESP to zephyr_publisher
1485663806: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
1485663807: Received PUBLISH from zephyr_publisher (d0, q1, r0, m28420, 'sensors', ... (15 bytes))
1485663807: Sending PUBACK to zephyr_publisher (Mid: 28420)
1485663807: Received PUBLISH from zephyr_publisher (d0, q2, r0, m49829, 'sensors', ... (15 bytes))
1485663807: Sending PUBREC to zephyr_publisher (Mid: 49829)
1485663807: Received PUBREL from zephyr_publisher (Mid: 49829)
1485663807: Sending PUBCOMP to zephyr_publisher (Mid: 49829)
1485663808: Received DISCONNECT from zephyr_publisher
```

以上日志为官方原页记录，时间戳、版本、返回值与消息均原样保留，不是本轮连接或发布结果。

## 60.9 Wi-Fi 与相关参考

通过[Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)启用 IPv4 Wi-Fi 支持。完整接口见[MQTT 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)。本轮未运行 Mosquitto、启动代理、改动网络、烧录或发布任何消息。


<a id="mqtt-publisher"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="build-and-running"></a>
<a id="mqtt-v5-0-support"></a>
<a id="connecting-securely-using-tls"></a>
<a id="tls-offloading"></a>
<a id="socks5-proxy-support"></a>
<a id="mqtt-logging-backend"></a>
<a id="running-on-cc3220sf-launchxl"></a>
<a id="sample-output"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P059_MQTT客户端库.md) · [返回大纲](大纲.md) · [下一章](P061_安全MQTT传感器与执行器示例.md)
