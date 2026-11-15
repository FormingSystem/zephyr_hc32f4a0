---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-55
title: NPCXADC阈值参数头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__threshold_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第55章\_NPCXADC阈值参数头文件参考

原文：[adc__npcx__threshold_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__threshold_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/adc_npcx_threshold.h` 提供NPCX模数转换器（Analog-to-Digital Converter，ADC）的阈值（Threshold）参数与控制函数。文件包含设备声明：

```c
#include <zephyr/device.h>
```

**本页三个函数均仅在选择 `CONFIG_ADC_CMP_NPCX` 配置选项时可用。** `dev` 均指向驱动实例的设备结构；`uint8_t`、`uint32_t` 分别为8位、32位无符号整数，`bool` 为布尔类型。

## 55.1\_阈值关系与参数类型

枚举（Enumeration）`adc_npcx_threshold_param_l_h` 按原顺序包含 `ADC_NPCX_THRESHOLD_PARAM_L_H_HIGHER` 和 `ADC_NPCX_THRESHOLD_PARAM_L_H_LOWER`，分别为高侧（Higher）与低侧（Lower）关系选项。原页未进一步说明相等时的判定方式。

枚举 `adc_npcx_threshold_param_type` 在参考页列出下列参数类型：

| 枚举项 | 中文说明 |
| --- | --- |
| `ADC_NPCX_THRESHOLD_PARAM_CHNSEL` | 选择用于测量的ADC通道 |
| `ADC_NPCX_THRESHOLD_PARAM_L_H` | 设置测量值与触发阈值（Assertion Threshold）之间的关系 |
| `ADC_NPCX_THRESHOLD_PARAM_THVAL` | 设置与测量数据进行比较的阈值 |
| `ADC_NPCX_THRESHOLD_PARAM_WORK` | 设置需要通知的工作队列线程（Worker Queue Thread） |

数据结构 `struct adc_npcx_threshold_param` 表示参数，完整字段说明见[NPCX阈值参数结构](../hardware/P466_NPCX_ADC阈值参数.md)。其 `type` 字段的类型为 `enum adc_npcx_threshold_param_type`，`val` 字段的类型为 `uint32_t`。

译注：[源码页](P056_NPCXADC阈值参数头文件源码.md)还保留 `ADC_NPCX_THRESHOLD_PARAM_MAX` 枚举成员，官方文件参考的枚举列表没有显示它。本译文明确区分两个页面的展示范围，不从源码中删除该成员。

## 55.2\_毫伏转换为阈值寄存器值

```c
int adc_npcx_threshold_mv_to_thrval(const struct device *dev,
                                   uint32_t val_mv, uint32_t *thrval);
```

函数 `adc_npcx_threshold_mv_to_thrval()` 把毫伏（Millivolt，mV）输入值转换成相应的阈值寄存器值（Threshold Register Value）。

| 参数 | 含义 |
| --- | --- |
| `dev` | 驱动实例的设备结构指针 |
| `val_mv` | 待转换的毫伏输入值 |
| `thrval` | 指向用于保存转换结果的变量 |

成功返回0；输入因溢出（Overflow）无法转换时返回负值。

## 55.3\_设置阈值参数

```c
int adc_npcx_threshold_ctrl_set_param(const struct device *dev,
                                     const uint8_t th_sel,
                                     const struct adc_npcx_threshold_param *param);
```

函数 `adc_npcx_threshold_ctrl_set_param()` 设置ADC阈值参数。`dev` 为驱动实例设备结构指针，`th_sel` 为选定的阈值，`param` 指向参数结构；支持的参数见前述结构与枚举。

成功返回0，失败返回负错误码（Negative Error Code）。

## 55.4\_使能或禁用阈值中断

```c
int adc_npcx_threshold_ctrl_enable(const struct device *dev,
                                  uint8_t th_sel, const bool enable);
```

函数 `adc_npcx_threshold_ctrl_enable()` 使能或禁用ADC阈值中断（Threshold Interrupt）。`dev` 为驱动实例设备结构指针，`th_sel` 指定阈值，`enable` 指定使能或禁用中断。

成功返回0，失败返回负错误码。**使能阈值中断之前必须配置所有参数，否则会返回错误。**

---

[上一章：NPCXADC比较器扩展源码](P054_NPCXADC比较器扩展源码.md) · [下一章：NPCXADC阈值参数头文件源码](P056_NPCXADC阈值参数头文件源码.md) · [返回大纲](大纲.md)
