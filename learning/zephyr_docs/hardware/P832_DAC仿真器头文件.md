---
id: learning.zephyr-docs.hardware.dacext-4
title: DAC仿真器头文件
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dac__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第832章\_DAC仿真器头文件

原文：[dac__emul_8h](https://docs.zephyrproject.org/latest/doxygen/html/dac__emul_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/dac/dac_emul.h` 提供仿真数模转换器（Emulated Digital-to-Analog Converter，Emulated DAC）的后端应用程序接口（Backend Application Programming Interface，Backend API）。头文件包含项如下；原始声明见[源码页](P833_DAC仿真器源码.md)。

```c
#include <zephyr/device.h>
#include <stdint.h>
```

## 832.1\_读取已写入的通道值

```c
int dac_emul_value_get(const struct device *dev, uint8_t channel,
                       uint32_t *value);
```

从驱动实例读取此前写入的值。**该通道必须已经完成配置。**

| 参数 | 含义 |
| --- | --- |
| `dev` | DAC仿真器设备（Emulator Device） |
| `channel` | 要读取的通道编号 |
| `value` | 保存通道当前值的指针 |

[`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)／[`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) 分别为8／32位无符号整数。此接口取得的是仿真驱动已保存的通道值。

## 832.2\_返回值

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EINVAL` | 通道无效或传入 `NULL` 空指针（Null Pointer） |
| `-ENXIO` | 通道尚未配置 |
| `-EBUSY` | 未能取得通道锁（Channel Lock） |

---

[上一章：DAC161S997扩展源码](P831_DAC161S997扩展源码.md) · [下一章：DAC仿真器源码](P833_DAC仿真器源码.md) · [返回大纲](大纲.md)
