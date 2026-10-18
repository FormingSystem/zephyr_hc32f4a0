---
id: learning.zephyr-docs.boards-shields.page-44
title: ArduCam CU450 OV5640 Camera Module
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arducam_cu450_ov5640/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arducam-cu450-ov5640-camera-module"></a>

<a id="arducam-cu450-ov5640"></a>

# 第44章\_ArduCam CU450 OV5640摄像头模块（Camera Module）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arducam_cu450_ov5640/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

ArduCam CU450 OV5640通过40针FFC连接器提供OV5640图像传感器，支持数字视频端口DVP及MIPI CSI-2接口，专为Renesas [EK-RA8P1](https://www.renesas.com/en/design-resources/boards-kits/ek-ra8p1/)评估套件[注1](#id1)设计。

<a id="pins-assignment"></a>

### 引脚分配（Pins Assignment）

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>地（GND）</td>
</tr>
<tr>
<td>2</td>
<td>D11</td>
</tr>
<tr>
<td>3</td>
<td>D10</td>
</tr>
<tr>
<td>4</td>
<td>地（GND）</td>
</tr>
<tr>
<td>5</td>
<td>D9／MIPI_CSI2_DL1_P</td>
</tr>
<tr>
<td>6</td>
<td>D8／MIPI_CSI2_DL1_N</td>
</tr>
<tr>
<td>7</td>
<td>地（GND）</td>
</tr>
<tr>
<td>8</td>
<td>D7／MIPI_CSI2_CL1_P</td>
</tr>
<tr>
<td>9</td>
<td>D6／MIPI_CSI2_CL1_N</td>
</tr>
<tr>
<td>10</td>
<td>地（GND）</td>
</tr>
<tr>
<td>11</td>
<td>D5／MIPI_CSI2_DL0_P</td>
</tr>
<tr>
<td>12</td>
<td>D4／MIPI_CSI2_DL0_N</td>
</tr>
<tr>
<td>13</td>
<td>地（GND）</td>
</tr>
<tr>
<td>14</td>
<td><code>D3</code></td>
</tr>
<tr>
<td>15</td>
<td>D2</td>
</tr>
<tr>
<td>16</td>
<td>地（GND）</td>
</tr>
<tr>
<td>17</td>
<td>D1</td>
</tr>
<tr>
<td>18</td>
<td>D0</td>
</tr>
<tr>
<td>19</td>
<td>地（GND）</td>
</tr>
<tr>
<td>20</td>
<td>串行时钟线（SCL）</td>
</tr>
<tr>
<td>21</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>22</td>
<td>地（GND）</td>
</tr>
<tr>
<td>23</td>
<td>VSYNC</td>
</tr>
<tr>
<td>24</td>
<td>HSYNC</td>
</tr>
<tr>
<td>25</td>
<td>复位（RESET）</td>
</tr>
<tr>
<td>26</td>
<td>XCLK</td>
</tr>
<tr>
<td>27</td>
<td>PCLK</td>
</tr>
<tr>
<td>28</td>
<td>中断（INT）</td>
</tr>
<tr>
<td>29</td>
<td>地（GND）</td>
</tr>
<tr>
<td>30</td>
<td>地（GND）</td>
</tr>
<tr>
<td>31</td>
<td>3V3</td>
</tr>
<tr>
<td>32</td>
<td>地（GND）</td>
</tr>
<tr>
<td>33</td>
<td>地（GND）</td>
</tr>
<tr>
<td>34</td>
<td>3V3</td>
</tr>
<tr>
<td>35</td>
<td>3V3</td>
</tr>
<tr>
<td>36</td>
<td>3V3</td>
</tr>
<tr>
<td>37</td>
<td>地（GND）</td>
</tr>
<tr>
<td>38</td>
<td>地（GND）</td>
</tr>
<tr>
<td>39</td>
<td>3V3</td>
</tr>
<tr>
<td>40</td>
<td>地（GND）</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板需要开发板提供40针FFC连接器，Renesas EK-RA8P1已完整支持。

注意（Note）

尽管模块及连接器同时提供DVP和MIPI CSI-2，Renesas RA SoC平台目前仅支持DVP，尚不支持MIPI CSI-2。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arducam_cu450_ov5640_dvp，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 --shield arducam_cu450_ov5640_dvp samples/subsys/video/capture
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.renesas.com/en/design-resources/boards-kits/ek-ra8p1/](https://www.renesas.com/en/design-resources/boards-kits/ek-ra8p1/)

## 译注

CU450硬件提供DVP及MIPI CSI-2，原文Renesas RA支持限于DVP。

---

[上一章](P043_ARCELI_W5500_ETH.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P045_ArduCam_Mega_SPI_Camera_Shield.md)
