---
id: learning.zephyr-docs.portability.page-12
title: POSIX符合性
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/services/portability/posix/conformance/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_POSIX符合性

原文：[官方页面](https://docs.zephyrproject.org/latest/services/portability/posix/conformance/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_POSIX 符合性（POSIX Conformance）

本节依据 [IEEE 1003.1-2017](https://standards.ieee.org/ieee/1003.1/7101/)，详细说明 Zephyr 的 POSIX 符合性。

译注：以下保留原表的符号、数值、空白和 † 标记。支持值不是布尔值，也不是运行时测量结果；原页列出某个配置或函数，不等于该特性在每个构建中都已启用或具备完整语义。† 的原文定义见本章末尾。

## 12.2\_POSIX 系统接口（POSIX System Interfaces）

### 12.2.1\_系统接口基础值

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| _POSIX_CHOWN_RESTRICTED | 0 |  |
| _POSIX_NO_TRUNC | 0 |  |
| _POSIX_VDISABLE | `'\0'` |  |

### 12.2.2\_系统接口选项

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| _POSIX_VERSION | 200809L |  |
| [_POSIX_ASYNCHRONOUS_IO](P015_POSIX选项与选项组.md#posix-option-asynchronous-io) | 200809L | [`CONFIG_POSIX_ASYNCHRONOUS_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_ASYNCHRONOUS_IO)[†](#posix-undefined-behaviour) |
| [_POSIX_BARRIERS](P015_POSIX选项与选项组.md#posix-option-group-barriers) | 200809L | [`CONFIG_POSIX_BARRIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_BARRIERS) |
| [_POSIX_CLOCK_SELECTION](P015_POSIX选项与选项组.md#posix-option-group-clock-selection) | 200809L | [`CONFIG_POSIX_CLOCK_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CLOCK_SELECTION) |
| [_POSIX_MAPPED_FILES](P015_POSIX选项与选项组.md#posix-option-group-mapped-files) | 200809L | [`CONFIG_POSIX_MAPPED_FILES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MAPPED_FILES) |
| [_POSIX_MEMORY_PROTECTION](P015_POSIX选项与选项组.md#posix-option-group-memory-protection) | 200809L | [`CONFIG_POSIX_MEMORY_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMORY_PROTECTION) [†](#posix-undefined-behaviour) |
| [_POSIX_READER_WRITER_LOCKS](P015_POSIX选项与选项组.md#posix-option-group-rw-locks) | 200809L | [`CONFIG_POSIX_RW_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RW_LOCKS) |
| [_POSIX_REALTIME_SIGNALS](P015_POSIX选项与选项组.md#posix-option-group-realtime-signals) | -1 | [`CONFIG_POSIX_REALTIME_SIGNALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_REALTIME_SIGNALS) |
| [_POSIX_SEMAPHORES](P015_POSIX选项与选项组.md#posix-option-group-semaphores) | 200809L | [`CONFIG_POSIX_SEMAPHORES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEMAPHORES) |
| [_POSIX_SPIN_LOCKS](P015_POSIX选项与选项组.md#posix-option-group-spin-locks) | 200809L | [`CONFIG_POSIX_SPIN_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SPIN_LOCKS) |
| [_POSIX_THREAD_SAFE_FUNCTIONS](P015_POSIX选项与选项组.md#posix-option-thread-safe-functions) | -1 | [`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS) |
| [_POSIX_THREADS](P015_POSIX选项与选项组.md#posix-option-group-threads-base) | -1 | [`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS) |
| [_POSIX_TIMEOUTS](P015_POSIX选项与选项组.md#posix-option-timeouts) | 200809L | [`CONFIG_POSIX_TIMEOUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMEOUTS) |
| [_POSIX_TIMERS](P015_POSIX选项与选项组.md#posix-option-group-timers) | 200809L | [`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS) |
| _POSIX2_C_BIND | 200809L |  |

### 12.2.3\_不支持的系统接口（Unsupported）

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| _POSIX_JOB_CONTROL | -1 | [†](#posix-undefined-behaviour) |
| _POSIX_REGEXP | -1 | [†](#posix-undefined-behaviour) |
| _POSIX_SAVED_IDS | -1 | [†](#posix-undefined-behaviour) |
| _POSIX_SHELL | -1 | [†](#posix-undefined-behaviour) |

### 12.2.4\_可选系统接口（Optional）

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| _POSIX_ADVISORY_INFO | -1 |  |
| [_POSIX_CPUTIME](P015_POSIX选项与选项组.md#posix-option-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CPUTIME) |
| [_POSIX_FSYNC](P015_POSIX选项与选项组.md#posix-option-fsync) | 200809L | [`CONFIG_POSIX_FSYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FSYNC) |
| [_POSIX_IPV6](P015_POSIX选项与选项组.md#posix-option-ipv6) | 200809L | [`CONFIG_POSIX_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_IPV6) |
| [_POSIX_MEMLOCK](P015_POSIX选项与选项组.md#posix-option-memlock) | 200809L | [`CONFIG_POSIX_MEMLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMLOCK) [†](#posix-undefined-behaviour) |
| [_POSIX_MEMLOCK_RANGE](P015_POSIX选项与选项组.md#posix-option-memlock-range) | 200809L | [`CONFIG_POSIX_MEMLOCK_RANGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMLOCK_RANGE) |
| [_POSIX_MESSAGE_PASSING](P015_POSIX选项与选项组.md#posix-option-message-passing) | 200809L | [`CONFIG_POSIX_MESSAGE_PASSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MESSAGE_PASSING) |
| [_POSIX_MONOTONIC_CLOCK](P015_POSIX选项与选项组.md#posix-option-monotonic-clock) | 200809L | [`CONFIG_POSIX_MONOTONIC_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MONOTONIC_CLOCK) |
| _POSIX_PRIORITIZED_IO | -1 |  |
| [_POSIX_PRIORITY_SCHEDULING](P015_POSIX选项与选项组.md#posix-option-priority-scheduling) | 200809L | [`CONFIG_POSIX_PRIORITY_SCHEDULING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_PRIORITY_SCHEDULING) |
| [_POSIX_RAW_SOCKETS](P015_POSIX选项与选项组.md#posix-option-raw-sockets) | 200809L | [`CONFIG_POSIX_RAW_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RAW_SOCKETS) |
| [_POSIX_SHARED_MEMORY_OBJECTS](P015_POSIX选项与选项组.md#posix-option-shared-memory-objects) | 200809L | [`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SHARED_MEMORY_OBJECTS) |
| _POSIX_SPAWN | -1 | [†](#posix-undefined-behaviour) |
| _POSIX_SPORADIC_SERVER | -1 | [†](#posix-undefined-behaviour) |
| [_POSIX_SYNCHRONIZED_IO](P015_POSIX选项与选项组.md#posix-option-synchronized-io) | 200809L | [`CONFIG_POSIX_SYNCHRONIZED_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYNCHRONIZED_IO) |
| [_POSIX_THREAD_ATTR_STACKADDR](P015_POSIX选项与选项组.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKADDR) |
| [_POSIX_THREAD_ATTR_STACKSIZE](P015_POSIX选项与选项组.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKSIZE) |
| [_POSIX_THREAD_CPUTIME](P015_POSIX选项与选项组.md#posix-option-thread-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CPUTIME) |
| [_POSIX_THREAD_PRIO_INHERIT](P015_POSIX选项与选项组.md#posix-option-thread-prio-inherit) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_INHERIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIO_INHERIT) |
| [_POSIX_THREAD_PRIO_PROTECT](P015_POSIX选项与选项组.md#posix-option-thread-prio-protect) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_PROTECT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIO_PROTECT) |
| [_POSIX_THREAD_PRIORITY_SCHEDULING](P015_POSIX选项与选项组.md#posix-option-thread-priority-scheduling) | 200809L | [`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING) |
| _POSIX_THREAD_PROCESS_SHARED | -1 |  |
| _POSIX_THREAD_SPORADIC_SERVER | -1 |  |
| _POSIX_TRACE | -1 |  |
| _POSIX_TRACE_EVENT_FILTER | -1 |  |
| _POSIX_TRACE_INHERIT | -1 |  |
| _POSIX_TRACE_LOG | -1 |  |
| _POSIX_TYPED_MEMORY_OBJECTS | -1 |  |
| _XOPEN_CRYPT | -1 |  |
| [_XOPEN_REALTIME](P015_POSIX选项与选项组.md#posix-option-group-xsi-realtime) | 700 | [`CONFIG_XSI_REALTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_REALTIME) |
| _XOPEN_REALTIME_THREADS | -1 |  |
| [_XOPEN_STREAMS](P015_POSIX选项与选项组.md#posix-option-xopen-streams) | 200809L | [`CONFIG_XSI_STREAMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_STREAMS) |
| _XOPEN_UNIX | -1 |  |

## 12.3\_POSIX Shell 与实用工具（POSIX Shell and Utilities）

Zephyr 当前不支持 POSIX Shell 或实用工具。

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| _POSIX2_C_DEV | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_CHAR_TERM | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_FORT_DEV | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_FORT_RUN | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_LOCALEDEF | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_PBS | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_PBS_ACCOUNTING | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_PBS_LOCATE | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_PBS_MESSAGE | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_PBS_TRACK | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_SW_DEV | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_UPE | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_UNIX | -1 | [†](#posix-undefined-behaviour) |
| _POSIX2_UUCP | -1 | [†](#posix-undefined-behaviour) |

## 12.4\_XSI 符合性（XSI Conformance）

X/Open 系统接口（X/Open System Interfaces，XSI）的支持情况如下。

| 符号（Symbol） | 支持值（Support） | 备注（Remarks） |
| --- | --- | --- |
| [_POSIX_FSYNC](P015_POSIX选项与选项组.md#posix-option-fsync) | 200809L | [`CONFIG_POSIX_FSYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FSYNC) |
| [_POSIX_THREAD_ATTR_STACKADDR](P015_POSIX选项与选项组.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKADDR) |
| [_POSIX_THREAD_ATTR_STACKSIZE](P015_POSIX选项与选项组.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKSIZE) |
| _POSIX_THREAD_PROCESS_SHARED | -1 |  |

## 12.5\_原文注意事项

某些功能超出 Zephyr 当前设计与能力范围，可能表现出未定义行为（Undefined Behaviour）。例如，多进程（Multi-Processing）、临时按需建立的内存映射（Ad-Hoc Memory-Mapping）、多用户（Multiple Users）或正则表达式（Regular Expressions），在低资源占用的嵌入式系统中并不常见。这类未定义行为用 †（原文称 Obelus）标记，更多细节见[选项与选项组说明](P015_POSIX选项与选项组.md#posix-option-groups)。

各 POSIX 选项或选项组中的功能，也可能全部或部分由符合标准的 C 库实现提供，其中包括但不限于 POSIX 对 ISO C 标准的扩展（[CX](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap01.html)）。


译注核对来源：[include/zephyr/posix/posix_features.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/posix_features.h)、[include/zephyr/posix/unistd.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/unistd.h)。

本仓库的[对应源码](../../../include/zephyr/posix/posix_features.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-conformance"></a>
<a id="id1"></a>
<a id="posix-system-interfaces"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="posix-system-interfaces-required"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="posix-shell-and-utilities"></a>
<a id="id7"></a>
<a id="xsi-conformance"></a>
<a id="x-open-system-interfaces"></a>
<a id="id8"></a>
<a id="posix-undefined-behaviour"></a>
<a id="posix-libc-provided"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：POSIX概述与配置](P011_POSIX概述与配置.md) · [本模块主线目录](../reading/portability.md) · [全部主线](../reading/README.md) · [下一篇：POSIX应用环境规范](P013_POSIX应用环境规范.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P011_POSIX概述与配置.md) · [返回大纲](大纲.md) · [下一章](P013_POSIX应用环境规范.md)

</details>

<!-- reading-navigation:end -->
