---
id: learning.zephyr-docs.power.regdtfile-5
title: NXP参考电压设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__vref_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第105章\_NXP参考电压设备树头文件

原文：[nxp__vref_8h](https://docs.zephyrproject.org/latest/doxygen/html/nxp__vref_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供NXP参考电压（Voltage Reference，VREF）稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/nxp_vref.h`。


## 105.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/nxp__vref_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P090_NXP参考电压设备树辅助接口.md)给出同组常量说明。

## 105.2\_参考电压模式

```c
#define NXP_VREF_MODE_STANDBY 0
#define NXP_VREF_MODE_LOW_POWER 1
#define NXP_VREF_MODE_HIGH_POWER 2
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NXP_VREF_MODE_STANDBY`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nxp__vref.html#gaafa0444f822634a90b0b1e035fb4a254) | `0` | 待机模式（Standby Mode） |
| [`NXP_VREF_MODE_LOW_POWER`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nxp__vref.html#ga2b53912bc6c2237388f648f98d320a5a) | `1` | 低功耗模式（Low Power Mode） |
| [`NXP_VREF_MODE_HIGH_POWER`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nxp__vref.html#ga3f4ed80e38130cb46933b94812b5e404) | `2` | 高功率模式（High Power Mode） |

---

[上一章：MSPM0参考电压设备树头文件](P104_MSPM0参考电压设备树头文件.md) · [下一章：RaspberryPi_Pico稳压器设备树头文件](P106_RaspberryPi_Pico稳压器设备树头文件.md) · [返回大纲](大纲.md)
