---
id: learning.zephyr-docs.api-file-configuration-reference.page-38
title: zephyr__xen__hvm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_xen\_\_hvm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hvm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen硬件虚拟机（HVM）的操作。

<a id="details"></a>

```c
#include <xen/public/hvm/hvm_op.h>
#include <xen/public/hvm/params.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

Xen硬件虚拟机（HVM）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 38.1\_函数（Functions）

<a id="r_gae375499424094b2f6f8059160456b53e"></a>

```c
int hvm_set_parameter (int idx, int domid, uint64_t value)
```

相关声明：[hvm_set_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gae375499424094b2f6f8059160456b53e)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

为 Xen 域（Domain）设置硬件虚拟机参数（HVM Parameter）。

<a id="r_gaa4c66d130a846c3effc5ec3052d95f82"></a>

```c
int hvm_get_parameter (int idx, int domid, uint64_t *value)
```

相关声明：[hvm_get_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gaa4c66d130a846c3effc5ec3052d95f82)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 Xen 域（Domain）获取硬件虚拟机参数（HVM Parameter）。


## 38.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P325_hvm.h_源码浏览.md)
- [hvm_set_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gae375499424094b2f6f8059160456b53e)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [hvm_get_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html#gaa4c66d130a846c3effc5ec3052d95f82)

<a id="header-details"></a>

---

[上一章](P037_zephyr__net__prometheus__histogram.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__drivers__i2c_emul.h_文件参考.md)
