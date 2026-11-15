---
id: learning.zephyr-docs.rtio-core-reference.page-1
title: RTIO公共接口
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_RTIO公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO公共接口、核心头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

实时输入输出（Real-Time I/O，RTIO）。

<a id="details"></a>

实时输入输出（Real-Time I/O，RTIO）。自3.2版提供；接口版本：0.2.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_rtio_5Fcqe_5Fflags"></a>

相关声明：[RTIO完成队列事件标志（CQE Flags）](../rtio_model_reference/P008_RTIO完成事件标志.md)。

RTIO完成队列事件（Completion Queue Event，CQE）标志。

<a id="r_rtio_5Fi2c_5Fflags"></a>

相关声明：[RTIO I2C输入输出设备标志（IODEV Flags）](../hardware/P442_RTIO的I2C标志.md)。

RTIO I2C输入输出设备（I/O Device，IODEV）标志。

<a id="r_rtio_5Fi3c_5Fflags"></a>

相关声明：[RTIO I3C输入输出设备标志（IODEV Flags）](../hardware/P434_RTIO的I3C标志.md)。

RTIO I3C输入输出设备（I/O Device，IODEV）标志。

<a id="r_rtio_5Fops"></a>

相关声明：[RTIO Operation Codes](../rtio_model_reference/P009_RTIO操作码.md)。

RTIO提交队列事件（Submission Queue Event，SQE）操作码（Operation Codes）。

<a id="r_rtio_5Fsqe_5Fprio"></a>

相关声明：[RTIO优先级（Priorities）](../rtio_model_reference/P011_RTIO优先级.md)。

RTIO预定义优先级（Predefined Priorities）。

<a id="r_rtio_5Fsqe_5Fflags"></a>

相关声明：[RTIO提交队列事件标志（SQE Flags）](../rtio_model_reference/P010_RTIO提交事件标志.md)。

RTIO提交队列事件（SQE）标志。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_cqe_2Eh"></a>

```c
file cqe.h
```

相关声明：[cqe.h](../rtio_headers_reference/P003_RTIO完成事件头文件参考.md)。

RTIO完成队列事件（Completion Queue Events）及相关函数。

<a id="r_iodev_2Eh"></a>

```c
file iodev.h
```

相关声明：[iodev.h](../rtio_headers_reference/P005_RTIO设备头文件参考.md)。

RTIO输入输出设备（I/O Device）及相关函数。

<a id="r_regmap_2Eh"></a>

```c
file regmap.h
```

相关声明：[regmap.h](../rtio_work_reference/P001_RTIO寄存器映射头文件参考.md)。

通过RTIO读写设备寄存器列表（Device Register Lists）的辅助函数。

<a id="r_rtio_2Eh"></a>

```c
file rtio.h
```

相关声明：[rtio.h](P002_RTIO核心头文件参考.md)。

以较少工作量移动字节的实时输入输出（Real-Time I/O，RTIO）设备API。

<a id="r_sqe_2Eh"></a>

```c
file sqe.h
```

相关声明：[sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)。

RTIO提交队列事件（Submission Queue Events）及相关函数。

<a id="r_work_2Eh"></a>

```c
file work.h
```

相关声明：[work.h](../rtio_work_reference/P005_RTIO工作队列头文件参考.md)。

用于异步执行阻塞操作的RTIO工作队列（Work Queues）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

<a id="r_rtio_5Fcqe"></a>

```c
struct rtio_cqe
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

一个完成队列事件（Completion Queue Event）。

<a id="r_rtio_5Fiodev_5Fapi"></a>

```c
struct rtio_iodev_api
```

相关声明：[rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)。

RTIO输入输出设备应实现的API。

<a id="r_rtio_5Fiodev"></a>

```c
struct rtio_iodev
```

相关声明：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

具有请求提交函数表（Function Table）的输入输出设备。

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

<a id="r_rtio_5Fsqe"></a>

```c
struct rtio_sqe
```

相关声明：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

一个提交队列事件（Submission Queue Event）。

<a id="r_rtio_5Fiodev_5Fsqe"></a>

```c
struct rtio_iodev_sqe
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_gaae51e2a679d37bc1cfba79961688c406"></a>

```c
#define RTIO_IODEV_DEFINE(name, iodev_api, iodev_data)
```

