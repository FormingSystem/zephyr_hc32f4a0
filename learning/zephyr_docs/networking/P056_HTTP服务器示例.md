---
id: learning.zephyr-docs.networking.page-56
title: HTTP服务器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/http_server/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_HTTP服务器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/http_server/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 56.1 概览（Overview）

本示例展示[HTTP 服务器库（HTTP Server Library）](P055_HTTP服务器库.md#http-server-interface)的用法。库提供高层函数，简化服务器实现。它支持 HTTP/1.1，以及升级到 HTTP/2 或直接使用 HTTP/2。

启用 [`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC) 后，还可支持 HTTP/3。原文说明可以从 HTTP/1.1 转向 HTTP/3，也可以直接使用 HTTP/3。网络 Shell 的 `net http services` 命令可显示每个服务支持的 HTTP 协议。HTTP 是超文本传输协议（Hypertext Transfer Protocol）。

> 源码核对译注：HTTP/3 使用单独的 QUIC 连接，不是把原有 TCP 字节流直接改成 HTTP/3。官方 [`http_server_core.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_server_core.c) 还检查 `CONFIG_HTTP_SERVER_VERSION_3` 和服务 TLS 凭据；不能把“只设置 QUIC”理解为任意服务就自动具备可用的 HTTP/3 配置。

## 56.2 前置要求与配置（Requirements and Configuration）

准备 [QEMU 联网](P009_QEMU联网概览.md)环境。译注：原文的 QEMU Networking 链接使用旧的 `connectivity/networking` 路径，这里改为对应译文，其来源指向当前官方 `services/connectivity/networking` 页面。

[示例目录](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server)提供下列配置；也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/http_server/README.rst/..)。

| 文件 | 用途 |
| --- | --- |
| [`prj.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/prj.conf) | 标准默认配置 |
| [`ieee802154-overlay.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/ieee802154-overlay.conf) | 添加 IEEE 802.15.4 支持 |
| [`overlay-usbd.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/overlay-usbd.conf) | 添加 USB 网络连接支持 |
| [`overlay-tls.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/overlay-tls.conf) | 构建 HTTPS 版本 |
| [`overlay-dhcpv4.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/overlay-dhcpv4.conf) | 启用动态主机配置协议第四版（Dynamic Host Configuration Protocol for IPv4，DHCPv4）客户端 |

## 56.3 构建与运行服务器（Building and Running the Server）

构建并运行 HTTP 服务器：

```shell
$ west build -p auto -b <board_to_use> -t run samples/net/sockets/http_server
```

HTTPS 版本：

```shell
$ west build -p auto -b <board_to_use> -t run --test samples/net/sockets/http_server/sample.net.sockets.https.server
```

`<board_to_use>` 是实际目标占位符；`-t run` 适用于提供运行目标的环境，实板需要相应的烧录步骤。`$` 是提示符，示例路径相对于 Zephyr 源码根目录。

服务器启动后，可以从主机用 HTTP/1.1 或 HTTP/2 发起请求：

| 协议与工具 | 原文访问方式 |
| --- | --- |
| HTTP/1.1，浏览器 | `http://192.0.2.1/` |
| HTTP/1.1，curl | `curl -v --compressed http://192.0.2.1/` |
| HTTP/1.1，Apache Bench | `ab -n10 http://192.0.2.1/` |
| HTTP/2，nghttp | `nghttp -v --no-dep http://192.0.2.1/` |
| HTTP/2，curl | `curl --http2 -v --compressed http://192.0.2.1/` |
| HTTP/2，h2load | `h2load -n10 http://192.0.2.1/` |

### 浏览器中的 HTTP/2 与证书

浏览器对 HTTP/2 使用更严格的安全设置。应在 HTTPS 构建基础上启用应用层协议协商（Application-Layer Protocol Negotiation，ALPN），并使服务器证书由浏览器信任的证书颁发机构（Certificate Authority，CA）签发。

原文写作在 west 构建命令添加 `-DCONFIG_NET_SAMPLE_HTTPS_USE_ALPN`。译注：实际 CMake 配置参数需要值，例如在 `--` 后使用 `-DCONFIG_NET_SAMPLE_HTTPS_USE_ALPN=y`；该示例选项定义见官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/Kconfig)。

