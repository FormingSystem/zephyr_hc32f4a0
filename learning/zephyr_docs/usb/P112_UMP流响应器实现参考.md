---
id: learning.zephyr-docs.usb.api-112
title: UMP流响应器实现参考
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_UMP流响应器实现参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8c.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 112.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注：本页是官方Doxygen实现文件参考；带static的函数为文件内部实现，不是应用公开调用接口。

```c
#include <string.h>
```

```c
#include <zephyr/devicetree.h>
```

```c
#include <zephyr/drivers/hwinfo.h>
```

```c
#include <zephyr/sys/byteorder.h>
```

```c
#include "ump_stream_responder.h"
```

## 112.2\_宏定义（Macros）

<a id="r_af22f6749914dd434e3b286a03adc2ff1"></a>

```c
#define BIT_IF(cond, n)
```



相关声明：[BIT_IF](P112_UMP流响应器实现参考.md#af22f6749914dd434e3b286a03adc2ff1)。

<a id="r_aab1e4db76018e2d9dc6146defdb9605c"></a>

```c
#define MIDI_CI_VERSION_FORMAT_UMP_1_1 0x01
```

用于 UMP v1.1 设备的 MIDI 能力查询（MIDI Capability Inquiry，MIDI-CI）版本标识符。

相关声明：[MIDI_CI_VERSION_FORMAT_UMP_1_1](P112_UMP流响应器实现参考.md#aab1e4db76018e2d9dc6146defdb9605c)。

## 112.3\_函数（Functions）

<a id="r_a9ade274ddda7615cbd8e524deba886d3"></a>

```c
static bool ep_has_midi1 (const struct ump_endpoint_dt_spec *ep)
```



相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ep_has_midi1](P112_UMP流响应器实现参考.md#a9ade274ddda7615cbd8e524deba886d3)、[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)。

<a id="r_aa742facf306250168f4899b02e2c46e2"></a>

```c
static bool ep_has_midi2 (const struct ump_endpoint_dt_spec *ep)
```



相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ep_has_midi2](P112_UMP流响应器实现参考.md#aa742facf306250168f4899b02e2c46e2)、[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)。

<a id="r_accfcc608d2991462b07b666dadbf39b7"></a>

```c
static struct midi_ump make_endpoint_info (const struct ump_endpoint_dt_spec *ep)
```

构建端点信息通知（Endpoint Info Notification）通用 MIDI 数据包。

相关声明：[midi_ump](P099_通用MIDI数据包结构.md)、[make_endpoint_info](P112_UMP流响应器实现参考.md#accfcc608d2991462b07b666dadbf39b7)、[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)。

<a id="r_a1ca4ec579939a748e14afa8f52c0f125"></a>

```c
static struct midi_ump make_function_block_info (const struct ump_endpoint_dt_spec *ep, size_t block_num)
```

构建功能块信息通知（Function Block Info Notification）通用 MIDI 数据包。

相关声明：[midi_ump](P099_通用MIDI数据包结构.md)、[make_function_block_info](P112_UMP流响应器实现参考.md#a1ca4ec579939a748e14afa8f52c0f125)、[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)。

<a id="r_a39a67d39eef882a7b55272eb04fd7322"></a>

```c
static size_t fill_str (struct midi_ump *ump, size_t offset, const char *src, size_t len)
```

将 ASCII 字符串复制到通用 MIDI 数据包中，同时保留从最高有效端开始的若干字节不变，以便调用者设置这段前缀（Prefix）。

相关声明：[fill_str](P112_UMP流响应器实现参考.md#a39a67d39eef882a7b55272eb04fd7322)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_af0e1c171cff0d7d934e3b91c56c2f76f"></a>

```c
static int send_string (const struct ump_stream_responder_cfg *cfg, const char *string, uint32_t prefix, size_t offset)
```

以 UMP 流的形式发送字符串；如果字符串长度超出一个 UMP 可容纳的范围，可能拆成多个数据包。

相关声明：[send_string](P112_UMP流响应器实现参考.md#af0e1c171cff0d7d934e3b91c56c2f76f)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ae3793fd76cd30ec5c3feb82f9c3ec99b"></a>

```c
static int ump_ep_discover (const struct ump_stream_responder_cfg *cfg, const struct midi_ump pkt)
```

处理端点发现消息。

相关声明：[ump_ep_discover](P112_UMP流响应器实现参考.md#ae3793fd76cd30ec5c3feb82f9c3ec99b)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_aeb7ba5871123d07ca8613152a60bc9e3"></a>

```c
static int ump_fb_discover_block (const struct ump_stream_responder_cfg *cfg, size_t block_num, uint8_t filter)
```



相关声明：[ump_fb_discover_block](P112_UMP流响应器实现参考.md#aeb7ba5871123d07ca8613152a60bc9e3)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a5900fd6e7ff32f0fd97701cbab3bbe86"></a>

```c
static int ump_fb_discover (const struct ump_stream_responder_cfg *cfg, const struct midi_ump pkt)
```

处理功能块发现消息。

相关声明：[ump_fb_discover](P112_UMP流响应器实现参考.md#a5900fd6e7ff32f0fd97701cbab3bbe86)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_ga276d63d84c2131290293ed6963e41f56"></a>

```c
const char * ump_product_instance_id (void)
```



相关声明：[ump_product_instance_id](P108_UMP流响应器API.md#ga276d63d84c2131290293ed6963e41f56)。

<a id="r_ga60167d03152b8f97555567f5cc7b73e7"></a>

```c
int ump_stream_respond (const struct ump_stream_responder_cfg *cfg, const struct midi_ump pkt)
```

响应一条 UMP 流消息。

相关声明：[ump_stream_respond](P108_UMP流响应器API.md#ga60167d03152b8f97555567f5cc7b73e7)、[ump_stream_responder_cfg](P110_UMP流响应器配置.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

## 112.4\_详细说明（Detailed Documentation）

<a id="af22f6749914dd434e3b286a03adc2ff1"></a>

### 112.4.1\_`BIT\_IF`

```c
#define BIT_IF ( cond, n )
```

**宏展开值（Value）**

```c
((cond) ? BIT(n) : 0)
```

> 译注（源码核对）：内部辅助宏：cond为真时返回BIT(n)，否则返回0；它构造通知消息中的条件标志位。

<a id="aab1e4db76018e2d9dc6146defdb9605c"></a>

### 112.4.2\_`MIDI\_CI\_VERSION\_FORMAT\_UMP\_1\_1`

```c
#define MIDI_CI_VERSION_FORMAT_UMP_1_1 0x01
```

用于 UMP v1.1 设备的 MIDI 能力查询（MIDI Capability Inquiry，MIDI-CI）版本标识符。

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.8 节“功能块信息通知”中的 MIDI-CI 消息版本／格式。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

<a id="a9ade274ddda7615cbd8e524deba886d3"></a>

### 112.4.3\_`ep\_has\_midi1()`

```c
static inline bool ep_has_midi1 ( const struct ump_endpoint_dt_spec * ep)
```

> 译注（源码核对）：遍历端点的功能块数组，任一块is_midi1为真即返回true，否则返回false。

<a id="aa742facf306250168f4899b02e2c46e2"></a>

### 112.4.4\_`ep\_has\_midi2()`

```c
static inline bool ep_has_midi2 ( const struct ump_endpoint_dt_spec * ep)
```

> 译注（源码核对）：遍历功能块数组，任一块is_midi1为假即返回true；这只依据配置元数据，不做协议探测。

<a id="a39a67d39eef882a7b55272eb04fd7322"></a>

### 112.4.5\_`fill\_str()`

```c
static inline size_t fill_str ( struct midi_ump * ump, size_t offset, const char * src, size_t len )
```

将 ASCII 字符串复制到通用 MIDI 数据包中，同时保留从最高有效端开始的若干字节不变，以便调用者设置这段前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` ump` | 字符串要复制到的 UMP。 |
| `[in] offset` | 从最高有效端开始需要保留的字节数。 |
| `[in] src` | 源字符串。 |
| `[in] len` | 源字符串长度。 |

**返回（Returns）**：已复制的字节数。

> 译注（源码核对）：offset从128位UMP最高有效端按字节计数；每字内部从高字节向低字节填入。实现使用按位或写入，调用者须先清零待填区域；offset大于等于容器大小时返回0。它处理ASCII字节，不执行字符集转换。

<a id="accfcc608d2991462b07b666dadbf39b7"></a>

### 112.4.6\_`make\_endpoint\_info()`

```c
static inline struct midi_ump make_endpoint_info ( const struct ump_endpoint_dt_spec * ep)
```

构建端点信息通知（Endpoint Info Notification）通用 MIDI 数据包。

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.2 节：端点信息通知消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

> 译注（源码核对）：当前通知写入UMP版本1.1、静态功能块标志、块数量以及根据块元数据计算的MIDI1／MIDI2支持位。描述的是响应器构造的能力消息，不代表外部音频硬件经过实测。

<a id="a1ca4ec579939a748e14afa8f52c0f125"></a>

### 112.4.7\_`make\_function\_block\_info()`

```c
static inline struct midi_ump make_function_block_info ( const struct ump_endpoint_dt_spec * ep, size_t block_num )
```

构建功能块信息通知（Function Block Info Notification）通用 MIDI 数据包。

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.8 节：功能块信息通知。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

> 译注（源码核对）：当前实现直接读取ep->blocks[block_num]，不在此函数内检查边界。通知将块标为活动，携带方向、组范围、MIDI-CI版本与最多255条同时SysEx流的字段；实际调用须通过上层发现路径的编号选择。

<a id="af0e1c171cff0d7d934e3b91c56c2f76f"></a>

### 112.4.8\_`send\_string()`

```c
static inline int send_string ( const struct ump_stream_responder_cfg * cfg, const char * string, uint32_t prefix, size_t offset )
```

以 UMP 流的形式发送字符串；如果字符串长度超出一个 UMP 可容纳的范围，可能拆成多个数据包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 响应器配置。 |
| `[in] string` | 要发送的字符串。 |
| `[in] prefix` | 待发送 UMP 数据包的固定前缀。 |
| `[in] offset` | 字符串在数据包中的起始偏移，单位为字节。 |

**返回（Returns）**：已发送的数据包数量。

> 译注（源码核对）：内部调用以offset=2发送端点／产品名称，以offset=3发送功能块名称，每包分别最多14或13字节。空字符串发送0包；非空字符串按Complete或Start／Continue／End分片，末包剩余区域清零。传入字符串必须可用于strlen，偏移须小于容器大小；发送回调结果不可获取。

<a id="ae3793fd76cd30ec5c3feb82f9c3ec99b"></a>

### 112.4.9\_`ump\_ep\_discover()`

```c
static inline int ump_ep_discover ( const struct ump_stream_responder_cfg * cfg, const struct midi_ump pkt )
```

处理端点发现消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 响应器配置。 |
| `[in] pkt` | 要处理的发现数据包。 |

**返回（Returns）**：作为回复发送的 UMP 数量。

> 译注（源码核对）：当前只处理端点信息、端点名称及启用CONFIG_HWINFO时的产品实例标识请求。设备身份与流配置过滤位虽已定义，此实现未对应生成通知。名称为NULL或产品ID为空时不会生成相应字符串包。

<a id="a5900fd6e7ff32f0fd97701cbab3bbe86"></a>

### 112.4.10\_`ump\_fb\_discover()`

```c
static inline int ump_fb_discover ( const struct ump_stream_responder_cfg * cfg, const struct midi_ump pkt )
```

处理功能块发现消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 响应器配置。 |
| `[in] pkt` | 要处理的发现数据包。 |

**返回（Returns）**：作为回复发送的 UMP 数量。

> 译注（源码核对）：请求编号小于n_blocks时处理单个块；0xff表示遍历全部块；其他越界编号返回0。过滤位决定是否发送块信息和名称。

<a id="aeb7ba5871123d07ca8613152a60bc9e3"></a>

### 112.4.11\_`ump\_fb\_discover\_block()`

```c
static inline int ump_fb_discover_block ( const struct ump_stream_responder_cfg * cfg, size_t block_num, uint8_t filter )
```

> 译注（源码核对）：内部按INFO过滤位发送一份信息通知，按NAME过滤位且名称非NULL时发送名称字符串；此函数自身不验证block_num边界。

## 112.5\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P111_UMP流响应器头文件接口.md) · [返回大纲](大纲.md) · [下一章](P113_UMP格式与MIDI协议依据.md)
