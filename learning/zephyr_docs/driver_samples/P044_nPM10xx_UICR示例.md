---
id: learning.zephyr-docs.driver_samples.page-44
title: nPM10xx_UICR示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/otp/npm10xx_uicr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="npm10xx_uicr"></a>

# 第44章\_nPM10xx\_UICR示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/otp/npm10xx_uicr/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 44.1\_概览（Overview）

Nordic nPM10系列电源管理集成电路（Power Management Integrated Circuit，PMIC）具有一次性可编程（One Time Programmable，OTP）的用户信息配置寄存器（User Information Configuration Registers，UICR）。

UICR由一组非易失性位（Non-volatile Bit）构成，用于定义部分PMIC控制寄存器的复位／默认值。这样可以减少启动序列中运行时软件需要介入的部分，使设计更加灵活、高效。

<a id="requirements"></a>

## 44.2\_要求（Requirements）

只要目标具有可与nPM10系列PMIC通信的I2C／双线接口（Two-wire Interface，TWI）总线，就可以运行本例。示例提供了[nRF54L15 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf54l15dk/doc/index.html#nrf54l15dk)覆盖文件供参考，假设它与**nPM1012 EK**按下表连接。

<a id="id1"></a>

nRF54L15 DK与nPM1012 EK接线表：

| nPM1012 EK引脚 | nRF54L15 DK引脚 |
| --- | --- |
| `SDA` | `P1.11` |
| `SCL` | `P1.12` |
| `VOUT` | P6 VDDM电流测量接口的VDD:nRF引脚（原标识：`P6 VDDM current measure, VDD:nRF pin`） |
| `GND` | `GND` |

此外，还必须在EK上完成以下设置：

1. 断开所有USB线缆。
2. 在**BUCK SET**排针上，用跳线把VSET连接到1.8V或3.0V。
3. 在**VDDIO REF**排针上，用跳线把VDDIO连接到BUCK。
4. 在**P1**排针上，用跳线连接VBAT和VBATIN。
5. 向**VBAT**连接器接入合适的电池。

<a id="building-and-running"></a>

## 44.3\_构建与运行（Building and Running）

按以下方式构建和烧录，将`nrf54l15dk/nrf54l15/cpuapp`替换为所用开发板目标：

> 译注——执行环境与配置前提：命令从已配置Zephyr环境的终端、Zephyr源码根目录执行。更换板目标还需要相应I2C、PMIC及子设备的设备树配置，不能只换板名。默认演练配置由随附prj.conf提供；先检查构建配置和设备条件，构建成功后再烧录，失败时返回对应配置检查。

```bash
west build -b nrf54l15dk/nrf54l15/cpuapp samples/drivers/otp/npm10xx_uicr
west flash
```

<a id="testing"></a>

## 44.4\_测试（Testing）

**注意：**出于安全考虑，默认启用演练编程（Dry-run Programming），对应[`CONFIG_OTP_NPM10XX_DRY_RUN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_NPM10XX_DRY_RUN)。如果确实要烧写UICR位，必须遵守器件数据手册对供电电压和结温（Junction Temperature）的要求。

> 译注——演练与真实编程：所读[prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/otp/npm10xx_uicr/prj.conf)同时启用OTP_PROGRAM和OTP_NPM10XX_DRY_RUN。演练会记录准备编程的位，不等于实际烧写已完成；后面的success日志也必须结合这个模式理解。拟写入的数据来自示例随附的[src/npm1012_otp.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/otp/npm10xx_uicr/src/npm1012_otp.h)，并非从读者设备自动推导出的目标配置。

烧录后，目标控制台应显示以下输出：

```text
[00:00:00.008,488] <wrn> main: This is a dry run - nothing will actually get programmed.
[00:00:00.017,227] <wrn> main: VBUS connection is required for UICR programming to proceed.
```

给VBUS供电后，即把USB线连接到EK的**USB PMIC**端口，编程流程会自动继续。演练期间，每个准备烧写的位索引都会记录到日志：

```text
[00:00:08.536,627] <inf> main: VBUS connected, parameters within range, starting UICR programming...
[00:00:08.546,227] <inf> otp_npm10xx: Dry run: would program UICR bit 6
[00:00:08.553,975] <inf> otp_npm10xx: Dry run: would program UICR bit 9
<...>
```

当驱动完成全部所需位的编程流程后，会打印以下消息：

```text
[00:00:08.655,851] <inf> main: UICR programming success. Remove VBUS...
```

一旦移除VBUS，微控制器（Microcontroller，MCU）就会向PMIC发出软件复位（Software Reset），并使MCU自身也经历断电再上电（Power Cycle）。

```text
[00:00:11.666,473] <inf> main: VBUS disconnected, resetting PMIC...
```

> 译注——演练仍有硬件动作：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/otp/npm10xx_uicr/src/main.c)在检测到VBUS后读取电压和芯片温度，满足条件才进入otp_program；其等待VBUS断开并调用PMIC复位的后续路径没有按dry-run模式跳过。因此“不实际编程UICR位”不表示整个示例不与硬件交互或不会复位供电。本批仅翻译并核对源码，没有连接电池／USB、烧录、烧写OTP或执行复位。


对应官方文档源码：[samples/drivers/otp/npm10xx_uicr/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/otp/npm10xx_uicr/README.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P043_OTP存储器示例目录.md) · [返回大纲](大纲.md) · [下一章](P045_HD44780液晶控制器示例.md)
