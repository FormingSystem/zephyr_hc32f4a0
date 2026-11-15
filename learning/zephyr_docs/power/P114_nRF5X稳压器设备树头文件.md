---
id: learning.zephyr-docs.power.regdtfile-14
title: nRF5X稳压器设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf5x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第114章\_nRF5X稳压器设备树头文件

原文：[nrf5x_8h](https://docs.zephyrproject.org/latest/doxygen/html/nrf5x_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供nRF5X稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/nrf5x.h`。


## 114.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/nrf5x_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P099_nRF5X稳压器设备树辅助接口.md)给出同组常量说明。

## 114.2\_稳压器模式

```c
#define NRF5X_REG_MODE_LDO 0
#define NRF5X_REG_MODE_DCDC 1
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NRF5X_REG_MODE_LDO`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html#gae0a71ea08465302fa7f741a14a6ea49f) | `0` | 低压差稳压器（Low-Dropout Regulator，LDO）模式 |
| [`NRF5X_REG_MODE_DCDC`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html#gad7aae568d96d9177fc1533d573bc6be2) | `1` | 直流转换模式（DC/DC Mode；DC为Direct Current） |

---

[上一章：nPM6001稳压器设备树头文件](P113_nPM6001稳压器设备树头文件.md) · [下一章：Infineon可编程参考设备树头文件](P115_Infineon可编程参考设备树头文件.md) · [返回大纲](大纲.md)
