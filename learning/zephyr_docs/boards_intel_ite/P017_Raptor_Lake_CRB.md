---
id: learning.zephyr-docs.boards-intel-ite.page-17
title: Raptor Lake CRB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/rpl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="raptor-lake-crb"></a>

<a id="intel-rpl-crb"></a>

# 第17章\_Raptor Lake客户参考板（CRB）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/rpl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Raptor Lake是第13代64位多核处理器，原文描述为采用10纳米工艺。它采用混合架构（Hybrid Architecture），以P核提供性能、E核提高能效。

支持Raptor Lake S及Raptor Lake P处理器系列。

S系列为双芯片平台，封装中包含处理器裸片及平台控制器集线器PCH-S裸片。S系列支持两个PCH-S版本：600系列ADL及700系列RPL。默认选择600系列，要选择700系列，构建时开发板名称应为`intel_rpl_s_crb@700`。

P系列采用包含两个裸片的多芯片封装（MCP），处理器裸片与平台控制器集线器PCH-P裸片位于同一封装。

Raptor Lake处理器系列、P核及E核的更多信息见[RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/)。

Raptor Lake客户参考板（RPL CRB）是面向物联网边缘设备的高性能紧凑型单板计算机实现示例。支持的开发板为`intel_rpl_s_crb`及`intel_rpl_p_crb`。

这些开发板配置为受支持的Raptor Lake开发板启用内核支持。

<a id="hardware"></a>

## 硬件（Hardware）

开发板一般信息见[RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

除了HPET、本地及I/O APIC等标准架构设备，Zephyr还支持以下Raptor Lake专用SoC设备：


- 系统管理总线（SMBus）

<a id="uart-serial-port-support"></a>

#### UART串口支持（Serial Port Support）

Raptor Lake UART兼容NS16550，uart0支持115.2 kbps波特率。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

更多信息见[RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按以下流程在RPL CRB上启动镜像。

<a id="contents"></a>


- <a id="id1"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id2"></a>

  [使用UEFI启动Raptor Lake S CRB开发板](#booting-the-raptor-lake-s-crb-board-using-uefi)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用。例如，在Raptor Lake S CRB上构建hello_world应用：

  ```text
  # From the root of the zephyr repository
  west build -b intel_rpl_s_crb samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

<a id="booting-the-raptor-lake-s-crb-board-using-uefi"></a>

### [使用UEFI启动Raptor Lake S CRB开发板](#contents)

<a id="preparing-the-boot-device"></a>

#### 准备启动设备（Preparing the Boot Device）

准备一个USB闪存盘，用于在开发板上启动Zephyr应用镜像。


1. 将USB闪存盘格式化为FAT32。

  在Windows中打开文件资源管理器，右键单击USB闪存盘并选择“格式化（Format...）”。确认“文件系统（File System）”选择FAT32，点击“格式化（Format）”按钮，等待完成。

  Linux下可使用gparted等图形工具，将USB闪存盘格式化为FAT32。也可在终端中找出对应设备节点，例如`/dev/sdd`，然后执行以下命令：

  ```text
  $ mkfs.vfat -F 32 <device-node>
  ```

  重要提示（Important）

  必须确认设备节点确实属于该USB闪存盘，否则可能擦除系统中的其他存储设备，导致系统无法使用。
2. 将Zephyr EFI镜像文件`zephyr/zephyr.efi`复制到USB闪存盘。

<a id="booting-zephyr-on-a-board"></a>

#### 在开发板上启动Zephyr（Booting Zephyr）

连接USB闪存盘，将开发板启动到EFI Shell。


1. 将准备好的启动设备，即USB闪存盘，插入开发板。
2. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
3. 给开发板上电。
4. 出现以下输出时，按F7：

  ```text
  Press <DEL> or <ESC> to enter setup.
  ```
5. 在显示的菜单中选择对应EFI Shell的菜单项。
6. 在EFI Shell中选择要启动的Zephyr EFI镜像。

  ```text
  Shell> fs0:zephyr.efi
  ```
7. 启动过程结束后，Zephyr应用镜像即已启动。

---

[上一章](P016_Panther_Lake_H_CRB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_Agilex_5_SoC_FPGA_Development_Kit.md)
