---
id: learning.zephyr-docs.boards-shields.page-135
title: NXP BTB-44 OV5640 Camera Module
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_btb44_ov5640/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-btb-44-ov5640-camera-module"></a>

<a id="nxp-btb44-ov5640"></a>

# 第135章\_NXP BTB-44 OV5640摄像头模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_btb44_ov5640/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

该扩展板支持使用44针板对板连接器及MIPI CSI或DVP并行接口的OV5640模块，专为NXP i.MX RT1160及RT1170 EVK设计并随套件提供。

<a id="id16"></a>

更多信息见[Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183) [注8](#id15)。

<a id="pins-assignment-of-the-nxp-board-to-board-44-pin-ov5640-camera-module"></a>

### NXP板对板44针OV5640摄像头模块的引脚分配

<table>
<tr>
<th>摄像头连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>模拟地（AGND）</td>
</tr>
<tr>
<td>2</td>
<td>AF_GND</td>
</tr>
<tr>
<td>3</td>
<td>STROBE</td>
</tr>
<tr>
<td>4</td>
<td>AF_VCC</td>
</tr>
<tr>
<td>5</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>6</td>
<td>VCMSINK</td>
</tr>
<tr>
<td>7</td>
<td>串行时钟线（SCL）</td>
</tr>
<tr>
<td>8</td>
<td>AVDD</td>
</tr>
<tr>
<td>9</td>
<td>RESETB</td>
</tr>
<tr>
<td>10</td>
<td>GPIO1</td>
</tr>
<tr>
<td>11</td>
<td>PCLK</td>
</tr>
<tr>
<td>12</td>
<td>GPIO0</td>
</tr>
<tr>
<td>13</td>
<td>VSYNC</td>
</tr>
<tr>
<td>14</td>
<td>FREX</td>
</tr>
<tr>
<td>15</td>
<td>HREF</td>
</tr>
<tr>
<td>16</td>
<td>MIPI_CSI_DP1／D9</td>
</tr>
<tr>
<td>17</td>
<td>PWDN</td>
</tr>
<tr>
<td>18</td>
<td>MIPI_CSI_DN1／D8</td>
</tr>
<tr>
<td>19</td>
<td>MIPI_CSI_DP1／D9</td>
</tr>
<tr>
<td>20</td>
<td>DGND</td>
</tr>
<tr>
<td>21</td>
<td>MIPI_CSI_DN1／D8</td>
</tr>
<tr>
<td>22</td>
<td>MIPI_CSI_CLKP／D7</td>
</tr>
<tr>
<td>23</td>
<td>MIPI_CSI_CLKP／D7</td>
</tr>
<tr>
<td>24</td>
<td>MIPI_CSI_CLKN／D6</td>
</tr>
<tr>
<td>25</td>
<td>MIPI_CSI_CLKN／D6</td>
</tr>
<tr>
<td>26</td>
<td>DGND</td>
</tr>
<tr>
<td>27</td>
<td>MIPI_CSI_DP0／D5</td>
</tr>
<tr>
<td>28</td>
<td>MIPI_CSI_DP0／D5</td>
</tr>
<tr>
<td>29</td>
<td>MIPI_CSI_DN0／D4</td>
</tr>
<tr>
<td>30</td>
<td>MIPI_CSI_DN0／D4</td>
</tr>
<tr>
<td>31</td>
<td><code>D3</code></td>
</tr>
<tr>
<td>32</td>
<td>DGND</td>
</tr>
<tr>
<td>33</td>
<td>D2</td>
</tr>
<tr>
<td>34</td>
<td>XCLK</td>
</tr>
<tr>
<td>35</td>
<td>D1</td>
</tr>
<tr>
<td>36</td>
<td>DVDD</td>
</tr>
<tr>
<td>37</td>
<td>D0</td>
</tr>
<tr>
<td>38</td>
<td>DOVDD</td>
</tr>
<tr>
<td>39</td>
<td>DGND</td>
</tr>
<tr>
<td>40</td>
<td>DGND</td>
</tr>
<tr>
<td>41</td>
<td>地（GND）</td>
</tr>
<tr>
<td>42</td>
<td>地（GND）</td>
</tr>
<tr>
<td>43</td>
<td>地（GND）</td>
</tr>
<tr>
<td>44</td>
<td>AF_GND</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供上述引脚定义的44针板对板MIPI CSI或DVP并行接口的开发板，例如i.MX RT1160及RT1170 EVK。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield nxp_btb44_ov5640，例如：

```text
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 --shield nxp_btb44_ov5640 samples/subsys/video/capture
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

〔[8](#id16)〕 [https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。

---

[上一章](P134_NXP_Arduino_WiFi_and_BT_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P136_NXP_M.2_IEEE_802.15.4_SPI_RCP_Shield.md)
