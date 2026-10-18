---
id: learning.zephyr-docs.boards-atmel.page-2
title: SAM4E Xplained Pro
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4e_xpro/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sam4e_xpro"></a>

# 第2章\_SAM4E Xplained Pro

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4e_xpro/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sam4e_xpro.jpg](images/sam4e_xpro.jpg)](images/sam4e_xpro.jpg)

SAM4E Xplained Pro

名称（Name）：

`sam4e_xpro`

厂商（Vendor）：

[Atmel公司（Atmel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=atmel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sam4e16e](https://docs.zephyrproject.org/latest/boards/index.html#soc=sam4e16e)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4e_xpro/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SAM4E Xplained Pro评估套件是用于评估Atmel SAM4E系列微控制器的开发平台。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAM4E16E ARM Cortex-M4F处理器
- 12 MHz晶体振荡器（Crystal Oscillator）
- 内部32.768 kHz晶体振荡器（类型依原文保留）
- 两片IS61WV5128BLL 4 Mb SRAM
- MT29F2G08ABAEAWP 2 Gb NAND闪存
- SD卡连接器（Connector）
- CAN总线，使用TLE7250GVIOXUMA1 CAN收发器（Transceiver）
- 以太网端口，使用KSZ8081MNXIA物理层（PHY）
- Micro-AB USB设备接口（Device）
- Micro-AB USB调试接口，支持CMSIS-DAP、虚拟COM端口（Virtual COM Port）及数据网关接口（DGI / Data Gateway Interface）
- 一个复位按键和一个用户按键
- 一个黄色用户LED

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sam4e_xpro`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sam4e_xpro-hw-features"></a>

<a id="sam4e_xpro-sam4e_xpro/sam4e16e-hw-features-section"></a>

#### `sam4e_xpro/sam4e16e`目标（Target）

<a id="sam4e_xpro-sam4e_xpro/sam4e16e-hw-features-panel"></a>

<a id="sam4e_xpro-sam4e_xpro/sam4e16e-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、1 MiB Flash。

<a id="sam4e_xpro-sam4e_xpro/sam4e16e-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列模拟前端控制器（AFEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L60">已启用：2</a>）</td>
<td><a href="../hardware/P857_AtmelSAM模拟前端ADC绑定.md#dtbinding-atmel-sam-afec"><code>atmel,sam-afec</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L248">已禁用：3</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAM以太网控制器（Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P019_microchip_sam-ethernet-controller.md#std-dtcompatible-microchip-sam-ethernet-controller"><code>microchip,sam-ethernet-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列千兆媒体访问控制器以太网（GMAC Ethernet）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L173">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P004_atmel_sam-gmac.md#std-dtcompatible-atmel-sam-gmac"><code>atmel,sam-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L182">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P016_atmel_sam-mdio.md#std-dtcompatible-atmel-sam-mdio"><code>atmel,sam-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L217">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM增强型嵌入式闪存控制器（EEFC / Enhanced Embedded Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P006_atmel_sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller"><code>atmel,sam-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L197">已启用：5</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P029_atmel_sam-gpio.md#std-dtcompatible-atmel-sam-gpio"><code>atmel,sam-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Atmel Xplained Pro排针引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L53">已启用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P003_atmel-xplained-pro-header.md#std-dtcompatible-atmel-xplained-pro-header"><code>atmel-xplained-pro-header</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L295">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P001_atmel_sam-rstc.md#std-dtcompatible-atmel-sam-rstc"><code>atmel,sam-rstc</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列I2C双线接口（TWI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L104">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L115">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P008_atmel_sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi"><code>atmel,sam-i2c-twi</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L43">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel静态存储器控制器（SMC / Static Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L302">已禁用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P003_atmel_sam-smc.md#std-dtcompatible-atmel-sam-smc"><code>atmel,sam-smc</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）描述Atmel SAM闪存区域布局（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P009_atmel_sam-flash.md#std-dtcompatible-atmel-sam-flash"><code>atmel,sam-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM电源控制器（SUPC / Supply Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P001_atmel_sam-supc.md#std-dtcompatible-atmel-sam-supc"><code>atmel,sam-supc</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L284">已启用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P007_atmel_sam-pwm.md#std-dtcompatible-atmel-sam-pwm"><code>atmel,sam-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列实时时钟（RTC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L318">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P004_atmel_sam-rtc.md#std-dtcompatible-atmel-sam-rtc"><code>atmel,sam-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>ATMEL（Microchip）SAM高速多媒体卡接口SD主机控制器（HSMCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L311">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P003_atmel_sam-hsmci.md#std-dtcompatible-atmel-sam-hsmci"><code>atmel,sam-hsmci</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>SAM系列通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L136">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L144">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P010_atmel_sam-uart.md#std-dtcompatible-atmel-sam-uart"><code>atmel,sam-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L160">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L152">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L126">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM USB设备端口控制器（UDP / USB Device Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L327">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P003_atmel_sam-udp.md#std-dtcompatible-atmel-sam-udp"><code>atmel,sam-udp</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM0看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L96">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P007_atmel_sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog"><code>atmel,sam-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id3"></a>

<a id="id5"></a>

[SAM4E Xplained Pro用户指南](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf)[注1](#id2)提供开发板连接的详细信息；更多细节可下载[SAM4E Xplained Pro文档](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip)[注2](#id4)查看。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAM4E MCU使用板上的12 MHz内部振荡器，经片上锁相环（PLL）生成120 MHz系统时钟（振荡器类型依原文保留）。

<a id="serial-port"></a>

### 串口（Serial Port）

ATSAM4E16E MCU提供两路UART及两路USART。其中UART0被配置为控制台，通过EDBG USB芯片表现为虚拟COM端口。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sam4e_xpro`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-bossac">bossac</a></td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="id7"></a>

将Zephyr项目烧录到SAM4E MCU需要[OpenOCD工具](http://openocd.org/)[注3](#id6)。全新SAM4E芯片默认启动ROM中的SAM-BA引导加载程序，而非闪存镜像；此行为由通用非易失性存储位1（GPNVM1）决定。烧录流程会将GPNVM1设为1，使芯片改为从闪存启动。

如果安全位GPNVM0已置位，将无法编程闪存或通过调试接口连接芯片。清除此位的唯一方法是执行整片擦除（Chip Erase），这会擦除所有GPNVM位及SAM4E闪存的全部内容：


- 在开发板断电时，短接J304排针上的跳线。
- 给开发板上电，随后即可移除跳线；擦除信号有效至少230 ms后，闪存擦除过程开始。

<a id="flashing"></a>

### 烧录（Flashing）

Zephyr提供两种烧录路径：默认的OpenOCD工具，以及[SAM启动助手（SAM-BA / SAM Boot Assistant）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#atmel-sam-ba-bootloader)。

<a id="using-openocd"></a>

#### 使用OpenOCD


1. 通过USB调试端口将SAM4E Xplained Pro连接到主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4e_xpro samples/hello_world
  west flash
  ```

<a id="using-sam-ba-bootloader"></a>

#### 使用SAM-BA引导加载程序（Bootloader）


1. 短接SAM4E Xplained Pro的ERASE跳线，给开发板上电10秒。
2. 断开ERASE跳线。
3. 通过SoC USB端口将SAM4E Xplained Pro连接到主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4e_xpro samples/hello_world
  ```

  ```text
  $ west flash -r bossac
  ```

<a id="visualizing-the-message"></a>

#### 查看输出消息（Visualizing the Message）


1. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
2. 按下复位按键。

  终端应显示`Hello World! sam4e_xpro`。

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b sam4e_xpro samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip)

<a id="id6"></a>

〔[3](#id7)〕 [http://openocd.org/](http://openocd.org/)

## 译注

原文时钟段落将板上的12 MHz振荡器称为internal oscillator，部分硬件列表也将32.768 kHz晶体称为internal；这里保留原始表述，不自行按器件资料改写。

GPNVM0整片擦除会清除全部GPNVM位和全部闪存内容；该效果、J304跳线、至少230 ms擦除信号及SAM-BA流程中的10秒上电要求均按原文完整保留。

---

[上一章](P001_Atmel_Corporation.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_SAM4L-EK.md)
