---
id: learning.zephyr-docs.api-topic-reference.page-28
title: 数据结构 API（Data Structure APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__datastructure__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_数据结构 API（Data Structure APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__datastructure__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-groups"></a>
<a id="groups"></a>

## 28.1\_主题（Topics）

<a id="r_rbtree_5Fapis"></a>

相关声明：[平衡红黑树（Balanced Red/Black Tree）](../rbtree_reference/P001_红黑树公共接口.md)。

平衡红黑树（Balanced Red/Black Tree）实现。

<a id="r_bitarray_5Fapis"></a>

相关声明：[位数组（Bit array）](../bitarray_reference/P001_位数组公共接口.md)。

在位数组（Bit Array）中存储和操作各个位。

<a id="r_union_5Ffind_5Fapis"></a>

相关声明：[并查集（Disjoint-set）](../unionfind_reference/P001_并查集公共接口.md)。

不相交集合／并查集（Disjoint-set／Union-Find）实现。

<a id="r_doubly-linked-list_5Fapis"></a>

相关声明：[双向链表（Doubly-linked list）](../dlist_reference/P001_双向链表公共接口.md)。

双向链表（Doubly-linked List）实现。

<a id="r_flagged-single-linked-list_5Fapis"></a>

相关声明：[带标志的单向链表（Flagged Single-linked list）](../sflist_reference/P001_带标志单向链表公共接口.md)。

带标志单向链表（Flagged Single-linked List）实现。

<a id="r_hashmap_5Fapis"></a>

相关声明：[哈希映射（Hashmap）](../hashmap_reference/P001_哈希映射公共接口.md)。

哈希映射（Hashmap，又称哈希表／Hash Table）API。

<a id="r_mpsc_5Fbuf"></a>

相关声明：[多生产者、单消费者（Multi producer, single consumer，MPSC）分组缓冲区 API](../intercore_reference/P166_MPSC数据包缓冲区接口.md)。

多生产者、单消费者分组缓冲区 API

<a id="r_mpsc_5Flockfree"></a>

相关声明：[MPSC 无锁队列 API（Lockfree Queue API）](../intercore_reference/P158_MPSC无锁队列接口.md)。

多生产者、单消费者（Multiple Producer Single Consumer，MPSC）无锁队列 API

<a id="r_min_5Fheap_5Fapis"></a>

相关声明：[最小堆（Min-heap）](../minheap_reference/P001_值最小堆公共接口.md)。

最小堆（Min-heap）实现。

<a id="r_min_5Fheap_5Fref_5Fapis"></a>

相关声明：[引用最小堆（Reference min-heap）](../minheap_reference/P005_引用最小堆公共接口.md)。

引用式、基于句柄的最小堆（Reference / Handle-based Min-heap）实现。

<a id="r_ring_5Fbuffer_5Fapis"></a>

相关声明：[环形缓冲区 API（Ring Buffer APIs）](../ringbuffer_reference/P001_环形缓冲区公共接口.md)。

简单、仅需头文件的环形缓冲区（Header-only Ring Buffer）实现。

<a id="r_sys_5Fringq_5Fapis"></a>

相关声明：[环形队列（Ring queue）](../ringq_reference/P001_环形队列公共接口.md)。

固定大小的环形队列（Fixed-size Circular Queue）。

<a id="r_spsc_5Fbuf"></a>

相关声明：[单生产者、单消费者（Single producer, single consumer，SPSC）分组缓冲区 API](../intercore_reference/P150_SPSC数据包缓冲区接口.md)。

单生产者、单消费者分组缓冲区 API

<a id="r_spsc_5Flockfree"></a>

相关声明：[SPSC API](../intercore_reference/P163_SPSC无锁队列接口.md)。

单生产者、单消费者（Single Producer Single Consumer，SPSC）无锁队列 API

<a id="r_single-linked-list_5Fapis"></a>

相关声明：[单向链表（Single-linked list）](../slist_reference/P001_单向链表公共接口.md)。

单向链表（Single-linked List）实现。


## 28.2\_原页交叉引用（Cross References）

- [平衡红黑树（Balanced Red/Black Tree）](../rbtree_reference/P001_红黑树公共接口.md)
- [位数组（Bit array）](../bitarray_reference/P001_位数组公共接口.md)
- [并查集（Disjoint-set）](../unionfind_reference/P001_并查集公共接口.md)
- [双向链表（Doubly-linked list）](../dlist_reference/P001_双向链表公共接口.md)
- [带标志的单向链表（Flagged Single-linked list）](../sflist_reference/P001_带标志单向链表公共接口.md)
- [哈希映射（Hashmap）](../hashmap_reference/P001_哈希映射公共接口.md)
- [多生产者、单消费者（Multi producer, single consumer，MPSC）分组缓冲区 API](../intercore_reference/P166_MPSC数据包缓冲区接口.md)
- [MPSC 无锁队列 API（Lockfree Queue API）](../intercore_reference/P158_MPSC无锁队列接口.md)
- [最小堆（Min-heap）](../minheap_reference/P001_值最小堆公共接口.md)
- [引用最小堆（Reference min-heap）](../minheap_reference/P005_引用最小堆公共接口.md)
- [环形缓冲区 API（Ring Buffer APIs）](../ringbuffer_reference/P001_环形缓冲区公共接口.md)
- [环形队列（Ring queue）](../ringq_reference/P001_环形队列公共接口.md)
- [单生产者、单消费者（Single producer, single consumer，SPSC）分组缓冲区 API](../intercore_reference/P150_SPSC数据包缓冲区接口.md)
- [SPSC API](../intercore_reference/P163_SPSC无锁队列接口.md)
- [单向链表（Single-linked list）](../slist_reference/P001_单向链表公共接口.md)

<a id="header-details"></a>

---

[上一章](P027_连接功能（Connectivity）.md) · [返回大纲](大纲.md) · [下一章](P029_按需分页（Demand Paging）.md)
