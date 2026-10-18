---
id: learning.zephyr-docs.boards-ebyte-to-enjoydigital.page-24
title: LiteX VexiiRiscv
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexiiriscv/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="litex_vexiiriscv"></a>

# 第24章\_LiteX VexiiRiscv

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexiiriscv/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`litex_vexiiriscv`

厂商（Vendor）：

[EnjoyDigital](https://docs.zephyrproject.org/latest/boards/index.html#vendor=enjoydigital)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[`litex_vexiiriscv`](https://docs.zephyrproject.org/latest/boards/index.html#soc=litex_vexiiriscv)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/enjoydigital/litex_vexiiriscv/doc/index.rst/../..)警告（Warning）

这个“开发板”不是一块固定硬件，而是由[LiteX SoC Builder](https://github.com/enjoy-digital/litex)生成、随时可能变化的软SoC（Soft SoC）。存储器映射、外设集合、基址及配置都在生成位流时确定，因此使用不同LiteX版本或不同配置构建的SoC，很可能与此开发板随附的设备树不匹配。

所以，树内开发板定义仅是某一种特定配置的快照。只要SoC与其不完全一致，就应使用`litex_json2dts_zephyr.py`为自己的构建生成设备树和Kconfig覆盖文件，见[位流生成（Bitstream Generation）](#bitstream-generation)，不要依赖树内文件。树内文件可能更改，且不保证向后兼容。

LiteX VexiiRiscv是一个由[VexiiRiscv处理器](https://github.com/SpinalHDL/VexiiRiscv)及附加外设组成的SoC示例，可使用[LiteX SoC Builder](https://github.com/enjoy-digital/litex)生成，适用于多种FPGA芯片。可以使用厂商专用工具或开源工具生成位流（Bitstream），即FPGA配置文件。

Zephyr的`litex_vexiiriscv`开发板配置，面向为[Efinix Titanium Ti375 C529开发套件](https://www.efinixinc.com/products-devkits-titaniumti375c529.html)生成的LiteX VexiiRiscv SoC实现。

LiteX基于[Migen](https://m-labs.hk/gateware/migen/)／MiSoC SoC构建器，提供总线、数据流、互连、通用核心及CPU封装（Wrappers）等现成系统组件，便于创建SoC。它支持集成、仿真及构建面向不同厂商芯片的多种设计。更多信息见[LiteX网站](https://github.com/enjoy-digital/litex)。（[MiSoC SoC构建器（Builder）](https://git.m-labs.hk/M-Labs/misoc)）

VexiiRiscv是以[SpinalHDL](https://spinalhdl.github.io/SpinalDoc-RTD/)编写的RISC-V CPU架构实现，针对FPGA芯片优化。更多信息见[VexiiRiscv网站](https://github.com/SpinalHDL/VexiiRiscv)。

要在VexiiRiscv CPU上运行Zephyr OS，需要为Efinix Titanium Ti375 C529开发套件的FPGA准备位流。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`litex_vexiiriscv`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="litex_vexiiriscv-hw-features"></a>

<a id="litex_vexiiriscv-litex_vexiiriscv/litex_vexiiriscv-hw-features-section"></a>

### `litex_vexiiriscv/litex_vexiiriscv`目标（Target）

<a id="litex_vexiiriscv-litex_vexiiriscv/litex_vexiiriscv-hw-features-panel"></a>

<a id="litex_vexiiriscv-litex_vexiiriscv/litex_vexiiriscv-hw-features-memory"></a>

该开发板目标的片上存储容量：1 GiB RAM、N/A Flash。

<a id="litex_vexiiriscv-litex_vexiiriscv/litex_vexiiriscv-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>采用LiteX标准配置的VexiiRiscv内核（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P018_litex_vexiiriscv-standard.md#std-dtcompatible-litex-vexiiriscv-standard"><code>litex,vexiiriscv-standard</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>LiteX LiteEth媒体相关接口管理（MDIO）软件模拟（Bitbang）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L130">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P019_litex_liteeth-mdio.md#std-dtcompatible-litex-liteeth-mdio"><code>litex,liteeth-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L140">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>LiteX以太网（Ethernet）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L147">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P013_litex_liteeth.md#std-dtcompatible-litex-liteeth"><code>litex,liteeth</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L93">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L223">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">RISC-V 架构（RISC-V Architecture）</td>
<td>板载（On-Board）</td>
<td>LiteX SoC控制器驱动（Controller Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L67">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P009_litex_soc-controller.md#std-dtcompatible-litex-soc-controller"><code>litex,soc-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>板载（On-Board）</td>
<td>LiteX LiteSDCard SD主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L233">已启用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P010_litex_mmc.md#std-dtcompatible-litex-mmc"><code>litex,mmc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>LiteX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L105">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P014_litex_uart.md#std-dtcompatible-litex-uart"><code>litex,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>LiteX SPI的LiteSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L188">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P003_litex_spi-litespi.md#std-dtcompatible-litex-spi-litespi"><code>litex,spi-litespi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L78">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>LiteX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/enjoydigital/litex_vexiiriscv/litex_vexiiriscv.dts?plain=1#L380">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P007_litex_watchdog.md#std-dtcompatible-litex-watchdog"><code>litex,watchdog</code></a></td>
</tr>
</table>

<a id="bitstream-generation"></a>

## 位流生成（Bitstream Generation）

使用[官方LiteX仓库](https://github.com/enjoy-digital/litex)生成位流。生成的SoC不一定匹配此开发板随附的设备树，因此应同时生成设备树及Kconfig覆盖文件（Overlays）。


1. 创建并激活虚拟环境（Virtual Environment）：

  ```text
  python3 -m venv .venv
  source .venv/bin/activate
  ```
2. 安装Migen／LiteX及LiteX核心组件：

  ```text
  wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py
  chmod +x litex_setup.py
  ./litex_setup.py --init --install --user (--user to install to user directory) --config=(minimal, standard, full)
  ```
3. 安装RISC-V工具链（Toolchain）：

  ```text
  pip3 install meson ninja
  ./litex_setup.py --gcc=riscv
  ```
4. 构建目标（Target）：

  ```text
  ./litex-boards/litex_boards/targets/efinix_ti375_c529_dev_kit.py --cpu-type=vexiiriscv --build
  ```
5. 生成DTS及配置覆盖文件（Config Overlay）：

  ```text
  ./litex/litex/tools/litex_json2dts_zephyr.py --dts overlay.dts --config overlay.config csr.json
  ```

<a id="programming-and-booting"></a>

## 编程与启动（Programming and Booting）

<a id="building"></a>

### 构建（Building）

`litex_vexiiriscv`配置的应用可按通常方式构建，见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；将`BOARD`设为`litex_vexiiriscv`，并传入针对实际SoC生成的覆盖文件：

```text
west build -b litex_vexiiriscv path/to/app -DDTC_OVERLAY_FILE=path/to/overlay.dts
```

<a id="booting"></a>

### 启动（Booting）

将位流上传到FPGA时，可使用`--load`选项；也可通过`--flash`选项写入SPI闪存。

可以使用`litex_term`从串口启动，将`ttyUSBX`替换为实际设备，例如：

```text
litex_term /dev/ttyUSBX --speed 115200 --kernel zephyr.bin
```

## 译注

此页针对会随位流配置变化的软SoC，树内板定义仅为特定快照。应按实际生成结果同时生成设备树和Kconfig覆盖文件；不将固定地址表视为所有LiteX构建通用。

---

[上一章](P023_EnjoyDigital.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P025_LiteX_VexRiscv.md)
