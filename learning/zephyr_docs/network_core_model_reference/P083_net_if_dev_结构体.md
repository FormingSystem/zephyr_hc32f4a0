---
id: learning.zephyr-docs.network-core-model-reference.page-83
title: net_if_dev_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__dev.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_net\_if\_dev\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__dev.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口设备（Network Interface Device）结构。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络接口设备结构（Network Interface Device structure）。用于在设备驱动实例（Device driver instance）之上管理网络接口。同一个设备可以对应多个 `net_if_dev` 实例。这类接口主要供链路层（Link layer）使用，同时还与网络上下文（Network context）关联，从而建立网络上下文与网络设备之间的联系。由于设备驱动与这类网络接口具有紧密关系，每个 `net_if_dev` 都应通过 `net_if.h` 中的某个网络设备初始化宏（Network device init macro）实例化。所有成员均为内部成员，不应直接访问。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 83.1\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [net_if_dev](P083_net_if_dev_结构体.md)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)

<a id="header-details"></a>

---

[上一章](P082_net_if_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_net_if_ip_结构体.md)
