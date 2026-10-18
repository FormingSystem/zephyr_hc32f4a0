---
id: learning.zephyr-docs.boards-shields.page-147
title: RAK19007 WisBlock Base Board 2nd Gen
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rakwireless_rak19007/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rak19007-wisblock-base-board-2nd-gen"></a>

<a id="rakwireless-rak19007"></a>

# 第147章\_RAK19007第二代WisBlock基板（Base Board 2nd Gen）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rakwireless_rak19007/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

RAK19007是第二代WisBlock基板，用于连接WisBlock Core、WisBlock IO及WisBlock模块，向安装其上的模块供电并提供互连。它有1个WisBlock Core专用插槽及4个WisBlock模块插槽A～D。Core安装在上面，其他模块可安装在RAK19007上面或下面。D槽容纳最大23 mm模块，A～C槽支持10 mm模块。另外还有3组2.54 mm间距扩展排针，引出BOOT、GPIO、I2C及UART。

为便于使用，USB Type-C连接器按所用WisBlock Core直接连接其MCU的USB端口（若支持），或连接USB-UART转换器，可上传固件及串口通信，也用作电池充电口。

WisBlock模块通过高速板对板连接器连接RAK19007基板，提供牢固可靠的互连，保证各数据总线的信号完整性；模块用螺钉固定，即使在强振动环境中也能保持可靠连接。

也可使用RAK19005 WisBlock传感器延长线，将模块放在远离基板的位置或外壳中的任意位置。

<a id="id2"></a>

![官方原图：RAK19007 WisBlock Base Board 2nd Gen (Credit: RAKwireless)](images/rakwireless_rak19007.webp)

RAK19007第二代WisBlock基板（Base Board 2nd Gen），图片来源：RAKwireless

<a id="product-features"></a>

## 产品特性（Product Features）


- 1个WisBlock Core模块
- 1个兼容WisBlock的IO插槽
- 4个兼容A～D槽的WisBlock模块
- 1个USB Type-C端口，用于编程及调试
- 3.7 V可充电电池连接器
- 5 V太阳能板连接器
- 4组4针排针，通过焊接触点访问BOOT、I2C及UART引脚

<a id="id4"></a>

