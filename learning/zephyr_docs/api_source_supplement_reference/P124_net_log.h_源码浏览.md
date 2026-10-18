---
id: learning.zephyr-docs.api-source-supplement-reference.page-124
title: net_log.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__log_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_net\_log.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__log_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__log_8h.html)。

## 124.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="alog_8h_html"></a>

```c
/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_LOG_H_
#define ZEPHYR_INCLUDE_NET_NET_LOG_H_

#include <zephyr/logging/log.h>

#ifdef __cplusplus
extern "C" {
#endif


#ifdef CONFIG_THREAD_NAME
#define NET_DBG(fmt, ...) LOG_DBG("(%s): " fmt,                         \
                        k_thread_name_get(k_current_get()), \
                        ##__VA_ARGS__)
#else
#define NET_DBG(fmt, ...) LOG_DBG("(%p): " fmt, k_current_get(),        \
                                  ##__VA_ARGS__)
#endif /* CONFIG_THREAD_NAME */
#define NET_ERR(fmt, ...) LOG_ERR(fmt, ##__VA_ARGS__)
#define NET_WARN(fmt, ...) LOG_WRN(fmt, ##__VA_ARGS__)
#define NET_INFO(fmt, ...) LOG_INF(fmt,  ##__VA_ARGS__)

/* Rate-limited network logging macros */
#define NET_ERR_RATELIMIT(fmt, ...)  LOG_ERR_RATELIMIT(fmt, ##__VA_ARGS__)
#define NET_WARN_RATELIMIT(fmt, ...) LOG_WRN_RATELIMIT(fmt, ##__VA_ARGS__)
#define NET_INFO_RATELIMIT(fmt, ...) LOG_INF_RATELIMIT(fmt, ##__VA_ARGS__)
#define NET_DBG_RATELIMIT(fmt, ...)  LOG_DBG_RATELIMIT(fmt, ##__VA_ARGS__)

#define NET_HEXDUMP_DBG(_data, _length, _str)  LOG_HEXDUMP_DBG(_data, _length, _str)
#define NET_HEXDUMP_ERR(_data, _length, _str)  LOG_HEXDUMP_ERR(_data, _length, _str)
#define NET_HEXDUMP_WARN(_data, _length, _str) LOG_HEXDUMP_WRN(_data, _length, _str)
#define NET_HEXDUMP_INFO(_data, _length, _str) LOG_HEXDUMP_INF(_data, _length, _str)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_LOG_H_ */
```

## 124.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

条件编译配置（Configuration）标记：`CONFIG_THREAD_NAME`。

### 注释 3：原第 38 行

限速网络日志宏（Rate-limited network logging macros）。

### 注释 4：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_LOG_H_`。

## 124.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__log_8h.html)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [log.h](../log_core_reference/P003_日志公共头文件参考.md)

---

[上一章](P123_net_config.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P125_net_time.h_源码浏览.md)
