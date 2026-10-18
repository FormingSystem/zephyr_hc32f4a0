---
id: learning.zephyr-docs.boards-infineon-innblue.page-3
title: PSOC 62S4 Pioneer Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/infineon/cy8ckit_062s4/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="cy8ckit_062s4"></a>

# 第3章\_PSOC 62S4先锋套件（Pioneer Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/infineon/cy8ckit_062s4/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/cy8ckit_062s4.webp](images/cy8ckit_062s4.webp)](images/cy8ckit_062s4.webp)

PSOC 62S4先锋套件（Pioneer Kit）

名称（Name）：

`cy8ckit_062s4`

厂商（Vendor）：

[英飞凌科技（Infineon Technologies）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[cy8c6244lqi_s4d92](https://docs.zephyrproject.org/latest/boards/index.html#soc=cy8c6244lqi_s4d92)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8ckit_062s4/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[CY8CKIT-062S4](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/)是PSOC 62S4先锋套件，采用CY8C6244LQI-S4D92双核微控制器，包含150 MHz Arm Cortex-M4及100 MHz Cortex-M0+，面向电池供电的模拟量感测应用。

主要特性包括256 KB Flash、128 KB SRAM、两个12位2 Msps SAR ADC、两个运算放大器（Opamps）、两个比较器（Comparators）、CAPSENSE触摸感应、环境光传感器、热敏电阻和串行存储器。

开发板支持Arduino Uno R3扩展排针，并集成通过USB Micro-B连接的[KitProg3](https://github.com/Infineon/KitProg3)编程器／调试器。

<a id="hardware"></a>

## 硬件（Hardware）


- 片上系统（SoC）：PSOC™ 62S4 (CY8C6244LQI-S4D92)
- CPU：双核，150 MHz Arm Cortex-M4及100 MHz Cortex-M0+
- 闪存（Flash）：256 KB
- 静态随机存储器（SRAM）：128 KB
- 模拟外设：两个12位2 Msps SAR ADC、两个运算放大器、两个比较器
- 触摸：CAPSENSE，5段滑条及2个按键
- 传感器：环境光传感器（Ambient Light Sensor）、热敏电阻
- 存储：512 Mbit Quad-SPI NOR闪存、串行存储器
- 调试：板载KitProg3，提供SWD及UART桥接
- 电源：USB供电，工作电压1.8–3.3 V
- 连接器：USB Micro-B，用于编程和供电
- 扩展：兼容Arduino Uno R3的排针

PSOC™ 62S4及CY8CKIT-062S4更多信息见：


- [PSOC 6 SoC网站](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu/)
- [CY8CKIT-062S4开发板网站](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/)

<a id="kit-contents"></a>

### 套件内容（Kit Contents）


- PSOC 62S4 Pioneer Kit开发板
- USB Type-A转Micro-B线缆
- 6根跳线
- 快速入门指南（Quick Start Guide）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`cy8ckit_062s4`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="cy8ckit_062s4-hw-features"></a>

<a id="cy8ckit_062s4-cy8ckit_062s4/cy8c6244lqi_s4d92-hw-features-section"></a>

#### `cy8ckit_062s4/cy8c6244lqi_s4d92`目标（Target）

<a id="cy8ckit_062s4-cy8ckit_062s4/cy8c6244lqi_s4d92-hw-features-panel"></a>

<a id="cy8ckit_062s4-cy8ckit_062s4/cy8c6244lqi_s4d92-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、256 KiB Flash。

<a id="cy8ckit_062s4-cy8ckit_062s4/cy8c6244lqi_s4d92-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>英飞凌Cat1 ADC，每个Cat1 ADC组对应一个Zephyr设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L199">已禁用：2</a>）</td>
<td><a href="../hardware/P877_Infineon模数转换器绑定.md#dtbinding-infineon-adc"><code>infineon,adc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L223">已禁用：4</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P014_infineon_flash-controller.md#std-dtcompatible-infineon-flash-controller"><code>infineon,flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L82">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L63">已禁用：11</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s4/cy8ckit_062s4.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s4/cy8ckit_062s4.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 SDHC／SDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L273">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P008_infineon_sdhc-sdio.md#std-dtcompatible-infineon-sdhc-sdio"><code>infineon,sdhc-sdio</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L233">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L213">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
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
<td>P2.5（高电平有效 / active high）</td>
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
<td>P3.1</td>
<td>SCB2 UART 发送（TX）</td>
<td>控制台发送（Console TX）</td>
</tr>
<tr>
<td>P3.0</td>
<td>SCB2 UART 接收（RX）</td>
<td>控制台接收（Console RX）</td>
</tr>
<tr>
<td>P2.5</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

PSOC 62S4默认使用内部主振荡器（IMO）作为系统时钟源，时钟路径如下：


- 内部主振荡器（IMO）：8 MHz
- 锁频环（FLL）：IMO → 100 MHz
- 锁相环（PLL）：IMO → 48 MHz
- CLK_HF0：100 MHz，系统时钟

<a id="serial-port"></a>

### 串口（Serial Port）

PSOC 62S4有多个串行通信模块（SCB）接口，可配置为UART、SPI或I2C。Zephyr控制台分配到SCB2（uart2），通过KitProg3 USB-UART桥接器连接主机。

默认通信设置为115200、8N1。

<a id="prerequisites"></a>

## 前置条件（Prerequisites）

<a id="fetch-binary-blobs"></a>

### 获取二进制文件（Fetch Binary Blobs）

`cy8ckit_062s4`需要二进制固件，即CM0+预构建睡眠镜像。运行以下命令获取：

```text
west blobs fetch hal_infineon
```

<a id="building"></a>

## 构建（Building）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b cy8ckit_062s4 samples/hello_world
```

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`cy8ckit_062s4`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

[CY8CKIT-062S4](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/)集成[KitProg3](https://github.com/Infineon/KitProg3)编程器／调试器，可编程及调试PSOC 62S4 Cortex-M4内核，默认运行工具（Runner）为pyOCD。

<a id="pyocd-installation"></a>

### 安装pyOCD

可通过pip安装pyOCD：

```text
pip install pyocd
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

使用USB线缆连接计算机与[CY8CKIT-062S4](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/)的KitProg3 USB Micro-B连接器J10，选择minicom、PuTTY等串口终端，并使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

使用pyOCD构建并烧录应用：

```text
west build -b cy8ckit_062s4 -p always samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
*** Booting Zephyr OS build vX.Y.Z ***
Hello World! cy8ckit_062s4
```

<a id="debugging"></a>

### 调试（Debugging）

```text
# From the root of the zephyr repository
west build -b cy8ckit_062s4 samples/hello_world
west debug
```

GDB控制台启动后，可设置断点（Breakpoints），并对PSOC™ 62S4 Cortex-M4内核执行标准GDB调试。

<a id="references"></a>

## 参考资料（References）

---

[上一章](P002_PSOC_6_AI_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_PSOC_4000T.md)
