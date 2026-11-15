---
id: learning.zephyr-docs.rtio-model-reference.page-2
title: RTIO完成事件
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__cqe.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_RTIO完成事件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__cqe.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

一个完成队列事件（Completion Queue Event，CQE）。

```c
#include <zephyr/rtio/cqe.h>
```

<a id="details"></a>

一个完成队列事件（Completion Queue Event，CQE）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_acbe2e6607a752b676d9336b9ca6ce435"></a>

```c
int32_t result
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[result](#acbe2e6607a752b676d9336b9ca6ce435)。

操作的结果。

<a id="r_a15128387ccbea55812ef229eab7241e7"></a>

```c
void * userdata
```

相关声明：[userdata](#a15128387ccbea55812ef229eab7241e7)。

与操作关联的用户数据（User Data）。

<a id="r_a8a7632ef1cfd31529d782bd761908d93"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a8a7632ef1cfd31529d782bd761908d93)。

与操作关联的标志（Flags）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a8a7632ef1cfd31529d782bd761908d93"></a>

### `flags`

```c
uint32_t rtio_cqe::flags
```

与操作关联的标志（Flags）。

<a id="acbe2e6607a752b676d9336b9ca6ce435"></a>

### `result`

```c
int32_t rtio_cqe::result
```

操作的结果。

<a id="a15128387ccbea55812ef229eab7241e7"></a>

### `userdata`

```c
void* rtio_cqe::userdata
```

与操作关联的用户数据（User Data）。

## 2.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：完成事件（CQE）的`result`是`int32_t`结果，`userdata`关联应用上下文，`flags`还可编码内存池信息。CQE对象归还与缓冲区归还是两件事：消费后用`rtio_cqe_release()`释放事件槽，内存池数据处理结束后另用`rtio_release_buffer()`归还；需要的信息应在CQE回收前取得。参见[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)及[完成事件标志](P008_RTIO完成事件标志.md)。

> 译注——源码核对：原始`cqe.h`还有Doxygen隐藏的队列节点`q`，用于CQE对象池及完成队列的入队操作。本页忠实保留公开成员，不能据此把CQE当成只有三个字段的可自行分配传输格式。结果含义由具体操作规定，不能把任意正结果一概解释为接收字节数。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [zephyr/rtio/cqe.h](../rtio_headers_reference/P004_RTIO完成事件头文件源码.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_RTIO上下文.md) · [返回大纲](大纲.md) · [下一章](P003_RTIO输入输出设备.md)
