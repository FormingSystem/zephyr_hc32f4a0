---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-8
title: FRDM-K64F
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_k64f"></a>

# 第8章\_FRDM-K64F

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_k64f.jpg](images/frdm_k64f.jpg)](images/frdm_k64f.jpg)

FRDM-K64F

名称（Name）：

`frdm_k64f`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mk64f12](https://docs.zephyrproject.org/latest/boards/index.html#soc=mk64f12)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_k64f/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Freedom-K64F是用于Kinetis K64、K63及K24 MCU的超低成本开发平台。


- 外形及引脚布局兼容Arduino R3
- 外设支持快速原型开发，包括组成完整电子罗盘的六轴数字加速度计及磁力计、用于交互的三色LED和两个用户按键、microSD卡槽、板载以太网端口，以及用于蓝牙和2.4 GHz无线扩展模块的排针
- OpenSDAv2是NXP开源硬件嵌入式串行调试适配器，运行开源引导加载程序，提供串行通信、闪存编程及运行控制调试（Run-control Debugging）选项

<a id="hardware"></a>

## 硬件（Hardware）


- MK64FN1M0VLL12 MCU：120 MHz，1 MB闪存，256 KB RAM，低功耗，无晶体USB，以及100引脚薄型四边扁平封装（LQFP）
- 双角色USB接口，使用Micro-B连接器
- RGB发光二极管（LED）
- FXOS8700CQ加速度计及磁力计
- 两个用户按键
- 灵活供电方式：OpenSDAv2 USB、Kinetis K64 USB或外部电源
- 通过兼容Arduino R3的I/O连接器便捷访问MCU输入输出
- 可编程OpenSDAv2调试电路支持CMSIS-DAP接口软件，提供：


  - 大容量存储设备（MSD）闪存编程接口
  - 通过无需专用驱动的USB HID连接提供CMSIS-DAP调试接口，支持运行控制调试并兼容IDE工具
  - 虚拟串口接口（Virtual Serial Port Interface）
  - 开源CMSIS-DAP软件项目
- 以太网（Ethernet）
- SD 主机控制器（SDHC）

K64F SoC及FRDM-K64F更多信息：


- [K64F网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k6x-ethernet/kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120)
- [K64F数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/K64P144M120SF5.pdf)
- [K64F参考手册（Reference Manual）](https://www.nxp.com/docs/en/reference-manual/K64P144M120SF5RM.pdf)
- [FRDM-K64F网站](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/mcu-boards/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F)
- [FRDM-K64F用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=FRDMK64FUG)
- [FRDM-K64F原理图（Schematics）](https://www.nxp.com/webapp/Download?colCode=FRDM-K64F-SCH-E4)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

NXP将FRDM-K64F视为Kinetis K系列功能更完整的开发板（Superset Board），并以此作为Zephyr完整平台支持的重点，优先为其启用新功能，以支持整个Kinetis K系列。

`frdm_k64f`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_k64f-hw-features"></a>

<a id="frdm_k64f-frdm_k64f/mk64f12-hw-features-section"></a>

#### `frdm_k64f/mk64f12`目标（Target）

<a id="frdm_k64f-frdm_k64f/mk64f12-hw-features-panel"></a>

<a id="frdm_k64f-frdm_k64f/mk64f12-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、1 MiB Flash。

<a id="frdm_k64f-frdm_k64f/mk64f12-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Kinetis 16位模数转换器（ADC16）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L436">已启用：2</a>）</td>
<td><a href="../hardware/P850_NXPKinetisADC16绑定.md#dtbinding-nxp-kinetis-adc16"><code>nxp,kinetis-adc16</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L528">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P017_nxp_flexcan.md#std-dtcompatible-nxp-flexcan"><code>nxp,flexcan</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis多用途时钟发生器（MCG）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L93">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P003_nxp_kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg"><code>nxp,kinetis-mcg</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Kinetis系统集成模块（SIM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P006_nxp_kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim"><code>nxp,kinetis-sim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L125">已启用：4</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L562">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L571">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis MCUX数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L462">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L471">已禁用：1</a>）</td>
<td><a href="../hardware/P768_NXPKinetis数模转换器绑定.md#dtbinding-nxp-kinetis-dac"><code>nxp,kinetis-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L542">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L489">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L494">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L504">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Microchip KSZ8081以太网PHY设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L300">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081"><code>microchip,ksz8081</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L511">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis闪存模块E（FTFE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P016_nxp_kinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe"><code>nxp,kinetis-ftfe</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L299">已启用：5</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L75">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RCM获取复位原因标志（Reset Cause Flags）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P012_nxp_rcm-hwinfo.md#std-dtcompatible-nxp-rcm-hwinfo"><code>nxp,rcm-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Kinetis I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L176">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L187">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P002_nxp_kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c"><code>nxp,kinetis-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L59">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L165">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L269">已启用：5</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexTimer模块（FTM）PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L400">已启用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P004_nxp_ftm-pwm.md#std-dtcompatible-nxp-ftm-pwm"><code>nxp,ftm-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis随机数发生器加速器（RNGA / Random Number Generator Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L521">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P019_nxp_kinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga"><code>nxp,kinetis-rnga</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP实时时钟（RTC / Real Time Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P002_nxp_rtc.md#std-dtcompatible-nxp-rtc"><code>nxp,rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L154">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP Kinetis温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L68">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L57">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P004_nxp_kinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature"><code>nxp,kinetis-temperature</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L209">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L219">已禁用：4</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P013_nxp_kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart"><code>nxp,kinetis-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L349">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L378">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexTimer模块（FTM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L409">已禁用：2</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P006_nxp_ftm.md#std-dtcompatible-nxp-ftm"><code>nxp,ftm</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式下的NPX Kinetis USBFSOTG控制器，厂商缩写NPX按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L480">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P007_nxp_kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd"><code>nxp,kinetis-usbd</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Kinetis看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi?plain=1#L393">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P010_nxp_kinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog"><code>nxp,kinetis-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

K64F SoC具有5对引脚复用／GPIO控制器（Pinmux/GPIO Controllers）。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PTB22</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（Red LED）</td>
</tr>
<tr>
<td>PTE26</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（Green LED）</td>
</tr>
<tr>
<td>PTB21</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（Blue LED）</td>
</tr>
<tr>
<td>PTC6</td>
<td>通用输入输出（GPIO）</td>
<td>SW2／FXOS8700中断1（INT1）</td>
</tr>
<tr>
<td>PTC13</td>
<td>通用输入输出（GPIO）</td>
<td>FXOS8700中断2（INT2）</td>
</tr>
<tr>
<td>PTA4</td>
<td>通用输入输出（GPIO）</td>
<td>SW3</td>
</tr>
<tr>
<td>PTB10</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道14</td>
</tr>
<tr>
<td>PTB16</td>
<td>UART0_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTB17</td>
<td>UART0_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td><code>PTB18</code></td>
<td><code>CAN0_TX</code></td>
<td>CAN发送（TX）</td>
</tr>
<tr>
<td><code>PTB19</code></td>
<td><code>CAN0_RX</code></td>
<td>CAN接收（RX）</td>
</tr>
<tr>
<td>PTC8</td>
<td>脉宽调制（PWM）</td>
<td>PWM_3通道4</td>
</tr>
<tr>
<td>PTC9</td>
<td>脉宽调制（PWM）</td>
<td>PWM_3通道5</td>
</tr>
<tr>
<td>PTC16</td>
<td>UART3_RX</td>
<td>UART蓝牙HCI</td>
</tr>
<tr>
<td>PTC17</td>
<td>UART3_TX</td>
<td>UART蓝牙HCI</td>
</tr>
<tr>
<td>PTD0</td>
<td>SPI0_PCS0</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTD1</td>
<td>SPI0_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTD2</td>
<td>SPI0_SOUT</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTD3</td>
<td>SPI0_SIN</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTE24</td>
<td>I2C0_SCL</td>
<td>I2C／FXOS8700</td>
</tr>
<tr>
<td>PTE25</td>
<td>I2C0_SDA</td>
<td>I2C／FXOS8700</td>
</tr>
<tr>
<td>PTA5</td>
<td>MII0_RXER</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA12</td>
<td>MII0_RXD1</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA13</td>
<td>MII0_RXD0</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA14</td>
<td>MII0_RXDV</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA15</td>
<td>MII0_TXEN</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA16</td>
<td>MII0_TXD0</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA17</td>
<td>MII0_TXD1</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTA28</td>
<td>MII0_TXER</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTB0</td>
<td>MII0_MDIO</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTB1</td>
<td>MII0_MDC</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTC16</td>
<td>ENET0_1588_TMR0</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTC17</td>
<td>ENET0_1588_TMR1</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTC18</td>
<td>ENET0_1588_TMR2</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>PTC19</td>
<td>ENET0_1588_TMR3</td>
<td>以太网（Ethernet）</td>
</tr>
</table>

注意（Note）

不要同时启用以太网和UART蓝牙HCI，因为它们在PTC16—17上冲突。

<a id="system-clock"></a>

### 系统时钟（System Clock）

K64F使用板载50 MHz外部振荡器及片上PLL，生成120 MHz系统时钟。

<a id="serial-port"></a>

### 串口（Serial Port）

K64F SoC有6个UART，其中一个用于控制台，另一个用于蓝牙HCI，其余未使用。

<a id="usb"></a>

### 通用串行总线（USB）

K64F USB OTG控制器支持通过K64F USB Micro接口提供设备及主机功能，但原文指出Zephyr当前仅支持设备功能。

<a id="can"></a>

### 控制器局域网（CAN）

FRDM-K64F没有板载CAN收发器。使用CAN总线时，需将外部收发器连接到PTB18（CAN0_TX）及PTB19（CAN0_RX）。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_k64f`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
<th>复位（reset）</th>
</tr>
<tr>
<td>canopen</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试均使用调试探针，默认配置为OpenSDA DAPLink板载调试探针。（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

早期开发板的OpenSDA引导加载程序版本过旧，需要更新。按DAPLink引导加载程序更新（Bootloader Update）页面说明，从CMSIS-DAP引导加载程序升级到DAPLink。（[更新DAPLink引导加载程序（Bootloader）](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/)）

<a id="tab-0-T3BlblNEQSBEQVBMaW5rIE9uYm9hcmQgKFJlY29tbWVuZGVkKQ=="></a>

<a id="tab-0-T3BlblNEQSBKTGluayBPbmJvYXJk"></a>

<a id="panel-0-T3BlblNEQSBEQVBMaW5rIE9uYm9hcmQgKFJlY29tbWVuZGVkKQ=="></a>

**板载OpenSDA DAPLink（推荐）**

安装LinkServer调试主机工具并加入搜索路径。LinkServer兼容板载调试器默认提供的CMSIS-DAP固件。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

此板默认使用LinkServer，west flash及west debug将调用linkserver运行工具。

```text
west flash
```

也可向west传递-r pyocd使用pyOCD烧录及调试。完成入门指南的“获取Zephyr并安装Python依赖”步骤时已安装pyOCD。NXP支持的运行工具为LinkServer及J-Link；pyOCD是另一种可能选择，但NXP不对其测试或提供支持。（[获取Zephyr并安装Python依赖项](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#gs-python-deps)）

<a id="panel-0-T3BlblNEQSBKTGluayBPbmJvYXJk"></a>

**板载OpenSDA J-Link**

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

应写入的J-Link固件版本取决于DAPLink引导加载程序版本，详情见OpenSDA串行调试适配器页面。在“Choose your board to start”下拉菜单选择FRDM-K64F，再查看“To update your board with OpenSDA applications”章节。SEGGER也提供此板专用OpenSDA J-Link固件，但它与DAPLink引导加载程序不兼容。下载合适固件后，按OpenSDA J-Link板载调试探针说明写入开发板。（[OpenSDA串行及调试适配器（Serial and Debug Adapter）](https://www.nxp.com/design/microcontrollers-developer-resources/ides-for-kinetis-mcus/opensda-serial-and-debug-adapter:OPENSDA#FRDM-K64F)；[OpenSDA J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-jlink-onboard-debug-probe)）

调用west build时添加-DBOARD_FLASH_RUNNER=jlink及-DBOARD_DEBUG_RUNNER=jlink，将默认运行工具改为J-Link：

```text
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选择哪种调试探针，串行控制台都使用OpenSDA微控制器作为USB转串口适配器。

用USB线缆将PC连接J26。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world
west flash
```

打开串口终端，按SW1复位开发板，应显示以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

若烧录或调试时pyOCD抛出未捕获的DAPAccessIntf.TransferFaultError()异常，可能是损坏的应用锁定了K64F闪存。可按以下pyOCD命令序列解锁：

```text
$ pyocd cmd
0001915:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
Connected to K64F [Halted]: 0240000026334e450028400d5e0e000e4eb1000097969900
>>> unlock
0016178:WARNING:target_kinetis:K64F secure state: unlocked successfully
>>> reinit
0034584:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
>>> load build/zephyr/zephyr.bin
[====================] 100%
>>> reset
Resetting target
>>> quit
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

Ethernet与Bluetooth HCI共用PTC16—PTC17，不能同时占用。CAN需要外接收发器。J-Link固件选择取决于OpenSDA引导加载程序版本；解锁恢复命令仅按原文收录，未实际执行。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [opensda-serial-and-debug-adapter:OPENSDA](https://www.nxp.com/design/microcontrollers-developer-resources/ides-for-kinetis-mcus/opensda-serial-and-debug-adapter:OPENSDA#FRDM-K64F)：HTTP Error 404: Not Found。
- [K64P144M120SF5.pdf](https://www.nxp.com/docs/en/data-sheet/K64P144M120SF5.pdf)：HTTP Error 404: Not Found。
- [K64P144M120SF5RM.pdf](https://www.nxp.com/docs/en/reference-manual/K64P144M120SF5RM.pdf)：HTTP Error 404: Not Found。
- [kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k6x-ethernet/kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120)：HTTP Error 404: Not Found。
- [freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/mcu-boards/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F)：HTTP Error 404: Not Found。
- [Download?colCode=FRDM-K64F-SCH-E4](https://www.nxp.com/webapp/Download?colCode=FRDM-K64F-SCH-E4)：HTTP Error 404: Not Found。
- [Download?colCode=FRDMK64FUG](https://www.nxp.com/webapp/Download?colCode=FRDMK64FUG)：HTTP Error 404: Not Found。

---

[上一章](P007_FRDM-K32L2B3.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_FRDM-K82F.md)
