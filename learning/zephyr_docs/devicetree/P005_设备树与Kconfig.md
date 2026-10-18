---
id: learning.zephyr-docs.devicetree.kconfig
title: 设备树与 Kconfig 的分工
kind: reference
status: maintained
domains: [zephyr, devicetree, kconfig]
source_url: https://docs.zephyrproject.org/latest/build/dts/dt-vs-kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_设备树与Kconfig的分工

原文：[Devicetree versus Kconfig](https://docs.zephyrproject.org/latest/build/dts/dt-vs-kconfig.html)。读取日期：2026-10-12，`latest`。

Zephyr 同时用设备树和 Kconfig 配置源码，有时不容易判断某项设置属于哪一个。本页给出的原则是：用设备树描述硬件及启动时配置，例如板上外设、启动时钟频率、中断线；用 Kconfig 选择编入最终映像的软件支持，例如网络功能和应用所需驱动。

## 5.1\_UART与无线电示例

假定板的 **片上系统（System on Chip，SoC）** 有两个 **通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）**。硬件的存在由设备树中的两个 UART 节点表示；`compatible` 指出 UART 类型，`reg` 提供寄存器地址范围。启动设置也放在设备树，例如 RX 中断优先级和波特率；即使运行中可以改变，初始值仍由设备树描述。

应用使用哪个 UART 通常不改变相关功能代码，只取决于板设计，因此具体硬件选择属于设备树。是否把 UART 驱动软件编译进来，则由 Kconfig 控制。应用不需要串口时可以通过 Kconfig 去掉驱动源码，即使设备树仍包含 UART 节点。

再看同时支持 Bluetooth LE 和 IEEE 802.15.4 的 2.4 GHz 多协议无线电。设备树描述硬件存在、兼容哪些驱动，以及启动发射功率（dBm）等初始配置。采用哪种协议会使用不同软件，尽管硬件相同，因此由 Kconfig 选择 BLE 或 802.15.4 协议栈。

过去用来启用特定驱动实例的某些 Kconfig 选项已移除。驱动整体仍由 Kconfig 控制，各硬件实例则用对应设备树节点的 `status` 选择。

## 5.2\_例外情况

Kconfig 不容易灵活表达某些按实例区分的驱动配置，例如内部缓冲区大小。这类设置可以放在设备树，但为说明它属于 Zephyr 驱动而非硬件描述或硬件配置，属性名应带 `zephyr,` 前缀，例如通用以太网属性 `zephyr,random-mac-address`。

设备树的 `chosen` 还允许为特定用途选择一个硬件实例，例如指定某个 UART 作为系统控制台。

<a id="auto-dts-kconfig"></a>

## 5.3\_由设备树自动生成的Kconfig符号

处理设备树时，CMake 运行 `scripts/dts/gen_driver_kconfig_dts.py`，扫描所有 **设备树源文件（Devicetree Source，DTS）** 根目录（包括 `dts/bindings`），在构建的 `KCONFIG_BINARY_DIR` 写出 `Kconfig.dts`。通常目录是 `<build>/zephyr`，sysbuild 中可能是 `<build>/<image>/zephyr`。

对绑定中每个 `compatible = "vendor,chip"`，生成：

```kconfig
DT_COMPAT_VENDOR_CHIP := vendor,chip

config DT_HAS_VENDOR_CHIP_ENABLED
        def_bool $(dt_compat_enabled,$(DT_COMPAT_VENDOR_CHIP))
```

赋值保留 compatible 原始字符串，供[自定义预处理函数](https://docs.zephyrproject.org/latest/build/kconfig/preprocessor-functions.html)使用。例如 Kconfig 可调用 `$(dt_compat_on_bus,$(DT_COMPAT_<compatible>),i2c)`。构造符号名时，`-`、`,`、`@` 等字符转换为下划线。

Kconfig 运行后，隐藏布尔符号表现为 `CONFIG_DT_HAS_<compatible>_ENABLED`，表示当前设备树是否至少有一个对应 compatible 且 `status` 为 okay 的节点。驱动启用选项通常应默认 `y`，并依赖此符号：

```kconfig
config SENSOR_VENDOR_CHIP
        bool "Vendor Chip sensor"
        default y
        depends on DT_HAS_VENDOR_CHIP_ENABLED
```

> 译注：在 Kconfig 定义中写 `depends on DT_HAS_...`，不加 `CONFIG_`；生成给配置文件和 C 代码使用时才有该前缀。原文说明句带了 `CONFIG_`，代码示例没有，以上明确区分两个层次。

因为符号自动生成，只需增加具有 `compatible` 的绑定，就可让对应 `DT_HAS_<compatible>_ENABLED` 与 `DT_COMPAT_<compatible>` 在 Kconfig 中可用。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：设备树输入与输出文件](P004_输入与输出文件.md) · [本模块主线目录](../reading/devicetree.md) · [全部主线](../reading/README.md) · [下一篇：设备树操作指南](P006_设备树操作指南.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：输入与输出文件](P004_输入与输出文件.md) · [下一章：设备树操作指南](P006_设备树操作指南.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
