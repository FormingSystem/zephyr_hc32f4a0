---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-2
title: FRDM-IMX93
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_imx93/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_imx93"></a>

# 第2章\_FRDM-IMX93

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_imx93/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_imx93.webp](images/frdm_imx93.webp)](images/frdm_imx93.webp)

FRDM-IMX93

名称（Name）：

`frdm_imx93`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

`[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64), [arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)`

片上系统（SoC）：

[mimx9352](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimx9352)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_imx93/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-IMX93是紧凑、低成本的平台，用于展示i.MX 93应用处理器的常用功能。作为入门开发板，它帮助开发者先熟悉处理器，再为更具体的设计投入大量资源。

i.MX93 MPU由包含两个Cortex®-A55内核的集群及一个Cortex®-M33内核组成。原文此处说明Zephyr RTOS移植于Cortex-A55。

<a id="hardware"></a>

## 硬件（Hardware）


- i.MX 93应用处理器（Applications Processor）


  - 处理器最多集成两个Arm Cortex-A55内核，并支持内置Arm Cortex-M33内核。
- RAM：2 GB LPDDR4
- 存储（Storage）：


  - SanDisk 16 GB eMMC 5.1
  - microSD卡插槽（Socket）
- 无线（Wireless）：


  - Murata Type-2EL模块，接口为SDIO、UART及SPI；基于NXP IW612 SoC，支持2.4 GHz／5 GHz双频1×1 Wi-Fi 6、蓝牙5.2及802.15.4
- 通用串行总线（USB）：


  - 一个USB 2.0 Type-C连接器
  - 一个USB 2.0 Type-A连接器
- 以太网（Ethernet）
- PCI-E M.2
- 接插件（Connectors）：


  - 40引脚双排排针
- 发光二极管（LED）：


  - 1个电源状态LED
  - 一个RGB LED
