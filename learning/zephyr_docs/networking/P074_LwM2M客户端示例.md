---
id: learning.zephyr-docs.networking.page-74
title: LwM2M客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/lwm2m_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_LwM2M客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/lwm2m_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 74.1 概览（Overview）

轻量级机器间通信（Lightweight Machine to Machine，LwM2M）是基于 CoAP／UDP 的应用层协议，面向轻量环境，通过服务器对客户端资源进行读取、写入和执行操作。

本示例使用 Zephyr LwM2M 库，按[OMA LwM2M 技术规范](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf)第 5.3 节“客户端注册接口”（Client Registration Interface）连接服务器。源码位于[samples/net/lwm2m_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client)，也可[浏览官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/lwm2m_client/README.rst/..)。

## 74.2 运行要求（Requirements）

需要 Linux 主机、[Leshan 演示服务器](https://eclipse.org/leshan/)，以及按照[QEMU 以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)、[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)或[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备的网络。

## 74.3 配置文件与基本运行（Building and Running）

[`samples/net/lwm2m_client`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client) 提供多种配置：

| 文件 | 用途 |
| --- | --- |
| `prj.conf` | 标准默认配置 |
| `overlay-bootstrap.conf` | 启用 LwM2M 引导（Bootstrap）支持 |
| `overlay-ot.conf` | 启用 OpenThread 支持 |
| `overlay-dtls.conf` | 通过 Mbed TLS 启用 DTLS |
| `overlay-dtls-cert.conf` | 通过 Mbed TLS 启用基于证书的 DTLS |
| `overlay-queue.conf` | 启用 LwM2M 队列模式（Queue Mode） |
| `overlay-send-scheduler.conf` | 启用发送调度器，并为温度、湿度 IPSO 对象启用缓存 |
| `overlay-tickless.conf` | 避免引擎周期性打断套接字轮询，某些设备上可明显降低功耗 |

> 源码核对译注：当前 [`overlay-tickless.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/overlay-tickless.conf) 启用 `CONFIG_ZVFS_EVENTFD` 和 `CONFIG_LWM2M_TICKLESS`；这里不是停止整个 LwM2M 引擎。[发送调度叠加配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/overlay-send-scheduler.conf)启用 1.1、缓存及调度对象，接入方式见[协议栈指南](P073_LwM2M协议栈.md)。

在 Zephyr 源码根目录构建，替换实际开发板和配置文件：

```shell
west build -b <board to use> samples/net/lwm2m_client -- -DCONF_FILE=<config file to use>
```

最方便的方式是使用默认 `prj.conf` 构建 native_sim 或 QEMU 目标，并先完成对应联网指南中的准备。

在 Linux 主机选定的可写工作目录下载并运行 Leshan 演示服务器，原命令如下：

```shell
$ wget https://ci.eclipse.org/leshan/job/leshan/lastSuccessfulBuild/artifact/leshan-server-demo.jar
$ java -jar ./leshan-server-demo.jar -wp 8080
```

`$` 是主机 Shell 提示符。下载的 JAR 文件位于执行命令的当前目录；它不是 Zephyr 源码预置文件。浏览器打开 `http://localhost:8080` 后，可以观察和管理已连接设备。原文使用持续集成（Continuous Integration，CI）的最新成功构建地址，具体构建及参数可能随版本变化；本轮对两个 Leshan JAR 地址的只读 HEAD 检查均返回 403，保留原址但未确认附件可下载，也没有下载或启动 Java 服务。

在 Zephyr 源码根目录构建并运行 QEMU 版本：

```shell
west build -b qemu_x86 samples/net/lwm2m_client
west build -t run
```

原文说明，示例随后自动连接 Leshan，以 IPv6 客户端端点 `qemu_x86` 注册。若改用 IPv4，原文要求在 `prj.conf` 禁用以下 IPv6 配置：

```kconfig
CONFIG_NET_IPV6=n
CONFIG_NET_CONFIG_NEED_IPV6=n
```

> 源码核对译注：当前示例 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/Kconfig) 通过 [`CONFIG_NET_SAMPLE_LWM2M_SERVER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/Kconfig) 指定完整服务器 URI。普通本地非安全分支默认是 `coap://192.0.2.2:5683`，所以不能仅凭启用 IPv6 就认定自动使用原文的 IPv6 端点。要用 IPv6，应显式设置可达服务器 URI，例如原文网络中的 `coap://[2001:db8::2]:5683`。端点名称由 [`CONFIG_NET_SAMPLE_LWM2M_ID`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/Kconfig) 决定，留空时取 [`CONFIG_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD)；多设备接入同一服务器应保证名称唯一。

## 74.4 DTLS 支持（DTLS Support）

数据报传输层安全（Datagram Transport Layer Security，DTLS）通过下面的叠加配置启用。在 Zephyr 源码根目录执行：

```shell
west build -b qemu_x86 samples/net/lwm2m_client -- -DCONF_FILE="prj.conf overlay-dtls.conf"
west build -t run
```

然后在 Leshan 演示服务器配置安全信息：

1. 打开 Web 界面。
2. 点击“Security”（安全）。
3. 点击“Add new client security configuration”（新增客户端安全配置）。
4. 按原文填写下表。
5. 启动 Zephyr 示例。

| 项目 | 原文示例值 |
| --- | --- |
| 客户端端点（Client endpoint） | `qemu_x86` |
| 安全模式（Security mode） | 预共享密钥（Pre-Shared Key） |
| 身份（Identity） | `Client_identity` |
| 密钥（Key） | `000102030405060708090a0b0c0d0e0f` |

> 源码核对译注：当前 [`lwm2m-client.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/src/lwm2m-client.c) 把端点名称同时写入 PSK 身份资源，因此默认 QEMU 情况通常是 `qemu_x86`，而非原表的 `Client_identity`。服务器身份必须与固件实际值一致。`CONFIG_NET_SAMPLE_LWM2M_PSK` 的十六进制文本由示例转成二进制；上表密钥是公开测试值。前面的 `west build -t run` 已会运行 QEMU，如需观察首次握手，应先完成服务器配置再运行。

## 74.5 引导支持（Bootstrap Support）

要运行引导过程，先在 Linux 主机可写工作目录下载并运行 Leshan 引导演示服务器（Demo Bootstrap Server）：

```shell
$ wget https://ci.eclipse.org/leshan/job/leshan/lastSuccessfulBuild/artifact/leshan-bsserver-demo.jar
$ java -jar ./leshan-bsserver-demo.jar -wp 8888 -lp 5783 -slp 5784
```

浏览器打开 `http://localhost:8888`，配置设备的引导信息：

1. 点击“Add new client bootstrap configuration”（新增客户端引导配置）。
2. 客户端端点填写 `qemu_x86`。
3. 在“LwM2M Server”页签填写服务器地址：IPv6 使用 `coap://[2001:db8::2]:5683`，IPv4 使用 `coap://192.0.2.2:5683`。
4. 安全模式设为“No Security”（无安全保护）。
5. “LwM2M Bootstrap Server”页签保持默认“No Security”。

在 Zephyr 源码根目录启用引导配置并运行：

```shell
west build -b qemu_x86 samples/net/lwm2m_client -- -DCONF_FILE="prj.conf overlay-bootstrap.conf"
west build -t run
```

原文描述的流程是：先连接引导服务器取得普通 LwM2M 服务器信息，然后按收到的配置连接 Leshan 演示服务器。

也可以组合叠加配置，例如同时启用 DTLS 与 Bootstrap。此时应调整引导端口；原文 Leshan 引导服务器的 DTLS 端口为 `5784`，Web 界面“LwM2M Bootstrap Server”页签应选择预共享密钥模式并设置相符凭据。

> 源码核对译注：当前 [`overlay-bootstrap.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/overlay-bootstrap.conf) 只启用引导支持，没有修改 URI。原启动命令的 `-lp 5783` 是非安全引导端口，客户端初始安全对象必须指向它，例如本地 IPv4 测试中的 `coap://192.0.2.2:5783`；引导下发的普通服务器 URI 则仍可使用 `5683`。不要把引导服务器端口、业务服务器端口和 Web 管理端口混为一谈。

## 74.6 OpenThread 支持（OpenThread Support）

需要通过 OpenThread 联网的硬件，在 Zephyr 源码根目录使用：

```shell
west build -b <board to use> samples/net/lwm2m_client -- -DCONF_FILE="prj.conf overlay-ot.conf"
```

原文说明：设备未被配备网络信息（例如烧录前已完全擦除）时，会形成新的 OpenThread 网络并成为领导者，状态显示 `Current role: leader`。这是原文对初始状态的说明，不是要求每次烧录都擦除设备。

加入已有网络有两种方式。一种是启用 `CONFIG_OPENTHREAD_JOINER=y`、`CONFIG_OPENTHREAD_JOINER_AUTOSTART=y`，自行设置没有默认值的 [`CONFIG_OPENTHREAD_JOINER_PSKD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_JOINER_PSKD)，并在已有网络的配网授权者（Commissioner）上登记相同 PSKd。

另一种是在设备控制台手工配置：

```text
ot thread stop
ot channel <channel>
ot networkname <network name>
ot masterkey <key>
ot panid <panid>
ot extpanid <extpanid>
ot thread start
```

尖括号内容需替换为现有网络参数。这些是设备上的 `ot` 子命令，不是主机 PowerShell／Bash 命令。原文可在 OpenThread 边界路由器（OpenThread Border Router，OTBR）主机上取得活动数据集（Active Dataset）：

```shell
wpanctl get Thread:ActiveDataset
```

> 译注：原例包含旧命令名称 `masterkey`；当前 OpenThread [CLI 参考](https://openthread.io/reference/cli/commands#networkkey)使用 `networkkey`。`wpanctl` 也要求主机安装并运行相应的旧式管理组件；原命令保留用于版本对照，不表示所有当前 OTBR 安装均提供该程序。

## 74.7 队列模式（Queue Mode Support）

在 Zephyr 源码根目录启用队列模式：

```shell
west build -b <board to use> samples/net/lwm2m_client -- -DCONF_FILE="prj.conf overlay-queue.conf"
```

客户端以“UDP with Queue Mode”（带队列模式的 UDP）绑定注册。接收窗口（RX Window）关闭时，引擎报告 `LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF`，应用可据此执行关闭无线接收等操作。后续收到 `LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE` 时，下一接收窗口打开。

## 74.8 WNC-M14A2A LTE-M 调制解调器

原文为 WNC-M14A2A LTE-M 调制解调器扩展板（Modem Shield）给出以下构建命令：

```shell
west build -b <board to use> samples/net/lwm2m_client -- -DCONF_FILE="prj.conf overlay-wncm14a2a.conf"
```

> 源码核对译注：读取时的[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/lwm2m_client)已无 `overlay-wncm14a2a.conf`，其原始文件地址返回 404。这一段是官方原页历史内容，保留但不记作当前可直接构建；其他调制解调器配置也不是它的自动替代品。

## 74.9 未启用 DTLS 的示例输出（Sample Output）

以下是原文 QEMU 控制台输出。首先初始化 LwM2M 引擎，然后多个智能对象（Smart Object）注册到引擎；应用设置客户端资源值，使其可在 Leshan 中看到，最后向服务器发送注册请求并建立端点：

```text
To exit from QEMU enter: 'CTRL+a, x'
[QEMU] CPU: qemu32,+nx,+pae
qemu-system-i386: warning: Unknown firmware file in legacy mode: genroms/multiboot.bin

shell> [lib/lwm2m_engine] [DBG] lwm2m_engine_init: LwM2M engine thread started
[lwm2m_obj_security] [DBG] security_create: Create LwM2M security instance: 0
[lwm2m_obj_server] [DBG] server_create: Create LwM2M server instance: 0
[lwm2m_obj_device] [DBG] device_create: Create LwM2M device instance: 0
[lwm2m_obj_firmware] [DBG] firmware_create: Create LwM2M firmware instance: 0
[lwm2m-client] [INF] main: Run LwM2M client
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/0, value:0x0001c99e, len:6
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/1, value:0x0001c9ab, len:23
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/2, value:0x0001c9c9, len:9
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/3, value:0x0001c9d9, len:3
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/9, value:0x0041a3a4, len:1
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/10, value:0x0041a3b4, len:4
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/17, value:0x0001c9fc, len:16
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/18, value:0x0001ca14, len:5
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/20, value:0x0041a3a4, len:1
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3/0/21, value:0x0041a3b4, len:4
[lib/lwm2m_engine] [DBG] lwm2m_engine_create_obj_inst: path:3303/0
[ipso_temp_sensor] [DBG] temp_sensor_create: Create IPSO Temperature Sensor instance: 0
[lib/lwm2m_engine] [DBG] lwm2m_engine_set: path:3303/0/5700, value:0x0041a3b8, len:8
[lib/lwm2m_rd_client] [INF] lwm2m_rd_client_start: LwM2M Client: qemu_x86
[lib/lwm2m_rd_client] [INF] sm_do_init: RD Client started with endpoint 'qemu_x86' and client lifetime 0
[lib/lwm2m_rd_client] [DBG] sm_send_registration: registration sent [2001:db8::2]
[lib/lwm2m_engine] [DBG] lwm2m_udp_receive: checking for reply from [2001:db8::2]
[lib/lwm2m_rd_client] [DBG] do_registration_reply_cb: Registration callback (code:2.1)
[lwm2m-client] [DBG] rd_client_event: Registration complete
[lib/lwm2m_rd_client] [INF] do_registration_reply_cb: Registration Done (EP='EZd501ZF26')
[lib/lwm2m_engine] [DBG] lwm2m_udp_receive: reply 0x004001ec handled and removed
```

原始警告、内存地址、日志接口名和服务器生成的端点标识均保留。它们属于上游历史输出，不是当前版本必须逐字复现的成功标准，也不是本轮运行结果。

## 74.10 相关参考（See Also）

参见[LwM2M 高层 API](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html)及[协议栈指南](P073_LwM2M协议栈.md)。本轮未下载或执行 JAR、启动服务器、修改配网、擦除／烧录设备、注册客户端或执行远程资源操作。


<a id="lwm2m-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="dtls-support"></a>
<a id="bootstrap-support"></a>
<a id="openthread-support"></a>
<a id="queue-mode-support"></a>
<a id="wnc-m14a2a-lte-m-modem-support"></a>
<a id="sample-output-without-dtls-enabled"></a>
<a id="see-also"></a>

[上一章](P073_LwM2M协议栈.md) · [返回大纲](大纲.md) · [下一章](P075_FTP客户端库.md)
