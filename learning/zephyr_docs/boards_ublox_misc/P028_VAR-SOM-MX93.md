---
id: learning.zephyr-docs.boards-ublox-misc.page-28
title: VAR-SOM-MX93
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/variscite/imx93_var_som/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="imx93_var_som"></a>

# 第28章\_VAR-SOM-MX93

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/variscite/imx93_var_som/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/imx93_var_som.webp](images/imx93_var_som.webp)](images/imx93_var_som.webp)

VAR-SOM-MX93

名称（Name）：

`imx93_var_som`

厂商（Vendor）：

[Variscite Ltd.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=variscite)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[mimx9352](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimx9352)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/variscite/imx93_var_som/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

VAR-SOM-MX93为低功耗系统模块提供高性能处理能力，基于NXP i.MX 93系列，面向智能家居、楼宇控制、非接触式人机界面（HMI）、物联网边缘及工业应用。原文称其为最新的功耗优化处理器，属于该页的版本背景。

i.MX 93包含最高1.7 GHz的双核Arm Cortex-A55，集成用于机器学习推理加速的NPU；另有最高250 MHz的通用Cortex-M33负责实时和低功耗处理。CAN-FD接口用于控制网络，两个1 Gbit/s以太网控制器支持低延迟网关应用，其中一个支持时间敏感网络（Time Sensitive Networking，TSN）。

Zephyr已移植到Cortex-A55与Cortex-M33，可选择其一运行。

<a id="specs-summary"></a>

## 规格概览（Specs Summary）

> - 中央处理器（CPU）
>
>
>   - NXP i.MX 93：
>   - 2个Cortex-A55核，1.7 GHz
>   - 1个Cortex-M33核，250 MHz
>   - 1个Ethos-U65微型神经网络处理器（microNPU），0.5 TOPS
> - 存储器（Memory）
>
>
>   - 最高2 GB LPDDR4 RAM
> - 图形处理器（GPU）
>
>
>   - PXP二维像素加速引擎
> - 神经网络处理器（Neural Processing Unit，NPU）
>
>
>   - 神经网络性能：256个乘加单元（MAC），最高1.0 GHz，每MAC每周期2次运算
>   - NPU面向8位及16位整数循环神经网络（RNN）
>   - 处理8位权重（Weights）
> - 显示（Display）
>
>
>   - LVDS最高1366×768p60或1280×800p60
>   - 并行RGB最高1366×768p60或1280×800p60
>   - 1路MIPI DSI，最高1920×1200p60，24位
> - 网络（Network）
>
>
>   - 2路10／100／1000 Mbit/s以太网接口
>   - 通过认证的Wi-Fi，支持802.11ax/ac/a/b/g/n
>   - 蓝牙／低功耗蓝牙5.4（Bluetooth／BLE 5.4）
> - 摄像头（Camera）
>
>
>   - 1路双通道MIPI CSI-2摄像头输入
> - 音频（Audio）
>
>
>   - 耳机（Headphones）
>   - 麦克风：数字、模拟立体声
>   - 3路I2S（SAI）、S/PDIF、4通道PDM
> - 通用串行总线（USB）
>
>
>   - 2路USB 2.0 OTG
> - 串行接口（Serial Interfaces）
>
>
>   - SPI：7路
>   - I2C：7路
>   - UART：7路，最高5 Mbit/s
>   - CAN：2路
> - 温度范围（Temperature Range）
>
>
>   - −40 °C至85 °C