相关声明：[RTIO_IODEV_DEFINE](#gaae51e2a679d37bc1cfba79961688c406)。

静态定义并初始化一个RTIO输入输出设备（IODev）。

<a id="r_ga338df088eabf3b8f7fefb4ac517b21d4"></a>

```c
#define RTIO_DEFINE(name, sq_sz, cq_sz)
```

相关声明：[RTIO_DEFINE](#ga338df088eabf3b8f7fefb4ac517b21d4)。

静态定义并初始化一个RTIO上下文（Context）。

<a id="r_ga2437af5061e078950d4a55211d9a902f"></a>

```c
#define RTIO_BMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_BMEM(rtio_partition) static), (static))
```

相关声明：[RTIO_BMEM](#ga2437af5061e078950d4a55211d9a902f)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)、[rtio_partition](#ga86a38086dd85150ab6e479d73db1c6d1)。

如果可用，分配到未初始化数据区（BSS）。

<a id="r_ga3b569c01b71e126cff852df50e98fd69"></a>

```c
#define RTIO_DMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_DMEM(rtio_partition) static), (static))
```

相关声明：[RTIO_DMEM](#ga3b569c01b71e126cff852df50e98fd69)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[K_APP_DMEM](../memory_domain_reference/P006_应用内存分区接口.md#gace571a7f6ee313a732976cc863b5d0e6)、[rtio_partition](#ga86a38086dd85150ab6e479d73db1c6d1)。

如果可用，分配为已初始化内存（Initialized Memory）。

<a id="r_gae4c2a9384a9ae4ed16dff914b1184ca8"></a>

```c
#define RTIO_DEFINE_WITH_MEMPOOL(name, sq_sz, cq_sz, num_blks, blk_size, balign)
```

相关声明：[RTIO_DEFINE_WITH_MEMPOOL](#gae4c2a9384a9ae4ed16dff914b1184ca8)。

静态定义并初始化一个RTIO上下文（Context）。

<a id="r_ga4575e199f9747909d4ec879a43a371e6"></a>

```c
#define RTIO_POOL_DEFINE(name, pool_sz, sq_sz, cq_sz)
```

相关声明：[RTIO_POOL_DEFINE](#ga4575e199f9747909d4ec879a43a371e6)。

静态定义并初始化一个RTIO上下文池（Context Pool）。

<a id="r_gad45b80544e4e894cf170fe44fb752930"></a>

```c
#define rtio_sqe_prep_delay(sqe, timeout, userdata)
```

相关声明：[rtio_sqe_prep_delay](#gad45b80544e4e894cf170fe44fb752930)。

准备一个延时操作（Delay Operation）提交，在指定超时后完成。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_ga6adaa4d7ef1fa8054000d8d9b8e634bd"></a>

```c
typedef void(* rtio_cqe_callback_t) (struct rtio *r, void *user_data)
```

相关声明：[rtio_cqe_callback_t](#ga6adaa4d7ef1fa8054000d8d9b8e634bd)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

RTIO完成队列事件回调（Completion Queue Event Callback）。

<a id="r_ga5d5b7d440eab064918424b0261455a9f"></a>

```c
typedef void(* rtio_callback_t) (struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0)
```

相关声明：[rtio_callback_t](#ga5d5b7d440eab064918424b0261455a9f)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

`RTIO_OP_CALLBACK`的回调函数签名（Callback Signature）。

<a id="r_gab254ffa4d10bfb670bacd1c47c1f8711"></a>

```c
typedef void(* rtio_signaled_t) (struct rtio_iodev_sqe *iodev_sqe, void *userdata)
```

相关声明：[rtio_signaled_t](#gab254ffa4d10bfb670bacd1c47c1f8711)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

`RTIO_OP_AWAIT`收到信号时的回调函数签名（Callback Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.6\_函数（Functions）

<a id="r_ga4213be028b0a1264daaa0d30c4c2d089"></a>

```c
static size_t rtio_mempool_block_size (const struct rtio *r)
```

相关声明：[rtio_mempool_block_size](#ga4213be028b0a1264daaa0d30c4c2d089)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

获取RTIO上下文的内存池块大小（Memory Pool Block Size）。

<a id="r_ga1f4fb7bccbaae08a94387e4b11275a78"></a>

```c
static uint32_t rtio_sqe_acquirable (struct rtio *r)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtio_sqe_acquirable](#ga1f4fb7bccbaae08a94387e4b11275a78)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

可获取的提交队列事件数。

<a id="r_ga8b47c954d15a334621def53acceb6799"></a>

```c
static struct rtio_sqe * rtio_sqe_acquire (struct rtio *r)
```

相关声明：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_sqe_acquire](#ga8b47c954d15a334621def53acceb6799)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，获取一个提交队列事件（SQE）。

<a id="r_gafb6e8c8679cb9483445c510cd6f14741"></a>

```c
static int rtio_sqe_acquire_array (struct rtio *r, size_t n, struct rtio_sqe **sqes)
```

相关声明：[rtio_sqe_acquire_array](#gafb6e8c8679cb9483445c510cd6f14741)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

如果可用，获取指定数量的提交队列事件（SQE）。

<a id="r_ga9486fb7b50e8d2409a50da235203536b"></a>

```c
static void rtio_sqe_drop_all (struct rtio *r)
```

相关声明：[rtio_sqe_drop_all](#ga9486fb7b50e8d2409a50da235203536b)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

丢弃先前获取的全部SQE。

<a id="r_gad848646651fdf3649b882e5268f72a3c"></a>

```c
static struct rtio_cqe * rtio_cqe_acquire (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_acquire](#gad848646651fdf3649b882e5268f72a3c)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，获取一个完成队列事件（CQE）。

<a id="r_gaabf5e6876e04f92f99a860591c7d310a"></a>

```c
static int rtio_set_cqe_callback (struct rtio *r, rtio_cqe_callback_t callback, void *user_data)
```

相关声明：[rtio_set_cqe_callback](#gaabf5e6876e04f92f99a860591c7d310a)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe_callback_t](#ga6adaa4d7ef1fa8054000d8d9b8e634bd)。

设置完成队列事件回调（CQE Callback）。

<a id="r_ga6f55202adeca60aed0343a7a0dcab071"></a>

```c
static void rtio_cqe_produce (struct rtio *r, struct rtio_cqe *cqe)
```

相关声明：[rtio_cqe_produce](#ga6f55202adeca60aed0343a7a0dcab071)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

如果可用，产生一个完成队列事件（CQE）。

<a id="r_gae562cf241911804cdb9f4e3a73b53df4"></a>

```c
static struct rtio_cqe * rtio_cqe_consume (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_consume](#gae562cf241911804cdb9f4e3a73b53df4)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

如果可用，从完成队列中取出一个完成队列事件（CQE）。

<a id="r_gaf617d05d9b59ce1f1d0697617ef6f249"></a>

```c
static struct rtio_cqe * rtio_cqe_consume_block (struct rtio *r)
```

相关声明：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[rtio_cqe_consume_block](#gaf617d05d9b59ce1f1d0697617ef6f249)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

等待并从完成队列中取出一个完成队列事件（CQE）。

<a id="r_gaa0799a5f8ad98425d385a07c5d27d9cb"></a>

```c
static void rtio_cqe_release (struct rtio *r, struct rtio_cqe *cqe)
```

相关声明：[rtio_cqe_release](#gaa0799a5f8ad98425d385a07c5d27d9cb)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

释放已取出的完成队列事件（CQE）。

<a id="r_ga98b8f272b175ff2c0e9f5ed420c3abcc"></a>

```c
static int rtio_flush_completion_queue (struct rtio *r)
```

相关声明：[rtio_flush_completion_queue](#ga98b8f272b175ff2c0e9f5ed420c3abcc)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

清空完成队列（Completion Queue）。

<a id="r_gae63ffc626a3e99406d36aa47f10b49e1"></a>

```c
void rtio_sqe_signal (struct rtio_sqe *sqe)
```

相关声明：[rtio_sqe_signal](#gae63ffc626a3e99406d36aa47f10b49e1)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

向一个等待操作SQE（AWAIT SQE）发送信号。

<a id="r_ga75661c8c6c94a0ac6254cec674b478c8"></a>

```c
static uint32_t rtio_cqe_compute_flags (struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtio_cqe_compute_flags](#ga75661c8c6c94a0ac6254cec674b478c8)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

根据`rtio_iodev_sqe`条目计算CQE标志。

<a id="r_gaedbf9386a36ed99baa290ef6c318ded1"></a>

```c
int rtio_cqe_get_mempool_buffer (const struct rtio *r, struct rtio_cqe *cqe, uint8_t **buff, uint32_t *buff_len)
```

相关声明：[rtio_cqe_get_mempool_buffer](#gaedbf9386a36ed99baa290ef6c318ded1)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得为该CQE分配的内存池缓冲区（Memory Pool Buffer）。

<a id="r_gacb1d2ffa2b07418d8a8aa319bd4336ab"></a>

```c
static void rtio_iodev_sqe_ok (struct rtio_iodev_sqe *iodev_sqe, int result)
```

相关声明：[rtio_iodev_sqe_ok](#gacb1d2ffa2b07418d8a8aa319bd4336ab)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通知执行器（Executor）：一次提交已成功完成。

<a id="r_gaada07aa6acefa548743b525225fa482f"></a>

```c
static void rtio_iodev_sqe_err (struct rtio_iodev_sqe *iodev_sqe, int result)
```

相关声明：[rtio_iodev_sqe_err](#gaada07aa6acefa548743b525225fa482f)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通知执行器（Executor）：一次提交已出错完成。

<a id="r_ga4abc221d5a90ab882000a72caa0ebd0f"></a>

```c
static void rtio_cqe_submit (struct rtio *r, int result, void *userdata, uint32_t flags)
```

相关声明：[rtio_cqe_submit](#ga4abc221d5a90ab882000a72caa0ebd0f)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

使用给定结果和用户数据（User Data）提交一个完成队列事件（CQE）。

<a id="r_gaab6843e2038d00a8354f57d7e2ffcf7e"></a>

```c
static int rtio_sqe_rx_buf (const struct rtio_iodev_sqe *iodev_sqe, uint32_t min_buf_len, uint32_t max_buf_len, uint8_t **buf, uint32_t *buf_len)
```

相关声明：[rtio_sqe_rx_buf](#gaab6843e2038d00a8354f57d7e2ffcf7e)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

获取与接收提交（RX Submission）关联的缓冲区。

<a id="r_ga6530bf56ccbab046a362a6448f941609"></a>

```c
void rtio_release_buffer (struct rtio *r, void *buff, uint32_t buff_len)
```

相关声明：[rtio_release_buffer](#ga6530bf56ccbab046a362a6448f941609)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

释放由RTIO内存池（Memory Pool）分配的内存。

<a id="r_ga9da42c98546930575525f0f92710f9e4"></a>

```c
static void rtio_access_grant (struct rtio *r, struct k_thread *t)
```

相关声明：[rtio_access_grant](#ga9da42c98546930575525f0f92710f9e4)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

授予用户线程（User Thread）访问RTIO上下文的权限。

<a id="r_ga9ab6490aa1893ae01bb0938a34c3e248"></a>

```c
static void rtio_access_revoke (struct rtio *r, struct k_thread *t)
```

相关声明：[rtio_access_revoke](#ga9ab6490aa1893ae01bb0938a34c3e248)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

撤销用户线程（User Thread）访问RTIO上下文的权限。

<a id="r_gac01252e55d2848b38c0ed77b71d600a7"></a>

```c
int rtio_sqe_cancel (struct rtio_sqe *sqe)
```

相关声明：[rtio_sqe_cancel](#gac01252e55d2848b38c0ed77b71d600a7)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

尝试取消一个SQE。

<a id="r_ga830863e6c8d9b96f4c473a038cab8f8c"></a>

```c
int rtio_sqe_copy_in_get_handles (struct rtio *r, const struct rtio_sqe *sqes, struct rtio_sqe **handle, size_t sqe_count)
```

相关声明：[rtio_sqe_copy_in_get_handles](#ga830863e6c8d9b96f4c473a038cab8f8c)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

将SQE数组复制到队列中，并取回生成的句柄（Handles）。

<a id="r_ga65e351af0a16dcf504a51ef4eb9316c7"></a>

```c
static int rtio_sqe_copy_in (struct rtio *r, const struct rtio_sqe *sqes, size_t sqe_count)
```

相关声明：[rtio_sqe_copy_in](#ga65e351af0a16dcf504a51ef4eb9316c7)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

将SQE数组复制到队列中。

<a id="r_ga98b2bbef95aea342a9b86a9775dd5c3b"></a>

```c
int rtio_cqe_copy_out (struct rtio *r, struct rtio_cqe *cqes, size_t cqe_count, k_timeout_t timeout)
```

相关声明：[rtio_cqe_copy_out](#ga98b2bbef95aea342a9b86a9775dd5c3b)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从队列中复制出CQE数组。

<a id="r_gafee27c64a4a4989c4eb774addde8eb2e"></a>

```c
int rtio_submit (struct rtio *r, uint32_t wait_count)
```

相关声明：[rtio_submit](#gafee27c64a4a4989c4eb774addde8eb2e)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

向底层执行器（Executor）提交I/O请求。

<a id="r_ga37c94f84cfce3810fd598040aba3841e"></a>

```c
struct rtio * rtio_pool_acquire (struct rtio_pool *pool)
```

相关声明：[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_pool_acquire](#ga37c94f84cfce3810fd598040aba3841e)、[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)。

从池中取得一个RTIO上下文（Context）。

<a id="r_ga05e24d59485f71cc0126d44abbe8cf2b"></a>

```c
void rtio_pool_release (struct rtio_pool *pool, struct rtio *r)
```

相关声明：[rtio_pool_release](#ga05e24d59485f71cc0126d44abbe8cf2b)、[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

将RTIO上下文（Context）归还到池中。

<a id="r_ga599ee43fdf35e1cf895cbbe9272e4c50"></a>

```c
static void rtio_sqe_prep_nop (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, void *userdata)
```

相关声明：[rtio_sqe_prep_nop](#ga599ee43fdf35e1cf895cbbe9272e4c50)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

准备一个空操作（No Operation，NOP）提交。

<a id="r_ga89c7cc2494e3dda50737f78f1a1376cf"></a>

```c
static void rtio_sqe_prep_read (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint8_t *buf, uint32_t len, void *userdata)
```

相关声明：[rtio_sqe_prep_read](#ga89c7cc2494e3dda50737f78f1a1376cf)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个读操作（Read Operation）提交。

<a id="r_ga15c1f623658d27d300d1a31a6f3d6b9d"></a>

```c
static void rtio_sqe_prep_read_with_pool (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_read_with_pool](#ga15c1f623658d27d300d1a31a6f3d6b9d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个使用上下文内存池的读操作提交。

<a id="r_ga9803aa829f8c0eeee746ea7d872c20cc"></a>

```c
static void rtio_sqe_prep_read_multishot (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_read_multishot](#ga9803aa829f8c0eeee746ea7d872c20cc)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个使用上下文内存池的多次完成读操作（Multishot Read）提交。

<a id="r_ga7f7856d1f4fd1d8c4f6eebcccfe77701"></a>

```c
static void rtio_sqe_prep_write (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *buf, uint32_t len, void *userdata)
```

相关声明：[rtio_sqe_prep_write](#ga7f7856d1f4fd1d8c4f6eebcccfe77701)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个写操作（Write Operation）提交。

<a id="r_ga31be14ece09e061a8d42ca8f2395286a"></a>

```c
static void rtio_sqe_prep_tiny_write (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tiny_write_data, uint8_t tiny_write_len, void *userdata)
```

相关声明：[rtio_sqe_prep_tiny_write](#ga31be14ece09e061a8d42ca8f2395286a)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

准备一个微量写操作（Tiny Write）提交。

<a id="r_ga9d0dd7d0e2e3d281092f2350d6e1713e"></a>

```c
static void rtio_sqe_prep_callback (struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

相关声明：[rtio_sqe_prep_callback](#ga9d0dd7d0e2e3d281092f2350d6e1713e)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_callback_t](#ga5d5b7d440eab064918424b0261455a9f)。

准备一个回调操作（Callback Operation）提交。

<a id="r_gae87be354087d038953dae07c7f9cd3b0"></a>

```c
static void rtio_sqe_prep_callback_no_cqe (struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

相关声明：[rtio_sqe_prep_callback_no_cqe](#gae87be354087d038953dae07c7f9cd3b0)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_callback_t](#ga5d5b7d440eab064918424b0261455a9f)。

准备一个不产生CQE的回调操作提交。

<a id="r_gab9b605dcbb01d21c88f9ae70588ea3b5"></a>

```c
static void rtio_sqe_prep_transceive (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tx_buf, uint8_t *rx_buf, uint32_t buf_len, void *userdata)
```

相关声明：[rtio_sqe_prep_transceive](#gab9b605dcbb01d21c88f9ae70588ea3b5)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个收发操作（Transceive Operation）提交。

<a id="r_gafd97c145b8525895494a31a87610f65d"></a>

```c
static void rtio_sqe_prep_await (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await](#gafd97c145b8525895494a31a87610f65d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作（Await Operation）提交。

<a id="r_ga5e55583901cd13d24f60744747c5c72b"></a>

```c
static void rtio_sqe_prep_await_iodev (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await_iodev](#ga5e55583901cd13d24f60744747c5c72b)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作提交，该操作会阻塞`rtio_iodev`直至完成。

<a id="r_gaa2f35d2909f4a19003199a3fd759fc41"></a>

```c
static void rtio_sqe_prep_await_executor (struct rtio_sqe *sqe, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await_executor](#gaa2f35d2909f4a19003199a3fd759fc41)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作提交，该操作在收到信号后完成SQE。

<a id="r_gabcb356e1df7b39bbb6f732d6fa6cc97d"></a>

```c
static void rtio_sqe_prep_i2c_configure (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint32_t dev_config, void *userdata)
```

相关声明：[rtio_sqe_prep_i2c_configure](#gabcb356e1df7b39bbb6f732d6fa6cc97d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个I2C配置操作（Configure Operation）提交。

<a id="r_ga274cb5490582b38682f255cac4703143"></a>

```c
static void rtio_sqe_prep_i2c_recover (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_i2c_recover](#ga274cb5490582b38682f255cac4703143)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个I2C总线恢复操作（Recover Operation）提交。

<a id="r_gaef904eb6a8810d8c3ea537c4d6edbee5"></a>

```c
static struct rtio_iodev_sqe * rtio_txn_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_txn_next](#gaef904eb6a8810d8c3ea537c4d6edbee5)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取事务（Transaction）中的下一个SQE。

<a id="r_gada1e3abf92a46e376138435debc8baf4"></a>

```c
static struct rtio_iodev_sqe * rtio_chain_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_chain_next](#gada1e3abf92a46e376138435debc8baf4)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取链（Chain）中的下一个SQE。

<a id="r_gae690e3dc0fc40dda57257b2eed432719"></a>

```c
static struct rtio_iodev_sqe * rtio_iodev_sqe_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_iodev_sqe_next](#gae690e3dc0fc40dda57257b2eed432719)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取链或事务中的下一个SQE。

<a id="r_ga7d2e5673582f32b630e2294dfbf0fe44"></a>

```c
static void rtio_iodev_sqe_await_signal (struct rtio_iodev_sqe *iodev_sqe, rtio_signaled_t callback, void *userdata)
```

相关声明：[rtio_iodev_sqe_await_signal](#ga7d2e5673582f32b630e2294dfbf0fe44)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_signaled_t](#gab254ffa4d10bfb670bacd1c47c1f8711)。

从RTIO IODEV等待一个AWAIT SQE信号。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 1.7\_变量（Variables）

<a id="r_ga86a38086dd85150ab6e479d73db1c6d1"></a>

```c
struct k_mem_partition rtio_partition
```

相关声明：[k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)、[rtio_partition](#ga86a38086dd85150ab6e479d73db1c6d1)。

与全部RTIO上下文信息关联的内存分区（Memory Partition）。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga2437af5061e078950d4a55211d9a902f"></a>

### `RTIO_BMEM`

```c
#define RTIO_BMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_BMEM(rtio_partition) static), (static))
```

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，分配到未初始化数据区（BSS）。

如果选择了`CONFIG_USERSPACE`，则分配到`rtio_partition`的BSS区。映射为：`K_APP_BMEM(rtio_partition) static`。

如果禁用了`CONFIG_USERSPACE`，则以普通`static`形式分配：`static`。

> 译注——源码核对：本次宏优先考虑DTCM和NOCACHE内存放置配置，只有默认分支才按CONFIG_USERSPACE选择K_APP_BMEM或普通static。原文描述保留，但不能把它视为所有配置下的完整展开。

<a id="ga338df088eabf3b8f7fefb4ac517b21d4"></a>

### `RTIO_DEFINE`

```c
#define RTIO_DEFINE ( name, sq_sz, cq_sz )
```

```c
#include <zephyr/rtio/rtio.h>
```

展开值（Value）：

```c
Z_RTIO_SQE_POOL_DEFINE(CONCAT(name, _sqe_pool), sq_sz);                 \
Z_RTIO_CQE_POOL_DEFINE(CONCAT(name, _cqe_pool), cq_sz);                 \
Z_RTIO_DEFINE(name, &CONCAT(name, _sqe_pool),                           \
              &CONCAT(name, _cqe_pool), NULL)
```

静态定义并初始化一个RTIO上下文（Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | RTIO的名称。 |
| `sq_sz` | 提交队列条目池（SQE Pool）的大小。 |
| `cq_sz` | 完成队列条目池（CQE Pool）的大小。 |

<a id="gae4c2a9384a9ae4ed16dff914b1184ca8"></a>

### `RTIO_DEFINE_WITH_MEMPOOL`

```c
#define RTIO_DEFINE_WITH_MEMPOOL ( name, sq_sz, cq_sz, num_blks, blk_size, balign )
```

```c
#include <zephyr/rtio/rtio.h>
```

展开值（Value）：

```c
Z_RTIO_SQE_POOL_DEFINE(name##_sqe_pool, sq_sz);         \
Z_RTIO_CQE_POOL_DEFINE(name##_cqe_pool, cq_sz);                 \
Z_RTIO_BLOCK_POOL_DEFINE(name##_block_pool, blk_size, num_blks, balign); \
Z_RTIO_DEFINE(name, &name##_sqe_pool, &name##_cqe_pool, &name##_block_pool)
```

静态定义并初始化一个RTIO上下文（Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | RTIO的名称。 |
| `sq_sz` | 提交队列的大小，必须是2的幂。 |
| `cq_sz` | 完成队列的大小，必须是2的幂。 |
| `num_blks` | 内存池中的块数。 |
| `blk_size` | 每块的字节数。 |
| `balign` | 块的对齐要求（Alignment）。 |

<a id="ga3b569c01b71e126cff852df50e98fd69"></a>

### `RTIO_DMEM`

```c
#define RTIO_DMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_DMEM(rtio_partition) static), (static))
```

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，分配为已初始化内存（Initialized Memory）。

如果选择了`CONFIG_USERSPACE`，则分配到`rtio_partition`的已初始化区。映射为：`K_APP_DMEM(rtio_partition) static`。

如果禁用了`CONFIG_USERSPACE`，则以普通`static`形式分配：`static`。

> 译注——源码核对：本次宏优先考虑DTCM和NOCACHE内存放置配置，默认分支才按CONFIG_USERSPACE选择K_APP_DMEM或普通static。

<a id="gaae51e2a679d37bc1cfba79961688c406"></a>

### `RTIO_IODEV_DEFINE`

```c
#define RTIO_IODEV_DEFINE ( name, iodev_api, iodev_data )
```

```c
#include <zephyr/rtio/iodev.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(rtio_iodev, name) = {           \
        .api = (iodev_api),                             \
        .data = (iodev_data),                           \
}
```

静态定义并初始化一个RTIO输入输出设备（IODev）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | IODEV的名称。 |
| `iodev_api` | 指向`struct rtio_iodev_api`的指针。 |
| `iodev_data` | 数据指针。 |

<a id="ga4575e199f9747909d4ec879a43a371e6"></a>

### `RTIO_POOL_DEFINE`

```c
#define RTIO_POOL_DEFINE ( name, pool_sz, sq_sz, cq_sz )
```

```c
#include <zephyr/rtio/rtio.h>
```

展开值（Value）：

```c
LISTIFY(pool_sz, Z_RTIO_POOL_DEFINE_N, (;), name, sq_sz, cq_sz);        \
static struct rtio *name##_contexts[] = {                               \
        LISTIFY(pool_sz, Z_RTIO_POOL_REF_N, (,), name)                  \
};                                                                      \
ATOMIC_DEFINE(name##_used, pool_sz);                                    \
STRUCT_SECTION_ITERABLE(rtio_pool, name) = {                            \
        .pool_size = pool_sz,                                           \
        .contexts = name##_contexts,                                    \
        .used = name##_used,                                            \
}
```

静态定义并初始化一个RTIO上下文池（Context Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | RTIO池的名称。 |
| `pool_sz` | 在池中分配的RTIO上下文数量。 |
| `sq_sz` | 每个上下文的提交队列条目池大小。 |
| `cq_sz` | 每个上下文的完成队列条目池大小。 |

<a id="gad45b80544e4e894cf170fe44fb752930"></a>

### `rtio_sqe_prep_delay`

```c
#define rtio_sqe_prep_delay ( sqe, timeout, userdata )
```

```c
#include <zephyr/rtio/sqe.h>
```

展开值（Value）：

```c
BUILD_ASSERT(false, "CONFIG_RTIO_OP_DELAY not enabled")
```

准备一个延时操作（Delay Operation）提交，在指定超时后完成。

此操作会以给定的超时值设置一个内核定时器（Kernel Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sqe` | 要准备的提交队列条目。 |
| `timeout` | 延时的`k_timeout_t`值，例如`K_MSEC(1)`。 |
| `userdata` | 用户提供的关联数据指针。 |

说明（Note）：此操作默认启用，但可以通过关闭`CONFIG_RTIO_OP_DELAY`来禁用。

> 译注——源码核对：本次Doxygen页面展示的是禁用CONFIG_RTIO_OP_DELAY时触发BUILD_ASSERT的宏分支；启用时同名入口是静态内联函数。原文称设置内核定时器（Kernel Timer）。本次sqe.h把操作交给共享rtio_timeout_iodev，rtio_timeout.c实际使用单个内核_timeout和按到期时间排序的列表，没有为每个SQE创建k_timer。延时从IODEV提交时计算，不从准备SQE时计算。

<a id="ga5d5b7d440eab064918424b0261455a9f"></a>

### `rtio_callback_t`

```c
typedef void(* rtio_callback_t) (struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0)
```

```c
#include <zephyr/rtio/sqe.h>
```

`RTIO_OP_CALLBACK`的回调函数签名（Callback Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | 回调所使用的RTIO上下文。 |
| `sqe` | 回调操作的提交。 |
| `res` | 前一个链接的提交的结果。 |
| `arg0` | SQE中携带的参数选项。 |

<a id="ga6adaa4d7ef1fa8054000d8d9b8e634bd"></a>

### `rtio_cqe_callback_t`

```c
typedef void(* rtio_cqe_callback_t) (struct rtio *r, void *user_data)
```

```c
#include <zephyr/rtio/rtio.h>
```

RTIO完成队列事件回调（Completion Queue Event Callback）。

如果已设置，每当新的完成队列事件提交到RTIO上下文时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | 该完成队列事件被提交到的RTIO上下文。 |
| `user_data` | 通过`rtio_set_cqe_callback`指定的用户数据。 |

<a id="gab254ffa4d10bfb670bacd1c47c1f8711"></a>

### `rtio_signaled_t`

```c
typedef void(* rtio_signaled_t) (struct rtio_iodev_sqe *iodev_sqe, void *userdata)
```

```c
#include <zephyr/rtio/sqe.h>
```

`RTIO_OP_AWAIT`收到信号时的回调函数签名（Callback Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 等待操作的IODEV提交。 |
| `userdata` | 用户数据（User Data）。 |

<a id="ga9da42c98546930575525f0f92710f9e4"></a>

### `rtio_access_grant()`

```c
void rtio_access_grant ( struct rtio * r, struct k_thread * t )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

授予用户线程（User Thread）访问RTIO上下文的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `t` | 要授予权限的线程。 |

<a id="ga9ab6490aa1893ae01bb0938a34c3e248"></a>

### `rtio_access_revoke()`

```c
void rtio_access_revoke ( struct rtio * r, struct k_thread * t )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

撤销用户线程（User Thread）访问RTIO上下文的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `t` | 要撤销权限的线程。 |

<a id="gada1e3abf92a46e376138435debc8baf4"></a>

### `rtio_chain_next()`

```c
struct rtio_iodev_sqe * rtio_chain_next ( const struct rtio_iodev_sqe * iodev_sqe)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

获取链（Chain）中的下一个SQE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 提交队列条目（Submission Queue Entry）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 当前SQE是链中的最后一个条目时。 |

返回（Returns）：如果存在可用条目，返回`struct rtio_sqe *`。

<a id="gad848646651fdf3649b882e5268f72a3c"></a>

### `rtio_cqe_acquire()`

```c
struct rtio_cqe * rtio_cqe_acquire ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，获取一个完成队列事件（CQE）。

<a id="ga75661c8c6c94a0ac6254cec674b478c8"></a>

### `rtio_cqe_compute_flags()`

```c
uint32_t rtio_cqe_compute_flags ( struct rtio_iodev_sqe * iodev_sqe)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

根据`rtio_iodev_sqe`条目计算CQE标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 所涉及的SQE条目。 |

返回（Returns）：应设置到CQE的`flags`字段中的值。

<a id="gae562cf241911804cdb9f4e3a73b53df4"></a>

### `rtio_cqe_consume()`

```c
struct rtio_cqe * rtio_cqe_consume ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，从完成队列中取出一个完成队列事件（CQE）。

如果返回了完成队列事件，则必须在后续某个时刻调用`rtio_cq_release(r)`，释放该CQE槽位，以供CQE生产者使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `cqe` | 从完成队列中取出的有效完成队列事件。 |
| `NULL` | 没有可用的完成队列事件。 |

> 译注——源码核对：原文写作`rtio_cq_release(r)`，本次公开声明与实现中的释放入口为`rtio_cqe_release(r, cqe)`；正文保留旧名称以便核对原文，实际代码应按当前声明传入上下文和CQE。

<a id="gaf617d05d9b59ce1f1d0697617ef6f249"></a>

### `rtio_cqe_consume_block()`

```c
struct rtio_cqe * rtio_cqe_consume_block ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

等待并从完成队列中取出一个完成队列事件（CQE）。

如果返回了完成队列事件，则必须在后续某个时刻调用`rtio_cq_release(r)`，释放该CQE槽位，以供CQE生产者使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `cqe` | 从完成队列中取出的有效完成队列事件。 |

> 译注——源码核对：原文写作`rtio_cq_release(r)`，当前入口为`rtio_cqe_release(r, cqe)`。阻塞消费没有超时参数，不代表所有已经提交的操作都已结束。

<a id="ga98b2bbef95aea342a9b86a9775dd5c3b"></a>

### `rtio_cqe_copy_out()`

```c
int rtio_cqe_copy_out ( struct rtio * r, struct rtio_cqe * cqes, size_t cqe_count, k_timeout_t timeout )
```

```c
#include <zephyr/rtio/rtio.h>
```

从队列中复制出CQE数组。

从RTIO上下文及其队列中复制出完成队列事件，在给定时限内等待收集请求数量的完成事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `cqes` | 指向SQE数组的指针。 |
| `cqe_count` | 数组中的SQE数量。 |
| `timeout` | 等待每个完成事件的超时。总等待时间最多可能达到`timeout*cqe_count`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `copy_count` | 复制出的CQE数量，范围为0至`cqe_count`。 |

> 译注——源码核对：原文参数说明误写为SQE数组及数量，函数声明实际是`struct rtio_cqe *cqes`和`cqe_count`。原文还将总超时描述为`timeout*cqe_count`，但本次实现只在循环前计算一次`end = sys_timepoint_calc(timeout)`，不会逐个事件重置截止点；K_FOREVER分支使用阻塞消费。实现采用do-while，也没有在入口对0数量提前返回，调用者应提供正数容量。

<a id="gaedbf9386a36ed99baa290ef6c318ded1"></a>

### `rtio_cqe_get_mempool_buffer()`

```c
int rtio_cqe_get_mempool_buffer ( const struct rtio * r, struct rtio_cqe * cqe, uint8_t ** buff, uint32_t * buff_len )
```

```c
#include <zephyr/rtio/rtio.h>
```

取得为该CQE分配的内存池缓冲区（Memory Pool Buffer）。

如果RTIO上下文包含内存池，而且该SQE由调用`rtio_sqe_read_with_pool()`创建，则可以用此函数取得与读操作关联的内存。处理结束后，应调用`rtio_release_buffer()`释放它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | RTIO上下文（Context）。 |
| `[in] cqe` | 处理该事件的CQE。 |
| `[out] buff` | 指向内存池缓冲区的指针。 |
| `[out] buff_len` | 所分配缓冲区的长度。 |

返回（Returns）：成功时为0；缓冲区不是为此CQE分配时为`-EINVAL`；禁用内存块支持时为`-ENOTSUP`。

> 译注——源码核对：原文的`rtio_sqe_read_with_pool()`是旧名称，本次公开辅助函数为`rtio_sqe_prep_read_with_pool()`。成功获取缓冲区信息不释放CQE或缓冲区；块数为0时实现返回NULL缓冲区及0长度。

<a id="ga6f55202adeca60aed0343a7a0dcab071"></a>

### `rtio_cqe_produce()`

```c
void rtio_cqe_produce ( struct rtio * r, struct rtio_cqe * cqe )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，产生一个完成队列事件（CQE）。

<a id="gaa0799a5f8ad98425d385a07c5d27d9cb"></a>

### `rtio_cqe_release()`

```c
void rtio_cqe_release ( struct rtio * r, struct rtio_cqe * cqe )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

释放已取出的完成队列事件（CQE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `cqe` | 完成队列条目（Completion Queue Entry）。 |

<a id="ga4abc221d5a90ab882000a72caa0ebd0f"></a>

### `rtio_cqe_submit()`

```c
void rtio_cqe_submit ( struct rtio * r, int result, void * userdata, uint32_t flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

使用给定结果和用户数据（User Data）提交一个完成队列事件（CQE）。

由执行器调用以产生完成队列事件；内部不执行加锁操作，因此多个调用者同时调用是不安全的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `result` | 整数结果码，可能为`-errno`。 |
| `userdata` | 随完成事件传递的用户数据。 |
| `flags` | 用于CEQ的标志，参见`RTIO_CQE_FLAG_*`。 |

> 译注——源码核对：原文参数说明中的CEQ为原拼写，此处对应CQE标志。CQE对象不足时丢弃事件并增加xcqcnt，但完成计数仍递增；不能把submit等待结束等同于结果已保存到完成队列。

<a id="ga98b8f272b175ff2c0e9f5ed420c3abcc"></a>

### `rtio_flush_completion_queue()`

```c
int rtio_flush_completion_queue ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

清空完成队列（Completion Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 排队的操作完成且没有错误时。 |
| `<0` | 发生错误时。 |

返回（Returns）：操作完成结果。

<a id="ga7d2e5673582f32b630e2294dfbf0fe44"></a>

### `rtio_iodev_sqe_await_signal()`

```c
void rtio_iodev_sqe_await_signal ( struct rtio_iodev_sqe * iodev_sqe, rtio_signaled_t callback, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

从RTIO IODEV等待一个AWAIT SQE信号。

如果SQE已经收到信号，则立即调用回调；否则在AWAIT SQE收到信号时调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] iodev_sqe` | 要等待其收到信号的IODEV SQE。 |
| `[in] callback` | SQE收到信号时调用的回调。 |
| `[in] userdata` | 传给回调的用户数据。 |

<a id="gaada07aa6acefa548743b525225fa482f"></a>

### `rtio_iodev_sqe_err()`

```c
void rtio_iodev_sqe_err ( struct rtio_iodev_sqe * iodev_sqe, int result )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

通知执行器（Executor）：一次提交已出错完成。

此操作必须使链中剩余的提交失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 失败的提交。 |
| `result` | 请求的结果。 |

<a id="gae690e3dc0fc40dda57257b2eed432719"></a>

### `rtio_iodev_sqe_next()`

```c
struct rtio_iodev_sqe * rtio_iodev_sqe_next ( const struct rtio_iodev_sqe * iodev_sqe)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

获取链或事务中的下一个SQE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 提交队列条目（Submission Queue Entry）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 当前SQE是链中的最后一个条目时。 |

返回（Returns）：如果存在可用条目，返回`struct rtio_iodev_sqe *`。

<a id="gacb1d2ffa2b07418d8a8aa319bd4336ab"></a>

### `rtio_iodev_sqe_ok()`

```c
void rtio_iodev_sqe_ok ( struct rtio_iodev_sqe * iodev_sqe, int result )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

通知执行器（Executor）：一次提交已成功完成。

如果存在下一个异步请求，此操作可能启动它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 成功的IODev提交。 |
| `result` | 请求的结果。 |

<a id="ga4213be028b0a1264daaa0d30c4c2d089"></a>

### `rtio_mempool_block_size()`

```c
size_t rtio_mempool_block_size ( const struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

获取RTIO上下文的内存池块大小（Memory Pool Block Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | RTIO上下文。 |

返回（Returns）：上下文内存池中每块的大小；上下文没有内存池时返回0。

<a id="ga37c94f84cfce3810fd598040aba3841e"></a>

### `rtio_pool_acquire()`

```c
struct rtio * rtio_pool_acquire ( struct rtio_pool * pool)
```

```c
#include <zephyr/rtio/rtio.h>
```

从池中取得一个RTIO上下文（Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要从中获取上下文的RTIO池。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 没有可用的上下文。 |
| `r` | 有效的上下文，已向调用线程授予相应权限。 |

<a id="ga05e24d59485f71cc0126d44abbe8cf2b"></a>

### `rtio_pool_release()`

```c
void rtio_pool_release ( struct rtio_pool * pool, struct rtio * r )
```

```c
#include <zephyr/rtio/rtio.h>
```

将RTIO上下文（Context）归还到池中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要将上下文归还到的RTIO池。 |
| `r` | 要归还到池中的RTIO上下文。 |

<a id="ga6530bf56ccbab046a362a6448f941609"></a>

### `rtio_release_buffer()`

```c
void rtio_release_buffer ( struct rtio * r, void * buff, uint32_t buff_len )
```

```c
#include <zephyr/rtio/rtio.h>
```

释放由RTIO内存池（Memory Pool）分配的内存。

如果RTIO上下文由调用`RTIO_DEFINE_WITH_MEMPOOL()`创建，则CQE数据可能包含一个由该RTIO上下文拥有的缓冲区。在这种情况下，如果读请求通过`rtio_sqe_read_with_pool()`配置，则必须将该缓冲区归还到池中。

处理结束时调用此函数。此函数会验证内存确实属于该RTIO上下文，并忽略无效参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `buff` | 指向待释放缓冲区的指针。 |
| `buff_len` | 要释放的字节数，将向上取整到最接近的内存块大小倍数。 |

> 译注——源码核对：原文的`rtio_sqe_read_with_pool()`对应当前`rtio_sqe_prep_read_with_pool()`。本次释放入口只先排除空上下文、空指针、空块池或0长度，再调用块池释放；长度在内部按右移计算块数，与原文“向上取整”不一致，实际应保留并传回分配长度。

<a id="gaabf5e6876e04f92f99a860591c7d310a"></a>

### `rtio_set_cqe_callback()`

```c
int rtio_set_cqe_callback ( struct rtio * r, rtio_cqe_callback_t callback, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

设置完成队列事件回调（CQE Callback）。

每当产生新的完成队列事件时，都会调用该回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `callback` | 要设置的回调。 |
| `user_data` | 传给回调的用户数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功设置回调。 |
| `-ENOTSUP` | 不支持CQE回调。 |

**警告（Warning）**：警告（Warning）：只有在没有SQE正在执行时，才能安全设置回调。

说明（Note）：将回调设为`NULL`即可禁用它。

<a id="ga1f4fb7bccbaae08a94387e4b11275a78"></a>

### `rtio_sqe_acquirable()`

```c
uint32_t rtio_sqe_acquirable ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

可获取的提交队列事件数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

返回（Returns）：可获取的提交队列事件数。

<a id="ga8b47c954d15a334621def53acceb6799"></a>

### `rtio_sqe_acquire()`

```c
struct rtio_sqe * rtio_sqe_acquire ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，获取一个提交队列事件（SQE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `sqe` | 从提交队列获取的有效提交队列事件。 |
| `NULL` | 没有可用的提交队列事件。 |

<a id="gafb6e8c8679cb9483445c510cd6f14741"></a>

### `rtio_sqe_acquire_array()`

```c
int rtio_sqe_acquire_array ( struct rtio * r, size_t n, struct rtio_sqe ** sqes )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

如果可用，获取指定数量的提交队列事件（SQE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `n` | 要获取的提交队列事件数量。 |
| `sqes` | 指向一个长度为`n`的`rtio_sqe`结构体指针数组的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 内存不足。 |

**警告（Warning）**：警告（Warning）：如果返回值为`-ENOMEM`，则SQE数组处于未定义状态。

<a id="gac01252e55d2848b38c0ed77b71d600a7"></a>

### `rtio_sqe_cancel()`

```c
int rtio_sqe_cancel ( struct rtio_sqe * sqe)
```

```c
#include <zephyr/rtio/rtio.h>
```

尝试取消一个SQE。

如果可能，即当前尚未执行，则取消SQE，并产生结果为`-ECANCELED`的失败事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sqe` | 要取消的SQE。 |

返回（Returns）：SQE被标记为取消时返回0；出错时返回小于0的值。

<a id="ga65e351af0a16dcf504a51ef4eb9316c7"></a>

### `rtio_sqe_copy_in()`

```c
int rtio_sqe_copy_in ( struct rtio * r, const struct rtio_sqe * sqes, size_t sqe_count )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

将SQE数组复制到队列中。

适用于一批提交存储在只读存储器（ROM）中，或RTIO用于必须复制数据的用户模式（User Mode）的情况。

不进行部分复制，因为链接的SQE必须作为完整集合提交。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `sqes` | 指向SQE数组的指针。 |
| `sqe_count` | 数组中的SQE数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 队列中没有足够空间。 |

<a id="ga830863e6c8d9b96f4c473a038cab8f8c"></a>

### `rtio_sqe_copy_in_get_handles()`

```c
int rtio_sqe_copy_in_get_handles ( struct rtio * r, const struct rtio_sqe * sqes, struct rtio_sqe ** handle, size_t sqe_count )
```

```c
#include <zephyr/rtio/rtio.h>
```

将SQE数组复制到队列中，并取回生成的句柄（Handles）。

将一个或多个SQE复制到RTIO上下文中，并可选地返回其生成的SQE句柄。可以通过`rtio_sqe_cancel()`使用句柄取消事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | RTIO上下文（Context）。 |
| `[in] sqes` | 指向SQE数组的指针。 |
| `[out] handle` | 可选的`rtio_sqe`指针的指针，用于保存第一个生成的SQE的句柄；使用`NULL`可忽略此输出。 |
| `[in] sqe_count` | 数组中的SQE数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 队列中没有足够空间。 |

> 译注——源码核对：尽管名称使用handles复数，输出参数只保存第一个生成的SQE句柄；实现复制SQE结构体，不深复制其指针指向的数据缓冲区。空间预检不提供跨并发调用的资源预留。

<a id="ga9486fb7b50e8d2409a50da235203536b"></a>

### `rtio_sqe_drop_all()`

```c
void rtio_sqe_drop_all ( struct rtio * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

丢弃先前获取的全部SQE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |

<a id="gafd97c145b8525895494a31a87610f65d"></a>

### `rtio_sqe_prep_await()`

```c
void rtio_sqe_prep_await ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个等待操作（Await Operation）提交。

等待操作会等待完成信号，然后SQE才完成。

如果提供了`rtio_iodev`，它将在等待期间被阻塞。这有助于以低延迟继续RTIO序列，可以理解为总线操作期间的一种“临界区”（Critical Section）。注意，等待期间正确阻塞的责任在于`rtio_iodev`驱动。

参见辅助函数`rtio_sqe_prep_await_iodev`，它会阻塞一个`rtio_iodev`；另见辅助函数`rtio_sqe_prep_await_executor`，它不会阻塞任何`rtio_iodev`。

> 译注——源码核对：本次准备函数将await.ok初始化为0；等待注册回调后以CAS将其变为1，发送信号也执行0→1的CAS，后到的一方在CAS失败后调用回调。这是单次等待与信号的交会机制，不是任意次数信号的计数器；重复发信号与已回收SQE不在安全使用前提内。

<a id="gaa2f35d2909f4a19003199a3fd759fc41"></a>

### `rtio_sqe_prep_await_executor()`

```c
void rtio_sqe_prep_await_executor ( struct rtio_sqe * sqe, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个等待操作提交，该操作在收到信号后完成SQE。

如果等待操作只是序列中的逻辑环节，完成后没有低延迟继续序列的要求，或预计等待操作需要“较长时间”才能完成，此变体可能有用。

详情见`rtio_sqe_prep_await`。另见对应的`rtio_sqe_prep_await_iodev`，后者会阻塞一个`rtio_iodev`。

<a id="ga5e55583901cd13d24f60744747c5c72b"></a>

### `rtio_sqe_prep_await_iodev()`

```c
void rtio_sqe_prep_await_iodev ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个等待操作提交，该操作会阻塞`rtio_iodev`直至完成。

如果等待操作属于必须在严格时间窗口内运行的序列，此变体可能有用，因为它实际上会在等待完成期间保持底层总线锁定。注意，等待期间正确阻塞的责任在于`rtio_iodev`驱动。

详情见`rtio_sqe_prep_await`。另见对应的`rtio_sqe_prep_await_executor`，后者不会阻塞任何`rtio_iodev`。

<a id="ga9d0dd7d0e2e3d281092f2350d6e1713e"></a>

### `rtio_sqe_prep_callback()`

```c
void rtio_sqe_prep_callback ( struct rtio_sqe * sqe, rtio_callback_t callback, void * arg0, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个回调操作（Callback Operation）提交。

这是一种比较特殊的操作，只能在内核模式（Kernel Mode）下执行。

当I/O操作队列需要通用逻辑来进行转换或逻辑处理时使用。

<a id="gae87be354087d038953dae07c7f9cd3b0"></a>

### `rtio_sqe_prep_callback_no_cqe()`

```c
void rtio_sqe_prep_callback_no_cqe ( struct rtio_sqe * sqe, rtio_callback_t callback, void * arg0, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个不产生CQE的回调操作提交。

类似于`rtio_sqe_prep_callback`，但会在SQE中设置`RTIO_SQE_NO_RESPONSE`标志，避免完成时产生CQE。

当回调是序列中的最后一个操作，负责清理先前所有CQE时，这可能有用。如果不设置`RTIO_SQE_NO_RESPONSE`，回调操作本身的完成还会产生一个CQE，而该CQE无法在这个回调中被取出。

<a id="gabcb356e1df7b39bbb6f732d6fa6cc97d"></a>

### `rtio_sqe_prep_i2c_configure()`

```c
void rtio_sqe_prep_i2c_configure ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, uint32_t dev_config, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个I2C配置操作（Configure Operation）提交。

<a id="ga274cb5490582b38682f255cac4703143"></a>

### `rtio_sqe_prep_i2c_recover()`

```c
void rtio_sqe_prep_i2c_recover ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个I2C总线恢复操作（Recover Operation）提交。

<a id="ga599ee43fdf35e1cf895cbbe9272e4c50"></a>

### `rtio_sqe_prep_nop()`

```c
void rtio_sqe_prep_nop ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个空操作（No Operation，NOP）提交。

<a id="ga89c7cc2494e3dda50737f78f1a1376cf"></a>

### `rtio_sqe_prep_read()`

```c
void rtio_sqe_prep_read ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, uint8_t * buf, uint32_t len, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个读操作（Read Operation）提交。

<a id="ga9803aa829f8c0eeee746ea7d872c20cc"></a>

### `rtio_sqe_prep_read_multishot()`

```c
void rtio_sqe_prep_read_multishot ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个使用上下文内存池的多次完成读操作（Multishot Read）提交。

此提交会持续产生完成事件，直到被取消。

另见（See Also）：`rtio_sqe_prep_read_with_pool()`。

<a id="ga15c1f623658d27d300d1a31a6f3d6b9d"></a>

### `rtio_sqe_prep_read_with_pool()`

```c
void rtio_sqe_prep_read_with_pool ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个使用上下文内存池的读操作提交。

另见（See Also）：`rtio_sqe_prep_read()`。

<a id="ga31be14ece09e061a8d42ca8f2395286a"></a>

### `rtio_sqe_prep_tiny_write()`

```c
void rtio_sqe_prep_tiny_write ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, const uint8_t * tiny_write_data, uint8_t tiny_write_len, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个微量写操作（Tiny Write）提交。

普通写操作要求源缓冲区在调用返回后继续保持有效；微量写操作则将数据复制到SQE中。数据必须足够小，才能放入规定大小的`rtio_sqe`。

在许多涉及寄存器传输级（Register-Transfer Level，RTL）逻辑的场景中，需要先写入后续要读取的寄存器地址，此操作在这些场景中很有用。

<a id="gab9b605dcbb01d21c88f9ae70588ea3b5"></a>

### `rtio_sqe_prep_transceive()`

```c
void rtio_sqe_prep_transceive ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, const uint8_t * tx_buf, uint8_t * rx_buf, uint32_t buf_len, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个收发操作（Transceive Operation）提交。

<a id="ga7f7856d1f4fd1d8c4f6eebcccfe77701"></a>

### `rtio_sqe_prep_write()`

```c
void rtio_sqe_prep_write ( struct rtio_sqe * sqe, const struct rtio_iodev * iodev, int8_t prio, const uint8_t * buf, uint32_t len, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

准备一个写操作（Write Operation）提交。

<a id="gaab6843e2038d00a8354f57d7e2ffcf7e"></a>

### `rtio_sqe_rx_buf()`

```c
int rtio_sqe_rx_buf ( const struct rtio_iodev_sqe * iodev_sqe, uint32_t min_buf_len, uint32_t max_buf_len, uint8_t ** buf, uint32_t * buf_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/rtio.h>
```

获取与接收提交（RX Submission）关联的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] iodev_sqe` | 要检查的提交。 |
| `[in] min_buf_len` | 操作需要的最少字节数。 |
| `[in] max_buf_len` | 操作需要的最多字节数。 |
| `[out] buf` | 用于保存缓冲区指针的位置。 |
| `[out] buf_len` | 用于保存缓冲区大小的位置。 |

返回（Returns）：成功填充`buf`和`buf_len`时返回0；内存不足以满足`min_buf_len`时返回`-ENOMEM`。

<a id="gae63ffc626a3e99406d36aa47f10b49e1"></a>

### `rtio_sqe_signal()`

```c
void rtio_sqe_signal ( struct rtio_sqe * sqe)
```

```c
#include <zephyr/rtio/rtio.h>
```

向一个等待操作SQE（AWAIT SQE）发送信号。

如果SQE当前正在阻塞执行，则解除阻塞；如果SQE当前没有阻塞执行，则跳过该SQE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sqe` | 要发送信号的SQE。 |

说明（Note）：如果要等到AWAIT SQE阻塞执行，可在该等待SQE之前链接一个NOP或回调SQE。

<a id="gafee27c64a4a4989c4eb774addde8eb2e"></a>

### `rtio_submit()`

```c
int rtio_submit ( struct rtio * r, uint32_t wait_count )
```

```c
#include <zephyr/rtio/rtio.h>
```

向底层执行器（Executor）提交I/O请求。

将提交队列事件队列提交给执行器（Executor）。执行器负责管理代表各条提交链的任务，完成后释放提交队列事件，并在提交完成时产生完成队列事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `wait_count` | 要等待其完成的提交数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

**警告（Warning）**：警告（Warning）：重入调用提交函数属于未定义行为（Undefined Behavior）。

<a id="gaef904eb6a8810d8c3ea537c4d6edbee5"></a>

### `rtio_txn_next()`

```c
struct rtio_iodev_sqe * rtio_txn_next ( const struct rtio_iodev_sqe * iodev_sqe)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/rtio/sqe.h>
```

获取事务（Transaction）中的下一个SQE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 提交队列条目（Submission Queue Entry）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 当前SQE是事务中的最后一个条目时。 |

返回（Returns）：如果存在可用条目，返回`struct rtio_sqe *`。

<a id="ga86a38086dd85150ab6e479d73db1c6d1"></a>

### `rtio_partition`

```c
struct k_mem_partition rtio_partition
```

声明属性：`extern`。

```c
#include <zephyr/rtio/rtio.h>
```

与全部RTIO上下文信息关联的内存分区（Memory Partition）。

## 1.9\_源码定位与版本边界

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

## 1.10\_原页交叉引用（Cross References）

- [RTIO完成队列事件标志（CQE Flags）](../rtio_model_reference/P008_RTIO完成事件标志.md)
- [RTIO I2C输入输出设备标志（IODEV Flags）](../hardware/P442_RTIO的I2C标志.md)
- [RTIO I3C输入输出设备标志（IODEV Flags）](../hardware/P434_RTIO的I3C标志.md)
- [RTIO Operation Codes](../rtio_model_reference/P009_RTIO操作码.md)
- [RTIO优先级（Priorities）](../rtio_model_reference/P011_RTIO优先级.md)
- [RTIO提交队列事件标志（SQE Flags）](../rtio_model_reference/P010_RTIO提交事件标志.md)
- [cqe.h](../rtio_headers_reference/P003_RTIO完成事件头文件参考.md)
- [iodev.h](../rtio_headers_reference/P005_RTIO设备头文件参考.md)
- [regmap.h](../rtio_work_reference/P001_RTIO寄存器映射头文件参考.md)
- [rtio.h](P002_RTIO核心头文件参考.md)
- [sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)
- [work.h](../rtio_work_reference/P005_RTIO工作队列头文件参考.md)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)
- [K_APP_DMEM](../memory_domain_reference/P006_应用内存分区接口.md#gace571a7f6ee313a732976cc863b5d0e6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)
- [CONCAT](../util_reference/P001_通用工具公共接口.md#ga770b921e59b3151931ee939a1ecf450e)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [LISTIFY](../util_reference/P001_通用工具公共接口.md#ga81cbc0233cf73048d65b76f716653af6)
- [K_MSEC(1)](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)
- [RTIO_SQE_NO_RESPONSE](../rtio_model_reference/P010_RTIO提交事件标志.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga770b921e59b3151931ee939a1ecf450e"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructrtio__iodev_html"></a>
<a id="agroup__sys-util_html_ga81cbc0233cf73048d65b76f716653af6"></a>
<a id="astructrtio__pool_html"></a>
<a id="astructrtio_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_RTIO核心头文件参考.md)
