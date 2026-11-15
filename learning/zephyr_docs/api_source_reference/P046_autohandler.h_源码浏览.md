---
id: learning.zephyr-docs.api-source-reference.page-46
title: autohandler.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_autohandler.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h.html)。

## 46.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="agroup__hawkbit__autohandler_html_ga41865255aa3020a34816c23ae7977f20"></a>
<a id="agroup__hawkbit__autohandler_html_ga47fe3e9cd227fd4da332e9eeff81f991"></a>
<a id="agroup__hawkbit__autohandler_html_ga6d13b3d7b9a61d06a6eaa346189a08c6"></a>
<a id="agroup__hawkbit__autohandler_html_gabc27308bb974d6e0b9650476243e5e9a"></a>
<a id="agroup__hawkbit_html_ga96c59c754178451d8dbd08b32813220b"></a>
<a id="ahawkbit_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2024 Vogl Electronic GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_MGMT_HAWKBIT_AUTOHANDLER_H_
#define ZEPHYR_INCLUDE_MGMT_HAWKBIT_AUTOHANDLER_H_

#include <zephyr/mgmt/hawkbit/hawkbit.h>

void hawkbit_autohandler(bool auto_reschedule);

enum hawkbit_response hawkbit_autohandler_wait(uint32_t events, k_timeout_t timeout);

int hawkbit_autohandler_cancel(void);

int hawkbit_autohandler_set_delay(k_timeout_t timeout, bool if_bigger);


#endif /* ZEPHYR_INCLUDE_MGMT_HAWKBIT_AUTOHANDLER_H_ */
```

## 46.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Vogl Electronic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_HAWKBIT_AUTOHANDLER_H_`。

## 46.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h.html)
- [zephyr/mgmt/hawkbit/hawkbit.h](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)
- [hawkbit_autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga41865255aa3020a34816c23ae7977f20)
- [hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)
- [hawkbit_autohandler_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga6d13b3d7b9a61d06a6eaa346189a08c6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [hawkbit_autohandler_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#gabc27308bb974d6e0b9650476243e5e9a)
- [hawkbit_autohandler_set_delay](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga47fe3e9cd227fd4da332e9eeff81f991)
- [hawkbit.h](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)

---

[上一章](P045_atmel_samx7x_dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P047_auxdisplay.h_源码浏览.md)
