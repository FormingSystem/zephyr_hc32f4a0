---
id: learning.zephyr-docs.boards-shields.page-89
title: Microchip MCP2515 CAN bus shields
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mcp2515/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="microchip-mcp2515-can-bus-shields"></a>

<a id="mcp2515-shield"></a>

# 第89章\_Microchip MCP2515 CAN总线扩展板（Shields）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mcp2515/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr支持多种搭载Microchip [MCP2515](https://www.microchip.com/en-us/product/MCP2515)独立SPI CAN控制器的扩展板。

<a id="dfrobot-can-bus-shield-v2-0"></a>

## DFRobot CAN总线扩展板V2.0

<a id="overview"></a>

### 概述（Overview）

DFRobot CAN BUS扩展板采用Microchip MCP2515独立CAN控制器及高速CAN收发器，原文型号写JTA1050，资料链接为TJA1050。硬件接口兼容Arduino Uno R3。

![官方原图：DFRobot_CAN_BUS_V2_0_SHIELD](images/dfrobot_can_bus_v2_0.jpg)

<a id="hardware"></a>

### 硬件（Hardware）


- MCP2515

  > - 独立CAN 2.0B控制器
  > - 最高1 Mbit/s比特率
  > - 标准及扩展数据帧与远程帧
  > - 3个发送缓冲区TX
  > - 2个接收缓冲区RX
  > - 6个29位滤波器
  > - 2个29位掩码
  > - 中断输出
  > - 单次发送模式（One-shot Mode）
  > - 高速SPI，10 MHz
- TJA1050

  > - 完全兼容ISO 11898标准
  > - 高速，最高1 Mbaud
- 连接能力（Connectivity）

  > - 工业标准DB9 CAN端子
  > - CAN螺丝端子
  > - 集成SPI microSD卡槽，用于数据存储
  > - 兼容Arduino Uno R3的SPI接口

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>A0</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A1</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D0</td>
<td>接收（RX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D1</td>
<td>发送（TX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D2</td>
<td>GPIO_ACTIVE_LOW</td>
<td>MCP2515中断INT</td>
</tr>
<tr>
<td><code>D3</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D4</code></td>
<td>SPI-CS</td>
<td>MicroSD</td>
</tr>
<tr>
<td>D5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D6</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D7</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D8</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D9</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D10</td>
<td>SPI-CS</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D11</td>
<td>SPI-MOSI</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D12</td>
<td>SPI-MISO</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D13</td>
<td>SPI-CLK</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D14</td>
<td>I2C-SDA</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D15</td>
<td>I2C_SCL</td>
<td>仅外部排针</td>
</tr>
</table>


- 电源（Power Supply）

  > - 3.3～5 V
- 组件（Components）

  > - 电源开关
  > - 电源LED
  > - RX0BF指示LED
  > - RX1BF指示LED

更多DFRobot CAN-BUS V2.0扩展板信息见：


