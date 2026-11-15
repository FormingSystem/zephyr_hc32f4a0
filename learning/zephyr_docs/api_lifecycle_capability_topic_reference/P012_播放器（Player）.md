---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-12
title: 播放器（Player）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_播放器（Player）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

位于管线之上的高层可复用控制层。

<a id="details"></a>

流水线（Pipeline）之上的高层可复用控制层。播放器（Player）是一个轻量辅助组件，负责流水线运行时生命周期（Run-time Lifecycle）：播放、暂停、停止、重播和退出（Play、Pause、Stop、Replay、Quit）。所有状态转换均在专用工作线程（Worker Thread）中串行执行，以保证调用者（例如交互式控制台循环）不会因流水线拆除（Teardown）而阻塞；来自流水线线程的流结束／错误通知（End-of-stream/Error Notifications）也不会在同一线程上下文中触发状态变化，避免尝试等待当前正在运行自身的线程结束（Join）。调用者通过 `mpipe_player_*()` API 将命令入队，工作线程逐条执行。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_mpipe_5Fplayer_2Eh"></a>

```c
file mpipe_player.h
```

相关声明：[mpipe_player.h](../api_file_network_device_reference/P025_zephyr__mpipe__utils__mpipe_player.h_文件参考.md)。

流水线（Pipeline）的类媒体播放器控制层。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fplayer"></a>

```c
struct mpipe_player
```

