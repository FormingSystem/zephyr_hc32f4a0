---
id: learning.zephyr-docs.rtio-headers-reference.page-3
title: RTIO完成事件头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cqe_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_RTIO完成事件头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cqe_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SQE、CQE和IODEV三个头文件的参考与源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

RTIO完成队列事件（Completion Queue Events）及相关函数。

<a id="details"></a>

```c
#include <stdint.h>
#include <string.h>
#include <zephyr/sys/mpsc_lockfree.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

RTIO完成队列事件（Completion Queue Events）及相关函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_rtio_5Fcqe"></a>

```c
struct rtio_cqe
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

一个完成队列事件（Completion Queue Event，CQE）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga0f212500447a5e37e225a6997953b609"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_BUFFER BIT(0)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_BUFFER](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0f212500447a5e37e225a6997953b609)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该条目的缓冲区由RTIO内存池分配。

<a id="r_gaef64ea020a20ac22a0edcb6eca032efc"></a>

```c
#define RTIO_CQE_FLAG_GET(flags)
```

相关声明：[RTIO_CQE_FLAG_GET](../rtio_model_reference/P008_RTIO完成事件标志.md#gaef64ea020a20ac22a0edcb6eca032efc)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从CQE标志值中取得标志位。

<a id="r_ga0b5f3f7e7be472ecf87bd2b08c1888da"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX(flags)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从内存池标志中取得块索引。

<a id="r_ga087465f866d417d5332602bb582cc1a7"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT(flags)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT](../rtio_model_reference/P008_RTIO完成事件标志.md#ga087465f866d417d5332602bb582cc1a7)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从内存池标志中取得块数。

<a id="r_ga28b3a5661248b6b3763aab47417114d6"></a>

```c
#define RTIO_CQE_FLAG_PREP_MEMPOOL(blk_idx, blk_cnt)
```

相关声明：[RTIO_CQE_FLAG_PREP_MEMPOOL](../rtio_model_reference/P008_RTIO完成事件标志.md#ga28b3a5661248b6b3763aab47417114d6)。

为内存池读操作准备CQE标志。

## 3.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：CQE对象记录result、userdata和flags，并含内部队列节点。对象池分配会清零CQE，归还时把节点放回空闲队列并增加pool_free；完成队列消费与CQE对象归还仍需按核心接口成对处理。不能在归还后继续读取旧CQE指针。

> 译注——源码核对：CQE对象与数据缓冲区分别管理。RTIO_CQE_FLAG_MEMPOOL_BUFFER指明缓冲区来自内存池，flags编码块索引和块数；取得并处理数据后用rtio_release_buffer归还缓冲区，再按需要释放CQE槽。释放CQE不会自动释放有效载荷。完整约定见[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——源码核对：本次编码使用位7..0保存标志、位19..8保存块索引、位31..20保存块数。准备宏只做移位与掩码组合，没有内存分配动作；字段宽度限制与分配长度由使用方遵守，不能把有效数据字节数直接当成块数。

> 译注——源码核对：本页内部pool_free是普通uint16_t计数；即使队列使用MPSC算法，也不能仅凭队列名称就推断所有对象池API都适用于任意数量的并发消费者或无外部协调的重复释放。使用范围按RTIO核心和调用上下文约定。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界。仓库相对链接用于定位同名文件，不将本机环境或任意本地版本作为读者前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P162_MPSC无锁队列完整头文件.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码](P004_RTIO完成事件头文件源码.md)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [RTIO_CQE_FLAG_MEMPOOL_BUFFER](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0f212500447a5e37e225a6997953b609)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [RTIO_CQE_FLAG_GET](../rtio_model_reference/P008_RTIO完成事件标志.md#gaef64ea020a20ac22a0edcb6eca032efc)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)
- [RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT](../rtio_model_reference/P008_RTIO完成事件标志.md#ga087465f866d417d5332602bb582cc1a7)
- [RTIO_CQE_FLAG_PREP_MEMPOOL](../rtio_model_reference/P008_RTIO完成事件标志.md#ga28b3a5661248b6b3763aab47417114d6)

<a id="header-details"></a>

---

[上一章](P002_RTIO提交事件头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_RTIO完成事件头文件源码.md)
