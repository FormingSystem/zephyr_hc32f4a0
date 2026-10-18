---
id: learning.zephyr-docs.hardware.virtqstruct-4
title: VirtIO接收回调条目
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第577章\_VirtIO接收回调条目

原文：[structvirtq__receive__callback__entry](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html)。读取日期：2026-10-13，`latest`。

`struct virtq_receive_callback_entry` 表示**回调描述符（Callback Descriptor）**，保存回调函数及其参数。Virtio 设备归还此条目关联的描述符链后，调用该回调。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 577.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`cb`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#ae892b29ffebb17cba4154e342278908d) | [`virtq_receive_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga311909fbebf3cb96ace6c751fabcf708) | 回调函数指针 |
| [`opaque`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#adc164ebec52cd00cc15839b1cda4be56) | `void *` | 传给回调函数的参数 |

## 577.2\_使用说明

回调签名及设备写入字节数参数见[队列接口](P572_VirtIO虚拟队列接口.md)。

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO已用环](P576_VirtIO已用环.md) · [下一章：VirtIO队列结构](P578_VirtIO队列结构.md) · [返回大纲](大纲.md)
