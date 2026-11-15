---
id: learning.zephyr-docs.api-source-reference.page-754
title: semaphore.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第754章\_semaphore.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html)。

## 754.1\_原始可见代码（Source Code）

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
<a id="aposix__types_8h_html"></a>
<a id="aposix__types_8h_html_afb4edc6a51d66a7a352424942b631a1e"></a>
<a id="asemaphore_8h_html_a0ed06fc3db017281dc6f1eefff97053a"></a>
<a id="asemaphore_8h_html_a0f2fd32f79e2815f52f2afd2f5069960"></a>
<a id="asemaphore_8h_html_a1fee59859601fb325fafb32ee41b5691"></a>
<a id="asemaphore_8h_html_a2bee748f81a960f80dfccf675f38e3d8"></a>
<a id="asemaphore_8h_html_a355d892eec64a2dc95143635469c6524"></a>
<a id="asemaphore_8h_html_a42cc945f89772ca24e87a569a5f2dbd7"></a>
<a id="asemaphore_8h_html_a4e398fea1080fd7919e5c72ee94e2fc5"></a>
<a id="asemaphore_8h_html_a776256d1a473906f8b7490689bfcb75c"></a>
<a id="asemaphore_8h_html_a91a6510735a16f94defc52ecbb7971ac"></a>
<a id="asemaphore_8h_html_af4d15a2fd215951eb7ea2424ffdd335e"></a>
<a id="astructtimespec_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SEMAPHORE_H_
#define ZEPHYR_INCLUDE_POSIX_SEMAPHORE_H_

#include <time.h>

#include <zephyr/posix/posix_types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define SEM_FAILED ((sem_t *) 0)

int sem_destroy(sem_t *semaphore);
int sem_getvalue(sem_t *ZRESTRICT semaphore, int *ZRESTRICT value);
int sem_init(sem_t *semaphore, int pshared, unsigned int value);
int sem_post(sem_t *semaphore);
int sem_timedwait(sem_t *ZRESTRICT semaphore, struct timespec *ZRESTRICT abstime);
int sem_trywait(sem_t *semaphore);
int sem_wait(sem_t *semaphore);
sem_t *sem_open(const char *name, int oflags, ...);
int sem_unlink(const char *name);
int sem_close(sem_t *sem);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SEMAPHORE_H_ */
```

## 754.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SEMAPHORE_H_`。

## 754.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [sem_destroy](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a42cc945f89772ca24e87a569a5f2dbd7)
- [sem_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#afb4edc6a51d66a7a352424942b631a1e)
- [sem_getvalue](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#af4d15a2fd215951eb7ea2424ffdd335e)
- [sem_init](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a1fee59859601fb325fafb32ee41b5691)
- [sem_post](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a2bee748f81a960f80dfccf675f38e3d8)
- [sem_timedwait](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a91a6510735a16f94defc52ecbb7971ac)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [sem_trywait](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a0f2fd32f79e2815f52f2afd2f5069960)
- [sem_wait](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a355d892eec64a2dc95143635469c6524)
- [sem_open](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a0ed06fc3db017281dc6f1eefff97053a)
- [sem_unlink](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a776256d1a473906f8b7490689bfcb75c)
- [sem_close](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html#a4e398fea1080fd7919e5c72ee94e2fc5)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)

---

[上一章](P753_select.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P755_semihost_loader.h_源码浏览.md)
