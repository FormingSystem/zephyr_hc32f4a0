---
id: learning.zephyr-docs.boards-waveshare-tail.page-54
title: Orange Pi 5 Ultra RK3588
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/xunlong/orangepi_5_ultra_rk3588/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="orangepi_5_ultra_rk3588"></a>

# 第54章\_Orange Pi 5 Ultra RK3588

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/xunlong/orangepi_5_ultra_rk3588/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`orangepi_5_ultra_rk3588`

厂商（Vendor）：

[深圳迅龙软件有限公司（Shenzhen Xunlong Software CO.,Limited）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=xunlong)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[rk3588](https://docs.zephyrproject.org/latest/boards/index.html#soc=rk3588)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/xunlong/orangepi_5_ultra_rk3588/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Orange Pi 5 Ultra采用瑞芯微（Rockchip）RK3588八核64位ARM处理器，包含四核A76及四核A55，以三星8 nm LP工艺制造，大核最高2.4 GHz。集成ARM Mali-G610 MP4 GPU、高性能三维／二维图像加速模块及最高6 TOPS的AI神经网络处理器（NPU），配备4／8／16 GB LPDDR5，支持最高8K显示处理。

Orange Pi 5 Ultra提供HDMI输入输出、Wi-Fi 6、M.2 M-key PCIe 3.0×4、2.5 Gbit/s网口、USB 2.0、USB 3.1及40针扩展排针等接口，面向高端平板、边缘计算、人工智能、云计算、AR／VR、智能安防、智能家居等AIoT应用。

支持Orange Pi官方Orange Pi OS，以及Android 13、Debian 11／12、Ubuntu 20.04／22.04等系统；版本列表按原文保留。

<a id="hardware"></a>

## 硬件（Hardware）


- 硬件功能（Hardware Features）：


  - 处理器（CPU）：


    - Rockchip RK3588，8 nm LP工艺
    - 八核64位处理器
    - 四核Cortex-A76与四核Cortex-A55大小核架构
    - 大核最高2.4 GHz，小核最高1.8 GHz
  - 图形处理器（GPU）：


    - 集成ARM Mali-G610图形处理器
    - OpenGL ES 1.1／2.0／3.2、OpenCL 2.2及Vulkan 1.2
  - 神经网络处理器（NPU）：


    - 内置AI NPU，最高6 TOPS
    - 支持INT4／INT8／INT16混合运算
  - 视频（Video）：


    - 1路HDMI 2.1，最高8K、60 Hz
    - 1路HDMI输入，最高4K、60帧/秒
    - 1路四通道MIPI D-PHY发送（TX）
  - 存储器（Memory）：


    - 4 GB／8 GB／16 GB LPDDR5内存
  - 摄像头（Camera）：


    - 2路四通道MIPI CSI
    - 1路四通道MIPI D-PHY接收（RX）
  - 电源管理单元（PMU）：


    - RK806-1
  - 板载存储（Onboard Storage）：


    - eMMC插座，可连接外部eMMC模块
    - 16 MB QSPI NOR闪存
    - MicroSD／TF卡槽
    - PCIe 3.0×4 M.2 M-KEY固态盘（SSD）插槽
  - 以太网（Ethernet）：


    - 1路PCIe 2.5 Gbit/s以太网，RTL8125BG
  - Wi-Fi及蓝牙（Bluetooth）：


    - 板载AP6611 Wi-Fi 6E及Bluetooth 5.3／BLE模块
    - Wi-Fi接口：SDIO 3.0
    - Bluetooth接口：UART／PCM
  - 音频（Audio）：


    - 3.5 mm耳机插孔，音频输入输出
    - 板载麦克风输入
    - 2路HDMI输出；原文此处与前文单路HDMI输出数量不同
  - PCIe M.2 M-KEY：


    - PCIe 3.0，4通道，用于NVMe SSD
  - USB接口：


    - 1路USB 3.0，支持设备或主机模式
    - 1路USB 3.0主机
    - 2路USB 2.0主机
  - 40针扩展排针：

    扩展UART、PWM、I2C、SPI、CAN及GPIO
  - 调试串口：

    包含在40针扩展口内
  - LED指示灯：

    RGB三色LED指示灯
  - 按键（Button）：


    - 1个MaskROM按键
    - 1个电源按键
  - 供电：

    Type-C接口，5 V／5 A

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`orangepi_5_ultra_rk3588`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="orangepi_5_ultra_rk3588-hw-features"></a>

<a id="orangepi_5_ultra_rk3588-orangepi_5_ultra_rk3588/rk3588-hw-features-section"></a>

#### `orangepi_5_ultra_rk3588/rk3588`目标（Target）

<a id="orangepi_5_ultra_rk3588-orangepi_5_ultra_rk3588/rk3588-hw-features-panel"></a>

<a id="orangepi_5_ultra_rk3588-orangepi_5_ultra_rk3588/rk3588-hw-features-memory"></a>

该开发板目标的片上存储容量：1 GiB RAM、N/A Flash。

<a id="orangepi_5_ultra_rk3588-orangepi_5_ultra_rk3588/rk3588-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L52">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588时钟复位单元（CRU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L118">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P023_rockchip_rk3588-cru.md#std-dtcompatible-rockchip-rk3588-cru"><code>rockchip,rk3588-cru</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P022_rockchip_rk3588-cru-clk.md#std-dtcompatible-rockchip-rk3588-cru-clk"><code>rockchip,rk3588-cru-clk</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588千兆以太网媒体访问控制器（GMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L154">已禁用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac"><code>rockchip,rk3588-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L173">已禁用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L180">已禁用：2</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P015_rockchip_rk3588-cru-rst.md#std-dtcompatible-rockchip-rk3588-cru-rst"><code>rockchip,rk3588-cru-rst</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L136">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L145">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xunlong/orangepi_5_ultra_rk3588/orangepi_5_ultra_rk3588.dts?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L106">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

开发板具有多个串口，Zephyr使用uart2作为串行控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`orangepi_5_ultra_rk3588`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

可使用此配置运行基本Zephyr应用及内核测试，例如[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)：

```text
# From the root of the zephyr repository
west build -b orangepi_5_ultra_rk3588 samples/hello_world
```

这会构建包含hello_world示例应用的镜像。

构建Zephyr镜像：

```text
mkimage -C none -A arm64 -O linux -a 0x10000000 -e 0x10000000 -d build/zephyr/zephyr.bin build/zephyr/zephyr.img
```

向板卡写入镜像：

```text
dd bs=1M if=/dev/zero of=/dev/mmcblk1 count=1000 status=progress
dd bs=1M if=zephyr.img of=/dev/mmcblk1 status=progress
```

使用U-Boot加载并运行Zephyr：

```text
mmc dev 1
mmc read 0x10000000 0x0 0x10000
bootm start 0x10000000
bootm loados
bootm go
```

0x10000是镜像大小，以扇区数计，必要时增大。

控制台应显示以下输出：

```text
*** Booting Zephyr OS build v4.2.0-455-gddc43f0d353d ***
Hello World! orangepi_5_ultra_rk3588/rk3588
```

<a id="flashing"></a>

### 烧录（Flashing）

可通过U-Boot从SD卡、eMMC、QSPI闪存或网络将Zephyr镜像加载到DDR地址0x10000000。

<a id="references"></a>

### 参考资料（References）

更多信息见Orange Pi官方网站。（[Orange Pi网站](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Ultra.html)）

## 译注

Orange Pi 5 Ultra原文HDMI输出数量及USB版本列表存在差异，分别保留。U-Boot中0x10000镜像长度单位为扇区数，DDR加载地址为0x10000000。

---

[上一章](P053_Orange_Pi_Zero_2W.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
