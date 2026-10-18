---
id: learning.zephyr-docs.boards-ebyte-to-enjoydigital.page-25
title: LiteX VexRiscv
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexriscv/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="litex_vexriscv"></a>

# 第25章\_LiteX VexRiscv

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexriscv/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/litex_vexriscv.jpg](images/litex_vexriscv.jpg)](images/litex_vexriscv.jpg)

LiteX VexRiscv

名称（Name）：

`litex_vexriscv`

厂商（Vendor）：

[EnjoyDigital](https://docs.zephyrproject.org/latest/boards/index.html#vendor=enjoydigital)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[`litex_vexriscv`](https://docs.zephyrproject.org/latest/boards/index.html#soc=litex_vexriscv)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/enjoydigital/litex_vexriscv/doc/index.rst/../..)LiteX VexRiscv是一个由[VexRiscv处理器](https://github.com/SpinalHDL/VexRiscv)及附加外设组成的SoC示例，可使用[Zephyr on LiteX VexRiscv参考平台](https://github.com/litex-hub/zephyr-on-litex-vexriscv)或[LiteX SoC Builder](https://github.com/enjoy-digital/litex)生成，适用于多种FPGA芯片。可使用厂商专用工具或开源工具生成位流，即FPGA配置文件；开源工具包括F4PGA工具链。（[F4PGA工具链（Toolchain）](https://f4pga.org/)）

Zephyr的`litex_vexriscv`开发板配置，面向为Digilent Arty A7-35T、A7-100T开发板或[SDI-MIPI视频转换器](https://github.com/antmicro/sdi-mipi-video-converter)生成的LiteX VexRiscv SoC实现。（[Digilent Arty A7-35T或A7-100T开发板](https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists)）

LiteX基于[Migen](https://m-labs.hk/gateware/migen/)／MiSoC SoC构建器，提供总线、数据流、互连、通用核心及CPU封装（Wrappers）等现成系统组件，便于创建SoC。它支持集成、仿真及构建面向不同厂商芯片的多种设计。更多信息见[LiteX网站](https://github.com/enjoy-digital/litex)。（[MiSoC SoC构建器（Builder）](https://github.com/m-labs/misoc)）

VexRiscv是以[SpinalHDL](https://spinalhdl.github.io/SpinalDoc-RTD/)编写的32位RISC-V CPU架构实现，支持RISC-V的M、C及A指令集扩展，包含多级流水线、数据缓存等优化。项目提供JTAG、MMU、乘除法（MUL/DIV）等可选扩展，可用于定制设计。该实现针对FPGA芯片优化，更多信息见[VexRiscv网站](https://github.com/SpinalHDL/VexRiscv)。

要在VexRiscv CPU上运行Zephyr OS，需要为Digilent Arty A7-35开发板或SDI-MIPI视频转换器的FPGA准备位流。可使用[Zephyr on LiteX VexRiscv参考平台](https://github.com/litex-hub/zephyr-on-litex-vexriscv)实现，也可使用官方LiteX SoC Builder。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`litex_vexriscv`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="litex_vexriscv-hw-features"></a>

<a id="litex_vexriscv-litex_vexriscv/litex_vexriscv-hw-features-section"></a>

### `litex_vexriscv/litex_vexriscv`目标（Target）

<a id="litex_vexriscv-litex_vexriscv/litex_vexriscv-hw-features-panel"></a>

<a id="litex_vexriscv-litex_vexriscv/litex_vexriscv-hw-features-memory"></a>

该开发板目标的片上存储容量：256 MiB RAM、N/A Flash。

<a id="litex_vexriscv-litex_vexriscv/litex_vexriscv-hw-features-table"></a>

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
<td>采用LiteX所用标准配置（Standard Configuration）的VexRiscv内核（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/riscv32-litex-vexriscv.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P019_litex_vexriscv-standard.md#std-dtcompatible-litex-vexriscv-standard"><code>litex,vexriscv-standard</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>LiteX混合模式时钟管理器（MMCM）时钟输出绑定（Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L453">已启用：2</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P015_litex_clkout.md#std-dtcompatible-litex-clkout"><code>litex,clkout</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>LiteX混合模式时钟管理器通用时钟驱动，带MMCM单元，支持最多七路时钟输出的动态重配置（Dynamic Reconfiguration），可修改频率、占空比及相位偏移（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L482">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P014_litex_clk.md#std-dtcompatible-litex-clk"><code>litex,clk</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>LiteX LiteEth媒体相关接口管理（MDIO）软件模拟（Bitbang）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L115">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P019_litex_liteeth-mdio.md#std-dtcompatible-litex-liteeth-mdio"><code>litex,liteeth-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L127">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>LiteX以太网（Ethernet）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L134">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P013_litex_liteeth.md#std-dtcompatible-litex-liteeth"><code>litex,liteeth</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>LiteX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L371">已启用：2</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P014_litex_gpio.md#std-dtcompatible-litex-gpio"><code>litex,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>板载（On-Board）</td>
<td>LiteX DNA标识读取器（ID Reader）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L173">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P004_litex_dna0.md#std-dtcompatible-litex-dna0"><code>litex,dna0</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>LiteX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L319">已启用：1</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P009_litex_i2c.md#std-dtcompatible-litex-i2c"><code>litex,i2c</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>LiteX LiteI2C I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L331">已启用：1</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P010_litex_litei2c.md#std-dtcompatible-litex-litei2c"><code>litex,litei2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>板载（On-Board）</td>
<td>LiteX I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L401">已启用：2</a>）</td>
<td><a href="../i2s_binding_reference/P009_litex_i2s.md#std-dtcompatible-litex-i2s"><code>litex,i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>LiteX VexRiscV中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/riscv32-litex-vexriscv.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P009_litex_vexriscv-intc0.md#std-dtcompatible-litex-vexriscv-intc0"><code>litex,vexriscv-intc0</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L232">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>板载（On-Board）</td>
<td>LiteX脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L359">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P007_litex_pwm.md#std-dtcompatible-litex-pwm"><code>litex,pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">RISC-V 架构（RISC-V Architecture）</td>
<td>板载（On-Board）</td>
<td>LiteX SoC控制器驱动（Controller Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P009_litex_soc-controller.md#std-dtcompatible-litex-soc-controller"><code>litex,soc-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>板载（On-Board）</td>
<td>LiteX伪随机二进制序列（PRBS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L312">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P009_litex_prbs.md#std-dtcompatible-litex-prbs"><code>litex,prbs</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>板载（On-Board）</td>
<td>LiteX LiteSDCard SD主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L239">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P010_litex_mmc.md#std-dtcompatible-litex-mmc"><code>litex,mmc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>LiteX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P014_litex_uart.md#std-dtcompatible-litex-uart"><code>litex,uart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>LiteX串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L186">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P004_litex_spi.md#std-dtcompatible-litex-spi"><code>litex,spi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>LiteX SPI的LiteSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L205">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P003_litex_spi-litespi.md#std-dtcompatible-litex-spi-litespi"><code>litex,spi-litespi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>LiteX定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L69">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P009_litex_timer0.md#std-dtcompatible-litex-timer0"><code>litex,timer0</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>LiteX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexriscv/litex_vexriscv.dts?plain=1#L96">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P007_litex_watchdog.md#std-dtcompatible-litex-watchdog"><code>litex,watchdog</code></a></td>
</tr>
</table>

<a id="bitstream-generation"></a>

## 位流生成（Bitstream Generation）

<a id="id1"></a>

### Zephyr on LiteX VexRiscv参考平台

使用此平台可确保所有寄存器地址位于正确位置。原文说明全部驱动都已使用该平台测试。按以下步骤生成位流：


1. 克隆仓库并更新全部子模块（Submodules）：

  ```text
  git clone https://github.com/litex-hub/zephyr-on-litex-vexriscv.git
  cd zephyr-on-litex-vexriscv
  git submodule update --init --recursive
  ```

  为Digilent Arty A7-35开发板生成位流需要安装F4PGA工具链，可按[此教程](https://f4pga-examples.readthedocs.io/en/latest/getting.html)操作。

  为SDI-MIPI视频转换器生成位流时，按[这些说明](https://github.com/gatecat/prjoxide#getting-started---complete-flow)安装oxide工具链，即yosys+nextpnr。
2. 然后获取全部必需软件包，并运行安装脚本：

  ```text
  apt-get install build-essential bzip2 python3 python3-dev python3-pip
  ./install.sh
  ```
3. 将LiteX加入路径：

  ```text
  source ./init
  ```
4. 为Digilent Arty A7-35开发板设置F4PGA环境：

  ```text
  export F4PGA_INSTALL_DIR=~/opt/f4pga
  export FPGA_FAM="xc7"
  export PATH="$F4PGA_INSTALL_DIR/$FPGA_FAM/install/bin:$PATH";
  source "$F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh"
  conda activate $FPGA_FAM
  ```
5. 为Arty 35T生成位流：

  ```text
  ./make.py --board=arty --variant=a7-35 --build --toolchain=symbiflow
  ```
6. 为Arty 100T生成位流：

  ```text
  ./make.py --board=arty --variant=a7-100 --build --toolchain=symbiflow
  ```
7. 为SDI-MIPI视频转换器生成位流：

  ```text
  ./make.py --board=sdi_mipi_bridge --build --toolchain=oxide
  ```

<a id="official-litex-soc-builder"></a>

### 官方LiteX SoC构建器（Official LiteX SoC Builder）

也可使用[官方LiteX仓库](https://github.com/enjoy-digital/litex)生成位流；这种情况下还必须生成DTS覆盖文件。


1. 安装Migen／LiteX及LiteX核心组件：

  ```text
  wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py
  chmod +x litex_setup.py
  ./litex_setup.py --init --install --user (--user to install to user directory) --config=(minimal, standard, full)
  ```
2. 安装RISC-V工具链（Toolchain）：

  ```text
  pip3 install meson ninja
  ./litex_setup.py --gcc=riscv
  ```
3. 构建目标（Target）：

  ```text
  ./litex-boards/litex_boards/targets/digilent_arty.py --build --timer-uptime --csr-json csr.json
  ```
4. 生成DTS及配置覆盖文件（Config Overlay）：

  ```text
  ./litex/litex/tools/litex_json2dts_zephyr.py --dts overlay.dts --config overlay.config csr.json
  ```

<a id="programming-and-booting"></a>

## 编程与启动（Programming and Booting）

<a id="building"></a>

### 构建（Building）

`litex_vexriscv`配置的应用可按通常方式构建，见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)。为其构建应用时，将`BOARD`变量设为`litex_vexriscv`。

如果使用官方LiteX SoC Builder生成位流，需要额外传入以下参数：

```text
west build -b litex_vexriscv path/to/app -DDTC_OVERLAY_FILE=path/to/overlay.dts
```

<a id="booting"></a>

### 启动（Booting）

可使用[xc3sprog](https://github.com/matrix-io/xc3sprog)或[openFPGALoader](https://github.com/trabucayre/openFPGALoader)将位流上传到Digilent Arty A7-35：

```text
xc3sprog -c nexys4 digilent_arty.bit
```

```text
openFPGALoader -b arty_a7_100t digilent_arty.bit
```

使用[ecpprog](https://github.com/gregdavill/ecpprog)将位流上传到SDI-MIPI视频转换器：

```text
ecpprog -S antmicro_sdi_mipi_video_converter.bit
```

可以使用`litex_term`从串口启动，将`ttyUSBX`替换为实际设备，例如：

```text
litex_term /dev/ttyUSBX --speed 115200 --kernel zephyr.bin
```

## 译注

参考平台与官方LiteX SoC Builder是两条不同生成路线；使用后者时需额外传入生成的DTS覆盖文件。Arty 35T／100T及SDI-MIPI转换器对应的位流与下载工具分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [prjoxide](https://github.com/gatecat/prjoxide#getting-started---complete-flow)：页面可访问，但未确认目标片段。
- [arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists](https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists)：HTTP Error 403: Forbidden。

---

[上一章](P024_LiteX_VexiiRiscv.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
