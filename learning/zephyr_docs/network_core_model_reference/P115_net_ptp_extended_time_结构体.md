---
id: learning.zephyr-docs.network-core-model-reference.page-115
title: net_ptp_extended_time_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ptp__extended__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_net\_ptp\_extended\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ptp__extended__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用精确时间协议（gPTP）的扩展时间戳格式。

```c
#include <zephyr/net/ptp_time.h>
```

<a id="details"></a>

广义精确时间协议扩展时间戳格式（Generalized Precision Time Protocol Extended Timestamp format）。此结构表示符合广义精确时间协议标准（IEEE 802.1AS，第 6.4.3.5 节）的扩展时间戳。秒数编码为 48 位无符号整数；带小数的纳秒值编码为 48 位，单位为 2 的负 16 次方纳秒（原文记为 `2*(-16) ns`）。有关 PTP 时间戳及其在 Zephyr 中用途的精确定义，参见 `net_ptp_time` 的说明。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 115.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a4719c7c4bc8f4a95cfd85ab0ae876452"></a>

```c
uint64_t second
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[second](#a97b1711e17fa229bab129da4148c3e55)。

第二个值。

<a id="r_a824769e27b57ec7cf80d14186b5e80ac"></a>

```c
};
```

编码为 48 位的秒数（Seconds）。

```c
union {
```

<a id="r_ae820b9ac38a4cec132009d47f4717ea6"></a>

```c
uint64_t fract_nsecond
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[fract_nsecond](#a94ec079b5d38fcd12ec54baf707ec587)。

带小数的纳秒值（Fractional nanoseconds value）。

<a id="r_ab0387b261c8369b74a8704bc12bb3de0"></a>

```c
};
```

用 48 位表示的带小数纳秒值（Fractional nanoseconds）。

## 115.2\_详细说明（Detailed Documentation）

<a id="a824769e27b57ec7cf80d14186b5e80ac"></a>

### `[union]`

```c
union { ... } net_ptp_extended_time
```

编码为 48 位的秒数（Seconds）。

<a id="ab0387b261c8369b74a8704bc12bb3de0"></a>

### `[union]`

```c
union { ... } net_ptp_extended_time
```

用 48 位表示的带小数纳秒值（Fractional nanoseconds）。

<a id="a94ec079b5d38fcd12ec54baf707ec587"></a>

### `fract_nsecond`

```c
uint64_t net_ptp_extended_time::fract_nsecond
```

带小数的纳秒值（Fractional nanoseconds value）。

<a id="a97b1711e17fa229bab129da4148c3e55"></a>

### `second`

```c
uint64_t net_ptp_extended_time::second
```

第二个值。

本数据类型文档由以下文件生成：

- `zephyr/net/ptp_time.h`

## 115.3\_原页交叉引用（Cross References）

- [zephyr/net/ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [net_ptp_time](P116_net_ptp_time_结构体.md)
- [net_ptp_extended_time](P115_net_ptp_extended_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P114_net_pkt_结构体.md) · [返回大纲](大纲.md) · [下一章](P116_net_ptp_time_结构体.md)
