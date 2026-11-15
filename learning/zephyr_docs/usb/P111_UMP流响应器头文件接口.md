---
id: learning.zephyr-docs.usb.api-111
title: UMP流响应器头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_UMP流响应器头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 111.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/audio/midi.h>
```

## 111.2\_数据结构（Data Structures）

<a id="r_ump_5Fblock_5Fdt_5Fspec"></a>

```c
struct ump_block_dt_spec
```

UMP 功能块配置描述（Function Block Specification）。

相关声明：[ump_block_dt_spec](P114_UMP功能块设备树配置.md)。

<a id="r_ump_5Fendpoint_5Fdt_5Fspec"></a>

```c
struct ump_endpoint_dt_spec
```

UMP 端点配置描述（Endpoint Specification）。

相关声明：[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)。

<a id="r_ump_5Fstream_5Fresponder_5Fcfg"></a>

```c
struct ump_stream_responder_cfg
```

UMP 流响应器（UMP Stream Responder）的配置。

相关声明：[ump_stream_responder_cfg](P110_UMP流响应器配置.md)。

## 111.3\_宏定义（Macros）

<a id="r_ga94a59bba33f8dd48d0044e3e048987c1"></a>

```c
#define UMP_STREAM_RESPONDER(_dev, _send, _ep_spec)
```

初始化 UMP 流响应器配置。

相关声明：[UMP_STREAM_RESPONDER](P108_UMP流响应器API.md#ga94a59bba33f8dd48d0044e3e048987c1)。

<a id="r_ga7aa6fafe515f65633f688325c1209dfb"></a>

```c
#define UMP_BLOCK_DT_SPEC_GET(_node)
```

从设备树（Devicetree）表示中取得通用 MIDI 数据包端点的功能块。

相关声明：[UMP_BLOCK_DT_SPEC_GET](P108_UMP流响应器API.md#ga7aa6fafe515f65633f688325c1209dfb)。

<a id="r_gabf5f00353c2020155db45098545a96e2"></a>

```c
#define UMP_BLOCK_SEP_IF_OKAY(_node)
```



相关声明：[UMP_BLOCK_SEP_IF_OKAY](P108_UMP流响应器API.md#gabf5f00353c2020155db45098545a96e2)。

<a id="r_ga7e17790c09506555db99a10332481ede"></a>

```c
#define UMP_ENDPOINT_DT_SPEC_GET(_node)
```

从 midi2 设备的设备树表示中取得通用 MIDI 数据包端点描述。

相关声明：[UMP_ENDPOINT_DT_SPEC_GET](P108_UMP流响应器API.md#ga7e17790c09506555db99a10332481ede)。

## 111.4\_类型定义（Typedefs）

<a id="r_ga2eb945a1c7ab32ffe8a88cb8389ecee2"></a>

```c
typedef void(* ump_send_func) (const void *, const struct midi_ump)
```

用于发送 UMP 的函数。

相关声明：[ump_send_func](P108_UMP流响应器API.md#ga2eb945a1c7ab32ffe8a88cb8389ecee2)、[midi_ump](P099_通用MIDI数据包结构.md)。

## 111.5\_函数（Functions）

<a id="r_ga60167d03152b8f97555567f5cc7b73e7"></a>

```c
int ump_stream_respond (const struct ump_stream_responder_cfg *cfg, const struct midi_ump pkt)
```

响应一条 UMP 流消息。

相关声明：[ump_stream_respond](P108_UMP流响应器API.md#ga60167d03152b8f97555567f5cc7b73e7)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_ga276d63d84c2131290293ed6963e41f56"></a>

```c
const char * ump_product_instance_id (void)
```



相关声明：[ump_product_instance_id](P108_UMP流响应器API.md#ga276d63d84c2131290293ed6963e41f56)。

## 111.6\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>

[上一章](P110_UMP流响应器配置.md) · [返回大纲](大纲.md) · [下一章](P112_UMP流响应器实现参考.md)
