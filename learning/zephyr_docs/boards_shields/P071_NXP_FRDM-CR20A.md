---
id: learning.zephyr-docs.boards-shields.page-71
title: NXP FRDM-CR20A
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/frdm_cr20a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-frdm-cr20a"></a>

<a id="frdm-cr20a-shield"></a>

# 第71章\_NXP FRDM-CR20A扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/frdm_cr20a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Freedom开发平台支持MCR20A 2.4 GHz无线收发器。FRDM-CR20A是小型、低功耗、经济的MCR20A参考设计，采用扩展板形态，兼容[FRDM-K64F](../boards_nxp_frdm_imx_kinetis/P008_FRDM-K64F.md#frdm_k64f)等现有Freedom开发平台。

![官方原图：FRDM-CR20A](images/frdm_cr20a.jpg)

<a id="hardware"></a>

## 硬件（Hardware）


- MCR20AVHM

  > - 低功耗（Low-power）
  > - 高性能2.4 GHz收发器，符合IEEE 802.15.4
- 连接能力（Connectivity）

  > - PCB倒F型天线及SMA射频端口
  > - 兼容Arduino
- 电源管理（Power Management）

  > - SMA连接器处可编程输出功率−32～+8 dBm，不带陷波器（原文no trap）
  > - 典型接收灵敏度−102 dBm
- 组件（Components）

  > - 所需匹配元件及外部巴伦数量很少
  > - 1个RGB LED指示灯
  > - 2个按键开关

更多MCR20A SoC及FRDM-CR20A信息见：


- [MCR20A网站](https://www.nxp.com/products/wireless/thread/2.4-ghz-802.15.4-wireless-transceiver:MCR20A)
- [MCR20A数据手册](https://www.nxp.com/docs/en/data-sheet/MCR20AVHM.pdf)
- [MCR20A参考手册](https://www.nxp.com/docs/en/reference-manual/MCR20RM.pdf)
- [FRDM-CR20A网站](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/wireless-connectivy/freedom-development-board-for-mcr20a-wireless-transceiver:FRDM-CR20A)
- [FRDM-CR20A用户指南](https://www.nxp.com/docs/en/user-guide/FRDMCR20AUG.pdf)
- [FRDM-CR20A原理图](https://www.nxp.com/downloads/en/schematics/FRDM-CR20A-SCH.pdf)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield frdm_cr20a，例如：

```text
# From the root of the zephyr repository
west build -b frdm_k64f --shield frdm_cr20a samples/net/wpan_serial
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [MCR20AVHM.pdf](https://www.nxp.com/docs/en/data-sheet/MCR20AVHM.pdf)：HTTP Error 404: Not Found。
- [MCR20RM.pdf](https://www.nxp.com/docs/en/reference-manual/MCR20RM.pdf)：HTTP Error 404: Not Found。
- [FRDMCR20AUG.pdf](https://www.nxp.com/docs/en/user-guide/FRDMCR20AUG.pdf)：HTTP Error 404: Not Found。
- [FRDM-CR20A-SCH.pdf](https://www.nxp.com/downloads/en/schematics/FRDM-CR20A-SCH.pdf)：HTTP Error 404: Not Found。
- [2.4-ghz-802.15.4-wireless-transceiver:MCR20A](https://www.nxp.com/products/wireless/thread/2.4-ghz-802.15.4-wireless-transceiver:MCR20A)：HTTP Error 404: Not Found。
- [freedom-development-board-for-mcr20a-wireless-transceiver:FRDM-CR20A](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/wireless-connectivy/freedom-development-board-for-mcr20a-wireless-transceiver:FRDM-CR20A)：HTTP Error 404: Not Found。

---

[上一章](P070_EVAL-CN0391-ARDZ.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P072_NXP_FRDM-KW41Z_Shield.md)
