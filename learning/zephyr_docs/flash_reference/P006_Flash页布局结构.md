---
id: learning.zephyr-docs.flash-reference.page-6
title: Flash页布局结构
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__pages__layout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Flash页布局结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__pages__layout.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

描述一段大小相同的闪存页序列。

```c
#include <zephyr/drivers/flash.h>
```

<a id="details"></a>

描述一段大小相同的闪存页序列。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_af5e496e680dbe9f4fd2738e6dc2534ec"></a>

```c
size_t pages_count
```

相关声明：[pages_count](#af5e496e680dbe9f4fd2738e6dc2534ec)。

该序列中大小相同的页数量。

<a id="r_aabdad4d8a197936f7756950bc73326ee"></a>

```c
size_t pages_size
```

相关声明：[pages_size](#aabdad4d8a197936f7756950bc73326ee)。

该序列中每页的大小，单位为字节。

## 6.2\_详细说明（Detailed Documentation）

<a id="af5e496e680dbe9f4fd2738e6dc2534ec"></a>

### `pages_count`

```c
size_t flash_pages_layout::pages_count
```

该序列中大小相同的页数量。

<a id="aabdad4d8a197936f7756950bc73326ee"></a>

### `pages_size`

```c
size_t flash_pages_layout::pages_size
```

该序列中每页的大小，单位为字节。

## 6.3\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

## 6.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](P010_Flash公共头文件源码.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_Flash页信息结构.md) · [返回大纲](大纲.md) · [下一章](P007_Flash驱动操作结构.md)
