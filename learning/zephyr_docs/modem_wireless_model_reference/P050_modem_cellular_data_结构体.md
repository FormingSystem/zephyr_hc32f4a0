---
id: learning.zephyr-docs.modem-wireless-model-reference.page-50
title: modem_cellular_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_modem\_cellular\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝调制解调器（Cellular Modem）驱动实例的运行时数据。

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

<a id="details"></a>

蜂窝调制解调器驱动实例的运行时数据。每个设备实例定义一个零初始化对象。此对象及其引用的全部配置数据，都必须在设备整个生命周期内保持有效。在将对象传给 `MODEM_CELLULAR_DEFINE_INSTANCE()` 之前，设置文档规定的配置成员。设备初始化后，其他所有成员由蜂窝调制解调器实现拥有并更新。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/modem_cellular.h`

## 50.1\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html)
- [MODEM_CELLULAR_DEFINE_INSTANCE()](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga4b61e995f86377dfbab0ca81d1efe492)

<a id="header-details"></a>

---

[上一章](P049_modem_cellular_config_scripts_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_modem_cellular_vendor_config_结构体.md)
