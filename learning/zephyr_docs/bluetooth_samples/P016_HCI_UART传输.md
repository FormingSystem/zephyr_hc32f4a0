---
id: learning.zephyr-docs.bluetooth-samples.page-16
title: HCI_UART传输
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_uart/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_hci_uart"></a>

# 第16章\_HCI\_UART传输

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_uart/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/hci_uart)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 16.1\_概览（Overview）

本示例通过通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART），向另一台设备或另一个处理器提供蓝牙控制器（Bluetooth Controller）功能，使用H:4主机控制器接口（Host Controller Interface，HCI）传输协议。H:4要求UART硬件流控。

<a id="requirements"></a>

## 16.2\_要求（Requirements）

需要支持低功耗蓝牙（Bluetooth Low Energy，LE）的开发板。

<a id="default-uart-settings"></a>

## 16.3\_默认UART设置（Default UART settings）

默认控制器构建采用：

- 波特率：1 Mbit/s。
- 8个数据位、无奇偶校验、1个停止位。
- 启用硬件流控（Hardware Flow Control），即请求发送／允许发送（Request to Send / Clear to Send，RTS/CTS）。

<a id="building-and-running"></a>

## 16.4\_构建与运行（Building and Running）

本示例位于Zephyr源码树的 [samples/bluetooth/hci_uart](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_uart)，按标准Zephyr应用构建。

<a id="using-the-controller-with-emulators-and-bluez"></a>

## 16.5\_与模拟器及BlueZ一起使用控制器（Using the controller with emulators and BlueZ）

以下步骤把Nordic nRF5x设备作为Zephyr蓝牙控制器，接入Linux上的BlueZ。

这种组合有助于用BlueZ主机（Host）测试Zephyr链路层（Link Layer）。原文还说明，Zephyr LE控制器可为Linux机器提供Bluetooth LE 5.0控制器，用于系统原生蓝牙支持或基于QEMU的开发。

