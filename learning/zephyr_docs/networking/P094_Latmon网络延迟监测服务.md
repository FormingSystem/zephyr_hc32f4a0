---
id: learning.zephyr-docs.networking.page-94
title: Latmon网络延迟监测服务
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/latmon.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_Latmon网络延迟监测服务

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/latmon.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 94.1\_概述

Latmon网络服务提供基于网络的延迟监测（Network-based Latency Monitoring）所需功能，包括套接字管理（Socket Management）、客户端与服务器通信，以及与被测系统（System Under Test，SUT）上运行的Latmus服务交换数据。

此服务负责建立和管理Latmon应用与Latmus服务之间的网络通信：Latmon应用运行在基于Zephyr的开发板上，Latmus服务运行在SUT上。它使用TCP套接字进行可靠通信，使用UDP套接字广播Latmon设备的IP地址。

## 94.2\_API参考与功能

完整接口见[延迟监测器API](P099_Latmon完整API参考.md)。

- 套接字管理（Socket Management）：创建和管理用于通信的TCP、UDP套接字。
- 客户端与服务器通信（Client-Server Communication）：处理Latmus服务发起的连接。
- 数据交换（Data Exchange）：向Latmus服务发送延迟指标和直方图数据（Histogram Data）。
- IP地址广播（IP Address Broadcasting）：广播Latmon设备的IP地址，便于Latmus服务发现设备。
- 线程安全设计（Thread-Safe Design）：使用Zephyr内核原语，例如消息队列（Message Queue）和信号量（Semaphore），实现同步。

## 94.3\_工作流程

### 创建套接字（Socket Creation）

调用[`net_latmon_get_socket()`](P099_Latmon完整API参考.md#ga48e9ce13fd948701739fcc2cd9e1a6b0)创建并配置TCP套接字，用于与Latmus服务通信。可以通过连接地址参数，将套接字绑定到特定接口和端口。

### 处理连接（Connection Handling）

[`net_latmon_connect()`](P099_Latmon完整API参考.md#ga6c8ad5a0a35ea7ef098c024ec142edc7)等待Latmus服务连接。如果在超时时间内没有收到连接，服务会通过UDP广播自身IP地址，并返回`-EAGAIN`。如果无法发送广播请求，函数返回`-1`，客户端应退出。

### 开始监测（Monitoring Start）

连接建立后，调用[`net_latmon_start()`](P099_Latmon完整API参考.md#ga36586599ee161959414097dbbd54a2d3)启动监测。该函数通过回调计算延迟差值（Latency Delta），并将数据发送给Latmus服务。

### 监测状态（Monitoring Status）

[`net_latmon_running()`](P099_Latmon完整API参考.md#ga968ebd93287d3968695c0dfebc7493d1)用于检查监测是否正在进行。

### 线程管理（Thread Management）

服务使用Zephyr线程处理传入连接并管理监测过程。

## 94.4\_启用与配置

必须在应用的`prj.conf`中启用[`CONFIG_NET_LATMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON)。以下选项用于定制服务：

| 配置项 | 含义 |
| --- | --- |
| [`CONFIG_NET_LATMON_PORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_PORT) | Latmon服务端口号（Port Number）。 |
| [`CONFIG_NET_LATMON_XFER_THREAD_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_XFER_THREAD_STACK_SIZE) | 传输线程栈大小（Transfer Thread Stack Size）。 |
| [`CONFIG_NET_LATMON_XFER_THREAD_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_XFER_THREAD_PRIORITY) | 传输线程优先级（Transfer Thread Priority）。 |
| [`CONFIG_NET_LATMON_THREAD_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_THREAD_STACK_SIZE) | Latmon线程栈大小。 |
| [`CONFIG_NET_LATMON_THREAD_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_THREAD_PRIORITY) | Latmon线程优先级。 |
| [`CONFIG_NET_LATMON_MONITOR_THREAD_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_MONITOR_THREAD_STACK_SIZE) | 监测线程栈大小（Monitor Thread Stack Size）。 |
| [`CONFIG_NET_LATMON_MONITOR_THREAD_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON_MONITOR_THREAD_PRIORITY) | 监测线程优先级（Monitor Thread Priority）。 |

译注：原页仅为端口项写出解释；其余含义依据[官方Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig)补充。该配置将服务标记为实验性（Experimental），默认端口为2306。

## 94.5\_使用示例

下面是官方页面的原始代码，展示创建套接字、等待连接、开始测量和退出时关闭监听套接字的流程。

```c
#include <zephyr/net/latmon.h>
#include <zephyr/net/socket.h>

void main(void)
{
    struct in_addr ip;
    int server_socket, client_socket;

    /* Create and configure the server socket */
    server_socket = net_latmon_get_socket(NULL);

    while (1) {
        /* Wait for a connection from the Latmus service */
        client_socket = net_latmon_connect(server_socket, &ip);
        if (client_socket < 0) {
            if (client_socket == -EAGAIN) {
                continue;
            }
            goto out;
        }

        /* Start the latency monitoring process */
        net_latmon_start(client_socket, measure_latency_cycles);
    }
out:
    close(server_socket);
}
```

> 译注：这是流程片段，未定义`measure_latency_cycles`，也未检查[`net_latmon_get_socket()`](P099_Latmon完整API参考.md#ga48e9ce13fd948701739fcc2cd9e1a6b0)的失败返回，不能直接当作完整应用。当前[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/latmon.h)声明的地址参数类型为`struct net_in_addr *`；原例使用`struct in_addr`，应按所用版本的网络类型及兼容配置核对。测量回调签名为`int (*)(uint32_t *delta)`，以周期数（Cycles）输出差值，成功返回0，失败返回负错误码。完整应用见[Latmon客户端示例](P095_Latmon客户端示例.md)，本仓库的[头文件](../../../include/zephyr/net/latmon.h)可用于版本对照。

> 译注（源码核对）：原例的局部变量`ip`未初始化，而当前[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/latmon.c)在连接超时时直接用该指针广播地址。应像[完整示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/latmon/src/main.c)一样，在DHCP绑定完成后传入本设备的有效IPv4地址；不要把此参数当成自动填充远端地址的输出变量。另外，当前[`net_latmon_start()`](P099_Latmon完整API参考.md#ga36586599ee161959414097dbbd54a2d3)会等待会话结束后返回，不是启动监测后立即返回的调用。


<a id="latmon-network-service"></a>
<a id="latmon"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="overview"></a>
<a id="api-reference"></a>
<a id="features"></a>
<a id="workflow"></a>
<a id="socket-creation"></a>
<a id="connection-handling"></a>
<a id="monitoring-start"></a>
<a id="monitoring-status"></a>
<a id="thread-management"></a>
<a id="enabling-the-latmon-service"></a>
<a id="example-usage"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：网络统计](P093_网络统计.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：zperf网络流量生成器](P096_zperf网络流量生成器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P093_网络统计.md) · [返回大纲](大纲.md) · [下一章](P095_Latmon客户端示例.md)

</details>

<!-- reading-navigation:end -->