- [DFRobot网站](https://www.dfrobot.com/product-1444.html)
- [DFRobot CAN BUS V2.0扩展板原理图](https://github.com/DFRobot/DFRobot_MCP2515/blob/master/resources/doc/DFR0370%20CAN%20BUS%20sheild(V2.0).pdf)
- [MCP2515数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
- [TJA1050数据手册](https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf)

<a id="keyestudio-can-bus-shield-ks0411"></a>

## Keyestudio CAN总线扩展板KS0411

<a id="id1"></a>

### 概述（Overview）

Keyestudio CAN BUS扩展板采用Microchip MCP2515独立CAN控制器及MCP2551高速CAN收发器，硬件接口兼容Arduino Uno R3。

<a id="id9"></a>

![官方原图：Keyestudio CAN-BUS Shield (KS0411)](images/keyestudio_can_bus_ks0411.jpg)

Keyestudio CAN总线扩展板KS0411，图片来源：Keyestudio

<a id="id2"></a>

### 硬件（Hardware）


- MCP2515

  > - 独立CAN 2.0B控制器
  > - 最高1 Mbit/s比特率
  > - 标准及扩展数据帧与远程帧
  > - 3个发送缓冲区TX
  > - 2个接收缓冲区RX
  > - 6个29位滤波器
  > - 2个29位掩码
  > - 中断输出
  > - 单次发送模式（One-shot Mode）
  > - 高速SPI，10 MHz
- MCP2551

  > - 完全兼容ISO 11898标准
  > - 高速，最高1 Mbaud
- 连接能力（Connectivity）

  > - 工业标准DB9 CAN端子
  > - CAN排针
  > - 集成SPI microSD卡槽，用于数据存储
  > - 兼容Arduino Uno R3的SPI接口

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>A0</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A1</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D0</td>
<td>接收（RX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D1</td>
<td>发送（TX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D2</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D3</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D4</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D6</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D7</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D8</td>
<td>GPIO_ACTIVE_LOW</td>
<td>MCP2515中断INT</td>
</tr>
<tr>
<td>D9</td>
<td>SPI-CS</td>
<td>MicroSD</td>
</tr>
<tr>
<td>D10</td>
<td>SPI-CS</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D11</td>
<td>SPI-MOSI</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D12</td>
<td>SPI-MISO</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D13</td>
<td>SPI-CLK</td>
<td>MCP2515／MicroSD</td>
</tr>
<tr>
<td>D14</td>
<td>I2C-SDA</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D15</td>
<td>I2C_SCL</td>
<td>仅外部排针</td>
</tr>
</table>


- 电源（Power Supply）

  > - 5.0VDC

更多Keyestudio CAN-BUS扩展板信息见：


- [Keyestudio网站](https://www.keyestudio.com/2019new-keyestudio-can-bus-shield-mcp2551-chip-with-sd-socket-for-arduino-uno-r3-p0543.html)
- [Keyestudio维基资料（Wiki）](https://wiki.keyestudio.com/KS0411_keyestudio_CAN-BUS_Shield)
- [MCP2515数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
- [MCP2551数据手册](https://ww1.microchip.com/downloads/en/DeviceDoc/20001667G.pdf)

<a id="elecfreaks-can-bus-shield-ef02037"></a>

## ElecFreaks CAN总线扩展板EF02037

<a id="id3"></a>

### 概述（Overview）

ElecFreaks CAN BUS扩展板采用Microchip MCP2515独立CAN控制器及MCP2551高速CAN收发器，硬件接口兼容Arduino Uno R3。

<a id="id10"></a>

![官方原图：ElecFreaks CAN-BUS Shield (EF02037)](images/elecfreaks_can_bus_ef02037.jpg)

ElecFreaks CAN总线扩展板EF02037，图片来源：ElecFreaks

ElecFreaks CAN-BUS扩展板也以DiyMore CAN-BUS Shield v1.2销售，两者引脚及功能兼容。MCP2515接线也兼容Elecrow CAN-BUS Shield v1.5，但Elecrow板缺少3个0 Ω跳接，须手工焊接才能将SPI信号接到Arduino Uno R3排针。Elecrow虽有microSD卡槽，但该槽仅能在SPI信号为5 V的系统中使用。（[CAN-BUS 扩展板 v1.2 by DiyMore](https://www.diymore.cc/products/mcp2515-ef02037-can-bus-shield-controller-board-communication-speed-high-can-v2-0b-module-for-arduino-for-freaduino-diy-kit)；[CAN-BUS 扩展板 v1.5 by Elecrow](https://www.elecrow.com/canbus-shield-p-1133.html)）

<a id="id4"></a>

### 硬件（Hardware）


- MCP2515

  > - 独立CAN 2.0B控制器
  > - 最高1 Mbit/s比特率
  > - 标准及扩展数据帧与远程帧
  > - 3个发送缓冲区TX
  > - 2个接收缓冲区RX
  > - 6个29位滤波器
  > - 2个29位掩码
  > - 中断输出
  > - 单次发送模式（One-shot Mode）
  > - 高速SPI，10 MHz
- MCP2551

  > - 完全兼容ISO 11898标准
  > - 高速，最高1 Mbaud
- 连接能力（Connectivity）

  > - 工业标准DB9 CAN端子
  > - CAN螺丝接线端子，2针、5.0 mm间距
  > - 兼容Arduino Uno R3的SPI接口

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>A0</td>
<td>I2C-SDA</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>A1</td>
<td>I2C-SCL</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>A2</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>A5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D0</td>
<td>接收（RX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D1</td>
<td>发送（TX）</td>
<td>仅外部排针</td>
</tr>
<tr>
<td>D2</td>
<td>GPIO_ACTIVE_LOW</td>
<td>MCP2515中断INT</td>
</tr>
<tr>
<td><code>D3</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D4</code></td>
<td>SPI-CS</td>
<td>MicroSD接口</td>
</tr>
<tr>
<td>D5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D6</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D7</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D8</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D9</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D10</td>
<td>SPI-CS</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D11</td>
<td>SPI-MOSI</td>
<td>MCP2515／MicroSD接口</td>
</tr>
<tr>
<td>D12</td>
<td>SPI-MISO</td>
<td>MCP2515／MicroSD接口</td>
</tr>
<tr>
<td>D13</td>
<td>SPI-CLK</td>
<td>MCP2515／MicroSD接口</td>
</tr>
<tr>
<td>D14</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D15</td>
<td>无（None）</td>
<td></td>
</tr>
</table>


- 电源（Power Supply）

  > - 5.0VDC

更多ElecFreaks CAN-BUS扩展板信息见：


- [ElecFreaks网站](https://web.archive.org/web/20140716155137/http://www.elecfreaks.com/store/canbus-shield-p-746.html)
- [ElecFreaks维基资料（Wiki）](https://web.archive.org/web/20160331032426/http://www.elecfreaks.com/wiki/index.php?title=CAN-BUS_Shield)
- [MCP2515数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
- [MCP2551数据手册](https://ww1.microchip.com/downloads/en/DeviceDoc/20001667G.pdf)

<a id="adafruit-picowbell-can-bus-shield-for-pico"></a>

## 适用于Pico的Adafruit PiCowbell CAN总线扩展板

<a id="id5"></a>

### 概述（Overview）

Adafruit PiCowbell CAN Bus采用Microchip MCP2515控制器及TJA1051/3收发器，专为Raspberry Pi Pico设计，通过SPI连接，并提供Qwiic传感器连接器。

<a id="id11"></a>

![官方原图：Adafruit PiCowbell CAN Bus Shield](images/adafruit_can_picowbell.jpg)

Adafruit PiCowbell CAN总线扩展板

<a id="id6"></a>

### 硬件（Hardware）


- MCP2515

  > - 独立CAN 2.0B控制器
  > - 最高1 Mbit/s比特率
  > - 标准及扩展数据帧与远程帧
  > - 3个发送缓冲区TX
  > - 2个接收缓冲区RX
  > - 6个29位滤波器
  > - 2个29位掩码
  > - 中断输出
  > - 单次发送模式（One-shot Mode）
  > - 高速SPI，10 MHz
- TJA1051

  > - 完全兼容ISO 11898-2:2016、SAE J2284-1及SAE J2284-5标准
  > - 支持CAN FD
  > - 高速数据传输，最高5 Mbit/s
- 连接能力（Connectivity）

  > - CAN接线端子，3针、3.5 mm间距
  > - 兼容Raspberry Pi Pico的SPI接口

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
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP3</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP4</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP5</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP6</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP7</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP8</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP9</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP10</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP11</td>
<td>无（None）</td>
<td></td>
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
<td>SPI-MISO</td>
<td>MCP2515</td>
</tr>
<tr>
<td>GP17</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>GP18</td>
<td>SPI-SCK</td>
<td>MCP2515</td>
</tr>
<tr>
<td>GP19</td>
<td>SPI-MOSI</td>
<td>MCP2515</td>
</tr>
<tr>
<td>GP20</td>
<td>SPI-CS</td>
<td>MCP2515</td>
</tr>
<tr>
<td>GP21</td>
<td>GPIO_ACTIVE_LOW</td>
<td>MCP2515中断INT</td>
</tr>
<tr>
<td>GP22</td>
<td>无（None）</td>
<td></td>
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


- 电源（Power Supply）

  > - 3.3～5 V

更多Adafruit PiCowbell CAN总线扩展板信息见：


- [Adafruit网站](https://www.adafruit.com/product/5728#technical-details)
- [MCP2515数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
- [TJA1051数据手册](https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf)

<a id="seeed-studio-xiao-can-bus-shield"></a>

## Seeed Studio XIAO CAN总线扩展板

<a id="id7"></a>

### 概述（Overview）

Seeed Studio XIAO CAN Bus专为XIAO系列开发板设计，采用Microchip MCP2515 CAN控制器及SN65HVD230高速CAN收发器，硬件接口兼容Seeed Studio XIAO。（[Seeed Studio XIAO系列](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction)）

<a id="id12"></a>

![官方原图：Seeed Studio XIAO CAN Bus Shield](images/seeed_xiao_can.jpg)

Seeed Studio XIAO CAN总线扩展板

<a id="id8"></a>

### 硬件（Hardware）

该扩展板的SPI片选及中断使用Zephyr未标准化为此用途的XIAO排针脚，与第一路UART的D6 TX及D7 RX冲突，因此扩展板配置禁用了UART。

因此不能继续通过该串口访问Zephyr控制台，需改用USB CDC/ACM等方式，例如在west build中添加--snippet cdc-acm-console。


- MCP2515

  > - 独立CAN 2.0B控制器
  > - 最高1 Mbit/s比特率
  > - 标准及扩展数据帧与远程帧
  > - 3个发送缓冲区TX
  > - 2个接收缓冲区RX
  > - 6个29位滤波器
  > - 2个29位掩码
  > - 中断输出
  > - 单次发送模式（One-shot Mode）
  > - 高速SPI，10 MHz
- SN65HVD230

  > - 完全兼容ISO 11898标准
  > - 高速，最高1 Mbaud
- 连接能力（Connectivity）

  > - CAN螺丝接线端子，3针、3.5 mm间距
  > - CAN总线终端电阻焊盘
  > - 兼容Seeed Studio XIAO的SPI接口

<table>
<tr>
<th>名称（Name）</th>
<th>原始功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>D0</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D1</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td>D2</td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D3</code></td>
<td>无（None）</td>
<td></td>
</tr>
<tr>
<td><code>D4</code></td>
<td>未使用，原为I2C SDA</td>
<td></td>
</tr>
<tr>
<td>D5</td>
<td>未使用，原为I2C SCL</td>
<td></td>
</tr>
<tr>
<td>D6</td>
<td>低有效GPIO，原为TX</td>
<td>MCP2515中断INT</td>
</tr>
<tr>
<td><code>D7</code></td>
<td>SPI片选，原为RX</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D8</td>
<td>SPI-CLK</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D9</td>
<td>SPI-MOSI</td>
<td>MCP2515</td>
</tr>
<tr>
<td>D10</td>
<td>SPI-MISO</td>
<td>MCP2515</td>
</tr>
</table>


- 电源（Power Supply）

  > - 3.3～5 V

更多Seeed Studio XIAO CAN总线扩展板信息见：


- [Seeed Studio网站](https://www.seeedstudio.com/Seeed-Studio-CAN-Bus-Breakout-Board-for-XIAO-and-QT-Py-p-5702.html)
- [Seeed Studio维基资料（Wiki）](https://wiki.seeedstudio.com/xiao-can-bus-expansion)
- [MCP2515数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
- [SN65HVD230数据手册](https://www.ti.com/lit/ds/symlink/sn65hvd230.pdf)

<a id="programming"></a>

## 编程（Programming）

在Zephyr应用中调用west build或CMake时选择--shield dfrobot_can_bus_v2_0、--shield keyestudio_can_bus_ks0411、--shield adafruit_can_picowbell或--shield seeed_xiao_can，例如：

```text
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 --shield dfrobot_can_bus_v2_0 samples/drivers/can/counter
west flash
```

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield keyestudio_can_bus_ks0411 samples/drivers/can/counter
west flash
```

使用west：

```text
# From the root of the zephyr repository
west build -b rpi_pico --shield adafruit_can_picowbell samples/drivers/can/counter
```

使用CMake及Ninja：

```text
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=rpi_pico -DSHIELD="adafruit_can_picowbell" samples/drivers/can/counter

# Now run the build tool on the generated build system:
ninja -Cbuild
```

使用west：

```text
# From the root of the zephyr repository
west build -b xiao_rp2040 -S cdc-acm-console --shield seeed_xiao_can samples/drivers/can/counter
```

使用CMake及Ninja：

```text
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=xiao_rp2040 -DSNIPPET="cdc-acm-console" -DSHIELD="seeed_xiao_can" samples/drivers/can/counter

# Now run the build tool on the generated build system:
ninja -Cbuild
```

## 译注

MCP2515与收发器规格分别阅读。TJA1051收发器的CAN FD速率描述不表示MCP2515控制器支持CAN FD。原文另有JTA1050与数据手册TJA1050拼写差异。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [canbus-shield-p-746.html](https://web.archive.org/web/20140716155137/http://www.elecfreaks.com/store/canbus-shield-p-746.html)：HTTP Error 429: Too Many Requests。
- [index.php?title=CAN-BUS_Shield](https://web.archive.org/web/20160331032426/http://www.elecfreaks.com/wiki/index.php?title=CAN-BUS_Shield)：HTTP Error 429: Too Many Requests。
- [mcp2515-ef02037-can-bus-shield-controller-board-communication-speed-high-can-v2-0b-module-for-arduino-for-freaduino-diy-kit](https://www.diymore.cc/products/mcp2515-ef02037-can-bus-shield-controller-board-communication-speed-high-can-v2-0b-module-for-arduino-for-freaduino-diy-kit)：HTTP Error 429: Too Many Requests。
- [MCP2515](https://www.microchip.com/en-us/product/MCP2515)：HTTP Error 403: Forbidden。
- [TJA1050.pdf](https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf)：HTTP Error 404: Not Found。
- [TJA1051.pdf](https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf)：HTTP Error 404: Not Found。

---

[上一章](P088_RNBD451_Add-on_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P090_MikroElektronika_3D_Hall_3_Click.md)
