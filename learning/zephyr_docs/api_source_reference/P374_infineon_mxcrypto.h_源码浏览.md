---
id: learning.zephyr-docs.api-source-reference.page-374
title: infineon_mxcrypto.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第374章\_infineon\_mxcrypto.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h.html)。

## 374.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__mfd__interface__infineon__mxcrypto_html_ga13bfa154453a651ad9db64cccfe29911"></a>
<a id="agroup__mfd__interface__infineon__mxcrypto_html_ga22a1877404d491be13303ae7f1356b84"></a>
<a id="agroup__mfd__interface__infineon__mxcrypto_html_ga786996a9934b87fe322e98bff53858e8"></a>
<a id="akernel_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MFD_INFINEON_MXCRYPTO_H_
#define ZEPHYR_INCLUDE_DRIVERS_MFD_INFINEON_MXCRYPTO_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>

#include "cy_device.h"
#include "cy_device_headers.h"


#ifdef __cplusplus
extern "C" {
#endif

CRYPTO_Type *mfd_infineon_mxcrypto_get_base(const struct device *dev);

int mfd_infineon_mxcrypto_lock(const struct device *dev, k_timeout_t timeout);

void mfd_infineon_mxcrypto_unlock(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MFD_INFINEON_MXCRYPTO_H_ */
```

## 374.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MFD_INFINEON_MXCRYPTO_H_`。

## 374.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mfd_infineon_mxcrypto_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga13bfa154453a651ad9db64cccfe29911)
- [device](../device_reference/P002_设备对象结构.md)
- [mfd_infineon_mxcrypto_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga22a1877404d491be13303ae7f1356b84)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mfd_infineon_mxcrypto_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga786996a9934b87fe322e98bff53858e8)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P373_infineon-xmc4xxx-intc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P375_infineon_mxcryptolite.h_源码浏览.md)
