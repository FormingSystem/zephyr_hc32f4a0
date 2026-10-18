---
id: learning.zephyr-docs.observability.obapi-7
title: STMESP日志解复用接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第32章\_STMESP日志解复用接口

原文：[group__log__frontend__stmesp__demux__apis](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html)。读取日期：2026-10-13，`latest`。

## 32.1\_用途、头文件与数据结构

本页描述 **STM扩展激励端口（STM Extended Stimulus Port，STMESP）**流的**解复用器（Demultiplexer）**。原文将其描述为主机端解复用器，用于拆分承载日志和跟踪点的 **MIPI系统跟踪协议第2版（MIPI System Trace Protocol v2，STPv2）**流。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

| 类型 | 含义 |
| --- | --- |
| [`struct log_frontend_stmesp_demux_log_header`](P036_STMESP日志消息头.md) | 日志消息头 |
| [`union log_frontend_stmesp_demux_header`](P037_STMESP消息头联合体.md) | 用于向日志消息头写入原始数据的联合体 |
| [`struct log_frontend_stmesp_demux_packet_generic`](P038_STMESP通用数据包.md) | 通用STP解复用数据包 |
| [`struct log_frontend_stmesp_demux_log`](P039_STMESP日志数据包.md) | 含日志消息的数据包 |
| [`struct log_frontend_stmesp_demux_trace_point`](P040_STMESP跟踪点数据包.md) | 含跟踪点的数据包 |
| [`struct log_frontend_stmesp_demux_hw_event`](P041_STMESP硬件事件数据包.md) | 含硬件事件（Hardware Event）的数据包 |
| [`union log_frontend_stmesp_demux_packet`](P042_STMESP数据包联合体.md) | 所有数据包类型的联合体 |
| [`struct log_frontend_stmesp_demux_config`](P043_STMESP解复用配置.md) | 解复用器配置 |

## 32.2\_位宽、容量与包类型宏

以下宏定义字段位宽、主设备（Major）容量和消息类型。宏 `BIT(n)` 表达第n位对应的位值。

| 宏 | 定义值 | 说明 |
| --- | --- | --- |
| <a id="ga33581c39a57eca7f96fea9c29386a3e3"></a>[`LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga33581c39a57eca7f96fea9c29386a3e3) | `3` | 主设备索引占用位数 |
| <a id="gaf2b7019394d33a082fec5ab2d2785257"></a>[`LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaf2b7019394d33a082fec5ab2d2785257) | `3` | 严重性级别（Severity Level）占用位数 |
| <a id="gaeaf76dcb74836740115c9b6e3fece73b"></a>[`LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaeaf76dcb74836740115c9b6e3fece73b) | `15` | 总长度占用位数 |
| <a id="ga56ad2b8067d56b9ccedefd57ad5aa0c2"></a>[`LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga56ad2b8067d56b9ccedefd57ad5aa0c2) | `10` | 参数包长度（Package Length）占用位数 |
| <a id="ga4ac8c23bbf2eaf23a73698e3e36a9594"></a>[`LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga4ac8c23bbf2eaf23a73698e3e36a9594) | `1` | 是否带十六进制转储（Hexdump）的标志位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_MAJOR_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga8f23994b914214a2c83d2e9aa63f0cb5) | `BIT(LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS)` | 支持的主设备最大数量 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_LOG`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga0f6129f8e757a6ef4b02779e57ff58f7) | `0` | 日志消息类型 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_TRACE_POINT`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga7a428120f117a62a5d649f18111364c2) | `1` | 跟踪点消息类型 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_HW_EVENT`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga67cbf7c7892b76c7347b229a0452bfa3) | `2` | 硬件事件消息类型 |

## 32.3\_初始化

<a id="ga97f9ac1d7b459e9d3d715b5367e29a31"></a>

```c
int log_frontend_stmesp_demux_init(const struct log_frontend_stmesp_demux_config *config);
```