- 调试（Debug）


  - 3引脚JTAG连接器
  - 用于UART调试的USB-C端口，提供分别用于A55及M33的两个COM端口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_imx93`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_imx93-hw-features"></a>

<a id="frdm_imx93-frdm_imx93/mimx9352/a55-hw-features-section"></a>

#### `frdm_imx93/mimx9352/a55`目标（Target）

<a id="frdm_imx93-frdm_imx93/mimx9352/a55-hw-features-panel"></a>

<a id="frdm_imx93-frdm_imx93/mimx9352/a55-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="frdm_imx93-frdm_imx93/mimx9352/a55-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L33">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L24">已禁用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L539">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L525">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX9小数N分频锁相环（Fractional-N PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P029_nxp_imx9-pll.md#std-dtcompatible-nxp-imx9-pll"><code>nxp,imx9-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L152">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L157">已启用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>作为定时器使用的NXP定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L693">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L682">已禁用：5</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P003_nxp_tpm-timer.md#std-dtcompatible-nxp-tpm-timer"><code>nxp,tpm-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L579">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX第3版LCD接口（LCDIFV3）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P020_nxp_imx-lcdifv3.md#std-dtcompatible-nxp-imx-lcdifv3"><code>nxp,imx-lcdifv3</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP增强型直接存储器访问（eDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L553">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P001_nxp_edma.md#std-dtcompatible-nxp-edma"><code>nxp,edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L564">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L650">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L656">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L666">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Motorcomm YT8521以太网PHY（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L103">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P007_motorcomm_yt8521.md#std-dtcompatible-motorcomm-yt8521"><code>motorcomm,yt8521</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L673">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L261">已启用：4</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCAL6408 I2C GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L125">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P016_nxp_pcal6408.md#std-dtcompatible-nxp-pcal6408"><code>nxp,pcal6408</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCAL6524 I2C GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L142">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P020_nxp_pcal6524.md#std-dtcompatible-nxp-pcal6524"><code>nxp,pcal6524</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L325">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L349">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L593">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L60">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L96">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L235">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX i.MX93 MEDIAMIX模块控制（Block Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L186">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P025_nxp_imx93-mediamix.md#std-dtcompatible-nxp-imx93-mediamix"><code>nxp,imx93-mediamix</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX93视频PLL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L192">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P001_nxp_imx93-video-pll.md#std-dtcompatible-nxp-imx93-video-pll"><code>nxp,imx93-video-pll</code></a></td>
</tr>
<tr>
<td rowspan="1">性能状态（Performance State）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX9 Cortex-A应用核性能状态（P-state）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L50">已启用：3</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P001_nxp_imx9-pstate.md#std-dtcompatible-nxp-imx9-pstate"><code>nxp,imx9-pstate</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L772">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L748">已禁用：5</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L611">已禁用：3</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L315">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L305">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L247">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L421">已禁用：8</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L820">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L833">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L211">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L198">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="frdm_imx93-frdm_imx93/mimx9352/a55/smp-hw-features-section"></a>

#### `frdm_imx93/mimx9352/a55/smp`目标（Target）

<a id="frdm_imx93-frdm_imx93/mimx9352/a55/smp-hw-features-panel"></a>

<a id="frdm_imx93-frdm_imx93/mimx9352/a55/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="frdm_imx93-frdm_imx93/mimx9352/a55/smp-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L24">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L539">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L525">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX9小数N分频锁相环（Fractional-N PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P029_nxp_imx9-pll.md#std-dtcompatible-nxp-imx9-pll"><code>nxp,imx9-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L152">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L157">已启用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>作为定时器使用的NXP定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L693">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L682">已禁用：5</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P003_nxp_tpm-timer.md#std-dtcompatible-nxp-tpm-timer"><code>nxp,tpm-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L579">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX第3版LCD接口（LCDIFV3）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P020_nxp_imx-lcdifv3.md#std-dtcompatible-nxp-imx-lcdifv3"><code>nxp,imx-lcdifv3</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP增强型直接存储器访问（eDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L553">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P001_nxp_edma.md#std-dtcompatible-nxp-edma"><code>nxp,edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L564">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L650">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L656">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L666">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Motorcomm YT8521以太网PHY（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L103">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P007_motorcomm_yt8521.md#std-dtcompatible-motorcomm-yt8521"><code>motorcomm,yt8521</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L673">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L261">已启用：4</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCAL6408 I2C GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L125">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P016_nxp_pcal6408.md#std-dtcompatible-nxp-pcal6408"><code>nxp,pcal6408</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCAL6524 I2C GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L142">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P020_nxp_pcal6524.md#std-dtcompatible-nxp-pcal6524"><code>nxp,pcal6524</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L325">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L349">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L593">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L60">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L96">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L235">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX i.MX93 MEDIAMIX模块控制（Block Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L186">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P025_nxp_imx93-mediamix.md#std-dtcompatible-nxp-imx93-mediamix"><code>nxp,imx93-mediamix</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX93视频PLL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L192">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P001_nxp_imx93-video-pll.md#std-dtcompatible-nxp-imx93-video-pll"><code>nxp,imx93-video-pll</code></a></td>
</tr>
<tr>
<td rowspan="1">性能状态（Performance State）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX9 Cortex-A应用核性能状态（P-state）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L50">已启用：3</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P001_nxp_imx9-pstate.md#std-dtcompatible-nxp-imx9-pstate"><code>nxp,imx9-pstate</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_a55.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L772">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L748">已禁用：5</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L611">已禁用：3</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L315">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L305">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L247">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L421">已禁用：8</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L820">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L833">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L211">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L198">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="frdm_imx93-frdm_imx93/mimx9352/m33-hw-features-section"></a>

#### `frdm_imx93/mimx9352/m33`目标（Target）

<a id="frdm_imx93-frdm_imx93/mimx9352/m33-hw-features-panel"></a>

<a id="frdm_imx93-frdm_imx93/mimx9352/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：124 KiB RAM、128 KiB Flash。

<a id="frdm_imx93-frdm_imx93/mimx9352/m33-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L460">已启用：1</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="2">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX指令紧耦合存储器（ITCM / Instruction Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P014_nxp_imx-itcm.md#std-dtcompatible-nxp-imx-itcm"><code>nxp,imx-itcm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L325">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L238">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L248">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L300">已启用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX第3版LCD接口（LCDIFV3）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L371">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P020_nxp_imx-lcdifv3.md#std-dtcompatible-nxp-imx-lcdifv3"><code>nxp,imx-lcdifv3</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L331">已启用：4</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L46">已禁用：8</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_m33.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imx93/frdm_imx93_mimx9352_m33.dts?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L184">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L383">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX i.MX93 MEDIAMIX模块控制（Block Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L394">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P025_nxp_imx93-mediamix.md#std-dtcompatible-nxp-imx93-mediamix"><code>nxp,imx93-mediamix</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX93视频PLL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L469">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P001_nxp_imx93-video-pll.md#std-dtcompatible-nxp-imx93-video-pll"><code>nxp,imx93-video-pll</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L314">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L319">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L400">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L363">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L112">已禁用：8</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此板配置使用24 MHz系统时钟。Cortex-A55最高运行频率1.7 GHz，Cortex-M33最高200 MHz，SYSTICK与M33同频。

<a id="cpu-frequency-scaling-a55"></a>

#### A55 CPU频率调整（Frequency Scaling）

Cortex-A55通过ARM_PLL P-state驱动支持CPU频率调整，提供1.692 GHz、1.4 GHz及900 MHz性能状态。驱动只重新配置内核时钟，因此所有频率都必须能在引导加载程序设置的VDD_SOC电压下工作。（[CPU 调频（CPU Frequency Scaling）](https://docs.zephyrproject.org/latest/services/cpu_freq/index.html#cpu-freq)）

两个Cortex-A55核共享ARM_PLL，因此频率转换总是作用于整个集群。此功能仅支持SMP目标frdm_imx93/mimx9352/a55/smp，由CPU频率子系统为各核设置相同P-state。

使用以下配置运行按需CPU频率调整（On-demand CPU Frequency Scaling）示例：（[按需CPU调频（On-demand CPU frequency scaling）](../power/P019_按需CPU调频示例.md#cpu_freq_on_demand)）

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55/smp samples/subsys/cpu_freq/on_demand
```

