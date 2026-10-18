---
id: learning.zephyr-docs.rtio-model-reference.page-6
title: RTIO上下文池
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__pool.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_RTIO上下文池

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__pool.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

供动态创建的线程使用的RTIO上下文池（Context Pool）。

```c
#include <zephyr/rtio/rtio.h>
```

<a id="details"></a>

供动态创建的线程使用的RTIO上下文池（Context Pool）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_abe49ac5f1cec586855dc5318e3091419"></a>

```c
size_t pool_size
```

相关声明：[pool_size](#abe49ac5f1cec586855dc5318e3091419)。

池的大小。

<a id="r_a5a148773dcd269e1d29be95c77fb6d99"></a>

```c
struct rtio ** contexts
```

相关声明：[rtio](P001_RTIO上下文.md)、[contexts](#a5a148773dcd269e1d29be95c77fb6d99)。

包含池内各上下文的数组。

<a id="r_a89240a8b8e9809d3f61ef903d24e3db2"></a>

```c
atomic_t * used
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[used](#a89240a8b8e9809d3f61ef903d24e3db2)。

用于指示成员已使用或未使用的原子位图（Atomic Bitmap）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a5a148773dcd269e1d29be95c77fb6d99"></a>

### `contexts`

```c
struct rtio** rtio_pool::contexts
```

包含池内各上下文的数组。

<a id="abe49ac5f1cec586855dc5318e3091419"></a>

### `pool_size`

```c
size_t rtio_pool::pool_size
```

池的大小。

<a id="a89240a8b8e9809d3f61ef903d24e3db2"></a>

### `used`

```c
atomic_t* rtio_pool::used
```

用于指示成员已使用或未使用的原子位图（Atomic Bitmap）。

## 6.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：`RTIO_POOL_DEFINE()`建立固定的一组上下文，所谓供动态线程使用不等于每次获取都动态分配内存。`rtio_pool_acquire()`通过原子位图领取空闲槽，并向当前线程授予上下文权限；没有空闲槽时返回NULL。

> 译注——源码核对：`rtio_pool_release()`归还占用位，在用户模式下还撤销当前线程的相应权限，但不会自动清空提交、完成或内存池缓冲区。应用应先完成在途工作、处理CQE并归还所属资源，再让其他线程取得该上下文。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.4\_原页交叉引用（Cross References）

- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [rtio](P001_RTIO上下文.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_RTIO设备提交条目.md) · [返回大纲](大纲.md) · [下一章](P007_RTIO提交事件.md)
