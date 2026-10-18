---
id: learning.zephyr-docs.api-file-configuration-reference.page-57
title: zephyr__mpipe__mpipe_workqueue.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_zephyr\_\_mpipe\_\_mpipe\_workqueue.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于元素级工作并行（Element-Level Work Parallelism）的共享P4WQ池。

<a id="details"></a>

```c
#include <zephyr/sys/p4wq.h>
```

查看此文件的源码。

用于元素级工作并行处理（Element-Level Work Parallelism）的共享 P4WQ 池（Shared P4WQ Pool）。元素直接使用 Zephyr P4WQ API，通过 `k_p4wq_submit()` 和 `k_p4wq_wait()` 操作共享的 `mpipe_p4wq` 实例。以下元素并行处理图块（Tiles）：

```c
#include <zephyr/mpipe/mpipe_workqueue.h>

static void tile_handler(struct k_p4wq_work *work) {
    // process one tile...
}

static int my_process_fn(struct mpipe_pad *pad, struct net_buf *in,
                      struct net_buf **out) {
    struct k_p4wq_work tile_work[4];

    for (int i = 0; i < 4; i++) {
        tile_work[i].handler = tile_handler;
        tile_work[i].priority = 7;
        tile_work[i].deadline = 0;
        tile_work[i].sync = true;
        k_sem_init(&tile_work[i].done_sem, 0, 1);
        k_p4wq_submit(mpipe_p4wq, &tile_work[i]);
    }
    for (int i = 0; i < 4; i++) {
        k_p4wq_wait(&tile_work[i], K_FOREVER);
    }
    // assemble output...
    *out = result;
    return 0;
}
```

原页随示例提供的符号说明（Symbol Descriptions）：

| 符号 | 声明或类型 | 说明与定义位置 |
| --- | --- | --- |
| `K_FOREVER` | `#define K_FOREVER` | 生成无限超时延迟（Infinite Timeout Delay）；定义位于 `kernel.h:1712`。 |
| `mpipe_p4wq` | `struct k_p4wq *const mpipe_p4wq` | 共享的 mpipe P4WQ 池实例（Shared Pool Instance）。 |
| `k_sem_init` | `int k_sem_init(struct k_sem *sem, unsigned int initial_count, unsigned int limit)` | 初始化信号量（Semaphore）。 |
| `mpipe_workqueue.h` | 头文件（Header） | 用于元素级工作并行处理的共享 P4WQ 池。 |
| `k_p4wq_submit` | `void k_p4wq_submit(struct k_p4wq *queue, struct k_p4wq_work *item)` | 将工作项（Work Item）提交到 P4 队列（P4 Queue）。 |
| `k_p4wq_wait` | `int k_p4wq_wait(struct k_p4wq_work *work, k_timeout_t timeout)` | 重新取得工作项的所有权（Ownership）；若工作项为同步（Synchronous），则等待其完成。 |
| `k_p4wq_work` | 结构体（Struct） | P4 队列工作项（P4 Queue Work Item）；定义位于 `p4wq.h:36`。 |
| `k_p4wq_work::done_sem` | `struct k_sem done_sem` | 定义位于 `p4wq.h:42`。 |
| `mpipe_pad` | 结构体（Struct） | 垫端结构（Pad Structure）；定义位于 `mpipe_pad.h:128`。 |
| `net_buf` | 结构体（Struct） | 网络缓冲区表示（Network Buffer Representation）；定义位于 `net_buf.h:1062`。 |

<a id="header-var-members"></a>
<a id="var-members"></a>

## 57.1\_变量（Variables）

<a id="r_gad175f6e485cce50815afc57ec5c46f55"></a>

```c
struct k_p4wq *const mpipe_p4wq
```

相关声明：[k_p4wq](../p4_work_reference/P003_P4工作队列结构.md)、[mpipe_p4wq](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html#gad175f6e485cce50815afc57ec5c46f55)。

共享的 mpipe P4WQ 池实例（Shared Pool Instance）。


## 57.2\_原页交叉引用（Cross References）

- [zephyr/sys/p4wq.h](../p4_work_reference/P002_P4工作队列头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P565_mpipe_workqueue.h_源码浏览.md)
- [k_p4wq](../p4_work_reference/P003_P4工作队列结构.md)
- [mpipe_p4wq](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html#gad175f6e485cce50815afc57ec5c46f55)
- [k_p4wq_submit()](../p4_work_reference/P001_P4工作队列头文件参考.md#a40e7660d999b94c517712d8b499dd157)
- [k_p4wq_wait()](../p4_work_reference/P001_P4工作队列头文件参考.md#a421ad1ac947495483b414ab89eb6996d)
- [zephyr/mpipe/mpipe_workqueue.h](P057_zephyr__mpipe__mpipe_workqueue.h_文件参考.md)
- [k_p4wq_work](../p4_work_reference/P005_P4工作项结构.md)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_sem_init](../synchronization_reference/P008_信号量公共接口.md#gadcd0e6cfba3392fb887222eafe4c1845)
- [done_sem](../p4_work_reference/P005_P4工作项结构.md#a8dec82b6c03fab9316b7a96c99466920)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)

<a id="header-details"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__mpipe__workqueue_html_gad175f6e485cce50815afc57ec5c46f55"></a>
<a id="agroup__semaphore__apis_html_gadcd0e6cfba3392fb887222eafe4c1845"></a>
<a id="ampipe__workqueue_8h_html"></a>
<a id="ap4wq_8h_html_a40e7660d999b94c517712d8b499dd157"></a>
<a id="ap4wq_8h_html_a421ad1ac947495483b414ab89eb6996d"></a>
<a id="astructk__p4wq__work_html"></a>
<a id="astructk__p4wq__work_html_a8dec82b6c03fab9316b7a96c99466920"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructnet__buf_html"></a>

---

[上一章](P056_zephyr__mpipe__mpipe_fake_src.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P058_zephyr__data__navigation.h_文件参考.md)
