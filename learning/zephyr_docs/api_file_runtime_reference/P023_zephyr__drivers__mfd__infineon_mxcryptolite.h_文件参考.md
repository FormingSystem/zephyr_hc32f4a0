---
id: learning.zephyr-docs.api-file-runtime-reference.page-23
title: zephyr__drivers__mfd__infineon_mxcryptolite.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcryptolite_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_mfd\_\_infineon\_mxcryptolite.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon__mxcryptolite_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MXCRYPTOLITE多功能设备（MFD）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include "cy_device_headers.h"
```

查看此文件的源码。

MXCRYPTOLITE多功能设备（MFD）驱动的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_ga4318b724c76568d2f2c528f9f18b171a"></a>

```c
CRYPTOLITE_Type * mfd_infineon_mxcryptolite_get_base (const struct device *dev)
```

相关声明：[mfd_infineon_mxcryptolite_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#ga4318b724c76568d2f2c528f9f18b171a)、[device](../device_reference/P002_设备对象结构.md)。

获取 MXCRYPTOLITE 寄存器基地址（Register Base Address）。

<a id="r_ga8b3ae73783208d75a136aded145ea43d"></a>

```c
int mfd_infineon_mxcryptolite_lock (const struct device *dev, k_timeout_t timeout)
```

相关声明：[mfd_infineon_mxcryptolite_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#ga8b3ae73783208d75a136aded145ea43d)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取共享的 MXCRYPTOLITE 访问互斥锁（Access Mutex）。

<a id="r_gaf67bd499b542ba7f831cb33c62daf5da"></a>

```c
void mfd_infineon_mxcryptolite_unlock (const struct device *dev)
```

相关声明：[mfd_infineon_mxcryptolite_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#gaf67bd499b542ba7f831cb33c62daf5da)、[device](../device_reference/P002_设备对象结构.md)。

释放共享的 MXCRYPTOLITE 访问互斥锁（Access Mutex）。


## 23.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P375_infineon_mxcryptolite.h_源码浏览.md)
- [mfd_infineon_mxcryptolite_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#ga4318b724c76568d2f2c528f9f18b171a)
- [device](../device_reference/P002_设备对象结构.md)
- [mfd_infineon_mxcryptolite_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#ga8b3ae73783208d75a136aded145ea43d)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mfd_infineon_mxcryptolite_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html#gaf67bd499b542ba7f831cb33c62daf5da)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__mfd__infineon_mxcrypto.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__input__input_keymap.h_文件参考.md)
