---
id: learning.zephyr-docs.api-guides.api_overview
title: API概览
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/develop/api/overview.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="api-overview"></a>

# 第2章\_API概览

原文：[API Overview](https://docs.zephyrproject.org/latest/develop/api/overview.html)。本次核对日期：2026-10-14；翻译基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

本表列出 Zephyr 的**应用程序编程接口（Application Programming Interface，API）**及其相关信息，包括当前的[稳定性级别（Stability Level）](P004_API生命周期.md)。主要发行版之间的 API 变更详情见[发行说明（Releases）](https://docs.zephyrproject.org/latest/releases/index.html#zephyr-release-notes)。

## 2.1\_版本号与稳定性

“版本（Version）”列采用[语义化版本（Semantic Versioning）](https://semver.org/)，遵循以下要求。

1. **主版本号（Major Version）为 0，即 `0.y.z`，表示初始开发阶段。**任何内容都可以（MAY）随时变化，不应（SHOULD NOT）认为公共 API 已经稳定。当次版本号不大于 1（原文以 `0.1.z` 表示）时，API 属于**实验性（Experimental）**；当次版本号大于 1，即 `0.y.z` 且 `y > 1` 时，API 属于**不稳定（Unstable）**。
2. **版本 `1.0.0` 定义公共 API。**此后如何递增版本号，取决于这个公共 API 及其变化方式。主版本号大于等于 1，即 `x.y.z` 且 `x >= 1` 的 API 被视为**稳定（Stable）**；Zephyr 中所有已有的稳定 API 都从 `1.0.0` 开始编号。
3. **补丁版本号（Patch Version）`Z`，即 `x.y.Z` 且 `x > 0`：**若只引入向后兼容的错误修复，就必须（MUST）递增。错误修复指纠正不正确行为的内部变更。
4. **次版本号（Minor Version）`Y`，即 `x.Y.z` 且 `x > 0`：**若向公共 API 引入向后兼容的新功能，就必须递增；若将任何公共 API 功能标记为**已弃用（Deprecated）**，也必须递增。若在私有代码中引入较大的新功能或改进，可以递增。次版本可以包含补丁级变更；递增次版本号时，必须把补丁版本号重置为 `0`。
5. **主版本号 `X`：**在主版本号已经大于 0 时，如果对 API 做出破坏兼容性的变更，就必须递增主版本号。

> 译注：原文第 5 条将版本形式写为 `x.Y.z`，该条要求递增的是主版本号 `X`。

**注意（Note）：**已有 API 的初始版本根据其当前状态设置：`0.1.0` 表示实验性 API，`0.8.0` 表示不稳定 API，`1.0.0` 表示稳定 API。今后修改 API 时，需要按照以上规则调整版本。

## 2.2\_完整API表

> 译注：以下保留官方表的全部 1625 行及其顺序，按原有顶层类别分成小节，缩进表示原有层级。“版本”是 API 版本，“自哪个 Zephyr 版本提供”是首次提供该 API 的 Zephyr 发行版，两者不可混用。空白单元格表示原表未填写，不从父项推断。中文与英文原名并列；厂商、芯片型号、产品名及标识符保留官方拼写。英文名称链接指向原始官方参考；已有对应译文时，中文名称提供相对路径链接。表中有相同名称出现在不同分组的情况，按原文保留，不合并。完成本概览不代表其链接的每份 API 参考正文都已翻译。

### 2.2.1\_设备驱动（Device Drivers）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 设备驱动 | [Device Drivers](https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html) |  |  |
| 　单总线（1-Wire） | [1-Wire](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html) | 0.8.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.2.0) |
| 　　单总线（1-Wire）驱动后端 API | [1-Wire Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html) |  |  |
| 　　1-Wire 传感器 API | [1-Wire Sensor API](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html) |  |  |
| 　　1-Wire 数据链路层 | [1-Wire data link layer](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html) |  |  |
| 　　1-Wire 网络层 | [1-Wire network layer](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html) |  |  |
| 　[模数转换器（ADC）](../hardware/P463_ADC公共接口参考.md) | [ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[模数转换器（ADC）驱动后端 API](../hardware/P456_ADC驱动后端.md) | [ADC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html) |  |  |
| 　　[ADS126X ADC 驱动 API](../hardware/P472_ADS126X驱动接口.md) | [ADS126X ADC driver API](https://docs.zephyrproject.org/latest/doxygen/html/group__ads126x__interface.html) |  |  |
| 　　[设备专用模数转换器（ADC） API 扩展](../hardware/P465_ADC设备专用扩展.md) | [Device-specific ADC API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__ext.html) |  |  |
| 　　　[ADS131M02](../hardware/P467_ADS131M02扩展接口.md) | [ADS131M02](https://docs.zephyrproject.org/latest/doxygen/html/group__ads131m02__interface.html) |  |  |
| 　　　[ADS1x4s0x](../hardware/P468_ADS1x4s0x扩展接口.md) | [ADS1x4s0x](https://docs.zephyrproject.org/latest/doxygen/html/group__ads1x4s0x__interface.html) |  |  |
| 　　　[电流检测放大器](../hardware/P457_ADC电流检测放大器接口.md) | [Current Sense Amplifier](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html) |  |  |
| 　　　[电流检测分流电阻](../hardware/P458_ADC电流检测分流器接口.md) | [Current Sense Shunt](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__shunt__interface.html) |  |  |
| 　　　[Infineon AutAnalog 逐次逼近型（SAR）ADC](../hardware/P469_Infineon自动模拟SAR扩展接口.md) | [Infineon AutAnalog SAR ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__infineon__autanalog__sar__interface.html) | 1.0.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　[LMP90xxx](../hardware/P470_LMP90xxx扩展接口.md) | [LMP90xxx](https://docs.zephyrproject.org/latest/doxygen/html/group__lmp90xxx__interface.html) |  |  |
| 　　　[分压器](../hardware/P459_ADC分压器接口.md) | [Voltage Divider](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html) |  |  |
| 　　　[WisBlock 模数转换器](../hardware/P471_WisBlock_ADC通道.md) | [WisBlock ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html) |  |  |
| 　　[模拟模数转换器（ADC）](../hardware/P464_ADC模拟器接口.md) | [Emulated ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html) |  |  |
| 　　[Renesas RA ADC_B 通道选择器](../hardware/P473_Renesas_ADC_B通道选择.md) | [Renesas RA ADC_B channel selectors](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html) |  |  |
| 　音频 | [Audio](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__interface.html) |  |  |
| 　　音频编解码器接口 | [Audio Codec Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html) | 0.3.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　音频编解码器驱动后端 API | [Audio Codec Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html) |  |  |
| 　　　设备专用音频编解码器 API 扩展 | [Device-specific audio codec API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__ext.html) |  |  |
| 　　　　CS35L5X | [CS35L5X](https://docs.zephyrproject.org/latest/doxygen/html/group__cs35l5x__interface.html) |  |  |
| 　　数字麦克风接口 | [Digital Microphone Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html) | 0.2.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　数字麦克风驱动后端 API | [Digital Microphone Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html) |  |  |
| 　　MIDI 2 通用 MIDI 数据包定义 | [MIDI2 Universal MIDI Packet definitions](../usb/P098_通用MIDI数据包定义.md) | 0.1.0 | [v4.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.1.0) |
| 　　　MIDI 命令 | [MIDI commands](../usb/P100_MIDI命令常量.md) |  |  |
| 　　　消息类型 | [Message types](../usb/P101_UMP消息类型.md) |  |  |
| 　　　系统公共消息与系统实时消息状态 | [System common and System Real Time message status](../usb/P102_MIDI系统消息状态.md) |  |  |
| 　　　UMP 流响应器 | [UMP Stream Responder](../usb/P108_UMP流响应器API.md) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　　UMP 流专用字段 | [UMP Stream specific fields](../usb/P103_UMP流消息字段.md) |  |  |
| 　　　　UMP 流功能块发现消息过滤位 | [UMP Stream Function Block discovery message filter bits](../usb/P107_UMP功能块发现过滤位.md) |  |  |
| 　　　　UMP 流端点发现消息过滤位 | [UMP Stream endpoint discovery message filter bits](../usb/P106_UMP端点发现过滤位.md) |  |  |
| 　　　　UMP 流格式 | [UMP Stream format](../usb/P104_UMP流消息格式.md) |  |  |
| 　　　　UMP 流状态 | [UMP Stream status](../usb/P105_UMP流消息状态.md) |  |  |
| 　　　通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议 | [Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](../usb/P113_UMP格式与MIDI协议依据.md) |  |  |
| 　辅助（文本）显示 | [Auxiliary (Text) Display](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　辅助显示驱动后端 API | [Auxiliary Display Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html) |  |  |
| 　电池备份 RAM（BBRAM） | [BBRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html) | 1.0.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　电池备份 RAM（BBRAM）驱动后端 API | [BBRAM Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html) |  |  |
| 　　[电池备份 RAM（BBRAM）模拟器后端 API](../hardware/P490_BBRAM仿真后端接口.md) | [BBRAM emulator backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html) |  |  |
| 　BCM283x 中断控制器 | [BCM283x interrupt controllers](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html) |  |  |
| 　电池充电器 | [Battery Charger](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　充电器驱动后端 API | [Charger Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html) |  |  |
| 　　设备专用充电器 API 扩展 | [Device-specific Charger API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__ext.html) |  |  |
| 　　　nPM10xx 充电器接口 | [nPM10xx Charger interface](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html) |  |  |
| 　生物特征识别 | [Biometrics](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　生物特征识别驱动后端 API | [Biometrics Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html) |  |  |
| 　　[生物特征识别模拟器测试辅助接口](../hardware/P495_生物识别仿真测试接口.md) | [Biometrics emulator test helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html) |  |  |
| 　[蜂鸣器](../hardware/P144_蜂鸣器接口参考.md) | [Buzzer](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　[蜂鸣器驱动后端 API](../hardware/P145_蜂鸣器驱动后端.md) | [Buzzer Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html) |  |  |
| 　[控制器局域网（CAN）](../hardware/P361_CAN公共接口.md) | [CAN](https://docs.zephyrproject.org/latest/doxygen/html/group__can__interface.html) |  |  |
| 　　[CAN 控制器](../hardware/P362_CAN控制器接口.md) | [CAN Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html) | 1.2.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　[CAN 控制器驱动后端 API](../hardware/P369_CAN控制器后端接口.md) | [CAN Controller Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html) |  |  |
| 　　[CAN 收发器](../hardware/P041_CAN收发器接口参考.md) | [CAN Transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver.html) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　　[CAN 收发器驱动后端 API](../hardware/P050_CAN收发器驱动后端接口.md) | [CAN Transceiver Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver__backend.html) |  |  |
| 　　[设备树控制器局域网（CAN） API](../hardware/P373_CAN设备树宏.md) | [Devicetree CAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-can.html) |  |  |
| 　　[伪 CAN 控制器](../hardware/P374_伪CAN控制器接口.md) | [Fake CAN controller](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html) |  |  |
| 　[循环冗余校验（CRC）驱动 API](../hardware/P038_CRC驱动接口参考.md) | [CRC driver APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　[CRC 驱动后端 API](../hardware/P047_CRC驱动后端接口.md) | [CRC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html) |  |  |
| 　蜂窝通信 | [Cellular](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html) | 0.8.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　蜂窝通信驱动后端 API | [Cellular Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html) |  |  |
| 　　　蜂窝调制解调器辅助接口 | [Cellular modem helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cellular__backend.html) |  |  |
| 　　　　蜂窝调制解调器驱动定义宏 | [Cellular modem driver definition macros](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html) |  |  |
| 　　设备专用蜂窝通信 API 扩展 | [Device-specific Cellular API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__ext.html) |  |  |
| 　　　HL7800 | [HL7800](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html) |  |  |
| 　　　HL78xx | [HL78xx](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html) |  |  |
| 　　　SIMCom SIM7080 | [SIMCom SIM7080](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html) |  |  |
| 　　　ST87Mxx | [ST87Mxx](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html) |  |  |
| 　　　　GNSS 配置 | [GNSS configuration](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__gnss__configuration.html) |  |  |
| 　　　　ST87Mxx 常量 | [ST87Mxx Constants](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__constants.html) |  |  |
| 　　　　Wi-Fi 扫描配置 | [WIFI scanning configuration](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__wscan__configuration.html) |  |  |
| 　[时钟控制](../timer_reference/P092_时钟控制公共接口.md) | [Clock Control](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[时钟控制驱动后端 API](../timer_reference/P093_时钟控制驱动后端接口.md) | [Clock Control Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface__backend.html) |  |  |
| 　　[设备专用时钟控制 API 扩展](../timer_reference/P097_时钟控制扩展接口总览.md) | [Device-specific Clock Control API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface__ext.html) |  |  |
| 　　　ARM CMSDK | [ARM CMSDK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html) |  |  |
| 　　　Ambiq | [Ambiq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html) |  |  |
| 　　　Analog Devices MAX32 | [Analog Devices MAX32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adi__max32.html) |  |  |
| 　　　Atmel SAM PMC | [Atmel SAM PMC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__atmel__sam__pmc.html) |  |  |
| 　　　Bouffalo Lab | [Bouffalo Lab](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html) |  |  |
| 　　　Core Devices SF32LB | [Core Devices SF32LB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html) |  |  |
| 　　　Espressif ESP32 | [Espressif ESP32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html) |  |  |
| 　　　GigaDevice GD32 | [GigaDevice GD32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__gd32.html) |  |  |
| 　　　Infineon CAT1 | [Infineon CAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html) |  |  |
| 　　　Intel ADSP | [Intel ADSP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adsp.html) |  |  |
| 　　　[LiteX](../timer_reference/P119_LiteX时钟控制接口.md) | [LiteX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__litex.html) |  |  |
| 　　　Microchip | [Microchip](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp.html) |  |  |
| 　　　　Microchip PIC32CM JH | [Microchip PIC32CM JH](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html) |  |  |
| 　　　　Microchip PIC32CM PL | [Microchip PIC32CM PL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html) |  |  |
| 　　　　Microchip PIC32CZ CA | [Microchip PIC32CZ CA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html) |  |  |
| 　　　　Microchip SAM D5x/E5x | [Microchip SAM D5x/E5x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html) |  |  |
| 　　　　Microchip SAM PMC | [Microchip SAM PMC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__pmc.html) |  |  |
| 　　　　Microchip XEC | [Microchip XEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__xec.html) |  |  |
| 　　　NXP | [NXP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nxp.html) |  |  |
| 　　　　NXP LPC11U6x | [NXP LPC11U6x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__lpc11u6x.html) |  |  |
| 　　　　NXP 时钟源 | [NXP clock sources](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nxp__sources.html) |  |  |
| 　　　Nordic nRF | [Nordic nRF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html) |  |  |
| 　　　Nuvoton NuMaker | [Nuvoton NuMaker](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numaker.html) |  |  |
| 　　　Nuvoton NuMicro | [Nuvoton NuMicro](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html) |  |  |
| 　　　Raspberry Pi Pico | [Raspberry Pi Pico](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html) |  |  |
| 　　　Realtek Ameba | [Realtek Ameba](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ameba.html) |  |  |
| 　　　Realtek BEE | [Realtek BEE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html) |  |  |
| 　　　Realtek RTS5912 | [Realtek RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rts5912.html) |  |  |
| 　　　Renesas R-Car | [Renesas R-Car](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html) |  |  |
| 　　　Renesas R-Car CPG/MSSR | [Renesas R-Car CPG/MSSR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__cpg__mssr.html) |  |  |
| 　　　Renesas RA CGC | [Renesas RA CGC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra.html) |  |  |
| 　　　　Renesas RA BSP 时钟输出分频常量 | [Renesas RA BSP Clock Clkout Divider Constants](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html) |  |  |
| 　　　　Renesas RA BSP 时钟源常量 | [Renesas RA BSP Clock Source Constants](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html) |  |  |
| 　　　　Renesas RA 时钟分频生成器 | [Renesas RA Clock Divider Generators](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html) |  |  |
| 　　　Renesas RX CGC | [Renesas RX CGC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html) |  |  |
| 　　　Renesas RZ CGC | [Renesas RZ CGC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rz.html) |  |  |
| 　　　Renesas SmartBond | [Renesas SmartBond](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html) |  |  |
| 　　　[STMicroelectronics STM32](../timer_reference/P123_STM32时钟控制接口.md) | [STMicroelectronics STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__stm32.html) |  |  |
| 　　　Silicon Labs | [Silicon Labs](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html) |  |  |
| 　　　Silicon Labs SiWx91x | [Silicon Labs SiWx91x](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html) |  |  |
| 　　　TI | [TI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__cdce9xx.html) |  |  |
| 　　　Texas Instruments MSPM0 | [Texas Instruments MSPM0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html) |  |  |
| 　　　Texas Instruments TISCI | [Texas Instruments TISCI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html) |  |  |
| 　　[设备树时钟 API](../timer_reference/P107_设备树时钟获取宏.md) | [Devicetree Clocks API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html) |  |  |
| 　　　Aesc Silicon 时钟域标识符 | [Aesc Silicon clock domain identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html) |  |  |
| 　　　FocalTech FT9001 时钟标识符 | [FocalTech FT9001 clock identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html) |  |  |
| 　　　Microchip SmartFusion2 时钟标识符 | [Microchip SmartFusion2 clock identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html) |  |  |
| 　　　NXP i.MX952 时钟源 | [NXP i.MX952 Clock Sources](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html) |  |  |
| 　　　　外设时钟（41–163） | [Peripheral Clocks (41-163)](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html) |  |  |
| 　　Nuvoton M48x 时钟控制器设备树辅助接口 | [Nuvoton M48x Clock Controller Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nuvoton__m48x.html) |  |  |
| 　　Nuvoton NuMaker 控制器设备树辅助接口 | [Nuvoton NuMaker controller Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__controller__nuvoton__m031x.html) |  |  |
| 　　Nuvoton NuMaker 控制器设备树辅助接口 | [Nuvoton NuMaker controller Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__controller__nuvoton__m335x.html) |  |  |
| 　　Silicon Labs Series 2 和 3 设备树辅助接口 | [Silicon Labs Series 2 and 3 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs.html) |  |  |
| 　　Silicon Labs SiWx91x 时钟标识符 | [Silicon Labs SiWx91x clock identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html) |  |  |
| 　[时钟监测器](../timer_reference/P098_时钟监控公共接口.md) | [Clock Monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__monitor__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　[时钟监测器驱动后端 API](../timer_reference/P099_时钟监控驱动后端接口.md) | [CLOCK_MONITOR Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__monitor__interface__backend.html) |  |  |
| 　[比较器](../hardware/P089_比较器接口参考.md) | [Comparator](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html) | 0.8.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　[比较器驱动后端 API](../hardware/P093_比较器驱动后端接口.md) | [Comparator Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface__backend.html) |  |  |
| 　　[伪比较器](../hardware/P090_伪比较器接口.md) | [Fake comparator](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html) |  |  |
| 　[核心转储伪设备](../observability/P053_核心转储设备接口.md) | [Coredump pseudo-device](https://docs.zephyrproject.org/latest/doxygen/html/group__coredump__device__interface.html) | 0.1.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.2.0) |
| 　　[核心转储伪设备驱动后端 API](../observability/P054_核心转储设备后端接口.md) | [Coredump pseudo-device Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__coredump__device__interface__backend.html) |  |  |
| 　[计数器](../timer_reference/P022_计数器公共接口.md) | [Counter](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface.html) | 1.1.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　[计数器驱动后端 API](../timer_reference/P023_计数器驱动后端接口.md) | [Counter Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface__backend.html) |  |  |
| 　　[计数器捕获 API](../timer_reference/P032_计数器捕获接口.md) | [Counter capture APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__capture.html) |  |  |
| 　　[设备专用计数器 API 扩展](../timer_reference/P041_计数器器件扩展入口.md) | [Device-specific Counter API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface__ext.html) |  |  |
| 　　　[STM32 计数器捕获](../timer_reference/P042_STM32计数器扩展接口.md) | [STM32 counter capture](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__stm32__interface.html) |  |  |
| 　　[设备树计数器捕获 API](../timer_reference/P034_计数器捕获设备树宏.md) | [Devicetree Counter Captures API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-counter-captures.html) |  |  |
| 　　[模拟计数器](../hardware/P493_计数器仿真后端接口.md) | [Emulated counter](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__emul.html) |  |  |
| 　[数模转换器（DAC）](../hardware/P822_数模转换器接口.md) | [DAC](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html) | 1.1.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　[数模转换器（DAC）驱动后端 API](../hardware/P823_DAC驱动实现接口.md) | [DAC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html) |  |  |
| 　　[设备专用数模转换器（DAC） API 扩展](../hardware/P824_DAC驱动扩展入口.md) | [Device-specific DAC API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__ext.html) |  |  |
| 　　　[DAC161S997](../hardware/P828_DAC161S997扩展接口.md) | [DAC161S997](https://docs.zephyrproject.org/latest/doxygen/html/group__dac161s997__interface.html) |  |  |
| 　数字音频接口（DAI） | [DAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html) | 0.9.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　数字音频接口（DAI）驱动后端 API | [DAI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface__backend.html) |  |  |
| 　数字可寻址照明接口（DALI） | [DALI](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　数字可寻址照明接口（DALI）驱动后端 API | [DALI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html) |  |  |
| 　DAP Link | [DAP Link](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　直接存储器访问（DMA） | [DMA](../dma_reference/P001_DMA公共接口.md) | 1.1.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　　DMA（SF32LB 专用部分） | [DMA (SF32LB specifics)](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html) |  |  |
| 　　直接存储器访问（DMA）驱动后端 API | [DMA Driver Backend API](../dma_reference/P002_DMA驱动后端接口.md) |  |  |
| 　　设备树直接存储器访问（DMA） API | [Devicetree DMA API](../dma_reference/P008_DMA设备树宏.md) |  |  |
| 　　Realtek Bee DMA 宏 | [Realtek Bee DMA Macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html) |  |  |
| 　　Xilinx ADMA 专用部分 | [Xilinx ADMA specifics](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html) |  |  |
| 　磁盘访问 | [Disk Access](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html) | 1.1.0 | [v1.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.6.0) |
| 　　设备专用磁盘访问 API 扩展 | [Device-specific Disk Access API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface__ext.html) |  |  |
| 　　　STM32 SDMMC | [STM32 SDMMC](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html) |  |  |
| 　[显示](../hardware/P214_显示公共接口.md) | [Display](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html) | 0.10.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　[AC057TC1 显示控制器](../hardware/P224_AC057TC1调色板扩展.md) | [AC057TC1 display controller](https://docs.zephyrproject.org/latest/doxygen/html/group__ac057tc1__display__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　[设备专用显示 API 扩展](../hardware/P223_显示器件扩展目录.md) | [Device-specific Display API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__ext.html) |  |  |
| 　　　[SSD16xx](../hardware/P228_SSD16xx显示扩展.md) | [SSD16xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html) |  |  |
| 　　[设备树显示 API](../hardware/P227_设备树显示接口.md) | [Devicetree Display API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-display.html) |  |  |
| 　　[显示驱动后端 API](../hardware/P219_显示驱动后端接口.md) | [Display Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html) |  |  |
| 　　　[颜色抖动](../hardware/P221_显示颜色抖动接口.md) | [Color dithering](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html) |  |  |
| 　　[显示面板设备树绑定](../hardware/P226_显示面板设备树格式.md) | [Display panel devicetree bindings](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html) |  |  |
| 　　[ED2208-GCA（EL073TF1）显示控制器](../hardware/P225_ED2208调色板扩展.md) | [ED2208-GCA (EL073TF1) display controller](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　[MIPI 显示接口](../hardware/P244_MIPI显示接口定义.md) | [MIPI Display interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html) |  |  |
| 　　[MIPI 显示总线接口（DBI）](../hardware/P245_MIPI显示总线接口.md) | [MIPI-DBI](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html) | 1.0.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　[MIPI 显示总线接口（DBI）驱动后端 API](../hardware/P251_MIPI显示总线后端.md) | [MIPI-DBI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html) |  |  |
| 　　[MIPI 显示串行接口（DSI）](../hardware/P246_MIPI显示串行接口.md) | [MIPI-DSI](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html) | 1.0.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　　[MIPI 显示串行接口（DSI）驱动后端 API](../hardware/P253_MIPI显示串行后端.md) | [MIPI-DSI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html) |  |  |
| 　　[单色字符帧缓冲区](../hardware/P184_单色字符帧缓冲接口.md) | [Monochrome Character Framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html) | 0.10.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　错误检测与纠正（EDAC） | [EDAC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.5.0) |
| 　　设备专用错误检测与纠正（EDAC） API 扩展 | [Device-specific EDAC API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface__ext.html) |  |  |
| 　　　NXP ERM 错误检测与纠正 | [NXP ERM EDAC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__nxp__erm__interface.html) |  |  |
| 　　　Synopsys DDR 控制器 EDAC | [Synopsys DDR controller EDAC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__synopsys__interface.html) |  |  |
| 　[电可擦可编程只读存储器（EEPROM）](../hardware/P040_EEPROM接口参考.md) | [EEPROM](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.1.0) |
| 　　[电可擦可编程只读存储器（EEPROM）驱动后端 API](../hardware/P049_EEPROM驱动后端接口.md) | [EEPROM Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html) |  |  |
| 　　[伪电可擦可编程只读存储器（EEPROM）](../hardware/P051_伪EEPROM接口.md) | [Fake EEPROM](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html) |  |  |
| 　增强型串行外设接口（eSPI） | [ESPI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html) | 1.0.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　　增强型串行外设接口（eSPI）驱动后端 API | [eSPI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html) |  |  |
| 　　[增强型串行外设接口（eSPI）模拟接口](../hardware/P486_eSPI总线仿真接口.md) | [eSPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html) |  |  |
| 　　eSPI 从属附接闪存（SAF） | [eSPI SAF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　eSPI 从属附接闪存（SAF）驱动后端 API | [eSPI SAF Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html) |  |  |
| 　[熵源](../hardware/P039_熵源接口参考.md) | [Entropy](https://docs.zephyrproject.org/latest/doxygen/html/group__entropy__interface.html) | 1.0.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　[熵源驱动后端 API](../hardware/P048_熵源驱动后端接口.md) | [Entropy Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__entropy__interface__backend.html) |  |  |
| 　外部缓存控制器 | [External Cache Controller](../cache_reference/P004_外部缓存接口.md) | 1.0.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　现场可编程门阵列（FPGA） | [FPGA](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　现场可编程门阵列（FPGA）驱动后端 API | [FPGA Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html) |  |  |
| 　闪存 | [Flash](../flash_reference/P001_Flash公共接口.md) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.2.0) |
| 　　扩展操作 | [Extended Operations](../flash_reference/P008_Flash扩展操作目录.md) |  |  |
| 　　　Andes QSPI-NOR 原地执行（XIP） | [Andes QSPI-NOR XIP](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html) |  |  |
| 　　　IT51XXX | [IT51XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html) |  |  |
| 　　　Microchip | [Microchip](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　Microchip NVMCTRL G1 | [Microchip NVMCTRL G1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html) |  |  |
| 　　　NPCX | [NPCX](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html) |  |  |
| 　　　Realtek RTS5912 | [Realtek RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html) |  |  |
| 　　　Renesas RA | [Renesas RA](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html) |  |  |
| 　　　ST M95P32 | [ST M95P32](../flash_reference/P011_M95P32扩展操作接口.md) |  |  |
| 　　　STM32 | [STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html) |  |  |
| 　　闪存驱动后端 API | [Flash Driver Backend API](../flash_reference/P002_Flash驱动后端接口.md) |  |  |
| 　　闪存内部接口 | [Flash Internal](../flash_reference/P003_Flash内部接口.md) |  |  |
| 　电量计 | [Fuel Gauge](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html) | 0.9.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　设备树电池辅助接口 | [Devicetree battery helpers](../dt_overview_reference/P002_电池开路电压曲线宏.md) |  |  |
| 　　电量计驱动后端 API | [Fuel Gauge Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html) |  |  |
| 　　[电量计后端模拟器 API](../hardware/P492_电量计仿真后端接口.md) | [Fuel gauge backend emulator APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html) |  |  |
| 　全球导航卫星系统（GNSS） | [GNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html) | 0.8.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　全球导航卫星系统（GNSS）驱动后端 API | [GNSS Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html) |  |  |
| 　[通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md) | [GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[设备专用通用输入输出（GPIO） API 扩展](../hardware/P274_GPIO器件扩展目录.md) | [Device-specific GPIO API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__ext.html) |  |  |
| 　　　[Ambiq](../hardware/P282_AmbiqGPIO扩展.md) | [Ambiq](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html) |  |  |
| 　　　[Bouffalolab BL61x GPIO FIFO／线输出](../hardware/P283_BL61xGPIO线输出.md) | [Bouffalolab BL61x GPIO FIFO / Wire Out](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__bl61x__wo__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　[MAX32 专用 GPIO 标志](../hardware/P277_MAX32GPIO标志.md) | [MAX32-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html) |  |  |
| 　　　[NCT38XX](../hardware/P285_NCT38XXGPIO扩展.md) | [NCT38XX](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html) |  |  |
| 　　　[NXP MCUX LPC](../hardware/P284_LPCGPIO扩展.md) | [NXP MCUX LPC](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html) |  |  |
| 　　　[NXP PCA 系列](../hardware/P286_PCAGPIO扩展.md) | [NXP PCA SERIES](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pca__series__interface.html) |  |  |
| 　　　[NXP PCAL64XXA](../hardware/P287_PCAL64XXAGPIO扩展.md) | [NXP PCAL64XXA](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pcal64xxa__interface.html) |  |  |
| 　　　[STM32 GPIO 专用标志](../hardware/P275_STM32GPIO标志.md) | [STM32 GPIO specific flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html) |  |  |
| 　　　[SX1509B](../hardware/P288_SX1509BGPIO扩展.md) | [SX1509B](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html) |  |  |
| 　　　[nPM10xx 专用 GPIO 标志](../hardware/P278_nPM10xxGPIO标志.md) | [nPM10xx-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html) |  |  |
| 　　　[nPM13xx 专用 GPIO 标志](../hardware/P279_nPM13xxGPIO标志.md) | [nPM13xx-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html) |  |  |
| 　　　[nPM2100 专用 GPIO 标志](../hardware/P280_nPM2100GPIO标志.md) | [nPM2100-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html) |  |  |
| 　　　[nPM6001 专用 GPIO 标志](../hardware/P281_nPM6001GPIO标志.md) | [nPM6001-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html) |  |  |
| 　　　[nRF 专用 GPIO 标志](../hardware/P276_nRFGPIO标志.md) | [nRF-specific GPIO Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html) |  |  |
| 　　[设备树通用输入输出（GPIO） API](../hardware/P290_设备树GPIO宏.md) | [Devicetree GPIO API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html) |  |  |
| 　　　[GPIO 排针接口](../hardware/P291_GPIO排针目录.md) | [GPIO pin headers](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio-pin-headers.html) |  |  |
| 　　　　[ArduCam FFC 40 引脚摄像头连接器](../hardware/P292_ArduCamFFC40针连接器.md) | [ArduCam FFC 40-pin camera connector.](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html) |  |  |
| 　　　　[Arducam DVP 20 引脚连接器](../hardware/P293_ArducamDVP连接器.md) | [Arducam DVP 20-pin connector](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html) |  |  |
| 　　　　[Arduino MKR 排针接口](../hardware/P294_ArduinoMKR排针.md) | [Arduino MKR header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html) |  |  |
| 　　　　[Arduino Mega 排针接口](../hardware/P295_ArduinoMega排针.md) | [Arduino Mega header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html) |  |  |
| 　　　　[Arduino Nano 排针接口](../hardware/P296_ArduinoNano排针.md) | [Arduino Nano header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html) |  |  |
| 　　　　[Arduino Uno（R3）排针接口](../hardware/P297_ArduinoUno排针.md) | [Arduino Uno (R3) header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html) |  |  |
| 　　　　[M.2 Key A 串行存储器连接器](../hardware/P298_M2串行存储器连接器.md) | [M.2 Key A serial memory connector](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html) |  |  |
| 　　　　[Raspberry Pi CSI 连接器](../hardware/P299_树莓派CSI连接器.md) | [Raspberry Pi CSI connector](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html) |  |  |
| 　　　　[ST Morpho 排针接口](../hardware/P300_STMorpho排针.md) | [ST Morpho header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html) |  |  |
| 　　　　[ST Zio 排针接口](../hardware/P301_STZio排针.md) | [ST Zio header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html) |  |  |
| 　　　　[STMod+ 连接器](../hardware/P302_STModPlus连接器.md) | [STMod+ connector](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html) |  |  |
| 　　　　[WisBlock IO 插槽连接器](../hardware/P303_WisBlockIO插槽.md) | [WisBlock IO slot connector](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html) |  |  |
| 　　　　[WisBlock 传感器插槽连接器](../hardware/P304_WisBlock传感器插槽.md) | [WisBlock Sensor Slot connector](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html) |  |  |
| 　　[模拟通用输入输出（GPIO）](../hardware/P273_GPIO模拟接口.md) | [Emulated GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html) |  |  |
| 　　[通用输入输出（GPIO）驱动后端 API](../hardware/P271_GPIO驱动后端.md) | [GPIO Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html) |  |  |
| 　[触觉反馈](../hardware/P147_触觉反馈接口参考.md) | [Haptics](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html) | 0.4.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　[设备专用触觉反馈 API 扩展](../hardware/P150_触觉驱动扩展入口.md) | [Device-specific Haptics API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__ext.html) |  |  |
| 　　　[CS40L26/27](../hardware/P152_CS40L26与CS40L27触觉扩展.md) | [CS40L26/27](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l26__interface.html) |  |  |
| 　　　[CS40L5x](../hardware/P153_CS40L5x触觉扩展.md) | [CS40L5x](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html) |  |  |
| 　　　[DRV2605](../hardware/P154_DRV2605触觉扩展.md) | [DRV2605](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html) |  |  |
| 　　　[TM6605](../hardware/P155_TM6605触觉扩展.md) | [TM6605](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html) |  |  |
| 　　[触觉反馈驱动后端 API](../hardware/P148_触觉驱动后端.md) | [Haptics Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html) |  |  |
| 　硬件信息 | [Hardware Info](../hardware_util_reference/P003_硬件信息公共接口.md) | 1.0.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　[硬件自旋锁](../intercore_reference/P001_硬件自旋锁公共接口.md) | [Hardware Spinlock](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　[硬件自旋锁驱动后端 API](../intercore_reference/P002_硬件自旋锁驱动后端.md) | [Hardware Spinlock Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface__backend.html) |  |  |
| 　[集成电路间总线（I2C）](../hardware/P305_I2C公共接口.md) | [I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[集成电路间总线（I2C）驱动后端 API](../hardware/P311_I2C驱动后端.md) | [I2C Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__interface__backend.html) |  |  |
| 　　[I2C EEPROM 目标设备](../hardware/P313_I2CEEPROM目标接口.md) | [I2C EEPROM Target](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　[集成电路间总线（I2C）模拟接口](../hardware/P314_I2C模拟后端.md) | [I2C Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html) |  |  |
| 　集成电路间音频总线（I2S） | [I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html) | 1.0.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.9.0) |
| 　　集成电路间音频总线（I2S）驱动后端 API | [I2S Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface__backend.html) |  |  |
| 　[改进型集成电路间总线（I3C）](../hardware/P425_I3C公共接口参考.md) | [I3C](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html) | 0.8.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.2.0) |
| 　　[I3C 地址相关辅助代码](../hardware/P383_I3C地址槽管理.md) | [I3C Address-related Helper Code](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html) |  |  |
| 　　[I3C 通用命令码](../hardware/P429_I3C通用命令码参考.md) | [I3C Common Command Codes](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html) |  |  |
| 　　[I3C 设备树相关内容](../hardware/P424_I3C设备树宏.md) | [I3C Devicetree related bits](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html) |  |  |
| 　　[I3C 高数据速率双倍数据率（HDR DDR）API](../hardware/P385_I3C高数据速率双沿模式.md) | [I3C HDR DDR API](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html) |  |  |
| 　　[I3C 带内中断](../hardware/P396_I3C带内中断接口.md) | [I3C In-Band Interrupts](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html) |  |  |
| 　　[I3C 目标设备 API](../hardware/P386_I3C目标设备接口.md) | [I3C Target Device API](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html) |  |  |
| 　　　[I3C 目标设备驱动后端 API](../hardware/P387_I3C目标设备驱动后端.md) | [I3C Target Device Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html) |  |  |
| 　　[I3C 传输 API](../hardware/P394_I3C传输接口.md) | [I3C Transfer API](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html) |  |  |
| 　[处理器间邮箱（IPM）](../intercore_reference/P058_处理器间消息公共接口.md) | [IPM](https://docs.zephyrproject.org/latest/doxygen/html/group__ipm__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[处理器间邮箱（IPM）驱动后端 API](../intercore_reference/P059_处理器间消息驱动后端.md) | [IPM Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__ipm__interface__backend.html) |  |  |
| 　输入 | [Input](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　模拟轴 | [Analog axis](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html) |  |  |
| 　　设备专用输入 API 扩展 | [Device-specific Input API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface__ext.html) |  |  |
| 　　　CY8CMBR3xxx | [CY8CMBR3xxx](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html) |  |  |
| 　　　Nunchuk | [Nunchuk](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html) |  |  |
| 　　　PAT912x | [PAT912x](https://docs.zephyrproject.org/latest/doxygen/html/group__pat912x__interface.html) |  |  |
| 　　　PAW32xx | [PAW32xx](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html) |  |  |
| 　　　PMW3610 | [PMW3610](https://docs.zephyrproject.org/latest/doxygen/html/group__pmw3610__interface.html) |  |  |
| 　　　Renesas RA 电容触摸检测单元（CTSU） | [Renesas RA CTSU](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__ra__ctsu__interface.html) |  |  |
| 　　　Renesas RX 电容触摸检测单元（CTSU） | [Renesas RX CTSU](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html) |  |  |
| 　　输入事件定义 | [Input Event Definitions](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html) |  |  |
| 　　键盘矩阵 | [Keyboard Matrix](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html) |  |  |
| 　　键位映射工具 | [Keymap utilities](https://docs.zephyrproject.org/latest/doxygen/html/group__input__keymap.html) |  |  |
| 　　LVGL 键盘按键 | [LVGL keypad keys](https://docs.zephyrproject.org/latest/doxygen/html/group__lvgl__keypad__dt.html) |  |  |
| 　　触摸屏事件 | [Touchscreen Events](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　虚拟机间共享内存 | [Inter-VM Shared Memory](../intercore_reference/P214_IVSHMEM共享内存接口.md) |  |  |
| 　[发光二极管（LED）](../hardware/P202_LED公共接口.md) | [LED](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　[伪 LED 控制器](../hardware/P207_模拟LED控制器.md) | [Fake LED controller](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html) |  |  |
| 　　[发光二极管（LED）驱动后端 API](../hardware/P205_LED驱动后端接口.md) | [LED Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html) |  |  |
| 　[LED 灯带](../hardware/P208_LED灯带公共接口.md) | [LED Strip](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　[设备专用 LED 灯带 API 扩展](../hardware/P212_LED灯带扩展接口目录.md) | [Device-specific LED Strip API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__ext.html) |  |  |
| 　　　[TLC5971](../hardware/P213_TLC5971灯带扩展.md) | [TLC5971](https://docs.zephyrproject.org/latest/doxygen/html/group__tlc5971__interface.html) |  |  |
| 　　[LED 灯带驱动后端 API](../hardware/P210_LED灯带后端接口.md) | [LED Strip Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html) |  |  |
| 　局部互连网络（LIN） | [LIN](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__interface.html) |  |  |
| 　　LIN 控制器 | [LIN Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　LIN 收发器 | [LIN Transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　LoRa | [LoRa](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html) | 0.9.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.2.0) |
| 　　LoRa 驱动后端 API | [LoRa Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html) |  |  |
| 　[邮箱（MBOX）](../intercore_reference/P014_邮箱驱动公共接口.md) | [MBOX](https://docs.zephyrproject.org/latest/doxygen/html/group__mbox__interface.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[设备树邮箱（MBOX） API](../intercore_reference/P021_邮箱设备树访问宏.md) | [Devicetree MBOX API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-mbox.html) |  |  |
| 　　[邮箱（MBOX）驱动后端 API](../intercore_reference/P015_邮箱驱动后端接口.md) | [MBOX Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__mbox__interface__backend.html) |  |  |
| 　管理数据输入输出（MDIO） | [MDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　管理数据输入输出（MDIO）驱动后端 API | [MDIO Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html) |  |  |
| 　存储器控制器（MEMC） | [MEMC](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　存储器控制器（MEMC）驱动后端 API | [MEMC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html) |  |  |
| 　多线串行外设接口（MSPI） | [MSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html) | 0.9.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　MSPI 配置 API | [MSPI Configure API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html) |  |  |
| 　　　Cadence MSPI 接口 | [Cadence MSPI interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html) |  |  |
| 　　MSPI 设备树相关宏 | [MSPI Devicetree related macros](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html) |  |  |
| 　　多线串行外设接口（MSPI）驱动后端 API | [MSPI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html) |  |  |
| 　　[多线串行外设接口（MSPI）模拟接口](../hardware/P487_MSPI总线仿真接口.md) | [MSPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html) |  |  |
| 　　MSPI 传输 API | [MSPI Transfer API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html) |  |  |
| 　　MSPI 回调 API | [MSPI callback API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html) |  |  |
| 　　MSPI 工具 | [Mspi_util](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html) |  |  |
| 　多路复用器（MUX） | [MUX](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　设备树多路复用器（MUX） API | [Devicetree MUX API](../dt_connection_reference/P007_设备树多路复用器宏.md) |  |  |
| 　杂项设备 | [Miscellaneous Devices](https://docs.zephyrproject.org/latest/doxygen/html/group__misc__interfaces.html) |  |  |
| 　　Coresight STMESP | [Coresight STMESP](../trace_interface_reference/P002_STMESP底层接口.md) |  |  |
| 　　设备多路复用器（Devmux） | [Devmux](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html) |  |  |
| 　　FTDI FT8xx | [FTDI FT8xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html) |  |  |
| 　　　FT8xx 协处理器 | [FT8xx co-processor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html) |  |  |
| 　　　FT8xx 公共函数 | [FT8xx common functions](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html) |  |  |
| 　　　FT8xx 显示列表 | [FT8xx display list](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html) |  |  |
| 　　　FT8xx 存储器映射 | [FT8xx memory map](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html) |  |  |
| 　　　FT8xx 参考 API | [FT8xx reference API](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html) |  |  |
| 　　MAX2221X 杂项接口 | [MAX2221X MISC](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html) |  |  |
| 　　NXP FlexIO | [NXP FlexIO](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html) |  |  |
| 　　Raspberry Pi Pico PIO | [Raspberry Pi Pico PIO](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html) |  |  |
| 　　[Raspberry Pi Pico 邮箱](../intercore_reference/P026_Pico邮箱扩展接口.md) | [Raspberry Pi Pico mailbox](https://docs.zephyrproject.org/latest/doxygen/html/group__mbox__rpi__pico__interface.html) |  |  |
| 　　Renesas ELC | [Renesas ELC](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html) |  |  |
| 　　TMC6460 杂项接口 | [TMC6460 MISC](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html) |  |  |
| 　多功能设备 | [Multi-function Devices](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interfaces.html) |  |  |
| 　　多功能设备 AD559X 接口 | [MFD AD559X interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html) |  |  |
| 　　多功能设备 ADP5360 接口 | [MFD ADP5360 Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　多功能设备 AXP192 接口 | [MFD AXP192 interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html) |  |  |
| 　　多功能设备 BD8LB600FS 接口 | [MFD BD8LB600FS interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html) |  |  |
| 　　多功能设备 Infineon MXCRYPTO 接口 | [MFD Infineon MXCRYPTO interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html) |  |  |
| 　　多功能设备 Infineon MXCRYPTOLITE 接口 | [MFD Infineon MXCRYPTOLITE interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcryptolite.html) |  |  |
| 　　多功能设备 M5PM1 接口 | [MFD M5PM1 Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　多功能设备 MAX22017 接口 | [MFD MAX22017 interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html) |  |  |
| 　　多功能设备 MAX2221X | [MFD MAX2221X](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__max2221x.html) |  |  |
| 　　多功能设备 NPM10XX 接口 | [MFD NPM10XX Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html) | 0.3.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　多功能设备 NPM13XX 接口 | [MFD NPM13XX Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html) |  |  |
| 　　多功能设备 NPM2100 接口 | [MFD NPM2100 Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html) |  |  |
| 　　多功能设备 PCA9422 接口 | [MFD PCA9422 Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html) |  |  |
| 　　多功能设备 TLA2528 接口 | [MFD TLA2528 Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　[非易失性存储器（NVMEM）](../storage/P013_NVMEM接口参考.md) | [NVMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　[NVMEM 设备树辅助接口](../storage/P018_NVMEM设备树辅助宏.md) | [NVMEM Devicetree Helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html) |  |  |
| 　[运算放大器（OPAMP）](../hardware/P091_运算放大器接口参考.md) | [OPAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__opamp__interface.html) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　[运算放大器（OPAMP）驱动后端 API](../hardware/P095_运算放大器驱动后端接口.md) | [OPAMP Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__opamp__interface__backend.html) |  |  |
| 　一次性可编程存储器 | [One Time Programmable Memory](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　一次性可编程存储器（OTP）驱动后端 API | [OTP Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html) |  |  |
| 　　nPM10xx OTP 接口 | [nPM10xx OTP interface](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　PCI Express（PCIe） | [PCIe](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface.html) |  |  |
| 　　PCIe 控制器 | [PCIe Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html) |  |  |
| 　　　PCIe 控制器驱动后端 API | [PCIe Controller Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html) |  |  |
| 　　PCIe 端点驱动后端 API | [PCIe Endpoint Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html) |  |  |
| 　　PCIe 主机 | [PCIe Host](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html) |  |  |
| 　　　PCIe 能力 | [PCIe Capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html) |  |  |
| 　　　PCIe 主机消息信号中断（MSI）接口 | [PCIe Host MSI Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html) |  |  |
| 　　　PCIe 主机精确时间测量（PTM）接口 | [PCIe Host PTM Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html) |  |  |
| 　　　PCIe 虚拟通道主机接口 | [PCIe Virtual Channel Host Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__vc__host__interface.html) |  |  |
| 　平台环境控制接口（PECI） | [PECI](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.1.0) |
| 　　平台环境控制接口（PECI）驱动后端 API | [PECI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html) |  |  |
| 　性能监测单元（PMU） | [PMU](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html) |  |  |
| 　PS/2 | [PS/2](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html) | 0.8.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.1.0) |
| 　　PS/2 驱动后端 API | [PS/2 Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html) |  |  |
| 　外围传感器接口 5（PSI5） | [PSI5](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html) | 0.1.0 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　　外围传感器接口 5（PSI5）驱动后端 API | [PSI5 Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html) |  |  |
| 　精确时间协议（PTP）时钟 | [PTP Clock](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　精确时间协议（PTP）时钟驱动后端 API | [PTP Clock Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html) |  |  |
| 　[脉宽调制（PWM）](../hardware/P255_PWM公共接口.md) | [PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[设备专用脉宽调制（PWM） API 扩展](../hardware/P261_PWM器件扩展目录.md) | [Device-specific PWM API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__ext.html) |  |  |
| 　　　[MAX2221X 脉宽调制](../hardware/P262_MAX2221xPWM扩展.md) | [MAX2221X PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html) |  |  |
| 　　　[MAX31790](../hardware/P263_MAX31790PWM扩展.md) | [MAX31790](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html) |  |  |
| 　　　[WisBlock 脉宽调制](../hardware/P265_WisBlockPWM通道.md) | [WisBlock PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html) |  |  |
| 　　[设备树 PWM API](../hardware/P264_设备树PWM宏.md) | [Devicetree PWMs API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-pwms.html) |  |  |
| 　　[伪脉宽调制（PWM）](../hardware/P260_PWM模拟控制器.md) | [Fake PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html) |  |  |
| 　　[脉宽调制（PWM）驱动后端 API](../hardware/P258_PWM驱动后端接口.md) | [PWM Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html) |  |  |
| 　引脚控制 | [Pin Control](../pinctrl_reference/P001_引脚控制公共接口.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　动态引脚控制 | [Dynamic Pin Control](../pinctrl_reference/P002_动态引脚控制接口.md) |  |  |
| 　　引脚控制 | [Pin control](../pinctrl_reference/P005_引脚控制设备树宏.md) |  |  |
| 　　　Ambiq 引脚控制辅助接口 | [Ambiq pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__ambiq__pinctrl.html) |  |  |
| 　　　　Ambiq Apollo2 引脚控制辅助接口 | [Ambiq Apollo2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo2.html) |  |  |
| 　　　　Ambiq Apollo3 引脚控制辅助接口 | [Ambiq Apollo3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo3.html) |  |  |
| 　　　　Ambiq Apollo4 引脚控制辅助接口 | [Ambiq Apollo4 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html) |  |  |
| 　　　　Ambiq Apollo5 引脚控制辅助接口 | [Ambiq Apollo5 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html) |  |  |
| 　　　Espressif 引脚控制辅助接口 | [Espressif pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__espressif__pinctrl.html) |  |  |
| 　　　　Espressif ESP32 引脚控制辅助接口 | [Espressif ESP32 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32.html) |  |  |
| 　　　　Espressif ESP32C2 引脚控制辅助接口 | [Espressif ESP32C2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c2.html) |  |  |
| 　　　　Espressif ESP32C3 引脚控制辅助接口 | [Espressif ESP32C3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c3.html) |  |  |
| 　　　　Espressif ESP32C5 引脚控制辅助接口 | [Espressif ESP32C5 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c5.html) |  |  |
| 　　　　Espressif ESP32C6 引脚控制辅助接口 | [Espressif ESP32C6 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html) |  |  |
| 　　　　Espressif ESP32C61 引脚控制辅助接口 | [Espressif ESP32C61 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c61.html) |  |  |
| 　　　　Espressif ESP32H2 引脚控制辅助接口 | [Espressif ESP32H2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32h2.html) |  |  |
| 　　　　Espressif ESP32P4 引脚控制辅助接口 | [Espressif ESP32P4 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32p4.html) |  |  |
| 　　　　Espressif ESP32S2 引脚控制辅助接口 | [Espressif ESP32S2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s2.html) |  |  |
| 　　　　Espressif ESP32S3 引脚控制辅助接口 | [Espressif ESP32S3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s3.html) |  |  |
| 　　　FocalTech 引脚控制辅助接口 | [FocalTech pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl.html) |  |  |
| 　　　　FocalTech FT9001 引脚控制辅助接口 | [FocalTech FT9001 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html) |  |  |
| 　　　　　FT9001 IOCTRL 寄存器偏移量 | [FT9001 IOCTRL register offsets](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html) |  |  |
| 　　　Nuvoton 引脚控制辅助接口 | [Nuvoton pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__nuvoton__pinctrl.html) |  |  |
| 　　　　Nuvoton NuMaker M46x 引脚控制辅助接口 | [Nuvoton NuMaker M46x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html) |  |  |
| 　　　Renesas 引脚控制辅助接口 | [Renesas pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__pinctrl.html) |  |  |
| 　　　　Renesas R-Car 引脚控制辅助接口 | [Renesas R-Car pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html) |  |  |
| 　　　　Renesas RA 引脚控制辅助接口 | [Renesas RA pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html) |  |  |
| 　　　　Renesas RA0 引脚控制辅助接口 | [Renesas RA0 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html) |  |  |
| 　　　　Renesas RX 引脚控制辅助接口 | [Renesas RX pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html) |  |  |
| 　　　　Renesas RZ/A 引脚控制辅助接口 | [Renesas RZ/A pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html) |  |  |
| 　　　　Renesas RZ/A2M 引脚控制辅助接口 | [Renesas RZ/A2M pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html) |  |  |
| 　　　　Renesas RZ/G 引脚控制辅助接口 | [Renesas RZ/G pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html) |  |  |
| 　　　　Renesas RZ/N 引脚控制辅助接口 | [Renesas RZ/N pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzn.html) |  |  |
| 　　　　Renesas RZ/T 引脚控制辅助接口 | [Renesas RZ/T pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html) |  |  |
| 　　　　Renesas RZ/V 引脚控制辅助接口 | [Renesas RZ/V pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html) |  |  |
| 　　　SiFli 引脚控制辅助接口 | [SiFli pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__sifli__pinctrl.html) |  |  |
| 　　　　SiFli SF32LB52x 引脚控制辅助接口 | [SiFli SF32LB52x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html) |  |  |
| 　　　Silicon Labs 引脚控制辅助接口 | [Silicon Labs pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__silabs__pinctrl.html) |  |  |
| 　　　　Silicon Labs SiWx91x 引脚控制辅助接口 | [Silicon Labs SiWx91x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html) |  |  |
| 　　　　Silicon Labs Six301 引脚控制辅助接口 | [Silicon Labs Six301 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html) |  |  |
| 　　　　Silicon Labs xG21 引脚控制辅助接口 | [Silicon Labs xG21 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg21.html) |  |  |
| 　　　　Silicon Labs xG22 引脚控制辅助接口 | [Silicon Labs xG22 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg22.html) |  |  |
| 　　　　Silicon Labs xG23 引脚控制辅助接口 | [Silicon Labs xG23 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg23.html) |  |  |
| 　　　　Silicon Labs xG24 引脚控制辅助接口 | [Silicon Labs xG24 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg24.html) |  |  |
| 　　　　Silicon Labs xG26 引脚控制辅助接口 | [Silicon Labs xG26 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg26.html) |  |  |
| 　　　　Silicon Labs xG27 引脚控制辅助接口 | [Silicon Labs xG27 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg27.html) |  |  |
| 　　　　Silicon Labs xG28 引脚控制辅助接口 | [Silicon Labs xG28 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html) |  |  |
| 　　　　Silicon Labs xG29 引脚控制辅助接口 | [Silicon Labs xG29 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg29.html) |  |  |
| 　　　WCH CH32H41x 引脚控制辅助接口 | [WCH CH32H41x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html) |  |  |
| 　脉冲输入输出 | [Pulse IO](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　QEMU 固件配置（fw_cfg） | [QEMU fw_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　[实时时钟（RTC）](../timer_reference/P009_实时时钟公共接口.md) | [RTC](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__interface.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　[设备专用实时时钟（RTC） API 扩展](../timer_reference/P015_实时时钟器件扩展入口.md) | [Device-specific RTC API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__interface__ext.html) |  |  |
| 　　[伪实时时钟（RTC）](../hardware/P497_RTC伪设备接口.md) | [Fake RTC](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__fake.html) |  |  |
| 　　[实时时钟（RTC）驱动后端 API](../timer_reference/P010_实时时钟驱动后端接口.md) | [RTC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__interface__backend.html) |  |  |
| 　[稳压器](../power/P073_稳压器接口.md) | [Regulator](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |
| 　　[设备树稳压器 API](../power/P081_设备树稳压器辅助接口目录.md) | [Devicetree Regulator API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-regulator.html) |  |  |
| 　　　[ADP5360 设备树辅助接口](../power/P085_ADP5360稳压器设备树辅助接口.md) | [ADP5360 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__adp5360.html) |  |  |
| 　　　[AXP192 设备树辅助接口](../power/P086_AXP192稳压器设备树辅助接口.md) | [AXP192 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__axp192.html) |  |  |
| 　　　[MAX20335 设备树辅助接口](../power/P087_MAX20335稳压器设备树辅助接口.md) | [MAX20335 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__max20335.html) |  |  |
| 　　　[MAX20362 设备树辅助接口](../power/P088_MAX20362稳压器设备树辅助接口.md) | [MAX20362 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__max20362.html) |  |  |
| 　　　[MSPM0 VREF 设备树辅助接口](../power/P089_MSPM0参考电压设备树辅助接口.md) | [MSPM0 VREF Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__mspm0__vref.html) |  |  |
| 　　　[NXP VREF 设备树辅助接口](../power/P090_NXP参考电压设备树辅助接口.md) | [NXP VREF Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nxp__vref.html) |  |  |
| 　　　[Raspberry Pi Pico 稳压器设备树辅助接口](../power/P091_RaspberryPi_Pico稳压器设备树辅助接口.md) | [Raspberry Pi Pico regulator Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__rpi__pico.html) |  |  |
| 　　　[Silicon Labs DCDC 设备树辅助接口](../power/P092_SiliconLabs_DCDC设备树辅助接口.md) | [Silicon Labs DCDC Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__silabs__dcdc.html) |  |  |
| 　　　[Texas Instruments TPS6287x 设备树辅助接口](../power/P093_TPS6287x稳压器设备树辅助接口.md) | [Texas Instruments TPS6287x Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__ti__tps6287x.html) |  |  |
| 　　　[nPM10xx 设备树辅助接口](../power/P094_nPM10xx稳压器设备树辅助接口.md) | [nPM10xx Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html) |  |  |
| 　　　[nPM1100 设备树辅助接口](../power/P095_nPM1100稳压器设备树辅助接口.md) | [nPM1100 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm1100.html) |  |  |
| 　　　[nPM13xx 设备树辅助接口](../power/P096_nPM13xx稳压器设备树辅助接口.md) | [nPM13xx Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html) |  |  |
| 　　　[nPM2100 设备树辅助接口](../power/P097_nPM2100稳压器设备树辅助接口.md) | [nPM2100 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm2100.html) |  |  |
| 　　　[nPM6001 设备树辅助接口](../power/P098_nPM6001稳压器设备树辅助接口.md) | [nPM6001 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm6001.html) |  |  |
| 　　　[nRF5X 设备树辅助接口](../power/P099_nRF5X稳压器设备树辅助接口.md) | [nRF5X Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html) |  |  |
| 　　[伪稳压器](../hardware/P498_稳压器伪设备接口.md) | [Fake regulator](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html) |  |  |
| 　　[稳压器驱动后端 API](../power/P077_稳压器驱动后端接口.md) | [Regulator Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html) |  |  |
| 　　[稳压器父设备接口](../power/P074_父级稳压器接口.md) | [Regulator Parent Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__interface.html) |  |  |
| 　　　[MAX20362 API](../power/P083_MAX20362父级控制接口.md) | [MAX20362 API](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html) |  |  |
| 　　　[PCA9420 工具](../power/P084_PCA9420父级控制接口.md) | [PCA9420 Utilities.](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__pca9420.html) |  |  |
| 　复位控制器 | [Reset Controller](../reset_reference/P001_复位控制器公共接口.md) | 0.2.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　CH32 复位控制器辅助接口 | [CH32 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__ch32.html) |  |  |
| 　　设备树复位控制器 API | [Devicetree Reset Controller API](../reset_reference/P007_复位控制器设备树辅助宏.md) |  |  |
| 　　FocalTech FT9001 复位控制器辅助接口 | [FocalTech FT9001 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__focaltech__ft9001.html) |  |  |
| 　　　FocalTech 复位控制模块寄存器 | [FocalTech Reset Control Module Registers](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html) |  |  |
| 　　　FocalTech 复位使能／禁用定义 | [FocalTech Reset Enable/Disable Definitions](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__enables.html) |  |  |
| 　　　　AHB3RSTCR 复位控制 | [AHB3RSTCR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ahb3rstcr__resets.html) |  |  |
| 　　　　ARITHRSTCR 复位控制 | [ARITHRSTCR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__arithrstcr__resets.html) |  |  |
| 　　　　EPORTRSTR 复位控制 | [EPORTRSTR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__eportrstr__resets.html) |  |  |
| 　　　　IPSRSTCR 复位控制 | [IPSRSTCR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ipsrstcr__resets.html) |  |  |
| 　　　　MULTIRSTCR 复位控制 | [MULTIRSTCR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__multirstcr__resets.html) |  |  |
| 　　　　SYSRSTCR 复位控制 | [SYSRSTCR Reset Control](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__sysrstcr__resets.html) |  |  |
| 　　GigaDevice 复位控制器辅助接口 | [GigaDevice reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gigadevice.html) |  |  |
| 　　　GigaDevice GD32A50x 复位控制器辅助接口 | [GigaDevice GD32A50x reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32a50x.html) |  |  |
| 　　　GigaDevice GD32E10x 复位控制器辅助接口 | [GigaDevice GD32E10x reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32e10x.html) |  |  |
| 　　　GigaDevice GD32E50x 复位控制器辅助接口 | [GigaDevice GD32E50x reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32e50x.html) |  |  |
| 　　　GigaDevice GD32F3x0 复位控制器辅助接口 | [GigaDevice GD32F3x0 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f3x0.html) |  |  |
| 　　　GigaDevice GD32F403 复位控制器辅助接口 | [GigaDevice GD32F403 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f403.html) |  |  |
| 　　　GigaDevice GD32F4xx 复位控制器辅助接口 | [GigaDevice GD32F4xx reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f4xx.html) |  |  |
| 　　　GigaDevice GD32L23x 复位控制器辅助接口 | [GigaDevice GD32L23x reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32l23x.html) |  |  |
| 　　　GigaDevice GD32VF103 复位控制器辅助接口 | [GigaDevice GD32VF103 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32vf103.html) |  |  |
| 　　Nuvoton M48X 复位控制器设备树辅助接口 | [Nuvoton M48X Reset controller Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m48x.html) |  |  |
| 　　Nuvoton NuMaker 复位控制器辅助接口 | [Nuvoton NuMaker reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__numaker.html) |  |  |
| 　　　Nuvoton NuMaker M031X 复位控制器辅助接口 | [Nuvoton NuMaker M031X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m031x.html) |  |  |
| 　　　Nuvoton NuMaker M2L31X 复位控制器辅助接口 | [Nuvoton NuMaker M2L31X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m2l31x.html) |  |  |
| 　　　Nuvoton NuMaker M333X 复位控制器辅助接口 | [Nuvoton NuMaker M333X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m333x.html) |  |  |
| 　　　Nuvoton NuMaker M335X 复位控制器辅助接口 | [Nuvoton NuMaker M335X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m335x.html) |  |  |
| 　　　Nuvoton NuMaker M46X 复位控制器辅助接口 | [Nuvoton NuMaker M46X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m46x.html) |  |  |
| 　　　Nuvoton NuMaker M55M1X 复位控制器辅助接口 | [Nuvoton NuMaker M55M1X reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m55m1x.html) |  |  |
| 　　Raspberry Pi RP2040 复位控制器辅助接口 | [Raspberry Pi RP2040 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2040.html) |  |  |
| 　　Raspberry Pi RP2350 复位控制器辅助接口 | [Raspberry Pi RP2350 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2350.html) |  |  |
| 　　复位控制器驱动后端 API | [Reset Controller Driver Backend API](../reset_reference/P002_复位控制器驱动后端.md) |  |  |
| 　　STM32 复位控制器辅助接口 | [STM32 reset controller helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__stm32.html) |  |  |
| 　[保持存储器](../hardware/P630_保留内存接口.md) | [Retained memory](https://docs.zephyrproject.org/latest/doxygen/html/group__retained__mem__interface.html) | 1.0.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　[保持存储器驱动后端 API](../hardware/P631_保留内存驱动接口.md) | [Retained Memory Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__retained__mem__interface__backend.html) |  |  |
| 　系统控制和管理接口（SCMI） | [SCMI](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html) |  |  |
| 　　协议 | [Protocols](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__protocols.html) |  |  |
| 　　　基础协议 | [Base Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html) |  |  |
| 　　　时钟协议 | [Clock Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html) |  |  |
| 　　　NXP CPU 域协议 | [NXP CPU Domain Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html) |  |  |
| 　　　NXP 系统电源协议 | [NXP System Power Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__system.html) |  |  |
| 　　　引脚控制协议 | [Pin Control Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html) |  |  |
| 　　　电源域协议 | [Power Domain Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html) |  |  |
| 　　　复位域管理协议 | [Reset domain management Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html) |  |  |
| 　　　系统电源协议 | [System Power Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html) |  |  |
| 　　传输 | [Transport](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html) |  |  |
| 　　　共享内存 | [Shared Memory](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html) |  |  |
| 　　工具 | [Utilities](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html) |  |  |
| 　SD 主机控制器（SDHC） | [SDHC](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html) | 0.8.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　SD 主机控制器（SDHC）驱动后端 API | [SDHC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface__backend.html) |  |  |
| 　单边沿半字节传输（SENT） | [SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html) | 0.1.0 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　　单边沿半字节传输（SENT）驱动后端 API | [SENT Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html) |  |  |
| 　系统管理总线（SMBus） | [SMBus](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　系统管理总线（SMBus）驱动后端 API | [SMBus Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html) |  |  |
| 　[串行外设接口（SPI）](../hardware/P318_SPI公共接口.md) | [SPI](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html) | 1.1.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[设备树串行外设接口（SPI） API](../hardware/P329_SPI设备树宏.md) | [Devicetree SPI API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-spi.html) |  |  |
| 　　[串行外设接口（SPI）驱动后端 API](../hardware/P324_SPI驱动后端接口.md) | [SPI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html) |  |  |
| 　　[串行外设接口（SPI）模拟接口](../hardware/P326_SPI模拟接口.md) | [SPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html) |  |  |
| 　串行线调试端口（SWDP） | [SWDP](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　传感器 | [Sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.2.0) |
| 　　电池 API | [Battery APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html) |  |  |
| 　　设备专用传感器 API 扩展与设备树常量 | [Device-specific Sensor API extensions and Devicetree constants.](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext.html) |  |  |
| 　　　1-Wire 传感器 API | [1-Wire Sensor API](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html) |  |  |
| 　　　AMS | [AMS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ams.html) |  |  |
| 　　　　TCS3400 | [TCS3400](https://docs.zephyrproject.org/latest/doxygen/html/group__tcs3400__interface.html) |  |  |
| 　　　Analog Devices | [Analog Devices](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__adi.html) |  |  |
| 　　　　ADLTC2990 | [ADLTC2990](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html) |  |  |
| 　　　　ADT7420 | [ADT7420](https://docs.zephyrproject.org/latest/doxygen/html/group__adt7420__interface.html) |  |  |
| 　　　　ADXL313 | [ADXL313](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl313__interface.html) |  |  |
| 　　　　ADXL345 | [ADXL345](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl345__interface.html) |  |  |
| 　　　　ADXL355 | [ADXL355](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl355__interface.html) |  |  |
| 　　　　ADXL362 | [ADXL362](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl362__interface.html) |  |  |
| 　　　　ADXL367 | [ADXL367](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html) |  |  |
| 　　　　ADXL372 | [ADXL372](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html) |  |  |
| 　　　　MAX17055 | [MAX17055](https://docs.zephyrproject.org/latest/doxygen/html/group__max17055__interface.html) |  |  |
| 　　　　MAX30009 | [MAX30009](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html) |  |  |
| 　　　　MAX30210 | [MAX30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html) |  |  |
| 　　　　MAX31790 | [MAX31790](https://docs.zephyrproject.org/latest/doxygen/html/group__max31790__interface.html) |  |  |
| 　　　　MAX32664C | [MAX32664C](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html) |  |  |
| 　　　Angst+Pfister | [Angst+Pfister](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ap.html) |  |  |
| 　　　　FCX-MLDX5 | [FCX-MLDX5](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html) |  |  |
| 　　　Avago Technologies | [Avago Technologies](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__avago.html) |  |  |
| 　　　　APDS9253 | [APDS9253](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9253__interface.html) |  |  |
| 　　　　APDS9960 | [APDS9960](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html) |  |  |
| 　　　Avia Semiconductor | [Avia Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__avia.html) |  |  |
| 　　　　HX711 | [HX711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html) |  |  |
| 　　　Bosch Sensortec | [Bosch Sensortec](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__bosch.html) |  |  |
| 　　　　BMM350 | [BMM350](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html) |  |  |
| 　　　　BMP581 | [BMP581](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html) |  |  |
| 　　　Broadcom | [Broadcom](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__brcm.html) |  |  |
| 　　　　AFBR-S50 | [AFBR-S50](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html) |  |  |
| 　　　MCUX 增强型正交解码器（EQDC） | [EQDC MCUX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html) |  |  |
| 　　　Festo | [Festo](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__festo.html) |  |  |
| 　　　　VEAA X-3 | [VEAA X-3](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html) |  |  |
| 　　　Fintek | [Fintek](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__fintek.html) |  |  |
| 　　　　F75303 | [F75303](https://docs.zephyrproject.org/latest/doxygen/html/group__f75303__interface.html) |  |  |
| 　　　Gas Sensing Solutions | [Gas Sensing Solutions](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__gss.html) |  |  |
| 　　　　ExplorIR-M | [ExplorIR-M](https://docs.zephyrproject.org/latest/doxygen/html/group__explorir__m__interface.html) |  |  |
| 　　　Hangzhou Grow | [Hangzhou Grow](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__hzgrow.html) |  |  |
| 　　　　Grow R502A | [Grow R502A](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html) |  |  |
| 　　　ITE | [ITE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ite.html) |  |  |
| 　　　　IT51XXX 转速计 | [IT51XXX tachometer](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__tach__interface.html) |  |  |
| 　　　　IT8XXX2 转速计 | [IT8XXX2 tachometer](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__tach__interface.html) |  |  |
| 　　　　IT8XXX2 电压比较器 | [IT8XXX2 voltage comparator](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__vcmp__interface.html) |  |  |
| 　　　Iclegend | [Iclegend](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__iclegend.html) |  |  |
| 　　　　Iclegend S3KM1110 | [Iclegend S3KM1110](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html) |  |  |
| 　　　Infineon | [Infineon](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__infineon.html) |  |  |
| 　　　　TLE9104 | [TLE9104](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html) |  |  |
| 　　　LTC4286 | [LTC4286](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html) |  |  |
| 　　　MEMSIC | [MEMSIC](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__memsic.html) |  |  |
| 　　　　MC3419 | [MC3419](https://docs.zephyrproject.org/latest/doxygen/html/group__mc3419__interface.html) |  |  |
| 　　　　MMC56X3 | [MMC56X3](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html) |  |  |
| 　　　Measurement Specialties | [Measurement Specialties](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__meas.html) |  |  |
| 　　　　HTU31D | [HTU31D](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html) |  |  |
| 　　　Melexis | [Melexis](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__melexis.html) |  |  |
| 　　　　MLX90394 | [MLX90394](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html) |  |  |
| 　　　Microchip | [Microchip](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__microchip.html) |  |  |
| 　　　　MCP9600 | [MCP9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html) |  |  |
| 　　　　MTCH9010 | [MTCH9010](https://docs.zephyrproject.org/latest/doxygen/html/group__mtch9010__interface.html) |  |  |
| 　　　　PAC194X | [PAC194X](https://docs.zephyrproject.org/latest/doxygen/html/group__pac194x__interface.html) |  |  |
| 　　　NXP | [NXP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nxp.html) |  |  |
| 　　　　MCUX 正交解码器（QDEC） | [QDEC MCUX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__qdec__mcux.html) |  |  |
| 　　　　NXP S32 正交解码器（QDEC） | [QDEC NXP S32](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nxp__s32__interface.html) |  |  |
| 　　　National Semiconductor | [National Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__national.html) |  |  |
| 　　　　LM95234 | [LM95234](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html) |  |  |
| 　　　Nordic Semiconductor | [Nordic Semiconductor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nordic.html) |  |  |
| 　　　　nRF 正交解码器（QDEC） | [QDEC nRF](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nrf__interface.html) |  |  |
| 　　　　nPM10xx 传感器接口 | [nPM10xx Sensor interface](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html) |  |  |
| 　　　Nuvoton | [Nuvoton](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__nuvoton.html) |  |  |
| 　　　　NPCX 转速计 | [NPCX tachometer](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html) |  |  |
| 　　　PNI | [PNI](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__pni.html) |  |  |
| 　　　　RM3100 | [RM3100](https://docs.zephyrproject.org/latest/doxygen/html/group__rm3100__interface.html) |  |  |
| 　　　Phosense | [Phosense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__phosense.html) |  |  |
| 　　　　XBR818 | [XBR818](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html) |  |  |
| 　　　PixArt | [PixArt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__pixart.html) |  |  |
| 　　　　PAJ7620 | [PAJ7620](https://docs.zephyrproject.org/latest/doxygen/html/group__paj7620__interface.html) |  |  |
| 　　　　PAT9136 | [PAT9136](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html) |  |  |
| 　　　ROHM | [ROHM](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__rohm.html) |  |  |
| 　　　　BD8LB600FS | [BD8LB600FS](https://docs.zephyrproject.org/latest/doxygen/html/group__bd8lb600fs__interface.html) |  |  |
| 　　　Realtek | [Realtek](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__realtek.html) |  |  |
| 　　　　Realtek Bee 正交解码器（QDEC） | [Realtek Bee QDEC](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html) |  |  |
| 　　　S9706 | [S9706](https://docs.zephyrproject.org/latest/doxygen/html/group__s9706__interface.html) |  |  |
| 　　　STMicroelectronics | [STMicroelectronics](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__st.html) |  |  |
| 　　　　IIS2DLPC | [IIS2DLPC](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2dlpc__interface.html) |  |  |
| 　　　　IIS2ICLX | [IIS2ICLX](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2iclx__interface.html) |  |  |
| 　　　　IIS3DWB | [IIS3DWB](https://docs.zephyrproject.org/latest/doxygen/html/group__iis3dwb__interface.html) |  |  |
| 　　　　ISM330DHCX | [ISM330DHCX](https://docs.zephyrproject.org/latest/doxygen/html/group__ism330dhcx__interface.html) |  |  |
| 　　　　ISM6HG256X | [ISM6HG256X](https://docs.zephyrproject.org/latest/doxygen/html/group__ism6hg256x__interface.html) |  |  |
| 　　　　LIS2DE12 | [LIS2DE12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2de12__interface.html) |  |  |
| 　　　　LIS2DH | [LIS2DH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html) |  |  |
| 　　　　LIS2DS12 | [LIS2DS12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2ds12__interface.html) |  |  |
| 　　　　LIS2DU12 | [LIS2DU12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2du12__interface.html) |  |  |
| 　　　　LIS2DUX12 | [LIS2DUX12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dux12__interface.html) |  |  |
| 　　　　LIS2DW12 | [LIS2DW12](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html) |  |  |
| 　　　　LPS22HH | [LPS22HH](https://docs.zephyrproject.org/latest/doxygen/html/group__lps22hh__interface.html) |  |  |
| 　　　　LPS2xDF | [LPS2xDF](https://docs.zephyrproject.org/latest/doxygen/html/group__lps2xdf__interface.html) |  |  |
| 　　　　LSM6DSO | [LSM6DSO](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso__interface.html) |  |  |
| 　　　　LSM6DSO16IS | [LSM6DSO16IS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso16is__interface.html) |  |  |
| 　　　　LSM6DSV16X | [LSM6DSV16X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv16x__interface.html) |  |  |
| 　　　　LSM6DSV320X | [LSM6DSV320X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv320x__interface.html) |  |  |
| 　　　　LSM6DSV32X | [LSM6DSV32X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv32x__interface.html) |  |  |
| 　　　　LSM6DSV80X | [LSM6DSV80X](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv80x__interface.html) |  |  |
| 　　　　LSM6DSVXXX | [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html) |  |  |
| 　　　　LSM9DS1 | [LSM9DS1](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html) |  |  |
| 　　　　STM32 正交解码器（QDEC） | [QDEC STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__stm32__interface.html) |  |  |
| 　　　　STTS22H | [STTS22H](https://docs.zephyrproject.org/latest/doxygen/html/group__stts22h__interface.html) |  |  |
| 　　　　VL53L0X | [VL53L0X](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html) |  |  |
| 　　　ScioSense | [ScioSense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__sciosense.html) |  |  |
| 　　　　ENS160 | [ENS160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html) |  |  |
| 　　　Sensirion | [Sensirion](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__sensirion.html) |  |  |
| 　　　　SCD4X | [SCD4X](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html) |  |  |
| 　　　　SGP40 | [SGP40](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html) |  |  |
| 　　　　SHT4X | [SHT4X](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html) |  |  |
| 　　　　STCC4 | [STCC4](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html) |  |  |
| 　　　传感器坐标轴对齐 | [Sensor axis alignment](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__axis__align__interface.html) |  |  |
| 　　　TDK InvenSense | [TDK InvenSense](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__tdk.html) |  |  |
| 　　　　ICM42686 | [ICM42686](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html) |  |  |
| 　　　　ICM42688 | [ICM42688](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html) |  |  |
| 　　　　ICM4268X | [ICM4268X](https://docs.zephyrproject.org/latest/doxygen/html/group__icm4268x__interface.html) |  |  |
| 　　　　ICM45686 | [ICM45686](https://docs.zephyrproject.org/latest/doxygen/html/group__icm45686__interface.html) |  |  |
| 　　　　ICM566xx | [ICM566xx](https://docs.zephyrproject.org/latest/doxygen/html/group__icm566xx__interface.html) |  |  |
| 　　　Texas Instruments | [Texas Instruments](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__ti.html) |  |  |
| 　　　　BQ274XX | [BQ274XX](https://docs.zephyrproject.org/latest/doxygen/html/group__bq274xx__interface.html) |  |  |
| 　　　　FDC2X1X | [FDC2X1X](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html) |  |  |
| 　　　　INA226 | [INA226](https://docs.zephyrproject.org/latest/doxygen/html/group__ina226__interface.html) |  |  |
| 　　　　INA230 | [INA230](https://docs.zephyrproject.org/latest/doxygen/html/group__ina230__interface.html) |  |  |
| 　　　　INA237 | [INA237](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html) |  |  |
| 　　　　INA2XX | [INA2XX](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html) |  |  |
| 　　　　TMAG5273 | [TMAG5273](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html) |  |  |
| 　　　　TMP114 | [TMP114](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp114__interface.html) |  |  |
| 　　　　TMP11X | [TMP11X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html) |  |  |
| 　　　　TMP451 | [TMP451](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html) |  |  |
| 　　　Vishay | [Vishay](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__vishay.html) |  |  |
| 　　　　VEML6031 | [VEML6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html) |  |  |
| 　　　　VEML6046 | [VEML6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html) |  |  |
| 　　　　VEML60XX | [VEML60XX](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html) |  |  |
| 　　　Winsen | [Winsen](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__winsen.html) |  |  |
| 　　　　MH-Z19B | [MH-Z19B](https://docs.zephyrproject.org/latest/doxygen/html/group__mhz19b__interface.html) |  |  |
| 　　　Wurth Elektronik | [Wurth Elektronik](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__we.html) |  |  |
| 　　　　WSEN-PADS-2511020213301 | [WSEN-PADS-2511020213301](https://docs.zephyrproject.org/latest/doxygen/html/group__wsen__pads__2511020213301__interface.html) |  |  |
| 　　　　WSEN-TIDS-2521020222501 | [WSEN-TIDS-2521020222501](https://docs.zephyrproject.org/latest/doxygen/html/group__wsen__tids__2521020222501__interface.html) |  |  |
| 　　　Zephyr | [Zephyr](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__ext__zephyr.html) |  |  |
| 　　　　[通用传感器模拟器](../hardware/P496_通用传感器仿真接口.md) | [Generic Sensor Emulator](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html) |  |  |
| 　　传感器驱动后端 API | [Sensor Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html) |  |  |
| 　　[传感器模拟器后端 API](../hardware/P494_传感器仿真后端接口.md) | [Sensor emulator backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html) |  |  |
| 　[步进电机](../hardware/P229_步进电机接口目录.md) | [Stepper](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__interface.html) |  |  |
| 　　[设备专用步进电机 API 扩展](../hardware/P237_步进器件扩展目录.md) | [Device-specific stepper API extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__interface__ext.html) |  |  |
| 　　　[DRV84XX 步进电机控制器](../hardware/P238_DRV84XX步进扩展.md) | [DRV84XX Stepper Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html) |  |  |
| 　　　[TMCM-3216 步进电机控制器](../hardware/P239_TMCM3216步进扩展.md) | [TMCM-3216 Stepper Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html) |  |  |
| 　　　[Trinamic 步进电机控制器](../hardware/P240_Trinamic步进扩展.md) | [Trinamic Stepper Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html) | 0.9.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　[步进电机硬件驱动](../hardware/P232_步进硬件驱动接口.md) | [Stepper Hardware Driver](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html) | 0.9.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　[步进电机硬件驱动后端 API](../hardware/P235_步进硬件驱动后端.md) | [Stepper Hardware Driver Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html) |  |  |
| 　　[步进电机运动控制器](../hardware/P230_步进运动控制接口.md) | [Stepper Motion Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html) | 0.9.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　[步进电机运动控制器驱动后端 API](../hardware/P233_步进运动控制后端.md) | [Stepper Motion Controller Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html) |  |  |
| 　系统控制（SYSCON） | [System control (SYSCON)](../syscon_reference/P001_系统控制器公共接口.md) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　系统控制（SYSCON）驱动后端 API | [SYSCON Driver Backend API](../syscon_reference/P002_系统控制器驱动后端.md) |  |  |
| 　可信执行环境（TEE） | [TEE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　可信执行环境（TEE）驱动后端 API | [TEE Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html) |  |  |
| 　时间感知 GPIO | [Time-aware GPIO](../timer_reference/P191_时间感知GPIO公共接口.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　时间感知 GPIO 驱动后端 API | [Time-aware GPIO Driver Backend API](../timer_reference/P192_时间感知GPIO驱动后端.md) |  |  |
| 　[通用异步收发器（UART）](../hardware/P330_UART公共接口.md) | [UART](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html) | 2.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[异步 UART API](../hardware/P334_UART异步接口.md) | [Async UART API](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html) | 1.0.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　[中断驱动 UART API](../hardware/P333_UART中断驱动接口.md) | [Interrupt-driven UART API](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html) |  |  |
| 　　[轮询 UART API](../hardware/P332_UART轮询接口.md) | [Polling UART API](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html) |  |  |
| 　　[通用异步收发器（UART）模拟接口](../hardware/P341_UART模拟接口.md) | [UART Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html) |  |  |
| 　通用串行总线（USB） | [USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__interfaces.html) |  |  |
| 　　电池充电（BC1.2） | [Battery Charging (BC1.2)](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html) |  |  |
| 　　　[BC1.2 后端模拟器 API](../hardware/P491_BC1点2仿真后端接口.md) | [BC1.2 backed emulator APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html) |  |  |
| 　　USB 设备控制器 | [USB Device Controller](../usb/P030_USB设备控制器API.md) | 0.1.1 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　USB 主机控制器 | [USB Host Controller](../usb/P073_USB主机控制器API.md) | 0.1.1 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　USB Type-C | [USB Type-C](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html) |  |  |
| 　　　USB 电力传输（USB PD） | [USB Power Delivery](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html) |  |  |
| 　　　　USB 电力传输电源数据对象 | [USB Power Delivery Power Data Objects](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html) |  |  |
| 　　　USB Type-C 端口控制器 API | [USB Type-C Port Controller API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html) | 0.1.1 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　　　USB Type-C 端口控制器驱动后端 API | [USB Type-C Port Controller Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html) |  |  |
| 　　　USB Type-C 电源路径控制器 | [USB Type-C Power Path Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html) |  |  |
| 　　　　USB Type-C 电源路径控制器驱动后端 API | [USB Type-C Power Path Controller Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller__backend.html) |  |  |
| 　　　USB-C VBUS API | [USB-C VBUS API](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　　USB-C VBUS 驱动后端 API | [USB-C VBUS Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api__backend.html) |  |  |
| 　[虚拟 I/O（VIRTIO）](../hardware/P571_VirtIO设备接口.md) | [VIRTIO](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html) | 0.1.0 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　　[虚拟 I/O（VIRTIO）驱动后端 API](../hardware/P580_VirtIO驱动后端接口.md) | [VIRTIO Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html) |  |  |
| 　　[虚拟队列接口](../hardware/P572_VirtIO虚拟队列接口.md) | [Virtqueue Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html) |  |  |
| 　视频驱动 | [Video Drivers](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html) | 1.3.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.1.0) |
| 　　视频控制项 | [Video Controls](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html) |  |  |
| 　　视频驱动后端 API | [Video Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html) |  |  |
| 　　视频接口总线类型 | [Video interface bus types](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__bus__types.html) |  |  |
| 　唤醒控制器（WUC） | [WUC](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　设备树唤醒控制器 API | [Devicetree WUC Controller API](../dt_irq_reference/P005_设备树唤醒控制器宏.md) |  |  |
| 　　唤醒控制器（WUC）驱动后端 API | [WUC Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html) |  |  |
| 　[看门狗](../timer_reference/P001_看门狗公共接口.md) | [Watchdog](https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　[看门狗驱动后端 API](../timer_reference/P002_看门狗驱动后端接口.md) | [Watchdog Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface__backend.html) |  |  |

### 2.2.2\_设备模型（Device Model）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 设备模型 | [Device Model](../device_reference/P001_设备模型公共接口.md) | 1.1.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　设备内存映射 I/O 管理 | [Device memory-mapped IO management](../device_reference/P011_设备MMIO管理概述.md) |  |  |
| 　　命名 MMIO 区域宏 | [Named MMIO region macros](../device_reference/P013_设备命名区域MMIO.md) |  |  |
| 　　单一 MMIO 区域宏 | [Single MMIO region macros](../device_reference/P012_设备单区域MMIO.md) |  |  |
| 　　顶层 MMIO 区域宏 | [Top-level MMIO region macros](../device_reference/P014_顶层MMIO区域.md) |  |  |
| 　EM32 时钟门控标识符 | [EM32 Clock Gating IDs](https://docs.zephyrproject.org/latest/doxygen/html/group__em32__clock__gating__ids.html) |  |  |

### 2.2.3\_设备树（Devicetree）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 设备树 | [Devicetree](../dt_overview_reference/P001_设备树API总览.md) | 1.2.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.2.0) |
| 　逐项遍历宏 | [“For-each” macros](../dt_foreach_reference/P001_设备树遍历宏.md) |  |  |
| 　总线辅助接口 | [Bus helpers](../dt_node_reference/P001_设备树总线查询宏.md) |  |  |
| 　选定节点 | [Chosen nodes](../dt_node_reference/P002_设备树chosen节点宏.md) |  |  |
| 　依赖跟踪 | [Dependency tracking](../dt_node_reference/P004_设备树依赖顺序宏.md) |  |  |
| 　[设备树控制器局域网（CAN） API](../hardware/P373_CAN设备树宏.md) | [Devicetree CAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-can.html) |  |  |
| 　[设备树时钟 API](../timer_reference/P107_设备树时钟获取宏.md) | [Devicetree Clocks API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html) |  |  |
| 　　Aesc Silicon 时钟域标识符 | [Aesc Silicon clock domain identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html) |  |  |
| 　　FocalTech FT9001 时钟标识符 | [FocalTech FT9001 clock identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html) |  |  |
| 　　Microchip SmartFusion2 时钟标识符 | [Microchip SmartFusion2 clock identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__microchip__smartfusion2__clocks.html) |  |  |
| 　　NXP i.MX952 时钟源 | [NXP i.MX952 Clock Sources](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html) |  |  |
| 　　　外设时钟（41–163） | [Peripheral Clocks (41-163)](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html) |  |  |
| 　[设备树计数器捕获 API](../timer_reference/P034_计数器捕获设备树宏.md) | [Devicetree Counter Captures API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-counter-captures.html) |  |  |
| 　设备树直接存储器访问（DMA） API | [Devicetree DMA API](../dma_reference/P008_DMA设备树宏.md) |  |  |
| 　[设备树显示 API](../hardware/P227_设备树显示接口.md) | [Devicetree Display API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-display.html) |  |  |
| 　设备树固定分区 API | [Devicetree Fixed Partition API](../dt_partition_reference/P002_设备树固定分区宏.md) |  |  |
| 　[设备树通用输入输出（GPIO） API](../hardware/P290_设备树GPIO宏.md) | [Devicetree GPIO API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html) |  |  |
| 　　[GPIO 排针接口](../hardware/P291_GPIO排针目录.md) | [GPIO pin headers](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio-pin-headers.html) |  |  |
| 　　　[ArduCam FFC 40 引脚摄像头连接器](../hardware/P292_ArduCamFFC40针连接器.md) | [ArduCam FFC 40-pin camera connector.](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html) |  |  |
| 　　　[Arducam DVP 20 引脚连接器](../hardware/P293_ArducamDVP连接器.md) | [Arducam DVP 20-pin connector](https://docs.zephyrproject.org/latest/doxygen/html/group__dvp-20pin-connector.html) |  |  |
| 　　　[Arduino MKR 排针接口](../hardware/P294_ArduinoMKR排针.md) | [Arduino MKR header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html) |  |  |
| 　　　[Arduino Mega 排针接口](../hardware/P295_ArduinoMega排针.md) | [Arduino Mega header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html) |  |  |
| 　　　[Arduino Nano 排针接口](../hardware/P296_ArduinoNano排针.md) | [Arduino Nano header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html) |  |  |
| 　　　[Arduino Uno（R3）排针接口](../hardware/P297_ArduinoUno排针.md) | [Arduino Uno (R3) header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html) |  |  |
| 　　　[M.2 Key A 串行存储器连接器](../hardware/P298_M2串行存储器连接器.md) | [M.2 Key A serial memory connector](https://docs.zephyrproject.org/latest/doxygen/html/group__m2-memory-connector.html) |  |  |
| 　　　[Raspberry Pi CSI 连接器](../hardware/P299_树莓派CSI连接器.md) | [Raspberry Pi CSI connector](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html) |  |  |
| 　　　[ST Morpho 排针接口](../hardware/P300_STMorpho排针.md) | [ST Morpho header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html) |  |  |
| 　　　[ST Zio 排针接口](../hardware/P301_STZio排针.md) | [ST Zio header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html) |  |  |
| 　　　[STMod+ 连接器](../hardware/P302_STModPlus连接器.md) | [STMod+ connector](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html) |  |  |
| 　　　[WisBlock IO 插槽连接器](../hardware/P303_WisBlockIO插槽.md) | [WisBlock IO slot connector](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html) |  |  |
| 　　　[WisBlock 传感器插槽连接器](../hardware/P304_WisBlock传感器插槽.md) | [WisBlock Sensor Slot connector](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html) |  |  |
| 　[设备树硬件自旋锁 API](../intercore_reference/P008_硬件自旋锁设备树宏.md) | [Devicetree HW spinlock API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-hwspinlock.html) |  |  |
| 　设备树 I/O 通道 API | [Devicetree IO Channels API](../dt_connection_reference/P001_设备树I_O通道宏.md) |  |  |
| 　设备树中断 CPU API | [Devicetree Interrupt CPU API](../dt_node_reference/P003_设备树CPU节点宏.md) |  |  |
| 　设备树中断控制器 API | [Devicetree Interrupt Controller API](../dt_irq_reference/P002_设备树中断控制器宏.md) |  |  |
| 　　Arm GIC 中断控制器 | [Arm GIC interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html) |  |  |
| 　　Espressif ESP32 中断分配器 | [Espressif ESP32 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32__intmux.html) |  |  |
| 　　Espressif ESP32-C2 中断分配器 | [Espressif ESP32-C2 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c2__intmux.html) |  |  |
| 　　Espressif ESP32-C3 中断分配器 | [Espressif ESP32-C3 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c3__intmux.html) |  |  |
| 　　Espressif ESP32-C5 中断分配器 | [Espressif ESP32-C5 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c5__intmux.html) |  |  |
| 　　Espressif ESP32-C6 中断分配器 | [Espressif ESP32-C6 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c6__intmux.html) |  |  |
| 　　Espressif ESP32-C61 中断分配器 | [Espressif ESP32-C61 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c61__intmux.html) |  |  |
| 　　Espressif ESP32-H2 中断分配器 | [Espressif ESP32-H2 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32h2__intmux.html) |  |  |
| 　　Espressif ESP32-P4 中断分配器 | [Espressif ESP32-P4 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32p4__intmux.html) |  |  |
| 　　Espressif ESP32-S2 中断分配器 | [Espressif ESP32-S2 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32s2__intmux.html) |  |  |
| 　　Espressif ESP32-S3 中断分配器 | [Espressif ESP32-S3 interrupt allocator](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32s3__intmux.html) |  |  |
| 　　ITE IT51XXX 中断控制器 | [ITE IT51XXX interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__intc.html) |  |  |
| 　　ITE IT51XXX 唤醒控制器 | [ITE IT51XXX wake-up controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__wuc.html) |  |  |
| 　　ITE IT8XXX2 中断控制器 | [ITE IT8XXX2 interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html) |  |  |
| 　　ITE IT8XXX2 唤醒控制器 | [ITE IT8XXX2 wake-up controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html) |  |  |
| 　　Infineon XMC4xxx 中断控制器 | [Infineon XMC4xxx interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html) |  |  |
| 　　Intel I/O APIC 中断控制器 | [Intel I/O APIC interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__intel__ioapic.html) |  |  |
| 　　Microchip SmartFusion2 中断控制器 | [Microchip SmartFusion2 interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__microchip__smartfusion2__irq.html) |  |  |
| 　　Microchip XEC ECIA 中断控制器 | [Microchip XEC ECIA interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html) |  |  |
| 　　OpenISA RV32M1 中断多路复用器（INTMUX） | [OpenISA RV32M1 INTMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__openisa__intmux.html) |  |  |
| 　　Realtek RTS5817 中断源 | [Realtek RTS5817 interrupt sources](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__realtek__rts5817__intc.html) |  |  |
| 　　TI VIM 中断控制器 | [TI VIM interrupt controller](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html) |  |  |
| 　[设备树邮箱（MBOX） API](../intercore_reference/P021_邮箱设备树访问宏.md) | [Devicetree MBOX API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-mbox.html) |  |  |
| 　设备树多路复用器（MUX） API | [Devicetree MUX API](../dt_connection_reference/P007_设备树多路复用器宏.md) |  |  |
| 　设备树映射分区 API | [Devicetree Mapped Partition API](../dt_partition_reference/P005_设备树映射分区宏.md) |  |  |
| 　[设备树 PWM API](../hardware/P264_设备树PWM宏.md) | [Devicetree PWMs API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-pwms.html) |  |  |
| 　设备树分区 API | [Devicetree Partition API](../dt_partition_reference/P001_设备树通用分区宏.md) |  |  |
| 　设备树端口端点 API | [Devicetree Port Endpoint API](../dt_connection_reference/P010_设备树端口与端点宏.md) |  |  |
| 　[设备树稳压器 API](../power/P081_设备树稳压器辅助接口目录.md) | [Devicetree Regulator API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-regulator.html) |  |  |
| 　　[ADP5360 设备树辅助接口](../power/P085_ADP5360稳压器设备树辅助接口.md) | [ADP5360 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__adp5360.html) |  |  |
| 　　[AXP192 设备树辅助接口](../power/P086_AXP192稳压器设备树辅助接口.md) | [AXP192 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__axp192.html) |  |  |
| 　　[MAX20335 设备树辅助接口](../power/P087_MAX20335稳压器设备树辅助接口.md) | [MAX20335 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__max20335.html) |  |  |
| 　　[MAX20362 设备树辅助接口](../power/P088_MAX20362稳压器设备树辅助接口.md) | [MAX20362 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__max20362.html) |  |  |
| 　　[MSPM0 VREF 设备树辅助接口](../power/P089_MSPM0参考电压设备树辅助接口.md) | [MSPM0 VREF Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__mspm0__vref.html) |  |  |
| 　　[NXP VREF 设备树辅助接口](../power/P090_NXP参考电压设备树辅助接口.md) | [NXP VREF Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nxp__vref.html) |  |  |
| 　　[Raspberry Pi Pico 稳压器设备树辅助接口](../power/P091_RaspberryPi_Pico稳压器设备树辅助接口.md) | [Raspberry Pi Pico regulator Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__rpi__pico.html) |  |  |
| 　　[Silicon Labs DCDC 设备树辅助接口](../power/P092_SiliconLabs_DCDC设备树辅助接口.md) | [Silicon Labs DCDC Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__silabs__dcdc.html) |  |  |
| 　　[Texas Instruments TPS6287x 设备树辅助接口](../power/P093_TPS6287x稳压器设备树辅助接口.md) | [Texas Instruments TPS6287x Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__ti__tps6287x.html) |  |  |
| 　　[nPM10xx 设备树辅助接口](../power/P094_nPM10xx稳压器设备树辅助接口.md) | [nPM10xx Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm10xx.html) |  |  |
| 　　[nPM1100 设备树辅助接口](../power/P095_nPM1100稳压器设备树辅助接口.md) | [nPM1100 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm1100.html) |  |  |
| 　　[nPM13xx 设备树辅助接口](../power/P096_nPM13xx稳压器设备树辅助接口.md) | [nPM13xx Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm13xx.html) |  |  |
| 　　[nPM2100 设备树辅助接口](../power/P097_nPM2100稳压器设备树辅助接口.md) | [nPM2100 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm2100.html) |  |  |
| 　　[nPM6001 设备树辅助接口](../power/P098_nPM6001稳压器设备树辅助接口.md) | [nPM6001 Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__npm6001.html) |  |  |
| 　　[nRF5X 设备树辅助接口](../power/P099_nRF5X稳压器设备树辅助接口.md) | [nRF5X Devicetree helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__nrf5x.html) |  |  |
| 　设备树 Renesas RA ELC 辅助接口 | [Devicetree Renesas RA ELC helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra__elc.html) |  |  |
| 　　Renesas RA2A1 ELC 设备树宏 | [Renesas RA2A1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra2a1__elc.html) |  |  |
| 　　Renesas RA2L1 ELC 设备树宏 | [Renesas RA2L1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra2l1__elc.html) |  |  |
| 　　Renesas RA4E1 ELC 设备树宏 | [Renesas RA4E1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4e1__elc.html) |  |  |
| 　　Renesas RA4E2 ELC 设备树宏 | [Renesas RA4E2 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4e2__elc.html) |  |  |
| 　　Renesas RA4L1 ELC 设备树宏 | [Renesas RA4L1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4l1__elc.html) |  |  |
| 　　Renesas RA4M1 ELC 设备树宏 | [Renesas RA4M1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m1__elc.html) |  |  |
| 　　Renesas RA4M2 ELC 设备树宏 | [Renesas RA4M2 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m2__elc.html) |  |  |
| 　　Renesas RA4M3 ELC 设备树宏 | [Renesas RA4M3 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4m3__elc.html) |  |  |
| 　　Renesas RA4T1 ELC 设备树宏 | [Renesas RA4T1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4t1__elc.html) |  |  |
| 　　Renesas RA4W1 ELC 设备树宏 | [Renesas RA4W1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra4w1__elc.html) |  |  |
| 　　Renesas RA6E1 ELC 设备树宏 | [Renesas RA6E1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6e1__elc.html) |  |  |
| 　　Renesas RA6E2 ELC 设备树宏 | [Renesas RA6E2 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6e2__elc.html) |  |  |
| 　　Renesas RA6M1 ELC 设备树宏 | [Renesas RA6M1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m1__elc.html) |  |  |
| 　　Renesas RA6M2 ELC 设备树宏 | [Renesas RA6M2 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m2__elc.html) |  |  |
| 　　Renesas RA6M3 ELC 设备树宏 | [Renesas RA6M3 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m3__elc.html) |  |  |
| 　　Renesas RA6M4 ELC 设备树宏 | [Renesas RA6M4 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m4__elc.html) |  |  |
| 　　Renesas RA6M5 ELC 设备树宏 | [Renesas RA6M5 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m5__elc.html) |  |  |
| 　　Renesas RA8D1 ELC 设备树宏 | [Renesas RA8D1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8d1__elc.html) |  |  |
| 　　Renesas RA8E1 ELC 设备树宏 | [Renesas RA8E1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8e1__elc.html) |  |  |
| 　　Renesas RA8M1 ELC 设备树宏 | [Renesas RA8M1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8m1__elc.html) |  |  |
| 　　Renesas RA8T1 ELC 设备树宏 | [Renesas RA8T1 ELC devicetree macros](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra8t1__elc.html) |  |  |
| 　设备树复位控制器 API | [Devicetree Reset Controller API](../reset_reference/P007_复位控制器设备树辅助宏.md) |  |  |
| 　[设备树串行外设接口（SPI） API](../hardware/P329_SPI设备树宏.md) | [Devicetree SPI API](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-spi.html) |  |  |
| 　设备树 SRAM API | [Devicetree SRAM API](../dt_overview_reference/P005_选定SRAM区域宏.md) |  |  |
| 　设备树唤醒控制器 API | [Devicetree WUC Controller API](../dt_irq_reference/P005_设备树唤醒控制器宏.md) |  |  |
| 　设备树电池辅助接口 | [Devicetree battery helpers](../dt_overview_reference/P002_电池开路电压曲线宏.md) |  |  |
| 　设备树内存属性 | [Devicetree memory attributes](../dt_memory_attribute_reference/P001_设备树内存属性总览.md) |  |  |
| 　　架构专用内存属性 | [Architecture-specific memory attributes](../dt_memory_attribute_reference/P003_架构专用内存属性宏.md) |  |  |
| 　　　ARM MPU 内存属性 | [ARM MPU memory attributes](../dt_memory_attribute_reference/P018_Arm_MPU内存类型宏.md) |  |  |
| 　　　ARM64 内存属性 | [ARM64 memory attributes](../dt_memory_attribute_reference/P019_Arm64_MMU内存类型宏.md) |  |  |
| 　　　RISC-V 内存属性 | [RISC-V memory attributes](../dt_memory_attribute_reference/P020_RISC_V内存类型宏.md) |  |  |
| 　　　Xtensa 内存属性 | [Xtensa memory attributes](../dt_memory_attribute_reference/P021_Xtensa内存类型宏.md) |  |  |
| 　　通用内存属性 | [Generic memory attributes](../dt_memory_attribute_reference/P002_通用内存属性宏.md) |  |  |
| 　　软件专用内存属性 | [Software-specific memory attributes](../dt_memory_attribute_reference/P004_软件专用内存属性宏.md) |  |  |
| 　　　软件定义的内存属性 | [Software-defined memory attributes](../dt_memory_attribute_reference/P017_软件内存分配属性宏.md) |  |  |
| 　存在性检查 | [Existence checks](../dt_identity_reference/P002_设备树存在性与状态宏.md) |  |  |
| 　基于实例的设备树 API | [Instance-based devicetree APIs](../dt_instance_reference/P001_设备树驱动实例宏.md) |  |  |
| 　映射辅助接口 | [Map helpers](../dt_connection_reference/P004_设备树描述符映射宏.md) |  |  |
| 　[NVMEM 设备树辅助接口](../storage/P018_NVMEM设备树辅助宏.md) | [NVMEM Devicetree Helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html) |  |  |
| 　NXP i.MX952 电源域 | [NXP i.MX952 Power Domains](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html) |  |  |
| 　节点标识符与辅助接口 | [Node identifiers and helpers](../dt_identity_reference/P001_设备树节点标识宏.md) |  |  |
| 　引脚控制 | [Pin control](../pinctrl_reference/P005_引脚控制设备树宏.md) |  |  |
| 　　Ambiq 引脚控制辅助接口 | [Ambiq pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__ambiq__pinctrl.html) |  |  |
| 　　　Ambiq Apollo2 引脚控制辅助接口 | [Ambiq Apollo2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo2.html) |  |  |
| 　　　Ambiq Apollo3 引脚控制辅助接口 | [Ambiq Apollo3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo3.html) |  |  |
| 　　　Ambiq Apollo4 引脚控制辅助接口 | [Ambiq Apollo4 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html) |  |  |
| 　　　Ambiq Apollo5 引脚控制辅助接口 | [Ambiq Apollo5 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html) |  |  |
| 　　Espressif 引脚控制辅助接口 | [Espressif pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__espressif__pinctrl.html) |  |  |
| 　　　Espressif ESP32 引脚控制辅助接口 | [Espressif ESP32 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32.html) |  |  |
| 　　　Espressif ESP32C2 引脚控制辅助接口 | [Espressif ESP32C2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c2.html) |  |  |
| 　　　Espressif ESP32C3 引脚控制辅助接口 | [Espressif ESP32C3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c3.html) |  |  |
| 　　　Espressif ESP32C5 引脚控制辅助接口 | [Espressif ESP32C5 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c5.html) |  |  |
| 　　　Espressif ESP32C6 引脚控制辅助接口 | [Espressif ESP32C6 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html) |  |  |
| 　　　Espressif ESP32C61 引脚控制辅助接口 | [Espressif ESP32C61 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c61.html) |  |  |
| 　　　Espressif ESP32H2 引脚控制辅助接口 | [Espressif ESP32H2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32h2.html) |  |  |
| 　　　Espressif ESP32P4 引脚控制辅助接口 | [Espressif ESP32P4 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32p4.html) |  |  |
| 　　　Espressif ESP32S2 引脚控制辅助接口 | [Espressif ESP32S2 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s2.html) |  |  |
| 　　　Espressif ESP32S3 引脚控制辅助接口 | [Espressif ESP32S3 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32s3.html) |  |  |
| 　　FocalTech 引脚控制辅助接口 | [FocalTech pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl.html) |  |  |
| 　　　FocalTech FT9001 引脚控制辅助接口 | [FocalTech FT9001 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html) |  |  |
| 　　　　FT9001 IOCTRL 寄存器偏移量 | [FT9001 IOCTRL register offsets](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html) |  |  |
| 　　Nuvoton 引脚控制辅助接口 | [Nuvoton pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__nuvoton__pinctrl.html) |  |  |
| 　　　Nuvoton NuMaker M46x 引脚控制辅助接口 | [Nuvoton NuMaker M46x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html) |  |  |
| 　　Renesas 引脚控制辅助接口 | [Renesas pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__pinctrl.html) |  |  |
| 　　　Renesas R-Car 引脚控制辅助接口 | [Renesas R-Car pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html) |  |  |
| 　　　Renesas RA 引脚控制辅助接口 | [Renesas RA pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html) |  |  |
| 　　　Renesas RA0 引脚控制辅助接口 | [Renesas RA0 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html) |  |  |
| 　　　Renesas RX 引脚控制辅助接口 | [Renesas RX pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html) |  |  |
| 　　　Renesas RZ/A 引脚控制辅助接口 | [Renesas RZ/A pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html) |  |  |
| 　　　Renesas RZ/A2M 引脚控制辅助接口 | [Renesas RZ/A2M pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html) |  |  |
| 　　　Renesas RZ/G 引脚控制辅助接口 | [Renesas RZ/G pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html) |  |  |
| 　　　Renesas RZ/N 引脚控制辅助接口 | [Renesas RZ/N pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzn.html) |  |  |
| 　　　Renesas RZ/T 引脚控制辅助接口 | [Renesas RZ/T pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html) |  |  |
| 　　　Renesas RZ/V 引脚控制辅助接口 | [Renesas RZ/V pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html) |  |  |
| 　　SiFli 引脚控制辅助接口 | [SiFli pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__sifli__pinctrl.html) |  |  |
| 　　　SiFli SF32LB52x 引脚控制辅助接口 | [SiFli SF32LB52x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html) |  |  |
| 　　Silicon Labs 引脚控制辅助接口 | [Silicon Labs pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__silabs__pinctrl.html) |  |  |
| 　　　Silicon Labs SiWx91x 引脚控制辅助接口 | [Silicon Labs SiWx91x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html) |  |  |
| 　　　Silicon Labs Six301 引脚控制辅助接口 | [Silicon Labs Six301 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html) |  |  |
| 　　　Silicon Labs xG21 引脚控制辅助接口 | [Silicon Labs xG21 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg21.html) |  |  |
| 　　　Silicon Labs xG22 引脚控制辅助接口 | [Silicon Labs xG22 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg22.html) |  |  |
| 　　　Silicon Labs xG23 引脚控制辅助接口 | [Silicon Labs xG23 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg23.html) |  |  |
| 　　　Silicon Labs xG24 引脚控制辅助接口 | [Silicon Labs xG24 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg24.html) |  |  |
| 　　　Silicon Labs xG26 引脚控制辅助接口 | [Silicon Labs xG26 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg26.html) |  |  |
| 　　　Silicon Labs xG27 引脚控制辅助接口 | [Silicon Labs xG27 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg27.html) |  |  |
| 　　　Silicon Labs xG28 引脚控制辅助接口 | [Silicon Labs xG28 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html) |  |  |
| 　　　Silicon Labs xG29 引脚控制辅助接口 | [Silicon Labs xG29 pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg29.html) |  |  |
| 　　WCH CH32H41x 引脚控制辅助接口 | [WCH CH32H41x pin control helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html) |  |  |
| 　属性访问接口 | [Property accessors](../dt_property_reference/P001_设备树属性读取宏.md) |  |  |
| 　厂商与型号名称辅助接口 | [Vendor and model name helpers](../dt_identity_reference/P003_设备树厂商与型号宏.md) |  |  |
| 　interrupts 属性 | [interrupts property](../dt_irq_reference/P001_设备树中断属性宏.md) |  |  |
| 　ranges 属性 | [ranges property](../dt_reg_reference/P002_设备树地址范围映射宏.md) |  |  |
| 　reg 属性 | [reg property](../dt_reg_reference/P001_设备树寄存器属性宏.md) |  |  |

### 2.2.4\_错误编号（Error numbers）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 错误编号 | [Error numbers](../error_reference/P003_系统错误号公共接口.md) |  |  |

### 2.2.5\_内部与系统 API（Internal and System API）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 内部与系统 API | [Internal and System API](https://docs.zephyrproject.org/latest/doxygen/html/group__internal__api.html) |  |  |
| 　架构接口 | [Architecture Interface](../arch_core_reference/P001_架构接口总览.md) |  |  |
| 　　架构线程 API | [Architecture thread APIs](../thread_stack_reference/P004_架构线程接口.md) |  |  |
| 　　架构计时 API | [Architecture timing APIs](../timing_reference/P009_架构计数周期接口.md) |  |  |
| 　　架构专用 IRQ API | [Architecture-specific IRQ APIs](../fatal_irq_reference/P008_架构中断接口.md) |  |  |
| 　　架构专用 SMP API | [Architecture-specific SMP APIs](../arch_core_reference/P005_架构多处理器接口.md) |  |  |
| 　　架构专用栈回溯 API | [Architecture-specific Stack Walk APIs](../thread_stack_reference/P005_架构栈遍历接口.md) |  |  |
| 　　架构专用线程局部存储 API | [Architecture-specific Thread Local Storage APIs](../arch_core_reference/P007_架构线程局部存储接口.md) |  |  |
| 　　架构专用缓存控制器 | [Architecture-specific cache controllers.](../arch_core_reference/P002_架构缓存接口.md) |  |  |
| 　　[架构专用核心转储 API](../observability/P060_核心转储架构接口.md) | [Architecture-specific core dump APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html) |  |  |
| 　　[架构专用 gdbstub API](../observability/P061_GDB桩架构接口.md) | [Architecture-specific gdbstub APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html) |  |  |
| 　　架构专用内存映射 API | [Architecture-specific memory-mapping APIs](../arch_core_reference/P003_架构内存映射接口.md) |  |  |
| 　　架构专用电源管理 API | [Architecture-specific power management APIs](../arch_core_reference/P006_架构电源管理接口.md) |  |  |
| 　　架构专用用户空间 API | [Architecture-specific userspace APIs](../arch_core_reference/P004_架构用户空间接口.md) |  |  |
| 　　指令存储器 API | [Instruction Memory APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html) |  |  |
| 　　其他架构 API | [Miscellaneous architecture APIs](../arch_core_reference/P008_架构杂项接口.md) |  |  |
| 　内核内存管理内部 API | [Kernel Memory Management Internal APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html) |  |  |
| 　用户模式内部 API | [User Mode Internal APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html) |  |  |
| 　用户模式与系统调用 API | [User mode and Syscall APIs](../syscall_boot_reference/P001_系统调用接口.md) |  |  |

### 2.2.6\_内核 API（Kernel APIs）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 内核 API | [Kernel APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　异步轮询 API | [Async polling APIs](../eventpoll_reference/P003_轮询公共接口.md) |  |  |
| 　原子操作服务 API | [Atomic Services APIs](../atomic_reference/P001_原子操作公共接口.md) |  |  |
| 　屏障服务 API | [Barrier Services APIs](../synchronization_reference/P001_内存屏障公共接口.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　CPU 空闲 API | [CPU Idling APIs](../fatal_irq_reference/P011_CPU空闲接口.md) |  |  |
| 　条件变量 API | [Condition Variables APIs](../synchronization_reference/P010_条件变量公共接口.md) |  |  |
| 　事件 API | [Event APIs](../eventpoll_reference/P001_事件公共接口.md) |  |  |
| 　先进先出（FIFO）API | [FIFO APIs](../queue_reference/P003_FIFO公共接口.md) |  |  |
| 　快速用户空间互斥锁（FUTEX）API | [FUTEX APIs](../userspace_sync_reference/P001_Futex公共接口.md) |  |  |
| 　致命错误 API | [Fatal error APIs](../fatal_irq_reference/P001_致命错误处理接口.md) |  |  |
| 　　致命错误基本类型 | [Fatal error base types](../fatal_irq_reference/P004_致命错误原因接口.md) |  |  |
| 　浮点 API | [Floating Point APIs](../fatal_irq_reference/P012_浮点上下文接口.md) |  |  |
| 　堆 API | [Heap APIs](../heap_reference/P001_内核堆公共接口.md) |  |  |
| 　中断服务例程 API | [Interrupt Service Routine APIs](../fatal_irq_reference/P007_中断服务接口.md) |  |  |
| 　内核内存管理 | [Kernel Memory Management](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html) |  |  |
| 　　按需分页 | [Demand Paging](https://docs.zephyrproject.org/latest/doxygen/html/group__demand__paging.html) |  |  |
| 　　　后备存储 API | [Backing Store APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html) |  |  |
| 　　　按需分页 API | [Demand Paging APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html) |  |  |
| 　　　页面淘汰算法 API | [Eviction Algorithm APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html) |  |  |
| 　后进先出（LIFO）API | [LIFO APIs](../queue_reference/P005_LIFO公共接口.md) |  |  |
| 　邮箱 API | [Mailbox APIs](../mboxpipe_reference/P001_邮箱公共接口.md) |  |  |
| 　内存块池 API | [Memory Slab APIs](../heap_reference/P003_固定块内存池公共接口.md) |  |  |
| 　内存域 API | [Memory domain APIs](../memory_domain_reference/P001_内存域接口.md) |  |  |
| 　　应用程序内存域 API | [Application memory domain APIs](../memory_domain_reference/P006_应用内存分区接口.md) |  |  |
| 　消息队列 API | [Message Queue APIs](../msgstack_reference/P001_消息队列公共接口.md) |  |  |
| 　互斥锁 API | [Mutex APIs](../synchronization_reference/P006_互斥量公共接口.md) |  |  |
| 　对象核心 API | [Object Core APIs](../object_core_reference/P001_对象核心公共接口.md) |  |  |
| 　对象核心统计 API | [Object Core Statistics APIs](../object_core_reference/P002_对象核心统计接口.md) |  |  |
| 　管道 API | [Pipe APIs](../mboxpipe_reference/P004_管道公共接口.md) |  |  |
| 　队列 API | [Queue APIs](../queue_reference/P001_通用队列公共接口.md) |  |  |
| 　信号量 API | [Semaphore APIs](../synchronization_reference/P008_信号量公共接口.md) |  |  |
| 　[自旋锁 API](../kernel/P065_自旋锁公共接口.md) | [Spinlock APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__spinlock__apis.html) |  |  |
| 　栈 API | [Stack APIs](../msgstack_reference/P004_栈公共接口.md) |  |  |
| 　[系统时钟 API](../timer_reference/P086_系统时钟公共接口.md) | [System Clock APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html) |  |  |
| 　　[系统定时器低功耗伴随接口](../timer_reference/P089_系统时钟低功耗交接接口.md) | [System Timer Low-power Companion Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__lpm.html) |  |  |
| 　线程 API | [Thread APIs](../thread_core_reference/P001_线程公共接口.md) |  |  |
| 　线程栈 API | [Thread Stack APIs](../thread_stack_reference/P001_线程栈接口.md) | 1.0.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　定时器 API | [Timer APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html) |  |  |
| 　用户模式 API | [User Mode APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html) |  |  |
| 　　用户模式互斥锁 API | [User mode mutex APIs](../userspace_sync_reference/P003_用户模式互斥量公共接口.md) |  |  |
| 　　用户模式信号量 API | [User mode semaphore APIs](../userspace_sync_reference/P007_用户模式信号量公共接口.md) |  |  |
| 　版本 API | [Version APIs](../boot_control_reference/P013_内核版本接口.md) |  |  |
| 　工作队列 API | [Work Queue APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html) |  |  |

### 2.2.7\_内存管理 API（Memory Management APIs）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 内存管理 API | [Memory Management APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mem__mgmt.html) |  |  |
| 　内存属性接口 | [Memory Attribute Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__attr__interface.html) |  |  |
| 　基于内存属性的内存堆 | [Memory heaps based on memory attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__attr__heap.html) |  |  |

### 2.2.8\_操作系统服务（Operating System Services）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 操作系统服务 | [Operating System Services](https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html) |  |  |
| 　异步通知 API | [Asynchronous Notification APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__sys__notify__apis.html) |  |  |
| 　身份验证 | [Authentication](https://docs.zephyrproject.org/latest/doxygen/html/group__authentication.html) |  |  |
| 　　FIDO2 | [FIDO2](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html) | 0.1.1 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　二进制描述符 | [Binary Descriptors](https://docs.zephyrproject.org/latest/doxygen/html/group__bindesc.html) |  |  |
| 　　二进制描述符定义 | [Binary Descriptor Definition](https://docs.zephyrproject.org/latest/doxygen/html/group__bindesc__define.html) |  |  |
| 　　二进制描述符读取 | [Binary Descriptor Reading](https://docs.zephyrproject.org/latest/doxygen/html/group__bindesc__read.html) |  |  |
| 　[CPU 频率（CPUFreq）](../power/P023_CPU调频接口.md) | [CPU Frequency (CPUFreq)](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq.html) | 0.8.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　[CPU 频率策略](../power/P024_CPU调频策略接口.md) | [CPU Frequency Policy](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html) | 0.8.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　[CPU 频率性能状态（pstate）](../power/P025_性能状态接口.md) | [CPU Frequency pstate](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__pstate.html) | 0.8.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　[CPU 负载监测器](../observability/P049_CPU负载接口.md) | [CPU load monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html) |  |  |
| 　缓存接口 | [Cache Interface](../cache_reference/P001_公共缓存接口.md) | 1.0.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　校验和 | [Checksum](../checksum_reference/P001_校验和主题目录.md) |  |  |
| 　　循环冗余校验（CRC） | [CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__crc.html) | 1.0.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　清理辅助接口 | [Cleanup Helper Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html) |  |  |
| 　连接功能 | [Connectivity](https://docs.zephyrproject.org/latest/doxygen/html/group__connectivity.html) |  |  |
| 　　蓝牙 API | [Bluetooth APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html) |  |  |
| 　　　高级音频分发配置文件（A2DP） | [Advanced Audio Distribution Profile (A2DP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html) |  |  |
| 　　　告警通知服务（ANS） | [Alert Notification Service (ANS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　分配编号 | [Assigned Numbers.](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　　蓝牙 Mesh 分配编号 | [Bluetooth Mesh Assigned Numbers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html) |  |  |
| 　　　　核心规范分配编号 | [Core Specification Assigned Numbers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html) |  |  |
| 　　　　通用音频分配编号 | [Generic Audio Assigned Numbers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html) |  |  |
| 　　　属性协议（ATT） | [Attribute Protocol (ATT)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html) | 1.1.0 | [v1.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.1.0) |
| 　　　音频输入控制服务（AICS） | [Audio Input Control Service (AICS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　音频流控制服务（ASCS） | [Audio Stream Control Service (ASCS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　音视频远程控制配置文件（AVRCP） | [Audio Video Remote Control Profile (AVRCP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html) |  |  |
| 　　　　音视频远程控制封面图配置文件 | [Audio Video Remote Control Cover Art Profile](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html) |  |  |
| 　　　基本音频配置文件（BAP）LC3 预设 | [Basic Audio Profile (BAP) LC3 Presets](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　基本成像配置文件（BIP） | [Basic Imaging Profile (BIP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html) |  |  |
| 　　　电池服务（BAS） | [Battery Service (BAS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html) |  |  |
| 　　　BlueNRG HCI 驱动扩展 API | [BlueNRG HCI driver extended API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html) |  |  |
| 　　　蓝牙音频 | [Bluetooth Audio](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html) | 0.8.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　　　分配编号转字符串 API | [Assigned numbers to string API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html) |  |  |
| 　　　　编解码器能力解析 API | [Codec capability parsing APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html) |  |  |
| 　　　　编解码器配置解析 API | [Codec config parsing APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html) |  |  |
| 　　　蓝牙基本音频配置文件 | [Bluetooth Basic Audio Profile](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　　BAP 广播 API | [BAP Broadcast  APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html) |  |  |
| 　　　　　BAP 广播接收端 API | [BAP Broadcast Sink APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html) |  |  |
| 　　　　　BAP 广播源 API | [BAP Broadcast Source APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html) |  |  |
| 　　　　BAP 广播接收端 API | [BAP Broadcast Sink APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html) |  |  |
| 　　　　BAP 广播源 API | [BAP Broadcast Source APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html) |  |  |
| 　　　　BAP 单播客户端 API | [BAP Unicast Client APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html) |  |  |
| 　　　　BAP 单播服务器 API | [BAP Unicast Server APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html) |  |  |
| 　　　蓝牙内容控制标识符 | [Bluetooth Content Control Identifier](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html) | 0.8.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　蓝牙控制器 | [Bluetooth Controller](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html) |  |  |
| 　　　蓝牙游戏音频配置文件 | [Bluetooth Gaming Audio Profile](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　蓝牙主机控制器接口（HCI） | [Bluetooth HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html) | 0.3.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　　蓝牙 H:4 UART 驱动厂商扩展接口 | [Bluetooth H:4 UART driver vendor extension interface](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　　蓝牙 HCI 驱动后端 API | [Bluetooth HCI Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html) |  |  |
| 　　　　蓝牙 HCI 锁步命令辅助接口 | [Bluetooth HCI lockstep command helper](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　蓝牙 HCI 数据包辅助接口 | [Bluetooth HCI packet helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　蓝牙人机接口设备（HID） | [Bluetooth HID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html) |  |  |
| 　　　蓝牙 HID 设备 | [Bluetooth HID Device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html) |  |  |
| 　　　蓝牙 HID 主机 | [Bluetooth HID Host](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html) |  |  |
| 　　　蓝牙 LC3 编解码器 | [Bluetooth LC3 codec](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　用于 BR/EDR 的蓝牙逻辑链路控制与适配协议（L2CAP） | [Bluetooth Logical Link Control and Adaptation Protocol (L2CAP) for BR/EDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html) |  |  |
| 　　　蓝牙 Mesh | [Bluetooth Mesh](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html) |  |  |
| 　　　　访问层 | [Access layer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html) |  |  |
| 　　　　蓝牙 Mesh BLOB 传输客户端模型 API | [Bluetooth Mesh BLOB Transfer Client model API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html) |  |  |
| 　　　　蓝牙 Mesh BLOB 传输服务器模型 API | [Bluetooth Mesh BLOB Transfer Server model API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html) |  |  |
| 　　　　蓝牙 Mesh BLOB 闪存流 | [Bluetooth Mesh BLOB flash stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html) |  |  |
| 　　　　蓝牙 Mesh BLOB 模型 API | [Bluetooth Mesh BLOB model API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html) |  |  |
| 　　　　蓝牙 Mesh 设备固件更新 | [Bluetooth Mesh Device Firmware Update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html) |  |  |
| 　　　　　蓝牙 Mesh 设备固件更新（DFU）元数据 | [Bluetooth Mesh Device Firmware Update (DFU) metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html) |  |  |
| 　　　　　固件更新服务器模型 | [Firmware Update Server model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html) |  |  |
| 　　　　　固件更新客户端模型 | [Firmware Uppdate Client model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html) |  |  |
| 　　　　蓝牙 Mesh 按需私有 GATT 代理客户端 | [Bluetooth Mesh On-Demand Private GATT Proxy Client](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html) |  |  |
| 　　　　蓝牙 Mesh 按需私有 GATT 代理服务器 | [Bluetooth Mesh On-Demand Private GATT Proxy Server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html) |  |  |
| 　　　　蓝牙 Mesh 私有信标客户端 | [Bluetooth Mesh Private Beacon Client](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html) |  |  |
| 　　　　蓝牙 Mesh 私有信标服务器 | [Bluetooth Mesh Private Beacon Server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html) |  |  |
| 　　　　蓝牙 Mesh 分段与重组（SAR）配置客户端模型 | [Bluetooth Mesh SAR Configuration Client Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html) |  |  |
| 　　　　蓝牙 Mesh 分段与重组（SAR）配置服务器模型 | [Bluetooth Mesh SAR Configuration Server Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__srv.html) |  |  |
| 　　　　蓝牙 Mesh 请求 PDU 重放保护列表（RPL）客户端 | [Bluetooth Mesh Solicitation PDU RPL Client](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html) |  |  |
| 　　　　蓝牙 Mesh 请求 PDU 重放保护列表（RPL）服务器 | [Bluetooth Mesh Solicitation PDU RPL Server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.html) |  |  |
| 　　　　桥接配置客户端模型 | [Bridge Configuration Client Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html) |  |  |
| 　　　　桥接配置服务器模型 | [Bridge Configuration Server Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__srv.html) |  |  |
| 　　　　桥接配置公共头文件 | [Bridge Configuration common header](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html) |  |  |
| 　　　　配置客户端模型 | [Configuration Client Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html) |  |  |
| 　　　　配置服务器模型 | [Configuration Server Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__srv.html) |  |  |
| 　　　　固件分发模型 | [Firmware Distribution models](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html) |  |  |
| 　　　　　固件分发服务器模型 | [Firmware Distribution Server model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html) |  |  |
| 　　　　健康客户端模型 | [Health Client Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html) |  |  |
| 　　　　健康服务器模型 | [Health Server Model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html) |  |  |
| 　　　　健康故障 | [Health faults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html) |  |  |
| 　　　　心跳 | [Heartbeat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html) |  |  |
| 　　　　大型组成数据客户端模型 | [Large Composition Data Client model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html) |  |  |
| 　　　　大型组成数据服务器模型 | [Large Composition Data Server model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__srv.html) |  |  |
| 　　　　消息 | [Message](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html) |  |  |
| 　　　　操作码聚合器客户端模型 | [Opcodes Aggregator Client model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html) |  |  |
| 　　　　操作码聚合器服务器模型 | [Opcodes Aggregator Server model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__srv.html) |  |  |
| 　　　　配网 | [Provisioning](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html) |  |  |
| 　　　　代理 | [Proxy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html) |  |  |
| 　　　　远程配网客户端模型 | [Remote Provisioning Client model](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html) |  |  |
| 　　　　远程配网模型 | [Remote Provisioning models](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html) |  |  |
| 　　　　远程配网服务器 | [Remote provisioning server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html) |  |  |
| 　　　　运行时配置 | [Runtime Configuration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html) |  |  |
| 　　　　　应用程序配置 | [Application Configuration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html) |  |  |
| 　　　　　子网配置 | [Subnet Configuration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html) |  |  |
| 　　　　分段与重组（SAR）配置公共头文件 | [SAR Configuration common header](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg.html) |  |  |
| 　　　　统计 | [Statistic](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html) |  |  |
| 　　　字节序 | [Byteorder](../byteorder_reference/P003_蓝牙字节序辅助接口.md) | 1.0.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　呼叫控制配置文件（CCP） | [Call Control Profile (CCP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　　CCP 呼叫控制客户端 API | [CCP Call Control Client APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html) |  |  |
| 　　　　CCP 呼叫控制服务器 API | [CCP Call Control Server APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html) |  |  |
| 　　　信道探测（CS） | [Channel Sounding (CS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html) |  |  |
| 　　　通用音频配置文件（CAP） | [Common Audio Profile (CAP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html) | 0.8.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.2.0) |
| 　　　连接管理 | [Connection management](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html) | 1.0.1 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　协调集标识配置文件（CSIP） | [Coordinated Set Identification Profile (CSIP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　密码学 | [Cryptography](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html) | 1.0.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　　　当前时间服务（CTS） | [Current Time Service (CTS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html) |  |  |
| 　　　数据缓冲区 | [Data buffers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html) | 1.0.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　设备地址 | [Device Address](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　经过时间服务（ETS） | [Elapsed Time Service (ETS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html) |  |  |
| 　　　加密广播数据（EAD） | [Encrypted Advertising Data (EAD)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html) |  |  |
| 　　　游戏音频配置文件（GMAP）LC3 预设 | [Gaming Audio Profile (GMAP) LC3 Presets](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap__lc3__preset.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　通用访问配置文件（GAP） | [Generic Access Profile (GAP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html) | 1.1.1 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　　定义与分配编号 | [Defines and Assigned Numbers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html) |  |  |
| 　　　通用属性配置文件（GATT） | [Generic Attribute Profile (GATT)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html) | 1.0.1 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　　GATT 客户端 API | [GATT Client APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html) |  |  |
| 　　　　GATT 服务器 API | [GATT Server APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html) |  |  |
| 　　　通用对象交换配置文件（GOEP） | [Generic Object Exchange Profile (GOEP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html) |  |  |
| 　　　　GOEP 的 L2CAP 传输 | [GOEP transport L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html) |  |  |
| 　　　　GOEP 的 RFCOMM 传输 | [GOEP transport RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html) |  |  |
| 　　　HCI 原始通道 | [HCI RAW channel](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html) | 1.0.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　　免提配置文件（HFP） | [Hands Free Profile (HFP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html) |  |  |
| 　　　免提配置文件音频网关（HFP-AG） | [Hands Free Profile - Audio Gateway (HFP-AG)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html) |  |  |
| 　　　听力访问服务（HAS） | [Hearing Access Service (HAS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html) | 0.8.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.1.0) |
| 　　　心率服务（HRS） | [Heart Rate Service (HRS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html) |  |  |
| 　　　即时告警服务（IAS） | [Immediate Alert Service (IAS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html) |  |  |
| 　　　IrDA 对象交换协议（OBEX） | [IrDA Object Exchange Protocol (OBEX)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html) |  |  |
| 　　　等时通道（ISO） | [Isochronous channels (ISO)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html) | 0.8.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　　逻辑链路控制与适配协议（L2CAP） | [L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html) | 1.0.1 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　　L2CAP 通道标识符 | [L2CAP channel identifiers](https://docs.zephyrproject.org/latest/doxygen/html/group__l2cap__cid.html) |  |  |
| 　　　媒体控制客户端（MCC） | [Media Control Client (MCC)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　媒体控制服务（MCS） | [Media Control Service (MCS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　媒体代理 | [Media Proxy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　消息访问配置文件（MAP） | [Message Access Profile (MAP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html) |  |  |
| 　　　　消息客户端设备（MCE）的 OBEX 客户端 | [Messaging Client Equipment(MCE) OBEX Client](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html) |  |  |
| 　　　　消息客户端设备（MCE）的 OBEX 服务器 | [Messaging Client Equipment(MCE) OBEX Server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html) |  |  |
| 　　　　消息服务器设备（MSE）的 OBEX 客户端 | [Messaging Server Equipment(MSE) OBEX Client](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html) |  |  |
| 　　　　消息服务器设备（MSE）的 OBEX 服务器 | [Messaging Server Equipment(MSE) OBEX Server](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html) |  |  |
| 　　　麦克风控制配置文件（MICP） | [Microphone Control Profile (MICP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　　对象传输服务（OTS） | [Object Transfer Service (OTS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |
| 　　　电话簿访问配置文件（PBAP） | [Phone Book Access Profile (PBAP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html) |  |  |
| 　　　公共广播配置文件（PBP） | [Public Broadcast Profile (PBP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　已发布音频能力服务（PACS） | [Published Audio Capabilities Service (PACS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　RFCOMM | [RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html) | 0.1.0 | [v1.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.6.0) |
| 　　　服务发现协议（SDP） | [Service Discovery Protocol (SDP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html) | 0.1.0 | [v1.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.6.0) |
| 　　　电话承载服务（TBS） | [Telephone Bearer Service (TBS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　电话与媒体音频配置文件（TMAP） | [Telephone and Media Audio Profile (TMAP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　通用唯一标识符（UUID） | [UUIDs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　音量控制配置文件（VCP） | [Volume Control Profile (VCP)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　　音量偏移控制服务（VOCS） | [Volume Offset Control Service (VOCS)](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　[CAN ISO-TP 协议](../hardware/P380_CAN_ISO-TP接口参考.md) | [CAN ISO-TP Protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html) | 1.0.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.2.0) |
| 　　IEEE 802.15.4 与 Thread API | [IEEE 802.15.4 and Thread APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　IEEE 802.15.4 驱动 | [IEEE 802.15.4 Drivers](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　IEEE 802.15.4 二层（L2） | [IEEE 802.15.4 L2](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　IEEE 802.15.4 网络管理 | [IEEE 802.15.4 Net Management](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__mgmt.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　OpenThread 协议栈 | [OpenThread stack](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html) | 0.8.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　　LoRaWAN API | [LoRaWAN APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html) | 0.2.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.5.0) |
| 　　MODBUS | [MODBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__modbus.html) |  |  |
| 　　调制解调器 API | [Modem APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__modem.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　调制解调器连接复用（CMUX） | [Modem CMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　调制解调器命令交互（Chat） | [Modem Chat](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　调制解调器 PPP | [Modem PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　调制解调器管道 | [Modem Pipe](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　调制解调器 UBX | [Modem Ubx](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html) | 1.0.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　调制解调器管道链路 | [Modem pipelink](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html) | 1.0.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　网络 | [Networking](https://docs.zephyrproject.org/latest/doxygen/html/group__networking.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　应用程序网络上下文 | [Application network context](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　兼容 BSD 套接字的 API | [BSD Sockets compatible API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html) | 1.0.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.9.0) |
| 　　　　IPv4 套接字选项 | [Socket options for IPv4](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html) |  |  |
| 　　　　IPv6 套接字选项 | [Socket options for IPv6](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html) |  |  |
| 　　　　TLS 套接字选项 | [Socket options for TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　　数据包套接字选项 | [Socket options for packet socket](https://docs.zephyrproject.org/latest/doxygen/html/group__packet__socket__options.html) |  |  |
| 　　　BSD 套接字服务 API | [BSD socket service API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html) | 0.2.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　CoAP 库 | [COAP Library](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　　CoAP 管理器事件 | [CoAP Manager Events](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　CoAP OSCORE API | [CoAP OSCORE API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　CoAP TCP 客户端 API | [CoAP TCP client API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html) |  |  |
| 　　　CoAP 客户端 API | [CoAP client API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　CoAP 服务 API | [CoAP service API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　连接管理器 API | [Connection Manager API](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html) | 0.1.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　　　连接管理器连接功能 API | [Connection Manager Connectivity API](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　　连接管理器连接功能批量操作 API | [Connection Manager Connectivity Bulk API](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　　连接管理器连接功能实现 API | [Connection Manager Connectivity Implementation API](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　动态主机配置协议第 4 版（DHCPv4） | [DHCPv4](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　DHCPv4 服务器 | [DHCPv4 server](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html) | 0.8.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　动态主机配置协议第 6 版（DHCPv6） | [DHCPv6](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　DHCPv6 服务器 | [DHCPv6 server](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　DNS 解析库 | [DNS Resolve Library](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html) | 0.9.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　　　DNS 服务发现 | [DNS Service Discovery](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.5.0) |
| 　　　数据报分组化层路径 MTU 发现（PLPMTUD）API | [Datagram PLPMTUD API](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　分布式交换架构（DSA） | [Distributed Switch Architecture (DSA)](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html) | 0.8.0 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　　　虚设二层／驱动支持函数 | [Dummy L2/driver Support Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__dummy.html) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　　以太网桥接 API | [Ethernet Bridging API](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　　以太网库 | [Ethernet Library](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　以太网物理层（PHY）接口 | [Ethernet PHY Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　　　以太网 PHY 驱动后端 API | [Ethernet PHY Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy__backend.html) |  |  |
| 　　　以太网支持函数 | [Ethernet Support Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　　DSA 标签协议 | [DSA tag protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html) | 0.8.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　　以太网媒体独立接口（MII）支持函数 | [Ethernet MII Support Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mii.html) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　　IEEE 802.3 管理接口 | [IEEE 802.3 management interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　以太网桥转发数据库（FDB） | [Ethernet bridge FDB](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　FTP 客户端库 API | [FTP client library API](https://docs.zephyrproject.org/latest/doxygen/html/group__ftp__client.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　HTTP 头部压缩（HPACK） | [HTTP HPACK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__hpack.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　HTTP 客户端 API | [HTTP client API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html) | 0.2.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.1.0) |
| 　　　HTTP 请求方法 | [HTTP request methods](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　HTTP 响应状态码 | [HTTP response status codes](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　HTTP 服务器 API | [HTTP server API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　HTTP 服务 API | [HTTP service API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　互联网控制消息协议（ICMP） | [ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　互联网组管理协议（IGMP）API | [IGMP API](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　IPv4 网络地址转换 | [IPv4 Network Address Translation](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　IPv4／IPv6 基本操作与辅助接口 | [IPv4/IPv6 primitives and helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　延迟监测器 | [Latency Monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__latmon.html) |  |  |
| 　　　链路层发现协议定义与辅助接口 | [Link Layer Discovery Protocol definitions and helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　LwM2M 高层 API | [LwM2M high-level API](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html) | 0.8.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.9.0) |
| 　　　　LwM2M 路径辅助宏 | [LwM2M path helper macros](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__path__helpers.html) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.5.0) |
| 　　　MCP 服务器 API | [MCP Server API](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp__server.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　MQTT 客户端库 | [MQTT Client library](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　　MQTT-SN 客户端库 | [MQTT-SN Client library](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　组播监听者发现 API | [Multicast Listener Discovery API](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html) | 0.8.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　　　网络配置库 | [Network Configuration Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html) | 0.8.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.8.0) |
| 　　　网络核心库 | [Network Core Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　网络主机名库 | [Network Hostname Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　　网络接口抽象层 | [Network Interface abstraction layer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html) | 1.1.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　　　网络二层抽象层 | [Network L2 Abstraction Layer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　　　网络链路地址库 | [Network Link Address Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　　网络 MIDI 2.0 | [Network MIDI 2.0](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　　　用于通用 MIDI 数据包的用户数据报协议 | [User Datagram Protocol for Universal MIDI Packets](https://docs.zephyrproject.org/latest/doxygen/html/group__netmidi10.html) |  |  |
| 　　　网络管理 | [Network Management](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html) | 2.0.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　网络卸载接口 | [Network Offloading Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__offload.html) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　网络数据包过滤 API | [Network Packet Filter API](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　　基本过滤条件 | [Basic Filter Conditions](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__basic__cond.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　　以太网过滤条件 | [Ethernet Filter Conditions](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　　网络数据包库 | [Network Packet Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html) | 0.8.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　　　网络统计库 | [Network Statistics Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html) | 0.8.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　　　网络长超时基本操作与辅助接口 | [Network long timeout primitives and helpers](../time_headers_reference/P008_网络超时接口.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　　网络命名空间兼容模式符号 | [Network namespace compatibility mode symbols](https://docs.zephyrproject.org/latest/doxygen/html/group__net__compat.html) | 0.0.1 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　网络抓包 | [Network packet capture](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　网络时间表示 | [Network time representation.](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　OCPP 库 | [OCPP library](https://docs.zephyrproject.org/latest/doxygen/html/group__ocpp__api.html) | 0.1.0 | [v4.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.3.0) |
| 　　　支持卸载的网络设备 | [Offloaded Net Devices](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　PPP 二层／驱动支持函数 | [PPP L2/driver Support Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html) | 0.8.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　　　精确时间协议（PTP）支持 | [PTP support](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　PTP 时间 | [PTP time](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　Prometheus API | [Prometheus API](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　混杂模式 | [Promiscuous mode](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　QUIC 库 | [QUIC Library](https://docs.zephyrproject.org/latest/doxygen/html/group__quic.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　实时传输协议（RTP） | [RTP (Real-time Transport Protocol)](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html) | 0.1.0 |  |
| 　　　简单网络时间协议（SNTP） | [SNTP](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　　　SNTP 服务器 | [SNTP server](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　SSH 客户端库 | [SSH Client Library](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　SSH 服务器库 | [SSH Server Library](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　SSH 客户端／服务器公共 API | [SSH client/server common API](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　SSH 密钥生成 API | [SSH keygen API](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　套接字 NET_MGMT 库 | [Socket NET_MGMT library](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html) | 0.1.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　　　SocketCAN 库 | [SocketCAN library](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　　TFTP 客户端库 | [TFTP Client library](https://docs.zephyrproject.org/latest/doxygen/html/group__tftp__client.html) | 0.1.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　　TLS 凭据管理 | [TLS credentials management](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　Trickle 算法库 | [Trickle Algorithm Library](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　　虚拟接口库 | [Virtual Interface Library](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual__mgmt.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　虚拟局域网定义与辅助接口 | [Virtual LAN definitions and helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　虚拟网络接口支持函数 | [Virtual Network Interface Support Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　　WebSocket API | [Websocket API](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html) | 0.1.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　Wi-Fi 管理 | [Wi-Fi Management](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　　ESP32 Wi-Fi Mesh | [ESP32 Wi-Fi Mesh](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　Wi-Fi 网络管理器 API | [Wi-Fi Network Manager API](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　　Wi-Fi 凭据库 | [Wi-Fi credentials library](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　WireGuard VPN 服务 | [Wireguard VPN service](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html) | 0.1.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　Zperf API | [Zperf API](https://docs.zephyrproject.org/latest/doxygen/html/group__zperf.html) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　广义精确时间协议（gPTP）支持 | [gPTP support](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html) | 0.1.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　通用串行总线（USB） | [USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb.html) |  |  |
| 　　　USB 音频类 2 设备 API | [USB Audio Class 2 device API](../usb/P089_USB音频2设备API.md) | 0.2.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.6.0) |
| 　　　USB 二进制设备对象存储（BOS）支持 | [USB BOS support](../usb/P145_USBBOS支持API.md) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　USB DFU 设备更新 API | [USB DFU device update API](../usb/P062_USB设备固件升级API.md) | 0.1.0 | [v4.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.1.0) |
| 　　　USB 人机接口设备（HID）类 API | [USB HID class API](../usb/P045_旧版HID类API.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　　　　HID 类的 USB 专用定义 | [HID class USB specific definitions](../usb/P046_旧版HID设备接口API.md) |  |  |
| 　　　USB HID 公共定义 | [USB HID common definitions](../usb/P048_HID通用定义.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　　　　鼠标与键盘报告描述符 | [Mouse and keyboard report descriptors](../usb/P050_HID报告描述符构造宏.md) |  |  |
| 　　　　USB HID 条目辅助接口 | [USB HID Item helpers](../usb/P049_HID报告项目定义.md) |  |  |
| 　　　USB 主机核心 API | [USB Host Core API](../usb/P079_USB主机核心API.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　USB MIDI 2.0 类设备 API | [USB MIDI 2.0 Class device API](../usb/P094_USBMIDI2设备API.md) | 0.1.0 | [v4.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.1.0) |
| 　　　USB 大容量存储类设备 API | [USB Mass Storage Class device API](../usb/P058_USB大容量存储API.md) | 0.2.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　　USB 视频类（UVC）设备 API | [USB Video Class (UVC) device API](../usb/P122_USB视频设备API.md) | 0.1.1 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　　　USB 缓冲区宏与定义 | [USB buffer macros and definitions](../usb/P039_USB缓冲区宏与定义.md) | 0.1.1 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　USB 设备核心 API | [USB device core API](../usb/P015_USB设备核心API.md) | 0.2.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　　USB 设备核心 API | [USB device core API](../usb/P016_USB设备消息API.md) | 0.2.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　　　USBD HID 设备 API | [USBD HID device API](../usb/P042_新版HID设备API.md) | 0.4.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.7.0) |
| 　控制台 API | [Console API](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html) |  |  |
| 　密码运算 | [Crypto](../crypto/P008_密码驱动通用接口.md) | 1.0.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.7.0) |
| 　　密码算法 | [Cipher](../crypto/P012_密码算法会话接口.md) |  |  |
| 　　密码运算驱动后端 API | [Crypto Driver Backend API](../crypto/P009_密码驱动后端接口.md) |  |  |
| 　　散列 | [Hash](../crypto/P023_密码散列会话接口.md) |  |  |
| 　　随机函数 API | [Random Function APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__random__api.html) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　调试 | [Debug](../debug_trace_reference/P001_调试接口目录.md) |  |  |
| 　　[核心转储 API](../observability/P052_核心转储接口.md) | [Coredump APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__coredump__apis.html) | 1.0.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |
| 　　CoreSight API | [Coresight APIs](../trace_interface_reference/P001_CoreSight接口目录.md) |  |  |
| 　　　[CoreSight 跟踪解格式器](../observability/P026_CoreSight解格式接口.md) | [Coresight Trace Deformatter](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html) |  |  |
| 　　[系统跟踪协议（STP）解码器 API](../observability/P027_MIPI_STP解码接口.md) | [STP Decoder API](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html) |  |  |
| 　　[符号表 API](../observability/P051_符号表接口.md) | [Symbol Table API](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html) |  |  |
| 　　[线程分析器](../observability/P050_线程分析器接口.md) | [Thread analyzer](https://docs.zephyrproject.org/latest/doxygen/html/group__thread__analyzer.html) |  |  |
| 　设备管理 | [Device Management](https://docs.zephyrproject.org/latest/doxygen/html/group__device__mgmt.html) |  |  |
| 　　嵌入式控制器（EC）主机命令接口 | [EC Host Command Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |
| 　　　主机命令驱动后端 API | [Host Command Driver Backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html) |  |  |
| 　　　模拟器 | [Simulator](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html) |  |  |
| 　　管理组件传输协议（MCTP） | [MCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__mctp.html) |  |  |
| 　　MCUmgr | [MCUmgr](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr.html) |  |  |
| 　　　回调 | [Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html) |  |  |
| 　　　　枚举管理回调 | [Enumeration Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html) |  |  |
| 　　　　文件系统管理回调 | [File System Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html) |  |  |
| 　　　　镜像管理回调 | [Image Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html) |  |  |
| 　　　　操作系统管理回调 | [OS Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html) |  |  |
| 　　　　设置管理回调 | [Settings Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html) |  |  |
| 　　　处理程序 | [Handlers](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html) |  |  |
| 　　　管理 | [Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　　　　枚举管理 | [Enumeration Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html) |  |  |
| 　　　　　枚举管理回调 | [Enumeration Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html) |  |  |
| 　　　　文件系统管理 | [File System Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html) |  |  |
| 　　　　　文件系统管理回调 | [File System Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html) |  |  |
| 　　　　镜像管理 | [Image Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html) |  |  |
| 　　　　　镜像管理回调 | [Image Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html) |  |  |
| 　　　　　镜像管理客户端 | [Image Management Client](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html) |  |  |
| 　　　　操作系统管理 | [OS Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html) |  |  |
| 　　　　　操作系统管理回调 | [OS Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html) |  |  |
| 　　　　　操作系统管理客户端 | [OS Management Client](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html) |  |  |
| 　　　　设置管理 | [Settings Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html) |  |  |
| 　　　　　设置管理回调 | [Settings Management Callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html) |  |  |
| 　　　　Shell 管理 | [Shell Management](../shell_management_reference/P004_mcumgr_Shell管理接口.md) |  |  |
| 　　　　统计管理 | [Statistics Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html) |  |  |
| 　　　　传输管理 | [Transport management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　　Zephyr 基础管理 | [Zephyr Basic Management](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html) |  |  |
| 　　　简单管理协议（SMP）客户端 | [SMP client](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html) |  |  |
| 　　　传输层 | [Transport layers](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport.html) |  |  |
| 　　　　蓝牙传输 | [Bluetooth transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html) |  |  |
| 　　　　虚设传输 | [Dummy transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html) |  |  |
| 　　　　SMP 传输 | [SMP transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html) |  |  |
| 　　　　串行传输 | [Serial transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html) |  |  |
| 　　　　Shell 传输 | [Shell transport](../shell_management_reference/P007_mcumgr_Shell传输接口.md) |  |  |
| 　　　　UDP 传输 | [UDP transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html) |  |  |
| 　错误检查 | [Error checking](../check_reference/P001_运行时检查接口.md) | 1.0.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.2.0) |
| 　通过 HTTP 的固件空中更新（FOTA） | [FOTA HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　[文件系统 API](../storage/P033_文件系统接口.md) | [File System APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__file__system__api.html) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |
| 　[文件系统存储](../storage/P034_文件系统存储参考.md) | [File System Storage](https://docs.zephyrproject.org/latest/doxygen/html/group__file__system__storage.html) |  |  |
| 　　[闪存循环缓冲区（FCB）](../storage/P046_闪存循环缓冲区参考目录.md) | [Flash Circular Buffer (FCB)](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb.html) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　　　[闪存循环缓冲区数据结构](../storage/P048_闪存循环缓冲区数据结构目录.md) | [Flash Circular Buffer Data Structures](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__data__structures.html) |  |  |
| 　　　[FCB API](../storage/P047_闪存循环缓冲区接口.md) | [fcb API](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html) |  |  |
| 　　　[FCB 非 API 原型](../storage/P049_闪存循环缓冲区内部读写接口.md) | [fcb non-API prototypes](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__internal.html) |  |  |
| 　　[非易失性存储（NVS）](../storage/P053_非易失性存储参考目录.md) | [Non-volatile Storage (NVS)](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs.html) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　[非易失性存储 API](../storage/P055_非易失性存储接口.md) | [Non-volatile Storage APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html) |  |  |
| 　　　[非易失性存储数据结构](../storage/P054_非易失性存储数据结构目录.md) | [Non-volatile Storage Data Structures](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__data__structures.html) |  |  |
| 　　[设置](../storage/P063_设置子系统接口.md) | [Settings](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.12.0) |
| 　　　[设置后端接口](../storage/P064_设置存储后端接口.md) | [Settings backend interface](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__backend.html) |  |  |
| 　　　[设置名称处理](../storage/P065_设置键名处理接口.md) | [Settings name processing](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__name__proc.html) |  |  |
| 　　　[设置子系统运行时](../storage/P017_设置运行时接口.md) | [Settings subsystem runtime](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__rt.html) |  |  |
| 　　[Zephyr 存储器存储（ZMS）](../storage/P057_Zephyr内存存储参考目录.md) | [Zephyr Memory Storage (ZMS)](https://docs.zephyrproject.org/latest/doxygen/html/group__zms.html) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.0.0) |
| 　　　[ZMS API](../storage/P059_Zephyr内存存储接口.md) | [ZMS API](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html) |  |  |
| 　　　[ZMS 数据结构](../storage/P058_Zephyr内存存储数据结构目录.md) | [ZMS data structures](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html) |  |  |
| 　闪存镜像 API | [Flash image API](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html) |  |  |
| 　堆管理 | [Heap Management](https://docs.zephyrproject.org/latest/doxygen/html/group__heaps.html) |  |  |
| 　　堆 KASAN API | [Heap KASAN APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html) |  |  |
| 　　堆监听器 API | [Heap Listener APIs](../lowheap_reference/P003_堆事件监听接口.md) |  |  |
| 　　底层堆分配器 | [Low Level Heap Allocator](../lowheap_reference/P001_底层堆分配接口.md) | 1.0.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　多堆封装 | [Multi-Heap Wrapper](../lowheap_reference/P002_多堆包装接口.md) |  |  |
| 　　共享多堆接口 | [Shared multi-heap interface](../lowheap_reference/P009_共享多堆公共接口.md) |  |  |
| 　[处理器间通信（IPC）](../intercore_reference/P181_IPC接口总览.md) | [IPC](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc.html) |  |  |
| 　　[IPC 服务 API](../intercore_reference/P111_IPC服务公共接口.md) | [IPC service APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__api.html) | 1.0.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　[IPC 服务 RPMsg API](../intercore_reference/P124_IPC的RPMsg公共层接口.md) | [IPC service RPMsg API](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__rpmsg__api.html) |  |  |
| 　　[IPC 服务后端](../intercore_reference/P115_IPC服务后端接口.md) | [IPC service backend](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__backend.html) |  |  |
| 　　[IPC 服务静态虚拟环（VRING）API](../intercore_reference/P129_IPC静态虚拟环接口.md) | [IPC service static VRINGs API](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__static__vrings__api.html) |  |  |
| 　　[Icmsg IPC 库 API](../intercore_reference/P135_ICMsg基础接口.md) | [Icmsg IPC library API](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__api.html) |  |  |
| 　　[Icmsg 多端点 IPC 库 API](../intercore_reference/P140_ICMsg多端点接口.md) | [Icmsg multi-endpoint IPC library API](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__me__api.html) |  |  |
| 　　[紧凑缓冲区 API](../intercore_reference/P144_核间数据包缓冲区接口.md) | [Packed Buffer API](https://docs.zephyrproject.org/latest/doxygen/html/group__pbuf.html) |  |  |
| 　　[RPMsg 服务 API](../intercore_reference/P121_RPMsg服务公共接口.md) | [RPMsg service APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__rpmsg__service__api.html) |  |  |
| 　[插桩](../observability/P025_插桩接口参考.md) | [Instrumentation](https://docs.zephyrproject.org/latest/doxygen/html/group__instrumentation__api.html) |  |  |
| 　可迭代段 API | [Iterable Sections APIs](../iterable_reference/P001_可遍历段公共接口.md) | 1.0.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　可链接可加载扩展 | [Linkable loadable extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__apis.html) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　　ELF 常量与数据类型 | [ELF constants and data types](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__elf.html) |  |  |
| 　　ELF 检查 API | [ELF inspection APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__inspect__apis.html) |  |  |
| 　　ELF 加载器上下文 | [ELF loader context](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__loader__apis.html) |  |  |
| 　　导出符号定义 | [Exported symbol definitions](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__symbols.html) |  |  |
| 　日志 | [Logging](../log_core_reference/P001_日志主题总览.md) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　日志系统 | [Logger system](https://docs.zephyrproject.org/latest/doxygen/html/group__logger.html) |  | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　日志链路 | [Log links](../log_link_reference/P001_日志链路接口.md) |  |  |
| 　　　日志消息 | [Log messages](../log_message_reference/P001_日志消息接口.md) |  |  |
| 　　　日志输出 | [Log output](../log_output_reference/P001_日志输出接口.md) |  |  |
| 　　　　日志输出格式标志 | [Log output formatting flags.](../log_output_format_reference/P001_日志输出格式化标志.md) |  |  |
| 　　　日志后端 | [Logger backends](../log_backend_reference/P001_日志后端接口.md) |  |  |
| 　　　　蓝牙日志后端 | [Bluetooth log backend](../log_transport_reference/P001_蓝牙低功耗日志后端接口.md) |  |  |
| 　　　　Intel ADSP HDA 日志后端 | [Intel ADSP HDA log backend](../log_backend_helpers_reference/P001_Intel_ADSP_HDA日志后端接口.md) |  |  |
| 　　　　Intel ADSP mtrace 日志后端 | [Intel ADSP mtrace log backend](../log_backend_helpers_reference/P004_Intel_ADSP_mtrace日志后端接口.md) |  |  |
| 　　　　日志多域后端辅助接口 | [Logger multidomain backend helpers](../log_backend_helpers_reference/P010_多域日志后端辅助接口.md) |  |  |
| 　　　　MQTT 日志后端 | [MQTT log backend](../log_transport_reference/P004_MQTT日志后端接口.md) |  |  |
| 　　　　网络日志后端 | [Network log backend](../log_transport_reference/P007_网络日志后端接口.md) |  |  |
| 　　　　标准后端辅助接口 | [Standard backend helpers](../log_backend_helpers_reference/P007_标准日志后端辅助接口.md) |  |  |
| 　　　　WebSocket 日志后端 | [Websocket log backend](../log_transport_reference/P010_WebSocket日志后端接口.md) |  |  |
| 　　　日志控制 API | [Logger control API](../log_core_reference/P005_日志控制接口.md) |  | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　　日志前端 | [Logger frontend](../log_frontend_reference/P001_日志前端接口.md) |  |  |
| 　　　　[STMESP 前端](../observability/P030_STMESP日志前端接口.md) | [STMESP frontend](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp.html) |  |  |
| 　　　日志 API | [Logging API](../log_core_reference/P002_日志公共接口.md) |  |  |
| 　　[跟踪与调试域](../observability/P031_STMESP日志接口目录.md) | [Trace and debug domain](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__apis.html) |  |  |
| 　　　[STMESP 解复用器](../observability/P032_STMESP日志解复用接口.md) | [STMESP demultiplexer](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html) |  |  |
| 　内存管理 | [Memory Management](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html) |  |  |
| 　　内存 Bank 驱动 API | [Memory Banks Driver APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html) |  |  |
| 　　内存块 API | [Memory Blocks APIs](../memblocks_reference/P001_内存块分配公共接口.md) |  |  |
| 　　内存管理驱动 API | [Memory Management Driver APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html) |  |  |
| 　　按字粒度访问存储器的 API | [Word Granular Access Memory APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html) |  |  |
| 　基于模块的断言处理 | [Module based assert handling](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html) |  |  |
| 　多媒体 | [Multimedia](https://docs.zephyrproject.org/latest/doxygen/html/group__multimedia.html) |  |  |
| 　　视频子系统 | [Video Subsystem](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api.html) | 0.2.0 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　视频缓冲区 | [Video Buffers](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html) |  |  |
| 　　　视频能力 | [Video Capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html) |  |  |
| 　　　视频控制项标识符 | [Video Control IDs](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html) | 0.0.1 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　视频控制项 | [Video Controls](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html) |  |  |
| 　　　视频格式 | [Video Format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html) |  |  |
| 　　　视频格式集合 | [Video Formats](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html) | 0.0.1 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　　　视频帧间隔 | [Video Frame Interval](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html) |  |  |
| 　　　视频流 | [Video Stream](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html) |  |  |
| 　　　视频类型 | [Video Types](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html) | 0.0.1 | [v4.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.4.0) |
| 　多媒体流水线 | [Multimedia Pipeline](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe.html) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　框架 | [Framework](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__framework.html) |  |  |
| 　　　元素容器（Bin） | [Bins](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html) |  |  |
| 　　　缓冲区 | [Buffers](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html) |  |  |
| 　　　能力结构 | [Capability Structure](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html) |  |  |
| 　　　分派 | [Dispatches](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html) |  |  |
| 　　　元素 | [Elements](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html) |  |  |
| 　　　消息 | [Messages](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html) |  |  |
| 　　　对象 | [Objects](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html) |  |  |
| 　　　连接端口（Pad） | [Pad](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html) |  |  |
| 　　　解析器 | [Parsers](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html) |  |  |
| 　　　流水线 | [Pipelines](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html) |  |  |
| 　　　接收端 | [Sinks](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html) |  |  |
| 　　　数据源 | [Sources](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html) |  |  |
| 　　　线程 | [Threads](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html) |  |  |
| 　　　变换 | [Transforms](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html) |  |  |
| 　　　值容器 | [Value Container](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html) |  |  |
| 　　　工作队列 | [Workqueues](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html) |  |  |
| 　　播放器 | [Player](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__player.html) |  |  |
| 　　插件 | [Plugins](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__plugins.html) |  |  |
| 　　　基础元素 | [Base Elements](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__base.html) |  |  |
| 　　　　应用程序接收端 | [Application sinks](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html) |  |  |
| 　　　　应用程序数据源 | [Application sources](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html) |  |  |
| 　　　　能力过滤器 | [Caps Filters](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html) |  |  |
| 　　　　队列 | [Queues](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html) |  |  |
| 　　　　分流器（Tee） | [Tee](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html) |  |  |
| 　　拓扑转储 | [Topology dump](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html) |  |  |
| 　网络缓冲区库 | [Network Buffer Library](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html) | 1.1.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　开关服务 API | [On-Off Service APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__resource__mgmt__onoff__apis.html) |  |  |
| 　[PSA 安全存储 API](../storage/P022_PSA安全存储接口.md) | [PSA Secure Storage API](https://docs.zephyrproject.org/latest/doxygen/html/group__psa__secure__storage.html) | 1.0.4 |  |
| 　[电源管理（PM）](../power/P031_电源管理接口分组.md) | [Power Management (PM)](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm.html) |  | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.2.0) |
| 　　[CPU 电源管理](../power/P061_CPU电源管理接口.md) | [CPU Power Management](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　[设备](../power/P036_设备电源管理接口.md) | [Device](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html) | 1.0.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　　[设备运行时](../power/P037_设备运行时电源管理接口.md) | [Device Runtime](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html) | 1.0.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.0.0) |
| 　　[挂起到 RAM（S2RAM）API](../power/P062_挂起到RAM接口.md) | [S2RAM APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html) |  |  |
| 　　[状态](../power/P034_电源状态接口.md) | [States](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html) |  |  |
| 　　[系统](../power/P032_系统电源管理接口.md) | [System](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys.html) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.2.0) |
| 　　　[钩子](../power/P033_系统电源管理钩子.md) | [Hooks](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__hooks.html) |  |  |
| 　　　[策略](../power/P035_系统电源管理策略接口.md) | [Policy](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html) | 1.0.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.7.0) |
| 　精密计时 | [Precision Timing](../timing_reference/P010_精确计时接口.md) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　精密时钟 | [Precision Clock](../precision_reference/P004_精确时钟接口.md) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　　精密时钟 PTP 适配器 | [Precision Clock PTP Adapter](../precision_reference/P009_PTP时钟适配器接口.md) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　精密比例积分（PI）控制器 | [Precision PI Controller](../precision_reference/P013_比例积分控制器接口.md) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　　精密时间 | [Precision Time](../precision_reference/P001_精确时间接口.md) | 0.1.0 | [v4.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.5.0) |
| 　实时 I/O（RTIO） | [RTIO](../rtio_core_reference/P001_RTIO公共接口.md) | 0.2.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.2.0) |
| 　　RTIO 完成队列项（CQE）标志 | [RTIO CQE Flags](../rtio_model_reference/P008_RTIO完成事件标志.md) |  |  |
| 　　[RTIO I2C I/O 设备（IODEV）标志](../hardware/P442_RTIO的I2C标志.md) | [RTIO I2C IODEV Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html) |  |  |
| 　　[RTIO I3C I/O 设备（IODEV）标志](../hardware/P434_RTIO的I3C标志.md) | [RTIO I3C IODEV Flags](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html) |  |  |
| 　　RTIO 操作码 | [RTIO Operation Codes](../rtio_model_reference/P009_RTIO操作码.md) |  |  |
| 　　RTIO 优先级 | [RTIO Priorities](../rtio_model_reference/P011_RTIO优先级.md) |  |  |
| 　　RTIO 提交队列项（SQE）标志 | [RTIO SQE Flags](../rtio_model_reference/P010_RTIO提交事件标志.md) |  |  |
| 　[保持存储 API](../storage/P014_数据保留接口参考.md) | [Retention API](https://docs.zephyrproject.org/latest/doxygen/html/group__retention__api.html) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.4.0) |
| 　　[启动模式接口](../storage/P015_启动模式接口参考.md) | [Boot mode interface](https://docs.zephyrproject.org/latest/doxygen/html/group__boot__mode__interface.html) |  |  |
| 　　[引导加载程序信息接口](../storage/P016_引导加载器信息接口.md) | [Bootloader info interface](https://docs.zephyrproject.org/latest/doxygen/html/group__bootloader__info__interface.html) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　半主机 API | [Semihosting APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html) |  |  |
| 　传感 | [Sensing](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html) |  |  |
| 　　数据类型 | [Data Types](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__datatypes.html) |  |  |
| 　　传感器类型（传感子系统） | [Sensor Types (Sensing)](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor__types.html) |  |  |
| 　　传感器（传感子系统） | [Sensors (Sensing)](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html) |  |  |
| 　命令行解释器（Shell） | [Shell](../shell_core_reference/P001_Shell核心接口.md) | 1.0.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.14.0) |
| 　　Shell 后端 | [Shell backends](../shell_backend_reference/P001_Shell后端目录.md) |  |  |
| 　　　ADSP 内存窗口 Shell 后端 | [ADSP memory window shell backend](../shell_transport_reference/P001_Shell_ADSP内存窗口后端接口.md) |  |  |
| 　　　虚设 Shell 后端 | [Dummy shell backend](../shell_backend_reference/P004_Shell虚拟后端接口.md) |  |  |
| 　　　MQTT Shell 后端 | [MQTT shell backend](../shell_transport_reference/P004_Shell_MQTT后端接口.md) |  |  |
| 　　　[RPMsg Shell 后端](../intercore_reference/P178_RPMsg命令行后端接口.md) | [RPMsg shell backend](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__rpmsg.html) |  |  |
| 　　　RTT Shell 后端 | [RTT shell backend](../shell_backend_reference/P007_Shell_RTT后端接口.md) |  |  |
| 　　　SSH Shell 后端 | [SSH shell backend](../shell_ssh_reference/P001_Shell_SSH后端接口.md) |  |  |
| 　　　Telnet Shell 后端 | [Telnet shell backend](../shell_transport_reference/P007_Shell_Telnet后端接口.md) |  |  |
| 　　　UART Shell 后端 | [UART shell backend](../shell_backend_reference/P010_Shell_UART后端接口.md) |  |  |
| 　　　WebSocket Shell 后端 | [Websocket shell backend](../shell_transport_reference/P010_Shell_WebSocket后端接口.md) |  |  |
| 　　远程 Shell | [Shell remote](../shell_remote_reference/P001_远端Shell接口.md) |  |  |
| 　状态机框架 API | [State Machine Framework API](https://docs.zephyrproject.org/latest/doxygen/html/group__smf.html) | 0.2.0 |  |
| 　统计 | [Statistics](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html) |  |  |
| 　存储 API | [Storage APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__storage__apis.html) |  |  |
| 　　磁盘访问接口 | [Disk Access Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html) |  |  |
| 　　流式写入闪存接口 | [Stream to flash interface](../stream_flash_reference/P004_流式Flash公共接口.md) | 0.1.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.3.0) |
| 　　闪存区域接口 | [flash area Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html) | 1.1.1 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.11.0) |
| 　系统初始化 | [System Initialization](../device_reference/P005_系统初始化接口.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　[系统关机](../power/P063_系统关机接口.md) | [System power off](https://docs.zephyrproject.org/latest/doxygen/html/group__sys__poweroff.html) | 1.0.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.5.0) |
| 　[任务看门狗 API](../power/P009_任务看门狗接口.md) | [Task Watchdog APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__task__wdt__api.html) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.5.0) |
| 　计时测量 API | [Timing Measurement APIs](../timing_reference/P001_计时公共接口.md) | 1.0.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |
| 　　架构专用计时测量 API | [Arch specific Timing Measurement APIs](../timing_reference/P002_架构计时接口.md) |  |  |
| 　　开发板专用计时测量 API | [Board specific Timing Measurement APIs](../timing_reference/P003_开发板计时接口.md) |  |  |
| 　　SoC 专用计时测量 API | [SoC specific Timing Measurement APIs](../timing_reference/P004_片上系统计时接口.md) |  |  |
| 　跟踪 | [Tracing](../tracing_core_reference/P001_跟踪子系统总览.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.13.0) |
| 　　跟踪格式 | [Tracing format](../tracing_core_reference/P003_跟踪格式接口.md) |  |  |
| 　　跟踪钩子 | [Tracing hooks](../tracing_core_reference/P002_跟踪API总览.md) |  |  |
| 　　　后端专用扩展 | [Backend-specific extensions](../network_thread_trace_reference/P005_后端扩展跟踪接口.md) |  |  |
| 　　　条件变量 | [Conditional variable](../sync_trace_reference/P003_条件变量跟踪接口.md) |  |  |
| 　　　可延迟工作项 | [Delayable work item](../driver_trace_reference/P006_可延时工作项跟踪接口.md) |  |  |
| 　　　事件 | [Event](../sync_trace_reference/P004_事件对象跟踪接口.md) |  |  |
| 　　　先进先出（FIFO） | [FIFO](../object_trace_reference/P001_FIFO跟踪接口.md) |  |  |
| 　　　通用输入输出（GPIO） | [GPIO](../driver_trace_reference/P002_GPIO跟踪接口.md) |  |  |
| 　　　堆 | [Heap](../object_trace_reference/P008_堆跟踪接口.md) |  |  |
| 　　　后进先出（LIFO） | [LIFO](../object_trace_reference/P002_LIFO跟踪接口.md) |  |  |
| 　　　邮箱 | [Mailbox](../object_trace_reference/P005_邮箱跟踪接口.md) |  |  |
| 　　　内存块池 | [Memory slab](../object_trace_reference/P009_内存块池跟踪接口.md) |  |  |
| 　　　消息队列 | [Message queue](../object_trace_reference/P004_消息队列跟踪接口.md) |  |  |
| 　　　互斥锁 | [Mutex](../sync_trace_reference/P002_互斥锁跟踪接口.md) |  |  |
| 　　　网络 | [Network](../network_thread_trace_reference/P002_网络跟踪接口.md) |  |  |
| 　　　网络套接字 | [Network socket](../network_thread_trace_reference/P003_套接字跟踪接口.md) |  |  |
| 　　　电源管理设备运行时 | [PM Device Runtime](../driver_trace_reference/P003_设备运行时电源管理跟踪.md) |  |  |
| 　　　管道 | [Pipe](../object_trace_reference/P006_管道跟踪接口.md) |  |  |
| 　　　轮询 | [Polling](../sync_trace_reference/P006_轮询跟踪接口.md) |  |  |
| 　　　队列 | [Queue](../object_trace_reference/P003_队列跟踪接口.md) |  |  |
| 　　　RTIO 跟踪 API | [RTIO Tracing APIs](../driver_trace_reference/P001_RTIO跟踪接口.md) |  |  |
| 　　　信号量 | [Semaphore](../sync_trace_reference/P001_信号量跟踪接口.md) |  |  |
| 　　　栈 | [Stack](../object_trace_reference/P007_栈跟踪接口.md) |  |  |
| 　　　系统调用跟踪 | [Syscall Tracing](../sync_trace_reference/P007_系统调用跟踪接口.md) |  |  |
| 　　　系统电源管理 | [System PM](../driver_trace_reference/P004_系统电源管理跟踪.md) |  |  |
| 　　　线程 | [Thread](../network_thread_trace_reference/P001_线程跟踪接口.md) |  |  |
| 　　　定时器 | [Timer](../sync_trace_reference/P005_定时器跟踪接口.md) |  |  |
| 　　　触发式工作项 | [Triggered work item](../driver_trace_reference/P007_轮询工作项跟踪接口.md) |  |  |
| 　　　用户定义事件 | [User-defined event](../network_thread_trace_reference/P004_命名事件跟踪接口.md) |  |  |
| 　　　工作项 | [Work item](../driver_trace_reference/P005_工作项跟踪接口.md) |  |  |
| 　　　工作队列 | [Work queue](../driver_trace_reference/P008_工作队列跟踪接口.md) |  |  |
| 　　跟踪辅助宏 | [Tracing utility macros](../tracing_core_reference/P004_跟踪包装宏接口.md) |  |  |
| 　Xen 支持 | [Xen support](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html) |  |  |
| 　　Xen Dom0 控制 | [Xen Dom0 control](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0.html) |  |  |
| 　　　Xen Dom0 域控制 | [Xen Dom0 domain control](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html) |  |  |
| 　　　Xen Dom0 系统控制（sysctl） | [Xen Dom0 sysctl](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html) |  |  |
| 　　Xen 硬件虚拟机（HVM）操作 | [Xen HVM operations](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html) |  |  |
| 　　Xen XSM FLASK | [Xen XSM FLASK](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html) |  |  |
| 　　Xen 设备模型 | [Xen device model](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html) |  |  |
| 　　Xen 事件通道 | [Xen event channels](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html) |  |  |
| 　　Xen 扩展区域 | [Xen extended regions](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html) |  |  |
| 　　Xen 授权表 | [Xen grant tables](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html) |  |  |
| 　　Xen 内部支持 | [Xen internal support](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__internal.html) |  |  |
| 　　　Xen 控制台驱动 | [Xen console driver](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html) |  |  |
| 　　Xen 内存管理 | [Xen memory management](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html) |  |  |
| 　　Xen 版本查询 | [Xen version queries](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html) |  |  |
| 　[Zbus API](../intercore_reference/P213_zbus核心接口.md) | [Zbus APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html) | 1.0.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　[Zbus 代理（Proxy Agent）API](../intercore_reference/P193_zbus代理接口.md) | [Zbus Proxy Agent API](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html) |  |  |
| 　　　[Zbus 代理的 IPC 后端](../intercore_reference/P201_zbus代理IPC后端接口.md) | [Zbus Proxy Agent IPC Backend](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent__ipc__backend.html) |  |  |

### 2.2.9\_测试（Testing）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| [测试](../hardware/P499_测试API目录.md) | [Testing](https://docs.zephyrproject.org/latest/doxygen/html/group__testing.html) |  |  |
| 　[模拟器接口](../hardware/P476_外设仿真器API.md) | [Emulator interfaces](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html) |  |  |
| 　　[电池备份 RAM（BBRAM）模拟器后端 API](../hardware/P490_BBRAM仿真后端接口.md) | [BBRAM emulator backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html) |  |  |
| 　　[BC1.2 后端模拟器 API](../hardware/P491_BC1点2仿真后端接口.md) | [BC1.2 backed emulator APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html) |  |  |
| 　　[生物特征识别模拟器测试辅助接口](../hardware/P495_生物识别仿真测试接口.md) | [Biometrics emulator test helpers](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html) |  |  |
| 　　[模拟模数转换器（ADC）](../hardware/P464_ADC模拟器接口.md) | [Emulated ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html) |  |  |
| 　　[模拟通用输入输出（GPIO）](../hardware/P273_GPIO模拟接口.md) | [Emulated GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html) |  |  |
| 　　[模拟计数器](../hardware/P493_计数器仿真后端接口.md) | [Emulated counter](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__emul.html) |  |  |
| 　　[伪 CAN 控制器](../hardware/P374_伪CAN控制器接口.md) | [Fake CAN controller](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html) |  |  |
| 　　[伪电可擦可编程只读存储器（EEPROM）](../hardware/P051_伪EEPROM接口.md) | [Fake EEPROM](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html) |  |  |
| 　　[伪 LED 控制器](../hardware/P207_模拟LED控制器.md) | [Fake LED controller](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html) |  |  |
| 　　[伪脉宽调制（PWM）](../hardware/P260_PWM模拟控制器.md) | [Fake PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html) |  |  |
| 　　[伪实时时钟（RTC）](../hardware/P497_RTC伪设备接口.md) | [Fake RTC](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__fake.html) |  |  |
| 　　[伪比较器](../hardware/P090_伪比较器接口.md) | [Fake comparator](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html) |  |  |
| 　　[伪稳压器](../hardware/P498_稳压器伪设备接口.md) | [Fake regulator](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html) |  |  |
| 　　[电量计后端模拟器 API](../hardware/P492_电量计仿真后端接口.md) | [Fuel gauge backend emulator APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html) |  |  |
| 　　[集成电路间总线（I2C）模拟接口](../hardware/P314_I2C模拟后端.md) | [I2C Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html) |  |  |
| 　　[多线串行外设接口（MSPI）模拟接口](../hardware/P487_MSPI总线仿真接口.md) | [MSPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html) |  |  |
| 　　[串行外设接口（SPI）模拟接口](../hardware/P326_SPI模拟接口.md) | [SPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html) |  |  |
| 　　[传感器模拟器后端 API](../hardware/P494_传感器仿真后端接口.md) | [Sensor emulator backend API](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html) |  |  |
| 　　[通用异步收发器（UART）模拟接口](../hardware/P341_UART模拟接口.md) | [UART Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html) |  |  |
| 　　[增强型串行外设接口（eSPI）模拟接口](../hardware/P486_eSPI总线仿真接口.md) | [eSPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html) |  |  |
| 　[伪函数框架（FFF）扩展](../hardware/P500_FFF测试扩展接口.md) | [FFF extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__fff__extensions.html) |  |  |
| 　[Zephyr 基准测试框架](../hardware/P501_ZTest基准测试接口.md) | [Zephyr Benchmarking Framework](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html) |  |  |
| 　[Zephyr 测试框架（ZTest）](../hardware/P502_ZTest测试框架接口.md) | [Zephyr Testing Framework (ZTest)](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest.html) |  |  |
| 　　[Ztest 断言宏](../hardware/P503_ZTest断言宏.md) | [Ztest assertion macros](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html) |  |  |
| 　　[Ztest 假定宏](../hardware/P504_ZTest假设宏.md) | [Ztest assumption macros](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html) |  |  |
| 　　[Ztest 期望宏](../hardware/P505_ZTest预期检查宏.md) | [Ztest expectation macros](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html) |  |  |
| 　　[Ztest 模拟支持](../hardware/P506_ZTest模拟支持.md) | [Ztest mocking support](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html) |  |  |
| 　　[Ztest 测试宏](../hardware/P507_ZTest测试定义宏.md) | [Ztest testing macros](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html) |  |  |
| 　　[Ztest ztress 宏](../hardware/P508_ZTest压力测试宏.md) | [Ztest ztress macros](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html) |  |  |

### 2.2.10\_第三方（Third-party）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 第三方 | [Third-party](https://docs.zephyrproject.org/latest/doxygen/html/group__third__party.html) |  |  |
| 　BBC micro:bit 显示 API | [BBC micro:bit display APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html) |  |  |
| 　Grove 显示 | [Grove display](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html) |  |  |
| 　MCUboot 镜像控制 API | [MCUboot image control API](../boot_control_reference/P001_MCUboot镜像控制接口.md) |  |  |
| 　[UpdateHub 固件空中更新](../firmware_update/P031_UpdateHub接口.md) | [UpdateHub Firmware Over-the-Air](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html) |  |  |
| 　[hawkBit 固件空中更新](../firmware_update/P027_hawkBit接口.md) | [hawkBit Firmware Over-the-Air](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html) |  |  |
| 　　[hawkBit 自动处理程序 API](../firmware_update/P028_hawkBit自动处理接口.md) | [hawkBit autohandler API](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html) |  |  |
| 　　[hawkBit 配置 API](../firmware_update/P029_hawkBit配置接口.md) | [hawkBit configuration API](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html) |  |  |
| 　　[hawkBit 事件 API](../firmware_update/P030_hawkBit事件接口.md) | [hawkBit event API](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html) |  |  |

### 2.2.11\_工具链抽象（Toolchain abstraction）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 工具链抽象 | [Toolchain abstraction](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html) |  |  |

### 2.2.12\_USB 设备控制器 API（USB Device Controller API）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| USB 设备控制器 API | [USB Device Controller API](../usb/P152_旧版USB控制器驱动API.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |

### 2.2.13\_USB 设备核心 API（USB Device Core API）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| USB 设备核心 API | [USB Device Core API](../usb/P155_旧版USB设备栈核心API.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.5.0) |

### 2.2.14\_USB-C 设备 API（USB-C Device API）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| USB-C 设备 API | [USB-C Device API](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　用电端回调 | [Sink_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html) |  |  |
| 　供电端回调 | [Source_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html) |  |  |

### 2.2.15\_工具（Utilities）

| 中文名称（缩进表示层级） | 英文原名（API） | 版本（Version） | 自哪个 Zephyr 版本提供（Available in Zephyr Since） |
| --- | --- | --- | --- |
| 工具 | [Utilities](https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html) |  |  |
| 　Base64 | [Base64](../base64_reference/P001_Base64编解码接口.md) |  |  |
| 　位反转操作 | [Bit Reverse Operations](../checksum_reference/P004_位反转接口.md) |  |  |
| 　固定开销字节填充（COBS） | [COBS (Consistent Overhead Byte Stuffing)](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html) |  |  |
| 　数字信号处理（DSP） | [DSP (Digital Signal Processing)](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　　基本数学函数 | [Basic Math Functions](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic.html) |  |  |
| 　　　向量绝对值 | [Vector Absolute Value](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html) |  |  |
| 　　　向量加法 | [Vector Addition](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html) |  |  |
| 　　　向量限幅 | [Vector Clipping](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html) |  |  |
| 　　　向量点积 | [Vector Dot Product](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html) |  |  |
| 　　　向量乘法 | [Vector Multiplication](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html) |  |  |
| 　　　向量取负 | [Vector Negate](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html) |  |  |
| 　　　向量偏置 | [Vector Offset](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html) |  |  |
| 　　　向量缩放 | [Vector Scale](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html) |  |  |
| 　　　向量移位 | [Vector Shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html) |  |  |
| 　　　向量减法 | [Vector Subtraction](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html) |  |  |
| 　　　向量按位与 | [Vector bitwise AND](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html) |  |  |
| 　　　向量按位非 | [Vector bitwise NOT](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html) |  |  |
| 　　　向量按位或 | [Vector bitwise OR](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__or.html) |  |  |
| 　　　向量按位异或 | [Vector bitwise XOR](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html) |  |  |
| 　　浮点／定点移位转换函数 | [Float/Fixed point shift conversion functions](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__utils__shifts.html) |  |  |
| 　　　定点转浮点 | [Fixed to Float point conversions](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html) |  |  |
| 　　　浮点转定点 | [Float to Fixed point conversions](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html) |  |  |
| 　　打印 Q 格式值的辅助宏 | [Helper macros for printing Q values.](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html) |  |  |
| 　数据结构 API | [Data Structure APIs](https://docs.zephyrproject.org/latest/doxygen/html/group__datastructure__apis.html) |  |  |
| 　　平衡红黑树 | [Balanced Red/Black Tree](../rbtree_reference/P001_红黑树公共接口.md) |  |  |
| 　　位数组 | [Bit array](../bitarray_reference/P001_位数组公共接口.md) | 1.0.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.6.0) |
| 　　并查集 | [Disjoint-set](../unionfind_reference/P001_并查集公共接口.md) |  |  |
| 　　双向链表 | [Doubly-linked list](../dlist_reference/P001_双向链表公共接口.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　带标志的单向链表 | [Flagged Single-linked list](../sflist_reference/P001_带标志单向链表公共接口.md) |  |  |
| 　　散列表 | [Hashmap](../hashmap_reference/P001_哈希映射公共接口.md) |  |  |
| 　　　散列函数 | [Hash Functions](../hashmap_reference/P019_哈希函数公共接口.md) |  |  |
| 　　　散列表实现 | [Hashmap Implementations](../hashmap_reference/P011_哈希映射实现概览.md) |  |  |
| 　　[多生产者单消费者（MPSC）数据包缓冲区 API](../intercore_reference/P166_MPSC数据包缓冲区接口.md) | [MPSC (Multi producer, single consumer) packet buffer API](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__buf.html) |  |  |
| 　　　[MPSC 数据包头](../intercore_reference/P172_MPSC数据包描述接口.md) | [MPSC (Multi producer, single consumer) packet header](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__packet.html) |  |  |
| 　　　[MPSC 数据包缓冲区标志](../intercore_reference/P167_MPSC数据包缓冲区标志.md) | [MPSC packet buffer flags](https://docs.zephyrproject.org/latest/doxygen/html/group__MPSC__PBUF__FLAGS.html) |  |  |
| 　　[MPSC 无锁队列 API](../intercore_reference/P158_MPSC无锁队列接口.md) | [MPSC Lockfree Queue API](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__lockfree.html) |  |  |
| 　　最小堆 | [Min-heap](../minheap_reference/P001_值最小堆公共接口.md) |  |  |
| 　　引用最小堆 | [Reference min-heap](../minheap_reference/P005_引用最小堆公共接口.md) |  |  |
| 　　环形缓冲区 API | [Ring Buffer APIs](../ringbuffer_reference/P001_环形缓冲区公共接口.md) |  |  |
| 　　环形队列 | [Ring queue](../ringq_reference/P001_环形队列公共接口.md) |  |  |
| 　　[单生产者单消费者（SPSC）数据包缓冲区 API](../intercore_reference/P150_SPSC数据包缓冲区接口.md) | [SPSC (Single producer, single consumer) packet buffer API](https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__buf.html) |  |  |
| 　　　[SPSC 数据包缓冲区标志](../intercore_reference/P157_SPSC数据包缓冲区标志.md) | [SPSC packet buffer flags](https://docs.zephyrproject.org/latest/doxygen/html/group__SPSC__PBUF__FLAGS.html) |  |  |
| 　　[SPSC API](../intercore_reference/P163_SPSC无锁队列接口.md) | [SPSC API](https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__lockfree.html) |  |  |
| 　　单向链表 | [Single-linked list](../slist_reference/P001_单向链表公共接口.md) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.2.0) |
| 　格式化输出 API | [Formatted Output APIs](../cbprintf_reference/P001_回调格式化输出接口.md) |  |  |
| 　　打包转换标志 | [Package convert flags](../cbprintf_reference/P014_格式化包转换标志.md) |  |  |
| 　　打包标志 | [Package flags](../cbprintf_reference/P013_格式化包创建标志.md) |  |  |
| 　　cbvprintf 处理标志 | [cbvprintf processing flags.](https://docs.zephyrproject.org/latest/doxygen/html/group__Z__CBVPRINTF__PROCESS__FLAGS.html) |  |  |
| 　JavaScript 对象表示法（JSON） | [JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__json.html) | 1.0.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.10.0) |
| 　　JSON Web 令牌（JWT） | [JSON Web Token (JWT)](../crypto/P030_JWT构建与签名接口.md) |  |  |
| 　线性范围 | [Linear Range](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html) | 1.0.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v3.3.0) |
| 　整数以 2 为底对数（Ilog2）函数 | [Math Ilog2 Functions](../numeric_reference/P005_整数二进制对数公共接口.md) |  |  |
| 　数学插值函数 | [Math Interpolation Functions](../interpolation_reference/P001_插值公共接口.md) |  |  |
| 　附加数学函数 | [Math extras](../math_reference/P001_数学辅助公共接口.md) | 1.0.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　导航 | [Navigation](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html) |  |  |
| 　引用计数 | [Reference counting](../sysref_reference/P001_引用计数接口.md) | 0.1.0 |  |
| 　系统 I/O API | [System I/O APIs](../device_reference/P017_系统IO公共接口.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v1.0.0) |
| 　　内存位操作 API | [Memory bit manipulation APIs](../device_reference/P020_内存位操作接口.md) |  |  |
| 　　内存映射寄存器 I/O API | [Memory-mapped register I/O APIs](../device_reference/P019_内存映射寄存器IO接口.md) |  |  |
| 　　端口 I/O API | [Port I/O APIs](../device_reference/P018_端口IO接口.md) |  |  |
| 　时间工具 API | [Time Utility APIs](../timeutil_reference/P001_时间工具接口概览.md) | 1.0.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.0.0) |
| 　　时间表示 API | [Time Representation APIs](../timeutil_reference/P002_时间表示接口.md) |  |  |
| 　　时间同步 API | [Time Synchronization APIs](../timeutil_reference/P003_时间同步接口.md) |  |  |
| 　　时间单位辅助接口 | [Time Units Helpers](../timeutil_reference/P007_时间单位辅助接口.md) |  |  |
| 　　timespec 工具 API | [Timespec Utility APIs](../timeutil_reference/P008_timespec时间工具接口.md) |  |  |
| 　通用唯一标识符（UUID） | [UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__uuid.html) | 0.8.0 | [v4.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0) |
| 　工具函数 | [Utility Functions](../util_reference/P001_通用工具公共接口.md) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v2.4.0) |

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：API状态与指南](P001_API状态与指南.md) · [本模块主线目录](../reading/api_guides.md) · [全部主线](../reading/README.md) · [下一篇：API术语](P003_API术语.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：API状态与指南](P001_API状态与指南.md) · [下一章：API术语](P003_API术语.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
