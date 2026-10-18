---
id: learning.zephyr-docs.boards-shields.page-81
title: Sharp memory display generic shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/ls0xx_generic/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sharp-memory-display-generic-shield"></a>

<a id="ls0xx-generic-shield"></a>

# 第81章\_Sharp存储型显示屏通用扩展板（Memory Display Generic Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/ls0xx_generic/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

这是Sharp存储像素LCD的通用扩展板定义，支持LS0XX显示屏。该类屏幕提供SPI及少量其他引脚，SCS片选为高电平有效。

DISP控制显示存储内容还是全白像素。它可直接接VDD以持续显示内容，也可接GPIO；若设备树包含disp-en-gpios，驱动初始化时将其置高，并可通过显示消隐（Blanking）API控制。

<a id="id2"></a>

<a id="id4"></a>

Sharp存储型显示屏需周期性翻转VCOM，防止面板产生直流偏置，见应用说明[注1](#id1)及数据手册[注2](#id3)；直流偏置可能损坏LCD并缩短寿命。该信号必须由串行软件输入或EXTCOMIN外部引脚提供。（[appnote](https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces)；[datasheet](https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC_SMA-224806.pdf)）

当前驱动仅支持通过EXTCOMIN翻转VCOM，此时EXTMODE接VDD。定义extcomin-gpios后，驱动启动线程，以extcomin-frequency频率翻转EXTCOMIN；高频提高对比度，低频节省功耗。

若希望改用PWM等方式，可不定义extcomin-gpios，并在应用中自行实现翻转。

<a id="pins-assignment-of-the-generic-sharp-memory-display-shield"></a>

### 通用Sharp存储型显示屏扩展板的引脚分配

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>SCS</td>
<td>串行从机选择</td>
</tr>
<tr>
<td>SI</td>
<td>串行数据输入</td>
</tr>
<tr>
<td>SCLK</td>
<td>串行时钟输入</td>
</tr>
<tr>
<td>EXTCOMIN</td>
<td>VCOM极性反转输入，也可通过软件控制VCOM</td>
</tr>
<tr>
<td>DISP</td>
<td>显示开关信号，可直接接VDD</td>
</tr>
<tr>
<td>EXTMODE</td>
<td>公共电极COM反转方式选择</td>
</tr>
</table>

<a id="current-supported-displays"></a>

### 当前支持的显示屏

驱动支持以下显示屏，但现有扩展板定义仅提供LS013B7DH03；可参考它并修改宽、高等配置，添加其他型号。

LS012B7DD01、LS013B7DH03、LS013B7DH05、LS027B7DH01A、LS032B7DD02、LS044Q7DH01

<table>
<tr>
<th>显示（Display）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>LS013B7DH03</td>
<td>ls013b7dh03</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield ls013b7dh03，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield ls013b7dh03 samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces](https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC_SMA-224806.pdf](https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC_SMA-224806.pdf)

## 译注

Sharp Memory LCD使用高有效片选并需要周期VCOM翻转；EXTMODE及EXTCOMIN配置不能省略。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Memory+LCD+Theory%2C+Programming%2C+and+Interfaces](https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1010)>。

---

[上一章](P080_LMP90100_Sensor_AFE_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P082_M5Stack-Cardputer_base_shield.md)
