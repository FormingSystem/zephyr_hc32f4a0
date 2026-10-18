---
id: learning.zephyr-docs.usb.page-66
title: USB命令行示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_USB命令行示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/shell/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 66.1\_概述（Overview）

本示例启用新版实验性USB设备支持与命令行解释器（Shell）。主要用于辅助开发和测试USB控制器驱动以及新的USB支持。

## 66.2\_构建与烧录（Building and Flashing）

通过 [文件后缀（File Suffixes）](../application/P001_应用开发.md#application-file-suffixes) 选择构建主机栈、设备栈，或两者同时启用；`-DFILE_SUFFIX=<mode>` 选择 `prj_<mode>.conf`。

> 译注：以下为独立构建分支，终端为Bash，位置为读者的Zephyr源码根目录；先具备依赖模块、工具链和所选开发板的烧录工具。更换构建目标或配置时使用独立构建目录，或按west说明重新配置。构建成功后再烧录，烧录完成后通过板的控制台输入后文命令。仅有USB插座不等于控制器支持主机角色。

若板上具有受支持的USB设备控制器（USB Device Controller，UDC），可构建：

```bash
west build -b reel_board samples/subsys/usb/shell -- -DFILE_SUFFIX=device
west flash
```

若板上具有受支持的USB主机控制器（USB Host Controller，UHC），可构建：

```bash
west build -b nrf52840dk/nrf52840 --shield sparkfun_max3421e samples/subsys/usb/shell -- -DFILE_SUFFIX=host
west flash
```

若板上同时具有受支持的USB设备和主机控制器，可构建：

```bash
west build -b nrf52840dk/nrf52840 --shield sparkfun_max3421e samples/subsys/usb/shell -- -DFILE_SUFFIX=device_and_host
west flash
```

理论上，所有平台都可以使用虚拟USB控制器构建USB支持。设备树覆盖文件（Devicetree Overlay）可能需要略作调整，具体取决于平台是否已定义 `zephyr_uhc0` 或 `zephyr_udc0` 节点标签。

```bash
west build -b nrf52840dk/nrf52840 samples/subsys/usb/shell -- -DFILE_SUFFIX=device_and_host -DDTC_OVERLAY_FILE=virtual.overlay
west flash
```

> 译注（源码跟踪）：当前 `virtual.overlay` 先删除已有的 `zephyr_udc0`，再创建虚拟主机控制器及其下的两个虚拟设备控制器，分别声明高速与全速。没有该既有标签的平台须调整删除语句；已定义主机标签的平台也要避免冲突。虚拟设备连接由模型提供，并不证明物理USB控制器、引脚或供电已经工作。

## 66.3\_命令行交互示例（Sample Shell Interaction）

以下为设备控制台交互记录，`uart:~$` 是提示符，不输入到主机终端：

```console
*** Booting Zephyr OS build v4.2.0-1588-g83f1bd7341de ***
uart:~$ usbd defcfg
dev: added default string descriptors
dev: register FS loopback_0
dev: register HS loopback_0
dev: USB initialized
uart:~$ usbh init
host: USB host initialized
uart:~$ usbh enable
host: USB host enabled
uart:~$ usbh bus resume
host: USB bus resumed
uart:~$ usbd enable
dev: USB enabled
[160:04:13.870,000] <inf> usb_loopback: Enable loopback_0
uart:~$ usbh device list
1
uart:~$ usbh device descriptor device 1
host: USB device with address 1
Device Descriptor:
  bLength                        18
  bDescriptorType                 1
  bcdUSB                       2.00
  bDeviceClass                  239
  bDeviceSubClass                 2
  bDeviceProtocol                 1
  bMaxPacketSize0                64
  idVendor                   0x2FE3
  idProduct                  0xFFFF
  bcdDevice                    4.02
  iManufacturer                   1
  iProduct                        2
  iSerial                         3
  bNumConfigurations              1
uart:~$
```

> 译注：`usbd defcfg` 添加默认字符串和配置、注册已编入的类并初始化设备栈；`usbd enable` 才启用设备。主机侧依次初始化、启用并恢复总线，再查询设备列表及描述符。`device` 配置明确启用回环类，但当前 `device_and_host` 配置未显式启用该选项，因此原日志中的 `loopback_0` 取决于最终Kconfig，不能当作每个分支的固定输出。地址1由示例枚举结果得到，实际使用应先查列表。失败时先核对构建分支、最终配置、控制器节点及上一条命令返回结果。

## 66.4\_参阅（See Also）

[USB设备核心API](P015_USB设备核心API.md)。


译注核对来源：[samples/subsys/usb/shell/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/shell/src/main.c)、[samples/subsys/usb/shell/prj_device.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/shell/prj_device.conf)、[samples/subsys/usb/shell/prj_host.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/shell/prj_host.conf)、[samples/subsys/usb/shell/prj_device_and_host.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/shell/prj_device_and_host.conf)、[samples/subsys/usb/shell/virtual.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/shell/virtual.overlay)、[subsys/usb/device_next/usbd_shell.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_shell.c)、[subsys/usb/host/usbh_shell.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_shell.c)。

本仓库的[对应源码](../../../samples/subsys/usb/shell/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-shell"></a>
<a id="overview"></a>
<a id="building-and-flashing"></a>
<a id="sample-shell-interaction"></a>
<a id="see-also"></a>

[上一章](P065_USB示例目录.md) · [返回大纲](大纲.md) · [下一章](P067_USB设备测试示例.md)
