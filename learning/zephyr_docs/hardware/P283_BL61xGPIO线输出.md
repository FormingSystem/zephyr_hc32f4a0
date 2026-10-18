---
id: learning.zephyr-docs.hardware.gpioextb-1
title: BL61xGPIO线输出
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第283章\_BL61xGPIO线输出

原文：[group__gpio__bl61x__wo__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html)。读取日期：2026-10-13，`latest`。

## 283.1\_接口与完成回调

本页提供 Bouffalolab BL61x 的通用输入/输出（General Purpose Input/Output，GPIO）先进先出队列（First In, First Out，FIFO）/线输出（Wire Out，WO）接口。接口自 Zephyr 4.4 提供，版本为0.1.0；声明来自 `zephyr/drivers/gpio/gpio_bl61x_wo.h`。

宏 [`BL61X_WO_PIN_CNT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gab204557fd1980f5a6f99902c9dddee87) 的值为 `16`，表示同时翻转的最大引脚数量。结构 [`bl61x_wo_config`](https://docs.zephyrproject.org/latest/doxygen/html/structbl61x__wo__config.html) 保存脉宽（Pulse Width）、极性（Polarity）等设置，参见[BL61x线输出配置](P289_BL61x线输出配置.md)。

异步写完成回调（Asynchronous Write Completion Callback）类型为：

```c
typedef void (*bl61x_wo_callback_t)(void *user_data);
```

回调从中断请求（Interrupt Request，IRQ）上下文执行。原文说明WO写入不会失败，因此回调只提供用户数据；`user_data` 为注册时提供的用户数据指针。

> 译注：上句描述完成回调不携带错误状态，不能据此忽略写入入口函数本身的错误返回值；下文两个写函数都列有 `-EIO` 或其他错误。

## 283.2\_配置引脚

函数 [`bl61x_wo_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gae3412749c6176638bc5a8fc417ba2aab) 配置GPIO FIFO：

```c
int bl61x_wo_configure(const struct bl61x_wo_config *const config,
                       const uint8_t *pins, const gpio_flags_t *flags,
                       const size_t pin_cnt);
```

`config` 指向配置结构，`pins` 指向最多16个引脚的数组，[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 给出这些引脚的标志，内部会与输出标志 `GPIO_OUTPUT` 按位或合并；`pin_cnt` 是待配置引脚数量。成功返回 `0`，配置无效返回 `-EINVAL`，也可能返回其他错误码。

函数 [`bl61x_wo_configure_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gabab8d53092752f0fecd864bbcaa1bb56) 使用设备树（Devicetree）引脚描述配置GPIO FIFO：

```c
int bl61x_wo_configure_dt(const struct bl61x_wo_config *const config,
                          const struct gpio_dt_spec *pins,
                          const size_t pin_cnt);
```

`config` 指向配置结构，`pins` 为最多16个引脚的描述数组，`pin_cnt` 为配置数量。成功返回 `0`，配置无效返回 `-EINVAL`，也可能返回其他错误码。

## 283.3\_频率与时间转换

函数 [`bl61x_wo_frequency_to_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#gac2c0c4a647d13039f7a90c56c804b5a0) 将频率换算为WO时钟周期数（Clock Cycles）：

```c
uint16_t bl61x_wo_frequency_to_cycles(const uint32_t frequency,
                                     const bool exact);
```

`frequency` 单位为Hz。通常返回最接近目标频率的周期数或 `0`；当 `exact` 为真且无法精确匹配时，返回 `0`，而不返回最接近值。

函数 [`bl61x_wo_time_to_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga4644ddfda65420dbe21900d31da85828) 将时间换算为WO时钟周期数：

```c
uint16_t bl61x_wo_time_to_cycles(const uint32_t time, const bool exact);
```

[`time`](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067) 单位为纳秒。通常返回最接近目标时间的周期数或 `0`；当 `exact` 为真且无法精确匹配时，返回 `0`，而不返回最接近值。

## 283.4\_写入翻转序列

函数 [`bl61x_wo_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga49ba177988201217332721e06af7308e) 向GPIO FIFO写入数据：

```c
int bl61x_wo_write(const uint16_t *const data, const size_t len);
```

`data` 是包含翻转序列（Sequence of Toggles）的数组，`len` 为数组长度。成功返回 `0`，失败返回输入/输出错误 `-EIO` 或其他错误码。

函数 [`bl61x_wo_write_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html#ga257585afa07fddec00f680d7aef38cc7) 异步写入GPIO FIFO：

```c
int bl61x_wo_write_async(const uint16_t *const data, const size_t len,
                         bl61x_wo_callback_t cb, void *user_data);
```

`data` 与 `len` 含义相同；`cb` 指向完成回调，`user_data` 是传给回调的用户数据。成功返回 `0`，失败返回 `-EIO` 或其他错误码。

---

[上一章：AmbiqGPIO扩展](P282_AmbiqGPIO扩展.md) · [下一章：LPCGPIO扩展](P284_LPCGPIO扩展.md) · [返回大纲](大纲.md)
