---
id: learning.zephyr-docs.boards-shields.page-173
title: SparkFun MAX3421E Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/sparkfun_max3421e/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sparkfun-max3421e-shield"></a>

<a id="max3421e-shield"></a>

# 第173章\_SparkFun MAX3421E扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/sparkfun_max3421e/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

支持基于MAX3421E USB外设／主机控制器（Peripheral/Host Controller）的扩展板。

<a id="sparkfun-usb-host-shield"></a>

## SparkFun USB主机扩展板（USB Host Shield）

<a id="pins-assignment-of-the-shield-connector"></a>

### 扩展板连接器的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
<th>MAX3421E引脚</th>
</tr>
<tr>
<td>D0</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D1</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D2</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td><code>D3</code></td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td><code>D4</code></td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D5</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D6</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td><code>D7</code></td>
<td>复位RESET引脚</td>
<td></td>
</tr>
<tr>
<td>D8</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D9</td>
<td>INTn</td>
<td>第24脚，中断输出</td>
</tr>
<tr>
<td>D10</td>
<td>SPI低有效片选CSn</td>
<td>第34脚，SPI片选</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入（MOSI）</td>
<td>第36脚，SPI串行数据输入</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出（MISO）</td>
<td>第35脚，SPI串行数据输出</td>
</tr>
<tr>
<td>D13</td>
<td>SPI串行时钟（SCK）</td>
<td>第37脚，SPI串行时钟输入</td>
</tr>
<tr>
<td>D14</td>
<td>未连接</td>
<td></td>
</tr>
<tr>
<td>D15</td>
<td>未连接</td>
<td></td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

在Zephyr应用中调用west build或cmake时设置--shield sparkfun_max3421e。

---

[上一章](P172_Sparkfun_Environmental_Combo_Shield_with_ENS160_and_BME280.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P174_Sparkfun_RV8803_Shield.md)
