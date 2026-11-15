---
id: learning.zephyr-docs.usb.page-67
title: USB设备测试示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/testusb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_USB设备测试示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/testusb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 67.1\_USB设备测试应用（USB Device Testing Application）

本示例实现回环（Loopback）功能，用于在连接Linux主机时测试USB设备驱动和设备栈。它的接口类似Linux内核的“Gadget Zero”，需要用户空间工具 `testusb` 启动测试。

## 67.2\_构建与烧录（Building and Flashing）

遵循Zephyr设备的一般构建和烧录流程。

> 译注：应用源码位于 `samples/subsys/usb/testusb`。构建在读者的Zephyr源码根进行，依赖目标板的USB设备支持及工具链；以下测试步骤则在Linux主机终端执行。当前配置启用新版设备栈和回环类，PID为 `0x0009`。设备固件准备完毕后，Linux主机还需可用的 `usbtest` 内核模块及已构建的 `testusb` 工具；固件构建成功不等于主机测试已通过。

## 67.3\_测试（Testing）

### 67.3.1\_加载Linux内核模块

在Linux主机加载 `usbtest`：

```bash
$ sudo modprobe usbtest vendor=0x2fe3 product=0x0009
```

查看内核诊断消息，应看到 `usbtest` 已接管设备：

```console
[21746.128743] usb 9-1: new full-speed USB device number 16 using uhci_hcd
[21746.303051] usb 9-1: New USB device found, idVendor=2fe3, idProduct=0009, bcdDevice= 2.03
[21746.303055] usb 9-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[21746.303058] usb 9-1: Product: Zephyr testusb sample
[21746.303060] usb 9-1: Manufacturer: ZEPHYR
[21746.303063] usb 9-1: SerialNumber: 86FE679A598AC47A
[21746.306149] usbtest 9-1:1.0: matched module params, vend=0x2fe3 prod=0x0009
[21746.306153] usbtest 9-1:1.0: Generic USB device
[21746.306156] usbtest 9-1:1.0: full-speed {control} tests
```

**注意（Note）**：可用 `journalctl -k -n 20` 或 `dmesg` 显示内核消息；可能需要root权限，例如 `sudo dmesg`。

第一条消息包含后面需要的两个数值：

- USB总线号：`usb 9-1: [...]` 中的 `9`。
- 被测设备（Device Under Test，DUT）的USB设备号：`USB device number 16` 中的 `16`。

### 67.3.2\_运行基本测试

使用Linux内核源码目录下 `linux/tools/usb` 中的 `testusb` 启动测试：

```console
$ sudo ./testusb -D /dev/bus/usb/009/016
/dev/bus/usb/009/016 test 0,    0.000007 secs
/dev/bus/usb/009/016 test 9,    4.994475 secs
/dev/bus/usb/009/016 test 10,   11.990054 secs
```

**注意**：将命令中的 `009` 和 `016` 分别替换为主机日志中的总线号和DUT设备号，并补齐前导零。

> 译注：此处在已构建 `testusb` 的目录运行 `./testusb`。`/dev/bus/usb/009/016` 是Linux运行时设备节点，不是作者工作区路径；设备重新连接后编号可能变化。找不到节点或驱动未接管时，应回到枚举日志核对，不能照抄历史编号。

### 67.3.3\_使用Gadget Zero测试配置

