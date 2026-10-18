---
id: learning.zephyr-docs.hardware.virtioapi-1
title: VirtIO虚拟队列接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第572章\_VirtIO虚拟队列接口

原文：[group__virtqueue__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html)。读取日期：2026-10-13，`latest`。

本页定义**虚拟输入输出（Virtual I/O，VIRTIO）**的**虚拟队列（Virtqueue）应用程序编程接口（Application Programming Interface，API）**。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 572.1\_数据结构

| 结构 | 含义 |
| --- | --- |
| [`struct virtq_desc`](P573_VirtIO队列描述符.md) | 虚拟队列**描述符（Descriptor）** |
| [`struct virtq_avail`](P574_VirtIO可用环.md) | 虚拟队列**可用环（Available Ring）** |
| [`struct virtq_used_elem`](P575_VirtIO已用链条目.md) | 已使用的描述符链 |
| [`struct virtq_used`](P576_VirtIO已用环.md) | 虚拟队列**已用环（Used Ring）** |
| [`struct virtq_receive_callback_entry`](P577_VirtIO接收回调条目.md) | **回调描述符（Callback Descriptor）** |
| [`struct virtq`](P578_VirtIO队列结构.md) | 虚拟队列 |
| [`struct virtq_buf`](P579_VirtIO缓冲区结构.md) | 传给 [`virtq_add_buffer_chain()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga5e01b141e28aec876c298047f8d623a6) 的单个缓冲区 |

相关头文件参考为 [`virtqueue.h`](P595_VirtIO队列头文件.md)。

## 572.2\_描述符标志

以下标志用于 [`virtq_desc::flags`](P573_VirtIO队列描述符.md)：

| 宏 | 定义值 | 含义 |
| --- | --- | --- |
| [`VIRTQ_DESC_F_NEXT`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga20e010fee3553a39ff6af7a5cc2837c2) | `1` | 通过 [`virtq_desc::next`](P573_VirtIO队列描述符.md) 将描述符连接为链 |
| [`VIRTQ_DESC_F_WRITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga208ab0e95f24325454621095b80fcf27) | `2` | 将描述符设为设备可写 |

## 572.3\_接收回调

```c
typedef void (*virtq_receive_callback)(void *opaque, uint32_t used_len);
```

这是**接收回调（Receive Callback）**函数类型，无返回值。

| 参数 | 含义 |
| --- | --- |
| `opaque` | 传给回调的参数 |
| `used_len` | Virtio 设备写入此描述符链的总字节数 |

## 572.4\_创建与释放队列

```c
int virtq_create(struct virtq *v, size_t size);
```

创建虚拟队列。`v` 指向要创建的队列，`size` 为队列大小。成功返回 0，失败返回错误码。

```c
void virtq_free(struct virtq *v);
```

释放 `v` 指定的虚拟队列，无返回值。

## 572.5\_添加缓冲区链

```c
int virtq_add_buffer_chain(struct virtq *v, struct virtq_buf *bufs,
                          uint16_t bufs_size, uint16_t device_readable_count,
                          virtq_receive_callback cb, void *cb_opaque,
                          k_timeout_t timeout);
```

向虚拟队列添加一条缓冲区链。

根据规范 **2.7.13.3**，设备在可用环索引 `avail->idx` 增加后即可访问缓冲区。此函数在末尾更新该索引，所以即使尚未调用 `virtio_notify_virtqueue()` 通知设备，设备也可能访问这些缓冲区。

| 参数 | 含义 |
| --- | --- |
| `v` | 要操作的虚拟队列 |
| `bufs` | 待添加到队列的缓冲区数组 |
| `bufs_size` | 缓冲区数量 |
| `device_readable_count` | 设备可读的缓冲区数量；数组中的前 `device_readable_count` 个缓冲区设为设备可读 |
| `cb` | 设备归还缓冲区链后调用的回调，可以为空指针 `NULL` |
| `cb_opaque` | 传给 `cb` 的用户值 |
| `timeout` | 等待空闲描述符的时长，类型为 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md)；使用不等待值 `K_NO_WAIT` 时，可从**中断服务例程（Interrupt Service Routine，ISR）**中调用 |

成功返回 0，失败返回错误码。

## 572.6\_获取与归还空闲描述符

```c
int virtq_get_free_desc(struct virtq *v, uint16_t *desc_idx, k_timeout_t timeout);
```

获取下一个空闲描述符。

| 参数 | 含义 |
| --- | --- |
| `v` | 要操作的虚拟队列 |
| `desc_idx` | 用于保存描述符索引的地址 |
| `timeout` | 等待空闲描述符的时长；使用 `K_NO_WAIT` 时可从 ISR 中调用 |

成功返回 0，失败返回错误码。

```c
void virtq_add_free_desc(struct virtq *v, uint16_t desc_idx);
```

归还空闲描述符。`v` 为所操作的虚拟队列，`desc_idx` 是归还的描述符索引。此函数无返回值。

---

[上一章：VirtIO设备接口](P571_VirtIO设备接口.md) · [下一章：VirtIO队列描述符](P573_VirtIO队列描述符.md) · [返回大纲](大纲.md)
