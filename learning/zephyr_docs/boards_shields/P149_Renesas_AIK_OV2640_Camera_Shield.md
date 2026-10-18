---
id: learning.zephyr-docs.boards-shields.page-149
title: Renesas AIK OV2640 Camera Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/renesas_aik_ov2640_cam/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="renesas-aik-ov2640-camera-shield"></a>

<a id="renesas-aik-ov2640-cam"></a>

# 第149章\_Renesas AIK OV2640摄像头扩展板（Camera Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/renesas_aik_ov2640_cam/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Renesas AIK OV2640摄像头扩展板采用OV2640图像传感器及20针DVP连接器，专为Renesas AI Kit开发平台设计。

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
<td>电源（VCC）</td>
</tr>
<tr>
<td>3</td>
<td>串行时钟线（SCL）</td>
</tr>
<tr>
<td>4</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>5</td>
<td>HSYNC</td>
</tr>
<tr>
<td>6</td>
<td>VSYNC</td>
</tr>
<tr>
<td>7</td>
<td>PCLK</td>
</tr>
<tr>
<td>8</td>
<td>XCLK</td>
</tr>
<tr>
<td>9</td>
<td><code>D7</code></td>
</tr>
<tr>
<td>10</td>
<td>D6</td>
</tr>
<tr>
<td>11</td>
<td>D5</td>
</tr>
<tr>
<td>12</td>
<td><code>D4</code></td>
</tr>
<tr>
<td>13</td>
<td><code>D3</code></td>
</tr>
<tr>
<td>14</td>
<td>D2</td>
</tr>
<tr>
<td>15</td>
<td>D1</td>
</tr>
<tr>
<td>16</td>
<td>D0</td>
</tr>
<tr>
<td>17</td>
<td>RET</td>
</tr>
<tr>
<td>18</td>
<td>PWDN</td>
</tr>
<tr>
<td>19</td>
<td>RET</td>
</tr>
<tr>
<td>20</td>
<td>PWDN</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板需要Renesas AI Kit开发平台，例如RA8D1 AI Kit开发平台。（[RA8D1人工智能套件开发平台（AI Kit Development Platform）](../boards_renesas_ra/P001_RA8D1_AI_Kit_Development_Platform.md#aik_ra8d1)）

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield renesas_aik_ov2640_cam，例如：

```text
# From the root of the zephyr repository
west build -b aik_ra8d1 --shield renesas_aik_ov2640_cam samples/subsys/video/capture
west flash
```

<a id="references"></a>

## 参考资料（References）

---

[上一章](P148_Raspberry_Pi_Camera_Module_2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P150_Renesas_DA14531_Pmod_Board.md)
