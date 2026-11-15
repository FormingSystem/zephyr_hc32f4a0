---
id: learning.zephyr-docs.userspace-sync-reference.page-2
title: Futex结构
kind: reference
status: maintained
domains: [zephyr, kernel, synchronization, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__futex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Futex结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__futex.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本册覆盖快速用户空间互斥量（Fast Userspace Mutex，Futex）、用户模式互斥量（User Mode Mutex）和用户模式信号量（User Mode Semaphore）。[本册大纲](大纲.md)连接基础指南和内核同步参考；原始接口、展开与示例保留，CONFIG_USERSPACE分支及源码差异另作译注。

Futex结构。

```c
#include <zephyr/kernel.h>
```

<a id="details"></a>

Futex结构。k_futex是一种轻量互斥原语（Lightweight Mutual Exclusion Primitive），旨在尽量减少内核参与。无竞争（Uncontended）操作只依赖对共享内存的原子访问。k_futex位于用户内存（User Memory），只要线程有权访问底层内存，就可以使用相应地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a454ad1b595b899306c8e9c8e1431e7a7"></a>

```c
atomic_t val
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[val](#a454ad1b595b899306c8e9c8e1431e7a7)。

Futex的值。

## 2.2\_详细说明（Detailed Documentation）

<a id="a454ad1b595b899306c8e9c8e1431e7a7"></a>

### `val`

```c
atomic_t k_futex::val
```

Futex的值。

用户模式线程通过原子操作直接修改此值，并将预期内容传给k_futex_wait()。

## 2.3\_源码定位与版本边界

> 译注——阅读与源码边界：本结构文档由zephyr/kernel.h生成，公开atomic_t val字段。原文的任意地址指可访问、满足对象存储与对齐要求的用户内存，并非任意整数都可转成有效指针；本次实现按Futex地址组织等待者，不能在仍有等待者时随意复用该存储。expected参数是int，而val类型是atomic_t，协议应使用能正确参与此比较的值。

仓库相对定位：[include/zephyr/kernel.h](../../../include/zephyr/kernel.h)与[kernel/userspace/futex.c](../../../kernel/userspace/futex.c)；本次核对[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h)和[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/futex.c)。

官方源码摘要见[来源记录](../SOURCES.md)；仓库源码、滚动更新的main和latest网页不能自动视为同一版本。本批完成文档与源码核对，未构建或运行用户模式、并发及实板实验。

## 2.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_futex](P002_Futex结构.md)
- [k_futex_wait()](P001_Futex公共接口.md#ga596bfa265f88567ad9e80fd38cd433d3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_Futex公共接口.md) · [返回大纲](大纲.md) · [下一章](P003_用户模式互斥量公共接口.md)