初始化解复用器。`config` 为配置。成功返回 `0`，配置无效返回 `-EINVAL`。

## 32.4\_流标识与日志源

以下接口将已识别的流信息传给解复用器：

```c
void log_frontend_stmesp_demux_major(uint16_t id);
void log_frontend_stmesp_demux_channel(uint16_t id);
void log_frontend_stmesp_demux_source_id(uint16_t source_id);
```

| 函数 | 行为与参数 |
| --- | --- |
| <a id="ga8be4ca332fa9145fad72a6b45245a9ff"></a>[`log_frontend_stmesp_demux_major()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga8be4ca332fa9145fad72a6b45245a9ff) | 通知遇到STPv2流中的主设备操作码（Major Opcode）；`id` 为主设备标识符（Master ID） |
| <a id="ga4f86c0cfb38fa05389462045019a6650"></a>[`log_frontend_stmesp_demux_channel()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga4f86c0cfb38fa05389462045019a6650) | 通知遇到通道操作码（Channel Opcode）；`id` 为通道标识符 |
| <a id="gae5925a640c401cc09dd744945eafd51c"></a>[`log_frontend_stmesp_demux_source_id()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gae5925a640c401cc09dd744945eafd51c) | 通知日志源标识符（Source ID）；参数为 `source_id` |

## 32.5\_包起止、时间戳与数据

下列接口用于通知包边界和包内容：

<a id="gaed29a1869e710cd95c19c48c67a36aa8"></a>

<a id="ga6a25dd796a8759009e14b5770f7653a9"></a>

<a id="ga184cc4d266a010aa094a45aba0fad638"></a>

<a id="ga235c0d680cb674b6e99d886497f257d5"></a>

<a id="ga38e05a234824b0adbeca16cb3e21cc75"></a>

```c
int log_frontend_stmesp_demux_packet_start(uint32_t *data, uint64_t *ts);
void log_frontend_stmesp_demux_timestamp(uint64_t ts);
void log_frontend_stmesp_demux_data(uint8_t *data, size_t len);
void log_frontend_stmesp_demux_packet_end(void);
int log_frontend_stmesp_demux_log0(uint16_t source_id, uint64_t *ts);
```

[`log_frontend_stmesp_demux_packet_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaed29a1869e710cd95c19c48c67a36aa8) 通知检测到包起始，原文标记为 `DMTS`。`data` 为数据，可以是 `NULL`，表示不带数据的跟踪点；时间戳（Timestamp）指针 `ts` 也可以是 `NULL`。原文未列出返回值约定。

[`log_frontend_stmesp_demux_timestamp()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga184cc4d266a010aa094a45aba0fad638) 传入时间戳值 `ts`。时间戳通知与包起始分离，因为按照 STM 规范3.2.2节，时间戳可能被分配给后续数据包。

[`log_frontend_stmesp_demux_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga235c0d680cb674b6e99d886497f257d5) 传入数据缓冲区 `data` 及长度 `len`。[`log_frontend_stmesp_demux_packet_end()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga38e05a234824b0adbeca16cb3e21cc75) 无参数，通知包结束标志（Flag）。

[`log_frontend_stmesp_demux_log0()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga6a25dd796a8759009e14b5770f7653a9) 通知一条无参数的优化日志消息；`source_id` 是日志源标识符，`ts` 是可为 `NULL` 的时间戳指针。原文未列出返回值约定。

## 32.6\_取得和释放数据包

<a id="gaf7b66578311278e6d58312ea239c9c0c"></a>

<a id="gad9c13b59d1e09a240ed35b03b04b1a96"></a>

```c
union log_frontend_stmesp_demux_packet log_frontend_stmesp_demux_claim(void);
void log_frontend_stmesp_demux_free(union log_frontend_stmesp_demux_packet packet);
```

