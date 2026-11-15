---
id: learning.zephyr-docs.usb.api-108
title: UMP流响应器API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ump__stream__responder.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_UMP流响应器API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ump__stream__responder.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 108.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注（路径修正）：原网页把文档构建服务器的绝对目录写入头文件包含展示。本译文统一使用 `#include "ump_stream_responder.h"`；文件位于官方源码树的 `lib/midi2/`。启用 `CONFIG_MIDI2_UMP_STREAM_RESPONDER` 后，该目录由对应CMake文件加入包含搜索路径。

响应 UMP 流消息中的端点发现（Endpoint Discovery）或功能块发现（Function Block Discovery）。

响应 UMP 流消息中的端点发现（Endpoint Discovery）或功能块发现（Function Block Discovery）。

引入版本（Since）：4.3。

接口版本（Version）：0.1.0。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》（Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol）第 7.1 节：UMP 流消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

## 108.2\_数据结构（Data Structures）

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

## 108.3\_宏定义（Macros）

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

## 108.4\_类型定义（Typedefs）

<a id="r_ga2eb945a1c7ab32ffe8a88cb8389ecee2"></a>

```c
typedef void(* ump_send_func) (const void *, const struct midi_ump)
```

用于发送 UMP 的函数。

相关声明：[ump_send_func](P108_UMP流响应器API.md#ga2eb945a1c7ab32ffe8a88cb8389ecee2)、[midi_ump](P099_通用MIDI数据包结构.md)。

## 108.5\_函数（Functions）

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

## 108.6\_详细说明（Detailed Documentation）

<a id="ga7aa6fafe515f65633f688325c1209dfb"></a>

### 108.6.1\_`UMP\_BLOCK\_DT\_SPEC\_GET`

```c
#define UMP_BLOCK_DT_SPEC_GET ( _node)
```

```c
#include "ump_stream_responder.h"
```

**宏展开值（Value）**

```c
{                                                                          \
        .name = DT_PROP_OR(_node, label, NULL),                            \
        .first_group = DT_REG_ADDR(_node),                                 \
        .groups_spanned = DT_REG_SIZE(_node),                              \
        .is_input = !DT_ENUM_HAS_VALUE(_node, terminal_type, output_only), \
        .is_output = !DT_ENUM_HAS_VALUE(_node, terminal_type, input_only), \
        .is_midi1 = !DT_ENUM_HAS_VALUE(_node, protocol, midi2),            \
        .is_31250bps = DT_PROP(_node, serial_31250bps),                    \
}
```

从设备树（Devicetree）表示中取得通用 MIDI 数据包端点的功能块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_node` | 表示 midi2 功能块的设备树节点。 |

> 译注（源码核对）：将reg的地址与长度分别解释为first_group和groups_spanned；input/output由terminal-type决定，is_midi1在protocol不是midi2时为真。它构造元数据，不创建USB接口或串行硬件。

<a id="gabf5f00353c2020155db45098545a96e2"></a>

### 108.6.2\_`UMP\_BLOCK\_SEP\_IF\_OKAY`

```c
#define UMP_BLOCK_SEP_IF_OKAY ( _node)
```

```c
#include "ump_stream_responder.h"
```

**宏展开值（Value）**

```c
COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(_node),     \
            (UMP_BLOCK_DT_SPEC_GET(_node),),    \
            ())
```

> 译注（源码核对）：只对状态为okay的节点展开功能块初始化器及尾随逗号，其余节点展开为空。这里的逗号用于拼接数组初始化列表。

<a id="ga7e17790c09506555db99a10332481ede"></a>

### 108.6.3\_`UMP\_ENDPOINT\_DT\_SPEC\_GET`

```c
#define UMP_ENDPOINT_DT_SPEC_GET ( _node)
```

```c
#include "ump_stream_responder.h"
```

**宏展开值（Value）**

```c
{                                                                               \
        .name = DT_PROP_OR(_node, label, NULL),                                 \
        .n_blocks = DT_FOREACH_CHILD_SEP(_node, DT_NODE_HAS_STATUS_OKAY, (+)),  \
        .blocks = {DT_FOREACH_CHILD(_node, UMP_BLOCK_SEP_IF_OKAY)},             \
}
```

从 midi2 设备的设备树表示中取得通用 MIDI 数据包端点描述。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_node` | 表示 midi2 设备的设备树节点。 |

