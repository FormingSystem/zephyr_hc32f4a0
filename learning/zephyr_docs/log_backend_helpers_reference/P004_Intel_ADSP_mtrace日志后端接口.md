---
id: learning.zephyr-docs.log-backend-helpers-reference.page-4
title: Intel_ADSP_mtrace日志后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__adsp__mtrace.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Intel\_ADSP\_mtrace日志后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__adsp__mtrace.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Intel ADSP日志后端、标准辅助接口与多域辅助接口。源码跟踪译注与官方原文分开标示。

向Intel ADSP mtrace SRAM缓冲区写入日志的后端。

<a id="details"></a>

向Intel ADSP mtrace SRAM缓冲区写入日志的后端。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_log_5Fbackend_5Fadsp_5Fmtrace_2Eh"></a>

```c
file log_backend_adsp_mtrace.h
```

相关声明：[log_backend_adsp_mtrace.h](P005_Intel_ADSP_mtrace日志后端头文件参考.md)。

Intel ADSP mtrace日志后端的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_gab6362dba4defcd461d24a155763b465d"></a>

```c
typedef void(* adsp_mtrace_log_hook_t) (size_t written, size_t space_left)
```

相关声明：[adsp_mtrace_log_hook_t](#gab6362dba4defcd461d24a155763b465d)。

mtrace日志记录器需要一个用于IPC消息的钩子（Hook）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga9bb9152344270b8257182471443caa78"></a>

```c
void adsp_mtrace_log_init (adsp_mtrace_log_hook_t hook)
```

相关声明：[adsp_mtrace_log_init](#ga9bb9152344270b8257182471443caa78)、[adsp_mtrace_log_hook_t](#gab6362dba4defcd461d24a155763b465d)。

初始化Intel ADSP mtrace日志记录器。

<a id="r_gaecd49115065234a120c75f450b799269"></a>

```c
const struct log_backend * log_backend_adsp_mtrace_get (void)
```

相关声明：[log_backend](../log_backend_reference/P004_日志后端结构.md)、[log_backend_adsp_mtrace_get](#gaecd49115065234a120c75f450b799269)。

取得Intel ADSP mtrace日志后端。

## 4.4\_详细说明（Detailed Documentation）

<a id="gab6362dba4defcd461d24a155763b465d"></a>

### `adsp_mtrace_log_hook_t`

```c
typedef void(* adsp_mtrace_log_hook_t) (size_t written, size_t space_left)
```

```c
#include <zephyr/logging/log_backend_adsp_mtrace.h>
```

mtrace日志记录器需要一个用于IPC消息的钩子（Hook）。

向SRAM缓冲区加入新的日志数据后，应发送一条IPC消息通知主机；此钩子函数指针用于实现该通知。

<a id="ga9bb9152344270b8257182471443caa78"></a>

### `adsp_mtrace_log_init()`

```c
void adsp_mtrace_log_init ( adsp_mtrace_log_hook_t hook)
```

```c
#include <zephyr/logging/log_backend_adsp_mtrace.h>
```

初始化Intel ADSP mtrace日志记录器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hook` | 每次写入SRAM缓冲区后调用此函数；如需串行化，由钩子的实现者负责。 |

<a id="gaecd49115065234a120c75f450b799269"></a>

### `log_backend_adsp_mtrace_get()`

```c
const struct log_backend * log_backend_adsp_mtrace_get ( void )
```

```c
#include <zephyr/logging/log_backend_adsp_mtrace.h>
```

取得Intel ADSP mtrace日志后端。

返回（Returns）：指向mtrace日志后端实例的指针。

## 4.5\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_adsp_mtrace.h](../../../include/zephyr/logging/log_backend_adsp_mtrace.h)、[subsys/logging/backends/log_backend_adsp_mtrace.c](../../../subsys/logging/backends/log_backend_adsp_mtrace.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下译注独立于官方正文，依据来源记录中的官方头文件与可取得的实现；本地链接均为相对路径。

> 译注——源码核对：mtrace把日志写入SRAM缓冲区，再由钩子通知主机；它与HDA的DMA流接口不同，初始化参数和回调声明应分别使用。

> 译注——源码核对：本次实现的adsp_mtrace_log_init初始化mtrace状态、保存钩子，并根据钩子是否非NULL设置mtrace_active。向get接口取得后端指针本身不会安装回调或替主机读取数据。

> 译注——源码核对：当前输出路径把本次写入量与剩余空间传给钩子；panic模式会将传给钩子的space_left改为0以促使尽快处理，因此此时该参数不能直接作为实际剩余容量测量值。缓冲与通知并不保证主机已完成日志持久保存。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.6\_原页交叉引用（Cross References）

- [log_backend_adsp_mtrace.h](P005_Intel_ADSP_mtrace日志后端头文件参考.md)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_Intel_ADSP_HDA日志后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_Intel_ADSP_mtrace日志后端头文件参考.md)
