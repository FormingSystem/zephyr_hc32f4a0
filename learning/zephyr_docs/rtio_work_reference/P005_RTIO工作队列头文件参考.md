---
id: learning.zephyr-docs.rtio-work-reference.page-5
title: RTIO工作队列头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/work_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_RTIO工作队列头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/work_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入寄存器映射、工作队列的参考与源码浏览页及相关结构体，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

用于异步执行阻塞操作的RTIO工作队列（Work Queues）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/sys/p4wq.h>
```

查看此文件的源码。

用于异步执行阻塞操作的RTIO工作队列（Work Queues）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_rtio_5Fwork_5Freq"></a>

```c
struct rtio_work_req
```

相关声明：[rtio_work_req](P007_RTIO工作请求.md)。

RTIO工作请求（Work Request）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_add537a23ac061970d890f65d76f5f906"></a>

```c
typedef void(* rtio_work_submit_t) (struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_work_submit_t](#add537a23ac061970d890f65d76f5f906)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

用于执行工作操作的回调API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_a705ee008834f10bd4b2ef26e67e1c87f"></a>

```c
struct rtio_work_req * rtio_work_req_alloc (void)
```

相关声明：[rtio_work_req](P007_RTIO工作请求.md)、[rtio_work_req_alloc](#a705ee008834f10bd4b2ef26e67e1c87f)。

分配一个用于执行RTIO工作请求的条目。

<a id="r_a62035ecd9def621b4e70b699d9027140"></a>

```c
void rtio_work_req_submit (struct rtio_work_req *req, struct rtio_iodev_sqe *iodev_sqe, rtio_work_submit_t handler)
```

相关声明：[rtio_work_req_submit](#a62035ecd9def621b4e70b699d9027140)、[rtio_work_req](P007_RTIO工作请求.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_work_submit_t](#add537a23ac061970d890f65d76f5f906)。

提交RTIO工作请求。

<a id="r_a352516812e7bc88b61cceb2f69d9fd3f"></a>

```c
uint32_t rtio_work_req_used_count_get (void)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtio_work_req_used_count_get](#a352516812e7bc88b61cceb2f69d9fd3f)。

获取预分配池（Pre-allocated Pool）中当前正在使用的条目数。

## 5.4\_详细说明（Detailed Documentation）

<a id="add537a23ac061970d890f65d76f5f906"></a>

### `rtio_work_submit_t`

```c
typedef void(* rtio_work_submit_t) (struct rtio_iodev_sqe *iodev_sqe)
```

用于执行工作操作的回调API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 关联的SQE操作。 |

<a id="a705ee008834f10bd4b2ef26e67e1c87f"></a>

### `rtio_work_req_alloc()`

```c
struct rtio_work_req * rtio_work_req_alloc ( void )
```

分配一个用于执行RTIO工作请求的条目。

此分配使用内部内存块分配器（Memory Slab），其中的元素已经预分配。

返回（Returns）：成功时返回已分配条目的指针；分配失败时返回`NULL`。

<a id="a62035ecd9def621b4e70b699d9027140"></a>

### `rtio_work_req_submit()`

```c
void rtio_work_req_submit ( struct rtio_work_req * req, struct rtio_iodev_sqe * iodev_sqe, rtio_work_submit_t handler )
```

提交RTIO工作请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `req` | 用于填入请求信息的条目。 |
| `iodev_sqe` | RTIO操作信息。 |
| `handler` | 实际执行工作操作的处理函数回调。 |

<a id="a352516812e7bc88b61cceb2f69d9fd3f"></a>

### `rtio_work_req_used_count_get()`

```c
uint32_t rtio_work_req_used_count_get ( void )
```

获取预分配池（Pre-allocated Pool）中当前正在使用的条目数。

返回（Returns）：已使用条目的数量。

## 5.5\_源码定位与版本边界

相对源码定位：[寄存器辅助头文件](../../../include/zephyr/rtio/regmap.h)、[工作队列头文件](../../../include/zephyr/rtio/work.h)、[工作队列实现](../../../subsys/rtio/rtio_workq.c)、[工作队列配置](../../../subsys/rtio/Kconfig.workq)、[核心接口](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)及[P4队列类型](../../../include/zephyr/sys/p4wq.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：rtio_work_req_alloc()从固定的内存块分配器（Memory Slab）以K_NO_WAIT取得请求；没有可用条目时返回NULL，不等待也不从通用堆扩容。请求数量受CONFIG_RTIO_WORKQ_POOL_ITEMS控制；used_count_get返回当前已分配条目数，不只计算排队中的条目。

> 译注——源码核对：rtio_work_req_submit()遇到NULL请求直接返回；请求存在而iodev_sqe或handler为NULL时会把请求归还slab并返回。函数返回void，不会在这些路径自动产生RTIO错误CQE。调用方应在提交前建立有效参数及错误处理，不能把一次无返回值调用当作已受理证明。

> 译注——源码核对：有效请求会保存iodev_sqe和handler后加入k_queue。工作线程取出请求，调用handler(req->iodev_sqe)，随后归还请求对象。handler返回后不得继续保留或重用已回收的req；IODEV SQE及其引用缓冲区也必须覆盖实际异步工作期间。

> 译注——源码核对：虽然公开结构体保留k_p4wq_work成员，当前rtio_workq.c并未调用P4工作队列调度API，而是使用k_queue和专用线程。入队顺序是FIFO，没有根据SQE.prio排序；多个工作线程可并行执行，完成顺序也不一定等于入队顺序。不能仅凭成员类型推断支持P4优先级或截止时间调度。

> 译注——源码核对：CONFIG_RTIO_WORKQ启用服务并选择RTIO_CONSUME_SEM。Kconfig中请求池默认4项，线程数在SPI_RTIO、I2C_RTIO或I3C_RTIO启用时默认2，否则默认1；线程栈默认1024字节，线程优先级默认MAIN_THREAD_PRIORITY。这些是可配置默认值，不能当成所有构建的固定资源量。

> 译注——源码核对：工作线程直接调用handler，返回后只释放工作请求，不自动调用rtio_iodev_sqe_ok／err。因此同步I/O的结果如何回报RTIO，需要由具体handler或其调用路径负责；把阻塞操作移到工作线程并没有使底层硬件操作本身变成无阻塞。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界；仓库源码使用相对链接，未加入本机环境路径或实板操作前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.6\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/sys/p4wq.h](../p4_work_reference/P002_P4工作队列头文件源码.md)
- [查看此文件的源码](P006_RTIO工作队列头文件源码.md)
- [rtio_work_req](P007_RTIO工作请求.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_RTIO寄存器列表.md) · [返回大纲](大纲.md) · [下一章](P006_RTIO工作队列头文件源码.md)
