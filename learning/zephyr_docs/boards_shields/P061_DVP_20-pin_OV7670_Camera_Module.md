---
id: learning.zephyr-docs.boards-shields.page-61
title: DVP 20-pin OV7670 Camera Module
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/dvp_20pin_ov7670/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="dvp-20-pin-ov7670-camera-module"></a>

<a id="dvp-20pin-ov7670"></a>

# 第61章\_DVP 20引脚OV7670摄像头模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/dvp_20pin_ov7670/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此系列扩展板支持使用18针连接器的OV7670摄像头模块，该连接器兼容[arducam,dvp-20pin-connector](../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector)，可通过数字视频端口DVP，即并行接口，连接开发板与传感器。

20针连接器中实际仅有18个引脚。

<a id="id4"></a>

<a id="id10"></a>

该模块最初由[Arducam](https://docs.arducam.com/DVP-Camera-Module/Arduino-GIGA/Arduino-GIGA/Quick-Start-Guide/) [注2](#id3)生产，现已停产，目前由[Olimex](https://www.olimex.com/Products/Components/Camera/CAMERA-OV7670/) [注5](#id9)供应。

<a id="pins-assignment"></a>

### 引脚分配（Pins Assignment）

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>3V3</td>
<td>2</td>
<td>地（GND）</td>
</tr>
<tr>
<td>3</td>
<td>串行时钟线（SCL）</td>
<td>4</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>5</td>
<td>VS</td>
<td>6</td>
<td>HS</td>
</tr>
<tr>
<td>7</td>
<td>PCLK</td>
<td>8</td>
<td>XCLK</td>
</tr>
<tr>
<td>9</td>
<td><code>D7</code></td>
<td>10</td>
<td>D6</td>
</tr>
<tr>
<td>11</td>
<td>D5</td>
<td>12</td>
<td><code>D4</code></td>
</tr>
<tr>
<td>13</td>
<td><code>D3</code></td>
<td>14</td>
<td>D2</td>
</tr>
<tr>
<td>15</td>
<td>D1</td>
<td>16</td>
<td>D0</td>
</tr>
<tr>
<td>17</td>
<td>POWER_EN</td>
<td>18</td>
<td>POWER_DOWN</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

<a id="id6"></a>

<a id="id8"></a>

<a id="id2"></a>

任意提供上述引脚分配、两排各9或10针的18／20针接口开发板均可使用，例如Arduino Giga R1 [注3](#id5)、[NXP FRDM-MCXN947](https://www.nxp.com/docs/en/application-note/AN14191.pdf) [注4](#id7)、配[ST-CAMS-OMV](https://www.st.com/en/evaluation-tools/b-cams-omv.html)适配器[注1](#id1)的ST开发板，或其他兼容接口开发板。（[arduino Giga R1产品资料](https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-camera/)）

也可用跳线接到将摄像头并行端口引出到排针的任意开发板。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield dvp_20pin_ov7670，例如：

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947 --shield dvp_20pin_ov7670 samples/subsys/video/capture
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/evaluation-tools/b-cams-omv.html](https://www.st.com/en/evaluation-tools/b-cams-omv.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://docs.arducam.com/DVP-Camera-Module/Arduino-GIGA/Arduino-GIGA/Quick-Start-Guide/](https://docs.arducam.com/DVP-Camera-Module/Arduino-GIGA/Arduino-GIGA/Quick-Start-Guide/)

<a id="id5"></a>

〔[3](#id6)〕 [https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-camera/](https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-camera/)

<a id="id7"></a>

〔[4](#id8)〕 [https://www.nxp.com/docs/en/application-note/AN14191.pdf](https://www.nxp.com/docs/en/application-note/AN14191.pdf)

<a id="id9"></a>

〔[5](#id10)〕 [https://www.olimex.com/Products/Components/Camera/CAMERA-OV7670/](https://www.olimex.com/Products/Components/Camera/CAMERA-OV7670/)

## 译注

连接器定义为20针，OV7670模块本体为18针，按官方接线表连接。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://docs.arducam.com/DVP-Camera-Module/Arduino-GIGA/Arduino-GIGA/Quick-Start-Guide/)：HTTP Error 403: Forbidden。
- [AN14191.pdf](https://www.nxp.com/docs/en/application-note/AN14191.pdf)：HTTP Error 404: Not Found。
- [b-cams-omv.html](https://www.st.com/en/evaluation-tools/b-cams-omv.html)：HTTP Error 567: Unknown Status。

---

[上一章](P060_DH_electronics_DHSBC_RS485_CAN_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P062_DVP_FPC-24_MT9M114_Camera_Module.md)
