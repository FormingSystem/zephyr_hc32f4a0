---
id: learning.zephyr-docs.boards-microchip.page-29
title: SAMA7D65 Curiosity Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/sam/sama7d65_curiosity/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sama7d65_curiosity"></a>

# 第29章\_SAMA7D65 Curiosity Kit

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/sam/sama7d65_curiosity/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sama7d65_curiosity.webp](images/sama7d65_curiosity.webp)](images/sama7d65_curiosity.webp)

SAMA7D65 Curiosity Kit

名称（Name）：

`sama7d65_curiosity`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sama7d65](https://docs.zephyrproject.org/latest/boards/index.html#soc=sama7d65)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/sam/sama7d65_curiosity/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EV63J76A，即SAMA7D65 Curiosity Kit，用于评估Microchip SAMA7D65微处理器（MPU）及进行原型开发。SAMA7D65是基于高性能ARM Cortex-A7 CPU的嵌入式MPU，最高运行频率1 GHz。

开发板支持评估用于连接、音频及用户接口应用的外设，包括带二维图形的MIPI-DSI与LVDS、支持时间敏感网络（TSN）的双千兆以太网及CAN-FD。MPU提供防篡改检测（Tamper Detection）、安全启动（Secure Boot）、安全密钥存储、真随机数发生器（TRNG）、物理不可克隆函数（PUF），以及更高性能的AES和SHA密码加速器。

SAMA7D65系列受Microchip MPLAB-X开发工具、Harmony V3、Linux发行版及面向Linux的Microchip Graphic Suite（MGS）支持。它适合工业和汽车应用，图形显示支持最高WXGA／720p。

<a id="hardware"></a>

## 硬件（Hardware）

EV63J76A提供以下硬件组件：


- 处理器（Processor）


  - Microchip SAMA7D65-V/4HB，343球TFBGA SoC，尺寸14×14 mm、间距0.65 mm
- 存储器（Memory）


  - 8 Gb DDR3L，型号AS4C512M16D3LA-10BIN
  - 64 Mb QSPI NOR闪存，带EUI-48，型号Microchip SST26VF064BEUI-104I/MF
  - 4 Gbit SLC NAND闪存，型号MX30LF4G28AD-XKI
  - 2 Kb EEPROM，带EUI-48，型号Microchip 24AA025E48
- SD/MMC


  - 一个4位SD卡插槽
  - 一个M.2无线模块接口，使用SDIO
- 通用串行总线（USB）


  - 一个设备端USB Type-C连接器
  - 两个主机端USB Type-A连接器，使用Microchip MIC2026-1YM
- 以太网（Ethernet）


  - 一个板载10/100/1000 RGMII接口
  - 一个10/100/1000 RGMII SODIMM扩展插槽，使用Microchip LAN8840-V/PSA
- 显示（Display）


  - 一个MIPI-DSI 34引脚FPC连接器
  - 一个LVDS 30引脚FPC连接器
- 调试端口（Debug Port）


  - 一个UART调试连接器
  - 一个JTAG接口
- 用户交互（User Interaction）


  - 一个RGB红绿蓝LED
  - 四个按钮开关
- CAN-FD


  - 三个板载CAN-FD收发器
  - mikroBUS插槽提供其中两个接口
- 扩展（Expansion）


  - Raspberry Pi 40引脚GPIO连接器
  - 两个mikroBUS™连接器
  - 两个PIOBU／系统排针
- 电源管理（Power Management）


  - 电源单元（Power Supply Unit），使用Microchip MCP16502TAB-E/S8B
  - 电源监测（Power Monitoring），使用Microchip PAC1934
  - 子卡电源，使用Microchip MIC23450-AAAYML-TR
  - 后备电源（Backup Power Supply），CR1220电池座
- 开发板供电（Board Supply）


  - 通过USB Type-C提供系统5 V直流电源
  - 通过DC插座提供系统5 V直流电源

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sama7d65_curiosity`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sama7d65_curiosity-hw-features"></a>

<a id="sama7d65_curiosity-sama7d65_curiosity/sama7d65-hw-features-section"></a>

#### `sama7d65_curiosity/sama7d65`目标（Target）

<a id="sama7d65_curiosity-sama7d65_curiosity/sama7d65-hw-features-panel"></a>

<a id="sama7d65_curiosity-sama7d65_curiosity/sama7d65-hw-features-memory"></a>

该开发板目标的片上存储容量：1 GiB RAM、N/A Flash。

<a id="sama7d65_curiosity-sama7d65_curiosity/sama7d65-hw-features-table"></a>

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
<td>Arm Cortex-A7 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P011_arm_cortex-a7.md#std-dtcompatible-arm-cortex-a7"><code>arm,cortex-a7</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>针对Atmel SAM定制的Bosch m_can CAN灵活数据速率控制器（CAN FD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L184">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L170">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P002_atmel_sam-can.md#std-dtcompatible-atmel-sam-can"><code>atmel,sam-can</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L140">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P019_microchip_sam-pmc.md#std-dtcompatible-microchip-sam-pmc"><code>microchip,sam-pmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip SCKC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P020_microchip_sama7g5-sckc.md#std-dtcompatible-microchip-sama7g5-sckc"><code>microchip,sama7g5-sckc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L38">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Microchip PIT64B（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L300">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L310">已禁用：4</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P008_microchip_sam-pit64b-counter.md#std-dtcompatible-microchip-sam-pit64b-counter"><code>microchip,sam-pit64b-counter</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Microchip AES G1加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L240">已启用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P017_microchip_aes-g1.md#std-dtcompatible-microchip-aes-g1"><code>microchip,aes-g1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip G1 SHA控制器驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L247">已禁用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P018_microchip_sha-g1-crypto.md#std-dtcompatible-microchip-sha-g1-crypto"><code>microchip,sha-g1-crypto</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAM以太网控制器（Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L254">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P019_microchip_sam-ethernet-controller.md#std-dtcompatible-microchip-sam-ethernet-controller"><code>microchip,sam-ethernet-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列千兆媒体访问控制器以太网（GMAC Ethernet）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L260">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P004_atmel_sam-gmac.md#std-dtcompatible-atmel-sam-gmac"><code>atmel,sam-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L274">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P016_atmel_sam-mdio.md#std-dtcompatible-atmel-sam-mdio"><code>atmel,sam-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Microchip LAN8840以太网PHY设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L167">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P004_microchip_lan8840.md#std-dtcompatible-microchip-lan8840"><code>microchip,lan8840</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM PIO4 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L88">已启用：5</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P002_microchip_sam-pio4.md#std-dtcompatible-microchip-sam-pio4"><code>microchip,sam-pio4</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1硬件信息（hwinfo）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L697">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P005_microchip_hwinfo-g1.md#std-dtcompatible-microchip-hwinfo-g1"><code>microchip,hwinfo-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列I2C双线接口（TWI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L668">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L338">已禁用：10</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P008_atmel_sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi"><code>atmel,sam-i2c-twi</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L72">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L705">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L83">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>Microchip Flexcom灵活串行通信单元（Flexible Serial Communication Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L540">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L330">已禁用：9</a>）</td>
<td><a href="../hardware/P701_SAM灵活通信接口绑定.md#dtbinding-microchip-sam-flexcom"><code>microchip,sam-flexcom</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L125">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>板载（On-Board）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sama7d65_curiosity/sama7d65_curiosity.dts?plain=1#L134">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAMA7G5引脚控制（Pinctrl）容器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P007_microchip_sama7g5-pinctrl.md#std-dtcompatible-microchip-sama7g5-pinctrl"><code>microchip,sama7g5-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Microchip PWM G1驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L320">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P009_microchip_pwm-g1.md#std-dtcompatible-microchip-pwm-g1"><code>microchip,pwm-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Microchip G2 TRNG熵（Entropy）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L282">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P011_microchip_trng-g2-entropy.md#std-dtcompatible-microchip-trng-g2-entropy"><code>microchip,trng-g2-entropy</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip RTC G2控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L155">已启用：1</a>）</td>
<td><a href="../rtc_binding_reference/P016_microchip_rtc-g2.md#std-dtcompatible-microchip-rtc-g2"><code>microchip,rtc-g2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L560">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L350">已禁用：10</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L165">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAM 64位周期性间隔定时器（PIT64B / Periodic Interval Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L291">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P002_microchip_sam-pit64b.md#std-dtcompatible-microchip-sam-pit64b"><code>microchip,sam-pit64b</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 USB设备高速端口（UDPHS / USB Device High Speed Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L55">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sama7/sama7d6/sama7d6.dtsi?plain=1#L68">已禁用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P017_microchip_udphs-g1-udc.md#std-dtcompatible-microchip-udphs-g1-udc"><code>microchip,udphs-g1-udc</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

SAMA7D65-Curiosity Kit用户指南提供开发板连接详情。（[SAMA7D65-Curiosity Kit用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MPU32/ProductDocuments/UserGuides/SAMA7D65-Curiosity-Kit-User-Guide-DS50003806.pdf)）

<a id="programming"></a>

## 编程（Programming）

<a id="prerequisite"></a>

### 前提条件（Prerequisite）

在SAMA7D65-Curiosity上运行Zephyr之前，必须先运行Microchip MPU的第二阶段引导加载程序（Second Stage Bootloader）[at91bootstrap](https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mpu/at91bootstrap/)。它负责初始化外设及存储器控制器、下载Zephyr并跳转到入口点。

<a id="loading-the-firmware"></a>

### 加载固件（Loading the Firmware）

使用sama7d65_curiositysd1_zephyr_defconfig配置编译引导加载程序后，可将Zephyr二进制文件zephyr.bin复制到SD卡，由引导加载程序在SAMA7D65-Curiosity板上加载运行。

<a id="references"></a>

## 参考资料（References）

SAMA7D65产品页面：

[https://www.microchip.com/en-us/product/sama7d65](https://www.microchip.com/en-us/product/sama7d65)

SAMA7D65 Curiosity Kit页面：

[https://www.microchip.com/en-us/development-tool/EV63J76A](https://www.microchip.com/en-us/development-tool/EV63J76A)

## 译注

必须先运行at91bootstrap，使用sama7d65_curiositysd1_zephyr_defconfig，再从SD卡加载zephyr.bin。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mpu/at91bootstrap/)：The read operation timed out。
- [EV63J76A](https://www.microchip.com/en-us/development-tool/EV63J76A)：HTTP Error 403: Forbidden。
- [sama7d65](https://www.microchip.com/en-us/product/sama7d65)：HTTP Error 403: Forbidden。

---

[上一章](P028_SAMA5D27_SOM1_Kit1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P030_SAMA7G54_Evaluation_Kit.md)
