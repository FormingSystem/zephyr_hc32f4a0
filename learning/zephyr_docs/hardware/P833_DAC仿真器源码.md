---
id: learning.zephyr-docs.hardware.dacext-5
title: DAC仿真器源码
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dac__emul_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第833章\_DAC仿真器源码

原文：[dac__emul_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/dac__emul_8h_source.html)。读取日期：2026-10-13，`latest`。

文件路径为 `zephyr/drivers/dac/dac_emul.h`。

本页给出仿真数模转换器（Emulated Digital-to-Analog Converter，Emulated DAC）的接口声明。网页的文件文档入口对应[DAC仿真器头文件](P832_DAC仿真器头文件.md)。

## 833.1\_声明与用途

头文件保护宏（Header Guard）使用原始名称 `ZEPHYR_INCLUDE_DRIVER_DAC_DAC_EMUL_H_`。包含项 `zephyr/device.h` 和 `stdint.h` 分别提供设备接口与固定宽度整数类型（Fixed-Width Integer Types）。函数 [`dac_emul_value_get()`](https://docs.zephyrproject.org/latest/doxygen/html/dac__emul_8h.html#adf4c2c9500300456205fe9947a7735e9) 读取已写入的通道值，参数为设备指针、通道编号和输出值指针；调用前必须配置通道，具体错误码见头文件参考页。

## 833.2\_网页源码

以下保留Doxygen源码页实际展示的代码，剔除网页行号并清理行尾空白。网页隐藏的文档注释由对应参考页提供，本节没有自行补写或修改代码。

```c


/*
 * Copyright (c) 2026 Vaisala Oyj
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVER_DAC_DAC_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVER_DAC_DAC_EMUL_H_

#include <zephyr/device.h>
#include <stdint.h>

int dac_emul_value_get(const struct device *dev, uint8_t channel, uint32_t *value);

#endif /* ZEPHYR_INCLUDE_DRIVER_DAC_DAC_EMUL_H_ */
```

---

[上一章：DAC仿真器头文件](P832_DAC仿真器头文件.md) · [下一章：DACx0508设备树常量源码](P834_DACx0508设备树常量源码.md) · [返回大纲](大纲.md)
