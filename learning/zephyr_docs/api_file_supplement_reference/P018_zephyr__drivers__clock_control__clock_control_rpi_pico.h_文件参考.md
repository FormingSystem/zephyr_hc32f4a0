---
id: learning.zephyr-docs.api-file-supplement-reference.page-18
title: zephyr__drivers__clock_control__clock_control_rpi_pico.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rpi__pico_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_rpi\_pico.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rpi__pico_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Raspberry Pi Pico设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

Raspberry Pi Pico设备的时钟控制定义（Clock Control Definitions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.1\_函数（Functions）

<a id="r_ga1c14aa77af4ca5a6cb24929a09c4ec30"></a>

```c
int clock_control_rpi_pico_reconfigure (const struct device *dev)
```

相关声明：[clock_control_rpi_pico_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html#ga1c14aa77af4ca5a6cb24929a09c4ec30)、[device](../device_reference/P002_设备对象结构.md)。

重新应用设备树（Devicetree）声明的外部晶体振荡器／锁相环／时钟拓扑（XOSC / PLL / Clock Topology）。


## 18.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P103_clock_control_rpi_pico.h_源码浏览.md)
- [clock_control_rpi_pico_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html#ga1c14aa77af4ca5a6cb24929a09c4ec30)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P017_zephyr__drivers__clock_control__clock_control_ambiq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__clock_control__clock_control_silabs_siwx91x.h_文件参考.md)
