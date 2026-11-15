---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-29
title: SilabsSiWx91xADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-siwx91x-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第29章\_SilabsSiWx91xADC设备树常量参考

原文：[silabs-siwx91x-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-siwx91x-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/silabs-siwx91x-adc.h` 定义SiWx91x模数转换器（Analog-to-Digital Converter，ADC）的正输入选择宏（Macro）。它们用于设备树（Devicetree）属性 `zephyr,input-positive`，把通用输入输出（General-Purpose Input/Output，GPIO）引脚映射到ADC通道。

## 29.1\_引脚组与选择编码

原源码注释将ULP GPIO（0至15）称为超低功耗GPIO（Ultra Low Power GPIO），将HP GPIO（25至30）称为高功率GPIO（High Power GPIO）。本译文按原注释保留HP的High Power措辞。下面是文件实际定义的18个选择宏，并非为注释范围内每个引脚都定义了宏。

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `SIWX91X_ADC_INPUT_ULP0` | `0` | ULP0引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP2` | `1` | ULP2引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP4` | `2` | ULP4引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP6` | `3` | ULP6引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP8` | `4` | ULP8引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP10` | `5` | ULP10引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP25` | `6` | HP25引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP27` | `7` | HP27引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP29` | `8` | HP29引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP1` | `10` | ULP1引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP3` | `11` | ULP3引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP5` | `12` | ULP5引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP11` | `13` | ULP11引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP9` | `14` | ULP9引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_ULP7` | `15` | ULP7引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP26` | `16` | HP26引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP28` | `17` | HP28引脚的ADC正输入选择 |
| `SIWX91X_ADC_INPUT_HP30` | `18` | HP30引脚的ADC正输入选择 |

## 29.2\_设备树使用与引脚模式

原源码注释中的设备树用法如下，表示映射到ULP4引脚：

```dts
zephyr,input-positive = <SIWX91X_ADC_INPUT_ULP4>;  // Maps to ULP4 pin
```

**必须另行在设备树中设置引脚控制（Pin Control，pinctrl），以启用GPIO引脚的模拟模式（Analog Mode）。** 输入选择宏本身不会代替这一步。完整原注释与定义见[源码页](P030_SilabsSiWx91xADC设备树常量源码.md)。

译注：ULP11、ULP9、ULP7对应的编码依次是13、14、15，不能按引脚编号排序后重新分配；原定义也没有编码9。

---

[上一章：SilabsADC设备树常量源码](P028_SilabsADC设备树常量源码.md) · [下一章：SilabsSiWx91xADC设备树常量源码](P030_SilabsSiWx91xADC设备树常量源码.md) · [返回大纲](大纲.md)