Linux的 `usbtest` 驱动默认不识别此Zephyr示例的厂商ID（Vendor ID，VID）和产品ID（Product ID，PID）组合，因此不能默认执行全部测试。可利用 [LWN.net文章“动态USB设备ID（Dynamic USB Device IDs）”](https://lwn.net/Articles/160944/) 描述的机制，向 `new_id` sysfs属性写入受支持的参考VID/PID。示例接口类似Gadget Zero，因此使用参考设备 `0525:a4a0`：

```bash
$ sudo sh -c "echo 0x2fe3 0x0009 0 0x0525 0xa4a0 > /sys/bus/usb/drivers/usbtest/new_id"
```

**注意**：可以在加载 `usbtest` 模块后立即完成此步，否则可能需要断开并重新连接DUT，使Gadget Zero接口生效。

> 译注（Linux源码核对）：五个值依次是待匹配VID、PID、接口类约束、参考VID、参考PID；这里第三个值0表示不添加接口类匹配条件。驱动从参考ID条目复制 `driver_info`，以启用Gadget Zero测试能力，并没有修改设备固件的USB标识。`new_id` 是运行中驱动的动态匹配表入口，不是把配置写回Zephyr工程；重启后需按实际模块状态重新设置。

完成后，连接DUT时的内核消息应类似：

```console
[100458.667241] usb 3-5.3.1: new full-speed USB device number 38 using xhci_hcd
[100458.761743] usb 3-5.3.1: New USB device found, idVendor=2fe3, idProduct=0009, bcdDevice= 4.02
[100458.761750] usb 3-5.3.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[100458.761753] usb 3-5.3.1: Product: Zephyr testusb sample
[100458.761755] usb 3-5.3.1: Manufacturer: Zephyr Project
[100458.761757] usb 3-5.3.1: SerialNumber: 2034354E32365007003C001C
[100458.773785] usbtest 3-5.3.1:1.0: Linux gadget zero
[100458.773791] usbtest 3-5.3.1:1.0: full-speed {control in/out bulk-in bulk-out} tests (+alt)
[100458.773858] usbtest 3-5.3.1:1.1: Linux gadget zero
[100458.773859] usbtest 3-5.3.1:1.1: full-speed {control in/out int-in int-out} tests (+alt)
[100458.773914] usbtest 3-5.3.1:1.2: Linux gadget zero
[100458.773916] usbtest 3-5.3.1:1.2: full-speed {control in/out iso-in iso-out} tests (+alt)
```

### 67.3.4\_再次启动测试

使用Linux源码中 `linux/tools/usb` 下的 `testusb`：

```console
$ sudo ./testusb -v 512 -D /dev/bus/usb/009/016
/dev/bus/usb/009/017 test 0,    0.000008 secs
/dev/bus/usb/009/017 test 1,    2.000001 secs
/dev/bus/usb/009/017 test 2,    2.003058 secs
/dev/bus/usb/009/017 test 3,    1.054082 secs
/dev/bus/usb/009/017 test 4,    1.001010 secs
/dev/bus/usb/009/017 test 5,   57.962142 secs
/dev/bus/usb/009/017 test 6,   35.000096 secs
/dev/bus/usb/009/017 test 7,   30.000063 secs
/dev/bus/usb/009/017 test 8,   18.000159 secs
/dev/bus/usb/009/017 test 9,    4.984975 secs
/dev/bus/usb/009/017 test 10,   11.991022 secs
/dev/bus/usb/009/017 test 11,   17.030996 secs
/dev/bus/usb/009/017 test 12,   17.103034 secs
/dev/bus/usb/009/017 test 13,   18.022084 secs
/dev/bus/usb/009/017 test 14,    2.458976 secs
/dev/bus/usb/009/017 test 17,    2.001089 secs
/dev/bus/usb/009/017 test 18,    1.998975 secs
/dev/bus/usb/009/017 test 19,    2.010055 secs
/dev/bus/usb/009/017 test 20,    1.999911 secs
/dev/bus/usb/009/017 test 21,    2.440972 secs
/dev/bus/usb/009/017 test 24,   55.112078 secs
/dev/bus/usb/009/017 test 27,   56.911052 secs
/dev/bus/usb/009/017 test 28,   34.163089 secs
/dev/bus/usb/009/017 test 29,    3.983999 secs
```

> 译注：这组原始命令使用 `/009/016`，其输出却是 `/009/017`，上一段重新枚举日志又为总线3、设备38，属于不同连接时刻的记录。必须以当前枚举结果组成路径，不把三段输出视为同一运行。测试范围还受控制器支持的端点、传输类型及Linux驱动版本限制；日志中没列出的编号不因此自动算通过。本译文没有加载内核模块、绑定设备或运行测试。

## 67.4\_参阅（See Also）

[USB设备核心API](P015_USB设备核心API.md)。

译注的Linux实现依据：[USB动态ID处理](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/core/driver.c)及[usbtest驱动](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/misc/usbtest.c)。


译注核对来源：[samples/subsys/usb/testusb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/testusb/src/main.c)、[samples/subsys/usb/testusb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/testusb/prj.conf)、[samples/subsys/usb/testusb/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/testusb/Kconfig)。

本仓库的[对应源码](../../../samples/subsys/usb/testusb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="testusb-app"></a>
<a id="building-and-flashing"></a>
<a id="testing"></a>
<a id="see-also"></a>

[上一章](P066_USB命令行示例.md) · [返回大纲](大纲.md) · [下一章](P068_USB转I2C桥接示例.md)
