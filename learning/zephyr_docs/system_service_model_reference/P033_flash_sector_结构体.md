---
id: learning.zephyr-docs.system-service-model-reference.page-33
title: flash_sector_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__sector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_flash\_sector\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__sector.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于传递闪存扇区边界（Flash Sector Boundaries）的结构。

```c
#include <zephyr/storage/flash_map.h>
```

<a id="details"></a>

用于传递 Flash 扇区边界的结构体。此模板用于表示 Flash 存储器布局，消耗的 RAM 远少于 `flash_area`。其中 `fs_off` 使用 `ptrdiff_t`，`fs_size` 使用 `size_t`，因此将 Flash 设备大小限制为不超过目标的地址空间，以控制此结构体的大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a7d3d01c03efcddd6deb757e64e3db865"></a>

```c
ptrdiff_t fs_off
```

相关声明：[fs_off](#a7d3d01c03efcddd6deb757e64e3db865)。

扇区相对于 Flash 设备起始位置的偏移量。

<a id="r_ab1fef4b1b6978d25b5f809d778888f75"></a>

```c
size_t fs_size
```

相关声明：[fs_size](#ab1fef4b1b6978d25b5f809d778888f75)。

扇区大小，单位为字节。

## 33.2\_详细说明（Detailed Documentation）

<a id="a7d3d01c03efcddd6deb757e64e3db865"></a>

### `fs_off`

```c
ptrdiff_t flash_sector::fs_off
```

扇区相对于 Flash 设备起始位置的偏移量。

<a id="ab1fef4b1b6978d25b5f809d778888f75"></a>

### `fs_size`

```c
size_t flash_sector::fs_size
```

扇区大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/storage/flash_map.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/storage/flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h_source.html)
- [flash_area](P027_flash_area_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_flash_mchp_ex_op_userrow_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_flash_stm32_ex_op_rdp_结构体.md)
