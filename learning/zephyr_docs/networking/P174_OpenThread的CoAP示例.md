---
id: learning.zephyr-docs.networking.page-174
title: OpenThread的CoAP示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/openthread/coap/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_OpenThread的CoAP示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/openthread/coap/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例展示 OpenThread 受限应用协议（Constrained Application Protocol，CoAP）API 的使用，可构建为服务器或客户端。

分别在两块开发板上运行客户端和服务器，可以建立本地 Thread 网络。OpenThread 使用 Kconfig 提供的网络密钥（Network Key）创建网络；烧写后，开发板会自动创建和配置网络。

网络工作后，客户端即可与服务器交互。每次按下客户端按键，服务器上的 LED 应翻转状态（Toggle）。源码位于官方[samples/net/openthread/coap](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/openthread/coap)。

> 原文说明：Zephyr 也有自己的 CoAP API，但这里使用 OpenThread CoAP API，因为 OpenThread 在内部用它实现许多服务，而且它对无线电的访问更直接。因此，相比使用 Zephyr CoAP API，预期可以降低开销，但应用的可移植性会减弱。这是原文的设计说明，不是本次测得的性能结果。

> 配置提示：当前官方[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/prj.conf)含用于演示的固定网络密钥和网络名。两块板需要一致的网络参数；公开的示例配置不应被误认为为实际部署生成了独立凭据。

## 2. 构建与运行

在具有目标板依赖的 Zephyr 环境中，从读者自己的 Zephyr 源码根目录构建。完整 Thread 设备（Full Thread Device，FTD）CoAP 服务器的原文命令为：

```sh
west build -b <board to use> -T sample.net.openthread.ftd.coap.server samples/net/openthread/coap
```

FTD CoAP 客户端：

```sh
west build -b <board to use> -T sample.net.openthread.ftd.coap.client samples/net/openthread/coap
```

以 `cc1352p7` LaunchPad 为服务器：

```sh
west build -b cc1352p7_lp -T sample.net.openthread.ftd.coap.server samples/net/openthread/coap
west flash
```

同类开发板作为客户端：

```sh
west build -b cc1352p7_lp -T sample.net.openthread.ftd.coap.client samples/net/openthread/coap
west flash
```

> 译注：`<board to use>` 需替换为实际目标。两组命令对应两块设备，烧写前应确认当前连接的设备和所选构建角色。`-T` 使用官方[tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/tests.yaml)中的场景配置；当前服务器场景额外设置服务器选项，而客户端使用默认角色。切换角色时避免复用错误配置的旧构建结果。启用按键部分时，[main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/src/main.c)要求设备树存在可用的 `sw0` 别名。

## 3. 检查 Thread 网络状态

分别打开服务器板和客户端板的控制台，检查状态：

```console
server:~$ ot state
router
Done
```

有效状态可以是 `child`（子节点）、`router`（路由器）或 `leader`（领导节点）。Thread 网络工作后，才开始使用客户端。

## 4. 通过客户端按键控制服务器 LED

网络建立后，无需额外操作，按客户端 `sw0`，应看到服务器 `led0` 翻转。

原文称客户端使用“广播地址”（Broadcast Address）请求服务器翻转 LED，因此无需知道服务器地址；如果网络中还有第二个服务器，它的 LED 也会翻转。

> 源码更正：当前[按键处理](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/src/main.c)和[Shell 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/src/coap_shell.c)使用 `ff03::1`。这是 IPv6 多播（Multicast）地址，原文的“广播”应理解为向该组中的节点发送请求，不能与 IPv4 广播等同。服务器还需运行相应资源处理，才会按收到的请求控制 LED。

## 5. 从计算机控制服务器 LED

虽然使用 OpenThread CoAP API，仍可与网络上的其他 CoAP 客户端或服务器交互。原文展示从不在 Thread 网络中的计算机控制 LED，并以同网中具有 NAT64 支持的 OpenThread Border Router（OTBR）为前提。

先检查服务器或客户端是否已连接 OTBR，以及是否有可用 NAT64：

