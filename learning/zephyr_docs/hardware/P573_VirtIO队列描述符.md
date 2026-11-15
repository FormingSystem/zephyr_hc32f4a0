---
id: learning.zephyr-docs.hardware.virtqstruct-0
title: VirtIO队列描述符
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第573章\_VirtIO队列描述符

原文：[structvirtq__desc](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html)。读取日期：2026-10-13，`latest`。

`struct virtq_desc` 表示**虚拟队列描述符（Virtqueue Descriptor）**，描述单个缓冲区。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 573.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`addr`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1d5146808360ff5e359673c193fe4d53) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 缓冲区的**物理地址（Physical Address）** |
| [`len`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1dcd1400d72aa7b628920258e226a7ce) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 缓冲区长度 |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a9731d25acdd201e07e4362f79fb5ba9e) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 缓冲区标志 |
| [`next`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a2703fcd4eb5bf97530687444203e8ee6) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 用于连接下一个描述符；仅当 `flags & VIRTQ_DESC_F_NEXT` 非零时有效 |

## 573.2\_使用说明

标志 `VIRTQ_DESC_F_NEXT` 用来启用描述符链接，`VIRTQ_DESC_F_WRITE` 表示设备可写，详见[队列接口](P572_VirtIO虚拟队列接口.md)。

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO虚拟队列接口](P572_VirtIO虚拟队列接口.md) · [下一章：VirtIO可用环](P574_VirtIO可用环.md) · [返回大纲](大纲.md)