<a id="serial-port"></a>

#### 串口（Serial Port）

原文说明，此板为A55及M33使用单一串行通信通道，即CPU的UART2。

<a id="usdhc-sd-or-emmc-interface-on-a55"></a>

#### uSDHC：A55上的SD或eMMC接口

i.MX 93提供3个uSDHC主控制器模块，支持SD／eMMC。FRDM-IMX93的uSDHC2连接MicroSD卡槽P13，uSDHC1连接SoM板上的eMMC。提供usdhc1.overlay及usdhc2.overlay设备树覆盖文件，用于启用指定控制器。

当前依靠U-Boot或Linux在Cortex-A核上启动Zephyr，因此Zephyr需使用不同的uSDHC控制器，避免资源冲突。例如，FRDM-IMX93从使用uSDHC2的SD卡启动时，Zephyr可用uSDHC1上的MMC测试：

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 tests/subsys/sd/mmc -- -DEXTRA_DTC_OVERLAY_FILE=usdhc1.overlay
```

若FRDM-IMX93从使用uSDHC1的MMC启动，Zephyr可用uSDHC2上的SD卡测试：

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 tests/subsys/sd/sdmmc -- -DEXTRA_DTC_OVERLAY_FILE=usdhc2.overlay
```

<a id="user-button-gpio-option"></a>

#### 用户按键GPIO选项（User Button GPIO Option）

USER_BTN1和USER_BTN2默认连接板载PCAL6524 GPIO扩展器，也可改接FRDM-IMX93 GPIO；文档附带设备树覆盖文件支持这种配置。

运行以下命令测试连接到FRDM-IMX93 GPIO的用户按键：

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/basic/button -- -DEXTRA_DTC_OVERLAY_FILE=frdm_imx93_mimx9352_native_btn.overlay
```

注意：覆盖文件仅支持mimx9352/a55；启用I2C及PCAL6524后，可扩展至mimx9352/m33。此条件按原文保留。

<a id="pwm-tpm"></a>

#### PWM，使用TPM

A55核为[PWM Blinky](../basic_samples/P004_PWM闪烁LED.md#pwm-blinky)应用启用TPM3，板上RGB LED LED1的绿色通道会以不同频率闪烁。

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/basic/blinky_pwm
```

<a id="programming-and-debugging-a55"></a>

## A55编程与调试（Programming and Debugging）

`frdm_imx93`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>复位（reset）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

有多种在A55核上编程及调试Zephyr的方法：

<a id="option-1-boot-zephyr-by-using-u-boot-command"></a>

### 选项1：使用U-Boot命令启动Zephyr

