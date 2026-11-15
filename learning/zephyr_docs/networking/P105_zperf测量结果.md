---
id: learning.zephyr-docs.networking.api-105
title: zperf测量结果
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzperf__results.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_zperf测量结果

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzperf__results.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 105.1\_阅读说明与来源

译注：先读[zperf指南](P096_zperf网络流量生成器.md)、[示例](P097_zperf网络流量生成器示例.md)和[回环吞吐量测试](P098_zperf确定性回环吞吐量.md)，再查本组接口。

本组：[完整API参考](P102_zperf完整API参考.md) · [头文件参考](P103_zperf头文件参考.md) · [头文件源码](P104_zperf头文件源码.md)。

性能测量结果（Performance Results）。

```c
#include <zephyr/net/zperf.h>
```

性能测量结果（Performance Results）。

## 105.2\_数据成员（Data Fields）

<a id="r_adfd2738991c8bea53f20079421da6d96"></a>

```c
uint32_t nb_packets_sent
```

发送的数据包数（Packets Sent）。

<a id="r_acf312d831d8e6707f7e769da92f8eb70"></a>

```c
uint32_t nb_packets_rcvd
```

收到的数据包数（Packets Received）。

<a id="r_ac9ad68ef3b6081b64f290720ad9b5bc8"></a>

```c
uint32_t nb_packets_lost
```

丢失的数据包数（Packets Lost）。

<a id="r_aa1e3c86bcab447bc888bba0bbaa057d1"></a>

```c
uint32_t nb_packets_outorder
```

乱序数据包数（Packets Out of Order）。

<a id="r_a517ba180a6414a2f2d1484e698d57650"></a>

```c
uint64_t total_len
```

已传输数据的总长度（Total Length）。

<a id="r_aafb7f2c221c91c59ab0d6936ebc6ce2a"></a>

```c
uint64_t time_in_us
```

传输总时间（Total Transfer Time），单位微秒。

<a id="r_af4a5ce512fb37ddae8e2c12a0b67c3a2"></a>

```c
uint32_t jitter_in_us
```

抖动（Jitter），单位微秒。

<a id="r_a550158fd641799c2a6b2d25617ac9a6c"></a>

```c
uint64_t client_time_in_us
```

客户端连接时间（Client Connection Time），单位微秒。

<a id="r_a8aedf97a8eeace1f4b9cda7e07e17e28"></a>

```c
uint32_t packet_size
```

数据包大小（Packet Size）。

<a id="r_a5fcccf6747c449418c246ac1d945a1f8"></a>

```c
uint32_t nb_packets_errors
```

数据包错误数（Packet Errors）。

<a id="r_a9253d70cca70d2b8112bac31cca6ea2f"></a>

```c
bool is_multicast
```

本次会话使用IP组播（IP Multicast）时为`true`。

## 105.3\_详细说明（Detailed Documentation）

<a id="a550158fd641799c2a6b2d25617ac9a6c"></a>

### `client_time_in_us`

```c
uint64_t zperf_results::client_time_in_us
```

客户端连接时间（Client Connection Time），单位微秒。

<a id="a9253d70cca70d2b8112bac31cca6ea2f"></a>

### `is_multicast`

```c
bool zperf_results::is_multicast
```

本次会话使用IP组播（IP Multicast）时为`true`。

<a id="af4a5ce512fb37ddae8e2c12a0b67c3a2"></a>

### `jitter_in_us`

```c
uint32_t zperf_results::jitter_in_us
```

抖动（Jitter），单位微秒。

<a id="a5fcccf6747c449418c246ac1d945a1f8"></a>

### `nb_packets_errors`

```c
uint32_t zperf_results::nb_packets_errors
```

数据包错误数（Packet Errors）。

<a id="ac9ad68ef3b6081b64f290720ad9b5bc8"></a>

### `nb_packets_lost`

```c
uint32_t zperf_results::nb_packets_lost
```

丢失的数据包数（Packets Lost）。

<a id="aa1e3c86bcab447bc888bba0bbaa057d1"></a>

### `nb_packets_outorder`

```c
uint32_t zperf_results::nb_packets_outorder
```

乱序数据包数（Packets Out of Order）。

<a id="acf312d831d8e6707f7e769da92f8eb70"></a>

### `nb_packets_rcvd`

```c
uint32_t zperf_results::nb_packets_rcvd
```

收到的数据包数（Packets Received）。

<a id="adfd2738991c8bea53f20079421da6d96"></a>

### `nb_packets_sent`

```c
uint32_t zperf_results::nb_packets_sent
```

发送的数据包数（Packets Sent）。

<a id="a8aedf97a8eeace1f4b9cda7e07e17e28"></a>

### `packet_size`

```c
uint32_t zperf_results::packet_size
```

数据包大小（Packet Size）。

<a id="aafb7f2c221c91c59ab0d6936ebc6ce2a"></a>

### `time_in_us`

```c
uint64_t zperf_results::time_in_us
```

传输总时间（Total Transfer Time），单位微秒。

<a id="a517ba180a6414a2f2d1484e698d57650"></a>

### `total_len`

```c
uint64_t zperf_results::total_len
```

已传输数据的总长度（Total Length）。

## 105.4\_相关源码与接口边界

此页声明来自`<zephyr/net/zperf.h>`。本仓库的[对应头文件](../../../include/zephyr/net/zperf.h)可用于源码跟踪；仓库版本可能与官网`latest`不同。

译注：官方本页API索引没有为上传／下载参数生成独立条目；其声明保留在[头文件源码译页](P104_zperf头文件源码.md)，该页还标明原始头文件中的补充注释。当前[官方API入口实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/zperf_api.c)按构建配置选择iPerf 2或iPerf 3后端；同步上传要求`param`和`result`非空，异步上传及服务器启动要求`param`和`callback`非空，否则返回`-EINVAL`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P104_zperf头文件源码.md) · [返回大纲](大纲.md) · [下一章](P106_以太网.md)
