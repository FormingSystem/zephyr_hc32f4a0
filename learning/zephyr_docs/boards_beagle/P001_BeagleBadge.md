---
id: learning.zephyr-docs.boards-beagle.page-1
title: BeagleBadge
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/beagle/beaglebadge/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="beaglebadge"></a>

# 第1章\_BeagleBadge

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/beagle/beaglebadge/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/beaglebadge.webp](images/beaglebadge.webp)](images/beaglebadge.webp)

BeagleBadge

名称（Name）：

`beaglebadge`

厂商（Vendor）：

[BeagleBoard.org基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=beagle)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[am62l3](https://docs.zephyrproject.org/latest/boards/index.html#soc=am62l3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beaglebadge/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

BeagleBoard.org BeagleBadge将丰富的内置传感能力与灵活扩展结合，为可穿戴设备提供新的设计方式。它基于TI Sitara AM62L双核ARM Cortex-A53片上系统（SoC）。

详情见BeagleBoard.org BeagleBadge产品页面。（[BeagleBoard.org BeagleBadge产品页面（Product Page）](https://www.beagleboard.org/boards/beaglebadge)）

<a id="hardware"></a>

## 硬件（Hardware）


- 处理器（Processor）


  - TI Sitara AM62L SoC，包含两个ARM Cortex-A53内核
- 存储器（Memory）


  - 256 MB低功耗DDR4（LPDDR4）
  - 256 Mb八线SPI闪存（OSPI Flash）
  - 32 Kb电可擦除可编程只读存储器（EEPROM）
- 无线连接（Wireless Connectivity）


  - BeagleMod CC3301-1216模块，支持2.4 GHz Wi-Fi 6
  - Bluetooth 5.2，带MHF4连接器
  - LoRaWAN，使用Wio SX1262模块及u.FL连接器
- 内置传感器（Built-In Sensors）


  - 一个惯性测量单元传感器（IMU）
  - 一个环境光传感器（Ambient Light Sensor）
  - 一个温度与湿度传感器
- 用户界面（User Interface）


  - 4.2英寸电子纸显示屏（ePaper Display）
  - 一个支持按下的四向操纵杆按键（Joystick）
  - 两个轻触按键，分别为返回（Back）及选择（Select）
  - 一个无源蜂鸣器（Passive Buzzer）
  - 一个RGB状态LED
  - 两个七段数码管（7-Segment LED Displays）
- 扩展（Expansion）


  - 用于LCD显示屏的MIPI显示串行接口连接器（DSI）
  - USB Type-C，用于电源输入和调试
  - 一个mikroBUS连接器
  - 一个USB 2.0 Type-A主机端口
  - 一个Micro-SD卡槽
  - 两个QWIIC连接器
  - 一个Grove连接器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`beaglebadge`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="beaglebadge-hw-features"></a>

<a id="beaglebadge-beaglebadge/am62l3/a53-hw-features-section"></a>

#### `beaglebadge/am62l3/a53`目标（Target）

<a id="beaglebadge-beaglebadge/am62l3/a53-hw-features-panel"></a>

<a id="beaglebadge-beaglebadge/am62l3/a53-hw-features-memory"></a>

该开发板目标的片上存储容量：224 MiB RAM、N/A Flash。

<a id="beaglebadge-beaglebadge/am62l3/a53-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L25">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>TI AM335X模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L321">已禁用：1</a>）</td>
<td><a href="../hardware/P904_TIAM335x模数转换器绑定.md#dtbinding-ti-am335x-adc"><code>ti,am335x-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI K3代处理器中基于计数器的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-wakeup.dtsi?plain=1#L57">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter"><code>ti,k3-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Solomon SSD16XX电子纸显示控制器（EPD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebadge/beaglebadge_am62l3_a53.dts?plain=1#L109">已启用：1</a>）</td>
<td><a href="../display_solomon_oled_epd_binding_reference/P020_solomon_ssd1681.md#std-dtcompatible-solomon-ssd1681"><code>solomon,ssd1681</code></a></td>
</tr>
<tr>
<td rowspan="4">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>系统控制与管理接口（SCMI），使用ARM安全监控调用（SMC）作为门铃通知，并通过共享内存（SHMEM）传输（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P601_SCMI安全调用传输绑定.md#dtbinding-arm-scmi-smc"><code>arm,scmi-smc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域协议（Power Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P604_SCMI电源域协议绑定.md#dtbinding-arm-scmi-power"><code>arm,scmi-power</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口时钟协议（Clock Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../hardware/P603_SCMI时钟协议绑定.md#dtbinding-arm-scmi-clock"><code>arm,scmi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口共享内存（SHMEM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L73">已启用：1</a>）</td>
<td><a href="../hardware/P602_SCMI共享内存绑定.md#dtbinding-arm-scmi-shmem"><code>arm,scmi-shmem</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L211">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-wakeup.dtsi?plain=1#L16">已禁用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L98">已禁用：5</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebadge/beaglebadge_am62l3_a53.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>带多线SPI接口（MSPI）的Cadence xSPI闪存控制器，支持双线、四线及八线SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L488">已禁用：1</a>）</td>
<td><a href="../mspi_binding_reference/P003_cdns_xspi-nor.md#std-dtcompatible-cdns-xspi-nor"><code>cdns,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-wakeup.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域（Power Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l_power_domains.dtsi?plain=1#L11">已启用：31</a>）</td>
<td><a href="../hardware/P613_SCMI电源域绑定.md#dtbinding-arm-scmi-power-domain"><code>arm,scmi-power-domain</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型高分辨率PWM（EHRPWM）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L431">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P014_ti_am3352-ehrpwm.md#std-dtcompatible-ti-am3352-ehrpwm"><code>ti,am3352-ehrpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型捕获模块（ECAP）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L461">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P013_ti_am3352-ecap.md#std-dtcompatible-ti-am3352-ecap"><code>ti,am3352-ecap</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L368">已禁用：3</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L21">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L32">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L265">已禁用：4</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L332">已禁用：6</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/am62l3_a53.dtsi?plain=1#L79">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L247">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置使用主域（MAIN Domain）的UART `main_uart0`提供单路串行通信通道。

<a id="sd-card"></a>

## SD卡（SD Card）

按[使用Yocto构建SDK（Building the SDK with Yocto）](https://software-dl.ti.com/processor-sdk-linux-rt/esd/AM62LX/11_02_08_02/exports/docs/linux/Overview_Building_the_SDK.html)的说明构建AM62L SDK，设置`MACHINE=beaglebadge-ti`。用镜像写入软件将生成的WIC文件写入SD卡。

构建Zephyr，例如使用以下命令构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b beaglebadge/am62l3/a53 samples/hello_world
```

构建生成的二进制文件名为`zephyr.bin`，位于`build/zephyr`目录。

将编译后的`zephyr.bin`复制到SD卡第一个FAT分区，把SD卡插入开发板，上电并在提示符处中断U-Boot执行。

使用U-Boot加载并启动`zephyr.bin`：

```text
fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

Zephyr应用应开始在A53内核上运行。

<a id="debugging"></a>

## 调试（Debugging）

开发板通过板边SOICbite连接器引出JTAG。

<a id="references"></a>

## 参考资料（References）


- [BeagleBoard.org BeagleBadge产品页面（Product Page）](https://www.beagleboard.org/boards/beaglebadge)

## 译注

原文分别使用256 MB LPDDR4、256 Mb OSPI及32 Kb EEPROM，字节与比特单位未统一替换。官方Yocto与U-Boot命令完整保留，本页未新增本仓库构建步骤。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_BeagleBone_AI-64.md)
