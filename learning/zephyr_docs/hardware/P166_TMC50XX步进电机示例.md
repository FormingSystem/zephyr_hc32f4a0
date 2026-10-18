---
id: learning.zephyr-docs.hardware.motorsamp-2
title: TMC50XX步进电机示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/stepper/tmc50xx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="tmc50xx"></a>

# 第166章\_TMC50XX步进电机示例

原文：[TMC50XX stepper](https://docs.zephyrproject.org/latest/samples/drivers/stepper/tmc50xx/README.html)。读取日期：2026-10-13，`latest`。

## 166.1\_说明（Description）

本示例按照 `CONFIG_PING_PONG_N_REV` 配置，使 **步进电机（Stepper Motor）**周期性地顺时针和逆时针旋转。原文的示例摘要还说明它展示运行时的速度改变。

## 166.2\_参考资料（References）

- [TMC5041数据手册，修订版1.16](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5041_datasheet_rev1.16.pdf)。
- [TMC5072数据手册，修订版1.26](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5072_datasheet_rev1.26.pdf)。

## 166.3\_接线（Wiring）

本示例使用 TMC5072 **引出板（Breakout Board，BOB）**，通过 **串行外设接口（Serial Peripheral Interface，SPI）**控制。开发板的 **设备树（Devicetree）**必须为步进电机节点定义名为 `stepper` 的别名（Alias）。

## 166.4\_构建与运行（Building and Running）

应用使步进电机旋转，并将事件输出到控制台（Console）。它需要 TMC50XX 步进驱动器，应能在具有 SPI 外设接口的平台上工作，不能在 QEMU 模拟器中运行。

译注：以下官方命令在已配置 Zephyr 开发环境的终端中执行，工作目录为 Zephyr 源码根目录。示例源码由官方仓库提供，west 生成构建产物，`west flash` 将固件烧录到开发板。

```bash
# From the root of the zephyr repository
west build -b nucleo_g071rb samples/drivers/stepper/tmc50xx
west flash
```

## 166.5\_示例输出（Sample Output）

日志报告示例启动、设备名称，以及步数完成后回调函数改变方向的事件；`<repeats endlessly>` 表示持续重复。

```text
Starting tmc50xx stepper sample
stepper is 0x8007240, name is tmc_stepper@0
stepper_callback steps completed changing direction
stepper_callback steps completed changing direction
stepper_callback steps completed changing direction

<repeats endlessly>
```

## 166.6\_相关接口

[步进电机应用程序编程接口（Application Programming Interface，API）](P229_步进电机接口目录.md) · [官方示例源码与应用配置](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/stepper/tmc50xx)

[上一章：通用步进电机示例](P165_通用步进电机示例.md) · [下一章：TMCM3216步进电机示例](P167_TMCM3216步进电机示例.md) · [返回大纲](大纲.md)
