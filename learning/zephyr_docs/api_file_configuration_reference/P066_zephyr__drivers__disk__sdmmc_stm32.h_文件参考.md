---
id: learning.zephyr-docs.api-file-configuration-reference.page-66
title: zephyr__drivers__disk__sdmmc_stm32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_zephyr\_\_drivers\_\_disk\_\_sdmmc\_stm32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32 SDMMC扩展磁盘（Disk）API的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <stdint.h>
```

查看此文件的源码。

STM32 SDMMC扩展磁盘（Disk）API的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 66.1\_函数（Functions）

<a id="r_gadfccc3613153a85f5b14d3b600220e42"></a>

```c
void stm32_sdmmc_get_card_cid (const struct device *dev, uint32_t cid[4])
```

相关声明：[stm32_sdmmc_get_card_cid](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#gadfccc3613153a85f5b14d3b600220e42)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SD/MMC 卡获取卡标识信息（Card Identification，CID）。

<a id="r_ga391e478b31cbe349faea2f531a0c1935"></a>

```c
void stm32_sdmmc_get_card_csd (const struct device *dev, uint32_t csd[4])
```

相关声明：[stm32_sdmmc_get_card_csd](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#ga391e478b31cbe349faea2f531a0c1935)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SD/MMC 卡获取卡特定数据信息（Card Specific Data，CSD）。


## 66.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P752_sdmmc_stm32.h_源码浏览.md)
- [stm32_sdmmc_get_card_cid](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#gadfccc3613153a85f5b14d3b600220e42)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [stm32_sdmmc_get_card_csd](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#ga391e478b31cbe349faea2f531a0c1935)

<a id="header-details"></a>

---

[上一章](P065_zephyr__drivers__sensor__s3km1110.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P067_zephyr__dt-bindings__gpio__semtech-sx1509b.h_文件参考.md)
