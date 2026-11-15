---
id: learning.zephyr-docs.hardware.virtiohdr-2
title: VirtIO队列头文件
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtqueue_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第595章\_VirtIO队列头文件

原文：[virtqueue_8h](https://docs.zephyrproject.org/latest/doxygen/html/virtqueue_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/virtio/virtqueue.h` 是**虚拟输入输出（Virtual I/O，VIRTIO）虚拟队列（Virtqueue）应用程序编程接口（Application Programming Interface，API）**的头文件。

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>
```

## 595.1\_数据结构

| 结构 | 内容 |
| --- | --- |
| [`virtq_desc`](P573_VirtIO队列描述符.md) | 虚拟队列描述符 |
| [`virtq_avail`](P574_VirtIO可用环.md) | 可用环（Available Ring） |
| [`virtq_used_elem`](P575_VirtIO已用链条目.md) | 已用描述符链 |
| [`virtq_used`](P576_VirtIO已用环.md) | 已用环（Used Ring） |
| [`virtq_receive_callback_entry`](P577_VirtIO接收回调条目.md) | 回调描述符 |
| [`virtq`](P578_VirtIO队列结构.md) | 虚拟队列 |
| [`virtq_buf`](P579_VirtIO缓冲区结构.md) | 传给 [`virtq_add_buffer_chain()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga5e01b141e28aec876c298047f8d623a6) 的单个缓冲区 |

## 595.2\_标志与回调类型

```c
#define VIRTQ_DESC_F_NEXT 1
#define VIRTQ_DESC_F_WRITE 2
typedef void(* virtq_receive_callback) (void *opaque, uint32_t used_len);
```

两个标志都用于 [`virtq_desc::flags`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a9731d25acdd201e07e4362f79fb5ba9e)：[`VIRTQ_DESC_F_NEXT`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga20e010fee3553a39ff6af7a5cc2837c2) 允许通过 [`virtq_desc::next`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a2703fcd4eb5bf97530687444203e8ee6) 连接下一个描述符，[`VIRTQ_DESC_F_WRITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga208ab0e95f24325454621095b80fcf27) 表示描述符由设备写入。[`virtq_receive_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga311909fbebf3cb96ace6c751fabcf708) 为接收回调函数类型。

## 595.3\_队列函数

```c
int virtq_create (struct virtq *v, size_t size);
void virtq_free (struct virtq *v);
int virtq_add_buffer_chain (struct virtq *v, struct virtq_buf *bufs, uint16_t bufs_size, uint16_t device_readable_count, virtq_receive_callback cb, void *cb_opaque, k_timeout_t timeout);
void virtq_add_free_desc (struct virtq *v, uint16_t desc_idx);
int virtq_get_free_desc (struct virtq *v, uint16_t *desc_idx, k_timeout_t timeout);
```

| 函数 | 作用 |
| --- | --- |
| [`virtq_create()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga3dce3b5099fc117a94da63a24571b6c3) | 创建虚拟队列 |
| [`virtq_free()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga9443eb15529fa16d1024a70075daca28) | 释放虚拟队列 |
| `virtq_add_buffer_chain()` | 向队列添加缓冲区链 |
| [`virtq_add_free_desc()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga55abe7b8204cf0b57cd1c2380dcd66fb) | 归还空闲描述符 |
| [`virtq_get_free_desc()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga79b1b54f0ea6fe8b5110712488f663eb) | 获取下一个空闲描述符 |

完整参数及返回值见[虚拟队列接口](P572_VirtIO虚拟队列接口.md)。

---

[上一章：VirtIO规范常量](P594_VirtIO规范常量.md) · [下一章：平台固件说明](P596_平台固件说明.md) · [返回大纲](大纲.md)
