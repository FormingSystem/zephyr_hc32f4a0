---
id: learning.zephyr-docs.network-core-model-reference.page-183
title: wifi_reg_chan_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__reg__chan__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_wifi\_reg\_chan\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__reg__chan__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

各信道的监管属性（Regulatory Attributes）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

各信道的监管属性（Regulatory Attributes）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 183.1\_数据成员（Data Fields）

<a id="r_a0addffc11ef29f50c01b700835e59930"></a>

```c
unsigned short center_frequency
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[center_frequency](#a0addffc11ef29f50c01b700835e59930)。

中心频率（Center frequency），单位为 MHz。

<a id="r_af9169ab4a41fac4c6f6766fc96799545"></a>

```c
unsigned short max_power:8
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[max_power](#af9169ab4a41fac4c6f6766fc96799545)。

最大发射功率（Maximum transmission power），单位为 dBm。

<a id="r_aa044611e18b7332b8577e29f6a769e3f"></a>

```c
unsigned short supported:1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[supported](#aa044611e18b7332b8577e29f6a769e3f)。

是否支持此信道（Channel supported）。

<a id="r_acc7a88b004c9a61c8bf9ee1a97f85928"></a>

```c
unsigned short passive_only:1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[passive_only](#acc7a88b004c9a61c8bf9ee1a97f85928)。

仅允许被动传输（Passive transmissions only）。

<a id="r_a1ab137c142902d2de7d6be2626d7ac1f"></a>

```c
unsigned short dfs:1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[dfs](#a1ab137c142902d2de7d6be2626d7ac1f)。

是否为动态频率选择信道（DFS channel）。

## 183.2\_详细说明（Detailed Documentation）

<a id="a0addffc11ef29f50c01b700835e59930"></a>

### `center_frequency`

```c
unsigned short wifi_reg_chan_info::center_frequency
```

中心频率（Center frequency），单位为 MHz。

<a id="a1ab137c142902d2de7d6be2626d7ac1f"></a>

### `dfs`

```c
unsigned short wifi_reg_chan_info::dfs
```

是否为动态频率选择信道（DFS channel）。

<a id="af9169ab4a41fac4c6f6766fc96799545"></a>

### `max_power`

```c
unsigned short wifi_reg_chan_info::max_power
```

最大发射功率（Maximum transmission power），单位为 dBm。

<a id="acc7a88b004c9a61c8bf9ee1a97f85928"></a>

### `passive_only`

```c
unsigned short wifi_reg_chan_info::passive_only
```

仅允许被动传输（Passive transmissions only）。

<a id="aa044611e18b7332b8577e29f6a769e3f"></a>

### `supported`

```c
unsigned short wifi_reg_chan_info::supported
```

是否支持此信道（Channel supported）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 183.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P182_wifi_raw_scan_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P184_wifi_reg_domain_结构体.md)
