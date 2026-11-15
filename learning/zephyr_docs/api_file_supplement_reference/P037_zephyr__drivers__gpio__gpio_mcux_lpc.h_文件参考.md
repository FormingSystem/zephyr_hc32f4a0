---
id: learning.zephyr-docs.api-file-supplement-reference.page-37
title: zephyr__drivers__gpio__gpio_mcux_lpc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_mcux\_lpc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCUX LPC GPIO驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

NXP MCUX LPC GPIO驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.1\_函数（Functions）

<a id="r_ga6ce1efd70bb2996ac993f2a322d74ac3"></a>

```c
void gpio_mcux_lpc_trigger_cb (const struct device *dev, uint32_t pins)
```

相关声明：[gpio_mcux_lpc_trigger_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html#ga6ce1efd70bb2996ac993f2a322d74ac3)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为给定引脚触发回调（Callback）。


## 37.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P298_gpio_mcux_lpc.h_源码浏览.md)
- [gpio_mcux_lpc_trigger_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html#ga6ce1efd70bb2996ac993f2a322d74ac3)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P036_zephyr__drivers__gpio__gpio_ambiq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__drivers__gpio__gpio_nct38xx.h_文件参考.md)
