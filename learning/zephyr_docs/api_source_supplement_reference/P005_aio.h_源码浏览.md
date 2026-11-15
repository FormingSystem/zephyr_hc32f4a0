---
id: learning.zephyr-docs.api-source-supplement-reference.page-5
title: aio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/aio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_aio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/aio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/aio_8h.html)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="foldopen00020"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="asignal_8h_html"></a>
<a id="astructaiocb_html"></a>
<a id="astructaiocb_html_a1e74b350a9ca189fa7c25b61c5cede6c"></a>
<a id="astructaiocb_html_a60a966202034e1abde4ca3ea0965fa30"></a>
<a id="astructaiocb_html_a6b4f8a1d05ed5444784389734d71cda7"></a>
<a id="astructaiocb_html_a7065f3086beb9cdffc525c1d09949268"></a>
<a id="astructaiocb_html_a7a8f63c080c8602ebcacbb86e9f5547e"></a>
<a id="astructaiocb_html_a8a23597de7bfc422b58ec9816ced7d47"></a>
<a id="astructaiocb_html_ad6b6e95e6e4a79487f7e6edaae26003f"></a>
<a id="astructsigevent_html"></a>
<a id="astructtimespec_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright 2024 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_AIO_H_
#define ZEPHYR_INCLUDE_POSIX_AIO_H_

#include <signal.h>
#include <sys/types.h>
#include <time.h>

#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

struct aiocb {
        int aio_fildes;
        off_t aio_offset;
        volatile void *aio_buf;
        size_t aio_nbytes;
        int aio_reqprio;
        struct sigevent aio_sigevent;
        int aio_lio_opcode;
};

#if _POSIX_C_SOURCE >= 200112L

int aio_cancel(int fildes, struct aiocb *aiocbp);
int aio_error(const struct aiocb *aiocbp);
int aio_fsync(int filedes, struct aiocb *aiocbp);
int aio_read(struct aiocb *aiocbp);
ssize_t aio_return(struct aiocb *aiocbp);
int aio_suspend(const struct aiocb *const list[], int nent, const struct timespec *timeout);
int aio_write(struct aiocb *aiocbp);
int lio_listio(int mode, struct aiocb *const ZRESTRICT list[], int nent,
               struct sigevent *ZRESTRICT sig);

#endif /* _POSIX_C_SOURCE >= 200112L */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_AIO_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

条件编译表达式：`_POSIX_C_SOURCE >= 200112L`。

### 注释 3：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_AIO_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/aio_8h.html)
- [signal.h](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [aiocb](../driver_model_reference/P007_异步IO控制块.md)
- [aio_fildes](../driver_model_reference/P007_异步IO控制块.md#ad6b6e95e6e4a79487f7e6edaae26003f)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [aio_offset](../driver_model_reference/P007_异步IO控制块.md#a1e74b350a9ca189fa7c25b61c5cede6c)
- [aio_buf](../driver_model_reference/P007_异步IO控制块.md#a60a966202034e1abde4ca3ea0965fa30)
- [aio_nbytes](../driver_model_reference/P007_异步IO控制块.md#a6b4f8a1d05ed5444784389734d71cda7)
- [aio_reqprio](../driver_model_reference/P007_异步IO控制块.md#a7a8f63c080c8602ebcacbb86e9f5547e)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)
- [aio_sigevent](../driver_model_reference/P007_异步IO控制块.md#a7065f3086beb9cdffc525c1d09949268)
- [aio_lio_opcode](../driver_model_reference/P007_异步IO控制块.md#a8a23597de7bfc422b58ec9816ced7d47)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [aiocb::aio_offset](../driver_model_reference/P007_异步IO控制块.md#a1e74b350a9ca189fa7c25b61c5cede6c)
- [aiocb::aio_buf](../driver_model_reference/P007_异步IO控制块.md#a60a966202034e1abde4ca3ea0965fa30)
- [aiocb::aio_nbytes](../driver_model_reference/P007_异步IO控制块.md#a6b4f8a1d05ed5444784389734d71cda7)
- [aiocb::aio_sigevent](../driver_model_reference/P007_异步IO控制块.md#a7065f3086beb9cdffc525c1d09949268)
- [aiocb::aio_reqprio](../driver_model_reference/P007_异步IO控制块.md#a7a8f63c080c8602ebcacbb86e9f5547e)
- [aiocb::aio_lio_opcode](../driver_model_reference/P007_异步IO控制块.md#a8a23597de7bfc422b58ec9816ced7d47)
- [aiocb::aio_fildes](../driver_model_reference/P007_异步IO控制块.md#ad6b6e95e6e4a79487f7e6edaae26003f)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P004_aead.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_ambiq-apollo2-pinctrl.h_源码浏览.md)
