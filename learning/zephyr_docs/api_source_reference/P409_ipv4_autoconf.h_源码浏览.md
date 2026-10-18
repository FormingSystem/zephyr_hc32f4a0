---
id: learning.zephyr-docs.api-source-reference.page-409
title: ipv4_autoconf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第409章\_ipv4\_autoconf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html)。

## 409.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="foldopen00015"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="aipv4__autoconf_8h_html_a4845fd81288d96d72bbf7e8001fd31a5"></a>
<a id="aipv4__autoconf_8h_html_a5cbac9cab526f57c9b4a8ec141dbfb99"></a>
<a id="aipv4__autoconf_8h_html_abdf8bb08f12768aad2ff95b902bdc899"></a>
<a id="aipv4__autoconf_8h_html_abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2"></a>
<a id="aipv4__autoconf_8h_html_abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b"></a>
<a id="aipv4__autoconf_8h_html_abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2017 Matthias Boesl
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IPV4_AUTOCONF_H_
#define ZEPHYR_INCLUDE_NET_IPV4_AUTOCONF_H_

enum net_ipv4_autoconf_state {
        NET_IPV4_AUTOCONF_INIT,
        NET_IPV4_AUTOCONF_ASSIGNED,
        NET_IPV4_AUTOCONF_RENEW,
};

struct net_if;

#if defined(CONFIG_NET_IPV4_AUTO)
void net_ipv4_autoconf_start(struct net_if *iface);
#else
static inline void net_ipv4_autoconf_start(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_IPV4_AUTO)
void net_ipv4_autoconf_reset(struct net_if *iface);
#else
static inline void net_ipv4_autoconf_reset(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_IPV4_AUTOCONF_H_ */
```

## 409.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Matthias Boesl。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IPV4_AUTOCONF_H_`。

## 409.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html)
- [net_ipv4_autoconf_state](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#abdf8bb08f12768aad2ff95b902bdc899)
- [NET_IPV4_AUTOCONF_INIT](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b)
- [NET_IPV4_AUTOCONF_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2)
- [NET_IPV4_AUTOCONF_RENEW](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_ipv4_autoconf_start](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#a5cbac9cab526f57c9b4a8ec141dbfb99)
- [net_ipv4_autoconf_reset](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html#a4845fd81288d96d72bbf7e8001fd31a5)

---

[上一章](P408_ioctl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P410_ipv4_nat.h_源码浏览.md)
