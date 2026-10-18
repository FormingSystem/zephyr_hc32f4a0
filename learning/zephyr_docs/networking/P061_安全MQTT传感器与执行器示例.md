---
id: learning.zephyr-docs.networking.page-61
title: 安全MQTT传感器与执行器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/secure_mqtt_sensor_actuator/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_安全MQTT传感器与执行器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/secure_mqtt_sensor_actuator/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 61.1 概览（Overview）

本示例实现物联网（Internet of Things，IoT）传感器／执行器（Sensor/Actuator）设备。应用通过消息队列遥测传输（Message Queuing Telemetry Transport，MQTT）向远端消息代理（Broker）安全发送传感器数据，并响应收到的 MQTT 命令。

示例功能包括：通过 DHCPv4 租约建立网络连接；使用 TLS 1.2 安全连接 MQTT Broker；按用户设置的周期发布 JSON 温度数据；订阅用户指定的主题；响应网络命令控制 LED；管理 MQTT 连接、重连与保活（Keep-alive）；通过网络状态 LED 指示连接。

DHCPv4 是动态主机配置协议第四版（Dynamic Host Configuration Protocol for IPv4），TLS 是传输层安全（Transport Layer Security），JSON 是 JavaScript 对象表示法（JavaScript Object Notation），LED 是发光二极管（Light-Emitting Diode）。可[在 GitHub 浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/secure_mqtt_sensor_actuator/README.rst/..)。

## 61.2 运行要求与硬件（Requirements and Hardware Setup）

