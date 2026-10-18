---
id: learning.zephyr-docs.boards-starfive-trenz.page-19
title: Verdin AM62
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/toradex/verdin_am62/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="verdin_am62"></a>

# 第19章\_Verdin AM62

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/toradex/verdin_am62/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/verdin_am62.webp](images/verdin_am62.webp)](images/verdin_am62.webp)

Verdin AM62

名称（Name）：

`verdin_am62`

厂商（Vendor）：

[Toradex AG](https://docs.zephyrproject.org/latest/boards/index.html#vendor=toradex)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[am6234](https://docs.zephyrproject.org/latest/boards/index.html#soc=am6234)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/toradex/verdin_am62/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Verdin-AM62板级配置用于在TI AM62x平台运行Zephyr应用，支持：


- Arm Cortex-M4F微控制器核及以下功能：

  > - 嵌套向量中断控制器（NVIC）
  > - 系统滴答系统时钟（SYSTICK / System Tick System Clock）

此板配置也启用半主机（Semihosting）调试控制台。

详情见[Toradex Verdin AM62产品页](https://www.toradex.com/computer-on-modules/verdin-arm-family/ti-am62)。

<a id="hardware"></a>

## 硬件（Hardware）

Toradex Verdin AM62是基于TI AM62x系列处理器的系统模块（System on Module，SoM），最多具有四个Arm Cortex-A53核、一个Cortex-M4F实时核，以及可编程实时单元（PRU）等专用外设。

Zephyr移植运行在M4F核，使用以下硬件规格：


- 低功耗Arm Cortex-M4F
- 存储器（Memory）

  > - 256 KB SRAM
  > - 16 MB DDR4；原文同时说明模块总容量可从512 MB至最高2 GB

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`verdin_am62`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="verdin_am62-hw-features"></a>

<a id="verdin_am62-verdin_am62/am6234/m4-hw-features-section"></a>

#### `verdin_am62/am6234/m4`目标（Target）

<a id="verdin_am62-verdin_am62/am6234/m4-hw-features-panel"></a>

<a id="verdin_am62-verdin_am62/am6234/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、N/A Flash。

<a id="verdin_am62-verdin_am62/am6234/m4-hw-features-table"></a>

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
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L239">已禁用：6</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此开发板配置使用400 MHz系统时钟。

<a id="ddr-ram"></a>

#### DDR随机存取存储器（DDR RAM）

开发板可配512 MB至2 GB DDR RAM。此板级配置为Zephyr分配约16 MB，包含资源表、核间通信共享内存及供Cortex-M使用的SRAM区域。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置使用MCU域UART，即MCU_UART0，作为唯一串行通信通道。

<a id="programming-the-m4f-core"></a>

## 为M4F核编程（Programming the M4F Core）

Linux内核及U-Boot均可通过remoteproc为Cortex-M4F加载程序。Linux remoteproc使用资源表（Resource Table）加载固件。

测试M4F时，使用以下命令构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)：

```text
# From the root of the Zephyr repository
west build -p -b verdin_am62/am6234/m4 samples/hello_world
```

生成的二进制为build/zephyr目录中的zephyr.elf。

将该文件复制到Verdin AM62，可经eMMC、SD卡或U盘传递，放在目标系统/lib/firmware目录并命名为am62-mcu-m4f0_0-fw，再通过以下Linux remoteproc命令加载；原文将板名写作Verdin AN62。

```text
echo start > /sys/class/remoteproc/remoteproc0/state
```

程序运行后，会向MCU_UART0端口输出Hello World。

若通过U-Boot加载，可在引导加载器终端执行：

```text
rproc init
rproc list
load mmc 0:2 ${loadaddr} /lib/firmware/am62-mcu-m4f0_0-fw
rproc load ${loadaddr} 0 0x${filesize}
rproc start 0
```

提示（Hint）

两种remoteproc示例都应检查远程处理器ID，确保固件加载到正确的核。

核启动后，Hello World将输出到Cortex-M UART。Dahlia及Verdin Development载板对应主机端口在原文中均为/dev/ttyUSB2：

```text
*** Booting Zephyr OS build v4.2.0-1172-g242870ac3feb ***
Hello World! verdin_am62/am6234/m4
```

<a id="references"></a>

## 参考资料（References）

## 译注

Verdin AM62的约16 MB是Zephyr分配内存，不等于模块全部RAM。remoteproc编号须以系统枚举为准，Linux固件安装路径属于目标系统路径。原文AN62拼写保留并注明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ti-am62](https://www.toradex.com/computer-on-modules/verdin-arm-family/ti-am62)：HTTP Error 403: Forbidden。

---

[上一章](P018_Toradex.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_Verdin_iMX8M_Mini.md)
