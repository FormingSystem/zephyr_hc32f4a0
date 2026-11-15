---
id: learning.zephyr-docs.api-file-supplement-reference.page-129
title: zephyr__xen__console.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_zephyr\_\_xen\_\_console.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen控制台驱动（Console Driver）的内部数据。

<a id="details"></a>

```c
#include <zephyr/init.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/device_mmio.h>
```

查看此文件的源码。

Xen控制台驱动（Console Driver）的内部数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 129.1\_函数（Functions）

<a id="r_ga6e114bd3611c8d2e10541011f0c7c65e"></a>

```c
int xen_console_init (const struct device *dev)
```

相关声明：[xen_console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html#ga6e114bd3611c8d2e10541011f0c7c65e)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Xen 控制台 UART 实例（Console UART Instance）。


## 129.2\_原页交叉引用（Cross References）

- [zephyr/init.h](../device_reference/P010_系统初始化头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P002_UART驱动头文件源码.md)
- [zephyr/sys/device_mmio.h](../device_reference/P016_设备MMIO头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P245_console.h_源码浏览.md)
- [xen_console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html#ga6e114bd3611c8d2e10541011f0c7c65e)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P128_zephyr__drivers__sensor__wsen_tids_2521020222501.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P130_zephyr__dt-bindings__dma__silabs__xg21-dma.h_文件参考.md)
