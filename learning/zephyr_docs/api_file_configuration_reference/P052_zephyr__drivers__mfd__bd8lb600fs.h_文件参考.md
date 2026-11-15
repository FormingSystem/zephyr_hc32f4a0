---
id: learning.zephyr-docs.api-file-configuration-reference.page-52
title: zephyr__drivers__mfd__bd8lb600fs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd_2bd8lb600fs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_drivers\_\_mfd\_\_bd8lb600fs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2bd8lb600fs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 52.1\_函数（Functions）

<a id="r_gaf155a458b77540f991d53c0827fad5cd"></a>

```c
int mfd_bd8lb600fs_set_outputs (const struct device *dev, uint32_t values)
```

相关声明：[mfd_bd8lb600fs_set_outputs](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html#gaf155a458b77540f991d53c0827fad5cd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置输出（Outputs）。

<a id="r_ga478f99d83f78a0ec0fcabeb3103df015"></a>

```c
int mfd_bd8lb600fs_get_output_diagnostics (const struct device *dev, uint32_t *old, uint32_t *ocp_or_tsd)
```

相关声明：[mfd_bd8lb600fs_get_output_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html#ga478f99d83f78a0ec0fcabeb3103df015)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取输出诊断信息（Output Diagnostics）。


## 52.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P515_bd8lb600fs.h_源码浏览.md)
- [mfd_bd8lb600fs_set_outputs](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html#gaf155a458b77540f991d53c0827fad5cd)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mfd_bd8lb600fs_get_output_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html#ga478f99d83f78a0ec0fcabeb3103df015)

---

[上一章](P051_zephyr__sys__mem_manage.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__dt-bindings__clock__microchip-smartfusion2-clock.h_文件参考.md)
