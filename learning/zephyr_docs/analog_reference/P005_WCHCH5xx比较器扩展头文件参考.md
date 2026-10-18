---
id: learning.zephyr-docs.analog_reference.analogheader-5
title: WCHCH5xx比较器扩展头文件参考
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/comparator__wch__ch5xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_WCHCH5xx比较器扩展头文件参考

原文：[comparator__wch__ch5xx_8h](https://docs.zephyrproject.org/latest/doxygen/html/comparator__wch__ch5xx_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/comparator/comparator_wch_ch5xx.h`是WCH CH5xx比较器（Comparator）驱动头文件，提供内部负端参考电平（Internal Negative Reference Level）选择接口。包含设备声明：

```c
#include <zephyr/device.h>
```

## 5.1\_负端参考电平

枚举`comp_nref_level`有16个选项，下表保留原顺序与首项显式赋值。毫伏（Millivolt，mV）值是参考电压，枚举编码并非电压本身。

| 枚举项 | 内部负端参考电平 |
| --- | --- |
| `COMP_NREF_LEVEL_50 = 0` | 50 mV |
| `COMP_NREF_LEVEL_100` | 100 mV |
| `COMP_NREF_LEVEL_150` | 150 mV |
| `COMP_NREF_LEVEL_200` | 200 mV |
| `COMP_NREF_LEVEL_250` | 250 mV |
| `COMP_NREF_LEVEL_300` | 300 mV |
| `COMP_NREF_LEVEL_350` | 350 mV |
| `COMP_NREF_LEVEL_400` | 400 mV |
| `COMP_NREF_LEVEL_450` | 450 mV |
| `COMP_NREF_LEVEL_500` | 500 mV |
| `COMP_NREF_LEVEL_550` | 550 mV |
| `COMP_NREF_LEVEL_600` | 600 mV |
| `COMP_NREF_LEVEL_650` | 650 mV |
| `COMP_NREF_LEVEL_700` | 700 mV |
| `COMP_NREF_LEVEL_750` | 750 mV |
| `COMP_NREF_LEVEL_800` | 800 mV |

## 5.2\_设置接口

下列函数为比较器设置负端参考电平：

```c
int comparator_wch_set_nref_level(const struct device *dev, enum comp_nref_level level);
```

`dev`是比较器设备，`level`是要设置的负端参考电平枚举。成功返回0，失败返回负的错误码（Error Number，errno）。

“负端参考”表示比较器负输入端使用的参考电平，不表示表中的50至800 mV应改成负电压。完整枚举定义见[源码页](P006_WCHCH5xx比较器扩展头文件源码.md)，设备树配置见[WCH CH5xx比较器绑定](../hardware/P759_WCHCH5xx比较器绑定.md)。

---

[上一章：MCUX模拟比较器扩展头文件源码](P004_MCUX模拟比较器扩展头文件源码.md) · [下一章：WCHCH5xx比较器扩展头文件源码](P006_WCHCH5xx比较器扩展头文件源码.md) · [返回大纲](大纲.md)
