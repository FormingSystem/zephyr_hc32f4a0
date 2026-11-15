---
id: learning.zephyr-docs.modem-wireless-model-reference.page-8
title: cellular_stats_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__stats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_cellular\_stats\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__stats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝链路（Cellular Link）的运行统计信息。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

蜂窝链路运行统计（Cellular link operational statistics）。各计数器从启动开始累计。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a55182117beb8835b88933fc06bbf456b"></a>

```c
uint32_t outage_ms
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[outage_ms](#a55182117beb8835b88933fc06bbf456b)。

调制解调器处于未注册状态的累计时间，单位为毫秒。

<a id="r_aea6fa41e067af9130a8680c2f2b65af6"></a>

```c
uint32_t deregistrations
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[deregistrations](#aea6fa41e067af9130a8680c2f2b65af6)。

从已注册转为未注册的次数。

<a id="r_ad5bd53938a943cac53c0efadcc292022"></a>

```c
uint32_t link_drops
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[link_drops](#ad5bd53938a943cac53c0efadcc292022)。

数据链路载波丢失次数。

<a id="r_a5385d92eca6a89ebce4845624aa5b52a"></a>

```c
uint32_t command_failures
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[command_failures](#a5385d92eca6a89ebce4845624aa5b52a)。

控制通道命令失败次数。

<a id="r_a48298ae752e4950d81929c2e77724f9f"></a>

```c
uint32_t command_errors_cme
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[command_errors_cme](#a48298ae752e4950d81929c2e77724f9f)。

`+CME ERROR` 响应次数。

<a id="r_af542f63589fdeecc4c6f108865177841"></a>

```c
uint32_t recoveries
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recoveries](#af542f63589fdeecc4c6f108865177841)。

进入恢复流程的次数。

<a id="r_a802456c378f817a07404c4d3cd488109"></a>

```c
uint32_t cmux_disconnects
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cmux_disconnects](#a802456c378f817a07404c4d3cd488109)。

串行端口复用（CMUX）失步或断连事件次数。

## 8.2\_详细说明（Detailed Documentation）

<a id="a802456c378f817a07404c4d3cd488109"></a>

### `cmux_disconnects`

```c
uint32_t cellular_stats::cmux_disconnects
```

串行端口复用（CMUX）失步或断连事件次数。

<a id="a48298ae752e4950d81929c2e77724f9f"></a>

### `command_errors_cme`

```c
uint32_t cellular_stats::command_errors_cme
```

`+CME ERROR` 响应次数。

<a id="a5385d92eca6a89ebce4845624aa5b52a"></a>

### `command_failures`

```c
uint32_t cellular_stats::command_failures
```

控制通道命令失败次数。

<a id="aea6fa41e067af9130a8680c2f2b65af6"></a>

### `deregistrations`

```c
uint32_t cellular_stats::deregistrations
```

从已注册转为未注册的次数。

<a id="ad5bd53938a943cac53c0efadcc292022"></a>

### `link_drops`

```c
uint32_t cellular_stats::link_drops
```

数据链路载波丢失次数。

<a id="a55182117beb8835b88933fc06bbf456b"></a>

### `outage_ms`

```c
uint32_t cellular_stats::outage_ms
```

调制解调器处于未注册状态的累计时间，单位为毫秒。

<a id="af542f63589fdeecc4c6f108865177841"></a>

### `recoveries`

```c
uint32_t cellular_stats::recoveries
```

进入恢复流程的次数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_cellular_network_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_conn_mgr_conn_api_结构体.md)
