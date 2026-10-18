---
id: learning.zephyr-docs.boards-shields.page-152
title: NXP RK043FN02H-CT Parallel Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rk043fn02h_ct/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-rk043fn02h-ct-parallel-display"></a>

<a id="rk043fn02h-ct"></a>

# 第152章\_NXP RK043FN02H-CT并行显示屏

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rk043fn02h_ct/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

该显示面板已停产，替代品是NXP RK043FN66HS-CTG 4.3英寸并行LCD显示扩展板。（[NXP RK043FN66HS-CTG并行显示屏](P153_NXP_RK043FN66HS-CTG_Parallel_Display.md#rk043fn66hs-ctg)）

RK043FN02H-CT是Rocktech的4.3英寸480×272像素TFT显示屏，具有LED背光及电容触摸面板，可与多种i.MX RT EVK及LPC MCU配合，评估显示应用。

<a id="id16"></a>

更多扩展板信息见RK043FN02H-CT产品页[注8](#id15)。（[RK043FN02H-CT 产品页](https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/4-3-lcd-panel:RK043FN02H-CT)）

此显示屏使用40针并行FPC接口及6针I2C接口，许多NXP EVK提供这些接口。注意，并行FPC接口与其他NXP EVK上的MIPI FPC接口不兼容。

<a id="pins-assignment-of-the-rocktech-rk043fn02h-ct-parallel-display"></a>

### Rocktech RK043FN02H-CT并行显示屏的引脚分配

<table>
<tr>
<th>并行FPC引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>LED背光阴极</td>
</tr>
<tr>
<td>2</td>
<td>LED背光阳极</td>
</tr>
<tr>
<td>3</td>
<td>地（GND）</td>
</tr>
<tr>
<td>4</td>
<td>VDD，3.3 V</td>
</tr>
<tr>
<td>5-7</td>
<td>地（GND）</td>
</tr>
<tr>
<td>8-12</td>
<td>LCD数据D11～D15</td>
</tr>
<tr>
<td>13-14</td>
<td>地（GND）</td>
</tr>
<tr>
<td>15-20</td>
<td>LCD数据D5～D10</td>
</tr>
<tr>
<td>21-23</td>
<td>地（GND）</td>
</tr>
<tr>
<td>24-28</td>
<td>LCD数据D0～D4</td>
</tr>
<tr>
<td>29</td>
<td>地（GND）</td>
</tr>
<tr>
<td>30</td>
<td>LCD时钟CLK</td>
</tr>
<tr>
<td>31</td>
<td>LCD显示控制DISP</td>
</tr>
<tr>
<td>32</td>
<td>LCD行同步HSYNC</td>
</tr>
<tr>
<td>33</td>
<td>LCD场同步VSYNC</td>
</tr>
<tr>
<td>34</td>
<td>LCD数据使能DE</td>
</tr>
<tr>
<td>35</td>
<td>未连接（NC）</td>
</tr>
<tr>
<td>36</td>
<td>地（GND）</td>
</tr>
<tr>
<td>37-40</td>
<td>未连接（NC）</td>
</tr>
</table>

<table>
<tr>
<th>I2C连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>VDD，3.3 V</td>
</tr>
<tr>
<td>2</td>
<td>LCD触摸复位</td>
</tr>
<tr>
<td>3</td>
<td>LCD触摸中断</td>
</tr>
<tr>
<td>4</td>
<td>LCD I2C时钟线（SCL）</td>
</tr>
<tr>
<td>5</td>
<td>LCD I2C数据线（SDA）</td>
</tr>
<tr>
<td>6</td>
<td>地（GND）</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于已配置40+6针并行／I2C FPC接口的开发板。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield rk043fn02h_ct，例如：

```text
# From the root of the zephyr repository
west build -b mimxrt1060_evk --shield rk043fn02h_ct samples/drivers/display
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

〔[8](#id16)〕 [https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/4-3-lcd-panel:RK043FN02H-CT](https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/4-3-lcd-panel:RK043FN02H-CT)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [4-3-lcd-panel:RK043FN02H-CT](https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/4-3-lcd-panel:RK043FN02H-CT)：HTTP Error 404: Not Found。

---

[上一章](P151_Reyax_LoRa_RYLR896_and_RYLR915_Modules.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P153_NXP_RK043FN66HS-CTG_Parallel_Display.md)
