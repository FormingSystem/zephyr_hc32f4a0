---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-206
title: zbus通道结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第206章\_zbus通道结构

原文：[structzbus__channel](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__channel.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_channel`表示消息总线（Message Bus）的通道（Channel）。每个通道都关联一个`zbus_channel`结构，用来控制通道的访问和使用。

头文件为`zephyr/zbus/zbus.h`。

`CONFIG_ZBUS_CHANNEL_NAME``CONFIG_ZBUS_CHANNEL_ID`是 Kconfig 构建配置系统（Build Configuration System）的配置宏，控制名称与标识（Identifier，ID）字段。

## 206.1\_对应的可见源码声明

原结构参考页没有逐字段说明。下面从同一头文件的官方可见源码摘录结构声明；保留名称和标识字段的条件编译（Conditional Compilation）：

```c
struct zbus_channel {
#if defined(CONFIG_ZBUS_CHANNEL_NAME) || defined(__DOXYGEN__)
        const char *name;
#endif
#if defined(CONFIG_ZBUS_CHANNEL_ID) || defined(__DOXYGEN__)
        uint32_t id;
#endif
        void *message;

        size_t message_size;

        void *user_data;

        zbus_validator validator;

        struct zbus_channel_data *data;
};
```

## 206.2\_阅读关联

`CONFIG_`开头的配置宏来自 Kconfig 构建配置系统（Build Configuration System）。源码中名称（Name）由`CONFIG_ZBUS_CHANNEL_NAME`控制，标识（Identifier，ID）由`CONFIG_ZBUS_CHANNEL_ID`控制；`__DOXYGEN__`用于文档生成。其他成员分别为消息、消息大小、用户数据、验证函数和通道可变数据。

可变数据见[zbus通道运行时结构](P207_zbus通道运行时结构.md)，运行时通道（Runtime Channel）见[zbus运行时通道结构](P210_zbus运行时通道结构.md)，访问约束和全部函数见[zbus核心接口](P213_zbus核心接口.md)，完整源码见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

---

[上一章：zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md) · [下一章：zbus通道运行时结构](P207_zbus通道运行时结构.md) · [返回大纲](大纲.md)
