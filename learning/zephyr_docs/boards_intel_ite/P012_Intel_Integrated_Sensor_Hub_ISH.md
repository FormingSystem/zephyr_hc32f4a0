---
id: learning.zephyr-docs.boards-intel-ite.page-12
title: Intel Integrated Sensor Hub ISH
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/ish/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel-integrated-sensor-hub-ish"></a>

<a id="intel-ish"></a>

# 第12章\_Intel集成传感器集线器（ISH / Integrated Sensor Hub）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/ish/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Intel集成传感器集线器（ISH）是多款Intel处理器内的低功耗、始终开启（Always-On）协处理器，可从主处理器卸载传感器处理任务，从而降低功耗。

<a id="hardware"></a>

## 硬件（Hardware）


- LMT MinuteIA内核：


  - 16 KB指令缓存及16 KB数据缓存。
  - 640 KB SRAM供代码及数据使用，以L2 SRAM实现。
  - 8 KB常开寄存器文件（AON RF）空间，用于在深度D0i2／D0i3电源门控（PG）状态保持代码。
- 连接传感器的外设接口：I2C、SPI、UART、I3C、GPIO及DMA。
- 与主处理器及其他IP处理器进行进程间通信（IPC / Inter Process Communications）。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

除了HPET、本地及I/O APIC等标准架构设备，Zephyr还支持以下ISH专用SoC设备：


- 高速UART（HSUART）

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按以下流程，在面向Chrome的ADL RVP开发板上启动ISH镜像。

<a id="contents"></a>


- <a id="id1"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id2"></a>

  [在面向Chrome的ADL RVP开发板上运行ish_fw.bin](#run-ish-fw-bin-on-adl-rvp-board-for-chrome)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用。例如，为Intel ADL处理器上的ISH 5.4.1构建hello_world应用：

  ```text
  # From the root of the zephyr repository
  west build -b intel_ish_5_4_1 samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录会自动生成名为`ish_fw.bin`的Zephyr镜像文件。

<a id="run-ish-fw-bin-on-adl-rvp-board-for-chrome"></a>

### [在面向Chrome的ADL RVP开发板上运行ish_fw.bin](#contents)


- 给ADL RVP开发板上电。
- 登录Chrome OS。用户必须具有root访问权限，详见[开发者模式（Developer Mode）](https://chromium.googlesource.com/chromiumos/docs/+/HEAD/developer_mode.md)。
- 将根文件系统重新挂载为可读写：

```text
$ mount -o remount,rw /
```


- 若重新挂载失败，执行以下命令移除根文件系统验证（Rootfs Verification）：

```text
$ /usr/share/vboot/bin/make_dev_ssd.sh --remove_rootfs_verification --partitions
$ reboot
```


- 进入ISH固件目录：

```text
$ cd /lib/firmware/intel
```


- 用构建得到的Zephyr镜像`ish_fw.bin`替换`adlrvp_ish.bin`。
- 重启后，通过ISH UART0观察Zephyr日志输出。

## 译注

原文IPC展开为Inter Process Communications，译文保留这一名称。移除rootfs验证、替换固件及重新挂载步骤均为官方原文操作，不代表已执行。

---

[上一章](P011_Intel_Corporation.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_INTEL_FPGA_niosv_g.md)
