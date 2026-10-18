---
id: learning.zephyr-docs.api-file-configuration-reference.page-13
title: zephyr__drivers__haptics__cs40l26.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs40l26_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_haptics\_\_cs40l26.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cs40l26_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供CS40L26/27触觉反馈（Haptic）驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/haptics.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

提供CS40L26/27触觉反馈（Haptic）驱动API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.1\_枚举（Enumerations）

<a id="r_ga2e2d8b57fd4d7452e543acf91ebbb692"></a>

```c
enum cs40l26_source { CS40L26_SOURCE_BUZ = HAPTICS_SOURCE_PRIV_START }
```

相关声明：[cs40l26_source](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#ga2e2d8b57fd4d7452e543acf91ebbb692)、[CS40L26_SOURCE_BUZ](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#gga2e2d8b57fd4d7452e543acf91ebbb692afcf75b890d48d6aa213d4519fb642ed7)。

用于效果（Effects）的波表源（Wavetable Sources）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.2\_函数（Functions）

<a id="r_ga3e190958f3449a923d99f15cb5a435e7"></a>

```c
int cs40l26_configure_buzz (const struct device *const dev, const uint32_t frequency, const uint8_t level, const uint32_t duration)
```

相关声明：[cs40l26_configure_buzz](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#ga3e190958f3449a923d99f15cb5a435e7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置用于触觉播放（Haptic Playback）的 ROM 嗡振（ROM Buzz）。


## 13.3\_原页交叉引用（Cross References）

- [zephyr/drivers/haptics.h](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P036_cs40l26.h_源码浏览.md)
- [cs40l26_source](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#ga2e2d8b57fd4d7452e543acf91ebbb692)
- [CS40L26_SOURCE_BUZ](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#gga2e2d8b57fd4d7452e543acf91ebbb692afcf75b890d48d6aa213d4519fb642ed7)
- [cs40l26_configure_buzz](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html#ga3e190958f3449a923d99f15cb5a435e7)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P012_zephyr__net__coap_link_format.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__input__cy8cmbr3xxx.h_文件参考.md)
