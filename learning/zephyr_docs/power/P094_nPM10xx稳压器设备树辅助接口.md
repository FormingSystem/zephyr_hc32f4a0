---
id: learning.zephyr-docs.power.regdthelp-9
title: nPM10xx稳压器设备树辅助接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第94章\_nPM10xx稳压器设备树辅助接口

原文：[group__regulator__npm10xx](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html)。读取日期：2026-10-13，`latest`。

本页提供Nordic nPM10系列电源管理集成电路（Power Management Integrated Circuit，PMIC）稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。相应头文件包含方式为：

```c
#include <zephyr/dt-bindings/regulator/npm10xx.h>
```

BUCK表示降压转换器（Buck Converter）。GPIO表示通用输入输出（General-Purpose Input/Output）；VOUT是输出电压（Output Voltage）的标识。`BIT(n)` 表示第n位的位掩码。

## 94.1\_BUCK稳压器模式

```c
#define NPM10XX_BUCK_PWRMODE_LP BIT(0)
#define NPM10XX_BUCK_PWRMODE_ULP BIT(1)
#define NPM10XX_BUCK_PASSTHRU_OFF BIT(2)
#define NPM10XX_BUCK_PASSTHRU_ON BIT(3)
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM10XX_BUCK_PWRMODE_LP`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga19b26ddb6b1dba4b61fbe4da55ac6bbf) | `BIT(0)` | 降压稳压器低功耗模式（BUCK Low Power Mode） |
| [`NPM10XX_BUCK_PWRMODE_ULP`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga8650337627cbe516e779c4ffc472a328) | `BIT(1)` | 降压稳压器超低功耗模式（BUCK Ultra-Low Power Mode） |
| [`NPM10XX_BUCK_PASSTHRU_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga89b18ad555f65a074002d6e02d796b10) | `BIT(2)` | 禁用降压稳压器直通模式（Pass-through Mode） |
| [`NPM10XX_BUCK_PASSTHRU_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga25c716b6e45793e0a63f2957930b8662) | `BIT(3)` | 启用降压稳压器直通模式 |

## 94.2\_LDO稳压器模式

```c
#define NPM10XX_LDO_MODE_LDO BIT(0)
#define NPM10XX_LDO_MODE_LS BIT(1)
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM10XX_LDO_MODE_LDO`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#gafca196ed848e9ff75df90e119010fbde) | `BIT(0)` | 低压差稳压器（Low-Dropout Regulator，LDO）模式 |
| [`NPM10XX_LDO_MODE_LS`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga6f909ccea12d4d2746d55c3112ba641b) | `BIT(1)` | 负载开关模式（Load Switch Mode，LS） |

## 94.3\_GPIO控制

```c
#define NPM10XX_REG_GPIO_EN BIT(4)
#define NPM10XX_BUCK_GPIO_PWRMODE BIT(5)
#define NPM10XX_BUCK_GPIO_ALTVOUT BIT(6)
#define NPM10XX_REG_GPIO_NONE BIT(7)
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM10XX_REG_GPIO_EN`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#gaa422f9de45a0e22814ad6ed86655c581) | `BIT(4)` | 启用稳压器的GPIO使能控制 |
| [`NPM10XX_BUCK_GPIO_PWRMODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga7ab19922d026b603032417901061dd4c) | `BIT(5)` | 启用BUCK电源模式切换的GPIO控制 |
| [`NPM10XX_BUCK_GPIO_ALTVOUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#gac20ae42da3008fd835d863bd93333bf3) | `BIT(6)` | 启用BUCK备用输出电压（Alternate VOUT）切换的GPIO控制 |
| [`NPM10XX_REG_GPIO_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html#ga293480bc8afb9830e15cc0133721a113) | `BIT(7)` | 禁用稳压器的全部GPIO控制，不能与其他GPIO标志组合 |

**BUCK稳压器可以组合多个GPIO控制标志；`NPM10XX_REG_GPIO_NONE` 不能与其他GPIO标志组合。**

---

[上一章：TPS6287x稳压器设备树辅助接口](P093_TPS6287x稳压器设备树辅助接口.md) · [下一章：nPM1100稳压器设备树辅助接口](P095_nPM1100稳压器设备树辅助接口.md) · [返回大纲](大纲.md)
