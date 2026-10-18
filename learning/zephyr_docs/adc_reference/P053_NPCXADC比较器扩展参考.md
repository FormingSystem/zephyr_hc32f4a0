---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-53
title: NPCXADC比较器扩展参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第53章\_NPCXADC比较器扩展参考

原文：[adc__cmp__npcx_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/sensor/adc_cmp_npcx.h` 在传感器（Sensor）驱动目录中定义NPCX模数转换器（Analog-to-Digital Converter，ADC）比较器（Comparator）的枚举。原页列出三个枚举（Enumeration），没有函数；下文的中文含义按名称补充，全部成员和原赋值关系保留。

## 53.1\_比较关系

枚举 `adc_cmp_npcx_comparison` 按原顺序包含：

| 枚举项 | 中文含义 |
| --- | --- |
| `ADC_CMP_NPCX_GREATER` | 大于（Greater） |
| `ADC_CMP_NPCX_LESS_OR_EQUAL` | 小于或等于（Less or Equal） |

## 53.2\_阈值控制器选择

枚举 `npcx_adc_cmp_thrctl` 对应NPCX系列支持的ADC阈值控制器（Threshold Controller）。

| 枚举项 | 中文含义 |
| --- | --- |
| `ADC_CMP_NPCX_THRCTL1` | 阈值控制器1 |
| `ADC_CMP_NPCX_THRCTL2` | 阈值控制器2 |
| `ADC_CMP_NPCX_THRCTL3` | 阈值控制器3 |
| `ADC_CMP_NPCX_THRCTL4` | 阈值控制器4 |
| `ADC_CMP_NPCX_THRCTL5` | 阈值控制器5 |
| `ADC_CMP_NPCX_THRCTL6` | 阈值控制器6 |
| `ADC_CMP_NPCX_THRCTL_COUNT` | 阈值控制器数量标记（Count） |

这些成员没有显式赋值，不能把名称中的控制器编号直接当成枚举值。

## 53.3\_传感器属性

枚举 `adc_cmp_npcx_sensor_attribute` 定义电压阈值属性：

```c
enum adc_cmp_npcx_sensor_attribute {
    SENSOR_ATTR_LOWER_VOLTAGE_THRESH = SENSOR_ATTR_PRIV_START,
    SENSOR_ATTR_UPPER_VOLTAGE_THRESH,
};
```

`SENSOR_ATTR_LOWER_VOLTAGE_THRESH` 表示电压下限阈值（Lower Voltage Threshold），从私有属性起点 `SENSOR_ATTR_PRIV_START` 开始；`SENSOR_ATTR_UPPER_VOLTAGE_THRESH` 表示电压上限阈值（Upper Voltage Threshold），按枚举规则承接上一项。原页没有给出电压单位或设置函数，不在此补造调用要求。完整定义见[源码页](P054_NPCXADC比较器扩展源码.md)。

---

[上一章：MCP356xR扩展头文件源码](P052_MCP356xR扩展头文件源码.md) · [下一章：NPCXADC比较器扩展源码](P054_NPCXADC比较器扩展源码.md) · [返回大纲](大纲.md)
