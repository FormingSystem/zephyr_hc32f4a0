---
id: learning.zephyr-docs.queue-reference.page-4
title: 内核FIFO结构
kind: reference
status: maintained
domains: [zephyr, kernel, synchronization, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__fifo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_内核FIFO结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__fifo.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本册覆盖通用队列（Queue）、先进先出队列（First In, First Out，FIFO）和后进先出队列（Last In, First Out，LIFO）。先读[本册大纲](大纲.md)及对应指南；原始宏展开、声明和参数保留，数据项布局、分配包装及源码差异另作明确译注。

内核FIFO结构（Kernel FIFO Structure）。

```c
#include <zephyr/kernel.h>
```

<a id="details"></a>

内核FIFO结构（Kernel FIFO Structure）。所有成员均属于内部实现，不应直接访问。

## 4.1\_源码定位与版本边界

> 译注——阅读与源码边界：本结构文档由zephyr/kernel.h生成。其内部_queue封装k_queue，可选obj_core受配置控制；字段被INTERNAL_HIDDEN隐藏。页面无成员表不是空结构，也不保证不同配置具有相同大小；请使用[FIFO公共接口](P003_FIFO公共接口.md)。

仓库相对定位：[kernel.h](../../../include/zephyr/kernel.h)、[kernel/queue.c](../../../kernel/queue.c)与[sys/sflist.h](../../../include/zephyr/sys/sflist.h)。本次依据为[官方内核头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h)、[官方队列实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/queue.c)及[官方带标志链表](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/sflist.h)，摘要见[来源记录](../SOURCES.md)。

仓库源码、滚动更新的main和latest网页不能自动视为同一版本。本批完成文档与源码核对，未构建或执行队列并发、内存分配及实板实验。

## 4.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)

<a id="header-details"></a>

---

[上一章](P003_FIFO公共接口.md) · [返回大纲](大纲.md) · [下一章](P005_LIFO公共接口.md)
