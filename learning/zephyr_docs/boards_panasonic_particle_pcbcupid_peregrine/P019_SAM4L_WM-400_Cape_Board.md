---
id: learning.zephyr-docs.boards-panasonic-particle-pcbcupid-peregrine.page-19
title: SAM4L WM-400 Cape Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/peregrine/sam4l_wm400_cape/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sam4l_wm400_cape"></a>

# 第19章\_SAM4L WM-400 Cape扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/peregrine/sam4l_wm400_cape/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/wm-400-pin-out.webp](images/wm-400-pin-out.webp)](images/wm-400-pin-out.webp)

SAM4L WM-400 Cape扩展板

名称（Name）：

`sam4l_wm400_cape`

厂商（Vendor）：

[Peregrine Consultoria e Servicos](https://docs.zephyrproject.org/latest/boards/index.html#vendor=peregrine)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sam4lc4b](https://docs.zephyrproject.org/latest/boards/index.html#soc=sam4lc4b)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/peregrine/sam4l_wm400_cape/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SAM4L WM-400 Cape是用于IEEE 802.15.4低功耗节点的完整设计，采用BeagleBone Black Cape扩展板概念，配备Atmel AT86RF233无线收发器，支持开发触摸界面，并可访问多种传感器及通信总线。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAM4LC4B Arm Cortex-M4处理器
- 12 MHz晶体振荡器（Crystal Oscillator）
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- 一路RS232接口
- 一路RS-485全双工接口（Full Duplex）
- Micro-AB USB OTG主机／设备
- 一个用户触摸按键及一个用户机械按键
- 4个用户LED
- 一个AT86RF233 IEEE 802.15.4收发器
- 一个MPL115A2 I2C气压／温度传感器
- 一个VCNL4010接近／光照传感器
- 一个CC2D33S高级湿度／温度传感器
- 一个NCP18WF104J03RB负温度系数（NTC）温度传感器
- 一个TEMT6000X01环境光传感器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sam4l_wm400_cape`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sam4l_wm400_cape-hw-features"></a>

<a id="sam4l_wm400_cape-sam4l_wm400_cape/sam4lc4b-hw-features-section"></a>

#### `sam4l_wm400_cape/sam4lc4b`目标（Target）

<a id="sam4l_wm400_cape-sam4l_wm400_cape/sam4lc4b-hw-features-panel"></a>

<a id="sam4l_wm400_cape-sam4l_wm400_cape/sam4lc4b-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="sam4l_wm400_cape-sam4l_wm400_cape/sam4lc4b-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L224">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L234">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM4L双字闪存控制器（FLASHCALW / Flash Controller Double Word）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P008_atmel_sam4l-flashcalw-controller.md#std-dtcompatible-atmel-sam4l-flashcalw-controller"><code>atmel,sam4l-flashcalw-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM4L通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L193">已启用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P001_atmel_sam4l-gpio.md#std-dtcompatible-atmel-sam4l-gpio"><code>atmel,sam4l-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM4L唯一120位序列号（Unique Serial Number）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L252">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P002_atmel_sam4l-uid.md#std-dtcompatible-atmel-sam4l-uid"><code>atmel,sam4l-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM4L系列I2C主机双线接口（TWIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L101">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L90">已禁用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P010_atmel_sam-i2c-twim.md#std-dtcompatible-atmel-sam-i2c-twim"><code>atmel,sam-i2c-twim</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>板载（On-Board）</td>
<td>ATMEL AT86RF2xx IEEE 802.15.4无线收发器（Wireless Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L102">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P001_atmel_rf2xx.md#std-dtcompatible-atmel-rf2xx"><code>atmel,rf2xx</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L58">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="4">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L161">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Atmel AT45或兼容SPI闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L112">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P008_atmel_at45.md#std-dtcompatible-atmel-at45"><code>atmel,at45</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L124">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L187">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM随机数发生器（RNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L244">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P004_atmel_sam-trng.md#std-dtcompatible-atmel-sam-trng"><code>atmel,sam-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L144">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L160">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L41">已启用：1</a>）</td>
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
<td>Atmel SAM系列USB控制器（USBC），设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P004_atmel_sam-usbc.md#std-dtcompatible-atmel-sam-usbc"><code>atmel,sam-usbc</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM4L看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L258">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P009_atmel_sam4l-watchdog.md#std-dtcompatible-atmel-sam4l-watchdog"><code>atmel,sam4l-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id3"></a>

详情见[SAM4L WM-400 Cape](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs) [注1](#id2)资料。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAM4L MCU使用板上的12 MHz内部振荡器，经片上PLL生成48 MHz系统时钟（振荡器类型依原文保留）。

<a id="serial-port"></a>

### 串口（Serial Port）

ATSAM4LC4B有4路USART，其中USART3在RS232及RS485接口之间共享。默认控制台可通过板载RS232端口或USB设备访问。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sam4l_wm400_cape`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-bossac">bossac</a></td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
</table>

此板有10引脚排针，可连接Segger J-Link对SAM4LC4B进行编程及调试。板上预装SAM-BA引导加载程序，仅支持烧录。

<a id="flashing"></a>

### 烧录（Flashing）


1. J-Link使用说明见“J-Link调试主机工具”。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
2. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
3. 通过USB调试端口连接SAM4L WM-400 Cape与主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4l_wm400_cape samples/hello_world
  west flash
  ```

  终端应显示Hello World! sam4l_wm400_cape。
4. SAM-BA引导加载程序说明见SAM启动助手（SAM Boot Assistant）。（[SAM启动助手（SAM-BA / SAM Boot Assistant）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#atmel-sam-ba-bootloader)）
5. 按住S1，通过USB调试端口将开发板连接主机，再构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)。编程结束后，应用自动启动。

  ```text
  # From the root of the zephyr repository
  west build -b sam4l_wm400_cape samples/hello_world
  west flash -r bossac
  ```

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b sam4l_wm400_cape samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs)

## 译注

SAM4L WM-400 Cape的USART3在RS232与RS485间共享；J-Link可烧录和调试，预装SAM-BA仅用于烧录，连接时按住S1。

---

[上一章](P018_Peregrine.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
