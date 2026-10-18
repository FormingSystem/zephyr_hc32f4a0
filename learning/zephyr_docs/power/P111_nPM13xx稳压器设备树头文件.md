---
id: learning.zephyr-docs.power.regdtfile-11
title: nPM13xx稳压器设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm13xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第111章\_nPM13xx稳压器设备树头文件

原文：[dt-bindings_2regulator_2npm13xx_8h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm13xx_8h.html)。读取日期：2026-10-13，`latest`。

本头文件提供Nordic nPM13系列电源管理集成电路（Power Management Integrated Circuit，PMIC）稳压器驱动的**设备树辅助接口（Devicetree Helpers）**。头文件路径为 `zephyr/dt-bindings/regulator/npm13xx.h`。


BUCK表示降压转换器（Buck Converter）。GPIO表示通用输入输出（General-Purpose Input/Output）。

## 111.1\_源码与包含关系

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm13xx_8h_source.html)。本参考页未列出包含项。

相关的[设备树辅助接口](P096_nPM13xx稳压器设备树辅助接口.md)给出同组常量说明。

## 111.2\_BUCK稳压器模式

```c
#define NPM13XX_BUCK_MODE_AUTO 0x00U
#define NPM13XX_BUCK_MODE_PWM 0x01U
#define NPM13XX_BUCK_MODE_PFM 0x04U
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM13XX_BUCK_MODE_AUTO`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gaa6a9106d64b5c69eb0bcd8a49f7395cf) | `0x00U` | 自动模式（Automatic Mode） |
| [`NPM13XX_BUCK_MODE_PWM`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#ga04f737111a1c0f78e14679764a10273d) | `0x01U` | 脉宽调制（Pulse Width Modulation，PWM）模式 |
| [`NPM13XX_BUCK_MODE_PFM`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gabcc7d0fb606c6bbfa7a73a555e16b40c) | `0x04U` | 脉频调制（Pulse Frequency Modulation，PFM）模式 |

## 111.3\_LDSW与LDO稳压器模式

```c
#define NPM13XX_LDSW_MODE_LDO 0x02U
#define NPM13XX_LDSW_MODE_LDSW 0x03U
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM13XX_LDSW_MODE_LDO`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#ga4a7899bf6566240cb5488aee91d6a660) | `0x02U` | 低压差稳压器（Low-Dropout Regulator，LDO）模式 |
| [`NPM13XX_LDSW_MODE_LDSW`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gaf3b3cd08075c1f5852408a50c98c0278) | `0x03U` | 负载开关模式（Load Switch Mode，LDSW） |

## 111.4\_GPIO通道选择

```c
#define NPM13XX_GPIO_CHAN_NONE 0x00U
#define NPM13XX_GPIO_CHAN_0 0x01U
#define NPM13XX_GPIO_CHAN_1 0x02U
#define NPM13XX_GPIO_CHAN_2 0x03U
#define NPM13XX_GPIO_CHAN_3 0x04U
#define NPM13XX_GPIO_CHAN_4 0x05U
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`NPM13XX_GPIO_CHAN_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gaca83ea4645a3529feef3c6d0494123a5) | `0x00U` | 不使用GPIO通道 |
| [`NPM13XX_GPIO_CHAN_0`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#ga489b934362bcc80189ae6cb58a753d30) | `0x01U` | GPIO通道0 |
| [`NPM13XX_GPIO_CHAN_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#ga2c2eca66af7e59189c6db79f937d265a) | `0x02U` | GPIO通道1 |
| [`NPM13XX_GPIO_CHAN_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gaed068808f742637fadee82eee4e30a1e) | `0x03U` | GPIO通道2 |
| [`NPM13XX_GPIO_CHAN_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gad9e0eaf56c8789eb7edbdca0775402ee) | `0x04U` | GPIO通道3 |
| [`NPM13XX_GPIO_CHAN_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html#gaaab0ba89f22f93480c18f79d17f8a9d0) | `0x05U` | GPIO通道4 |

---

[上一章：nPM1100稳压器设备树头文件](P110_nPM1100稳压器设备树头文件.md) · [下一章：nPM2100稳压器设备树头文件](P112_nPM2100稳压器设备树头文件.md) · [返回大纲](大纲.md)
