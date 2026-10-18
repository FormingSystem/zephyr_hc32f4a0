---
id: learning.zephyr-docs.power.regdthelp-14
title: nRF5X稳压器设备树辅助接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第99章\_nRF5X稳压器设备树辅助接口

原文：[group__regulator__nrf5x](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html)。读取日期：2026-10-13，`latest`。

本页提供nRF5X稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。相应头文件包含方式为：

```c
#include <zephyr/dt-bindings/regulator/nrf5x.h>
```

## 99.1\_稳压器模式

```c
#define NRF5X_REG_MODE_LDO 0
#define NRF5X_REG_MODE_DCDC 1
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NRF5X_REG_MODE_LDO`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html#gae0a71ea08465302fa7f741a14a6ea49f) | `0` | 低压差稳压器（Low-Dropout Regulator，LDO）模式 |
| [`NRF5X_REG_MODE_DCDC`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html#gad7aae568d96d9177fc1533d573bc6be2) | `1` | 直流转换模式（DC/DC Mode；DC为Direct Current） |

---

[上一章：nPM6001稳压器设备树辅助接口](P098_nPM6001稳压器设备树辅助接口.md) · [下一章：ADP5360稳压器设备树头文件](P100_ADP5360稳压器设备树头文件.md) · [返回大纲](大纲.md)