相关声明：[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

播放器实例（Player Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_ga180394243652a94c476f1cb83c2c14f7"></a>

```c
int mpipe_player_init (struct mpipe_player *player, struct mpipe *pipeline)
```

相关声明：[mpipe_player_init](#ga180394243652a94c476f1cb83c2c14f7)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)、[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)。

初始化播放器（Player）并启动其工作线程（Worker Thread）。

<a id="r_ga63c7cf14daf0190a8d22dc1f7d4fca5b"></a>

```c
int mpipe_player_play (struct mpipe_player *player)
```

相关声明：[mpipe_player_play](#ga63c7cf14daf0190a8d22dc1f7d4fca5b)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入播放状态（PLAYING）。

<a id="r_gaabb613b55eefc3cdb97e145e7d3a3c4f"></a>

```c
int mpipe_player_pause (struct mpipe_player *player)
```

相关声明：[mpipe_player_pause](#gaabb613b55eefc3cdb97e145e7d3a3c4f)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入暂停状态（PAUSED）。

<a id="r_gab5482257b941d59d57c494ff56db48e7"></a>

```c
int mpipe_player_toggle (struct mpipe_player *player)
```

相关声明：[mpipe_player_toggle](#gab5482257b941d59d57c494ff56db48e7)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

在播放（PLAYING）与暂停（PAUSED）状态之间切换。

<a id="r_ga91e6fc41ff14ef49975abf8456ffb46c"></a>

```c
int mpipe_player_stop (struct mpipe_player *player)
```

相关声明：[mpipe_player_stop](#ga91e6fc41ff14ef49975abf8456ffb46c)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入就绪状态（READY）。

<a id="r_ga1a60c7e2006f7a44dc063f6366f9b35d"></a>

```c
int mpipe_player_replay (struct mpipe_player *player)
```

相关声明：[mpipe_player_replay](#ga1a60c7e2006f7a44dc063f6366f9b35d)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

从头重新开始播放（Playback）。

<a id="r_gaf565c1500aa1ce5136fafb743e042a7e"></a>

```c
int mpipe_player_quit (struct mpipe_player *player)
```

相关声明：[mpipe_player_quit](#gaf565c1500aa1ce5136fafb743e042a7e)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求工作线程停止流水线（Pipeline）并退出。

<a id="r_ga5ff5de85569a7cc388be28fbf1dddb62"></a>

```c
int mpipe_player_wait_quit (struct mpipe_player *player)
```

相关声明：[mpipe_player_wait_quit](#ga5ff5de85569a7cc388be28fbf1dddb62)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

阻塞等待播放器工作线程（Player Worker）退出。

<a id="r_ga561e172ea9426f73203c600b912993d9"></a>

```c
int mpipe_player_deinit (struct mpipe_player *player)
```

相关声明：[mpipe_player_deinit](#ga561e172ea9426f73203c600b912993d9)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

等待工作线程退出，并释放播放器资源（Player Resources）。

## 12.4\_详细说明（Detailed Documentation）

<a id="ga561e172ea9426f73203c600b912993d9"></a>

### `mpipe_player_deinit()`

```c
int mpipe_player_deinit ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

等待工作线程退出，并释放播放器资源（Player Resources）。

若尚未请求工作线程（Worker）退出，则先发出退出请求。本调用之后，播放器（Player）必须重新初始化才能再次使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="ga180394243652a94c476f1cb83c2c14f7"></a>

### `mpipe_player_init()`

```c
int mpipe_player_init ( struct mpipe_player * player, struct mpipe * pipeline )
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

初始化播放器（Player）并启动其工作线程（Worker Thread）。

注册总线监听器（Bus Listener），在流结束或发生错误时自动停止流水线（Pipeline）。流水线必须已构建并连接，但应处于 `READY` 状态，尚未播放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 指向尚未初始化的播放器（Player）的指针。 |
| `pipeline` | 指向要控制的流水线（Pipeline）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EBUSY` | 已有另一个播放器实例（Player Instance）处于活动状态。 |
| `-EIO` | 无法附加总线观察者（Bus Observer）。 |

**说明（Note）**：**注意（Note）：**同一时刻只能有一个活动播放器实例（Player Instance）。

<a id="gaabb613b55eefc3cdb97e145e7d3a3c4f"></a>

### `mpipe_player_pause()`

```c
int mpipe_player_pause ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

请求进入暂停状态（PAUSED）。

暂停流传输（Streaming），保留已排队的数据。仅在 `PLAYING` 状态下有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga63c7cf14daf0190a8d22dc1f7d4fca5b"></a>

### `mpipe_player_play()`

```c
int mpipe_player_play ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

请求进入播放状态（PLAYING）。

在 `READY` 状态下启动流水线；在 `PAUSED` 状态下恢复且不丢失数据；已经处于 `PLAYING` 状态时无效果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaf565c1500aa1ce5136fafb743e042a7e"></a>

### `mpipe_player_quit()`

```c
int mpipe_player_quit ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

请求工作线程停止流水线（Pipeline）并退出。

立即返回。使用 `mpipe_player_deinit` 等待工作线程（Worker）结束并释放其资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga1a60c7e2006f7a44dc063f6366f9b35d"></a>

### `mpipe_player_replay()`

```c
int mpipe_player_replay ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

从头重新开始播放（Playback）。

等价于先停止（Stop）再播放（Play）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga91e6fc41ff14ef49975abf8456ffb46c"></a>

### `mpipe_player_stop()`

```c
int mpipe_player_stop ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

请求进入就绪状态（READY）。

清空已排队的数据，并等待全部流处理线程结束（Join All Streaming Threads）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gab5482257b941d59d57c494ff56db48e7"></a>

### `mpipe_player_toggle()`

```c
int mpipe_player_toggle ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

在播放（PLAYING）与暂停（PAUSED）状态之间切换。

若处于 `PLAYING` 则暂停；否则播放，即从 `PAUSED` 恢复或从 `READY` 启动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga5ff5de85569a7cc388be28fbf1dddb62"></a>

### `mpipe_player_wait_quit()`

```c
int mpipe_player_wait_quit ( struct mpipe_player * player)
```

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

阻塞等待播放器工作线程（Player Worker）退出。

流水线已停止且工作线程即将退出时返回，即在已请求退出之后返回；通常通过 `q`／`player quit` shell 命令或 `mpipe_player_quit` 请求退出。这使应用主线程可以等待用户操作结束，同时由 shell 驱动播放器（Player）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 已通过 `mpipe_player_init` 初始化的播放器（Player）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

**说明（Note）**：**注意（Note）：**此接口只负责等待；之后还需调用 `mpipe_player_deinit` 等待工作线程真正结束（Join）并释放播放器资源。


## 12.5\_原页交叉引用（Cross References）

- [mpipe_player.h](../api_file_network_device_reference/P025_zephyr__mpipe__utils__mpipe_player.h_文件参考.md)
- [mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [播放器（Player）](P012_播放器（Player）.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_蜂窝调制解调器驱动定义宏（Driver definition macros）.md) · [返回大纲](大纲.md) · [下一章](P013_变换元素（Transforms）.md)
