---
id: learning.zephyr-docs.api-source-reference.page-115
title: console.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_console.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h.html)。

## 115.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="agroup__console__api_html_ga0bf949437e32d17992435003cf8b46b5"></a>
<a id="agroup__console__api_html_ga204fd795daf9ef6b1f2803547747545e"></a>
<a id="agroup__console__api_html_ga27785534c14d4098822db2b870b7d81d"></a>
<a id="agroup__console__api_html_ga2ba36eb1081cd0b98aa43216ccd6fbd5"></a>
<a id="agroup__console__api_html_ga3454f5b84d38d46a6c2bbf7fd6baa815"></a>
<a id="agroup__console__api_html_ga401af68bb10c5b5e2a99997cee7de9c7"></a>
<a id="agroup__console__api_html_ga7bd842f1cda6c8218cb1d41420e4de49"></a>
<a id="agroup__console__api_html_ga83d86a81638a96ae84df792265dc0219"></a>
<a id="agroup__console__api_html_gacd13267df8567c63f2285ce0e1cbbc20"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_CONSOLE_CONSOLE_H_
#define ZEPHYR_INCLUDE_CONSOLE_CONSOLE_H_

#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


int console_init(void);

ssize_t console_read(void *dummy, void *buf, size_t size);

ssize_t console_write(void *dummy, const void *buf, size_t size);

int console_getchar(void);

int console_putchar(char c);

void console_getline_init(void);

char *console_getline(void);

void console_set_rx_timeout(k_timeout_t timeout);


void console_set_tx_timeout(k_timeout_t timeout);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_CONSOLE_CONSOLE_H_ */
```

## 115.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 143 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_CONSOLE_CONSOLE_H_`。

## 115.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga0bf949437e32d17992435003cf8b46b5)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [console_read](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga27785534c14d4098822db2b870b7d81d)
- [console_write](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga204fd795daf9ef6b1f2803547747545e)
- [console_getchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga2ba36eb1081cd0b98aa43216ccd6fbd5)
- [console_putchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga7bd842f1cda6c8218cb1d41420e4de49)
- [console_getline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#gacd13267df8567c63f2285ce0e1cbbc20)
- [console_getline](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga3454f5b84d38d46a6c2bbf7fd6baa815)
- [console_set_rx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga83d86a81638a96ae84df792265dc0219)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [console_set_tx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga401af68bb10c5b5e2a99997cee7de9c7)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)

---

[上一章](P114_connectivity_wifi_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P116_tty.h_源码浏览.md)
