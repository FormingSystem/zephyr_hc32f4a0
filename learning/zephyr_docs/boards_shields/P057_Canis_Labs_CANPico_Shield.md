---
id: learning.zephyr-docs.boards-shields.page-57
title: Canis Labs CANPico Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/canis_canpico/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="canis-labs-canpico-shield"></a>

<a id="canis-canpico"></a>

# 第57章\_Canis Labs CANPico扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/canis_canpico/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Canis Labs CANPico支持Microchip MCP2517FD或MCP2518FD独立CAN控制器及MCP2562FD高速CAN FD收发器，是套装在Raspberry Pi Pico系列上的“袜套式”（Sock）载板。

![官方原图：Canis_Labs_CANPico_SHIELD](images/canis_canpico.webp)

<a id="hardware"></a>

## 硬件（Hardware）


- MCP2517/2518FD

  > - 带SPI接口的外部CAN FD控制器
  > - 仲裁阶段比特率最高1 Mbit/s
  > - 数据阶段比特率最高8 Mbit/s
  > - CAN FD控制器支持CAN 2.0B模式，或CAN 2.0B与CAN FD混合模式
  > - 符合ISO 11898-1:2015
- MCP2562FD

  > - 针对2、5及8 Mbit/s的灵活数据速率CAN FD优化
  > - 最大传播延迟120 ns
  > - 满足ISO-11898-2及ISO-11898-5物理层要求
  > - 极低待机电流，典型5 µA
  > - VIO供电脚可直接连接I/O电压1.8～5.5 V的CAN控制器及微控制器
- 连接能力（Connectivity）

  > - 用于接入CAN终端电阻的跳线；原文写120W，后文写120 Ω，差异保留
  > - 用于使能连接到收发器的CAN TX线路的跳线
  > - CAN总线螺丝端子
  > - CAN控制器中断及帧起始信号连接GPIO
  > - 通过GPIO直接访问CAN收发器的TX及RX引脚
  > - 示波器或逻辑分析仪测试排针

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GP0</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP1</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP2</td>
<td>TRIG</td>
<td>可编程触发</td>
</tr>
<tr>
<td>GP3</td>
<td>STBY</td>
<td>收发器待机</td>
</tr>
<tr>
<td>GP4</td>
<td>SOF</td>
<td>Clock/SOF</td>
</tr>
<tr>
<td>GP5</td>
<td>IRQ</td>
<td>收发器中断</td>
</tr>
<tr>
<td>GP6</td>
<td>无（None）</td>
<td>SPI片选（CS）</td>
</tr>
<tr>
<td>GP7</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP8</td>
<td>SPI1_Rx</td>
<td>SPI接收RX</td>
</tr>
<tr>
<td>GP9</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP10</td>
<td>SPI1_SCK</td>
<td>SPI时钟（Clock）</td>
</tr>
<tr>
<td>GP11</td>
<td>SPI1_Tx</td>
<td>SPI发送TX</td>
</tr>
<tr>
<td>GP12</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP13</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP14</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP15</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP16</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP17</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP18</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP19</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP20</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP21</td>
<td>接收（Rx）</td>
<td>CAN接收数据RX</td>
</tr>
<tr>
<td>GP22</td>
<td>发送（Tx）</td>
<td>CAN发送数据TX</td>
</tr>
<tr>
<td>GP23</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP24</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP25</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP26</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP27</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP28</td>
<td>无（None）</td>
<td></td>
</tr>
</table>


- 测试排针

  > - TRIG：可编程触发输出
  > - TX：逻辑电平CAN发送数据
  > - RX：逻辑电平CAN接收数据
  > - H：原始CAN-Hi信号
  > - L：原始CAN-Low信号
- 电源（Power Supply）

  > - 3.3～5 V
- 组件（Components）

  > - TX使能跳线
  > - 120 Ω终端电阻跳线

更多Canis Labs CANPico信息见：


- [Canis Labs网站](https://canislabs.com/)
- [CANPico CAN总线扩展板](https://kentindell.github.io/canpico)
- [MCP2517FD数据手册](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/MCP2517FD-External-CAN-FD-Controller-with-SPI-Interface-20005688B.pdf)
- [MCP2518FD数据手册](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/External-CAN-FD-Controller-with-SPI-Interface-DS20006027B.pdf)
- [MCP2562FD数据手册](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/20005284A.pdf)

<a id="programming"></a>

## 编程（Programming）

在Zephyr应用中调用west build或CMake时设置--shield canis-canpico，例如：

```text
# From the root of the zephyr repository
west build -b rpi_pico --shield canpico samples/drivers/can/counter
west flash
```

## 译注

原文一处将终端电阻写作120W，另一处为120 Ω；来源差异已在正文标注。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [20005284A.pdf](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/20005284A.pdf)：HTTP Error 403: Forbidden。

---

[上一章](P056_Buydisplay_3.5_TFT_Touch_Shield_with_Arduino_adapter.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P058_DAC80508_Evaluation_Module.md)
