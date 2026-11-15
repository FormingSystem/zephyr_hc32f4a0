---
id: learning.zephyr-docs.intercore_reference.mboxextra-26
title: Pico邮箱扩展接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mbox__rpi__pico__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第26章\_Pico邮箱扩展接口

原文：[group__mbox__rpi__pico__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mbox__rpi__pico__interface.html)。读取日期：2026-10-13，`latest`。

本页为树莓派（Raspberry Pi）Pico 的 SIO 先进先出队列（First In, First Out，FIFO）邮箱（Mailbox）接口。头文件为`zephyr/drivers/misc/mbox_rpi_pico/mbox_rpi_pico.h`。

**术语译注：**SIO 指单周期输入输出（Single-cycle IO），名称依据[树莓派官方Pico SDK寄存器头文件](https://raw.githubusercontent.com/raspberrypi/pico-sdk/master/src/rp2040/hardware_regs/include/hardware/regs/sio.h)。这里仅补充术语，以下函数契约与实现仍按 Zephyr 原页翻译。

## 26.1\_判断是否可写


```c
static inline bool rpi_pico_mbox_write_ready(sio_hw_t *const sio_block);
```

检查 FIFO 是否可写。参数`sio_block`指向 SIO 结构；写 FIFO 未满时返回`true`，没有可写空间时返回`false`。

## 26.2\_判断是否可读


```c
static inline bool rpi_pico_mbox_read_valid(sio_hw_t *const sio_block);
```

检查 FIFO 是否可读。参数`sio_block`指向 SIO 结构；读 FIFO 有可用数据时返回`true`，否则返回`false`。

## 26.3\_丢弃待处理消息


```c
static inline void rpi_pico_mbox_drain(sio_hw_t *const sio_block);
```

丢弃 FIFO 中待处理的消息。参数`sio_block`指向 SIO 结构。

## 26.4\_写入值


```c
static inline void rpi_pico_mbox_write(sio_hw_t *const sio_block, uint32_t value);
```

参数`sio_block`指向 SIO 结构，`value`是要压入队列的值。

原函数简介写为“检查 FIFO 是否可写”。**译注：**[可见源码](P028_Pico邮箱头文件源码.md)实际直接执行`sio_block->fifo_wr = value`，没有检查可写状态；检查函数是`rpi_pico_mbox_write_ready()`。本函数执行写入，不能当作可写性检查使用。

## 26.5\_读取值


```c
static inline uint32_t rpi_pico_mbox_read(sio_hw_t *const sio_block);
```

参数`sio_block`指向 SIO 结构，返回从 FIFO 接收到的值。

原函数简介写为“检查 FIFO 是否可读”。**译注：**可见实现实际直接返回`sio_block->fifo_rd`；检查可读状态的函数是`rpi_pico_mbox_read_valid()`。完整代码见[源码页](P028_Pico邮箱头文件源码.md)，头文件符号汇总见[参考页](P027_Pico邮箱头文件参考.md)。

---

[上一章：邮箱数据传输示例](P025_邮箱数据传输示例.md) · [下一章：Pico邮箱头文件参考](P027_Pico邮箱头文件参考.md) · [返回大纲](大纲.md)
