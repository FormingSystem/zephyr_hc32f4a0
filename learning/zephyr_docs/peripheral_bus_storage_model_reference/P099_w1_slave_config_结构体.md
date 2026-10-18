---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-99
title: w1_slave_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structw1__slave__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_w1\_slave\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structw1__slave__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

节点专用的单总线（1-Wire）配置结构。

```c
#include <zephyr/drivers/w1.h>
```

<a id="details"></a>

节点特定的 1-Wire 配置结构体。此结构体传递给网络函数，使其能够配置总线，以选定的速度寻址特定从设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a9f42fd1257483f308115ae02e6ef8596"></a>

```c
struct w1_rom rom
```

相关声明：[w1_rom](P098_w1_rom_结构体.md)、[rom](#a9f42fd1257483f308115ae02e6ef8596)。

唯一的 1-Wire ROM。

<a id="r_ab8a2d4522505416863fed561df22d058"></a>

```c
uint32_t overdrive: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[overdrive](#ab8a2d4522505416863fed561df22d058)。

设为 `1` 时使用超速模式（Overdrive speed）。

## 99.2\_详细说明（Detailed Documentation）

<a id="ab8a2d4522505416863fed561df22d058"></a>

### `overdrive`

```c
uint32_t w1_slave_config::overdrive
```

设为 `1` 时使用超速模式（Overdrive speed）。

<a id="a9f42fd1257483f308115ae02e6ef8596"></a>

### `rom`

```c
struct w1_rom w1_slave_config::rom
```

唯一的 1-Wire ROM。

本数据类型文档由以下文件生成：

- `zephyr/drivers/w1.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/drivers/w1.h](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [w1_rom](P098_w1_rom_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_w1_rom_结构体.md) · [返回大纲](大纲.md)
