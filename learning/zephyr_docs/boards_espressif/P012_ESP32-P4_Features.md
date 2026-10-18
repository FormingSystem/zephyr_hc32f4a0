---
id: learning.zephyr-docs.boards-espressif.page-12
title: ESP32-P4 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32p4-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-p4-features"></a>

# 第12章\_ESP32-P4特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32p4-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-P4是乐鑫高性能MCU，具有最高400 MHz的双核32位RISC-V高性能（HP）处理器，以及一个低功耗（LP）32位RISC-V协处理器。它面向人机界面（HMI）及边缘计算应用，集成二级缓存（L2 Cache）、高带宽存储器接口及丰富连接选项。

ESP32-P4包含以下功能：


- 双核32位RISC-V高性能处理器，最高400 MHz
- 32位RISC-V低功耗处理器，最高40 MHz
- 768 KB高性能SRAM
- 32 KB低功耗SRAM
- 128 KB只读存储器（ROM）
- 一级指令及数据缓存，加统一二级缓存（Unified L2 Cache）
- 最高64 MB外部PSRAM，支持十六线（HEX）或八线（Octal）模式
- 最高16 MB外部闪存

数字接口（Digital Interfaces）：


- 55个可编程GPIO
- 五路UART
- 1路低功耗通用异步收发器（LP UART）
- 两路通用SPI
- 2路I2C总线
- 1路低功耗I2C接口（LP I2C）
- 三路I2S
- 一个SDIO 3.0主机控制器，带两个插槽
- 一个USB 2.0 OTG高速（HS）接口，集成物理层（PHY）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 一个10/100 Mbit以太网媒体访问控制器（MAC），采用RMII接口
- 一个MIPI摄像头串行接口（CSI）
- 一个MIPI显示串行接口（DSI）
- 一个JPEG编解码器（Codec）
- 一个二维像素处理加速器（PPA / Pixel Processing Accelerator）
- LED脉宽调制控制器（PWM Controller），最多8个通道
- 两个电机控制PWM（MCPWM）
- 三个TWAI控制器，兼容ISO 11898-1，即CAN规范2.0
- 1个脉冲计数器（Pulse Counter）
- 一个远程控制外设（Remote Control Peripheral）
- 通过AHB及AXI总线工作的通用DMA控制器（GDMA）
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 一个12位SAR ADC
- 1个温度传感器（Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 两个54位通用定时器
- 两个看门狗定时器

低功耗（Low Power）：


- 面向典型场景的多种电源模式：活动（Active）、调制解调器睡眠（Modem-Sleep）、浅度睡眠（Light-Sleep）及深度睡眠（Deep-Sleep）
- 四通道可编程片上低压差稳压器（LDO）
- 带专用保持DMA（Retention DMA）的电源管理单元（PMU）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 密码硬件加速：AES-128／256、SHA、RSA、ECC、HMAC、数字签名（Digital Signature）及ECDSA
- 真随机数发生器（TRNG）
- 密钥管理器（Key Manager）

<a id="low-power-cpu-lp-core"></a>

# 第12章\_低功耗处理器（LP CORE / Low-Power CPU）

ESP32-P4 SoC除双HP内核外，还具有一个低功耗（LP）32位RISC-V协处理器。LP内核具有超低功耗特性、中断控制器、调试模块，以及用于访问存储器和外设的系统总线接口。

LP内核默认处于睡眠模式（Sleep Mode），有以下两类应用场景：


- 对功耗不敏感的场景：HP内核处于活动状态时，LP内核可辅助执行对速度及效率要求不高的控制与计算。
- 对功耗敏感的场景：HP内核为省电而断电时，可唤醒LP内核处理某些外部唤醒事件。

LP内核支持已完整集成到[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)中。可以在项目中加入以下配置来启用LP内核：

```text
CONFIG_ESP32_ULP_COPROC_ENABLED=y
```

代码参考见[低功耗处理器（LP CORE / Low-Power CPU）](../board_samples/P101_低功耗CPU示例目录.md#low-power-cpu-lp-core)目录。

更多信息见ESP32-P4数据手册或ESP32-P4技术参考手册。（[ESP32-P4数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf)；[ESP32-P4技术参考手册（Technical Reference Manual）](https://www.espressif.com/sites/default/files/documentation/esp32-p4_technical_reference_manual_en.pdf)）

---

[上一章](P011_ESP32-H2_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_ESP32-S2_Features.md)
