---
id: learning.zephyr-docs.dma-reference.page-6
title: DMA通道分配上下文
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdma__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_DMA通道分配上下文

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdma__context.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA上下文结构（Context）。注意：dma_context必须是通过dev->data取得的DMA客户端驱动数据的第一个成员。

```c
#include <zephyr/drivers/dma.h>
```

<a id="details"></a>

DMA上下文结构（Context）。注意：dma_context必须是通过dev->data取得的DMA客户端驱动数据的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a25355c8cc60df536c9a37cdef52aa653"></a>

```c
int32_t magic
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[magic](#a25355c8cc60df536c9a37cdef52aa653)。

用于识别上下文的魔数（Magic Code）。

<a id="r_ac6685cf14ca69c7b77160e5031c0a800"></a>

```c
int dma_channels
```

相关声明：[dma_channels](#ac6685cf14ca69c7b77160e5031c0a800)。

DMA通道数量。

<a id="r_a5b5776088155c9f19488d479924bec8e"></a>

```c
atomic_t * atomic
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[atomic](#a5b5776088155c9f19488d479924bec8e)。

保存各通道位标志的原子对象（Atomic），用于标记已使用／未使用状态。

## 6.2\_详细说明（Detailed Documentation）

<a id="a5b5776088155c9f19488d479924bec8e"></a>

### `atomic`

```c
atomic_t* dma_context::atomic
```

保存各通道位标志的原子对象（Atomic），用于标记已使用／未使用状态。

> 译注——源码核对：这是指向原子位图存储的指针，不是单个通道编号。申请／释放辅助函数按通道号访问对应位；驱动须提供足以容纳dma_channels个位的有效存储，并正确初始化上下文。

<a id="ac6685cf14ca69c7b77160e5031c0a800"></a>

### `dma_channels`

```c
int dma_context::dma_channels
```

DMA通道数量。

<a id="a25355c8cc60df536c9a37cdef52aa653"></a>

### `magic`

```c
int32_t dma_context::magic
```

用于识别上下文的魔数（Magic Code）。

## 6.3\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

> 译注——布局约定：申请和释放辅助函数直接把dev->data转成dma_context指针，因此使用这些辅助函数的驱动必须把它放在数据结构首成员；magic设为DMA_MAGIC并不代替位图和通道数初始化。该上下文只跟踪申请位，不提供任意调用者之间的通道所有权认证。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 6.4\_原页交叉引用（Cross References）

- [dma_context](P006_DMA通道分配上下文.md)
- [zephyr/drivers/dma.h](P010_DMA驱动头文件源码.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_DMA运行状态.md) · [返回大纲](大纲.md) · [下一章](P007_DMA驱动操作结构.md)
