---
id: learning.zephyr-docs.boards-ti.page-2
title: AM62L TMDS62LEVM evaluation module EVM
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/am62l_evm/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="am62l_evm"></a>

# 第2章\_AM62L TMDS62LEVM评估模块（EVM）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/am62l_evm/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/am62l_evm.webp](images/am62l_evm.webp)](images/am62l_evm.webp)

AM62L TMDS62LEVM评估模块（EVM）

名称（Name）：

`am62l_evm`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[am62l3](https://docs.zephyrproject.org/latest/boards/index.html#soc=am62l3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/am62l_evm/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

AM62L EVM板级配置用于在TI AM62L平台上运行Zephyr应用，支持：


- Arm Cortex-A53核及以下功能：

  > - 通用中断控制器（GIC）
  > - Arm通用定时器（arch_timer）
  > - 片上SRAM（oc_sram）
  > - UART接口，uart0至uart6
  > - 通过ti-io-exp配置片段（Snippet）启用的I/O扩展器

此板配置也启用半主机（Semihosting）调试控制台。

详情见[TI AM62L产品页](https://www.ti.com/product/AM62L)。

<a id="hardware"></a>

## 硬件（Hardware）

AM62L EVM搭载包含双核Cortex-A53集群的AM62L SoC，使用以下硬件规格：


- 高性能Arm Cortex-A53
- 存储器（Memory）

  > - 160 KB SRAM
  > - 2 GB DDR4
- 调试（Debug）

  > - 基于XDS110的JTAG

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`am62l_evm`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="am62l_evm-hw-features"></a>

<a id="am62l_evm-am62l_evm/am62l3/a53-hw-features-section"></a>

#### `am62l_evm/am62l3/a53`目标（Target）

<a id="am62l_evm-am62l_evm/am62l3/a53-hw-features-panel"></a>

<a id="am62l_evm-am62l_evm/am62l3/a53-hw-features-memory"></a>

此板级目标的存储：2016 MiB RAM及64 MiB Flash。

<a id="am62l_evm-am62l_evm/am62l3/a53-hw-features-table"></a>

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
<td>TI AM335X模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L321">已启用：1</a>）</td>
<td><a href="../hardware/P904_TIAM335x模数转换器绑定.md#dtbinding-ti-am335x-adc"><code>ti,am335x-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI K3代处理器中基于计数器的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-wakeup.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter"><code>ti,k3-rtc-counter</code></a></td>
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
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>TI TCA6424A，基于I2C的GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am62l_evm/am62l_evm_am62l3_a53.dts?plain=1#L143">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P019_ti_tca6424a.md#std-dtcompatible-ti-tca6424a"><code>ti,tca6424a</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L238">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L211">已禁用：4</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L98">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L120">已禁用：3</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
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
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am62l_evm/am62l_evm_am62l3_a53.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>带多线SPI接口（MSPI）的Cadence xSPI闪存控制器，支持双线、四线及八线SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L488">已启用：1</a>）</td>
<td><a href="../mspi_binding_reference/P003_cdns_xspi-nor.md#std-dtcompatible-cdns-xspi-nor"><code>cdns,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am62l_evm/am62l_evm_am62l3_a53.dts?plain=1#L128">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Infineon S28HX512T闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am62l_evm/am62l_evm_am62l3_a53.dts?plain=1#L246">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P020_infineon_s28hx512t-mspi.md#std-dtcompatible-infineon-s28hx512t"><code>infineon,s28hx512t</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am62l_evm/am62l_evm_am62l3_a53.dts?plain=1#L268">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
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
<td>TI SoC基于增强型高分辨率PWM（EHRPWM）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L431">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L441">已禁用：2</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P014_ti_am3352-ehrpwm.md#std-dtcompatible-ti-am3352-ehrpwm"><code>ti,am3352-ehrpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型捕获模块（ECAP）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L461">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L470">已禁用：2</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P013_ti_am3352-ecap.md#std-dtcompatible-ti-am3352-ecap"><code>ti,am3352-ecap</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L368">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L411">已禁用：1</a>）</td>
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
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L247">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am62l-main.dtsi?plain=1#L256">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="i-o-expander-support"></a>

### I/O扩展器支持（I/O Expander Support）

AM62L EVM配有I/O扩展器J2，其信号默认路由到HDMI接口。配置SoC_VOUT0_FET_SEL0，即GPIO0_89，或短接J29，可使信号路由到扩展排针。

<a id="enabling-i-o-expander-support"></a>

#### 启用I/O扩展器支持

构建应用时使用ti-io-exp配置片段，以启用I/O扩展器：

```text
west build -b am62l_evm/am62l3/a53 samples/hello_world -- -S ti-io-exp
```

此配置片段自动通过CONFIG_GPIO=y启用GPIO，并通过CONFIG_GPIO_HOGS=y启用GPIO占用配置（GPIO Hog）支持。

球位E13用于GPIO0_89配置，复用模式为MUX MODE 7，因此不能再通过该padconfig偏移配置与之冲突的SPI0_CLK（MUX MODE 0）、CP_GEMAC_CPTS0_TS_SYN（MUX MODE 1）或EHRPWM1_A（MUX MODE 2）信号。

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此板级配置使用1250 MHz系统时钟。

<a id="ddr-ram"></a>

#### DDR随机存取存储器（DDR RAM）

开发板具有2 GB DDR RAM。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置使用主域（MAIN Domain）的UART `main_uart0`提供单路串行通信通道。

<a id="sd-card"></a>

## SD卡（SD Card）

下载TI官方[WIC](https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/11.02.08.02/tisdk-default-image-am62lxx-evm-11.02.08.02.rootfs.wic.xz)镜像，使用镜像写入软件将WIC文件写入SD卡。

将编译的zephyr.bin复制到SD卡第一个FAT分区，插入开发板，上电后在提示符处停止U-Boot执行。

使用U-Boot加载并启动`zephyr.bin`：

```text
fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

Zephyr应用应开始在A53核上运行。

<a id="debugging"></a>

## 调试（Debugging）

此板配备XDS110 JTAG调试器，使用debug构建目标调试二进制：

```text
west build -b am62l_evm/am62l3/a53 <my_app>
west debug
```

提示（Hint）

此功能需要OpenOCD 0.12或更新版本。软件源可能提供旧版，原文建议[从源码构建OpenOCD](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source)。

<a id="references"></a>

## 参考资料（References）

[https://www.ti.com/tool/TMDS62LEVM](https://www.ti.com/tool/TMDS62LEVM)

## 译注

AM62L通过ti-io-exp配置片段启用J2扩展接口，GPIO0_89复用球位E13，不能同时配置所列SPI／时间同步／PWM信号。此处为A53运行Zephyr，与AM62的M4 remoteproc方式区分。

---

[上一章](P001_TI_AM243x-EVM.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_CC1312R1_LaunchXL.md)
