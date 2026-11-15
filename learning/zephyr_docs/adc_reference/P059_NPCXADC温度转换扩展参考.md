---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-59
title: NPCXADC温度转换扩展参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__v2t__npcx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第59章\_NPCXADC温度转换扩展参考

原文：[adc__v2t__npcx_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc__v2t__npcx_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/sensor/adc_v2t_npcx.h` 位于传感器（Sensor）驱动目录，为NPCX电压转温度（Voltage to Temperature，V2T）功能定义传感器属性枚举（Enumeration）。它包含：

```c
#include <zephyr/drivers/sensor.h>
```

## 59.1\_通道配置属性

枚举 `npcx_adc_v2t_sensor_attr` 只有一个成员，原始赋值关系如下：

```c
enum npcx_adc_v2t_sensor_attr {
    SENSOR_ATTR_NPCX_V2T_CHANNEL_CFG = SENSOR_ATTR_PRIV_START,
};
```

`SENSOR_ATTR_NPCX_V2T_CHANNEL_CFG` 是V2T通道配置（Channel Configuration）属性，从传感器私有属性起点 `SENSOR_ATTR_PRIV_START` 开始编号；保留这个符号关系，不替换成假定的整数。

## 59.2\_文件范围

原页只列出这个枚举，没有另行描述参数单位、返回值或函数。模数转换器（Analog-to-Digital Converter，ADC）驱动层的V2T通道设置／查询声明另见[温度参数头文件](P057_NPCXADC温度参数头文件参考.md)，本文件完整定义见[源码页](P060_NPCXADC温度转换扩展源码.md)。

---

[上一章：NPCXADC温度参数头文件源码](P058_NPCXADC温度参数头文件源码.md) · [下一章：NPCXADC温度转换扩展源码](P060_NPCXADC温度转换扩展源码.md) · [返回大纲](大纲.md)
