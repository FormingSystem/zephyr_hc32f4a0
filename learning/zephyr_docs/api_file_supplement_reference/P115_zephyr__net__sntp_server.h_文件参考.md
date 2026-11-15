---
id: learning.zephyr-docs.api-file-supplement-reference.page-115
title: zephyr__net__sntp_server.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_zephyr\_\_net\_\_sntp\_server.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sntp__server_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络时间协议（Simple Network Time Protocol，SNTP，RFC 5905）的服务器。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

简单网络时间协议（Simple Network Time Protocol，SNTP，RFC 5905）的服务器。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 115.1\_函数（Functions）

<a id="r_ga36c5b4a695294c7ad6777fe79d08b798"></a>

```c
void sntp_server_clock_source (const uint8_t ref_id[4], uint8_t stratum, int8_t precision)
```

相关声明：[sntp_server_clock_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html#ga36c5b4a695294c7ad6777fe79d08b798)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置简单网络时间协议（SNTP）的时间源标识（Time Source ID）、层级（Stratum）和精度（Precision）。


## 115.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P801_sntp_server.h_源码浏览.md)
- [sntp_server_clock_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html#ga36c5b4a695294c7ad6777fe79d08b798)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>

---

[上一章](P114_zephyr__drivers__clock_control__smartbond_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P116_zephyr__bluetooth__mesh__sol_pdu_rpl_srv.h_文件参考.md)
