---
id: learning.zephyr-docs.boards-nxp-imx-rt-multicore.page-4
title: MIMXRT2660-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt2660_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt2660_evk"></a>

# 第4章\_MIMXRT2660-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt2660_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`mimxrt2660_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt2663](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt2663)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt2660_evk/doc/index.rst/../..)<a id="mimxrt2660-evk"></a>

<a id="id1"></a>

## MIMXRT2660-EVK

<a id="overview"></a>

### 概述（Overview）

MIMXRT2660-EVK是NXP i.MX RT266x系列评估板，采用MIMXRT2663跨界MCU。i.MX RT266x按子系统分区设计：单个Arm Cortex-M85计算核与HSP、MAIN、WAKE、AUDIO、MEDIA、COMM、SYSCON及VBAT域并列，各域具有独立时钟及电源控制。

<a id="hardware"></a>

### 硬件（Hardware）


- MIMXRT2663跨界微控制器（Crossover MCU）：


  - 最高1 GHz Arm Cortex-M85，支持Helium、TrustZone、内存保护单元（MPU）及一级缓存（L1 Cache）
  - 256 KB指令紧耦合存储器（ITCM）、256 KB数据紧耦合存储器（DTCM），以及3个各256 KB的片上RAM存储体（Banks）
  - Neutron N256神经网络处理单元（NPU）及显示／图形子系统
  - 两个xSPI接口，分别为8位及16位；另有8路UART、4路I2C、2路I3C及6路SPI
  - 两路支持时间敏感网络（TSN）的千兆以太网、两路10BASE-T1S及3路CAN FD
  - EdgeLock安全隔离区（Security Enclave）及末级缓存（Last-level Cache）
- 开发板（Board）：


  - MIMXRT2663CVVAA，工业级、289球BGA、0.8 mm间距、1 GHz
  - XSPI0上的64 MB Winbond W25H512NWEAM串行NOR闪存
  - XSPI1上的32 MB Winbond W958D6NMYA Xccela伪静态RAM（PSRAM）
  - eMMC、SD卡槽、以太网及USB
  - 板载MCU-Link调试探针

<a id="id3"></a>

<a id="id4"></a>

