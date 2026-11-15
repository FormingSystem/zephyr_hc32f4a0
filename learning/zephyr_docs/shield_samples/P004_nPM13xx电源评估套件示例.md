---
id: learning.zephyr-docs.shield-samples.page-4
title: nPM13xx电源评估套件示例
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/npm13xx_ek/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="npm13xx_ek"></a>

# 第4章\_nPM13xx 评估套件（nPM13xx EK）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/npm13xx_ek/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/npm13xx_ek/index.rst/..)

<a id="overview"></a>

## 4.1 概述（Overview）

本示例用于评估 [nPM1300 EK](https://docs.zephyrproject.org/latest/boards/shields/npm1300_ek/doc/index.html#npm1300-ek) 和 [nPM1304 EK](https://docs.zephyrproject.org/latest/boards/shields/npm1304_ek/doc/index.html#npm1304-ek)。它演示稳压器 API 的动态电压调节（Dynamic Voltage Scaling，DVS）功能：一次稳压器 API 调用即可切换已配置的 GPIO，从而在选定电压级别或稳压器模式之间切换。

> 译注——术语：BUCK 是降压转换器（Buck Converter），LDO 是低压差稳压器（Low-Dropout Regulator）。这里的 DVS 既可以选择电压，也可以按预先配置的 GPIO 组合切换稳压器启停或模式，并非每次都由软件写入一个新的电压数值。

示例还提供 Shell 接口，用于操作 nPM1300 和 nPM1304 电源管理集成电路（Power Management Integrated Circuit，PMIC）的以下功能：

- 稳压器（Regulators）：BUCK1／2、LDO1／2

- 通用输入输出（GPIO）

<a id="requirements"></a>

## 4.2 硬件与配置要求（Requirements）

扩展板需要接到具有 Arduino I2C 接口的主开发板。PMIC 的 GPIO3 用作中断输出，GPIO1 和 GPIO2 配置为稳压器模式控制引脚，由 MCU 软件通过 DVS 控制。

此外，PMIC 的 VDDIO 引脚应连接到适当的参考电压。

例如，连接 nRF52 系列开发套件（Development Kit，DK）时，接线如下：

> | nPM13xx EK 引脚 | SDA | SCL | GPIO1 | GPIO2 | GPIO3 | VDDIO | GND |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | nRF52 DK 引脚 | P0.26 | P0.27 | P0.17 | P0.18 | P0.22 | VDD | GND |

<a id="building-and-running"></a>

## 4.3 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，使用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块和工具链，再核对本页指定主开发板、扩展板、接线与配置。设备 Shell 命令在目标板串口执行。遇到构建或设备就绪错误，先回查所选 board／shield 与接线；下方日志是官方预期示例。本次仅核对文档与源码，未构建、烧录、擦写存储或进行实板测量。

示例按可适配任意平台设计；需在 `npm13xx.overlay` 文件中更新连接到 nPM13xx EK 的主机 GPIO 引用，使其符合所用硬件。

> 译注——文件名差异：原文使用 npm13xx.overlay 这一名称；本次源码实际提供 npm1300.overlay、npm1304.overlay，以及 boards/nrf52dk_nrf52832.overlay。应按所选扩展板和主开发板检查当前构建使用的覆盖文件（Devicetree Overlay），不能照原文名称另造一个未接入构建的文件。

例如，为 nRF52 DK 和 nPM1300 EK 构建时，可使用以下命令：

```text
west build -b nrf52dk/nrf52832 --shield npm1300_ek samples/shields/npm13xx_ek
```

<a id="testing"></a>

## 4.4 测试（Testing）

烧录示例固件后，连接 Shell 接口。初始化成功时，可以看到 nPM13xx PMIC 状态消息，包括充电器状态、电池电压、电流和温度。按下和释放 EK 上的 SHPHLD 按钮会产生中断，相应事件也会打印到 Shell。

按下主 DK 上的专用按钮，在 nRF52 系列 DK 上为 Button 1，会依次循环 DVS 状态。

> 译注——按键行为：main.c 以 100 ms 间隔轮询 sw0，仅在逻辑按下状态的上升沿将 DVS 状态加一并对 4 取模；释放不会再前进一个状态。状态消息的计数条件是 ++count > 2000/100，约每 21 轮输出一次，另需加上处理时间。

> | DVS 状态（GPIO1 \| GPIO2 电平） | BUCK2 模式 | LDO1 模式 | LDO2 模式 |
> | --- | --- | --- | --- |
> | 0（HIGH \| HIGH） | 关闭（OFF） | 关闭（OFF） | 关闭（OFF） |
> | 1（LOW \| HIGH） | 保持模式开启（ON retention） | 关闭（OFF） | 关闭（OFF） |
> | 2（HIGH \| LOW） | 关闭（OFF） | 开启（ON） | 开启（ON） |
> | 3（LOW \| LOW） | PWM 模式开启（ON PWM） | 开启（ON） | 开启（ON） |

注意（Note）

nRF52 系列 DK 上，DVS 引脚还用于板载 LED1 和 LED2，因此可以直观看到状态：相应引脚为低电平（LOW）时，LED 点亮。

<a id="regulators"></a>

## 4.5 稳压器（Regulators）

`regulator` Shell 接口提供多个子命令，用于测试 PMIC 内部稳压器。以下是一些命令示例。

> 译注——命令差异：当前通用 regulator_shell.c 注册的是 vset、vget；下方原文末两条 regulator set/get 与源码不符。对应当前版本应使用 regulator vset BUCK1 2.35V 2.45V 和 regulator vget BUCK1。前面的 vset BUCK2 后紧接 vget BUCK1，读取的是另一通道，不能用该输出验证 BUCK2 的设置。

```text
# list all the supported voltages by BUCK1
uart:~$ regulator vlist BUCK1
1.000 V
1.100 V
...
```

```text
# enable BUCK2
uart:~$ regulator enable BUCK2
# disable BUCK2
uart:~$ regulator disable BUCK2
```

```text
# set BUCK2 voltage to exactly 2V
uart:~$ regulator vset BUCK2 2V
# obtain the actual BUCK1 configured voltage
uart:~$ regulator vget BUCK1
1.800 V
# set BUCK1 voltage to a value between 2.35V and 2.45V
uart:~$ regulator set BUCK1 2.35V 2.45V
# obtain the actual BUCK1 configured voltage
uart:~$ regulator get BUCK1
2.400 V
```

> 译注——源码入口：[src/main.c](../../../samples/shields/npm13xx_ek/src/main.c)；[CMakeLists.txt](../../../samples/shields/npm13xx_ek/CMakeLists.txt)；[prj.conf](../../../samples/shields/npm13xx_ek/prj.conf)；[npm1300.overlay](../../../samples/shields/npm13xx_ek/npm1300.overlay)；[npm1304.overlay](../../../samples/shields/npm13xx_ek/npm1304.overlay)；[boards/nrf52dk_nrf52832.overlay](../../../samples/shields/npm13xx_ek/boards/nrf52dk_nrf52832.overlay)；[drivers/regulator/regulator_shell.c](../../../drivers/regulator/regulator_shell.c)。本地源码使用相对链接；上游快照摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/shields/npm13xx_ek/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/npm13xx_ek/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/shields/npm13xx_ek/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、擦写存储或连接设备。

[上一章](P003_LMP90100扩展板示例目录.md) · [返回大纲](大纲.md) · [下一章](P005_nPM2100电源评估套件示例.md)
