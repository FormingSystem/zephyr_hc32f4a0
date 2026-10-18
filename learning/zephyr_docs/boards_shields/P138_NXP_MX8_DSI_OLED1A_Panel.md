---
id: learning.zephyr-docs.boards-shields.page-138
title: NXP MX8 DSI OLED1A Panel
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_mx8_dsi_oled1a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-mx8-dsi-oled1a-panel"></a>

<a id="nxp-mx8-dsi-oled1a"></a>

# 第138章\_NXP MX8 DSI OLED1A显示面板（Panel）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_mx8_dsi_oled1a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

NXP MX8 DSI OLED1A是面向i.MX8系列的高分辨率OLED面板，通过MIPI DSI连接，利用OLED提供良好色彩及对比度，适合嵌入式显示。

<a id="id2"></a>

更多信息见NXP MX8 DSI OLED1A扩展板网站[注1](#id1)。（[NXP MX8 DSI OLED1A 扩展板 网站](https://www.nxp.com/part/MX8-DSI-OLED1A)）

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>MX8 DSI OLED1A显示面板</td>
<td>nxp_mx8_dsi_oled1a</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时，须输入与显示屏匹配的扩展板名称，见上表。

例如：

```text
# From the root of the zephyr repository
west build -b imx93_evk/mimx9352/m33/ddr --shield nxp_mx8_dsi_oled1a samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.nxp.com/part/MX8-DSI-OLED1A](https://www.nxp.com/part/MX8-DSI-OLED1A)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [MX8-DSI-OLED1A](https://www.nxp.com/part/MX8-DSI-OLED1A)：HTTP Error 404: Not Found。

---

[上一章](P137_NXP_M.2_Wi-Fi_and_BT_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P139_NXP_MX9_DSI_OLED_Panel.md)
