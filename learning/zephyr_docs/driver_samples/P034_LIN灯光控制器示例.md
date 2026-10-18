---
id: learning.zephyr-docs.driver_samples.page-34
title: LIN灯光控制器示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lin/ncv7430/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lin-ncv7430"></a>

# 第34章\_LIN灯光控制器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lin/ncv7430/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 34.1\_概览（Overview）

本例演示通过局部互联网络（Local Interconnect Network，LIN）API使用NCV7430 LED控制器，控制红绿蓝（Red, Green, Blue，RGB）LED。NCV7430的更多信息见[NCV7430数据手册（Datasheet）](https://www.onsemi.com/pdf/datasheet/ncv7430-d.pdf)。

LIN控制器作为命令节点（Commander Node），向NCV7430发送命令以改变LED颜色。应用循环使用一组预定义颜色，并发送对应的LIN消息更新LED。

<a id="requirements"></a>

## 34.2\_要求（Requirements）

- 支持LIN控制器的开发板，例如`ek_ra8m1/r7fa8m1ahecbd`。
- 连接到LIN控制器引脚的NCV7430评估板，例如[skpang NCV7430转接板（Breakout Board）](https://www.skpang.co.uk/ncv7430-led-controller-breakout-board-p-5187.html)。

<a id="building-and-running"></a>

> 译注——厂商链接变更：2026-10-14核对时，原skpang转接板链接返回404。原引用保留供追溯，厂商当前产品入口为[NCV7430 LIN-Bus RGB LED Breakout Board](https://www.skpang.co.uk/products/ncv7430-lin-bus-rgb-led-breakout-baord)；这里只补充入口，不扩展翻译厂商网站。

## 34.3\_构建与运行（Building and Running）

<a id="building-and-running-for-ek-ra8m1"></a>

### 34.3.1\_EK-RA8M1构建与运行（Building and Running for EK-RA8M1）

[RA8M1评估套件（Evaluation Kit）](https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#ek_ra8m1)没有板载LIN收发器（Transceiver）。在EK-RA8M1上使用LIN总线时，需要连接外部[MikroElektronika LIN Click](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lin_click/doc/index.html#mikroe-lin-click-shield)收发器，原文接线如下：

| EK-RA8M1端 | mikroe LIN Click端 |
| --- | --- |
| P609（TXD） | RXD |
| P610（RXD） | TXD |
| GND | GND |
| 3.3V | 3V3 |
| P601 | EN |
| P602 | WK |

**注意：**EK-RA8M1的P609（TXD）和3.3V之间还需要一个10 kΩ上拉电阻（Pull-up Resistor），以保证LIN总线具有正确的空闲状态（Idle State）。

> 译注——执行前提：接线名称按原文保留，具体接口位置按上方板卡和扩展板文档确认。以下命令在已配置Zephyr开发环境的终端、Zephyr源码根目录执行；构建成功后再烧录，出现目标或设备配置错误时先核对所用版本的板目标、扩展板和LIN配置。

可以按下列方式为EK-RA8M1构建并运行本例：

```bash
west build -b ek_ra8m1 --shield mikroe_lin_click samples/drivers/lin/ncv7430
west flash
```

观察NCV7430评估板上的LED，确认应用按预定义颜色循环改变灯光。

<a id="sample-output"></a>

### 34.3.2\_示例输出（Sample Output）

```text
NCV7430 sample started
Set LED color: Red - read back actual color code: 0xFF0000
Set LED color: Green - read back actual color code: 0x00FF00
Set LED color: Blue - read back actual color code: 0x0000FF
```

> 译注——循环与读回：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lin/ncv7430/src/main.c)通过lin0别名选择设备，以19200波特运行，循环使用红、绿、蓝、黄、青、品红、白、黑八种颜色。每次设置后读回并比较，再休眠1000毫秒；原日志仅展示前三种颜色，不表示只有三个测试项。若读回颜色不符，程序另外打印不匹配提示。本批未连接收发器或控制实际LED。

<a id="see-also"></a>

## 34.4\_相关接口（See also）

[LIN控制器（LIN Controller）接口](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html)。


对应官方文档源码：[samples/drivers/lin/ncv7430/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lin/ncv7430/README.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P033_LIN示例目录.md) · [返回大纲](大纲.md) · [下一章](P035_LIN模拟响应节点示例.md)
