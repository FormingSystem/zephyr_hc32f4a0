---
id: learning.zephyr-docs.api-source-reference.page-366
title: inet.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inet_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第366章\_inet.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html)。

## 366.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="ain_8h_html"></a>
<a id="ain_8h_html_a73e57c1190f8731fb8b0217f929c4e1b"></a>
<a id="ainet_8h_html_a3e3b8f43e05dc3b87977b6a7a2ed09ca"></a>
<a id="ainet_8h_html_a98b38134a62f24554da0ffcabde8062c"></a>
<a id="ainet_8h_html_aabfaede889b4bc47241ab0c49a7a3cab"></a>
<a id="ainet_8h_html_ae93e32740fb355baef0cab02133e7ff4"></a>
<a id="ainet_8h_html_aeac5d8b00354beb2127ba1468e021ef4"></a>
<a id="anet_2socket_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_ARPA_INET_H_
#define ZEPHYR_INCLUDE_POSIX_ARPA_INET_H_

#include <stddef.h>

#include <zephyr/posix/netinet/in.h>
#include <zephyr/posix/sys/socket.h>

#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef uint32_t in_addr_t;

in_addr_t inet_addr(const char *cp);
char *inet_ntoa(struct in_addr in);
char *inet_ntop(sa_family_t family, const void *src, char *dst, size_t size);
int inet_pton(sa_family_t family, const char *src, void *dst);

#define ntohs(x)  net_ntohs(x)
#define ntohl(x)  net_ntohl(x)
#define ntohll(x) net_ntohll(x)
#define htons(x)  net_htons(x)
#define htonl(x)  net_htonl(x)
#define htonll(x) net_htonll(x)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_ARPA_INET_H_ */
```

## 366.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_ARPA_INET_H_`。

## 366.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html)
- [zephyr/posix/netinet/in.h](https://docs.zephyrproject.org/latest/doxygen/html/in_8h.html)
- [zephyr/posix/sys/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [in_addr_t](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#a98b38134a62f24554da0ffcabde8062c)
- [inet_addr](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#a3e3b8f43e05dc3b87977b6a7a2ed09ca)
- [inet_ntoa](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#aeac5d8b00354beb2127ba1468e021ef4)
- [in_addr](https://docs.zephyrproject.org/latest/doxygen/html/in_8h.html#a73e57c1190f8731fb8b0217f929c4e1b)
- [inet_ntop](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#ae93e32740fb355baef0cab02133e7ff4)
- [inet_pton](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#aabfaede889b4bc47241ab0c49a7a3cab)
- [in.h](https://docs.zephyrproject.org/latest/doxygen/html/in_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html)

---

[上一章](P365_openthread.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P367_infineon-autanalog-ctb.h_源码浏览.md)
