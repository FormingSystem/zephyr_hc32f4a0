---
id: learning.zephyr-docs.networking.page-96
title: zperf网络流量生成器
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/zperf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_zperf网络流量生成器

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/zperf.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 96.1\_概述

zperf是用于在Zephyr中生成网络流量（Network Traffic）的Shell工具，可用于评估网络带宽（Network Bandwidth）。

zperf兼容iPerf 2.0.10及更新版本。需要兼容更早版本时，启用[`CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT)。也可以选择iperf3协议，见本章对应小节；一次构建只使用这两种协议中的一种。

任意应用都可以启用zperf；Zephyr也提供了专用的[zperf示例应用](P097_zperf网络流量生成器示例.md#zperf)。

## 96.2\_示例用法

### Zephyr作为客户端（Client）

iPerf必须以服务器模式（Server Mode）运行。例如在主机终端进行UDP测试时使用：

```console
$ iperf -s -l 1K -u -V -B 2001:db8::2
```

TCP测试使用：

```console
$ iperf -s -l 1K -V -B 2001:db8::2
```

随后在Zephyr控制台执行UDP上传（Upload）：

```console
zperf udp upload 2001:db8::2 5001 10 1K 1M
```

UDP目标速率（原文称baud rate）为0时，会尽可能快地发送，与`iperf -b 0`相同。

TCP的zperf命令为：

```console
zperf tcp upload 2001:db8::2 5001 10 1K 1M
```

如果配置文件中已经指定Zephyr和主机的IP地址，可以这样启动UDP测试：

```console
zperf udp upload2 v6 10 1K 1M
```

或者这样启动TCP测试：

```console
zperf tcp upload2 v6 10 1K 1M
```

### Zephyr作为服务器（Server）

UDP使用以下下载模式（Download Mode）：

```console
zperf udp download 5001
```

TCP使用：

```console
zperf tcp download 5001
```

然后在主机侧执行iPerf客户端命令。UDP为：

```console
$ iperf -l 1K -u -V -c 2001:db8::1 -p 5001
```

TCP为：

```console
$ iperf -l 1K -V -c 2001:db8::1 -p 5001
```

如果Zephyr无法有序接收全部数据包，可以用iPerf的`-b`选项限制输出速率。

译注：带`$`的命令在主机终端执行，不输入提示符；`zperf`命令在Zephyr Shell执行。示例的`2001:db8::1`和`2001:db8::2`分别表示设备与主机地址，使用前需要按实际网络配置替换；两端应已具备可用网络路径。

## 96.3\_iperf3

启用[`CONFIG_NET_ZPERF_IPERF3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF3)后，zperf与iperf3互操作，替代iPerf 2；该支持是实验性（Experimental）的。zperf API和Shell命令不变，默认端口改为iperf3使用的5201。

Zephyr作为服务器时，启用要接受的协议：

```console
zperf tcp download
zperf udp download
```

iperf3客户端每次测试选择TCP或UDP，两者使用同一个端口，并且都需要一条TCP控制连接（Control Connection）。因此这两条命令共享监听端口，各自启用自己的协议；请求未启用协议的测试会被拒绝。在主机侧执行：

```console
$ iperf3 -c 2001:db8::1
$ iperf3 -c 2001:db8::1 -u -b 10M
```

Zephyr作为客户端时，在主机运行`iperf3 -s`，再在Zephyr控制台执行：

```console
zperf tcp upload 2001:db8::2 5201 10 1K
zperf udp upload 2001:db8::2 5201 10 1K 10M
```