SoM更多信息见[Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX93)及[Variscite网站](https://www.variscite.com/product/system-on-module-som/cortex-a55/var-som-mx93-nxp-i-mx-93/)。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`imx93_var_som`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="imx93_var_som-hw-features"></a>

<a id="imx93_var_som-imx93_var_som/mimx9352/a55-hw-features-section"></a>

### `imx93_var_som/mimx9352/a55`目标（Target）

<a id="imx93_var_som-imx93_var_som/mimx9352/a55-hw-features-panel"></a>

<a id="imx93_var_som-imx93_var_som/mimx9352/a55-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="imx93_var_som-imx93_var_som/mimx9352/a55-hw-features-table"></a>

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
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L272">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L261">已禁用：2</a>）</td>
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
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som_mimx9352_a55.dts?plain=1#L61">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som_mimx9352_a55.dts?plain=1#L53">已启用：1</a>）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som_mimx9352_a55.dts?plain=1#L35">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx93_a55.dtsi?plain=1#L305">已禁用：2</a>）</td>
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

<a id="imx93_var_som-imx93_var_som/mimx9352/m33-hw-features-section"></a>

### `imx93_var_som/mimx9352/m33`目标（Target）

<a id="imx93_var_som-imx93_var_som/mimx9352/m33-hw-features-panel"></a>

<a id="imx93_var_som-imx93_var_som/mimx9352/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：124 KiB RAM、128 KiB Flash。

<a id="imx93_var_som-imx93_var_som/mimx9352/m33-hw-features-table"></a>

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
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som_mimx9352_m33.dts?plain=1#L42">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som_mimx9352_m33.dts?plain=1#L34">已启用：1</a>）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx93_var_som/imx93_var_som-m33-common.dtsi?plain=1#L11">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx93_m33.dtsi?plain=1#L363">已禁用：1</a>）</td>
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

注意（Note）

建议在Linux主机侧禁用M33所使用的外设。

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此板配置使用24 MHz系统时钟。Cortex-A55最高运行频率1.7 GHz，Cortex-M33最高200 MHz，SYSTICK与M33同频。

<a id="serial-port"></a>

#### 串口（Serial Port）

此板级配置为A55与M33使用CPU的UART7作为唯一串行通信通道。

<a id="programming-and-debugging-a55"></a>

## A55编程与调试（Programming and Debugging）

将编译好的zephyr.bin复制到SD卡的boot目录，插入开发板，上电后在提示符处中断U-Boot自动启动。

通过U-Boot在Cortex-A55上加载并运行zephyr.bin：

```text
load mmc $mmcdev:$mmcpart $loadaddr /boot/zephyr.bin
dcache off; icache flush; go $loadaddr
```

可使用此配置运行基本Zephyr应用及内核测试，例如[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)：

```text
# From the root of the zephyr repository
west build -b imx93_var_som/mimx9352/a55 samples/hello_world
```

上述命令构建含hello_world示例的镜像，加载运行后，RAM控制台应显示：

```text
*** Booting Zephyr OS build v4.0.0-45-gf012a8b9f506 ***
Hello World! imx93_var_som/mimx9352/a55
```

<a id="programming-and-debugging-m33"></a>

## M33编程与调试（Programming and Debugging）

`imx93_var_som`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

M33镜像有两种加载方法：U-Boot命令及Linux远程处理器框架（remoteproc）。

<a id="load-and-run-m33-zephyr-image-from-u-boot"></a>

### 从U-Boot加载并运行M33 Zephyr镜像

要从A55通过U-Boot加载M33上的Zephyr，将编译好的zephyr.bin复制到SD卡boot目录，插入板卡，上电并在提示符处中断U-Boot。

使用以下命令将M33二进制加载到所需存储区域并启动：

```text
load mmc $mmcdev:$mmcpart 0x80000000 /boot/zephyr.bin
cp.b 0x80000000 0x201e0000 0x30000
bootaux 0x1ffe0000 0
```

<a id="load-and-run-m33-zephyr-image-by-using-linux-remoteproc"></a>

### 通过Linux remoteproc加载并运行M33 Zephyr镜像

通过scp或USB存储设备，将zephyr.bin及zephyr.elf分别复制到SoM上的/boot及/lib/firmware。

在Linux中运行Cortex-M33二进制前，必须启用专供Cortex-M33应用的设备树：

```text
root@imx93-var-som:~# fw_setenv fdt_file imx93-var-som-symphony-m33.dtb
root@imx93-var-som:~# reboot
```

可用Variscite为MCUXpresso二进制提供的remoteproc脚本运行Zephyr二进制：

```text
root@imx93-var-som:~# /etc/remoteproc/variscite-rproc-linux -f /lib/firmware/zephyr.elf
[   44.366948] remoteproc remoteproc0: powering up imx-rproc
[   44.374250] remoteproc remoteproc0: Booting fw image zephyr.elf, size 469352
[   44.383338] remoteproc remoteproc0: No resource table in elf
[   44.904615] remoteproc remoteproc0: remote processor imx-rproc is now up
```

UART7串口控制台应显示以下结果：

```text
*** Booting Zephyr OS build v4.0.0-44-g93cbaccbbc41 ***
Hello World! imx93_var_som/mimx9352/m33
```

也可配置U-Boot在启动时加载固件：

```text
root@imx93-var-som:~# /etc/remoteproc/variscite-rproc-u-boot -f /boot/zephyr.bin
Configuring for TCM memory
+ fw_setenv m33_addr 0x201E0000
+ fw_setenv fdt_file imx93-var-som-symphony-m33.dtb
+ fw_setenv use_m33 yes
+ fw_setenv m33_bin zephyr.bin

Finished: Please reboot, the m33 firmware will run during U-Boot
```

Variscite remoteproc脚本及Cortex-M33支持的更多信息见[Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX93)。

<a id="references"></a>

## 参考资料（References）


- [Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX93)
- [Variscite网站](https://www.variscite.com/product/system-on-module-som/cortex-a55/var-som-mx93-nxp-i-mx-93/)
- [NXP网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-processors/i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93)

## 译注

VAR-SOM-MX93保留其独立板级目标与加载命令，控制台为UART7。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [index.php?title=VAR-SOM-MX93](https://variwiki.com/index.php?title=VAR-SOM-MX93)：HTTP Error 403: Forbidden。
- [i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-processors/i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93)：HTTP Error 404: Not Found。
- [](https://www.variscite.com/product/system-on-module-som/cortex-a55/var-som-mx93-nxp-i-mx-93/)：HTTP Error 403: Forbidden。

---

[上一章](P027_DART-MX93.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P029_Variscite.md)
