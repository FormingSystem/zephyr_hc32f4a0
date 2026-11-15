---
id: learning.zephyr-docs.hardware.virtqstruct-3
title: VirtIO已用环
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第576章\_VirtIO已用环

原文：[structvirtq__used](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html)。读取日期：2026-10-13，`latest`。

`struct virtq_used` 表示**虚拟队列已用环（Virtqueue Used Ring）**，用于接收 Virtio 设备归还的描述符。驱动可读，设备可写。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 576.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#a77e64d4bc15ae058515aa96987794f90) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 环标志，例如 `VIRTQ_USED_F_NO_NOTIFY`；当前未使用 |
| [`idx`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#ad3e466c8aee5efcfef250e907717e656) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 环头部索引 |
| `ring[]` | `struct virtq_used_elem` | 由 `struct virtq_used_elem` 构成的环 |

## 576.2\_使用说明

各环元素的链头索引和写入长度见[已用链条目](P575_VirtIO已用链条目.md)。

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO已用链条目](P575_VirtIO已用链条目.md) · [下一章：VirtIO接收回调条目](P577_VirtIO接收回调条目.md) · [返回大纲](大纲.md)
