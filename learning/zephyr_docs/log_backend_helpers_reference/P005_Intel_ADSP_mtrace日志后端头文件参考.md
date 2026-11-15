---
id: learning.zephyr-docs.log-backend-helpers-reference.page-5
title: Intel_ADSP_mtrace日志后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__mtrace_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Intel\_ADSP\_mtrace日志后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__mtrace_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Intel ADSP日志后端、标准辅助接口与多域辅助接口。源码跟踪译注与官方原文分开标示。

Intel ADSP mtrace日志后端的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
```

查看此文件的源码。

Intel ADSP mtrace日志后端的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.1\_类型定义（Typedefs）

<a id="r_gab6362dba4defcd461d24a155763b465d"></a>

```c
typedef void(* adsp_mtrace_log_hook_t) (size_t written, size_t space_left)
```

相关声明：[adsp_mtrace_log_hook_t](P004_Intel_ADSP_mtrace日志后端接口.md#gab6362dba4defcd461d24a155763b465d)。

mtrace日志记录器需要一个用于IPC消息的钩子（Hook）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga9bb9152344270b8257182471443caa78"></a>

```c
void adsp_mtrace_log_init (adsp_mtrace_log_hook_t hook)
```

相关声明：[adsp_mtrace_log_init](P004_Intel_ADSP_mtrace日志后端接口.md#ga9bb9152344270b8257182471443caa78)、[adsp_mtrace_log_hook_t](P004_Intel_ADSP_mtrace日志后端接口.md#gab6362dba4defcd461d24a155763b465d)。

初始化Intel ADSP mtrace日志记录器。

<a id="r_gaecd49115065234a120c75f450b799269"></a>

```c
const struct log_backend * log_backend_adsp_mtrace_get (void)
```

相关声明：[log_backend](../log_backend_reference/P004_日志后端结构.md)、[log_backend_adsp_mtrace_get](P004_Intel_ADSP_mtrace日志后端接口.md#gaecd49115065234a120c75f450b799269)。

取得Intel ADSP mtrace日志后端。

## 5.3\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_adsp_mtrace.h](../../../include/zephyr/logging/log_backend_adsp_mtrace.h)、[subsys/logging/backends/log_backend_adsp_mtrace.c](../../../subsys/logging/backends/log_backend_adsp_mtrace.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下译注独立于官方正文，依据来源记录中的官方头文件与可取得的实现；本地链接均为相对路径。

> 译注——源码核对：mtrace把日志写入SRAM缓冲区，再由钩子通知主机；它与HDA的DMA流接口不同，初始化参数和回调声明应分别使用。

> 译注——源码核对：本次实现的adsp_mtrace_log_init初始化mtrace状态、保存钩子，并根据钩子是否非NULL设置mtrace_active。向get接口取得后端指针本身不会安装回调或替主机读取数据。

> 译注——源码核对：当前输出路径把本次写入量与剩余空间传给钩子；panic模式会将传给钩子的space_left改为0以促使尽快处理，因此此时该参数不能直接作为实际剩余容量测量值。缓冲与通知并不保证主机已完成日志持久保存。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码](P006_Intel_ADSP_mtrace日志后端头文件源码.md)
- [adsp_mtrace_log_hook_t](P004_Intel_ADSP_mtrace日志后端接口.md#gab6362dba4defcd461d24a155763b465d)
- [adsp_mtrace_log_init](P004_Intel_ADSP_mtrace日志后端接口.md#ga9bb9152344270b8257182471443caa78)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [log_backend_adsp_mtrace_get](P004_Intel_ADSP_mtrace日志后端接口.md#gaecd49115065234a120c75f450b799269)

<a id="header-details"></a>

---

[上一章](P004_Intel_ADSP_mtrace日志后端接口.md) · [返回大纲](大纲.md) · [下一章](P006_Intel_ADSP_mtrace日志后端头文件源码.md)