需要具备联网能力的开发板、[Eclipse Mosquitto MQTT Broker](https://mosquitto.org/download/)、DHCP 服务器，以及开发板与代理之间的网络连接。原文在 `adi_eval_adin1110ebz` 上测试过。

代理可以部署在本地主机，也可使用[公共 Mosquitto 测试服务](https://test.mosquitto.org/)。示例还提供静态 IP、无 TLS 的本地快速测试配置。

使用以太网时，把开发板连接到本地代理所在 PC，或连接到互联网路由器以访问公共代理。若需要，另接温度传感器。

## 61.3 软件准备（Software Setup）

温度传感器应在设备树（Devicetree）中设置别名 `ambient-temp0`。没有板载温度传感器时，可外接传感器，并用板级叠加文件（Board Overlay）添加节点和别名。原文片段如下：

```devicetree
/ {
        aliases {
                        ambient-temp0 = &adt7420;
                };
        };
};
```

> 译注：上面的原始片段末尾多了一个 `};`。根节点与 `aliases` 两层各关闭一次即可；同时 `adt7420` 必须是已定义并正确连接的节点标签，单独增加别名并不会创建传感器节点。官方 [`src/device.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/src/device.c) 通过 `DT_ALIAS(ambient_temp0)` 查找它。

也可以使用其他类型传感器：在设备树添加对应节点，并修改 `device.c` 中的 `SENSOR_CHAN`，使其与传感器类型匹配。当前源码文件实际位于 `src/device.c`。

| 配置文件 | 模式 |
| --- | --- |
| `prj.conf` | 默认配置：安全 MQTT，DHCP 动态 IP |
| `overlay-static.conf` | 安全 MQTT，静态 IP |
| `overlay-static-insecure.conf` | 无 TLS 的 MQTT，静态 IP |

### 默认配置（Default Config）

默认通过 DHCP 获取地址，并尝试使用 TLS 1.2 连接代理。[`CONFIG_NET_SAMPLE_MQTT_BROKER_HOSTNAME`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/Kconfig) 指定代理，默认是 `test.mosquitto.org`。

TLS 连接需要把代理的 CA 证书编入应用。CA 是证书颁发机构（Certificate Authority）：

1. 从[测试代理网站](https://test.mosquitto.org)下载 DER 或 PEM 格式证书。
2. 将证书内容写入 `tls_config/cert.h` 的 `ca_certificate[]`。当前官方文件位于 [`src/tls_config/cert.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/src/tls_config/cert.h)。
3. 开发板连接到互联网路由器后，通过 DHCP 获取 IPv4 地址，再尝试连接公共代理并发布数据。

DER 是可辨别编码规则（Distinguished Encoding Rules），PEM 是隐私增强邮件（Privacy-Enhanced Mail）证书文本格式。

也可安全连接本地代理，但需要配置证书，并按上述方式将 CA 证书加入构建。将 [`CONFIG_NET_SAMPLE_MQTT_BROKER_HOSTNAME`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/Kconfig) 设置为本地代理的主机名／IP。根据证书类型，还可能需要启用额外的 Mbed TLS 选项，可通过 Kconfig 或自定义 Mbed TLS 配置文件设置，原文指向 `modules/mbedtls/Kconfig`。本地 Mosquitto TLS 设置见[官方 TLS 说明](https://mosquitto.org/man/mosquitto-tls-7.html)。

主机可安装 DHCP 服务器为开发板分配地址，原文举例为 Linux 的 dnsmasq 或 Windows 的 DHCP Server for Windows。使用默认配置构建：

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator
```

### 静态 IP 配置（Static IP Config）

叠加 `overlay-static.conf` 禁用 DHCP，改用静态地址。设备、网关和 DNS 服务器地址须按本地网络配置。DNS 是域名系统（Domain Name System）。

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator -- -DCONF_FILE="prj.conf overlay-static.conf"
```

### 静态 IP、无 TLS 配置（Static IP/Unsecure MQTT Config）

`overlay-static-insecure.conf` 同时禁用 TLS 和 DHCP，连接本地 Mosquitto。文件中填写开发板地址和代理地址，也就是主机以太网接口地址；两者应在同一子网，例如 `192.0.2.1` 与 `192.0.2.2`。

在主机安装 Mosquitto，并创建 `unsecure.conf`：

```conf
listener 1883 0.0.0.0
allow_anonymous true
```

按这个配置启动代理：

```shell
$ sudo mosquitto -v -c unsecure.conf
```

用快速测试配置构建：

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator -- -DCONF_FILE="prj.conf overlay-static-insecure.conf"
```

所有构建路径均相对于 Zephyr 源码根目录；`$` 为主机 Shell 提示符。

## 61.4 使用示例（Using the Sample）

开发板与代理建立 MQTT 连接后，网络 LED 点亮，并按 [`CONFIG_NET_SAMPLE_MQTT_PUBLISH_INTERVAL`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/Kconfig) 周期发布 JSON 传感器读数。该示例私有选项的单位为秒，见官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/Kconfig)。

使用 Mosquitto 订阅传感器数据：

```shell
$ mosquitto_sub -d -h <test.mosquitto.org/local broker IP> -t zephyr_sample/sensor
```

应用同时订阅 [`CONFIG_NET_SAMPLE_MQTT_SUB_TOPIC_CMD`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/secure_mqtt_sensor_actuator/Kconfig) 指定的命令主题。收到支持的字符串后，调用相应命令处理函数（Command Handler）。`device.c` 中（原文 `in device.c`）定义的命令为：

| 命令 | 操作 |
| --- | --- |
| `led_on` | 点亮开发板 LED |
| `led_off` | 熄灭开发板 LED |

通过主机向代理发布命令：

```shell
$ mosquitto_pub -d -h <test.mosquitto.org/local broker IP> --cafile <path/to/ca.crt> -t zephyr_sample/command -m "led_on"
```

> 译注：尖括号内容是需要替换的代理地址或证书路径，不是命令字面参数。上方订阅命令没有提供 TLS 配置，带 `--cafile` 的发布命令则使用证书配置；主机客户端与开发板是分别连接代理的两个端点，应按各自实际监听端口和传输方式设置。原命令保留，本轮未执行发布或 LED 操作。

MQTT 发布和订阅使用的服务质量（Quality of Service，QoS）级别可通过 Kconfig 配置。

## 61.5 示例输出（Sample Output）

```text
*** Booting Zephyr OS build v3.6.0-2212-g2c9c4f3733e9 ***
[00:00:00.181,000] <inf> app_device: Device adt7420@48 is ready
[00:00:00.181,000] <inf> app_device: Device leds is ready
[00:00:00.181,000] <inf> app_main: MAC Address: 00:E0:FE:FE:DA:C8
[00:00:00.181,000] <inf> app_main: Bringing up network..
[00:00:00.801,000] <inf> net_dhcpv4: Received: 192.168.1.17
[00:00:00.801,000] <inf> app_main: Network connectivity up!
[00:00:00.818,000] <inf> app_mqtt: Connecting to MQTT broker @ 91.121.93.94
[00:00:01.154,000] <inf> net_mqtt: Connect completed
[00:00:01.197,000] <inf> app_mqtt: Connected to MQTT broker!
[00:00:01.197,000] <inf> app_mqtt: Hostname: test.mosquitto.org
[00:00:01.198,000] <inf> app_mqtt: Client ID: adi_eval_adin1110ebz_9a
[00:00:01.198,000] <inf> app_mqtt: Port: 8883
[00:00:01.198,000] <inf> app_mqtt: TLS: Enabled
[00:00:01.198,000] <inf> app_mqtt: Subscribing to 1 topic(s)
[00:00:01.238,000] <inf> app_mqtt: SUBACK packet ID: 5841
[00:00:04.200,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:04.319,000] <inf> app_mqtt: PUBACK packet ID: 1
[00:00:07.202,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:07.323,000] <inf> app_mqtt: PUBACK packet ID: 2
[00:00:10.204,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:10.322,000] <inf> app_mqtt: PUBACK packet ID: 3
[00:00:12.769,000] <inf> app_mqtt: MQTT payload received!
[00:00:12.769,000] <inf> app_mqtt: topic: 'zephyr_sample/command', payload: led_on
[00:00:12.770,000] <inf> app_device: Executing device command: led_on
```

以上是官方原页的历史输出，包含 Zephyr 版本、传感器初始化、联网、发布和命令处理，不是本轮设备日志。

## 61.6 相关参考（See Also）

参见[MQTT 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)、[传感器接口（Sensor API）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)与[JSON 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__json.html)。本轮未搭建代理／DHCP 服务、下载固件、读取传感器或控制设备。


<a id="secure-mqtt-sensor-actuator"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="build-and-running"></a>
<a id="hardware-setup"></a>
<a id="software-setup"></a>
<a id="using-the-sample"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P060_MQTT发布者示例.md) · [返回大纲](大纲.md) · [下一章](P062_MQTT_SN客户端库.md)
