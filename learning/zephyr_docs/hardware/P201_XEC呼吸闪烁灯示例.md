---
id: learning.zephyr-docs.hardware.ledrest-4
title: XEC呼吸闪烁灯示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/xec/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="led-xec"></a>

# 第201章\_XEC呼吸闪烁灯示例

原文：[Breathing-blinking LED (BBLED)](https://docs.zephyrproject.org/latest/samples/drivers/led/xec/README.html)。读取日期：2026-10-13，`latest`。

## 201.1\_概述（Overview）

本示例测试 Microchip 的 `led-xec` 驱动，它使用 **呼吸闪烁发光二极管（Breathing-Blinking Light-Emitting Diode，BBLED）**控制器。**片上系统（System on Chip，SoC）**的硬件设计固定了每个 BBLED 控制器所能控制的一个 **通用输入输出（General-Purpose Input/Output，GPIO）**引脚。

| 芯片系列 | 控制器实例 | 固定GPIO |
| --- | --- | --- |
| MEC15xx、MEC172x | BBLED 0 | `0156` |
| MEC15xx、MEC172x | BBLED 1 | `0157` |
| MEC15xx、MEC172x | BBLED 2 | `0153` |
| MEC172x | BBLED 3，第四个实例 | `0035` |

译注：表中编号保留官方写法与前导零。

## 201.2\_测试图案（Test Pattern）

依次处理每个 LED：点亮、关闭、按亮 0.1 秒/灭 0.1 秒闪烁、再按亮 1 秒/灭 1 秒闪烁。

## 201.3\_mec172xevb_assy6906评估板跳线

以下跳线（Jumper）与引脚标识来自官方原页，适用于该评估板。

**BBLED0，GPIO `0156`：**用导线连接 `JP71-11` 与 `J47-3`，把 GPIO `0156` 接到板载 LED4。确保 `JP54 1-2` 和 `JP21 4-5` 上没有跳线。

**BBLED1，GPIO `0157`：**用导线连接 `JP71-12` 与 `J48-3`，连接到板载 LED5。确保 `JP54 3-4` 和 `JP21 16-17` 上没有跳线。

译注：BBLED1 的小标题写 GPIO `0157`，但同一条原文接线说明写的是“Connect GPIO 0156 to board LED5”。这里保留其 `JP71-12` 至 `J48-3` 的端点，并明确记录两处 GPIO 号矛盾；不能把它们当成已核实一致的接线说明。

**BBLED2，GPIO `0153`：**用导线连接 `JP71-5` 与 `JP146-5`，把 GPIO `0153` 接到板载 LED7。

原文说明，不装跳线时，`JP146-5` 连接到 MEC172x 的 `VCI_OUT1` 输出信号。通过把 `VCI_IN1` 输入信号拉高，将 `VCI_OUT1` 置高：在 `J55 3-4` 安装跳线，经 100 kΩ 上拉电阻（Pull-up Resistor）把 `VCI_IN1` 接到 VBAT 电源轨（Power Rail）。这要求 VBAT 已连接到 VTR 电源轨或其他电源。

**BBLED3，GPIO `0035`：**用导线连接 `JP67-19` 与 `JP146-1`，把 GPIO `0035` 接到板载 LED7。确保 `JP79 17-18` 上没有跳线。

原文说明，不装跳线时，`JP146-1` 连接到 MEC172x 的 `VCI_OUT2` 输出信号。通过把 `VCI_IN2` 输入信号拉高，将 `VCI_OUT2` 置高：在 `J55 5-6` 安装跳线，经 100 kΩ 上拉电阻把 `VCI_IN2` 接到 VBAT。这同样要求 VBAT 已连接到 VTR 或其他电源。

译注：VCI_IN1/2、VCI_OUT1/2、VBAT、VTR 为原页使用的芯片信号和供电网络标识，此处保留名称及原文给出的连接关系。

## 201.4\_mec15xxevb_assy6853评估板跳线

| 控制器与GPIO | 按原文添加跳线 | 按原文移除跳线 |
| --- | --- | --- |
| BBLED0，GPIO `0156` | `JP41 1-2`，连接到板载 LED2。 | `JP31 13-14`。 |
| BBLED1，GPIO `0157` | `JP41 3-4`，连接到板载 LED3。 | `JP31 15-16`。 |
| BBLED2，GPIO `0153` | `JP41 3-4`，连接到板载 LED4。 | `JP31 17-18`。 |

译注：原页在 BBLED1 与 BBLED2 两条说明中重复写了 `JP41 3-4`，却描述了不同 GPIO 和 LED。表中保留该差异；原页未提供足以在此确定替代跳线端点的信息。

## 201.5\_构建与运行（Building and Running）

本示例可在已连接这些 LED 的开发板上构建和执行。必须在 **设备树源（Devicetree Source，DTS）**中正确描述它们。芯片设计已把每个呼吸闪烁控制器固定连接到一个 GPIO，因此 `bbled` 节点的 **引脚控制（Pin Control，PINCTRL）**属性必须设置为对应的正确 GPIO。

[LED应用程序编程接口（Application Programming Interface，API）](P202_LED公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/led/xec)

[上一章：SX1509B三色LED示例](P200_SX1509B三色LED示例.md) · [下一章：LED公共接口](P202_LED公共接口.md) · [返回大纲](大纲.md)
