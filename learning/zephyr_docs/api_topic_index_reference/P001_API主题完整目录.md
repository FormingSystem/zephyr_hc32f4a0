---
id: learning.zephyr-docs.api-topic-index-reference.page-1
title: API主题完整目录
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/topics.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_API主题完整目录

原文：[Zephyr 官方主题目录（Topics）](https://docs.zephyrproject.org/latest/doxygen/html/topics.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以下列出全部主题及其简要说明。

> 译注：本页逐项对应官方目录的 1621 个主题条目，保留 12 个顶层分类及原有层级、英文名称、简要说明和链接。层级编号各段表示在相应父分类下的顺序；空说明表示原目录未提供说明。已译正文链接到本地，其他条目链接到官方页面。目录翻译不改变各主题正文的完成状态，详见[全站覆盖清单](../catalog.html)。

[设备驱动（Device Drivers）](#row_0_) · [设备模型（Device Model）。](#row_1_) · [设备树（Devicetree）](#row_2_) · [错误编号（Error numbers）](#row_3_) · [内部与系统 API（Internal and System API）](#row_4_) · [内核 API（Kernel APIs）](#row_5_) · [内存管理 API（Memory Management APIs）](#row_6_) · [操作系统服务（Operating System Services）](#row_7_) · [测试（Testing）](#row_8_) · [第三方（Third-party）](#row_9_) · [工具链抽象（Toolchain abstraction）](#row_10_) · [实用工具（Utilities）](#row_11_)

## 1.1\_设备驱动（Device Drivers）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_0_"></a><a id="arr_0_"></a>1 | [设备驱动（Device Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html) | Device Drivers | 与各类硬件外设交互的接口。 |
| <a id="row_0_0_"></a><a id="arr_0_0_"></a>1.1 | [单总线（1-Wire）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html) | 1-Wire | 1-Wire 设备接口。 |
| <a id="row_0_0_0_"></a>1.1.1 | [1-Wire 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html) | 1-Wire Driver Backend API |  |
| <a id="row_0_0_1_"></a>1.1.2 | [1-Wire 传感器 API（Sensor API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html) | 1-Wire Sensor API | 1-Wire 传感器 API（Sensor API） |
| <a id="row_0_0_2_"></a>1.1.3 | [1-Wire 数据链路层（Data link layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html) | 1-Wire data link layer | 1-Wire 数据链路层（Data link layer） |
| <a id="row_0_0_3_"></a>1.1.4 | [1-Wire 网络层（Network layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html) | 1-Wire network layer | 1-Wire 网络层（Network layer） |
| <a id="row_0_1_"></a><a id="arr_0_1_"></a>1.2 | [模数转换器（ADC）](../hardware/P463_ADC公共接口参考.md) | ADC | 模数转换器（Analog-to-Digital Converter，ADC）接口。 |
| <a id="row_0_1_0_"></a>1.2.1 | [ADC 驱动后端 API（Driver Backend API）](../hardware/P456_ADC驱动后端.md) | ADC Driver Backend API |  |
| <a id="row_0_1_1_"></a>1.2.2 | [ADS126X ADC 驱动 API（Driver API）](../hardware/P472_ADS126X驱动接口.md) | ADS126X ADC driver API | ADS126X ADC 驱动 API（Driver API） |
| <a id="row_0_1_2_"></a><a id="arr_0_1_2_"></a>1.2.3 | [设备专用 ADC API 扩展（Device-specific API extensions）](../hardware/P465_ADC设备专用扩展.md) | Device-specific ADC API extensions |  |
| <a id="row_0_1_2_0_"></a>1.2.3.1 | [ADS131M02](../hardware/P467_ADS131M02扩展接口.md) | ADS131M02 | 德州仪器（Texas Instruments）双通道 SPI ADC。 |
| <a id="row_0_1_2_1_"></a>1.2.3.2 | [ADS1x4s0x](../hardware/P468_ADS1x4s0x扩展接口.md) | ADS1x4s0x | 德州仪器（Texas Instruments）ADS1x4s0x。 |
| <a id="row_0_1_2_2_"></a>1.2.3.3 | [电流检测放大器（Current Sense Amplifier）](../hardware/P457_ADC电流检测放大器接口.md) | Current Sense Amplifier | 电流检测放大器（Current Sense Amplifier） |
| <a id="row_0_1_2_3_"></a>1.2.3.4 | [电流检测分流器（Current Sense Shunt）](../hardware/P458_ADC电流检测分流器接口.md) | Current Sense Shunt | 电流检测分流器（Current Sense Shunt） |
| <a id="row_0_1_2_4_"></a>1.2.3.5 | [英飞凌 AutAnalog 逐次逼近型 ADC（Infineon AutAnalog SAR ADC）](../hardware/P469_Infineon自动模拟SAR扩展接口.md) | Infineon AutAnalog SAR ADC | 英飞凌 AutAnalog SAR ADC 扩展 API（Extended API）。 |
| <a id="row_0_1_2_5_"></a>1.2.3.6 | [LMP90xxx](../hardware/P470_LMP90xxx扩展接口.md) | LMP90xxx | 德州仪器（Texas Instruments）LMP90xxx 模拟前端（Analog Front End，AFE）。 |
| <a id="row_0_1_2_6_"></a>1.2.3.7 | [分压器（Voltage Divider）](../hardware/P459_ADC分压器接口.md) | Voltage Divider | 分压器（Voltage Divider） |
| <a id="row_0_1_2_7_"></a>1.2.3.8 | [WisBlock 模数转换器（ADC）](../hardware/P471_WisBlock_ADC通道.md) | WisBlock ADC | WisBlock Core 模块引出 ADC 通道的常量（Constants）。 |
| <a id="row_0_1_3_"></a>1.2.4 | [仿真 ADC（Emulated ADC）](../hardware/P464_ADC模拟器接口.md) | Emulated ADC | 仿真 ADC 后端 API（Backend API）。 |
| <a id="row_0_1_4_"></a>1.2.5 | [瑞萨 RA ADC_B 通道选择器（Renesas RA ADC_B channel selectors）](../hardware/P473_Renesas_ADC_B通道选择.md) | Renesas RA ADC_B channel selectors | 瑞萨 RA ADC_B 控制器的物理模拟输入通道标识符（Physical analog input channel identifiers）。 |
| <a id="row_0_2_"></a><a id="arr_0_2_"></a>1.3 | [音频（Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__interface.html) | Audio | 音频设备接口。 |
| <a id="row_0_2_0_"></a><a id="arr_0_2_0_"></a>1.3.1 | [音频编解码器接口（Audio Codec Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html) | Audio Codec Interface | 音频编解码器的抽象（Abstraction）。 |
| <a id="row_0_2_0_0_"></a>1.3.1.1 | [音频编解码器驱动后端 API（Audio Codec Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html) | Audio Codec Driver Backend API |  |
| <a id="row_0_2_0_1_"></a><a id="arr_0_2_0_1_"></a>1.3.1.2 | [设备专用音频编解码器 API 扩展（Device-specific audio codec API extensions）。](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__ext.html) | Device-specific audio codec API extensions |  |
| <a id="row_0_2_0_1_0_"></a>1.3.1.2.1 | [CS35L5X](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html) | CS35L5X | CS35L5X 智能放大器（Smart amplifier）。 |
| <a id="row_0_2_1_"></a><a id="arr_0_2_1_"></a>1.3.2 | [数字麦克风接口（Digital Microphone Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html) | Digital Microphone Interface | 数字麦克风的抽象（Abstraction）。 |
| <a id="row_0_2_1_0_"></a>1.3.2.1 | [数字麦克风驱动后端 API（Digital Microphone Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html) | Digital Microphone Driver Backend API |  |
| <a id="row_0_2_2_"></a><a id="arr_0_2_2_"></a>1.3.3 | [MIDI 2 通用 MIDI 数据包定义（Universal MIDI Packet definitions）](../usb/P098_通用MIDI数据包定义.md) | MIDI2 Universal MIDI Packet definitions | 通用 MIDI 数据包定义（Universal MIDI Packet definitions） |
| <a id="row_0_2_2_0_"></a>1.3.3.1 | [MIDI 命令（Commands）](../usb/P100_MIDI命令常量.md) | MIDI commands |  |
| <a id="row_0_2_2_1_"></a>1.3.3.2 | [消息类型（Message types）](../usb/P101_UMP消息类型.md) | Message types |  |
| <a id="row_0_2_2_2_"></a>1.3.3.3 | [系统公共消息与系统实时消息状态（System Common / System Real Time message status）](../usb/P102_MIDI系统消息状态.md) | System common and System Real Time message status |  |
| <a id="row_0_2_2_3_"></a>1.3.3.4 | [UMP 流响应方（Stream Responder）](../usb/P108_UMP流响应器API.md) | UMP Stream Responder | 响应 UMP 流消息中的端点或功能块发现（Endpoint / Function Block discovery）请求。 |
| <a id="row_0_2_2_4_"></a><a id="arr_0_2_2_4_"></a>1.3.3.5 | [UMP 流专用字段（Stream specific fields）](../usb/P103_UMP流消息字段.md) | UMP Stream specific fields |  |
| <a id="row_0_2_2_4_0_"></a>1.3.3.5.1 | [UMP 流功能块发现消息的过滤位（Function Block discovery message filter bits）](../usb/P107_UMP功能块发现过滤位.md) | UMP Stream Function Block discovery message filter bits |  |
| <a id="row_0_2_2_4_1_"></a>1.3.3.5.2 | [UMP 流端点发现消息的过滤位（Endpoint discovery message filter bits）](../usb/P106_UMP端点发现过滤位.md) | UMP Stream endpoint discovery message filter bits |  |
| <a id="row_0_2_2_4_2_"></a>1.3.3.5.3 | [UMP 流格式（Stream format）](../usb/P104_UMP流消息格式.md) | UMP Stream format |  |
| <a id="row_0_2_2_4_3_"></a>1.3.3.5.4 | [UMP 流状态（Stream status）](../usb/P105_UMP流消息状态.md) | UMP Stream status |  |
| <a id="row_0_2_2_5_"></a>1.3.3.6 | [通用 MIDI 数据包（Universal MIDI Packet，UMP）格式与 MIDI 2.0 协议](../usb/P113_UMP格式与MIDI协议依据.md) | Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol |  |
| <a id="row_0_3_"></a><a id="arr_0_3_"></a>1.4 | [辅助文本显示器（Auxiliary Text Display）](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html) | Auxiliary (Text) Display | 辅助显示器接口，适用于文本显示和非图形显示（Textual/non-graphical displays）。 |
| <a id="row_0_3_0_"></a>1.4.1 | [辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html) | Auxiliary Display Driver Backend API |  |
| <a id="row_0_4_"></a><a id="arr_0_4_"></a>1.5 | [电池备份 RAM（BBRAM）](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html) | BBRAM | 电池备份 RAM（Battery-Backed RAM，BBRAM）接口。 |
| <a id="row_0_4_0_"></a>1.5.1 | [BBRAM 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html) | BBRAM Driver Backend API |  |
| <a id="row_0_4_1_"></a>1.5.2 | [BBRAM 仿真器后端 API（Emulator backend API）](../hardware/P490_BBRAM仿真后端接口.md) | BBRAM emulator backend API | BBRAM 仿真器后端 API（Emulator backend API） |
| <a id="row_0_5_"></a>1.6 | [BCM283x 中断控制器（Interrupt controllers）](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html) | BCM283x interrupt controllers |  |
| <a id="row_0_6_"></a><a id="arr_0_6_"></a>1.7 | [电池充电器（Battery Charger）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html) | Battery Charger | 电池充电器接口。 |
| <a id="row_0_6_0_"></a>1.7.1 | [充电器驱动后端 API（Charger Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html) | Charger Driver Backend API |  |
| <a id="row_0_6_1_"></a><a id="arr_0_6_1_"></a>1.7.2 | [设备专用充电器 API 扩展（Device-specific Charger API extensions）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__ext.html) | Device-specific Charger API extensions |  |
| <a id="row_0_6_1_0_"></a>1.7.2.1 | [nPM10xx 充电器接口（Charger interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html) | nPM10xx Charger interface |  |
| <a id="row_0_7_"></a><a id="arr_0_7_"></a>1.8 | [生物识别（Biometrics）](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html) | Biometrics | 生物识别传感器（Biometric sensors）接口。 |
| <a id="row_0_7_0_"></a>1.8.1 | [生物识别驱动后端 API（Biometrics Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html) | Biometrics Driver Backend API |  |
| <a id="row_0_7_1_"></a>1.8.2 | [生物识别仿真器测试辅助功能（Emulator test helpers）](../hardware/P495_生物识别仿真测试接口.md) | Biometrics emulator test helpers | 生物识别仿真器测试控制函数（Emulator test control functions）。 |
| <a id="row_0_8_"></a><a id="arr_0_8_"></a>1.9 | [蜂鸣器（Buzzer）](../hardware/P144_蜂鸣器接口参考.md) | Buzzer | 蜂鸣器接口。 |
| <a id="row_0_8_0_"></a>1.9.1 | [蜂鸣器驱动后端 API（Buzzer Driver Backend API）](../hardware/P145_蜂鸣器驱动后端.md) | Buzzer Driver Backend API |  |
| <a id="row_0_9_"></a><a id="arr_0_9_"></a>1.10 | [控制器局域网（CAN）](../hardware/P361_CAN公共接口.md) | CAN | 控制器局域网（Controller Area Network，CAN）控制器与收发器接口。 |
| <a id="row_0_9_0_"></a><a id="arr_0_9_0_"></a>1.10.1 | [CAN 控制器（Controller）](../hardware/P362_CAN控制器接口.md) | CAN Controller | CAN 控制器接口。 |
| <a id="row_0_9_0_0_"></a>1.10.1.1 | [CAN 控制器驱动后端 API（Controller Driver Backend API）](../hardware/P369_CAN控制器后端接口.md) | CAN Controller Driver Backend API |  |
| <a id="row_0_9_1_"></a><a id="arr_0_9_1_"></a>1.10.2 | [CAN 收发器（Transceiver）](../hardware/P041_CAN收发器接口参考.md) | CAN Transceiver | CAN 收发器接口。 |
| <a id="row_0_9_1_0_"></a>1.10.2.1 | [CAN 收发器驱动后端 API（Transceiver Driver Backend API）](../hardware/P050_CAN收发器驱动后端接口.md) | CAN Transceiver Driver Backend API |  |
| <a id="row_0_9_2_"></a>1.10.3 | [设备树 CAN API（Devicetree CAN API）](../hardware/P373_CAN设备树宏.md) | Devicetree CAN API |  |
| <a id="row_0_9_3_"></a>1.10.4 | [模拟 CAN 控制器（Fake CAN controller）](../hardware/P374_伪CAN控制器接口.md) | Fake CAN controller | 模拟 CAN 控制器驱动（Fake CAN controller driver）。 |
| <a id="row_0_10_"></a><a id="arr_0_10_"></a>1.11 | [CRC 驱动 API（Driver APIs）](../hardware/P038_CRC驱动接口参考.md) | CRC driver APIs | 循环冗余校验（Cyclic Redundancy Check，CRC）设备接口。 |
| <a id="row_0_10_0_"></a>1.11.1 | [CRC 驱动后端 API（Driver Backend API）](../hardware/P047_CRC驱动后端接口.md) | CRC Driver Backend API |  |
| <a id="row_0_11_"></a><a id="arr_0_11_"></a>1.12 | [蜂窝通信（Cellular）](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html) | Cellular | 蜂窝调制解调器（Cellular modems）接口。 |
| <a id="row_0_11_0_"></a><a id="arr_0_11_0_"></a>1.12.1 | [蜂窝通信驱动后端 API（Cellular Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html) | Cellular Driver Backend API |  |
| <a id="row_0_11_0_0_"></a><a id="arr_0_11_0_0_"></a>1.12.1.1 | [蜂窝调制解调器辅助功能（Cellular modem helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cellular__backend.html) | Cellular modem helpers | 使用通用的 AT 交互（Chat）、连接多路复用（CMUX）、点对点协议（PPP）和电源管理支持，实现供应商特定的蜂窝调制解调器驱动。 |
| <a id="row_0_11_0_0_0_"></a>1.12.1.1.1 | [蜂窝调制解调器驱动定义宏（Driver definition macros）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html) | Cellular modem driver definition macros | 定义使用蜂窝调制解调器驱动的设备实例。 |
| <a id="row_0_11_1_"></a><a id="arr_0_11_1_"></a>1.12.2 | [设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__ext.html) | Device-specific Cellular API extensions |  |
| <a id="row_0_11_1_0_"></a>1.12.2.1 | [HL7800](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html) | HL7800 | Sierra Wireless HL7800 蜂窝调制解调器（Cellular modems）。 |
| <a id="row_0_11_1_1_"></a>1.12.2.2 | [HL78xx](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html) | HL78xx | Sierra Wireless HL78xx 蜂窝调制解调器（Cellular modems）。 |
| <a id="row_0_11_1_2_"></a>1.12.2.3 | [SIMCom SIM7080](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html) | SIMCom SIM7080 | SIMCom SIM7080 蜂窝调制解调器（Cellular modems）。 |
| <a id="row_0_11_1_3_"></a><a id="arr_0_11_1_3_"></a>1.12.2.4 | [ST87Mxx](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html) | ST87Mxx | 意法半导体（STMicroelectronics）ST87Mxx 蜂窝调制解调器。 |
| <a id="row_0_11_1_3_0_"></a>1.12.2.4.1 | [全球导航卫星系统（GNSS）配置](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__gnss__configuration.html) | GNSS configuration |  |
| <a id="row_0_11_1_3_1_"></a>1.12.2.4.2 | [ST87Mxx 常量（Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__constants.html) | ST87Mxx Constants |  |
| <a id="row_0_11_1_3_2_"></a>1.12.2.4.3 | [Wi-Fi 扫描配置（Scanning configuration）](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__wscan__configuration.html) | WIFI scanning configuration |  |
| <a id="row_0_12_"></a><a id="arr_0_12_"></a>1.13 | [时钟控制（Clock Control）](../timer_reference/P092_时钟控制公共接口.md) | Clock Control | 时钟控制器接口。 |
| <a id="row_0_12_0_"></a>1.13.1 | [时钟控制驱动后端 API（Clock Control Driver Backend API）](../timer_reference/P093_时钟控制驱动后端接口.md) | Clock Control Driver Backend API |  |
| <a id="row_0_12_1_"></a><a id="arr_0_12_1_"></a>1.13.2 | [设备专用时钟控制 API 扩展（Device-specific Clock Control API extensions）](../timer_reference/P097_时钟控制扩展接口总览.md) | Device-specific Clock Control API extensions |  |
| <a id="row_0_12_1_0_"></a>1.13.2.1 | [ARM CMSDK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html) | ARM CMSDK |  |
| <a id="row_0_12_1_1_"></a>1.13.2.2 | [Ambiq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html) | Ambiq |  |
| <a id="row_0_12_1_2_"></a>1.13.2.3 | [亚德诺（Analog Devices）MAX32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adi__max32.html) | Analog Devices MAX32 |  |
| <a id="row_0_12_1_3_"></a>1.13.2.4 | [Atmel SAM 电源管理控制器（PMC）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html) | Atmel SAM PMC |  |
| <a id="row_0_12_1_4_"></a>1.13.2.5 | [博流智能（Bouffalo Lab）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html) | Bouffalo Lab |  |
| <a id="row_0_12_1_5_"></a>1.13.2.6 | [Core Devices SF32LB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html) | Core Devices SF32LB |  |
| <a id="row_0_12_1_6_"></a>1.13.2.7 | [乐鑫（Espressif）ESP32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html) | Espressif ESP32 |  |
| <a id="row_0_12_1_7_"></a>1.13.2.8 | [兆易创新（GigaDevice）GD32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__gd32.html) | GigaDevice GD32 |  |
| <a id="row_0_12_1_8_"></a>1.13.2.9 | [英飞凌（Infineon）CAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html) | Infineon CAT1 |  |
| <a id="row_0_12_1_9_"></a>1.13.2.10 | [英特尔（Intel）音频数字信号处理器（ADSP）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adsp.html) | Intel ADSP |  |
| <a id="row_0_12_1_10_"></a>1.13.2.11 | [LiteX](../timer_reference/P119_LiteX时钟控制接口.md) | LiteX |  |
| <a id="row_0_12_1_11_"></a><a id="arr_0_12_1_11_"></a>1.13.2.12 | [微芯（Microchip）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp.html) | Microchip |  |
| <a id="row_0_12_1_11_0_"></a>1.13.2.12.1 | [微芯（Microchip）PIC32CM JH](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html) | Microchip PIC32CM JH |  |
| <a id="row_0_12_1_11_1_"></a>1.13.2.12.2 | [微芯（Microchip）PIC32CM PL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html) | Microchip PIC32CM PL |  |
| <a id="row_0_12_1_11_2_"></a>1.13.2.12.3 | [微芯（Microchip）PIC32CZ CA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html) | Microchip PIC32CZ CA |  |
| <a id="row_0_12_1_11_3_"></a>1.13.2.12.4 | [微芯（Microchip）SAM D5x/E5x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html) | Microchip SAM D5x/E5x |  |
| <a id="row_0_12_1_11_4_"></a>1.13.2.12.5 | [微芯（Microchip）SAM 电源管理控制器（PMC）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html) | Microchip SAM PMC |  |
| <a id="row_0_12_1_11_5_"></a>1.13.2.12.6 | [微芯（Microchip）XEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__xec.html) | Microchip XEC |  |
| <a id="row_0_12_1_12_"></a><a id="arr_0_12_1_12_"></a>1.13.2.13 | [恩智浦（NXP）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nxp.html) | NXP |  |
| <a id="row_0_12_1_12_0_"></a>1.13.2.13.1 | [恩智浦（NXP）LPC11U6x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__lpc11u6x.html) | NXP LPC11U6x |  |
| <a id="row_0_12_1_12_1_"></a>1.13.2.13.2 | [NXP 时钟源（Clock sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nxp__sources.html) | NXP clock sources |  |
| <a id="row_0_12_1_13_"></a>1.13.2.14 | [Nordic nRF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html) | Nordic nRF |  |
| <a id="row_0_12_1_14_"></a>1.13.2.15 | [新唐（Nuvoton）NuMaker](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numaker.html) | Nuvoton NuMaker |  |
| <a id="row_0_12_1_15_"></a>1.13.2.16 | [新唐（Nuvoton）NuMicro](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html) | Nuvoton NuMicro |  |
| <a id="row_0_12_1_16_"></a>1.13.2.17 | [树莓派 Pico（Raspberry Pi Pico）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html) | Raspberry Pi Pico |  |
| <a id="row_0_12_1_17_"></a>1.13.2.18 | [瑞昱（Realtek）Ameba](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ameba.html) | Realtek Ameba |  |
| <a id="row_0_12_1_18_"></a>1.13.2.19 | [瑞昱（Realtek）BEE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html) | Realtek BEE |  |
| <a id="row_0_12_1_19_"></a>1.13.2.20 | [瑞昱（Realtek）RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rts5912.html) | Realtek RTS5912 |  |
| <a id="row_0_12_1_20_"></a>1.13.2.21 | [瑞萨（Renesas）R-Car](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html) | Renesas R-Car |  |
| <a id="row_0_12_1_21_"></a>1.13.2.22 | [瑞萨（Renesas）R-Car CPG/MSSR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__cpg__mssr.html) | Renesas R-Car CPG/MSSR |  |
| <a id="row_0_12_1_22_"></a><a id="arr_0_12_1_22_"></a>1.13.2.23 | [瑞萨（Renesas）RA 时钟生成电路（CGC）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra.html) | Renesas RA CGC |  |
| <a id="row_0_12_1_22_0_"></a>1.13.2.23.1 | [瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html) | Renesas RA BSP Clock Clkout Divider Constants | PCLK 时钟源（Clock source） |
| <a id="row_0_12_1_22_1_"></a>1.13.2.23.2 | [瑞萨 RA BSP 时钟源常量（Clock Source Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html) | Renesas RA BSP Clock Source Constants | 瑞萨 RA BSP 时钟源常量（Clock source constants） |
| <a id="row_0_12_1_22_2_"></a>1.13.2.23.3 | [瑞萨 RA 时钟分频生成器（Clock Divider Generators）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html) | Renesas RA Clock Divider Generators | 面向多个时钟域（Clock domains）的分频生成宏。 |
| <a id="row_0_12_1_23_"></a>1.13.2.24 | [瑞萨（Renesas）RX 时钟生成电路（CGC）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html) | Renesas RX CGC |  |
| <a id="row_0_12_1_24_"></a>1.13.2.25 | [瑞萨（Renesas）RZ 时钟生成电路（CGC）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html) | Renesas RZ CGC |  |
| <a id="row_0_12_1_25_"></a>1.13.2.26 | [瑞萨（Renesas）SmartBond](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html) | Renesas SmartBond |  |
| <a id="row_0_12_1_26_"></a>1.13.2.27 | [意法半导体（STMicroelectronics）STM32](../timer_reference/P123_STM32时钟控制接口.md) | STMicroelectronics STM32 |  |
| <a id="row_0_12_1_27_"></a>1.13.2.28 | [芯科科技（Silicon Labs）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html) | Silicon Labs |  |
| <a id="row_0_12_1_28_"></a>1.13.2.29 | [芯科科技（Silicon Labs）SiWx91x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html) | Silicon Labs SiWx91x |  |
| <a id="row_0_12_1_29_"></a>1.13.2.30 | [德州仪器（TI）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__cdce9xx.html) | TI |  |
| <a id="row_0_12_1_30_"></a>1.13.2.31 | [德州仪器（Texas Instruments）MSPM0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html) | Texas Instruments MSPM0 |  |
| <a id="row_0_12_1_31_"></a>1.13.2.32 | [德州仪器（Texas Instruments）TI SCI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html) | Texas Instruments TISCI |  |
| <a id="row_0_12_2_"></a><a id="arr_0_12_2_"></a>1.13.3 | [设备树时钟 API（Devicetree Clocks API）](../timer_reference/P107_设备树时钟获取宏.md) | Devicetree Clocks API |  |
| <a id="row_0_12_2_0_"></a>1.13.3.1 | [Aesc Silicon 时钟域标识符（Clock domain identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html) | Aesc Silicon clock domain identifiers | Aesc Silicon ElemRV-H片上系统（SoC）的时钟域标识符。 |
| <a id="row_0_12_2_1_"></a>1.13.3.2 | [敦泰（FocalTech）FT9001 时钟标识符（Clock identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html) | FocalTech FT9001 clock identifiers | FocalTech FT9001的时钟标识符（Clock Identifiers）。 |
| <a id="row_0_12_2_2_"></a>1.13.3.3 | [微芯（Microchip）SmartFusion2 时钟标识符](https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html) | Microchip SmartFusion2 clock identifiers | Microchip SmartFusion2 片上系统（SoC）的时钟标识符。 |
| <a id="row_0_12_2_3_"></a><a id="arr_0_12_2_3_"></a>1.13.3.4 | [NXP i.MX952 时钟源（Clock Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html) | NXP i.MX952 Clock Sources | i.MX952 SoC 的根时钟源（Root clock sources）。 |
| <a id="row_0_12_2_3_0_"></a>1.13.3.4.1 | [外设时钟（Peripheral Clocks），编号 41–163](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html) | Peripheral Clocks (41-163) | 基于 MIMX9529 `fsl_clock.h` 的外设时钟定义。 |
| <a id="row_0_12_3_"></a>1.13.4 | [新唐 M48x 时钟控制器设备树辅助功能（Devicetree helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nuvoton__m48x.html) | Nuvoton M48x Clock Controller Devicetree helpers |  |
| <a id="row_0_12_4_"></a>1.13.5 | [新唐 NuMaker 控制器设备树辅助功能（Devicetree helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__controller__nuvoton__m031x.html) | Nuvoton NuMaker controller Devicetree helpers |  |
| <a id="row_0_12_5_"></a>1.13.6 | [新唐 NuMaker 控制器设备树辅助功能（Devicetree helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__controller__nuvoton__m335x.html) | Nuvoton NuMaker controller Devicetree helpers |  |
| <a id="row_0_12_6_"></a>1.13.7 | [Silicon Labs Series 2 和 Series 3 设备树辅助功能（Devicetree helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs.html) | Silicon Labs Series 2 and 3 Devicetree helpers |  |
| <a id="row_0_12_7_"></a>1.13.8 | [Silicon Labs SiWx91x 时钟标识符（Clock identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html) | Silicon Labs SiWx91x clock identifiers |  |
| <a id="row_0_13_"></a><a id="arr_0_13_"></a>1.14 | [时钟监测器（Clock Monitor）](../timer_reference/P098_时钟监控公共接口.md) | Clock Monitor | 时钟监测器接口（Clock Monitor Interface） |
| <a id="row_0_13_0_"></a>1.14.1 | [CLOCK_MONITOR 驱动后端 API（Driver Backend API）](../timer_reference/P099_时钟监控驱动后端接口.md) | CLOCK_MONITOR Driver Backend API |  |
| <a id="row_0_14_"></a><a id="arr_0_14_"></a>1.15 | [比较器（Comparator）](../hardware/P089_比较器接口参考.md) | Comparator | 比较器接口。 |
| <a id="row_0_14_0_"></a>1.15.1 | [比较器驱动后端 API（Comparator Driver Backend API）](../hardware/P093_比较器驱动后端接口.md) | Comparator Driver Backend API |  |
| <a id="row_0_14_1_"></a>1.15.2 | [模拟比较器（Fake comparator）](../hardware/P090_伪比较器接口.md) | Fake comparator | 模拟比较器驱动（Fake comparator driver）。 |
| <a id="row_0_15_"></a><a id="arr_0_15_"></a>1.16 | [核心转储伪设备（Coredump pseudo-device）](../observability/P053_核心转储设备接口.md) | Coredump pseudo-device | 核心转储伪设备接口。 |
| <a id="row_0_15_0_"></a>1.16.1 | [核心转储伪设备驱动后端 API（Coredump pseudo-device Driver Backend API）](../observability/P054_核心转储设备后端接口.md) | Coredump pseudo-device Driver Backend API |  |
| <a id="row_0_16_"></a><a id="arr_0_16_"></a>1.17 | [计数器（Counter）](../timer_reference/P022_计数器公共接口.md) | Counter | 计数器接口。 |
| <a id="row_0_16_0_"></a>1.17.1 | [计数器驱动后端 API（Counter Driver Backend API）](../timer_reference/P023_计数器驱动后端接口.md) | Counter Driver Backend API |  |
| <a id="row_0_16_1_"></a>1.17.2 | [计数器捕获 API（Counter capture APIs）](../timer_reference/P032_计数器捕获接口.md) | Counter capture APIs | 计数器捕获 API（Counter capture APIs） |
| <a id="row_0_16_2_"></a><a id="arr_0_16_2_"></a>1.17.3 | [设备专用计数器 API 扩展（Device-specific Counter API extensions）](../timer_reference/P041_计数器器件扩展入口.md) | Device-specific Counter API extensions |  |
| <a id="row_0_16_2_0_"></a>1.17.3.1 | [STM32 计数器捕获（Counter capture）](../timer_reference/P042_STM32计数器扩展接口.md) | STM32 counter capture | STM32 计数器捕获驱动（Counter capture driver）。 |
| <a id="row_0_16_3_"></a>1.17.4 | [设备树计数器捕获 API（Devicetree Counter Captures API）](../timer_reference/P034_计数器捕获设备树宏.md) | Devicetree Counter Captures API |  |
| <a id="row_0_16_4_"></a>1.17.5 | [仿真计数器（Emulated counter）](../hardware/P493_计数器仿真后端接口.md) | Emulated counter | 仿真计数器后端 API（Emulated counter backend API）。 |
| <a id="row_0_17_"></a><a id="arr_0_17_"></a>1.18 | [数模转换器（DAC）](../hardware/P822_数模转换器接口.md) | DAC | 数模转换器（Digital-to-Analog Converter）接口。 |
| <a id="row_0_17_0_"></a>1.18.1 | [DAC 驱动后端 API（Driver Backend API）](../hardware/P823_DAC驱动实现接口.md) | DAC Driver Backend API |  |
| <a id="row_0_17_1_"></a><a id="arr_0_17_1_"></a>1.18.2 | [设备专用 DAC API 扩展（Device-specific DAC API extensions）](../hardware/P824_DAC驱动扩展入口.md) | Device-specific DAC API extensions |  |
| <a id="row_0_17_1_0_"></a>1.18.2.1 | [DAC161S997](../hardware/P828_DAC161S997扩展接口.md) | DAC161S997 | TI DAC161S997：用于 4–20 mA 电流环（Current loops）的 16 位单通道 SPI DAC。 |
| <a id="row_0_18_"></a><a id="arr_0_18_"></a>1.19 | [数字音频接口（DAI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html) | DAI | 数字音频接口（Digital Audio Interfaces）相关接口。 |
| <a id="row_0_18_0_"></a>1.19.1 | [DAI 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface__backend.html) | DAI Driver Backend API |  |
| <a id="row_0_19_"></a><a id="arr_0_19_"></a>1.20 | [数字可寻址照明接口（DALI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html) | DALI | DALI 接口（Interface） |
| <a id="row_0_19_0_"></a>1.20.1 | [DALI 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html) | DALI Driver Backend API |  |
| <a id="row_0_20_"></a>1.21 | [调试访问端口链路（DAP Link）](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html) | DAP Link | 调试访问端口（Debug Access Port，DAP）链路后端接口。 |
| <a id="row_0_21_"></a><a id="arr_0_21_"></a>1.22 | [直接内存访问（DMA）](../dma_reference/P001_DMA公共接口.md) | DMA | 直接内存访问（Direct Memory Access，DMA）控制器接口。 |
| <a id="row_0_21_0_"></a>1.22.1 | [DMA的SF32LB专用功能（SF32LB Specifics）。](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html) | DMA (SF32LB specifics) | DMA的SF32LB专用功能（SF32LB Specifics）。 |
| <a id="row_0_21_1_"></a>1.22.2 | [DMA 驱动后端 API（Driver Backend API）](../dma_reference/P002_DMA驱动后端接口.md) | DMA Driver Backend API |  |
| <a id="row_0_21_2_"></a>1.22.3 | [设备树 DMA API（Devicetree DMA API）](../dma_reference/P008_DMA设备树宏.md) | Devicetree DMA API |  |
| <a id="row_0_21_3_"></a>1.22.4 | [Realtek Bee DMA 宏（Macros）](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html) | Realtek Bee DMA Macros | 用于从设备树（Devicetree）提取DMA配置的宏。 |
| <a id="row_0_21_4_"></a>1.22.5 | [Xilinx ADMA 专用功能（Specifics）](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html) | Xilinx ADMA specifics |  |
| <a id="row_0_22_"></a><a id="arr_0_22_"></a>1.23 | [磁盘访问（Disk Access）](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html) | Disk Access | 磁盘接口。 |
| <a id="row_0_22_0_"></a><a id="arr_0_22_0_"></a>1.23.1 | [设备专用磁盘访问 API 扩展（Device-specific Disk Access API extensions）](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface__ext.html) | Device-specific Disk Access API extensions |  |
| <a id="row_0_22_0_0_"></a>1.23.1.1 | [STM32 SDMMC](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html) | STM32 SDMMC | STM32 SDMMC 控制器（Controller）。 |
| <a id="row_0_23_"></a><a id="arr_0_23_"></a>1.24 | [显示（Display）](../hardware/P214_显示公共接口.md) | Display | 显示控制器接口。 |
| <a id="row_0_23_0_"></a>1.24.1 | [AC057TC1 显示控制器（Display controller）](../hardware/P224_AC057TC1调色板扩展.md) | AC057TC1 display controller | AC057TC1 七色电子墨水（E-ink）显示控制器的设备专用 API 扩展。 |
| <a id="row_0_23_1_"></a><a id="arr_0_23_1_"></a>1.24.2 | [设备专用显示 API 扩展（Device-specific Display API extensions）](../hardware/P223_显示器件扩展目录.md) | Device-specific Display API extensions |  |
| <a id="row_0_23_1_0_"></a>1.24.2.1 | [SSD16xx](../hardware/P228_SSD16xx显示扩展.md) | SSD16xx | Solomon SSD16xx 电子纸（EPD）显示控制器。 |
| <a id="row_0_23_2_"></a>1.24.3 | [设备树显示接口（Devicetree Display API）](../hardware/P227_设备树显示接口.md) | Devicetree Display API |  |
| <a id="row_0_23_3_"></a><a id="arr_0_23_3_"></a>1.24.4 | [显示驱动后端 API（Display Driver Backend API）](../hardware/P219_显示驱动后端接口.md) | Display Driver Backend API |  |
| <a id="row_0_23_3_0_"></a>1.24.4.1 | [颜色抖动（Color dithering）](../hardware/P221_显示颜色抖动接口.md) | Color dithering | 面向显示驱动的 RGB 到调色板（Palette）抖动转换辅助功能。 |
| <a id="row_0_23_4_"></a>1.24.5 | [显示面板设备树绑定（Display panel devicetree bindings）](../hardware/P226_显示面板设备树格式.md) | Display panel devicetree bindings | 设备树中用于表示面板像素格式（Pixel formats）的位掩码。 |
| <a id="row_0_23_5_"></a>1.24.6 | [ED2208-GCA（EL073TF1）显示控制器（Display controller）](../hardware/P225_ED2208调色板扩展.md) | ED2208-GCA (EL073TF1) display controller | ED2208-GCA 六色电子墨水（E-ink）显示控制器的设备专用 API 扩展。 |
| <a id="row_0_23_6_"></a>1.24.7 | [MIPI 显示接口（Display interface）](../hardware/P244_MIPI显示接口定义.md) | MIPI Display interface | MIPI 显示定义（Display definitions） |
| <a id="row_0_23_7_"></a><a id="arr_0_23_7_"></a>1.24.8 | [MIPI 显示总线接口（MIPI-DBI）](../hardware/P245_MIPI显示总线接口.md) | MIPI-DBI | MIPI 显示总线接口（Display Bus Interface，MIPI-DBI）相关接口。 |
| <a id="row_0_23_7_0_"></a>1.24.8.1 | [MIPI-DBI 驱动后端 API（Driver Backend API）](../hardware/P251_MIPI显示总线后端.md) | MIPI-DBI Driver Backend API |  |
| <a id="row_0_23_8_"></a><a id="arr_0_23_8_"></a>1.24.9 | [MIPI 显示串行接口（MIPI-DSI）](../hardware/P246_MIPI显示串行接口.md) | MIPI-DSI | MIPI 显示串行接口（Display Serial Interface，MIPI-DSI）相关接口。 |
| <a id="row_0_23_8_0_"></a>1.24.9.1 | [MIPI-DSI 驱动后端 API（Driver Backend API）](../hardware/P253_MIPI显示串行后端.md) | MIPI-DSI Driver Backend API |  |
| <a id="row_0_23_9_"></a>1.24.10 | [单色字符帧缓冲区（Monochrome Character Framebuffer）](../hardware/P184_单色字符帧缓冲接口.md) | Monochrome Character Framebuffer | 单色字符帧缓冲区（Monochrome Character Framebuffer）的公共API。 |
| <a id="row_0_24_"></a><a id="arr_0_24_"></a>1.25 | [错误检测与纠正（EDAC）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html) | EDAC | 错误检测与纠正（Error Detection and Correction，EDAC）控制器接口。 |
| <a id="row_0_24_0_"></a><a id="arr_0_24_0_"></a>1.25.1 | [设备专用 EDAC API 扩展（Device-specific API extensions）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface__ext.html) | Device-specific EDAC API extensions |  |
| <a id="row_0_24_0_0_"></a>1.25.1.1 | [NXP ERM 错误检测与纠正（EDAC）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__nxp__erm__interface.html) | NXP ERM EDAC | NXP ERM EDAC 驱动。 |
| <a id="row_0_24_0_1_"></a>1.25.1.2 | [Synopsys DDR 控制器错误检测与纠正（EDAC）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__synopsys__interface.html) | Synopsys DDR controller EDAC | Synopsys DDR 控制器 EDAC 驱动。 |
| <a id="row_0_25_"></a><a id="arr_0_25_"></a>1.26 | [电可擦可编程只读存储器（EEPROM）](../hardware/P040_EEPROM接口参考.md) | EEPROM | 电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）接口。 |
| <a id="row_0_25_0_"></a>1.26.1 | [EEPROM 驱动后端 API（Driver Backend API）](../hardware/P049_EEPROM驱动后端接口.md) | EEPROM Driver Backend API |  |
| <a id="row_0_25_1_"></a>1.26.2 | [模拟 EEPROM（Fake EEPROM）](../hardware/P051_伪EEPROM接口.md) | Fake EEPROM | 模拟 EEPROM 驱动（Fake EEPROM driver）。 |
| <a id="row_0_26_"></a><a id="arr_0_26_"></a>1.27 | [增强串行外设接口（ESPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html) | ESPI | 增强串行外设接口（Enhanced Serial Peripheral Interface，eSPI）目标硬件接口。 |
| <a id="row_0_26_0_"></a>1.27.1 | [eSPI 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html) | eSPI Driver Backend API |  |
| <a id="row_0_26_1_"></a>1.27.2 | [eSPI 仿真接口（Emulation Interface）](../hardware/P486_eSPI总线仿真接口.md) | eSPI Emulation Interface | eSPI 仿真接口（Emulation Interface） |
| <a id="row_0_26_2_"></a><a id="arr_0_26_2_"></a>1.27.3 | [eSPI SAF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html) | eSPI SAF | eSPI SAF 控制器接口；原文此处将 SAF 展开为串行附接 Flash（Serial Attached Flash）。 |
| <a id="row_0_26_2_0_"></a>1.27.3.1 | [eSPI SAF 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html) | eSPI SAF Driver Backend API |  |
| <a id="row_0_27_"></a><a id="arr_0_27_"></a>1.28 | [熵（Entropy）](../hardware/P039_熵源接口参考.md) | Entropy | 熵源硬件接口（Entropy hardware interfaces）。 |
| <a id="row_0_27_0_"></a>1.28.1 | [熵源驱动后端 API（Entropy Driver Backend API）](../hardware/P048_熵源驱动后端接口.md) | Entropy Driver Backend API |  |
| <a id="row_0_28_"></a>1.29 | [外部缓存控制器（External Cache Controller）](../cache_reference/P004_外部缓存接口.md) | External Cache Controller | 外部缓存控制器接口（External Cache Controller Interfaces）。 |
| <a id="row_0_29_"></a><a id="arr_0_29_"></a>1.30 | [现场可编程门阵列（FPGA）](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html) | FPGA | 现场可编程门阵列（Field-Programmable Gate Arrays，FPGA）接口。 |
| <a id="row_0_29_0_"></a>1.30.1 | [FPGA 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html) | FPGA Driver Backend API |  |
| <a id="row_0_30_"></a><a id="arr_0_30_"></a>1.31 | [闪存（Flash）](../flash_reference/P001_Flash公共接口.md) | Flash | 闪存控制器（Flash Memory Controller）的接口。 |
| <a id="row_0_30_0_"></a><a id="arr_0_30_0_"></a>1.31.1 | [扩展操作（Extended Operations）](../flash_reference/P008_Flash扩展操作目录.md) | Extended Operations | 闪存驱动的厂商专用扩展操作（Vendor-specific Extended Operations）。 |
| <a id="row_0_30_0_0_"></a>1.31.1.1 | [Andes QSPI-NOR 原地执行（XIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html) | Andes QSPI-NOR XIP | Andes QSPI-NOR 就地执行（Execute In Place，XIP）闪存的扩展操作。 |
| <a id="row_0_30_0_1_"></a>1.31.1.2 | [IT51XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html) | IT51XXX | IT51XXX 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_2_"></a>1.31.1.3 | [微芯（Microchip）](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html) | Microchip | Microchip G3 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_3_"></a>1.31.1.4 | [Microchip NVMCTRL G1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html) | Microchip NVMCTRL G1 | Microchip NVMCTRL G1 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_4_"></a>1.31.1.5 | [NPCX](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html) | NPCX | NPCX 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_5_"></a>1.31.1.6 | [瑞昱（Realtek）RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html) | Realtek RTS5912 | Realtek RTS5912 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_6_"></a>1.31.1.7 | [瑞萨（Renesas）RA](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html) | Renesas RA | Renesas RA 闪存控制器的扩展操作。 |
| <a id="row_0_30_0_7_"></a>1.31.1.8 | [ST M95P32](../flash_reference/P011_M95P32扩展操作接口.md) | ST M95P32 | ST M95P32 页式电可擦可编程只读存储器（Electrically Erasable Programmable Read-only Memory，EEPROM）的扩展操作。 |
| <a id="row_0_30_0_8_"></a>1.31.1.9 | [STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html) | STM32 | STM32 闪存控制器的扩展操作。 |
| <a id="row_0_30_1_"></a>1.31.2 | [Flash 驱动后端 API（Driver Backend API）](../flash_reference/P002_Flash驱动后端接口.md) | Flash Driver Backend API |  |
| <a id="row_0_30_2_"></a>1.31.3 | [Flash 内部接口（Flash Internal）](../flash_reference/P003_Flash内部接口.md) | Flash Internal | 闪存控制器的内部接口（Internal Interfaces）。 |
| <a id="row_0_31_"></a><a id="arr_0_31_"></a>1.32 | [电量计（Fuel Gauge）](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html) | Fuel Gauge | 电量计接口。 |
| <a id="row_0_31_0_"></a>1.32.1 | [设备树电池辅助宏（Devicetree Battery Helpers）](../dt_overview_reference/P002_电池开路电压曲线宏.md) | Devicetree battery helpers |  |
| <a id="row_0_31_1_"></a>1.32.2 | [电量计驱动后端 API（Fuel Gauge Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html) | Fuel Gauge Driver Backend API |  |
| <a id="row_0_31_2_"></a>1.32.3 | [电量计后端仿真器 API（Fuel gauge backend emulator APIs）](../hardware/P492_电量计仿真后端接口.md) | Fuel gauge backend emulator APIs | 电量计后端仿真器 API（Fuel gauge backend emulator APIs） |
| <a id="row_0_32_"></a><a id="arr_0_32_"></a>1.33 | [全球导航卫星系统（GNSS）](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html) | GNSS | 全球导航卫星系统（Global Navigation Satellite System，GNSS）接收机接口。 |
| <a id="row_0_32_0_"></a>1.33.1 | [GNSS 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html) | GNSS Driver Backend API |  |
| <a id="row_0_33_"></a><a id="arr_0_33_"></a>1.34 | [通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md) | GPIO | 通用输入/输出（General Purpose Input/Output，GPIO）控制器接口。 |
| <a id="row_0_33_0_"></a><a id="arr_0_33_0_"></a>1.34.1 | [设备专用 GPIO API 扩展（Device-specific API extensions）](../hardware/P274_GPIO器件扩展目录.md) | Device-specific GPIO API extensions |  |
| <a id="row_0_33_0_0_"></a>1.34.1.1 | [Ambiq](../hardware/P282_AmbiqGPIO扩展.md) | Ambiq | Ambiq GPIO 控制器（Controller） |
| <a id="row_0_33_0_1_"></a>1.34.1.2 | [Bouffalolab BL61x GPIO FIFO / 线路输出（Wire Out）](../hardware/P283_BL61xGPIO线输出.md) | Bouffalolab BL61x GPIO FIFO / Wire Out | BL61x GPIO FIFO / 线路输出（Wire Out）接口。 |
| <a id="row_0_33_0_2_"></a>1.34.1.3 | [MAX32 专用 GPIO 标志（Flags）](../hardware/P277_MAX32GPIO标志.md) | MAX32-specific GPIO Flags | MAX32 专用 GPIO 标志（Flags） |
| <a id="row_0_33_0_3_"></a>1.34.1.4 | [NCT38XX](../hardware/P285_NCT38XXGPIO扩展.md) | NCT38XX | 新唐（Nuvoton）NCT38XX 系列基于 I2C 的 GPIO 扩展器（Expander）。 |
| <a id="row_0_33_0_4_"></a>1.34.1.5 | [NXP MCUX LPC](../hardware/P284_LPCGPIO扩展.md) | NXP MCUX LPC | NXP MCUX LPC GPIO 控制器。 |
| <a id="row_0_33_0_5_"></a>1.34.1.6 | [NXP PCA 系列（SERIES）](../hardware/P286_PCAGPIO扩展.md) | NXP PCA SERIES | NXP PCA 系列基于 I2C 的 I/O 扩展器。 |
| <a id="row_0_33_0_6_"></a>1.34.1.7 | [NXP PCAL64XXA](../hardware/P287_PCAL64XXAGPIO扩展.md) | NXP PCAL64XXA | NXP PCAL64XXA 基于 I2C 的 I/O 扩展器。 |
| <a id="row_0_33_0_7_"></a>1.34.1.8 | [STM32 GPIO 专用标志（Specific flags）](../hardware/P275_STM32GPIO标志.md) | STM32 GPIO specific flags | STM32 GPIO 专用标志（Specific flags） |
| <a id="row_0_33_0_8_"></a>1.34.1.9 | [SX1509B](../hardware/P288_SX1509BGPIO扩展.md) | SX1509B | Semtech SX1509B 低电压电平转换（Low-voltage level-shifting）GPIO 控制器。 |
| <a id="row_0_33_0_9_"></a>1.34.1.10 | [nPM10xx专用GPIO标志（Flags）。](../hardware/P278_nPM10xxGPIO标志.md) | nPM10xx-specific GPIO Flags | 这些标志按如下方式编码在 `gpio_dt_flags_t` 的高 8 位中： |
| <a id="row_0_33_0_10_"></a>1.34.1.11 | [nPM13xx 专用 GPIO 标志（Flags）](../hardware/P279_nPM13xxGPIO标志.md) | nPM13xx-specific GPIO Flags | nPM13xx 专用 GPIO 标志（Flags） |
| <a id="row_0_33_0_11_"></a>1.34.1.12 | [nPM2100 专用 GPIO 标志（Flags）](../hardware/P280_nPM2100GPIO标志.md) | nPM2100-specific GPIO Flags | nPM2100 专用 GPIO 标志（Flags） |
| <a id="row_0_33_0_12_"></a>1.34.1.13 | [nPM6001 专用 GPIO 标志（Flags）](../hardware/P281_nPM6001GPIO标志.md) | nPM6001-specific GPIO Flags | nPM6001 专用 GPIO 标志（Flags） |
| <a id="row_0_33_0_13_"></a>1.34.1.14 | [nRF 专用 GPIO 标志（Flags）](../hardware/P276_nRFGPIO标志.md) | nRF-specific GPIO Flags | nRF 专用 GPIO 标志（Flags） |
| <a id="row_0_33_1_"></a><a id="arr_0_33_1_"></a>1.34.2 | [设备树通用输入输出接口（Devicetree GPIO API）](../hardware/P290_设备树GPIO宏.md) | Devicetree GPIO API |  |
| <a id="row_0_33_1_0_"></a><a id="arr_0_33_1_0_"></a>1.34.2.1 | [GPIO 排针（Pin headers）](../hardware/P291_GPIO排针目录.md) | GPIO pin headers | 常见 GPIO 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_0_"></a>1.34.2.1.1 | [ArduCam FFC 40 引脚摄像头连接器（Camera connector）](../hardware/P292_ArduCamFFC40针连接器.md) | ArduCam FFC 40-pin camera connector. | ArduCam FFC 40 引脚摄像头连接器所引出引脚的常量。 |
| <a id="row_0_33_1_0_1_"></a>1.34.2.1.2 | [Arducam DVP 20 引脚连接器（Connector）](../hardware/P293_ArducamDVP连接器.md) | Arducam DVP 20-pin connector | Arducam DVP 20 引脚或 18 引脚连接器所引出引脚的常量。 |
| <a id="row_0_33_1_0_2_"></a>1.34.2.1.3 | [Arduino MKR 排针（Header）](../hardware/P294_ArduinoMKR排针.md) | Arduino MKR header | Arduino MKR 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_3_"></a>1.34.2.1.4 | [Arduino Mega 排针（Header）](../hardware/P295_ArduinoMega排针.md) | Arduino Mega header | Arduino Mega 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_4_"></a>1.34.2.1.5 | [Arduino Nano 排针（Header）](../hardware/P296_ArduinoNano排针.md) | Arduino Nano header | Arduino Nano 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_5_"></a>1.34.2.1.6 | [Arduino Uno（R3）排针（Header）](../hardware/P297_ArduinoUno排针.md) | Arduino Uno (R3) header | Arduino Uno（R3）排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_6_"></a>1.34.2.1.7 | [M.2 Key A 串行存储器连接器（Serial memory connector）](../hardware/P298_M2串行存储器连接器.md) | M.2 Key A serial memory connector | ST M.2 串行存储器连接器引出的非电源信号（Non-power signals）常量。 |
| <a id="row_0_33_1_0_7_"></a>1.34.2.1.8 | [树莓派 CSI 连接器（Raspberry Pi CSI connector）](../hardware/P299_树莓派CSI连接器.md) | Raspberry Pi CSI connector | 树莓派 CSI 摄像头连接器所引出引脚的常量。 |
| <a id="row_0_33_1_0_8_"></a>1.34.2.1.9 | [ST Morpho 排针（Header）](../hardware/P300_STMorpho排针.md) | ST Morpho header | ST Morpho 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_9_"></a>1.34.2.1.10 | [ST Zio 排针（Header）](../hardware/P301_STZio排针.md) | ST Zio header | ST Zio 排针所引出引脚的常量。 |
| <a id="row_0_33_1_0_10_"></a>1.34.2.1.11 | [STMod+ 连接器（Connector）](../hardware/P302_STModPlus连接器.md) | STMod+ connector | STMod+ 连接器所引出引脚的常量。 |
| <a id="row_0_33_1_0_11_"></a>1.34.2.1.12 | [WisBlock IO 插槽连接器（Slot connector）](../hardware/P303_WisBlockIO插槽.md) | WisBlock IO slot connector | WisBlock IO 插槽连接器所引出引脚的常量。 |
| <a id="row_0_33_1_0_12_"></a>1.34.2.1.13 | [WisBlock 传感器插槽连接器（Sensor Slot connector）](../hardware/P304_WisBlock传感器插槽.md) | WisBlock Sensor Slot connector | RAKwireless WisBlock 传感器插槽所引出引脚的常量。 |
| <a id="row_0_33_2_"></a>1.34.3 | [仿真 GPIO（Emulated GPIO）](../hardware/P273_GPIO模拟接口.md) | Emulated GPIO | 仿真 GPIO 后端 API（Backend API）。 |
| <a id="row_0_33_3_"></a>1.34.4 | [GPIO 驱动后端 API（Driver Backend API）](../hardware/P271_GPIO驱动后端.md) | GPIO Driver Backend API |  |
| <a id="row_0_34_"></a><a id="arr_0_34_"></a>1.35 | [触觉反馈（Haptics）](../hardware/P147_触觉反馈接口参考.md) | Haptics | 触觉反馈驱动（Haptic drivers）接口。 |
| <a id="row_0_34_0_"></a><a id="arr_0_34_0_"></a>1.35.1 | [设备专用触觉反馈 API 扩展（Device-specific Haptics API extensions）](../hardware/P150_触觉驱动扩展入口.md) | Device-specific Haptics API extensions |  |
| <a id="row_0_34_0_0_"></a>1.35.1.1 | [CS40L26/27](../hardware/P152_CS40L26与CS40L27触觉扩展.md) | CS40L26/27 | 面向线性谐振执行器（LRA）和音圈电机（VCM）的 CS40L26 触觉反馈驱动器（Haptic Driver）。 |
| <a id="row_0_34_0_1_"></a>1.35.1.2 | [CS40L5x](../hardware/P153_CS40L5x触觉扩展.md) | CS40L5x | 面向线性谐振执行器（LRA）和音圈电机（VCM）的 CS40L5x 触觉反馈驱动器。 |
| <a id="row_0_34_0_2_"></a>1.35.1.3 | [DRV2605](../hardware/P154_DRV2605触觉扩展.md) | DRV2605 | 面向偏心旋转质量电机（ERM）和线性谐振执行器（LRA）的 DRV2605 触觉反馈驱动器。 |
| <a id="row_0_34_0_3_"></a>1.35.1.4 | [TM6605](../hardware/P155_TM6605触觉扩展.md) | TM6605 | 面向线性谐振执行器（LRA）的 TM6605 触觉反馈驱动器。 |
| <a id="row_0_34_1_"></a>1.35.2 | [触觉反馈驱动后端 API（Haptics Driver Backend API）](../hardware/P148_触觉驱动后端.md) | Haptics Driver Backend API |  |
| <a id="row_0_35_"></a>1.36 | [硬件信息（Hardware Info）](../hardware_util_reference/P003_硬件信息公共接口.md) | Hardware Info | 用于获取硬件信息（Hardware Information）的接口。 |
| <a id="row_0_36_"></a><a id="arr_0_36_"></a>1.37 | [硬件自旋锁（Hardware Spinlock）](../intercore_reference/P001_硬件自旋锁公共接口.md) | Hardware Spinlock | 硬件自旋锁接口。 |
| <a id="row_0_36_0_"></a>1.37.1 | [硬件自旋锁驱动后端 API（Hardware Spinlock Driver Backend API）](../intercore_reference/P002_硬件自旋锁驱动后端.md) | Hardware Spinlock Driver Backend API |  |
| <a id="row_0_37_"></a><a id="arr_0_37_"></a>1.38 | [集成电路间总线（I2C）](../hardware/P305_I2C公共接口.md) | I2C | 集成电路间总线（Inter-Integrated Circuit，I2C）控制器接口。 |
| <a id="row_0_37_0_"></a>1.38.1 | [I2C 驱动后端 API（Driver Backend API）](../hardware/P311_I2C驱动后端.md) | I2C Driver Backend API |  |
| <a id="row_0_37_1_"></a>1.38.2 | [I2C EEPROM 目标设备（Target）](../hardware/P313_I2CEEPROM目标接口.md) | I2C EEPROM Target | I2C EEPROM 目标设备接口。 |
| <a id="row_0_37_2_"></a>1.38.3 | [I2C 仿真接口（Emulation Interface）](../hardware/P314_I2C模拟后端.md) | I2C Emulation Interface | I2C 仿真接口（Emulation Interface） |
| <a id="row_0_38_"></a><a id="arr_0_38_"></a>1.39 | [集成电路间音频总线（I2S）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html) | I2S | 集成电路间音频（Inter-IC Sound，I2S）控制器接口。 |
| <a id="row_0_38_0_"></a>1.39.1 | [I2S 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface__backend.html) | I2S Driver Backend API |  |
| <a id="row_0_39_"></a><a id="arr_0_39_"></a>1.40 | [改进型集成电路间总线（I3C）](../hardware/P425_I3C公共接口参考.md) | I3C | 改进型集成电路间总线（Improved Inter-Integrated Circuit，I3C）控制器接口。 |
| <a id="row_0_39_0_"></a>1.40.1 | [I3C 地址相关辅助代码（Address-related Helper Code）](../hardware/P383_I3C地址槽管理.md) | I3C Address-related Helper Code | I3C 地址相关辅助代码（Address-related Helper Code） |
| <a id="row_0_39_1_"></a>1.40.2 | [I3C 公共命令码（Common Command Codes）](../hardware/P429_I3C通用命令码参考.md) | I3C Common Command Codes | I3C 公共命令码（Common Command Codes） |
| <a id="row_0_39_2_"></a>1.40.3 | [I3C 设备树相关定义（Devicetree related bits）](../hardware/P424_I3C设备树宏.md) | I3C Devicetree related bits | I3C 设备树相关定义（Devicetree related bits） |
| <a id="row_0_39_3_"></a>1.40.4 | [I3C 高数据速率双数据速率模式 API（HDR DDR API）](../hardware/P385_I3C高数据速率双沿模式.md) | I3C HDR DDR API | I3C 高数据速率双数据速率模式 API（HDR DDR API） |
| <a id="row_0_39_4_"></a>1.40.5 | [I3C 带内中断（In-Band Interrupts）](../hardware/P396_I3C带内中断接口.md) | I3C In-Band Interrupts | I3C 带内中断（In-Band Interrupts） |
| <a id="row_0_39_5_"></a><a id="arr_0_39_5_"></a>1.40.6 | [I3C 目标设备 API（Target Device API）](../hardware/P386_I3C目标设备接口.md) | I3C Target Device API | I3C 目标设备 API（Target Device API） |
| <a id="row_0_39_5_0_"></a>1.40.6.1 | [I3C 目标设备驱动后端 API（Target Device Driver Backend API）](../hardware/P387_I3C目标设备驱动后端.md) | I3C Target Device Driver Backend API |  |
| <a id="row_0_39_6_"></a>1.40.7 | [I3C 传输 API（Transfer API）](../hardware/P394_I3C传输接口.md) | I3C Transfer API | I3C 传输 API（Transfer API） |
| <a id="row_0_40_"></a><a id="arr_0_40_"></a>1.41 | [处理器间邮箱（IPM）](../intercore_reference/P058_处理器间消息公共接口.md) | IPM | 处理器间邮箱（Inter-Processor Mailbox，IPM）控制器接口。 |
| <a id="row_0_40_0_"></a>1.41.1 | [IPM 驱动后端 API（Driver Backend API）](../intercore_reference/P059_处理器间消息驱动后端.md) | IPM Driver Backend API |  |
| <a id="row_0_41_"></a><a id="arr_0_41_"></a>1.42 | [`input`（输入）。](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html) | Input | 输入设备接口。 |
| <a id="row_0_41_0_"></a>1.42.1 | [模拟轴（Analog axis）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html) | Analog axis |  |
| <a id="row_0_41_1_"></a><a id="arr_0_41_1_"></a>1.42.2 | [设备专用输入 API 扩展（Device-specific Input API extensions）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface__ext.html) | Device-specific Input API extensions | 具有标准输入 API 之外扩展功能的输入设备接口。 |
| <a id="row_0_41_1_0_"></a>1.42.2.1 | [CY8CMBR3xxx](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html) | CY8CMBR3xxx | CY8CMBR3xxx 电容触摸传感器（Capacitive touch sensor）。 |
| <a id="row_0_41_1_1_"></a>1.42.2.2 | [Nunchuk](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html) | Nunchuk | 任天堂 Nunchuk 操纵杆（Nintendo Nunchuk joystick）。 |
| <a id="row_0_41_1_2_"></a>1.42.2.3 | [PAT912x](https://docs.zephyrproject.org/latest/doxygen/html/group__pat912x__interface.html) | PAT912x | PAT912x 微型光学导航芯片（Miniature Optical Navigation Chip）。 |
| <a id="row_0_41_1_3_"></a>1.42.2.4 | [PAW32xx](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html) | PAW32xx | PAW32xx 超低功耗无线鼠标芯片（Ultra low power wireless mouse chip）。 |
| <a id="row_0_41_1_4_"></a>1.42.2.5 | [PMW3610](https://docs.zephyrproject.org/latest/doxygen/html/group__pmw3610__interface.html) | PMW3610 | PMW3610 低功耗激光鼠标传感器（Low Power Laser Mouse Sensor）。 |
| <a id="row_0_41_1_5_"></a>1.42.2.6 | [瑞萨（Renesas）RA CTSU](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__ra__ctsu__interface.html) | Renesas RA CTSU | 瑞萨 RA 电容触摸传感器单元（Capacitive Touch Sensor Unit）。 |
| <a id="row_0_41_1_6_"></a>1.42.2.7 | [瑞萨（Renesas）RX CTSU](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html) | Renesas RX CTSU | 瑞萨 RX 电容触摸传感器单元（Capacitive Touch Sensor Unit）。 |
| <a id="row_0_41_2_"></a>1.42.3 | [输入事件定义（Input Event Definitions）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html) | Input Event Definitions |  |
| <a id="row_0_41_3_"></a>1.42.4 | [键盘矩阵（Keyboard Matrix）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html) | Keyboard Matrix |  |
| <a id="row_0_41_4_"></a>1.42.5 | [键位映射实用工具（Keymap utilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__keymap.html) | Keymap utilities |  |
| <a id="row_0_41_5_"></a>1.42.6 | [LVGL 键盘按键（Keypad keys）](https://docs.zephyrproject.org/latest/doxygen/html/group__lvgl__keypad__dt.html) | LVGL keypad keys | 供设备树（Devicetree）使用的预定义 LVGL 按键。 |
| <a id="row_0_41_6_"></a>1.42.7 | [触摸屏事件（Touchscreen Events）](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html) | Touchscreen Events |  |
| <a id="row_0_42_"></a>1.43 | [虚拟机间共享内存（Inter-VM Shared Memory）](../intercore_reference/P214_IVSHMEM共享内存接口.md) | Inter-VM Shared Memory | 虚拟机间共享内存（Inter-VM Shared Memory，ivshmem）接口。 |
| <a id="row_0_43_"></a><a id="arr_0_43_"></a>1.44 | [发光二极管（LED）](../hardware/P202_LED公共接口.md) | LED | 发光二极管（Light-Emitting Diode，LED）控制器接口。 |
| <a id="row_0_43_0_"></a>1.44.1 | [模拟 LED 控制器（Fake LED controller）](../hardware/P207_模拟LED控制器.md) | Fake LED controller | 模拟 LED 控制器驱动程序。 |
| <a id="row_0_43_1_"></a>1.44.2 | [LED 驱动后端 API（LED Driver Backend API）](../hardware/P205_LED驱动后端接口.md) | LED Driver Backend API |  |
| <a id="row_0_44_"></a><a id="arr_0_44_"></a>1.45 | [LED 灯带（LED Strip）](../hardware/P208_LED灯带公共接口.md) | LED Strip | LED 灯带接口。 |
| <a id="row_0_44_0_"></a><a id="arr_0_44_0_"></a>1.45.1 | [设备专用 LED 灯带 API 扩展。](../hardware/P212_LED灯带扩展接口目录.md) | Device-specific LED Strip API extensions |  |
| <a id="row_0_44_0_0_"></a>1.45.1.1 | [TLC5971](../hardware/P213_TLC5971灯带扩展.md) | TLC5971 | Texas Instruments TLC5971 及其兼容的 LED 灯带控制器。 |
| <a id="row_0_44_1_"></a>1.45.2 | [LED 灯带驱动后端 API](../hardware/P210_LED灯带后端接口.md) | LED Strip Driver Backend API |  |
| <a id="row_0_45_"></a><a id="arr_0_45_"></a>1.46 | [局部互连网络（LIN）](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__interface.html) | LIN | 局部互连网络（Local Interconnect Network，LIN）控制器和收发器接口。 |
| <a id="row_0_45_0_"></a>1.46.1 | [LIN 控制器（LIN Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html) | LIN Controller | LIN 控制器接口。 |
| <a id="row_0_45_1_"></a>1.46.2 | [LIN 收发器（LIN Transceiver）](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html) | LIN Transceiver | LIN 收发器接口。 |
| <a id="row_0_46_"></a><a id="arr_0_46_"></a>1.47 | [LoRa](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html) | LoRa | LoRa 收发器接口。 |
| <a id="row_0_46_0_"></a>1.47.1 | [模拟 LoRa（Fake LoRa）](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__fake.html) | Fake LoRa | 模拟 LoRa 驱动程序。 |
| <a id="row_0_46_1_"></a>1.47.2 | [LoRa 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html) | LoRa Driver Backend API |  |
| <a id="row_0_47_"></a><a id="arr_0_47_"></a>1.48 | [邮箱（MBOX）](../intercore_reference/P014_邮箱驱动公共接口.md) | MBOX | 邮箱（Mailbox，MBOX）设备接口。 |
| <a id="row_0_47_0_"></a>1.48.1 | [设备树邮箱接口（Devicetree MBOX API）](../intercore_reference/P021_邮箱设备树访问宏.md) | Devicetree MBOX API |  |
| <a id="row_0_47_1_"></a>1.48.2 | [MBOX 驱动后端 API](../intercore_reference/P015_邮箱驱动后端接口.md) | MBOX Driver Backend API |  |
| <a id="row_0_48_"></a><a id="arr_0_48_"></a>1.49 | [管理数据输入/输出（MDIO）](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html) | MDIO | 管理数据输入/输出（Management Data Input/Output，MDIO）控制器接口。 |
| <a id="row_0_48_0_"></a>1.49.1 | [MDIO 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html) | MDIO Driver Backend API |  |
| <a id="row_0_49_"></a><a id="arr_0_49_"></a>1.50 | [存储器控制器（MEMC）](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html) | MEMC | 存储器控制器（Memory Controller，MEMC）接口。 |
| <a id="row_0_49_0_"></a>1.50.1 | [MEMC 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html) | MEMC Driver Backend API |  |
| <a id="row_0_50_"></a><a id="arr_0_50_"></a>1.51 | [多位串行外设接口（MSPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html) | MSPI | 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）控制器接口。 |
| <a id="row_0_50_0_"></a><a id="arr_0_50_0_"></a>1.51.1 | [MSPI 配置 API（MSPI Configure API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html) | MSPI Configure API | MSPI 配置 API（MSPI Configure API） |
| <a id="row_0_50_0_0_"></a>1.51.1.1 | [Cadence MSPI 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html) | Cadence MSPI interface | Cadence MSPI 控制器的配置接口。 |
| <a id="row_0_50_1_"></a>1.51.2 | [MSPI 设备树相关宏](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html) | MSPI Devicetree related macros | MSPI 设备树相关宏 |
| <a id="row_0_50_2_"></a>1.51.3 | [MSPI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html) | MSPI Driver Backend API |  |
| <a id="row_0_50_3_"></a>1.51.4 | [MSPI 仿真接口（MSPI Emulation Interface）](../hardware/P487_MSPI总线仿真接口.md) | MSPI Emulation Interface | MSPI 仿真接口（MSPI Emulation Interface） |
| <a id="row_0_50_4_"></a>1.51.5 | [MSPI 传输 API（MSPI Transfer API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html) | MSPI Transfer API | MSPI 传输 API（MSPI Transfer API） |
| <a id="row_0_50_5_"></a>1.51.6 | [MSPI 回调 API（MSPI callback API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html) | MSPI callback API | MSPI 回调 API（MSPI callback API） |
| <a id="row_0_50_6_"></a>1.51.7 | [MSPI 工具（Mspi_util）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html) | Mspi_util |  |
| <a id="row_0_51_"></a><a id="arr_0_51_"></a>1.52 | [多路复用器（MUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html) | MUX | MUX 控制器接口（MUX Controller Interface） |
| <a id="row_0_51_0_"></a>1.52.1 | [设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md) | Devicetree MUX API |  |
| <a id="row_0_52_"></a><a id="arr_0_52_"></a>1.53 | [其他设备（Miscellaneous Devices）](https://docs.zephyrproject.org/latest/doxygen/html/group__misc__interfaces.html) | Miscellaneous Devices | 没有专用驱动类别的硬件外设接口。 |
| <a id="row_0_52_0_"></a>1.53.1 | [Coresight STMESP](../trace_interface_reference/P002_STMESP底层接口.md) | Coresight STMESP | CoreSight STMESP（STM扩展激励端口，STM Extended Stimulus Port）的接口。 |
| <a id="row_0_52_1_"></a>1.53.2 | [设备多路复用器（Devmux）](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html) | Devmux | 设备多路复用器（Device multiplexer）接口。 |
| <a id="row_0_52_2_"></a><a id="arr_0_52_2_"></a>1.53.3 | [FTDI FT8xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html) | FTDI FT8xx | FTDI FT8xx 图形控制器接口。 |
| <a id="row_0_52_2_0_"></a>1.53.3.1 | [FT8xx 协处理器（Co-processor）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html) | FT8xx co-processor | FT8xx 协处理器引擎函数。 |
| <a id="row_0_52_2_1_"></a>1.53.3.2 | [FT8xx 通用函数](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html) | FT8xx common functions | FT8xx 内存读写函数。 |
| <a id="row_0_52_2_2_"></a>1.53.3.3 | [FT8xx 显示列表（Display list）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html) | FT8xx display list | FT8xx 显示列表命令。 |
| <a id="row_0_52_2_3_"></a>1.53.3.4 | [FT8xx 内存映射（Memory map）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html) | FT8xx memory map | FT8xx 内存地址。 |
| <a id="row_0_52_2_4_"></a>1.53.3.5 | [FT8xx 参考 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html) | FT8xx reference API | FT8xx 参考 API |
| <a id="row_0_52_3_"></a>1.53.4 | [MAX2221X 其他功能（MISC）](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html) | MAX2221X MISC |  |
| <a id="row_0_52_4_"></a>1.53.5 | [NXP FlexIO](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html) | NXP FlexIO | NXP FlexIO 接口。 |
| <a id="row_0_52_5_"></a>1.53.6 | [Raspberry Pi Pico 可编程 I/O（PIO）](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html) | Raspberry Pi Pico PIO | Raspberry Pi Pico 可编程 I/O（Programmable I/O，PIO）接口。 |
| <a id="row_0_52_6_"></a>1.53.7 | [Raspberry Pi Pico 邮箱（Mailbox）](../intercore_reference/P026_Pico邮箱扩展接口.md) | Raspberry Pi Pico mailbox | Raspberry Pi Pico SIO FIFO 邮箱接口。 |
| <a id="row_0_52_7_"></a>1.53.8 | [Renesas 事件链接控制器（ELC）](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html) | Renesas ELC | Renesas 事件链接控制器（Event Link Controller，ELC）接口。 |
| <a id="row_0_52_8_"></a>1.53.9 | [TMC6460 其他功能（MISC）](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html) | TMC6460 MISC |  |
| <a id="row_0_53_"></a><a id="arr_0_53_"></a>1.54 | [多功能设备（Multi-function Devices）](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interfaces.html) | Multi-function Devices | 多功能设备接口。 |
| <a id="row_0_53_0_"></a>1.54.1 | [MFD AD559X 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html) | MFD AD559X interface |  |
| <a id="row_0_53_1_"></a>1.54.2 | [MFD ADP5360 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html) | MFD ADP5360 Interface |  |
| <a id="row_0_53_2_"></a>1.54.3 | [MFD AXP192 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html) | MFD AXP192 interface | AXP192 的引脚支持多种不同功能。 |
| <a id="row_0_53_3_"></a>1.54.4 | [MFD BD8LB600FS 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html) | MFD BD8LB600FS interface |  |
| <a id="row_0_53_4_"></a>1.54.5 | [MFD Infineon MXCRYPTO 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html) | MFD Infineon MXCRYPTO interface |  |
| <a id="row_0_53_5_"></a>1.54.6 | [MFD Infineon MXCRYPTOLITE 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html) | MFD Infineon MXCRYPTOLITE interface |  |
| <a id="row_0_53_6_"></a>1.54.7 | [MFD M5PM1 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html) | MFD M5PM1 Interface | M5Stack M5PM1 电源管理配套微控制器（MCU）接口。 |
| <a id="row_0_53_7_"></a>1.54.8 | [MFD MAX22017 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html) | MFD MAX22017 interface |  |
| <a id="row_0_53_8_"></a>1.54.9 | [多功能设备（MFD）MAX2221X](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__max2221x.html) | MFD MAX2221X |  |
| <a id="row_0_53_9_"></a>1.54.10 | [MFD NPM10XX 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html) | MFD NPM10XX Interface |  |
| <a id="row_0_53_10_"></a>1.54.11 | [MFD NPM13XX 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html) | MFD NPM13XX Interface |  |
| <a id="row_0_53_11_"></a>1.54.12 | [MFD NPM2100 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html) | MFD NPM2100 Interface |  |
| <a id="row_0_53_12_"></a>1.54.13 | [MFD PCA9422 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html) | MFD PCA9422 Interface |  |
| <a id="row_0_53_13_"></a>1.54.14 | [MFD TLA2528 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html) | MFD TLA2528 Interface |  |
| <a id="row_0_54_"></a><a id="arr_0_54_"></a>1.55 | [非易失性存储器（NVMEM）](../storage/P013_NVMEM接口参考.md) | NVMEM | 非易失性存储单元（Non-volatile memory cells）。 |
| <a id="row_0_54_0_"></a>1.55.1 | [非易失性存储器设备树辅助宏（NVMEM Devicetree Helpers）](../storage/P018_NVMEM设备树辅助宏.md) | NVMEM Devicetree Helpers | 非易失性存储器（Non-Volatile Memory，NVMEM）的设备树支持。 |
| <a id="row_0_55_"></a><a id="arr_0_55_"></a>1.56 | [运算放大器（OPAMP）](../hardware/P091_运算放大器接口参考.md) | OPAMP | 运算放大器（Operational amplifier，OPAMP）接口。 |
| <a id="row_0_55_0_"></a>1.56.1 | [OPAMP 驱动后端 API](../hardware/P095_运算放大器驱动后端接口.md) | OPAMP Driver Backend API |  |
| <a id="row_0_56_"></a><a id="arr_0_56_"></a>1.57 | [一次性可编程存储器（One Time Programmable Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html) | One Time Programmable Memory | 一次性可编程（One Time Programmable，OTP）存储器接口。 |
| <a id="row_0_56_0_"></a>1.57.1 | [OTP 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html) | OTP Driver Backend API |  |
| <a id="row_0_56_1_"></a>1.57.2 | [nPM10xx OTP 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html) | nPM10xx OTP interface |  |
| <a id="row_0_57_"></a><a id="arr_0_57_"></a>1.58 | [PCI Express（PCIe）](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface.html) | PCIe | PCIe 设备接口。 |
| <a id="row_0_57_0_"></a><a id="arr_0_57_0_"></a>1.58.1 | [PCIe 控制器（PCIe Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html) | PCIe Controller | PCIe 控制器接口。 |
| <a id="row_0_57_0_0_"></a>1.58.1.1 | [PCIe 控制器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html) | PCIe Controller Driver Backend API |  |
| <a id="row_0_57_1_"></a>1.58.2 | [PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html) | PCIe Endpoint Driver Backend API |  |
| <a id="row_0_57_2_"></a><a id="arr_0_57_2_"></a>1.58.3 | [PCIe 主机（PCIe Host）](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html) | PCIe Host | PCIe 主机接口。 |
| <a id="row_0_57_2_0_"></a>1.58.3.1 | [PCIe能力（Capabilities）。](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html) | PCIe Capabilities |  |
| <a id="row_0_57_2_1_"></a>1.58.3.2 | [PCIe 主机消息信号中断（MSI）接口](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html) | PCIe Host MSI Interface | PCIe 主机消息信号中断（MSI）接口 |
| <a id="row_0_57_2_2_"></a>1.58.3.3 | [PCIe 主机精确时间测量（PTM）接口](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html) | PCIe Host PTM Interface | PCIe 主机精确时间测量（PTM）接口 |
| <a id="row_0_57_2_3_"></a>1.58.3.4 | [PCIe 虚拟通道（Virtual Channel）主机接口](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__vc__host__interface.html) | PCIe Virtual Channel Host Interface | PCIe 虚拟通道（Virtual Channel）主机接口 |
| <a id="row_0_58_"></a><a id="arr_0_58_"></a>1.59 | [平台环境控制接口（PECI）](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html) | PECI | 平台环境控制接口（Platform Environment Control Interface，PECI）设备接口。 |
| <a id="row_0_58_0_"></a>1.59.1 | [PECI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html) | PECI Driver Backend API |  |
| <a id="row_0_59_"></a>1.60 | [性能监控单元（PMU）](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html) | PMU |  |
| <a id="row_0_60_"></a><a id="arr_0_60_"></a>1.61 | [PS/2](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html) | PS/2 | PS/2 设备接口。 |
| <a id="row_0_60_0_"></a>1.61.1 | [PS/2 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html) | PS/2 Driver Backend API |  |
| <a id="row_0_61_"></a><a id="arr_0_61_"></a>1.62 | [外设传感器接口（PSI5）](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html) | PSI5 | 外设传感器接口（Peripheral Sensor Interface，PSI5）接口。 |
| <a id="row_0_61_0_"></a>1.62.1 | [PSI5 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html) | PSI5 Driver Backend API |  |
| <a id="row_0_62_"></a><a id="arr_0_62_"></a>1.63 | [精确时间协议时钟（PTP Clock）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html) | PTP Clock | 精确时间协议（Precision Time Protocol，PTP）时钟接口。 |
| <a id="row_0_62_0_"></a>1.63.1 | [PTP 时钟驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html) | PTP Clock Driver Backend API |  |
| <a id="row_0_63_"></a><a id="arr_0_63_"></a>1.64 | [脉宽调制（PWM）](../hardware/P255_PWM公共接口.md) | PWM | 脉宽调制（Pulse Width Modulation，PWM）控制器接口。 |
| <a id="row_0_63_0_"></a><a id="arr_0_63_0_"></a>1.64.1 | [设备专用 PWM API 扩展。](../hardware/P261_PWM器件扩展目录.md) | Device-specific PWM API extensions |  |
| <a id="row_0_63_0_0_"></a>1.64.1.1 | [MAX2221X PWM](../hardware/P262_MAX2221xPWM扩展.md) | MAX2221X PWM |  |
| <a id="row_0_63_0_1_"></a>1.64.1.2 | [MAX31790](../hardware/P263_MAX31790PWM扩展.md) | MAX31790 | Maxim MAX31790 六通道 I2C 总线 PWM 控制器。 |
| <a id="row_0_63_0_2_"></a>1.64.1.3 | [WisBlock PWM](../hardware/P265_WisBlockPWM通道.md) | WisBlock PWM | WisBlock 连接器上提供的 PWM 通道所用常量。 |
| <a id="row_0_63_1_"></a>1.64.2 | [设备树脉宽调制接口（Devicetree PWMs API）](../hardware/P264_设备树PWM宏.md) | Devicetree PWMs API |  |
| <a id="row_0_63_2_"></a>1.64.3 | [模拟 PWM（Fake PWM）](../hardware/P260_PWM模拟控制器.md) | Fake PWM | 模拟 PWM 驱动程序。 |
| <a id="row_0_63_3_"></a>1.64.4 | [PWM 驱动后端 API](../hardware/P258_PWM驱动后端接口.md) | PWM Driver Backend API |  |
| <a id="row_0_64_"></a><a id="arr_0_64_"></a>1.65 | [引脚控制（Pin Control）](../pinctrl_reference/P001_引脚控制公共接口.md) | Pin Control | 引脚控制器（Pin Controller）接口。 |
| <a id="row_0_64_0_"></a>1.65.1 | [动态引脚控制（Dynamic Pin Control）](../pinctrl_reference/P002_动态引脚控制接口.md) | Dynamic Pin Control |  |
| <a id="row_0_64_1_"></a><a id="arr_0_64_1_"></a>1.65.2 | [引脚控制（Pin Control）](../pinctrl_reference/P005_引脚控制设备树宏.md) | Pin control |  |
| <a id="row_0_64_1_0_"></a><a id="arr_0_64_1_0_"></a>1.65.2.1 | [Ambiq 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__ambiq__pinctrl.html) | Ambiq pin control helpers |  |
| <a id="row_0_64_1_0_0_"></a>1.65.2.1.1 | [Ambiq Apollo2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo2.html) | Ambiq Apollo2 pin control helpers | 用于配置 Ambiq Apollo2 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_0_1_"></a>1.65.2.1.2 | [Ambiq Apollo3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo3.html) | Ambiq Apollo3 pin control helpers | 用于配置 Ambiq Apollo3 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_0_2_"></a>1.65.2.1.3 | [Ambiq Apollo4 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html) | Ambiq Apollo4 pin control helpers | 用于配置 Ambiq Apollo4 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_0_3_"></a>1.65.2.1.4 | [Ambiq Apollo5 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html) | Ambiq Apollo5 pin control helpers | 用于配置 Ambiq Apollo5 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_"></a><a id="arr_0_64_1_1_"></a>1.65.2.2 | [Espressif 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__espressif__pinctrl.html) | Espressif pin control helpers |  |
| <a id="row_0_64_1_1_0_"></a>1.65.2.2.1 | [Espressif ESP32 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32.html) | Espressif ESP32 pin control helpers | 用于配置 Espressif ESP32 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_1_"></a>1.65.2.2.2 | [Espressif ESP32C2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c2.html) | Espressif ESP32C2 pin control helpers | 用于配置 Espressif ESP32C2 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_2_"></a>1.65.2.2.3 | [Espressif ESP32C3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c3.html) | Espressif ESP32C3 pin control helpers | 用于配置 Espressif ESP32C3 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_3_"></a>1.65.2.2.4 | [Espressif ESP32C5 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c5.html) | Espressif ESP32C5 pin control helpers | 用于配置 Espressif ESP32C5 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_4_"></a>1.65.2.2.5 | [Espressif ESP32C6 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html) | Espressif ESP32C6 pin control helpers | 用于配置 Espressif ESP32C6 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_5_"></a>1.65.2.2.6 | [Espressif ESP32C61 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c61.html) | Espressif ESP32C61 pin control helpers | 用于配置 Espressif ESP32C61 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_6_"></a>1.65.2.2.7 | [Espressif ESP32H2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32h2.html) | Espressif ESP32H2 pin control helpers | 用于配置 Espressif ESP32H2 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_7_"></a>1.65.2.2.8 | [Espressif ESP32P4 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32p4.html) | Espressif ESP32P4 pin control helpers | 用于配置 Espressif ESP32P4 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_8_"></a>1.65.2.2.9 | [Espressif ESP32S2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s2.html) | Espressif ESP32S2 pin control helpers | 用于配置 Espressif ESP32S2 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_1_9_"></a>1.65.2.2.10 | [Espressif ESP32S3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s3.html) | Espressif ESP32S3 pin control helpers | 用于配置 Espressif ESP32S3 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_2_"></a><a id="arr_0_64_1_2_"></a>1.65.2.3 | [FocalTech 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl.html) | FocalTech pin control helpers |  |
| <a id="row_0_64_1_2_0_"></a><a id="arr_0_64_1_2_0_"></a>1.65.2.3.1 | [FocalTech FT9001 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html) | FocalTech FT9001 pin control helpers | 用于配置 FocalTech FT9001 引脚复用（Pin multiplexing）的宏。 |
| <a id="row_0_64_1_2_0_0_"></a>1.65.2.3.1.1 | [FT9001 IOCTRL 寄存器偏移量（Register offsets）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html) | FT9001 IOCTRL register offsets | 用作 `FOCALTECH_PINMUX` 的 `reg` 参数的寄存器偏移量。 |
| <a id="row_0_64_1_3_"></a><a id="arr_0_64_1_3_"></a>1.65.2.4 | [Nuvoton 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__nuvoton__pinctrl.html) | Nuvoton pin control helpers |  |
| <a id="row_0_64_1_3_0_"></a>1.65.2.4.1 | [Nuvoton NuMaker M46x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html) | Nuvoton NuMaker M46x pin control helpers | 用于配置 Nuvoton NuMaker M46x 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_"></a><a id="arr_0_64_1_4_"></a>1.65.2.5 | [Renesas 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__pinctrl.html) | Renesas pin control helpers |  |
| <a id="row_0_64_1_4_0_"></a>1.65.2.5.1 | [Renesas R-Car 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html) | Renesas R-Car pin control helpers | Renesas R-Car Gen3/Gen4/Gen5 片上系统（SoC）的引脚宏和功能宏。 |
| <a id="row_0_64_1_4_1_"></a>1.65.2.5.2 | [Renesas RA 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html) | Renesas RA pin control helpers | 用于配置 Renesas RA 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_2_"></a>1.65.2.5.3 | [Renesas RA0 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html) | Renesas RA0 pin control helpers | 用于配置 Renesas RA0 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_3_"></a>1.65.2.5.4 | [Renesas RX 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html) | Renesas RX pin control helpers | 用于配置 Renesas RX 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_4_"></a>1.65.2.5.5 | [Renesas RZ/A 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html) | Renesas RZ/A pin control helpers | 用于配置 Renesas RZ/A 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_5_"></a>1.65.2.5.6 | [Renesas RZ/A2M 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html) | Renesas RZ/A2M pin control helpers | 用于配置 Renesas RZ/A2M 片上系统（SoC）引脚控制的宏。 |
| <a id="row_0_64_1_4_6_"></a>1.65.2.5.7 | [Renesas RZ/G 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html) | Renesas RZ/G pin control helpers | 用于配置 Renesas RZ/G 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_7_"></a>1.65.2.5.8 | [Renesas RZ/N 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzn.html) | Renesas RZ/N pin control helpers | 用于配置 Renesas RZ/N 系列 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_8_"></a>1.65.2.5.9 | [Renesas RZ/T 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html) | Renesas RZ/T pin control helpers | 用于配置 Renesas RZ/T 系列 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_4_9_"></a>1.65.2.5.10 | [Renesas RZ/V 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html) | Renesas RZ/V pin control helpers | 用于配置 Renesas RZ/V 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_5_"></a><a id="arr_0_64_1_5_"></a>1.65.2.6 | [SiFli 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__sifli__pinctrl.html) | SiFli pin control helpers |  |
| <a id="row_0_64_1_5_0_"></a>1.65.2.6.1 | [SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html) | SiFli SF32LB52x pin control helpers | 用于配置 SiFli SF32LB52x 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_"></a><a id="arr_0_64_1_6_"></a>1.65.2.7 | [Silicon Labs 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__silabs__pinctrl.html) | Silicon Labs pin control helpers |  |
| <a id="row_0_64_1_6_0_"></a>1.65.2.7.1 | [Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html) | Silicon Labs SiWx91x pin control helpers | 用于配置 Silicon Labs SiWx91x 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_1_"></a>1.65.2.7.2 | [Silicon Labs Six301 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html) | Silicon Labs Six301 pin control helpers | 用于配置 Silicon Labs Six301 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_2_"></a>1.65.2.7.3 | [Silicon Labs xG21 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg21.html) | Silicon Labs xG21 pin control helpers | 用于配置 Silicon Labs xG21 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_3_"></a>1.65.2.7.4 | [Silicon Labs xG22 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg22.html) | Silicon Labs xG22 pin control helpers | 用于配置 Silicon Labs xG22 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_4_"></a>1.65.2.7.5 | [Silicon Labs xG23 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg23.html) | Silicon Labs xG23 pin control helpers | 用于配置 Silicon Labs xG23 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_5_"></a>1.65.2.7.6 | [Silicon Labs xG24 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg24.html) | Silicon Labs xG24 pin control helpers | 用于配置 Silicon Labs xG24 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_6_"></a>1.65.2.7.7 | [Silicon Labs xG26 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg26.html) | Silicon Labs xG26 pin control helpers | 用于配置 Silicon Labs xG26 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_7_"></a>1.65.2.7.8 | [Silicon Labs xG27 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg27.html) | Silicon Labs xG27 pin control helpers | 用于配置 Silicon Labs xG27 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_8_"></a>1.65.2.7.9 | [Silicon Labs xG28 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html) | Silicon Labs xG28 pin control helpers | 用于配置 Silicon Labs xG28 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_6_9_"></a>1.65.2.7.10 | [Silicon Labs xG29 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg29.html) | Silicon Labs xG29 pin control helpers | 用于配置 Silicon Labs xG29 引脚控制（Pin control）的宏。 |
| <a id="row_0_64_1_7_"></a>1.65.2.8 | [WCH CH32H41x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html) | WCH CH32H41x pin control helpers | 用于配置 WCH CH32H41x 引脚控制（Pin control）的宏。 |
| <a id="row_0_65_"></a>1.66 | [脉冲 I/O（Pulse IO）](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html) | Pulse IO | 脉冲 I/O 接口（Pulse IO Interface） |
| <a id="row_0_66_"></a>1.67 | [QEMU 固件配置（fw_cfg）](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html) | QEMU fw_cfg | QEMU 固件配置（Firmware configuration，fw_cfg）驱动接口。 |
| <a id="row_0_67_"></a><a id="arr_0_67_"></a>1.68 | [实时时钟（RTC）](../timer_reference/P009_实时时钟公共接口.md) | RTC | 实时时钟（Real-time clock，RTC）接口。 |
| <a id="row_0_67_0_"></a>1.68.1 | [设备专用 RTC API 扩展。](../timer_reference/P015_实时时钟器件扩展入口.md) | Device-specific RTC API extensions |  |
| <a id="row_0_67_1_"></a>1.68.2 | [模拟 RTC（Fake RTC）](../hardware/P497_RTC伪设备接口.md) | Fake RTC | 模拟 RTC 驱动程序。 |
| <a id="row_0_67_2_"></a>1.68.3 | [RTC 驱动后端 API](../timer_reference/P010_实时时钟驱动后端接口.md) | RTC Driver Backend API |  |
| <a id="row_0_68_"></a><a id="arr_0_68_"></a>1.69 | [稳压器（Regulator）](../power/P073_稳压器接口.md) | Regulator | 稳压器接口。 |
| <a id="row_0_68_0_"></a><a id="arr_0_68_0_"></a>1.69.1 | [设备树稳压器接口（Devicetree Regulator API）](../power/P081_设备树稳压器辅助接口目录.md) | Devicetree Regulator API |  |
| <a id="row_0_68_0_0_"></a>1.69.1.1 | [ADP5360 设备树辅助工具（Devicetree helpers）](../power/P085_ADP5360稳压器设备树辅助接口.md) | ADP5360 Devicetree helpers | Analog Devices ADP5360 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_1_"></a>1.69.1.2 | [AXP192 设备树辅助工具（Devicetree helpers）](../power/P086_AXP192稳压器设备树辅助接口.md) | AXP192 Devicetree helpers | X-Powers AXP192 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_2_"></a>1.69.1.3 | [MAX20335 设备树辅助工具（Devicetree helpers）](../power/P087_MAX20335稳压器设备树辅助接口.md) | MAX20335 Devicetree helpers | Maxim MAX20335 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_3_"></a>1.69.1.4 | [MAX20362 设备树辅助工具（Devicetree helpers）](../power/P088_MAX20362稳压器设备树辅助接口.md) | MAX20362 Devicetree helpers | Analog Devices MAX20362 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_4_"></a>1.69.1.5 | [MSPM0 VREF 设备树辅助工具（Devicetree helpers）](../power/P089_MSPM0参考电压设备树辅助接口.md) | MSPM0 VREF Devicetree helpers | Texas Instruments MSPM0 VREF 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_5_"></a>1.69.1.6 | [NXP VREF 设备树辅助工具（Devicetree helpers）](../power/P090_NXP参考电压设备树辅助接口.md) | NXP VREF Devicetree helpers | NXP VREF 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_6_"></a>1.69.1.7 | [Raspberry Pi Pico 稳压器设备树辅助工具（Regulator Devicetree helpers）](../power/P091_RaspberryPi_Pico稳压器设备树辅助接口.md) | Raspberry Pi Pico regulator Devicetree helpers | Raspberry Pi Pico 片上稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_7_"></a>1.69.1.8 | [Silicon Labs DCDC 设备树辅助工具（Devicetree helpers）](../power/P092_SiliconLabs_DCDC设备树辅助接口.md) | Silicon Labs DCDC Devicetree helpers | Silicon Labs DCDC 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_8_"></a>1.69.1.9 | [Texas Instruments TPS6287x 设备树辅助工具（Devicetree helpers）](../power/P093_TPS6287x稳压器设备树辅助接口.md) | Texas Instruments TPS6287x Devicetree helpers | Texas instruments TPS6287x 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_9_"></a>1.69.1.10 | [nPM10xx 设备树辅助工具（Devicetree helpers）](../power/P094_nPM10xx稳压器设备树辅助接口.md) | nPM10xx Devicetree helpers | Nordic nPM10 系列电源管理芯片（PMIC）的稳压器驱动设备树辅助工具。 |
| <a id="row_0_68_0_10_"></a>1.69.1.11 | [nPM1100 设备树辅助工具（Devicetree helpers）](../power/P095_nPM1100稳压器设备树辅助接口.md) | nPM1100 Devicetree helpers | Nordic nPM1100 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_11_"></a>1.69.1.12 | [nPM13xx 设备树辅助工具（Devicetree helpers）](../power/P096_nPM13xx稳压器设备树辅助接口.md) | nPM13xx Devicetree helpers | Nordic nPM13 系列电源管理芯片（PMIC）的稳压器驱动设备树辅助工具。 |
| <a id="row_0_68_0_12_"></a>1.69.1.13 | [nPM2100 设备树辅助工具（Devicetree helpers）](../power/P097_nPM2100稳压器设备树辅助接口.md) | nPM2100 Devicetree helpers | Nordic nPM2100 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_13_"></a>1.69.1.14 | [nPM6001 设备树辅助工具（Devicetree helpers）](../power/P098_nPM6001稳压器设备树辅助接口.md) | nPM6001 Devicetree helpers | Nordic nPM6001 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_0_68_0_14_"></a>1.69.1.15 | [nRF5X 设备树辅助工具（Devicetree helpers）](../power/P099_nRF5X稳压器设备树辅助接口.md) | nRF5X Devicetree helpers | NRF5X 稳压器设备树辅助工具。 |
| <a id="row_0_68_1_"></a>1.69.2 | [模拟稳压器（Fake regulator）](../hardware/P498_稳压器伪设备接口.md) | Fake regulator | 模拟稳压器驱动程序。 |
| <a id="row_0_68_2_"></a>1.69.3 | [稳压器驱动后端 API](../power/P077_稳压器驱动后端接口.md) | Regulator Driver Backend API |  |
| <a id="row_0_68_3_"></a><a id="arr_0_68_3_"></a>1.69.4 | [稳压器父设备接口（Regulator Parent Interface）](../power/P074_父级稳压器接口.md) | Regulator Parent Interface | 稳压器父设备接口（Regulator Parent Interface） |
| <a id="row_0_68_3_0_"></a>1.69.4.1 | [MAX20362 API](../power/P083_MAX20362父级控制接口.md) | MAX20362 API | MAX20362 稳压器驱动的公共 API。 |
| <a id="row_0_68_3_1_"></a>1.69.4.2 | [PCA9420 工具（Utilities）](../power/P084_PCA9420父级控制接口.md) | PCA9420 Utilities. |  |
| <a id="row_0_69_"></a><a id="arr_0_69_"></a>1.70 | [复位控制器（Reset Controller）](../reset_reference/P001_复位控制器公共接口.md) | Reset Controller | 复位控制器（Reset Controller）的接口。 |
| <a id="row_0_69_0_"></a>1.70.1 | [CH32复位控制器辅助定义（Reset Controller Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__ch32.html) | CH32 reset controller helpers | 用于编码CH32外设复位说明单元（Reset Cells）的宏。 |
| <a id="row_0_69_1_"></a>1.70.2 | [设备树复位控制器API（Devicetree Reset Controller API）](../reset_reference/P007_复位控制器设备树辅助宏.md) | Devicetree Reset Controller API |  |
| <a id="row_0_69_2_"></a><a id="arr_0_69_2_"></a>1.70.3 | [FocalTech FT9001 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__focaltech__ft9001.html) | FocalTech FT9001 reset controller helpers | FocalTech FT9001 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_2_0_"></a>1.70.3.1 | [FocalTech 复位控制模块寄存器（Reset Control Module Registers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html) | FocalTech Reset Control Module Registers | 复位控制模块寄存器的偏移量。 |
| <a id="row_0_69_2_1_"></a><a id="arr_0_69_2_1_"></a>1.70.3.2 | [FocalTech 复位使能/禁用定义（Reset Enable/Disable Definitions）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__enables.html) | FocalTech Reset Enable/Disable Definitions | 外设的复位使能/禁用定义。 |
| <a id="row_0_69_2_1_0_"></a>1.70.3.2.1 | [AHB3RSTCR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ahb3rstcr__resets.html) | AHB3RSTCR Reset Control | AHB3 复位控制寄存器对应的外设。 |
| <a id="row_0_69_2_1_1_"></a>1.70.3.2.2 | [ARITHRSTCR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__arithrstcr__resets.html) | ARITHRSTCR Reset Control | 算法复位控制寄存器（Algorithm Reset Control Register）对应的外设。 |
| <a id="row_0_69_2_1_2_"></a>1.70.3.2.3 | [EPORTRSTR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__eportrstr__resets.html) | EPORTRSTR Reset Control | EPORT 复位控制寄存器对应的外设。 |
| <a id="row_0_69_2_1_3_"></a>1.70.3.2.4 | [IPSRSTCR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ipsrstcr__resets.html) | IPSRSTCR Reset Control | IPS 复位控制寄存器对应的外设。 |
| <a id="row_0_69_2_1_4_"></a>1.70.3.2.5 | [MULTIRSTCR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__multirstcr__resets.html) | MULTIRSTCR Reset Control | 多重复位控制寄存器（Multi Reset Control Register）对应的外设。 |
| <a id="row_0_69_2_1_5_"></a>1.70.3.2.6 | [SYSRSTCR 复位控制（Reset Control）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__sysrstcr__resets.html) | SYSRSTCR Reset Control | 系统复位控制寄存器（System Reset Control Register）对应的外设。 |
| <a id="row_0_69_3_"></a><a id="arr_0_69_3_"></a>1.70.4 | [GigaDevice复位控制器辅助定义](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gigadevice.html) | GigaDevice reset controller helpers | 用于编码GD32外设复位说明单元的宏。 |
| <a id="row_0_69_3_0_"></a>1.70.4.1 | [GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32a50x.html) | GigaDevice GD32A50x reset controller helpers | GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_1_"></a>1.70.4.2 | [GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32e10x.html) | GigaDevice GD32E10x reset controller helpers | GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_2_"></a>1.70.4.3 | [GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32e50x.html) | GigaDevice GD32E50x reset controller helpers | GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_3_"></a>1.70.4.4 | [GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f3x0.html) | GigaDevice GD32F3x0 reset controller helpers | GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_4_"></a>1.70.4.5 | [GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f403.html) | GigaDevice GD32F403 reset controller helpers | GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_5_"></a>1.70.4.6 | [GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f4xx.html) | GigaDevice GD32F4xx reset controller helpers | GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_6_"></a>1.70.4.7 | [GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32l23x.html) | GigaDevice GD32L23x reset controller helpers | GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_3_7_"></a>1.70.4.8 | [GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32vf103.html) | GigaDevice GD32VF103 reset controller helpers | GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers） |
| <a id="row_0_69_4_"></a>1.70.5 | [Nuvoton M48X 复位控制器设备树辅助工具（Reset controller Devicetree helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m48x.html) | Nuvoton M48X Reset controller Devicetree helpers |  |
| <a id="row_0_69_5_"></a><a id="arr_0_69_5_"></a>1.70.6 | [Nuvoton NuMaker复位控制器辅助定义](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__numaker.html) | Nuvoton NuMaker reset controller helpers | Nuvoton NuMaker设备的外设复位说明单元标识符。 |
| <a id="row_0_69_5_0_"></a>1.70.6.1 | [Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m031x.html) | Nuvoton NuMaker M031X reset controller helpers | M031X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_5_1_"></a>1.70.6.2 | [Nuvoton NuMaker M2L31X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m2l31x.html) | Nuvoton NuMaker M2L31X reset controller helpers | M2L31X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_5_2_"></a>1.70.6.3 | [Nuvoton NuMaker M333X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m333x.html) | Nuvoton NuMaker M333X reset controller helpers | M333X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_5_3_"></a>1.70.6.4 | [Nuvoton NuMaker M335X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m335x.html) | Nuvoton NuMaker M335X reset controller helpers | M335X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_5_4_"></a>1.70.6.5 | [Nuvoton NuMaker M46X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m46x.html) | Nuvoton NuMaker M46X reset controller helpers | M46X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_5_5_"></a>1.70.6.6 | [Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m55m1x.html) | Nuvoton NuMaker M55M1X reset controller helpers | M55M1X 设备的外设复位单元（reset-cell）标识符。 |
| <a id="row_0_69_6_"></a>1.70.7 | [Raspberry Pi RP2040复位控制器辅助定义](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2040.html) | Raspberry Pi RP2040 reset controller helpers | RP2040片上系统（System on Chip，SoC）的外设复位说明单元标识符。 |
| <a id="row_0_69_7_"></a>1.70.8 | [Raspberry Pi RP2350复位控制器辅助定义](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2350.html) | Raspberry Pi RP2350 reset controller helpers | RP2350片上系统（System on Chip，SoC）的外设复位说明单元标识符。 |
| <a id="row_0_69_8_"></a>1.70.9 | [复位控制器驱动后端接口（Driver Backend API）](../reset_reference/P002_复位控制器驱动后端.md) | Reset Controller Driver Backend API |  |
| <a id="row_0_69_9_"></a>1.70.10 | [STM32复位控制器辅助定义](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__stm32.html) | STM32 reset controller helpers | 用于编码STM32外设复位说明单元的宏。 |
| <a id="row_0_70_"></a><a id="arr_0_70_"></a>1.71 | [保持存储器（Retained memory）](../hardware/P630_保留内存接口.md) | Retained memory | 保持存储器接口。 |
| <a id="row_0_70_0_"></a>1.71.1 | [保持存储器驱动后端 API](../hardware/P631_保留内存驱动接口.md) | Retained Memory Driver Backend API |  |
| <a id="row_0_71_"></a><a id="arr_0_71_"></a>1.72 | [系统控制与管理接口（SCMI）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html) | SCMI | ARM 系统控制与管理接口（System Control and Management Interface，SCMI）。 |
| <a id="row_0_71_0_"></a><a id="arr_0_71_0_"></a>1.72.1 | [协议（Protocols）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__protocols.html) | Protocols | 标准 SCMI 协议定义。 |
| <a id="row_0_71_0_0_"></a>1.72.1.1 | [基础协议（Base Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html) | Base Protocol | SCMI 基础协议操作。 |
| <a id="row_0_71_0_1_"></a>1.72.1.2 | [时钟协议（Clock Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html) | Clock Protocol | 通过 SCMI 进行时钟管理的操作。 |
| <a id="row_0_71_0_2_"></a>1.72.1.3 | [NXP CPU 域协议（NXP CPU Domain Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html) | NXP CPU Domain Protocol | 通过 SCMI 进行 NXP 厂商专用的 CPU 域管理。 |
| <a id="row_0_71_0_3_"></a>1.72.1.4 | [NXP 系统电源协议（NXP System Power Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__system.html) | NXP System Power Protocol | SCMI 系统电源协议的 NXP 厂商专用扩展。 |
| <a id="row_0_71_0_4_"></a>1.72.1.5 | [引脚控制协议（Pin Control Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html) | Pin Control Protocol | 通过 SCMI 进行引脚配置与控制。 |
| <a id="row_0_71_0_5_"></a>1.72.1.6 | [电源域协议（Power Domain Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html) | Power Domain Protocol | 通过 SCMI 进行电源域状态管理。 |
| <a id="row_0_71_0_6_"></a>1.72.1.7 | [复位域管理协议（Reset domain management Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html) | Reset domain management Protocol | 通过 SCMI 进行复位域管理。 |
| <a id="row_0_71_0_7_"></a>1.72.1.8 | [系统电源协议（System Power Protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html) | System Power Protocol | 通过 SCMI 管理整个系统的电源状态。 |
| <a id="row_0_71_1_"></a><a id="arr_0_71_1_"></a>1.72.2 | [传输（Transport）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html) | Transport | SCMI 传输层的抽象与定义。 |
| <a id="row_0_71_1_0_"></a>1.72.2.1 | [共享内存（Shared Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html) | Shared Memory | SCMI 的共享内存传输定义。 |
| <a id="row_0_71_2_"></a>1.72.3 | [实用工具（Utilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html) | Utilities | SCMI 驱动的辅助宏和工具。 |
| <a id="row_0_72_"></a><a id="arr_0_72_"></a>1.73 | [安全数字主机控制器（SDHC）](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html) | SDHC | 安全数字主机控制器（Secure Digital Host Controller，SDHC）接口。 |
| <a id="row_0_72_0_"></a>1.73.1 | [SDHC 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface__backend.html) | SDHC Driver Backend API |  |
| <a id="row_0_73_"></a><a id="arr_0_73_"></a>1.74 | [单边沿半字节传输（SENT）](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html) | SENT | 单边沿半字节传输（Single Edge Nibble Transmission，SENT）外设接口。 |
| <a id="row_0_73_0_"></a>1.74.1 | [SENT 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html) | SENT Driver Backend API |  |
| <a id="row_0_74_"></a><a id="arr_0_74_"></a>1.75 | [系统管理总线（SMBus）](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html) | SMBus | 系统管理总线（System Management Bus，SMBus）接口。 |
| <a id="row_0_74_0_"></a>1.75.1 | [SMBus 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html) | SMBus Driver Backend API |  |
| <a id="row_0_75_"></a><a id="arr_0_75_"></a>1.76 | [串行外设接口（SPI）](../hardware/P318_SPI公共接口.md) | SPI | 串行外设接口（Serial Peripheral Interface，SPI）控制器接口。 |
| <a id="row_0_75_0_"></a>1.76.1 | [设备树串行外设接口（Devicetree SPI API）](../hardware/P329_SPI设备树宏.md) | Devicetree SPI API |  |
| <a id="row_0_75_1_"></a>1.76.2 | [SPI 驱动后端 API](../hardware/P324_SPI驱动后端接口.md) | SPI Driver Backend API |  |
| <a id="row_0_75_2_"></a>1.76.3 | [SPI 仿真接口（SPI Emulation Interface）](../hardware/P326_SPI模拟接口.md) | SPI Emulation Interface | SPI 仿真接口（SPI Emulation Interface） |
| <a id="row_0_76_"></a>1.77 | [串行线调试端口（SWDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html) | SWDP | 串行线调试端口（Serial Wire Debug Port，SWDP）接口。 |
| <a id="row_0_77_"></a><a id="arr_0_77_"></a>1.78 | [传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html) | Sensor | 传感器接口。 |
| <a id="row_0_77_0_"></a>1.78.1 | [电池 API（Battery APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html) | Battery APIs | 电池 API（Battery API） |
| <a id="row_0_77_1_"></a><a id="arr_0_77_1_"></a>1.78.2 | [设备专用传感器 API 扩展和设备树常量。](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext.html) | Device-specific Sensor API extensions and Devicetree constants. |  |
| <a id="row_0_77_1_0_"></a>1.78.2.1 | [1-Wire 传感器 API（Sensor API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html) | 1-Wire Sensor API | 1-Wire 传感器 API（Sensor API） |
| <a id="row_0_77_1_1_"></a><a id="arr_0_77_1_1_"></a>1.78.2.2 | [AMS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ams.html) | AMS | AMS 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_1_0_"></a>1.78.2.2.1 | [TCS3400](https://docs.zephyrproject.org/latest/doxygen/html/group__tcs3400__interface.html) | TCS3400 | AMS TCS3400 红、绿、蓝、透明光通道（RGBC）传感器。 |
| <a id="row_0_77_1_2_"></a><a id="arr_0_77_1_2_"></a>1.78.2.3 | [Analog Devices](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__adi.html) | Analog Devices | Analog Devices 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_2_0_"></a>1.78.2.3.1 | [ADLTC2990](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html) | ADLTC2990 | Analog Devices ADLTC2990 四通道 I2C 电压、电流和温度监测器。 |
| <a id="row_0_77_1_2_1_"></a>1.78.2.3.2 | [ADT7420](https://docs.zephyrproject.org/latest/doxygen/html/group__adt7420__interface.html) | ADT7420 | Analog Devices ADT7420 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_2_2_"></a>1.78.2.3.3 | [ADXL313](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl313__interface.html) | ADXL313 | Analog Devices ADXL313 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_3_"></a>1.78.2.3.4 | [ADXL345](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl345__interface.html) | ADXL345 | Analog Devices ADXL345 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_4_"></a>1.78.2.3.5 | [ADXL355](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl355__interface.html) | ADXL355 | Analog Devices ADXL355 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_5_"></a>1.78.2.3.6 | [ADXL362](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl362__interface.html) | ADXL362 | Analog Devices ADXL362 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_6_"></a>1.78.2.3.7 | [ADXL367](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html) | ADXL367 | Analog Devices ADXL367 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_7_"></a>1.78.2.3.8 | [ADXL372](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html) | ADXL372 | Analog Devices ADXL372 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_2_8_"></a>1.78.2.3.9 | [MAX17055](https://docs.zephyrproject.org/latest/doxygen/html/group__max17055__interface.html) | MAX17055 | Maxim Integrated MAX17055 电量计（Fuel gauge）。 |
| <a id="row_0_77_1_2_9_"></a>1.78.2.3.10 | [MAX30009](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html) | MAX30009 | Analog Devices MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）。 |
| <a id="row_0_77_1_2_10_"></a>1.78.2.3.11 | [MAX30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html) | MAX30210 | Analog Devices MAX30210 高精度温度传感器（High-Accuracy Temperature Sensor）。 |
| <a id="row_0_77_1_2_11_"></a>1.78.2.3.12 | [MAX31790](https://docs.zephyrproject.org/latest/doxygen/html/group__max31790__interface.html) | MAX31790 | Maxim MAX31790 六通道 PWM 输出风扇转速（RPM）控制器。 |
| <a id="row_0_77_1_2_12_"></a>1.78.2.3.13 | [MAX32664C](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html) | MAX32664C | Maxim Integrated MAX32664C 生物识别传感器集线器（Biometric sensor hub）。 |
| <a id="row_0_77_1_3_"></a><a id="arr_0_77_1_3_"></a>1.78.2.4 | [Angst+Pfister](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ap.html) | Angst+Pfister | Angst+Pfister 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_3_0_"></a>1.78.2.4.1 | [FCX-MLDX5](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html) | FCX-MLDX5 | Angst+Pfister FCX-MLDX5 氧气（O2）传感器。 |
| <a id="row_0_77_1_4_"></a><a id="arr_0_77_1_4_"></a>1.78.2.5 | [Avago Technologies](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__avago.html) | Avago Technologies | Avago Technologies 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_4_0_"></a>1.78.2.5.1 | [APDS9253](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9253__interface.html) | APDS9253 | Broadcom APDS9253 RGB 与环境光传感器。 |
| <a id="row_0_77_1_4_1_"></a>1.78.2.5.2 | [APDS9960](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html) | APDS9960 | Avago APDS9960 环境光、RGB、接近和手势传感器。 |
| <a id="row_0_77_1_5_"></a><a id="arr_0_77_1_5_"></a>1.78.2.6 | [Avia Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__avia.html) | Avia Semiconductor | Avia Semiconductor 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_5_0_"></a>1.78.2.6.1 | [HX711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html) | HX711 | Avia Semiconductor HX711 专用于称重传感器/应变计（Load Cells / Strain Gauges）的 24 位模数转换器（ADC）。 |
| <a id="row_0_77_1_6_"></a><a id="arr_0_77_1_6_"></a>1.78.2.7 | [Bosch Sensortec](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__bosch.html) | Bosch Sensortec | Bosch Sensortec 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_6_0_"></a>1.78.2.7.1 | [BMM350](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html) | BMM350 | Bosch BMM350 三轴磁力计（3-Axis Magnetometer）。 |
| <a id="row_0_77_1_6_1_"></a>1.78.2.7.2 | [BMP581](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html) | BMP581 | Bosch BMP581 大气压力传感器（Barometric pressure sensor）。 |
| <a id="row_0_77_1_7_"></a><a id="arr_0_77_1_7_"></a>1.78.2.8 | [Broadcom](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__brcm.html) | Broadcom | Broadcom 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_7_0_"></a>1.78.2.8.1 | [AFBR-S50](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html) | AFBR-S50 | Broadcom AFBR-S50 三维飞行时间（3D ToF）传感器。 |
| <a id="row_0_77_1_8_"></a>1.78.2.9 | [MCUX 增强型正交解码器（EQDC MCUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html) | EQDC MCUX | NXP MCUX 增强型正交解码器（EQDC）传感器。 |
| <a id="row_0_77_1_9_"></a><a id="arr_0_77_1_9_"></a>1.78.2.10 | [Festo](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__festo.html) | Festo | Festo 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_9_0_"></a>1.78.2.10.1 | [VEAA X-3](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html) | VEAA X-3 | Festo VEAA X-3 压力调节器（Pressure regulator）。 |
| <a id="row_0_77_1_10_"></a><a id="arr_0_77_1_10_"></a>1.78.2.11 | [Fintek](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__fintek.html) | Fintek | Fintek 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_10_0_"></a>1.78.2.11.1 | [F75303](https://docs.zephyrproject.org/latest/doxygen/html/group__f75303__interface.html) | F75303 | Fintek F75303 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_11_"></a><a id="arr_0_77_1_11_"></a>1.78.2.12 | [Gas Sensing Solutions](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__gss.html) | Gas Sensing Solutions | Gas Sensing Solutions 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_11_0_"></a>1.78.2.12.1 | [ExplorIR-M](https://docs.zephyrproject.org/latest/doxygen/html/group__explorir__m__interface.html) | ExplorIR-M | Gas Sensing Solutions ExplorIR-M 二氧化碳（CO2）传感器。 |
| <a id="row_0_77_1_12_"></a><a id="arr_0_77_1_12_"></a>1.78.2.13 | [Hangzhou Grow](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__hzgrow.html) | Hangzhou Grow | Hangzhou Grow 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_12_0_"></a>1.78.2.13.1 | [Grow R502A](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html) | Grow R502A | HZ-Grow GROW_R502A 指纹传感器（Fingerprint sensor）。 |
| <a id="row_0_77_1_13_"></a><a id="arr_0_77_1_13_"></a>1.78.2.14 | [ITE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ite.html) | ITE | ITE 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_13_0_"></a>1.78.2.14.1 | [IT51XXX 转速计（Tachometer）](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__tach__interface.html) | IT51XXX tachometer | ITE IT51xxx 转速计（Tachometer） |
| <a id="row_0_77_1_13_1_"></a>1.78.2.14.2 | [IT8XXX2 转速计（Tachometer）](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__tach__interface.html) | IT8XXX2 tachometer | ITE IT8xxx2 转速计（Tachometer） |
| <a id="row_0_77_1_13_2_"></a>1.78.2.14.3 | [IT8XXX2 电压比较器（Voltage comparator）](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__vcmp__interface.html) | IT8XXX2 voltage comparator | ITE IT8xxx2 电压比较器（Voltage comparator） |
| <a id="row_0_77_1_14_"></a><a id="arr_0_77_1_14_"></a>1.78.2.15 | [Iclegend](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__iclegend.html) | Iclegend | Iclegend 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_14_0_"></a>1.78.2.15.1 | [Iclegend S3KM1110](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html) | Iclegend S3KM1110 | Iclegend S3KM1110 24 GHz 毫米波雷达（mmWave radar）。 |
| <a id="row_0_77_1_15_"></a><a id="arr_0_77_1_15_"></a>1.78.2.16 | [Infineon](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__infineon.html) | Infineon | Infineon 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_15_0_"></a>1.78.2.16.1 | [TLE9104](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html) | TLE9104 | TLE9104 四通道动力总成开关（Powertrain switch）。 |
| <a id="row_0_77_1_16_"></a>1.78.2.17 | [LTC4286](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html) | LTC4286 | Analog Devices LTC4286 热插拔控制器（Hot Swap controller）和功率监测器。 |
| <a id="row_0_77_1_17_"></a><a id="arr_0_77_1_17_"></a>1.78.2.18 | [MEMSIC](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__memsic.html) | MEMSIC | MEMSIC 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_17_0_"></a>1.78.2.18.1 | [MC3419](https://docs.zephyrproject.org/latest/doxygen/html/group__mc3419__interface.html) | MC3419 | MEMSIC MC3419 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_17_1_"></a>1.78.2.18.2 | [MMC56X3](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html) | MMC56X3 | Memsic MMC56X3 三轴磁场与温度传感器。 |
| <a id="row_0_77_1_18_"></a><a id="arr_0_77_1_18_"></a>1.78.2.19 | [Measurement Specialties](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__meas.html) | Measurement Specialties | Measurement Specialties 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_18_0_"></a>1.78.2.19.1 | [HTU31D](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html) | HTU31D | TE Connectivity HTU31D 温湿度传感器（Temperature and humidity sensor）。 |
| <a id="row_0_77_1_19_"></a><a id="arr_0_77_1_19_"></a>1.78.2.20 | [Melexis](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__melexis.html) | Melexis | Melexis 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_19_0_"></a>1.78.2.20.1 | [MLX90394](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html) | MLX90394 | Melexis MLX90394 磁力计（Magnetometer）。 |
| <a id="row_0_77_1_20_"></a><a id="arr_0_77_1_20_"></a>1.78.2.21 | [微芯（Microchip）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__microchip.html) | Microchip | Microchip 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_20_0_"></a>1.78.2.21.1 | [MCP9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html) | MCP9600 | Microchip MCP9600 热电偶电动势（Thermocouple Electromotive Force，EMF）至摄氏温度（°C）转换器。 |
| <a id="row_0_77_1_20_1_"></a>1.78.2.21.2 | [MTCH9010](https://docs.zephyrproject.org/latest/doxygen/html/group__mtch9010__interface.html) | MTCH9010 | Microchip MTCH9010 电容式/电导式液位传感器（Capacitive/conductive liquid-level sensor）。 |
| <a id="row_0_77_1_20_2_"></a>1.78.2.21.3 | [PAC194X](https://docs.zephyrproject.org/latest/doxygen/html/group__pac194x__interface.html) | PAC194X | Microchip PAC194x 功率监测器（Power monitor）。 |
| <a id="row_0_77_1_21_"></a><a id="arr_0_77_1_21_"></a>1.78.2.22 | [恩智浦（NXP）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nxp.html) | NXP | NXP 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_21_0_"></a>1.78.2.22.1 | [MCUX 正交解码器（QDEC MCUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__qdec__mcux.html) | QDEC MCUX | NXP MCUX 正交解码器（QDEC）传感器。 |
| <a id="row_0_77_1_21_1_"></a>1.78.2.22.2 | [NXP S32 正交解码器（QDEC NXP S32）](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nxp__s32__interface.html) | QDEC NXP S32 | NXP S32 正交解码器的 TRGMUX 和 LCU 路由。 |
| <a id="row_0_77_1_22_"></a><a id="arr_0_77_1_22_"></a>1.78.2.23 | [National Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__national.html) | National Semiconductor | National Semiconductor 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_22_0_"></a>1.78.2.23.1 | [LM95234](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html) | LM95234 | LM95234 四路远端二极管与本地温度传感器（Quad Remote Diode and Local Temperature Sensor）。 |
| <a id="row_0_77_1_23_"></a><a id="arr_0_77_1_23_"></a>1.78.2.24 | [Nordic Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nordic.html) | Nordic Semiconductor | Nordic Semiconductor 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_23_0_"></a>1.78.2.24.1 | [nRF 正交解码器（QDEC nRF）](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nrf__interface.html) | QDEC nRF | Nordic nRF 正交解码器（Quadrature decoder，QDEC）。 |
| <a id="row_0_77_1_23_1_"></a>1.78.2.24.2 | [nPM10xx 传感器接口（Sensor interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html) | nPM10xx Sensor interface |  |
| <a id="row_0_77_1_24_"></a><a id="arr_0_77_1_24_"></a>1.78.2.25 | [Nuvoton](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nuvoton.html) | Nuvoton | Nuvoton 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_24_0_"></a>1.78.2.25.1 | [NPCX 转速计（Tachometer）](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html) | NPCX tachometer | Nuvoton NPCX 转速计（Tachometer） |
| <a id="row_0_77_1_25_"></a><a id="arr_0_77_1_25_"></a>1.78.2.26 | [PNI](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__pni.html) | PNI | PNI 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_25_0_"></a>1.78.2.26.1 | [RM3100](https://docs.zephyrproject.org/latest/doxygen/html/group__rm3100__interface.html) | RM3100 | PNI RM3100 三轴磁力计（3-axis magnetometer）。 |
| <a id="row_0_77_1_26_"></a><a id="arr_0_77_1_26_"></a>1.78.2.27 | [Phosense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__phosense.html) | Phosense | Phosense 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_26_0_"></a>1.78.2.27.1 | [XBR818](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html) | XBR818 | Phosense XBR818 10 GHz 雷达（Radar）。 |
| <a id="row_0_77_1_27_"></a><a id="arr_0_77_1_27_"></a>1.78.2.28 | [PixArt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__pixart.html) | PixArt | PixArt 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_27_0_"></a>1.78.2.28.1 | [PAJ7620](https://docs.zephyrproject.org/latest/doxygen/html/group__paj7620__interface.html) | PAJ7620 | Pixart PAJ7620 手势传感器（Gesture sensor）。 |
| <a id="row_0_77_1_27_1_"></a>1.78.2.28.2 | [PAT9136](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html) | PAT9136 | Pixart PAT9136 光流传感器（Optical flow sensor）。 |
| <a id="row_0_77_1_28_"></a><a id="arr_0_77_1_28_"></a>1.78.2.29 | [ROHM](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__rohm.html) | ROHM | ROHM 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_28_0_"></a>1.78.2.29.1 | [BD8LB600FS](https://docs.zephyrproject.org/latest/doxygen/html/group__bd8lb600fs__interface.html) | BD8LB600FS | ROHM Semiconductor BD8LB600FS 开路负载与过流检测（Open load and over-current detection）。 |
| <a id="row_0_77_1_29_"></a><a id="arr_0_77_1_29_"></a>1.78.2.30 | [Realtek](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__realtek.html) | Realtek | Realtek 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_29_0_"></a>1.78.2.30.1 | [Realtek Bee 正交解码器（QDEC）](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html) | Realtek Bee QDEC | Realtek Bee 正交解码器（QDEC） |
| <a id="row_0_77_1_30_"></a>1.78.2.31 | [S9706](https://docs.zephyrproject.org/latest/doxygen/html/group__s9706__interface.html) | S9706 | Hamamatsu S9706 RGB 传感器。 |
| <a id="row_0_77_1_31_"></a><a id="arr_0_77_1_31_"></a>1.78.2.32 | [STMicroelectronics](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__st.html) | STMicroelectronics | STMicroelectronics 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_31_0_"></a>1.78.2.32.1 | [IIS2DLPC](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2dlpc__interface.html) | IIS2DLPC | STMicroelectronics IIS2DLPC 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_1_"></a>1.78.2.32.2 | [IIS2ICLX](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2iclx__interface.html) | IIS2ICLX | STMicroelectronics IIS2ICLX 双轴倾角计（2-axis inclinometer）。 |
| <a id="row_0_77_1_31_2_"></a>1.78.2.32.3 | [IIS3DWB](https://docs.zephyrproject.org/latest/doxygen/html/group__iis3dwb__interface.html) | IIS3DWB | STMicroelectronics IIS3DWB 三轴振动加速度计（3-axis vibration accelerometer）。 |
| <a id="row_0_77_1_31_3_"></a>1.78.2.32.4 | [ISM330DHCX](https://docs.zephyrproject.org/latest/doxygen/html/group__ism330dhcx__interface.html) | ISM330DHCX | STMicroelectronics ISM330DHCX 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_31_4_"></a>1.78.2.32.5 | [ISM6HG256X](https://docs.zephyrproject.org/latest/doxygen/html/group__ism6hg256x__interface.html) | ISM6HG256X | STMicroelectronics ISM6HG256X 高 g 值六轴惯性测量单元（High-g 6-axis IMU）。 |
| <a id="row_0_77_1_31_5_"></a>1.78.2.32.6 | [LIS2DE12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2de12__interface.html) | LIS2DE12 | STMicroelectronics LIS2DE12 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_6_"></a>1.78.2.32.7 | [LIS2DH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html) | LIS2DH | ST Microelectronics LIS2DH 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_7_"></a>1.78.2.32.8 | [LIS2DS12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2ds12__interface.html) | LIS2DS12 | STMicroelectronics LIS2DS12 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_8_"></a>1.78.2.32.9 | [LIS2DU12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2du12__interface.html) | LIS2DU12 | STMicroelectronics LIS2DU12 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_9_"></a>1.78.2.32.10 | [LIS2DUX12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dux12__interface.html) | LIS2DUX12 | STMicroelectronics LIS2DUX12 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_10_"></a>1.78.2.32.11 | [LIS2DW12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html) | LIS2DW12 | STMicroelectronics LIS2DW12 三轴加速度计（3-axis accelerometer）。 |
| <a id="row_0_77_1_31_11_"></a>1.78.2.32.12 | [LPS22HH](https://docs.zephyrproject.org/latest/doxygen/html/group__lps22hh__interface.html) | LPS22HH | STMicroelectronics LPS22HH 压力和温度传感器。 |
| <a id="row_0_77_1_31_12_"></a>1.78.2.32.13 | [LPS2xDF](https://docs.zephyrproject.org/latest/doxygen/html/group__lps2xdf__interface.html) | LPS2xDF | STMicroelectronics LPS2xDF 压力和温度传感器。 |
| <a id="row_0_77_1_31_13_"></a>1.78.2.32.14 | [LSM6DSO](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso__interface.html) | LSM6DSO | STMicroelectronics LSM6DSO 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_31_14_"></a>1.78.2.32.15 | [LSM6DSO16IS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso16is__interface.html) | LSM6DSO16IS | STMicroelectronics LSM6DSO16IS 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_31_15_"></a>1.78.2.32.16 | [LSM6DSV16X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv16x__interface.html) | LSM6DSV16X | STMicroelectronics LSM6DSV16X 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_31_16_"></a>1.78.2.32.17 | [LSM6DSV320X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv320x__interface.html) | LSM6DSV320X | STMicroelectronics LSM6DSV320X 双加速度计与陀螺仪惯性测量单元（Dual accelerometer and gyroscope IMU）。 |
| <a id="row_0_77_1_31_17_"></a>1.78.2.32.18 | [LSM6DSV32X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv32x__interface.html) | LSM6DSV32X | STMicroelectronics LSM6DSV32X 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_31_18_"></a>1.78.2.32.19 | [LSM6DSV80X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv80x__interface.html) | LSM6DSV80X | STMicroelectronics LSM6DSV80X 双加速度计与陀螺仪惯性测量单元（Dual accelerometer and gyroscope IMU）。 |
| <a id="row_0_77_1_31_19_"></a>1.78.2.32.20 | [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html) | LSM6DSVXXX | ST Microelectronics LSM6DSVXXX 三轴惯性测量单元（3-axis IMU）系列。 |
| <a id="row_0_77_1_31_20_"></a>1.78.2.32.21 | [LSM9DS1](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html) | LSM9DS1 | STMicroelectronics LSM9DS1 九轴惯性测量单元（IMU），包含加速度计、陀螺仪和磁力计。 |
| <a id="row_0_77_1_31_21_"></a>1.78.2.32.22 | [STM32 正交解码器（QDEC STM32）](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__stm32__interface.html) | QDEC STM32 | 基于 STM32 定时器的正交解码器（Quadrature decoder，QDEC）。 |
| <a id="row_0_77_1_31_22_"></a>1.78.2.32.23 | [STTS22H](https://docs.zephyrproject.org/latest/doxygen/html/group__stts22h__interface.html) | STTS22H | STMicroelectronics STTS22H 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_31_23_"></a>1.78.2.32.24 | [VL53L0X](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html) | VL53L0X | ST VL53L0X 飞行时间测距传感器（Time-of-flight ranging sensor）。 |
| <a id="row_0_77_1_32_"></a><a id="arr_0_77_1_32_"></a>1.78.2.33 | [ScioSense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__sciosense.html) | ScioSense | ScioSense 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_32_0_"></a>1.78.2.33.1 | [ENS160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html) | ENS160 | ScioSense ENS160 数字金属氧化物多气体传感器（Digital metal-oxide multi-gas sensor）。 |
| <a id="row_0_77_1_33_"></a><a id="arr_0_77_1_33_"></a>1.78.2.34 | [Sensirion](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__sensirion.html) | Sensirion | Sensirion 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_33_0_"></a>1.78.2.34.1 | [SCD4X](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html) | SCD4X | Sensirion SCD4X 二氧化碳（CO2）传感器。 |
| <a id="row_0_77_1_33_1_"></a>1.78.2.34.2 | [SGP40](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html) | SGP40 | Sensirion SGP40 气体传感器。 |
| <a id="row_0_77_1_33_2_"></a>1.78.2.34.3 | [SHT4X](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html) | SHT4X | Sensirion SHT4X 温湿度传感器。 |
| <a id="row_0_77_1_33_3_"></a>1.78.2.34.4 | [STCC4](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html) | STCC4 | Sensirion STCC4 二氧化碳（CO2）传感器。 |
| <a id="row_0_77_1_34_"></a>1.78.2.35 | [传感器坐标轴对齐（Sensor axis alignment）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__axis__align__interface.html) | Sensor axis alignment | 在设备树中重新映射传感器坐标轴时使用的共享常量。 |
| <a id="row_0_77_1_35_"></a><a id="arr_0_77_1_35_"></a>1.78.2.36 | [TDK InvenSense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__tdk.html) | TDK InvenSense | TDK InvenSense 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_35_0_"></a>1.78.2.36.1 | [ICM42686](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html) | ICM42686 | TDK InvenSense ICM42686 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_35_1_"></a>1.78.2.36.2 | [ICM42688](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html) | ICM42688 | TDK InvenSense ICM42688 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_35_2_"></a>1.78.2.36.3 | [ICM4268X](https://docs.zephyrproject.org/latest/doxygen/html/group__icm4268x__interface.html) | ICM4268X | TDK InvenSense ICM4268x 六轴惯性测量单元（IMU）系列。 |
| <a id="row_0_77_1_35_3_"></a>1.78.2.36.4 | [ICM45686](https://docs.zephyrproject.org/latest/doxygen/html/group__icm45686__interface.html) | ICM45686 | TDK InvenSense ICM45686 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_35_4_"></a>1.78.2.36.5 | [ICM566xx](https://docs.zephyrproject.org/latest/doxygen/html/group__icm566xx__interface.html) | ICM566xx | TDK InvenSense ICM566xx 六轴惯性测量单元（IMU）。 |
| <a id="row_0_77_1_36_"></a><a id="arr_0_77_1_36_"></a>1.78.2.37 | [Texas Instruments](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ti.html) | Texas Instruments | Texas Instruments 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_36_0_"></a>1.78.2.37.1 | [BQ274XX](https://docs.zephyrproject.org/latest/doxygen/html/group__bq274xx__interface.html) | BQ274XX | Texas Instruments BQ274xx 电池电量计（Battery fuel gauge）。 |
| <a id="row_0_77_1_36_1_"></a>1.78.2.37.2 | [FDC2X1X](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html) | FDC2X1X | Texas Instruments FDC2X1X 电容传感器（Capacitive sensor）。 |
| <a id="row_0_77_1_36_2_"></a>1.78.2.37.3 | [INA226](https://docs.zephyrproject.org/latest/doxygen/html/group__ina226__interface.html) | INA226 | Texas Instruments INA226 电流与功率监测器。 |
| <a id="row_0_77_1_36_3_"></a>1.78.2.37.4 | [INA230](https://docs.zephyrproject.org/latest/doxygen/html/group__ina230__interface.html) | INA230 | Texas Instruments INA230 电流与功率监测器。 |
| <a id="row_0_77_1_36_4_"></a>1.78.2.37.5 | [INA237](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html) | INA237 | Texas Instruments INA237 电流与功率监测器。 |
| <a id="row_0_77_1_36_5_"></a>1.78.2.37.6 | [INA2XX](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html) | INA2XX | TI INA2xx 电流/功率监测器系列。 |
| <a id="row_0_77_1_36_6_"></a>1.78.2.37.7 | [TMAG5273](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html) | TMAG5273 | Texas Instruments TMAG5273 低功耗线性三维霍尔效应传感器（Low-Power Linear 3D Hall-Effect Sensor）。 |
| <a id="row_0_77_1_36_7_"></a>1.78.2.37.8 | [TMP114](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp114__interface.html) | TMP114 | Texas Instruments TMP114 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_36_8_"></a>1.78.2.37.9 | [TMP11X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html) | TMP11X | TMP11X 温度传感器。 |
| <a id="row_0_77_1_36_9_"></a>1.78.2.37.10 | [TMP451](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html) | TMP451 | TI TMP451 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_37_"></a><a id="arr_0_77_1_37_"></a>1.78.2.38 | [Vishay](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__vishay.html) | Vishay | Vishay 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_37_0_"></a>1.78.2.38.1 | [VEML6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html) | VEML6031 | Vishay VEML6031 高精度环境光传感器（High Accuracy Ambient Light Sensor）。 |
| <a id="row_0_77_1_37_1_"></a>1.78.2.38.2 | [VEML6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html) | VEML6046 | Vishay VEML6046 红、绿、蓝与红外（RGBIR）传感器。 |
| <a id="row_0_77_1_37_2_"></a>1.78.2.38.3 | [VEML60XX](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html) | VEML60XX | Vishay VEML60xx 传感器系列的公共属性。 |
| <a id="row_0_77_1_38_"></a><a id="arr_0_77_1_38_"></a>1.78.2.39 | [Winsen](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__winsen.html) | Winsen | Winsen 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_38_0_"></a>1.78.2.39.1 | [MH-Z19B](https://docs.zephyrproject.org/latest/doxygen/html/group__mhz19b__interface.html) | MH-Z19B | Winsen MH-Z19B 二氧化碳（CO2）传感器。 |
| <a id="row_0_77_1_39_"></a><a id="arr_0_77_1_39_"></a>1.78.2.40 | [Wurth Elektronik](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__we.html) | Wurth Elektronik | Wurth Elektronik 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_39_0_"></a>1.78.2.40.1 | [WSEN-PADS-2511020213301](https://docs.zephyrproject.org/latest/doxygen/html/group__wsen__pads__2511020213301__interface.html) | WSEN-PADS-2511020213301 | Würth Elektronik WSEN-PADS-2511020213301 绝对压力传感器（Absolute pressure sensor）。 |
| <a id="row_0_77_1_39_1_"></a>1.78.2.40.2 | [WSEN-TIDS-2521020222501](https://docs.zephyrproject.org/latest/doxygen/html/group__wsen__tids__2521020222501__interface.html) | WSEN-TIDS-2521020222501 | Würth Elektronik WSEN-TIDS-2521020222501 温度传感器（Temperature sensor）。 |
| <a id="row_0_77_1_40_"></a><a id="arr_0_77_1_40_"></a>1.78.2.41 | [Zephyr](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__zephyr.html) | Zephyr | Zephyr 传感器的设备专用扩展（Device-specific extensions）。 |
| <a id="row_0_77_1_40_0_"></a>1.78.2.41.1 | [通用传感器仿真器（Generic Sensor Emulator）](../hardware/P496_通用传感器仿真接口.md) | Generic Sensor Emulator | 用于测试的通用传感器仿真器。 |
| <a id="row_0_77_2_"></a>1.78.3 | [传感器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html) | Sensor Driver Backend API |  |
| <a id="row_0_77_3_"></a>1.78.4 | [传感器仿真器后端 API](../hardware/P494_传感器仿真后端接口.md) | Sensor emulator backend API | 传感器仿真器后端 API |
| <a id="row_0_78_"></a><a id="arr_0_78_"></a>1.79 | [步进电机（Stepper）](../hardware/P229_步进电机接口目录.md) | Stepper | 步进电机运动控制器和硬件驱动器接口。 |
| <a id="row_0_78_0_"></a><a id="arr_0_78_0_"></a>1.79.1 | [设备专用步进电机 API 扩展。](../hardware/P237_步进器件扩展目录.md) | Device-specific stepper API extensions |  |
| <a id="row_0_78_0_0_"></a>1.79.1.1 | [DRV84XX 步进电机控制器（Stepper Controller）](../hardware/P238_DRV84XX步进扩展.md) | DRV84XX Stepper Controller | TI DRV84XX 步进电机控制器。 |
| <a id="row_0_78_0_1_"></a>1.79.1.2 | [TMCM-3216 步进电机控制器（Stepper Controller）](../hardware/P239_TMCM3216步进扩展.md) | TMCM-3216 Stepper Controller | ADI TMCM-3216 步进电机控制器。 |
| <a id="row_0_78_0_2_"></a>1.79.1.3 | [Trinamic 步进电机控制器（Stepper Controller）](../hardware/P240_Trinamic步进扩展.md) | Trinamic Stepper Controller | Trinamic 步进电机控制器（Stepper Controller） |
| <a id="row_0_78_1_"></a><a id="arr_0_78_1_"></a>1.79.2 | [步进电机硬件驱动器（Stepper Hardware Driver）](../hardware/P232_步进硬件驱动接口.md) | Stepper Hardware Driver | 步进电机硬件驱动器接口。 |
| <a id="row_0_78_1_0_"></a>1.79.2.1 | [步进电机硬件驱动器的驱动后端 API](../hardware/P235_步进硬件驱动后端.md) | Stepper Hardware Driver Driver Backend API |  |
| <a id="row_0_78_2_"></a><a id="arr_0_78_2_"></a>1.79.3 | [步进电机运动控制器（Stepper Motion Controller）](../hardware/P230_步进运动控制接口.md) | Stepper Motion Controller | 步进电机运动控制器接口。 |
| <a id="row_0_78_2_0_"></a>1.79.3.1 | [步进电机运动控制器的驱动后端 API](../hardware/P233_步进运动控制后端.md) | Stepper Motion Controller Driver Backend API |  |
| <a id="row_0_79_"></a><a id="arr_0_79_"></a>1.80 | [系统控制（System control，SYSCON）](../syscon_reference/P001_系统控制器公共接口.md) | System control (SYSCON) | 系统控制寄存器（System Control Registers）的接口。 |
| <a id="row_0_79_0_"></a>1.80.1 | [SYSCON 驱动后端 API](../syscon_reference/P002_系统控制器驱动后端.md) | SYSCON Driver Backend API |  |
| <a id="row_0_80_"></a><a id="arr_0_80_"></a>1.81 | [可信执行环境（TEE）](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html) | TEE | 与可信执行环境（Trusted Execution Environment，TEE）交互的接口。 |
| <a id="row_0_80_0_"></a>1.81.1 | [TEE 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html) | TEE Driver Backend API |  |
| <a id="row_0_81_"></a><a id="arr_0_81_"></a>1.82 | [时间感知 GPIO（Time-aware GPIO）](../timer_reference/P191_时间感知GPIO公共接口.md) | Time-aware GPIO | 时间感知 GPIO 控制器接口。 |
| <a id="row_0_81_0_"></a>1.82.1 | [时间感知 GPIO 驱动后端 API](../timer_reference/P192_时间感知GPIO驱动后端.md) | Time-aware GPIO Driver Backend API |  |
| <a id="row_0_82_"></a><a id="arr_0_82_"></a>1.83 | [通用异步收发器（UART）](../hardware/P330_UART公共接口.md) | UART | 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）控制器接口。 |
| <a id="row_0_82_0_"></a>1.83.1 | [异步 UART API（Async UART API）](../hardware/P334_UART异步接口.md) | Async UART API |  |
| <a id="row_0_82_1_"></a>1.83.2 | [中断驱动 UART API（Interrupt-driven UART API）](../hardware/P333_UART中断驱动接口.md) | Interrupt-driven UART API |  |
| <a id="row_0_82_2_"></a>1.83.3 | [轮询 UART API（Polling UART API）](../hardware/P332_UART轮询接口.md) | Polling UART API |  |
| <a id="row_0_82_3_"></a>1.83.4 | [UART 仿真接口（UART Emulation Interface）](../hardware/P341_UART模拟接口.md) | UART Emulation Interface | UART 仿真接口（UART Emulation Interface） |
| <a id="row_0_83_"></a><a id="arr_0_83_"></a>1.84 | [通用串行总线（USB）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__interfaces.html) | USB | USB 硬件及相关标准的接口。 |
| <a id="row_0_83_0_"></a><a id="arr_0_83_0_"></a>1.84.1 | [电池充电（Battery Charging，BC1.2）](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html) | Battery Charging (BC1.2) | USB 电池充电（Battery Charging，BC1.2）驱动 API。 |
| <a id="row_0_83_0_0_"></a>1.84.1.1 | [BC1.2 仿真器支持 API（原文：BC1.2 backed emulator APIs）](../hardware/P491_BC1点2仿真后端接口.md) | BC1.2 backed emulator APIs | BC1.2 仿真器后端 API（BC1.2 backend emulator APIs） |
| <a id="row_0_83_1_"></a>1.84.2 | [USB 设备控制器（USB Device Controller）](../usb/P030_USB设备控制器API.md) | USB Device Controller | 新的USB设备控制器（UDC）驱动API。 |
| <a id="row_0_83_2_"></a>1.84.3 | [USB 主机控制器（USB Host Controller）](../usb/P073_USB主机控制器API.md) | USB Host Controller | USB主控制器（UHC）的驱动API。 |
| <a id="row_0_83_3_"></a><a id="arr_0_83_3_"></a>1.84.4 | [USB Type-C](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html) | USB Type-C | USB Type-C 线缆和连接器支持。 |
| <a id="row_0_83_3_0_"></a><a id="arr_0_83_3_0_"></a>1.84.4.1 | [USB 电力传输（USB Power Delivery）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html) | USB Power Delivery | USB 电力传输（USB Power Delivery） |
| <a id="row_0_83_3_0_0_"></a>1.84.4.1.1 | [USB 电力传输电源数据对象（USB Power Delivery Power Data Objects）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html) | USB Power Delivery Power Data Objects | 构建 USB 电力传输电源数据对象（Power Data Object，PDO）的宏。 |
| <a id="row_0_83_3_1_"></a><a id="arr_0_83_3_1_"></a>1.84.4.2 | [USB Type-C 端口控制器 API（Port Controller API）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html) | USB Type-C Port Controller API | USB Type-C 端口控制器 API（Port Controller API） |
| <a id="row_0_83_3_1_0_"></a>1.84.4.2.1 | [USB Type-C 端口控制器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html) | USB Type-C Port Controller Driver Backend API |  |
| <a id="row_0_83_3_2_"></a><a id="arr_0_83_3_2_"></a>1.84.4.3 | [USB Type-C 电源路径控制器（Power Path Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html) | USB Type-C Power Path Controller | USB Type-C 电源路径控制器（Power Path Controller） |
| <a id="row_0_83_3_2_0_"></a>1.84.4.3.1 | [USB Type-C 电源路径控制器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller__backend.html) | USB Type-C Power Path Controller Driver Backend API |  |
| <a id="row_0_83_3_3_"></a><a id="arr_0_83_3_3_"></a>1.84.4.4 | [USB-C 总线电源（VBUS）API](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html) | USB-C VBUS API | USB-C 总线电源（VBUS）API |
| <a id="row_0_83_3_3_0_"></a>1.84.4.4.1 | [USB-C VBUS 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api__backend.html) | USB-C VBUS Driver Backend API |  |
| <a id="row_0_84_"></a><a id="arr_0_84_"></a>1.85 | [虚拟 I/O（VIRTIO）](../hardware/P571_VirtIO设备接口.md) | VIRTIO | 虚拟 I/O（Virtual I/O，VIRTIO）设备接口。 |
| <a id="row_0_84_0_"></a>1.85.1 | [VIRTIO 驱动后端 API](../hardware/P580_VirtIO驱动后端接口.md) | VIRTIO Driver Backend API |  |
| <a id="row_0_84_1_"></a>1.85.2 | [虚拟队列接口（Virtqueue Interface）](../hardware/P572_VirtIO虚拟队列接口.md) | Virtqueue Interface | 虚拟队列接口（Virtqueue Interface） |
| <a id="row_0_85_"></a><a id="arr_0_85_"></a>1.86 | [视频驱动（Video Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html) | Video Drivers | 供视频子系统使用的视频驱动 API。 |
| <a id="row_0_85_0_"></a>1.86.1 | [视频控制项（Video Controls）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html) | Video Controls | 访问驱动程序视频控制项时使用的类型。 |
| <a id="row_0_85_1_"></a>1.86.2 | [视频驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html) | Video Driver Backend API |  |
| <a id="row_0_85_2_"></a>1.86.3 | [视频接口总线类型（Video interface bus types）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__bus__types.html) | Video interface bus types | 设备树 `bus-type` 属性使用的总线类型值。 |
| <a id="row_0_86_"></a><a id="arr_0_86_"></a>1.87 | [唤醒控制器（WUC）](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html) | WUC | 唤醒控制器（Wakeup Controller，WUC）驱动 API。 |
| <a id="row_0_86_0_"></a>1.87.1 | [设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md) | Devicetree WUC Controller API |  |
| <a id="row_0_86_1_"></a>1.87.2 | [WUC 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html) | WUC Driver Backend API |  |
| <a id="row_0_87_"></a><a id="arr_0_87_"></a>1.88 | [看门狗（Watchdog）](../timer_reference/P001_看门狗公共接口.md) | Watchdog | 看门狗设备接口。 |
| <a id="row_0_87_0_"></a>1.88.1 | [看门狗驱动后端 API](../timer_reference/P002_看门狗驱动后端接口.md) | Watchdog Driver Backend API |  |

## 1.2\_设备模型（Device Model）。

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_1_"></a><a id="arr_1_"></a>2 | [设备模型（Device Model）。](../device_reference/P001_设备模型公共接口.md) | Device Model | 设备模型（Device Model）。 |
| <a id="row_1_0_"></a><a id="arr_1_0_"></a>2.1 | [设备内存映射 I/O 管理（Device memory-mapped IO management）](../device_reference/P011_设备MMIO管理概述.md) | Device memory-mapped IO management | 用于在RAM或ROM中适当管理驱动内存映射输入输出（Memory-Mapped Input/Output，MMIO）区域的定义与辅助宏。 |
| <a id="row_1_0_0_"></a>2.1.1 | [命名 MMIO 区域宏（Named MMIO region macros）](../device_reference/P013_设备命名区域MMIO.md) | Named MMIO region macros | 适用于需要管理多个MMIO区域，并按名称引用各区域的驱动。 |
| <a id="row_1_0_1_"></a>2.1.2 | [单个 MMIO 区域宏（Single MMIO region macros）](../device_reference/P012_设备单区域MMIO.md) | Single MMIO region macros | 适用于只需管理一个MMIO区域的驱动；这是最常见的情况。 |
| <a id="row_1_0_2_"></a>2.1.3 | [顶层 MMIO 区域宏（Top-level MMIO region macros）](../device_reference/P014_顶层MMIO区域.md) | Top-level MMIO region macros | 适用于不使用Zephyr驱动模型、也不将struct device与驱动实例关联的驱动。 |
| <a id="row_1_1_"></a>2.2 | [EM32 时钟门控标识符（Clock Gating IDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__em32__clock__gating__ids.html) | EM32 Clock Gating IDs | EM32平台外设的时钟门控（Clock Gating）ID。 |

## 1.3\_设备树（Devicetree）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_2_"></a><a id="arr_2_"></a>3 | [设备树（Devicetree）](../dt_overview_reference/P001_设备树API总览.md) | Devicetree | `devicetree.h` 应用程序编程接口（API）。 |
| <a id="row_2_0_"></a>3.1 | [逐项展开宏（For-each Macros）](../dt_foreach_reference/P001_设备树遍历宏.md) | &quot;For-each&quot; macros | 重要：不能在设备树逐项展开宏（DT For-each Macros）自身的展开过程中再次使用同一个宏。 |
| <a id="row_2_1_"></a>3.2 | [总线辅助宏（Bus Helpers）](../dt_node_reference/P001_设备树总线查询宏.md) | Bus helpers |  |
| <a id="row_2_2_"></a>3.3 | [选定节点（Chosen Nodes）](../dt_node_reference/P002_设备树chosen节点宏.md) | Chosen nodes |  |
| <a id="row_2_3_"></a>3.4 | [依赖跟踪（Dependency Tracking）](../dt_node_reference/P004_设备树依赖顺序宏.md) | Dependency tracking |  |
| <a id="row_2_4_"></a>3.5 | [设备树 CAN API（Devicetree CAN API）](../hardware/P373_CAN设备树宏.md) | Devicetree CAN API |  |
| <a id="row_2_5_"></a><a id="arr_2_5_"></a>3.6 | [设备树时钟 API（Devicetree Clocks API）](../timer_reference/P107_设备树时钟获取宏.md) | Devicetree Clocks API |  |
| <a id="row_2_5_0_"></a>3.6.1 | [Aesc Silicon 时钟域标识符（Clock domain identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html) | Aesc Silicon clock domain identifiers | Aesc Silicon ElemRV-H片上系统（SoC）的时钟域标识符。 |
| <a id="row_2_5_1_"></a>3.6.2 | [敦泰（FocalTech）FT9001 时钟标识符（Clock identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html) | FocalTech FT9001 clock identifiers | FocalTech FT9001的时钟标识符（Clock Identifiers）。 |
| <a id="row_2_5_2_"></a>3.6.3 | [微芯（Microchip）SmartFusion2 时钟标识符](https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html) | Microchip SmartFusion2 clock identifiers | Microchip SmartFusion2 片上系统（SoC）的时钟标识符。 |
| <a id="row_2_5_3_"></a><a id="arr_2_5_3_"></a>3.6.4 | [NXP i.MX952 时钟源（Clock Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html) | NXP i.MX952 Clock Sources | i.MX952 SoC 的根时钟源（Root clock sources）。 |
| <a id="row_2_5_3_0_"></a>3.6.4.1 | [外设时钟（Peripheral Clocks），编号 41–163](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html) | Peripheral Clocks (41-163) | 基于 MIMX9529 `fsl_clock.h` 的外设时钟定义。 |
| <a id="row_2_6_"></a>3.7 | [设备树计数器捕获 API（Devicetree Counter Captures API）](../timer_reference/P034_计数器捕获设备树宏.md) | Devicetree Counter Captures API |  |
| <a id="row_2_7_"></a>3.8 | [设备树 DMA API（Devicetree DMA API）](../dma_reference/P008_DMA设备树宏.md) | Devicetree DMA API |  |
| <a id="row_2_8_"></a>3.9 | [设备树显示接口（Devicetree Display API）](../hardware/P227_设备树显示接口.md) | Devicetree Display API |  |
| <a id="row_2_9_"></a>3.10 | [设备树固定分区接口（Devicetree Fixed Partition API）](../dt_partition_reference/P002_设备树固定分区宏.md) | Devicetree Fixed Partition API |  |
| <a id="row_2_10_"></a><a id="arr_2_10_"></a>3.11 | [设备树通用输入输出接口（Devicetree GPIO API）](../hardware/P290_设备树GPIO宏.md) | Devicetree GPIO API |  |
| <a id="row_2_10_0_"></a><a id="arr_2_10_0_"></a>3.11.1 | [GPIO 排针（Pin headers）](../hardware/P291_GPIO排针目录.md) | GPIO pin headers | 常见 GPIO 排针所引出引脚的常量。 |
| <a id="row_2_10_0_0_"></a>3.11.1.1 | [ArduCam FFC 40 引脚摄像头连接器（Camera connector）](../hardware/P292_ArduCamFFC40针连接器.md) | ArduCam FFC 40-pin camera connector. | ArduCam FFC 40 引脚摄像头连接器所引出引脚的常量。 |
| <a id="row_2_10_0_1_"></a>3.11.1.2 | [Arducam DVP 20 引脚连接器（Connector）](../hardware/P293_ArducamDVP连接器.md) | Arducam DVP 20-pin connector | Arducam DVP 20 引脚或 18 引脚连接器所引出引脚的常量。 |
| <a id="row_2_10_0_2_"></a>3.11.1.3 | [Arduino MKR 排针（Header）](../hardware/P294_ArduinoMKR排针.md) | Arduino MKR header | Arduino MKR 排针所引出引脚的常量。 |
| <a id="row_2_10_0_3_"></a>3.11.1.4 | [Arduino Mega 排针（Header）](../hardware/P295_ArduinoMega排针.md) | Arduino Mega header | Arduino Mega 排针所引出引脚的常量。 |
| <a id="row_2_10_0_4_"></a>3.11.1.5 | [Arduino Nano 排针（Header）](../hardware/P296_ArduinoNano排针.md) | Arduino Nano header | Arduino Nano 排针所引出引脚的常量。 |
| <a id="row_2_10_0_5_"></a>3.11.1.6 | [Arduino Uno（R3）排针（Header）](../hardware/P297_ArduinoUno排针.md) | Arduino Uno (R3) header | Arduino Uno（R3）排针所引出引脚的常量。 |
| <a id="row_2_10_0_6_"></a>3.11.1.7 | [M.2 Key A 串行存储器连接器（Serial memory connector）](../hardware/P298_M2串行存储器连接器.md) | M.2 Key A serial memory connector | ST M.2 串行存储器连接器引出的非电源信号（Non-power signals）常量。 |
| <a id="row_2_10_0_7_"></a>3.11.1.8 | [树莓派 CSI 连接器（Raspberry Pi CSI connector）](../hardware/P299_树莓派CSI连接器.md) | Raspberry Pi CSI connector | 树莓派 CSI 摄像头连接器所引出引脚的常量。 |
| <a id="row_2_10_0_8_"></a>3.11.1.9 | [ST Morpho 排针（Header）](../hardware/P300_STMorpho排针.md) | ST Morpho header | ST Morpho 排针所引出引脚的常量。 |
| <a id="row_2_10_0_9_"></a>3.11.1.10 | [ST Zio 排针（Header）](../hardware/P301_STZio排针.md) | ST Zio header | ST Zio 排针所引出引脚的常量。 |
| <a id="row_2_10_0_10_"></a>3.11.1.11 | [STMod+ 连接器（Connector）](../hardware/P302_STModPlus连接器.md) | STMod+ connector | STMod+ 连接器所引出引脚的常量。 |
| <a id="row_2_10_0_11_"></a>3.11.1.12 | [WisBlock IO 插槽连接器（Slot connector）](../hardware/P303_WisBlockIO插槽.md) | WisBlock IO slot connector | WisBlock IO 插槽连接器所引出引脚的常量。 |
| <a id="row_2_10_0_12_"></a>3.11.1.13 | [WisBlock 传感器插槽连接器（Sensor Slot connector）](../hardware/P304_WisBlock传感器插槽.md) | WisBlock Sensor Slot connector | RAKwireless WisBlock 传感器插槽所引出引脚的常量。 |
| <a id="row_2_11_"></a>3.12 | [设备树硬件自旋锁接口（Devicetree HW Spinlock API）](../intercore_reference/P008_硬件自旋锁设备树宏.md) | Devicetree HW spinlock API |  |
| <a id="row_2_12_"></a>3.13 | [设备树输入输出通道接口（Devicetree IO Channels API）](../dt_connection_reference/P001_设备树I_O通道宏.md) | Devicetree IO Channels API |  |
| <a id="row_2_13_"></a>3.14 | [设备树中断CPU接口（Devicetree Interrupt CPU API）](../dt_node_reference/P003_设备树CPU节点宏.md) | Devicetree Interrupt CPU API |  |
| <a id="row_2_14_"></a><a id="arr_2_14_"></a>3.15 | [设备树中断控制器接口（Devicetree Interrupt Controller API）](../dt_irq_reference/P002_设备树中断控制器宏.md) | Devicetree Interrupt Controller API |  |
| <a id="row_2_14_0_"></a>3.15.1 | [Arm通用中断控制器（GIC Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html) | Arm GIC interrupt controller | Arm 通用中断控制器（Generic Interrupt Controller，GIC）的设备树宏。 |
| <a id="row_2_14_1_"></a>3.15.2 | [Espressif ESP32 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32__intmux.html) | Espressif ESP32 interrupt allocator | Espressif ESP32 的设备树中断源编号。 |
| <a id="row_2_14_2_"></a>3.15.3 | [Espressif ESP32-C2 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c2__intmux.html) | Espressif ESP32-C2 interrupt allocator | Espressif ESP32-C2 的设备树中断源编号。 |
| <a id="row_2_14_3_"></a>3.15.4 | [Espressif ESP32-C3 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c3__intmux.html) | Espressif ESP32-C3 interrupt allocator | Espressif ESP32-C3 的设备树中断源编号。 |
| <a id="row_2_14_4_"></a>3.15.5 | [Espressif ESP32-C5 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c5__intmux.html) | Espressif ESP32-C5 interrupt allocator | Espressif ESP32-C5 的设备树中断源编号。 |
| <a id="row_2_14_5_"></a>3.15.6 | [Espressif ESP32-C6 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c6__intmux.html) | Espressif ESP32-C6 interrupt allocator | Espressif ESP32-C6 的设备树中断源编号。 |
| <a id="row_2_14_6_"></a>3.15.7 | [Espressif ESP32-C61 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c61__intmux.html) | Espressif ESP32-C61 interrupt allocator | Espressif ESP32-C61 的设备树中断源编号。 |
| <a id="row_2_14_7_"></a>3.15.8 | [Espressif ESP32-H2 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32h2__intmux.html) | Espressif ESP32-H2 interrupt allocator | Espressif ESP32-H2 的设备树中断源编号。 |
| <a id="row_2_14_8_"></a>3.15.9 | [Espressif ESP32-P4 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32p4__intmux.html) | Espressif ESP32-P4 interrupt allocator | Espressif ESP32-P4 的设备树中断源编号。 |
| <a id="row_2_14_9_"></a>3.15.10 | [Espressif ESP32-S2 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32s2__intmux.html) | Espressif ESP32-S2 interrupt allocator | Espressif ESP32-S2 的设备树中断源编号。 |
| <a id="row_2_14_10_"></a>3.15.11 | [Espressif ESP32-S3 中断分配器（Interrupt allocator）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32s3__intmux.html) | Espressif ESP32-S3 interrupt allocator | Espressif ESP32-S3 的设备树中断源编号。 |
| <a id="row_2_14_11_"></a>3.15.12 | [ITE IT51XXX中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__intc.html) | ITE IT51XXX interrupt controller | ITE IT51XXX 中断控制器（Interrupt Controller，INTC）的设备树宏。 |
| <a id="row_2_14_12_"></a>3.15.13 | [ITE IT51XXX唤醒控制器（Wake-up Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__wuc.html) | ITE IT51XXX wake-up controller | ITE IT51XXX 唤醒控制器（Wake-Up Controller，WUC）的设备树宏。 |
| <a id="row_2_14_13_"></a>3.15.14 | [ITE IT8XXX2中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html) | ITE IT8XXX2 interrupt controller | ITE IT8XXX2 中断控制器（INTC）的设备树宏。 |
| <a id="row_2_14_14_"></a>3.15.15 | [ITE IT8XXX2唤醒控制器（Wake-up Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html) | ITE IT8XXX2 wake-up controller | ITE IT8XXX2 唤醒控制器（WUC）的设备树宏。 |
| <a id="row_2_14_15_"></a>3.15.16 | [Infineon XMC4xxx中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html) | Infineon XMC4xxx interrupt controller | Infineon XMC4xxx 中断控制器的设备树宏。 |
| <a id="row_2_14_16_"></a>3.15.17 | [Intel I/O APIC中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__intel__ioapic.html) | Intel I/O APIC interrupt controller | Intel I/O APIC 中断控制器的设备树标志。 |
| <a id="row_2_14_17_"></a>3.15.18 | [Microchip SmartFusion2中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__microchip__smartfusion2__irq.html) | Microchip SmartFusion2 interrupt controller | Microchip SmartFusion2 中断控制器的设备树宏。 |
| <a id="row_2_14_18_"></a>3.15.19 | [Microchip XEC ECIA中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html) | Microchip XEC ECIA interrupt controller | Microchip XEC ECIA 中断聚合器（Interrupt Aggregator）的设备树宏。 |
| <a id="row_2_14_19_"></a>3.15.20 | [OpenISA RV32M1中断多路复用器（INTMUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__openisa__intmux.html) | OpenISA RV32M1 INTMUX | OpenISA RV32M1 中断多路复用器（Interrupt Multiplexer，INTMUX）的设备树宏。 |
| <a id="row_2_14_20_"></a>3.15.21 | [Realtek RTS5817中断源（Interrupt Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__realtek__rts5817__intc.html) | Realtek RTS5817 interrupt sources | Realtek RTS5817 的设备树中断源编号。 |
| <a id="row_2_14_21_"></a>3.15.22 | [TI VIM中断控制器（Interrupt Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html) | TI VIM interrupt controller | Texas Instruments 向量中断管理器（Vectored Interrupt Manager，VIM）的设备树标志。 |
| <a id="row_2_15_"></a>3.16 | [设备树邮箱接口（Devicetree MBOX API）](../intercore_reference/P021_邮箱设备树访问宏.md) | Devicetree MBOX API |  |
| <a id="row_2_16_"></a>3.17 | [设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md) | Devicetree MUX API |  |
| <a id="row_2_17_"></a>3.18 | [设备树映射分区接口（Devicetree Mapped Partition API）](../dt_partition_reference/P005_设备树映射分区宏.md) | Devicetree Mapped Partition API |  |
| <a id="row_2_18_"></a>3.19 | [设备树脉宽调制接口（Devicetree PWMs API）](../hardware/P264_设备树PWM宏.md) | Devicetree PWMs API |  |
| <a id="row_2_19_"></a>3.20 | [设备树分区接口（Devicetree Partition API）](../dt_partition_reference/P001_设备树通用分区宏.md) | Devicetree Partition API |  |
| <a id="row_2_20_"></a>3.21 | [设备树端口与端点接口（Devicetree Port Endpoint API）](../dt_connection_reference/P010_设备树端口与端点宏.md) | Devicetree Port Endpoint API |  |
| <a id="row_2_21_"></a><a id="arr_2_21_"></a>3.22 | [设备树稳压器接口（Devicetree Regulator API）](../power/P081_设备树稳压器辅助接口目录.md) | Devicetree Regulator API |  |
| <a id="row_2_21_0_"></a>3.22.1 | [ADP5360 设备树辅助工具（Devicetree helpers）](../power/P085_ADP5360稳压器设备树辅助接口.md) | ADP5360 Devicetree helpers | Analog Devices ADP5360 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_1_"></a>3.22.2 | [AXP192 设备树辅助工具（Devicetree helpers）](../power/P086_AXP192稳压器设备树辅助接口.md) | AXP192 Devicetree helpers | X-Powers AXP192 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_2_"></a>3.22.3 | [MAX20335 设备树辅助工具（Devicetree helpers）](../power/P087_MAX20335稳压器设备树辅助接口.md) | MAX20335 Devicetree helpers | Maxim MAX20335 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_3_"></a>3.22.4 | [MAX20362 设备树辅助工具（Devicetree helpers）](../power/P088_MAX20362稳压器设备树辅助接口.md) | MAX20362 Devicetree helpers | Analog Devices MAX20362 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_4_"></a>3.22.5 | [MSPM0 VREF 设备树辅助工具（Devicetree helpers）](../power/P089_MSPM0参考电压设备树辅助接口.md) | MSPM0 VREF Devicetree helpers | Texas Instruments MSPM0 VREF 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_5_"></a>3.22.6 | [NXP VREF 设备树辅助工具（Devicetree helpers）](../power/P090_NXP参考电压设备树辅助接口.md) | NXP VREF Devicetree helpers | NXP VREF 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_6_"></a>3.22.7 | [Raspberry Pi Pico 稳压器设备树辅助工具（Regulator Devicetree helpers）](../power/P091_RaspberryPi_Pico稳压器设备树辅助接口.md) | Raspberry Pi Pico regulator Devicetree helpers | Raspberry Pi Pico 片上稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_7_"></a>3.22.8 | [Silicon Labs DCDC 设备树辅助工具（Devicetree helpers）](../power/P092_SiliconLabs_DCDC设备树辅助接口.md) | Silicon Labs DCDC Devicetree helpers | Silicon Labs DCDC 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_8_"></a>3.22.9 | [Texas Instruments TPS6287x 设备树辅助工具（Devicetree helpers）](../power/P093_TPS6287x稳压器设备树辅助接口.md) | Texas Instruments TPS6287x Devicetree helpers | Texas instruments TPS6287x 稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_9_"></a>3.22.10 | [nPM10xx 设备树辅助工具（Devicetree helpers）](../power/P094_nPM10xx稳压器设备树辅助接口.md) | nPM10xx Devicetree helpers | Nordic nPM10 系列电源管理芯片（PMIC）的稳压器驱动设备树辅助工具。 |
| <a id="row_2_21_10_"></a>3.22.11 | [nPM1100 设备树辅助工具（Devicetree helpers）](../power/P095_nPM1100稳压器设备树辅助接口.md) | nPM1100 Devicetree helpers | Nordic nPM1100 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_11_"></a>3.22.12 | [nPM13xx 设备树辅助工具（Devicetree helpers）](../power/P096_nPM13xx稳压器设备树辅助接口.md) | nPM13xx Devicetree helpers | Nordic nPM13 系列电源管理芯片（PMIC）的稳压器驱动设备树辅助工具。 |
| <a id="row_2_21_12_"></a>3.22.13 | [nPM2100 设备树辅助工具（Devicetree helpers）](../power/P097_nPM2100稳压器设备树辅助接口.md) | nPM2100 Devicetree helpers | Nordic nPM2100 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_13_"></a>3.22.14 | [nPM6001 设备树辅助工具（Devicetree helpers）](../power/P098_nPM6001稳压器设备树辅助接口.md) | nPM6001 Devicetree helpers | Nordic nPM6001 电源管理芯片（PMIC）的稳压器驱动 设备树辅助工具（Devicetree helpers） |
| <a id="row_2_21_14_"></a>3.22.15 | [nRF5X 设备树辅助工具（Devicetree helpers）](../power/P099_nRF5X稳压器设备树辅助接口.md) | nRF5X Devicetree helpers | NRF5X 稳压器设备树辅助工具。 |
| <a id="row_2_22_"></a><a id="arr_2_22_"></a>3.23 | [设备树Renesas RA事件链接控制器辅助宏（Devicetree Renesas RA ELC Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra__elc.html) | Devicetree Renesas RA ELC helpers |  |
| <a id="row_2_22_0_"></a>3.23.1 | [Renesas RA2A1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra2a1__elc.html) | Renesas RA2A1 ELC devicetree macros | 用于 Renesas RA2A1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_1_"></a>3.23.2 | [Renesas RA2L1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra2l1__elc.html) | Renesas RA2L1 ELC devicetree macros | 用于 Renesas RA2L1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_2_"></a>3.23.3 | [Renesas RA4E1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4e1__elc.html) | Renesas RA4E1 ELC devicetree macros | 用于 Renesas RA4E1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_3_"></a>3.23.4 | [Renesas RA4E2 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4e2__elc.html) | Renesas RA4E2 ELC devicetree macros | 用于 Renesas RA4E2 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_4_"></a>3.23.5 | [Renesas RA4L1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4l1__elc.html) | Renesas RA4L1 ELC devicetree macros | 用于 Renesas RA4L1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_5_"></a>3.23.6 | [Renesas RA4M1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m1__elc.html) | Renesas RA4M1 ELC devicetree macros | 用于 Renesas RA4M1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_6_"></a>3.23.7 | [Renesas RA4M2 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m2__elc.html) | Renesas RA4M2 ELC devicetree macros | 用于 Renesas RA4M2 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_7_"></a>3.23.8 | [Renesas RA4M3 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m3__elc.html) | Renesas RA4M3 ELC devicetree macros | 用于 Renesas RA4M3 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_8_"></a>3.23.9 | [Renesas RA4T1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4t1__elc.html) | Renesas RA4T1 ELC devicetree macros | 用于 Renesas RA4T1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_9_"></a>3.23.10 | [Renesas RA4W1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4w1__elc.html) | Renesas RA4W1 ELC devicetree macros | 用于 Renesas RA4W1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_10_"></a>3.23.11 | [Renesas RA6E1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6e1__elc.html) | Renesas RA6E1 ELC devicetree macros | 用于 Renesas RA6E1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_11_"></a>3.23.12 | [Renesas RA6E2 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6e2__elc.html) | Renesas RA6E2 ELC devicetree macros | 用于 Renesas RA6E2 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_12_"></a>3.23.13 | [Renesas RA6M1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m1__elc.html) | Renesas RA6M1 ELC devicetree macros | 用于 Renesas RA6M1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_13_"></a>3.23.14 | [Renesas RA6M2 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m2__elc.html) | Renesas RA6M2 ELC devicetree macros | 用于 Renesas RA6M2 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_14_"></a>3.23.15 | [Renesas RA6M3 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m3__elc.html) | Renesas RA6M3 ELC devicetree macros | 用于 Renesas RA6M3 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_15_"></a>3.23.16 | [Renesas RA6M4 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m4__elc.html) | Renesas RA6M4 ELC devicetree macros | 用于 Renesas RA6M4 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_16_"></a>3.23.17 | [Renesas RA6M5 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m5__elc.html) | Renesas RA6M5 ELC devicetree macros | 用于 Renesas RA6M5 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_17_"></a>3.23.18 | [Renesas RA8D1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8d1__elc.html) | Renesas RA8D1 ELC devicetree macros | 用于 Renesas RA8D1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_18_"></a>3.23.19 | [Renesas RA8E1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8e1__elc.html) | Renesas RA8E1 ELC devicetree macros | 用于 Renesas RA8E1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_19_"></a>3.23.20 | [Renesas RA8M1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8m1__elc.html) | Renesas RA8M1 ELC devicetree macros | 用于 Renesas RA8M1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_22_20_"></a>3.23.21 | [Renesas RA8T1 事件链接控制器（ELC）的设备树宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8t1__elc.html) | Renesas RA8T1 ELC devicetree macros | 用于 Renesas RA8T1 事件链接控制器（ELC）路由的设备树事件宏和外设宏。 |
| <a id="row_2_23_"></a>3.24 | [设备树复位控制器API（Devicetree Reset Controller API）](../reset_reference/P007_复位控制器设备树辅助宏.md) | Devicetree Reset Controller API |  |
| <a id="row_2_24_"></a>3.25 | [设备树串行外设接口（Devicetree SPI API）](../hardware/P329_SPI设备树宏.md) | Devicetree SPI API |  |
| <a id="row_2_25_"></a>3.26 | [设备树静态随机存取存储器接口（Devicetree SRAM API）](../dt_overview_reference/P005_选定SRAM区域宏.md) | Devicetree SRAM API |  |
| <a id="row_2_26_"></a>3.27 | [设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md) | Devicetree WUC Controller API |  |
| <a id="row_2_27_"></a>3.28 | [设备树电池辅助宏（Devicetree Battery Helpers）](../dt_overview_reference/P002_电池开路电压曲线宏.md) | Devicetree battery helpers |  |
| <a id="row_2_28_"></a><a id="arr_2_28_"></a>3.29 | [设备树内存属性（Devicetree Memory Attributes）](../dt_memory_attribute_reference/P001_设备树内存属性总览.md) | Devicetree memory attributes | 用于内存属性（Memory Attributes）的设备树宏。 |
| <a id="row_2_28_0_"></a><a id="arr_2_28_0_"></a>3.29.1 | [架构专用内存属性（Architecture-specific Memory Attributes）。](../dt_memory_attribute_reference/P003_架构专用内存属性宏.md) | Architecture-specific memory attributes | 架构专用内存属性（Architecture-specific Memory Attributes）。 |
| <a id="row_2_28_0_0_"></a>3.29.1.1 | [Arm内存保护单元属性（ARM MPU Memory Attributes）](../dt_memory_attribute_reference/P018_Arm_MPU内存类型宏.md) | ARM MPU memory attributes |  |
| <a id="row_2_28_0_1_"></a>3.29.1.2 | [Arm64内存属性（ARM64 Memory Attributes）](../dt_memory_attribute_reference/P019_Arm64_MMU内存类型宏.md) | ARM64 memory attributes |  |
| <a id="row_2_28_0_2_"></a>3.29.1.3 | [RISC-V内存属性（RISC-V Memory Attributes）](../dt_memory_attribute_reference/P020_RISC_V内存类型宏.md) | RISC-V memory attributes |  |
| <a id="row_2_28_0_3_"></a>3.29.1.4 | [Xtensa内存属性（Xtensa Memory Attributes）](../dt_memory_attribute_reference/P021_Xtensa内存类型宏.md) | Xtensa memory attributes |  |
| <a id="row_2_28_1_"></a>3.29.2 | [通用内存属性（Generic Memory Attributes）](../dt_memory_attribute_reference/P002_通用内存属性宏.md) | Generic memory attributes | 应当适用于所有架构的通用内存属性（Generic Memory Attributes）。 |
| <a id="row_2_28_2_"></a><a id="arr_2_28_2_"></a>3.29.3 | [软件专用内存属性（Software-specific Memory Attributes）。](../dt_memory_attribute_reference/P004_软件专用内存属性宏.md) | Software-specific memory attributes | 软件专用内存属性（Software-specific Memory Attributes）。 |
| <a id="row_2_28_2_0_"></a>3.29.3.1 | [软件定义的内存属性（Software-defined Memory Attributes）](../dt_memory_attribute_reference/P017_软件内存分配属性宏.md) | Software-defined memory attributes |  |
| <a id="row_2_29_"></a>3.30 | [存在性检查（Existence Checks）](../dt_identity_reference/P002_设备树存在性与状态宏.md) | Existence checks |  |
| <a id="row_2_30_"></a>3.31 | [基于实例的设备树接口（Instance-based Devicetree APIs）](../dt_instance_reference/P001_设备树驱动实例宏.md) | Instance-based devicetree APIs |  |
| <a id="row_2_31_"></a>3.32 | [映射辅助宏（Map Helpers）](../dt_connection_reference/P004_设备树描述符映射宏.md) | Map helpers |  |
| <a id="row_2_32_"></a>3.33 | [非易失性存储器设备树辅助宏（NVMEM Devicetree Helpers）](../storage/P018_NVMEM设备树辅助宏.md) | NVMEM Devicetree Helpers | 非易失性存储器（Non-Volatile Memory，NVMEM）的设备树支持。 |
| <a id="row_2_33_"></a>3.34 | [NXP i.MX952电源域（Power Domains）](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html) | NXP i.MX952 Power Domains | i.MX952 系统级芯片（SoC）的电源域分区索引（Power Domain Slice Indices）。 |
| <a id="row_2_34_"></a>3.35 | [节点标识符及辅助宏（Node Identifiers and Helpers）](../dt_identity_reference/P001_设备树节点标识宏.md) | Node identifiers and helpers |  |
| <a id="row_2_35_"></a><a id="arr_2_35_"></a>3.36 | [引脚控制（Pin Control）](../pinctrl_reference/P005_引脚控制设备树宏.md) | Pin control |  |
| <a id="row_2_35_0_"></a><a id="arr_2_35_0_"></a>3.36.1 | [Ambiq 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__ambiq__pinctrl.html) | Ambiq pin control helpers |  |
| <a id="row_2_35_0_0_"></a>3.36.1.1 | [Ambiq Apollo2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo2.html) | Ambiq Apollo2 pin control helpers | 用于配置 Ambiq Apollo2 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_0_1_"></a>3.36.1.2 | [Ambiq Apollo3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo3.html) | Ambiq Apollo3 pin control helpers | 用于配置 Ambiq Apollo3 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_0_2_"></a>3.36.1.3 | [Ambiq Apollo4 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html) | Ambiq Apollo4 pin control helpers | 用于配置 Ambiq Apollo4 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_0_3_"></a>3.36.1.4 | [Ambiq Apollo5 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html) | Ambiq Apollo5 pin control helpers | 用于配置 Ambiq Apollo5 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_"></a><a id="arr_2_35_1_"></a>3.36.2 | [Espressif 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__espressif__pinctrl.html) | Espressif pin control helpers |  |
| <a id="row_2_35_1_0_"></a>3.36.2.1 | [Espressif ESP32 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32.html) | Espressif ESP32 pin control helpers | 用于配置 Espressif ESP32 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_1_"></a>3.36.2.2 | [Espressif ESP32C2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c2.html) | Espressif ESP32C2 pin control helpers | 用于配置 Espressif ESP32C2 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_2_"></a>3.36.2.3 | [Espressif ESP32C3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c3.html) | Espressif ESP32C3 pin control helpers | 用于配置 Espressif ESP32C3 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_3_"></a>3.36.2.4 | [Espressif ESP32C5 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c5.html) | Espressif ESP32C5 pin control helpers | 用于配置 Espressif ESP32C5 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_4_"></a>3.36.2.5 | [Espressif ESP32C6 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html) | Espressif ESP32C6 pin control helpers | 用于配置 Espressif ESP32C6 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_5_"></a>3.36.2.6 | [Espressif ESP32C61 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c61.html) | Espressif ESP32C61 pin control helpers | 用于配置 Espressif ESP32C61 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_6_"></a>3.36.2.7 | [Espressif ESP32H2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32h2.html) | Espressif ESP32H2 pin control helpers | 用于配置 Espressif ESP32H2 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_7_"></a>3.36.2.8 | [Espressif ESP32P4 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32p4.html) | Espressif ESP32P4 pin control helpers | 用于配置 Espressif ESP32P4 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_8_"></a>3.36.2.9 | [Espressif ESP32S2 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s2.html) | Espressif ESP32S2 pin control helpers | 用于配置 Espressif ESP32S2 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_1_9_"></a>3.36.2.10 | [Espressif ESP32S3 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s3.html) | Espressif ESP32S3 pin control helpers | 用于配置 Espressif ESP32S3 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_2_"></a><a id="arr_2_35_2_"></a>3.36.3 | [FocalTech 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl.html) | FocalTech pin control helpers |  |
| <a id="row_2_35_2_0_"></a><a id="arr_2_35_2_0_"></a>3.36.3.1 | [FocalTech FT9001 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html) | FocalTech FT9001 pin control helpers | 用于配置 FocalTech FT9001 引脚复用（Pin multiplexing）的宏。 |
| <a id="row_2_35_2_0_0_"></a>3.36.3.1.1 | [FT9001 IOCTRL 寄存器偏移量（Register offsets）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html) | FT9001 IOCTRL register offsets | 用作 `FOCALTECH_PINMUX` 的 `reg` 参数的寄存器偏移量。 |
| <a id="row_2_35_3_"></a><a id="arr_2_35_3_"></a>3.36.4 | [Nuvoton 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__nuvoton__pinctrl.html) | Nuvoton pin control helpers |  |
| <a id="row_2_35_3_0_"></a>3.36.4.1 | [Nuvoton NuMaker M46x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html) | Nuvoton NuMaker M46x pin control helpers | 用于配置 Nuvoton NuMaker M46x 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_"></a><a id="arr_2_35_4_"></a>3.36.5 | [Renesas 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__pinctrl.html) | Renesas pin control helpers |  |
| <a id="row_2_35_4_0_"></a>3.36.5.1 | [Renesas R-Car 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html) | Renesas R-Car pin control helpers | Renesas R-Car Gen3/Gen4/Gen5 片上系统（SoC）的引脚宏和功能宏。 |
| <a id="row_2_35_4_1_"></a>3.36.5.2 | [Renesas RA 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html) | Renesas RA pin control helpers | 用于配置 Renesas RA 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_2_"></a>3.36.5.3 | [Renesas RA0 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html) | Renesas RA0 pin control helpers | 用于配置 Renesas RA0 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_3_"></a>3.36.5.4 | [Renesas RX 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html) | Renesas RX pin control helpers | 用于配置 Renesas RX 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_4_"></a>3.36.5.5 | [Renesas RZ/A 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html) | Renesas RZ/A pin control helpers | 用于配置 Renesas RZ/A 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_5_"></a>3.36.5.6 | [Renesas RZ/A2M 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html) | Renesas RZ/A2M pin control helpers | 用于配置 Renesas RZ/A2M 片上系统（SoC）引脚控制的宏。 |
| <a id="row_2_35_4_6_"></a>3.36.5.7 | [Renesas RZ/G 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html) | Renesas RZ/G pin control helpers | 用于配置 Renesas RZ/G 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_7_"></a>3.36.5.8 | [Renesas RZ/N 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzn.html) | Renesas RZ/N pin control helpers | 用于配置 Renesas RZ/N 系列 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_8_"></a>3.36.5.9 | [Renesas RZ/T 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html) | Renesas RZ/T pin control helpers | 用于配置 Renesas RZ/T 系列 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_4_9_"></a>3.36.5.10 | [Renesas RZ/V 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html) | Renesas RZ/V pin control helpers | 用于配置 Renesas RZ/V 片上系统（SoC） 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_5_"></a><a id="arr_2_35_5_"></a>3.36.6 | [SiFli 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__sifli__pinctrl.html) | SiFli pin control helpers |  |
| <a id="row_2_35_5_0_"></a>3.36.6.1 | [SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html) | SiFli SF32LB52x pin control helpers | 用于配置 SiFli SF32LB52x 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_"></a><a id="arr_2_35_6_"></a>3.36.7 | [Silicon Labs 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__silabs__pinctrl.html) | Silicon Labs pin control helpers |  |
| <a id="row_2_35_6_0_"></a>3.36.7.1 | [Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html) | Silicon Labs SiWx91x pin control helpers | 用于配置 Silicon Labs SiWx91x 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_1_"></a>3.36.7.2 | [Silicon Labs Six301 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html) | Silicon Labs Six301 pin control helpers | 用于配置 Silicon Labs Six301 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_2_"></a>3.36.7.3 | [Silicon Labs xG21 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg21.html) | Silicon Labs xG21 pin control helpers | 用于配置 Silicon Labs xG21 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_3_"></a>3.36.7.4 | [Silicon Labs xG22 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg22.html) | Silicon Labs xG22 pin control helpers | 用于配置 Silicon Labs xG22 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_4_"></a>3.36.7.5 | [Silicon Labs xG23 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg23.html) | Silicon Labs xG23 pin control helpers | 用于配置 Silicon Labs xG23 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_5_"></a>3.36.7.6 | [Silicon Labs xG24 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg24.html) | Silicon Labs xG24 pin control helpers | 用于配置 Silicon Labs xG24 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_6_"></a>3.36.7.7 | [Silicon Labs xG26 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg26.html) | Silicon Labs xG26 pin control helpers | 用于配置 Silicon Labs xG26 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_7_"></a>3.36.7.8 | [Silicon Labs xG27 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg27.html) | Silicon Labs xG27 pin control helpers | 用于配置 Silicon Labs xG27 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_8_"></a>3.36.7.9 | [Silicon Labs xG28 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html) | Silicon Labs xG28 pin control helpers | 用于配置 Silicon Labs xG28 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_6_9_"></a>3.36.7.10 | [Silicon Labs xG29 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg29.html) | Silicon Labs xG29 pin control helpers | 用于配置 Silicon Labs xG29 引脚控制（Pin control）的宏。 |
| <a id="row_2_35_7_"></a>3.36.8 | [WCH CH32H41x 引脚控制辅助工具（Pin control helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html) | WCH CH32H41x pin control helpers | 用于配置 WCH CH32H41x 引脚控制（Pin control）的宏。 |
| <a id="row_2_36_"></a>3.37 | [属性访问器（Property Accessors）](../dt_property_reference/P001_设备树属性读取宏.md) | Property accessors |  |
| <a id="row_2_37_"></a>3.38 | [厂商与型号名称辅助宏（Vendor and Model Name Helpers）](../dt_identity_reference/P003_设备树厂商与型号宏.md) | Vendor and model name helpers |  |
| <a id="row_2_38_"></a>3.39 | [中断属性（interrupts Property）](../dt_irq_reference/P001_设备树中断属性宏.md) | interrupts property |  |
| <a id="row_2_39_"></a>3.40 | [地址范围映射属性（ranges Property）](../dt_reg_reference/P002_设备树地址范围映射宏.md) | ranges property |  |
| <a id="row_2_40_"></a>3.41 | [寄存器区域属性（reg Property）](../dt_reg_reference/P001_设备树寄存器属性宏.md) | reg property |  |

## 1.4\_错误编号（Error numbers）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_3_"></a>4 | [错误编号（Error numbers）](../error_reference/P003_系统错误号公共接口.md) | Error numbers | 系统错误号（System Error Numbers）。 |

## 1.5\_内部与系统 API（Internal and System API）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_4_"></a><a id="arr_4_"></a>5 | [内部与系统 API（Internal and System API）](https://docs.zephyrproject.org/latest/doxygen/html/group__internal__api.html) | Internal and System API | 内部与系统 API（Internal and System API） |
| <a id="row_4_0_"></a><a id="arr_4_0_"></a>5.1 | [架构接口（Architecture Interface）](../arch_core_reference/P001_架构接口总览.md) | Architecture Interface | 具有公共可见范围的内核内部 API（Internal Kernel APIs with Public Scope）。 |
| <a id="row_4_0_0_"></a>5.1.1 | [架构线程接口（Architecture Thread APIs）](../thread_stack_reference/P004_架构线程接口.md) | Architecture thread APIs |  |
| <a id="row_4_0_1_"></a>5.1.2 | [架构计时接口（Architecture Timing APIs）](../timing_reference/P009_架构计数周期接口.md) | Architecture timing APIs |  |
| <a id="row_4_0_2_"></a>5.1.3 | [架构中断请求接口（Architecture-specific IRQ APIs）](../fatal_irq_reference/P008_架构中断接口.md) | Architecture-specific IRQ APIs |  |
| <a id="row_4_0_3_"></a>5.1.4 | [架构对称多处理接口（Architecture-specific SMP APIs）](../arch_core_reference/P005_架构多处理器接口.md) | Architecture-specific SMP APIs |  |
| <a id="row_4_0_4_"></a>5.1.5 | [架构专有栈遍历 API（Architecture-specific Stack Walk APIs）。](../thread_stack_reference/P005_架构栈遍历接口.md) | Architecture-specific Stack Walk APIs | 架构专有栈遍历 API（Architecture-specific Stack Walk APIs）。 |
| <a id="row_4_0_5_"></a>5.1.6 | [架构线程局部存储接口（Architecture-specific Thread Local Storage APIs）](../arch_core_reference/P007_架构线程局部存储接口.md) | Architecture-specific Thread Local Storage APIs |  |
| <a id="row_4_0_6_"></a>5.1.7 | [架构缓存控制器（Architecture-specific Cache Controllers）](../arch_core_reference/P002_架构缓存接口.md) | Architecture-specific cache controllers. |  |
| <a id="row_4_0_7_"></a>5.1.8 | [架构核心转储接口（Architecture-specific Core Dump APIs）](../observability/P060_核心转储架构接口.md) | Architecture-specific core dump APIs |  |
| <a id="row_4_0_8_"></a>5.1.9 | [架构GDB调试桩接口（Architecture-specific GDB Stub APIs）](../observability/P061_GDB桩架构接口.md) | Architecture-specific gdbstub APIs |  |
| <a id="row_4_0_9_"></a>5.1.10 | [架构内存映射接口（Architecture-specific Memory-mapping APIs）](../arch_core_reference/P003_架构内存映射接口.md) | Architecture-specific memory-mapping APIs |  |
| <a id="row_4_0_10_"></a>5.1.11 | [架构电源管理接口（Architecture-specific Power Management APIs）](../arch_core_reference/P006_架构电源管理接口.md) | Architecture-specific power management APIs |  |
| <a id="row_4_0_11_"></a>5.1.12 | [架构用户空间接口（Architecture-specific Userspace APIs）](../arch_core_reference/P004_架构用户空间接口.md) | Architecture-specific userspace APIs |  |
| <a id="row_4_0_12_"></a>5.1.13 | [指令内存接口（Instruction Memory APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html) | Instruction Memory APIs |  |
| <a id="row_4_0_13_"></a>5.1.14 | [架构杂项接口（Miscellaneous Architecture APIs）](../arch_core_reference/P008_架构杂项接口.md) | Miscellaneous architecture APIs |  |
| <a id="row_4_1_"></a>5.2 | [内核内存管理内部 API](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html) | Kernel Memory Management Internal APIs |  |
| <a id="row_4_2_"></a>5.3 | [用户模式内部 API（User Mode Internal APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html) | User Mode Internal APIs |  |
| <a id="row_4_3_"></a>5.4 | [用户模式与系统调用 API（User Mode and Syscall APIs）。](../syscall_boot_reference/P001_系统调用接口.md) | User mode and Syscall APIs | 用户模式与系统调用 API（User Mode and Syscall APIs）。 |

## 1.6\_内核 API（Kernel APIs）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_5_"></a><a id="arr_5_"></a>6 | [内核 API（Kernel APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html) | Kernel APIs | 内核 API（Kernel APIs） |
| <a id="row_5_0_"></a>6.1 | [异步轮询 API（Async polling APIs）](../eventpoll_reference/P003_轮询公共接口.md) | Async polling APIs | 一种能够同时等待多个条件中任意一个得到满足的API。 |
| <a id="row_5_1_"></a>6.2 | [原子操作服务 API（Atomic Services APIs）](../atomic_reference/P001_原子操作公共接口.md) | Atomic Services APIs |  |
| <a id="row_5_2_"></a>6.3 | [屏障服务 API（Barrier Services APIs）](../synchronization_reference/P001_内存屏障公共接口.md) | Barrier Services APIs |  |
| <a id="row_5_3_"></a>6.4 | [CPU 空闲 API（CPU Idling APIs）](../fatal_irq_reference/P011_CPU空闲接口.md) | CPU Idling APIs |  |
| <a id="row_5_4_"></a>6.5 | [条件变量 API（Condition Variables APIs）](../synchronization_reference/P010_条件变量公共接口.md) | Condition Variables APIs |  |
| <a id="row_5_5_"></a>6.6 | [事件 API（Event APIs）](../eventpoll_reference/P001_事件公共接口.md) | Event APIs |  |
| <a id="row_5_6_"></a>6.7 | [先进先出队列 API（FIFO APIs）](../queue_reference/P003_FIFO公共接口.md) | FIFO APIs |  |
| <a id="row_5_7_"></a>6.8 | [快速用户空间互斥锁 API（FUTEX APIs）](../userspace_sync_reference/P001_Futex公共接口.md) | FUTEX APIs |  |
| <a id="row_5_8_"></a><a id="arr_5_8_"></a>6.9 | [致命错误 API（Fatal error APIs）](../fatal_irq_reference/P001_致命错误处理接口.md) | Fatal error APIs |  |
| <a id="row_5_8_0_"></a>6.9.1 | [致命错误基本类型（Fatal error base types）](../fatal_irq_reference/P004_致命错误原因接口.md) | Fatal error base types |  |
| <a id="row_5_9_"></a>6.10 | [浮点 API（Floating Point APIs）](../fatal_irq_reference/P012_浮点上下文接口.md) | Floating Point APIs |  |
| <a id="row_5_10_"></a>6.11 | [堆 API（Heap APIs）](../heap_reference/P001_内核堆公共接口.md) | Heap APIs | 从堆（Heap）分配内存。 |
| <a id="row_5_11_"></a>6.12 | [中断服务程序 API（Interrupt Service Routine APIs）](../fatal_irq_reference/P007_中断服务接口.md) | Interrupt Service Routine APIs |  |
| <a id="row_5_12_"></a><a id="arr_5_12_"></a>6.13 | [内核内存管理（Kernel Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html) | Kernel Memory Management | 内核内存管理（Kernel Memory Management） |
| <a id="row_5_12_0_"></a><a id="arr_5_12_0_"></a>6.13.1 | [按需分页（Demand Paging）](https://docs.zephyrproject.org/latest/doxygen/html/group__demand__paging.html) | Demand Paging |  |
| <a id="row_5_12_0_0_"></a>6.13.1.1 | [后备存储 API（Backing Store APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html) | Backing Store APIs | 后备存储 API（Backing store APIs） |
| <a id="row_5_12_0_1_"></a>6.13.1.2 | [按需分页 API（Demand Paging APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html) | Demand Paging APIs |  |
| <a id="row_5_12_0_2_"></a>6.13.1.3 | [页面淘汰算法 API（Eviction Algorithm APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html) | Eviction Algorithm APIs | 页面淘汰算法 API（Eviction algorithm APIs） |
| <a id="row_5_13_"></a>6.14 | [后进先出队列 API（LIFO APIs）](../queue_reference/P005_LIFO公共接口.md) | LIFO APIs |  |
| <a id="row_5_14_"></a>6.15 | [邮箱 API（Mailbox APIs）](../mboxpipe_reference/P001_邮箱公共接口.md) | Mailbox APIs |  |
| <a id="row_5_15_"></a>6.16 | [内存块池 API（Memory Slab APIs）](../heap_reference/P003_固定块内存池公共接口.md) | Memory Slab APIs |  |
| <a id="row_5_16_"></a><a id="arr_5_16_"></a>6.17 | [内存域 API（Memory domain APIs）](../memory_domain_reference/P001_内存域接口.md) | Memory domain APIs |  |
| <a id="row_5_16_0_"></a>6.17.1 | [应用内存域 API（Application Memory Domain APIs）。](../memory_domain_reference/P006_应用内存分区接口.md) | Application memory domain APIs | 应用内存域 API（Application Memory Domain APIs）。 |
| <a id="row_5_17_"></a>6.18 | [消息队列 API（Message Queue APIs）](../msgstack_reference/P001_消息队列公共接口.md) | Message Queue APIs |  |
| <a id="row_5_18_"></a>6.19 | [互斥锁 API（Mutex APIs）](../synchronization_reference/P006_互斥量公共接口.md) | Mutex APIs |  |
| <a id="row_5_19_"></a>6.20 | [对象核心 API（Object Core APIs）](../object_core_reference/P001_对象核心公共接口.md) | Object Core APIs |  |
| <a id="row_5_20_"></a>6.21 | [对象核心统计API（Object Core Statistics APIs）](../object_core_reference/P002_对象核心统计接口.md) | Object Core Statistics APIs |  |
| <a id="row_5_21_"></a>6.22 | [管道 API（Pipe APIs）](../mboxpipe_reference/P004_管道公共接口.md) | Pipe APIs |  |
| <a id="row_5_22_"></a>6.23 | [队列 API（Queue APIs）](../queue_reference/P001_通用队列公共接口.md) | Queue APIs |  |
| <a id="row_5_23_"></a>6.24 | [信号量 API（Semaphore APIs）](../synchronization_reference/P008_信号量公共接口.md) | Semaphore APIs |  |
| <a id="row_5_24_"></a>6.25 | [自旋锁 API（Spinlock APIs）](../kernel/P065_自旋锁公共接口.md) | Spinlock APIs | 自旋锁 API（Spinlock APIs） |
| <a id="row_5_25_"></a>6.26 | [栈 API（Stack APIs）](../msgstack_reference/P004_栈公共接口.md) | Stack APIs |  |
| <a id="row_5_26_"></a><a id="arr_5_26_"></a>6.27 | [系统时钟 API（System Clock APIs）](../timer_reference/P086_系统时钟公共接口.md) | System Clock APIs | 系统时钟 API（System Clock APIs） |
| <a id="row_5_26_0_"></a>6.27.1 | [系统定时器低功耗协同接口（System Timer Low-power Companion Interface）](../timer_reference/P089_系统时钟低功耗交接接口.md) | System Timer Low-power Companion Interface | 系统定时器低功耗协同接口（System Timer Low-Power Companion Interface）。 |
| <a id="row_5_27_"></a>6.28 | [线程 API（Thread APIs）](../thread_core_reference/P001_线程公共接口.md) | Thread APIs |  |
| <a id="row_5_28_"></a>6.29 | [线程栈 API（Thread Stack APIs）。](../thread_stack_reference/P001_线程栈接口.md) | Thread Stack APIs | 线程栈 API（Thread Stack APIs）。 |
| <a id="row_5_29_"></a>6.30 | [定时器 API（Timer APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html) | Timer APIs |  |
| <a id="row_5_30_"></a><a id="arr_5_30_"></a>6.31 | [用户模式 API（User Mode APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html) | User Mode APIs |  |
| <a id="row_5_30_0_"></a>6.31.1 | [用户模式互斥锁 API](../userspace_sync_reference/P003_用户模式互斥量公共接口.md) | User mode mutex APIs |  |
| <a id="row_5_30_1_"></a>6.31.2 | [用户模式信号量 API](../userspace_sync_reference/P007_用户模式信号量公共接口.md) | User mode semaphore APIs |  |
| <a id="row_5_31_"></a>6.32 | [版本 API（Version APIs）](../boot_control_reference/P013_内核版本接口.md) | Version APIs | 内核版本 API（Kernel Version APIs）。 |
| <a id="row_5_32_"></a>6.33 | [工作队列 API（Work Queue APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html) | Work Queue APIs |  |

## 1.7\_内存管理 API（Memory Management APIs）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_6_"></a><a id="arr_6_"></a>7 | [内存管理 API（Memory Management APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem__mgmt.html) | Memory Management APIs | 内存管理 API（Memory Management APIs） |
| <a id="row_6_0_"></a>7.1 | [内存属性接口（Memory Attribute Interface）](../memory_services/P003_内存属性接口.md) | Memory Attribute Interface | 内存属性接口（Memory Attribute Interface） |
| <a id="row_6_1_"></a>7.2 | [基于内存属性的内存堆。](../memory_services/P004_内存属性堆接口.md) | Memory heaps based on memory attributes | 基于内存属性的内存堆。 |

## 1.8\_操作系统服务（Operating System Services）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_7_"></a><a id="arr_7_"></a>8 | [操作系统服务（Operating System Services）](https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html) | Operating System Services | 操作系统服务（Operating System Services） |
| <a id="row_7_0_"></a>8.1 | [异步通知 API（Asynchronous Notification APIs）](../memory_services/P011_异步通知接口.md) | Asynchronous Notification APIs |  |
| <a id="row_7_1_"></a><a id="arr_7_1_"></a>8.2 | [身份认证（Authentication）](https://docs.zephyrproject.org/latest/doxygen/html/group__authentication.html) | Authentication | 身份认证（Authentication） |
| <a id="row_7_1_0_"></a>8.2.1 | [FIDO2](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html) | FIDO2 | FIDO2 身份认证器子系统（Authenticator subsystem）。 |
| <a id="row_7_2_"></a><a id="arr_7_2_"></a>8.3 | [二进制描述符（Binary Descriptors）](../data_utilities/P016_二进制描述符接口总览.md) | Binary Descriptors |  |
| <a id="row_7_2_0_"></a>8.3.1 | [二进制描述符定义（Binary Descriptor Definition）](../data_utilities/P017_二进制描述符定义接口.md) | Binary Descriptor Definition | 在固件映像中定义二进制描述符的宏。 |
| <a id="row_7_2_1_"></a>8.3.2 | [二进制描述符读取（Binary Descriptor Reading）](../data_utilities/P018_二进制描述符读取接口.md) | Binary Descriptor Reading | 从固件映像中读取二进制描述符的函数。 |
| <a id="row_7_3_"></a><a id="arr_7_3_"></a>8.4 | [CPU 频率（CPU Frequency，CPUFreq）](../power/P023_CPU调频接口.md) | CPU Frequency (CPUFreq) | 动态 CPU 频率调节（Dynamic CPU Frequency Scaling） |
| <a id="row_7_3_0_"></a>8.4.1 | [CPU 频率策略（CPU Frequency Policy）](../power/P024_CPU调频策略接口.md) | CPU Frequency Policy | CPU 频率调节策略（CPU Frequency Scaling Policy） |
| <a id="row_7_3_1_"></a>8.4.2 | [CPU 频率性能状态（CPU Frequency pstate）](../power/P025_性能状态接口.md) | CPU Frequency pstate | CPU 频率调节性能状态（CPU Frequency Scaling Performance State，pstate） |
| <a id="row_7_4_"></a>8.5 | [CPU 负载监测器（CPU load monitor）](../observability/P049_CPU负载接口.md) | CPU load monitor | 监测 CPU 负载的模块。 |
| <a id="row_7_5_"></a>8.6 | [缓存接口（Cache Interface）](../cache_reference/P001_公共缓存接口.md) | Cache Interface |  |
| <a id="row_7_6_"></a><a id="arr_7_6_"></a>8.7 | [校验和（Checksum）](../checksum_reference/P001_校验和主题目录.md) | Checksum |  |
| <a id="row_7_6_0_"></a>8.7.1 | [循环冗余校验（Cyclic Redundancy Check，CRC）](../data_utilities/P003_CRC计算接口.md) | CRC |  |
| <a id="row_7_7_"></a>8.8 | [清理辅助接口（Cleanup Helper Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html) | Cleanup Helper Interface |  |
| <a id="row_7_8_"></a><a id="arr_7_8_"></a>8.9 | [连接功能（Connectivity）](https://docs.zephyrproject.org/latest/doxygen/html/group__connectivity.html) | Connectivity | 连接功能（Connectivity） |
| <a id="row_7_8_0_"></a><a id="arr_7_8_0_"></a>8.9.1 | [蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html) | Bluetooth APIs | 蓝牙 API（Bluetooth APIs） |
| <a id="row_7_8_0_0_"></a>8.9.1.1 | [高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html) | Advanced Audio Distribution Profile (A2DP) |  |
| <a id="row_7_8_0_1_"></a>8.9.1.2 | [警报通知服务（Alert Notification Service，ANS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html) | Alert Notification Service (ANS) | 警报通知服务（Alert Notification Service，ANS） |
| <a id="row_7_8_0_2_"></a><a id="arr_7_8_0_2_"></a>8.9.1.3 | [分配编号（Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html) | Assigned Numbers. | 蓝牙分配编号（Bluetooth Assigned Numbers）、代码和标识符。 |
| <a id="row_7_8_0_2_0_"></a>8.9.1.3.1 | [蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html) | Bluetooth Mesh Assigned Numbers | 蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers） |
| <a id="row_7_8_0_2_1_"></a>8.9.1.3.2 | [核心规范分配编号（Core Specification Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html) | Core Specification Assigned Numbers | 核心规范分配编号（Core Specification Assigned Numbers） |
| <a id="row_7_8_0_2_2_"></a>8.9.1.3.3 | [通用音频分配编号（Generic Audio Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html) | Generic Audio Assigned Numbers | 通用音频分配编号（Generic Audio Assigned Numbers） |
| <a id="row_7_8_0_3_"></a>8.9.1.4 | [属性协议（Attribute Protocol，ATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html) | Attribute Protocol (ATT) | 属性协议（Attribute Protocol，ATT） |
| <a id="row_7_8_0_4_"></a>8.9.1.5 | [音频输入控制服务（Audio Input Control Service，AICS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html) | Audio Input Control Service (AICS) | 音频输入控制服务（Audio Input Control Service，AICS） |
| <a id="row_7_8_0_5_"></a>8.9.1.6 | [音频流控制服务（Audio Stream Control Service，ASCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html) | Audio Stream Control Service (ASCS) | 音频流控制服务（Audio Stream Control Service，ASCS） |
| <a id="row_7_8_0_6_"></a><a id="arr_7_8_0_6_"></a>8.9.1.7 | [音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html) | Audio Video Remote Control Profile (AVRCP) | 音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP） |
| <a id="row_7_8_0_6_0_"></a>8.9.1.7.1 | [音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html) | Audio Video Remote Control Cover Art Profile | 音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile，AVRCP-CA） |
| <a id="row_7_8_0_7_"></a>8.9.1.8 | [基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html) | Basic Audio Profile (BAP) LC3 Presets | 基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设 |
| <a id="row_7_8_0_8_"></a>8.9.1.9 | [基本成像配置文件（Basic Imaging Profile，BIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html) | Basic Imaging Profile (BIP) | 基本成像配置文件（Basic Imaging Profile，BIP） |
| <a id="row_7_8_0_9_"></a>8.9.1.10 | [电池服务（Battery Service，BAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html) | Battery Service (BAS) | 电池服务（Battery Service，BAS） |
| <a id="row_7_8_0_10_"></a>8.9.1.11 | [BlueNRG HCI 驱动扩展 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html) | BlueNRG HCI driver extended API | BlueNRG HCI 驱动专用 API |
| <a id="row_7_8_0_11_"></a><a id="arr_7_8_0_11_"></a>8.9.1.12 | [蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html) | Bluetooth Audio | 蓝牙音频（Bluetooth Audio） |
| <a id="row_7_8_0_11_0_"></a>8.9.1.12.1 | [分配编号转字符串 API（Assigned numbers to string API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html) | Assigned numbers to string API | 分配编号转字符串 API（Assigned numbers to string API） |
| <a id="row_7_8_0_11_1_"></a>8.9.1.12.2 | [编解码器能力解析 API（Codec capability parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html) | Codec capability parsing APIs | 音频编解码器能力 API（Audio codec capabilities APIs） |
| <a id="row_7_8_0_11_2_"></a>8.9.1.12.3 | [编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html) | Codec config parsing APIs | 音频编解码器配置 API（Audio codec Config APIs） |
| <a id="row_7_8_0_12_"></a><a id="arr_7_8_0_12_"></a>8.9.1.13 | [蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html) | Bluetooth Basic Audio Profile | 蓝牙基本音频配置文件（Bluetooth Basic Audio Profile，BAP） |
| <a id="row_7_8_0_12_0_"></a><a id="arr_7_8_0_12_0_"></a>8.9.1.13.1 | [BAP 广播 API（Broadcast APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html) | BAP Broadcast APIs | BAP 广播 API（Broadcast APIs） |
| <a id="row_7_8_0_12_0_0_"></a>8.9.1.13.1.1 | [BAP 广播接收端 API（Broadcast Sink APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html) | BAP Broadcast Sink APIs | BAP 广播接收端 API（Broadcast Sink APIs） |
| <a id="row_7_8_0_12_0_1_"></a>8.9.1.13.1.2 | [BAP 广播源 API（Broadcast Source APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html) | BAP Broadcast Source APIs | BAP 广播源 API（Broadcast Source APIs） |
| <a id="row_7_8_0_12_1_"></a>8.9.1.13.2 | [BAP 广播接收端 API（Broadcast Sink APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html) | BAP Broadcast Sink APIs | BAP 广播接收端 API（Broadcast Sink APIs） |
| <a id="row_7_8_0_12_2_"></a>8.9.1.13.3 | [BAP 广播源 API（Broadcast Source APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html) | BAP Broadcast Source APIs | BAP 广播源 API（Broadcast Source APIs） |
| <a id="row_7_8_0_12_3_"></a>8.9.1.13.4 | [BAP 单播客户端 API（Unicast Client APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html) | BAP Unicast Client APIs |  |
| <a id="row_7_8_0_12_4_"></a>8.9.1.13.5 | [BAP 单播服务器 API（Unicast Server APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html) | BAP Unicast Server APIs |  |
| <a id="row_7_8_0_13_"></a>8.9.1.14 | [蓝牙内容控制标识符（Bluetooth Content Control Identifier）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html) | Bluetooth Content Control Identifier | 蓝牙内容控制标识符（Bluetooth Content Control Identifier，CCID） |
| <a id="row_7_8_0_14_"></a>8.9.1.15 | [蓝牙控制器（Bluetooth Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html) | Bluetooth Controller | 蓝牙控制器（Bluetooth Controller） |
| <a id="row_7_8_0_15_"></a>8.9.1.16 | [蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html) | Bluetooth Gaming Audio Profile | 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile，GMAP） |
| <a id="row_7_8_0_16_"></a><a id="arr_7_8_0_16_"></a>8.9.1.17 | [蓝牙主机控制器接口（Bluetooth HCI）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html) | Bluetooth HCI | 蓝牙主机控制器接口（Host Controller Interface，HCI）的相关接口。 |
| <a id="row_7_8_0_16_0_"></a>8.9.1.17.1 | [蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html) | Bluetooth H:4 UART driver vendor extension interface | 蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。 |
| <a id="row_7_8_0_16_1_"></a>8.9.1.17.2 | [蓝牙 HCI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html) | Bluetooth HCI Driver Backend API |  |
| <a id="row_7_8_0_16_2_"></a>8.9.1.17.3 | [蓝牙HCI锁步命令（Lockstep Command）的辅助接口。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html) | Bluetooth HCI lockstep command helper | 蓝牙HCI锁步命令（Lockstep Command）的辅助接口。 |
| <a id="row_7_8_0_17_"></a>8.9.1.18 | [蓝牙HCI数据包辅助接口（Packet Helpers）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html) | Bluetooth HCI packet helpers | 蓝牙HCI数据包辅助接口（Packet Helpers）。 |
| <a id="row_7_8_0_18_"></a>8.9.1.19 | [蓝牙人机接口设备（Bluetooth HID）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html) | Bluetooth HID | 蓝牙人机接口设备（Bluetooth HID） |
| <a id="row_7_8_0_19_"></a>8.9.1.20 | [蓝牙 HID 设备（Device）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html) | Bluetooth HID Device | 蓝牙 HID 设备（Device） |
| <a id="row_7_8_0_20_"></a>8.9.1.21 | [蓝牙 HID 主机（Host）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html) | Bluetooth HID Host | 蓝牙 HID 主机（Host） |
| <a id="row_7_8_0_21_"></a>8.9.1.22 | [蓝牙 LC3 编解码器（Bluetooth LC3 codec）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html) | Bluetooth LC3 codec | LC3 |
| <a id="row_7_8_0_22_"></a>8.9.1.23 | [用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html) | Bluetooth Logical Link Control and Adaptation Protocol (L2CAP) for BR/EDR | 用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。 |
| <a id="row_7_8_0_23_"></a><a id="arr_7_8_0_23_"></a>8.9.1.24 | [蓝牙网状网络（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html) | Bluetooth Mesh | 蓝牙网状网络（Bluetooth Mesh） |
| <a id="row_7_8_0_23_0_"></a>8.9.1.24.1 | [访问层（Access layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html) | Access layer | 访问层（Access layer） |
| <a id="row_7_8_0_23_1_"></a>8.9.1.24.2 | [蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html) | Bluetooth Mesh BLOB Transfer Client model API |  |
| <a id="row_7_8_0_23_2_"></a>8.9.1.24.3 | [蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html) | Bluetooth Mesh BLOB Transfer Server model API |  |
| <a id="row_7_8_0_23_3_"></a>8.9.1.24.4 | [蓝牙 Mesh BLOB 闪存数据流（Flash stream）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html) | Bluetooth Mesh BLOB flash stream |  |
| <a id="row_7_8_0_23_4_"></a>8.9.1.24.5 | [蓝牙 Mesh BLOB 模型 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html) | Bluetooth Mesh BLOB model API |  |
| <a id="row_7_8_0_23_5_"></a><a id="arr_7_8_0_23_5_"></a>8.9.1.24.6 | [蓝牙 Mesh 设备固件更新（Device Firmware Update）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html) | Bluetooth Mesh Device Firmware Update |  |
| <a id="row_7_8_0_23_5_0_"></a>8.9.1.24.6.1 | [蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html) | Bluetooth Mesh Device Firmware Update (DFU) metadata | 蓝牙 Mesh DFU 元数据的公共类型与函数。 |
| <a id="row_7_8_0_23_5_1_"></a>8.9.1.24.6.2 | [固件更新服务器模型（Firmware Update Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html) | Firmware Update Server model | 蓝牙 Mesh 固件更新服务器模型的 API。 |
| <a id="row_7_8_0_23_5_2_"></a>8.9.1.24.6.3 | [固件更新客户端模型（原文：Firmware Uppdate Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html) | Firmware Uppdate Client model | 蓝牙 Mesh 固件更新客户端模型的 API。 |
| <a id="row_7_8_0_23_6_"></a>8.9.1.24.7 | [蓝牙 Mesh 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html) | Bluetooth Mesh On-Demand Private GATT Proxy Client |  |
| <a id="row_7_8_0_23_7_"></a>8.9.1.24.8 | [蓝牙 Mesh 按需私有 GATT 代理服务器（On-Demand Private GATT Proxy Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html) | Bluetooth Mesh On-Demand Private GATT Proxy Server |  |
| <a id="row_7_8_0_23_8_"></a>8.9.1.24.9 | [蓝牙 Mesh 私有信标客户端（Private Beacon Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html) | Bluetooth Mesh Private Beacon Client |  |
| <a id="row_7_8_0_23_9_"></a>8.9.1.24.10 | [蓝牙 Mesh 私有信标服务器（Private Beacon Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html) | Bluetooth Mesh Private Beacon Server |  |
| <a id="row_7_8_0_23_10_"></a>8.9.1.24.11 | [蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html) | Bluetooth Mesh SAR Configuration Client Model | 蓝牙网状网络（Bluetooth Mesh） |
| <a id="row_7_8_0_23_11_"></a>8.9.1.24.12 | [蓝牙 Mesh 分段与重组配置服务器模型（SAR Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__srv.html) | Bluetooth Mesh SAR Configuration Server Model | 蓝牙网状网络（Bluetooth Mesh） |
| <a id="row_7_8_0_23_12_"></a>8.9.1.24.13 | [蓝牙 Mesh 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html) | Bluetooth Mesh Solicitation PDU RPL Client |  |
| <a id="row_7_8_0_23_13_"></a>8.9.1.24.14 | [蓝牙 Mesh 请求 PDU 重放保护列表服务器（Solicitation PDU RPL Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.html) | Bluetooth Mesh Solicitation PDU RPL Server |  |
| <a id="row_7_8_0_23_14_"></a>8.9.1.24.15 | [桥接配置客户端模型（Bridge Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html) | Bridge Configuration Client Model | 蓝牙 Mesh 桥接配置客户端模型的 API。 |
| <a id="row_7_8_0_23_15_"></a>8.9.1.24.16 | [桥接配置服务器模型（Bridge Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__srv.html) | Bridge Configuration Server Model | 蓝牙 Mesh 桥接配置服务器模型的 API。 |
| <a id="row_7_8_0_23_16_"></a>8.9.1.24.17 | [桥接配置公共头文件（Bridge Configuration common header）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html) | Bridge Configuration common header |  |
| <a id="row_7_8_0_23_17_"></a>8.9.1.24.18 | [配置客户端模型（Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html) | Configuration Client Model | 配置客户端模型（Configuration Client Model） |
| <a id="row_7_8_0_23_18_"></a>8.9.1.24.19 | [配置服务器模型（Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__srv.html) | Configuration Server Model | 配置服务器模型（Configuration Server Model） |
| <a id="row_7_8_0_23_19_"></a><a id="arr_7_8_0_23_19_"></a>8.9.1.24.20 | [固件分发模型（Firmware Distribution models）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html) | Firmware Distribution models |  |
| <a id="row_7_8_0_23_19_0_"></a>8.9.1.24.20.1 | [固件分发服务器模型（Firmware Distribution Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html) | Firmware Distribution Server model | 固件分发服务器模型的 API。 |
| <a id="row_7_8_0_23_20_"></a>8.9.1.24.21 | [健康客户端模型（Health Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html) | Health Client Model | 健康客户端模型（Health Client Model） |
| <a id="row_7_8_0_23_21_"></a>8.9.1.24.22 | [健康服务器模型（Health Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html) | Health Server Model | 健康服务器模型（Health Server Model） |
| <a id="row_7_8_0_23_22_"></a>8.9.1.24.23 | [健康故障（Health Faults）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html) | Health faults | 规范定义的健康故障值（Health fault values）列表。 |
| <a id="row_7_8_0_23_23_"></a>8.9.1.24.24 | [心跳（Heartbeat）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html) | Heartbeat | 心跳（Heartbeat） |
| <a id="row_7_8_0_23_24_"></a>8.9.1.24.25 | [大型组成数据客户端模型（Large Composition Data Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html) | Large Composition Data Client model |  |
| <a id="row_7_8_0_23_25_"></a>8.9.1.24.26 | [大型组成数据服务器模型（Large Composition Data Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__srv.html) | Large Composition Data Server model |  |
| <a id="row_7_8_0_23_26_"></a>8.9.1.24.27 | [消息（Message）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html) | Message | 消息（Message）。 |
| <a id="row_7_8_0_23_27_"></a>8.9.1.24.28 | [操作码聚合器客户端模型（Opcodes Aggregator Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html) | Opcodes Aggregator Client model |  |
| <a id="row_7_8_0_23_28_"></a>8.9.1.24.29 | [操作码聚合器服务器模型（Opcodes Aggregator Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__srv.html) | Opcodes Aggregator Server model |  |
| <a id="row_7_8_0_23_29_"></a>8.9.1.24.30 | [配网（Provisioning）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html) | Provisioning | 配网（Provisioning） |
| <a id="row_7_8_0_23_30_"></a>8.9.1.24.31 | [代理（Proxy）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html) | Proxy | 代理（Proxy） |
| <a id="row_7_8_0_23_31_"></a>8.9.1.24.32 | [远程配网客户端模型（Remote Provisioning Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html) | Remote Provisioning Client model |  |
| <a id="row_7_8_0_23_32_"></a>8.9.1.24.33 | [远程配网模型（Remote Provisioning models）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html) | Remote Provisioning models |  |
| <a id="row_7_8_0_23_33_"></a>8.9.1.24.34 | [远程配网服务器（Remote provisioning server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html) | Remote provisioning server |  |
| <a id="row_7_8_0_23_34_"></a><a id="arr_7_8_0_23_34_"></a>8.9.1.24.35 | [运行时配置（Runtime Configuration）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html) | Runtime Configuration | 运行时配置（Runtime Configuration） |
| <a id="row_7_8_0_23_34_0_"></a>8.9.1.24.35.1 | [应用配置（Application Configuration）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html) | Application Configuration | 应用配置（Application Configuration） |
| <a id="row_7_8_0_23_34_1_"></a>8.9.1.24.35.2 | [子网配置（Subnet Configuration）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html) | Subnet Configuration | 子网配置（Subnet Configuration） |
| <a id="row_7_8_0_23_35_"></a>8.9.1.24.36 | [分段与重组（SAR）配置公共头文件](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg.html) | SAR Configuration common header |  |
| <a id="row_7_8_0_23_36_"></a>8.9.1.24.37 | [统计（Statistic）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html) | Statistic | 统计（Statistic） |
| <a id="row_7_8_0_24_"></a>8.9.1.25 | [字节序（Byte Order）。](../byteorder_reference/P003_蓝牙字节序辅助接口.md) | Byteorder | 字节序（Byte Order）。 |
| <a id="row_7_8_0_25_"></a><a id="arr_7_8_0_25_"></a>8.9.1.26 | [呼叫控制配置文件（Call Control Profile，CCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp.html) | Call Control Profile (CCP) | 呼叫控制配置文件（Call Control Profile，CCP） |
| <a id="row_7_8_0_25_0_"></a>8.9.1.26.1 | [CCP 呼叫控制客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html) | CCP Call Control Client APIs |  |
| <a id="row_7_8_0_25_1_"></a>8.9.1.26.2 | [CCP 呼叫控制服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html) | CCP Call Control Server APIs |  |
| <a id="row_7_8_0_26_"></a>8.9.1.27 | [信道探测（Channel Sounding，CS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html) | Channel Sounding (CS) | 低功耗蓝牙信道探测（LE Channel Sounding，CS） |
| <a id="row_7_8_0_27_"></a>8.9.1.28 | [通用音频配置文件（Common Audio Profile，CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html) | Common Audio Profile (CAP) | 通用音频配置文件（Common Audio Profile，CAP） |
| <a id="row_7_8_0_28_"></a>8.9.1.29 | [连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html) | Connection management | 连接管理（Connection management） |
| <a id="row_7_8_0_29_"></a>8.9.1.30 | [协调集标识配置文件（Coordinated Set Identification Profile，CSIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html) | Coordinated Set Identification Profile (CSIP) | 协调集标识配置文件（Coordinated Set Identification Profile，CSIP） |
| <a id="row_7_8_0_30_"></a>8.9.1.31 | [密码学（Cryptography）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html) | Cryptography | 密码学（Cryptography） |
| <a id="row_7_8_0_31_"></a>8.9.1.32 | [当前时间服务（Current Time Service，CTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html) | Current Time Service (CTS) | 当前时间服务（Current Time Service，CTS） |
| <a id="row_7_8_0_32_"></a>8.9.1.33 | [数据缓冲区（Data buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html) | Data buffers | 数据缓冲区（Data buffers） |
| <a id="row_7_8_0_33_"></a>8.9.1.34 | [设备地址（Device Address）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html) | Device Address | 蓝牙设备地址（Bluetooth Device Address）的定义和工具。 |
| <a id="row_7_8_0_34_"></a>8.9.1.35 | [经过时间服务（Elapsed Time Service，ETS）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html) | Elapsed Time Service (ETS) |  |
| <a id="row_7_8_0_35_"></a>8.9.1.36 | [加密广播数据（Encrypted Advertising Data，EAD）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html) | Encrypted Advertising Data (EAD) | 加密广播数据（Encrypted Advertising Data，EAD） |
| <a id="row_7_8_0_36_"></a>8.9.1.37 | [游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap__lc3__preset.html) | Gaming Audio Profile (GMAP) LC3 Presets | 游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设 |
| <a id="row_7_8_0_37_"></a><a id="arr_7_8_0_37_"></a>8.9.1.38 | [通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html) | Generic Access Profile (GAP) | 通用访问配置文件（Generic Access Profile，GAP） |
| <a id="row_7_8_0_37_0_"></a>8.9.1.38.1 | [定义与分配编号（Defines and Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html) | Defines and Assigned Numbers | 蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。 |
| <a id="row_7_8_0_38_"></a><a id="arr_7_8_0_38_"></a>8.9.1.39 | [通用属性配置文件（Generic Attribute Profile，GATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html) | Generic Attribute Profile (GATT) | 通用属性配置文件（Generic Attribute Profile，GATT） |
| <a id="row_7_8_0_38_0_"></a>8.9.1.39.1 | [GATT 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html) | GATT Client APIs |  |
| <a id="row_7_8_0_38_1_"></a>8.9.1.39.2 | [GATT 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html) | GATT Server APIs |  |
| <a id="row_7_8_0_39_"></a><a id="arr_7_8_0_39_"></a>8.9.1.40 | [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html) | Generic Object Exchange Profile (GOEP) | 通用对象交换规范（Generic Object Exchange Profile，GOEP） |
| <a id="row_7_8_0_39_0_"></a>8.9.1.40.1 | [GOEP 的 L2CAP 传输](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html) | GOEP transport L2CAP |  |
| <a id="row_7_8_0_39_1_"></a>8.9.1.40.2 | [GOEP 的 RFCOMM 传输](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html) | GOEP transport RFCOMM |  |
| <a id="row_7_8_0_40_"></a>8.9.1.41 | [HCI 原始通道（RAW channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html) | HCI RAW channel | HCI 原始通道（RAW channel） |
| <a id="row_7_8_0_41_"></a>8.9.1.42 | [免提配置文件（Hands Free Profile，HFP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html) | Hands Free Profile (HFP) | 免提配置文件（Hands Free Profile，HFP） |
| <a id="row_7_8_0_42_"></a>8.9.1.43 | [免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html) | Hands Free Profile - Audio Gateway (HFP-AG) | 免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG） |
| <a id="row_7_8_0_43_"></a>8.9.1.44 | [助听接入服务（Hearing Access Service，HAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html) | Hearing Access Service (HAS) | 助听接入服务（Hearing Access Service，HAS） |
| <a id="row_7_8_0_44_"></a>8.9.1.45 | [心率服务（Heart Rate Service，HRS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html) | Heart Rate Service (HRS) | 心率服务（Heart Rate Service，HRS） |
| <a id="row_7_8_0_45_"></a>8.9.1.46 | [即时警报服务（Immediate Alert Service，IAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html) | Immediate Alert Service (IAS) | 即时警报服务（Immediate Alert Service，IAS） |
| <a id="row_7_8_0_46_"></a>8.9.1.47 | [IrDA 对象交换协议（Object Exchange Protocol，OBEX）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html) | IrDA Object Exchange Protocol (OBEX) | IrDA 对象交换协议（Object Exchange Protocol，OBEX） |
| <a id="row_7_8_0_47_"></a>8.9.1.48 | [等时通道（Isochronous channels，ISO）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html) | Isochronous channels (ISO) | 等时通道（Isochronous channels，ISO） |
| <a id="row_7_8_0_48_"></a><a id="arr_7_8_0_48_"></a>8.9.1.49 | [逻辑链路控制与适配协议（L2CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html) | L2CAP | 逻辑链路控制与适配协议（L2CAP） |
| <a id="row_7_8_0_48_0_"></a>8.9.1.49.1 | [L2CAP 通道标识符（L2CAP channel identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__l2cap__cid.html) | L2CAP channel identifiers | 标准 L2CAP 通道标识符。 |
| <a id="row_7_8_0_49_"></a>8.9.1.50 | [媒体控制客户端（Media Control Client，MCC）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html) | Media Control Client (MCC) | 蓝牙媒体控制客户端（Media Control Client，MCC）接口。 |
| <a id="row_7_8_0_50_"></a>8.9.1.51 | [媒体控制服务（Media Control Service，MCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html) | Media Control Service (MCS) | 媒体控制服务（Media Control Service，MCS） |
| <a id="row_7_8_0_51_"></a>8.9.1.52 | [媒体代理（Media Proxy）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html) | Media Proxy | 媒体代理模块。 |
| <a id="row_7_8_0_52_"></a><a id="arr_7_8_0_52_"></a>8.9.1.53 | [消息访问配置文件（Message Access Profile，MAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html) | Message Access Profile (MAP) | 消息访问配置文件（Message Access Profile，MAP） |
| <a id="row_7_8_0_52_0_"></a>8.9.1.53.1 | [消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html) | Messaging Client Equipment(MCE) OBEX Client | 消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端 |
| <a id="row_7_8_0_52_1_"></a>8.9.1.53.2 | [消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html) | Messaging Client Equipment(MCE) OBEX Server | 消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器 |
| <a id="row_7_8_0_52_2_"></a>8.9.1.53.3 | [消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html) | Messaging Server Equipment(MSE) OBEX Client | 消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端 |
| <a id="row_7_8_0_52_3_"></a>8.9.1.53.4 | [消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html) | Messaging Server Equipment(MSE) OBEX Server | 消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器 |
| <a id="row_7_8_0_53_"></a>8.9.1.54 | [麦克风控制配置文件（Microphone Control Profile，MICP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html) | Microphone Control Profile (MICP) | 麦克风控制配置文件（Microphone Control Profile，MICP） |
| <a id="row_7_8_0_54_"></a>8.9.1.55 | [对象传输服务（Object Transfer Service，OTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html) | Object Transfer Service (OTS) | 对象传输服务（Object Transfer Service，OTS） |
| <a id="row_7_8_0_55_"></a>8.9.1.56 | [电话簿访问配置文件（Phone Book Access Profile，PBAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html) | Phone Book Access Profile (PBAP) | 电话簿访问配置文件（Phone Book Access Profile，PBAP） |
| <a id="row_7_8_0_56_"></a>8.9.1.57 | [公共广播配置文件（Public Broadcast Profile，PBP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html) | Public Broadcast Profile (PBP) | 公共广播配置文件（Public Broadcast Profile，PBP） |
| <a id="row_7_8_0_57_"></a>8.9.1.58 | [已发布音频能力服务（Published Audio Capabilities Service，PACS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html) | Published Audio Capabilities Service (PACS) | 已发布音频能力服务（Published Audio Capabilities Service，PACS） |
| <a id="row_7_8_0_58_"></a>8.9.1.59 | [RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html) | RFCOMM | RFCOMM |
| <a id="row_7_8_0_59_"></a>8.9.1.60 | [服务发现协议（Service Discovery Protocol，SDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html) | Service Discovery Protocol (SDP) |  |
| <a id="row_7_8_0_60_"></a>8.9.1.61 | [电话承载服务（Telephone Bearer Service，TBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html) | Telephone Bearer Service (TBS) | 电话承载服务（Telephone Bearer Service，TBS） |
| <a id="row_7_8_0_61_"></a>8.9.1.62 | [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html) | Telephone and Media Audio Profile (TMAP) | 电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP） |
| <a id="row_7_8_0_62_"></a>8.9.1.63 | [通用唯一标识符（UUIDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html) | UUIDs | 通用唯一标识符（UUIDs） |
| <a id="row_7_8_0_63_"></a>8.9.1.64 | [音量控制配置文件（Volume Control Profile，VCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html) | Volume Control Profile (VCP) | 音量控制配置文件（Volume Control Profile，VCP） |
| <a id="row_7_8_0_64_"></a>8.9.1.65 | [音量偏移控制服务（Volume Offset Control Service，VOCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html) | Volume Offset Control Service (VOCS) | 音量偏移控制服务（Volume Offset Control Service，VOCS） |
| <a id="row_7_8_1_"></a>8.9.2 | [CAN ISO-TP 传输协议（CAN ISO-TP Protocol）](../hardware/P380_CAN_ISO-TP接口参考.md) | CAN ISO-TP Protocol | CAN ISO-TP 传输协议（CAN ISO-TP Protocol） |
| <a id="row_7_8_2_"></a><a id="arr_7_8_2_"></a>8.9.3 | [IEEE 802.15.4 与 Thread API](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154.html) | IEEE 802.15.4 and Thread APIs | IEEE 802.15.4 原生与 OpenThread 二层（L2）、配置、管理和驱动 API。 |
| <a id="row_7_8_2_0_"></a>8.9.3.1 | [IEEE 802.15.4 驱动（Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html) | IEEE 802.15.4 Drivers | IEEE 802.15.4 驱动 API |
| <a id="row_7_8_2_1_"></a>8.9.3.2 | [IEEE 802.15.4 二层（L2）](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html) | IEEE 802.15.4 L2 | IEEE 802.15.4 二层（L2）API |
| <a id="row_7_8_2_2_"></a>8.9.3.3 | [IEEE 802.15.4 网络管理（Net Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__mgmt.html) | IEEE 802.15.4 Net Management | IEEE 802.15.4 网络管理库。 |
| <a id="row_7_8_2_3_"></a>8.9.3.4 | [OpenThread 协议栈（Stack）](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html) | OpenThread stack | OpenThread协议栈（Stack）的公共头文件。 |
| <a id="row_7_8_3_"></a>8.9.4 | [LoRaWAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html) | LoRaWAN APIs |  |
| <a id="row_7_8_4_"></a>8.9.5 | [MODBUS](../modbus/P008_Modbus完整API参考.md) | MODBUS | MODBUS 传输协议 API。 |
| <a id="row_7_8_5_"></a><a id="arr_7_8_5_"></a>8.9.6 | [调制解调器 API（Modem APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem.html) | Modem APIs | 调制解调器 API（Modem APIs） |
| <a id="row_7_8_5_0_"></a>8.9.6.1 | [调制解调器串口复用（Modem CMUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html) | Modem CMUX | 调制解调器串口复用（Modem CMUX） |
| <a id="row_7_8_5_1_"></a>8.9.6.2 | [调制解调器命令会话（Modem Chat）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html) | Modem Chat | 调制解调器命令会话（Modem Chat） |
| <a id="row_7_8_5_2_"></a>8.9.6.3 | [调制解调器点对点协议（Modem PPP）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html) | Modem PPP | 调制解调器点对点协议（Modem PPP） |
| <a id="row_7_8_5_3_"></a>8.9.6.4 | [调制解调器管道（Modem Pipe）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html) | Modem Pipe | 调制解调器管道（Modem Pipe） |
| <a id="row_7_8_5_4_"></a>8.9.6.5 | [调制解调器 UBX 协议（Modem Ubx）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html) | Modem Ubx | 调制解调器 UBX 协议（Modem Ubx） |
| <a id="row_7_8_5_5_"></a>8.9.6.6 | [调制解调器管道链接（Modem pipelink）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html) | Modem pipelink | 调制解调器管道链接（Modem pipelink） |
| <a id="row_7_8_6_"></a><a id="arr_7_8_6_"></a>8.9.7 | [网络（Networking）](https://docs.zephyrproject.org/latest/doxygen/html/group__networking.html) | Networking | 网络（Networking） |
| <a id="row_7_8_6_0_"></a>8.9.7.1 | [应用网络上下文（Application network context）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html) | Application network context | 应用网络上下文（Application network context） |
| <a id="row_7_8_6_1_"></a><a id="arr_7_8_6_1_"></a>8.9.7.2 | [BSD 套接字兼容 API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html) | BSD Sockets compatible API | BSD 套接字兼容 API（BSD Sockets compatible API） |
| <a id="row_7_8_6_1_0_"></a>8.9.7.2.1 | [IPv4 套接字选项（Socket options）](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html) | Socket options for IPv4 |  |
| <a id="row_7_8_6_1_1_"></a>8.9.7.2.2 | [IPv6 套接字选项（Socket options）](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html) | Socket options for IPv6 |  |
| <a id="row_7_8_6_1_2_"></a>8.9.7.2.3 | [TLS 套接字选项（Socket options）](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html) | Socket options for TLS |  |
| <a id="row_7_8_6_1_3_"></a>8.9.7.2.4 | [分组套接字的套接字选项（Socket options for packet socket）](https://docs.zephyrproject.org/latest/doxygen/html/group__packet__socket__options.html) | Socket options for packet socket |  |
| <a id="row_7_8_6_2_"></a>8.9.7.3 | [BSD 套接字服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html) | BSD socket service API | BSD 套接字服务 API |
| <a id="row_7_8_6_3_"></a>8.9.7.4 | [受限应用协议库（COAP Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html) | COAP Library | 受限应用协议库（COAP library） |
| <a id="row_7_8_6_4_"></a>8.9.7.5 | [CoAP 管理器事件（CoAP Manager Events）](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html) | CoAP Manager Events | CoAP 管理器事件（CoAP Manager Events） |
| <a id="row_7_8_6_5_"></a>8.9.7.6 | [CoAP的受限RESTful环境对象安全（OSCORE）API。](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html) | CoAP OSCORE API | CoAP的受限RESTful环境对象安全（OSCORE）API。 |
| <a id="row_7_8_6_6_"></a>8.9.7.7 | [CoAP TCP客户端（Client）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html) | CoAP TCP client API | CoAP TCP客户端（Client）的API。 |
| <a id="row_7_8_6_7_"></a>8.9.7.8 | [CoAP客户端（Client）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html) | CoAP client API | CoAP客户端（Client）的API。 |
| <a id="row_7_8_6_8_"></a>8.9.7.9 | [CoAP 服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html) | CoAP service API | CoAP服务（Service）的API。 |
| <a id="row_7_8_6_9_"></a>8.9.7.10 | [连接管理器 API（Connection Manager API）](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html) | Connection Manager API | 连接管理器 API（Connection Manager API） |
| <a id="row_7_8_6_10_"></a><a id="arr_7_8_6_10_"></a>8.9.7.11 | [连接管理器连接性 API（Connectivity API）](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html) | Connection Manager Connectivity API | 连接管理器连接性 API（Connectivity API） |
| <a id="row_7_8_6_10_0_"></a>8.9.7.11.1 | [连接管理器连接性批量 API（Connectivity Bulk API）](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html) | Connection Manager Connectivity Bulk API | 连接管理器批量 API（Bulk API） |
| <a id="row_7_8_6_10_1_"></a>8.9.7.11.2 | [连接管理器连接性实现 API（Connectivity Implementation API）](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html) | Connection Manager Connectivity Implementation API | 连接管理器连接性实现 API（Connectivity Implementation API） |
| <a id="row_7_8_6_11_"></a>8.9.7.12 | [动态主机配置协议第 4 版（DHCPv4）](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html) | DHCPv4 | 动态主机配置协议第 4 版（DHCPv4） |
| <a id="row_7_8_6_12_"></a>8.9.7.13 | [DHCPv4 服务器](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html) | DHCPv4 server | DHCPv4 服务器 |
| <a id="row_7_8_6_13_"></a>8.9.7.14 | [动态主机配置协议第 6 版（DHCPv6）](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html) | DHCPv6 | 动态主机配置协议第 6 版（DHCPv6） |
| <a id="row_7_8_6_14_"></a>8.9.7.15 | [DHCPv6 服务器](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html) | DHCPv6 server | DHCPv6 服务器 |
| <a id="row_7_8_6_15_"></a>8.9.7.16 | [域名解析库（DNS Resolve Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html) | DNS Resolve Library | DNS解析库（Resolving Library）。 |
| <a id="row_7_8_6_16_"></a>8.9.7.17 | [DNS服务发现（Service Discovery）。](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html) | DNS Service Discovery | DNS服务发现（Service Discovery）。 |
| <a id="row_7_8_6_17_"></a>8.9.7.18 | [数据报分组层路径 MTU 发现 API（Datagram PLPMTUD API）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html) | Datagram PLPMTUD API |  |
| <a id="row_7_8_6_18_"></a>8.9.7.19 | [分布式交换架构（Distributed Switch Architecture，DSA）。](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html) | Distributed Switch Architecture (DSA) | 分布式交换架构（Distributed Switch Architecture，DSA）。 |
| <a id="row_7_8_6_19_"></a>8.9.7.20 | [虚拟二层/驱动支持函数（Dummy L2/driver Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__dummy.html) | Dummy L2/driver Support Functions | 虚拟二层/驱动支持函数（Dummy L2/driver support functions） |
| <a id="row_7_8_6_20_"></a>8.9.7.21 | [以太网桥接 API（Ethernet Bridging API）](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html) | Ethernet Bridging API | 以太网桥接 API（Ethernet Bridging API） |
| <a id="row_7_8_6_21_"></a>8.9.7.22 | [以太网库（Ethernet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html) | Ethernet Library | 以太网库（Ethernet library） |
| <a id="row_7_8_6_22_"></a><a id="arr_7_8_6_22_"></a>8.9.7.23 | [以太网物理层接口（Ethernet PHY Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html) | Ethernet PHY Interface | 以太网物理层接口（Ethernet PHY Interface） |
| <a id="row_7_8_6_22_0_"></a>8.9.7.23.1 | [以太网 PHY 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy__backend.html) | Ethernet PHY Driver Backend API |  |
| <a id="row_7_8_6_23_"></a><a id="arr_7_8_6_23_"></a>8.9.7.24 | [以太网支持函数（Ethernet Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html) | Ethernet Support Functions | 以太网支持函数（Ethernet support functions） |
| <a id="row_7_8_6_23_0_"></a>8.9.7.24.1 | [分布式交换架构标签协议（DSA tag protocol）](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html) | DSA tag protocol | 分布式交换架构（DSA）标签协议（Tag Protocol）的定义。 |
| <a id="row_7_8_6_23_1_"></a>8.9.7.24.2 | [以太网介质无关接口支持函数（Ethernet MII Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mii.html) | Ethernet MII Support Functions | 以太网介质无关接口（Media independent interface，MII）函数。 |
| <a id="row_7_8_6_23_2_"></a>8.9.7.24.3 | [IEEE 802.3 管理接口。](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html) | IEEE 802.3 management interface | IEEE 802.3管理接口（Management Interface）的定义。 |
| <a id="row_7_8_6_24_"></a>8.9.7.25 | [以太网桥转发数据库（Ethernet bridge FDB）](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html) | Ethernet bridge FDB | 以太网桥转发数据库（FDB）的定义。 |
| <a id="row_7_8_6_25_"></a>8.9.7.26 | [文件传输协议（FTP）客户端库 API](../networking/P080_FTP完整API参考.md) | FTP client library API |  |
| <a id="row_7_8_6_26_"></a>8.9.7.27 | [HTTP头部压缩（HPACK）。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__hpack.html) | HTTP HPACK | HTTP头部压缩（HPACK）。 |
| <a id="row_7_8_6_27_"></a>8.9.7.28 | [HTTP客户端（Client）API。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html) | HTTP client API | HTTP客户端（Client）API。 |
| <a id="row_7_8_6_28_"></a>8.9.7.29 | [HTTP请求方法（Request Methods）。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html) | HTTP request methods | HTTP请求方法（Request Methods）。 |
| <a id="row_7_8_6_29_"></a>8.9.7.30 | [HTTP响应状态码（Response Status Codes）。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html) | HTTP response status codes | HTTP响应状态码（Response Status Codes）。 |
| <a id="row_7_8_6_30_"></a>8.9.7.31 | [HTTP服务器（Server）API。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html) | HTTP server API |  |
| <a id="row_7_8_6_31_"></a>8.9.7.32 | [HTTP服务（Service）API。](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html) | HTTP service API |  |
| <a id="row_7_8_6_32_"></a>8.9.7.33 | [互联网控制消息协议（ICMP）](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html) | ICMP | 发送和接收 IPv4 或 IPv6 的互联网控制消息协议（Internet Control Message Protocol，ICMP）回显请求消息（Echo Request）。 |
| <a id="row_7_8_6_33_"></a>8.9.7.34 | [互联网组管理协议（IGMP）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html) | IGMP API | 互联网组管理协议（Internet Group Management Protocol，IGMP） |
| <a id="row_7_8_6_34_"></a>8.9.7.35 | [IPv4 网络地址转换（Network Address Translation）](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html) | IPv4 Network Address Translation |  |
| <a id="row_7_8_6_35_"></a>8.9.7.36 | [IPv4/IPv6 原语与辅助工具（Primitives and helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html) | IPv4/IPv6 primitives and helpers | IPv4/IPv6 原语与辅助工具（Primitives and helpers） |
| <a id="row_7_8_6_36_"></a>8.9.7.37 | [延迟监测器（Latency Monitor）](../networking/P099_Latmon完整API参考.md) | Latency Monitor | 延迟监测器（Latency Monitor） |
| <a id="row_7_8_6_37_"></a>8.9.7.38 | [链路层发现协议（Link Layer Discovery Protocol）的定义与辅助工具。](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html) | Link Layer Discovery Protocol definitions and helpers | LLDP 定义与辅助工具。 |
| <a id="row_7_8_6_38_"></a><a id="arr_7_8_6_38_"></a>8.9.7.39 | [轻量级M2M（LwM2M）的高层API。](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html) | LwM2M high-level API |  |
| <a id="row_7_8_6_38_0_"></a>8.9.7.39.1 | [轻量级M2M（LwM2M）的路径辅助宏。](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__path__helpers.html) | LwM2M path helper macros |  |
| <a id="row_7_8_6_39_"></a>8.9.7.40 | [模型上下文协议（MCP）服务器 API](../networking/P183_MCP完整API参考.md) | MCP Server API |  |
| <a id="row_7_8_6_40_"></a>8.9.7.41 | [MQTT 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html) | MQTT Client library |  |
| <a id="row_7_8_6_41_"></a>8.9.7.42 | [MQTT-SN 客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html) | MQTT-SN Client library |  |
| <a id="row_7_8_6_42_"></a>8.9.7.43 | [组播监听发现（Multicast Listener Discovery）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html) | Multicast Listener Discovery API | 组播监听器发现（Multicast Listener Discovery，MLD） |
| <a id="row_7_8_6_43_"></a>8.9.7.44 | [网络配置库（Network Configuration Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html) | Network Configuration Library | 网络配置库（Network configuration library） |
| <a id="row_7_8_6_44_"></a>8.9.7.45 | [网络核心库（Network Core Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html) | Network Core Library | 网络核心库（Network core library） |
| <a id="row_7_8_6_45_"></a>8.9.7.46 | [网络主机名库（Network Hostname Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html) | Network Hostname Library | 网络主机名配置库。 |
| <a id="row_7_8_6_46_"></a>8.9.7.47 | [网络接口抽象层（Network Interface abstraction layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html) | Network Interface abstraction layer | 网络接口抽象层（Network Interface abstraction layer） |
| <a id="row_7_8_6_47_"></a>8.9.7.48 | [网络二层抽象层（Network L2 Abstraction Layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html) | Network L2 Abstraction Layer | 网络第二层抽象层（Network Layer 2 abstraction layer） |
| <a id="row_7_8_6_48_"></a>8.9.7.49 | [网络链路地址库（Network Link Address Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html) | Network Link Address Library | 网络链路地址库（Network link address library） |
| <a id="row_7_8_6_49_"></a><a id="arr_7_8_6_49_"></a>8.9.7.50 | [网络 MIDI 2.0（Network MIDI 2.0）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html) | Network MIDI 2.0 |  |
| <a id="row_7_8_6_49_0_"></a>8.9.7.50.1 | [用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）](https://docs.zephyrproject.org/latest/doxygen/html/group__netmidi10.html) | User Datagram Protocol for Universal MIDI Packets |  |
| <a id="row_7_8_6_50_"></a>8.9.7.51 | [网络管理（Network Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html) | Network Management | 网络管理（Network Management） |
| <a id="row_7_8_6_51_"></a>8.9.7.52 | [网络卸载接口（Network Offloading Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__offload.html) | Network Offloading Interface | 网络卸载接口（Network offloading interface） |
| <a id="row_7_8_6_52_"></a><a id="arr_7_8_6_52_"></a>8.9.7.53 | [网络分组过滤器 API（Network Packet Filter API）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html) | Network Packet Filter API | 网络分组过滤器 API（Network Packet Filter API） |
| <a id="row_7_8_6_52_0_"></a>8.9.7.53.1 | [基本过滤条件（Basic Filter Conditions）](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__basic__cond.html) | Basic Filter Conditions |  |
| <a id="row_7_8_6_52_1_"></a>8.9.7.53.2 | [以太网过滤条件（Ethernet Filter Conditions）](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html) | Ethernet Filter Conditions |  |
| <a id="row_7_8_6_53_"></a>8.9.7.54 | [网络分组库（Network Packet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html) | Network Packet Library | 网络分组管理库。 |
| <a id="row_7_8_6_54_"></a>8.9.7.55 | [网络统计库（Network Statistics Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html) | Network Statistics Library | 网络统计库（Network statistics library） |
| <a id="row_7_8_6_55_"></a>8.9.7.56 | [网络长超时原语与辅助函数（Network Long Timeout Primitives and Helpers）。](../time_headers_reference/P008_网络超时接口.md) | Network long timeout primitives and helpers | 网络长超时原语与辅助函数（Network Long Timeout Primitives and Helpers）。 |
| <a id="row_7_8_6_56_"></a>8.9.7.57 | [网络命名空间兼容模式符号（Network namespace compatibility mode symbols）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__compat.html) | Network namespace compatibility mode symbols | 网络命名空间兼容模式符号（Network namespace compatibility mode symbols） |
| <a id="row_7_8_6_57_"></a>8.9.7.58 | [网络抓包（Network packet capture）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html) | Network packet capture | 网络抓包支持函数。 |
| <a id="row_7_8_6_58_"></a>8.9.7.59 | [网络时间表示（Network time representation）。](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html) | Network time representation. |  |
| <a id="row_7_8_6_59_"></a>8.9.7.60 | [开放充电点协议（OCPP）库](../networking/P191_OCPP完整API参考.md) | OCPP library | OCPP 充电点实现（Charge Point Implementation） |
| <a id="row_7_8_6_60_"></a>8.9.7.61 | [卸载型网络设备（Offloaded Net Devices）](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html) | Offloaded Net Devices | 卸载型网络设备（Offloaded Net Devices） |
| <a id="row_7_8_6_61_"></a>8.9.7.62 | [点对点协议二层/驱动支持函数（PPP L2/driver Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html) | PPP L2/driver Support Functions | 点对点协议（Point-to-point，PPP）二层/驱动支持函数。 |
| <a id="row_7_8_6_62_"></a>8.9.7.63 | [PTP 支持](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html) | PTP support | 精确时间协议（Precision Time Protocol，PTP）支持。 |
| <a id="row_7_8_6_63_"></a>8.9.7.64 | [PTP 时间](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html) | PTP time | 精确时间协议时间规范（Precision Time Protocol time specification）。 |
| <a id="row_7_8_6_64_"></a>8.9.7.65 | [Prometheus API](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html) | Prometheus API |  |
| <a id="row_7_8_6_65_"></a>8.9.7.66 | [混杂模式（Promiscuous mode）](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html) | Promiscuous mode | 混杂模式支持。 |
| <a id="row_7_8_6_66_"></a>8.9.7.67 | [QUIC 库（QUIC Library）](../networking/P147_QUIC完整API参考.md) | QUIC Library | QUIC 库（QUIC library） |
| <a id="row_7_8_6_67_"></a>8.9.7.68 | [实时传输协议（Real-time Transport Protocol，RTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html) | RTP (Real-time Transport Protocol) |  |
| <a id="row_7_8_6_68_"></a><a id="arr_7_8_6_68_"></a>8.9.7.69 | [简单网络时间协议（SNTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html) | SNTP | 简单网络时间协议（Simple Network Time Protocol）API |
| <a id="row_7_8_6_68_0_"></a>8.9.7.69.1 | [SNTP 服务器](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html) | SNTP server | 简单网络时间协议服务器 API |
| <a id="row_7_8_6_69_"></a>8.9.7.70 | [安全外壳（SSH）客户端库](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html) | SSH Client Library |  |
| <a id="row_7_8_6_70_"></a>8.9.7.71 | [安全外壳（SSH）服务器库](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html) | SSH Server Library |  |
| <a id="row_7_8_6_71_"></a>8.9.7.72 | [安全Shell（SSH）客户端/服务器的通用API。](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html) | SSH client/server common API |  |
| <a id="row_7_8_6_72_"></a>8.9.7.73 | [安全Shell（SSH）密钥生成（Keygen）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html) | SSH keygen API |  |
| <a id="row_7_8_6_73_"></a>8.9.7.74 | [套接字 NET_MGMT 库](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html) | Socket NET_MGMT library | 套接字 NET_MGMT 库 |
| <a id="row_7_8_6_74_"></a>8.9.7.75 | [SocketCAN 库](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html) | SocketCAN library | SocketCAN 库 |
| <a id="row_7_8_6_75_"></a>8.9.7.76 | [简单文件传输协议（TFTP）客户端库](../networking/P084_TFTP完整API参考.md) | TFTP Client library |  |
| <a id="row_7_8_6_76_"></a>8.9.7.77 | [传输层安全（TLS）的凭据管理。](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html) | TLS credentials management | 传输层安全（TLS）的凭据管理。 |
| <a id="row_7_8_6_77_"></a>8.9.7.78 | [Trickle 算法库（Trickle Algorithm Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html) | Trickle Algorithm Library | Trickle 算法库（Trickle algorithm library） |
| <a id="row_7_8_6_78_"></a>8.9.7.79 | [虚拟接口库（Virtual Interface Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual__mgmt.html) | Virtual Interface Library | 虚拟接口库（Virtual interface library） |
| <a id="row_7_8_6_79_"></a>8.9.7.80 | [虚拟局域网（Virtual LAN）定义与辅助工具。](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html) | Virtual LAN definitions and helpers | VLAN 定义与辅助工具。 |
| <a id="row_7_8_6_80_"></a>8.9.7.81 | [虚拟网络接口支持函数（Virtual Network Interface Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html) | Virtual Network Interface Support Functions | 虚拟网络接口支持函数（Virtual network interface support functions） |
| <a id="row_7_8_6_81_"></a>8.9.7.82 | [WebSocket的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html) | Websocket API | WebSocket的API。 |
| <a id="row_7_8_6_82_"></a><a id="arr_7_8_6_82_"></a>8.9.7.83 | [Wi-Fi 管理（Wi-Fi Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html) | Wi-Fi Management | Wi-Fi 管理 API |
| <a id="row_7_8_6_82_0_"></a>8.9.7.83.1 | [ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html) | ESP32 Wi-Fi Mesh | ESP32 Wi-Fi Mesh API |
| <a id="row_7_8_6_83_"></a>8.9.7.84 | [Wi-Fi 网络管理器 API（Network Manager API）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html) | Wi-Fi Network Manager API | Wi-Fi网络管理器（Network Manager）的API。 |
| <a id="row_7_8_6_84_"></a>8.9.7.85 | [Wi-Fi 凭据库（Credentials library）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html) | Wi-Fi credentials library | 提供 Wi-Fi 凭据存储和加载方式的库。 |
| <a id="row_7_8_6_85_"></a>8.9.7.86 | [Wireguard 虚拟专用网络（VPN）服务](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html) | Wireguard VPN service | Wireguard 虚拟专用网络（VPN）服务 |
| <a id="row_7_8_6_86_"></a>8.9.7.87 | [Zperf的API。](../networking/P102_zperf完整API参考.md) | Zperf API |  |
| <a id="row_7_8_6_87_"></a>8.9.7.88 | [gPTP 支持](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html) | gPTP support | 通用精确时间协议（Generic Precision Time Protocol，gPTP）支持。 |
| <a id="row_7_8_7_"></a><a id="arr_7_8_7_"></a>8.9.8 | [通用串行总线（USB）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb.html) | USB | 通用串行总线（USB） |
| <a id="row_7_8_7_0_"></a>8.9.8.1 | [USB 音频类 2（Audio Class 2）设备 API](../usb/P089_USB音频2设备API.md) | USB Audio Class 2 device API | USB 音频类 2（Audio Class 2）设备 API |
| <a id="row_7_8_7_1_"></a>8.9.8.2 | [USB 二进制设备对象存储（BOS）支持](../usb/P145_USBBOS支持API.md) | USB BOS support | USB二进制设备对象存储（Binary Device Object Store）的支持。 |
| <a id="row_7_8_7_2_"></a>8.9.8.3 | [USB 设备固件更新（DFU）API](../usb/P062_USB设备固件升级API.md) | USB DFU device update API | USB 设备固件更新（DFU）API |
| <a id="row_7_8_7_3_"></a><a id="arr_7_8_7_3_"></a>8.9.8.4 | [USB 人机接口设备类（HID class）API](../usb/P045_旧版HID类API.md) | USB HID class API | Usb_hid.h API |
| <a id="row_7_8_7_3_0_"></a>8.9.8.4.1 | [HID 类的 USB 专用定义。](../usb/P046_旧版HID设备接口API.md) | HID class USB specific definitions |  |
| <a id="row_7_8_7_4_"></a><a id="arr_7_8_7_4_"></a>8.9.8.5 | [USB HID 公共定义](../usb/P048_HID通用定义.md) | USB HID common definitions | Hid.h API |
| <a id="row_7_8_7_4_0_"></a>8.9.8.5.1 | [鼠标和键盘报告描述符（Report descriptors）。](../usb/P050_HID报告描述符构造宏.md) | Mouse and keyboard report descriptors |  |
| <a id="row_7_8_7_4_1_"></a>8.9.8.5.2 | [USB HID 条目辅助工具（Item helpers）](../usb/P049_HID报告项目定义.md) | USB HID Item helpers |  |
| <a id="row_7_8_7_5_"></a>8.9.8.6 | [USB 主机核心 API（Host Core API）](../usb/P079_USB主机核心API.md) | USB Host Core API | USB 主机核心层 API（HOST Core Layer API） |
| <a id="row_7_8_7_6_"></a>8.9.8.7 | [USB MIDI 2.0 类设备 API](../usb/P094_USBMIDI2设备API.md) | USB MIDI 2.0 Class device API | USB MIDI 2.0 类设备 API |
| <a id="row_7_8_7_7_"></a>8.9.8.8 | [USB 大容量存储类（Mass Storage Class）设备 API](../usb/P058_USB大容量存储API.md) | USB Mass Storage Class device API | USB 大容量存储类（Mass Storage Class）设备 API |
| <a id="row_7_8_7_8_"></a>8.9.8.9 | [USB 视频类（USB Video Class，UVC）设备 API](../usb/P122_USB视频设备API.md) | USB Video Class (UVC) device API | USB 视频类（USB Video Class，UVC）设备 API |
| <a id="row_7_8_7_9_"></a>8.9.8.10 | [USB 缓冲区宏与定义](../usb/P039_USB缓冲区宏与定义.md) | USB buffer macros and definitions | USB 缓冲区宏与定义 |
| <a id="row_7_8_7_10_"></a>8.9.8.11 | [USB 设备核心 API（Device core API）](../usb/P015_USB设备核心API.md) | USB device core API | 新 USB 设备协议栈核心 API（New USB device stack core API） |
| <a id="row_7_8_7_11_"></a>8.9.8.12 | [USB 设备核心 API（Device core API）](../usb/P016_USB设备消息API.md) | USB device core API |  |
| <a id="row_7_8_7_12_"></a>8.9.8.13 | [USBD HID 设备 API](../usb/P042_新版HID设备API.md) | USBD HID device API | USBD HID 设备 API |
| <a id="row_7_9_"></a>8.10 | [控制台 API（Console API）](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html) | Console API | 控制台 API（Console API） |
| <a id="row_7_10_"></a><a id="arr_7_10_"></a>8.11 | [密码处理（Crypto）](../crypto/P008_密码驱动通用接口.md) | Crypto | 密码处理 API（Crypto APIs） |
| <a id="row_7_10_0_"></a>8.11.1 | [密码算法（Cipher）](../crypto/P012_密码算法会话接口.md) | Cipher | 密码功能的密码算法API（Crypto Cipher APIs）。 |
| <a id="row_7_10_1_"></a>8.11.2 | [密码处理驱动后端 API](../crypto/P009_密码驱动后端接口.md) | Crypto Driver Backend API |  |
| <a id="row_7_10_2_"></a>8.11.3 | [哈希（Hash）](../crypto/P023_密码散列会话接口.md) | Hash | 密码功能的哈希API（Crypto Hash APIs）。 |
| <a id="row_7_10_3_"></a>8.11.4 | [随机函数 API（Random Function APIs）](../data_utilities/P007_随机数接口.md) | Random Function APIs | 随机函数 API（Random Function APIs） |
| <a id="row_7_11_"></a><a id="arr_7_11_"></a>8.12 | [调试（Debug）](../debug_trace_reference/P001_调试接口目录.md) | Debug | 调试服务（Debug Services）。 |
| <a id="row_7_11_0_"></a>8.12.1 | [核心转储（Coredump）API。](../observability/P052_核心转储接口.md) | Coredump APIs | 核心转储（Coredump）API。 |
| <a id="row_7_11_1_"></a><a id="arr_7_11_1_"></a>8.12.2 | [CoreSight接口（CoreSight APIs）](../trace_interface_reference/P001_CoreSight接口目录.md) | Coresight APIs |  |
| <a id="row_7_11_1_0_"></a>8.12.2.1 | [CoreSight跟踪解格式器（Trace Deformatter）](../observability/P026_CoreSight解格式接口.md) | Coresight Trace Deformatter |  |
| <a id="row_7_11_2_"></a>8.12.3 | [STP解码器API（STP Decoder API）](../observability/P027_MIPI_STP解码接口.md) | STP Decoder API |  |
| <a id="row_7_11_3_"></a>8.12.4 | [符号表API（Symbol Table API）](../observability/P051_符号表接口.md) | Symbol Table API |  |
| <a id="row_7_11_4_"></a>8.12.5 | [线程分析器（Thread Analyzer）](../observability/P050_线程分析器接口.md) | Thread analyzer | 用于分析线程（Thread）的模块。 |
| <a id="row_7_12_"></a><a id="arr_7_12_"></a>8.13 | [设备管理（Device Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__device__mgmt.html) | Device Management | 设备管理（Device Management） |
| <a id="row_7_12_0_"></a><a id="arr_7_12_0_"></a>8.13.1 | [嵌入式控制器主机命令接口（EC Host Command Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html) | EC Host Command Interface | 嵌入式控制器主机命令接口（EC Host Command Interface） |
| <a id="row_7_12_0_0_"></a>8.13.1.1 | [主机命令驱动后端 API（Host Command Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html) | Host Command Driver Backend API |  |
| <a id="row_7_12_0_1_"></a>8.13.1.2 | [模拟器（Simulator）](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html) | Simulator | EC 主机命令模拟器接口。 |
| <a id="row_7_12_1_"></a>8.13.2 | [管理组件传输协议（MCTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__mctp.html) | MCTP | 管理组件传输协议（Management Component Transport Protocol，MCTP） |
| <a id="row_7_12_2_"></a><a id="arr_7_12_2_"></a>8.13.3 | [MCUmgr](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr.html) | MCUmgr | MCUmgr |
| <a id="row_7_12_2_0_"></a><a id="arr_7_12_2_0_"></a>8.13.3.1 | [回调（Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html) | Callbacks | MCUmgr 回调 API |
| <a id="row_7_12_2_0_0_"></a>8.13.3.1.1 | [枚举管理回调（Enumeration Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html) | Enumeration Management Callbacks | MCUmgr 枚举管理回调 API |
| <a id="row_7_12_2_0_1_"></a>8.13.3.1.2 | [文件系统管理回调（File System Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html) | File System Management Callbacks | MCUmgr 文件系统管理回调 API |
| <a id="row_7_12_2_0_2_"></a>8.13.3.1.3 | [映像管理回调（Image Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html) | Image Management Callbacks | MCUmgr 映像管理回调 API |
| <a id="row_7_12_2_0_3_"></a>8.13.3.1.4 | [操作系统管理回调（OS Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html) | OS Management Callbacks | MCUmgr 操作系统管理回调 API |
| <a id="row_7_12_2_0_4_"></a>8.13.3.1.5 | [设置管理回调（Settings Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html) | Settings Management Callbacks | MCUmgr 设置管理回调 API |
| <a id="row_7_12_2_1_"></a>8.13.3.2 | [处理程序（Handlers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html) | Handlers | MCUmgr 处理程序注册 API。 |
| <a id="row_7_12_2_2_"></a><a id="arr_7_12_2_2_"></a>8.13.3.3 | [管理（Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html) | Management | MCUmgr 管理 API |
| <a id="row_7_12_2_2_0_"></a><a id="arr_7_12_2_2_0_"></a>8.13.3.3.1 | [枚举管理（Enumeration Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html) | Enumeration Management | MCUmgr 枚举管理 API |
| <a id="row_7_12_2_2_0_0_"></a>8.13.3.3.1.1 | [枚举管理回调（Enumeration Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html) | Enumeration Management Callbacks | MCUmgr 枚举管理回调 API |
| <a id="row_7_12_2_2_1_"></a><a id="arr_7_12_2_2_1_"></a>8.13.3.3.2 | [文件系统管理（File System Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html) | File System Management | MCUmgr 文件系统管理 API |
| <a id="row_7_12_2_2_1_0_"></a>8.13.3.3.2.1 | [文件系统管理回调（File System Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html) | File System Management Callbacks | MCUmgr 文件系统管理回调 API |
| <a id="row_7_12_2_2_2_"></a><a id="arr_7_12_2_2_2_"></a>8.13.3.3.3 | [映像管理（Image Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html) | Image Management | MCUmgr 映像管理 API |
| <a id="row_7_12_2_2_2_0_"></a>8.13.3.3.3.1 | [映像管理回调（Image Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html) | Image Management Callbacks | MCUmgr 映像管理回调 API |
| <a id="row_7_12_2_2_2_1_"></a>8.13.3.3.3.2 | [映像管理客户端（Image Management Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html) | Image Management Client | MCUmgr 映像管理客户端 API |
| <a id="row_7_12_2_2_3_"></a><a id="arr_7_12_2_2_3_"></a>8.13.3.3.4 | [操作系统管理（OS Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html) | OS Management | MCUmgr 操作系统管理 API |
| <a id="row_7_12_2_2_3_0_"></a>8.13.3.3.4.1 | [操作系统管理回调（OS Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html) | OS Management Callbacks | MCUmgr 操作系统管理回调 API |
| <a id="row_7_12_2_2_3_1_"></a>8.13.3.3.4.2 | [操作系统管理客户端（OS Management Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html) | OS Management Client | MCUmgr 操作系统管理客户端 API |
| <a id="row_7_12_2_2_4_"></a><a id="arr_7_12_2_2_4_"></a>8.13.3.3.5 | [设置管理（Settings Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html) | Settings Management | MCUmgr 设置管理 API |
| <a id="row_7_12_2_2_4_0_"></a>8.13.3.3.5.1 | [设置管理回调（Settings Management Callbacks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html) | Settings Management Callbacks | MCUmgr 设置管理回调 API |
| <a id="row_7_12_2_2_5_"></a>8.13.3.3.6 | [命令行管理（Shell Management）](../shell_management_reference/P004_mcumgr_Shell管理接口.md) | Shell Management | MCUmgr Shell管理API（Shell Management API）。 |
| <a id="row_7_12_2_2_6_"></a>8.13.3.3.7 | [统计信息管理（Statistics Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html) | Statistics Management | MCUmgr 统计信息管理 API |
| <a id="row_7_12_2_2_7_"></a>8.13.3.3.8 | [传输管理（Transport management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html) | Transport management | MCUmgr 传输管理 API |
| <a id="row_7_12_2_2_8_"></a>8.13.3.3.9 | [Zephyr 基础管理（Zephyr Basic Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html) | Zephyr Basic Management | MCUmgr Zephyr 基础管理 API |
| <a id="row_7_12_2_3_"></a>8.13.3.4 | [简单管理协议客户端（SMP client）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html) | SMP client | MCUmgr SMP 客户端 API |
| <a id="row_7_12_2_4_"></a><a id="arr_7_12_2_4_"></a>8.13.3.5 | [传输层（Transport layers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport.html) | Transport layers | MCUmgr 使用的传输层：SMP、UART 等。 |
| <a id="row_7_12_2_4_0_"></a>8.13.3.5.1 | [蓝牙传输（Bluetooth transport）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html) | Bluetooth transport | 允许通过蓝牙使用 MCUmgr SMP 协议。 |
| <a id="row_7_12_2_4_1_"></a>8.13.3.5.2 | [虚拟传输（Dummy transport）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html) | Dummy transport | 允许通过虚拟传输使用 MCUmgr SMP 协议，通常用于测试。 |
| <a id="row_7_12_2_4_2_"></a>8.13.3.5.3 | [SMP 传输（SMP transport）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html) | SMP transport | MCUmgr SMP 传输 API |
| <a id="row_7_12_2_4_3_"></a>8.13.3.5.4 | [串行传输（Serial transport）](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html) | Serial transport | 允许通过串行连接使用 MCUmgr SMP 协议。 |
| <a id="row_7_12_2_4_4_"></a>8.13.3.5.5 | [命令行传输（Shell transport）](../shell_management_reference/P007_mcumgr_Shell传输接口.md) | Shell transport | 允许通过Zephyr Shell使用MCUmgr简单管理协议（Simple Management Protocol，SMP）。 |
| <a id="row_7_12_2_4_5_"></a>8.13.3.5.6 | [UDP 传输](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html) | UDP transport | 允许通过 UDP 使用 MCUmgr SMP 协议。 |
| <a id="row_7_13_"></a>8.14 | [错误检查（Error checking）](../check_reference/P001_运行时检查接口.md) | Error checking |  |
| <a id="row_7_14_"></a>8.15 | [基于 HTTP 的固件空中升级（FOTA HTTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html) | FOTA HTTP | 基于HTTP的固件空中升级（Firmware Over-the-Air）。 |
| <a id="row_7_15_"></a>8.16 | [文件系统 API（File System APIs）](../storage/P033_文件系统接口.md) | File System APIs | 文件系统 API（File System APIs） |
| <a id="row_7_16_"></a><a id="arr_7_16_"></a>8.17 | [文件系统存储（File System Storage）](../storage/P034_文件系统存储参考.md) | File System Storage |  |
| <a id="row_7_16_0_"></a><a id="arr_7_16_0_"></a>8.17.1 | [闪存循环缓冲区（Flash Circular Buffer，FCB）](../storage/P046_闪存循环缓冲区参考目录.md) | Flash Circular Buffer (FCB) |  |
| <a id="row_7_16_0_0_"></a>8.17.1.1 | [闪存循环缓冲区数据结构](../storage/P048_闪存循环缓冲区数据结构目录.md) | Flash Circular Buffer Data Structures |  |
| <a id="row_7_16_0_1_"></a>8.17.1.2 | [fcb API](../storage/P047_闪存循环缓冲区接口.md) | fcb API | 闪存循环缓冲区 API |
| <a id="row_7_16_0_2_"></a>8.17.1.3 | [fcb 非 API 函数原型（Non-API prototypes）](../storage/P049_闪存循环缓冲区内部读写接口.md) | fcb non-API prototypes | 闪存循环缓冲区内部功能（Flash Circular internal） |
| <a id="row_7_16_1_"></a><a id="arr_7_16_1_"></a>8.17.2 | [非易失性存储（Non-volatile Storage，NVS）](../storage/P053_非易失性存储参考目录.md) | Non-volatile Storage (NVS) | 非易失性存储（Non-volatile Storage，NVS） |
| <a id="row_7_16_1_0_"></a>8.17.2.1 | [非易失性存储 API](../storage/P055_非易失性存储接口.md) | Non-volatile Storage APIs | 非易失性存储 API |
| <a id="row_7_16_1_1_"></a>8.17.2.2 | [非易失性存储数据结构](../storage/P054_非易失性存储数据结构目录.md) | Non-volatile Storage Data Structures | 非易失性存储数据结构 |
| <a id="row_7_16_2_"></a><a id="arr_7_16_2_"></a>8.17.3 | [设置（Settings）。](../storage/P063_设置子系统接口.md) | Settings |  |
| <a id="row_7_16_2_0_"></a>8.17.3.1 | [设置后端接口（Settings backend interface）](../storage/P064_设置存储后端接口.md) | Settings backend interface | 设置（Settings）。 |
| <a id="row_7_16_2_1_"></a>8.17.3.2 | [设置名称处理（Settings name processing）](../storage/P065_设置键名处理接口.md) | Settings name processing | 常量名称处理 API（API for const name processing） |
| <a id="row_7_16_2_2_"></a>8.17.3.3 | [设置子系统运行时（Settings subsystem runtime）](../storage/P017_设置运行时接口.md) | Settings subsystem runtime | 运行时设置 API（API for runtime settings） |
| <a id="row_7_16_3_"></a><a id="arr_7_16_3_"></a>8.17.4 | [Zephyr 存储系统（Zephyr Memory Storage，ZMS）](../storage/P057_Zephyr内存存储参考目录.md) | Zephyr Memory Storage (ZMS) |  |
| <a id="row_7_16_3_0_"></a>8.17.4.1 | [ZMS API](../storage/P059_Zephyr内存存储接口.md) | ZMS API |  |
| <a id="row_7_16_3_1_"></a>8.17.4.2 | [ZMS 数据结构](../storage/P058_Zephyr内存存储数据结构目录.md) | ZMS data structures |  |
| <a id="row_7_17_"></a>8.18 | [闪存映像 API（Flash image API）](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html) | Flash image API | 将固件映像写入闪存的抽象层。 |
| <a id="row_7_18_"></a><a id="arr_7_18_"></a>8.19 | [堆管理（Heap Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__heaps.html) | Heap Management | 堆管理（Heap Management） |
| <a id="row_7_18_0_"></a>8.19.1 | [堆内核地址消毒器 API（Heap KASAN APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html) | Heap KASAN APIs |  |
| <a id="row_7_18_1_"></a>8.19.2 | [堆监听器 API（Heap Listener APIs）](../lowheap_reference/P003_堆事件监听接口.md) | Heap Listener APIs |  |
| <a id="row_7_18_2_"></a>8.19.3 | [底层堆分配器（Low Level Heap Allocator）](../lowheap_reference/P001_底层堆分配接口.md) | Low Level Heap Allocator |  |
| <a id="row_7_18_3_"></a>8.19.4 | [多堆封装（Multi-Heap Wrapper）](../lowheap_reference/P002_多堆包装接口.md) | Multi-Heap Wrapper |  |
| <a id="row_7_18_4_"></a>8.19.5 | [共享多堆接口（Shared multi-heap interface）](../lowheap_reference/P009_共享多堆公共接口.md) | Shared multi-heap interface | 共享多堆（Shared Multi-Heap，SMH）接口。 |
| <a id="row_7_19_"></a><a id="arr_7_19_"></a>8.20 | [进程间通信（IPC）](../intercore_reference/P181_IPC接口总览.md) | IPC | 进程间通信（IPC） |
| <a id="row_7_19_0_"></a>8.20.1 | [IPC 服务 API](../intercore_reference/P111_IPC服务公共接口.md) | IPC service APIs | IPC 服务 API |
| <a id="row_7_19_1_"></a>8.20.2 | [IPC 服务 RPMsg API](../intercore_reference/P124_IPC的RPMsg公共层接口.md) | IPC service RPMsg API | IPC 服务 RPMsg API |
| <a id="row_7_19_2_"></a>8.20.3 | [IPC 服务后端（Backend）](../intercore_reference/P115_IPC服务后端接口.md) | IPC service backend | IPC 服务后端（Backend） |
| <a id="row_7_19_3_"></a>8.20.4 | [IPC 服务静态 VRING API](../intercore_reference/P129_IPC静态虚拟环接口.md) | IPC service static VRINGs API | IPC 服务静态 VRING API |
| <a id="row_7_19_4_"></a>8.20.5 | [Icmsg IPC 库 API](../intercore_reference/P135_ICMsg基础接口.md) | Icmsg IPC library API | Icmsg IPC 库 API |
| <a id="row_7_19_5_"></a>8.20.6 | [Icmsg 多端点 IPC 库 API](../intercore_reference/P140_ICMsg多端点接口.md) | Icmsg multi-endpoint IPC library API | icmsg IPC 库的多端点扩展。 |
| <a id="row_7_19_6_"></a>8.20.7 | [打包缓冲区 API（Packed Buffer API）](../intercore_reference/P144_核间数据包缓冲区接口.md) | Packed Buffer API | 打包缓冲区 API（Packed buffer API） |
| <a id="row_7_19_7_"></a>8.20.8 | [RPMsg 服务 API](../intercore_reference/P121_RPMsg服务公共接口.md) | RPMsg service APIs | RPMsg 服务 API |
| <a id="row_7_20_"></a>8.21 | [插桩（Instrumentation）](../observability/P025_插桩接口参考.md) | Instrumentation |  |
| <a id="row_7_21_"></a>8.22 | [可遍历段接口（Iterable Sections APIs）。](../iterable_reference/P001_可遍历段公共接口.md) | Iterable Sections APIs | 可遍历段接口（Iterable Sections APIs）。 |
| <a id="row_7_22_"></a><a id="arr_7_22_"></a>8.23 | [可链接、可加载扩展（Linkable loadable extensions）](../llext/P011_扩展管理API.md) | Linkable loadable extensions |  |
| <a id="row_7_22_0_"></a>8.23.1 | [可执行与可链接格式（ELF）的常量和数据类型](../llext/P012_ELF常量与类型.md) | ELF constants and data types |  |
| <a id="row_7_22_1_"></a>8.23.2 | [ELF 检查 API（ELF inspection APIs）](../llext/P013_ELF检查API.md) | ELF inspection APIs |  |
| <a id="row_7_22_2_"></a>8.23.3 | [ELF 加载器上下文（ELF loader context）](../llext/P014_ELF加载器API.md) | ELF loader context |  |
| <a id="row_7_22_3_"></a>8.23.4 | [导出符号定义（Exported symbol definitions）](../llext/P015_导出符号API.md) | Exported symbol definitions |  |
| <a id="row_7_23_"></a><a id="arr_7_23_"></a>8.24 | [日志（Logging）。](../log_core_reference/P001_日志主题总览.md) | Logging | 日志（Logging）。 |
| <a id="row_7_23_0_"></a><a id="arr_7_23_0_"></a>8.24.1 | [日志记录器系统（Logger System）](https://docs.zephyrproject.org/latest/doxygen/html/group__logger.html) | Logger system | 日志记录器（Logger）。 |
| <a id="row_7_23_0_0_"></a>8.24.1.1 | [日志链路（Log links）](../log_link_reference/P001_日志链路接口.md) | Log links | 从远端日志域接入消息的日志链路（Log Link）接口。 |
| <a id="row_7_23_0_1_"></a>8.24.1.2 | [日志消息（Log messages）](../log_message_reference/P001_日志消息接口.md) | Log messages | 日志消息。 |
| <a id="row_7_23_0_2_"></a><a id="arr_7_23_0_2_"></a>8.24.1.3 | [日志输出（Log output）](../log_output_reference/P001_日志输出接口.md) | Log output | 将日志消息格式化为人类可读或结构化输出。 |
| <a id="row_7_23_0_2_0_"></a>8.24.1.3.1 | [日志输出格式化标志（Log Output Formatting Flags）](../log_output_format_reference/P001_日志输出格式化标志.md) | Log output formatting flags. |  |
| <a id="row_7_23_0_3_"></a><a id="arr_7_23_0_3_"></a>8.24.1.4 | [日志记录器后端（Logger backends）](../log_backend_reference/P001_日志后端接口.md) | Logger backends | 由日志后端（Logging Backend）实现、供日志核心（Log Core）使用的接口。 |
| <a id="row_7_23_0_3_0_"></a>8.24.1.4.1 | [蓝牙日志后端（Bluetooth log backend）](../log_transport_reference/P001_蓝牙低功耗日志后端接口.md) | Bluetooth log backend | 通过蓝牙低功耗（Bluetooth LE）服务传输消息的日志后端。 |
| <a id="row_7_23_0_3_1_"></a>8.24.1.4.2 | [Intel ADSP HDA 日志后端](../log_backend_helpers_reference/P001_Intel_ADSP_HDA日志后端接口.md) | Intel ADSP HDA log backend | 通过Intel ADSP HDA DMA通道传输日志流的后端。 |
| <a id="row_7_23_0_3_2_"></a>8.24.1.4.3 | [Intel ADSP mtrace 日志后端](../log_backend_helpers_reference/P004_Intel_ADSP_mtrace日志后端接口.md) | Intel ADSP mtrace log backend | 向Intel ADSP mtrace SRAM缓冲区写入日志的后端。 |
| <a id="row_7_23_0_3_3_"></a>8.24.1.4.4 | [日志多域后端辅助工具（Multidomain Backend Helpers）。](../log_backend_helpers_reference/P010_多域日志后端辅助接口.md) | Logger multidomain backend helpers | 日志多域后端辅助工具（Multidomain Backend Helpers）。 |
| <a id="row_7_23_0_3_4_"></a>8.24.1.4.5 | [MQTT 日志后端](../log_transport_reference/P004_MQTT日志后端接口.md) | MQTT log backend | 向MQTT代理（MQTT Broker）发布消息的日志后端。 |
| <a id="row_7_23_0_3_5_"></a>8.24.1.4.6 | [网络日志后端（Network log backend）](../log_transport_reference/P007_网络日志后端接口.md) | Network log backend | 通过网络向syslog服务器发送消息的日志后端。 |
| <a id="row_7_23_0_3_6_"></a>8.24.1.4.7 | [标准后端辅助工具（Standard backend helpers）](../log_backend_helpers_reference/P007_标准日志后端辅助接口.md) | Standard backend helpers | 通过日志输出（Log Output）组件格式化消息的后端辅助工具。 |
| <a id="row_7_23_0_3_7_"></a>8.24.1.4.8 | [Websocket 日志后端](../log_transport_reference/P010_WebSocket日志后端接口.md) | Websocket log backend | 通过WebSocket连接发送消息的日志后端。 |
| <a id="row_7_23_0_4_"></a>8.24.1.5 | [日志记录器控制 API（Logger Control API）。](../log_core_reference/P005_日志控制接口.md) | Logger control API | 日志记录器控制 API（Logger Control API）。 |
| <a id="row_7_23_0_5_"></a><a id="arr_7_23_0_5_"></a>8.24.1.6 | [日志记录器前端（Logger frontend）](../log_frontend_reference/P001_日志前端接口.md) | Logger frontend | 由绕过日志核心（Log Core）的日志前端（Logging Frontend）实现的接口。 |
| <a id="row_7_23_0_5_0_"></a>8.24.1.6.1 | [STMESP前端（STMESP Frontend）](../observability/P030_STMESP日志前端接口.md) | STMESP frontend | 通过STM（STMESP）发出消息与跟踪点（Trace Points）的日志前端。 |
| <a id="row_7_23_0_6_"></a>8.24.1.7 | [日志 API（Logging API）](../log_core_reference/P002_日志公共接口.md) | Logging API | 日志记录器 API（Logger API）。 |
| <a id="row_7_23_1_"></a><a id="arr_7_23_1_"></a>8.24.2 | [跟踪与调试域（Trace and Debug Domain）](../observability/P031_STMESP日志接口目录.md) | Trace and debug domain |  |
| <a id="row_7_23_1_0_"></a>8.24.2.1 | [STMESP 解复用器（Demultiplexer）](../observability/P032_STMESP日志解复用接口.md) | STMESP demultiplexer | 主机端解复用器，用于处理承载日志和跟踪点的 STPv2 数据流。 |
| <a id="row_7_24_"></a><a id="arr_7_24_"></a>8.25 | [内存管理（Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html) | Memory Management | 内存管理（Memory Management） |
| <a id="row_7_24_0_"></a>8.25.1 | [内存组（Memory Banks）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html) | Memory Banks Driver APIs | 内存组（Memory Banks）的驱动API。 |
| <a id="row_7_24_1_"></a>8.25.2 | [内存块 API（Memory Blocks APIs）](../memblocks_reference/P001_内存块分配公共接口.md) | Memory Blocks APIs |  |
| <a id="row_7_24_2_"></a>8.25.3 | [内存管理（Memory Management）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html) | Memory Management Driver APIs | 内存管理（Memory Management）的驱动API。 |
| <a id="row_7_24_3_"></a>8.25.4 | [按字粒度访问内存 API（Word Granular Access Memory APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html) | Word Granular Access Memory APIs |  |
| <a id="row_7_25_"></a>8.26 | [基于模块的断言处理（Module based assert handling）](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html) | Module based assert handling |  |
| <a id="row_7_26_"></a><a id="arr_7_26_"></a>8.27 | [多媒体（Multimedia）](https://docs.zephyrproject.org/latest/doxygen/html/group__multimedia.html) | Multimedia | 硬件和软件多媒体流支持。 |
| <a id="row_7_26_0_"></a><a id="arr_7_26_0_"></a>8.27.1 | [视频子系统（Video Subsystem）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api.html) | Video Subsystem | 视频子系统公共 API。 |
| <a id="row_7_26_0_0_"></a>8.27.1.1 | [视频缓冲区（Video Buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html) | Video Buffers | 用于分配和交换视频缓冲区的函数。 |
| <a id="row_7_26_0_1_"></a>8.27.1.2 | [视频能力（Video Capabilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html) | Video Capabilities | 视频能力 API。 |
| <a id="row_7_26_0_2_"></a>8.27.1.3 | [视频控制 ID（Video Control IDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html) | Video Control IDs | 视频控制 ID（Video Control IDs） |
| <a id="row_7_26_0_3_"></a>8.27.1.4 | [视频控制项（Video Controls）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html) | Video Controls | 操作视频控制项的 API。 |
| <a id="row_7_26_0_4_"></a>8.27.1.5 | [视频格式（Video Format）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html) | Video Format | 视频格式 API。 |
| <a id="row_7_26_0_5_"></a>8.27.1.6 | [视频格式（Video Formats）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html) | Video Formats | 视频像素格式定义。 |
| <a id="row_7_26_0_6_"></a>8.27.1.7 | [视频帧间隔（Video Frame Interval）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html) | Video Frame Interval | 视频帧间隔 API。 |
| <a id="row_7_26_0_7_"></a>8.27.1.8 | [视频流（Video Stream）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html) | Video Stream | 视频流状态控制。 |
| <a id="row_7_26_0_8_"></a>8.27.1.9 | [视频类型（Video Types）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html) | Video Types | 视频类型定义。 |
| <a id="row_7_27_"></a><a id="arr_7_27_"></a>8.28 | [多媒体管线（Multimedia Pipeline）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe.html) | Multimedia Pipeline | 通过自包含的处理元素构建媒体流。 |
| <a id="row_7_27_0_"></a><a id="arr_7_27_0_"></a>8.28.1 | [框架（Framework）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__framework.html) | Framework | 对象模型、协商过程和运行时。 |
| <a id="row_7_27_0_0_"></a>8.28.1.1 | [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html) | Bins | 包含其他元素的元素。 |
| <a id="row_7_27_0_1_"></a>8.28.1.2 | [缓冲区（Buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html) | Buffers | 用于承载数据的对象，以及这些对象的提供者。 |
| <a id="row_7_27_0_2_"></a>8.28.1.3 | [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html) | Capability Structure | 描述一种媒体能力的固定大小容器。 |
| <a id="row_7_27_0_3_"></a>8.28.1.4 | [分派（Dispatches）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html) | Dispatches | 元素（Elements）之间交换的查询和事件。 |
| <a id="row_7_27_0_4_"></a>8.28.1.5 | [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html) | Elements | 构成管线的单元。 |
| <a id="row_7_27_0_5_"></a>8.28.1.6 | [消息（Messages）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html) | Messages | 元素向应用程序反馈的内容。 |
| <a id="row_7_27_0_6_"></a>8.28.1.7 | [对象（Objects）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html) | Objects | 为每一种类型提供身份和属性的公共基类。 |
| <a id="row_7_27_0_7_"></a>8.28.1.8 | [连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html) | Pad | 两个元素相连接的位置。 |
| <a id="row_7_27_0_8_"></a>8.28.1.9 | [解析器（Parsers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html) | Parsers | 将无固定结构的字节流切分为帧的元素。 |
| <a id="row_7_27_0_9_"></a>8.28.1.10 | [管线（Pipelines）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html) | Pipelines | 顶层容器，以及实际运行处理图的对象。 |
| <a id="row_7_27_0_10_"></a>8.28.1.11 | [接收端（Sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html) | Sinks | 消耗缓冲区并终结数据流的元素。 |
| <a id="row_7_27_0_11_"></a>8.28.1.12 | [源（Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html) | Sources | 产生缓冲区并驱动协商过程的元素。 |
| <a id="row_7_27_0_12_"></a>8.28.1.13 | [线程（Threads）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html) | Threads | 一种 `k_thread`，其栈来自池，且栈的生命周期长于该线程。 |
| <a id="row_7_27_0_13_"></a>8.28.1.14 | [变换元素（Transforms）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html) | Transforms | 同时具有输入与输出、处于协商过程中间环节的元素。 |
| <a id="row_7_27_0_14_"></a>8.28.1.15 | [值容器（Value Container）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html) | Value Container | 一个带类型的标量或范围，是能力描述中的最小组成部分。 |
| <a id="row_7_27_0_15_"></a>8.28.1.16 | [工作队列（Workqueues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html) | Workqueues | 可选择将元素的工作卸载到共享工作线程上。 |
| <a id="row_7_27_1_"></a>8.28.2 | [播放器（Player）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html) | Player | 位于管线之上的高层可复用控制层。 |
| <a id="row_7_27_2_"></a><a id="arr_7_27_2_"></a>8.28.3 | [插件（Plugins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__plugins.html) | Plugins | 按所服务的领域分组的具体元素。 |
| <a id="row_7_27_2_0_"></a><a id="arr_7_27_2_0_"></a>8.28.3.1 | [基础元素（Base Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__base.html) | Base Elements | 与媒体类型无关的元素，用于塑造处理图的结构，而非处理其中的数据。 |
| <a id="row_7_27_2_0_0_"></a>8.28.3.1.1 | [应用接收端（Application sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html) | Application sinks | 将管线缓冲区交给应用程序的元素。 |
| <a id="row_7_27_2_0_1_"></a>8.28.3.1.2 | [应用源（Application sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html) | Application sources | 将应用数据注入管线的元素。 |
| <a id="row_7_27_2_0_2_"></a>8.28.3.1.3 | [能力过滤器（Caps Filters）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html) | Caps Filters | 对协商得到的能力施加约束的变换元素。 |
| <a id="row_7_27_2_0_3_"></a>8.28.3.1.4 | [队列（Queues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html) | Queues | 管线层面的线程化元素。 |
| <a id="row_7_27_2_0_4_"></a>8.28.3.1.5 | [分流器（Tee）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html) | Tee | 管线分支元素：具有一个接收端口（Sink pad）和 N 个源端口（Source pad）。 |
| <a id="row_7_27_3_"></a>8.28.4 | [拓扑转储（Topology dump）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html) | Topology dump | 呈现容器的拓扑，以及每个端口协商得到的能力。 |
| <a id="row_7_28_"></a>8.29 | [网络缓冲区库（Network Buffer Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html) | Network Buffer Library | 网络缓冲区库（Network buffer library） |
| <a id="row_7_29_"></a>8.30 | [开关服务 API（On-Off Service APIs）](../memory_services/P016_开关服务接口.md) | On-Off Service APIs |  |
| <a id="row_7_30_"></a>8.31 | [PSA 安全存储 API（PSA Secure Storage API）](../storage/P022_PSA安全存储接口.md) | PSA Secure Storage API |  |
| <a id="row_7_31_"></a><a id="arr_7_31_"></a>8.32 | [电源管理（Power Management，PM）](../power/P031_电源管理接口分组.md) | Power Management (PM) | 系统和设备电源管理。 |
| <a id="row_7_31_0_"></a>8.32.1 | [CPU 电源管理（CPU Power Management）](../power/P061_CPU电源管理接口.md) | CPU Power Management |  |
| <a id="row_7_31_1_"></a>8.32.2 | [设备（Device）。](../power/P036_设备电源管理接口.md) | Device | 设备电源管理 API（Device Power Management API） |
| <a id="row_7_31_2_"></a>8.32.3 | [设备运行时（Device Runtime）](../power/P037_设备运行时电源管理接口.md) | Device Runtime | 设备运行时电源管理 API（Device Runtime Power Management API） |
| <a id="row_7_31_3_"></a>8.32.4 | [挂起到 RAM API（S2RAM APIs）](../power/P062_挂起到RAM接口.md) | S2RAM APIs |  |
| <a id="row_7_31_4_"></a>8.32.5 | [状态（States）](../power/P034_电源状态接口.md) | States | 系统电源管理状态（System Power Management States） |
| <a id="row_7_31_5_"></a><a id="arr_7_31_5_"></a>8.32.6 | [系统（System）](../power/P032_系统电源管理接口.md) | System | 系统电源管理 API（System Power Management API） |
| <a id="row_7_31_5_0_"></a>8.32.6.1 | [钩子（Hooks）](../power/P033_系统电源管理钩子.md) | Hooks | 系统电源管理钩子（System Power Management Hooks） |
| <a id="row_7_31_5_1_"></a>8.32.6.2 | [策略（Policy）](../power/P035_系统电源管理策略接口.md) | Policy | 系统电源管理策略 API（System Power Management Policy API） |
| <a id="row_7_32_"></a><a id="arr_7_32_"></a>8.33 | [精确计时（Precision Timing）。](../timing_reference/P010_精确计时接口.md) | Precision Timing | 精确计时（Precision Timing）。 |
| <a id="row_7_32_0_"></a><a id="arr_7_32_0_"></a>8.33.1 | [精确时钟（Precision Clock）。](../precision_reference/P004_精确时钟接口.md) | Precision Clock | 精确时钟（Precision Clock）。 |
| <a id="row_7_32_0_0_"></a>8.33.1.1 | [精确时钟的 PTP 适配器（Precision Clock PTP Adapter）。](../precision_reference/P009_PTP时钟适配器接口.md) | Precision Clock PTP Adapter | 精确时钟的 PTP 适配器（Precision Clock PTP Adapter）。 |
| <a id="row_7_32_1_"></a>8.33.2 | [精确比例积分控制器（Precision PI Controller）。](../precision_reference/P013_比例积分控制器接口.md) | Precision PI Controller | 精确比例积分控制器（Precision PI Controller）。 |
| <a id="row_7_32_2_"></a>8.33.3 | [精确时间（Precision Time）。](../precision_reference/P001_精确时间接口.md) | Precision Time | 精确时间（Precision Time）。 |
| <a id="row_7_33_"></a><a id="arr_7_33_"></a>8.34 | [实时输入输出（Real-Time I/O，RTIO）。](../rtio_core_reference/P001_RTIO公共接口.md) | RTIO | 实时输入输出（Real-Time I/O，RTIO）。 |
| <a id="row_7_33_0_"></a>8.34.1 | [RTIO完成队列事件标志（CQE Flags）。](../rtio_model_reference/P008_RTIO完成事件标志.md) | RTIO CQE Flags | RTIO完成队列事件标志（CQE Flags）。 |
| <a id="row_7_33_1_"></a>8.34.2 | [RTIO I2C输入输出设备（I/O Device，IODEV）标志。](../hardware/P442_RTIO的I2C标志.md) | RTIO I2C IODEV Flags | RTIO I2C输入输出设备（I/O Device，IODEV）标志。 |
| <a id="row_7_33_2_"></a>8.34.3 | [RTIO I3C输入输出设备（I/O Device，IODEV）标志。](../hardware/P434_RTIO的I3C标志.md) | RTIO I3C IODEV Flags | RTIO I3C输入输出设备（I/O Device，IODEV）标志。 |
| <a id="row_7_33_3_"></a>8.34.4 | [实时 I/O 操作码（RTIO Operation Codes）](../rtio_model_reference/P009_RTIO操作码.md) | RTIO Operation Codes | RTIO提交队列事件操作码（SQE Operation Codes）。 |
| <a id="row_7_33_4_"></a>8.34.5 | [RTIO优先级（Priorities）](../rtio_model_reference/P011_RTIO优先级.md) | RTIO Priorities | RTIO预定义优先级（Predefined Priorities）。 |
| <a id="row_7_33_5_"></a>8.34.6 | [RTIO提交队列事件标志（SQE Flags）。](../rtio_model_reference/P010_RTIO提交事件标志.md) | RTIO SQE Flags | RTIO提交队列事件标志（SQE Flags）。 |
| <a id="row_7_34_"></a><a id="arr_7_34_"></a>8.35 | [保持数据 API（Retention API）](../storage/P014_数据保留接口参考.md) | Retention API | 保持数据 API（Retention API） |
| <a id="row_7_34_0_"></a>8.35.1 | [启动模式接口（Boot mode interface）](../storage/P015_启动模式接口参考.md) | Boot mode interface | 启动模式接口（Boot mode interface） |
| <a id="row_7_34_1_"></a>8.35.2 | [引导加载程序信息接口（Bootloader info interface）](../storage/P016_引导加载器信息接口.md) | Bootloader info interface | 引导加载程序信息接口（Bootloader info interface） |
| <a id="row_7_35_"></a>8.36 | [半主机 API（Semihosting APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html) | Semihosting APIs |  |
| <a id="row_7_36_"></a><a id="arr_7_36_"></a>8.37 | [感知（Sensing）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html) | Sensing | 高层传感器框架（High-level sensor framework）。 |
| <a id="row_7_36_0_"></a>8.37.1 | [数据类型（Data Types）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__datatypes.html) | Data Types | 感知子系统使用的传感器数据结构。 |
| <a id="row_7_36_1_"></a>8.37.2 | [传感器类型——感知子系统（Sensor Types，Sensing）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor__types.html) | Sensor Types (Sensing) | 感知子系统使用的传感器类型标识符。 |
| <a id="row_7_36_2_"></a>8.37.3 | [传感器——感知子系统（Sensors，Sensing）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html) | Sensors (Sensing) | 用于操作感知子系统中传感器的接口。 |
| <a id="row_7_37_"></a><a id="arr_7_37_"></a>8.38 | [命令行解释器（Shell）](../shell_core_reference/P001_Shell核心接口.md) | Shell |  |
| <a id="row_7_37_0_"></a><a id="arr_7_37_0_"></a>8.38.1 | [Shell后端（Shell Backends）](../shell_backend_reference/P001_Shell后端目录.md) | Shell backends | 将Shell实例连接到通信通道（Communication Channel）的传输后端（Transport Backend）。 |
| <a id="row_7_37_0_0_"></a>8.38.1.1 | [ADSP内存窗口后端（Memory Window Backend）](../shell_transport_reference/P001_Shell_ADSP内存窗口后端接口.md) | ADSP memory window shell backend | 通过ADSP内存窗口（Memory Window）访问Shell。 |
| <a id="row_7_37_0_1_"></a>8.38.1.2 | [虚拟后端（Dummy Backend）](../shell_backend_reference/P004_Shell虚拟后端接口.md) | Dummy shell backend | 用于测试的内存内Shell后端（In-memory Shell Backend）。 |
| <a id="row_7_37_0_2_"></a>8.38.1.3 | [MQTT后端（MQTT Backend）](../shell_transport_reference/P004_Shell_MQTT后端接口.md) | MQTT shell backend | 通过消息队列遥测传输协议（MQTT）连接访问Shell。 |
| <a id="row_7_37_0_3_"></a>8.38.1.4 | [RPMsg后端（RPMsg Backend）](../intercore_reference/P178_RPMsg命令行后端接口.md) | RPMsg shell backend | 通过RPMsg端点（Endpoint）访问Shell。 |
| <a id="row_7_37_0_4_"></a>8.38.1.5 | [RTT后端（RTT Backend）](../shell_backend_reference/P007_Shell_RTT后端接口.md) | RTT shell backend | 通过SEGGER实时传输（Real Time Transfer，RTT）通道访问Shell。 |
| <a id="row_7_37_0_5_"></a>8.38.1.6 | [SSH后端（SSH Backend）](../shell_ssh_reference/P001_Shell_SSH后端接口.md) | SSH shell backend | 通过安全外壳协议（Secure Shell，SSH）连接访问Shell。 |
| <a id="row_7_37_0_6_"></a>8.38.1.7 | [Telnet 命令行后端（Telnet shell backend）](../shell_transport_reference/P007_Shell_Telnet后端接口.md) | Telnet shell backend | 通过TELNET连接访问Shell。 |
| <a id="row_7_37_0_7_"></a>8.38.1.8 | [UART后端（UART Backend）](../shell_backend_reference/P010_Shell_UART后端接口.md) | UART shell backend | 通过通用异步收发器（UART）串行连接访问Shell。 |
| <a id="row_7_37_0_8_"></a>8.38.1.9 | [Websocket 命令行后端（Websocket shell backend）](../shell_transport_reference/P010_Shell_WebSocket后端接口.md) | Websocket shell backend | 通过WebSocket连接访问Shell。 |
| <a id="row_7_37_1_"></a>8.38.2 | [远程命令行（Shell remote）](../shell_remote_reference/P001_远端Shell接口.md) | Shell remote | 远端Shell API（Shell Remote API）。 |
| <a id="row_7_38_"></a>8.39 | [状态机框架 API（State Machine Framework API）](../smf/P005_状态机API参考.md) | State Machine Framework API | 状态机框架 API（State Machine Framework API） |
| <a id="row_7_39_"></a>8.40 | [统计信息（Statistics）。](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html) | Statistics | 跟踪并报告子系统事件计数器。 |
| <a id="row_7_40_"></a><a id="arr_7_40_"></a>8.41 | [存储 API（Storage APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__storage__apis.html) | Storage APIs | 存储 API（Storage APIs） |
| <a id="row_7_40_0_"></a>8.41.1 | [磁盘访问接口（Disk Access Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html) | Disk Access Interface | 磁盘访问 API（Disk Access APIs） |
| <a id="row_7_40_1_"></a>8.41.2 | [数据流写入闪存接口（Stream to flash interface）](../stream_flash_reference/P004_流式Flash公共接口.md) | Stream to flash interface | 对向Flash进行流式写入的抽象（Abstraction）。 |
| <a id="row_7_40_2_"></a>8.41.3 | [闪存区域接口（flash area Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html) | flash area Interface | 对闪存分区/区域及其驱动的抽象。 |
| <a id="row_7_41_"></a>8.42 | [系统初始化（System Initialization）](../device_reference/P005_系统初始化接口.md) | System Initialization |  |
| <a id="row_7_42_"></a>8.43 | [系统关机（System power off）](../power/P063_系统关机接口.md) | System power off |  |
| <a id="row_7_43_"></a>8.44 | [任务看门狗 API（Task Watchdog APIs）](../power/P009_任务看门狗接口.md) | Task Watchdog APIs | 任务看门狗 API（Task Watchdog APIs） |
| <a id="row_7_44_"></a><a id="arr_7_44_"></a>8.45 | [计时测量接口（Timing Measurement APIs）。](../timing_reference/P001_计时公共接口.md) | Timing Measurement APIs | 计时测量接口（Timing Measurement APIs）。 |
| <a id="row_7_44_0_"></a>8.45.1 | [架构专有的计时测量接口（Architecture-specific Timing Measurement APIs）。](../timing_reference/P002_架构计时接口.md) | Arch specific Timing Measurement APIs | 架构专有的计时测量接口（Architecture-specific Timing Measurement APIs）。 |
| <a id="row_7_44_1_"></a>8.45.2 | [开发板专有的计时测量接口（Board-specific Timing Measurement APIs）。](../timing_reference/P003_开发板计时接口.md) | Board specific Timing Measurement APIs | 开发板专有的计时测量接口（Board-specific Timing Measurement APIs）。 |
| <a id="row_7_44_2_"></a>8.45.3 | [片上系统专有的计时测量接口（SoC-specific Timing Measurement APIs）。](../timing_reference/P004_片上系统计时接口.md) | SoC specific Timing Measurement APIs | 片上系统专有的计时测量接口（SoC-specific Timing Measurement APIs）。 |
| <a id="row_7_45_"></a><a id="arr_7_45_"></a>8.46 | [跟踪（Tracing）](../tracing_core_reference/P001_跟踪子系统总览.md) | Tracing | 跟踪子系统（Tracing Subsystem）的接口。 |
| <a id="row_7_45_0_"></a>8.46.1 | [跟踪格式（Tracing Format）](../tracing_core_reference/P003_跟踪格式接口.md) | Tracing format | 将跟踪消息格式化为字符串或原始数据的辅助接口。 |
| <a id="row_7_45_1_"></a><a id="arr_7_45_1_"></a>8.46.2 | [跟踪钩子（Tracing Hooks）](../tracing_core_reference/P002_跟踪API总览.md) | Tracing hooks | 跟踪后端（Tracing Backends）使用的钩子位置（Hook Points）。 |
| <a id="row_7_45_1_0_"></a>8.46.2.1 | [后端专用扩展（Backend-specific Extensions）](../network_thread_trace_reference/P005_后端扩展跟踪接口.md) | Backend-specific extensions | 仅由特定后端（Backends）提供的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_1_"></a>8.46.2.2 | [条件变量（Condition Variable）](../sync_trace_reference/P003_条件变量跟踪接口.md) | Conditional variable | 条件变量（Condition Variable）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_2_"></a>8.46.2.3 | [可延时工作项（Delayable Work Item）](../driver_trace_reference/P006_可延时工作项跟踪接口.md) | Delayable work item | 可延时工作项（Delayable Work Item）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_3_"></a>8.46.2.4 | [事件（Event）。](../sync_trace_reference/P004_事件对象跟踪接口.md) | Event | 事件对象（Event）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_4_"></a>8.46.2.5 | [先进先出队列（FIFO）](../object_trace_reference/P001_FIFO跟踪接口.md) | FIFO | 先进先出队列（FIFO）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_5_"></a>8.46.2.6 | [通用输入输出（GPIO）](../driver_trace_reference/P002_GPIO跟踪接口.md) | GPIO | 通用输入输出（GPIO）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_6_"></a>8.46.2.7 | [堆（Heap）](../object_trace_reference/P008_堆跟踪接口.md) | Heap | 堆（Heap）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_7_"></a>8.46.2.8 | [后进先出队列（LIFO）](../object_trace_reference/P002_LIFO跟踪接口.md) | LIFO | 后进先出队列（LIFO）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_8_"></a>8.46.2.9 | [邮箱（Mailbox）](../object_trace_reference/P005_邮箱跟踪接口.md) | Mailbox | 邮箱（Mailbox）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_9_"></a>8.46.2.10 | [内存块池（Memory Slab）](../object_trace_reference/P009_内存块池跟踪接口.md) | Memory slab | 内存块池（Memory Slab）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_10_"></a>8.46.2.11 | [消息队列（Message Queue）](../object_trace_reference/P004_消息队列跟踪接口.md) | Message queue | 消息队列（Message Queue）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_11_"></a>8.46.2.12 | [互斥锁（Mutex）](../sync_trace_reference/P002_互斥锁跟踪接口.md) | Mutex | 互斥锁（Mutex）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_12_"></a>8.46.2.13 | [网络（Network）](../network_thread_trace_reference/P002_网络跟踪接口.md) | Network | 网络（Network）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_13_"></a>8.46.2.14 | [网络套接字（Network Socket）](../network_thread_trace_reference/P003_套接字跟踪接口.md) | Network socket | 网络套接字（Network Socket）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_14_"></a>8.46.2.15 | [设备运行时电源管理（Runtime PM）](../driver_trace_reference/P003_设备运行时电源管理跟踪.md) | PM Device Runtime | 设备运行时电源管理（Device Runtime Power Management）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_15_"></a>8.46.2.16 | [管道（Pipe）](../object_trace_reference/P006_管道跟踪接口.md) | Pipe | 管道（Pipe）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_16_"></a>8.46.2.17 | [轮询（Polling）](../sync_trace_reference/P006_轮询跟踪接口.md) | Polling | 轮询（Polling）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_17_"></a>8.46.2.18 | [队列（Queue）](../object_trace_reference/P003_队列跟踪接口.md) | Queue | 队列（Queue）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_18_"></a>8.46.2.19 | [实时输入输出（RTIO）跟踪API（Tracing APIs）。](../driver_trace_reference/P001_RTIO跟踪接口.md) | RTIO Tracing APIs | 实时输入输出（RTIO）跟踪API（Tracing APIs）。 |
| <a id="row_7_45_1_19_"></a>8.46.2.20 | [信号量（Semaphore）](../sync_trace_reference/P001_信号量跟踪接口.md) | Semaphore | 信号量（Semaphore）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_20_"></a>8.46.2.21 | [栈（Stack）](../object_trace_reference/P007_栈跟踪接口.md) | Stack | 栈（Stack）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_21_"></a>8.46.2.22 | [系统调用跟踪（Syscall Tracing）](../sync_trace_reference/P007_系统调用跟踪接口.md) | Syscall Tracing | 系统调用（System Calls）的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_22_"></a>8.46.2.23 | [系统电源管理（System PM）](../driver_trace_reference/P004_系统电源管理跟踪.md) | System PM | 系统电源管理（System Power Management）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_23_"></a>8.46.2.24 | [线程（Thread）](../network_thread_trace_reference/P001_线程跟踪接口.md) | Thread | 线程（Thread）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_24_"></a>8.46.2.25 | [定时器（Timer）](../sync_trace_reference/P005_定时器跟踪接口.md) | Timer | 定时器（Timer）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_25_"></a>8.46.2.26 | [触发式工作项（Triggered Work Item）](../driver_trace_reference/P007_轮询工作项跟踪接口.md) | Triggered work item | 触发式工作项（Triggered Work Item）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_26_"></a>8.46.2.27 | [用户定义事件（User-defined Event）](../network_thread_trace_reference/P004_命名事件跟踪接口.md) | User-defined event | 用户定义的命名事件（Named Events）的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_27_"></a>8.46.2.28 | [工作项（Work Item）](../driver_trace_reference/P005_工作项跟踪接口.md) | Work item | 工作项（Work Item）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_1_28_"></a>8.46.2.29 | [工作队列（Work Queue）。](../driver_trace_reference/P008_工作队列跟踪接口.md) | Work queue | 工作队列（Work Queue）事件的跟踪钩子（Tracing Hooks）。 |
| <a id="row_7_45_2_"></a>8.46.3 | [跟踪辅助宏（Tracing Utility Macros）](../tracing_core_reference/P004_跟踪包装宏接口.md) | Tracing utility macros | 用于发出跟踪事件的编译期辅助接口（Compile-time Helpers）。 |
| <a id="row_7_46_"></a><a id="arr_7_46_"></a>8.47 | [Xen 支持](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html) | Xen support | Xen 虚拟机监控器（Hypervisor）支持。 |
| <a id="row_7_46_0_"></a><a id="arr_7_46_0_"></a>8.47.1 | [Xen Dom0 控制](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0.html) | Xen Dom0 control | 从特权域管理 Xen 域（Domain）和主机资源。 |
| <a id="row_7_46_0_0_"></a>8.47.1.1 | [Xen Dom0 域控制（Domain control）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html) | Xen Dom0 domain control | 从特权域控制域的生命周期、资源和虚拟 CPU（vCPU）。 |
| <a id="row_7_46_0_1_"></a>8.47.1.2 | [Xen Dom0 系统控制（sysctl）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html) | Xen Dom0 sysctl | 发起仅供 Dom0 使用的 Xen sysctl 操作。 |
| <a id="row_7_46_1_"></a>8.47.2 | [Xen硬件虚拟机（HVM）的操作。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html) | Xen HVM operations | 通过 HVM 超级调用（Hypercall）配置 Xen 硬件虚拟机（HVM）客户机参数。 |
| <a id="row_7_46_2_"></a>8.47.3 | [Xen 安全模块 FLASK（Xen XSM FLASK）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html) | Xen XSM FLASK | 加载 Xen 安全策略，管理 FLASK 强制执行模式，将上下文转换为安全标识符（SID），管理对象上下文（ocontexts），以及执行其他 FLASK 相关任务。 |
| <a id="row_7_46_3_"></a>8.47.4 | [Xen 设备模型（Device model）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html) | Xen device model | 管理 Xen I/O 请求服务器及相关的设备模型状态。 |
| <a id="row_7_46_4_"></a>8.47.5 | [Xen 事件通道（Event channels）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html) | Xen event channels | 从 Zephyr 分配、绑定和处理 Xen 事件通道。 |
| <a id="row_7_46_5_"></a>8.47.6 | [Xen 扩展区域（Extended regions）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html) | Xen extended regions | 从 Xen 扩展内存区域分配、释放和映射缓冲区。 |
| <a id="row_7_46_6_"></a>8.47.7 | [Xen 授权表（Grant tables）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html) | Xen grant tables | 与其他域共享内存，并映射其他域的内存授权（Foreign grants）。 |
| <a id="row_7_46_7_"></a><a id="arr_7_46_7_"></a>8.47.8 | [Xen 内部支持（Internal support）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__internal.html) | Xen internal support | 共享 Zephyr Xen 支持代码所用的底层辅助工具。 |
| <a id="row_7_46_7_0_"></a>8.47.8.1 | [Xen 控制台驱动（Console driver）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html) | Xen console driver | 使 Xen UART 控制台实现与其设备数据布局保持同步。 |
| <a id="row_7_46_8_"></a>8.47.9 | [Xen 内存管理（Memory management）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html) | Xen memory management | 管理域的物理映射（Physmaps）和由 Xen 拥有的资源。 |
| <a id="row_7_46_9_"></a>8.47.10 | [Xen版本查询（Version Queries）。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html) | Xen version queries | 查询向当前域公开的 Xen 虚拟机监控器版本。 |
| <a id="row_7_47_"></a><a id="arr_7_47_"></a>8.48 | [Zbus API](../intercore_reference/P213_zbus核心接口.md) | Zbus APIs | Zbus API |
| <a id="row_7_47_0_"></a><a id="arr_7_47_0_"></a>8.48.1 | [Zbus 代理 API（Proxy Agent API）](../intercore_reference/P193_zbus代理接口.md) | Zbus Proxy Agent API |  |
| <a id="row_7_47_0_0_"></a>8.48.1.1 | [Zbus 代理 IPC 后端（Proxy Agent IPC Backend）](../intercore_reference/P201_zbus代理IPC后端接口.md) | Zbus Proxy Agent IPC Backend |  |

## 1.9\_测试（Testing）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_8_"></a><a id="arr_8_"></a>9 | [测试（Testing）](../hardware/P499_测试API目录.md) | Testing | 测试（Testing） |
| <a id="row_8_0_"></a><a id="arr_8_0_"></a>9.1 | [仿真器接口（Emulator interfaces）](../hardware/P476_外设仿真器API.md) | Emulator interfaces | 用于测试驱动及使用这些驱动的上层代码的仿真器。 |
| <a id="row_8_0_0_"></a>9.1.1 | [BBRAM 仿真器后端 API（Emulator backend API）](../hardware/P490_BBRAM仿真后端接口.md) | BBRAM emulator backend API | BBRAM 仿真器后端 API（Emulator backend API） |
| <a id="row_8_0_1_"></a>9.1.2 | [BC1.2 仿真器支持 API（原文：BC1.2 backed emulator APIs）](../hardware/P491_BC1点2仿真后端接口.md) | BC1.2 backed emulator APIs | BC1.2 仿真器后端 API（BC1.2 backend emulator APIs） |
| <a id="row_8_0_2_"></a>9.1.3 | [生物识别仿真器测试辅助功能（Emulator test helpers）](../hardware/P495_生物识别仿真测试接口.md) | Biometrics emulator test helpers | 生物识别仿真器测试控制函数（Emulator test control functions）。 |
| <a id="row_8_0_3_"></a>9.1.4 | [仿真 ADC（Emulated ADC）](../hardware/P464_ADC模拟器接口.md) | Emulated ADC | 仿真 ADC 后端 API（Backend API）。 |
| <a id="row_8_0_4_"></a>9.1.5 | [仿真 GPIO（Emulated GPIO）](../hardware/P273_GPIO模拟接口.md) | Emulated GPIO | 仿真 GPIO 后端 API（Backend API）。 |
| <a id="row_8_0_5_"></a>9.1.6 | [仿真计数器（Emulated counter）](../hardware/P493_计数器仿真后端接口.md) | Emulated counter | 仿真计数器后端 API（Emulated counter backend API）。 |
| <a id="row_8_0_6_"></a>9.1.7 | [模拟 CAN 控制器（Fake CAN controller）](../hardware/P374_伪CAN控制器接口.md) | Fake CAN controller | 模拟 CAN 控制器驱动（Fake CAN controller driver）。 |
| <a id="row_8_0_7_"></a>9.1.8 | [模拟 EEPROM（Fake EEPROM）](../hardware/P051_伪EEPROM接口.md) | Fake EEPROM | 模拟 EEPROM 驱动（Fake EEPROM driver）。 |
| <a id="row_8_0_8_"></a>9.1.9 | [模拟 LED 控制器（Fake LED controller）](../hardware/P207_模拟LED控制器.md) | Fake LED controller | 模拟 LED 控制器驱动程序。 |
| <a id="row_8_0_9_"></a>9.1.10 | [模拟 LoRa（Fake LoRa）](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__fake.html) | Fake LoRa | 模拟 LoRa 驱动程序。 |
| <a id="row_8_0_10_"></a>9.1.11 | [模拟 PWM（Fake PWM）](../hardware/P260_PWM模拟控制器.md) | Fake PWM | 模拟 PWM 驱动程序。 |
| <a id="row_8_0_11_"></a>9.1.12 | [模拟 RTC（Fake RTC）](../hardware/P497_RTC伪设备接口.md) | Fake RTC | 模拟 RTC 驱动程序。 |
| <a id="row_8_0_12_"></a>9.1.13 | [模拟比较器（Fake comparator）](../hardware/P090_伪比较器接口.md) | Fake comparator | 模拟比较器驱动（Fake comparator driver）。 |
| <a id="row_8_0_13_"></a>9.1.14 | [模拟稳压器（Fake regulator）](../hardware/P498_稳压器伪设备接口.md) | Fake regulator | 模拟稳压器驱动程序。 |
| <a id="row_8_0_14_"></a>9.1.15 | [电量计后端仿真器 API（Fuel gauge backend emulator APIs）](../hardware/P492_电量计仿真后端接口.md) | Fuel gauge backend emulator APIs | 电量计后端仿真器 API（Fuel gauge backend emulator APIs） |
| <a id="row_8_0_15_"></a>9.1.16 | [I2C 仿真接口（Emulation Interface）](../hardware/P314_I2C模拟后端.md) | I2C Emulation Interface | I2C 仿真接口（Emulation Interface） |
| <a id="row_8_0_16_"></a>9.1.17 | [MSPI 仿真接口（MSPI Emulation Interface）](../hardware/P487_MSPI总线仿真接口.md) | MSPI Emulation Interface | MSPI 仿真接口（MSPI Emulation Interface） |
| <a id="row_8_0_17_"></a>9.1.18 | [SPI 仿真接口（SPI Emulation Interface）](../hardware/P326_SPI模拟接口.md) | SPI Emulation Interface | SPI 仿真接口（SPI Emulation Interface） |
| <a id="row_8_0_18_"></a>9.1.19 | [传感器仿真器后端 API](../hardware/P494_传感器仿真后端接口.md) | Sensor emulator backend API | 传感器仿真器后端 API |
| <a id="row_8_0_19_"></a>9.1.20 | [UART 仿真接口（UART Emulation Interface）](../hardware/P341_UART模拟接口.md) | UART Emulation Interface | UART 仿真接口（UART Emulation Interface） |
| <a id="row_8_0_20_"></a>9.1.21 | [eSPI 仿真接口（Emulation Interface）](../hardware/P486_eSPI总线仿真接口.md) | eSPI Emulation Interface | eSPI 仿真接口（Emulation Interface） |
| <a id="row_8_1_"></a>9.2 | [FFF 扩展（FFF extensions）](../hardware/P500_FFF测试扩展接口.md) | FFF extensions | 本模块为 FFF 提供扩展，简化模拟函数（Fake）的配置和使用。 |
| <a id="row_8_2_"></a>9.3 | [Zephyr 基准测试框架（Zephyr Benchmarking Framework）。](../hardware/P501_ZTest基准测试接口.md) | Zephyr Benchmarking Framework |  |
| <a id="row_8_3_"></a><a id="arr_8_3_"></a>9.4 | [Zephyr 测试框架（Zephyr Testing Framework，ZTest）](../hardware/P502_ZTest测试框架接口.md) | Zephyr Testing Framework (ZTest) |  |
| <a id="row_8_3_0_"></a>9.4.1 | [Ztest 断言宏（Assertion macros）](../hardware/P503_ZTest断言宏.md) | Ztest assertion macros | 本模块在使用 Ztest 时提供断言（Assertion）。 |
| <a id="row_8_3_1_"></a>9.4.2 | [Ztest 假设宏（Assumption macros）](../hardware/P504_ZTest假设宏.md) | Ztest assumption macros | 本模块在使用 Ztest 时提供假设检查（Assumption）。 |
| <a id="row_8_3_2_"></a>9.4.3 | [Ztest 期望宏（Expectation macros）](../hardware/P505_ZTest预期检查宏.md) | Ztest expectation macros | 本模块在使用 Ztest 时提供期望检查（Expectation）。 |
| <a id="row_8_3_3_"></a>9.4.4 | [Ztest的模拟（Mocking）支持。](../hardware/P506_ZTest模拟支持.md) | Ztest mocking support | 本模块提供用于单元测试的简单模拟函数（Mocking functions）。 |
| <a id="row_8_3_4_"></a>9.4.5 | [Ztest 测试宏（Testing macros）](../hardware/P507_ZTest测试定义宏.md) | Ztest testing macros | 本模块通过提供实用宏和其他测试结构来简化测试过程。 |
| <a id="row_8_3_5_"></a>9.4.6 | [Ztest ztress 宏](../hardware/P508_ZTest压力测试宏.md) | Ztest ztress macros | 本模块在使用 Ztest 时提供压力测试。 |

## 1.10\_第三方（Third-party）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_9_"></a><a id="arr_9_"></a>10 | [第三方（Third-party）](https://docs.zephyrproject.org/latest/doxygen/html/group__third__party.html) | Third-party | 与第三方服务或应用程序交互的 API。 |
| <a id="row_9_0_"></a>10.1 | [BBC micro:bit显示（Display）的API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html) | BBC micro:bit display APIs | BBC micro:bit显示（Display）的API。 |
| <a id="row_9_1_"></a>10.2 | [Grove 显示器（Grove display）](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html) | Grove display | Grove LCD RGB 显示器接口。 |
| <a id="row_9_2_"></a>10.3 | [MCUboot 映像控制 API（Image control API）](../boot_control_reference/P001_MCUboot镜像控制接口.md) | MCUboot image control API | 用于控制镜像启动过程（Image Boot Process）的 MCUboot 公共 API。 |
| <a id="row_9_3_"></a>10.4 | [UpdateHub 固件空中升级（Firmware Over-the-Air）](../firmware_update/P031_UpdateHub接口.md) | UpdateHub Firmware Over-the-Air | 面向 Zephyr 项目的 UpdateHub 固件空中升级。 |
| <a id="row_9_4_"></a><a id="arr_9_4_"></a>10.5 | [hawkBit 固件空中升级（Firmware Over-the-Air）](../firmware_update/P027_hawkBit接口.md) | hawkBit Firmware Over-the-Air | 面向 Zephyr 项目的 HawkBit 固件空中升级。 |
| <a id="row_9_4_0_"></a>10.5.1 | [hawkBit 自动处理程序 API（Autohandler API）](../firmware_update/P028_hawkBit自动处理接口.md) | hawkBit autohandler API | hawkBit 自动处理程序 API（Autohandler API） |
| <a id="row_9_4_1_"></a>10.5.2 | [hawkBit 配置 API（Configuration API）](../firmware_update/P029_hawkBit配置接口.md) | hawkBit configuration API | hawkBit 配置 API（Configuration API） |
| <a id="row_9_4_2_"></a>10.5.3 | [hawkBit 事件 API（Event API）](../firmware_update/P030_hawkBit事件接口.md) | hawkBit event API | hawkBit 事件 API（Event API） |

## 1.11\_工具链抽象（Toolchain abstraction）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_10_"></a>11 | [工具链抽象（Toolchain abstraction）](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html) | Toolchain abstraction | 利用工具链专用属性（Attribute）和/或编译指示（Pragma）来抽象编译器能力的宏。 |

## 1.12\_实用工具（Utilities）

| 层级 | 主题译名与链接 | 原文名称（English） | 简要说明 |
| --- | --- | --- | --- |
| <a id="row_11_"></a><a id="arr_11_"></a>12 | [实用工具（Utilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html) | Utilities | 实用工具（Utilities） |
| <a id="row_11_0_"></a>12.1 | [Base64](../base64_reference/P001_Base64编解码接口.md) | Base64 | Base64编码／解码（Encoding / Decoding）函数。 |
| <a id="row_11_1_"></a>12.2 | [位反转操作（Bit Reverse Operations）](../checksum_reference/P004_位反转接口.md) | Bit Reverse Operations |  |
| <a id="row_11_2_"></a>12.3 | [一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html) | COBS (Consistent Overhead Byte Stuffing) | 支持自定义分隔符的 COBS 编码与解码函数。 |
| <a id="row_11_3_"></a><a id="arr_11_3_"></a>12.4 | [数字信号处理（Digital Signal Processing，DSP）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html) | DSP (Digital Signal Processing) | 数字信号处理（DSP）数学函数和工具。 |
| <a id="row_11_3_0_"></a><a id="arr_11_3_0_"></a>12.4.1 | [基本数学函数（Basic Math Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic.html) | Basic Math Functions | 用于 DSP 的基本逐元素数学运算。 |
| <a id="row_11_3_0_0_"></a>12.4.1.1 | [向量绝对值（Vector Absolute Value）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html) | Vector Absolute Value | 逐元素计算向量的绝对值。 |
| <a id="row_11_3_0_1_"></a>12.4.1.2 | [向量加法（Vector Addition）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html) | Vector Addition | 对两个向量逐元素相加。 |
| <a id="row_11_3_0_2_"></a>12.4.1.3 | [向量限幅（Vector Clipping）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html) | Vector Clipping | 逐元素对值进行限幅。 |
| <a id="row_11_3_0_3_"></a>12.4.1.4 | [向量点积（Vector Dot Product）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html) | Vector Dot Product | 计算两个向量的点积。 |
| <a id="row_11_3_0_4_"></a>12.4.1.5 | [向量乘法（Vector Multiplication）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html) | Vector Multiplication | 对两个向量逐元素相乘。 |
| <a id="row_11_3_0_5_"></a>12.4.1.6 | [向量取负（Vector Negate）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html) | Vector Negate | 对向量的各元素取负。 |
| <a id="row_11_3_0_6_"></a>12.4.1.7 | [向量偏移（Vector Offset）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html) | Vector Offset | 为向量的每个元素加上一个常量偏移值。 |
| <a id="row_11_3_0_7_"></a>12.4.1.8 | [向量缩放（Vector Scale）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html) | Vector Scale | 将向量乘以一个标量值。 |
| <a id="row_11_3_0_8_"></a>12.4.1.9 | [向量移位（Vector Shift）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html) | Vector Shift | 将定点向量的各元素移位指定的位数。 |
| <a id="row_11_3_0_9_"></a>12.4.1.10 | [向量减法（Vector Subtraction）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html) | Vector Subtraction | 对两个向量逐元素相减。 |
| <a id="row_11_3_0_10_"></a>12.4.1.11 | [向量按位与（Vector bitwise AND）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html) | Vector bitwise AND | 计算逻辑按位与。 |
| <a id="row_11_3_0_11_"></a>12.4.1.12 | [向量按位非（Vector bitwise NOT）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html) | Vector bitwise NOT | 计算逻辑按位非。 |
| <a id="row_11_3_0_12_"></a>12.4.1.13 | [向量按位或（Vector bitwise OR）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__or.html) | Vector bitwise OR | 计算逻辑按位或。 |
| <a id="row_11_3_0_13_"></a>12.4.1.14 | [向量按位异或（Vector bitwise XOR）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html) | Vector bitwise XOR | 计算逻辑按位异或。 |
| <a id="row_11_3_1_"></a><a id="arr_11_3_1_"></a>12.4.2 | [浮点/定点移位转换函数（Float/Fixed point shift conversion functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__utils__shifts.html) | Float/Fixed point shift conversion functions | 在 Float 或 Double 表示与 Q31/Q15/Q7 表示之间双向转换数值。 |
| <a id="row_11_3_1_0_"></a>12.4.2.1 | [定点到浮点转换（Fixed to Float point conversions）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html) | Fixed to Float point conversions | 通过移位将 Q7/Q15/Q31 数值转换为 Float 或 Double 表示。 |
| <a id="row_11_3_1_1_"></a>12.4.2.2 | [浮点到定点转换（Float to Fixed point conversions）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html) | Float to Fixed point conversions | 将 Float 或 Double 数值表示转换为 Q31/Q15/Q7 表示。 |
| <a id="row_11_3_2_"></a>12.4.3 | [用于打印 Q 格式数值的辅助宏。](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html) | Helper macros for printing Q values. | 扩展现有的 `inttypes` 头文件，以支持打印格式化。 |
| <a id="row_11_4_"></a><a id="arr_11_4_"></a>12.5 | [数据结构 API（Data Structure APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__datastructure__apis.html) | Data Structure APIs |  |
| <a id="row_11_4_0_"></a>12.5.1 | [平衡红黑树（Balanced Red/Black Tree）](../rbtree_reference/P001_红黑树公共接口.md) | Balanced Red/Black Tree | 平衡红黑树（Balanced Red/Black Tree）实现。 |
| <a id="row_11_4_1_"></a>12.5.2 | [位数组（Bit array）](../bitarray_reference/P001_位数组公共接口.md) | Bit array | 在位数组（Bit Array）中存储和操作各个位。 |
| <a id="row_11_4_2_"></a>12.5.3 | [并查集（Disjoint-set）](../unionfind_reference/P001_并查集公共接口.md) | Disjoint-set | 不相交集合／并查集（Disjoint-set／Union-Find）实现。 |
| <a id="row_11_4_3_"></a>12.5.4 | [双向链表（Doubly-linked list）](../dlist_reference/P001_双向链表公共接口.md) | Doubly-linked list | 双向链表（Doubly-linked List）实现。 |
| <a id="row_11_4_4_"></a>12.5.5 | [带标志的单向链表（Flagged Single-linked list）](../sflist_reference/P001_带标志单向链表公共接口.md) | Flagged Single-linked list | 带标志单向链表（Flagged Single-linked List）实现。 |
| <a id="row_11_4_5_"></a><a id="arr_11_4_5_"></a>12.5.6 | [哈希映射（Hashmap）](../hashmap_reference/P001_哈希映射公共接口.md) | Hashmap | 哈希映射（Hashmap，又称哈希表／Hash Table）API。 |
| <a id="row_11_4_5_0_"></a>12.5.6.1 | [哈希函数（Hash Functions）](../hashmap_reference/P019_哈希函数公共接口.md) | Hash Functions |  |
| <a id="row_11_4_5_1_"></a>12.5.6.2 | [哈希映射实现（Hashmap Implementations）](../hashmap_reference/P011_哈希映射实现概览.md) | Hashmap Implementations |  |
| <a id="row_11_4_6_"></a><a id="arr_11_4_6_"></a>12.5.7 | [多生产者、单消费者（Multi producer, single consumer，MPSC）分组缓冲区 API](../intercore_reference/P166_MPSC数据包缓冲区接口.md) | MPSC (Multi producer, single consumer) packet buffer API | 多生产者、单消费者分组缓冲区 API |
| <a id="row_11_4_6_0_"></a>12.5.7.1 | [多生产者、单消费者（Multi producer, single consumer，MPSC）分组头](../intercore_reference/P172_MPSC数据包描述接口.md) | MPSC (Multi producer, single consumer) packet header | 多生产者、单消费者分组头 |
| <a id="row_11_4_6_1_"></a>12.5.7.2 | [MPSC 分组缓冲区标志](../intercore_reference/P167_MPSC数据包缓冲区标志.md) | MPSC packet buffer flags |  |
| <a id="row_11_4_7_"></a>12.5.8 | [MPSC 无锁队列 API（Lockfree Queue API）](../intercore_reference/P158_MPSC无锁队列接口.md) | MPSC Lockfree Queue API | 多生产者、单消费者（Multiple Producer Single Consumer，MPSC）无锁队列 API |
| <a id="row_11_4_8_"></a>12.5.9 | [最小堆（Min-heap）](../minheap_reference/P001_值最小堆公共接口.md) | Min-heap | 最小堆（Min-heap）实现。 |
| <a id="row_11_4_9_"></a>12.5.10 | [引用最小堆（Reference min-heap）](../minheap_reference/P005_引用最小堆公共接口.md) | Reference min-heap | 引用式、基于句柄的最小堆（Reference / Handle-based Min-heap）实现。 |
| <a id="row_11_4_10_"></a>12.5.11 | [环形缓冲区 API（Ring Buffer APIs）](../ringbuffer_reference/P001_环形缓冲区公共接口.md) | Ring Buffer APIs | 简单、仅需头文件的环形缓冲区（Header-only Ring Buffer）实现。 |
| <a id="row_11_4_11_"></a>12.5.12 | [环形队列（Ring queue）](../ringq_reference/P001_环形队列公共接口.md) | Ring queue | 固定大小的环形队列（Fixed-size Circular Queue）。 |
| <a id="row_11_4_12_"></a><a id="arr_11_4_12_"></a>12.5.13 | [单生产者、单消费者（Single producer, single consumer，SPSC）分组缓冲区 API](../intercore_reference/P150_SPSC数据包缓冲区接口.md) | SPSC (Single producer, single consumer) packet buffer API | 单生产者、单消费者分组缓冲区 API |
| <a id="row_11_4_12_0_"></a>12.5.13.1 | [SPSC 分组缓冲区标志](../intercore_reference/P157_SPSC数据包缓冲区标志.md) | SPSC packet buffer flags |  |
| <a id="row_11_4_13_"></a>12.5.14 | [SPSC API](../intercore_reference/P163_SPSC无锁队列接口.md) | SPSC API | 单生产者、单消费者（Single Producer Single Consumer，SPSC）无锁队列 API |
| <a id="row_11_4_14_"></a>12.5.15 | [单向链表（Single-linked list）](../slist_reference/P001_单向链表公共接口.md) | Single-linked list | 单向链表（Single-linked List）实现。 |
| <a id="row_11_5_"></a><a id="arr_11_5_"></a>12.6 | [格式化输出 API（Formatted Output APIs）](../cbprintf_reference/P001_回调格式化输出接口.md) | Formatted Output APIs |  |
| <a id="row_11_5_0_"></a>12.6.1 | [封装包转换标志（Package convert flags）](../cbprintf_reference/P014_格式化包转换标志.md) | Package convert flags |  |
| <a id="row_11_5_1_"></a>12.6.2 | [封装包标志（Package flags）](../cbprintf_reference/P013_格式化包创建标志.md) | Package flags |  |
| <a id="row_11_6_"></a><a id="arr_11_6_"></a>12.7 | [JSON](../serialization/P006_JSON接口参考.md) | JSON |  |
| <a id="row_11_6_0_"></a>12.7.1 | [JSON Web 令牌（JSON Web Token，JWT）](../crypto/P030_JWT构建与签名接口.md) | JSON Web Token (JWT) | JSON Web 令牌（JSON Web Token，JWT）——RFC 7519 |
| <a id="row_11_7_"></a>12.8 | [线性范围（Linear Range）](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html) | Linear Range |  |
| <a id="row_11_8_"></a>12.9 | [整数以 2 为底的对数数学函数（Math Ilog2 Functions）](../numeric_reference/P005_整数二进制对数公共接口.md) | Math Ilog2 Functions | 用于数学运算的整数 log2 工具。 |
| <a id="row_11_9_"></a>12.10 | [数学插值函数（Math Interpolation Functions）](../interpolation_reference/P001_插值公共接口.md) | Math Interpolation Functions | 用于数学运算的线性插值工具（Linear Interpolation Utilities）。 |
| <a id="row_11_10_"></a>12.11 | [数学扩展（Math extras）](../math_reference/P001_数学辅助公共接口.md) | Math extras | 额外的算术与位操作函数（Arithmetic and Bit Manipulation Functions）。 |
| <a id="row_11_11_"></a>12.12 | [导航（Navigation）](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html) | Navigation | 导航工具。 |
| <a id="row_11_12_"></a>12.13 | [引用计数（Reference counting）](../sysref_reference/P001_引用计数接口.md) | Reference counting |  |
| <a id="row_11_13_"></a><a id="arr_11_13_"></a>12.14 | [系统输入输出接口（System I/O APIs）。](../device_reference/P017_系统IO公共接口.md) | System I/O APIs | 系统输入输出接口（System I/O APIs）。 |
| <a id="row_11_13_0_"></a>12.14.1 | [内存位操作 API（Memory bit manipulation APIs）](../device_reference/P020_内存位操作接口.md) | Memory bit manipulation APIs |  |
| <a id="row_11_13_1_"></a>12.14.2 | [内存映射寄存器 I/O API（Memory-mapped register I/O APIs）](../device_reference/P019_内存映射寄存器IO接口.md) | Memory-mapped register I/O APIs |  |
| <a id="row_11_13_2_"></a>12.14.3 | [端口 I/O API（Port I/O APIs）](../device_reference/P018_端口IO接口.md) | Port I/O APIs |  |
| <a id="row_11_14_"></a><a id="arr_11_14_"></a>12.15 | [时间工具 API（Time Utility APIs）](../timeutil_reference/P001_时间工具接口概览.md) | Time Utility APIs |  |
| <a id="row_11_14_0_"></a>12.15.1 | [时间表示 API（Time Representation APIs）](../timeutil_reference/P002_时间表示接口.md) | Time Representation APIs |  |
| <a id="row_11_14_1_"></a>12.15.2 | [时间同步 API（Time Synchronization APIs）](../timeutil_reference/P003_时间同步接口.md) | Time Synchronization APIs |  |
| <a id="row_11_14_2_"></a>12.15.3 | [时间单位辅助工具（Time Units Helpers）](../timeutil_reference/P007_时间单位辅助接口.md) | Time Units Helpers | 用于不同时间单位之间转换的辅助API。 |
| <a id="row_11_14_3_"></a>12.15.4 | [timespec 工具 API（Timespec Utility APIs）](../timeutil_reference/P008_timespec时间工具接口.md) | Timespec Utility APIs |  |
| <a id="row_11_15_"></a>12.16 | [通用唯一标识符（UUID）。](../data_utilities/P023_UUID生成与转换接口.md) | UUID |  |
| <a id="row_11_16_"></a>12.17 | [实用函数（Utility Functions）](../util_reference/P001_通用工具公共接口.md) | Utility Functions |  |

---

[返回大纲](大纲.md) · [返回官方参考库](../reference_library/README.md)
