---
id: learning.zephyr-docs.power.regprbheader-0
title: Infineon可编程参考设备树头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第115章\_Infineon可编程参考设备树头文件

原文：[infineon-autanalog-prb_8h](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html)。读取日期：2026-10-13，`latest`。

本头文件为Infineon AutAnalog可编程参考模块（Programmable Reference Block，PRB）稳压器提供设备树绑定常量（Devicetree Binding Constants）。头文件路径为 `zephyr/dt-bindings/regulator/infineon-autanalog-prb.h`。

这些常量与外设驱动库（Peripheral Driver Library，PDL）的枚举值一致，用于配置PRB参考电压输出的设备树属性。相关配置结构见[PRB父节点绑定](../hardware/P659_Infineon可编程参考模块绑定.md)，输出节点见[参考电压绑定](../hardware/P650_Infineon自主模拟参考电压绑定.md)。

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h_source.html)。原页没有列出包含项。

## 115.1\_源电压选择

源电压选择器（Source Voltage Selector）对应PDL枚举类型 `cy_en_autanalog_prb_src_t`。VBGR与VDDA是原页使用的源电压名称。

```c
#define IFX_AUTANALOG_PRB_SRC_VBGR 0
#define IFX_AUTANALOG_PRB_SRC_VDDA 1
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_PRB_SRC_VBGR`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#abcfc7b254597478097a560766adb9253) | `0` | VBGR源，标称电压（Nominal Voltage）0.9 V |
| [`IFX_AUTANALOG_PRB_SRC_VDDA`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a6ab5bf82c5247dd7b0f23934cab22eae) | `1` | VDDA源，最高电压（Maximum Voltage）1.8 V |

## 115.2\_抽头位置选择

抽头位置选择器（Tap Position Selector）对应PDL枚举类型 `cy_en_autanalog_prb_tap_t`。输出电压计算公式为 `((tap + 1) / 16) * Vsrc`，其中 `tap` 为抽头位置，`Vsrc` 为选定源电压。

```c
#define IFX_AUTANALOG_PRB_TAP_0 0
#define IFX_AUTANALOG_PRB_TAP_1 1
#define IFX_AUTANALOG_PRB_TAP_2 2
#define IFX_AUTANALOG_PRB_TAP_3 3
#define IFX_AUTANALOG_PRB_TAP_4 4
#define IFX_AUTANALOG_PRB_TAP_5 5
#define IFX_AUTANALOG_PRB_TAP_6 6
#define IFX_AUTANALOG_PRB_TAP_7 7
#define IFX_AUTANALOG_PRB_TAP_8 8
#define IFX_AUTANALOG_PRB_TAP_9 9
#define IFX_AUTANALOG_PRB_TAP_10 10
#define IFX_AUTANALOG_PRB_TAP_11 11
#define IFX_AUTANALOG_PRB_TAP_12 12
#define IFX_AUTANALOG_PRB_TAP_13 13
#define IFX_AUTANALOG_PRB_TAP_14 14
#define IFX_AUTANALOG_PRB_TAP_15 15
```

| 宏 | 值 | 输出电压 |
| --- | --- | --- |
| [`IFX_AUTANALOG_PRB_TAP_0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a48e3f4a8d0aea798e2f20fffba9c8a24) | `0` | 输出为 `0.0625 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#ae3683a8c24d975494911388e1103bfeb) | `1` | 输出为 `0.1250 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_2`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a92a3567653faefae55832b543bf60a27) | `2` | 输出为 `0.1875 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_3`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a80403879da00a4fe99120a4975d53c81) | `3` | 输出为 `0.2500 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_4`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a007656b62e884ddd2b1a1c4fdea2da36) | `4` | 输出为 `0.3125 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_5`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a1eb40c0641c75aa730a9910d9d352b98) | `5` | 输出为 `0.3750 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_6`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#ab1445d2f4e5df3ce5ba034d9000e35b2) | `6` | 输出为 `0.4375 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_7`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a3830e68699388fa877badef3027e3394) | `7` | 输出为 `0.5000 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_8`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a89d7b53d2da6611c76abaec82559a982) | `8` | 输出为 `0.5625 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_9`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a1bc75026e993457cd4d16e0d53c332ec) | `9` | 输出为 `0.6250 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_10`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#ab2dd654ac70446f0f057ab79e21dc851) | `10` | 输出为 `0.6875 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_11`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#aa471f7cc781b0611182130dad1d53e8e) | `11` | 输出为 `0.7500 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_12`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a97dd37b92f9711991925cda3962aa43c) | `12` | 输出为 `0.8125 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_13`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a36e927310ea22498f2eb96f9418291f1) | `13` | 输出为 `0.8750 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_14`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a14495f0b7c585849163588bd5766bd8c) | `14` | 输出为 `0.9375 * Vsrc` |
| [`IFX_AUTANALOG_PRB_TAP_15`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-prb_8h.html#a79ec7b2e9abccfd4f96a8f429de27417) | `15` | 输出为 `1.0000 * Vsrc` |

---

[上一章：nRF5X稳压器设备树头文件](P114_nRF5X稳压器设备树头文件.md) · [返回大纲](大纲.md)
