---
id: learning.zephyr-docs.intercore_reference.pbufref-151
title: SPSC数据包缓冲区结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第151章\_SPSC数据包缓冲区结构

原文：[structspsc__pbuf](https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf.html)。读取日期：2026-10-13，`latest`。

单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区（Packet Buffer）在读者（Reader）和写者（Writer）共享的内存区域上实现轻量级单向（Unidirectional）缓冲区，提供读／写语义。它可选地管理缓存（Cache）和内存屏障（Memory Barrier），以确保正确的数据访问。

它支持单个写者与单个读者。数据封装为带长度头部（Length Header）的消息。

## 151.1\_完整结构

```c
struct spsc_pbuf {
        struct spsc_pbuf_common common;
        union {
                struct spsc_pbuf_ext_cache cache;
                struct spsc_pbuf_ext_nocache nocache;
        } ext;
};
```

## 151.2\_成员与联合体

| 参数 | 含义 |
| --- | --- |
| `common` | 公共控制部分，类型为`struct spsc_pbuf_common` |
| `ext.cache` | 使用缓存的扩展，类型为`struct spsc_pbuf_ext_cache` |
| `ext.nocache` | 不使用缓存的扩展，类型为`struct spsc_pbuf_ext_nocache` |

译注：原字段参考同时列出`cache``nocache`和匿名联合体类型的`ext`。完整源码表明，前两者位于`ext`联合体（Union）内部，实际成员访问为`ext.cache`和`ext.nocache`；上方保留该嵌套关系。

头文件为`zephyr/sys/spsc_pbuf.h`。成员细节见[SPSC数据包缓冲区公共布局](P152_SPSC数据包缓冲区公共布局.md)、[SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md)和[SPSC数据包缓冲区无缓存扩展](P154_SPSC数据包缓冲区无缓存扩展.md)。

---

[上一章：SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md) · [下一章：SPSC数据包缓冲区公共布局](P152_SPSC数据包缓冲区公共布局.md) · [返回大纲](大纲.md)
