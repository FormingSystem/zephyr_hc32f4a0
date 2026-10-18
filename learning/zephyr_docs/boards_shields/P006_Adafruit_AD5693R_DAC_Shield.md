---
id: learning.zephyr-docs.boards-shields.page-6
title: Adafruit AD5693R DAC Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ad5693r/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ad5693r-dac-shield"></a>

<a id="adafruit-ad5693r"></a>

# 第6章\_Adafruit AD5693R数模转换器扩展板（DAC Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ad5693r/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit AD5693R DAC扩展板采用Analog Devices AD5693R 16位DAC，带2个STEMMA QT连接器，输出跨度2.5 V。（[Adafruit AD5693R数模转换器扩展板（DAC Shield）](https://learn.adafruit.com/adafruit-ad5693r-16-bit-dac-breakout-board)；[Analog Devices AD5693R 16位数模转换器DAC](https://www.analog.com/en/products/ad5693r.html)）

<a id="id2"></a>

![官方原图：Adafruit AD5693R DAC Shield](images/adafruit_ad5693r.webp)

Adafruit AD5693R数模转换器扩展板（DAC Shield），图片来源：Adafruit

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
<td>AD5693R I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>AD5693R I2C时钟线（SCL）</td>
</tr>
<tr>
<td>A0</td>
<td>AD5693R I2C地址选择</td>
</tr>
<tr>
<td>VREF</td>
<td>AD5693R参考电压输出</td>
</tr>
<tr>
<td>LDAC</td>
<td>AD5693R加载DAC输入（LDAC）</td>
</tr>
</table>

通过STEMMA QT连接器使用时，电源电压3.3 V，最大输出电压2.5 V。

扩展板的LDAC引脚下拉，因此写入输入寄存器后立即更新输出电压。

如何修改设备树，例如调整掉电模式，见[adi,ad5693](../hardware/P798_AD5693数模转换器绑定.md#dtbinding-adi-ad5693)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ad5693r，例如运行数模转换器DAC示例：（[数模转换器（DAC）](../driver_samples/P001_DAC数模转换示例.md#dac)）

```text
# From the root of the zephyr repository
west build -b adafruit_feather_rp2040 --shield adafruit_ad5693r samples/drivers/dac
west flash
```

将电压表连接扩展板输出，观察电压变化。

## 译注

3.3 V供电时最大输出2.5 V；LDAC下拉使写入后立即更新。

---

[上一章](P005_Adafruit_I2C_to_8_Channel_Solenoid_Driver_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_Adafruit_Adalogger_Featherwing_Shield.md)
