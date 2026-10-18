---
id: learning.zephyr-docs.boards-retronix-sifli.page-4
title: LoDev
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ronoth/lodev/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ronoth_lodev"></a>

# 第4章\_LoDev

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ronoth/lodev/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/ronoth_lodev.jpg](images/ronoth_lodev.jpg)](images/ronoth_lodev.jpg)

LoDev

名称（Name）：

`ronoth_lodev`

厂商（Vendor）：

[Ronoth](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ronoth)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32l073xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32l073xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ronoth/lodev/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[Ronoth](https://ronoth.com/) [LoDev](https://www.crowdsupply.com/ronoth/lodev)是一块小型开源开发板，采用[AcSIP S76S](http://www.acsip.com.tw/index.php?action=products-detail&fid1=11&fid2=29&fid3=27&id=79&lang=3)系统级封装（SiP）。完整设计资料可在GitHub获取，开发板可从[Ronoth](https://ronoth.com/)或Crowd Supply购买。（[AcSIP](http://www.acsip.com.tw)；[完整LoDev设计资料](https://github.com/ronoth/LoDev)；[LoDev](https://www.crowdsupply.com/ronoth/lodev)；[CrowdSupply](https://www.crowdsupply.com/ronoth/lodev)）

S76S内含STMicroelectronics STM32L073RZ微控制器、[Semtech SX1276](https://www.semtech.com/products/wireless-rf/lora-transceivers/sx1276) LoRaWAN收发器及+20 dBm功率放大器，详情见[AcSIP S76S产品简介](https://www.acsip.com.tw/index.php?action=download_pro&perm=d&id=365)。

Zephyr应用可使用ronoth_lodev配置在此板运行。

[板卡设计文件](https://github.com/ronoth/LoDev)可在GitHub获取。

<a id="device-resources"></a>

## 器件资源（Device Resources）

内嵌STM32L073RZ的一些GPIO及SPI2已在封装内部专用于LoRaWAN收发器，资源列表见[内部专用端口](#internally-dedicated-ports)。

<a id="debugging"></a>

## 调试（Debugging）

与其他STM32处理器一样，编程及调试使用串行线调试（SWD）端口。可使用ST-LINK/V2适配器及配套软件，Linux下为st-utils软件包。

<a id="connector-pin-out"></a>

## 连接器引脚排列（Connector Pinout）

LoDev具有两排排针。两个连接器的第1脚均靠近板上Micro-USB接口，远离射频天线连接器。

从板的元件面俯视，令Micro-USB连接器靠近观察者、射频天线连接器远离观察者，此时左侧为[CN6](#cn6)，右侧为[CN7](#cn7)。

S76S SiP的UART1连接到Micro-USB接口上的USB转UART器件，因此PA9及PA10通常不能用作一般I/O。

开发板提供丝印标注，便于识别引脚。

<a id="id3"></a>

![官方原图：Ronoth LoDev sketch with pinout](images/pinout.jpg)

Ronoth LoDev引脚排列（Pinout）；原文拼作Ronth

<a id="cn6-pin-out"></a>

<a id="cn6"></a>

### CN6引脚排列

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>注意（Note）</th>
</tr>
<tr>
<td>1</td>
<td>3.3V</td>
<td>输出最大500 mA</td>
</tr>
<tr>
<td>2</td>
<td>地（GND）</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>PC1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>PC0</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>PB8</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>BOOT0</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>PB7</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>PB6</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>PB5</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>PD2</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>PC12</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>PC11</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>PC10</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>PA14</td>
<td>串行线时钟（SWCLK）</td>
</tr>
<tr>
<td>15</td>
<td>PA13</td>
<td>串行线调试数据（SWDIO）</td>
</tr>
<tr>
<td>16</td>
<td>PA12</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>PA11</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>PA9</td>
<td>USB串口发送TX驱动此输入引脚，用于UART1</td>
</tr>
<tr>
<td>19</td>
<td>PA10</td>
<td>此输出引脚驱动USB串口接收RX，用于UART1</td>
</tr>
<tr>
<td>20</td>
<td>PA8</td>
<td></td>
</tr>
</table>

<a id="cn7-pin-out"></a>

<a id="cn7"></a>

### CN7引脚排列

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>注意（Note）</th>
</tr>
<tr>
<td>1</td>
<td>PC2</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>PC3</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>低电平复位（nRESET）</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>PA0</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>PA2</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>PA3</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>PA4</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>PA5</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>PA6</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>PA7</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>PC4</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>PC5</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>PB0</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>PB1</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>PC6</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>PC7</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>PC8</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>PC9</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>地（GND）</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>PA1</td>
<td>在S76S内用于“RF FEM CPS”信号</td>
</tr>
</table>

<a id="internally-dedicated-ports"></a>

<a id="id1"></a>

### 内部专用端口（Internally Dedicated Ports）

<table>
<tr>
<th>引脚名称（Pin Name）</th>
<th>引脚类型（Pin Type）</th>
<th>I/O结构（I/O Structure）</th>
<th>注意（Note）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>PA15</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D5</td>
</tr>
<tr>
<td>PB3</td>
<td>输入输出（I/O）</td>
<td>FTf</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D4</td>
</tr>
<tr>
<td>PB4</td>
<td>输入输出（I/O）</td>
<td>FTf</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D3</td>
</tr>
<tr>
<td>PB9</td>
<td>输入输出（I/O）</td>
<td>FTf</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D2</td>
</tr>
<tr>
<td>PB10</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276复位（Reset）</td>
</tr>
<tr>
<td>PB11</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D0</td>
</tr>
<tr>
<td>PB12</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 SPI低有效片选（nCS）</td>
</tr>
<tr>
<td>PB13</td>
<td>输入输出（I/O）</td>
<td>FTf</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 SPI2_SCK</td>
</tr>
<tr>
<td>PB14</td>
<td>输入输出（I/O）</td>
<td>FTf</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 SPI2_MISO</td>
</tr>
<tr>
<td>PB15</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 SPI2_MOSI</td>
</tr>
<tr>
<td>PC13</td>
<td>输入输出（I/O）</td>
<td>FT</td>
<td><ul><li></li></ul></td>
<td>内部SX1276 D1</td>
</tr>
</table>

<a id="references"></a>

## 参考资料（References）

<a id="license"></a>

## 许可证（License）

本文档版权（Copyright）归2021年Dean Weiten <[dmw@weiten.com](mailto:dmw%40weiten.com)>所有。

SPDX许可证标识：Apache-2.0

## 译注

LoDev排针方向以元件面朝上、Micro-USB靠近观察者为准，CN6在左、CN7在右。S76S内的GPIO与SPI2已部分专用于LoRa收发器，UART1也占用PA9／PA10。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://ronoth.com/)：HTTP Error 429: Too Many Requests。

---

[上一章](P003_Ronoth.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_AcSIP_S76S.md)