i.MX RT266x SoC及此板的更多信息见[i.MX RT2660参考手册](https://www.nxp.com/) [注1](#id2)及数据手册 [注1](#id2)。（[i.MX RT2660数据手册](https://www.nxp.com/)）

<a id="memory-layout"></a>

#### 内存布局（Memory Layout）

此板从外部闪存就地执行（XIP），并使用外部RAM：


- zephyr,flash指向64 MB XSPI0 NOR闪存，代码从中就地执行。
- zephyr,sram指向32 MB XSPI1 PSRAM，.data、.bss、内核栈及堆位于其中。
- ITCM保存时钟启动配置期间使用的代码，DTCM中的临时栈支撑该阶段执行。重新配置PLL时需暂停两个XSPI控制器，因此在该时段内，运行的代码及其栈都不能位于外部存储器。其他内容无需迁移，应用仍可使用完整PSRAM保存自己的栈及堆，TCM也保留给应用使用。

运行此镜像前，启动ROM会依据启动头初始化两种存储器：NOR使用闪存配置块（FCB），PSRAM使用外部存储器配置数据。

注意（Note）

此SoC的启动ROM采用基于容器的高级高保障启动（AHAB）镜像格式，不读取镜像向量表（IVT）。构建产出ROM读取的3个块：偏移0x400处的闪存配置块、0xA00处的外部存储器配置数据，以及0x1000处的AHAB容器；镜像本体位于0xC000。因此将zephyr.bin写入启动闪存后即可从冷复位启动，无需构建后处理。原文说明，评估板的出厂生命周期（Out-of-fab Life Cycle）忽略认证错误，因此无需签名，容器包含空签名块。

注意（Note）

此目标只用闪存执行代码，不包含闪存驱动及分区，因此不能使用Flash API、MCUboot或基于闪存的Settings存储。启用闪存驱动需要移植Zephyr共享XSPI驱动，因为这些驱动引用了此SoC未实现的xspi_config_t字段。

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`mimxrt2660_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt2660_evk-hw-features"></a>

<a id="mimxrt2660_evk-mimxrt2660_evk/mimxrt2663/cm85-hw-features-section"></a>

##### `mimxrt2660_evk/mimxrt2663/cm85`目标（Target）

<a id="mimxrt2660_evk-mimxrt2660_evk/mimxrt2663/cm85-hw-features-panel"></a>

<a id="mimxrt2660_evk-mimxrt2660_evk/mimxrt2663/cm85-hw-features-memory"></a>

该开发板目标的片上存储容量：32 MiB RAM、64 MiB Flash。

<a id="mimxrt2660_evk-mimxrt2660_evk/mimxrt2663/cm85-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x_cm85.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1634">已禁用：2</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L952">已禁用：3</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="9">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX时钟生成单元模拟模块（CGUANA），负责产生时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L117">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P028_nxp_imx-cguana.md#std-dtcompatible-nxp-imx-cguana"><code>nxp,imx-cguana</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的晶体振荡器（Crystal Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L124">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P027_nxp_imx-cguana-sxosc.md#std-dtcompatible-nxp-imx-cguana-sxosc"><code>nxp,imx-cguana-sxosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的高频自由运行振荡器（FRO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L143">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P026_nxp_imx-cguana-fro192m.md#std-dtcompatible-nxp-imx-cguana-fro192m"><code>nxp,imx-cguana-fro192m</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的低频自由运行振荡器（FRO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L151">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P025_nxp_imx-cguana-fro12m.md#std-dtcompatible-nxp-imx-cguana-fro12m"><code>nxp,imx-cguana-fro12m</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的整数锁相环（Integer PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L160">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P023_nxp_imx-cguana-core-pll.md#std-dtcompatible-nxp-imx-cguana-core-pll"><code>nxp,imx-cguana-core-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的分数锁相环（Fractional PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L176">已启用：2</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P024_nxp_imx-cguana-frac-pll.md#std-dtcompatible-nxp-imx-cguana-frac-pll"><code>nxp,imx-cguana-frac-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CGUANA中的音频／视频锁相环（Audio/Video PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L210">已启用：2</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P022_nxp_imx-cguana-avpll.md#std-dtcompatible-nxp-imx-cguana-avpll"><code>nxp,imx-cguana-avpll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX第3版时钟控制模块（CCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L254">已启用：7</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P020_nxp_imx-ccm-rev3.md#std-dtcompatible-nxp-imx-ccm-rev3"><code>nxp,imx-ccm-rev3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX CCM第3版控制器中的一个可配置时钟根（Clock Root）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L312">已启用：20</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P019_nxp_imx-ccm-rev3-root.md#std-dtcompatible-nxp-imx-ccm-rev3-root"><code>nxp,imx-ccm-rev3-root</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1589">已禁用：4</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="5">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器（QTMR / Quad Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1316">已启用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P005_nxp_imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr"><code>nxp,imx-qtmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器通道（Quad Timer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1323">已禁用：16</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P007_nxp_imx-tmr.md#std-dtcompatible-nxp-imx-tmr"><code>nxp,imx-tmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1482">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1493">已禁用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1555">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1672">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX低功耗数模转换器（LPDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1664">已禁用：1</a>）</td>
<td><a href="../hardware/P770_NXP低功耗数模转换器绑定.md#dtbinding-nxp-lpdac"><code>nxp,lpdac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1679">已禁用：4</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1826">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1833">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1842">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1849">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1859">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare媒体访问控制器（MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1866">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P007_snps_dwmac.md#std-dtcompatible-snps-dwmac"><code>snps,dwmac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt2660_evk/mimxrt2660_evk.dtsi?plain=1#L60">已禁用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P019_nxp_xspi-nor.md#std-dtcompatible-nxp-xspi-nor"><code>nxp,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L707">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L718">已禁用：5</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P029_nxp_imx-gpio-v2.md#std-dtcompatible-nxp-imx-gpio-v2"><code>nxp,imx-gpio-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L789">已禁用：4</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1789">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L923">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt2660_evk/mimxrt2660_evk.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt2660_evk/mimxrt2660_evk.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L992">已禁用：3</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x_cm85.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt2660_evk/mimxrt2660_evk.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L555">已启用：3</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>在MCUX RT266x SoC设备树中设有pinctrl节点标签的节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L559">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P014_nxp_mcux-rt266x-pinctrl.md#std-dtcompatible-nxp-mcux-rt266x-pinctrl"><code>nxp,mcux-rt266x-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1023">已启用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1028">已禁用：16</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1227">已禁用：8</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1744">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1445">已禁用：4</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P008_nxp_mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec"><code>nxp,mcux-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L597">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L613">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L838">已禁用：6</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1771">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1782">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX CMOS传感器接口（Sensor Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1889">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P008_nxp_imx-csi.md#std-dtcompatible-nxp-imx-csi"><code>nxp,imx-csi</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt266x.dtsi?plain=1#L1626">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt2663_cm85_ns.dtsi?plain=1#L43">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt266x/nxp_rt2663_cm85_ns.dtsi?plain=1#L47">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

<a id="connections-and-i-os"></a>

#### 连接与I/O（Connections and I/Os）

<table>
<tr>
<th>功能（Function）</th>
<th>信号（Signal）</th>
<th>焊盘（Pad）</th>
</tr>
<tr>
<td>控制台（Console）</td>
<td>LPUART0发送数据（TXD）</td>
<td>PIO3_30</td>
</tr>
<tr>
<td>控制台（Console）</td>
<td>LPUART0接收数据（RXD）</td>
<td>PIO3_31</td>
</tr>
<tr>
<td>用户LED（User LED）</td>
<td>HSP GPIO0第26脚</td>
<td>PIO2_26，D16，低电平有效</td>
</tr>
<tr>
<td>用户开关（User SW）</td>
<td>WAKE GPIO0第0脚</td>
<td>PIO1_0，WAKE_SS_BTN</td>
</tr>
<tr>
<td>XSPI0</td>
<td>SCLK0、SS0_N及DATA0—DATA3</td>
<td>PIO6_0、PIO6_1及PIO6_2—PIO6_5；四线模式，此板闪存未按八线方式连接</td>
</tr>
</table>

调试控制台通过MCU-Link虚拟COM端口运行，参数为115200、8N1。

<a id="system-clock"></a>

#### 系统时钟（System Clock）

板卡启动时通过电源控制器进入超驱动运行（Over Drive Run）工作点，使Cortex-M85运行于1 GHz。此转换还需将PLL参考源从片上振荡器切换到板载晶体，所以其中一部分代码在关闭缓存及两个xSPI控制器后从RAM执行。这也是相关代码及栈分别放在ITCM和DTCM、不能放在外部存储器的原因。

系统定时器计数的是板载晶体派生的外部24 MHz参考，即计算子系统的SysTick时钟根，而非内核时钟。因此节拍精度由晶体决定，不依赖核心频率。

外设时钟根在设备树中用nxp,imx-ccm-rev3-root节点描述。按其在时钟树中的位置，有两种配置方式。

上游及共享时钟根：CGU分配根，以及没有单一使用者的时钟根，如main_rootclk或为全部PERI3来源外设供时钟的peri3_rootclk，其多路选择及分频属性写在时钟根节点本身。应用可用覆盖文件更改这类根，无需修改板级C代码，所有从它取时钟的叶节点会一起变化。例如，修改共享PERI3根的时钟来源：

```text
&peri3_rootclk {
        clock-mux = <IMX_CCM_MUX_PERI3_SYSPLL_DIVOUT2>;
        clock-div = <1>;
};
```

外设叶时钟根：由单个设备独占的实例功能时钟根，如每个LPUART，将默认多路选择及分频参数内联放在使用它的外设节点中，作为门控时钟之外的第二个clocks条目。这样无需单独覆盖文件，各设备即可获得板级默认配置。控制台LPUART0使用PERI3五分频，即80 MHz：

```text
&lpuart0 {
        clock-names = "gate", "source";
        clocks = <&ccm IMX_CCM_CLK(IMX_CCM_LPCG_MAIN_HSP_LPUART0,
                                   IMX_CCM_ROOT_MAIN_LPUART0_FCLK)>,
                 <&ccm IMX_CCM_ROOT_CFG(IMX_CCM_ROOT_MAIN_LPUART0_FCLK,
                                        IMX_CCM_MUX_LPUART0_PERI3, 5, 1)>;
};
```

目前只有LPUART驱动读取第二个条目。尚未应用该条目的外设驱动会保留时钟根复位值，因此仅为LPSPI、LPI2C等添加该条目，不会改变实际时钟。

注意（Note）

只有外设叶时钟根适合按上述方式安全改配。模拟源、CPU及总线根、PLL分配根也都是设备树节点，SoC时钟初始化读取这些节点而非硬编码数值；但它们需要在前述参考源切换过程中暂停、断电及重新切换，所以单改属性无法保证其他设置工作。两个xSPI功能时钟根在xspi0／xspi1节点上声明，而非作为控制器子节点，还会在该切换阶段由代码手工写入。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

`mimxrt2660_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

#### 配置调试探针（Configuring a Debug Probe）

此板默认配置为使用板载MCU-Link CMSIS-DAP调试探针。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)）

