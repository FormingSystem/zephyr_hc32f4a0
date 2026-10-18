---
id: learning.zephyr-docs.boards-ublox-misc.page-10
title: EVK-IRIS-W106-RW612
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/u-blox/ubx_evk_iris_w1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ubx_evk_iris_w1"></a>

# 第10章\_EVK-IRIS-W106-RW612

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/u-blox/ubx_evk_iris_w1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id3"></a>

[![官方原图：../../../../_images/ubx_evk_iris_w1.webp](images/ubx_evk_iris_w1.webp)](images/ubx_evk_iris_w1.webp)

EVK-IRIS-W106-RW612

名称（Name）：

`ubx_evk_iris_w1`

厂商（Vendor）：

[u-blox](https://docs.zephyrproject.org/latest/boards/index.html#vendor=u-blox)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rw612](https://docs.zephyrproject.org/latest/boards/index.html#soc=rw612)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/u-blox/ubx_evk_iris_w1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EVK-IRIS-W10x评估套件可独立使用IRIS-W10系列模块。本指南介绍EVK-IRIS-W10开发板的硬件功能及开始开发的设置步骤。

IRIS-W10系列模块支持的所有引脚和接口均可从评估板方便地访问。USB连接提供供电、编程COM端口、调试及USB外设接口；另有以太网RJ45及SDIO排针。板上配备复位键、启动键和两个用户可配置按键，并使用电流检测电阻精确测量模块电流。

GPIO通过排针引出，并有四个mikroBUS标准插槽可安装Click扩展板。Click板可直接插入空闲插槽，以标准化小型附加板扩展硬件，涵盖传感器、收发器、显示器、编码器、电机驱动器及连接端口等。更多信息见MIKROE网站。

<a id="hardware"></a>

## 硬件（Hardware）


- 260 MHz Arm Cortex-M33及Wi-Fi 6、BLE 5.3、802.15.4三套无线电核
- 1.2 MB片上SRAM
- EVK-IRIS-W101评估板搭载IRIS-W101模块，提供WLAN双频PCB天线、100 mm同轴线及U.FL连接器。
- EVK-IRIS-W106评估板搭载IRIS-W106模块，集成双频PCB走线天线，不随附外部天线。

<a id="flash-memory-configuration"></a>

### 闪存配置（Flash Memory Configuration）

IRIS-W1支持多种闪存厂商及容量，通过板卡修订版本（Board Revision）选择：

<table>
<tr>
<th>修订版本（Revision）</th>
<th>厂商（Vendor）</th>
<th>大小（Size）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>@fidelix</code></td>
<td>Fidelix FM25Q64A</td>
<td>8MB</td>
<td>自2023年第46周起生产的模块，默认版本</td>
</tr>
<tr>
<td><code>@fidelix_16mb</code></td>
<td>Fidelix FM25Q128A</td>
<td>16MB</td>
<td>Fidelix 16 MB变体</td>
</tr>
<tr>
<td><code>@macronix</code></td>
<td>Macronix MX25L6433F</td>
<td>8MB</td>
<td>截至2023年第45周生产的模块</td>
</tr>
<tr>
<td><code>@macronix_16mb</code></td>
<td>Macronix MX25L12845G</td>
<td>16MB</td>
<td>Macronix 16 MB变体</td>
</tr>
</table>

指定闪存修订版本构建：

```text
west build -b ubx_evk_iris_w1@fidelix/rw612 samples/hello_world
west build -b ubx_evk_iris_w1@fidelix_16mb/rw612 samples/hello_world
west build -b ubx_evk_iris_w1@macronix/rw612 samples/hello_world
west build -b ubx_evk_iris_w1@macronix_16mb/rw612 samples/hello_world
```

不指定版本时，默认使用fidelix（8 MB）。

每个版本都有专用DTS覆盖文件，定义该闪存变体的节点与分区布局。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ubx_evk_iris_w1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ubx_evk_iris_w1-hw-features"></a>

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612-hw-features-section"></a>

#### `ubx_evk_iris_w1@fidelix/rw612`目标（Target）

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612-hw-features-panel"></a>

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612-hw-features-memory"></a>

此目标可用存储：960 KiB RAM、8 MiB闪存。

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP GAU通用模数转换器（GPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L664">已禁用：2</a>）</td>
<td><a href="../hardware/P849_NXPGAU模数转换器绑定.md#dtbinding-nxp-gau-adc"><code>nxp,gau-adc</code></a></td>
</tr>
<tr>
<td rowspan="3">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L351">已禁用：2</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RW SoC控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L401">已启用：2</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P018_nxp_rw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl"><code>nxp,rw-soc-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NBU中断信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L707">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P017_nxp_nbu.md#std-dtcompatible-nxp-nbu"><code>nxp,nbu</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP数字麦克风接口（DMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L624">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P013_nxp_dmic.md#std-dtcompatible-nxp-dmic"><code>nxp,dmic</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗蓝牙主机控制器接口（BLE HCI）信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L713">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P009_nxp_hci-ble.md#std-dtcompatible-nxp-hci-ble"><code>nxp,hci-ble</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L155">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L94">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP BASIC频率测量（FREQME / fmeas）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L183">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P003_nxp_fmeas.md#std-dtcompatible-nxp-fmeas"><code>nxp,fmeas</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP模拟比较器（ACOMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L691">已禁用：1</a>）</td>
<td><a href="../hardware/P742_NXP模拟比较器绑定.md#dtbinding-nxp-acomp"><code>nxp,acomp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>使用NXP LPC RTC高分辨率计数器（High Resolution Counter）的驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L481">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P010_nxp_lpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres"><code>nxp,lpc-rtc-highres</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L487">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L500">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L550">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L562">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L568">已禁用：7</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc"><code>nxp,lpc-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP GAU数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L682">已禁用：1</a>）</td>
<td><a href="../hardware/P766_NXPGAU数模转换器绑定.md#dtbinding-nxp-gau-dac"><code>nxp,gau-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L442">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P003_nxp_lpc-dma.md#std-dtcompatible-nxp-lpc-dma"><code>nxp,lpc-dma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP通用直接存储器访问（GDMA / General DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L452">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P002_nxp_gdma.md#std-dtcompatible-nxp-gdma"><code>nxp,gdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L757">已禁用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L725">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L730">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L740">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L748">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L277">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L283">已启用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">IEEE 802.15.4 HDLC 无线协处理器接口（RCP Interface）</td>
<td>片上（On-Chip）</td>
<td>NXP高级数据链路控制（HDLC）无线电协处理器（RCP）接口节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L718">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P003_nxp_hdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if"><code>nxp,hdlc-rcp-if</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>LPC I2S音频总线节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L321">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P012_nxp_lpc-i2s.md#std-dtcompatible-nxp-lpc-i2s"><code>nxp,lpc-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L413">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P004_nxp_pint.md#std-dtcompatible-nxp-pint"><code>nxp,pint</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP LCD接口控制器（LCDIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L462">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P003_nxp_lcdic.md#std-dtcompatible-nxp-lcdic"><code>nxp,lcdic</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_fidelix.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L175">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCI输入输出复用（IO MUX）引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P011_nxp_mci-io-mux.md#std-dtcompatible-nxp-mci-io-mux"><code>nxp,mci-io-mux</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP RW电源管理单元（PMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P016_nxp_rw-pmu.md#std-dtcompatible-nxp-rw-pmu"><code>nxp,rw-pmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>部分NXP SoC具有专门用于产生唤醒中断的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L246">已禁用：2</a>）</td>
<td><a href="../power_control_binding_reference/P013_nxp_aon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin"><code>nxp,aon-wakeup-pin</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通过PDCFG寄存器实现NXP电源管理的属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L53">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L65">已禁用：1</a>）</td>
<td><a href="../power_control_binding_reference/P015_nxp_pdcfg-power.md#std-dtcompatible-nxp-pdcfg-power"><code>nxp,pdcfg-power</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L87">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L539">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L230">已启用：2</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L259">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L475">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P013_nxp_lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc"><code>nxp,lpc-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L366">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L336">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L111">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L699">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L312">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L267">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td rowspan="1">无线局域网（Wi-Fi）</td>
<td>片上（On-Chip）</td>
<td>NXP Wi-Fi模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L426">已启用：1</a>）</td>
<td><a href="../wifi_nordic_nxp_simulation_binding_reference/P010_nxp_wifi.md#std-dtcompatible-nxp-wifi"><code>nxp,wifi</code></a></td>
</tr>
</table>

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612/ethernet-hw-features-section"></a>

#### `ubx_evk_iris_w1@fidelix/rw612/ethernet`目标（Target）

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612/ethernet-hw-features-panel"></a>

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612/ethernet-hw-features-memory"></a>

此目标可用存储：960 KiB RAM、8 MiB闪存。

<a id="ubx_evk_iris_w1-ubx_evk_iris_w1@fidelix/rw612/ethernet-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP GAU通用模数转换器（GPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L664">已禁用：2</a>）</td>
<td><a href="../hardware/P849_NXPGAU模数转换器绑定.md#dtbinding-nxp-gau-adc"><code>nxp,gau-adc</code></a></td>
</tr>
<tr>
<td rowspan="3">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L351">已禁用：2</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RW SoC控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L401">已启用：2</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P018_nxp_rw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl"><code>nxp,rw-soc-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NBU中断信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L707">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P017_nxp_nbu.md#std-dtcompatible-nxp-nbu"><code>nxp,nbu</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP数字麦克风接口（DMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L624">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P013_nxp_dmic.md#std-dtcompatible-nxp-dmic"><code>nxp,dmic</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗蓝牙主机控制器接口（BLE HCI）信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L713">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P009_nxp_hci-ble.md#std-dtcompatible-nxp-hci-ble"><code>nxp,hci-ble</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L155">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L94">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP BASIC频率测量（FREQME / fmeas）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L183">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P003_nxp_fmeas.md#std-dtcompatible-nxp-fmeas"><code>nxp,fmeas</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP模拟比较器（ACOMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L691">已禁用：1</a>）</td>
<td><a href="../hardware/P742_NXP模拟比较器绑定.md#dtbinding-nxp-acomp"><code>nxp,acomp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>使用NXP LPC RTC高分辨率计数器（High Resolution Counter）的驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L481">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P010_nxp_lpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres"><code>nxp,lpc-rtc-highres</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L487">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L500">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L550">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L562">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L568">已禁用：7</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc"><code>nxp,lpc-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP GAU数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L682">已禁用：1</a>）</td>
<td><a href="../hardware/P766_NXPGAU数模转换器绑定.md#dtbinding-nxp-gau-dac"><code>nxp,gau-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L442">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P003_nxp_lpc-dma.md#std-dtcompatible-nxp-lpc-dma"><code>nxp,lpc-dma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP通用直接存储器访问（GDMA / General DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L452">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P002_nxp_gdma.md#std-dtcompatible-nxp-gdma"><code>nxp,gdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L757">已禁用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L725">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L730">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L740">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Microchip KSZ8081以太网PHY设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_rw612_ethernet.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081"><code>microchip,ksz8081</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L748">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L277">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L283">已启用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">IEEE 802.15.4 HDLC 无线协处理器接口（RCP Interface）</td>
<td>片上（On-Chip）</td>
<td>NXP高级数据链路控制（HDLC）无线电协处理器（RCP）接口节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L718">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P003_nxp_hdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if"><code>nxp,hdlc-rcp-if</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>LPC I2S音频总线节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L321">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P012_nxp_lpc-i2s.md#std-dtcompatible-nxp-lpc-i2s"><code>nxp,lpc-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L413">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P004_nxp_pint.md#std-dtcompatible-nxp-pint"><code>nxp,pint</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP LCD接口控制器（LCDIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L462">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P003_nxp_lcdic.md#std-dtcompatible-nxp-lcdic"><code>nxp,lcdic</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_fidelix.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L175">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCI输入输出复用（IO MUX）引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P011_nxp_mci-io-mux.md#std-dtcompatible-nxp-mci-io-mux"><code>nxp,mci-io-mux</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP RW电源管理单元（PMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P016_nxp_rw-pmu.md#std-dtcompatible-nxp-rw-pmu"><code>nxp,rw-pmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>部分NXP SoC具有专门用于产生唤醒中断的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L246">已禁用：2</a>）</td>
<td><a href="../power_control_binding_reference/P013_nxp_aon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin"><code>nxp,aon-wakeup-pin</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通过PDCFG寄存器实现NXP电源管理的属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L53">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L65">已禁用：1</a>）</td>
<td><a href="../power_control_binding_reference/P015_nxp_pdcfg-power.md#std-dtcompatible-nxp-pdcfg-power"><code>nxp,pdcfg-power</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L87">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L539">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L230">已启用：2</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L259">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L475">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P013_nxp_lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc"><code>nxp,lpc-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L366">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L336">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L111">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L699">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L312">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L267">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td rowspan="1">无线局域网（Wi-Fi）</td>
<td>片上（On-Chip）</td>
<td>NXP Wi-Fi模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/rw/nxp_rw6xx_common.dtsi?plain=1#L426">已启用：1</a>）</td>
<td><a href="../wifi_nordic_nxp_simulation_binding_reference/P010_nxp_wifi.md#std-dtcompatible-nxp-wifi"><code>nxp,wifi</code></a></td>
</tr>
</table>

支持UART（默认FC3）、GPIO（I²C、SPI）及板载RGB LED等基本功能。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`ubx_evk_iris_w1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
</table>

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

调试探针用于烧录和调试，开发板默认配置为使用J-Link固件。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线将PC连接到USB3，选择minicom、PuTTY等串口终端，配置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

以下以hello_world应用为例。

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
**** Booting Zephyr OS build v4.1.0-2794-g6463c68bc394 ****
     Hello World ! ubx_evk_iris_w1/rw612
```

<a id="wireless-connectivity-support"></a>

## 无线连接支持（Wireless Connectivity Support）

<a id="fetch-binary-blobs"></a>

### 获取二进制文件（Fetch Binary Blobs）

为支持Bluetooth或Wi-Fi，ubx_evk_iris_w1需要获取二进制固件文件（Binary Blobs），运行以下命令：

```text
west blobs fetch hal_nxp
```

<a id="bluetooth"></a>

### 蓝牙（Bluetooth）

BLE功能依赖二进制固件文件，请先完成“获取二进制固件文件”一节。

所需的<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_ble_a2.bin将直接与应用镜像链接，形成单一整体镜像（Monolithic Image）。

<a id="wi-fi"></a>

### 无线局域网（Wi-Fi）

Wi-Fi功能也依赖二进制固件文件，请先完成“获取二进制固件文件”一节。

所需的<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_wifi_a2.bin将直接与应用镜像链接，形成单一整体镜像。

<a id="board-variants"></a>

## 开发板变体（Board Variants）

<a id="ethernet"></a>

### 以太网（Ethernet）

EVK-IRIS-W1带以太网RJ45连接器，配合ethernet板卡变体使用。要启用以太网，以ubx_evk_iris_w1//ethernet为目标构建。

```text
west build -b ubx_evk_iris_w1@fidelix/rw612/ethernet
west build -b ubx_evk_iris_w1@fidelix_16mb/rw612/ethernet
west build -b ubx_evk_iris_w1@macronix/rw612/ethernet
west build -b ubx_evk_iris_w1@macronix_16mb/rw612/ethernet
```

注意（Note）

以太网PHY与外部振荡器存在引脚冲突，需要修改板卡硬件；修改方法见以下文档：


- [EVK-IRIS-W1用户指南](https://www.u-blox.com/docs/UBX-23007837)
- [IRIS-W10系统集成手册（SIM）](https://content.u-blox.com/sites/default/files/documents/IRIS-W10_SIM_UBX-23003263.pdf)

<a id="resources"></a>

## 资源（Resources）


- [EVK-IRIS-W1网站](https://www.u-blox.com/en/product/evk-iris-w1)
- [EVK-IRIS-W1 GitHub仓库](https://github.com/u-blox/u-blox-sho-OpenCPU/tree/master/MCUXpresso/IRIS-W1)
- [EVK-IRIS-W1用户指南](https://www.u-blox.com/docs/UBX-23007837)
- [IRIS-W10系统集成手册（SIM）](https://content.u-blox.com/sites/default/files/documents/IRIS-W10_SIM_UBX-23003263.pdf)

## 译注

IRIS-W1依模块制造时间及容量选择Fidelix／Macronix修订版本，默认Fidelix 8 MB。BLE和Wi-Fi分别依赖二进制固件；以太网变体还需要处理PHY与外部振荡器的硬件引脚冲突。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [UBX-23007837](https://www.u-blox.com/docs/UBX-23007837)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [evk-iris-w1](https://www.u-blox.com/en/product/evk-iris-w1)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。

---

[上一章](P009_EVK-BMD-34_48_BMD-380-EVAL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_EVK-ANNA-B11x.md)
