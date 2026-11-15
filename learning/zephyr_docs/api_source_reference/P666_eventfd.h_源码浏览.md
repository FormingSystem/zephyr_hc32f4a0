---
id: learning.zephyr-docs.api-source-reference.page-666
title: eventfd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第666章\_eventfd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html)。

## 666.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aposix_2sys_2eventfd_8h_html_a32e55549cb7aea88db8a14be9ed5d092"></a>
<a id="aposix_2sys_2eventfd_8h_html_a9c7aafe8ee787e3ba362fb6aab3e5542"></a>
<a id="aposix_2sys_2eventfd_8h_html_ab06039421a08cedb36946381608fa7f7"></a>
<a id="aposix_2sys_2eventfd_8h_html_ac8eb3d8ee0d064d293a5433c2c1f6165"></a>
<a id="azvfs_2eventfd_8h_html"></a>
<a id="azvfs_2eventfd_8h_html_a2f8a313f0a8175844c91c78d5b9340ad"></a>

```c
/*
 * Copyright (c) 2020 Tobias Svehagen
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_SYS_EVENTFD_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_EVENTFD_H_

#include <zephyr/zvfs/eventfd.h>

#ifdef __cplusplus
extern "C" {
#endif

#define EFD_SEMAPHORE ZVFS_EFD_SEMAPHORE
#define EFD_NONBLOCK  ZVFS_EFD_NONBLOCK

typedef zvfs_eventfd_t eventfd_t;

int eventfd(unsigned int initval, int flags);

int eventfd_read(int fd, eventfd_t *value);

int eventfd_write(int fd, eventfd_t value);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_EVENTFD_H_ */
```

## 666.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Tobias Svehagen。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_EVENTFD_H_`。

## 666.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html)
- [zephyr/zvfs/eventfd.h](https://docs.zephyrproject.org/latest/doxygen/html/zvfs_2eventfd_8h.html)
- [zvfs_eventfd_t](https://docs.zephyrproject.org/latest/doxygen/html/zvfs_2eventfd_8h.html#a2f8a313f0a8175844c91c78d5b9340ad)
- [eventfd_t](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html#ac8eb3d8ee0d064d293a5433c2c1f6165)
- [eventfd](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html#ab06039421a08cedb36946381608fa7f7)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [eventfd_read](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html#a32e55549cb7aea88db8a14be9ed5d092)
- [eventfd_write](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html#a9c7aafe8ee787e3ba362fb6aab3e5542)
- [eventfd.h](https://docs.zephyrproject.org/latest/doxygen/html/zvfs_2eventfd_8h.html)

---

[上一章](P665_poll.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P667_socket.h_源码浏览.md)
