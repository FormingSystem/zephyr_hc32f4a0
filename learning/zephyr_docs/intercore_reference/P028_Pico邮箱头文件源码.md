---
id: learning.zephyr-docs.intercore_reference.mboxextra-28
title: Pico邮箱头文件源码
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mbox__rpi__pico_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第28章\_Pico邮箱头文件源码

原文：[mbox__rpi__pico_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mbox__rpi__pico_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留树莓派（Raspberry Pi）Pico 邮箱头文件`zephyr/drivers/misc/mbox_rpi_pico/mbox_rpi_pico.h`的完整可见源码（Source Code）。只去除网页行号与行尾空白，原版权、许可证和实现均保留；中文入口见[头文件参考](P027_Pico邮箱头文件参考.md)。

## 28.1\_完整可见源码

```c
/*
 * Copyright (c) 2025 Igalia S.L.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_MISC_MBOX_PICO_RPI_PIO_PICO_RPI_H_
#define ZEPHYR_DRIVERS_MISC_MBOX_PICO_RPI_PIO_PICO_RPI_H_


#include <hardware/structs/sio.h>

static inline bool rpi_pico_mbox_write_ready(sio_hw_t *const sio_block)
{
        return sio_block->fifo_st & SIO_FIFO_ST_RDY_BITS;
}

static inline bool rpi_pico_mbox_read_valid(sio_hw_t *const sio_block)
{
        return sio_block->fifo_st & SIO_FIFO_ST_VLD_BITS;
}

static inline void rpi_pico_mbox_drain(sio_hw_t *const sio_block)
{
        while (rpi_pico_mbox_read_valid(sio_block)) {
                (void)sio_block->fifo_rd;
        }
}

static inline void rpi_pico_mbox_write(sio_hw_t *const sio_block, uint32_t value)
{
        sio_block->fifo_wr = value;
}

static inline uint32_t rpi_pico_mbox_read(sio_hw_t *const sio_block)
{
        return sio_block->fifo_rd;
}


#endif /* ZEPHYR_DRIVERS_MISC_MBOX_PICO_RPI_PIO_PICO_RPI_H_ */
```

## 28.2\_状态检查与直接读写

**译注：**两个状态检查函数分别用`SIO_FIFO_ST_RDY_BITS`和`SIO_FIFO_ST_VLD_BITS`掩码检查状态寄存器。清空函数在有可读数据时循环读取并丢弃`fifo_rd`；写函数直接写`fifo_wr`，读函数直接读`fifo_rd`。后二者自身不等待可写或可读状态，原简介的差异见[接口说明](P026_Pico邮箱扩展接口.md)。

---

[上一章：Pico邮箱头文件参考](P027_Pico邮箱头文件参考.md) · [下一章：BCM2711邮箱通道常量](P029_BCM2711邮箱通道常量.md) · [返回大纲](大纲.md)
