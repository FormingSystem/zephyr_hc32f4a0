---
id: learning.zephyr-docs.hardware.virtioapi-0
title: VirtIO设备接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第571章\_VirtIO设备接口

原文：[group__virtio__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html)。读取日期：2026-10-13，`latest`。

本页定义**虚拟输入输出（Virtual I/O，VIRTIO）**设备的**应用程序编程接口（Application Programming Interface，API）**。接口自 Zephyr **4.2** 提供，版本为 **0.1.0**。

```c
#include <zephyr/drivers/virtio.h>
```

## 571.1\_相关主题与头文件

| 项目 | 内容 |
| --- | --- |
| [VIRTIO驱动后端接口](P580_VirtIO驱动后端接口.md) | 驱动后端 API |
| [虚拟队列接口](P572_VirtIO虚拟队列接口.md) | **虚拟队列（Virtqueue）**操作 |
| [`virtio.h`](P593_VirtIO公共头文件.md) | Virtio 驱动 API 的主头文件 |
| [`virtio_config.h`](P594_VirtIO规范常量.md) | 根据规范定义的 Virtio 公共定义 |

后续所有设备函数的 `dev` 都指向要操作的 Virtio 设备。以下声明按原页概要保留 `static`；详细条目还将这些函数标记为内联函数。

## 571.2\_队列枚举回调

```c
typedef uint16_t (*virtio_enumerate_queues)(uint16_t queue_idx,
                                          uint16_t max_queue_size,
                                          void *opaque);
```

[`virtio_enumerate_queues`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gac66779305009c3896eff113f680c29c4) 是枚举虚拟队列时调用的**回调（Callback）**类型。

| 参数 | 含义 |
| --- | --- |
| `queue_idx` | 当前检查的队列索引 |
| `max_queue_size` | 当前队列允许的最大大小 |
| `opaque` | 指向用户提供数据的指针 |

返回希望为当前虚拟队列设置的大小。

## 571.3\_读取与选择特性位

**特性位（Feature Bit）**用来表示设备提供的能力和驱动选择的能力。

```c
static bool virtio_read_device_feature_bit(const struct device *dev, int bit);
```

读取 Virtio 设备提供的特性位。`bit` 指定要读取的位，返回设备所提供的该位的值。

```c
static int virtio_write_driver_feature_bit(const struct device *dev, int bit, bool value);
```

设置驱动特性位。`bit` 是所选位，`value` 是要写入的值。成功返回 0，失败返回负错误码。

```c
static int virtio_commit_feature_bits(const struct device *dev);
```

提交已选择的特性位。成功返回 0，失败返回负错误码。

## 571.4\_初始化虚拟队列与设备

```c
static int virtio_init_virtqueues(const struct device *dev, uint16_t num_queues,
                                  virtio_enumerate_queues cb, void *opaque);
```

初始化虚拟队列。

| 参数 | 含义 |
| --- | --- |
| `dev` | 要操作的 Virtio 设备 |
| `num_queues` | 要初始化的队列数量 |
| `cb` | 针对每个可用虚拟队列调用的回调 |
| `opaque` | 指向用户提供数据的指针，将传给回调 |

成功返回 0，失败返回负错误码。

```c
static void virtio_finalize_init(const struct device *dev);
```

完成 Virtio 设备初始化。此函数没有返回值。

## 571.5\_获取队列与设备专属配置

```c
static struct virtq *virtio_get_virtqueue(const struct device *dev, uint16_t queue_idx);
```

获取指定索引的虚拟队列。`queue_idx` 为要获取的队列索引。返回队列指针；若队列不存在，返回空指针 `NULL`。

```c
static void *virtio_get_device_specific_config(const struct device *dev);
```

返回**设备专属配置（Device-specific Configuration）**的指针；若设备没有此配置，返回 `NULL`。

## 571.6\_通知虚拟队列

```c
static void virtio_notify_virtqueue(const struct device *dev, uint16_t queue_idx);
```

通知 `queue_idx` 指定的虚拟队列，无返回值。

根据规范 **2.7.13.3**，一旦可用环索引 `avail->idx` 增加，设备就可以访问缓冲区。该索引由 `virtq_add_buffer_chain()` 更新。因此，即使还没有调用 [`virtio_notify_virtqueue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gada51c40981fcdf232b571e1a11dc3cee) 通知设备，设备也可能已经访问缓冲区。

---

[上一章：VirtIO虚拟设备](P570_VirtIO虚拟设备.md) · [下一章：VirtIO虚拟队列接口](P572_VirtIO虚拟队列接口.md) · [返回大纲](大纲.md)
