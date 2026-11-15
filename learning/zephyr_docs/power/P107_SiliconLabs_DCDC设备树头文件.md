---
id: learning.zephyr-docs.power.regdtfile-7
title: SiliconLabs_DCDC设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs__dcdc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第107章\_SiliconLabs_DCDC设备树头文件

原文：[silabs__dcdc_8h](https://docs.zephyrproject.org/latest/doxygen/html/silabs__dcdc_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供Silicon Labs直流到直流（DC-to-DC，DC为Direct Current）稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/silabs_dcdc.h`。


## 107.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/silabs__dcdc_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P092_SiliconLabs_DCDC设备树辅助接口.md)给出同组常量说明。

## 107.2\_直流转换模式

```c
#define SILABS_DCDC_MODE_BUCK 0
#define SILABS_DCDC_MODE_BOOST 1
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`SILABS_DCDC_MODE_BUCK`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__silabs__dcdc.html#ga15c978649938cb62eb55320484ea96ad) | `0` | 降压模式（Buck Mode） |
| [`SILABS_DCDC_MODE_BOOST`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__silabs__dcdc.html#gae15aea17f55c8e88dadc3df044933157) | `1` | 升压模式（Boost Mode） |

---

[上一章：RaspberryPi_Pico稳压器设备树头文件](P106_RaspberryPi_Pico稳压器设备树头文件.md) · [下一章：TPS6287x稳压器设备树头文件](P108_TPS6287x稳压器设备树头文件.md) · [返回大纲](大纲.md)
