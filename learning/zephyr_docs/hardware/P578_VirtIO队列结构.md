---
id: learning.zephyr-docs.hardware.virtqstruct-5
title: VirtIO队列结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第578章\_VirtIO队列结构

原文：[structvirtq](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html)。读取日期：2026-10-13，`latest`。

`struct virtq` 表示**虚拟队列（Virtqueue）**，包含虚拟队列运行所需的数据结构。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 578.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`lock`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa4a4101177743201210ec1267df31b57) | `struct k_spinlock` | 用于同步虚拟队列操作的**自旋锁（Spinlock）** |
| [`num`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#afeb3f726fe78a18574d7ddd77a1837f9) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 虚拟队列大小 |
| [`desc`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa299da6b7d7b4ede53423d17d3973a92) | `struct virtq_desc *` | 描述符数组 |
| [`avail`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a872b79dd002eb3adf0f680c252323346) | `struct virtq_avail *` | 可用环（Available Ring） |
| [`used`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a7f12283618d0acc418d378a8d554215d) | `struct virtq_used *` | 已用环（Used Ring） |
| [`last_used_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a811241bbc1032b299f303c96e45e39c8) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 最后观察到的已用环索引；用于在收到虚拟队列中断后确定第一个待处理描述符 |
| [`free_desc_stack`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a441e32c89c78d6b432469957cb38db25) | `struct k_stack` | 保存空闲描述符索引的**栈（Stack）** |
| [`free_desc_n`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a540cc380e0e9ec5fc92cf1ea7f3252fe) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | `free_desc_stack` 中空闲描述符的数量 |
| [`recv_cbs`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a2cd048d18e1f8f30a197f33f24f53575) | `struct virtq_receive_callback_entry *` | 回调数组；从设备收回缓冲区后调用其中的回调 |

## 578.2\_使用说明

除非设备提供了 `VIRTIO_F_IN_ORDER` 特性，否则规范不要求 Virtio 设备按收到的顺序使用描述符，参见规范 **2.7.9**。因此，不能直接把描述符数组当作另一个环形缓冲区，每次总是取下一个描述符。`free_desc_stack` 是用于方便地确定下一个空闲描述符的辅助结构。

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO接收回调条目](P577_VirtIO接收回调条目.md) · [下一章：VirtIO缓冲区结构](P579_VirtIO缓冲区结构.md) · [返回大纲](大纲.md)
