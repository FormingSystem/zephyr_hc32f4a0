---
id: learning.zephyr-docs.api-file-runtime-reference.page-22
title: zephyr__drivers__mfd__infineon_mxcrypto.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_mfd\_\_infineon\_mxcrypto.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcrypto_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MXCRYPTO多功能设备（MFD）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include "cy_device.h"
#include "cy_device_headers.h"
```

查看此文件的源码。

MXCRYPTO多功能设备（MFD）驱动的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_ga13bfa154453a651ad9db64cccfe29911"></a>

```c
CRYPTO_Type * mfd_infineon_mxcrypto_get_base (const struct device *dev)
```

相关声明：[mfd_infineon_mxcrypto_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga13bfa154453a651ad9db64cccfe29911)、[device](../device_reference/P002_设备对象结构.md)。

获取 MXCRYPTO 寄存器基地址（Register Base Address）。

<a id="r_ga22a1877404d491be13303ae7f1356b84"></a>

```c
int mfd_infineon_mxcrypto_lock (const struct device *dev, k_timeout_t timeout)
```

相关声明：[mfd_infineon_mxcrypto_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga22a1877404d491be13303ae7f1356b84)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取共享的 MXCRYPTO 访问互斥锁（Access Mutex）。

<a id="r_ga786996a9934b87fe322e98bff53858e8"></a>

```c
void mfd_infineon_mxcrypto_unlock (const struct device *dev)
```

相关声明：[mfd_infineon_mxcrypto_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga786996a9934b87fe322e98bff53858e8)、[device](../device_reference/P002_设备对象结构.md)。

释放共享的 MXCRYPTO 访问互斥锁（Access Mutex）。


## 22.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P374_infineon_mxcrypto.h_源码浏览.md)
- [mfd_infineon_mxcrypto_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga13bfa154453a651ad9db64cccfe29911)
- [device](../device_reference/P002_设备对象结构.md)
- [mfd_infineon_mxcrypto_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga22a1877404d491be13303ae7f1356b84)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mfd_infineon_mxcrypto_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html#ga786996a9934b87fe322e98bff53858e8)

<a id="header-details"></a>

---

[上一章](P021_zephyr__drivers__sensor__hx711.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__mfd__infineon_mxcryptolite.h_文件参考.md)
