---
id: learning.zephyr-docs.boards-shields.page-62
title: DVP FPC-24 MT9M114 Camera Module
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/dvp_fpc24_mt9m114/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="dvp-fpc-24-mt9m114-camera-module"></a>

<a id="dvp-fpc24-mt9m114"></a>

# 第62章\_DVP FPC-24 MT9M114摄像头模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/dvp_fpc24_mt9m114/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

该扩展板支持采用24针FPC连接器及DVP并行接口的MT9M114模块。这些摄像头与i.MX RT1050、RT1060及RT1064 EVK兼容并随套件提供，详情见[Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183) [注1](#id1)。

<a id="pins-assignment-of-the-dvp-fpc-24-mt9m114-camera-module"></a>

### DVP FPC-24 MT9M114摄像头模块的引脚分配

<table>
<tr>
<th>FPC连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>未连接（NC）</td>
</tr>
<tr>
<td>2</td>
<td>模拟地（AGND）</td>
</tr>
<tr>
<td>3</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>4</td>
<td>AVDD</td>
</tr>
<tr>
<td>5</td>
<td>串行时钟线（SCL）</td>
</tr>
<tr>
<td>6</td>
<td>复位（Reset）</td>
</tr>
<tr>
<td>7</td>
<td>Vsync</td>
</tr>
<tr>
<td>8</td>
<td>掉电（Powerdown）</td>
</tr>
<tr>
<td>9</td>
<td>Hsync</td>
</tr>
<tr>
<td>10</td>
<td>DVDD</td>
</tr>
<tr>
<td>11</td>
<td>DOVDD</td>
</tr>
<tr>
<td>12</td>
<td>数据9</td>
</tr>
<tr>
<td>13</td>
<td>主时钟（Master Clock）</td>
</tr>
<tr>
<td>14</td>
<td>数据8</td>
</tr>
<tr>
<td>15</td>
<td>DGND</td>
</tr>
<tr>
<td>16</td>
<td>数据7</td>
</tr>
<tr>
<td>17</td>
<td>像素时钟（Pixel Clock）</td>
</tr>
<tr>
<td>18</td>
<td>数据6</td>
</tr>
<tr>
<td>19</td>
<td>数据2</td>
</tr>
<tr>
<td>20</td>
<td>数据5</td>
</tr>
<tr>
<td>21</td>
<td>数据3</td>
</tr>
<tr>
<td>22</td>
<td>数据4</td>
</tr>
<tr>
<td>23</td>
<td>数据1</td>
</tr>
<tr>
<td>24</td>
<td>数据0</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于已提供24针FPC DVP并行接口配置的开发板，例如i.MX RT1050、RT1060及RT1064 EVK。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield dvp_fpc24_mt9m114，例如：

```text
# From the root of the zephyr repository
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 samples/subsys/video/capture
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)：HTTP Error 403: Forbidden。

---

[上一章](P061_DVP_20-pin_OV7670_Camera_Module.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P063_EK-RA8D1_to_RTK7EKA6M3B00001BU_Display_Adapter.md)