先按[在Zephyr中使用BlueZ](../bluetooth/P008_蓝牙开发工具.md#bluetooth-bluez)安装较新的BlueZ版本。

然后为所选Nordic nRF5x板构建并烧录。原文说明Nordic开发套件带有Segger芯片，可提供调试接口和CDC ACM串口桥；CDC ACM指通信设备类抽象控制模型（Communications Device Class, Abstract Control Model）。详情见[Nordic nRF5x Segger J-Link](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger)。

例如，为nRF52832开发套件构建：

```bash
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 samples/bluetooth/hci_uart
west flash
```

> 译注——构建位置：原注释“From the root of the zephyr repository”表示从读者自己的Zephyr源码根目录执行，板型按原文示例保留。下面的Linux串口接入命令是在Linux主机Shell执行，与固件构建和烧录属于不同操作。

<a id="using-the-controller-with-qemu-or-native-sim"></a>
<a id="bluetooth-hci-uart-qemu-posix"></a>

### 16.5.1\_与QEMU或native\_sim一起使用控制器（Using the controller with QEMU or native\_sim）

要把H:4 HCI UART控制器用于QEMU或 [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)，先将其接入Linux主机。构建示例，将UART连接到Linux机器，再执行：

```bash
sudo btattach -B /dev/ttyACM0 -S 1000000 -R
```

**注意：**将 `/dev/ttyACM0` 替换为控制器实际连接的串口设备节点。这是Linux设备路径，不是仓库位置。

**注意：**BBC micro:bit需要将波特率参数从 `1000000` 改为 `115200`。

**注意：**原文解释，传给 `btattach` 的 `-R` 标志让内核不主动与控制器交互，而只识别它，以便后续代理给QEMU。

若正在运行蓝牙监视工具 `btmon`，应能看到Linux内核识别所接控制器的简短日志。

接入成功后，按[在QEMU或native_sim上运行](../bluetooth/P008_蓝牙开发工具.md#bluetooth-qemu-native)继续配置和使用QEMU。

<a id="using-the-controller-with-bluez"></a>
<a id="bluetooth-hci-uart-bluez"></a>

### 16.5.2\_与BlueZ一起使用控制器（Using the controller with BlueZ）

先构建示例，将UART连接到Linux机器，再将H:4 HCI UART控制器接入Linux主机：

```bash
sudo btattach -B /dev/ttyACM0 -S 1000000
```

**注意：**将 `/dev/ttyACM0` 替换为控制器实际连接的串口设备节点。

**注意：**BBC micro:bit需要把 `1000000` 改为 `115200`。

若正在运行 `btmon`，应能看到BlueZ加载并初始化控制器的详细日志。接入后按[用BlueZ使用基于Zephyr的控制器](../bluetooth/P008_蓝牙开发工具.md#bluetooth-ctlr-bluez)继续操作。

<a id="debugging-the-controller"></a>

### 16.5.3\_调试控制器（Debugging the controller）

UART已用于本应用，因此可以通过实时传输（Real Time Transfer，RTT）调试。原文使用以下调试配置命令启用RTT：

```bash
west build samples/bluetooth/hci_uart -- -DEXTRA_CONF_FILE='debug.conf'
```

然后按[使用Segger J-Link](../debugging/P003_调试探针.md#using-segger-j-link)连接RTT。

<a id="support-for-the-direction-finding"></a>

### 16.5.4\_支持测向（Support for the Direction Finding）

本示例可以启用低功耗蓝牙测向（Bluetooth LE Direction Finding）。需使用为无线电提供所需硬件配置的特定开发板变体：

```bash
west build samples/bluetooth/hci_uart -b nrf52833dk/nrf52833@df -- -DCONFIG_BT_CTLR_DF=y
```

原文列出的目标如下：

- `nrf5340dk/nrf5340/cpunet@df`
- `nrf52833dk/nrf52833@df`

详情见[测向周期性广播定位器](https://docs.zephyrproject.org/latest/samples/bluetooth/direction_finding_connectionless_rx/README.html#ble_direction_finding_connectionless_rx)和[测向周期性广播信标](https://docs.zephyrproject.org/latest/samples/bluetooth/direction_finding_connectionless_tx/README.html#ble_direction_finding_connectionless_tx)。

<a id="using-a-usb-cdc-acm-uart"></a>

### 16.5.5\_使用USB CDC ACM UART（Using a USB CDC ACM UART）

本示例也可以改用USB UART，配置示例见 [samples/bluetooth/hci_uart/boards/nrf52840dongle_nrf52840.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_uart/boards/nrf52840dongle_nrf52840.conf)。

<a id="using-the-controller-with-the-zephyr-host"></a>

### 16.5.6\_与Zephyr主机一起使用控制器（Using the controller with the Zephyr host）

本节说明如何把运行此控制器示例的开发板，连接到运行Zephyr Host应用的另一块开发板。

控制器端通过设备树源文件（Devicetree Source，DTS）中 `chosen` 块的 `zephyr,bt-c2h-uart` 属性选择UART设备。例如，保留 `uart0` 输出控制台日志，让HCI使用 `uart1`：

```dts
/ {
   chosen {
      zephyr,console = &uart0;
      zephyr,shell-uart = &uart0;
      zephyr,bt-c2h-uart = &uart1;
   };
};
```

在主机应用中，使用以下配置选择H4驱动，替代内置控制器：

```kconfig
CONFIG_BT_HCI=y
CONFIG_BT_LL_SW_SPLIT=n
```

类似地，`zephyr,bt-hci` 属性选择所用HCI实例。UART必须包含一个HCI UART子节点：

```dts
/ {
   chosen {
      zephyr,console = &uart0;
      zephyr,shell-uart = &uart0;
      zephyr,bt-hci = &bt_hci_uart;
   };
};

&uart1 {
   status = "okay";
   bt_hci_uart: bt_hci_uart {
      compatible = "zephyr,bt-hci-uart";
      status = "okay";
   };
};
```

> 译注——片段位置：以上DTS片段分别用于控制器板和Host板的设备树覆盖文件，Kconfig片段用于Host应用配置；它们不是Shell命令，也不是要求两端共用同一配置文件。UART实例、引脚和连接应与所选硬件相符，`uart0`／`uart1`是原文布局示例。

<a id="see-also"></a>

## 16.6\_另请参阅（See also）

[HCI原始通道（RAW Channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)、[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)、[UART接口](../hardware/P330_UART公共接口.md)。


对应官方文档源码：[samples/bluetooth/hci_uart/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_uart/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/hci_uart/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P015_HCI_SPI传输.md) · [返回大纲](大纲.md) · [下一章](P017_HCI三线传输.md)
