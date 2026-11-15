---
id: learning.zephyr-docs.modem-wireless-model-reference.page-17
title: hl78xx_at_monitor_entry_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__at__monitor__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_hl78xx\_at\_monitor\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__at__monitor__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AT监测器（AT Monitor）的条目结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

AT 监视器条目（AT monitor entry）结构体。表示已注册的、处理解析后非请求 AT 通知的监视器，包含回调、过滤器和状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a0ce16aebf50d69f6dbece9f34b1afe1c"></a>

```c
const char * filter
```

相关声明：[filter](#a0ce16aebf50d69f6dbece9f34b1afe1c)。

要监视的非请求 AT 通知的精确匹配模式；为 `NULL` 时监视所有通知。

<a id="r_a7d8c73e1cb6c9ddde19aa05c75e941c8"></a>

```c
const hl78xx_at_monitor_handler_t handler
```

相关声明：[hl78xx_at_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98fde2c3465abce3b4b7d94816bc029c)、[handler](#a7d8c73e1cb6c9ddde19aa05c75e941c8)。

监视器回调函数。

<a id="r_af7417e320aa5dabb1283d5593f4166fd"></a>

```c
hl78xx_at_monitor_release_t release
```

相关声明：[hl78xx_at_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga517a58c85701991214ddb3a9d786f367)、[release](#af7417e320aa5dabb1283d5593f4166fd)。

可选回调，在最后一个运行时引用被释放时调用。

<a id="r_a0dbf62a2521370ab77e9edb1ea3f728a"></a>

```c
struct hl78xx_at_monitor_entry * next
```

相关声明：[hl78xx_at_monitor_entry](P017_hl78xx_at_monitor_entry_结构体.md)、[next](#a0dbf62a2521370ab77e9edb1ea3f728a)。

运行时列表的链接节点。

<a id="r_ad6d1767212a7cf7f69b113e55b56b99f"></a>

```c
atomic_t refcnt
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[refcnt](#ad6d1767212a7cf7f69b113e55b56b99f)。

用于列表成员关系和正在处理的分派快照（dispatch snapshots）的引用计数。

<a id="r_a378b71d4ebac3e4de62dcae118abe218"></a>

```c
struct k_work release_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[release_work](#a378b71d4ebac3e4de62dcae118abe218)。

用于将释放操作推迟到注销或分派上下文之外执行的工作项（work item）。

```c
struct {
```

<a id="r_a58b925eb93efdfe7caca1ada192daf8b"></a>

```c
uint8_t paused: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[paused](#a718aac1e812cf9466bb263cc3369533e)。

监视器已暂停。

<a id="r_a79d4b2c7258147579fe3cc0517bfc908"></a>

```c
uint8_t direct: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direct](#af5f4bcca2ba5a4e9670694182ed8f6eb)。

直接在 HL78xx 调制解调器接收（RX）工作队列上下文中分派。

<a id="r_aa8e084c925d5b57524c722f74f1b629c"></a>

```c
} flags
```

相关声明：[flags](#aa8e084c925d5b57524c722f74f1b629c)。

监视器标志。

## 17.2\_详细说明（Detailed Documentation）

<a id="af5f4bcca2ba5a4e9670694182ed8f6eb"></a>

### `direct`

```c
uint8_t hl78xx_at_monitor_entry::direct
```

直接在 HL78xx 调制解调器接收（RX）工作队列上下文中分派。

<a id="a0ce16aebf50d69f6dbece9f34b1afe1c"></a>

### `filter`

```c
const char* hl78xx_at_monitor_entry::filter
```

要监视的非请求 AT 通知的精确匹配模式；为 `NULL` 时监视所有通知。

<a id="aa8e084c925d5b57524c722f74f1b629c"></a>

### `[struct]`

```c
struct { ... } hl78xx_at_monitor_entry::flags
```

监视器标志。

<a id="a7d8c73e1cb6c9ddde19aa05c75e941c8"></a>

### `handler`

```c
const hl78xx_at_monitor_handler_t hl78xx_at_monitor_entry::handler
```

监视器回调函数。

<a id="a0dbf62a2521370ab77e9edb1ea3f728a"></a>

### `next`

```c
struct hl78xx_at_monitor_entry* hl78xx_at_monitor_entry::next
```

运行时列表的链接节点。

<a id="a718aac1e812cf9466bb263cc3369533e"></a>

### `paused`

```c
uint8_t hl78xx_at_monitor_entry::paused
```

监视器已暂停。

<a id="ad6d1767212a7cf7f69b113e55b56b99f"></a>

### `refcnt`

```c
atomic_t hl78xx_at_monitor_entry::refcnt
```

用于列表成员关系和正在处理的分派快照（dispatch snapshots）的引用计数。

<a id="af7417e320aa5dabb1283d5593f4166fd"></a>

### `release`

```c
hl78xx_at_monitor_release_t hl78xx_at_monitor_entry::release
```

可选回调，在最后一个运行时引用被释放时调用。

<a id="a378b71d4ebac3e4de62dcae118abe218"></a>

### `release_work`

```c
struct k_work hl78xx_at_monitor_entry::release_work
```

用于将释放操作推迟到注销或分派上下文之外执行的工作项（work item）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_at_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98fde2c3465abce3b4b7d94816bc029c)
- [hl78xx_at_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga517a58c85701991214ddb3a9d786f367)
- [hl78xx_at_monitor_entry](P017_hl78xx_at_monitor_entry_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_hl78xx_agnss_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_hl78xx_at_notification_结构体.md)
