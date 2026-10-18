---
id: learning.zephyr-docs.power.regdtfile-4
title: MSPM0参考电压设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__vref_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第104章\_MSPM0参考电压设备树头文件

原文：[mspm0__vref_8h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__vref_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供Texas Instruments MSPM0参考电压（Voltage Reference，VREF）稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/mspm0_vref.h`。


## 104.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__vref_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P089_MSPM0参考电压设备树辅助接口.md)给出同组常量说明。

## 104.2\_参考电压模式

```c
#define MSPM0_VREF_MODE_NORMAL 0
#define MSPM0_VREF_MODE_SHMODE 1
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`MSPM0_VREF_MODE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__mspm0__vref.html#gab99d544a430e9085600f61e31e9cfca5) | `0` | 正常工作模式（Normal Operating Mode） |
| [`MSPM0_VREF_MODE_SHMODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__mspm0__vref.html#ga82d0657395301bbf6aaa1a1d04051430) | `1` | 采样保持模式（Sample and Hold Mode） |

---

[上一章：MAX20362稳压器设备树头文件](P103_MAX20362稳压器设备树头文件.md) · [下一章：NXP参考电压设备树头文件](P105_NXP参考电压设备树头文件.md) · [返回大纲](大纲.md)
