---
id: learning.zephyr-docs.timer_reference.api-192
title: 时间感知GPIO驱动后端
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tgpio__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第192章\_时间感知GPIO驱动后端

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tgpio__interface__backend.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 192.1\_阅读说明与导航

> 译注：本组说明时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）的公共接口、驱动后端（Driver Backend）、结构和源码。对应[周期脉冲与时间戳示例](../driver_samples/P065_时间感知GPIO示例.md)；设备的硬件周期与操作系统时间不能直接混用。

本组：[时间感知GPIO公共接口](P191_时间感知GPIO公共接口.md) · [时间感知GPIO驱动后端](P192_时间感知GPIO驱动后端.md) · [时间感知GPIO驱动接口结构](P193_时间感知GPIO驱动接口结构.md) · [时间感知GPIO头文件参考](P194_时间感知GPIO头文件参考.md) · [时间感知GPIO头文件源码](P195_时间感知GPIO头文件源码.md)。

本分组包含实现时间感知GPIO驱动所需的API类型定义、回调函数签名及其他辅助内容。

## 192.2\_数据结构（Data Structures）

<a id="r_tgpio_5Fdriver_5Fapi"></a>

```c
struct tgpio_driver_api
```

驱动操作（Driver Operations）：时间感知GPIO驱动操作。

相关声明：[tgpio_driver_api](P193_时间感知GPIO驱动接口结构.md)。

## 192.3\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/timeaware_gpio.h)、[驱动实现](../../../drivers/timeaware_gpio/timeaware_gpio_intel.c)和[系统调用验证包装](../../../drivers/timeaware_gpio/timeaware_gpio_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/timeaware_gpio.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_intel.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P191_时间感知GPIO公共接口.md) · [返回大纲](大纲.md) · [下一章](P193_时间感知GPIO驱动接口结构.md)
