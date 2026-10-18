---
id: learning.zephyr-docs.timer_reference.clocksample-118
title: MicrochipXEC时钟控制示例
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/clock_control_xec/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第118章\_MicrochipXEC时钟控制示例

原文：[Microchip XEC (MEC15xx/MEC172x) clock control driver sample application](https://docs.zephyrproject.org/latest/samples/drivers/clock_control_xec/README.html)。读取日期：2026-10-13，`latest`。

本示例面向 Microchip XEC 的 MEC15xx／MEC172x，演示通过设备树（Devicetree）配置32 kHz时钟选项。应用输出硬件配置，并调用部分时钟控制驱动应用程序编程接口（Clock Control Driver API）。

## 118.1\_构建、运行与观察引脚

示例可通过 west 在开发板上构建并执行。原页没有提供具体构建命令。

原文说明一般无需引脚配置，但使用通用输入输出（General-Purpose Input/Output，GPIO）引脚`GPIO014`指示进入／退出，使用`GPIO060`输出48 MHz锁相环（Phase-Locked Loop，PLL）时钟。

`GPIO221`的复用功能1（Alternate Function 1）为`32KHZ_OUT`，可在6915组件板（Assembly 6915）的`JP7`第5脚监测。

## 118.2\_内部硅32 kHz振荡器

选择内部硅振荡器（Internal Silicon Oscillator）时，MEC172x 的6915组件板采用以下跳线（Jumper）配置：

- `JP1`第2脚接地（Ground，GND），即将 MEC172x 的`XTAL1`引脚接地。文中`XTAL1`和`XTAL2`保留芯片晶体连接引脚（Crystal Pin）的标识。
- `JP2`不安装跳线。

## 118.3\_双端32 kHz晶体

选择双端晶体（Dual-ended Crystal）时，MEC172x 的6915组件板：

- `JP1`第1—2脚安装跳线，将晶体器件位号（Reference Designator）`Y1`的第1脚连接到 MEC172x 的`XTAL1`。
- `JP2`第2—3脚安装跳线，将晶体`Y1`第2脚连接到 MEC172x 的`XTAL2`。

在6906底板（Assembly 6906，Baseboard）上，**移除跳线连接器`JP121`上的跳线**，防止器件位号`U15`的32 kHz、50%占空比（Duty Cycle）波形耦合到6915组件板的`JP2`。

## 118.4\_外部单端波形输入XTAL2

将外部单端（External Single-ended）32 kHz波形送入 MEC172x 的`XTAL2`时，6915组件板：

- `JP1`第2脚接地，使`XTAL1`接地。
- `JP2`第1—2脚安装跳线，将外部32 kHz信号连接到`XTAL2`。

6906底板的`JP121`第3—4脚安装跳线，将`U15`的32 kHz输出连接到`XTAL2_32KHZ_IN`信号。该信号被布线到6915组件板上 MEC172x 的`XTAL2`引脚。

## 118.5\_外部单端波形输入32KHZ_IN

将外部单端32 kHz波形送入 MEC172x 的`32KHZ_IN`引脚时，6915组件板：

- `JP1`第2脚接地，使`XTAL1`接地。
- 移除`JP2`跳线。

6906底板的`JP121`第1—2脚安装跳线，将`U15`的32 kHz输出连接到6915组件板上 MEC172x 的`32KHZ_IN`引脚。

以上四节分别对应不同的时钟源方案，应按所选方案核对对应组件板上的跳线，不是把四组设置依次叠加。

## 118.6\_示例输出说明

原页本节的代码框没有实际寄存器数值，只包含关于`VBAT`和`PCR`寄存器的文字说明，按原样保留：

```text
Prints MEC172x VBAT and PCR register pertaining to power on status and
clock control.
```

其含义为：输出 MEC172x 中与上电状态（Power-on Status）及时钟控制有关的`VBAT`和`PCR`寄存器。原页未给出这两个标识的展开名称或具体输出值，此处保留硬件标识。

---

[上一章：LiteX时钟控制示例](P117_LiteX时钟控制示例.md) · [下一章：LiteX时钟控制接口](P119_LiteX时钟控制接口.md) · [返回大纲](大纲.md)
