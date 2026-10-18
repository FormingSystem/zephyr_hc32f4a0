---
id: learning.zephyr-docs.observability.obheader-3
title: STMESP日志前端头文件
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第47章\_STMESP日志前端头文件

原文：[log__frontend__stmesp_8h](https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp_8h.html)。读取日期：2026-10-13，`latest`。

## 47.1\_用途与包含关系

`zephyr/logging/log_frontend_stmesp.h` 是STM扩展激励端口（STM Extended Stimulus Port，STMESP）日志前端的头文件。STM是系统跟踪宏单元（System Trace Macrocell），ETR是嵌入式跟踪路由器（Embedded Trace Router）；快速日志（Turbo Logging）用于优化无参数或单参数消息。

官方页面列出的包含项如下：

```c
#include <errno.h>
#include <zephyr/types.h>
```

[查看官方头文件源码](../stmesp_source_reference/P001_STMESP日志前端头文件源码.md)。

## 47.2\_日志宏

| 宏签名 | 说明 |
| --- | --- |
| `LOG_FRONTEND_STMESP_LOG0(_source, ...)` | 处理无参数快速日志消息 |
| `LOG_FRONTEND_STMESP_LOG1(_source, ...)` | 处理单参数快速日志消息 |

本文件参考页只列宏签名；完整宏值见[日志前端接口](P030_STMESP日志前端接口.md)。

## 47.3\_函数声明

以下声明与官方头文件参考页对应，完整参数和返回值见[对应接口说明](P030_STMESP日志前端接口.md)。

| 声明 | 说明 |
| --- | --- |
| `int log_frontend_stmesp_etr_ready(void);` | 通知前端ETR/STM已就绪 |
| `void log_frontend_stmesp_pre_sleep(void);` | 进入睡眠前调用的钩子 |
| `void log_frontend_stmesp_dummy_write(void);` | 向STMESP执行空写入 |
| `static void log_frontend_stmesp_tp(uint16_t x);` | 记录跟踪点 |
| `static void log_frontend_stmesp_tp_d32(uint16_t x, uint32_t d);` | 记录带32位数据的跟踪点 |
| `void log_frontend_stmesp_log0(const void *source, uint32_t x);` | 启用快速日志时，处理无参数的日志消息 |
| `void log_frontend_stmesp_log1(const void *source, uint32_t x, uint32_t arg);` | 启用快速日志时，处理带一个参数的日志消息 |

---

[上一章：MIPI_STP解码头文件](P046_MIPI_STP解码头文件.md) · [下一章：STMESP日志解复用头文件](P048_STMESP日志解复用头文件.md) · [返回大纲](大纲.md)
