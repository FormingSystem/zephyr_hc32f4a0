---
id: learning.zephyr-docs.boards-intel-ite.page-9
title: Prepare Linux host
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/common/net_boot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="prepare-linux-host"></a>

# 第9章\_准备Linux主机（Prepare Linux Host）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/common/net_boot.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。


1. 安装DHCP及TFTP服务器，例如dnsmasq。

  ```text
  $ sudo apt-get install dnsmasq
  ```
2. 配置DHCP服务器，dnsmasq配置如下：

  ```text
  # Only listen to this interface
  interface=eno2
  dhcp-range=10.1.1.20,10.1.1.30,12h
  ```
3. 配置TFTP服务器。

  ```text
  # tftp
  enable-tftp
  tftp-root=/srv/tftp
  dhcp-boot=zephyr.efi
  ```

  `zephyr.efi`是前面生成的Zephyr EFI二进制文件。
4. 将Zephyr EFI镜像`zephyr/zephyr.efi`复制到`/srv/tftp`目录。

  > ```text
  > $ cp zephyr/zephyr.efi /srv/tftp
  > ```
5. TFTP根目录应如下所示：

  ```text
  $ tree /srv/tftp
  /srv/tftp
  └── zephyr.efi
  ```
6. 重启dnsmasq服务：

  ```text
  $ sudo systemctl restart dnsmasq.service
  ```

<a id="prepare-the-board-for-network-boot"></a>

# 第9章\_为开发板准备网络启动（Network Boot）


1. 在BIOS设置中启用PXE网络启动。
2. 将网络启动设为第一启动选项。

<a id="booting-the-board"></a>

# 第9章\_启动开发板（Booting the Board）


1. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
2. 给开发板上电。
3. 确认开发板已获得IP地址。在Linux主机运行：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-dhcp[5386]: DHCPDISCOVER(eno2) 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPOFFER(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPREQUEST(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPACK(eno2) 10.1.1.28 00:07:32:52:25:88
  ```
4. 确认网络启动已开始：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-tftp[5386]: sent /srv/tftp/zephyr.efi to 10.1.1.28
  ```
5. 启动过程结束后，Zephyr应用镜像即已启动。

---

[上一章](P008_Preparing_the_Boot_Device.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_Elkhart_Lake_CRB.md)
