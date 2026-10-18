---
id: learning.zephyr-docs.api-file-network-device-reference.page-25
title: zephyr__mpipe__utils__mpipe_player.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_mpipe\_\_utils\_\_mpipe\_player.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流水线（Pipeline）的类媒体播放器控制层。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/zbus/zbus.h>
#include <zephyr/mpipe/mpipe_message.h>
#include <zephyr/mpipe/mpipe_pipeline.h>
```

查看此文件的源码。

流水线（Pipeline）的类媒体播放器控制层。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fplayer"></a>

```c
struct mpipe_player
```

相关声明：[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

播放器实例（Player Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_ga180394243652a94c476f1cb83c2c14f7"></a>

```c
int mpipe_player_init (struct mpipe_player *player, struct mpipe *pipeline)
```

相关声明：[mpipe_player_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga180394243652a94c476f1cb83c2c14f7)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)、[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)。

初始化播放器（Player）并启动其工作线程（Worker Thread）。

<a id="r_ga63c7cf14daf0190a8d22dc1f7d4fca5b"></a>

```c
int mpipe_player_play (struct mpipe_player *player)
```

相关声明：[mpipe_player_play](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga63c7cf14daf0190a8d22dc1f7d4fca5b)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入播放状态（PLAYING）。

<a id="r_gaabb613b55eefc3cdb97e145e7d3a3c4f"></a>

```c
int mpipe_player_pause (struct mpipe_player *player)
```

相关声明：[mpipe_player_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaabb613b55eefc3cdb97e145e7d3a3c4f)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入暂停状态（PAUSED）。

<a id="r_gab5482257b941d59d57c494ff56db48e7"></a>

```c
int mpipe_player_toggle (struct mpipe_player *player)
```

相关声明：[mpipe_player_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gab5482257b941d59d57c494ff56db48e7)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

在播放（PLAYING）与暂停（PAUSED）状态之间切换。

<a id="r_ga91e6fc41ff14ef49975abf8456ffb46c"></a>

```c
int mpipe_player_stop (struct mpipe_player *player)
```

相关声明：[mpipe_player_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga91e6fc41ff14ef49975abf8456ffb46c)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求进入就绪状态（READY）。

<a id="r_ga1a60c7e2006f7a44dc063f6366f9b35d"></a>

```c
int mpipe_player_replay (struct mpipe_player *player)
```

相关声明：[mpipe_player_replay](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga1a60c7e2006f7a44dc063f6366f9b35d)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

从头重新开始播放（Playback）。

<a id="r_gaf565c1500aa1ce5136fafb743e042a7e"></a>

```c
int mpipe_player_quit (struct mpipe_player *player)
```

相关声明：[mpipe_player_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaf565c1500aa1ce5136fafb743e042a7e)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

请求工作线程停止流水线（Pipeline）并退出。

<a id="r_ga5ff5de85569a7cc388be28fbf1dddb62"></a>

```c
int mpipe_player_wait_quit (struct mpipe_player *player)
```

相关声明：[mpipe_player_wait_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga5ff5de85569a7cc388be28fbf1dddb62)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

阻塞等待播放器工作线程（Player Worker）退出。

<a id="r_ga561e172ea9426f73203c600b912993d9"></a>

```c
int mpipe_player_deinit (struct mpipe_player *player)
```

相关声明：[mpipe_player_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga561e172ea9426f73203c600b912993d9)、[mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)。

等待工作线程退出，并释放播放器资源（Player Resources）。


## 25.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/zbus/zbus.h](../intercore_reference/P212_zbus核心完整头文件.md)
- [zephyr/mpipe/mpipe_message.h](../api_source_reference/P552_mpipe_message.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pipeline.h](../api_source_reference/P556_mpipe_pipeline.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P117_mpipe_player.h_源码浏览.md)
- [mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)
- [mpipe_player_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga180394243652a94c476f1cb83c2c14f7)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [mpipe_player_play](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga63c7cf14daf0190a8d22dc1f7d4fca5b)
- [mpipe_player_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaabb613b55eefc3cdb97e145e7d3a3c4f)
- [mpipe_player_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gab5482257b941d59d57c494ff56db48e7)
- [mpipe_player_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga91e6fc41ff14ef49975abf8456ffb46c)
- [mpipe_player_replay](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga1a60c7e2006f7a44dc063f6366f9b35d)
- [mpipe_player_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaf565c1500aa1ce5136fafb743e042a7e)
- [mpipe_player_wait_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga5ff5de85569a7cc388be28fbf1dddb62)
- [mpipe_player_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga561e172ea9426f73203c600b912993d9)

<a id="header-details"></a>

---

[上一章](P024_zephyr__drivers__modem__modem_cellular.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考.md)
