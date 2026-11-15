---
id: learning.zephyr-docs.networking.page-216
title: AWS物联网MQTT示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/cloud/aws_iot_mqtt/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="aws-iot-mqtt"></a>

# 第216章\_AWS物联网MQTT示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/cloud/aws_iot_mqtt/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 216.1 概述（Overview）

本示例实现一个MQTT客户端，通过MQTT协议向AWS IoT Core发布消息。主要功能包括：

- 获取DHCPv4租约（Lease）。
- 连接SNTP服务器，取得当前时间。
- 与AWS IoT Core服务器建立TLS 1.2连接。
- 订阅AWS IoT Core中的主题（Topic）。
- 向AWS IoT Core发布数据。
- 通过AWS设备资格认证计划（Device Qualification Program，DQP）测试套件，见[Device Qualification Program (DQP)](https://aws.amazon.com/partners/programs/dqp/)。
- 发送和接收保活ping（Keep-alive ping）。
- 使用指数退避（Exponential backoff）算法重试连接。

<a id="requirements"></a>

## 216.2 要求（Requirements）

- 熵源（Entropy source）。
- 能够访问AWS IoT Core的AWS账户。
- AWS凭据与必要信息。
- 网络连接。

<a id="building-and-running"></a>

## 216.3 构建与运行（Building and Running）

原文说明，此应用已在ST NUCLEO-F429ZI与QEMU x86目标上构建并测试。认证到AWS IoT Core需要有效证书与私钥。示例附带转换脚本，用于将证书及私钥嵌入应用。

在AWS IoT Core注册一个物品（Thing），下载证书与私钥，将它们复制到[samples/net/cloud/aws_iot_mqtt/src/creds](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/aws_iot_mqtt/src/creds)目录。运行[samples/net/cloud/aws_iot_mqtt/src/creds/convert_keys.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/aws_iot_mqtt/src/creds/convert_keys.py)，生成`ca.c`、`cert.c`和`key.c`。

> 译注——文件匹配规则：当前脚本只将以`-certificate.pem.crt`结尾的文件转换为`cert.c`，将以`-private.pem.key`结尾的文件转换为`key.c`，并读取同目录下的`AmazonRootCA1.pem`生成`ca.c`。仅把任意名称的文件复制进去，并不能保证被识别；应检查脚本输出及这三个生成文件。脚本路径相对于Zephyr源码根目录，凭据内容不属于公共译文。

根据AWS IoT Core区域、Thing及Device Advisor配置，设置以下Kconfig选项：

- `CONFIG_AWS_ENDPOINT`：AWS IoT Core MQTT代理（Broker）端点，可从AWS IoT Core控制台取得；使用Device Advisor测试套件时，该端点有对应的专用值。
- `CONFIG_AWS_MQTT_PORT`：MQTT代理端口。
- `CONFIG_AWS_THING_NAME`：创建的Thing名称；与证书关联后，作为客户端标识（Client ID）。本例使用`zephyr_sample`。
- `CONFIG_AWS_SUBSCRIBE_TOPIC`：订阅主题。
- `CONFIG_AWS_PUBLISH_TOPIC`：发布主题。
- `CONFIG_AWS_QOS`：订阅与发布使用的服务质量（Quality of Service，QoS）等级。
- `CONFIG_AWS_EXPONENTIAL_BACKOFF`：启用指数退避算法。

更多信息见[AWS IoT Core文档](https://docs.aws.amazon.com/iot/index.html)。

还可以调整固件以通过AWS DQP测试套件：将`CONFIG_AWS_TEST_SUITE_DQP`设为`y`。Device Advisor的更多信息见[AWS IoT Core Device Advisor](https://aws.amazon.com/iot-core/device-advisor/)。

> 译注——验证含义：DQP相关配置是官方示例支持的测试模式；启用它不等于某块板或某个修改后的固件已经通过资格认证。本文保留上游所述支持范围与测试记录，没有运行云端测试。

<a id="mqtt-test-client"></a>

### 216.3.1 MQTT测试客户端（MQTT test client）

在AWS IoT Core控制台打开MQTT测试客户端，订阅`zephyr_sample/data`，并向`zephyr_sample/downlink`发布载荷（Payload）。设备控制台会显示收到的载荷，AWS控制台会在`zephyr_sample/data`主题下显示设备发送的JSON消息。

<a id="sample-output"></a>

### 216.3.2 示例输出（Sample output）

以下是原文所列NUCLEO-F429ZI开发板ST-Link UART输出：

```text
*** Booting Zephyr OS build zephyr-v3.3.0 ***
[00:00:01.626,000] <inf> aws: starting DHCPv4
[00:00:01.969,000] <dbg> aws: sntp_sync_time: Acquired time from NTP server: 1683472436
[00:00:01.977,000] <inf> aws: Resolved: 52.212.60.110:8883
[00:00:03.327,000] <dbg> aws: mqtt_event_cb: MQTT event: CONNACK [0] result: 0
[00:00:03.327,000] <inf> aws: Subscribing to 1 topic(s)
[00:00:03.390,000] <dbg> aws: mqtt_event_cb: MQTT event: SUBACK [7] result: 0
[00:00:03.390,000] <inf> aws: PUBLISHED on topic "zephyr_sample/data" [ id: 1 qos: 0 ], payload: 13 B
[00:00:03.390,000] <dbg> aws: publish_message: Published payload:
                              7b 22 63 6f 75 6e 74 65  72 22 3a 30 7d          |{"counte r":0}
[00:00:11.856,000] <dbg> aws: mqtt_event_cb: MQTT event: PUBLISH [2] result: 0
[00:00:11.856,000] <inf> aws: RECEIVED on topic "zephyr_sample/downlink" [ id: 13 qos: 0 ] payload: 45 / 4096 B
[00:00:11.856,000] <dbg> aws: handle_published_message: Received payload:
                              7b 0a 20 20 22 6d 65 73  73 61 67 65 22 3a 20 22 |{.  "mes sage": "
                              48 65 6c 6c 6f 20 66 72  6f 6d 20 41 57 53 20 49 |Hello fr om AWS I
                              6f 54 20 63 6f 6e 73 6f  6c 65 22 0a 7d          |oT conso le".}
[00:00:11.857,000] <inf> aws: PUBLISHED on topic "zephyr_sample/data" [ id: 2 qos: 0 ], payload: 13 B
[00:00:11.857,000] <dbg> aws: publish_message: Published payload:
                              7b 22 63 6f 75 6e 74 65  72 22 3a 31 7d          |{"counte r":1}
[00:01:11.755,000] <dbg> aws: mqtt_event_cb: MQTT event: 9 result: 0
[00:02:11.755,000] <dbg> aws: mqtt_event_cb: MQTT event: 9 result: 0
```

<a id="run-in-qemu-x86"></a>

### 216.3.3 在QEMU x86中运行（Run in QEMU x86）

本示例也可运行在QEMU x86中。需要在主机配置网络地址转换／地址伪装（NAT／MASQUERADE），详情见[与QEMU联网（Networking with QEMU）](P009_QEMU联网概览.md#networking-with-qemu)。

<a id="see-also"></a>

## 216.4 另请参阅（See also）

[BSD套接字兼容API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[MQTT客户端库（MQTT Client library）](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html)、[DNS解析库（DNS Resolve Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html)、[TLS凭据管理（TLS credentials management）](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)、[JSON](../serialization/P006_JSON接口参考.md)、[SNTP](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html)、[随机数API（Random Function APIs）](../data_utilities/P007_随机数接口.md)。


> 译注——实现依据：[samples/net/cloud/aws_iot_mqtt/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/aws_iot_mqtt/Kconfig)、[samples/net/cloud/aws_iot_mqtt/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/aws_iot_mqtt/src/main.c)、[samples/net/cloud/aws_iot_mqtt/src/creds/convert_keys.py](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/aws_iot_mqtt/src/creds/convert_keys.py)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/cloud/aws_iot_mqtt/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/cloud/aws_iot_mqtt/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/cloud/aws_iot_mqtt/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/cloud/aws_iot_mqtt/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P215_物联网云接入示例目录.md) · [返回大纲](大纲.md) · [下一章](P217_Azure物联网MQTT示例.md)