```console
server:~$ ot netdata show
router
Done
Prefixes:
fd6f:cb3a:802:1::/64 paos low dc00
Routes:
fc00::/7 sa med dc00
fd6f:cb3a:802:2:0:0::/96 sn low dc00
Services:
44970 01 14000500000e10 s dc00 0
44970 5d fd78b9ce54779c6eb5484d062c3b5b22d120 s dc00 1
Contexts:
fd6f:cb3a:802:1::/64 1 c
Commissioning:
11426 - - -
Done
```

`Prefixes` 列出可用于从 Thread 网络外访问设备的 IPv6 前缀。设备应拥有使用该前缀的 IPv6 地址：

```console
server:~$ ot ipaddr
fd78:b9ce:5477:9c6e:0:ff:fe00:a800
fd6f:cb3a:802:1:f0ec:c1e2:c1bb:744
fd78:b9ce:5477:9c6e:75b8:386c:1f79:1013
fe80:0:0:0:50d1:bed5:6e6e:ad75
Done
```

示例中的 `fd6f:cb3a:802:1:f0ec:c1e2:c1bb:744` 可用于从 Thread 网络外联系 CoAP 服务器。

还可以检查 Thread 网络是否能够访问互联网：

```console
server:~$ ot ping 8.8.8.8
Pinging synthesized IPv6 address: fd6f:cb3a:802:2:0:0:808:808
16 bytes from fd6f:cb3a:802:2:0:0:808:808: icmp_seq=1 hlim=114 time=36ms
1 packets transmitted, 1 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 36/36.0/36 ms.
Done
```

> 译注：原文网络数据输出中的 `router` 和前置 `Done` 也按原样保留，不将其当作每次 `ot netdata show` 都会输出的固定格式。上述地址、前缀和延时均属于官方示例，应根据自己的设备输出判断。

> 网络边界：NAT64 用于 IPv6 与 IPv4 之间的转换，见 OpenThread 官方[边界路由器说明](https://github.com/openthread/ot-docs/blob/main/site/en/guides/border-router/index.md)。本例 `ot ping 8.8.8.8` 明确使用合成 IPv6 地址来访问 IPv4 目的地；下面计算机对方括号内 IPv6 地址的 CoAP 访问则是 IPv6 路径，需要正确的路由和可达性，不能仅以“NAT64 已启用”证明它可用。

如果上述网络正常，可在计算机上使用 Python 编写的 `aiocoap-client`。先安装：

```sh
pip install aiocoap
```

然后发送翻转 LED 的请求：

```sh
aiocoap-client -m PUT --payload '{"led_id":0,"state":2}'  coap://[fd6f:cb3a:802:1:f0ec:c1e2:c1bb:744]/led
```

此时 LED 状态应发生变化。该命令在主机 Python 环境对应的终端中运行，IPv6 地址应替换为实际服务器地址；`/led` 是资源路径，JSON 的 `led_id` 是 LED 编号，`state` 为 `2` 表示翻转。当前[led.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coap/src/led.h)还定义 `0` 关闭、`1` 打开。本次没有安装客户端或向任何网络发送请求。

## 6. 通过 Shell 命令控制服务器 LED

示例还提供客户端 Shell 命令。翻转 LED：

```console
$client:~$ ot_coap led set 0 toggle
```

LED 状态应发生变化。与按键相同，默认使用原文所称的“广播地址”，实际多播语义见前面的源码更正。

要只控制某一个服务器，指定它的 IPv6 地址：

```console
$client:~$ ot_coap led set 0 toggle fd6f:cb3a:802:1:f0ec:c1e2:c1bb:744
```

## 7. 另见（See Also）

[OpenThread 协议栈 API](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html)。

> 验证边界：已核对原文所有构建命令、交互及网络日志，并对照角色配置、多播目的地址和 LED 状态值；没有构建、烧写、组网或执行实板 LED 控制测试。


<a id="ot-coap"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="checking-thread-network-state"></a>
<a id="controlling-server-board-s-led-using-a-button-on-client-board"></a>
<a id="controlling-server-board-s-led-from-a-computer"></a>
<a id="controlling-server-board-s-led-using-shell-command"></a>
<a id="see-also"></a>

[上一章](P173_OpenThread边界路由器.md) · [返回大纲](大纲.md) · [下一章](P175_OpenThread协处理器.md)