每次测试只使用单条数据流（Single Stream）。反向测试`-R`、双向测试`--bidir`、并行测试`-P`以及忽略测试开始阶段的`-O`均不受支持，会返回iperf3针对服务器未实现选项的提示。一次只能运行一个测试，第二个客户端会被告知服务器忙。组播（Multicast）和[`CONFIG_ZPERF_SESSION_PER_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZPERF_SESSION_PER_THREAD)属于iPerf 2功能。

与iPerf 2比较结果时，需要注意以下区别：

- iperf3服务器在客户端通过控制连接结束测试时停止统计TCP数据；结束消息可能先于最后一部分数据到达，因此服务器统计量可能略小于客户端发送量。iPerf 2服务器则统计到连接关闭为止。
- UDP场景中，服务器最后收到的数据报之后丢失的数据报，会像iPerf 2一样计入zperf上传报告的丢包数；iperf3自身不计入这一部分。
- iperf3不报告重排序（Reordering），因此上传报告不会显示乱序数据包（Out-of-order Packets）。
- 服务器仅读取每个UDP数据报的报头，依赖`ZSOCK_MSG_TRUNC`取得完整长度。如果套接字卸载驱动（Socket Offload Driver）忽略该标志，统计的字节数会偏少。
- 一次测试在两端各占用一条控制连接和一条数据流。每次测试结束后，已关闭连接还会在`TIME_WAIT`状态停留一段时间，应像示例的`overlay-iperf3.conf`一样，在[`CONFIG_NET_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MAX_CONTEXTS)和[`CONFIG_NET_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MAX_CONN)中为此预留容量。

## 96.4\_会话管理

设置[`CONFIG_ZPERF_SESSION_PER_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZPERF_SESSION_PER_THREAD)后，启动上传时指定`-a`可同时进行多个上传会话（Upload Session）。每个会话拥有自己的工作队列（Work Queue），测试结束后仍可查看会话结果。

使用`-w`启动会话时，工作线程先等待启动信号，然后可以一起开始。这可以避免已启动的会话线程优先级较高、导致zperf Shell无法运行。只有一个上传会话时，通常不需要`-w`。

以下命令在`zperf`命令下用于会话管理：

| 子命令 | 说明 |
| --- | --- |
| `jobs` | 显示当前活动或已完成的会话。 |
| `jobs all` | 显示已完成会话的统计。 |
| `jobs clear` | 清除已完成会话的统计。 |
| `jobs start` | 启动全部等待中的会话。 |

原文示例：

```console
uart:~$ zperf udp upload -a -t 5 192.0.2.2 5001 10 1K 1M
Remote port is 5001
Connecting to 192.0.2.2
Duration:       10.00 s
Packet size:    1000 bytes
Rate:           1000 kbps
Starting...
Rate:           1.00 Mbps
Packet duration 7 ms

uart:~$ zperf jobs all
No sessions sessions found
uart:~$ zperf jobs
           Thread    Remaining
Id  Proto  Priority  time (sec)
[1] UDP    5            4

Active sessions have not yet finished
-
Upload completed!
Statistics:             server  (client)
Duration:               30.01 s (30.01 s)
Num packets:            3799    (3799)
Num packets out order:  0
Num packets lost:       0
Jitter:                 63 us
Rate:                   1.01 Mbps       (1.01 Mbps)
Thread priority:        5
Protocol:               UDP
Session id:             1

uart:~$ zperf jobs all
-
Upload completed!
Statistics:             server  (client)
Duration:               30.01 s (30.01 s)
Num packets:            3799    (3799)
Num packets out order:  0
Num packets lost:       0
Jitter:                 63 us
Rate:                   1.01 Mbps       (1.01 Mbps)
Thread priority:        5
Protocol:               UDP
Session id:             1
Total 1 sessions done

uart:~$ zperf jobs clear
Cleared data from 1 sessions

uart:~$ zperf jobs
No active upload sessions
No finished sessions found
```

> 译注：原始记录的命令请求10秒测试，后面的统计显示30.01秒；这里保留这处原文不一致，不将该日志作为精确时长验证依据。`-t 5`指定线程优先级（Thread Priority），不是持续时间。

`-w`可按下面方式延迟作业（Job）启动：

