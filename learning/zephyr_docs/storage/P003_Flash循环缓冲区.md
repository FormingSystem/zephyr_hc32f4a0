---
id: learning.zephyr-docs.storage.fcb
title: Flash循环缓冲区
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/fcb/fcb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第3章\_Flash循环缓冲区

原文：[Flash Circular Buffer (FCB)](https://docs.zephyrproject.org/latest/services/storage/fcb/fcb.html)。读取日期：2026-10-12，`latest`。

**Flash循环缓冲区（Flash Circular Buffer，FCB）**把 Flash 抽象为**先进先出（First In, First Out，FIFO）**队列：在末尾追加记录，从开头读取记录。

## 3.1\_记录与回收

每条记录包含长度、数据，以及覆盖条目内容的校验和。申请下一条记录空间时，从已用区域末尾分配；开始读取时，首先得到 Flash 中最老的记录。

可以不断追加直到空间耗尽。之后由使用者决定擦除最老的数据块以释放空间，还是暂停写入，等待已有数据被收集完。FCB 把底层存储视为 Flash 扇区数组，每次按扇区擦除旧数据。

校验和用于判断一条记录是否写入完成。FCB 会跳过校验和无效的记录。

## 3.2\_追加记录

1. 调用 `fcb_append()` 取得可写入位置。如果因空间不足失败，可调用 `fcb_rotate()` 擦除最老扇区，然后重新调用 `fcb_append()`。
2. 调用 `flash_area_write()` 写入记录内容。
3. 写完后调用 `fcb_append_finish()`，计算校验和，完成该条记录的写入。

> 译注：`fcb_rotate()` 会丢弃整个最老扇区，应在确认不再需要其中数据后调用；并非只删除一个条目。实际区域偏移应按 FCB 返回的位置计算，不能把扇区内偏移直接当成整个 Flash 设备的绝对地址。

## 3.3\_读取记录

可调用 `fcb_walk()` 并传入回调函数指针，在回调中用 `flash_area_read()` 复制记录内容。观察返回条目的区域指针，可以判断一个扇区中的数据是否已全部读取；确认用完后可调用 `fcb_rotate()`。

另一种方式是逐条迭代：先将记录偏移设为 0，调用 `fcb_getnext()` 取得最老记录；用 `flash_area_read()` 读取内容，再将当前记录指针传给 `fcb_getnext()` 取得下一条，依次继续。

> 译注：原文把“偏移为 0”概括为从最老记录开始。头文件的确切规则是：`loc->fe_sector == NULL` 时从整个 FCB 的最老记录开始；如果扇区指针已指定且 `fe_elem_off == 0`，则从该扇区的第一条开始。首次遍历可将整个 `struct fcb_entry` 清零，不能只清偏移而保留未初始化的扇区指针。

## 3.4\_API参考

FCB 接口由 `fcb.h` 提供，见 [FCB 数据结构](P048_闪存循环缓冲区数据结构目录.md)和 [FCB 操作 API](P047_闪存循环缓冲区接口.md)。底层区域读写见 [Flash 区域 API](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：非易失存储NVS](P002_非易失存储NVS.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：流式Flash写入](P004_流式Flash写入.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：非易失存储NVS](P002_非易失存储NVS.md) · [下一章：流式Flash写入](P004_流式Flash写入.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
