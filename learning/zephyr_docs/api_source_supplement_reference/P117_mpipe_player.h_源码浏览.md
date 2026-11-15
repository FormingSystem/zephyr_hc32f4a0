---
id: learning.zephyr-docs.api-source-supplement-reference.page-117
title: mpipe_player.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_mpipe\_player.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h.html)。

## 117.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__mpipe__player_html_ga180394243652a94c476f1cb83c2c14f7"></a>
<a id="agroup__mpipe__player_html_ga1a60c7e2006f7a44dc063f6366f9b35d"></a>
<a id="agroup__mpipe__player_html_ga561e172ea9426f73203c600b912993d9"></a>
<a id="agroup__mpipe__player_html_ga5ff5de85569a7cc388be28fbf1dddb62"></a>
<a id="agroup__mpipe__player_html_ga63c7cf14daf0190a8d22dc1f7d4fca5b"></a>
<a id="agroup__mpipe__player_html_ga91e6fc41ff14ef49975abf8456ffb46c"></a>
<a id="agroup__mpipe__player_html_gaabb613b55eefc3cdb97e145e7d3a3c4f"></a>
<a id="agroup__mpipe__player_html_gab5482257b941d59d57c494ff56db48e7"></a>
<a id="agroup__mpipe__player_html_gaf565c1500aa1ce5136fafb743e042a7e"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__message_8h_html"></a>
<a id="ampipe__pipeline_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructmpipe__message_html"></a>
<a id="astructmpipe__player_html"></a>
<a id="astructmpipe__player_html_a3b9478c32a290093ed0fc3df63aa08eb"></a>
<a id="astructmpipe__player_html_a5b1f32dff992d10647b415b6e64989ef"></a>
<a id="astructmpipe__player_html_a74be28568a290c8136e88a9b915d023c"></a>
<a id="astructmpipe__player_html_aac812a851a4654c47b93f21e6dfe47ab"></a>
<a id="astructmpipe__player_html_ab059d41757dda23908fc406b1df56e71"></a>
<a id="astructmpipe__player_html_ac316dcfe9b0b276c02c3854186f995d1"></a>
<a id="astructmpipe__player_html_afae2bc92ca0a0fd2a070ad7948cb4bf3"></a>
<a id="astructmpipe_html"></a>
<a id="azbus_8h_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_PLAYER_H_
#define ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_PLAYER_H_


#include <zephyr/kernel.h>

#include <zephyr/zbus/zbus.h>

#include <zephyr/mpipe/mpipe_message.h>
#include <zephyr/mpipe/mpipe_pipeline.h>

/*
 * One entry of the player command queue. run_id names the run the command was
 * posted from, so the worker can tell an end-of-run raised for the run in
 * progress from one describing a run that has already been torn down.
 */
struct mpipe_player_cmd_msg {
        uint8_t cmd;
        uint8_t run_id;
};

struct mpipe_player {
        struct mpipe *pipeline;
        struct k_msgq cmd_q;
        char cmd_buf[CONFIG_MPIPE_PLAYER_CMD_QUEUE_DEPTH * sizeof(struct mpipe_player_cmd_msg)];
        uint8_t run_id;
        struct mpipe_message last_error;
        struct k_thread worker;
        struct k_sem exited;
};

int mpipe_player_init(struct mpipe_player *player, struct mpipe *pipeline);

int mpipe_player_play(struct mpipe_player *player);

int mpipe_player_pause(struct mpipe_player *player);

int mpipe_player_toggle(struct mpipe_player *player);

int mpipe_player_stop(struct mpipe_player *player);

int mpipe_player_replay(struct mpipe_player *player);

int mpipe_player_quit(struct mpipe_player *player);

int mpipe_player_wait_quit(struct mpipe_player *player);

int mpipe_player_deinit(struct mpipe_player *player);


#endif /* ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_PLAYER_H_ */
```

## 117.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

播放器命令队列中的一个条目。`run_id` 标明提交该命令时所属的运行实例，使工作线程（Worker）能够区分：结束运行事件来自正在进行的运行实例，还是描述一个已经拆除的运行实例。

### 注释 3：原第 188 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_PLAYER_H_`。

## 117.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/zbus/zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)
- [zephyr/mpipe/mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [zephyr/mpipe/mpipe_pipeline.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mpipe_player](../audio_video_model_reference/P027_mpipe_player_结构体.md)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [pipeline](../audio_video_model_reference/P027_mpipe_player_结构体.md#a5b1f32dff992d10647b415b6e64989ef)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [cmd_q](../audio_video_model_reference/P027_mpipe_player_结构体.md#aac812a851a4654c47b93f21e6dfe47ab)
- [cmd_buf](../audio_video_model_reference/P027_mpipe_player_结构体.md#ac316dcfe9b0b276c02c3854186f995d1)
- [run_id](../audio_video_model_reference/P027_mpipe_player_结构体.md#a3b9478c32a290093ed0fc3df63aa08eb)
- [mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)
- [last_error](../audio_video_model_reference/P027_mpipe_player_结构体.md#afae2bc92ca0a0fd2a070ad7948cb4bf3)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [worker](../audio_video_model_reference/P027_mpipe_player_结构体.md#a74be28568a290c8136e88a9b915d023c)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [exited](../audio_video_model_reference/P027_mpipe_player_结构体.md#ab059d41757dda23908fc406b1df56e71)
- [mpipe_player_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga180394243652a94c476f1cb83c2c14f7)
- [mpipe_player_play](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga63c7cf14daf0190a8d22dc1f7d4fca5b)
- [mpipe_player_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaabb613b55eefc3cdb97e145e7d3a3c4f)
- [mpipe_player_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gab5482257b941d59d57c494ff56db48e7)
- [mpipe_player_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga91e6fc41ff14ef49975abf8456ffb46c)
- [mpipe_player_replay](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga1a60c7e2006f7a44dc063f6366f9b35d)
- [mpipe_player_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#gaf565c1500aa1ce5136fafb743e042a7e)
- [mpipe_player_wait_quit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga5ff5de85569a7cc388be28fbf1dddb62)
- [mpipe_player_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html#ga561e172ea9426f73203c600b912993d9)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [mpipe_pipeline.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)
- [mpipe_player::run_id](../audio_video_model_reference/P027_mpipe_player_结构体.md#a3b9478c32a290093ed0fc3df63aa08eb)
- [mpipe_player::pipeline](../audio_video_model_reference/P027_mpipe_player_结构体.md#a5b1f32dff992d10647b415b6e64989ef)
- [mpipe_player::worker](../audio_video_model_reference/P027_mpipe_player_结构体.md#a74be28568a290c8136e88a9b915d023c)
- [mpipe_player::cmd_q](../audio_video_model_reference/P027_mpipe_player_结构体.md#aac812a851a4654c47b93f21e6dfe47ab)
- [mpipe_player::exited](../audio_video_model_reference/P027_mpipe_player_结构体.md#ab059d41757dda23908fc406b1df56e71)
- [mpipe_player::cmd_buf](../audio_video_model_reference/P027_mpipe_player_结构体.md#ac316dcfe9b0b276c02c3854186f995d1)
- [mpipe_player::last_error](../audio_video_model_reference/P027_mpipe_player_结构体.md#afae2bc92ca0a0fd2a070ad7948cb4bf3)
- [zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)

---

[上一章](P116_uart.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P118_mqtt_sn.h_源码浏览.md)
