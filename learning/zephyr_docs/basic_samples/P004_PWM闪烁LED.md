---
id: learning.zephyr-docs.basic-samples.basic-pwm
title: PWM闪烁LED
kind: reference
status: maintained
domains: [zephyr, development, samples]
source_url: https://docs.zephyrproject.org/latest/samples/basic/blinky_pwm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_PWM闪烁LED

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/basic/blinky_pwm/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/blinky_pwm)。本仓库的[源码参照](../../../samples/basic/blinky_pwm/src/main.c)采用相对链接；参照版本不自动等同于官网版本。

<a id="pwm-blinky"></a>
<a id="overview"></a>

## 4.1\_概述

本应用使用[脉宽调制（Pulse Width Modulation，PWM）API](https://docs.zephyrproject.org/latest/hardware/peripherals/pwm.html#pwm-api)闪烁LED。基于GPIO的示例见[Blinky](https://docs.zephyrproject.org/latest/samples/basic/blinky/README.html#blinky)。

LED最初以1 Hz频率闪烁，每4秒将频率加倍，直到128 Hz；随后每4秒将频率减半，直到回到1 Hz，完成一次闪烁循环。这种先加快、再减慢的循环会持续重复。

某些PWM硬件无法将周期设置为1秒，以实现1 Hz闪烁频率。示例在启动时根据硬件能力自校准：适当减小最大PWM周期，直到找到硬件支持的值。

<a id="requirements"></a>

## 4.2\_要求

开发板必须有连接到PWM输出通道的LED。控制该LED的PWM必须通过`pwm_led0`[设备树别名](https://docs.zephyrproject.org/latest/build/dts/index.html#dt-guide)配置，通常位于[`BOARD.dts`文件](https://docs.zephyrproject.org/latest/build/dts/intro-input-output.html#devicetree-in-out-files)中。

<a id="wiring"></a>

## 4.3\_接线

如果`pwm_led0`指向的硬件已经连接到板载LED，则不需要额外接线。下列情况需要手动连接：

| 开发板（Board） | 接线（Wiring） |
| --- | --- |
| [Nucleo F401RE](https://docs.zephyrproject.org/latest/boards/st/nucleo_f401re/doc/index.html#nucleo_f401re) | 将PWM2（PA0）连接到LED。 |
| [Nucleo L476RG](https://docs.zephyrproject.org/latest/boards/st/nucleo_l476rg/doc/index.html#nucleo_l476rg) | 将PWM2（PA0）连接到LED。 |
| [STM32F4 Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32f4_disco/doc/index.html#stm32f4_disco) | 将PWM2（PA0）连接到LED。 |
| [Nucleo F302R8](https://docs.zephyrproject.org/latest/boards/st/nucleo_f302r8/doc/index.html#nucleo_f302r8) | 将PWM2（PA0）连接到LED。 |
| [Nucleo F103RB](https://docs.zephyrproject.org/latest/boards/st/nucleo_f103rb/doc/index.html#nucleo_f103rb) | 将PWM1（PA8）连接到LED。 |
| [Nucleo WB55RG](https://docs.zephyrproject.org/latest/boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.html#nucleo_wb55rg) | 将PWM1（PA8）连接到LED。 |
| [ESP32-DevKitC](https://docs.zephyrproject.org/latest/boards/espressif/esp32_devkitc/doc/index.html#esp32_devkitc) | 将GPIO2连接到LED。 |
| [ESP32-S2-Saola](https://docs.zephyrproject.org/latest/boards/espressif/esp32s2_saola/doc/index.html#esp32s2_saola) | 将GPIO2连接到LED。 |
| [ESP32-C3-DevKitM](https://docs.zephyrproject.org/latest/boards/espressif/esp32c3_devkitm/doc/index.html#esp32c3_devkitm) | 将GPIO2连接到LED。 |
| [i.MX943 EVK](https://docs.zephyrproject.org/latest/boards/nxp/imx943_evk/doc/index.html#imx943_evk) | 将PWM6（J47-6）连接到LED。 |
| [i.MX95 EVK](https://docs.zephyrproject.org/latest/boards/nxp/imx95_evk/doc/index.html#imx95_evk) | 将PWM2（R881）连接到LED。 |
| [i.MX8MM EVK](https://docs.zephyrproject.org/latest/boards/nxp/imx8mm_evk/doc/index.html#imx8mm_evk) | 将PWM3（J1001-47）连接到LED。 |
| [i.MX8MN EVK（Cortex-A53）](https://docs.zephyrproject.org/latest/boards/nxp/imx8mn_evk/doc/index.html#imx8mn_evk) | 将PWM3（J1001-47）连接到LED。 |
| [i.MX8MP EVK](https://docs.zephyrproject.org/latest/boards/nxp/imx8mp_evk/doc/index.html#imx8mp_evk) | 将PWM4（J21-32）连接到LED。 |

<a id="building-and-running"></a>

## 4.4\_构建与运行

为[nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)构建并烧录：

```shell
west build -b nrf52840dk/nrf52840 samples/basic/blinky_pwm
west flash
```

其他受支持开发板应相应替换`nrf52840dk/nrf52840`。烧录后，示例按前述方式闪烁LED，同时向开发板控制台打印信息。

<a id="see-also"></a>

## 4.5\_另请参阅

- [PWM API](../hardware/P255_PWM公共接口.md)

[上一章：按钮输入](P003_按钮输入.md) · [返回大纲](大纲.md) · [下一章：LED渐变](P005_LED渐变.md)
