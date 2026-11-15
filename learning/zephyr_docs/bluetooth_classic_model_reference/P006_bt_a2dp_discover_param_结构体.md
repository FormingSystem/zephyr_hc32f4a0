---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-6
title: bt_a2dp_discover_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__discover__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_bt\_a2dp\_discover\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__discover__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a806fdbaf6d26ad269608afaa21c2035f"></a>

```c
bt_a2dp_discover_ep_cb cb
```

相关声明：[bt_a2dp_discover_ep_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae054d7f9fa92e45c7d40ec0e1d8730ed)、[cb](#a806fdbaf6d26ad269608afaa21c2035f)。

发现回调（Discovery Callback）。

<a id="r_a14b69e2449f1d2379183690246f55a88"></a>

```c
struct bt_a2dp_ep_info info
```

相关声明：[bt_a2dp_ep_info](P008_bt_a2dp_ep_info_结构体.md)、[info](#a14b69e2449f1d2379183690246f55a88)。

由 `cb` 回调返回的已发现端点信息。

<a id="r_ab4174f0b43d1804192cd4647d29779d3"></a>

```c
struct bt_avdtp_sep_info * seps_info
```

相关声明：[bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)、[seps_info](#ab4174f0b43d1804192cd4647d29779d3)。

能够获取的远端端点的最大数量；其端点信息在内部保存。

<a id="r_a21921b756aae5e7e18bf4a018228d93e"></a>

```c
uint16_t avdtp_version
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[avdtp_version](#a21921b756aae5e7e18bf4a018228d93e)。

对端 A2DP 服务发现协议（SDP）服务中的 AVDTP 版本。

<a id="r_a382ce8462958f69af19e325491c6f01b"></a>

```c
uint8_t sep_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sep_count](#a382ce8462958f69af19e325491c6f01b)。

本次调用流程能够获取的流端点（Stream End Points，SEP）的最大数量。

## 6.2\_详细说明（Detailed Documentation）

<a id="a21921b756aae5e7e18bf4a018228d93e"></a>

### `avdtp_version`

```c
uint16_t bt_a2dp_discover_param::avdtp_version
```

对端 A2DP 服务发现协议（SDP）服务中的 AVDTP 版本。

协议栈使用此值来决定采用 `get_all_cap` 还是 `get_cap` 命令。当双方版本均为 v1.3 或更高时，使用 `get_all_cap`，否则使用 `get_cap`。该值与 AVDTP 规范中的版本值相同，例如 `0x0103` 表示版本 1.3。若其值为 0，表示未知，协议栈按低于 v1.3 处理。

<a id="a806fdbaf6d26ad269608afaa21c2035f"></a>

### `cb`

```c
bt_a2dp_discover_ep_cb bt_a2dp_discover_param::cb
```

发现回调（Discovery Callback）。

<a id="a14b69e2449f1d2379183690246f55a88"></a>

### `info`

```c
struct bt_a2dp_ep_info bt_a2dp_discover_param::info
```

由 `cb` 回调返回的已发现端点信息。

<a id="a382ce8462958f69af19e325491c6f01b"></a>

### `sep_count`

```c
uint8_t bt_a2dp_discover_param::sep_count
```

本次调用流程能够获取的流端点（Stream End Points，SEP）的最大数量。

<a id="ab4174f0b43d1804192cd4647d29779d3"></a>

### `seps_info`

```c
struct bt_avdtp_sep_info* bt_a2dp_discover_param::seps_info
```

能够获取的远端端点的最大数量；其端点信息在内部保存。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [bt_a2dp_discover_ep_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae054d7f9fa92e45c7d40ec0e1d8730ed)
- [bt_a2dp_ep_info](P008_bt_a2dp_ep_info_结构体.md)
- [bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_bt_a2dp_codec_sbc_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_bt_a2dp_ep_结构体.md)
