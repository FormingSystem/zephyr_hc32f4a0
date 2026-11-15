---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-27
title: SilabsADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_SilabsADC设备树常量参考

原文：[silabs-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/silabs-adc.h` 定义Silicon Labs模数转换器（Analog-to-Digital Converter，ADC）和增量式ADC（Incremental ADC，IADC）的输入选择宏（Macro）。原页列出145个定义，没有逐项说明；表中中文释义用于解释标识符，原始值完整保留。

## 27.1\_ADC输入

这一组使用 `ADC_INPUT_` 前缀，包括内部节点和A至D端口各16个引脚。电源名称AVDD、IOVDD、DVDD保留原节点标识。

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `ADC_INPUT_GND` | `0x0` | 接地（Ground，GND）输入 |
| `ADC_INPUT_AVDD` | `0x10` | AVDD模拟电源输入 |
| `ADC_INPUT_IOVDD` | `0x11` | IOVDD输入输出电源输入 |
| `ADC_INPUT_DVDD` | `0x12` | DVDD数字电源输入 |
| `ADC_INPUT_DECOUPLE` | `0x13` | 去耦节点（Decouple）输入 |
| `ADC_INPUT_PA0` | `0x80` | 端口引脚（Port Pin）PA0输入 |
| `ADC_INPUT_PA1` | `0x81` | 端口引脚（Port Pin）PA1输入 |
| `ADC_INPUT_PA2` | `0x82` | 端口引脚（Port Pin）PA2输入 |
| `ADC_INPUT_PA3` | `0x83` | 端口引脚（Port Pin）PA3输入 |
| `ADC_INPUT_PA4` | `0x84` | 端口引脚（Port Pin）PA4输入 |
| `ADC_INPUT_PA5` | `0x85` | 端口引脚（Port Pin）PA5输入 |
| `ADC_INPUT_PA6` | `0x86` | 端口引脚（Port Pin）PA6输入 |
| `ADC_INPUT_PA7` | `0x87` | 端口引脚（Port Pin）PA7输入 |
| `ADC_INPUT_PA8` | `0x88` | 端口引脚（Port Pin）PA8输入 |
| `ADC_INPUT_PA9` | `0x89` | 端口引脚（Port Pin）PA9输入 |
| `ADC_INPUT_PA10` | `0x8a` | 端口引脚（Port Pin）PA10输入 |
| `ADC_INPUT_PA11` | `0x8b` | 端口引脚（Port Pin）PA11输入 |
| `ADC_INPUT_PA12` | `0x8c` | 端口引脚（Port Pin）PA12输入 |
| `ADC_INPUT_PA13` | `0x8d` | 端口引脚（Port Pin）PA13输入 |
| `ADC_INPUT_PA14` | `0x8e` | 端口引脚（Port Pin）PA14输入 |
| `ADC_INPUT_PA15` | `0x8f` | 端口引脚（Port Pin）PA15输入 |
| `ADC_INPUT_PB0` | `0x90` | 端口引脚（Port Pin）PB0输入 |
| `ADC_INPUT_PB1` | `0x91` | 端口引脚（Port Pin）PB1输入 |
| `ADC_INPUT_PB2` | `0x92` | 端口引脚（Port Pin）PB2输入 |
| `ADC_INPUT_PB3` | `0x93` | 端口引脚（Port Pin）PB3输入 |
| `ADC_INPUT_PB4` | `0x94` | 端口引脚（Port Pin）PB4输入 |
| `ADC_INPUT_PB5` | `0x95` | 端口引脚（Port Pin）PB5输入 |
| `ADC_INPUT_PB6` | `0x96` | 端口引脚（Port Pin）PB6输入 |
| `ADC_INPUT_PB7` | `0x97` | 端口引脚（Port Pin）PB7输入 |
| `ADC_INPUT_PB8` | `0x98` | 端口引脚（Port Pin）PB8输入 |
| `ADC_INPUT_PB9` | `0x99` | 端口引脚（Port Pin）PB9输入 |
| `ADC_INPUT_PB10` | `0x9a` | 端口引脚（Port Pin）PB10输入 |
| `ADC_INPUT_PB11` | `0x9b` | 端口引脚（Port Pin）PB11输入 |
| `ADC_INPUT_PB12` | `0x9c` | 端口引脚（Port Pin）PB12输入 |
| `ADC_INPUT_PB13` | `0x9d` | 端口引脚（Port Pin）PB13输入 |
| `ADC_INPUT_PB14` | `0x9e` | 端口引脚（Port Pin）PB14输入 |
| `ADC_INPUT_PB15` | `0x9f` | 端口引脚（Port Pin）PB15输入 |
| `ADC_INPUT_PC0` | `0xa0` | 端口引脚（Port Pin）PC0输入 |
| `ADC_INPUT_PC1` | `0xa1` | 端口引脚（Port Pin）PC1输入 |
| `ADC_INPUT_PC2` | `0xa2` | 端口引脚（Port Pin）PC2输入 |
| `ADC_INPUT_PC3` | `0xa3` | 端口引脚（Port Pin）PC3输入 |
| `ADC_INPUT_PC4` | `0xa4` | 端口引脚（Port Pin）PC4输入 |
| `ADC_INPUT_PC5` | `0xa5` | 端口引脚（Port Pin）PC5输入 |
| `ADC_INPUT_PC6` | `0xa6` | 端口引脚（Port Pin）PC6输入 |
| `ADC_INPUT_PC7` | `0xa7` | 端口引脚（Port Pin）PC7输入 |
| `ADC_INPUT_PC8` | `0xa8` | 端口引脚（Port Pin）PC8输入 |
| `ADC_INPUT_PC9` | `0xa9` | 端口引脚（Port Pin）PC9输入 |
| `ADC_INPUT_PC10` | `0xaa` | 端口引脚（Port Pin）PC10输入 |
| `ADC_INPUT_PC11` | `0xab` | 端口引脚（Port Pin）PC11输入 |
| `ADC_INPUT_PC12` | `0xac` | 端口引脚（Port Pin）PC12输入 |
| `ADC_INPUT_PC13` | `0xad` | 端口引脚（Port Pin）PC13输入 |
| `ADC_INPUT_PC14` | `0xae` | 端口引脚（Port Pin）PC14输入 |
| `ADC_INPUT_PC15` | `0xaf` | 端口引脚（Port Pin）PC15输入 |
| `ADC_INPUT_PD0` | `0xb0` | 端口引脚（Port Pin）PD0输入 |
| `ADC_INPUT_PD1` | `0xb1` | 端口引脚（Port Pin）PD1输入 |
| `ADC_INPUT_PD2` | `0xb2` | 端口引脚（Port Pin）PD2输入 |
| `ADC_INPUT_PD3` | `0xb3` | 端口引脚（Port Pin）PD3输入 |
| `ADC_INPUT_PD4` | `0xb4` | 端口引脚（Port Pin）PD4输入 |
| `ADC_INPUT_PD5` | `0xb5` | 端口引脚（Port Pin）PD5输入 |
| `ADC_INPUT_PD6` | `0xb6` | 端口引脚（Port Pin）PD6输入 |
| `ADC_INPUT_PD7` | `0xb7` | 端口引脚（Port Pin）PD7输入 |
| `ADC_INPUT_PD8` | `0xb8` | 端口引脚（Port Pin）PD8输入 |
| `ADC_INPUT_PD9` | `0xb9` | 端口引脚（Port Pin）PD9输入 |
| `ADC_INPUT_PD10` | `0xba` | 端口引脚（Port Pin）PD10输入 |
| `ADC_INPUT_PD11` | `0xbb` | 端口引脚（Port Pin）PD11输入 |
| `ADC_INPUT_PD12` | `0xbc` | 端口引脚（Port Pin）PD12输入 |
| `ADC_INPUT_PD13` | `0xbd` | 端口引脚（Port Pin）PD13输入 |
| `ADC_INPUT_PD14` | `0xbe` | 端口引脚（Port Pin）PD14输入 |
| `ADC_INPUT_PD15` | `0xbf` | 端口引脚（Port Pin）PD15输入 |

## 27.2\_IADC输入

这一组使用 `IADC_INPUT_` 前缀。它的内部节点编码与ADC组不同，例如DVDD和DECOUPLE不能沿用上一组的值。

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `IADC_INPUT_GND` | `0x0` | 接地（Ground，GND）输入 |
| `IADC_INPUT_AVDD` | `0x10` | AVDD模拟电源输入 |
| `IADC_INPUT_IOVDD` | `0x11` | IOVDD输入输出电源输入 |
| `IADC_INPUT_VBAT` | `0x12` | 电池电压（Battery Voltage，VBAT）输入 |
| `IADC_INPUT_DVDD` | `0x14` | DVDD数字电源输入 |
| `IADC_INPUT_DECOUPLE` | `0x17` | 去耦节点（Decouple）输入 |
| `IADC_INPUT_DAC0` | `0x20` | 数模转换器（Digital-to-Analog Converter，DAC）0输入 |
| `IADC_INPUT_DAC1` | `0x20` | 数模转换器（Digital-to-Analog Converter，DAC）1输入 |
| `IADC_INPUT_AIN0` | `0x40` | 模拟输入（Analog Input）AIN0 |
| `IADC_INPUT_AIN1` | `0x40` | 模拟输入（Analog Input）AIN1 |
| `IADC_INPUT_AIN2` | `0x50` | 模拟输入（Analog Input）AIN2 |
| `IADC_INPUT_AIN3` | `0x50` | 模拟输入（Analog Input）AIN3 |
| `IADC_INPUT_PA0` | `0x80` | 端口引脚（Port Pin）PA0输入 |
| `IADC_INPUT_PA1` | `0x81` | 端口引脚（Port Pin）PA1输入 |
| `IADC_INPUT_PA2` | `0x82` | 端口引脚（Port Pin）PA2输入 |
| `IADC_INPUT_PA3` | `0x83` | 端口引脚（Port Pin）PA3输入 |
| `IADC_INPUT_PA4` | `0x84` | 端口引脚（Port Pin）PA4输入 |
| `IADC_INPUT_PA5` | `0x85` | 端口引脚（Port Pin）PA5输入 |
| `IADC_INPUT_PA6` | `0x86` | 端口引脚（Port Pin）PA6输入 |
| `IADC_INPUT_PA7` | `0x87` | 端口引脚（Port Pin）PA7输入 |
| `IADC_INPUT_PA8` | `0x88` | 端口引脚（Port Pin）PA8输入 |
| `IADC_INPUT_PA9` | `0x89` | 端口引脚（Port Pin）PA9输入 |
| `IADC_INPUT_PA10` | `0x8a` | 端口引脚（Port Pin）PA10输入 |
| `IADC_INPUT_PA11` | `0x8b` | 端口引脚（Port Pin）PA11输入 |
| `IADC_INPUT_PA12` | `0x8c` | 端口引脚（Port Pin）PA12输入 |
| `IADC_INPUT_PA13` | `0x8d` | 端口引脚（Port Pin）PA13输入 |
| `IADC_INPUT_PA14` | `0x8e` | 端口引脚（Port Pin）PA14输入 |
| `IADC_INPUT_PA15` | `0x8f` | 端口引脚（Port Pin）PA15输入 |
| `IADC_INPUT_PB0` | `0x90` | 端口引脚（Port Pin）PB0输入 |
| `IADC_INPUT_PB1` | `0x91` | 端口引脚（Port Pin）PB1输入 |
| `IADC_INPUT_PB2` | `0x92` | 端口引脚（Port Pin）PB2输入 |
| `IADC_INPUT_PB3` | `0x93` | 端口引脚（Port Pin）PB3输入 |
| `IADC_INPUT_PB4` | `0x94` | 端口引脚（Port Pin）PB4输入 |
| `IADC_INPUT_PB5` | `0x95` | 端口引脚（Port Pin）PB5输入 |
| `IADC_INPUT_PB6` | `0x96` | 端口引脚（Port Pin）PB6输入 |
| `IADC_INPUT_PB7` | `0x97` | 端口引脚（Port Pin）PB7输入 |
| `IADC_INPUT_PB8` | `0x98` | 端口引脚（Port Pin）PB8输入 |
| `IADC_INPUT_PB9` | `0x99` | 端口引脚（Port Pin）PB9输入 |
| `IADC_INPUT_PB10` | `0x9a` | 端口引脚（Port Pin）PB10输入 |
| `IADC_INPUT_PB11` | `0x9b` | 端口引脚（Port Pin）PB11输入 |
| `IADC_INPUT_PB12` | `0x9c` | 端口引脚（Port Pin）PB12输入 |
| `IADC_INPUT_PB13` | `0x9d` | 端口引脚（Port Pin）PB13输入 |
| `IADC_INPUT_PB14` | `0x9e` | 端口引脚（Port Pin）PB14输入 |
| `IADC_INPUT_PB15` | `0x9f` | 端口引脚（Port Pin）PB15输入 |
| `IADC_INPUT_PC0` | `0xa0` | 端口引脚（Port Pin）PC0输入 |
| `IADC_INPUT_PC1` | `0xa1` | 端口引脚（Port Pin）PC1输入 |
| `IADC_INPUT_PC2` | `0xa2` | 端口引脚（Port Pin）PC2输入 |
| `IADC_INPUT_PC3` | `0xa3` | 端口引脚（Port Pin）PC3输入 |
| `IADC_INPUT_PC4` | `0xa4` | 端口引脚（Port Pin）PC4输入 |
| `IADC_INPUT_PC5` | `0xa5` | 端口引脚（Port Pin）PC5输入 |
| `IADC_INPUT_PC6` | `0xa6` | 端口引脚（Port Pin）PC6输入 |
| `IADC_INPUT_PC7` | `0xa7` | 端口引脚（Port Pin）PC7输入 |
| `IADC_INPUT_PC8` | `0xa8` | 端口引脚（Port Pin）PC8输入 |
| `IADC_INPUT_PC9` | `0xa9` | 端口引脚（Port Pin）PC9输入 |
| `IADC_INPUT_PC10` | `0xaa` | 端口引脚（Port Pin）PC10输入 |
| `IADC_INPUT_PC11` | `0xab` | 端口引脚（Port Pin）PC11输入 |
| `IADC_INPUT_PC12` | `0xac` | 端口引脚（Port Pin）PC12输入 |
| `IADC_INPUT_PC13` | `0xad` | 端口引脚（Port Pin）PC13输入 |
| `IADC_INPUT_PC14` | `0xae` | 端口引脚（Port Pin）PC14输入 |
| `IADC_INPUT_PC15` | `0xaf` | 端口引脚（Port Pin）PC15输入 |
| `IADC_INPUT_PD0` | `0xb0` | 端口引脚（Port Pin）PD0输入 |
| `IADC_INPUT_PD1` | `0xb1` | 端口引脚（Port Pin）PD1输入 |
| `IADC_INPUT_PD2` | `0xb2` | 端口引脚（Port Pin）PD2输入 |
| `IADC_INPUT_PD3` | `0xb3` | 端口引脚（Port Pin）PD3输入 |
| `IADC_INPUT_PD4` | `0xb4` | 端口引脚（Port Pin）PD4输入 |
| `IADC_INPUT_PD5` | `0xb5` | 端口引脚（Port Pin）PD5输入 |
| `IADC_INPUT_PD6` | `0xb6` | 端口引脚（Port Pin）PD6输入 |
| `IADC_INPUT_PD7` | `0xb7` | 端口引脚（Port Pin）PD7输入 |
| `IADC_INPUT_PD8` | `0xb8` | 端口引脚（Port Pin）PD8输入 |
| `IADC_INPUT_PD9` | `0xb9` | 端口引脚（Port Pin）PD9输入 |
| `IADC_INPUT_PD10` | `0xba` | 端口引脚（Port Pin）PD10输入 |
| `IADC_INPUT_PD11` | `0xbb` | 端口引脚（Port Pin）PD11输入 |
| `IADC_INPUT_PD12` | `0xbc` | 端口引脚（Port Pin）PD12输入 |
| `IADC_INPUT_PD13` | `0xbd` | 端口引脚（Port Pin）PD13输入 |
| `IADC_INPUT_PD14` | `0xbe` | 端口引脚（Port Pin）PD14输入 |
| `IADC_INPUT_PD15` | `0xbf` | 端口引脚（Port Pin）PD15输入 |

## 27.3\_相同编码与生成来源

译注：原文件中 `IADC_INPUT_DAC0` 和 `IADC_INPUT_DAC1` 都是 `0x20`；AIN0和AIN1都是 `0x40`，AIN2和AIN3都是 `0x50`。本译文保留这些相同值，不自行分配不同编号。实际输入选择仍须遵循对应外设和驱动的规则。

[源码页](P028_SilabsADC设备树常量源码.md)的原注释说明：此文件由 `hal_silabs` 模块中的 `gen_adc.py` 脚本生成，不应手工编辑。该说明针对上游生成头文件，译文保留其来源与维护约束。

---

[上一章：MCUXLPADC设备树常量源码](P026_MCUXLPADC设备树常量源码.md) · [下一章：SilabsADC设备树常量源码](P028_SilabsADC设备树常量源码.md) · [返回大纲](大纲.md)