U-Boot的cpu命令用于加载Zephyr并启动Cortex-A次级核。目前[Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot)支持此命令，分支格式为uboot_vxxxx.xx-y.y.y，其中xxxx.xx为U-Boot版本，y.y.y为[Real-Time Edge软件](https://www.nxp.com/rtedge)版本。例如，uboot_v2023.04-2.9.0表示Real-Time Edge Software v2.9.0使用的U-Boot v2023.04。预构建镜像及用户指南见Real-Time Edge Software。

将编译的zephyr.bin复制到SD卡第一个FAT分区，插入开发板，上电后在提示符处停止U-Boot执行。

使用U-Boot加载zephyr.bin并启动Cortex-A55 Core1：

```text
fatload mmc 1:1 0xd0000000 zephyr.bin; dcache flush; icache flush; cpu 1 release 0xd0000000
```

也可使用以下命令启动Core0上的zephyr.bin：

```text
fatload mmc 1:1 0xd0000000 zephyr.bin; dcache off; icache flush; go 0xd0000000
```

此配置可运行基础Zephyr应用及内核测试，例如[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)示例：

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/synchronization
```

这将构建包含同步（Synchronization）示例的镜像，启动后控制台输出如下：

```text
*** Booting Zephyr OS build v4.1.0-41-g6395333e3d18 ***
thread_a: Hello World from cpu 0 on frdm_imx93!
thread_b: Hello World from cpu 0 on frdm_imx93!
thread_a: Hello World from cpu 0 on frdm_imx93!
thread_b: Hello World from cpu 0 on frdm_imx93!
```

<a id="option-2-boot-zephyr-by-using-jlink-runner"></a>

### 选项2：使用J-Link运行工具（Runner）启动Zephyr

<a id="hardware-setup"></a>

#### 硬件设置（Hardware Setup）

默认运行工具为J-Link。FRDM-IMX93上有一个SWD连接器P14。

按[NXP在线文档](https://community.nxp.com/t5/FRDM-Training-Hub/How-to-use-J-link-on-FRDM-IMX93/ta-p/2122902)改装FRDM-IMX93，并将SWD连接器P14连接J-Link调试器。

<a id="flash-and-run"></a>

#### 烧录与运行（Flash and Run）

给开发板上电，并停在U-Boot命令行。

随后使用west flash从主机加载zephyr.bin，并启动A55核上的Zephyr应用。

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/hello_world
west flash
```

UART1控制台应显示以下日志：

```text
*** Booting Zephyr OS build v4.3.0-1976-g8f0df404c2ee ***
Hello World! frdm_imx93/mimx9352
```

<a id="debug"></a>

#### 调试（Debug）

给开发板上电，并停在U-Boot命令行。

随后使用west debug从主机加载zephyr.bin，并调试A55核上的Zephyr应用。

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/hello_world
west debug
```

<a id="option-3-boot-zephyr-by-using-spsdk-runner"></a>

### 选项3：使用SPSDK运行工具（Runner）启动Zephyr

SPSDK运行工具使用[https://spsdk.readthedocs.io](https://spsdk.readthedocs.io)提供的工具集，构建包含全部所需固件组件的可启动镜像flash.bin。west flash可将其下载到DDR、SD卡或eMMC。镜像不包含U-Boot，因此由TF-A直接启动第一个Cortex-A55核上的Zephyr。

使用SPSDK运行工具前需要获取二进制组件（Binary Blobs），命令如下：

```text
west blobs fetch hal_nxp
```

注意（Note）

建议在 `west update` 之后运行上述命令。

SPSDK运行工具通过CONFIG_BOARD_NXP_SPSDK_IMAGE启用，FRDM-IMX93默认未启用。以下以基本同步示例说明配置方法：（[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)）

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/synchronization -- -DCONFIG_BOARD_NXP_SPSDK_IMAGE=y
```

若开发板变体提供并启用CONFIG_BOARD_NXP_SPSDK_IMAGE，将自动生成flash.bin。编程前，将SW1[3:0]设为0b0001，以USB下载模式启动，并把USB1及DBG端口连接Linux主机。系统枚举两个115200、8N1串口，第二个用于Cortex-A55 Zephyr控制台。spsdk烧录工具已通过scripts/requirements.txt安装；Linux下需按[https://spsdk.readthedocs.io](https://spsdk.readthedocs.io)的安装指南配置USB设备权限。随后可执行以下命令：

```text
# load and run without programming. for next flashing, need to reset the board firstly
$ west flash -r spsdk

# program to SD card, then set SW1[3:0]=0b0011 to reboot from SD
$ west flash -r spsdk --bootdevice sd

# program to emmc card, then set SW1[3:0]=0b0010 to reboot from EMMC
$ west flash -r spsdk --bootdevice=emmc
```

Zephyr日志随后显示在第二个串口控制台。

<a id="system-reboot-a55"></a>

### A55系统重启（System Reboot）

当前i.MX93仅支持冷重启（Cold Reboot），不支持热重启（Warm Reboot）。可用以下配置及自定义Shell模块示例验证冷重启：（[自定义Shell模块（Custom Shell module）](../interaction/P010_Shell命令模块示例.md#shell-module)）

```text
# From the root of the zephyr repository
west build -b frdm_imx93/mimx9352/a55 samples/subsys/shell/shell_module
```

这将构建包含Shell示例的镜像。启动后，在Shell命令行执行kernel reboot：

```text
uart:~$ kernel reboot cold
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

原文概述的最高1.7 GHz和P-state中的1.692 GHz分别保留；共用ARM_PLL的A55核必须作为SMP集群一起调频，电压由引导加载程序预设。U-Boot启动辅助核依赖原文指定的Real-Time Edge分支；J-Link连接要求先完成官方硬件返工。SPSDK调试串口为第二路，区别于IMX91的第一路。UART2及USERBTN相关表述按原文保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2122902](https://community.nxp.com/t5/FRDM-Training-Hub/How-to-use-J-link-on-FRDM-IMX93/ta-p/2122902)：HTTP Error 403: Forbidden。
- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [rtedge](https://www.nxp.com/rtedge)：HTTP Error 404: Not Found。

---

[上一章](P001_FRDM-IMX91.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_FRDM-IMXRT1152.md)
