---
id: learning.zephyr-docs.rtio-work-reference.page-3
title: RTIO寄存器配置
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__regs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_RTIO寄存器配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__regs.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入寄存器映射、工作队列的参考与源码浏览页及相关结构体，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

用于描述RTIO操作所涉及的一组不连续内存块（Non-consecutive Memory Chunks）的结构体。

```c
#include <zephyr/rtio/regmap.h>
```

<a id="details"></a>

用于描述RTIO操作所涉及的一组不连续内存块（Non-consecutive Memory Chunks）的结构体。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_rtio_5Fregs_5Flist"></a>

```c
struct rtio_regs_list
```

相关声明：[rtio_regs_list](P004_RTIO寄存器列表.md)。

单个内存块的描述。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.2\_数据成员（Data Fields）

<a id="r_a1234a064ccc401b70dcc78b12938722c"></a>

```c
size_t rtio_regs_num
```

相关声明：[rtio_regs_num](#a1234a064ccc401b70dcc78b12938722c)。

列表中的寄存器数量。

<a id="r_adc88caf9fee2e0a8d5bcc83355d361dd"></a>

```c
struct rtio_regs::rtio_regs_list * rtio_regs_list
```

相关声明：[rtio_regs_list](#adc88caf9fee2e0a8d5bcc83355d361dd)。

包含`rtio_regs_num`个内存块的数组。

## 3.3\_详细说明（Detailed Documentation）

<a id="adc88caf9fee2e0a8d5bcc83355d361dd"></a>

### `rtio_regs_list`

```c
struct rtio_regs::rtio_regs_list * rtio_regs::rtio_regs_list
```

包含`rtio_regs_num`个内存块的数组。

<a id="a1234a064ccc401b70dcc78b12938722c"></a>

### `rtio_regs_num`

```c
size_t rtio_regs::rtio_regs_num
```

列表中的寄存器数量。

## 3.4\_源码定位与版本边界

相对源码定位：[寄存器辅助头文件](../../../include/zephyr/rtio/regmap.h)、[工作队列头文件](../../../include/zephyr/rtio/work.h)、[工作队列实现](../../../subsys/rtio/rtio_workq.c)、[工作队列配置](../../../subsys/rtio/Kconfig.workq)、[核心接口](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)及[P4队列类型](../../../include/zephyr/sys/p4wq.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：非空列表N项会取得2N个读写SQE和1个末尾回调SQE，全部准备完才调用rtio_submit(r, 0)。应考虑上下文已有待提交请求以及整组2N+1个条目的容量。获取失败时通过rtio_iodev_sqe_err(iodev_sqe, -ENOMEM)报告，并调用rtio_sqe_drop_all(r)清理整个上下文待提交队列，不仅是当前寄存器列表。

> 译注——源码核对：rtio_regs_num是size_t，但本次遍历变量为uint8_t。对超过255项的列表，循环变量会回绕，不能据size_t类型认为任意大列表都受支持。此处记录源码限制，没有修改官方实现。

> 译注——源码核对：rtio_regs保存列表项数和列表指针，不持有独立的列表副本；成员名称rtio_regs_list与嵌套结构体类型相同，应按其所在位置区分类型和指针。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界；仓库源码使用相对链接，未加入本机环境路径或实板操作前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [zephyr/rtio/regmap.h](P002_RTIO寄存器映射头文件源码.md)
- [rtio_regs_list](P004_RTIO寄存器列表.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_RTIO寄存器映射头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_RTIO寄存器列表.md)