> 译注（源码核对）：n_blocks统计状态为okay的子节点，blocks按对应遍历顺序生成。后续功能块发现使用此数组的连续索引，不能将功能块编号与first_group的UMP组号混为一谈。

<a id="ga94a59bba33f8dd48d0044e3e048987c1"></a>

### 108.6.4\_`UMP\_STREAM\_RESPONDER`

```c
#define UMP_STREAM_RESPONDER ( _dev, _send, _ep_spec )
```

```c
#include "ump_stream_responder.h"
```

**宏展开值（Value）**

```c
{                                                                       \
        .dev = _dev,                                                    \
        .send = (ump_send_func) _send,  \
        .ep_spec = _ep_spec,                                            \
}
```

初始化 UMP 流响应器配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 用于发送回复数据包的设备。 |
| `_send` | 发送函数。 |
| `_ep_spec` | UMP 端点配置描述。 |

> 译注（源码核对）：宏仅创建含dev、send、ep_spec三个成员的初始化器，不启动线程或注册USB回调；_send被强制转换为ump_send_func。应用仍须在收到UMP时调用ump_stream_respond，且保证配置及其引用对象在调用期间有效。

<a id="ga2eb945a1c7ab32ffe8a88cb8389ecee2"></a>

### 108.6.5\_`ump\_send\_func`

```c
typedef void(* ump_send_func) (const void *, const struct midi_ump)
```

```c
#include "ump_stream_responder.h"
```

用于发送 UMP 的函数。

> 译注（源码核对）：返回类型为void，响应器无法通过它取得底层发送错误。官方USB MIDI示例将返回int的usbd_midi_send经初始化宏转换使用；该接口安排不等于发送错误已经由响应器处理，应用设计应核对函数指针类型和失败处理。

<a id="ga276d63d84c2131290293ed6963e41f56"></a>

### 108.6.6\_`ump\_product\_instance\_id()`

```c
const char * ump_product_instance_id ( void )
```

```c
#include "ump_stream_responder.h"
```

**返回（Returns）**：此设备的 UMP 产品实例标识（Product Instance ID）；硬件信息（hwinfo）可用时以其为依据，否则返回空字符串。

> 译注（源码核对）：当前实现返回内部静态43字节缓冲区，最多编码21字节硬件ID为大写十六进制字符串，调用者不应释放或修改它。CONFIG_HWINFO启用且hwinfo_get_device_id返回-ENOSYS时才尝试EUI-64；其他错误得到空字符串。成功值缓存在静态缓冲区，空结果后续调用仍可能重试。

<a id="ga60167d03152b8f97555567f5cc7b73e7"></a>

### 108.6.7\_`ump\_stream\_respond()`

```c
int ump_stream_respond ( const struct ump_stream_responder_cfg * cfg, const struct midi_ump pkt )
```

```c
#include "ump_stream_responder.h"
```

响应一条 UMP 流消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 响应器配置。 |
| `[in] pkt` | 要响应的消息。 |

**返回（Returns）**：作为回复发送的 UMP 数据包数量；出错时返回 -errno。

> 译注（源码核对）：当前实现先检查cfg->send，为NULL返回-EINVAL；非UMP Stream消息、不支持的流状态或未匹配请求均返回0。只分发端点发现与功能块发现。正返回值是调用发送回调的次数，不是链路送达证明，也不会传播void发送回调内部的错误。cfg和所用ep_spec等对象需由调用者保证有效。

## 108.7\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__devicetree-generic-prop_html_ga72e66a2b7a159d8b6210ef9be015c955"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="agroup__devicetree-reg-prop_html_gad223efc6c77d008e55c3588953e85bfb"></a>
<a id="agroup__devicetree-generic-exist_html_gaed773a8782fe00db90e8599ff673e8ed"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__ump__stream__responder_html_ga7aa6fafe515f65633f688325c1209dfb"></a>
<a id="agroup__devicetree-generic-foreach_html_ga1fbeb335d66745803dbf7a185bf10afc"></a>
<a id="agroup__devicetree-generic-foreach_html_ga2f4eead8e8190110f5c0eb353e6a408f"></a>
<a id="agroup__ump__stream__responder_html_gabf5f00353c2020155db45098545a96e2"></a>
<a id="agroup__ump__stream__responder_html_ga2eb945a1c7ab32ffe8a88cb8389ecee2"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P107_UMP功能块发现过滤位.md) · [返回大纲](大纲.md) · [下一章](P109_UMP端点设备树配置.md)
