---
id: learning.zephyr-docs.observability.obheader-4
title: STMESP日志解复用头文件
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp__demux_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第48章\_STMESP日志解复用头文件

原文：[log__frontend__stmesp__demux_8h](https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp__demux_8h.html)。读取日期：2026-10-13，`latest`。

## 48.1\_用途与包含关系

`zephyr/logging/log_frontend_stmesp_demux.h` 是STM扩展激励端口（STM Extended Stimulus Port，STMESP）流解复用器（Demultiplexer）的头文件。STPv2表示MIPI系统跟踪协议第2版（MIPI System Trace Protocol v2）；接口传递主设备（Major）、通道（Channel）、源标识符（Source ID）、时间戳（Timestamp）和快速日志（Turbo Logging）数据。

官方页面列出的包含项如下：

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/mpsc_packet.h>
```

[查看官方头文件源码](../stmesp_source_reference/P002_STMESP日志解复用头文件源码.md)。

## 48.2\_数据结构

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

## 48.3\_位宽和消息类型宏

以下宏定义字段位宽、主设备（Major）容量和消息类型。宏 `BIT(n)` 表达第n位对应的位值。

| 宏 | 定义值 | 说明 |
| --- | --- | --- |
| [`LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga33581c39a57eca7f96fea9c29386a3e3) | `3` | 主设备索引占用位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaf2b7019394d33a082fec5ab2d2785257) | `3` | 严重性级别（Severity Level）占用位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#gaeaf76dcb74836740115c9b6e3fece73b) | `15` | 总长度占用位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga56ad2b8067d56b9ccedefd57ad5aa0c2) | `10` | 参数包长度（Package Length）占用位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga4ac8c23bbf2eaf23a73698e3e36a9594) | `1` | 是否带十六进制转储（Hexdump）的标志位数 |
| [`LOG_FRONTEND_STMESP_DEMUX_MAJOR_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga8f23994b914214a2c83d2e9aa63f0cb5) | `BIT(LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS)` | 支持的主设备最大数量 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_LOG`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga0f6129f8e757a6ef4b02779e57ff58f7) | `0` | 日志消息类型 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_TRACE_POINT`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga7a428120f117a62a5d649f18111364c2) | `1` | 跟踪点消息类型 |
| [`LOG_FRONTEND_STMESP_DEMUX_TYPE_HW_EVENT`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga67cbf7c7892b76c7347b229a0452bfa3) | `2` | 硬件事件消息类型 |

## 48.4\_函数声明

`DMTS` 是原文用于标识包起始的操作码记号。以下声明与官方头文件参考页对应，完整参数和返回值见[对应接口说明](P032_STMESP日志解复用接口.md)。

| 声明 | 说明 |
| --- | --- |
| `int log_frontend_stmesp_demux_init(const struct log_frontend_stmesp_demux_config *config);` | 初始化解复用器 |
| `void log_frontend_stmesp_demux_major(uint16_t id);` | 通知STPv2流中的主设备操作码 |
| `void log_frontend_stmesp_demux_channel(uint16_t id);` | 通知STPv2流中的通道操作码 |
| `int log_frontend_stmesp_demux_packet_start(uint32_t *data, uint64_t *ts);` | 通知检测到包起始（DMTS） |
| `int log_frontend_stmesp_demux_log0(uint16_t source_id, uint64_t *ts);` | 通知不带参数的优化日志消息 |
| `void log_frontend_stmesp_demux_source_id(uint16_t source_id);` | 通知源标识符 |
| `void log_frontend_stmesp_demux_timestamp(uint64_t ts);` | 通知时间戳 |
| `void log_frontend_stmesp_demux_data(uint8_t *data, size_t len);` | 通知数据 |
| `void log_frontend_stmesp_demux_packet_end(void);` | 通知包结束标志（Flag） |
| `uint32_t log_frontend_stmesp_demux_get_dropped(void);` | 取得丢弃消息数并重置计数器 |
| `union log_frontend_stmesp_demux_packet log_frontend_stmesp_demux_claim(void);` | 取得数据包 |
| `void log_frontend_stmesp_demux_free(union log_frontend_stmesp_demux_packet packet);` | 释放先前取得的数据包 |
| `const char * log_frontend_stmesp_demux_sname_get(uint32_t m_id, uint16_t s_id);` | 取得快速日志消息的源名称 |
| `const char * log_frontend_stmesp_demux_str_get(uint32_t m_id, uint16_t s_id);` | 取得快速日志消息的格式字符串 |
| `bool log_frontend_stmesp_demux_is_idle(void);` | 检查是否有已开始但未完成的日志消息 |
| `void log_frontend_stmesp_demux_reset(void);` | 关闭所有已打开消息并标为无效 |
| `int log_frontend_stmesp_demux_max_utilization(void);` | 取得缓冲区最大使用量 |

---

[上一章：STMESP日志前端头文件](P047_STMESP日志前端头文件.md) · [下一章：CPU负载接口](P049_CPU负载接口.md) · [返回大纲](大纲.md)
