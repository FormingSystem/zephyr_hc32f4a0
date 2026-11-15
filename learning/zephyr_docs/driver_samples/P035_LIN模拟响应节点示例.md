---
id: learning.zephyr-docs.driver_samples.page-35
title: LIN模拟响应节点示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lin/ncv7430_responder/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lin-ncv7430-responder"></a>

# 第35章\_LIN模拟响应节点示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lin/ncv7430_responder/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 35.1\_概览（Overview）

本例通过模拟NCV7430 LED控制器在LIN总线一侧的行为，演示局部互联网络（Local Interconnect Network，LIN）API的响应节点模式（Responder Mode）。真实NCV7430协议的更多说明见[NCV7430数据手册](https://www.onsemi.com/pdf/datasheet/ncv7430-d.pdf)。

LIN控制器作为响应节点，对[NCV7430命令节点示例](P034_LIN灯光控制器示例.md#lin-ncv7430)使用的相同帧ID作出反应：保存`Set_LED_Control`（0x23）和`Set_Color`（0x24）帧写入的LED颜色／控制数据，并针对`Commander_Command`／`Responder_Response`（0x3C／0x3D）读请求，返回最近一次被要求设置的颜色。

这样，不需要真实的NCV7430芯片，只要两块开发板接到同一LIN总线，就能测试上述命令节点示例，或测试其他发送相同帧ID的LIN命令节点。

**注意：**本例没有安装LIN接收过滤器（RX Filter），即不调用[`lin_set_rx_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga7594e89b4fc3a018c1cd0010bd4a6ac1)，因此会检查总线上的每个帧头（Header）。这使模拟实现较为简单；在有许多其他节点的总线上，响应节点通常应只过滤出自己需要应答的帧ID。

<a id="requirements"></a>

## 35.2\_要求（Requirements）

- 两块支持LIN控制器的开发板，例如`ek_ra8m1/r7fa8m1ahecbd`：一块运行本例，另一块运行[NCV7430命令节点示例](P034_LIN灯光控制器示例.md#lin-ncv7430)。
- 每块板各配一个外部LIN收发器（Transceiver），例如两块[MikroElektronika LIN Click](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lin_click/doc/index.html#mikroe-lin-click-shield)，把两端的LIN总线和GND相连。

<a id="building-and-running"></a>

## 35.3\_构建与运行（Building and Running）

<a id="building-and-running-for-ek-ra8m1"></a>

### 35.3.1\_EK-RA8M1构建与运行（Building and Running for EK-RA8M1）

[RA8M1评估套件](https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#ek_ra8m1)没有板载LIN收发器。与[命令节点示例](P034_LIN灯光控制器示例.md#lin-ncv7430)相同，需要连接外部[MikroElektronika LIN Click](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lin_click/doc/index.html#mikroe-lin-click-shield)：

| EK-RA8M1端 | mikroe LIN Click端 |
| --- | --- |
| P609（TXD） | RXD |
| P610（RXD） | TXD |
| GND | GND |
| 3.3V | 3V3 |
| P601 | EN |
| P602 | WK |

**注意：**EK-RA8M1的P609（TXD）和3.3V之间还需要一个10 kΩ上拉电阻（Pull-up Resistor），以保证LIN总线具有正确的空闲状态。

把本板mikroe LIN Click扩展板（Shield）的LIN总线和GND，分别连接到第二块板扩展板的LIN总线和GND；第二块板运行命令节点示例。每块开发板独立为自己的收发器供电。

可以按下列方式为EK-RA8M1构建并运行：

> 译注——执行环境：以下原命令从已配置Zephyr环境的终端、Zephyr源码根目录执行；先核对板目标、扩展板配置与上述两端接线。构建成功后再烧录，失败时返回对应配置检查。

```bash
west build -b ek_ra8m1 --shield mikroe_lin_click samples/drivers/lin/ncv7430_responder
west flash
```

在第二块板上烧录[命令节点示例](P034_LIN灯光控制器示例.md#lin-ncv7430)。观察其控制台，确认设置的颜色被正确读回，以证明模拟响应节点用收到的颜色应答了读取请求。

<a id="sample-output"></a>

### 35.3.2\_示例输出（Sample Output）

```text
NCV7430 mock responder started
NCV7430 mock: LED color updated to R=0xFF G=0x00 B=0x00
NCV7430 mock: LED color updated to R=0x00 G=0xFF B=0x00
NCV7430 mock: LED color updated to R=0x00 G=0x00 B=0xFF
```

> 译注——模拟范围：这里验证的是LIN消息与保存颜色的响应行为，不是实际NCV7430灯光、电气特性或全部命令的仿真。所读[ncv7430_mock.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lin/ncv7430_responder/src/ncv7430_mock.c)以保存的颜色构造响应；两板读回正确不代表真实芯片的所有功能已被覆盖。本批没有进行总线通信测试。

<a id="see-also"></a>

## 35.4\_相关接口（See also）

[LIN控制器接口](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html)。


对应官方文档源码：[samples/drivers/lin/ncv7430_responder/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lin/ncv7430_responder/README.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P034_LIN灯光控制器示例.md) · [返回大纲](大纲.md) · [下一章](P036_DALI照明接口示例.md)
