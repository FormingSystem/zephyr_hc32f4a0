---
id: learning.zephyr-docs.hardware.headers-2
title: ArducamDVP连接器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第293章\_ArducamDVP连接器

原文：[group__dvp-20pin-connector](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 293.1\_接口与术语

本页定义Arducam数字视频端口（Digital Video Port，DVP）20针或18针连接器对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/dvp-20pin-connector.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

信号中包括水平/垂直同步（Horizontal/Vertical Sync）、像素时钟（Pixel Clock）、系统时钟（System Clock）、电源使能（Power Enable）及掉电（Power Down）。末尾两个GPIO引脚仅存在于部分模块。

## 293.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`DVP_20PIN_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga58145bd4871cc8b28b6e6bb412f9ef5f) | `3` | I²C时钟引脚 | I2C clock pin. |
| [`DVP_20PIN_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga796a3794fcf657d8158f6c69ca6e723d) | `4` | I²C数据引脚 | I2C data pin. |
| [`DVP_20PIN_VS`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga5541dd217d110b47d4270f0bba21ed6a) | `5` | 垂直同步 | Vertical sync. |
| [`DVP_20PIN_HS`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#gac4697663b6261ca57d3145cbcccf38d0) | `6` | 水平同步 | Horizontal sync. |
| [`DVP_20PIN_PCLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga7b9d97b3083a739448f8c701c19f1e9a) | `7` | 用于传输数据的像素时钟 | Pixel clock used to transmit the data. |
| [`DVP_20PIN_XCLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga371640a91f1f698f82210780f83f54ff) | `8` | 系统时钟，通常为I²C通信所需 | System clock often needed for I2C communication. |
| [`DVP_20PIN_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#gab7a0e1af4afebad48c6d8ab7b27ceda5) | `9` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga84d65f9963b84283b9a65d708807c5b3) | `10` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga070ade610145532b5604dea74889f352) | `11` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga429e2d8fffa4fb31ded576e20e9e8fa2) | `12` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga931ef69ab1b7ebb7ab79253817a6d0f6) | `13` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga04cf72a20be635abecda90bf270e24f6) | `14` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga7efd3c52e078859a4214bddf5772538e) | `15` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga99957525e3e2ff645c46a49dd3aac6b1) | `16` | 并行端口数据 | Parallel port data. |
| [`DVP_20PIN_PEN`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#gacd31b75aa5b74c5f0ae8ce88a53c102c) | `17` | 电源使能 | Power Enable. |
| [`DVP_20PIN_PDN`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga9fe565b5fea04dec4341ae581b6e1409) | `18` | 掉电控制 | Power Down. |
| [`DVP_20PIN_GPIO0`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga9385baa7efeb3b0bd9014a62a89f100c) | `19` | 部分模块提供的额外GPIO引脚 | Extra GPIO pin present on some modules. |
| [`DVP_20PIN_GPIO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html#ga4306cbd71fd1b5818a203602a55a28ca) | `20` | 部分模块提供的额外GPIO引脚 | Extra GPIO pin present on some modules. |

---

[上一章：ArduCamFFC40针连接器](P292_ArduCamFFC40针连接器.md) · [下一章：ArduinoMKR排针](P294_ArduinoMKR排针.md) · [返回大纲](大纲.md)