<a id="using-linkserver"></a>

##### 使用LinkServer

默认运行工具为LinkServer，需要v26.09或更新版本；旧版本不包含MIMXRT2663器件。安装LinkServer调试主机工具并加入搜索路径，再按以下方式构建及烧录：（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

```text
# From the root of the zephyr repository
west build -b mimxrt2660_evk/mimxrt2663/cm85 samples/hello_world
west flash
```

<a id="using-j-link"></a>

##### 使用J-Link

可按MCU-Link J-Link板载调试探针说明，把板载调试电路更新为Segger J-Link固件，或将外部J-Link探针接至SWD排针。（[MCU-Link J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-jlink-onboard-debug-probe)；[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

```text
# From the root of the zephyr repository
west build -b mimxrt2660_evk/mimxrt2663/cm85 samples/hello_world
west flash -r jlink
```

以115200、8N1打开MCU-Link虚拟COM串口终端，复位开发板，示例将输出：

```text
*** Booting Zephyr OS build v4.5.0 ***
Hello World! mimxrt2660_evk/mimxrt2663/cm85
```

<a id="references"></a>

### 参考资料（References）

<a id="id2"></a>

〔1〕 ([1](#id3),[2](#id4)) [https://www.nxp.com/](https://www.nxp.com/)

注意（Note）

原文说明，下方链接指向NXP网站的产品入口，而非具体文档，因为当时i.MX RT2660参考手册及数据手册尚未发布；发布后将更新为实际文档链接。此处保留来源状态。

## 译注

RT2660当前目标从外部闪存XIP，但无Flash API、MCUboot及闪存Settings支持。PLL切换需暂时停用两个xSPI控制器，因此配置代码及临时栈位于ITCM／DTCM。系统定时器使用24 MHz参考源。只有LPUART读取第二个clocks条目；共享根、叶根及模拟／总线根的改配范围分开说明。AHAB空签名块仅按原文评估板生命周期条件描述，未推广至其他生命周期。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://www.nxp.com/)：HTTP Error 404: Not Found。

---

[上一章](P003_MIMXRT1180-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_MIMXRT595-EVK.md)
