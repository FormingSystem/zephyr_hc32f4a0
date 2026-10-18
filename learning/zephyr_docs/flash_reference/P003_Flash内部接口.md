---
id: learning.zephyr-docs.flash-reference.page-3
title: Flash内部接口
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__internal__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Flash内部接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__internal__interface.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存控制器的内部接口（Internal Interfaces）。

<a id="details"></a>

闪存控制器的内部接口（Internal Interfaces）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_flash_5Fpages_5Flayout"></a>

```c
struct flash_pages_layout
```

相关声明：[flash_pages_layout](P006_Flash页布局结构.md)。

描述一段大小相同的闪存页序列。

## 3.2\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

## 3.3\_原页交叉引用（Cross References）

- [flash_pages_layout](P006_Flash页布局结构.md)

<a id="header-details"></a>

---

[上一章](P002_Flash驱动后端接口.md) · [返回大纲](大纲.md) · [下一章](P004_Flash存储参数结构.md)
