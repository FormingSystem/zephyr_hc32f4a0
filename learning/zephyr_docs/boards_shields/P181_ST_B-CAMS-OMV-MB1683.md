---
id: learning.zephyr-docs.boards-shields.page-181
title: ST B-CAMS-OMV-MB1683
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st_b_cams_omv_mb1683/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="st-b-cams-omv-mb1683"></a>

<a id="id1"></a>

# 第181章\_ST B-CAMS-OMV-MB1683摄像头模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st_b_cams_omv_mb1683/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

摄像头模块套件B-CAMS-OMV为STMicroelectronics MB1379摄像头子板及OpenMV、Waveshare等第三方模块提供扩展连接器，可用于具有1×30针ZIF连接器的STM32开发板，以连接多种摄像头，便于在STM32微控制器上实现计算机视觉。

此摄像头模块套件兼容所有具有ZIF连接器的STM32 Discovery及Evaluation开发板，例如STM32H747I-DISCO、STM32H7B3I-DK及32L4R9IDISCOVERY套件。

<a id="id2"></a>

[![官方原图：B-CAMS-OMV-MB1683](images/st_b_cams_omv_mb1683.webp)](images/st_b_cams_omv_mb1683.webp)

B-CAMS-OMV MB1683图片，来源：STMicroelectronics。

摄像头信号由支持的输入连接器CN1、CN2或CN4进入扩展板，再由30针ZIF输出连接器CN5连接到运行Zephyr的主板。

CN1及CN2引脚定义见用户手册。（[用户手册（User Manual）](https://www.st.com/resource/en/user_manual/um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)）

<a id="waveshare-camera-board-connector-cn4-camera-input"></a>

## Waveshare摄像头板连接器CN4，摄像头输入

<table>
<tr>
<th>引脚编号（Pin Number）</th>
<th>说明（Description）</th>
<th>引脚编号（Pin Number）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td>1</td>
<td>地（GND）</td>
<td>2</td>
<td>VCAM</td>
</tr>
<tr>
<td>3</td>
<td>I2C_SDA</td>
<td>4</td>
<td>I2C_SCL</td>
</tr>
<tr>
<td>5</td>
<td>DCMI_HSYNC</td>
<td>6</td>
<td>DCMI_VSYNC</td>
</tr>
<tr>
<td>7</td>
<td>Camera_CLK</td>
<td>8</td>
<td>DCMI_PIXCLK</td>
</tr>
<tr>
<td>9</td>
<td>DCMI_D6</td>
<td>10</td>
<td>DCMI_D7</td>
</tr>
<tr>
<td>11</td>
<td>DCMI_D4</td>
<td>12</td>
<td>DCMI_D5</td>
</tr>
<tr>
<td>13</td>
<td>DCMI_D2</td>
<td>14</td>
<td>DCMI_D3</td>
</tr>
<tr>
<td>15</td>
<td>DCMI_D0</td>
<td>16</td>
<td>DCMI_D1</td>
</tr>
<tr>
<td>17</td>
<td>电源使能PWR_EN／LED1</td>
<td>18</td>
<td>低有效复位RESET#</td>
</tr>
</table>

<a id="zif-connector-cn5-camera-output"></a>

## ZIF连接器CN5，摄像头输出

<table>
<tr>
<th>引脚编号（Pin Number）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td>1</td>
<td>3V3</td>
</tr>
<tr>
<td>2</td>
<td>地（GND）</td>
</tr>
<tr>
<td>3</td>
<td>I2C_SCL</td>
</tr>
<tr>
<td>4</td>
<td>I2C_SDA</td>
</tr>
<tr>
<td>5</td>
<td>低有效复位RESET#</td>
</tr>
<tr>
<td>6</td>
<td>电源使能PWR_EN／LED1</td>
</tr>
<tr>
<td>7</td>
<td>SHUTTER</td>
</tr>
<tr>
<td>8</td>
<td>地（GND）</td>
</tr>
<tr>
<td>9</td>
<td>下拉PULLDOWN／LED2</td>
</tr>
<tr>
<td>10</td>
<td>Camera_CLK</td>
</tr>
<tr>
<td>11</td>
<td>3V3</td>
</tr>
<tr>
<td>12</td>
<td>DCMI_VSYNC</td>
</tr>
<tr>
<td>13</td>
<td>5 V，RSU</td>
</tr>
<tr>
<td>14</td>
<td>DCMI_HSYNC</td>
</tr>
<tr>
<td>15</td>
<td>地（GND）</td>
</tr>
<tr>
<td>16</td>
<td>DCMI_PIXCK</td>
</tr>
<tr>
<td>17</td>
<td>地（GND）</td>
</tr>
<tr>
<td>18</td>
<td>SPI_MISO</td>
</tr>
<tr>
<td>19</td>
<td>SPI_CS</td>
</tr>
<tr>
<td>20</td>
<td>DCMI_D7</td>
</tr>
<tr>
<td>21</td>
<td>DCMI_D6</td>
</tr>
<tr>
<td>22</td>
<td>DCMI_D5</td>
</tr>
<tr>
<td>23</td>
<td>DCMI_D4</td>
</tr>
<tr>
<td>24</td>
<td>DCMI_D3</td>
</tr>
<tr>
<td>25</td>
<td>DCMI_D2</td>
</tr>
<tr>
<td>26</td>
<td>DCMI_D1</td>
</tr>
<tr>
<td>27</td>
<td>DCMI_D0</td>
</tr>
<tr>
<td>28</td>
<td>SPI_MOSI</td>
</tr>
<tr>
<td>29</td>
<td>SPI_CLK</td>
</tr>
<tr>
<td>30</td>
<td>地（GND）</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此摄像头模块套件兼容所有具有ZIF连接器的STM32 Discovery及Evaluation开发板，例如STM32H747I-DISCO、STM32H7B3I-DK及32L4R9IDISCOVERY套件。

<a id="usage"></a>

## 用途（Usage）

将SHIELD设为_st_b_cams_omv_mb1683并添加所需设备树属性，即可在任意应用中使用此扩展板；此处名称的前导下划线按原文保留，下面命令使用st_b_cams_omv_mb1683。

调用west build时设置--shield "st_b_cams_omv_mb1683"，例如：

```text
# From the root of the zephyr repository
west build -b stm32h7b3i_dk --shield st_b_cams_omv_mb1683 samples/subsys/video/capture_to_lvgl
```

<a id="references"></a>

## 参考资料（References）


- [产品页面（Product Page）](https://www.st.com/en/evaluation-tools/b-cams-omv.html)
- [产品简介（Databrief）](https://www.st.com/resource/en/data_brief/b-cams-omv.pdf)
- [用户手册（User Manual）](https://www.st.com/resource/en/user_manual/um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)

## 译注

原文SHIELD说明带前导下划线，构建命令不带；两处按来源保留并注明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [b-cams-omv.html](https://www.st.com/en/evaluation-tools/b-cams-omv.html)：HTTP Error 567: Unknown Status。
- [b-cams-omv.pdf](https://www.st.com/resource/en/data_brief/b-cams-omv.pdf)：HTTP Error 567: Unknown Status。
- [um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2779-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P180_ST_B-CAMS-IMX-MB1854.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P182_ST_B-DSI-MB1314.md)
