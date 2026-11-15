---
id: learning.zephyr-docs.api-source-reference.page-114
title: connectivity_wifi_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_connectivity\_wifi\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h.html)。

## 114.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
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
<a id="aconn__mgr__connectivity__impl_8h_html"></a>

```c
/*
 * Copyright (c) 2024 CSIRO
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_WIFI_MGMT_H_
#define ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_WIFI_MGMT_H_

#include <zephyr/net/conn_mgr_connectivity_impl.h>

#ifdef __cplusplus
extern "C" {
#endif

#define CONNECTIVITY_WIFI_MGMT_CTX_TYPE void *

#define CONNECTIVITY_WIFI_MGMT_BIND(dev_id)                               \
        IF_ENABLED(CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT,  \
                   (CONN_MGR_CONN_DECLARE_PUBLIC(CONNECTIVITY_WIFI_MGMT); \
                    CONN_MGR_BIND_CONN(dev_id, CONNECTIVITY_WIFI_MGMT)))

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_WIFI_MGMT_H_ */
```

## 114.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 CSIRO。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_WIFI_MGMT_H_`。

## 114.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h.html)
- [zephyr/net/conn_mgr_connectivity_impl.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html)
- [conn_mgr_connectivity_impl.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html)

---

[上一章](P113_conn_mgr_monitor.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P115_console.h_源码浏览.md)
