---
id: learning.zephyr-docs.api-source-supplement-reference.page-119
title: mqueue.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_mqueue.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html)。

## 119.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="foldopen00024"></a>
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
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="afcntl_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amqueue_8h_html_a3fbd3906296be63451c64d69be2bc371"></a>
<a id="amqueue_8h_html_a5a55ce03d8466a53a36601aaca9ee328"></a>
<a id="amqueue_8h_html_a5eadbb82e0b9702d77f384a27827b334"></a>
<a id="amqueue_8h_html_a6e6c4881ac0fd3ad18d733b96d088b8b"></a>
<a id="amqueue_8h_html_a83b7aa93cb6f1f5a4fd938baea5579a6"></a>
<a id="amqueue_8h_html_aa03ac56b19aba70879b7e2934da6a507"></a>
<a id="amqueue_8h_html_aaf2e88ac75eac32eb5a3672fd56759b7"></a>
<a id="amqueue_8h_html_ac19939c8157d7ef9033a5be97a7ca6a1"></a>
<a id="amqueue_8h_html_accd8c5ee36e60d990963e1d544ef4140"></a>
<a id="amqueue_8h_html_ae0ff0175064ab31858eff0669b7e745b"></a>
<a id="amqueue_8h_html_af13b6f0b3b15e14624b0c50050d062a4"></a>
<a id="aposix__types_8h_html"></a>
<a id="asignal_8h_html"></a>
<a id="astat_8h_html"></a>
<a id="astructmq__attr_html"></a>
<a id="astructmq__attr_html_a08cfd508cef817ba351c1af8d9af50f5"></a>
<a id="astructmq__attr_html_a19c05fa88c6d1126120d800647ddb0dd"></a>
<a id="astructmq__attr_html_aa535e1fa6c07c1d189e720ba15f9af08"></a>
<a id="astructmq__attr_html_ae975d1d907081c1e53b079c981c32209"></a>
<a id="astructsigevent_html"></a>
<a id="astructtimespec_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_MQUEUE_H_
#define ZEPHYR_INCLUDE_POSIX_MQUEUE_H_

#include <time.h>
#include <signal.h>

#include <zephyr/kernel.h>
#include <zephyr/posix/fcntl.h>
#include <zephyr/posix/sys/stat.h>
#include <zephyr/posix/posix_types.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void *mqd_t;

struct mq_attr {
        long mq_flags;
        long mq_maxmsg;
        long mq_msgsize;
        long mq_curmsgs;        /* Number of messages currently queued. */
};

mqd_t mq_open(const char *name, int oflags, ...);
int mq_close(mqd_t mqdes);
int mq_unlink(const char *name);
int mq_getattr(mqd_t mqdes, struct mq_attr *mqstat);
int mq_receive(mqd_t mqdes, char *msg_ptr, size_t msg_len,
                   unsigned int *msg_prio);
int mq_send(mqd_t mqdes, const char *msg_ptr, size_t msg_len,
            unsigned int msg_prio);
int mq_setattr(mqd_t mqdes, const struct mq_attr *mqstat,
               struct mq_attr *omqstat);
int mq_timedreceive(mqd_t mqdes, char *msg_ptr, size_t msg_len,
                        unsigned int *msg_prio, const struct timespec *abstime);
int mq_timedsend(mqd_t mqdes, const char *msg_ptr, size_t msg_len,
                 unsigned int msg_prio, const struct timespec *abstime);
int mq_notify(mqd_t mqdes, const struct sigevent *notification);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_MQUEUE_H_ */
```

## 119.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

当前已排队的消息数量。

### 注释 3：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_MQUEUE_H_`。

## 119.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html)
- [signal.h](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/posix/fcntl.h](https://docs.zephyrproject.org/latest/doxygen/html/fcntl_8h.html)
- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [mqd_t](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#aa03ac56b19aba70879b7e2934da6a507)
- [mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)
- [mq_flags](../posix_system_model_reference/P007_mq_attr_结构体.md#a19c05fa88c6d1126120d800647ddb0dd)
- [mq_maxmsg](../posix_system_model_reference/P007_mq_attr_结构体.md#aa535e1fa6c07c1d189e720ba15f9af08)
- [mq_msgsize](../posix_system_model_reference/P007_mq_attr_结构体.md#ae975d1d907081c1e53b079c981c32209)
- [mq_curmsgs](../posix_system_model_reference/P007_mq_attr_结构体.md#a08cfd508cef817ba351c1af8d9af50f5)
- [mq_open](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#a6e6c4881ac0fd3ad18d733b96d088b8b)
- [mq_close](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#a3fbd3906296be63451c64d69be2bc371)
- [mq_unlink](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#accd8c5ee36e60d990963e1d544ef4140)
- [mq_getattr](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#a5a55ce03d8466a53a36601aaca9ee328)
- [mq_receive](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#ae0ff0175064ab31858eff0669b7e745b)
- [mq_send](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#af13b6f0b3b15e14624b0c50050d062a4)
- [mq_setattr](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#a83b7aa93cb6f1f5a4fd938baea5579a6)
- [mq_timedreceive](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#aaf2e88ac75eac32eb5a3672fd56759b7)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [mq_timedsend](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#ac19939c8157d7ef9033a5be97a7ca6a1)
- [mq_notify](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html#a5eadbb82e0b9702d77f384a27827b334)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)
- [fcntl.h](https://docs.zephyrproject.org/latest/doxygen/html/fcntl_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [mq_attr::mq_curmsgs](../posix_system_model_reference/P007_mq_attr_结构体.md#a08cfd508cef817ba351c1af8d9af50f5)
- [mq_attr::mq_flags](../posix_system_model_reference/P007_mq_attr_结构体.md#a19c05fa88c6d1126120d800647ddb0dd)
- [mq_attr::mq_maxmsg](../posix_system_model_reference/P007_mq_attr_结构体.md#aa535e1fa6c07c1d189e720ba15f9af08)
- [mq_attr::mq_msgsize](../posix_system_model_reference/P007_mq_attr_结构体.md#ae975d1d907081c1e53b079c981c32209)

---

[上一章](P118_mqtt_sn.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P120_mspm0-pinctrl.h_源码浏览.md)
