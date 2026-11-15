---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-75
title: Infineon自主模拟SAR驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon__autanalog__sar_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第75章\_Infineon自主模拟SAR驱动头文件参考

原文：[infineon__autanalog__sar_8h](https://docs.zephyrproject.org/latest/doxygen/html/infineon__autanalog__sar_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/infineon_autanalog_sar.h` 提供Infineon自主模拟（Autonomous Analog，AutAnalog）逐次逼近寄存器（Successive Approximation Register，SAR）模数转换器（Analog-to-Digital Converter，ADC）驱动的公共扩展应用程序接口（Application Programming Interface，API）。这些厂商专用辅助函数用于读取有限冲激响应（Finite Impulse Response，FIR）滤波器和先进先出（First In, First Out，FIFO）缓冲区。文件包含：

```c
#include <zephyr/device.h>
#include <stdint.h>
```

## 75.1\_FIR结果、限值状态与系数

四个函数依次读取FIR滤波器输出、取得范围检测（Range Detection，又称Limit）的状态位图、清除范围检测状态位，以及在运行时（Runtime）加载滤波器系数（Coefficient）。

```c
int adc_ifx_autanalog_sar_fir_read_result(const struct device *dev, uint8_t fir_idx, int32_t *result);
int adc_ifx_autanalog_sar_fir_get_limit_status(const struct device *dev, uint8_t fir_idx, uint8_t *status);
int adc_ifx_autanalog_sar_fir_clear_limit_status(const struct device *dev, uint8_t fir_idx);
int adc_ifx_autanalog_sar_fir_load_coefficients(const struct device *dev, uint8_t fir_idx, const int16_t *coefficients, uint8_t num_coefficients);
```

`fir_idx` 选择FIR实例；结果、状态、系数及系数数量分别保留 `int32_t *`、`uint8_t *`、`const int16_t *` 和 `uint8_t` 类型。

## 75.2\_FIFO数据与填充量

四个读取函数依次读取缓冲区数据、读取全部数据、同时读取数据和通道标识（Channel ID），以及取得当前填充量（Fill Level）。

```c
int adc_ifx_autanalog_sar_fifo_read(const struct device *dev, uint8_t buf_idx, int32_t *data_out, uint16_t max_words);
int adc_ifx_autanalog_sar_fifo_read_all(const struct device *dev, uint8_t buf_idx, int32_t *data_out);
int adc_ifx_autanalog_sar_fifo_read_chan_id(const struct device *dev, uint8_t buf_idx, uint8_t input, int32_t *data_out, uint8_t *chan_id_out);
int adc_ifx_autanalog_sar_fifo_get_size(const struct device *dev, uint8_t buf_idx, uint16_t *size);
```

`buf_idx` 选择缓冲区。`fifo_read` 提供 `max_words` 参数；`fifo_read_all` 没有该参数；`fifo_read_chan_id` 额外接收 `input` 并通过 `chan_id_out` 输出通道标识。保留这些签名差异，避免仅按函数名替换调用。

## 75.3\_水位中断回调与停止流

FIFO水位（Watermark）中断回调（Callback）类型如下，回调接收设备、FIFO状态和用户数据指针：

```c
typedef void (*adc_ifx_autanalog_sar_fifo_callback_t)(const struct device *dev,
                                                      uint32_t fifo_status, void *user_data);
```

下面第一个函数注册FIFO水位中断回调。第二个函数停止正在运行的实时输入输出（Real-Time I/O，RTIO）ADC数据流（Stream），并清理其软件状态。

```c
int adc_ifx_autanalog_sar_fifo_set_callback(const struct device *dev, adc_ifx_autanalog_sar_fifo_callback_t callback, void *user_data);
int adc_ifx_autanalog_sar_stream_stop(const struct device *dev);
```

函数的完整参数约束与返回值见[Infineon自动模拟SAR扩展接口](../hardware/P469_Infineon自动模拟SAR扩展接口.md)。本头文件的全部可见声明见[源码页](P076_Infineon自主模拟SAR驱动头文件源码.md)。

---

[上一章：LMP90xxx扩展头文件源码](P074_LMP90xxx扩展头文件源码.md) · [下一章：Infineon自主模拟SAR驱动头文件源码](P076_Infineon自主模拟SAR驱动头文件源码.md) · [返回大纲](大纲.md)
