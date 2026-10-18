---
id: learning.zephyr-docs.rtio-core-reference.page-2
title: RTIO核心头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtio_2rtio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_RTIO核心头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtio_2rtio_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO公共接口、核心头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

以较少工作量移动字节的实时输入输出（Real-Time I/O，RTIO）设备API。

<a id="details"></a>

```c
#include <string.h>
#include <zephyr/app_memory/app_memdomain.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/mem_blocks.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/rtio/sqe.h>
#include <zephyr/rtio/cqe.h>
#include <zephyr/rtio/iodev.h>
#include <zephyr/syscalls/rtio.h>
```

查看此文件的源码。

以较少工作量移动字节的实时输入输出（Real-Time I/O，RTIO）设备API。RTIO是一个使用提交队列（Submission Queue）和完成队列（Completion Queue）执行异步批量操作的上下文（Context）。异步I/O操作在提交队列中设置，每个条目按约定的语义描述要执行的操作。可以将这些操作链接为链（Chain），使当前操作完成后才执行下一个操作。如果当前操作失败，所有链接的操作也会失败。操作也可以作为事务（Transaction）提交，将一组操作视为一个操作。这些操作完成时通常产生一个或多个完成队列事件（Completion Queue Events）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_rtio"></a>

```c
struct rtio
```

