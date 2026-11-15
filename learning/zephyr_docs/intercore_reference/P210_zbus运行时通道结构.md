---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-210
title: zbus运行时通道结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__runtime__channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第210章\_zbus运行时通道结构

原文：[structzbus__runtime__channel](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__runtime__channel.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_runtime_channel`表示运行时通道（Runtime Channel），头文件为`zephyr/zbus/zbus.h`。

## 210.1\_公开成员

原参考页列出`struct zbus_channel channel`成员，并要求参见[zbus通道结构](P206_zbus通道结构.md)。

## 210.2\_对应的可见源码声明

```c
struct zbus_runtime_channel {
        struct zbus_channel channel;
        sys_snode_t _node;
};
```

源码补充：除`channel`之外，可见源码还包含类型为`sys_snode_t`的`_node`内部单向链表节点（Singly Linked List Node），原参考页没有给出该内部成员的说明。

初始化、注册和注销函数见[zbus核心接口](P213_zbus核心接口.md)。消息存储区必须在整个通道生命周期内有效，注册／注销不能在通道遍历中调用；完整原始源码见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

---

[上一章：zbus运行时观察者节点](P209_zbus运行时观察者节点.md) · [下一章：zbus核心头文件参考](P211_zbus核心头文件参考.md) · [返回大纲](大纲.md)
