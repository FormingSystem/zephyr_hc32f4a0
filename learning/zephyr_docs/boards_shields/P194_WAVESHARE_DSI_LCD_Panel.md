---
id: learning.zephyr-docs.boards-shields.page-194
title: WAVESHARE DSI LCD Panel
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/waveshare_dsi_lcd/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="waveshare-dsi-lcd-panel"></a>

<a id="waveshare-dsi-lcd"></a>

# 第194章\_WAVESHARE DSI LCD面板（Panel）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/waveshare_dsi_lcd/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

WAVESHARE DSI LCD面板扩展板是通用驱动扩展板，可驱动多种DSI LCD面板。

<a id="id2"></a>

更多信息见WAVESHARE DSI LCD扩展板网站[注1](#id1)。（[WAVESHARE DSI LCD显示屏 扩展板 网站](https://www.waveshare.com/product/displays/lcd-oled/7inch-dsi-lcd-c.htm)）

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>7英寸DSI<br><br>LCD，C型</td>
<td>waveshare_7inch_dsi_lcd_c</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于已配置MIPI DSI并定义I2C接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时，必须输入与显示屏匹配的扩展板名称，见上表。例如：

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 --shield waveshare_7inch_dsi_lcd_c samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.waveshare.com/product/displays/lcd-oled/7inch-dsi-lcd-c.htm](https://www.waveshare.com/product/displays/lcd-oled/7inch-dsi-lcd-c.htm)

---

[上一章](P193_ARM_V2C-DAPLink_for_DesignStart_FPGA.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P195_WAVESHARE_e-Paper_Raw_Panel_Shield.md)
