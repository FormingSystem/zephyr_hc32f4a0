---
id: learning.zephyr-docs.boards-phytec.page-5
title: phyBOARD-Lyra AM62x M4F Core
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_m4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="phyboard-lyra-am62x-m4f-core"></a>

<a id="phyboard-lyra-am62xx-m4"></a>

# 第5章\_phyBOARD-Lyra AM62x M4F核

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_m4.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

phyBOARD-Lyra AM62x配置供运行于TI AM62x平台的Zephyr应用使用，支持Arm Cortex-M4F MCU核及以下功能：


- 嵌套向量中断控制器（NVIC）
- 系统滴答系统时钟（SYSTICK / System Tick System Clock）

此板配置也启用半主机（Semihosting）调试控制台。

详情见[PHYTEC AM62x产品页](https://www.phytec.com/product/phycore-am62x/)。

<a id="id1"></a>

![官方原图：phyBOARD-Lyra AM62x](images/phyCORE-AM62x_Lyra_frontside.webp)

搭载phyCORE-AM62x SoM的PHYTEC phyBOARD-Lyra

<a id="hardware"></a>

## 硬件（Hardware）

phyBOARD-Lyra AM62x套件采用AM62x SoC，包含一个四Cortex-A53集群及MCU域中的单Cortex-M4核。此页Zephyr移植运行于M4F，使用以下硬件：


- 低功耗Arm Cortex-M4F
- 存储器（Memory）

  > - 256 KB SRAM
  > - 2 GB DDR4
- 调试（Debug）

  > - 基于XDS110的JTAG

<a id="supported-features"></a>

### 支持的功能（Supported Features）

phyboard_lyra/am6234/m4配置支持以下硬件功能：

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>嵌套向量中断控制器（NVIC）</td>
<td>片上（On-Chip）</td>
<td>嵌套向量中断控制器（Nested Vectored Interrupt Controller）。</td>
</tr>
<tr>
<td>系统节拍（SYSTICK）</td>
<td>片上（On-Chip）</td>
<td>systick</td>
</tr>
<tr>
<td>引脚控制（PINCTRL）</td>
<td>片上（On-Chip）</td>
<td>pinctrl</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>片上（On-Chip）</td>
<td>串行接口（Serial）</td>
</tr>
<tr>
<td>邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>核间通信邮箱（IPC Mailbox）</td>
</tr>
</table>

此移植目前不支持其他硬件功能。

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此开发板配置使用400 MHz系统时钟。

<a id="ddr-ram"></a>

#### DDR随机存取存储器（DDR RAM）

此板有2 GB DDR RAM。原文称为Zephyr分配4 KB RAM，仅用于资源表，并给出范围0x9CC00000至0x9CC00400；该范围实际跨度为1 KiB，容量与地址均按原文保留。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置使用MCU域UART，即MCU_UART0，作为唯一串行通信通道。

<a id="sd-card"></a>

## SD卡（SD Card）

下载PHYTEC官方[WIC](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.xz)镜像及[BMAP](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.bmap)文件，使用镜像写入软件将WIC写入SD卡。SoM的A53应用核将启动Linux，再通过remoteproc将Zephyr二进制加载到M4。

默认配置位于[boards/phytec/phyboard_lyra/phyboard_lyra_am6234_m4_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_lyra/phyboard_lyra_am6234_m4_defconfig)。

<a id="flashing"></a>

## 烧录（Flashing）

A53上的Linux通过远程处理器框架（Remoteproc）管理M4F协处理器。因此测试时需先将二进制复制到SD卡，使A53启动时可通过remoteproc加载。

测试M4F内核时，使用以下命令构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例。

```text
# From the root of the Zephyr repository
west build -p -b phyboard_lyra/am6234/m4 samples/hello_world
```

构建生成的二进制文件名为`zephyr.elf`，位于`build/zephyr`目录。

将该文件复制到SD卡上的`/lib/firmware`系统目录，并命名为`am62-mcu-m4f0_0-fw`。

```text
# Mount the SD card at sdcard for example
sudo mount /dev/sdX sdcard
# copy the elf to the /lib/firmware directory
sudo cp --remove-destination zephyr.elf sdcard/lib/firmware/am62-mcu-m4f0_0-fw
```

随后可用SD卡启动系统，启动时二进制程序会被加载到M4F内核。

将启动引脚设为SD卡模式以从SD卡启动，参见[phyBOARD SD卡启动要点](https://docs.phytec.com/projects/yocto-phycore-am62x/en/bsp-yocto-ampliphy-am62x-pd23.2.1/bootingessentials/sdcard.html)。

修改启动模式后，在U-Boot中停下，以启用M4F协处理器。

```text
setenv overlays k3-am62-phyboard-lyra-rpmsg.dtbo
# Save the overlays variable permanently
saveenv
boot
```

开发板应启动Linux，随后二进制运行并向MCU_UART0输出Hello world。

<a id="debugging"></a>

## 调试（Debugging）

此板配备XDS110 JTAG调试器，使用debug构建目标调试二进制：

```text
west build -b phyboard_lyra/am6234/m4 <my_app>
west debug
```

提示（Hint）

此功能需要OpenOCD 0.12或更新版本。软件源可能提供旧版，原文建议[从源码构建OpenOCD](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source)。

## 译注

Lyra M4F由A53加载，需在U-Boot启用协处理器。原文资源表4 KB与0x9CC00000至0x9CC00400的1 KiB跨度不一致，已注明；XDS110调试要求OpenOCD 0.12或更新。

---

[上一章](P004_phyBOARD-Lyra_AM62x_A53_Core.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_phyBOARD-Nash_i.MX93.md)
