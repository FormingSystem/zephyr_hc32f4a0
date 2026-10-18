---
id: learning.zephyr-docs.hardware.virtqstruct-6
title: VirtIO缓冲区结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第579章\_VirtIO缓冲区结构

原文：[structvirtq__buf](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html)。读取日期：2026-10-13，`latest`。

`struct virtq_buf` 表示传给 `virtq_add_buffer_chain()` 的单个**缓冲区（Buffer）**。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 579.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`addr`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#ad05060db8d467017fca4af593bab9417) | `void *` | 缓冲区的**虚拟地址（Virtual Address）** |
| [`len`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#aaa047b4296f5c104d5a8f5eaf48aaaac) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 缓冲区长度 |

## 579.2\_使用说明

译注：此处 `addr` 是虚拟地址，类型为 `void *`；[设备描述符](P573_VirtIO队列描述符.md)中的 `addr` 是物理地址，类型为 `uint64_t`，二者不要混淆。

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO队列结构](P578_VirtIO队列结构.md) · [下一章：VirtIO驱动后端接口](P580_VirtIO驱动后端接口.md) · [返回大纲](大纲.md)