相关声明：[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

一个RTIO上下文（Context），其内容可以视为一对队列。

<a id="r_rtio_5Fpool"></a>

```c
struct rtio_pool
```

相关声明：[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)。

供动态创建的线程使用的RTIO上下文池（Context Pool）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga338df088eabf3b8f7fefb4ac517b21d4"></a>

```c
#define RTIO_DEFINE(name, sq_sz, cq_sz)
```

相关声明：[RTIO_DEFINE](P001_RTIO公共接口.md#ga338df088eabf3b8f7fefb4ac517b21d4)。

静态定义并初始化一个RTIO上下文（Context）。

<a id="r_ga2437af5061e078950d4a55211d9a902f"></a>

```c
#define RTIO_BMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_BMEM(rtio_partition) static), (static))
```

相关声明：[RTIO_BMEM](P001_RTIO公共接口.md#ga2437af5061e078950d4a55211d9a902f)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)、[rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)。

如果可用，分配到未初始化数据区（BSS）。

<a id="r_ga3b569c01b71e126cff852df50e98fd69"></a>

```c
#define RTIO_DMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_DMEM(rtio_partition) static), (static))
```

相关声明：[RTIO_DMEM](P001_RTIO公共接口.md#ga3b569c01b71e126cff852df50e98fd69)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[K_APP_DMEM](../memory_domain_reference/P006_应用内存分区接口.md#gace571a7f6ee313a732976cc863b5d0e6)、[rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)。

如果可用，分配为已初始化内存（Initialized Memory）。

<a id="r_gae4c2a9384a9ae4ed16dff914b1184ca8"></a>

```c
#define RTIO_DEFINE_WITH_MEMPOOL(name, sq_sz, cq_sz, num_blks, blk_size, balign)
```

相关声明：[RTIO_DEFINE_WITH_MEMPOOL](P001_RTIO公共接口.md#gae4c2a9384a9ae4ed16dff914b1184ca8)。

静态定义并初始化一个RTIO上下文（Context）。

<a id="r_ga4575e199f9747909d4ec879a43a371e6"></a>

```c
#define RTIO_POOL_DEFINE(name, pool_sz, sq_sz, cq_sz)
```

相关声明：[RTIO_POOL_DEFINE](P001_RTIO公共接口.md#ga4575e199f9747909d4ec879a43a371e6)。

静态定义并初始化一个RTIO上下文池（Context Pool）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_ga6adaa4d7ef1fa8054000d8d9b8e634bd"></a>

```c
typedef void(* rtio_cqe_callback_t) (struct rtio *r, void *user_data)
```

相关声明：[rtio_cqe_callback_t](P001_RTIO公共接口.md#ga6adaa4d7ef1fa8054000d8d9b8e634bd)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

RTIO完成队列事件回调（Completion Queue Event Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga4213be028b0a1264daaa0d30c4c2d089"></a>

```c
static size_t rtio_mempool_block_size (const struct rtio *r)
```

相关声明：[rtio_mempool_block_size](P001_RTIO公共接口.md#ga4213be028b0a1264daaa0d30c4c2d089)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

获取RTIO上下文的内存池块大小（Memory Pool Block Size）。

<a id="r_ga1f4fb7bccbaae08a94387e4b11275a78"></a>

```c
static uint32_t rtio_sqe_acquirable (struct rtio *r)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtio_sqe_acquirable](P001_RTIO公共接口.md#ga1f4fb7bccbaae08a94387e4b11275a78)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

可获取的提交队列事件数。

<a id="r_ga8b47c954d15a334621def53acceb6799"></a>

```c
static struct rtio_sqe * rtio_sqe_acquire (struct rtio *r)
```

相关声明：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_sqe_acquire](P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，获取一个提交队列事件（SQE）。

<a id="r_gafb6e8c8679cb9483445c510cd6f14741"></a>

```c
static int rtio_sqe_acquire_array (struct rtio *r, size_t n, struct rtio_sqe **sqes)
```

相关声明：[rtio_sqe_acquire_array](P001_RTIO公共接口.md#gafb6e8c8679cb9483445c510cd6f14741)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

如果可用，获取指定数量的提交队列事件（SQE）。

<a id="r_ga9486fb7b50e8d2409a50da235203536b"></a>

```c
static void rtio_sqe_drop_all (struct rtio *r)
```

相关声明：[rtio_sqe_drop_all](P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

丢弃先前获取的全部SQE。

<a id="r_gad848646651fdf3649b882e5268f72a3c"></a>

```c
static struct rtio_cqe * rtio_cqe_acquire (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_acquire](P001_RTIO公共接口.md#gad848646651fdf3649b882e5268f72a3c)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，获取一个完成队列事件（CQE）。

<a id="r_gaabf5e6876e04f92f99a860591c7d310a"></a>

```c
static int rtio_set_cqe_callback (struct rtio *r, rtio_cqe_callback_t callback, void *user_data)
```

相关声明：[rtio_set_cqe_callback](P001_RTIO公共接口.md#gaabf5e6876e04f92f99a860591c7d310a)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe_callback_t](P001_RTIO公共接口.md#ga6adaa4d7ef1fa8054000d8d9b8e634bd)。

设置完成队列事件回调（CQE Callback）。

<a id="r_ga6f55202adeca60aed0343a7a0dcab071"></a>

```c
static void rtio_cqe_produce (struct rtio *r, struct rtio_cqe *cqe)
```

相关声明：[rtio_cqe_produce](P001_RTIO公共接口.md#ga6f55202adeca60aed0343a7a0dcab071)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

如果可用，产生一个完成队列事件（CQE）。

<a id="r_gae562cf241911804cdb9f4e3a73b53df4"></a>

```c
static struct rtio_cqe * rtio_cqe_consume (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_consume](P001_RTIO公共接口.md#gae562cf241911804cdb9f4e3a73b53df4)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，从完成队列中取出一个完成队列事件（CQE）。

<a id="r_gaf617d05d9b59ce1f1d0697617ef6f249"></a>

```c
static struct rtio_cqe * rtio_cqe_consume_block (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_consume_block](P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

等待并从完成队列中取出一个完成队列事件（CQE）。

<a id="r_gaa0799a5f8ad98425d385a07c5d27d9cb"></a>

```c
static void rtio_cqe_release (struct rtio *r, struct rtio_cqe *cqe)
```

相关声明：[rtio_cqe_release](P001_RTIO公共接口.md#gaa0799a5f8ad98425d385a07c5d27d9cb)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

释放已取出的完成队列事件（CQE）。

<a id="r_ga98b8f272b175ff2c0e9f5ed420c3abcc"></a>

```c
static int rtio_flush_completion_queue (struct rtio *r)
```

相关声明：[rtio_flush_completion_queue](P001_RTIO公共接口.md#ga98b8f272b175ff2c0e9f5ed420c3abcc)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

清空完成队列（Completion Queue）。

<a id="r_gae63ffc626a3e99406d36aa47f10b49e1"></a>

```c
void rtio_sqe_signal (struct rtio_sqe *sqe)
```

相关声明：[rtio_sqe_signal](P001_RTIO公共接口.md#gae63ffc626a3e99406d36aa47f10b49e1)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

向一个等待操作SQE（AWAIT SQE）发送信号。

<a id="r_ga75661c8c6c94a0ac6254cec674b478c8"></a>

```c
static uint32_t rtio_cqe_compute_flags (struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtio_cqe_compute_flags](P001_RTIO公共接口.md#ga75661c8c6c94a0ac6254cec674b478c8)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

根据`rtio_iodev_sqe`条目计算CQE标志。

<a id="r_gaedbf9386a36ed99baa290ef6c318ded1"></a>

```c
int rtio_cqe_get_mempool_buffer (const struct rtio *r, struct rtio_cqe *cqe, uint8_t **buff, uint32_t *buff_len)
```

相关声明：[rtio_cqe_get_mempool_buffer](P001_RTIO公共接口.md#gaedbf9386a36ed99baa290ef6c318ded1)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得为该CQE分配的内存池缓冲区（Memory Pool Buffer）。

<a id="r_gacb1d2ffa2b07418d8a8aa319bd4336ab"></a>

```c
static void rtio_iodev_sqe_ok (struct rtio_iodev_sqe *iodev_sqe, int result)
```

相关声明：[rtio_iodev_sqe_ok](P001_RTIO公共接口.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通知执行器（Executor）：一次提交已成功完成。

<a id="r_gaada07aa6acefa548743b525225fa482f"></a>

```c
static void rtio_iodev_sqe_err (struct rtio_iodev_sqe *iodev_sqe, int result)
```

相关声明：[rtio_iodev_sqe_err](P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通知执行器（Executor）：一次提交已出错完成。

<a id="r_ga4abc221d5a90ab882000a72caa0ebd0f"></a>

```c
static void rtio_cqe_submit (struct rtio *r, int result, void *userdata, uint32_t flags)
```

相关声明：[rtio_cqe_submit](P001_RTIO公共接口.md#ga4abc221d5a90ab882000a72caa0ebd0f)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

使用给定结果和用户数据（User Data）提交一个完成队列事件（CQE）。

<a id="r_gaab6843e2038d00a8354f57d7e2ffcf7e"></a>

```c
static int rtio_sqe_rx_buf (const struct rtio_iodev_sqe *iodev_sqe, uint32_t min_buf_len, uint32_t max_buf_len, uint8_t **buf, uint32_t *buf_len)
```

相关声明：[rtio_sqe_rx_buf](P001_RTIO公共接口.md#gaab6843e2038d00a8354f57d7e2ffcf7e)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

获取与接收提交（RX Submission）关联的缓冲区。

<a id="r_ga6530bf56ccbab046a362a6448f941609"></a>

```c
void rtio_release_buffer (struct rtio *r, void *buff, uint32_t buff_len)
```

相关声明：[rtio_release_buffer](P001_RTIO公共接口.md#ga6530bf56ccbab046a362a6448f941609)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

释放由RTIO内存池（Memory Pool）分配的内存。

<a id="r_ga9da42c98546930575525f0f92710f9e4"></a>

```c
static void rtio_access_grant (struct rtio *r, struct k_thread *t)
```

相关声明：[rtio_access_grant](P001_RTIO公共接口.md#ga9da42c98546930575525f0f92710f9e4)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

授予用户线程（User Thread）访问RTIO上下文的权限。

<a id="r_ga9ab6490aa1893ae01bb0938a34c3e248"></a>

```c
static void rtio_access_revoke (struct rtio *r, struct k_thread *t)
```

相关声明：[rtio_access_revoke](P001_RTIO公共接口.md#ga9ab6490aa1893ae01bb0938a34c3e248)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

撤销用户线程（User Thread）访问RTIO上下文的权限。

<a id="r_gac01252e55d2848b38c0ed77b71d600a7"></a>

```c
int rtio_sqe_cancel (struct rtio_sqe *sqe)
```

相关声明：[rtio_sqe_cancel](P001_RTIO公共接口.md#gac01252e55d2848b38c0ed77b71d600a7)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

尝试取消一个SQE。

<a id="r_ga830863e6c8d9b96f4c473a038cab8f8c"></a>

```c
int rtio_sqe_copy_in_get_handles (struct rtio *r, const struct rtio_sqe *sqes, struct rtio_sqe **handle, size_t sqe_count)
```

相关声明：[rtio_sqe_copy_in_get_handles](P001_RTIO公共接口.md#ga830863e6c8d9b96f4c473a038cab8f8c)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

将SQE数组复制到队列中，并取回生成的句柄（Handles）。

<a id="r_ga65e351af0a16dcf504a51ef4eb9316c7"></a>

```c
static int rtio_sqe_copy_in (struct rtio *r, const struct rtio_sqe *sqes, size_t sqe_count)
```

相关声明：[rtio_sqe_copy_in](P001_RTIO公共接口.md#ga65e351af0a16dcf504a51ef4eb9316c7)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

将SQE数组复制到队列中。

<a id="r_ga98b2bbef95aea342a9b86a9775dd5c3b"></a>

```c
int rtio_cqe_copy_out (struct rtio *r, struct rtio_cqe *cqes, size_t cqe_count, k_timeout_t timeout)
```

相关声明：[rtio_cqe_copy_out](P001_RTIO公共接口.md#ga98b2bbef95aea342a9b86a9775dd5c3b)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从队列中复制出CQE数组。

<a id="r_gafee27c64a4a4989c4eb774addde8eb2e"></a>

```c
int rtio_submit (struct rtio *r, uint32_t wait_count)
```

相关声明：[rtio_submit](P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

向底层执行器（Executor）提交I/O请求。

<a id="r_ga37c94f84cfce3810fd598040aba3841e"></a>

```c
struct rtio * rtio_pool_acquire (struct rtio_pool *pool)
```

相关声明：[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_pool_acquire](P001_RTIO公共接口.md#ga37c94f84cfce3810fd598040aba3841e)、[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)。

从池中取得一个RTIO上下文（Context）。

<a id="r_ga05e24d59485f71cc0126d44abbe8cf2b"></a>

```c
void rtio_pool_release (struct rtio_pool *pool, struct rtio *r)
```

相关声明：[rtio_pool_release](P001_RTIO公共接口.md#ga05e24d59485f71cc0126d44abbe8cf2b)、[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

将RTIO上下文（Context）归还到池中。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 2.5\_变量（Variables）

<a id="r_ga86a38086dd85150ab6e479d73db1c6d1"></a>

```c
struct k_mem_partition rtio_partition
```

相关声明：[k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)、[rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)。

与全部RTIO上下文信息关联的内存分区（Memory Partition）。

## 2.6\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)及[构建条件](../../../subsys/rtio/CMakeLists.txt)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：上下文（Context）把提交队列、完成队列和各自的对象池组织在一起。`rtio_sqe_acquire()`成功后已把条目放入待提交队列，调用者仍需填写操作；`rtio_submit()`才启动执行。`rtio_sqe_acquirable()`只是当前可用量，不能据此推导出并发调用间的预留保证。`rtio_sqe_acquire_array()`失败会归还已经取得的条目，但输出数组按原文约定不可使用；`rtio_sqe_drop_all()`清理的是该上下文整个待提交队列。

> 译注——源码核对：完成事件对象（CQE）与有效载荷缓冲区（Payload Buffer）是两种资源。消费CQE后用`rtio_cqe_release(r, cqe)`归还事件槽；通过内存池读操作取得的数据缓冲区，应先获取并处理，再用`rtio_release_buffer()`归还。`rtio_flush_completion_queue()`只取出当下可消费的CQE、释放事件槽并保留遇到的首个负结果，不等待所有在途操作，也不替代数据缓冲区的归还。

> 译注——源码核对：等待完成（Wait for Completion）不等于读取结果。`rtio_submit(r, wait_count)`等待完成计数达到要求；每次`rtio_cqe_submit()`即使没有空闲CQE、仅增加丢弃计数`xcqcnt`，仍会推进`cq_count`与提交等待计数。因此成功返回不能证明已经取到全部结果或所有I/O成功。`RTIO_SQE_NO_RESPONSE`、提交前取消等不产生完成事件的路径不能计入预期CQE数量，否则等待可能无法结束。

> 译注——源码核对：回调在产生完成事件的调用路径上直接执行，没有自动切换到工作线程。`rtio_set_cqe_callback()`仅在`CONFIG_RTIO_CQE_CALLBACK`启用时可用，修改时必须满足原文要求：没有SQE正在执行。`rtio_cqe_produce()`本身只将事件入队；信号量通知、回调和完成计数由`rtio_cqe_submit()`处理。不能把两者当成等价替换。

> 译注——源码核对：取消（Cancellation）是标志请求，不是中止硬件的保证。`z_impl_rtio_sqe_cancel()`沿已有链接设置`RTIO_SQE_CANCELED`；执行器会在适当阶段检查。提交前已取消的条目会附加`RTIO_SQE_NO_RESPONSE`，单次完成处理也可能不生成CQE，因此原文“产生-ECANCELED失败”不能理解成每次取消必定收到一个失败CQE。句柄只在对应SQE仍有效时使用，不能在对象回收复用后继续取消。

> 译注——源码核对：链（Chain）与事务（Transaction）的失败描述按原文保留。当前读取的`rtio_executor_handle_oneshot()`在错误路径上把事务内后续结果设为`-ECANCELED`，但循环后的CHAINED分支仍调用`rtio_iodev_submit(curr, last_result)`，没有在此处统一为后续链设置取消标志。仅凭本次源码不能把原文“所有链接操作都会失败”当作已验证的全链行为；实际依赖该约定时需要对照所使用版本及驱动补充验证。本次没有修改实现。

> 译注——源码核对：内存池读操作（Mempool Read）通过CQE标志记录块索引和数量；数据缓冲区的实际容量可能按块大小向上取整。释放说明声称长度会向上取整，但本次`rtio_block_pool_free()`实际以右移计算块数。应传回取得时的完整缓冲区指针和实际分配长度，不能以有效数据字节数代替，也不要把“忽略无效参数”理解成任意错误地址与长度都能被安全接受。

> 译注——源码核对：多次完成读操作（Multishot Read）正常完成后会重新排队，并为下次内存池读清空原缓冲区字段以便重新分配；读取的执行器在取消或错误路径上停止重提并释放资源。原文的“持续到取消”不是错误后仍自动重试的保证。应用仍需按各完成事件的结果和所有权处理数据。

> 译注——源码核对：用户空间（Userspace）权限授予涉及上下文、按配置存在的信号量及共享延时IODEV，不代表任意外设IODEV也自动授权。系统调用校验会检查操作码、对象权限和读写缓冲区；不能把内核可准备的所有操作都推定为用户模式可用。上下文池释放仅处理权限和占用位，不会自动排空SQE、CQE或释放全部在途数据；归还前应完成所属工作并清理资源。

> 译注——源码核对：源码定位均为相对路径。本页链接的本仓库文件用于追踪同名实现，是否与滚动更新的官方main一致应另行比较；本次结论以来源记录中的官方文件SHA-256为界。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.7\_原页交叉引用（Cross References）

- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)
- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P010_应用内存域头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/mem_blocks.h](../memory_source_reference/P002_内存块头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/rtio/sqe.h](../rtio_headers_reference/P002_RTIO提交事件头文件源码.md)
- [zephyr/rtio/cqe.h](../rtio_headers_reference/P004_RTIO完成事件头文件源码.md)
- [zephyr/rtio/iodev.h](../rtio_headers_reference/P006_RTIO设备头文件源码.md)
- [查看此文件的源码](P003_RTIO核心头文件源码.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)
- [RTIO_DEFINE](P001_RTIO公共接口.md#ga338df088eabf3b8f7fefb4ac517b21d4)
- [RTIO_BMEM](P001_RTIO公共接口.md#ga2437af5061e078950d4a55211d9a902f)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)
- [rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)
- [RTIO_DMEM](P001_RTIO公共接口.md#ga3b569c01b71e126cff852df50e98fd69)
- [K_APP_DMEM](../memory_domain_reference/P006_应用内存分区接口.md#gace571a7f6ee313a732976cc863b5d0e6)
- [RTIO_DEFINE_WITH_MEMPOOL](P001_RTIO公共接口.md#gae4c2a9384a9ae4ed16dff914b1184ca8)
- [RTIO_POOL_DEFINE](P001_RTIO公共接口.md#ga4575e199f9747909d4ec879a43a371e6)
- [rtio_cqe_callback_t](P001_RTIO公共接口.md#ga6adaa4d7ef1fa8054000d8d9b8e634bd)
- [rtio_mempool_block_size](P001_RTIO公共接口.md#ga4213be028b0a1264daaa0d30c4c2d089)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rtio_sqe_acquirable](P001_RTIO公共接口.md#ga1f4fb7bccbaae08a94387e4b11275a78)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_sqe_acquire](P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)
- [rtio_sqe_acquire_array](P001_RTIO公共接口.md#gafb6e8c8679cb9483445c510cd6f14741)
- [rtio_sqe_drop_all](P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [rtio_cqe_acquire](P001_RTIO公共接口.md#gad848646651fdf3649b882e5268f72a3c)
- [rtio_set_cqe_callback](P001_RTIO公共接口.md#gaabf5e6876e04f92f99a860591c7d310a)
- [rtio_cqe_produce](P001_RTIO公共接口.md#ga6f55202adeca60aed0343a7a0dcab071)
- [rtio_cqe_consume](P001_RTIO公共接口.md#gae562cf241911804cdb9f4e3a73b53df4)
- [rtio_cqe_consume_block](P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249)
- [rtio_cqe_release](P001_RTIO公共接口.md#gaa0799a5f8ad98425d385a07c5d27d9cb)
- [rtio_flush_completion_queue](P001_RTIO公共接口.md#ga98b8f272b175ff2c0e9f5ed420c3abcc)
- [rtio_sqe_signal](P001_RTIO公共接口.md#gae63ffc626a3e99406d36aa47f10b49e1)
- [rtio_cqe_compute_flags](P001_RTIO公共接口.md#ga75661c8c6c94a0ac6254cec674b478c8)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [rtio_cqe_get_mempool_buffer](P001_RTIO公共接口.md#gaedbf9386a36ed99baa290ef6c318ded1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rtio_iodev_sqe_ok](P001_RTIO公共接口.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)
- [rtio_iodev_sqe_err](P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)
- [rtio_cqe_submit](P001_RTIO公共接口.md#ga4abc221d5a90ab882000a72caa0ebd0f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [rtio_sqe_rx_buf](P001_RTIO公共接口.md#gaab6843e2038d00a8354f57d7e2ffcf7e)
- [rtio_release_buffer](P001_RTIO公共接口.md#ga6530bf56ccbab046a362a6448f941609)
- [rtio_access_grant](P001_RTIO公共接口.md#ga9da42c98546930575525f0f92710f9e4)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [rtio_access_revoke](P001_RTIO公共接口.md#ga9ab6490aa1893ae01bb0938a34c3e248)
- [rtio_sqe_cancel](P001_RTIO公共接口.md#gac01252e55d2848b38c0ed77b71d600a7)
- [rtio_sqe_copy_in_get_handles](P001_RTIO公共接口.md#ga830863e6c8d9b96f4c473a038cab8f8c)
- [rtio_sqe_copy_in](P001_RTIO公共接口.md#ga65e351af0a16dcf504a51ef4eb9316c7)
- [rtio_cqe_copy_out](P001_RTIO公共接口.md#ga98b2bbef95aea342a9b86a9775dd5c3b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [rtio_submit](P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)
- [rtio_pool_acquire](P001_RTIO公共接口.md#ga37c94f84cfce3810fd598040aba3841e)
- [rtio_pool_release](P001_RTIO公共接口.md#ga05e24d59485f71cc0126d44abbe8cf2b)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)

<a id="header-details"></a>

---

[上一章](P001_RTIO公共接口.md) · [返回大纲](大纲.md) · [下一章](P003_RTIO核心头文件源码.md)
