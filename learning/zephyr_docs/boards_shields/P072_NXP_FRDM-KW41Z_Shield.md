---
id: learning.zephyr-docs.boards-shields.page-72
title: NXP FRDM-KW41Z Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/frdm_kw41z/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-frdm-kw41z-shield"></a>

<a id="frdm-kw41z-shield"></a>

# 第72章\_NXP FRDM-KW41Z扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/frdm_kw41z/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

FRDM-KW41Z开发套件基于Kinetis® W系列KW41Z／31Z／21Z器件，简称KW41Z。器件采用ARM® Cortex®-M0+，集成2.4 GHz收发器，支持Bluetooth® Smart／低功耗蓝牙（BLE）v4.2、通用频移键控（Generic FSK）、IEEE® 802.15.4及Thread。

[FRDM-KW41Z](../boards_nxp_frdm_imx_kinetis/P015_FRDM-KW41Z.md#frdm_kw41z)可独立使用，也可作为Arduino扩展板。本页介绍扩展板用法，独立开发板用法见FRDM-KW41Z文档。

<a id="bluetooth-controller"></a>

## 蓝牙控制器（Bluetooth Controller）

将FRDM-KW41Z用作带串行主机控制器接口HCI的低功耗蓝牙控制器扩展板，步骤如下：


1. <a id="id16"></a>

  从MCUXpresso SDK Builder网站[注8](#id15)下载FRDM-KW41Z的MCUXpresso SDK。（[MCUXpresso SDK Builder 网站](https://mcuxpresso.nxp.com)）
2. 打开boards/frdmkw41z/wireless_examples/bluetooth/hci_black_box/bm中的MCUXpresso IDE或IAR工程。
3. 打开source/common/app_preinclude.h并添加以下内容：

  ```text
  #define gSerialMgrRxBufSize_c 64
  ```
4. 构建工程，生成hci_black_box_frdmkw41z.bin。
5. 用USB连接FRDM-KW41Z与主机，板卡应枚举为USB大容量存储设备。
6. 将二进制文件复制到该USB存储设备，写入Flash。
7. 拔下USB线，使开发板断电。
8. 按以下方式配置J30及J31：


  - J30第1脚连接J31第2脚
  - J30第2脚连接J31第1脚

  跳线方向应平行于Arduino排针，使UART RX及TX连接到Arduino排针，而不是OpenSDA电路。
9. 将FRDM-KW41Z插到所选主板的Arduino排针，例如[MIMXRT1050-EVK](../boards_nxp_imx_rt10xx/P006_MIMXRT1050-EVK.md#mimxrt1050_evk)或[FRDM-K64F](../boards_nxp_frdm_imx_kinetis/P008_FRDM-K64F.md#frdm_k64f)。
10. 构建Zephyr蓝牙应用时设置--shield frdm_kw41z，例如：

  ```text
  # From the root of the zephyr repository
  west build -b frdm_k64f --shield frdm_kw41z samples/bluetooth/peripheral_hr
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

〔[8](#id16)〕 [https://mcuxpresso.nxp.com](https://mcuxpresso.nxp.com)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。

---

[上一章](P071_NXP_FRDM-CR20A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P073_NXP_FRDM-STBC-AGM01.md)
