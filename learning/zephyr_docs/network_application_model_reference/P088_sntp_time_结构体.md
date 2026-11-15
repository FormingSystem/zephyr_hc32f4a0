---
id: learning.zephyr-docs.network-application-model-reference.page-88
title: sntp_time_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsntp__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_sntp\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsntp__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SNTP API返回的时间，以自1970年1月1日起经过的秒数表示，包含小数秒部分。

```c
#include <zephyr/net/sntp.h>
```

<a id="details"></a>

SNTP API返回的时间，以自1970年1月1日起经过的秒数表示，包含小数秒部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_a7dc90613b6ac0265ff49b931a786354f"></a>

```c
uint64_t seconds
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[seconds](#a7dc90613b6ac0265ff49b931a786354f)。

第二个值。

<a id="r_ad33fb2e743756bde8538ac6d2ff3eae8"></a>

```c
uint32_t fraction
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fraction](#ad33fb2e743756bde8538ac6d2ff3eae8)。

小数秒值（Fractional Seconds Value）。

<a id="r_a59a1abe8f7129bad82e33e5709cf46af"></a>

```c
uint32_t rsp_delay_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rsp_delay_us](#a59a1abe8f7129bad82e33e5709cf46af)。

服务器发送响应到客户端接收之间的估计延迟（Estimated Delay），单位为微秒。

## 88.2\_详细说明（Detailed Documentation）

<a id="ad33fb2e743756bde8538ac6d2ff3eae8"></a>

### `fraction`

```c
uint32_t sntp_time::fraction
```

小数秒值（Fractional Seconds Value）。

<a id="a59a1abe8f7129bad82e33e5709cf46af"></a>

### `rsp_delay_us`

```c
uint32_t sntp_time::rsp_delay_us
```

服务器发送响应到客户端接收之间的估计延迟（Estimated Delay），单位为微秒。

<a id="a7dc90613b6ac0265ff49b931a786354f"></a>

### `seconds`

```c
uint64_t sntp_time::seconds
```

第二个值。

本数据类型文档由以下文件生成：

- `zephyr/net/sntp.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/net/sntp.h](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_sntp_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_websocket_request_结构体.md)
