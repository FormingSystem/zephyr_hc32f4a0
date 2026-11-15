---
id: learning.zephyr-docs.rtio-model-reference.page-5
title: RTIO设备提交条目
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev__sqe.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_RTIO设备提交条目

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev__sqe.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

```c
#include <zephyr/rtio/sqe.h>
```

<a id="details"></a>

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。可以安全地与`rtio_sqe`相互转换，因为二者占据池提供的同一块内存。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a2bd98599678909c0ddb22f879affa12b"></a>

```c
struct rtio_sqe sqe
```

相关声明：[rtio_sqe](P007_RTIO提交事件.md)、[sqe](#a2bd98599678909c0ddb22f879affa12b)。

此条目携带的提交。

<a id="r_a9cfdd004b65a5e2bc111bc2fb333498c"></a>

```c
struct mpsc_node q
```

相关声明：[mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)、[q](#a9cfdd004b65a5e2bc111bc2fb333498c)。

用于将此条目入队的链接。

<a id="r_a2afb82e550e614f87db7cd1bf2c3a352"></a>

```c
struct rtio_iodev_sqe * next
```

相关声明：[rtio_iodev_sqe](P005_RTIO设备提交条目.md)、[next](#a2afb82e550e614f87db7cd1bf2c3a352)。

链（Chain）或事务（Transaction）中的下一个条目；如果当前是最后一个条目，则为`NULL`。

<a id="r_a3c3a050793589258eab5ff5ac30f24c8"></a>

```c
struct rtio * r
```

相关声明：[rtio](P001_RTIO上下文.md)、[r](#a3c3a050793589258eab5ff5ac30f24c8)。

该提交所属的RTIO上下文。

## 5.2\_详细说明（Detailed Documentation）

<a id="a2afb82e550e614f87db7cd1bf2c3a352"></a>

### `next`

```c
struct rtio_iodev_sqe* rtio_iodev_sqe::next
```

链（Chain）或事务（Transaction）中的下一个条目；如果当前是最后一个条目，则为`NULL`。

<a id="a9cfdd004b65a5e2bc111bc2fb333498c"></a>

### `q`

```c
struct mpsc_node rtio_iodev_sqe::q
```

用于将此条目入队的链接。

<a id="a3c3a050793589258eab5ff5ac30f24c8"></a>

### `r`

```c
struct rtio* rtio_iodev_sqe::r
```

该提交所属的RTIO上下文。

<a id="a2bd98599678909c0ddb22f879affa12b"></a>

### `sqe`

```c
struct rtio_sqe rtio_iodev_sqe::sqe
```

此条目携带的提交。

## 5.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：`rtio_iodev_sqe`把公开SQE放在第一个成员`sqe`中，再附带队列节点、下一项链接和所属上下文。原文的安全转换以对象实际来自这个池布局为前提；不能把单独在栈上创建的`struct rtio_sqe`强转成更大的`struct rtio_iodev_sqe`后访问附加成员。

> 译注——源码核对：`next`由执行器在提交时依据链／事务标志建立，`r`指向所属上下文。它们不是供应用任意改写的外设数据。一次提交完成后，执行器可能把对象归还池中；保存SQE或IODEV SQE指针不延长其生命周期。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/rtio/sqe.h](../rtio_headers_reference/P002_RTIO提交事件头文件源码.md)
- [rtio_sqe](P007_RTIO提交事件.md)
- [mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)
- [rtio_iodev_sqe](P005_RTIO设备提交条目.md)
- [rtio](P001_RTIO上下文.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_RTIO设备函数表.md) · [返回大纲](大纲.md) · [下一章](P006_RTIO上下文池.md)
