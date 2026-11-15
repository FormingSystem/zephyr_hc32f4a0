---
id: learning.zephyr-docs.rtio-work-reference.page-7
title: RTIO工作请求
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__work__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_RTIO工作请求

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__work__req.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入寄存器映射、工作队列的参考与源码浏览页及相关结构体，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

RTIO工作请求（Work Request）。

```c
#include <zephyr/rtio/work.h>
```

<a id="details"></a>

RTIO工作请求（Work Request）。此请求使工作操作在RTIO工作队列中的执行与提交相互分离。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a35fc6d43ec653ca463ebd513145e9051"></a>

```c
struct k_p4wq_work work
```

相关声明：[k_p4wq_work](../p4_work_reference/P005_P4工作项结构.md)、[work](#a35fc6d43ec653ca463ebd513145e9051)。

用于提交工作单元的工作项（Work Item）。

<a id="r_ae6ea29d7fb3b205dc36cd3155d5e885a"></a>

```c
struct rtio_iodev_sqe * iodev_sqe
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[iodev_sqe](#ae6ea29d7fb3b205dc36cd3155d5e885a)。

包含该操作的IODEV SQE句柄（Handle）。

<a id="r_acdd57e58b85bbc9a75b9b62d4cb3f771"></a>

```c
rtio_work_submit_t handler
```

相关声明：[rtio_work_submit_t](P005_RTIO工作队列头文件参考.md#add537a23ac061970d890f65d76f5f906)、[handler](#acdd57e58b85bbc9a75b9b62d4cb3f771)。

可在其中执行同步操作的回调处理函数。

## 7.2\_详细说明（Detailed Documentation）

<a id="acdd57e58b85bbc9a75b9b62d4cb3f771"></a>

### `handler`

```c
rtio_work_submit_t rtio_work_req::handler
```

可在其中执行同步操作的回调处理函数。

此字段由`rtio_work_req_submit`在内部填写。

<a id="ae6ea29d7fb3b205dc36cd3155d5e885a"></a>

### `iodev_sqe`

```c
struct rtio_iodev_sqe* rtio_work_req::iodev_sqe
```

包含该操作的IODEV SQE句柄（Handle）。

此字段由`rtio_work_req_submit`在内部填写。

<a id="a35fc6d43ec653ca463ebd513145e9051"></a>

### `work`

```c
struct k_p4wq_work rtio_work_req::work
```

用于提交工作单元的工作项（Work Item）。

## 7.3\_源码定位与版本边界

相对源码定位：[寄存器辅助头文件](../../../include/zephyr/rtio/regmap.h)、[工作队列头文件](../../../include/zephyr/rtio/work.h)、[工作队列实现](../../../subsys/rtio/rtio_workq.c)、[工作队列配置](../../../subsys/rtio/Kconfig.workq)、[核心接口](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)及[P4队列类型](../../../include/zephyr/sys/p4wq.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：有效请求会保存iodev_sqe和handler后加入k_queue。工作线程取出请求，调用handler(req->iodev_sqe)，随后归还请求对象。handler返回后不得继续保留或重用已回收的req；IODEV SQE及其引用缓冲区也必须覆盖实际异步工作期间。

> 译注——源码核对：虽然公开结构体保留k_p4wq_work成员，当前rtio_workq.c并未调用P4工作队列调度API，而是使用k_queue和专用线程。入队顺序是FIFO，没有根据SQE.prio排序；多个工作线程可并行执行，完成顺序也不一定等于入队顺序。不能仅凭成员类型推断支持P4优先级或截止时间调度。

> 译注——源码核对：工作线程直接调用handler，返回后只释放工作请求，不自动调用rtio_iodev_sqe_ok／err。因此同步I/O的结果如何回报RTIO，需要由具体handler或其调用路径负责；把阻塞操作移到工作线程并没有使底层硬件操作本身变成无阻塞。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界；仓库源码使用相对链接，未加入本机环境路径或实板操作前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.4\_原页交叉引用（Cross References）

- [zephyr/rtio/work.h](P006_RTIO工作队列头文件源码.md)
- [k_p4wq_work](../p4_work_reference/P005_P4工作项结构.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [rtio_work_submit_t](P005_RTIO工作队列头文件参考.md#add537a23ac061970d890f65d76f5f906)
- [rtio_work_req_submit](P005_RTIO工作队列头文件参考.md#a62035ecd9def621b4e70b699d9027140)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_RTIO工作队列头文件源码.md) · [返回大纲](大纲.md)
