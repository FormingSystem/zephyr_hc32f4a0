---
id: learning.zephyr-docs.api-source-supplement-reference.page-184
title: socket_poll.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__poll_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_socket\_poll.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__poll_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__poll_8h.html)。

## 184.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00031"></a>
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
<a id="l00047"></a>
<a id="l00048"></a>
<a id="afdtable_8h_html"></a>
<a id="astructzsock__pollfd_html"></a>
<a id="astructzsock__pollfd_html_a31929c24c64b58c6f7e443645352f67d"></a>
<a id="astructzsock__pollfd_html_a58fcd3f9af542bb15a936319aaf9c32e"></a>
<a id="astructzsock__pollfd_html_a98838f19b29e759a4b53db9b15349917"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKET_POLL_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_POLL_H_

#include <zephyr/sys/fdtable.h>

/* Setting for pollfd to avoid circular inclusion */


#ifdef __cplusplus
extern "C" {
#endif

#ifdef __DOXYGEN__
struct zsock_pollfd {
        int fd;
        short events;
        short revents;
};
#else
#define zsock_pollfd zvfs_pollfd
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SOCKET_POLL_H_ */
```

## 184.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

`pollfd` 的设置，用于避免循环包含（Circular inclusion）。

### 注释 3：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_POLL_H_`。

## 184.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__poll_8h.html)
- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [fd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a58fcd3f9af542bb15a936319aaf9c32e)
- [events](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a31929c24c64b58c6f7e443645352f67d)
- [revents](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a98838f19b29e759a4b53db9b15349917)
- [fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [zsock_pollfd::events](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a31929c24c64b58c6f7e443645352f67d)
- [zsock_pollfd::fd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a58fcd3f9af542bb15a936319aaf9c32e)
- [zsock_pollfd::revents](../posix_system_model_reference/P030_zsock_pollfd_结构体.md#a98838f19b29e759a4b53db9b15349917)

---

[上一章](P183_socket_offload.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P185_speculation.h_源码浏览.md)