原文建议生成自己的 CA 证书：

```shell
$ west build -b <board_to_use> -t sample_ca_cert samples/net/sockets/http_server
```

再生成由该 CA 签名的服务器证书：

```shell
$ west build -t sample_server_cert samples/net/sockets/http_server
```

随后用新生成的证书和密钥构建应用：

```shell
$ west build samples/net/sockets/http_server
```

把 CA 证书加入浏览器信任机构列表，才能按此方案使用 HTTP/2。原文还提到，Firefox 可能需要把 `network.http.http2.enforce-tls-profile` 设为 `false`，并将原因描述为 Firefox 对未知机构签发的 CA 证书可能按 HTTP/2 安全错误处理。

> 译注：这是保留的上游浏览器兼容性说明，未在当前浏览器验证，不把关闭 TLS 检查当作通用前提。本轮未生成密钥、修改浏览器配置或系统信任库。官方 [CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/CMakeLists.txt) 中的证书目标会在示例证书目录运行生成脚本，读者执行前应区分该操作与普通编译。

## 56.4 服务器定制（Server Customization）

| 配置 | 原文作用 |
| --- | --- |
| [`CONFIG_NET_SAMPLE_HTTP_SERVER_SERVICE_PORT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/Kconfig) | 设置 HTTP 服务端口 |
| [`CONFIG_HTTP_SERVER_MAX_CLIENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_MAX_CLIENTS) | 服务器能同时处理的客户端上限；原文在这里描述为 HTTP/2 客户端数量 |
| [`CONFIG_HTTP_SERVER_MAX_STREAMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_MAX_STREAMS) | 每个客户端可建立的 HTTP/2 流（Stream）上限 |
| [`CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE) | 每个客户端的缓冲区大小，限制单个 HTTP 请求头的最大长度 |
| [`CONFIG_HTTP_SERVER_MAX_URL_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_MAX_URL_LENGTH) | 服务器可处理的 URL 最大长度 |
| [`CONFIG_NET_SAMPLE_WEBSOCKET_SERVICE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/Kconfig) | 启用 WebSocket 服务端点；原文称客户端连到 `/` 后会收到自身数据的回显 |

