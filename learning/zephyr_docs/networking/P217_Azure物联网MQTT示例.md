---
id: learning.zephyr-docs.networking.page-217
title: Azure物联网MQTT示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/cloud/mqtt_azure/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mqtt-azure"></a>

# 第217章\_Azure物联网MQTT示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/cloud/mqtt_azure/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 217.1 概述（Overview）

本示例演示MQTT客户端如何通过MQTT协议，向Azure云物联网中心（Azure IoT Hub）发布消息。功能包括：

- 获取DHCPv4租约。
- 与Azure IoT Hub建立TLS连接。
- 向Azure云发布数据。
- 支持SOCKS5代理。
- 支持DNS。

源码位于[samples/net/cloud/mqtt_azure](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/mqtt_azure)。

<a id="requirements"></a>

## 217.2 要求（Requirements）

- Azure云账户。
- Azure物联网凭据及所需信息。
- Freedom开发板（FRDM-K64F）。
- 网络连接。

<a id="building-and-running"></a>

## 217.3 构建与运行（Building and Running）

原文说明，此应用已在NXP FRDMK64F上构建并测试。认证到Azure IoT Hub需要证书。原文所列[samples/net/cloud/mqtt_azure/src/digicert.cer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/mqtt_azure/src/digicert.cer)中的证书来自[Azure IoT C SDK的certs.c](https://github.com/Azure/azure-iot-sdk-c/blob/master/certs/certs.c)。

按照自己的Azure IoT Hub配置，在自定义覆盖配置文件（Overlay configuration file）中设置以下Kconfig选项。

`SAMPLE_CLOUD_AZURE_USERNAME`为用户名字段，原文格式如下：

```text
{iothubhostname}/{device_id}/?api-version=2018-06-30,
```

其中`{iothubhostname}`是IoT Hub的完整规范名称（CName）。

- `SAMPLE_CLOUD_AZURE_PASSWORD`：密码字段，使用共享访问签名令牌（Shared Access Signature，SAS token）。
- `SAMPLE_CLOUD_AZURE_CLIENT_ID`：ClientId字段，使用设备标识（Device ID）。
- `SAMPLE_CLOUD_AZURE_HOSTNAME`：IoT Hub主机名。
- `SAMPLE_CLOUD_AZURE_SERVER_ADDR`：Azure MQTT代理的IP地址。
- `SAMPLE_CLOUD_AZURE_SERVER_PORT`：Azure MQTT代理端口。

如果通过代理运行，还需设置：

- `SAMPLE_SOCKS_ADDR`：SOCKS5代理服务器IP地址。
- `SAMPLE_SOCKS_PORT`：SOCKS5代理服务器端口。

在Linux主机打开终端，找到[本示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/mqtt_azure)后，按以下方式构建并烧录：

```sh
west build -b frdm_k64f samples/net/cloud/mqtt_azure -- -DCONF_FILE="prj.conf <overlay.conf>"
west flash
```

> 译注——命令目录与用户名：上面的命令带有完整的[`samples/net/cloud/mqtt_azure`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/mqtt_azure)相对应用路径，因此应从Zephyr源码根目录执行；若已进入应用目录，则应调整应用路径。原用户名格式末尾的逗号是文档标点，不属于MQTT用户名。Kconfig文件中的符号在`.conf`赋值时使用下方示例展示的`CONFIG_`前缀；密码字段是SAS令牌，不是Azure账户登录密码。

也可以通过QEMU测试，详见[与QEMU联网](P009_QEMU联网概览.md#networking-with-qemu)。配置Zephyr及主机NAT／地址伪装，使其能够访问互联网，并使用`overlay-qemu_x86.conf`。QEMU配置未启用DHCP，而是使用静态IP地址。

> 译注——证书与服务版本：本次取得的`digicert.cer`实际包含Baltimore CyberTrust Root，而不是名称相近的DigiCert根证书。解码证书得到的有效期终点为2025-05-12 23:59:00 GMT，已早于本次读取日期。微软当前[IoT Hub MQTT说明](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub)使用DigiCert Global Root G2，并给出`api-version=2021-04-12`用户名格式。这里保留上游旧文件来源与`2018-06-30`原文，复现时须按当前服务要求准备信任根；不要通过关闭证书验证来掩盖过期证书问题。本文未替换源码证书，也未连接真实账户。

<a id="sample-overlay-file"></a>

### 217.3.1 覆盖配置文件示例（Sample overlay file）

Azure IoT Hub及其他参数的覆盖配置模板：

```cfg
CONFIG_SAMPLE_CLOUD_AZURE_USERNAME="<username>"
CONFIG_SAMPLE_CLOUD_AZURE_PASSWORD="<SAS token>"
CONFIG_SAMPLE_CLOUD_AZURE_CLIENT_ID="<device id>"
CONFIG_SAMPLE_CLOUD_AZURE_HOSTNAME="<IoT hub hostname>"
CONFIG_SAMPLE_SOCKS_ADDR="<proxy addr>"
CONFIG_SAMPLE_SOCKS_PORT=<proxy port>
CONFIG_SAMPLE_CLOUD_AZURE_SERVER_ADDR="<server ip addr, if DNS disabled set this>"
CONFIG_SAMPLE_CLOUD_AZURE_SERVER_PORT=<server port, if DNS disabled set this>
```

> 译注——模板与端口：尖括号内均为占位符，应替换成实际值；代理字段只在启用相应功能时使用。当前源码无论是否启用DNS，都从`CONFIG_SAMPLE_CLOUD_AZURE_SERVER_PORT`构造代理连接端口，因此不能将模板中“DNS disabled”的提示理解成启用DNS后完全不需要正确端口配置。

<a id="sample-output"></a>

### 217.3.2 示例输出（Sample output）

以下是原文的FRDM UART控制台输出：

```text
[00:00:03.001,000] <inf> eth_mcux: Enabled 100M full-duplex mode.
[00:00:03.010,000] <dbg> mqtt_azure.main: Waiting for network to setup...
[00:00:03.115,000] <inf> net_dhcpv4: Received: 10.0.0.2
[00:00:03.124,000] <inf> net_config: IPv4 address: 10.0.0.2
[00:00:03.132,000] <inf> net_config: Lease time: 43200 seconds
[00:00:03.140,000] <inf> net_config: Subnet: 255.255.255.0
[00:00:03.149,000] <inf> net_config: Router: 10.0.0.10
[00:00:06.157,000] <dbg> mqtt_azure.try_to_connect: attempting to connect...
[00:00:06.167,000] <dbg> net_sock_tls.tls_alloc: (0x200024f8): Allocated TLS context, 0x20001110
[00:00:19.412,000] <dbg> mqtt_azure.mqtt_event_handler: MQTT client connected!
[00:00:19.424,000] <dbg> mqtt_azure.publish_message: mqtt_publish OK
[00:00:19.830,000] <dbg> mqtt_azure.mqtt_event_handler: PUBACK packet id: 63387
[00:00:31.842,000] <dbg> mqtt_azure.publish_message: mqtt_publish OK
[00:00:51.852,000] <dbg> mqtt_azure.publish_message: mqtt_publish OK
[00:00:51.861,000] <dbg> mqtt_azure.mqtt_event_handler: PUBACK packet id: 38106
```

也可在Azure门户（Azure Portal）查看事件或消息信息。

<a id="cloud-to-device-communication"></a>

### 217.3.3 从云到设备的通信（Cloud to device communication）

在Azure Portal进入物联网设备（IoT devices），选择目标设备；如果配置了多个设备，要选中正确设备。进入向设备发送消息（Message to Device），在消息正文（Message Body）输入文本，然后点击发送消息（Send Message）。详情见[Azure云MQTT文档](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support)。

<a id="see-also"></a>

## 217.4 另请参阅（See also）

[BSD套接字兼容API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[MQTT客户端库（MQTT Client library）](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)、[TLS凭据管理（TLS credentials management）](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)、[随机数API（Random Function APIs）](../data_utilities/P007_随机数接口.md)。


> 译注——实现依据：[samples/net/cloud/mqtt_azure/src/config.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/mqtt_azure/src/config.h)、[samples/net/cloud/mqtt_azure/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/mqtt_azure/src/main.c)、[samples/net/cloud/mqtt_azure/src/digicert.cer](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/mqtt_azure/src/digicert.cer)、[samples/net/cloud/mqtt_azure/overlay-qemu_x86.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/mqtt_azure/overlay-qemu_x86.conf)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/cloud/mqtt_azure/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/mqtt_azure/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/cloud/mqtt_azure/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/cloud/mqtt_azure/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P216_AWS物联网MQTT示例.md) · [返回大纲](大纲.md) · [下一章](P218_TagoIO的HTTP上报示例.md)
