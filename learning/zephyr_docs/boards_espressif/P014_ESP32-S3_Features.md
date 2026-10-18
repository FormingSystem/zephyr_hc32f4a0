---
id: learning.zephyr-docs.boards-espressif.page-14
title: ESP32-S3 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32s3-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-s3-features"></a>

# 第14章\_ESP32-S3特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32s3-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-S3是基于低功耗微控制器（MCU）的片上系统（SoC），集成2.4 GHz Wi-Fi和低功耗蓝牙（Bluetooth® LE）。它由高性能双核微处理器（Xtensa® 32位LX7）、低功耗协处理器（Low-power Coprocessor）、Wi-Fi基带（Baseband）、Bluetooth LE基带、射频模块（RF Module）及大量外设组成。

ESP32-S3片上系统（SoC）包含以下特性：


- 双核32位Xtensa微处理器（Tensilica LX7），最高运行频率240 MHz
- 增加了用于人工智能加速（AI Acceleration）的向量指令（Vector Instructions）支持
- 512 KB静态随机存储器（SRAM）
- 384 KB只读存储器（ROM）
- Wi-Fi 802.11b/g/n
- 低功耗蓝牙（Bluetooth LE）5.0，支持远距离通信（Long Range），数据速率最高2 Mbps

数字接口（Digital Interfaces）：


- 45个可编程通用输入输出（GPIO）引脚
- 4路串行外设接口（SPI）
- 1路液晶显示接口（LCD），支持8至16位并行RGB、I8080和MOTO6800，以及RGB565、YUV422、YUV420和YUV411之间的转换
- 1路8至16位数字视频端口摄像头接口（DVP Camera Interface）
- 3路通用异步收发器（UART）
- 2路I2C总线
- 2路芯片间音频接口（I2S）
- 1个遥控收发器（RMT，TX/RX）
- 1个脉冲计数器（Pulse Counter）
- LED脉宽调制控制器（PWM Controller），最多8个通道
- 1路全速USB OTG（Full-speed USB OTG）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 2个电机控制脉宽调制器（MCPWM）
- 1个SDIO主控制器（Host Controller），带2个插槽
- 通用直接存储器访问控制器（GDMA / General DMA Controller），具有5个发送通道和5个接收通道
- 1个TWAI®控制器，兼容ISO 11898-1，即CAN 2.0规范（CAN Specification 2.0）
- 可寻址RGB LED（Addressable RGB LED），由GPIO38驱动

模拟接口（Analog Interfaces）：


- 2个12位逐次逼近模数转换器（SAR ADC），最多20个通道
- 1个温度传感器（Temperature Sensor）
- 14个触摸感应输入输出引脚（Touch-sensing IOs）

定时器（Timers）：


- 4个54位通用定时器（General-purpose Timers）
- 1个52位系统定时器（System Timer）
- 3个看门狗定时器（Watchdog Timers）

低功耗（Low Power）：


- 电源管理单元（Power Management Unit），具有5种电源模式
- 超低功耗协处理器（ULP / Ultra-Low-Power Coprocessors）：ULP-RISC-V和ULP-FSM

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 4 Kbit一次性可编程存储器（OTP），用户最多可使用1792位
- 密码硬件加速（Cryptographic Hardware Acceleration）：AES-128/256、散列（Hash）、RSA、随机数发生器（RNG）、HMAC和数字签名（Digital Signature）

<a id="asymmetric-multiprocessing-amp"></a>

# 第14章\_非对称多处理（AMP / Asymmetric Multiprocessing）

采用ESP32或ESP32-S3片上系统（SoC）的开发板允许运行两个不同的应用。借助双核架构，各内核可以独立运行自定义任务，也可以通过OpenAMP框架交换数据。代码参考见[处理器间通信（IPC / Inter-Processor Communication）](../intercore_reference/P086_处理器间通信示例目录.md#inter-processor-communication-ipc)目录。

注意（Note）

AMP与串口输出支持（AMP and Serial Output Support）

在原文所述的Zephyr ESP32实现中，尚未为运行于APPCPU的应用实现对Zephyr管理的串口驱动的访问，例如`printk()`、日志（Logging）和控制台UART。因此，Zephyr提供的串口输出API仅可用于PROCPU。

作为替代办法，运行于APPCPU的应用可以使用ESP32 ROM函数，例如`ets_printf()`，输出诊断或调试信息。

更多信息见ESP32-S3数据手册或ESP32-S3技术参考手册。（[ESP32-S3数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)；[ESP32-S3技术参考手册（Technical Reference Manual）](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)）

---

[上一章](P013_ESP32-S2_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_Binary_Blobs.md)
