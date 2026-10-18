---
id: learning.zephyr-docs.modem-wireless-model-reference.page-22
title: hl78xx_evt_monitor_entry_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__evt__monitor__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_hl78xx\_evt\_monitor\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__evt__monitor__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

事件监测器（Event Monitor）的条目结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

事件监视器条目（Event monitor entry）结构体。表示已注册的事件监视器，包含回调和状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_ae1af8f99fe962deaf80f13f3d61552e3"></a>

```c
const hl78xx_evt_monitor_handler_t handler
```

相关声明：[hl78xx_evt_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa1346c7b8b44abae64f59cc8d5fa9c01)、[handler](#ae1af8f99fe962deaf80f13f3d61552e3)。

监视器回调函数。

<a id="r_aa17d06c0c99da863e3eabecc43c89b7b"></a>

```c
hl78xx_evt_monitor_release_t release
```

相关声明：[hl78xx_evt_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga774bbdee241bfb63374fdc74d2353a3d)、[release](#aa17d06c0c99da863e3eabecc43c89b7b)。

可选回调，在最后一个运行时引用被释放时调用。

<a id="r_aad60b03dc6f1a53b0eaebd4c2e90bf77"></a>

```c
struct hl78xx_evt_monitor_entry * next
```

相关声明：[hl78xx_evt_monitor_entry](P022_hl78xx_evt_monitor_entry_结构体.md)、[next](#aad60b03dc6f1a53b0eaebd4c2e90bf77)。

运行时列表的链接节点。

<a id="r_a3c4abc63ba2c55c2e5e718a4873187bb"></a>

```c
atomic_t refcnt
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[refcnt](#a3c4abc63ba2c55c2e5e718a4873187bb)。

用于列表成员关系和正在处理的分派快照（dispatch snapshots）的引用计数。

<a id="r_ab53ac16078049c955f04edd1f26a6b7f"></a>

```c
struct k_work release_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[release_work](#ab53ac16078049c955f04edd1f26a6b7f)。

用于推迟执行释放回调的工作项。

```c
struct {
```

<a id="r_a0b400a38986cc38524b7ac81fa0935c1"></a>

```c
uint8_t paused: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[paused](#aac567b983a9bde01f6d34f6376c1c3c5)。

监视器已暂停。

<a id="r_a5ec0cbd3dde167a1cd87551709c66f2b"></a>

```c
uint8_t direct: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direct](#a4dbe58f2974287076a4629d9ca1ebe77)。

在中断服务例程（ISR）上下文中分派。

<a id="r_acb7a79b0dca67c9a719494c97ab3e710"></a>

```c
} flags
```

相关声明：[flags](#acb7a79b0dca67c9a719494c97ab3e710)。

监视器标志。

## 22.2\_详细说明（Detailed Documentation）

<a id="a4dbe58f2974287076a4629d9ca1ebe77"></a>

### `direct`

```c
uint8_t hl78xx_evt_monitor_entry::direct
```

在中断服务例程（ISR）上下文中分派。

<a id="acb7a79b0dca67c9a719494c97ab3e710"></a>

### `[struct]`

```c
struct { ... } hl78xx_evt_monitor_entry::flags
```

监视器标志。

<a id="ae1af8f99fe962deaf80f13f3d61552e3"></a>

### `handler`

```c
const hl78xx_evt_monitor_handler_t hl78xx_evt_monitor_entry::handler
```

监视器回调函数。

<a id="aad60b03dc6f1a53b0eaebd4c2e90bf77"></a>

### `next`

```c
struct hl78xx_evt_monitor_entry* hl78xx_evt_monitor_entry::next
```

运行时列表的链接节点。

<a id="aac567b983a9bde01f6d34f6376c1c3c5"></a>

### `paused`

```c
uint8_t hl78xx_evt_monitor_entry::paused
```

监视器已暂停。

<a id="a3c4abc63ba2c55c2e5e718a4873187bb"></a>

### `refcnt`

```c
atomic_t hl78xx_evt_monitor_entry::refcnt
```

用于列表成员关系和正在处理的分派快照（dispatch snapshots）的引用计数。

<a id="aa17d06c0c99da863e3eabecc43c89b7b"></a>

### `release`

```c
hl78xx_evt_monitor_release_t hl78xx_evt_monitor_entry::release
```

可选回调，在最后一个运行时引用被释放时调用。

<a id="ab53ac16078049c955f04edd1f26a6b7f"></a>

### `release_work`

```c
struct k_work hl78xx_evt_monitor_entry::release_work
```

用于推迟执行释放回调的工作项。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_evt_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa1346c7b8b44abae64f59cc8d5fa9c01)
- [hl78xx_evt_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga774bbdee241bfb63374fdc74d2353a3d)
- [hl78xx_evt_monitor_entry](P022_hl78xx_evt_monitor_entry_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_hl78xx_evt_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_hl78xx_gnss_aux_data_callback_结构体.md)
