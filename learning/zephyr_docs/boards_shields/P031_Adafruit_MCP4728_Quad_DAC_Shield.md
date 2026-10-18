---
id: learning.zephyr-docs.boards-shields.page-31
title: Adafruit MCP4728 Quad DAC Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_mcp4728/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-mcp4728-quad-dac-shield"></a>

<a id="adafruit-mcp4728"></a>

# 第31章\_Adafruit MCP4728四路DAC扩展板（Quad DAC Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_mcp4728/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit MCP4728四路DAC扩展板采用Microchip 12位四输出DAC，带2个STEMMA QT连接器，具有4路输出及内部电压参考。（[Adafruit MCP4728四路DAC扩展板（Quad DAC Shield）](https://learn.adafruit.com/adafruit-mcp4728-i2c-quad-dac)；[Microchip 12位四输出数模转换器DAC](https://www.microchip.com/en-us/product/mcp4728)）

<a id="id2"></a>

![官方原图：Adafruit MCP4728 DAC Shield](images/adafruit_mcp4728.webp)

Adafruit MCP4728 DAC扩展板，图片来源：Adafruit

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
<td>串行时钟线（SCL）</td>
<td>MCP4728 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>MCP4728 I2C数据线（SDA）</td>
</tr>
<tr>
<td>LDAC</td>
<td>MCP4728加载DAC输入LDAC</td>
</tr>
<tr>
<td>RDY</td>
<td>MCP4728就绪信号，EEPROM写入忙时为低电平</td>
</tr>
<tr>
<td>VA～VD</td>
<td>MCP4728输出通道</td>
</tr>
</table>

通过STEMMA QT连接器使用时，电源电压3.3 V，可使用的最大内部参考电压为2.048 V。

扩展板的LDAC引脚下拉，因此写入输入寄存器后立即更新输出电压。

如何修改设备树，例如调整电压参考、增益或掉电模式，见[microchip,mcp4728](../hardware/P803_MCP4728数模转换器绑定.md#dtbinding-microchip-mcp4728)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_mcp4728，例如运行数模转换器DAC示例：（[数模转换器（DAC）](../driver_samples/P001_DAC数模转换示例.md#dac)）

```text
# From the root of the zephyr repository
west build -b adafruit_feather_adalogger_rp2040 --shield adafruit_mcp4728 samples/drivers/dac
west flash
```

将电压表接到输出VA，观察电压变化。若测试其他输出通道，修改该扩展板.overlay文件中的dac-channel-id属性。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mcp4728](https://www.microchip.com/en-us/product/mcp4728)：HTTP Error 403: Forbidden。

---

[上一章](P030_Adafruit_MAX17048_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P032_Adafruit_MCP9808_Shield.md)
