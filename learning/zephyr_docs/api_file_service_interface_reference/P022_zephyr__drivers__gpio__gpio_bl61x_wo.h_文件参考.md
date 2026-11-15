---
id: learning.zephyr-docs.api-file-service-interface-reference.page-22
title: zephyr__drivers__gpio__gpio_bl61x_wo.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_bl61x\_wo.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__bl61x__wo_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Bouffalolab BL61x GPIO先进先出队列/线路输出（FIFO / Wire Out）的设备专用API扩展。

<a id="details"></a>

```c
#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

Bouffalolab BL61x GPIO先进先出队列/线路输出（FIFO / Wire Out）的设备专用API扩展。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 22.1\_数据结构（Data Structures）

<a id="r_bl61x_5Fwo_5Fconfig"></a>

```c
struct bl61x_wo_config
```

相关声明：[bl61x_wo_config](../hardware/P289_BL61x线输出配置.md)。

保存 GPIO 先进先出队列（FIFO）脉冲宽度、极性和引脚配置的结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.2\_宏定义（Macros）

<a id="r_gab204557fd1980f5a6f99902c9dddee87"></a>

```c
#define BL61X_WO_PIN_CNT 16
```

相关声明：[BL61X_WO_PIN_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gab204557fd1980f5a6f99902c9dddee87)。

可同时翻转（Toggle）的最大引脚数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 22.3\_类型定义（Typedefs）

<a id="r_gac45b67106001a4cdb5c1c6703c764fcd"></a>

```c
typedef void(* bl61x_wo_callback_t) (void *user_data)
```

相关声明：[bl61x_wo_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac45b67106001a4cdb5c1c6703c764fcd)。

用于通知用户异步写入（Asynchronous Write）已完成的回调类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.4\_函数（Functions）

<a id="r_gac2c0c4a647d13039f7a90c56c804b5a0"></a>

```c
uint16_t bl61x_wo_frequency_to_cycles (const uint32_t frequency, const bool exact)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bl61x_wo_frequency_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac2c0c4a647d13039f7a90c56c804b5a0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将频率转换为WO 时钟周期数（Clock Cycles）。

<a id="r_ga4644ddfda65420dbe21900d31da85828"></a>

```c
uint16_t bl61x_wo_time_to_cycles (const uint32_t time, const bool exact)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bl61x_wo_time_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga4644ddfda65420dbe21900d31da85828)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将时间转换为WO 时钟周期数（Clock Cycles）。

<a id="r_gae3412749c6176638bc5a8fc417ba2aab"></a>

```c
int bl61x_wo_configure (const struct bl61x_wo_config *const config, const uint8_t *pins, const gpio_flags_t *flags, const size_t pin_cnt)
```

相关声明：[bl61x_wo_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gae3412749c6176638bc5a8fc417ba2aab)、[bl61x_wo_config](../hardware/P289_BL61x线输出配置.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置 GPIO 先进先出缓冲区（FIFO）。

<a id="r_gabab8d53092752f0fecd864bbcaa1bb56"></a>

```c
int bl61x_wo_configure_dt (const struct bl61x_wo_config *const config, const struct gpio_dt_spec *pins, const size_t pin_cnt)
```

相关声明：[bl61x_wo_configure_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gabab8d53092752f0fecd864bbcaa1bb56)、[bl61x_wo_config](../hardware/P289_BL61x线输出配置.md)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

使用设备树（Devicetree）配置 GPIO FIFO。

<a id="r_ga49ba177988201217332721e06af7308e"></a>

```c
int bl61x_wo_write (const uint16_t *const data, const size_t len)
```

相关声明：[bl61x_wo_write](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga49ba177988201217332721e06af7308e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

写入 GPIO FIFO。

<a id="r_ga257585afa07fddec00f680d7aef38cc7"></a>

```c
int bl61x_wo_write_async (const uint16_t *const data, const size_t len, bl61x_wo_callback_t cb, void *user_data)
```

相关声明：[bl61x_wo_write_async](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga257585afa07fddec00f680d7aef38cc7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bl61x_wo_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac45b67106001a4cdb5c1c6703c764fcd)。

异步写入（Asynchronous Write）GPIO FIFO。


## 22.5\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_visible_fragment_reference/P002_gpio_bl61x_wo.h_源码浏览.md)
- [bl61x_wo_config](../hardware/P289_BL61x线输出配置.md)
- [BL61X_WO_PIN_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gab204557fd1980f5a6f99902c9dddee87)
- [bl61x_wo_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac45b67106001a4cdb5c1c6703c764fcd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bl61x_wo_frequency_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac2c0c4a647d13039f7a90c56c804b5a0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bl61x_wo_time_to_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga4644ddfda65420dbe21900d31da85828)
- [time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)
- [bl61x_wo_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gae3412749c6176638bc5a8fc417ba2aab)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bl61x_wo_configure_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gabab8d53092752f0fecd864bbcaa1bb56)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [bl61x_wo_write](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga49ba177988201217332721e06af7308e)
- [bl61x_wo_write_async](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga257585afa07fddec00f680d7aef38cc7)

<a id="header-details"></a>

---

[上一章](P021_zephyr__bluetooth__classic__goep.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__gpio__gpio_emul.h_文件参考.md)