[`log_frontend_stmesp_demux_claim()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaf7b66578311278e6d58312ea239c9c0c) 取得待处理的日志消息数据包。取得后必须通过 [`log_frontend_stmesp_demux_free()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gad9c13b59d1e09a240ed35b03b04b1a96) 释放；后者的参数 `packet` 为先前取得的包。

> 译注：原文将 `claim()` 的返回值描述为“包指针或NULL”，但实际声明返回的是 `union log_frontend_stmesp_demux_packet` 联合体。这里保留准确函数签名；指针通过联合体成员承载，不能把函数返回值本身当成普通指针。

## 32.7\_丢弃计数、空闲状态与重置

下列接口读取或维护解复用器状态：

```c
uint32_t log_frontend_stmesp_demux_get_dropped(void);
bool log_frontend_stmesp_demux_is_idle(void);
void log_frontend_stmesp_demux_reset(void);
int log_frontend_stmesp_demux_max_utilization(void);
```

| 函数 | 行为与返回值 |
| --- | --- |
| <a id="gaa624af8e67b4be013f0ec1507d805c34"></a>[`log_frontend_stmesp_demux_get_dropped()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaa624af8e67b4be013f0ec1507d805c34) | 返回丢弃的消息数，并重置计数器；包缓冲区空间不足时可能丢弃消息 |
| <a id="ga1d693b8936666f7b352fd7e25535ac16"></a>[`log_frontend_stmesp_demux_is_idle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga1d693b8936666f7b352fd7e25535ac16) | 检查是否存在已开始但尚未完成的日志消息；没有这类待处理消息时返回 `true`，存在时返回 `false` |
| <a id="ga487c9163e6477a879136350d4c109641"></a>[`log_frontend_stmesp_demux_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga487c9163e6477a879136350d4c109641) | 关闭所有已打开的消息，并标为无效；无返回值 |
| <a id="ga7be93bc9ad1ecfe37f5af64adf029f39"></a>[`log_frontend_stmesp_demux_max_utilization()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga7be93bc9ad1ecfe37f5af64adf029f39) | 返回缓冲区最大使用量，成功值大于或等于 `0`；功能未启用返回 `-ENOTSUP`。原文未注明该数值单位 |

## 32.8\_快速日志的名称与格式字符串

以下接口解析**快速日志（Turbo Logging）**的源名称与格式字符串：

<a id="ga10621a1e4c5b875650b3ff89b3e97297"></a>

<a id="ga7c692b9d84aedfb30673a58959465ccf"></a>

```c
const char *log_frontend_stmesp_demux_sname_get(uint32_t m_id, uint16_t s_id);
const char *log_frontend_stmesp_demux_str_get(uint32_t m_id, uint16_t s_id);
```

[`log_frontend_stmesp_demux_sname_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga10621a1e4c5b875650b3ff89b3e97297) 返回快速日志的源名称。启动时，协处理器会发送保存日志源数据的内存位置，包括**快速轻量处理器（Fast Lightweight Processor，FLPR）**和**外围处理器（Peripheral Processor，PPR）**。如果应用核心拥有这些核心并能访问该内存，就可根据芯片标识符与日志源标识符取得源名称。参数 `m_id` 为主设备标识符，`s_id` 为日志源标识符。返回源名称字符串指针；无法取得时返回表示未知名称的字符串。

[`log_frontend_stmesp_demux_str_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga7c692b9d84aedfb30673a58959465ccf) 返回快速日志的格式字符串。快速日志通过索引引用格式字符串，不直接携带字符串；此函数利用来源核心共享的日志源数据，将索引还原为格式字符串。`m_id` 为主设备标识符，`s_id` 为日志源标识符，即字符串索引。成功返回格式字符串指针；无法取得时返回空字符串或 `"unknown"` 字符串。

---

[上一章：STMESP日志接口目录](P031_STMESP日志接口目录.md) · [下一章：插桩事件头](P033_插桩事件头.md) · [返回大纲](大纲.md)
