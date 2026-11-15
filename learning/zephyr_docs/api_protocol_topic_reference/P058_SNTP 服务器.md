---
id: learning.zephyr-docs.api-protocol-topic-reference.page-58
title: SNTP 服务器
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_SNTP 服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络时间协议服务器 API

<a id="details"></a>

简单网络时间协议服务器 API（Simple Network Time Protocol Server API）。自 Zephyr 4.5 起提供；API 版本为 0.1.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 58.1\_函数（Functions）

<a id="r_ga36c5b4a695294c7ad6777fe79d08b798"></a>

```c
void sntp_server_clock_source (const uint8_t ref_id[4], uint8_t stratum, int8_t precision)
```

相关声明：[sntp_server_clock_source](#ga36c5b4a695294c7ad6777fe79d08b798)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置简单网络时间协议（SNTP）的时间源标识（Time Source ID）、层级（Stratum）和精度（Precision）。

## 58.2\_详细说明（Detailed Documentation）

<a id="ga36c5b4a695294c7ad6777fe79d08b798"></a>

### `sntp_server_clock_source()`

```c
void sntp_server_clock_source ( const uint8_t ref_id[4], uint8_t stratum, int8_t precision )
```

```c
#include <zephyr/net/sntp_server.h>
```

设置简单网络时间协议（SNTP）的时间源标识（Time Source ID）、层级（Stratum）和精度（Precision）。

调用此函数之前，服务器在回答查询时会将闰秒指示器（leap indicator）设为“时钟未同步”（clock not synchronized），并将层级（stratum）设为 16，以告知客户端不得使用其时间。应在将系统时钟设为可信时间之后调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ref_id` | 参考标识符（reference ID），参见 RFC 5905 图 12。 |
| `stratum` | 表示时钟源的层级（stratum）。 |
| `precision` | 以 2 为底的指数；2 的该次幂所得值表示系统时钟的精度（precision），单位为秒。 |


## 58.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [zephyr/net/sntp_server.h](../api_file_supplement_reference/P115_zephyr__net__sntp_server.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P057_STM32复位控制器辅助定义.md) · [返回大纲](大纲.md) · [下一章](P059_Wi-Fi 扫描配置（Scanning configuration）.md)
