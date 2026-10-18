---
id: learning.zephyr-docs.hardware.spi
title: SPI总线
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="spi-api"></a>

# 第14章\_SPI总线

原文：[Serial Peripheral Interface (SPI) Bus](https://docs.zephyrproject.org/latest/hardware/peripherals/spi.html)。读取日期：2026-10-12，`latest`。

Zephyr **串行外设接口（Serial Peripheral Interface，SPI）**采用[编码规则 A.2 的包容性语言](../contributing/P009_编码准则.md#coding-guideline-inclusive-language)，遵循 [OSHWA 重新定义 SPI 信号名的决议](https://oshwa.org/resources/a-resolution-to-redefine-spi-signal-names/)。

## 14.1\_术语

驱动时钟的设备称为控制器（controller），被其寻址的设备称为外设（peripheral），分别对应 `SPI_OP_MODE_CONTROLLER` 与 `SPI_OP_MODE_PERIPHERAL`。

数据信号以各设备自身视角命名：SDO（Serial Data Out）为串行数据输出，SDI（Serial Data In）为串行数据输入；CS（Chip Select）为片选信号。

旧的 master/slave 与 MOSI/MISO 名称仍作为兼容别名存在。原文说明这些名称从 Zephyr v4.5 起弃用，计划在 v5.0 移除。

> 译注：上述是所读取文档的版本计划，不代表本地版本已经移除兼容符号。连接两个设备时，SDO/SDI 各自相对本设备定义，应核对发送端与接收端，不能简单按同名引脚直连。

## 14.2\_接口与示例

完整接口见 [SPI 参考](P318_SPI公共接口.md)。原页关联示例为：

- [增强型 SPI（eSPI）](../driver_samples/P053_eSPI接口示例.md)：连接设备并交换虚拟线数据包。
- [HCI SPI](../bluetooth_samples/P015_HCI_SPI传输.md)：通过 SPI 向其他设备或 **中央处理器（Central Processing Unit，CPU）** 暴露蓝牙控制器。
- [SPI 软件模拟](../driver_samples/P004_SPI软件模拟示例.md)：使用 bitbang 驱动与外设通信。
- [SPI RTIO 回环](../driver_samples/P003_SPI实时IO回环示例.md)：通过 RTIO 在 SPI 控制器与目标之间传输。
- [SPIS 唤醒](https://docs.zephyrproject.org/latest/samples/boards/nordic/spis_wakeup/README.html)：使用 SPIS 时处理唤醒线以降低电流消耗。

> 译注：eSPI 是原页关联的独立接口示例，不应据列表位置理解为任意 SPI 控制器都支持 eSPI 协议。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：I2C总线](P013_I2C总线.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：PWM脉宽调制](P015_PWM脉宽调制.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：I2C总线](P013_I2C总线.md) · [下一章：PWM脉宽调制](P015_PWM脉宽调制.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
