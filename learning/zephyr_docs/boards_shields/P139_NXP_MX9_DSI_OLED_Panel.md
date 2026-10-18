---
id: learning.zephyr-docs.boards-shields.page-139
title: NXP MX9 DSI OLED Panel
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_mx9_dsi_oled/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-mx9-dsi-oled-panel"></a>

<a id="nxp-mx9-dsi-oled"></a>

# 第139章\_NXP MX9 DSI OLED显示面板（Panel）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_mx9_dsi_oled/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

NXP MX9 DSI OLED是面向i.MX9系列的高分辨率OLED面板，通过MIPI DSI连接，利用OLED提供良好色彩及对比度，适合嵌入式显示。

<a id="id2"></a>

更多信息见NXP MX9 DSI OLED扩展板网站[注1](#id1)。（[NXP MX9 DSI OLED 扩展板 网站](https://www.nxp.com/design/design-center/development-boards-and-designs/mx9-dsi-oled-display-panel:MX9-DSI-OLED)）

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>MX9 DSI OLED显示面板</td>
<td>nxp_mx9_dsi_oled</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时，须输入与显示屏匹配的扩展板名称，见上表。

例如：

```text
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/m7 --shield nxp_mx9_dsi_oled tests/drivers/mipi_dsi/api
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.nxp.com/design/design-center/development-boards-and-designs/mx9-dsi-oled-display-panel:MX9-DSI-OLED](https://www.nxp.com/design/design-center/development-boards-and-designs/mx9-dsi-oled-display-panel:MX9-DSI-OLED)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mx9-dsi-oled-display-panel:MX9-DSI-OLED](https://www.nxp.com/design/design-center/development-boards-and-designs/mx9-dsi-oled-display-panel:MX9-DSI-OLED)：HTTP Error 404: Not Found。

---

[上一章](P138_NXP_MX8_DSI_OLED1A_Panel.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P140_NXP_S32K5XX-MB_Shield.md)