```console
uart:~$ zperf tcp upload -a -t 6 -w 192.0.2.2 5001 10 1K
Remote port is 5001
Connecting to 192.0.2.2
Duration:       10.00 s
Packet size:    1000 bytes
Rate:           10 kbps
Waiting "zperf jobs start" command.
[01:06:51.392,288] <inf> net_zperf: [0] TCP waiting for start

uart:~$ zperf udp upload -a -t 6 -w 192.0.2.2 5001 10 1K 10M
Remote port is 5001
Connecting to 192.0.2.2
Duration:       10.00 s
Packet size:    1000 bytes
Rate:           10000 kbps
Waiting "zperf jobs start" command.
Rate:           10.00 Mbps
Packet duration 781 us
[01:06:58.064,552] <inf> net_zperf: [0] UDP waiting for start

uart:~$ zperf jobs start
-
Upload completed!
-
Upload completed!

# Note that the output may be garbled as two threads printed
# output at the same time. Just print out the fresh listing
# like this.

uart:~$ zperf jobs all
-
Upload completed!
Statistics:             server  (client)
Duration:               9.99 s  (10.00 s)
Num packets:            11429   (11429)
Num packets out order:  0
Num packets lost:       0
Jitter:                 164 us
Rate:                   9.14 Mbps       (9.14 Mbps)
Thread priority:        6
Protocol:               UDP
Session id:             0
-
Upload completed!
Duration:               10.00 s
Num packets:            15487
Num errors:             0 (retry or fail)
Rate:                   12.38 Mbps
Thread priority:        6
Protocol:               TCP
Session id:             0
Total 2 sessions done
```

原例中的注释提醒：两个线程同时输出时，内容可能交错；重新运行`zperf jobs all`即可获取新的完整列表。

## 96.5\_自定义上传数据

通过`zperf_upload_params.data_loader`设置自定义数据源（Custom Data Source），可以进行更深入的上传性能分析。这样能够生成自定义包内容，而非始终发送仅由字符`z`组成的固定包。例如，可用它测量从外部Flash存储芯片读取数据并上传时的最大吞吐量（Maximum Throughput）。

## 96.6\_原始发送模式

原始发送模式（Raw TX Mode）用于测试自定义二层帧（L2 Frame）或厂商专用协议。它绕过UDP／TCP，使用数据包套接字（Packet Socket）直接发送原始数据包。

要启用此模式，设置以下Kconfig选项：

```kconfig
CONFIG_NET_SOCKETS_PACKET=y
CONFIG_NET_ZPERF_RAW_TX=y
```

最大报头长度由[`CONFIG_NET_ZPERF_RAW_TX_MAX_HDR_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_RAW_TX_MAX_HDR_SIZE)控制，默认64字节。使用前必须为网络接口启用发送注入模式（TX Injection Mode）：

```console
uart:~$ net iface txinjection 1 on
```

原始上传命令语法如下，尖括号内容是参数占位符：

```console
zperf raw upload [-a] <if_index> <header_hex> [<duration_sec>] [<packet_size>] [<rate_kbps>]
```

| 参数 | 含义 |
| --- | --- |
| `-a` | 可选的异步模式（Async Mode）标志。 |
| `if_index` | 网络接口索引（Network Interface Index），例如1。 |
| `header_hex` | 用户提供的十六进制报头字符串，包含厂商元数据（Vendor Metadata）和帧报头（Frame Header）。 |
| `duration_sec` | 测试持续时间，单位为秒，默认1。 |
| `packet_size` | 包含报头的总数据包大小，默认256。 |
| `rate_kbps` | 目标速率，单位Kbps，支持K／M后缀，默认10；0表示尽可能快地发送。 |

发送带厂商元数据的原始802.11帧的示例：

```console
uart:~$ zperf raw upload 1 12345678000400030000000088000000ffffffffffa06960e35215a06960e3521500000000aaaa030000000800 10 1024 50M
```

本例的报头十六进制字符串依次包含厂商元数据（前12字节），以及带逻辑链路控制／子网访问协议（Logical Link Control／Subnetwork Access Protocol，LLC／SNAP）的802.11 QoS数据报头。工具会自动追加填充字符`z`的有效载荷（Payload），直至达到指定的数据包大小。


<a id="zperf-network-traffic-generator"></a>
<a id="zperf"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="iperf3"></a>
<a id="zperf-iperf3"></a>
<a id="session-management"></a>
<a id="custom-data-upload"></a>
<a id="raw-tx-mode"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Latmon网络延迟监测服务](P094_Latmon网络延迟监测服务.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：以太网](P106_以太网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P095_Latmon客户端示例.md) · [返回大纲](大纲.md) · [下一章](P097_zperf网络流量生成器示例.md)

</details>

<!-- reading-navigation:end -->