> 源码核对译注：当前官方 [`main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/src/main.c) 将回显资源注册在 `/ws_echo`，与下方 Python 示例一致；不能把根路径 `/` 当作回显端点。`CONFIG_HTTP_SERVER_MAX_CLIENTS` 在服务器核心中配置公共客户端上下文池，也不应仅理解为独立于其他 HTTP 版本的专用计数。

运行 `west build -t menuconfig` 打开交互式配置，原文给出的菜单路径是 `-> Subsystems and OS Services -> Networking -> Network Protocols`。示例私有选项还应在该示例的配置项中查找。

### WebSocket 连接（WebSocket Connectivity）

可使用下面的简单客户端测试回显：

```python
import websocket

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://192.0.2.1/ws_echo")
ws.send("Hello, Server")
print(ws.recv())
while True:
  line = input("> ")
  if line == "quit":
    break
  ws.send(line)
  print(ws.recv())
ws.close()
```

它连接 `/ws_echo`，先发送问候，再逐行发送并打印响应，输入 `quit` 后关闭连接。

## 56.5 通过 USB 测试（Testing over USB）

原文用 nRF52840 开发板与 Linux PC 通过 USB 联网演示 HTTP(S) 测试。先构建启用 HTTPS 的示例并烧录，原文给出的构建命令是：

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 samples/net/sockets/http_server/ -- -DCONFIG_NET_SAMPLE_HTTPS_SERVICE=y -DEXTRA_CONF_FILE=overlay-netusb.conf
```

> 源码核对译注：这里的 `overlay-netusb.conf` 已不在当前官方示例目录中。官方 [tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/tests.yaml) 的 USB CDC NCM 配置使用 [`overlay-usbd.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/overlay-usbd.conf)，并额外指定设备树叠加文件（Devicetree Overlay）`usbd_cdc_ncm.overlay`。因此不能只复制旧文件名，需按当前版本组合 USB 与 TLS 配置，构建后再执行板卡对应烧录流程。本轮没有执行实板构建或烧录。

连接 USB 后，用以下命令查看 Linux 分配的 USB 以太网接口名称：

```shell
$ ip link show
```

以下假设名称为 `eth-device`，配置 IP 与路由：

```shell
$ sudo ip addr add 192.0.2.2/24 dev eth-device
$ sudo ip route add 192.0.2.0/24 dev eth-device
```

主机接口选择 `192.0.2.2/24`，与服务器的 [`CONFIG_NET_CONFIG_MY_IPV4_ADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_MY_IPV4_ADDR) 不同，但处于 `/24` 掩码定义的同一网段。原文接着写道“假设 `192.168.0.x` 地址范围不与主机已有地址和路由冲突；若冲突，应修改示例、主机接口和证书中的全部 IP 地址”。

> 译注：上段原文 `192.168.0.x` 与实际命令的 `192.0.2.0/24` 不一致；判断冲突时应以实际选用的网段为准。`eth-device` 是需替换的接口占位名。

配置好后，用 curl 分别测试 HTTP 和 HTTPS：

```shell
$ curl -v --compressed http://192.0.2.1
$ curl -v --compressed https://192.0.2.1
```

> 原文注意事项：要让 HTTPS 连接成功，需要把[示例 CA 证书](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_server/src/certs/ca_cert.pem)加入 Linux 主机的已知 CA 列表。

## 56.6 性能分析（Performance Analysis）

### CPU 使用分析（CPU Usage Profiling）

当服务器运行在 `native_sim` 上时，可用 Linux `perf stat` 收集处理器（Central Processing Unit，CPU）统计：

```shell
$ sudo perf stat -p <pid_of_server>
```

将 `<pid_of_server>` 替换为服务器进程标识（Process ID，PID）。监视期间向服务器发请求，收集足够数据后停止 `perf stat`，它会打印统计摘要。

### 热点分析（Hotspot Analysis）

通过 `perf record` 与 `perf report` 找出消耗最多 CPU 时间的函数：

```shell
$ sudo perf record -g -p <pid_of_server> -o perf.data
```

服务器在负载下运行一段时间，例如使用 ApacheBench 发起请求，然后停止记录并分析：

```shell
$ sudo perf report -i perf.data
```

`perf.data` 保存剖析数据。可以用火焰图（FlameGraph）寻找开销较大的执行路径。先转换数据格式：

```shell
$ sudo perf script | ~/FlameGraph/stackcollapse-perf.pl > out.perf-folded
```

再生成火焰图：

```shell
$ ~/FlameGraph/flamegraph.pl out.perf-folded > flamegraph.svg
```

最后用浏览器打开 `flamegraph.svg`。

> 译注：原文的 `~/FlameGraph` 是脚本安装位置示例，需换成读者实际准备好的工具目录，不要求固定用户名或仓库位置。这里的 SVG 是运行分析命令后生成的结果，原网页没有提供现成火焰图原件；本轮没有编造或代替生成测试结果。

## 56.7 相关参考（See Also）

参见[HTTP 服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html)、[HTTP 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html)、[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)和[JSON 数据接口](https://docs.zephyrproject.org/latest/doxygen/html/group__json.html)。JSON 是 JavaScript 对象表示法（JavaScript Object Notation）。本轮未运行服务器、网络性能测试、USB 联网或 perf 分析。


<a id="sockets-http-server"></a>
<a id="overview"></a>
<a id="requirement"></a>
<a id="building-and-running-the-server"></a>
<a id="server-customization"></a>
<a id="websocket-connectivity"></a>
<a id="testing-over-usb"></a>
<a id="performance-analysis"></a>
<a id="cpu-usage-profiling"></a>
<a id="hotspot-analysis"></a>
<a id="see-also"></a>

[上一章](P055_HTTP服务器库.md) · [返回大纲](大纲.md) · [下一章](P057_简易HTTP服务器示例.md)
