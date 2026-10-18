---
id: learning.zephyr-docs.api-source-reference.page-322
title: hostname.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第322章\_hostname.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html)。

## 322.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
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
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__net__hostname_html_ga2b9d6f604afcde27b6d1543495e2ba8b"></a>
<a id="agroup__net__hostname_html_ga6aa3799b3b0d7eec7fb8b276485ae2c5"></a>
<a id="agroup__net__hostname_html_ga8870e80f16f934d1d8a86ea6bddbaf0b"></a>
<a id="agroup__net__hostname_html_ga96adbfaa629b6d450f06e19678eba9bc"></a>
<a id="agroup__net__hostname_html_gad15b0b79870f9ae9e295808bc58d8cef"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__system__errno_html_gae37becfaa095a9df5c5c788bce5aa06f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HOSTNAME_H_
#define ZEPHYR_INCLUDE_NET_HOSTNAME_H_

#include <errno.h>

#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_NET_HOSTNAME_MAX_LEN)
#define NET_HOSTNAME_MAX_LEN                                                                       \
        MAX(CONFIG_NET_HOSTNAME_MAX_LEN,                                                           \
            (sizeof(CONFIG_NET_HOSTNAME) - 1 +                                                     \
             (IS_ENABLED(CONFIG_NET_HOSTNAME_UNIQUE) ? sizeof("0011223344556677") - 1 : 0)))
#else
#define NET_HOSTNAME_MAX_LEN                                                                       \
        (sizeof(CONFIG_NET_HOSTNAME) - 1 +                                                         \
         (IS_ENABLED(CONFIG_NET_HOSTNAME_UNIQUE) ? sizeof("0011223344556677") - 1 : 0))
#endif


#if defined(CONFIG_NET_HOSTNAME_ENABLE)
#define NET_HOSTNAME_SIZE NET_HOSTNAME_MAX_LEN + 1
#else
#define NET_HOSTNAME_SIZE 1
#endif


#if defined(CONFIG_NET_HOSTNAME_ENABLE)
const char *net_hostname_get(void);
#else
static inline const char *net_hostname_get(void)
{
        return "zephyr";
}
#endif /* CONFIG_NET_HOSTNAME_ENABLE */

#if defined(CONFIG_NET_HOSTNAME_DYNAMIC)
int net_hostname_set(const char *host, size_t len);
#else
static inline int net_hostname_set(const char *host, size_t len)
{
        ARG_UNUSED(host);
        ARG_UNUSED(len);
        return -ENOTSUP;
}
#endif

#if defined(CONFIG_NET_HOSTNAME_ENABLE)
void net_hostname_init(void);
#else
static inline void net_hostname_init(void)
{
}
#endif /* CONFIG_NET_HOSTNAME_ENABLE */

#if defined(CONFIG_NET_HOSTNAME_UNIQUE)
int net_hostname_set_postfix(const uint8_t *hostname_postfix,
                              int postfix_len);
#else
static inline int net_hostname_set_postfix(const uint8_t *hostname_postfix,
                                           int postfix_len)
{
        ARG_UNUSED(hostname_postfix);
        ARG_UNUSED(postfix_len);
        return -EMSGSIZE;
}
#endif /* CONFIG_NET_HOSTNAME_UNIQUE */

#if defined(CONFIG_NET_HOSTNAME_UNIQUE)
int net_hostname_set_postfix_str(const uint8_t *hostname_postfix,
                             int postfix_len);
#else
static inline int net_hostname_set_postfix_str(const uint8_t *hostname_postfix,
                                           int postfix_len)
{
        ARG_UNUSED(hostname_postfix);
        ARG_UNUSED(postfix_len);
        return -EMSGSIZE;
}
#endif /* CONFIG_NET_HOSTNAME_UNIQUE */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_HOSTNAME_H_ */
```

## 322.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 68 行

条件编译配置（Configuration）标记：`CONFIG_NET_HOSTNAME_ENABLE`。

### 注释 3：原第 99 行

条件编译配置（Configuration）标记：`CONFIG_NET_HOSTNAME_ENABLE`。

### 注释 4：原第 125 行

条件编译配置（Configuration）标记：`CONFIG_NET_HOSTNAME_UNIQUE`。

### 注释 5：原第 152 行

条件编译配置（Configuration）标记：`CONFIG_NET_HOSTNAME_UNIQUE`。

### 注释 6：原第 162 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HOSTNAME_H_`。

## 322.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [net_hostname_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga8870e80f16f934d1d8a86ea6bddbaf0b)
- [net_hostname_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#gad15b0b79870f9ae9e295808bc58d8cef)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_hostname_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga96adbfaa629b6d450f06e19678eba9bc)
- [net_hostname_set_postfix](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga6aa3799b3b0d7eec7fb8b276485ae2c5)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [EMSGSIZE](../error_reference/P003_系统错误号公共接口.md#gae37becfaa095a9df5c5c788bce5aa06f)
- [net_hostname_set_postfix_str](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga2b9d6f604afcde27b6d1543495e2ba8b)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P321_hooks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P323_hrs.h_源码浏览.md)
