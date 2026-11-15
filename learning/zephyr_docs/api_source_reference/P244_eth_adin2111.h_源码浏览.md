---
id: learning.zephyr-docs.api-source-reference.page-244
title: eth_adin2111.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第244章\_eth\_adin2111.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html)。

## 244.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="adevice_8h_html"></a>
<a id="aeth__adin2111_8h_html_a340b4d3786807c7feb423b36d6533a87"></a>
<a id="aeth__adin2111_8h_html_a54e88cd118466a1a44ef02197fe2b59d"></a>
<a id="aeth__adin2111_8h_html_a72b5466138f087ac4e788bc878781c3e"></a>
<a id="aeth__adin2111_8h_html_a86de61f524a1837ff8f701c5af969d1b"></a>
<a id="aeth__adin2111_8h_html_a9752b1a6a75880af069af1b00ce43928"></a>
<a id="aeth__adin2111_8h_html_ad737f44a16702f4c8ce3f8a8ae994364"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2023 PHOENIX CONTACT Electronics GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ETH_ADIN2111_H__
#define ZEPHYR_INCLUDE_DRIVERS_ETH_ADIN2111_H__

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

int eth_adin2111_lock(const struct device *dev, k_timeout_t timeout);

int eth_adin2111_unlock(const struct device *dev);

int eth_adin2111_sw_reset(const struct device *dev, uint16_t delay);

int eth_adin2111_mac_reset(const struct device *dev);

int eth_adin2111_broadcast_filter(const struct device *dev, bool enable);

struct net_if *eth_adin2111_get_iface(const struct device *dev, const uint16_t port_idx);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_ETH_ADIN2111_H__ */
```

## 244.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 PHOENIX CONTACT Electronics GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_ETH_ADIN2111_H__`。

## 244.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [eth_adin2111_lock](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#a54e88cd118466a1a44ef02197fe2b59d)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [eth_adin2111_unlock](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#a72b5466138f087ac4e788bc878781c3e)
- [eth_adin2111_sw_reset](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#a340b4d3786807c7feb423b36d6533a87)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [eth_adin2111_mac_reset](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#ad737f44a16702f4c8ce3f8a8ae994364)
- [eth_adin2111_broadcast_filter](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#a9752b1a6a75880af069af1b00ce43928)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [eth_adin2111_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html#a86de61f524a1837ff8f701c5af969d1b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P243_espressif-esp32-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P245_ethernet_bridge_fdb.h_源码浏览.md)
