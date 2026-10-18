---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-30
title: RZ G3E Evaluation Board Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/rzg3e_smarc/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rzg3e_smarc"></a>

# 第30章\_RZ/G3E评估板套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/rzg3e_smarc/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rzg3e_smarc.webp](images/rzg3e_smarc.webp)](images/rzg3e_smarc.webp)

RZ/G3E评估板套件

名称（Name）：

`rzg3e_smarc`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[r9a09g047e57gbg](https://docs.zephyrproject.org/latest/boards/index.html#soc=r9a09g047e57gbg)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzg3e_smarc/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

瑞萨RZ/G3E评估板套件RZ/G3E-EVKIT由SMARC v2.1模块板及载板组成。


- 器件：RZ/G3E R9A09G047E57GBG


  - 4个Cortex-A55及1个Cortex-M33
  - 529引脚FCBGA，15 mm方形本体，0.5 mm间距
- SMARC v2.1模块板功能


  - LPDDR4X SDRAM：4 GB×1颗
  - QSPI闪存：16 MB×1颗
  - eMMC：64 GB×1颗
  - 配备电源管理集成电路（PMIC）RAA215300A2GNP#HA8
  - 2个microSD插槽
  - 并行接口
  - I3C连接器
  - JTAG连接器
  - 8通道ADC
  - 电流监测，USB Micro-B
- 载板功能（Carrier Board Functions）


  - 2个千兆以太网接口
  - USB 2.0：原文写2通道，同时括注1通道OTG、2通道Host，数量不一致，保留并提示核对
  - USB 3.2：1通道，主机1通道
  - 2个CAN-FD接口
  - MIPI CSI-2摄像头接口
  - 经MIPI-DS连接的Micro-HDMI；原文接口名写MIPI-DS
  - 2个低压差分信号（LVDS）接口
  - microSD插槽
  - 单声道扬声器、立体声耳机、麦克风及辅助音频接口
  - 3个Pmod接口，Type 3A与Type 6A互斥
  - PCIe Gen3四通道插槽，G3E仅支持两通道；M.2 Key E接口
  - M.2 Key B接口及SIM卡槽
  - USB Type-C电源输入

<a id="hardware"></a>

## 硬件（Hardware）

板卡详细硬件功能见：


- <a id="id3"></a>

  [RZ/G3E组网站](https://www.renesas.com/en/products/rz-g3e)[注1](#id2)
- <a id="id5"></a>

  [RZ/G3E-EVKIT网站](https://www.renesas.com/en/design-resources/boards-kits/rz-g3e-evkit)[注2](#id4)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rzg3e_smarc`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rzg3e_smarc-hw-features"></a>

<a id="rzg3e_smarc-rzg3e_smarc/r9a09g047e57gbg/cm33-hw-features-section"></a>

#### `rzg3e_smarc/r9a09g047e57gbg/cm33`目标（Target）

<a id="rzg3e_smarc-rzg3e_smarc/r9a09g047e57gbg/cm33-hw-features-panel"></a>

<a id="rzg3e_smarc-rzg3e_smarc/r9a09g047e57gbg/cm33-hw-features-memory"></a>

此开发板目标的存储器：245 KiB RAM；闪存容量不适用（N/A）。

<a id="rzg3e_smarc-rzg3e_smarc/r9a09g047e57gbg/cm33-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ GPIO公共部分（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P022_renesas_rz-gpio-common.md#std-dtcompatible-renesas-rz-gpio-common"><code>renesas,rz-gpio-common</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L76">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L49">已禁用：20</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P025_renesas_rz-gpio.md#std-dtcompatible-renesas-rz-gpio"><code>renesas,rz-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg3e_smarc/rzg3e_smarc_r9a09g047e57gbg_cm33.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L248">已启用：1</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P007_renesas_rz-intc-v2.md#std-dtcompatible-renesas-rz-intc-v2"><code>renesas,rz-intc-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ GPIO中断（TINT）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L263">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L272">已禁用：31</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P009_renesas_rz-tint.md#std-dtcompatible-renesas-rz-tint"><code>renesas,rz-tint</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ SCI-B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L612">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L552">已禁用：9</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P028_renesas_rz-sci-b.md#std-dtcompatible-renesas-rz-sci-b"><code>renesas,rz-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ/G引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P015_renesas_rzg-pinctrl.md#std-dtcompatible-renesas-rzg-pinctrl"><code>renesas,rzg-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ SCI-B UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L620">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a09g047.dtsi?plain=1#L560">已禁用：9</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P014_renesas_rz-sci-b-uart.md#std-dtcompatible-renesas-rz-sci-b-uart"><code>renesas,rz-sci-b-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg3e_smarc/rzg3e_smarc_r9a09g047e57gbg_cm33.dts?plain=1#L53">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rzg3e_smarc`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

rzg3e_smarc应用可按“构建应用”中的常规方式构建。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

<a id="console"></a>

### 控制台（Console）

将[Pmod USBUART](https://store.digilentinc.com/pmod-usbuart-usb-to-uart-interface/)连接到PMOD1_3A上侧，即可访问Cortex-M33系统核的UART端口。

<a id="debugging"></a>

### 调试（Debugging）

可使用J-Link调试器及[J-Link Debug Host Tools](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)，将Zephyr应用二进制加载到此板内部SRAM，并在Cortex-M33系统核上执行。

以下为构建并调试[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例。

```text
# From the root of the zephyr repository
west build -b rzg3e_smarc/r9a09g047e57gbg/cm33 samples/hello_world
west debug
```

<a id="flashing"></a>

### 烧录（Flashing）

RZ/G3E-EVKIT设计为在不同内核运行不同系统。它使用Yocto构建Linux及引导加载程序，并通过U-Boot在Cortex-M33上运行Zephyr，最少步骤如下。


1. <a id="id7"></a>

  按《[RZ/G3E-EVKIT Linux启动指南](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)》[注3](#id6)的“2.1 Building Images”准备构建环境。
2. <a id="id13"></a>

  在步骤5，按《RZ/G3E Multi-OS Package快速入门指南》[注4](#id12)的“3.2 Integration of OpenAMP related stuff”，执行“2. Download Multi-OS Package”及“3. Add the layer for Multi-OS Package”，添加多操作系统软件包构建层。（[RZ/G3E多操作系统软件包快速入门指南](https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3e-multi-os-package)）

```text
$ cd ~/rzg_vlp_<pkg ver>
$ unzip <Multi-OS Dir>/r01an5869ej0300-rzg-multi-os-pkg.zip
$ tar zxvf r01an5869ej0300-rzg-multi-os-pkg/meta-rz-features_multi-os_v3.0.0.tar.gz
$ cd build
$ bitbake-layers add-layer ../meta-rz-features/meta-rz-multi-os/meta-rzg3e
```


1. 开始构建：

```text
$ MACHINE=smarc-rzg3e bitbake core-image-minimal
```

下列必需产物位于build/tmp/deploy/images：

<table>
<tr>
<th>构建产物（Artifacts）</th>
<th>文件名</th>
</tr>
<tr>
<td>引导加载程序（Boot Loader）</td>
<td>bl2_bp_spi-smarc-rzg3e.srec<br><br>fip-smarc-rzg3e.srec</td>
</tr>
<tr>
<td>闪存写入工具（Flash Writer）</td>
<td>Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot</td>
</tr>
<tr>
<td>SD卡镜像</td>
<td>core-image-minimal-smarc-rzg3e.rootfs.wic.gz<br><br>core-image-minimal-smarc-rzg3e.rootfs.wic.bmap</td>
</tr>
</table>


1. <a id="id8"></a>

  按《[RZ/G3E-EVKIT Linux启动指南](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)》[注3](#id6)的“4.4 Startup Procedure for RZ/G3E”配置电源及板卡。SCIF下载：SW_MODE[1:4]依次OFF、ON、OFF、ON；Cortex-A55冷启动：BOOT[1:6]依次OFF、OFF、ON、OFF、OFF、OFF。
2. <a id="id9"></a>

  按该Linux启动指南[注3](#id6)的“4.5 Download Flash Writer to RAM”，将Flash Writer下载到RAM。（[RZ/G3E-EVKIT Linux启动指南](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)）
3. <a id="id10"></a>

  按该Linux启动指南[注3](#id6)的“4.6 Write the Bootloader”，使用Flash Writer将引导加载程序写入目标板。（[RZ/G3E-EVKIT Linux启动指南](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)）
4. 按“4.7 Change Boot Mode and set U-Boot variables”更改启动模式及U-Boot变量，SW_MODE[1:4]依次设为OFF、OFF、OFF、ON。
5. <a id="id11"></a>

  按该Linux启动指南[注3](#id6)的“3. Preparing the SD Card”，将文件写入microSD卡。（[RZ/G3E-EVKIT Linux启动指南](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)）
6. 运行以下命令将zephyr.bin写入SD卡。

```text
$ sudo mkdir /mnt/sd -p
$ sudo mount /dev/sdb2 /mnt/sd
$ sudo cp /path/to/zephyr.bin /mnt/sd/boot
$ sync
$ sudo umount /mnt/sd
```

警告（Warning）

将命令中的/dev/sdb替换为实际microSD卡设备名。原文建议使用dh -h检查；该命令拼写有疑点，此处保留提示。


1. <a id="id14"></a>

  按《RZ/G3E Multi-OS Package快速入门指南》[注4](#id12)的“4.3.2 CM33 Sample Program Invocation from u-boot”，执行步骤2至4。（[RZ/G3E多操作系统软件包快速入门指南](https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3e-multi-os-package)）
2. 在控制台执行以下命令，以CM33内核启动Zephyr应用。

```text
=> setenv cm33start 'dcache off
=> mw.l 0x10420D2C 0x02000000
=> mw.l 0x1043080c 0x08003000
=> mw.l 0x10430810 0x18003000
=> mw.l 0x10420604 0x00040004
=> mw.l 0x10420C1C 0x00003100
=> mw.l 0x10420C0C 0x00000001
=> mw.l 0x10420904 0x00380008
=> mw.l 0x10420904 0x00380038
=> ext4load mmc 1:2 0x08003000 boot/zephyr.bin
=> mw.l 0x10420C0C 0x00000000
=> dcache on'
=> saveenv
=> run cm33start
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.renesas.com/en/products/rz-g3e](https://www.renesas.com/en/products/rz-g3e)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.renesas.com/en/design-resources/boards-kits/rz-g3e-evkit](https://www.renesas.com/en/design-resources/boards-kits/rz-g3e-evkit)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id8),[3](#id9),[4](#id10),[5](#id11)) [https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100](https://www.renesas.com/en/document/gde/rzg3e-linux-start-guide-rev100)

<a id="id12"></a>

〔4〕 ([1](#id13),[2](#id14)) [https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3e-multi-os-package](https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3e-multi-os-package)

## 译注

RZ/G3E的USB 2.0总数与括号分项数量不一致，MIPI-DS及dh -h也保留并注明原文疑点。PCIe插槽有四通道外形，但SoC仅支持两通道。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://store.digilentinc.com/pmod-usbuart-usb-to-uart-interface/)：HTTP Error 403: Forbidden。
- [quick-start-guide-rzg3e-multi-os-package](https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3e-multi-os-package)：HTTP Error 429: Too Many Requests。
- [rz-g3e](https://www.renesas.com/en/products/rz-g3e)：HTTP Error 429: Too Many Requests。

---

[上一章](P029_RZ_G2UL_SMARC_Evaluation_Board_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P031_RZ_G3S_SMARC_Evaluation_Board_Kit.md)
