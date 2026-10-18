---
id: learning.zephyr-docs.boards-bouffalo-qnx-bliiot-blues.page-7
title: BLIIoT ARMxy BL350 AM62x M4
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/bliiot/am62x_m4_bl350/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="am62x_m4_bl350"></a>

# 第7章\_BLIIoT ARMxy BL350 AM62x M4

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/bliiot/am62x_m4_bl350/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/am62x_m4_bl350.webp](images/am62x_m4_bl350.webp)](images/am62x_m4_bl350.webp)

BLIIoT ARMxy BL350 AM62x M4

名称（Name）：

`am62x_m4_bl350`

厂商（Vendor）：

[BLIIoT科技有限公司（BLIIoT Technology Co., Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=bliiot)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[am6254](https://docs.zephyrproject.org/latest/boards/index.html#soc=am6254)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bliiot/am62x_m4_bl350/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

BLIIoT ARMxy BL350 AM62x Cortex-M4F属于BL350工业嵌入式控制器系列，采用TI Sitara AM62x（AM6254）SoC，包含最高1.4 GHz的四核Cortex-A53簇及专用Cortex-M4F MCU内核。它面向工业自动化，支持−40 °C至85 °C工作温度范围。

Zephyr移植面向Cortex-M4F MCU域，为工业I/O控制提供确定性的实时性能；主Cortex-A53簇运行Linux。两域通过预留共享DDR区域（Carveout）上的OpenAMP／RPMsg处理器间通信（IPC）交换数据。

<a id="hardware"></a>

## 硬件（Hardware）

开发板基于TI AM6254 SoC：


- Linux域CPU：四核ARM Cortex-A53，最高1.4 GHz
- Zephyr域MCU：ARM Cortex-M4F，400 MHz
- Memory:


  - 256 KB MCU SRAM：192 KB指令区（I-Code）位于`0x0`，64 KB数据区（D-Code）位于`0x30000`
  - 最多2 GB共享DDR4，Linux为M4F预留以下区域：


    - 14 MB M4F区域，基址`0x9cc00000`；前4 KB存放资源表，之后存放代码和数据
    - 1 MB IPC／DMA区域，基址`0x9cb00000`，用于OpenAMP虚拟环（Vrings）
  - 最多8 GB eMMC，供Linux使用
- 工业I/O：RS232／RS485、两路CAN FD、数字输入／输出（DI/DO）、电阻温度检测器（RTD）、热电偶（Thermocouple）及可配置X／Y系列扩展模块

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`am62x_m4_bl350`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="am62x_m4_bl350-hw-features"></a>

<a id="am62x_m4_bl350-am62x_m4_bl350/am6254/m4-hw-features-section"></a>

#### `am62x_m4_bl350/am6254/m4`目标（Target）

<a id="am62x_m4_bl350-am62x_m4_bl350/am6254/m4-hw-features-panel"></a>

<a id="am62x_m4_bl350-am62x_m4_bl350/am6254/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、192 KiB Flash。

<a id="am62x_m4_bl350-am62x_m4_bl350/am6254/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI K3代处理器中基于计数器的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L302">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter"><code>ti,k3-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L161">已禁用：6</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L73">已禁用：5</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L315">已禁用：3</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L84">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L10">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L274">已禁用：3</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L35">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L114">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L239">已禁用：5</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

BL350通过X／Y系列I/O扩展连接器提供RS232／RS485、CAN、DI/DO、RTD、热电偶（TC）等接口。Zephyr M4F镜像通过RPMsg IPC通道与A53 Linux应用层通信。

<a id="system-clock"></a>

#### 系统时钟（System Clock）

M4F MCU域使用固定400 MHz系统时钟，由设备树配置确定。

<a id="serial-port"></a>

#### 串口（Serial Port）

Zephyr默认控制台连接到MCU域UART `uart0`，设置为115200 8N1。基础设备树未启用AM62x主域UART及路由到X／Y系列扩展连接器的其他I/O；应用需要哪些接口，应通过设备树覆盖文件启用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="building"></a>

### 构建（Building）

使用目标限定符`am62x_m4_bl350/am6254/m4`构建M4F内核的Zephyr应用：

```text
west build -b am62x_m4_bl350/am6254/m4 samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

M4F二进制程序由运行Linux的A53内核通过remoteproc加载。将编译后的ELF传到目标文件系统，再通过sysfs启动内核：

```text
# On the target Linux system (as root):
cp zephyr.elf /lib/firmware/
echo zephyr.elf > /sys/class/remoteproc/remoteproc1/firmware
echo start      > /sys/class/remoteproc/remoteproc1/state
```

停止内核：

```text
echo stop > /sys/class/remoteproc/remoteproc1/state
```

<a id="debugging"></a>

### 调试（Debugging）

M4F的崩溃及日志输出可通过MCU UART查看，在Linux侧通常为`/dev/ttyS0`或类似设备，波特率115200。

使用JTAG调试时，将XDS110或兼容探针连接到AM62x JTAG排针，并使用Code Composer Studio（CCS）或配有TI专用目标配置的OpenOCD。M4F在AM62x调试链中对应`Cortex_M4_0`目标。

<a id="references"></a>

## 参考资料（References）


- [BLIIoT BL350产品页面（Product Page）](https://bliiot.com/products/industrial-controller-bl350)
- [TI AM62x技术参考手册（Technical Reference Manual）](https://www.ti.com/lit/ug/spruj40c/spruj40c.pdf)
- [TI AM62x数据手册（Datasheet）](https://www.ti.com/lit/ds/symlink/am6254.pdf)
- [Zephyr remoteproc文档](https://docs.zephyrproject.org/latest/services/ipc/openamp.html)

## 译注

本页/lib/firmware、/sys、/dev等为目标Linux系统目录，不是文档仓库的位置。M4F预留DDR、OpenAMP vring区域、MCU控制台及未默认启用的扩展I/O条件均按官方页面保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [openamp.html](https://docs.zephyrproject.org/latest/services/ipc/openamp.html)：HTTP Error 404: Not Found。
- [am6254.pdf](https://www.ti.com/lit/ds/symlink/am6254.pdf)：HTTP Error 404: Not Found。

---

[上一章](P006_QNX_Hypervisor_Virtual_Machine.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_BLIIoT_Technology_Co._Ltd..md)
