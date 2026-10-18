---
id: learning.zephyr-docs.boards-shields.page-155
title: NXP RK055HDMIPI4MA0 MIPI Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rk055hdmipi4ma0/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-rk055hdmipi4ma0-mipi-display"></a>

<a id="rk055hdmipi4ma0"></a>

# 第155章\_NXP RK055HDMIPI4MA0 MIPI显示屏

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rk055hdmipi4ma0/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Rocktech RK055HDMIPI4MA0是5.5英寸720×1280像素TFT显示面板，具有LED背光、全视角、MIPI接口及电容触摸面板。

<a id="id16"></a>

更多扩展板信息见RK055HDMIPI4MA0产品页[注8](#id15)。（[RK055HDMIPI4MA0 产品页](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0)）

此显示屏使用许多NXP EVK提供的40针FPC接口。

<a id="pins-assignment-of-the-rocktech-rk055hdmipi4ma0-mipi-display"></a>

### Rocktech RK055HDMIPI4MA0 MIPI显示屏的引脚分配

<table>
<tr>
<th>FPC连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>LED背光阴极</td>
</tr>
<tr>
<td>21</td>
<td>控制器复位</td>
</tr>
<tr>
<td>22</td>
<td>控制器LPTE信号</td>
</tr>
<tr>
<td>26</td>
<td>触摸控制器I2C数据SDA</td>
</tr>
<tr>
<td>27</td>
<td>触摸控制器I2C时钟SCL</td>
</tr>
<tr>
<td>28</td>
<td>触摸控制器复位</td>
</tr>
<tr>
<td>29</td>
<td>触摸控制器中断</td>
</tr>
<tr>
<td>32</td>
<td>LCD电源使能</td>
</tr>
<tr>
<td>34</td>
<td>背光电源使能</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于已提供40针FPC接口配置的开发板。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield rk055hdmipi4ma0，例如：

```text
# From the root of the zephyr repository
west build -b mimxrt1170_evk//cm7 --shield rk055hdmipi4ma0 samples/drivers/display
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- <a id="id2"></a>

  [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)[注1](#id1)
- <a id="id4"></a>

  [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)[注2](#id3)
- <a id="id6"></a>

  <a id="id8"></a>

  [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode) [注3](#id5)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html) [注4](#id7)
- <a id="id10"></a>

  [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)[注5](#id9)
- <a id="id12"></a>

  [NXP的Zephyr专题页面](https://nxp.com/zephyr) [注6](#id11)，含培训资源
- <a id="id14"></a>

  NXP Zephyr支持社区论坛 [注7](#id13)（[NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)）

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

<a id="id5"></a>

〔[3](#id6)〕 [https://mcuxpresso.nxp.com/mcux-vscode](https://mcuxpresso.nxp.com/mcux-vscode)

<a id="id7"></a>

〔[4](#id8)〕 [https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)

<a id="id9"></a>

〔[5](#id10)〕 [https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

<a id="id11"></a>

〔[6](#id12)〕 [https://nxp.com/zephyr](https://nxp.com/zephyr)

<a id="id13"></a>

〔[7](#id14)〕 [https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

<a id="id15"></a>

〔[8](#id16)〕 [https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [5-5-lcd-panel:RK055HDMIPI4MA0](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0)：HTTP Error 404: Not Found。

---

[上一章](P154_NXP_RK055HDMIPI4M_MIPI_Display.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P156_Raspberry_Pi_Pico_to_UNO_FlexyPin_Adapter.md)
