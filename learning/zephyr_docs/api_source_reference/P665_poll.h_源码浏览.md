---
id: learning.zephyr-docs.api-source-reference.page-665
title: poll.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/poll_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第665章\_poll.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html)。

## 665.1\_原始可见代码（Source Code）

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
<a id="anet_2socket_8h_html"></a>
<a id="apoll_8h_html_aa49b6bf041fda66eda01c0170243c271"></a>
<a id="apoll_8h_html_af78a57e8ee17b7ecfe4510253d858afd"></a>
<a id="apoll_8h_html_afa7e83ddea0ab5b08fcf614b89ac48ba"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_POLL_H_
#define ZEPHYR_INCLUDE_POSIX_POLL_H_

#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef unsigned int nfds_t;

#define pollfd zsock_pollfd

#define POLLIN ZSOCK_POLLIN
#define POLLPRI ZSOCK_POLLPRI
#define POLLOUT ZSOCK_POLLOUT
#define POLLERR ZSOCK_POLLERR
#define POLLHUP ZSOCK_POLLHUP
#define POLLNVAL ZSOCK_POLLNVAL

int poll(struct pollfd *fds, int nfds, int timeout);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_POSIX_POLL_H_ */
```

## 665.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POLL_H_`。

## 665.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [nfds_t](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html#aa49b6bf041fda66eda01c0170243c271)
- [poll](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html#afa7e83ddea0ab5b08fcf614b89ac48ba)
- [pollfd](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html#af78a57e8ee17b7ecfe4510253d858afd)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)

---

[上一章](P664_pmu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P666_eventfd.h_源码浏览.md)
