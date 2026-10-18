---
id: learning.zephyr-docs.boards-shields.page-199
title: WeAct Studio MiniSTM32H7xx OV2640 Camera Sensor
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/weact_ov2640_cam_module/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="weact-studio-ministm32h7xx-ov2640-camera-sensor"></a>

<a id="weact-ov2640-cam-module"></a>

# 第199章\_WeAct Studio MiniSTM32H7xx OV2640摄像头传感器

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/weact_ov2640_cam_module/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此OV2640摄像头传感器设计用于WeAct Studio MiniSTM32H7xx开发板，为其提供摄像头能力。扩展板集成OV2640模块，可采集最高200万像素的图像及视频。

![官方原图：OV2640 Camera Sensor](images/ov2640.webp)

OV2640摄像头传感器详情见[MiniSTM32H7xx GitHub](https://github.com/WeActStudio/MiniSTM32H7xx)及OV2640数据手册。（[OV2640 数据手册](https://www.uctronics.com/download/cam_module/OV2640DS.pdf)）

<a id="requirements"></a>

## 前置要求（Requirements）

开发板必须具有zephyr_camera_dvp设备树标签，才能使用此扩展板。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

扩展板通过以下引脚连接WeAct Studio MiniSTM32H7xx开发板：

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>开发板引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>DCMI_D0</td>
<td>PC6</td>
<td>DCMI数据线0</td>
</tr>
<tr>
<td>DCMI_D1</td>
<td>PC7</td>
<td>DCMI数据线1</td>
</tr>
<tr>
<td>DCMI_D2</td>
<td>PE0</td>
<td>DCMI数据线2</td>
</tr>
<tr>
<td>DCMI_D3</td>
<td>PE1</td>
<td>DCMI数据线3</td>
</tr>
<tr>
<td>DCMI_D4</td>
<td>PE4</td>
<td>DCMI数据线4</td>
</tr>
<tr>
<td>DCMI_D5</td>
<td>PD3</td>
<td>DCMI数据线5</td>
</tr>
<tr>
<td>DCMI_D6</td>
<td>PE5</td>
<td>DCMI数据线6</td>
</tr>
<tr>
<td>DCMI_D7</td>
<td>PE6</td>
<td>DCMI数据线7</td>
</tr>
<tr>
<td>DCMI_HSYNC</td>
<td>PA4</td>
<td>DCMI行同步HSYNC</td>
</tr>
<tr>
<td>DCMI_VSYNC</td>
<td>PB7</td>
<td>DCMI场同步VSYNC</td>
</tr>
<tr>
<td>DCMI_PIXCLK</td>
<td>PA6</td>
<td>DCMI像素时钟</td>
</tr>
<tr>
<td>I2C_SDA</td>
<td>PB9</td>
<td>I2C数据线</td>
</tr>
<tr>
<td>I2C_SCL</td>
<td>PB8</td>
<td>I2C时钟线</td>
</tr>
<tr>
<td>RCC_MCO1</td>
<td>PA8</td>
<td>时钟输出</td>
</tr>
<tr>
<td>SUPPLY</td>
<td>PA7</td>
<td>电源控制，GPIO</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield weact_ov2640_cam_module，例如：

```text
# From the root of the zephyr repository
west build -b mini_stm32h743 --shield weact_ov2640_cam_module samples/subsys/video/capture_to_lvgl/ -- -DCONFIG_BOOT_DELAY=2000
```

---

[上一章](P198_Waveshare_Pico_UPS-B_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P200_WIZnet_W5500_Ethernet_Shield.md)
