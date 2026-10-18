---
id: learning.zephyr-docs.boards-microchip.page-19
title: PIC32CM PL10 Curiosity Nano
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_pl10_cnano/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pic32cm_pl10_cnano"></a>

# 第19章\_PIC32CM PL10 Curiosity Nano

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_pl10_cnano/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/pic32cm_pl10_cnano.webp](images/pic32cm_pl10_cnano.webp)](images/pic32cm_pl10_cnano.webp)

PIC32CM PL10 Curiosity Nano

名称（Name）：

`pic32cm_pl10_cnano`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[pic32cm6408pl10048](https://docs.zephyrproject.org/latest/boards/index.html#soc=pic32cm6408pl10048)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/pic32c/pic32cm_pl10_cnano/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PIC32CM PL10 Curiosity Nano评估套件EV10P22A用于评估PIC32CM PL10系列微控制器，板载PIC32CM6408PL10048微控制器。

<a id="hardware"></a>

## 硬件（Hardware）


- PIC32CM6408PL10048 MCU
- Arm Cortex-M0+内核，在1.8—5.5 V供电范围内最高运行频率为24 MHz
- 64 KB支持在系统自编程（In-System Self-Programmable）的闪存及8 KB SRAM
- 工作电压1.8—5.5 V
- 提供48引脚TQFP及48引脚VQFN WF封装
- 低功耗（Low Power）


  - 空闲（Idle）及待机（Standby）睡眠模式
  - 支持睡眠漫游（Sleep Walking）的外设
- 多电压I/O（MVIO / Multi-Voltage I/O）
- 外设触摸控制器（PTC），具有25个自电容（Self-Capacitance）通道
- 一个12位、800 ksps模数转换器（ADC）
- 两个带窗口比较功能（Window Compare）的模拟比较器（AC）
- 四个16位定时器／计数器（Timer/Counters）：


  - 三个16位基本定时器／计数器TC0—2
  - 一个带4路PWM的16位控制用定时器／计数器TCC0
- 32位实时时钟计数器（RTC），支持时钟／日历功能
- 两个串行通信接口（SERCOM），可配置为：


  - 支持全双工及单线半双工配置的USART
  - ISO7816 UART
  - 最高1 MHz的I2C，使用SERCOM0
  - 串行外设接口（SPI）
  - LIN主机／客户端（Host/Client）
  - RS-485
- 双通道直接存储器访问控制器（DMAC），带CRC发生器
- 四通道事件系统（EVSYS / Event System）
- 可配置自定义逻辑（CCL），带4个查找表（LUT）
- 编程及调试接口禁用（PDID）功能
- 看门狗定时器（WDT）
- 带故障检测的外部晶体振荡器
- 集成温度传感器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pic32cm_pl10_cnano`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pic32cm_pl10_cnano-hw-features"></a>

<a id="pic32cm_pl10_cnano-pic32cm_pl10_cnano/pic32cm6408pl10048-hw-features-section"></a>

#### `pic32cm_pl10_cnano/pic32cm6408pl10048`目标（Target）

<a id="pic32cm_pl10_cnano-pic32cm_pl10_cnano/pic32cm6408pl10048-hw-features-panel"></a>

<a id="pic32cm_pl10_cnano-pic32cm_pl10_cnano/pic32cm6408pl10048-hw-features-memory"></a>

该开发板目标的片上存储容量：8 KiB RAM、64 KiB Flash。

<a id="pic32cm_pl10_cnano-pic32cm_pl10_cnano/pic32cm6408pl10048-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L110">已禁用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P013_microchip_sercom-g1.md#std-dtcompatible-microchip-sercom-g1"><code>microchip,sercom-g1</code></a></td>
</tr>
<tr>
<td rowspan="9">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PIC32CM_PL SoC系列时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P018_microchip_pic32cm-pl-clock.md#std-dtcompatible-microchip-pic32cm-pl-clock"><code>microchip,pic32cm-pl-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL内部高频振荡器（OSCHF）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P024_microchip_pic32cm-pl-oschf.md#std-dtcompatible-microchip-pic32cm-pl-oschf"><code>microchip,pic32cm-pl-oschf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL RTC时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P025_microchip_pic32cm-pl-rtc.md#std-dtcompatible-microchip-pic32cm-pl-rtc"><code>microchip,pic32cm-pl-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL外部晶体振荡器（XOSC32K）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_sam_binding_reference/P001_microchip_pic32cm-pl-xosc32k.md#std-dtcompatible-microchip-pic32cm-pl-xosc32k"><code>microchip,pic32cm-pl-xosc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL内部振荡器（OSC32K）控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P023_microchip_pic32cm-pl-osc32k.md#std-dtcompatible-microchip-pic32cm-pl-osc32k"><code>microchip,pic32cm-pl-osc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL通用时钟发生器（Generic Clock Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P019_microchip_pic32cm-pl-gclkgen.md#std-dtcompatible-microchip-pic32cm-pl-gclkgen"><code>microchip,pic32cm-pl-gclkgen</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL通用时钟外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P020_microchip_pic32cm-pl-gclkperiph.md#std-dtcompatible-microchip-pic32cm-pl-gclkperiph"><code>microchip,pic32cm-pl-gclkperiph</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL CPU主时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P021_microchip_pic32cm-pl-mclkcpu.md#std-dtcompatible-microchip-pic32cm-pl-mclkcpu"><code>microchip,pic32cm-pl-mclkcpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_PL MCLK外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P022_microchip_pic32cm-pl-mclkperiph.md#std-dtcompatible-microchip-pic32cm-pl-mclkperiph"><code>microchip,pic32cm-pl-mclkperiph</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Microchip G2 DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P014_microchip_dmac-g2-dma.md#std-dtcompatible-microchip-dmac-g2-dma"><code>microchip,dmac-g2-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip Port G1 GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl_048.dtsi?plain=1#L10">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L89">已禁用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio"><code>microchip,port-g1-gpio</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_pl10_cnano/pic32cm_pl10_cnano.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PORT引脚控制（Pinctrl）容器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P006_microchip_port-g1-pinctrl.md#std-dtcompatible-microchip-port-g1-pinctrl"><code>microchip,port-g1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P019_microchip_sercom-g1-uart.md#std-dtcompatible-microchip-sercom-g1-uart"><code>microchip,sercom-g1-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_pl/common/pic32cm_pl.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

PIC32CM PL10 Curiosity Nano用户指南提供开发板连接详情。（[PIC32CM PL10 Curiosity Nano用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/UserGuides/PIC32CM-PL10-UserGuide-DS50004003.pdf)）

<a id="programming-debugging"></a>

## 编程与调试（Programming & Debugging）

`pic32cm_pl10_cnano`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>mplab_ipe</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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

<a id="flash-using-mplab-ipe"></a>

### 使用MPLAB IPE烧录（Flash）

使用MPLAB IPE烧录的方法见“使用Microchip MPLAB IPE烧录”。（[使用Microchip MPLAB IPE烧录（Flashing）](P001_Flashing_with_Microchip_MPLAB_IPE.md#microchip-mplab-ipe-flashing)）

<a id="setting-up-the-debug-interface"></a>

### 设置调试接口（Debug Interface）

<a id="pyocd-setup"></a>

### PyOCD设置（Setup）


1. 安装器件包（Device Pack）


  - 使用以下命令添加PIC32CM系列器件支持：

  ```text
  pyocd pack install pic32cm
  ```
2. 验证器件支持（Device Support）


  - 确认能够识别目标：

  ```text
  pyocd list --targets
  ```


  - 应看到类似以下条目：

  ```text
  pic32cm6408pl10048        Microchip                PIC32CM6408PL10048           PIC32CM-PL   pack
  ```
3. 连接开发板（Connect the Board）


  - 将开发板DEBUG USB端口连接主机。
  - 该连接为开发板供电，并提供对板载嵌入式调试器（EDBG）的访问，使PyOCD能够对目标微控制器编程及调试。

<a id="building-and-flashing-the-application"></a>

### 构建与烧录应用（Building and Flashing）


1. 构建应用（Build the Application）

  可用west工具构建Blinky等Zephyr示例应用。从Zephyr工作区执行以下命令：

  ```text
  west build -b pic32cm_pl10_cnano -p -s samples/basic/blinky
  ```

  这将为pic32cm_pl10_cnano开发板构建Blinky应用。
2. 烧录设备（Flash the Device）

  构建完成后，用以下命令烧录固件：

  ```text
  west flash
  ```
3. 观察结果（Observe the Result）

  烧录后LED0应开始闪烁，表明应用成功运行。

<a id="references"></a>

## 参考资料（References）

PIC32CM PL10产品页面：

[https://www.microchip.com/en-us/product/PIC32CM6408PL10048](https://www.microchip.com/en-us/product/PIC32CM6408PL10048)

PIC32CM PL10 Curiosity Nano评估套件页面：

[https://www.microchip.com/en-us/development-tool/ev10p22a](https://www.microchip.com/en-us/development-tool/ev10p22a)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ev10p22a](https://www.microchip.com/en-us/development-tool/ev10p22a)：HTTP Error 403: Forbidden。
- [PIC32CM6408PL10048](https://www.microchip.com/en-us/product/PIC32CM6408PL10048)：HTTP Error 403: Forbidden。

---

[上一章](P018_PIC32CM_JH01_Curiosity_Pro.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_PIC32CM_SG00_Curiosity_Pro.md)
