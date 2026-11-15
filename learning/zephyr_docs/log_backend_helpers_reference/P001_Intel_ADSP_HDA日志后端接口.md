---
id: learning.zephyr-docs.log-backend-helpers-reference.page-1
title: Intel_ADSP_HDA日志后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__adsp__hda.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Intel\_ADSP\_HDA日志后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__log__backend__adsp__hda.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Intel ADSP日志后端、标准辅助接口与多域辅助接口。源码跟踪译注与官方原文分开标示。

通过Intel ADSP HDA DMA通道传输日志流的后端。

<a id="details"></a>

通过Intel ADSP HDA DMA通道传输日志流的后端。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_log_5Fbackend_5Fadsp_5Fhda_2Eh"></a>

```c
file log_backend_adsp_hda.h
```

相关声明：[log_backend_adsp_hda.h](P002_Intel_ADSP_HDA日志后端头文件参考.md)。

Intel ADSP HDA日志后端的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_ga8d50e67fece0cf916b72fcaa7c2bd11a"></a>

```c
typedef void(* adsp_hda_log_hook_t) (uint32_t written)
```

相关声明：[adsp_hda_log_hook_t](#ga8d50e67fece0cf916b72fcaa7c2bd11a)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

HDA日志记录器需要一个用于进程间通信（IPC）消息的钩子（Hook）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gac9ae5b9b36f95d30643c0acf95d51e82"></a>

```c
void adsp_hda_log_init (adsp_hda_log_hook_t hook, uint32_t channel)
```

相关声明：[adsp_hda_log_init](#gac9ae5b9b36f95d30643c0acf95d51e82)、[adsp_hda_log_hook_t](#ga8d50e67fece0cf916b72fcaa7c2bd11a)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

初始化Intel ADSP HDA日志记录器。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga8d50e67fece0cf916b72fcaa7c2bd11a"></a>

### `adsp_hda_log_hook_t`

```c
typedef void(* adsp_hda_log_hook_t) (uint32_t written)
```

```c
#include <zephyr/logging/log_backend_adsp_hda.h>
```

HDA日志记录器需要一个用于进程间通信（IPC）消息的钩子（Hook）。

日志被刷新并通过DMA写入后，应发送一条IPC消息通知主机；此钩子函数指针用于实现该通知。

<a id="gac9ae5b9b36f95d30643c0acf95d51e82"></a>

### `adsp_hda_log_init()`

```c
void adsp_hda_log_init ( adsp_hda_log_hook_t hook, uint32_t channel )
```

```c
#include <zephyr/logging/log_backend_adsp_hda.h>
```

初始化Intel ADSP HDA日志记录器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hook` | 每次HDA刷新（Flush）后调用此函数，以通知主机有关DMA日志数据的信息。此钩子可能由多个CPU和多个调用上下文并发调用；如需串行化，由钩子的实现者负责。保证每次刷新调用一次。 |
| `channel` | 用于日志的HDA流，即DMA通道（DMA Channel）。 |

## 1.5\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_adsp_hda.h](../../../include/zephyr/logging/log_backend_adsp_hda.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下译注独立于官方正文，依据来源记录中的官方头文件与可取得的实现；本地链接均为相对路径。

> 译注——源码核对：HDA接口使用指定的DMA通道（DMA Channel），钩子用于通知主机可读取日志；声明中的channel不是一般意义上的Zephyr线程或日志域编号。

> 译注——源码核对：原文明确保证每次刷新调用一次钩子，但允许多个CPU和调用上下文并发执行。需要共享计数或发送IPC消息时，串行化由钩子实现者负责，不能假定日志核心已经替它加锁。

> 译注——源码核对：本次已核对官方头文件声明；当前官方路径未取得对应HDA后端实现，因此不补造通道配置、DMA完成时序或written参数的额外语义。此项限制不影响对这三份官方页面本身的完整翻译。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [log_backend_adsp_hda.h](P002_Intel_ADSP_HDA日志后端头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Intel_ADSP_HDA日志后端头文件参考.md)
