---
id: learning.zephyr-docs.api-source-reference.page-802
title: socket_select.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第802章\_socket\_select.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h.html)。

## 802.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="afdtable_8h_html"></a>
<a id="afdtable_8h_html_a029809dfde96846d9e7871e252d74546"></a>
<a id="afdtable_8h_html_a46ae4a3ac3d192de02fb1b6c4a4e95ac"></a>
<a id="afdtable_8h_html_a84f63f19ea89e5711725f4d753b5484c"></a>
<a id="afdtable_8h_html_a8ced1fc0adbdf35b71ec486a8ec68665"></a>
<a id="afdtable_8h_html_afa48d92e5f545412139f567a19e01f71"></a>
<a id="agroup__bsd__sockets_html_ga1a065da89061bcb10b10663a9ffbdd10"></a>
<a id="agroup__bsd__sockets_html_ga1cdeeddce9000b9fd29b638c422f48f8"></a>
<a id="agroup__bsd__sockets_html_ga5d07f52910f6d881295ec659716767f1"></a>
<a id="agroup__bsd__sockets_html_ga7023ec00d24af41a7cbf5f376fb44487"></a>
<a id="agroup__bsd__sockets_html_gaa4855f07c1329a150f371044e4384490"></a>
<a id="agroup__bsd__sockets_html_gab92b08adccc22a85e7a1c06bf11a88bc"></a>
<a id="agroup__clock__apis_html_ga2180f263d149841a7c1fde663edb84c5"></a>
<a id="asocket__types_8h_html"></a>
<a id="astructtimespec_html"></a>
<a id="astructzvfs__fd__set_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_SOCKET_SELECT_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_SELECT_H_


#include <time.h>

#include <zephyr/toolchain.h>
#include <zephyr/net/socket_types.h>
#include <zephyr/sys/fdtable.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct zvfs_fd_set zsock_fd_set;

static inline int zsock_select(int nfds, zsock_fd_set *readfds, zsock_fd_set *writefds,
                               zsock_fd_set *exceptfds, struct zsock_timeval *timeout)
{
        struct timespec to = {
                .tv_sec = (timeout == NULL) ? 0 : timeout->tv_sec,
                .tv_nsec = (long)((timeout == NULL) ? 0 : timeout->tv_usec * NSEC_PER_USEC)};

        return zvfs_select(nfds, readfds, writefds, exceptfds, (timeout == NULL) ? NULL : &to,
                           NULL);
}

#define ZSOCK_FD_SETSIZE ZVFS_FD_SETSIZE

static inline void ZSOCK_FD_ZERO(zsock_fd_set *set)
{
        ZVFS_FD_ZERO(set);
}

static inline int ZSOCK_FD_ISSET(int fd, zsock_fd_set *set)
{
        return ZVFS_FD_ISSET(fd, set);
}

static inline void ZSOCK_FD_CLR(int fd, zsock_fd_set *set)
{
        ZVFS_FD_CLR(fd, set);
}

static inline void ZSOCK_FD_SET(int fd, zsock_fd_set *set)
{
        ZVFS_FD_SET(fd, set);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SOCKET_SELECT_H_ */
```

## 802.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_SELECT_H_`。

## 802.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/net/socket_types.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h.html)
- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)
- [zsock_select](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1a065da89061bcb10b10663a9ffbdd10)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [NSEC_PER_USEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2180f263d149841a7c1fde663edb84c5)
- [zvfs_select](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a8ced1fc0adbdf35b71ec486a8ec68665)
- [ZSOCK_FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa4855f07c1329a150f371044e4384490)
- [ZVFS_FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a46ae4a3ac3d192de02fb1b6c4a4e95ac)
- [ZSOCK_FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab92b08adccc22a85e7a1c06bf11a88bc)
- [ZVFS_FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a84f63f19ea89e5711725f4d753b5484c)
- [ZSOCK_FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7023ec00d24af41a7cbf5f376fb44487)
- [ZVFS_FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a029809dfde96846d9e7871e252d74546)
- [ZSOCK_FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5d07f52910f6d881295ec659716767f1)
- [ZVFS_FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#afa48d92e5f545412139f567a19e01f71)
- [fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [socket_types.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P801_sntp_server.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P803_socketcan_utils.h_源码浏览.md)
