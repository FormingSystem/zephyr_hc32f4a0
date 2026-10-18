---
id: learning.zephyr-docs.api-file-configuration-reference.page-43
title: zephyr__input__input_paw32xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__paw32xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_input\_\_input\_paw32xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__paw32xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAW32xx输入（Input）驱动的头文件。

查看此文件的源码。

<a id="details"></a>

PAW32xx输入（Input）驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.1\_函数（Functions）

<a id="r_ga7c15c20653486833cb07a43cd92c97cf"></a>

```c
int paw32xx_set_resolution (const struct device *dev, uint16_t res_cpi)
```

相关声明：[paw32xx_set_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html#ga7c15c20653486833cb07a43cd92c97cf)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 paw32xx 设备的分辨率（Resolution）。

<a id="r_ga03c6aa7e9e7b370791c16292055b9fff"></a>

```c
int paw32xx_force_awake (const struct device *dev, bool enable)
```

相关声明：[paw32xx_force_awake](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html#ga03c6aa7e9e7b370791c16292055b9fff)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 paw32xx 设备的强制唤醒模式（Force Awake Mode）。


## 43.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P384_input_paw32xx.h_源码浏览.md)
- [paw32xx_set_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html#ga7c15c20653486833cb07a43cd92c97cf)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [paw32xx_force_awake](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html#ga03c6aa7e9e7b370791c16292055b9fff)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P042_zephyr__input__input_hid.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__input__input_pmw3610.h_文件参考.md)
