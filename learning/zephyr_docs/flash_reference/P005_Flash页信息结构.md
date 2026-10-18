---
id: learning.zephyr-docs.flash-reference.page-5
title: Flash页信息结构
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__pages__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Flash页信息结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__pages__info.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存页的信息（Flash Page Information）。

```c
#include <zephyr/drivers/flash.h>
```

<a id="details"></a>

闪存页的信息（Flash Page Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a5c841987fef1636b83141871456ea867"></a>

```c
off_t start_offset
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[start_offset](#a5c841987fef1636b83141871456ea867)。

该页相对于闪存地址空间起点的偏移。

<a id="r_a1ef4b965caaeed26014a6d6ae85c93c1"></a>

```c
size_t size
```

相关声明：[size](#a1ef4b965caaeed26014a6d6ae85c93c1)。

页大小，单位为字节。

<a id="r_adca463710082164f4323d3011235eb6f"></a>

```c
uint32_t index
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[index](#adca463710082164f4323d3011235eb6f)。

页索引，从 0 开始计数。

## 5.2\_详细说明（Detailed Documentation）

<a id="adca463710082164f4323d3011235eb6f"></a>

### `index`

```c
uint32_t flash_pages_info::index
```

页索引，从 0 开始计数。

<a id="a1ef4b965caaeed26014a6d6ae85c93c1"></a>

### `size`

```c
size_t flash_pages_info::size
```

页大小，单位为字节。

<a id="a5c841987fef1636b83141871456ea867"></a>

### `start_offset`

```c
off_t flash_pages_info::start_offset
```

该页相对于闪存地址空间起点的偏移。

## 5.3\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](P010_Flash公共头文件源码.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_Flash存储参数结构.md) · [返回大纲](大纲.md) · [下一章](P006_Flash页布局结构.md)
