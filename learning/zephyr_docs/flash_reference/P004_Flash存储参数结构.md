---
id: learning.zephyr-docs.flash-reference.page-4
title: Flash存储参数结构
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__parameters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Flash存储参数结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__parameters.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存参数（Flash Memory Parameters）。

```c
#include <zephyr/drivers/flash.h>
```

<a id="details"></a>

闪存参数（Flash Memory Parameters）。结构体内容应在闪存设备初始化时填入，并在整个运行期间保持不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a9795a3e4fae4d7b81745e876f62ab3a8"></a>

```c
const size_t write_block_size
```

相关声明：[write_block_size](#a9795a3e4fae4d7b81745e876f62ab3a8)。

最小写入对齐要求和大小。

<a id="r_a218b0cbc797572ce096d0d6f55475ff9"></a>

```c
uint8_t erase_value
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[erase_value](#a218b0cbc797572ce096d0d6f55475ff9)。

设备已擦除区域中的填充值。

## 4.2\_详细说明（Detailed Documentation）

<a id="a218b0cbc797572ce096d0d6f55475ff9"></a>

### `erase_value`

```c
uint8_t flash_parameters::erase_value
```

设备已擦除区域中的填充值。

<a id="a9795a3e4fae4d7b81745e876f62ab3a8"></a>

### `write_block_size`

```c
const size_t flash_parameters::write_block_size
```

最小写入对齐要求和大小。

> 译注——源码核对：这是驱动对外承诺的最小写入对齐和大小，不等于擦除页大小。擦除能力应通过 flash_params_get_erase_cap 查询；当前头文件还含文档隐藏的 caps 字段，不应由本页公开的两个字段推断完整内部布局。

## 4.3\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

## 4.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](P010_Flash公共头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_Flash内部接口.md) · [返回大纲](大纲.md) · [下一章](P005_Flash页信息结构.md)
