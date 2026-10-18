---
id: learning.zephyr-docs.boards-retronix-sifli.page-21
title: Ganymed Starter Kit SK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/sensry/ganymed_sk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ganymed_sk"></a>

# 第21章\_Ganymed入门套件（Starter Kit，SK）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/sensry/ganymed_sk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/ganymed_sk.webp](images/ganymed_sk.webp)](images/ganymed_sk.webp)

Ganymed入门套件（Starter Kit，SK）

名称（Name）：

`ganymed_sk`

厂商（Vendor）：

[sensry.io](https://docs.zephyrproject.org/latest/boards/index.html#vendor=sensry)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[`riscv`](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[sy120_gen1](https://docs.zephyrproject.org/latest/boards/index.html#soc=sy120_gen1)、[sy120_gbm](https://docs.zephyrproject.org/latest/boards/index.html#soc=sy120_gbm)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sensry/ganymed_sk/doc/index.rst/../..)<a id="overview"></a>

<a id="ganymed-sk"></a>

## 概述（Overview）

注意（Note）

Ganymed入门套件的全部软件均为实验性（Experimental），硬件仅向有限样品计划的参与者提供。

Ganymed板支持Ganymed SY1xx系列物联网多核RISC-V SoC，并可选配传感器层。

<a id="hardware"></a>

## 硬件（Hardware）


- 32位RISC-V 1+8核处理器，最高500 MHz


  - 一个数据采集单元（Data Acquisition Unit）
  - 八个数据处理单元（Data Processing Unit）
  - 事件总线（Event Bus）
  - MicroDMA
- 4096 KB全局SRAM（Global SRAM）
- 64 KB安全SRAM（Secure SRAM）
- 512 KB全局磁阻式存储器（Global MRAM）
- 512 KB安全磁阻式存储器（Secure MRAM）
- 时钟（CLOCK）
- 外设（Peripherals）

  > - 32路GPIO
  > - 四路双线接口主机（TWIM）
  > - 四路I2S
  > - 七路SPI
  > - 3路通用异步收发器（UART）
  > - 一路时间敏感网络（TSN）接口
  > - 一路可变数据速率CAN（CAN-FD）
  > - 三路模数转换器（ADC）
- 可选的板载电源生成及电源测量部分

  > - USB Type-C
  > - 外部5 V电源
- 40引脚JTAG连接器，兼容Olimex ARM-JTAG-OCD-H
- 通过FTDI连接USB，内部连接UART0
- 用于全部I/O及配置的排针
- SoC装配选项（Assembly Options）


  - SY120-GBM：通用基础模块（Generic Base Module），不带上层传感器
  - SY120-GEN1：通用一型模块（Generic Module Type 1），带上层传感器，见下文

ganymed-sk/sy120-gen1带有额外板载传感器。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ganymed_sk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ganymed_sk-hw-features"></a>

<a id="ganymed_sk-ganymed_sk/sy120_gbm-hw-features-section"></a>

#### `ganymed_sk/sy120_gbm`目标（Target）

<a id="ganymed_sk-ganymed_sk/sy120_gbm-hw-features-panel"></a>

<a id="ganymed_sk-ganymed_sk/sy120_gbm-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、N/A Flash。

<a id="ganymed_sk-ganymed_sk/sy120_gbm-hw-features-table"></a>

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
<td>Sensry Ganymed SY1xx处理器核（Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P036_sensry_sy1xx.md#std-dtcompatible-sensry-sy1xx"><code>sensry,sy1xx</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P007_sensry_sy1xx-mdio.md#std-dtcompatible-sensry-sy1xx-mdio"><code>sensry,sy1xx-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>单端口千兆铜缆以太网物理层收发器（PHY），支持GMII／RGMII／MII／RMII接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_sk/ganymed_sk_sy120_gbm.dts?plain=1#L39">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P006_microchip_vsc8541.md#std-dtcompatible-microchip-vsc8541"><code>microchip,vsc8541</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>需要指定一组引脚控制器状态（Pinctrl States）的设备应包含此文件（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L237">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P019_sensry_sy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac"><code>sensry,sy1xx-mac</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P007_sensry_sy1xx-gpio.md#std-dtcompatible-sensry-sy1xx-gpio"><code>sensry,sy1xx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx I2C驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L97">已禁用：4</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P001_sensry_sy1xx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c"><code>sensry,sy1xx-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx事件单元（Event Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P013_sensry_sy1xx-event-unit.md#std-dtcompatible-sensry-sy1xx-event-unit"><code>sensry,sy1xx-event-unit</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_sk/ganymed_sk_sy120_gbm.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L220">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P021_sensry_sy1xx-pinctrl.md#std-dtcompatible-sensry-sy1xx-pinctrl"><code>sensry,sy1xx-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L141">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P011_sensry_sy1xx-trng.md#std-dtcompatible-sensry-sy1xx-trng"><code>sensry,sy1xx-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L73">已启用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P001_sensry_sy1xx-uart.md#std-dtcompatible-sensry-sy1xx-uart"><code>sensry,sy1xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L157">已禁用：7</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P002_sensry_sy1xx-spi.md#std-dtcompatible-sensry-sy1xx-spi"><code>sensry,sy1xx-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L30">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Sensry Ganymed定时器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L57">已启用：2</a>）</td>
<td><a href="../system_timer_binding_reference/P013_sensry_sy1xx-sys-timer.md#std-dtcompatible-sensry-sy1xx-sys-timer"><code>sensry,sy1xx-sys-timer</code></a></td>
</tr>
</table>

<a id="ganymed_sk-ganymed_sk/sy120_gen1-hw-features-section"></a>

#### `ganymed_sk/sy120_gen1`目标（Target）

<a id="ganymed_sk-ganymed_sk/sy120_gen1-hw-features-panel"></a>

<a id="ganymed_sk-ganymed_sk/sy120_gen1-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、N/A Flash。

<a id="ganymed_sk-ganymed_sk/sy120_gen1-hw-features-table"></a>

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
<td>Sensry Ganymed SY1xx处理器核（Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P036_sensry_sy1xx.md#std-dtcompatible-sensry-sy1xx"><code>sensry,sy1xx</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P007_sensry_sy1xx-mdio.md#std-dtcompatible-sensry-sy1xx-mdio"><code>sensry,sy1xx-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>单端口千兆铜缆以太网物理层收发器（PHY），支持GMII／RGMII／MII／RMII接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_sk/ganymed_sk_sy120_gen1.dts?plain=1#L39">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P006_microchip_vsc8541.md#std-dtcompatible-microchip-vsc8541"><code>microchip,vsc8541</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>需要指定一组引脚控制器状态（Pinctrl States）的设备应包含此文件（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L237">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P019_sensry_sy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac"><code>sensry,sy1xx-mac</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P007_sensry_sy1xx-gpio.md#std-dtcompatible-sensry-sy1xx-gpio"><code>sensry,sy1xx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx I2C驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L97">已禁用：4</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P001_sensry_sy1xx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c"><code>sensry,sy1xx-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx事件单元（Event Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P013_sensry_sy1xx-event-unit.md#std-dtcompatible-sensry-sy1xx-event-unit"><code>sensry,sy1xx-event-unit</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_sk/ganymed_sk_sy120_gen1.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L220">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P021_sensry_sy1xx-pinctrl.md#std-dtcompatible-sensry-sy1xx-pinctrl"><code>sensry,sy1xx-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L141">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P011_sensry_sy1xx-trng.md#std-dtcompatible-sensry-sy1xx-trng"><code>sensry,sy1xx-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L73">已启用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P001_sensry_sy1xx-uart.md#std-dtcompatible-sensry-sy1xx-uart"><code>sensry,sy1xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Sensry SY1xx SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L157">已禁用：7</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P002_sensry_sy1xx-spi.md#std-dtcompatible-sensry-sy1xx-spi"><code>sensry,sy1xx-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L30">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Sensry Ganymed定时器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L57">已启用：2</a>）</td>
<td><a href="../system_timer_binding_reference/P013_sensry_sy1xx-sys-timer.md#std-dtcompatible-sensry-sy1xx-sys-timer"><code>sensry,sy1xx-sys-timer</code></a></td>
</tr>
</table>

<a id="id3"></a>

更详细说明见[Ganymed入门套件文档](https://docs.sensry.net/datasheets/sy120-bob/)[注1](#id2)。

<a id="programming-and-testing"></a>

## 编程及测试（Programming and Testing）

`ganymed_sk`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>sy1xx</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

ganymed_sk/sy120_gbm板级配置的应用可按常规方式构建及烧录，构建和运行详情见“构建应用”及“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
west build -b ganymed_sk/sy120_gbm samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

使用[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例测试Ganymed。

烧录Zephyr镜像：

```text
west build -b None --dev-id /dev/ttyUSB0 samples/hello_world
west flash
```

<a id="testing"></a>

### 测试（Testing）

随后连接minicom、picocom或PuTTY等串口控制台，并复位目标；示例输出应为：

```text
Hello World! ganymed_sk/sy120_gbm
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://docs.sensry.net/datasheets/sy120-bob/](https://docs.sensry.net/datasheets/sy120-bob/)

## 译注

Ganymed Starter Kit同样处于实验性状态，不能把BOB的板名直接用于SK构建。1+8核、全局及安全存储容量按原文保留。

---

[上一章](P020_Ganymed_Break-Out-Board_BOB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_Sensry.md)
