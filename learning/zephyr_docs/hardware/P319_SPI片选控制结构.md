---
id: learning.zephyr-docs.hardware.spistruct-0
title: SPI片选控制结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第319章\_SPI片选控制结构

原文：[structspi__cs__control](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html)。读取日期：2026-10-13，`latest`。

## 319.1\_片选控制信息

[`spi_cs_control`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html) 是串行外设接口（Serial Peripheral Interface，SPI）的片选（Chip Select，CS）控制结构，来自 `zephyr/drivers/spi.h`。它支持通过通用输入输出（General-Purpose Input/Output，GPIO）引脚控制片选，以代替控制器内部的片选逻辑。

结构内有匿名联合体（Anonymous Union）：其中一个匿名结构保存 [`gpio`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html#a8ad907e168666c2ddca77e89f9b9f47f)、[`delay`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html#a04569d78ac7d6022ffee0c28f5d3b629)，另一个保存 [`setup_ns`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html#ab3d5a48c9e725070cf72a42365222bff)、[`hold_ns`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html#a5bb1c6185fe550f6cbc20d95bda6abab)；联合体之外有 [`cs_is_gpio`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__cs__control.html#a8614da6ccc73ce2a2a457fbd7a0882e2) 字段。联合体成员共享存储，不能把两组延时同时当成独立数据。

## 319.2\_字段及时间单位

| 字段 | 类型 | 官方说明 |
| --- | --- | --- |
| <a id="a8ad907e168666c2ddca77e89f9b9f47f"></a>`gpio` | `struct gpio_dt_spec` | 片选 GPIO 的设备树（Devicetree）描述 |
| <a id="a04569d78ac7d6022ffee0c28f5d3b629"></a>`delay` | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 开始传输前及释放片选前等待的延时，单位为微秒 |
| <a id="ab3d5a48c9e725070cf72a42365222bff"></a>`setup_ns` | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 片选建立时间（Setup/Lead Time），即首个时钟到来之前片选应保持有效多久，单位为纳秒 |
| <a id="a5bb1c6185fe550f6cbc20d95bda6abab"></a>`hold_ns` | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 片选保持时间（Hold/Lag Time），即最后一个时钟之后、解除片选之前继续保持有效多久，单位为纳秒 |
| <a id="a8614da6ccc73ce2a2a457fbd7a0882e2"></a>`cs_is_gpio` | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 原页仅列出字段；译注：公共接口用此字段标识是否由 GPIO 控制片选 |

必要时，可以把 `gpio` 内的设备指针设为 `NULL`，完全禁止片选控制。原文要求 GPIO 标志 `GPIO_ACTIVE_LOW` / `GPIO_ACTIVE_HIGH` 与 [`spi_config`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html) 的 `SPI_CS_ACTIVE_HIGH` / `SPI_CS_ACTIVE_LOW` 选项相符。

> 译注：上一句按原页保留名称及列举顺序，不表示高低电平应交叉匹配。SPI 公共接口页面只定义了 `SPI_CS_ACTIVE_HIGH`，默认是低电平有效，并未定义 `SPI_CS_ACTIVE_LOW`。实际应保持 GPIO 与 SPI 配置的有效电平一致；不要直接复制原说明中未定义的宏名。

---

[上一章：SPI公共接口](P318_SPI公共接口.md) · [下一章：SPI控制器配置结构](P320_SPI控制器配置结构.md) · [返回大纲](大纲.md)
