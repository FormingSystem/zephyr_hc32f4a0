---
id: learning.zephyr-docs.boards-ti.page-21
title: MSPM33C321A Launchpad
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/lp_mspm33c321a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lp_mspm33c321a"></a>

# 第21章\_MSPM33C321A LaunchPad

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/lp_mspm33c321a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`lp_mspm33c321a`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mspm33c321a](https://docs.zephyrproject.org/latest/boards/index.html#soc=mspm33c321a)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/lp_mspm33c321a/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MSPM33C321A属于TI MSP高度集成、超低功耗32位微控制器系列，基于Arm Cortex-M33，最高160 MHz，集成高性能模拟外设，支持−40 °C至125 °C扩展温度范围及1.62—3.6 V供电。

MSPM33C321A提供1 MB内置纠错码（ECC）的嵌入式程序闪存及256 KB可选硬件奇偶校验的SRAM，还集成存储器保护单元（MPU）、DMA及以下外设：


- 模拟功能（Analog）


  - 一个12位高速逐次逼近型模数转换器（SAR HSADC），具有4个序列器、最多32个输入通道、最高8倍过采样及1.4 V／2.5 V内部电压基准
- 数字功能（Digital）


  - 多个定时器组（TIMG），支持闹钟及捕获／比较（Capture/Compare）
  - 最多三个支持中断的GPIO端口：GPIOA、GPIOB及GPIOC
  - 最多16通道的DMA控制器
- 通信接口（Communication）


  - 通用通信（Universal Communication，UNICOMM）外设，支持UART、SPI及I2C模式，可按实例配置

<a id="id4"></a>

<a id="id6"></a>

完整规格见[MSPM33C321A数据手册](https://www.ti.com/product/MSPM33C321A)[注2](#id3)及技术参考手册[注3](#id5)。（[MSPM33C321A技术参考手册](https://www.ti.com/lit/ug/slau962/slau962.pdf)）

<a id="hardware"></a>

## 硬件（Hardware）

LP-MSPM33C321A LaunchPad是用于MSPM33C321A微控制器的低成本开发板。

开发板特性（Board Features）：


- MSPM33C321A微控制器：160 MHz Arm Cortex-M33、1 MB闪存及256 KB SRAM
- 板载XDS110调试探针，提供SWD接口
- 三个用户LED，红、绿、蓝，以及两个按键
- 多个扩展排针，兼容BoosterPack生态
- 板载32.768 kHz晶体，用于低频时钟（LFCLK）

<a id="id2"></a>

LP-MSPM33C321A LaunchPad详情见[TI LP-MSPM33C321A产品页](https://www.ti.com/tool/LP-MSPM33C321A)[注1](#id1)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lp_mspm33c321a`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lp_mspm33c321a-hw-features"></a>

<a id="lp_mspm33c321a-lp_mspm33c321a/mspm33c321a-hw-features-section"></a>

#### `lp_mspm33c321a/mspm33c321a`目标（Target）

<a id="lp_mspm33c321a-lp_mspm33c321a/mspm33c321a-hw-features-panel"></a>

<a id="lp_mspm33c321a-lp_mspm33c321a/mspm33c321a-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="lp_mspm33c321a-lp_mspm33c321a/mspm33c321a-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm33c/mspm33c.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm33c/mspm33c.dtsi?plain=1#L49">已禁用：3</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P016_ti_mspm0-gpio.md#std-dtcompatible-ti-mspm0-gpio"><code>ti,mspm0-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm33c/mspm33c.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0引脚控制节点（Pinctrl）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm33c/mspm33c.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P014_ti_mspm0-pinctrl.md#std-dtcompatible-ti-mspm0-pinctrl"><code>ti,mspm0-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm33c/mspm33c.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="leds"></a>

#### 发光二极管（LEDs）


- LED0，红色：PC26
- LED1，绿色：PC27
- LED2，蓝色：PA2

<a id="push-buttons"></a>

#### 按键（Push Buttons）


- S1：复位（Reset）
- S2，用户按键：PB21

<a id="serial-port"></a>

#### 串口（Serial Port）

Zephyr控制台使用UNICOMM12 UART，TX为PA10，RX为PA11。默认115200、8N1、无流控，可通过XDS110调试器的USB虚拟COM端口访问。

<a id="system-clock"></a>

#### 系统时钟（System Clock）

MSPM33C321A时钟树由32 MHz系统振荡器（SYSOSC）经系统锁相环（PLL）驱动：


- SYSOSC（32 MHz）→ SYSPLL → HSCLK → MCLK（160 MHz CPU时钟）
- ULPCLK：40 MHz超低功耗外设时钟
- LFCLK：32.768 kHz低频时钟，来自板载晶体

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lp_mspm33c321a`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

注意（Note）

原文编写时MSPM33支持尚未进入上游OpenOCD。对此板使用west flash或west debug前，必须先构建TI定制OpenOCD分支，见下文“构建带补丁的OpenOCD”。（[构建带补丁的OpenOCD（Building a Patched OpenOCD）](#building-a-patched-openocd)）

<a id="building"></a>

### 构建（Building）

Zephyr应用开发请遵循[入门指南](../getting_started/P002_入门指南.md#getting-started)。

```text
# From the root of the zephyr repository
west build -b lp_mspm33c321a samples/basic/blinky
```

<a id="flashing"></a>

### 烧录（Flashing）

构建定制OpenOCD后，按以下方式烧录：

```text
$ west flash --openocd <path-to-openocd>/src/openocd \
      --openocd-search <path-to-openocd>/tcl
```

烧录后需要复位才能启动应用。可按板上nRST按键，或运行：

```text
$ <path-to-openocd>/src/openocd -s <path-to-openocd>/tcl \
      -f board/ti_mspm33_launchpad.cfg \
      -c "init; mspm33_board_reset; shutdown"
```

连接多块开发板时，先查明各板XDS110序列号，再将其传给适配器：

```text
$ lsusb -v -d 0451:bef3 | grep iSerial
$ west flash --openocd <path-to-openocd>/src/openocd \
      --openocd-search <path-to-openocd>/tcl \
      --cmd-pre-init "adapter serial <serial_number>"
```

<a id="debugging"></a>

### 调试（Debugging）

```text
# From the root of the zephyr repository
west build -b lp_mspm33c321a samples/basic/blinky
west debug
```

传入与烧录时相同的--openocd及--openocd-search参数。

<a id="building-a-patched-openocd"></a>

### 构建带补丁的OpenOCD（Building a Patched OpenOCD）

MSPM33的OpenOCD支持由TI分支提供，构建步骤如下：


1. 安装Ubuntu依赖项：

  ```text
  $ sudo apt install autoconf automake libtool pkg-config \
        libusb-1.0-0-dev libhidapi-dev
  ```
2. 克隆并构建：

  ```text
  $ git clone -b ti-release https://github.com/TexasInstruments/ti-openocd
  $ cd ti-openocd
  $ git submodule update --init --recursive
  $ ./bootstrap
  $ ./configure --enable-xds110
  $ make
  ```

<a id="id8"></a>

[TI OpenOCD ti-v1.2.0发布页](https://github.com/TexasInstruments/ti-openocd/releases/tag/ti-v1.2.0)[注4](#id7)提供Linux及Windows预构建二进制文件。

<a id="recovery"></a>

### 恢复（Recovery）

TI OpenOCD提供器件恢复命令：

恢复出厂设置（Factory Reset），用于恢复锁定或无法正常使用的开发板：

```text
$ <path-to-openocd>/src/openocd -s <path-to-openocd>/tcl \
      -f board/ti_mspm33_launchpad.cfg \
      -c "init; mspm33_factory_reset; shutdown"
```

整片擦除（Mass Erase），擦除全部闪存：

```text
$ <path-to-openocd>/src/openocd -s <path-to-openocd>/tcl \
      -f board/ti_mspm33_launchpad.cfg \
      -c "init; mspm33_mass_erase; shutdown"
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.ti.com/tool/LP-MSPM33C321A](https://www.ti.com/tool/LP-MSPM33C321A)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.ti.com/product/MSPM33C321A](https://www.ti.com/product/MSPM33C321A)

<a id="id5"></a>

〔[3](#id6)〕 [https://www.ti.com/lit/ug/slau962/slau962.pdf](https://www.ti.com/lit/ug/slau962/slau962.pdf)

<a id="id7"></a>

〔[4](#id8)〕 [https://github.com/TexasInstruments/ti-openocd/releases/tag/ti-v1.2.0](https://github.com/TexasInstruments/ti-openocd/releases/tag/ti-v1.2.0)

## 译注

MSPM33C321A控制台为UNICOMM12，PA10发送、PA11接收，经XDS110虚拟串口。原文要求TI OpenOCD分支，烧录后须复位；恢复出厂及整片擦除命令按原文保留，仅作翻译，未执行。

---

[上一章](P020_MSPM0L2228_Launchpad.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_MSP-EXP432P401R_LaunchXL.md)
