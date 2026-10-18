---
id: learning.zephyr-docs.boards-intel-ite.page-8
title: Preparing the Boot Device
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/common/efi_boot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="preparing-the-boot-device"></a>

# 第8章\_准备启动设备（Preparing the Boot Device）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/common/efi_boot.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

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

# 第8章\_在开发板上启动Zephyr（Booting Zephyr）

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

格式化命令中的设备节点是示例，原文要求核对实际USB设备，避免擦除其他存储。

---

[上一章](P007_Bartlett_Lake_P_CRB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_Prepare_Linux_host.md)