更多扩展板信息见RAK19007第二代WisBlock基板[注1](#id3)。（[RAK19007第二代WisBlock基板（Base Board 2nd Gen）](https://docs.rakwireless.com/product-categories/wisblock/rak19007)）

<a id="requirements"></a>

## 前置要求（Requirements）

RAK19007 WisBlock Mini基板需要WisBlock Core模块才能工作，兼容几乎所有WisBlock Core模块，但可用特性取决于具体Core模块。

<a id="mounting"></a>

## 安装（Mounting）

WisBlock Core通过称为WisBlock I/O连接器的40针排针安装在RAK19007基板上，兼容WisBlock生态，方便集成各种WisBlock模块及传感器。

<a id="id6"></a>

RAK19007安装方法见[RAK19007 WisBlock基板安装指南](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#assembling-a-wisblock-module)[注2](#id5)。

<a id="pin-assignments"></a>

## 引脚分配（Pin Assignments）

WisBlock IO连接器引脚分配

<table>
<tr>
<td>功能（Function）</td>
<td>引脚（Pin）</td>
<td>引脚（Pin）</td>
<td>功能（Function）</td>
</tr>
<tr>
<td>电池电源（VBAT）</td>
<td>1</td>
<td>2</td>
<td>电池电源（VBAT）</td>
</tr>
<tr>
<td>地（GND）</td>
<td>3</td>
<td>4</td>
<td>地（GND）</td>
</tr>
<tr>
<td>3V3</td>
<td>5</td>
<td>6</td>
<td>3V3</td>
</tr>
<tr>
<td>USB_P</td>
<td>7</td>
<td>8</td>
<td>USB_N</td>
</tr>
<tr>
<td>USB总线电源（VBUS）</td>
<td>9</td>
<td>10</td>
<td>SW1</td>
</tr>
<tr>
<td>TXD0</td>
<td>11</td>
<td>12</td>
<td>RXD0</td>
</tr>
<tr>
<td>复位（RESET）</td>
<td>13</td>
<td>14</td>
<td><code>LED1</code></td>
</tr>
<tr>
<td><code>LED2</code></td>
<td>15</td>
<td>16</td>
<td>LED3</td>
</tr>
<tr>
<td>电源（VDD）</td>
<td>17</td>
<td>18</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>I2C1_SDA</td>
<td>19</td>
<td>20</td>
<td>I2C1_SCL</td>
</tr>
<tr>
<td>AIN0</td>
<td>21</td>
<td>22</td>
<td>AIN1</td>
</tr>
<tr>
<td>BOOT0</td>
<td>23</td>
<td>24</td>
<td>IO7</td>
</tr>
<tr>
<td>SPI_CS</td>
<td>25</td>
<td>26</td>
<td>SPI_CLK</td>
</tr>
<tr>
<td>SPI_MISO</td>
<td>27</td>
<td>28</td>
<td>SPI_MOSI</td>
</tr>
<tr>
<td>IO1</td>
<td>29</td>
<td>30</td>
<td>IO2</td>
</tr>
<tr>
<td>IO3</td>
<td>31</td>
<td>32</td>
<td>IO4</td>
</tr>
<tr>
<td>TXD1</td>
<td>33</td>
<td>34</td>
<td>RXD1</td>
</tr>
<tr>
<td>I2C2_SDA</td>
<td>35</td>
<td>36</td>
<td>I2C2_SCL</td>
</tr>
<tr>
<td>IO5</td>
<td>37</td>
<td>38</td>
<td>IO6</td>
</tr>
<tr>
<td>地（GND）</td>
<td>39</td>
<td>40</td>
<td>地（GND）</td>
</tr>
</table>

WisBlock传感器A～D槽引脚分配

<table>
<tr>
<td>D</td>
<td>C</td>
<td>B</td>
<td>A</td>
<td>引脚（Pin）</td>
<td>引脚（Pin）</td>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>TXD0</td>
<td>1</td>
<td>2</td>
<td>地（GND）</td>
<td>地（GND）</td>
<td>地（GND）</td>
<td>地（GND）</td>
</tr>
<tr>
<td>SPI_CS</td>
<td>SPI_CS</td>
<td>SPI_CS</td>
<td>SPI_CS</td>
<td>3</td>
<td>4</td>
<td>SPI_CS</td>
<td>SPI_CS</td>
<td>SPI_CS</td>
<td>SPI_CS</td>
</tr>
<tr>
<td>SPI_MISO</td>
<td>SPI_MISO</td>
<td>SPI_MISO</td>
<td>SPI_MISO</td>
<td>5</td>
<td>6</td>
<td>SPI_MOSI</td>
<td>SPI_MOSI</td>
<td>SPI_MOSI</td>
<td>SPI_MOSI</td>
</tr>
<tr>
<td>I2C1_SCL</td>
<td>I2C1_SCL</td>
<td>I2C1_SCL</td>
<td>I2C1_SCL</td>
<td>7</td>
<td>8</td>
<td>I2C1_SDA</td>
<td>I2C1_SDA</td>
<td>I2C1_SDA</td>
<td>I2C1_SDA</td>
</tr>
<tr>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
<td>9</td>
<td>10</td>
<td>IO2</td>
<td>IO1</td>
<td>IO4</td>
<td>IO6</td>
</tr>
<tr>
<td>3V3</td>
<td>3V3</td>
<td>3V3</td>
<td>3V3</td>
<td>11</td>
<td>12</td>
<td>IO1</td>
<td>IO2</td>
<td>IO3</td>
<td>IO5</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>13</td>
<td>14</td>
<td>3V3</td>
<td>3V3</td>
<td>3V3</td>
<td>3V3</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>15</td>
<td>16</td>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>17</td>
<td>18</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>19</td>
<td>20</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
</tr>
<tr>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>21</td>
<td>22</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
</tr>
<tr>
<td>地（GND）</td>
<td>地（GND）</td>
<td>地（GND）</td>
<td>地（GND）</td>
<td>19</td>
<td>20</td>
<td>RXD0</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
<td>未连接（NC）</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield rakwireless_rak19007，例如：

```text
# From the root of the zephyr repository
west build -b rak4631/nrf52840 --shield rakwireless_rak19007 samples/drivers/fuel_gauge
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://docs.rakwireless.com/product-categories/wisblock/rak19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007)

<a id="id5"></a>

〔[2](#id6)〕 [RAK19007快速入门中的WisBlock模块组装指南：https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#assembling-a-wisblock-module](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#assembling-a-wisblock-module)

## 译注

概述写3组扩展排针，特性表写4组4针排针；正文还使用Mini Base称呼，均保留来源差异。

---

[上一章](P146_Digilent_Pmod_SD.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P148_Raspberry_Pi_Camera_Module_2.md)
