---
id: learning.zephyr-docs.api-source-reference.page-917
title: wifi_certs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第917章\_wifi\_certs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html)。

## 917.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astructnet__if_html"></a>
<a id="awifi__certs_8h_html_a1ed064792c11d2760b6b5c3dfdaabe82"></a>
<a id="awifi__certs_8h_html_a21f62e407bc403636fbe6ed973e620f6"></a>
<a id="awifi__mgmt_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_WIFI_CERTS_H_
#define ZEPHYR_INCLUDE_NET_WIFI_CERTS_H_

#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/net/wifi_mgmt.h>

int wifi_set_enterprise_credentials(struct net_if *iface, bool is_ap);

void wifi_clear_enterprise_credentials(void);

#endif /* ZEPHYR_INCLUDE_NET_WIFI_CERTS_H_ */
```

## 917.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 44 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_CERTS_H_`。

## 917.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)
- [wifi_set_enterprise_credentials](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html#a21f62e407bc403636fbe6ed973e620f6)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [wifi_clear_enterprise_credentials](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html#a1ed064792c11d2760b6b5c3dfdaabe82)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)

---

[上一章](P916_websocket.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P918_wifi_credentials.h_源码浏览.md)
