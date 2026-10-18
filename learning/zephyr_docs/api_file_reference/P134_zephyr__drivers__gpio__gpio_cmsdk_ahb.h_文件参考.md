---
id: learning.zephyr-docs.api-file-reference.page-134
title: zephyr__drivers__gpio__gpio_cmsdk_ahb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_cmsdk\_ahb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 134.1\_数据结构（Data Structures）

<a id="r_gpio_5Fcmsdk_5Fahb"></a>

```c
struct gpio_cmsdk_ahb
```

相关声明：[gpio_cmsdk_ahb](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 134.2\_函数（Functions）

<a id="r_aff8513705856d9a28013299a93649691"></a>

```c
int cmsdk_ahb_gpio_config (const struct device *dev, uint32_t mask, gpio_flags_t flags)
```

相关声明：[cmsdk_ahb_gpio_config](#aff8513705856d9a28013299a93649691)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

## 134.3\_详细说明（Detailed Documentation）

<a id="aff8513705856d9a28013299a93649691"></a>

### `cmsdk_ahb_gpio_config()`

```c
int cmsdk_ahb_gpio_config ( const struct device * dev, uint32_t mask, gpio_flags_t flags )
```


## 134.4\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h_source.html)
- [gpio_cmsdk_ahb](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P133_zephyr__xen__generic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P135_zephyr__drivers__gpio__gpio_intel.h_文件参考.md)
