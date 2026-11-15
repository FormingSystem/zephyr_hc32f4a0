---
id: learning.zephyr-docs.hardware.virtqstruct-1
title: VirtIO可用环
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第574章\_VirtIO可用环

原文：[structvirtq__avail](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html)。读取日期：2026-10-13，`latest`。

`struct virtq_avail` 表示**虚拟队列可用环（Virtqueue Available Ring）**，用于向 Virtio 设备提交描述符。驱动可写，设备可读。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 574.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#ab013600ebaa7a4c855112599755ce607) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 环标志，例如 `VIRTQ_AVAIL_F_NO_INTERRUPT`；当前未使用 |
| [`idx`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#a70caebae8d3a86d05cb718c5e0a9f88d) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 环头部索引；增加它会提交新加入的描述符 |
| `ring[]` | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 保存描述符索引的环 |

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO队列描述符](P573_VirtIO队列描述符.md) · [下一章：VirtIO已用链条目](P575_VirtIO已用链条目.md) · [返回大纲](大纲.md)
