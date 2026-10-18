---
id: learning.zephyr-docs.rtio-work-reference.page-6
title: RTIO工作队列头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/work_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_RTIO工作队列头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/work_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_RTIO工作队列头文件参考.md)和[公共API](../rtio_core_reference/P001_RTIO公共接口.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00038"></a>
<a id="adevice_8h_html"></a>
<a id="ap4wq_8h_html"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructk__p4wq__work_html"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__work__req_html"></a>
<a id="astructrtio__work__req_html_a35fc6d43ec653ca463ebd513145e9051"></a>
<a id="astructrtio__work__req_html_acdd57e58b85bbc9a75b9b62d4cb3f771"></a>
<a id="astructrtio__work__req_html_ae6ea29d7fb3b205dc36cd3155d5e885a"></a>
<a id="awork_8h_html_a352516812e7bc88b61cceb2f69d9fd3f"></a>
<a id="awork_8h_html_a62035ecd9def621b4e70b699d9027140"></a>
<a id="awork_8h_html_a705ee008834f10bd4b2ef26e67e1c87f"></a>
<a id="awork_8h_html_add537a23ac061970d890f65d76f5f906"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Croxel Inc.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_RTIO_WORK_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_RTIO_WORK_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;stdint.h&gt;
<a id="l00017"></a>#include &lt;zephyr/device.h&gt;
<a id="l00018"></a>#include &lt;zephyr/rtio/rtio.h&gt;
<a id="l00019"></a>#include &lt;zephyr/sys/p4wq.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#ifdef __cplusplus
<a id="l00022"></a>extern "C" {
<a id="l00023"></a>#endif
<a id="l00024"></a>
<a id="l00030"></a>typedef void (*rtio_work_submit_t)(struct rtio_iodev_sqe *iodev_sqe);
<a id="l00031"></a>
<a id="l00038"></a>struct rtio_work_req {
<a id="l00040"></a>        struct k_p4wq_work work;
<a id="l00041"></a>
<a id="l00045"></a>        struct rtio_iodev_sqe *iodev_sqe;
<a id="l00046"></a>
<a id="l00050"></a>        rtio_work_submit_t handler;
<a id="l00051"></a>};
<a id="l00052"></a>
<a id="l00062"></a>struct rtio_work_req *rtio_work_req_alloc(void);
<a id="l00063"></a>
<a id="l00071"></a>void rtio_work_req_submit(struct rtio_work_req *req,
<a id="l00072"></a>                          struct rtio_iodev_sqe *iodev_sqe,
<a id="l00073"></a>                          rtio_work_submit_t handler);
<a id="l00074"></a>
<a id="l00080"></a>uint32_t rtio_work_req_used_count_get(void);
<a id="l00081"></a>
<a id="l00082"></a>#ifdef __cplusplus
<a id="l00083"></a>}
<a id="l00084"></a>#endif
<a id="l00085"></a>
<a id="l00086"></a>#endif /* ZEPHYR_INCLUDE_RTIO_WORK_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权属于Croxel Inc.（2024年），许可证为Apache-2.0；原始版权与SPDX记录保留。

2. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_WORK_H_`结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API和宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `p4wq.h`

符号定位：[p4wq.h](../p4_work_reference/P001_P4工作队列头文件参考.md)。

### `rtio.h`

以较少工作量移动字节的实时输入输出（Real-Time I/O，RTIO）设备API。

符号定位：[rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `k_p4wq_work`

P4队列工作项（P4 Queue Work Item）。

定义位置（Definition）：p4wq.h:36。

符号定位：[k_p4wq_work](../p4_work_reference/P005_P4工作项结构.md)。

### `rtio_iodev_sqe`

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_work_req`

RTIO工作请求（Work Request）。

定义位置（Definition）：work.h:38。

符号定位：[rtio_work_req](P007_RTIO工作请求.md)。

### `rtio_work_req::work`

```c
struct k_p4wq_work work
```

用于提交工作单元的工作项（Work Item）。

定义位置（Definition）：work.h:40。

符号定位：[rtio_work_req::work](P007_RTIO工作请求.md#a35fc6d43ec653ca463ebd513145e9051)。

### `rtio_work_req::handler`

```c
rtio_work_submit_t handler
```

可在其中执行同步操作的回调处理函数。

定义位置（Definition）：work.h:50。

符号定位：[rtio_work_req::handler](P007_RTIO工作请求.md#acdd57e58b85bbc9a75b9b62d4cb3f771)。

### `rtio_work_req::iodev_sqe`

```c
struct rtio_iodev_sqe * iodev_sqe
```

包含该操作的IODEV SQE句柄（Handle）。

定义位置（Definition）：work.h:45。

符号定位：[rtio_work_req::iodev_sqe](P007_RTIO工作请求.md#ae6ea29d7fb3b205dc36cd3155d5e885a)。

### `rtio_work_req_used_count_get`

```c
uint32_t rtio_work_req_used_count_get(void)
```

获取预分配池（Pre-allocated Pool）中当前正在使用的条目数。

符号定位：[rtio_work_req_used_count_get](P005_RTIO工作队列头文件参考.md#a352516812e7bc88b61cceb2f69d9fd3f)。

### `rtio_work_req_submit`

```c
void rtio_work_req_submit(struct rtio_work_req *req, struct rtio_iodev_sqe *iodev_sqe, rtio_work_submit_t handler)
```

提交RTIO工作请求。

符号定位：[rtio_work_req_submit](P005_RTIO工作队列头文件参考.md#a62035ecd9def621b4e70b699d9027140)。

### `rtio_work_req_alloc`

```c
struct rtio_work_req * rtio_work_req_alloc(void)
```

分配一个用于执行RTIO工作请求的条目。

符号定位：[rtio_work_req_alloc](P005_RTIO工作队列头文件参考.md#a705ee008834f10bd4b2ef26e67e1c87f)。

### `rtio_work_submit_t`

```c
void(* rtio_work_submit_t)(struct rtio_iodev_sqe *iodev_sqe)
```

用于执行工作操作的回调API。

定义位置（Definition）：work.h:30。

符号定位：[rtio_work_submit_t](P005_RTIO工作队列头文件参考.md#add537a23ac061970d890f65d76f5f906)。

## 6.4\_源码跟踪译注

> 译注——rtio_work_req_alloc()从固定的内存块分配器（Memory Slab）以K_NO_WAIT取得请求；没有可用条目时返回NULL，不等待也不从通用堆扩容。请求数量受CONFIG_RTIO_WORKQ_POOL_ITEMS控制；used_count_get返回当前已分配条目数，不只计算排队中的条目。

> 译注——rtio_work_req_submit()遇到NULL请求直接返回；请求存在而iodev_sqe或handler为NULL时会把请求归还slab并返回。函数返回void，不会在这些路径自动产生RTIO错误CQE。调用方应在提交前建立有效参数及错误处理，不能把一次无返回值调用当作已受理证明。

> 译注——有效请求会保存iodev_sqe和handler后加入k_queue。工作线程取出请求，调用handler(req->iodev_sqe)，随后归还请求对象。handler返回后不得继续保留或重用已回收的req；IODEV SQE及其引用缓冲区也必须覆盖实际异步工作期间。

> 译注——虽然公开结构体保留k_p4wq_work成员，当前rtio_workq.c并未调用P4工作队列调度API，而是使用k_queue和专用线程。入队顺序是FIFO，没有根据SQE.prio排序；多个工作线程可并行执行，完成顺序也不一定等于入队顺序。不能仅凭成员类型推断支持P4优先级或截止时间调度。

> 译注——CONFIG_RTIO_WORKQ启用服务并选择RTIO_CONSUME_SEM。Kconfig中请求池默认4项，线程数在SPI_RTIO、I2C_RTIO或I3C_RTIO启用时默认2，否则默认1；线程栈默认1024字节，线程优先级默认MAIN_THREAD_PRIORITY。这些是可配置默认值，不能当成所有构建的固定资源量。

> 译注——工作线程直接调用handler，返回后只释放工作请求，不自动调用rtio_iodev_sqe_ok／err。因此同步I/O的结果如何回报RTIO，需要由具体handler或其调用路径负责；把阻塞操作移到工作线程并没有使底层硬件操作本身变成无阻塞。

头文件相对定位：[include/zephyr/rtio/work.h](../../../include/zephyr/rtio/work.h)，关联实现／接口：[subsys/rtio/rtio_workq.c](../../../subsys/rtio/rtio_workq.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/work.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/rtio_workq.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_RTIO工作队列头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [zephyr/sys/p4wq.h](../p4_work_reference/P001_P4工作队列头文件参考.md)
- [rtio_work_submit_t](P005_RTIO工作队列头文件参考.md#add537a23ac061970d890f65d76f5f906)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [rtio_work_req](P007_RTIO工作请求.md)
- [k_p4wq_work](../p4_work_reference/P005_P4工作项结构.md)
- [work](P007_RTIO工作请求.md#a35fc6d43ec653ca463ebd513145e9051)
- [iodev_sqe](P007_RTIO工作请求.md#ae6ea29d7fb3b205dc36cd3155d5e885a)
- [handler](P007_RTIO工作请求.md#acdd57e58b85bbc9a75b9b62d4cb3f771)
- [rtio_work_req_alloc](P005_RTIO工作队列头文件参考.md#a705ee008834f10bd4b2ef26e67e1c87f)
- [rtio_work_req_submit](P005_RTIO工作队列头文件参考.md#a62035ecd9def621b4e70b699d9027140)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rtio_work_req_used_count_get](P005_RTIO工作队列头文件参考.md#a352516812e7bc88b61cceb2f69d9fd3f)

---

[上一章](P005_RTIO工作队列头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_RTIO工作请求.md)
