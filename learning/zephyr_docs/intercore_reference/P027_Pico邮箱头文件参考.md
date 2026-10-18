---
id: learning.zephyr-docs.intercore_reference.mboxextra-27
title: Pico邮箱头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mbox__rpi__pico_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_Pico邮箱头文件参考

原文：[mbox__rpi__pico_8h](https://docs.zephyrproject.org/latest/doxygen/html/mbox__rpi__pico_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/misc/mbox_rpi_pico/mbox_rpi_pico.h`为树莓派（Raspberry Pi）Pico 邮箱（Mailbox）头文件，包含硬件 SIO 结构声明。SIO 为单周期输入输出（Single-cycle IO），术语来源见[扩展接口](P026_Pico邮箱扩展接口.md)。

## 27.1\_包含项和函数声明

```c
#include <hardware/structs/sio.h>
```


```c
static inline bool rpi_pico_mbox_write_ready(sio_hw_t *const sio_block);
static inline bool rpi_pico_mbox_read_valid(sio_hw_t *const sio_block);
static inline void rpi_pico_mbox_drain(sio_hw_t *const sio_block);
static inline void rpi_pico_mbox_write(sio_hw_t *const sio_block, uint32_t value);
static inline uint32_t rpi_pico_mbox_read(sio_hw_t *const sio_block);
```

`write_ready`检查先进先出队列（First In, First Out，FIFO）是否可写；`read_valid`检查是否可读；`drain`丢弃待处理消息；`write`写入值；`read`读取值。

原页将最后两个函数的简介也分别写成“检查 FIFO 是否可写”和“检查 FIFO 是否可读”。这些文字与实际读写实现的差异见[公共扩展接口中的译注](P026_Pico邮箱扩展接口.md)，完整实现见[源码](P028_Pico邮箱头文件源码.md)。

---

[上一章：Pico邮箱扩展接口](P026_Pico邮箱扩展接口.md) · [下一章：Pico邮箱头文件源码](P028_Pico邮箱头文件源码.md) · [返回大纲](大纲.md)
