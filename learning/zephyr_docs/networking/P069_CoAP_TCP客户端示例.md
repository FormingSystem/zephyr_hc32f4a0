---
id: learning.zephyr-docs.networking.page-69
title: CoAP_TCP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/coap_client_tcp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_CoAP_TCP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/coap_client_tcp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 69.1 概览（Overview）

本示例展示如何使用 CoAP over TCP 客户端 API，通过 RFC 8323 定义的可靠传输（Reliable Transport）与服务器通信。所选平台须具备网络能力，必要时调整配置。可[浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_client_tcp/README.rst/..)。

示例涵盖连接 TCP 服务器；使用事件回调等待能力与设置消息（Capabilities and Settings Message，CSM）交换完成；通过 TCP 发送 GET；使用 Ping/Pong 信令并基于事件等待；正常释放会话（Graceful Session Release）；通过回调接收服务器的 Release／Abort 信号。

## 69.2 运行要求（Requirements）

先按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)、[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备网络。开发板与运行服务器的主机之间须能通信，并提供支持 TCP 的 CoAP 服务器，例如[aiocoap](https://github.com/chrysn/aiocoap)。

## 69.3 构建与运行（Building and Running）

最方便的方式是按 native_sim 联网指南构建并运行原生模拟应用。主机须先运行支持 TCP 的服务器。下面保留原页使用 aiocoap 的命令；在 Linux 主机选定的可写工作目录中，安装依赖并创建服务器使用的 `file_root/test` 文件：

```shell
python -m pip install "aiocoap[all]"
mkdir file_root
echo "Hello from CoAP TCP!" > file_root/test
aiocoap-fileserver --bind "coap+tcp://[::]:5683" file_root
```

> 译注：原例给 `--bind` 传入完整的 `coap+tcp://` URI。aiocoap 的[命令说明](https://aiocoap.readthedocs.io/en/latest/module/aiocoap.cli.fileserver.html)将此参数描述为绑定主机／端口，详细格式应按所安装版本的 `--help-bind` 核对，不能把本页命令保留等同于已验证该参数兼容。`file_root` 是上述命令创建的服务器目录，不是 Zephyr 原有源码目录。

另开终端，在已取得的 `net-tools` 目录运行 `net-setup.sh`：

```shell
./net-setup.sh
```

再在 Zephyr 源码根目录构建并运行客户端：

```shell
west build -b native_sim samples/net/sockets/coap_client_tcp
west build -t run
```

## 69.4 配置（Configuration）

服务器地址、端口和请求路径通过 Kconfig 或 `src/main.c` 调整：

| 参数 | 含义 |
| --- | --- |
| [`CONFIG_NET_CONFIG_PEER_IPV4_ADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_PEER_IPV4_ADDR) | 服务器 IPv4 地址 |
| `PEER_PORT` | 服务器端口，默认 `5683` |
| `RESOURCE_PATH` | 请求资源路径，默认 `"test"` |

| Kconfig 选项 | 作用 |
| --- | --- |
| [`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OVER_RELIABLE_TRANSPORT) | 启用 CoAP over TCP 支持 |
| [`CONFIG_COAP_CLIENT_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_TCP) | 启用 CoAP TCP 客户端 |
| [`CONFIG_COAP_CLIENT_MESSAGE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MESSAGE_SIZE) | 最大消息尺寸 |

> 源码核对译注：当前 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_client_tcp/src/main.c) 构造 IPv4 地址，并以 `IPPROTO_TCP` 连接。CSM 与 Pong 分别等待最多 5 秒，GET 响应等待最多 30 秒；本例并不因为协议支持 TLS 就自动执行 TLS 握手。

## 69.5 相关参考（See Also）

- [CoAP 客户端示例](P068_CoAP客户端示例.md#coap-client)与[CoAP 服务示例](P072_CoAP服务示例.md#coap-server)。
- [RFC 8323：CoAP over TCP、TLS 和 WebSockets](https://tools.ietf.org/html/rfc8323)。
- [aiocoap](https://github.com/chrysn/aiocoap)。
- [CoAP 基础库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)与[CoAP TCP 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html)。

本轮未安装 aiocoap、启动服务器、建立网桥、构建或测试 TCP 会话。


<a id="coap-client-tcp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="configuration"></a>
<a id="see-also"></a>

[上一章](P068_CoAP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P070_CoAP下载示例.md)
