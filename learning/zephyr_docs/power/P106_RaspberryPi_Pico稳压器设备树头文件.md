---
id: learning.zephyr-docs.power.regdtfile-6
title: RaspberryPi_Pico稳压器设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第106章\_RaspberryPi_Pico稳压器设备树头文件

原文：[rpi__pico_8h](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供Raspberry Pi Pico片上稳压器（On-Chip Regulator）驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/rpi_pico.h`。


## 106.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P091_RaspberryPi_Pico稳压器设备树辅助接口.md)给出同组常量说明。

## 106.2\_稳压器模式

```c
#define REGULATOR_RPI_PICO_MODE_NORMAL 0x0
#define REGULATOR_RPI_PICO_MODE_HI_Z 0x2
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`REGULATOR_RPI_PICO_MODE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__rpi__pico.html#gac87ca6db9e70fe67a87b987f6e9711c9) | `0x0` | 正常工作模式（Normal Operating Mode） |
| [`REGULATOR_RPI_PICO_MODE_HI_Z`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__rpi__pico.html#gacdf5a511bbdd83712feb1ede0af5d3a5) | `0x2` | 高阻抗模式（High Impedance Mode） |

---

[上一章：NXP参考电压设备树头文件](P105_NXP参考电压设备树头文件.md) · [下一章：SiliconLabs_DCDC设备树头文件](P107_SiliconLabs_DCDC设备树头文件.md) · [返回大纲](大纲.md)
