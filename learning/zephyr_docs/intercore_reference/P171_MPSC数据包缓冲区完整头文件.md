---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-171
title: MPSC数据包缓冲区完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__pbuf_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第171章\_MPSC数据包缓冲区完整头文件

原文：[mpsc__pbuf_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__pbuf_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/sys/mpsc_pbuf.h`的完整官方可见源码（Source Code），仅去除网页行号与行尾空白。版权为2021年的 Nordic Semiconductor ASA，许可证为`Apache-2.0`。MPSC 指多生产者、单消费者（Multiple Producer, Single Consumer）。

标志位掩码（Bit Mask）、数据包长度回调（Callback）和各函数的解释分别见[MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md)和[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)。

## 171.1\_完整源码

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_MPSC_PBUF_H_
#define ZEPHYR_INCLUDE_SYS_MPSC_PBUF_H_

#include <zephyr/kernel.h>
#include <zephyr/sys/mpsc_packet.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


/*
 * Multi producer, single consumer packet buffer allows to allocate variable
 * length consecutive space for storing a packet. When space is allocated
 * it can be filled by the user (except for the first 2 bits) and when packet
 * is ready it is committed. It is allowed to allocate another packet before
 * committing the previous one.
 *
 * If buffer is full and packet cannot be allocated then null is returned unless
 * overwrite mode is selected. In that mode, oldest entry are dropped (user is
 * notified) until allocation succeeds. It can happen that candidate for
 * dropping is currently being claimed. In that case, it is omitted and next
 * packet is dropped and claimed packet is marked as invalid when freeing.
 *
 * Reading packets is performed in two steps. First packet is claimed. Claiming
 * returns pointer to the packet within the buffer. Packet is freed when no
 * longer in use.
 */


#define MPSC_PBUF_SIZE_POW2 BIT(0)

#define MPSC_PBUF_MODE_OVERWRITE BIT(1)

#define MPSC_PBUF_MAX_UTILIZATION BIT(2)

#define MPSC_PBUF_FULL BIT(3)


/* Forward declaration */
struct mpsc_pbuf_buffer;

typedef uint32_t (*mpsc_pbuf_get_wlen)(const union mpsc_pbuf_generic *packet);

typedef void (*mpsc_pbuf_notify_drop)(const struct mpsc_pbuf_buffer *buffer,
                                      const union mpsc_pbuf_generic *packet);

struct mpsc_pbuf_buffer {
        uint32_t tmp_wr_idx;

        uint32_t wr_idx;

        uint32_t tmp_rd_idx;

        uint32_t rd_idx;

        uint32_t flags;

        struct k_spinlock lock;

        mpsc_pbuf_notify_drop notify_drop;

        mpsc_pbuf_get_wlen get_wlen;

        /* Buffer. */
        uint32_t *buf;

        /* Buffer size in 32 bit words. */
        uint32_t size;

        /* Store max buffer usage. */
        uint32_t max_usage;

        struct k_sem sem;
};

struct mpsc_pbuf_buffer_config {
        /* Pointer to a memory used for storing packets. */
        uint32_t *buf;

        /* Buffer size in 32 bit words. */
        uint32_t size;

        /* Callbacks. */
        mpsc_pbuf_notify_drop notify_drop;
        mpsc_pbuf_get_wlen get_wlen;

        /* Configuration flags. */
        uint32_t flags;
};

void mpsc_pbuf_init(struct mpsc_pbuf_buffer *buffer,
                    const struct mpsc_pbuf_buffer_config *config);

union mpsc_pbuf_generic *mpsc_pbuf_alloc(struct mpsc_pbuf_buffer *buffer,
                                         size_t wlen, k_timeout_t timeout);

void mpsc_pbuf_commit(struct mpsc_pbuf_buffer *buffer,
                        union mpsc_pbuf_generic *packet);

void mpsc_pbuf_put_word(struct mpsc_pbuf_buffer *buffer,
                        const union mpsc_pbuf_generic word);

void mpsc_pbuf_put_word_ext(struct mpsc_pbuf_buffer *buffer,
                            const union mpsc_pbuf_generic word,
                            const void *data);

void mpsc_pbuf_put_data(struct mpsc_pbuf_buffer *buffer,
                        const uint32_t *data, size_t wlen);

const union mpsc_pbuf_generic *mpsc_pbuf_claim(struct mpsc_pbuf_buffer *buffer);

void mpsc_pbuf_free(struct mpsc_pbuf_buffer *buffer,
                    const union mpsc_pbuf_generic *packet);

bool mpsc_pbuf_is_pending(struct mpsc_pbuf_buffer *buffer);

void mpsc_pbuf_get_utilization(struct mpsc_pbuf_buffer *buffer,
                               uint32_t *size, uint32_t *now);

int mpsc_pbuf_get_max_utilization(struct mpsc_pbuf_buffer *buffer, uint32_t *max);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_MPSC_PBUF_H_ */
```

## 171.2\_缓冲区工作方式注释译文

多生产者、单消费者数据包缓冲区允许分配可变长度（Variable Length）的连续空间（Consecutive Space）来存储数据包。空间分配后可由用户填充，**但最开始的2位除外**；数据包准备好后再提交（Commit）。**允许在前一个数据包尚未提交时继续分配另一个数据包。**

缓冲区已满、无法分配数据包时，通常返回空指针；选择覆盖模式（Overwrite Mode）时则会丢弃最旧的条目，并通知用户，直到分配成功。候选丢弃数据包可能正被领取（Claim）；这时跳过它，丢弃下一个数据包，而被领取的数据包会在释放时标记为无效（Invalid）。

读取分两步进行：首先领取数据包，得到其位于缓冲区内部的指针；不再使用时再释放（Free）数据包。

## 171.3\_其他可见注释译文

`Forward declaration`表示前向声明，对象为`struct mpsc_pbuf_buffer`。

运行时结构中的`buf`是缓冲区；`size`是缓冲区大小，单位为32位字（32-bit Word）；`max_usage`用于保存最大缓冲区使用量（Maximum Buffer Usage）。

配置结构中的`buf`指向用于存放数据包的内存；`size`仍以32位字计；`notify_drop`和`get_wlen`是回调；`flags`是配置标志（Configuration Flags）。其余字段的原文描述在参考页面中，见[MPSC数据包缓冲区运行时结构](P168_MPSC数据包缓冲区运行时结构.md)和[MPSC数据包缓冲区配置](P169_MPSC数据包缓冲区配置.md)。

`__cplusplus`分支提供 C++ 的 C 语言链接约定，末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SYS_MPSC_PBUF_H_`的结束。网页未显示的文档注释不补造到源码中。

---

[上一章：MPSC数据包缓冲区头文件参考](P170_MPSC数据包缓冲区头文件参考.md) · [下一章：MPSC数据包描述接口](P172_MPSC数据包描述接口.md) · [返回大纲](大纲.md)
