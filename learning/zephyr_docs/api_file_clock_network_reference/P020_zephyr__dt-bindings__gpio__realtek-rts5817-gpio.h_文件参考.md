---
id: learning.zephyr-docs.api-file-clock-network-reference.page-20
title: zephyr__dt-bindings__gpio__realtek-rts5817-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_dt-bindings\_\_gpio\_\_realtek-rts5817-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTS5817 GPIO控制器（Controller）的定义。

查看此文件的源码。

<a id="details"></a>

瑞昱 RTS5817 GPIO 控制器定义（GPIO Controller Definitions）。本文件包含 Realtek RTS5817 SoC 的 GPIO 名称定义及专用配置标志。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="define-members-0"></a>

<a id="r_a3a89436d61c4759a1348d31ec002d03f"></a>

```c
#define GPIO_CACHE_CS2 0
```

相关声明：[GPIO_CACHE_CS2](#a3a89436d61c4759a1348d31ec002d03f)。

GPIO 名称定义（Name Definition）。

<a id="r_a837c31cd31245179c3e2f77924f26250"></a>

```c
#define GPIO_SSI_M_MISO 4
```

相关声明：[GPIO_SSI_M_MISO](#a837c31cd31245179c3e2f77924f26250)。

SPI1 主设备（Master）的 MISO。

<a id="r_a8a422755f090c343f145a4657679a324"></a>

```c
#define GPIO_SSI_M_MOSI 5
```

相关声明：[GPIO_SSI_M_MOSI](#a8a422755f090c343f145a4657679a324)。

SPI1 主设备（Master）的 MOSI。

<a id="r_af5b4cbb951c2dc238134ecb22e5646f6"></a>

```c
#define GPIO_SSI_M_CS 6
```

相关声明：[GPIO_SSI_M_CS](#af5b4cbb951c2dc238134ecb22e5646f6)。

SPI1 主设备（Master）的片选（CS）。

<a id="r_a1aae55075f2b95e184d6f8b54b781970"></a>

```c
#define GPIO_SSI_M_SCK 7
```

相关声明：[GPIO_SSI_M_SCK](#a1aae55075f2b95e184d6f8b54b781970)。

SPI1 主设备（Master）的时钟（SCK）。

<a id="r_ae50185bfa96f9bf92cc98d8be9776755"></a>

```c
#define GPIO_SCL0 8
```

相关声明：[GPIO_SCL0](#ae50185bfa96f9bf92cc98d8be9776755)。

I2C0 的时钟线（SCL）。

<a id="r_a5203492f39a707a87f13ecbd479eced8"></a>

```c
#define GPIO_SDA0 9
```

相关声明：[GPIO_SDA0](#a5203492f39a707a87f13ecbd479eced8)。

I2C0 的数据线（SDA）。

<a id="r_af9677dc3ef7d388e2c48b32e780d1b5a"></a>

```c
#define GPIO_SCL2 10
```

相关声明：[GPIO_SCL2](#af9677dc3ef7d388e2c48b32e780d1b5a)。

I2C2 的时钟线（SCL）。

<a id="r_aaccc9d48ccebd5b8274b9b4d606adf87"></a>

```c
#define GPIO_SDA2 11
```

相关声明：[GPIO_SDA2](#aaccc9d48ccebd5b8274b9b4d606adf87)。

I2C2 的数据线（SDA）。

<a id="r_a8a7e11ae6df393ce4bfedc2b9ea40fd3"></a>

```c
#define GPIO_SCL1 12
```

相关声明：[GPIO_SCL1](#a8a7e11ae6df393ce4bfedc2b9ea40fd3)。

I2C1 的时钟线（SCL）。

<a id="r_a24afe6130cc45d8a237cd7a33dda7b3f"></a>

```c
#define GPIO_SDA1 13
```

相关声明：[GPIO_SDA1](#a24afe6130cc45d8a237cd7a33dda7b3f)。

I2C1 的数据线（SDA）。

<a id="r_abe1d143ad51130a2d42610e4e237146c"></a>

```c
#define GPIO_SSI_S_MISO 14
```

相关声明：[GPIO_SSI_S_MISO](#abe1d143ad51130a2d42610e4e237146c)。

SPI2 从设备（Slave）的 MISO。

<a id="r_a714987a6196f2c016aee7f57460b4561"></a>

```c
#define GPIO_SSI_S_MOSI 15
```

相关声明：[GPIO_SSI_S_MOSI](#a714987a6196f2c016aee7f57460b4561)。

SPI2 从设备（Slave）的 MOSI。

<a id="r_aa15b885210b020ed458ad259cd856da4"></a>

```c
#define GPIO_SSI_S_CS 16
```

相关声明：[GPIO_SSI_S_CS](#aa15b885210b020ed458ad259cd856da4)。

SPI2 从设备（Slave）的片选（CS）。

<a id="r_abc878adbd6401643923d7a3f03ff19f0"></a>

```c
#define GPIO_SSI_S_SCK 17
```

相关声明：[GPIO_SSI_S_SCK](#abc878adbd6401643923d7a3f03ff19f0)。

SSI 从设备（Slave）的时钟（SCK）。

<a id="r_a465a14bfa53c7bec26b68a5e0d96dd0d"></a>

```c
#define GPIO_GPIO14 18
```

相关声明：[GPIO_GPIO14](#a465a14bfa53c7bec26b68a5e0d96dd0d)。

GPIO14 引脚。

<a id="r_ae4a65f8fe32dc36a81fda6c9521b8c9f"></a>

```c
#define GPIO_GPIO15 19
```

相关声明：[GPIO_GPIO15](#ae4a65f8fe32dc36a81fda6c9521b8c9f)。

GPIO15 引脚。

<a id="r_a9b3e0061091100e7c02363fb9b3592c4"></a>

```c
#define GPIO_AL0 20
```

相关声明：[GPIO_AL0](#a9b3e0061091100e7c02363fb9b3592c4)。

GPIO AL0 引脚。

<a id="r_a5395ac289ab86ed5c3d8ffd5dcc0ec2e"></a>

```c
#define GPIO_AL1 21
```

相关声明：[GPIO_AL1](#a5395ac289ab86ed5c3d8ffd5dcc0ec2e)。

GPIO AL1 引脚。

<a id="r_a244b3164e36222146018078fd3da8f4f"></a>

```c
#define GPIO_AL2 22
```

相关声明：[GPIO_AL2](#a244b3164e36222146018078fd3da8f4f)。

GPIO AL2 引脚。

<a id="r_a571fc2cdfe851fa67d5050bda7327ec3"></a>

```c
#define GPIO_SNR_RST 23
```

相关声明：[GPIO_SNR_RST](#a571fc2cdfe851fa67d5050bda7327ec3)。

指纹传感器（FP Sensor）的复位引脚（Reset Pin）。

<a id="r_afe0e5e164f8ba4317de0ad1b29a88d9d"></a>

```c
#define GPIO_SNR_CS 24
```

相关声明：[GPIO_SNR_CS](#afe0e5e164f8ba4317de0ad1b29a88d9d)。

SPI0 的片选（CS），用于指纹传感器 SPI（FP Sensor SPI）。

<a id="r_a0370a68df99e69d11a7bf590ce4e3bb4"></a>

```c
#define GPIO_SNR_GPIO 25
```

相关声明：[GPIO_SNR_GPIO](#a0370a68df99e69d11a7bf590ce4e3bb4)。

指纹传感器（FP Sensor）的 GPIO。

<a id="r_a509176e28ee4cf40819298fb2874797a"></a>

```c
#define GPI_WAKE1 26
```

相关声明：[GPI_WAKE1](#a509176e28ee4cf40819298fb2874797a)。

用于唤醒（Wake Up）的 GPI1。

<a id="r_a7f0fb98e0e41de9dcc6117e557be4424"></a>

```c
#define GPI_WAKE2 27
```

相关声明：[GPI_WAKE2](#a7f0fb98e0e41de9dcc6117e557be4424)。

用于唤醒（Wake Up）的 GPI2。

<a id="define-members-1"></a>

<a id="r_ab1d73879f708e7071ff585f39f76039e"></a>

```c
#define GPIO_POWER_3V3 BIT(8)
```

相关声明：[GPIO_POWER_3V3](#ab1d73879f708e7071ff585f39f76039e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GPIO 供电电平标志（Power Level Flags）定义。

<a id="r_a054e0ad77274af55ffbba28e16e41dda"></a>

```c
#define GPIO_POWER_1V8 BIT(9)
```

相关声明：[GPIO_POWER_1V8](#a054e0ad77274af55ffbba28e16e41dda)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电压（Voltage）：1.8 V。

## 20.2\_详细说明（Detailed Documentation）

<a id="a509176e28ee4cf40819298fb2874797a"></a>

### `GPI_WAKE1`

```c
#define GPI_WAKE1 26
```

用于唤醒（Wake Up）的 GPI1。

<a id="a7f0fb98e0e41de9dcc6117e557be4424"></a>

### `GPI_WAKE2`

```c
#define GPI_WAKE2 27
```

用于唤醒（Wake Up）的 GPI2。

<a id="a9b3e0061091100e7c02363fb9b3592c4"></a>

### `GPIO_AL0`

```c
#define GPIO_AL0 20
```

GPIO AL0 引脚。

<a id="a5395ac289ab86ed5c3d8ffd5dcc0ec2e"></a>

### `GPIO_AL1`

```c
#define GPIO_AL1 21
```

GPIO AL1 引脚。

<a id="a244b3164e36222146018078fd3da8f4f"></a>

### `GPIO_AL2`

```c
#define GPIO_AL2 22
```

GPIO AL2 引脚。

<a id="a3a89436d61c4759a1348d31ec002d03f"></a>

### `GPIO_CACHE_CS2`

```c
#define GPIO_CACHE_CS2 0
```

GPIO 名称定义（Name Definition）。

定义 GPIO 别名（Aliases），以便访问和使用。

设备树用法示例（Example DT Usage）：

原始示例（Example）：

```c
gpios = <&gpio GPIO_AL0 0>;
```

闪存控制器（Flash Controller）的 CS2。

<a id="a465a14bfa53c7bec26b68a5e0d96dd0d"></a>

### `GPIO_GPIO14`

```c
#define GPIO_GPIO14 18
```

GPIO14 引脚。

<a id="ae4a65f8fe32dc36a81fda6c9521b8c9f"></a>

### `GPIO_GPIO15`

```c
#define GPIO_GPIO15 19
```

GPIO15 引脚。

<a id="a054e0ad77274af55ffbba28e16e41dda"></a>

### `GPIO_POWER_1V8`

```c
#define GPIO_POWER_1V8 BIT(9)
```

电压（Voltage）：1.8 V。

<a id="ab1d73879f708e7071ff585f39f76039e"></a>

### `GPIO_POWER_3V3`

```c
#define GPIO_POWER_3V3 BIT(8)
```

GPIO 供电电平标志（Power Level Flags）定义。

RTS5817 的部分 GPIO 支持两种工作电压（Operating Voltages）：1.8 V 或 3.3 V。此项为 3.3 V。

<a id="ae50185bfa96f9bf92cc98d8be9776755"></a>

### `GPIO_SCL0`

```c
#define GPIO_SCL0 8
```

I2C0 的时钟线（SCL）。

<a id="a8a7e11ae6df393ce4bfedc2b9ea40fd3"></a>

### `GPIO_SCL1`

```c
#define GPIO_SCL1 12
```

I2C1 的时钟线（SCL）。

<a id="af9677dc3ef7d388e2c48b32e780d1b5a"></a>

### `GPIO_SCL2`

```c
#define GPIO_SCL2 10
```

I2C2 的时钟线（SCL）。

<a id="a5203492f39a707a87f13ecbd479eced8"></a>

### `GPIO_SDA0`

```c
#define GPIO_SDA0 9
```

I2C0 的数据线（SDA）。

<a id="a24afe6130cc45d8a237cd7a33dda7b3f"></a>

### `GPIO_SDA1`

```c
#define GPIO_SDA1 13
```

I2C1 的数据线（SDA）。

<a id="aaccc9d48ccebd5b8274b9b4d606adf87"></a>

### `GPIO_SDA2`

```c
#define GPIO_SDA2 11
```

I2C2 的数据线（SDA）。

<a id="afe0e5e164f8ba4317de0ad1b29a88d9d"></a>

### `GPIO_SNR_CS`

```c
#define GPIO_SNR_CS 24
```

SPI0 的片选（CS），用于指纹传感器 SPI（FP Sensor SPI）。

<a id="a0370a68df99e69d11a7bf590ce4e3bb4"></a>

### `GPIO_SNR_GPIO`

```c
#define GPIO_SNR_GPIO 25
```

指纹传感器（FP Sensor）的 GPIO。

<a id="a571fc2cdfe851fa67d5050bda7327ec3"></a>

### `GPIO_SNR_RST`

```c
#define GPIO_SNR_RST 23
```

指纹传感器（FP Sensor）的复位引脚（Reset Pin）。

<a id="af5b4cbb951c2dc238134ecb22e5646f6"></a>

### `GPIO_SSI_M_CS`

```c
#define GPIO_SSI_M_CS 6
```

SPI1 主设备（Master）的片选（CS）。

<a id="a837c31cd31245179c3e2f77924f26250"></a>

### `GPIO_SSI_M_MISO`

```c
#define GPIO_SSI_M_MISO 4
```

SPI1 主设备（Master）的 MISO。

<a id="a8a422755f090c343f145a4657679a324"></a>

### `GPIO_SSI_M_MOSI`

```c
#define GPIO_SSI_M_MOSI 5
```

SPI1 主设备（Master）的 MOSI。

<a id="a1aae55075f2b95e184d6f8b54b781970"></a>

### `GPIO_SSI_M_SCK`

```c
#define GPIO_SSI_M_SCK 7
```

SPI1 主设备（Master）的时钟（SCK）。

<a id="aa15b885210b020ed458ad259cd856da4"></a>

### `GPIO_SSI_S_CS`

```c
#define GPIO_SSI_S_CS 16
```

SPI2 从设备（Slave）的片选（CS）。

<a id="abe1d143ad51130a2d42610e4e237146c"></a>

### `GPIO_SSI_S_MISO`

```c
#define GPIO_SSI_S_MISO 14
```

SPI2 从设备（Slave）的 MISO。

<a id="a714987a6196f2c016aee7f57460b4561"></a>

### `GPIO_SSI_S_MOSI`

```c
#define GPIO_SSI_S_MOSI 15
```

SPI2 从设备（Slave）的 MOSI。

<a id="abc878adbd6401643923d7a3f03ff19f0"></a>

### `GPIO_SSI_S_SCK`

```c
#define GPIO_SSI_S_SCK 17
```

SSI 从设备（Slave）的时钟（SCK）。


## 20.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P698_realtek-rts5817-gpio.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P019_zephyr__sys__printk.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__misc__interconn__renesas_elc__renesas_elc.h_文件参考.md)
