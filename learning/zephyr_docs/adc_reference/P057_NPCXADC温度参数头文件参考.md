---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-57
title: NPCXADC温度参数头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__v2t_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第57章\_NPCXADC温度参数头文件参考

原文：[adc__npcx__v2t_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__v2t_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/adc_npcx_v2t.h` 提供NPCX模数转换器（Analog-to-Digital Converter，ADC）的电压转温度（Voltage to Temperature，V2T）通道配置与查询函数。文件包含项为：

```c
#include <zephyr/device.h>
```

**这两个函数仅在启用Kconfig配置选项 `CONFIG_ADC_V2T_NPCX` 时可用。** `uint32_t` 为32位无符号整数，`dev` 均指向ADC设备实例。

## 57.1\_配置V2T通道

```c
int adc_npcx_v2t_set_channels(const struct device *dev, uint32_t channels);
```

函数 `adc_npcx_v2t_set_channels()` 设置ADC的V2T通道。参数 `channels` 是位掩码（Bit Mask），指示哪些通道配置为V2T。

成功返回0，配置失败返回负值。

## 57.2\_查询已配置的通道

```c
uint32_t adc_npcx_v2t_get_channels(const struct device *dev);
```

函数 `adc_npcx_v2t_get_channels()` 获取当前V2T通道配置，返回通道位掩码：**对应位为0表示ADC模式，为1表示V2T模式**。这里的0和1是每个通道位的含义，不把整个返回值限制成只能是0或1。

完整原始声明见[源码页](P058_NPCXADC温度参数头文件源码.md)，传感器属性入口见[NPCX温度转换扩展](P059_NPCXADC温度转换扩展参考.md)。

---

[上一章：NPCXADC阈值参数头文件源码](P056_NPCXADC阈值参数头文件源码.md) · [下一章：NPCXADC温度参数头文件源码](P058_NPCXADC温度参数头文件源码.md) · [返回大纲](大纲.md)
