---
id: learning.zephyr-docs.boards-shields.page-190
title: HL RC Module Evaluation Kit Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="hl-rc-module-evaluation-kit-shield"></a>

<a id="swir-hl78xx-ev-kit"></a>

# 第190章\_HL/RC模块评估套件扩展板（Module Evaluation Kit Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

欢迎阅读HL78模块入门指南。本指南帮助配置评估套件，向HL78模块发送AT命令并开始数据传输。

<a id="id1"></a>

![官方原图：HL/RC Module Evaluation Kit Shield Shield](images/SW-Dev-RC76.3.webp)

HL/RC模块评估套件扩展板，图片来源：Sierra Wireless

<a id="id3"></a>

更多扩展板信息见HL/RC模块评估套件指南网站[注1](#id2)。（[HL/RC 模块评估套件 扩展板 指南网站](https://source.sierrawireless.com/resources/airprime/development_kits/hl78xx-hl7900-development-kit-guide/)）

<a id="pins-assignment-of-hl-rc-module-evaluation-kit-shield"></a>

### HL/RC模块评估套件扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>CN403别名</td>
<td>UART 1，带CTS及RTS引脚</td>
</tr>
<tr>
<td>CN303别名</td>
<td>SPI／UART 3</td>
</tr>
<tr>
<td>CN1000别名</td>
<td>GPIO测试引脚</td>
</tr>
<tr>
<td>GPIO6，CN1000_3</td>
<td>低功耗监测（LOW POWER MONITORING）</td>
</tr>
<tr>
<td>VGPIO别名</td>
<td>间接指示进入／退出休眠模式（Hibernate）</td>
</tr>
<tr>
<td>复位RESET，CN1000_12</td>
<td>复位信号RESET SIGNAL</td>
</tr>
<tr>
<td>唤醒WAKE-UP，CN1000_8</td>
<td>SPI／UART 3</td>
</tr>
</table>

HL/RC模块评估套件的更多设置说明见指南网站。原网页此处显示未解析的引用声明“.. _HL/RC Module Evaluation Kit Shield guide website:”。

<a id="checking-your-basic-configurations-in-putty"></a>

### 在PuTTY中检查基本配置

在尝试建立开发板与主机MCU的有线连接前，建议先通过PC的USB COM端口运行这组基本AT命令。HL78xx模块的完整AT命令可在来源（Source）链接中查阅。

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板可用于任何已配置排针连接器并定义UART、SPI及USB接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield swir_hl78xx_ev_kit，例如：

```text
# From the root of the zephyr repository
west build -b st/nucleo_u575zi_q --shield swir_hl78xx_ev_kit samples/drivers/modem/hello_hl78xx
```

<a id="documentation"></a>

## 文档（Documentation）

<a id="automatic-baud-rate-detection"></a>

### 自动波特率检测：

完整说明见HL78xx自动波特率切换。（[HL78xx自动波特率切换（Auto Baud Rate Switching）](P188_HL78xx_Auto_Baud_Rate_Switching.md#hl78xx-auto-baudrate)）

简要说明见HL78xx自动波特率速查。（[HL78xx自动波特率速查（Auto Baud Rate - Quick Reference）](P189_HL78xx_Auto_Baud_Rate_-_Quick_Reference.md#hl78xx-auto-baudrate-quick-reference)）

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://source.sierrawireless.com/resources/airprime/development_kits/hl78xx-hl7900-development-kit-guide/](https://source.sierrawireless.com/resources/airprime/development_kits/hl78xx-hl7900-development-kit-guide/)

---

[上一章](P189_HL78xx_Auto_Baud_Rate_-_Quick_Reference.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P191_Texas_Instruments_TCAN4550EVM.md)
