---
id: learning.zephyr-docs.network-core-model-reference.page-181
title: wifi_ps_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ps__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第181章\_wifi\_ps\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ps__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi省电参数（Power Save Parameters）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi省电参数（Power Save Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 181.1\_数据成员（Data Fields）

<a id="r_abb22aaa45833ac130922204bd2fe841b"></a>

```c
enum wifi_ps enabled
```

相关声明：[wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)、[enabled](#abb22aaa45833ac130922204bd2fe841b)。

省电状态（Power save state）。

<a id="r_a8510c799ab0c5825f1c6349f9799c62f"></a>

```c
unsigned short listen_interval
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[listen_interval](#a8510c799ab0c5825f1c6349f9799c62f)。

监听间隔（Listen interval）。

<a id="r_a7cb3e7fb7d9f8bd7c2cab41f879b3b66"></a>

```c
enum wifi_ps_wakeup_mode wakeup_mode
```

相关声明：[wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)、[wakeup_mode](#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)。

Wi‑Fi 省电唤醒模式（Power save wakeup mode）。

<a id="r_a5a022d89d43ecf2cd1f15fc72c0f2bed"></a>

```c
enum wifi_ps_mode mode
```

相关声明：[wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)、[mode](#a5a022d89d43ecf2cd1f15fc72c0f2bed)。

Wi‑Fi 省电模式（Power save mode）。

<a id="r_ad963f1bf78dc271f08b73f3aadb36a91"></a>

```c
unsigned int timeout_ms
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[timeout_ms](#ad963f1bf78dc271f08b73f3aadb36a91)。

Wi‑Fi 省电超时（Power save timeout）。

<a id="r_aef62e5bf6216bf4dc461efe71735c4bd"></a>

```c
enum wifi_ps_param_type type
```

相关声明：[wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)、[type](#aef62e5bf6216bf4dc461efe71735c4bd)。

Wi‑Fi 省电类型（Power save type）。

<a id="r_a63fa2ee03bc4aefada61c298ee14336c"></a>

```c
enum wifi_config_ps_param_fail_reason fail_reason
```

相关声明：[wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)、[fail_reason](#a63fa2ee03bc4aefada61c298ee14336c)。

Wi‑Fi 省电失败原因（Power save fail reason）。

<a id="r_ab9fc62dd1e2928320274fa1554a550a6"></a>

```c
enum wifi_ps_exit_strategy exit_strategy
```

相关声明：[wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)、[exit_strategy](#ab9fc62dd1e2928320274fa1554a550a6)。

Wi‑Fi 省电退出策略（Power save exit strategy）。

## 181.2\_详细说明（Detailed Documentation）

<a id="abb22aaa45833ac130922204bd2fe841b"></a>

### `enabled`

```c
enum wifi_ps wifi_ps_params::enabled
```

省电状态（Power save state）。

<a id="ab9fc62dd1e2928320274fa1554a550a6"></a>

### `exit_strategy`

```c
enum wifi_ps_exit_strategy wifi_ps_params::exit_strategy
```

Wi‑Fi 省电退出策略（Power save exit strategy）。

<a id="a63fa2ee03bc4aefada61c298ee14336c"></a>

### `fail_reason`

```c
enum wifi_config_ps_param_fail_reason wifi_ps_params::fail_reason
```

Wi‑Fi 省电失败原因（Power save fail reason）。

<a id="a8510c799ab0c5825f1c6349f9799c62f"></a>

### `listen_interval`

```c
unsigned short wifi_ps_params::listen_interval
```

监听间隔（Listen interval）。

<a id="a5a022d89d43ecf2cd1f15fc72c0f2bed"></a>

### `mode`

```c
enum wifi_ps_mode wifi_ps_params::mode
```

Wi‑Fi 省电模式（Power save mode）。

<a id="ad963f1bf78dc271f08b73f3aadb36a91"></a>

### `timeout_ms`

```c
unsigned int wifi_ps_params::timeout_ms
```

Wi‑Fi 省电超时（Power save timeout）。

这是发送数据包（TX packet）后、重新进入省电状态（Power save）前的等待超时，单位为毫秒，用于接收来自接入点（AP）的任何回复。值为零表示禁用此功能。

这是功耗（Power consumption）与延迟（Latency）之间的权衡。

<a id="aef62e5bf6216bf4dc461efe71735c4bd"></a>

### `type`

```c
enum wifi_ps_param_type wifi_ps_params::type
```

Wi‑Fi 省电类型（Power save type）。

<a id="a7cb3e7fb7d9f8bd7c2cab41f879b3b66"></a>

### `wakeup_mode`

```c
enum wifi_ps_wakeup_mode wifi_ps_params::wakeup_mode
```

Wi‑Fi 省电唤醒模式（Power save wakeup mode）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 181.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)
- [wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)
- [wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)
- [wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)
- [wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P180_wifi_ps_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P182_wifi_raw_scan_result_结构体.md)
