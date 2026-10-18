---
id: learning.zephyr-docs.boards-intel-ite.page-1
title: Alder Lake N
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="alder-lake-n"></a>

<a id="intel-adl-n"></a>

# 第1章\_Alder Lake N

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Alder Lake处理器是采用10纳米工艺的64位多核处理器。

目前支持N系列处理器。这是一种单芯片平台，在同一多芯片封装（MCP / Multi-Chip Package）中包含处理器裸片及Alder Lake N平台控制器集线器（ADL-N PCH）裸片。

原文所述Adler Lake N的拟用品牌为Intel Processor，型号N100、N200，以及Intel Core i3，型号N300、N305。

Alder Lake N客户参考板（ADL-N CRB / Customer Reference Board）及参考验证平台（ADL-N RVP / Reference Validation Platform）是面向物联网边缘设备的高性能紧凑型单板计算机实现示例。

此开发板配置为Alder Lake N开发板启用内核支持。

<a id="hardware"></a>

## 硬件（Hardware）

开发板一般信息见[INTEL_ADL](https://edc.intel.com/content/www/us/en/design/products/platforms/processor-and-core-i3-n-series-datasheet-volume-1-of-2/)网站。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

更多信息见[INTEL_ADL](https://edc.intel.com/content/www/us/en/design/products/platforms/processor-and-core-i3-n-series-datasheet-volume-1-of-2/)网站。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按以下流程在Alder Lake N CRB上启动镜像。

<a id="contents"></a>


- <a id="id1"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id2"></a>

  [使用UEFI启动Alder Lake N CRB开发板](#booting-the-alder-lake-n-crb-board-using-uefi)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用。例如，为Alder Lake N CRB构建hello_world应用：

  ```text
  # From the root of the zephyr repository
  west build -b intel_adl_crb samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

<a id="booting-the-alder-lake-n-crb-board-using-uefi"></a>

### [使用UEFI启动Alder Lake N CRB开发板](#contents)

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

## 译注

原文概述将名称写为Adler Lake N，标题及其余段落使用Alder Lake N；该处拼写已保留。USB格式化会擦除设备，示例设备节点必须按实际USB闪存盘确认。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md)
