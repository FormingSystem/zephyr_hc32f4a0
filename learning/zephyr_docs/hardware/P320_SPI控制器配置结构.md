---
id: learning.zephyr-docs.hardware.spistruct-1
title: SPI控制器配置结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第320章\_SPI控制器配置结构

原文：[structspi__config](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html)。读取日期：2026-10-13，`latest`。

## 320.1\_配置对象与指针身份

[`spi_config`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html) 是串行外设接口（Serial Peripheral Interface，SPI）控制器配置结构，声明来自 `zephyr/drivers/spi.h`。

**警告：**多数驱动通过比较指针，判断本次传入的配置是否不同于上次事务的配置。只修改同一个结构对象内部的字段，可能不会被检测到。字段内容变化与配置指针变化不是同一件事。

## 320.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="aa1ec6933fe66f91653c5be488e4c9b2a"></a>[`frequency`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#aa1ec6933fe66f91653c5be488e4c9b2a) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 总线频率，单位为赫兹（Hertz，Hz） |
| <a id="a71a02ea548e187e6511abf10fdfa4829"></a>[`operation`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#a71a02ea548e187e6511abf10fdfa4829) | [`spi_operation_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga398a8ae1c4799e77fb6c067b6d47294a) | 操作标志位域（Bit Field），具体布局见下一节 |
| <a id="ae952e508c8e719098b15edf665c4eb81"></a>[`peripheral`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#ae952e508c8e719098b15edf665c4eb81) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 外设（Peripheral）编号，范围从 0 到主控制器支持的外设上限 |
| <a id="a020ca853537483b9641c37be70ab6ca0"></a>[`slave`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#a020ca853537483b9641c37be70ab6ca0) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 外设编号的旧字段名，已弃用；使用 `spi_config.peripheral` |
| <a id="a537dbfe323fafedaa219de1be2097dde"></a>[`cs`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#a537dbfe323fafedaa219de1be2097dde) | `struct spi_cs_control` | 可选的通用输入输出（General-Purpose Input/Output，GPIO）片选（Chip Select，CS）控制；不用时必须初始化为零 |
| <a id="af55961609841e6f42fb20bf807710a5d"></a>[`word_delay`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html#af55961609841e6f42fb20bf807710a5d) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 如果支持，指定串行时钟（Serial Clock，SCK）线上 SPI 数据字之间的延时，单位为纳秒 |

`peripheral` 与 `slave` 位于同一个匿名联合体（Anonymous Union）中，表示同一份外设编号。`word_delay` 为零时，会尝试使用 SCK 周期的一半作为字间延时。

## 320.3\_操作标志位布局

操作字段同时描述时钟、数据字、片选和所有权。最低有效位（Least Significant Bit，LSB）与最高有效位（Most Significant Bit，MSB）决定字内发送顺序；全双工（Full Duplex）与半双工（Half Duplex）决定两个方向是否同时传输。Motorola 和 Texas Instruments（TI）为帧格式名称使用的厂商名称。

| 位 | 原文定义 |
| --- | --- |
| 0 | 控制器或外设模式（Controller / Peripheral） |
| 1–3 | 时钟极性（Clock Polarity）、相位（Phase）及回环（Loopback）模式 |
| 4 | LSB 或 MSB 先传 |
| 5–10 | 数据帧/数据字（Data Frame / Word）的位数 |
| 11 | 全双工或半双工 |
| 12 | 如果可能，保持片选有效 |
| 13 | 为调用者保持资源锁定 |
| 14 | 片选高电平有效 |
| 15 | Motorola 或 TI 帧格式，可选 |

启用 Kconfig 配置项 [`CONFIG_SPI_EXTENDED_MODES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_EXTENDED_MODES) 后，还包括：

| 位 | 原文定义 |
| --- | --- |
| 16–17 | 数据线数：单线/双线/四线/八线（Single / Dual / Quad / Octal） |
| 18–31 | 保留供将来使用 |

---

[上一章：SPI片选控制结构](P319_SPI片选控制结构.md) · [下一章：SPI设备树描述结构](P321_SPI设备树描述结构.md) · [返回大纲](大纲.md)
