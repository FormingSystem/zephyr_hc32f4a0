---
id: learning.zephyr-docs.hardware.comper-2
title: 多位SPI总线
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/mspi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="mspi-api"></a>

# 第65章\_多位SPI总线

原文：[Multi-bit SPI Bus](https://docs.zephyrproject.org/latest/hardware/peripherals/mspi.html)。读取日期：2026-10-13，`latest`。

## 65.1\_多位SPI与控制器接口

**多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**提供通用 **应用程序编程接口（Application Programming Interface，API）**，适配高级SPI外设和设备。这类设备通常需要命令、地址、数据等阶段，并在这些阶段使用多根信号线。它支持 **原位执行（Execute in Place，XIP）**与 **扰码（Scrambling）**等高级特性，同时兼容普通 **串行外设接口（Serial Peripheral Interface，SPI）**。

系统存在多位SPI控制器时，可以使用Zephyr的MSPI控制器API，例如Ambiq MSPI、**四线SPI（Quad SPI，QSPI）**、**八线SPI（Octal SPI，OSPI）**和FlexSPI等。FlexSPI与Ambiq MSPI保留为硬件接口名称。

接口支持从单线到十六线的 **单数据速率（Single Data Rate，SDR）**／**双数据速率（Double Data Rate，DDR）** **输入／输出（Input/Output，I/O）**，允许可变延迟，并支持XIP和扰码。适用设备包括但不限于高速高密度 **闪存（Flash Memory）**、**伪静态随机存取存储器（Pseudo-Static Random Access Memory，PSRAM）**、显示器和传感器。

> 译注：原文将线宽范围写作“single to hex”。这里的hex对应接口中的十六线模式，不是六线；本地头文件也使用 `MSPI_IO_MODE_HEX_8_8_16`、`MSPI_IO_MODE_HEX_8_16_16` 等模式名。具体控制器不一定支持接口能表达的全部模式。

接口由两层组成：与 **片上系统（System on Chip，SoC）**平台相关、实现MSPI API的控制器驱动，以及调用这些API的设备驱动。两层之间是多对多关系，便于在平台之间切换。下面按原文顺序介绍通用初始化过程。

## 65.2\_控制器初始化

首先初始化MSPI控制器驱动实例的数据结构。可以使用常见的设备定义宏 [`DEVICE_DT_INST_DEFINE`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)，将初始化函数、配置和数据作为参数提供给它。

随后初始化硬件，至少考虑原文列出的这些动作：

1. 将 [`mspi_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cfg.html) 配置与硬件实际能力比较，避免错误使用。
2. 设置默认 **引脚复用（Pin Multiplexing，Pinmux）**。
3. 配置控制器时钟。
4. 给硬件上电。
5. 使用 [`mspi_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cfg.html) 以及可能存在的平台专用设置配置硬件。

通常，[`mspi_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cfg.html) 从设备树填充，包含启动时使用的静态参数。必要时，也可以在运行期间通过 [`mspi_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga46c2b98e99ecea045c1ecac4bdf3f087) 使用新参数重新初始化硬件。最后释放本阶段所持有的锁（如果适用）。

## 65.3\_设备驱动初始化

设备驱动也可使用 [`DEVICE_DT_INST_DEFINE`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419) 定义实例。在设备驱动初始化函数内，完成以下原文要求的步骤。

先调用 [`mspi_dev_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b)，传入从设备数据手册得到的硬件设置。设备配置结构 [`mspi_dev_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__cfg.html) 应由设备树填充，可使用辅助宏 [`MSPI_DEVICE_CONFIG_DT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaa8e730d85dede3d1e5dc9f69f30098b2)。控制器驱动随后应校验该结构的成员，避免错误使用。

控制器驱动应实现 **互斥量（Mutex）**，防止意外的并发访问；它还可依据设备标识结构 [`mspi_dev_id`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__id.html) 在不同设备之间切换。

如果硬件支持，继续执行附加配置：

| 接口 | 配置内容 |
| --- | --- |
| [`mspi_memmap_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce) | 内存映射访问，例如XIP。 |
| [`mspi_scramble_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gacf287e08b6ce4898524884e8de22b806) | 扰码功能。 |
| [`mspi_timing_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaff82af1cfc99b9e78cec17ea27f79ab6) | 平台特定的时序设置。 |

必要时使用 [`mspi_register_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga967f5fed63f08ac2d5a88625b030cd14) 注册 **回调函数（Callback Function）**，最后释放控制器互斥锁。这里先完成设备工作模式和时序等配置，再进入收发；不能因为设备树节点存在就省略驱动侧的能力校验。

## 65.4\_收发请求与回调控制

**收发请求（Transceive Request）**使用 [`mspi_xfer`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer.html) 类型。在工作模式已由 [`mspi_dev_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b) 确定并配置后，请求仍允许动态调整与传输有关的设置。

接口还通过 [`mspi_xfer_packet`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer__packet.html) 支持起始地址、大小不同的批量传输。但是否支持 **分散I/O（Scatter I/O）**以及回调管理，取决于控制器实现。

如果已通过 [`mspi_register_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga967f5fed63f08ac2d5a88625b030cd14) 注册回调，控制器可在每次异步／同步传输完成后，根据 [`mspi_bus_event_cb_mask`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1) 决定触发哪个用户回调。即使回调已经注册，也可通过 `MSPI_BUS_NO_CB` 选择不触发任何回调。

在驱动支持的前提下，`MSPI_BUS_XFER_COMPLETE_CB` 用于报告传输完成，`MSPI_BUS_TIMEOUT_CB` 用于报告传输或请求超时。若控制器支持硬件命令队列，并且驱动实现了分散I/O及回调管理，使用者可充分利用硬件性能。回调注册、每次请求选择的事件掩码和驱动实际支持，是三个需要同时考虑的条件。

## 65.5\_设备树中的控制器

以下是原文定义MSPI控制器的设备树例子。控制器的 **绑定（Binding）**应将官方 `mspi-controller.yaml` 作为基础绑定之一。**设备树源文件（Devicetree Source，DTS）**描述硬件实例及其启动参数；这里保留原节点，不把其地址和引脚当作HC32配置。片段中 `MSPI_CONTROLLER` 是控制器角色的配置值，`MSPI_HALF_DUPLEX` 是 **半双工（Half-Duplex）**方式的配置值，表示收发不同时进行。

```devicetree
mspi0: mspi@400 {
         status = "okay";
         compatible = "zephyr,mspi-emul-controller";

         reg = <0x400 0x4>;
         #address-cells = <0x1>;
         #size-cells = <0x0>;

         clock-frequency = <0x17d7840>;
         op-mode = "MSPI_CONTROLLER";
         duplex = "MSPI_HALF_DUPLEX";
         ce-gpios = <&gpio0 0x5 0x1>, <&gpio0 0x12 0x1>;
         dqs-support;

         pinctrl-0 = <&pinmux-mspi0>;
         pinctrl-names = "default";
};
```

`compatible` 表明这是MSPI模拟控制器的示例；`reg` 是设备地址范围，`clock-frequency` 是时钟频率，`op-mode` 和 `duplex` 指定操作角色与双工方式。`ce-gpios` 表示 **芯片使能（Chip Enable，CE）**使用的 **通用输入／输出（General-Purpose Input/Output，GPIO）**，`dqs-support` 表示 **数据选通信号（Data Strobe，DQS）**支持；`pinctrl-0` 和 `pinctrl-names` 选择引脚控制配置。

## 65.6\_设备树中的外设

设备绑定应将官方 `mspi-device.yaml` 作为基础之一。下面在同一控制器下定义一个MSPI设备，代码保持原文。配置值 `MSPI_IO_MODE_QUAD` 选择四线I/O，`MSPI_DATA_RATE_SINGLE` 选择单数据速率，`INSTR_1_BYTE` 选择1字节指令，`ADDR_4_BYTE` 选择4字节地址：

```devicetree
&mspi0 {

         mspi_dev0: mspi_dev0@0 {
                  status = "okay";
                  compatible = "zephyr,mspi-emul-device";

                  reg = <0x0>;
                  size = <0x10000>;

                  mspi-max-frequency = <0x2dc6c00>;
                  mspi-io-mode = "MSPI_IO_MODE_QUAD";
                  mspi-data-rate = "MSPI_DATA_RATE_SINGLE";
                  mspi-hardware-ce-num = <0x0>;
                  read-instruction = <0xb>;
                  write-instruction = <0x2>;
                  instruction-length = "INSTR_1_BYTE";
                  address-length = "ADDR_4_BYTE";
                  rx-dummy = <0x8>;
                  tx-dummy = <0x0>;
                  memmap-config = <0x0 0x0 0x0 0x0>;
                  ce-break-config = <0x0 0x0>;
         };

};
```

即使运行时允许改变，也应在DTS中指定目标运行参数，例如 `mspi-max-frequency`、`mspi-io-mode` 和 `mspi-data-rate`。这些值应代表设备正常工作时的典型配置。

> 译注：两个片段用于说明控制器与子设备的声明关系；原控制器的 `pinctrl-0` 引用了名为 `pinmux-mspi0` 的标签，实际工程必须提供可用的引脚配置。该标签引用中的连字符也不符合设备树标签的标识符规则；正式代码应采用合法标签名（例如 `pinmux_mspi0`），并同步修改定义与引用。本译文保留原片段以便对照。示例地址、使能引脚、指令长度和dummy周期也必须匹配实际硬件与设备，不能原样视为已经可构建的板级配置。

## 65.7\_同一控制器上的多个设备

[`mspi_dev_id`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__id.html) 包含设备索引以及从设备树取得的CE GPIO信息，使API可以支持同一控制器实例下的多个设备。控制器驱动可能支持设备切换，也可能不支持；切换可以通过软件或硬件实现。

如果由软件完成切换，应在 [`mspi_dev_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b) 调用中进行。设备驱动需要保存并更新 [`mspi_dev_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__cfg.html)、其他相关MSPI结构或私有数据结构，记录设备当前运行条件，以支持软件控制的切换。尤其是包含设备身份的 [`mspi_dev_id`](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__id.html)，必须用于每一次API调用。

## 65.8\_配置与示例入口

原页列出以下Kconfig配置项；Kconfig是Zephyr的配置系统，实际依赖和可用能力以所选驱动与硬件为准。

| 配置项 | 含义 |
| --- | --- |
| [`CONFIG_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI) | MSPI总线支持。 |
| [`CONFIG_MSPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_ASYNC) | 异步调用支持。 |
| [`CONFIG_MSPI_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_PERIPHERAL) | 外设模式操作支持。 |
| [`CONFIG_MSPI_MEMMAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_MEMMAP) | 内存映射设备访问。 |
| [`CONFIG_MSPI_SCRAMBLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_SCRAMBLE) | 扰码支持。 |
| [`CONFIG_MSPI_TIMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_TIMING) | 时序配置支持。 |
| [`CONFIG_MSPI_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_INIT_PRIORITY) | 初始化优先级。 |
| [`CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE) | 完成超时逻辑的容差，单位为毫秒。 |
| [`CONFIG_MSPI_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_DMA) | **直接内存访问（Direct Memory Access，DMA）**支持。 |

完整接口见[MSPI参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)。相关示例为[MSPI异步传输](../driver_samples/P022_MSPI异步传输示例.md#mspi-async)，使用异步API访问MSPI存储设备；以及[MSPI吞吐性能测试](../driver_samples/P024_MSPI吞吐量示例.md#mspi-throughput)，以不同缓冲区大小和包数量测量吞吐性能。本次未执行上述配置、传输或性能测试。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：I2C_EEPROM目标设备](P064_I2C_EEPROM目标设备.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：系统管理总线](P066_系统管理总线.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：I2C_EEPROM目标设备](P064_I2C_EEPROM目标设备.md) · [下一章：系统管理总线](P066_系统管理总线.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
