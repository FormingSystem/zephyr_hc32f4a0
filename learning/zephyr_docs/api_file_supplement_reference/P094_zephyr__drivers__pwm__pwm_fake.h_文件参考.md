---
id: learning.zephyr-docs.api-file-supplement-reference.page-94
title: zephyr__drivers__pwm__pwm_fake.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_zephyr\_\_drivers\_\_pwm\_\_pwm\_fake.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟脉宽调制（Fake PWM）驱动的API函数。

<a id="details"></a>

```c
#include <zephyr/drivers/pwm.h>
#include <zephyr/fff.h>
```

查看此文件的源码。

模拟脉宽调制（Fake PWM）驱动的API函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 94.1\_函数（Functions）

<a id="r_ga2dc0e23bd07cecf5ec38bf37b576ff57"></a>

```c
int fake_pwm_set_cycles (const struct device *, uint32_t, uint32_t, uint32_t, pwm_flags_t)
```

相关声明：[fake_pwm_set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html#ga2dc0e23bd07cecf5ec38bf37b576ff57)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)。

`pwm_driver_api::set_cycles` 驱动操作的伪实现（Fake Implementation）。


## 94.2\_原页交叉引用（Cross References）

- [zephyr/drivers/pwm.h](../pwm_driver_reference/P002_PWM驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P684_pwm_fake.h_源码浏览.md)
- [fake_pwm_set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html#ga2dc0e23bd07cecf5ec38bf37b576ff57)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [pwm_driver_api::set_cycles](../hardware/P259_PWM驱动函数表.md#a5d4e7cb7f3610fcc7a9981baf4ec3654)

<a id="header-details"></a>

---

[上一章](P093_zephyr__drivers__pcie__ptm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P095_zephyr__drivers__sensor__qdec_bee.h_文件参考.md)
