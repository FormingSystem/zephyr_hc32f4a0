---
id: learning.zephyr-docs.api-source-reference.page-538
title: tty.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第538章\_tty.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h.html)。

## 538.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00022"></a>
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
<a id="foldopen00032"></a>
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
<a id="aarch__interface_8h_html_a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>
<a id="aatomic_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2backend_2tty_8h_html_a507f79d94144e3e4a75ec7fed1501f80"></a>
<a id="apipe_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructmodem__backend__tty__config_html"></a>
<a id="astructmodem__backend__tty__config_html_a139e7e96f3b021f560fa5ef8aa4d9e9f"></a>
<a id="astructmodem__backend__tty__config_html_a74cb7ee08a116261b19d834000db5242"></a>
<a id="astructmodem__backend__tty__config_html_ae8dd6da28163e6f97549e13e750d939d"></a>
<a id="astructmodem__backend__tty_html"></a>
<a id="astructmodem__backend__tty_html_a23afe812c5951bfa41251610056aa3aa"></a>
<a id="astructmodem__backend__tty_html_a2ea8d323973de8423f558a7a2e6b8984"></a>
<a id="astructmodem__backend__tty_html_a7f85f1f41fbcdf69ad1846a3af1b0b1e"></a>
<a id="astructmodem__backend__tty_html_abe654bb7b24f23417e60bc8af7b73d36"></a>
<a id="astructmodem__backend__tty_html_abf93189b2640afa8bad440089bb1a863"></a>
<a id="astructmodem__backend__tty_html_ad454321f08f334b028bb63cbb0d8e8f6"></a>
<a id="astructmodem__backend__tty_html_af6a76d369957f01f9d44c7f4bba67642"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/modem/pipe.h>

#ifndef ZEPHYR_INCLUDE_MODEM_BACKEND_TTY_H_
#define ZEPHYR_INCLUDE_MODEM_BACKEND_TTY_H_

#ifdef __cplusplus
extern "C" {
#endif

struct modem_backend_tty {
        const char *tty_path;
        int tty_fd;
        struct modem_pipe pipe;
        struct k_thread thread;
        k_thread_stack_t *stack;
        size_t stack_size;
        atomic_t state;
};

struct modem_backend_tty_config {
        const char *tty_path;
        k_thread_stack_t *stack;
        size_t stack_size;
};

struct modem_pipe *modem_backend_tty_init(struct modem_backend_tty *backend,
                                          const struct modem_backend_tty_config *config);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_BACKEND_TTY_H_ */
```

## 538.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_BACKEND_TTY_H_`。

## 538.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [modem_backend_tty](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md)
- [tty_path](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#af6a76d369957f01f9d44c7f4bba67642)
- [tty_fd](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#abf93189b2640afa8bad440089bb1a863)
- [pipe](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#abe654bb7b24f23417e60bc8af7b73d36)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [thread](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#ad454321f08f334b028bb63cbb0d8e8f6)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [stack](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a23afe812c5951bfa41251610056aa3aa)
- [stack_size](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a2ea8d323973de8423f558a7a2e6b8984)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a7f85f1f41fbcdf69ad1846a3af1b0b1e)
- [modem_backend_tty_config](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md)
- [tty_path](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#a139e7e96f3b021f560fa5ef8aa4d9e9f)
- [stack](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#ae8dd6da28163e6f97549e13e750d939d)
- [stack_size](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#a74cb7ee08a116261b19d834000db5242)
- [modem_backend_tty_init](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h.html#a507f79d94144e3e4a75ec7fed1501f80)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [modem_backend_tty_config::tty_path](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#a139e7e96f3b021f560fa5ef8aa4d9e9f)
- [modem_backend_tty_config::stack_size](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#a74cb7ee08a116261b19d834000db5242)
- [modem_backend_tty_config::stack](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md#ae8dd6da28163e6f97549e13e750d939d)
- [modem_backend_tty::stack](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a23afe812c5951bfa41251610056aa3aa)
- [modem_backend_tty::stack_size](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a2ea8d323973de8423f558a7a2e6b8984)
- [modem_backend_tty::state](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#a7f85f1f41fbcdf69ad1846a3af1b0b1e)
- [modem_backend_tty::pipe](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#abe654bb7b24f23417e60bc8af7b73d36)
- [modem_backend_tty::tty_fd](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#abf93189b2640afa8bad440089bb1a863)
- [modem_backend_tty::thread](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#ad454321f08f334b028bb63cbb0d8e8f6)
- [modem_backend_tty::tty_path](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md#af6a76d369957f01f9d44c7f4bba67642)

---

[上一章](P537_mmc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P539_stats.h_源码浏览.md)
