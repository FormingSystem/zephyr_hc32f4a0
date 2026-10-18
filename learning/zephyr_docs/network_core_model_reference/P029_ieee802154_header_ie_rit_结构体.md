---
id: learning.zephyr-docs.network-core-model-reference.page-29
title: ieee802154_header_ie_rit_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rit.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_ieee802154\_header\_ie\_rit\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rit.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收方发起传输信息元素（RIT IE），见第7.4.2.4节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

接收方发起传输信息元素（RIT IE），见第7.4.2.4节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a94efc1605d6799a9d88e6cb801f7ec0b"></a>

```c
uint8_t time_to_first_listen
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[time_to_first_listen](#a94efc1605d6799a9d88e6cb801f7ec0b)。

到首次监听的时间（Time to First Listen）。

<a id="r_a5eaca9e09ebdbb933b4324c899c248b4"></a>

```c
uint8_t number_of_repeat_listen
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[number_of_repeat_listen](#a5eaca9e09ebdbb933b4324c899c248b4)。

重复监听次数（Number of Repeat Listen）。

<a id="r_a73cd396d5e98799b655242f525ccf42b"></a>

```c
uint16_t repeat_listen_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[repeat_listen_interval](#a73cd396d5e98799b655242f525ccf42b)。

重复监听间隔（Repeat Listen Interval）。

## 29.2\_详细说明（Detailed Documentation）

<a id="a5eaca9e09ebdbb933b4324c899c248b4"></a>

### `number_of_repeat_listen`

```c
uint8_t ieee802154_header_ie_rit::number_of_repeat_listen
```

重复监听次数（Number of Repeat Listen）。

<a id="a73cd396d5e98799b655242f525ccf42b"></a>

### `repeat_listen_interval`

```c
uint16_t ieee802154_header_ie_rit::repeat_listen_interval
```

重复监听间隔（Repeat Listen Interval）。

<a id="a94efc1605d6799a9d88e6cb801f7ec0b"></a>

### `time_to_first_listen`

```c
uint8_t ieee802154_header_ie_rit::time_to_first_listen
```

到首次监听的时间（Time to First Listen）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_ieee802154_header_ie_time_correction_结构体.md)
