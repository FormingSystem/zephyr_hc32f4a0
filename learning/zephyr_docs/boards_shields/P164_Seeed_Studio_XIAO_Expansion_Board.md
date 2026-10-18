---
id: learning.zephyr-docs.boards-shields.page-164
title: Seeed Studio XIAO Expansion Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_expansion_board/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="seeed-studio-xiao-expansion-board"></a>

<a id="seeed-xiao-expansion-board"></a>

# 第164章\_Seeed Studio XIAO扩展板（Expansion Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_expansion_board/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Seeed Studio XIAO扩展板面向XIAO系列，大小仅为树莓派4的一半，具有丰富功能，便于快速搭建原型及项目。利用其丰富外设，可以探索XIAO系列的各种用途。（[Seeed Studio XIAO系列](https://www.seeedstudio.com/XIAO-c-1964.html)）

<a id="id1"></a>

![官方原图：Seeed Studio XIAO Expansion Board](images/seeed_xiao_expansion_board.webp)

Seeed Studio XIAO扩展板，图片来源：Seeed Studio

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>0</td>
<td>1个Grove接口，A0／D0</td>
</tr>
<tr>
<td>1</td>
<td>用户按键（User Button）</td>
</tr>
<tr>
<td>2</td>
<td>MicroSD SPI低有效片选CSn</td>
</tr>
<tr>
<td>3</td>
<td>蜂鸣器，A3</td>
</tr>
<tr>
<td>4</td>
<td>2个Grove接口，I2C数据SDA</td>
</tr>
<tr>
<td>5</td>
<td>2个Grove接口，I2C时钟SCL</td>
</tr>
<tr>
<td>6</td>
<td>1个Grove接口，UART发送TX</td>
</tr>
<tr>
<td>7</td>
<td>1个Grove接口，UART接收RX</td>
</tr>
<tr>
<td>8</td>
<td>MicroSD SPI SCK，串行时钟输入</td>
</tr>
<tr>
<td>9</td>
<td>MicroSD SPI MISO，串行数据输入（按原文保留）</td>
</tr>
<tr>
<td>10</td>
<td>MicroSD SPI MOSI，串行数据输出（按原文保留）</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

<a id="led-button-sample"></a>

### LED按键示例（LED Button Sample）

调用west build时设置--shield seeed_xiao_expansion_board，例如：

```text
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840 --shield seeed_xiao_expansion_board samples/basic/button
```

<a id="lvgl-basic-sample"></a>

### LVGL基础示例（Basic Sample）

调用west build时设置--shield seeed_xiao_expansion_board，例如：

```text
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840 --shield seeed_xiao_expansion_board samples/subsys/display/lvgl
```

## 译注

microSD表格MISO／MOSI的数据方向描述按来源保留，读者须结合主从端与信号名辨认。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [XIAO-c-1964.html](https://www.seeedstudio.com/XIAO-c-1964.html)：HTTP Error 404: Not Found。

---

[上一章](P163_Seeed_Studio_COB_LED_Driver_Board_for_XIAO.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P165_Seeed_Studio_24GHz_mmWave_Sensor_for_XIAO.md)
