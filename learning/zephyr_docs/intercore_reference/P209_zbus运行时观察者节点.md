---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-209
title: zbus运行时观察者节点
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__observer__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第209章\_zbus运行时观察者节点

原文：[structzbus__observer__node](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__observer__node.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_observer_node`用于注册运行时观察者（Runtime Observer），头文件为`zephyr/zbus/zbus.h`。

**可用条件：** 启用 Kconfig 构建配置系统（Build Configuration System）的`CONFIG_ZBUS_RUNTIME_OBSERVERS`选项。

## 209.1\_参考页列出的成员

| 成员 | 类型 | 类型阅读说明 |
| --- | --- | --- |
| `node` | `sys_snode_t` | 单向链表节点（Singly Linked List Node） |
| `obs` | `const struct zbus_observer *` | 观察者指针（Observer Pointer） |

原页给出上述两个字段及类型，没有额外逐字段契约。

## 209.2\_完整可见声明

```c
struct zbus_observer_node {
        sys_snode_t node;
        const struct zbus_observer *obs;
#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE)
        const struct zbus_channel *chan;
#endif
};
```

源码补充：当启用`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`时，还包含`chan`通道指针成员。上方参考页未列出它，完整代码保留此条件成员。

添加观察者时使用现有节点的接口，以及节点须持久存在的要求，见[zbus核心接口](P213_zbus核心接口.md)；观察者见[zbus观察者结构](P208_zbus观察者结构.md)；完整头文件见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

---

[上一章：zbus观察者结构](P208_zbus观察者结构.md) · [下一章：zbus运行时通道结构](P210_zbus运行时通道结构.md) · [返回大纲](大纲.md)
