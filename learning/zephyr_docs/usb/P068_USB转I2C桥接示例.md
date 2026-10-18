---
id: learning.zephyr-docs.usb.page-68
title: USB转I2C桥接示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/i2c_tiny_usb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_USB转I2C桥接示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/i2c_tiny_usb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 68.1\_概述（Overview）

本示例在USB设备支持和集成电路间总线（Inter-Integrated Circuit，I²C）驱动API之上，实现 [I2C-Tiny-USB项目](https://github.com/harbaum/I2C-Tiny-USB)[1]的厂商请求协议（Vendor Request Protocol）。它将Zephyr板转换成USB转I²C适配器，可与Linux的 `i2c-tiny-usb` [总线驱动](https://elixir.bootlin.com/linux/latest/source/drivers/i2c/busses/i2c-tiny-usb.c)[2]配合，使主机能通过 `i2c-dev` 接口及 `i2cdetect`、`i2cget`、`i2cset` 等工具访问板上的I²C总线。

所有通信都通过默认控制管道（Default Control Pipe）的厂商请求完成。I²C传输命令由厂商请求节点处理；查询适配器能力和传输状态的命令则由一个最小USB功能处理，该功能包含厂商专用接口，不带额外端点。属于同一事务（Transaction）的I²C消息先汇集，再在一次I²C传输中执行，以保留消息之间的重复起始条件（Repeated START）。

可使用任何I²C控制器驱动；没有空闲硬件I²C控制器的板，也可使用通过通用输入输出（General-Purpose Input/Output，GPIO）模拟时序（Bit Banging）的 [gpio-i2c](../i2c_infineon_ite_nordic_binding_reference/P002_gpio-i2c.md#std-dtcompatible-gpio-i2c) 驱动。通过设备树节点标签 `zephyr_i2c` 选择控制器，许多板已提供此标签。没有标签时，可在设备树覆盖文件中将它附加到任一I²C控制器，例如 `zephyr_i2c: &arduino_i2c {};`。

## 68.2\_前提条件（Requirements）

需要采用USB设备控制器（USB Device Controller，UDC）API的驱动，以及带 `zephyr_i2c` 节点标签的I²C控制器。

主机需要：

- 含 `i2c-tiny-usb` 驱动（`CONFIG_I2C_TINY_USB`）的Linux内核；多数发行版内核启用了它。
- `i2c-tools` 软件包，提供下文使用的 `i2cdetect`、`i2cget`、`i2cset`。Debian／Ubuntu可用 `sudo apt install i2c-tools` 安装，Fedora使用 `sudo dnf install i2c-tools`。

## 68.3\_构建与运行（Building and Running）

构建并烧录示例：

> 译注：构建块在读者的Zephyr源码根目录、Bash终端执行，前提是已准备依赖模块、工具链及板级烧录工具。之后的模块加载、日志和I²C访问全部在Linux主机终端执行。I²C外设电压、地址和寄存器须以实际连接为准；扫描与寄存器读取会访问真实总线，不保证任意设备都适合这些探测命令。

```bash
west build -b adafruit_feather_rp2040 samples/subsys/usb/i2c_tiny_usb
west flash
```

在 [Feather RP2040](https://docs.zephyrproject.org/latest/boards/adafruit/feather_rp2040/doc/index.html#adafruit_feather_rp2040) 上，`zephyr_i2c` 对应连接到STEMMA QT插座的控制器，因此STEMMA QT或Qwiic扩展模块可以直接插接，无需额外布线。

示例使用Zephyr Project的厂商ID和独立 [产品ID](P004_USB厂商与产品标识.md#usbd-vid-pid)，`i2c-tiny-usb` 驱动尚不认识这组标识。在这组ID加入上游驱动表之前，可以使用 [LWN.net文章“动态USB设备ID”](https://lwn.net/Articles/160944/)[3]所述功能，让驱动接管设备：

```bash
$ sudo modprobe i2c-tiny-usb
$ sudo sh -c "echo 0x2fe3 0x0013 > /sys/bus/usb/drivers/i2c-tiny-usb/new_id"
```

**注意（Note）**：可在加载 `i2c-tiny-usb` 模块后立即完成这一步；否则可能需要拔插开发板以触发绑定。

驱动随后绑定设备，并注册新的I²C适配器：

```console
$ sudo dmesg | grep i2c-tiny-usb
i2c-tiny-usb 1-2.1:1.0: version 1.05 found at bus 001 address 016
i2c i2c-20: connected i2c-tiny-usb device

$ i2cdetect -l | grep tiny
i2c-20  i2c   i2c-tiny-usb at bus 001 device 016    I2C adapter
```

适配器显示为 `i2c-N`，其中 `N` 是内核动态分配的总线号。上例为 `i2c-20`，你的系统可能不同，重新插接后也可能改变。将这个 `N` 作为 `i2c-tools` 的总线参数，替换下面示例中的 `20`。

现在可以在主机访问板上的I²C总线，例如扫描设备，或从地址 `0x1c` 的传感器读取厂商ID寄存器：

```console
$ sudo i2cdetect -y 20
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- 1c -- -- --
...

$ sudo i2cget -y 20 0x1c 0x0d
0xc7
```

> 译注：示例读取寄存器 `0x0d` 并得到 `0xc7`，这些值只对应原示例器件，不是所有I²C设备的公共约定。驱动没绑定时先查USB枚举与动态ID，绑定成功但无目标响应时再检查总线编号、接线、地址和控制器配置。

## 68.4\_限制（Limitations）

事务中的传输只有在主机声明最后一条消息，或请求读数据时才执行。因此，延迟写入产生的否定应答（Negative Acknowledgement，NAK）会通过整个事务的状态报告，而不能对应到实际导致失败的那一条消息。不支持同一事务访问多个不同目标地址；这样的事务会被拒绝并报告失败。

> 译注（源码跟踪）：当前实现最多缓存8条消息、总计256字节数据，超限或地址改变都会重置事务并报告NAK。主机设置时钟延时的请求会映射为标准／快速／快速增强速率；如果控制器不支持运行时配置，示例只记录警告并继续，不能据请求成功认定速率已经改变。能力位表示协议暴露的能力，实际传输仍受底层控制器约束。

## 68.5\_参考资料（References）

1. [I2C-Tiny-USB项目](https://github.com/harbaum/I2C-Tiny-USB)。
2. [Linux i2c-tiny-usb驱动源码](https://elixir.bootlin.com/linux/latest/source/drivers/i2c/busses/i2c-tiny-usb.c)；译注另保存了[Linux官方仓库版本](https://raw.githubusercontent.com/torvalds/linux/master/drivers/i2c/busses/i2c-tiny-usb.c)用于核对。
3. [LWN.net：动态USB设备ID](https://lwn.net/Articles/160944/)。

## 68.6\_参阅（See Also）

- [USB设备核心API](P015_USB设备核心API.md)。
- [I²C驱动API](../hardware/P305_I2C公共接口.md)。


译注核对来源：[samples/subsys/usb/i2c_tiny_usb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/i2c_tiny_usb/src/main.c)、[samples/subsys/usb/i2c_tiny_usb/src/i2c_tiny_usb.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/i2c_tiny_usb/src/i2c_tiny_usb.c)、[samples/subsys/usb/i2c_tiny_usb/src/i2c_tiny_usb.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/i2c_tiny_usb/src/i2c_tiny_usb.h)、[samples/subsys/usb/i2c_tiny_usb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/i2c_tiny_usb/prj.conf)、[samples/subsys/usb/i2c_tiny_usb/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/i2c_tiny_usb/Kconfig)。

本仓库的[对应源码](../../../samples/subsys/usb/i2c_tiny_usb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="i2c-tiny-usb"></a>
<a id="overview"></a>
<a id="id2"></a>
<a id="id4"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="id6"></a>
<a id="limitations"></a>
<a id="references"></a>
<a id="id1"></a>
<a id="id3"></a>
<a id="id5"></a>
<a id="see-also"></a>

[上一章](P067_USB设备测试示例.md) · [返回大纲](大纲.md) · [下一章](P069_WebUSB示例.md)
