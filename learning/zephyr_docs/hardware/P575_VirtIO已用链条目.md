---
id: learning.zephyr-docs.hardware.virtqstruct-2
title: VirtIO已用链条目
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第575章\_VirtIO已用链条目

原文：[structvirtq__used__elem](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html)。读取日期：2026-10-13，`latest`。

`struct virtq_used_elem` 表示**已用描述符链（Used Descriptor Chain）**条目，描述 Virtio 设备归还的一条描述符链。

本页属于**虚拟输入输出（Virtual I/O，VIRTIO）**接口参考。

```c
#include <zephyr/drivers/virtio/virtqueue.h>
```

## 575.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`id`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#a7f1f8b4bc3590a00e85bed3657a9fbdc) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 描述符链头部的索引 |
| [`len`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#ad61ce7642ec40dba74c2f8ffd28ba8ed) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | Virtio 设备写入该描述符链的总字节数 |

本结构的文档由 `zephyr/drivers/virtio/virtqueue.h` 生成。

---

[上一章：VirtIO可用环](P574_VirtIO可用环.md) · [下一章：VirtIO已用环](P576_VirtIO已用环.md) · [返回大纲](大纲.md)
