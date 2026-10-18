---
id: learning.zephyr-docs.boards-espressif.page-9
title: ESP32-C6 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c6-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-c6-features"></a>

# 第9章\_ESP32-C6特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c6-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-C6是乐鑫（Espressif）首款集成2.4 GHz Wi-Fi 6、蓝牙5.3低功耗（Bluetooth LE）和IEEE 802.15.4协议的Wi-Fi 6片上系统（SoC）。原文介绍其具有业界领先的射频（RF）性能、可靠的安全功能和多种存储资源，面向物联网（IoT）产品。它包含一个最高160 MHz的高性能32位RISC-V处理器（HP Processor），以及一个最高20 MHz的低功耗32位RISC-V处理器（LP Processor），具有320 KB ROM、512 KB SRAM，并使用外部闪存（Flash）。

ESP32-C6包含以下特性：


- 32位RISC-V内核微控制器（Microcontroller），最高时钟频率160 MHz
- 400 KB内部随机存储器（RAM）
- 2.4 GHz Wi-Fi 802.11ax
- 完全兼容IEEE 802.11b/g/n协议
- 低功耗蓝牙（Bluetooth LE），通过Bluetooth 5.3认证
- 内部Wi-Fi与蓝牙共存机制（Co-existence Mechanism），共享同一天线
- IEEE 802.15.4，支持Zigbee和Thread

数字接口（Digital Interfaces）：


- 30个GPIO引脚（QFN40封装）或22个GPIO引脚（QFN32封装）
- 2 个 UART 接口。
- 1路低功耗通用异步收发器（LP UART）
- 1路通用串行外设接口（General-purpose SPI）
- 1 个 I2C 接口。
- 1路低功耗I2C接口（LP I2C）
- 1 个 I2S 接口。
- 1个脉冲计数器（Pulse Counter）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 1个TWAI®控制器，兼容ISO 11898-1，即CAN 2.0规范（CAN Specification 2.0）
- 1个SDIO 2.0从控制器（Slave Controller）
- LED脉宽调制控制器（PWM Controller），最多6个通道
- 1个电机控制脉宽调制器（MCPWM）
- 1个遥控外设（Remote Control Peripheral）
- 1个并行输入输出接口（PARLIO / Parallel IO Interface）
- 通用直接存储器访问控制器（GDMA / General DMA Controller），具有3个发送通道和3个接收通道
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 1个12位逐次逼近模数转换器（SAR ADC），最多7个通道
- 1个温度传感器（Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 1个54位通用定时器（General-purpose Timer）
- 3个看门狗定时器（Watchdog Timers）
- 1个模拟看门狗定时器（Analog Watchdog Timer）

低功耗（Low Power）：


- 针对典型场景设计的4种电源模式：活动（Active）、调制解调器睡眠（Modem-sleep）、浅睡眠（Light-sleep）和深度睡眠（Deep-sleep）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 4 Kbit一次性可编程存储器（OTP），用户最多可使用1792位
- 密码硬件加速（Cryptographic Hardware Acceleration）：AES-128/256、椭圆曲线密码（ECC）、HMAC、RSA、SHA、数字签名（Digital Signature）和散列（Hash）
- 随机数发生器（RNG / Random Number Generator）

<a id="low-power-cpu-lp-core"></a>

# 第9章\_低功耗处理器（LP CORE / Low-Power CPU）

ESP32-C6片上系统（SoC）具有两个RISC-V内核：高性能内核（HP CORE / High-Performance Core）和低功耗内核（LP CORE / Low-Power Core）。LP内核功耗极低，并带有中断控制器（Interrupt Controller）、调试模块（Debug Module）和用于访问存储器及外设的系统总线接口（System Bus Interface）。

LP内核默认处于睡眠模式（Sleep Mode），有以下两类应用场景：


- 对功耗不敏感的场景（Power-insensitive Scenario）：高性能处理器（HP Core）活动时，LP内核可以协助完成一些对速度和效率要求不高的控制与计算任务。
- 对功耗敏感的场景（Power-sensitive Scenario）：HP处理器为了省电而处于掉电状态（Power-down State）时，可以唤醒LP内核来处理外部唤醒事件（Wake-up Events）。

LP内核支持已完整集成到[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)中。可以在项目中加入以下配置来启用LP内核：

```text
CONFIG_ESP32_ULP_COPROC_ENABLED=y
```

代码参考见[低功耗处理器（LP CORE / Low-Power CPU）](../board_samples/P101_低功耗CPU示例目录.md#low-power-cpu-lp-core)目录。

更多信息见ESP32-C6数据手册或ESP32-C6技术参考手册。（[ESP32-C6数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)；[ESP32-C6技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf)）

---

[上一章](P008_ESP32-C5_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_ESP32-C61_Features.md)
