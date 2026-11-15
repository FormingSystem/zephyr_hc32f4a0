---
id: learning.zephyr-docs.audio-video-model-reference.page-27
title: mpipe_player_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__player.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_mpipe\_player\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__player.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

播放器实例（Player Instance）。

```c
#include <zephyr/mpipe/utils/mpipe_player.h>
```

<a id="details"></a>

播放器（Player）实例。所有字段均供内部使用；应将此结构体视为不透明类型，只向 `mpipe_player_*()` API 传递其指针。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a5b1f32dff992d10647b415b6e64989ef"></a>

```c
struct mpipe * pipeline
```

相关声明：[mpipe](P011_mpipe_结构体.md)、[pipeline](#a5b1f32dff992d10647b415b6e64989ef)。

受控管线（pipeline）。

<a id="r_aac812a851a4654c47b93f21e6dfe47ab"></a>

```c
struct k_msgq cmd_q
```

相关声明：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[cmd_q](#aac812a851a4654c47b93f21e6dfe47ab)。

向工作线程提供命令的队列。

<a id="r_ac316dcfe9b0b276c02c3854186f995d1"></a>

```c
char cmd_buf [CONFIG_MPIPE_PLAYER_CMD_QUEUE_DEPTH *sizeof(struct mpipe_player_cmd_msg)]
```

相关声明：[cmd_buf](#ac316dcfe9b0b276c02c3854186f995d1)。

命令队列的后备缓冲区。

<a id="r_a3b9478c32a290093ed0fc3df63aa08eb"></a>

```c
uint8_t run_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[run_id](#a3b9478c32a290093ed0fc3df63aa08eb)。

运行计数器；工作线程每开始一次运行就递增一次。

<a id="r_afae2bc92ca0a0fd2a070ad7948cb4bf3"></a>

```c
struct mpipe_message last_error
```

相关声明：[mpipe_message](P023_mpipe_message_结构体.md)、[last_error](#afae2bc92ca0a0fd2a070ad7948cb4bf3)。

总线监听器观察到的最后一个错误，由工作线程报告。

<a id="r_a74be28568a290c8136e88a9b915d023c"></a>

```c
struct k_thread worker
```

相关声明：[k_thread](../thread_core_reference/P004_线程对象结构.md)、[worker](#a74be28568a290c8136e88a9b915d023c)。

工作线程控制块（thread control block）。

<a id="r_ab059d41757dda23908fc406b1df56e71"></a>

```c
struct k_sem exited
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[exited](#ab059d41757dda23908fc406b1df56e71)。

工作线程即将退出时发出的信号。

## 27.2\_详细说明（Detailed Documentation）

<a id="ac316dcfe9b0b276c02c3854186f995d1"></a>

### `cmd_buf`

```c
char mpipe_player::cmd_buf[CONFIG_MPIPE_PLAYER_CMD_QUEUE_DEPTH *sizeof(struct mpipe_player_cmd_msg)]
```

命令队列的后备缓冲区。

<a id="aac812a851a4654c47b93f21e6dfe47ab"></a>

### `cmd_q`

```c
struct k_msgq mpipe_player::cmd_q
```

向工作线程提供命令的队列。

<a id="ab059d41757dda23908fc406b1df56e71"></a>

### `exited`

```c
struct k_sem mpipe_player::exited
```

工作线程即将退出时发出的信号。

<a id="afae2bc92ca0a0fd2a070ad7948cb4bf3"></a>

### `last_error`

```c
struct mpipe_message mpipe_player::last_error
```

总线监听器观察到的最后一个错误，由工作线程报告。

<a id="a5b1f32dff992d10647b415b6e64989ef"></a>

### `pipeline`

```c
struct mpipe* mpipe_player::pipeline
```

受控管线（pipeline）。

<a id="a3b9478c32a290093ed0fc3df63aa08eb"></a>

### `run_id`

```c
uint8_t mpipe_player::run_id
```

运行计数器；工作线程每开始一次运行就递增一次。

<a id="a74be28568a290c8136e88a9b915d023c"></a>

### `worker`

```c
struct k_thread mpipe_player::worker
```

工作线程控制块（thread control block）。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/utils/mpipe_player.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/utils/mpipe_player.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__player_8h_source.html)
- [mpipe](P011_mpipe_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_message](P023_mpipe_message_结构体.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_mpipe_parser_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_mpipe_queue_结构体.md)
