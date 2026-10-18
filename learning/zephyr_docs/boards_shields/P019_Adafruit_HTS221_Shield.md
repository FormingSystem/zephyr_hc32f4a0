---
id: learning.zephyr-docs.boards-shields.page-19
title: Adafruit HTS221 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_hts221/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-hts221-shield"></a>

<a id="adafruit-hts221"></a>

# 第19章\_Adafruit HTS221扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_hts221/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit HTS221温湿度扩展板采用意法半导体HTS221，带2个STEMMA QT连接器，用于测量温度及湿度。（[Adafruit HTS221 温湿度传感器 扩展板](https://learn.adafruit.com/adafruit-hts221-temperature-humidity-sensor)；[ST Microelectronics HTS221 湿度及温度传感器](https://www.st.com/resource/en/datasheet/hts221.pdf)）

<a id="id1"></a>

![官方原图：Adafruit HTS221 Shield](images/adafruit_hts221.webp)

Adafruit HTS221扩展板（Shield），图片来源：Adafruit

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于提供I2C连接器的开发板，例如STEMMA QT或Qwiic；目标板必须定义zephyr_i2c节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>DRDY</td>
<td>数据就绪（Data Ready）输出</td>
</tr>
<tr>
<td>片选（CS）</td>
<td>保持高电平以使用I2C模式</td>
</tr>
</table>

可用设备树设置，例如DRDY引脚配置，见[st,hts221](../compatible_binding_reference/P069_st_hts221.md#std-dtcompatible-st-hts221)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_hts221，例如运行[通用数字温湿度传感器轮询](../sensors/P016_温湿度传感器轮询示例.md#dht_polling)示例：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_scorpio_rp2040 --shield adafruit_hts221 samples/sensor/dht_polling
west flash
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [hts221.pdf](https://www.st.com/resource/en/datasheet/hts221.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P018_Adafruit_HT16K33_LED_Matrix_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_Adafruit_INA219_Shield.md)
