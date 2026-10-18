---
id: learning.zephyr-docs.network-core-model-reference.page-116
title: net_ptp_time_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ptp__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_net\_ptp\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ptp__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

（通用）精确时间协议（(g)PTP）的时间戳格式。

```c
#include <zephyr/net/ptp_time.h>
```

<a id="details"></a>

（广义）精确时间协议时间戳格式（(Generalized) Precision Time Protocol Timestamp format）。此结构表示符合精确时间协议（Precision Time Protocol，PTP；IEEE 1588，第 5.3.3 节）、广义精确时间协议（Generalized Precision Time Protocol，gPTP；IEEE 802.1AS，第 6.4.3.4 节）标准的时间戳，也适用于 Zephyr 网络消息中其他明确定义、需要精确结构化时间戳的上下文。秒数编码为 48 位无符号整数，纳秒数编码为 32 位无符号整数。

在 (g)PTP 中，时间戳表示消息时间戳点（Message timestamp point）通过参考平面（Reference plane）时，相对于本地时钟（LocalClock）的时间。该参考平面标记 PTP 实例（PTP Instance）与网络介质之间的边界（IEEE 1855，第 7.3.4.2 节；IEEE 802.1AS，第 8.4.3 节）。消息时间戳点和参考平面的精确定义取决于网络介质和用例。对于 (g)PTP，标准定义了与介质对应的消息时间戳点和参考平面。对于 Zephyr 特有的非 PTP 上下文，时间戳相对于同一本地时钟测量，但消息时间戳点和参考平面由具体上下文决定，下文按用例说明。

本地时钟（LocalClock）是一种自由运行时钟（Freerunning clock），嵌入某个明确定义的实体（例如 PTP 实例）中，以任意选定的纪元（Epoch）为基准，向该实体提供统一时间（IEEE 1855，第 3.1.26 节；IEEE 802.1AS，第 3.16 节）。在 Zephyr 中，本地时钟通常是内核系统时钟驱动（Kernel system clock driver）、计数器驱动（Counter driver）、实时时钟 API 驱动（RTC API driver），或低层计数器／定时器外设的某个实例，例如支持硬件时间戳的以太网外设或无线电定时器；其精度必须足以满足使用场景。有关 gPTP 上下文本地时钟符合性所需的具体性能要求，参见 IEEE 802.1AS 附录 B；有关 PTP 本地时钟的一般性能要求，参见 IEEE 1588 附录 A 第 A5.4 节；有关测距应用（Ranging applications）的要求，参见 IEEE 802.15.4-2020 第 15.7 节。同一标准第 6.7.6 节说明了保护时间（Guard times）与时钟精度之间的关系，它们也会影响协调采样监听（CSL）、时隙信道跳频（TSCH）、接收机发起传输（RIT）等子协议所需的精度。

跨子系统或跨介质使用时间戳的应用，必须理解相应参考平面的定义，并据此解释时间戳。应用还必须保证所有时间戳以同一本地时钟为基准，或者使用足够精确的转换算法在不同时钟之间换算。

时间戳可在网络消息进入时测量，即接收时间戳（RX timestamps），也可在离开时测量，即发送时间戳（TX timestamps）。时间戳还可用于将网络消息安排在未来一个明确定义的时刻发送到介质上，即定时发送（Timed TX）。给出一个未来时间戳和一个持续时间，两者都以本地时钟为基准，也可指定网络设备预期接收消息的时间窗口，即接收窗口（RX window）。

Zephyr 当前在以下上下文中使用此时间戳结构：

- 全双工点对点 IEEE 802.3 链路的 gPTP（IEEE 802.1AS，第 11 节）：参考平面和消息时间戳点按标准定义。
- IEEE 802.15.4 定时发送与接收（Timed TX and RX）：时间戳表示帧起始定界符（Start-of-frame delimiter，SFD）最后一个符号的结束位置到达本地天线的时刻；等价地，也就是物理层报头（PHY header）第一个符号开始的位置到达本地天线的时刻。根据上下文，标准也称其为测距标记（RMARKER；IEEE 802.15.4-2020，第 6.9.1 节）或符号边界（Symbol boundary；同标准第 6.5.2 节）。对于信标时间戳（Beacon timestamps），时间戳测量平面与参考平面之间的差异由 MAC PIB 属性 `macSyncSymbolOffset` 定义，参见同标准第 8.4.3.1 节表 8-94。

若 Zephyr 新增使用此时间戳结构的用例，必须（SHALL）将该用例的时钟性能要求、消息时间戳点和参考平面定义加入上述列表。

译注：原文两处引用写作 IEEE 1855，此处按原文保留，不擅自改写标准编号。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 116.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a2c25adfd0a2f5206cab7ea2538aad37d"></a>

```c
uint64_t second
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[second](#a8d61359ca53147d2da761edeb9e1ab04)。

第二个值。

<a id="r_a9ef6ab971069f9ea8fb55a27d7dacd99"></a>

```c
};
```

编码为 48 位的秒数（Seconds）。

<a id="r_a31af3f0b8f924336c17585ee1b15ee0e"></a>

```c
uint32_t nanosecond
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nanosecond](#a31af3f0b8f924336c17585ee1b15ee0e)。

纳秒（Nanoseconds）。

## 116.2\_详细说明（Detailed Documentation）

<a id="a9ef6ab971069f9ea8fb55a27d7dacd99"></a>

### `[union]`

```c
union { ... } net_ptp_time
```

编码为 48 位的秒数（Seconds）。

<a id="a31af3f0b8f924336c17585ee1b15ee0e"></a>

### `nanosecond`

```c
uint32_t net_ptp_time::nanosecond
```

纳秒（Nanoseconds）。

<a id="a8d61359ca53147d2da761edeb9e1ab04"></a>

### `second`

```c
uint64_t net_ptp_time::second
```

第二个值。

本数据类型文档由以下文件生成：

- `zephyr/net/ptp_time.h`

## 116.3\_原页交叉引用（Cross References）

- [zephyr/net/ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_ptp_time](P116_net_ptp_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P115_net_ptp_extended_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P117_net_sockaddr_结构体.md)
