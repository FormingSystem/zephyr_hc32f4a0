---
id: learning.zephyr-docs.boards-infineon-innblue.page-1
title: PSOC 4100S Max pioneer kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/infineon/cy8ckit_041s_max/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="cy8ckit_041s_max"></a>

# 第1章\_PSOC 4100S Max先锋套件（Pioneer Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/infineon/cy8ckit_041s_max/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/cy8ckit_041s_max.webp](images/cy8ckit_041s_max.webp)](images/cy8ckit_041s_max.webp)

PSOC 4100S Max先锋套件（Pioneer Kit）

名称（Name）：

`cy8ckit_041s_max`

厂商（Vendor）：

[英飞凌科技（Infineon Technologies）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[cy8c4149azi_s598](https://docs.zephyrproject.org/latest/boards/index.html#soc=cy8c4149azi_s598)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8ckit_041s_max/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[CY8CKIT-041S-MAX](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-041s-max/)是基于PSOC 4100S Max系列的先锋套件，采用PSOC 4100S Max微控制器CY8C4149AZI_S598，Arm Cortex-M0+内核最高运行于48 MHz，适用于电容式触摸感应（Capacitive Touch Sensing）及通用嵌入式应用。

主要特性包括384 KB Flash、32 KB SRAM、CAPSENSE按键、触摸板、滑条与接近感应（Proximity Sensing）、热敏电阻（Thermistor），以及通过USB Micro-B连接的板载[KitProg3](https://github.com/Infineon/KitProg3)编程器／调试器。

<a id="hardware"></a>

## 硬件（Hardware）


- 片上系统（SoC）：PSOC™ 4100S Max (CY8C4149AZI_S598)
- CPU：Arm Cortex-M0+，48 MHz
- 闪存（Flash）：384 KB
- 静态随机存储器（SRAM）：32 KB
- 外设：逐次逼近模数转换器（SAR ADC）、定时器／计数器／PWM（TCPWM）、串行通信模块（SCB，支持UART／SPI／I2C）
- 触摸感应：CAPSENSE按键、触摸板、滑条及接近感应
- 传感器：用于温度测量的热敏电阻
- 调试：板载KitProg3，提供SWD及UART桥接
- 电源：通过Micro-B接口由USB供电，工作电压5 V

PSOC™ 4100S Max及CY8CKIT-041S-MAX更多信息见：


- [PSOC 4 SoC网站](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-4-32-bit-arm-cortex-m0-mcu/)
- [CY8CKIT-041S-MAX开发板网站](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-041s-max/)

<a id="kit-contents"></a>

### 套件内容（Kit Contents）


- PSOC 4100S Max Pioneer Kit开发板
- CAPSENSE扩展板（Expansion Board）
- USB-A转Micro-B线缆
- 6根跳线
- 40针柔性扁平线缆（FFC）
- 快速入门指南（Quick Start Guide）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`cy8ckit_041s_max`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="cy8ckit_041s_max-hw-features"></a>

<a id="cy8ckit_041s_max-cy8ckit_041s_max/cy8c4149azi_s598-hw-features-section"></a>

#### `cy8ckit_041s_max/cy8c4149azi_s598`目标（Target）

<a id="cy8ckit_041s_max-cy8ckit_041s_max/cy8c4149azi_s598-hw-features-panel"></a>

<a id="cy8ckit_041s_max-cy8ckit_041s_max/cy8c4149azi_s598-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、384 KiB Flash。

<a id="cy8ckit_041s_max-cy8ckit_041s_max/cy8c4149azi_s598-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.cm0p.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>英飞凌逐次逼近模数转换器（SAR ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L215">已禁用：1</a>）</td>
<td><a href="../hardware/P882_InfineonSAR模数转换器绑定.md#dtbinding-infineon-sar-adc"><code>infineon,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L175">已禁用：3</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/system_clocks.dtsi?plain=1#L19">已启用：4</a>）</td>
<td><a href="../timer_reference/P112_Infineon固定时钟绑定.md#dtbinding-infineon-fixed-clock"><code>infineon,fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/system_clocks.dtsi?plain=1#L54">已启用：2</a>）</td>
<td><a href="../timer_reference/P113_Infineon固定比例时钟绑定.md#dtbinding-infineon-fixed-factor-clock"><code>infineon,fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设分频器（Peripheral Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/system_clocks.dtsi?plain=1#L75">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/system_clocks.dtsi?plain=1#L120">已禁用：13</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div"><code>infineon,peri-div</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>英飞凌TCPWM计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L262">已禁用：8</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P002_infineon_tcpwm-counter.md#std-dtcompatible-infineon-tcpwm-counter"><code>infineon,tcpwm-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>英飞凌直接存储器访问控制器（DMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L233">已禁用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P001_infineon_dmac.md#std-dtcompatible-infineon-dmac"><code>infineon,dmac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P014_infineon_flash-controller.md#std-dtcompatible-infineon-flash-controller"><code>infineon,flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L55">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L45">已禁用：10</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌共享GPIO集合（Shared GPIO Set）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P002_infineon_shared-gpio.md#std-dtcompatible-infineon-shared-gpio"><code>infineon,shared-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_041s_max/cy8ckit_041s_max.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>英飞凌TCPWM脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L256">已禁用：8</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P019_infineon_tcpwm-pwm.md#std-dtcompatible-infineon-tcpwm-pwm"><code>infineon,tcpwm-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L191">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P017_infineon_spi.md#std-dtcompatible-infineon-spi"><code>infineon,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌TCPWM定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L247">已禁用：8</a>）</td>
<td><a href="../mcu_timer_binding_reference/P009_infineon_tcpwm.md#std-dtcompatible-infineon-tcpwm"><code>infineon,tcpwm</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/psoc4/psoc4100smax/psoc4100smax.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P001_infineon_watchdog.md#std-dtcompatible-infineon-watchdog"><code>infineon,watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="leds"></a>

#### 发光二极管（LEDs）

<table>
<tr>
<th>名称（Name）</th>
<th>GPIO引脚（Pin）</th>
</tr>
<tr>
<td>LED0</td>
<td>P7.3（低电平有效 / active low）</td>
</tr>
</table>

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr默认外设映射（Default Peripheral Mapping）

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>P0.5</td>
<td>SCB2 UART 发送（TX）</td>
<td>控制台发送（Console TX）</td>
</tr>
<tr>
<td>P0.4</td>
<td>SCB2 UART 接收（RX）</td>
<td>控制台接收（Console RX）</td>
</tr>
<tr>
<td>P7.3</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

PSOC 4100S Max默认使用内部主振荡器（IMO / Internal Main Oscillator）作为系统时钟源，时钟路径如下：


- 内部主振荡器（IMO）：48 MHz
- CLK_HF：48 MHz，系统时钟

<a id="serial-port"></a>

### 串口（Serial Port）

PSOC 4100S Max有多个串行通信模块（SCB）接口，可配置为UART、SPI或I2C。Zephyr控制台分配到SCB2（uart2），通过KitProg3 USB-UART桥接器连接主机。

默认通信设置为115200、8N1。

<a id="building"></a>

## 构建（Building）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b cy8ckit_041s_max samples/hello_world
```

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`cy8ckit_041s_max`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

[CY8CKIT-041S-MAX](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-041s-max/)集成板载[KitProg3](https://github.com/Infineon/KitProg3)编程器／调试器，可编程及调试PSOC™ 4100S Max Cortex-M0+内核。

<a id="infineon-openocd-installation"></a>

### 英飞凌OpenOCD安装（Installation）

ModusToolbox编程工具包（Programming Tools）包含[英飞凌OpenOCD](https://github.com/Infineon/openocd/releases/latest)。也可下载适用于当前系统的英飞凌OpenOCD发行版，解压到选定位置，独立安装。（[ModusToolbox编程工具（Programming Tools）](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)）

注意（Note）

Linux需要为KitProg3设置设备访问权限，ModusToolbox编程工具安装过程会自动处理。独立安装OpenOCD时，可手动执行`openocd/udev_rules/install_rules.sh`脚本设置。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

使用USB线缆连接计算机与[CY8CKIT-041S-MAX](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-041s-max/)的KitProg3 USB Micro-B连接器J8，选择minicom、PuTTY等串口终端，并使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

<a id="tab-0-V2luZG93cw=="></a>

<a id="tab-0-TGludXg="></a>

<a id="panel-0-V2luZG93cw=="></a>

**Windows**

一次性设置英飞凌OpenOCD路径：

```text
west config build.cmake-args -- "-DOPENOCD=path/to/infineon/openocd/bin/openocd.exe"
```

构建并烧录应用：

```text
west build -b cy8ckit_041s_max -p always samples/hello_world
west flash
```

<a id="panel-0-TGludXg="></a>

**Linux**

一次性设置英飞凌OpenOCD路径：

```text
west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
```

构建并烧录应用：

```text
west build -b cy8ckit_041s_max -p always samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
*** Booting Zephyr OS build vX.Y.Z ***
Hello World! cy8ckit_041s_max
```

<a id="debugging"></a>

### 调试（Debugging）

```text
# From the root of the zephyr repository
west build -b cy8ckit_041s_max samples/hello_world
west debug
```

GDB控制台启动后，可设置断点（Breakpoints），并对PSOC™ 4100S Max Cortex-M0+内核执行标准GDB调试。

<a id="references"></a>

## 参考资料（References）

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_PSOC_6_AI_Evaluation_Kit.md)
