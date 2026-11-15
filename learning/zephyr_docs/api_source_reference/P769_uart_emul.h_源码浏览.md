---
id: learning.zephyr-docs.api-source-reference.page-769
title: uart_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第769章\_uart\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P359_UART模拟控制接口.md)。

## 769.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aserial_2uart__emul_8h_html_a1b7ee65706693f0489e6464bc04f689b"></a>
<a id="aserial_2uart__emul_8h_html_a305c155ed8a824e7ddec0ad078669aa0"></a>
<a id="aserial_2uart__emul_8h_html_a33278a5d083c2bb26cbd11088a1cba2e"></a>
<a id="aserial_2uart__emul_8h_html_ad0a91bf5b91639c912f41bd93aeacd69"></a>
<a id="aserial_2uart__emul_8h_html_ad31912ff18e7c7faf9849322d9c8a55b"></a>
<a id="aserial_2uart__emul_8h_html_ae8aba3de78a625318524abfd46da1daa"></a>
<a id="aserial_2uart__emul_8h_html_af15ff078214f0c7a96fc8c0091a8f922"></a>
<a id="aserial_2uart__emul_8h_html_af3abd76a768e8031a1bba533f74044be"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>

```c
/*
 * Copyright (c) 2023 Fabian Blatz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SERIAL_UART_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_SERIAL_UART_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void (*uart_emul_callback_tx_data_ready_t)(const struct device *dev, size_t size,
                                                   void *user_data);

void uart_emul_callback_tx_data_ready_set(const struct device *dev,
                                          uart_emul_callback_tx_data_ready_t cb, void *user_data);

uint32_t uart_emul_put_rx_data(const struct device *dev, const uint8_t *data, size_t size);

uint32_t uart_emul_get_tx_data(const struct device *dev, uint8_t *data, size_t size);

uint32_t uart_emul_flush_rx_data(const struct device *dev);

uint32_t uart_emul_flush_tx_data(const struct device *dev);

void uart_emul_set_errors(const struct device *dev, int errors);

void uart_emul_set_release_buffer_on_timeout(const struct device *dev, bool release_on_timeout);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SERIAL_UART_EMUL_H_ */
```

## 769.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Fabian Blatz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 106 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SERIAL_UART_EMUL_H_`。

## 769.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P359_UART模拟控制接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uart_emul_callback_tx_data_ready_t](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#ad31912ff18e7c7faf9849322d9c8a55b)
- [device](../device_reference/P002_设备对象结构.md)
- [uart_emul_callback_tx_data_ready_set](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#af3abd76a768e8031a1bba533f74044be)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uart_emul_put_rx_data](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#ad0a91bf5b91639c912f41bd93aeacd69)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [uart_emul_get_tx_data](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#ae8aba3de78a625318524abfd46da1daa)
- [uart_emul_flush_rx_data](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#a33278a5d083c2bb26cbd11088a1cba2e)
- [uart_emul_flush_tx_data](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#a1b7ee65706693f0489e6464bc04f689b)
- [uart_emul_set_errors](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#a305c155ed8a824e7ddec0ad078669aa0)
- [uart_emul_set_release_buffer_on_timeout](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#af15ff078214f0c7a96fc8c0091a8f922)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)

---

[上一章](P768_sensor_data_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P770_serial.h_源码浏览.md)
