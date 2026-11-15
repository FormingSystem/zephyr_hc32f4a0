---
id: learning.zephyr-docs.intercore_reference.lockfreeref-160
title: MPSC无锁队列节点
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第160章\_MPSC无锁队列节点

原文：[structmpsc__node](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__node.html)。读取日期：2026-10-13，`latest`。

`mpsc_node`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）队列的节点（Node），即原页所称的队列成员（Queue Member），定义在`zephyr/sys/mpsc_lockfree.h`。

## 160.1\_完整结构

```c
struct mpsc_node {
        mpsc_ptr_t next;
};
```

唯一字段`next`的类型为`mpsc_ptr_t`。原页没有额外字段说明；阅读说明：源码通过该字段链接下一个节点，其指针类型随对称多处理（Symmetric Multiprocessing，SMP）配置变化。条件定义见[MPSC无锁队列接口](P158_MPSC无锁队列接口.md)，完整实现见[MPSC无锁队列完整头文件](P162_MPSC无锁队列完整头文件.md)。

---

[上一章：MPSC无锁队列结构](P159_MPSC无锁队列结构.md) · [下一章：MPSC无锁队列头文件参考](P161_MPSC无锁队列头文件参考.md) · [返回大纲](大纲.md)
