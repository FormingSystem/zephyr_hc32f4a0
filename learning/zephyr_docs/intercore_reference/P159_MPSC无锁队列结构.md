---
id: learning.zephyr-docs.intercore_reference.lockfreeref-159
title: MPSC无锁队列结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第159章\_MPSC无锁队列结构

原文：[structmpsc](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc.html)。读取日期：2026-10-13，`latest`。

`mpsc`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）队列结构，定义在`zephyr/sys/mpsc_lockfree.h`。

## 159.1\_完整结构

```c
struct mpsc {
        mpsc_ptr_t head;
        struct mpsc_node *tail;
        struct mpsc_node stub;
};
```

## 159.2\_字段参考

| 成员 | 类型 |
| --- | --- |
| `head` | `mpsc_ptr_t` |
| `tail` | `struct mpsc_node *` |
| `stub` | `struct mpsc_node` |

原页只列出成员类型，没有逐字段说明。阅读说明：源码中，生产者通过`head`追加节点，消费者通过`tail`推进；`stub`是用于处理边界情况的哨兵节点（Sentinel Node）。这些关系来自[MPSC无锁队列完整头文件](P162_MPSC无锁队列完整头文件.md)的实现；`mpsc_ptr_t`的条件定义见[MPSC无锁队列接口](P158_MPSC无锁队列接口.md)。

---

[上一章：MPSC无锁队列接口](P158_MPSC无锁队列接口.md) · [下一章：MPSC无锁队列节点](P160_MPSC无锁队列节点.md) · [返回大纲](大纲.md)
