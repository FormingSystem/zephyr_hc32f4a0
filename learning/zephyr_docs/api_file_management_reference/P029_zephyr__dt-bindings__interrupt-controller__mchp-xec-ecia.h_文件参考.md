---
id: learning.zephyr-docs.api-file-management-reference.page-29
title: zephyr__dt-bindings__interrupt-controller__mchp-xec-ecia.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_mchp-xec-ecia.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip XEC嵌入式控制器中断聚合器（ECIA）的设备树宏。

查看此文件的源码。

<a id="details"></a>

Microchip XEC嵌入式控制器中断聚合器（ECIA）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="r_gaca04c194e5bdd4922d927b35f39fbe79"></a>

```c
#define MCHP_XEC_ECIA_GIRQ_ENC(g, b)
```

相关声明：[MCHP_XEC_ECIA_GIRQ_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#gaca04c194e5bdd4922d927b35f39fbe79)。

仅编码外设的分组中断请求（GIRQ）及 GIRQ 位位置。

<a id="r_gac1daa9f5e1b5764f0748577ee60550d3"></a>

```c
#define MCHP_XEC_ECIA(g, gb, na, nd)
```

相关声明：[MCHP_XEC_ECIA](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#gac1daa9f5e1b5764f0748577ee60550d3)。

将外设中断信息（peripheral interrupt information）编码为一个 32 位值。

<a id="r_ga6fee82b914dc9f73392586224f0708e7"></a>

```c
#define MCHP_XEC_ECIA_GIRQ(e)
```

相关声明：[MCHP_XEC_ECIA_GIRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga6fee82b914dc9f73392586224f0708e7)。

从已编码的 `MCHP_XEC_ECIA()` 值提取 GIRQ 编号。

<a id="r_ga32c0b5e661fbee763a496b3b06eae34a"></a>

```c
#define MCHP_XEC_ECIA_GIRQ_POS(e)
```

相关声明：[MCHP_XEC_ECIA_GIRQ_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga32c0b5e661fbee763a496b3b06eae34a)。

从已编码的 `MCHP_XEC_ECIA()` 值提取中断源位位置。

<a id="r_ga9099e944648c0d8b6946b2092f872122"></a>

```c
#define MCHP_XEC_ECIA_NVIC_AGGR(e)
```

相关声明：[MCHP_XEC_ECIA_NVIC_AGGR](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga9099e944648c0d8b6946b2092f872122)。

从已编码的 `MCHP_XEC_ECIA()` 值提取聚合 GIRQ 的 NVIC 编号。

<a id="r_ga1efb0ece73d7b15da7cdc316c162bc3a"></a>

```c
#define MCHP_XEC_ECIA_NVIC_DIRECT(e)
```

相关声明：[MCHP_XEC_ECIA_NVIC_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga1efb0ece73d7b15da7cdc316c162bc3a)。

从已编码的 `MCHP_XEC_ECIA()` 值提取直接中断的 NVIC 编号。


## 29.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P490_mchp-xec-ecia.h_源码浏览.md)
- [MCHP_XEC_ECIA_GIRQ_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#gaca04c194e5bdd4922d927b35f39fbe79)
- [MCHP_XEC_ECIA](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#gac1daa9f5e1b5764f0748577ee60550d3)
- [MCHP_XEC_ECIA_GIRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga6fee82b914dc9f73392586224f0708e7)
- [MCHP_XEC_ECIA_GIRQ_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga32c0b5e661fbee763a496b3b06eae34a)
- [MCHP_XEC_ECIA_NVIC_AGGR](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga9099e944648c0d8b6946b2092f872122)
- [MCHP_XEC_ECIA_NVIC_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html#ga1efb0ece73d7b15da7cdc316c162bc3a)

<a id="header-details"></a>

---

[上一章](P028_zephyr__display__mb_display.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__drivers__clock_control__mchp_clock_pic32cm_jh.h_文件参考.md)
