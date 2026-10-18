---
id: learning.zephyr-docs.boards-shields.page-34
title: Adafruit 16-channel PWM Servo Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_pca9685/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-16-channel-pwm-servo-shield"></a>

<a id="adafruit-pca9685"></a>

# 第34章\_Adafruit 16通道PWM／舵机扩展板（Servo Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_pca9685/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit 16通道PWM／舵机扩展板基于NXP PCA9685，兼容Arduino UNO R3。

<a id="id3"></a>

更多信息见Adafruit 16通道PWM／舵机扩展板网页[注1](#id2)。（[Adafruit 16通道PWM／舵机 扩展板 网页](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all)）

<a id="id1"></a>

![官方原图：Adafruit 16-channel PWM/Servo Shield](images/adafruit_pca9685.webp)

Adafruit 16通道PWM／舵机扩展板（Servo Shield），图片来源：Adafruit

<a id="pins-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>A5</td>
<td>I2C时钟SCL1</td>
</tr>
<tr>
<td>A4</td>
<td>I2C数据SDA1</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_pca9685，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield adafruit_pca9685 samples/drivers/led/pwm
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [Adafruit 16通道PWM／舵机扩展板官方指南](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all)

---

[上一章](P033_Adafruit_5x5_NeoPixel_Grid_BFF.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P035_Adafruit_PCF8523_Shield.md)
