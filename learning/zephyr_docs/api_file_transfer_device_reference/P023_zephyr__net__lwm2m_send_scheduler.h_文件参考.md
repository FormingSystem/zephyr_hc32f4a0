---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-23
title: zephyr__net__lwm2m_send_scheduler.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_net\_\_lwm2m\_send\_scheduler.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
#include <zephyr/net/lwm2m.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_ae71df037474bca27032fd7d395f84f04"></a>

```c
int lwm2m_send_sched_init (void)
```

相关声明：[lwm2m_send_sched_init](#ae71df037474bca27032fd7d395f84f04)。

注册发送调度器（Send Scheduler）的 LwM2M 对象（Objects），并初始化状态。

<a id="r_acc3495441c7fb3391211a360d0602431"></a>

```c
bool lwm2m_send_sched_cache_filter (const struct lwm2m_obj_path *path, const struct lwm2m_time_series_elem *element)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lwm2m_send_sched_cache_filter](#acc3495441c7fb3391211a360d0602431)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

执行已配置调度器规则（Scheduler Rules）的缓存过滤器（Cache Filter）。

<a id="r_a896f3773c77143e90858bdeab8ba326a"></a>

```c
void lwm2m_send_sched_handle_registration_event (void)
```

相关声明：[lwm2m_send_sched_handle_registration_event](#a896f3773c77143e90858bdeab8ba326a)。

处理注册或注册更新完成事件（Registration or Registration-update Completion Event）。

## 23.2\_详细说明（Detailed Documentation）

<a id="acc3495441c7fb3391211a360d0602431"></a>

### `lwm2m_send_sched_cache_filter()`

```c
bool lwm2m_send_sched_cache_filter ( const struct lwm2m_obj_path * path, const struct lwm2m_time_series_elem * element )
```

执行已配置调度器规则（Scheduler Rules）的缓存过滤器（Cache Filter）。

对希望由调度器（Scheduler）控制的每个缓存资源（Cached Resource），通过 `lwm2m_set_cache_filter` 接入此过滤器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 缓存资源（Cached Resource）的 LwM2M 路径。 |
| `element` | 即将加入缓存的候选样本（Candidate Sample）。 |

**返回（Returns）**：**返回值（Returns）：**`true` 表示将样本保留在缓存（Cache）中，`false` 表示丢弃或推迟该样本。

<a id="a896f3773c77143e90858bdeab8ba326a"></a>

### `lwm2m_send_sched_handle_registration_event()`

```c
void lwm2m_send_sched_handle_registration_event ( void )
```

处理注册或注册更新完成事件（Registration or Registration-update Completion Event）。

应用应在其 LwM2M RD 客户端报告注册或注册更新成功时调用此接口，使发送调度器（Send Scheduler）能够执行更新时刷新策略（Flush-on-update Policy）。

<a id="ae71df037474bca27032fd7d395f84f04"></a>

### `lwm2m_send_sched_init()`

```c
int lwm2m_send_sched_init ( void )
```

注册发送调度器（Send Scheduler）的 LwM2M 对象（Objects），并初始化状态。

安装调度器控制（Scheduler Control，10523）和采样规则（Sampling Rules，10524）对象，并准备缓存过滤器辅助接口（Cache Filter Helpers）所需的状态记录。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`；对象注册（Object Registration）失败时返回负 `errno`。


## 23.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net/lwm2m.h](../api_source_runtime_reference/P040_lwm2m.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P468_lwm2m_send_scheduler.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)
- [lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)
- [lwm2m_set_cache_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_zephyr__dt-bindings__lvgl__lvgl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__drivers__sensor__paj7620.h_文件参考.md)
