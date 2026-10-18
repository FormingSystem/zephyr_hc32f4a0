---
id: learning.zephyr-docs.boards-phytec.page-6
title: phyBOARD-Nash i.MX93
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/phytec/phyboard_nash/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="phyboard_nash"></a>

# 第6章\_phyBOARD-Nash i.MX93

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/phytec/phyboard_nash/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/phyboard_nash.webp](images/phyboard_nash.webp)](images/phyboard_nash.webp)

phyBOARD-Nash i.MX93

名称（Name）：

`phyboard_nash`

厂商（Vendor）：

[PHYTEC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=phytec)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[mimx9352](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimx9352)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/phytec/phyboard_nash/doc/index.rst/../..)<a id="phyboard-nash-i-mx93"></a>

## phyBOARD-Nash i.MX93

<a id="overview"></a>

### 概述（Overview）

phyBOARD-Nash基于phyCORE-i.MX93核心模块，后者基于NXP i.MX93 SoC。此板提供常见工业接口，可作开发参考或用于最终产品；作为入门板，可先熟悉模块，再投入更多资源开展专用设计。

i.MX93微处理器（MPU）包含一个双Cortex-A55集群及一个Cortex-M33核。Zephyr既移植到单个A55核，也移植到M33核。


- 存储器（Memory）：

  > - RAM：512 MB—2 GB LPDDR4
  > - EEPROM：4—32 KB
  > - eMMC：8—256 GB
- 接口（Interfaces）：

  > - 以太网：两路10／100BASE-T，其中一路支持时间敏感网络（TSN）
  > - USB：两路USB 2.0主机／OTG
  > - 串口：一路RS232／RS485，支持全双工／半双工
  > - CAN：一路CAN FD
  > - 数字I/O：通过扩展连接器
  > - MMX／SD／SDIO：MicroSD卡槽，MMX拼写按原文保留
  > - 显示：LVDS，1×4或1×8；MIPI DSI，1×4；以及HDMI
  > - 音频：串行音频接口（SAI）
  > - 摄像头：一路MIPI CSI-2，即phyCAM-M，以及一路并行接口
  > - 扩展总线：I2C、SPI、SDIO、UART及USB
- 调试（Debug）：

  > - 10引脚JTAG连接器
  > - USB-C UART调试接口，分别为A55及M33提供两个串口

[![官方原图：phyBOARD-Nash](images/phyboard_nash1.webp)](images/phyboard_nash1.webp)

开发板更多信息见[PHYTEC网站](https://www.phytec.eu/en/produkte/development-kits/phyboard-nash/)。

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`phyboard_nash`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="phyboard_nash-hw-features"></a>

<a id="phyboard_nash-phyboard_nash/mimx9352/a55-hw-features-section"></a>

##### `phyboard_nash/mimx9352/a55`目标（Target）

<a id="phyboard_nash-phyboard_nash/mimx9352/a55-hw-features-panel"></a>

<a id="phyboard_nash-phyboard_nash/mimx9352/a55-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="phyboard_nash-phyboard_nash/mimx9352/a55-hw-features-table"></a>

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
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L525">已禁用：2</a>）</td>
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
<td>作为定时器使用的NXP定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L682">已禁用：6</a>）</td>
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
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L650">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L656">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L666">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L673">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L261">已禁用：4</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L325">已禁用：8</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L593">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L96">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
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
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L748">已禁用：6</a>）</td>
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
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L820">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L198">已禁用：2</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="phyboard_nash-phyboard_nash/mimx9352/m33-hw-features-section"></a>

##### `phyboard_nash/mimx9352/m33`目标（Target）

<a id="phyboard_nash-phyboard_nash/mimx9352/m33-hw-features-panel"></a>

<a id="phyboard_nash-phyboard_nash/mimx9352/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：124 KiB RAM、128 KiB Flash。

<a id="phyboard_nash-phyboard_nash/mimx9352/m33-hw-features-table"></a>

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
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L460">已禁用：1</a>）</td>
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
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L300">已禁用：2</a>）</td>
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
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
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

#### 设备（Devices）

<a id="system-clock"></a>

##### 系统时钟（System Clock）

此板配置使用24 MHz系统时钟。Cortex-A55最高运行频率1.7 GHz，Cortex-M33最高200 MHz，SYSTICK与M33同频。

<a id="serial-port"></a>

##### 串口（Serial Port）

此配置为A55及M33使用CPU的UART2作为串行通信通道。U-Boot或Linux通过第二个串口输出调试信息。

<a id="programming-and-debugging-a55"></a>

### A55编程与调试（Programming and Debugging）

将构建出的zephyr.bin复制到SD卡BOOT分区，插卡上电，并在U-Boot提示符处停止自动启动。

使用U-Boot在Cortex-A55 Core0上加载并执行zephyr.bin：

```text
fatload mmc 1:1 0xd0000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0xd0000000
```

使用此配置运行基本Zephyr应用及内核测试，例如：

```text
# From the root of the zephyr repository
west build -b phyboard_nash/mimx9352/a55 samples/hello_world
```

使用此配置运行基本Zephyr应用，例如：

```text
*** Booting Zephyr OS build v3.7.0-848-gb4d99b124c6d ***
Hello World! phyboard_nash/mimx9352/a55
```

<a id="programming-and-debugging-m33"></a>

### M33编程与调试（Programming and Debugging）

将构建出的zephyr.bin复制到SD卡BOOT分区，插卡上电，并在U-Boot提示符处停止自动启动。

使用U-Boot加载zephyr.bin，并启动Cortex-M33核：

```text
load mmc 1:1 0x80000000 zephyr.bin;cp.b 0x80000000 0x201e0000 0x30000;bootaux 0x1ffe0000 0
```

使用此配置运行基本Zephyr应用，例如：

```text
# From the root of the zephyr repository
west build -b phyboard_nash/mimx9352/m33 samples/hello_world
```

这将构建包含同步（Synchronization）示例的镜像，启动后控制台输出如下：

```text
*** Booting Zephyr OS build v3.7.0-848-gb4d99b124c6d ***
Hello World! phyboard_nash/mimx9352/m33
```

<a id="starting-the-m33-core-from-u-boot-and-linux"></a>

#### 从U-Boot及Linux启动M33核

Linux支持通过remoteproc加载二进制并启动M33，更多信息见[phyCORE-i.MX93 BSP手册](https://phytec.github.io/doc-bsp-yocto/bsp/imx9/imx9.html)。

<a id="references"></a>

#### 参考资料（References）

更多信息见[PHYTEC网站](https://www.phytec.eu/en/produkte/development-kits/phyboard-nash/)。

## 译注

Nash支持A55及M33，保留U-Boot启动A55和Linux remoteproc启动M33的区别。原文MMX／SD／SDIO拼写保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [imx9.html](https://phytec.github.io/doc-bsp-yocto/bsp/imx9/imx9.html)：HTTP Error 404: Not Found。

---

[上一章](P005_phyBOARD-Lyra_AM62x_M4F_Core.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_phyBOARD-Polis_i.MX8M_Mini.md)
