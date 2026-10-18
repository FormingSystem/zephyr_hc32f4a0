---
id: learning.zephyr-docs.devicetree-api-index.page-1
title: 设备树 API（Devicetree API）
kind: reference
status: maintained
domains: [zephyr, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

<a id="devicetree-api"></a>

<a id="id1"></a>

# 第1章\_设备树 API（Devicetree API）

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/api.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本页是 `<zephyr/devicetree.h>` API 的参考文档。此 API 基于宏（Macro），使用这些宏不会影响调度（Scheduling）；它们可用于任何调用上下文（Calling Context）以及文件作用域（File Scope）。

其中以 `DT_INST_` 开头的宏要求在使用前定义专用宏 `DT_DRV_COMPAT`，下文逐项说明。这类宏主要用于[设备驱动（Device Drivers）](../hardware/P003_设备驱动模型.md#device-model-api)内部；谨慎处理相关条件时，也可在驱动以外使用。

<a id="contents"></a>

目录（Contents）

- <a id="id3"></a>

  [通用 API（Generic APIs）](#generic-apis)

  - <a id="id4"></a>

    [节点标识符与辅助宏（Node Identifiers and Helpers）](#node-identifiers-and-helpers)
  - <a id="id5"></a>

    [属性访问（Property Access）](#property-access)
  - <a id="id6"></a>

    [ranges 属性（ranges Property）](#ranges-property)
  - <a id="id7"></a>

    [reg 属性（reg Property）](#reg-property)
  - <a id="id8"></a>

    [interrupts 属性（interrupts Property）](#interrupts-property)
  - <a id="id9"></a>

    [遍历宏（For-Each Macros）](#for-each-macros)
  - <a id="id10"></a>

    [存在性检查（Existence Checks）](#existence-checks)
  - <a id="id11"></a>

    [节点间依赖（Inter-Node Dependencies）](#inter-node-dependencies)
  - <a id="id12"></a>

    [总线辅助宏（Bus Helpers）](#bus-helpers)
- <a id="id13"></a>

  [基于实例的 API（Instance-Based APIs）](#instance-based-apis)
- <a id="id14"></a>

  [硬件专用 API（Hardware Specific APIs）](#hardware-specific-apis)

  - <a id="id15"></a>

    [控制器局域网（CAN）](#can)
  - <a id="id16"></a>

    [时钟（Clocks）](#clocks)
  - <a id="id17"></a>

    [直接存储器访问（DMA）](#dma)
  - <a id="id18"></a>

    [显示（Display）](#display)
  - <a id="id19"></a>

    [固定与映射闪存分区（Fixed and Mapped Flash Partitions）](#fixed-and-mapped-flash-partitions)
  - <a id="id20"></a>

    [通用输入输出（GPIO）](#gpio)
  - <a id="id21"></a>

    [硬件自旋锁（HWSpinlock）](#hwspinlock)
  - <a id="id22"></a>

    [输入输出通道（IO Channels）](#io-channels)
  - <a id="id23"></a>

    [邮箱（MBOX）](#mbox)
  - <a id="id24"></a>

    [多路复用器（MUX）](#mux)
  - <a id="id25"></a>

    [非易失存储器（NVMEM）](#nvmem)
  - <a id="id26"></a>

    [依赖序号（Ordinals）](#ordinals)
  - <a id="id27"></a>

    [引脚控制（Pinctrl / Pin Control）](#pinctrl-pin-control)
  - <a id="id28"></a>

    [脉宽调制（PWM）](#pwm)
  - <a id="id29"></a>

    [复位控制器（Reset Controller）](#reset-controller)
  - <a id="id30"></a>

    [串行外设接口（SPI）](#spi)
- <a id="id31"></a>

  [被选节点（Chosen Nodes）](#chosen-nodes)
- <a id="id32"></a>

  [Zephyr 专用被选节点（Zephyr-Specific Chosen Nodes）](#zephyr-specific-chosen-nodes)

<a id="generic-apis"></a>

<a id="devicetree-generic-apis"></a>

## [通用 API（Generic APIs）](#id3)

本节 API 可在任何位置使用，无需定义 `DT_DRV_COMPAT`。

<a id="node-identifiers-and-helpers"></a>

### [节点标识符与辅助宏（Node Identifiers and Helpers）](#id4)

节点标识符（Node Identifier）用于在 C 预处理（Preprocessor）阶段引用设备树节点。节点标识符本身不是 C 值，但可通过[属性访问（Property Access）](#devicetree-property-access)等 API，将设备树数据作为 C 右值（Rvalue）访问。

根节点 `/` 的标识符为 `DT_ROOT`。其他节点的标识符可由 [`DT_PATH`](../dt_identity_reference/P001_设备树节点标识宏.md#ga015b4819473797982e83cae497697086)、[`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)、[`DT_ALIAS`](../dt_identity_reference/P001_设备树节点标识宏.md#gaa49e19bbc39dc0d6f16b78a5d02482c9) 和 [`DT_INST`](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead) 创建。

还可使用 [`DT_PARENT`](../dt_identity_reference/P001_设备树节点标识宏.md#ga3ac56d491510275ee1321446796ab63b) 和 [`DT_CHILD`](../dt_identity_reference/P001_设备树节点标识宏.md#ga88259608f4e9083ccc2e9ca5ec2c212e)，分别为指定节点的父节点或某个子节点创建节点标识符。

以下宏用于创建或操作节点标识符。

[节点标识符与辅助宏（Node Identifiers and Helpers）](../dt_identity_reference/P001_设备树节点标识宏.md)

相关代码示例（Related Code Samples）

- [使用自定义设备树绑定的 GPIO（GPIO with Custom Devicetree Binding）](../basic_samples/P008_自定义设备树绑定.md#gpio-custom-dts-binding)使用自定义设备树绑定控制 GPIO。

<a id="property-access"></a>

<a id="devicetree-property-access"></a>

### [属性访问（Property Access）](#id5)

以下通用宏用于访问节点属性。`ranges`、`reg` 和 `interrupts` 属性另有专用访问 API。（参见：[ranges 属性（ranges Property）](#devicetree-ranges-property)；[reg 属性（reg Property）](#devicetree-reg-property)；[interrupts 属性（interrupts Property）](#devicetree-interrupts-property)）

只要节点有匹配的绑定（Binding），即使节点被禁用，也可通过这些宏读取其属性值。

[属性访问宏（Property Accessors）](../dt_property_reference/P001_设备树属性读取宏.md)

<a id="ranges-property"></a>

<a id="devicetree-ranges-property"></a>

### [ranges 属性（ranges Property）](#id6)

访问 `ranges` 属性应使用本节 API，而非通用属性访问 API。该属性的语义由设备树规范定义，因此节点即使没有匹配的绑定，也可使用这些宏。但当绑定指出节点为 PCIe 总线节点时，这些宏遵循《[PCI 总线绑定：IEEE 1275-1994 启动固件标准（PCI Bus Binding to: IEEE Std 1275-1994 Standard for Boot (Initialization Configuration) Firmware）](https://www.devicetree.org/open-firmware/bindings/pci/pci2_1.pdf)》定义的特殊语义。（参见：[属性访问（Property Access）](#devicetree-property-access)）

[ranges 属性（ranges Property）](../dt_reg_reference/P002_设备树地址范围映射宏.md)

<a id="reg-property"></a>

<a id="devicetree-reg-property"></a>

### [reg 属性（reg Property）](#id7)

访问 `reg` 属性应使用本节 API，而非通用属性访问 API。该属性的语义由设备树规范定义，因此节点即使没有匹配的绑定，也可使用这些宏。（参见：[属性访问（Property Access）](#devicetree-property-access)）

[reg 属性（reg Property）](../dt_reg_reference/P001_设备树寄存器属性宏.md)

<a id="interrupts-property"></a>

<a id="devicetree-interrupts-property"></a>

### [interrupts 属性（interrupts Property）](#id8)

访问 `interrupts` 属性应使用本节 API，而非通用属性访问 API。（参见：[属性访问（Property Access）](#devicetree-property-access)）

该属性的语义由设备树规范定义，因此其中部分宏也可用于没有匹配绑定的节点；但以单元名称（Cell Names）为参数的宏不适用此规则。

[interrupts 属性（interrupts Property）](../dt_irq_reference/P001_设备树中断属性宏.md)

<a id="for-each-macros"></a>

### [遍历宏（For-Each Macros）](#id9)

[`DT_FOREACH_ANCESTOR`](../dt_foreach_reference/P001_设备树遍历宏.md#gac4f9fee38bffbd5d315d386fe3c7bc91) 用于遍历设备树节点的祖先节点（Ancestor Nodes），[`DT_FOREACH_CHILD`](../dt_foreach_reference/P001_设备树遍历宏.md#ga2f4eead8e8190110f5c0eb353e6a408f) 用于遍历子节点（Child Nodes）。

另有 [`DT_INST_FOREACH_STATUS_OKAY`](../dt_instance_reference/P001_设备树驱动实例宏.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7) 等专用遍历宏（For-Each Macros），但使用前必须定义 `DT_DRV_COMPAT`。

[遍历宏（For-Each Macros）](../dt_foreach_reference/P001_设备树遍历宏.md)

<a id="existence-checks"></a>

### [存在性检查（Existence Checks）](#id10)

本节说明检查节点是否存在、某类节点有多少个、节点是否具有某属性等用途的宏。[`DT_IRQ_HAS_IDX`](../dt_irq_reference/P001_设备树中断属性宏.md#ga238a290dc6cea9479104ff8f95de1c4c) 以及所有要求定义 `DT_DRV_COMPAT` 的宏等专用宏，在本页其他位置说明。

[存在性检查（Existence Checks）](../dt_identity_reference/P002_设备树存在性与状态宏.md)

相关代码示例（Related Code Samples）

- [使用自定义设备树绑定的 GPIO（GPIO with Custom Devicetree Binding）](../basic_samples/P008_自定义设备树绑定.md#gpio-custom-dts-binding)使用自定义设备树绑定控制 GPIO。

<a id="inter-node-dependencies"></a>

<a id="devicetree-dep-ord"></a>

### [节点间依赖（Inter-Node Dependencies）](#id11)

`devicetree.h` API 支持跟踪节点之间的依赖（Dependencies）。依赖跟踪基于节点间的二元“依赖于”关系，它是以下“直接依赖于”关系的[传递闭包（Transitive Closure）](https://en.wikipedia.org/wiki/Transitive_closure)：

- 每个非根节点直接依赖其父节点。
- 节点直接依赖其属性通过节点引用（Phandle）指向的任何节点；可通过该节点绑定中的 [`dependency-mode`](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#dt-bindings-dependency-mode) 改变此行为。
- 具有 `interrupts` 属性的节点直接依赖其 `interrupt-parent`。
- 父节点继承其所有子节点的依赖。

设备树的依赖顺序（Dependency Ordering）是一个节点列表，其中任意节点 `n` 都排在所有依赖 `n` 的节点之前。节点的依赖序号（Dependency Ordinal）是它在列表中从 0 开始的索引。对于不同节点 `n1`、`n2` 及其序号 `d1`、`d2`，因此有：

- `d1 != d2`
- 若 `n1` 依赖 `n2`，则 `d1 > d2`。
- `d1 > d2` 并不必然表示 `n1` 依赖 `n2`。

Zephyr 构建系统为最终设备树选择一个依赖顺序，并为每个节点分配依赖序号。以下宏可访问依赖信息。具体选择哪个依赖顺序属于实现细节；循环依赖（Cyclic Dependencies）会被检测并报错，因此使用这些宏时可假定不存在循环依赖。

还有基于实例编号（Instance Number）的辅助宏，参见 [`DT_INST_DEP_ORD`](../dt_node_reference/P004_设备树依赖顺序宏.md#ga9c5e6f36c6e7a250368177a9f0713f86) 及其后的说明。

[依赖跟踪（Dependency Tracking）](../dt_node_reference/P004_设备树依赖顺序宏.md)

<a id="bus-helpers"></a>

### [总线辅助宏（Bus Helpers）](#id12)

Zephyr 设备树绑定语言支持 `bus:` 键，用于声明具有特定兼容字符串（Compatible String）的节点描述系统总线。此时子节点被视为位于该类型总线上，可使用以下 API。

[总线辅助宏（Bus Helpers）](../dt_node_reference/P001_设备树总线查询宏.md)

<a id="instance-based-apis"></a>

<a id="devicetree-inst-apis"></a>

## [基于实例的 API（Instance-Based APIs）](#id13)

建议在设备驱动内部使用本节 API。使用时，将 `DT_DRV_COMPAT` 定义为驱动支持的兼容字符串的小写加下划线形式。下面给出设备树片段：

```dts
serial@40001000 {
        compatible = "vnd,serial";
        status = "okay";
        current-speed = <115200>;
};
```

以下用法假定 `serial@40001000` 是唯一启用且兼容字符串为 `vnd,serial` 的节点：

```c
#define DT_DRV_COMPAT vnd_serial
DT_DRV_INST(0)                  // node identifier for serial@40001000
DT_INST_PROP(0, current_speed)  // 115200
```

警告（Warning）

不要轻率地假定实例编号。API 对编号提供的保证见 [`DT_INST`](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

如上所示，`DT_INST_*` API 便于通过实例编号引用节点，几乎都基于某个通用 API 定义。从宏名去掉 `INST_` 通常就能找到对应通用 API。例如，`DT_INST_PROP(inst, prop)` 等价于 `DT_PROP(DT_DRV_INST(inst), prop)`；`DT_INST_REG_ADDR(inst)` 等价于 `DT_REG_ADDR(DT_DRV_INST(inst))`，其余类似。例外包括 [`DT_ANY_INST_ON_BUS_STATUS_OKAY`](../dt_instance_reference/P001_设备树驱动实例宏.md#gaa4ff1fe4242399fbd667fbee7e98040a) 和 [`DT_INST_FOREACH_STATUS_OKAY`](../dt_instance_reference/P001_设备树驱动实例宏.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)，这些专用辅助宏没有直接对应的通用形式。（参见：[通用 API（Generic APIs）](#devicetree-generic-apis)）

由于 `DT_DRV_INST()` 要求定义 `DT_DRV_COMPAT`，未定义该宏就使用本节任何宏都会出错。

另有针对特定硬件的辅助宏，见[硬件专用 API（Hardware Specific APIs）](#devicetree-hw-api)。

[基于实例的设备树 API（Instance-Based Devicetree APIs）](../dt_instance_reference/P001_设备树驱动实例宏.md)

<a id="hardware-specific-apis"></a>

<a id="devicetree-hw-api"></a>

## [硬件专用 API（Hardware Specific APIs）](#id14)

以下 API 也可通过包含 `<devicetree.h>` 使用，无需额外包含其他头文件。

<a id="can"></a>

<a id="devicetree-can-api"></a>

### [控制器局域网（CAN）](#id15)

这些辅助宏用于描述控制器局域网（CAN）控制器／收发器的节点及相关属性。

[设备树CAN API（Devicetree CAN API）](../hardware/P373_CAN设备树宏.md)

<a id="clocks"></a>

### [时钟（Clocks）](#id16)

这些辅助宏用于描述时钟源（Clock Sources）的节点及相关属性。

[设备树时钟 API（Devicetree Clocks API）](../timer_reference/P107_设备树时钟获取宏.md)

<a id="dma"></a>

### [直接存储器访问（DMA）](#id17)

这些辅助宏用于描述直接存储器访问（Direct Memory Access，DMA）控制器或通道的节点及相关属性。

[设备树DMA API（Devicetree DMA API）](../dma_reference/P008_DMA设备树宏.md)

<a id="display"></a>

<a id="devicetree-display-api"></a>

### [显示（Display）](#id18)

这些辅助宏用于描述显示控制器（Display Controllers）的节点及相关属性。

[设备树显示 API（Devicetree Display API）](../hardware/P227_设备树显示接口.md)

<a id="fixed-and-mapped-flash-partitions"></a>

<a id="devicetree-flash-api"></a>

### [固定与映射闪存分区（Fixed and Mapped Flash Partitions）](#id19)

这些辅助宏用于专用兼容字符串 [`fixed-partitions`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/fixed-partitions.html#std-dtcompatible-fixed-partitions) 和 [`zephyr,mapped-partition`](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)，它们在设备树中编码闪存分区（Flash Partitions）信息。更多信息见这两个绑定。

[设备树固定分区 API（Devicetree Fixed Partition API）](../dt_partition_reference/P002_设备树固定分区宏.md)

<a id="gpio"></a>

<a id="devicetree-gpio-api"></a>

### [通用输入输出（GPIO）](#id20)

这些辅助宏用于描述通用输入输出（GPIO）控制器／引脚的节点及相关属性。

[设备树GPIO API（Devicetree GPIO API）](../hardware/P290_设备树GPIO宏.md)

<a id="hwspinlock"></a>

<a id="devicetree-hwspinlock-api"></a>

### [硬件自旋锁（HWSpinlock）](#id21)

这些辅助宏用于描述硬件自旋锁（Hardware Spinlock）的节点及相关属性。

[设备树硬件自旋锁 API（Devicetree HW spinlock API）](../intercore_reference/P008_硬件自旋锁设备树宏.md)

<a id="io-channels"></a>

### [输入输出通道（IO Channels）](#id22)

需要通过输入输出通道（IO Channels）完成转换的设备驱动通常使用这些宏，例如 ADC 或 DAC 通道。

[设备树输入输出通道 API（Devicetree IO Channels API）](../dt_connection_reference/P001_设备树I_O通道宏.md)

<a id="mbox"></a>

<a id="devicetree-mbox-api"></a>

### [邮箱（MBOX）](#id23)

这些辅助宏用于描述邮箱（MBOX）控制器／用户的节点及相关属性。

[设备树邮箱 API（Devicetree MBOX API）](../intercore_reference/P021_邮箱设备树访问宏.md)

<a id="mux"></a>

<a id="devicetree-mux-api"></a>

### [多路复用器（MUX）](#id24)

这些辅助宏用于描述多路复用器（MUX）控制器／使用者的节点及相关属性。

[设备树多路复用器 API（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md)

<a id="nvmem"></a>

<a id="devicetree-nvmem-api"></a>

### [非易失存储器（NVMEM）](#id25)

这些辅助宏用于描述非易失存储器（Non-Volatile Memory，NVMEM）的节点及相关属性。

[NVMEM 设备树辅助宏（NVMEM Devicetree Helpers）](../storage/P018_NVMEM设备树辅助宏.md)

<a id="ordinals"></a>

<a id="devicetree-ordinals-api"></a>

### [依赖序号（Ordinals）](#id26)

这些辅助宏用于节点的依赖跟踪（Dependency Tracking）及相关属性。

[依赖跟踪（Dependency Tracking）](../dt_node_reference/P004_设备树依赖顺序宏.md)

<a id="pinctrl-pin-control"></a>

<a id="devicetree-pinctrl-api"></a>

### [引脚控制（Pinctrl / Pin Control）](#id27)

这些宏通过名称或索引访问引脚控制（Pin Control）属性。

设备树节点可通过属性指定引脚控制设置，也称引脚复用（Pin Mux）设置。节点内使用 `pinctrl-<index>` 属性表达，`<index>` 是从 0 开始的连续整数；也可用 `pinctrl-names` 为它们命名。

例如：

```dts
node {
    ...
    pinctrl-0 = <&foo &bar ...>;
    pinctrl-1 = <&baz ...>;
    pinctrl-names = "default", "sleep";
};
```

上例中，`pinctrl-0` 名为 `default`，`pinctrl-1` 名为 `sleep`。`pinctrl-<index>` 属性值包含节点引用（Phandles）；其中 `&foo`、`&bar` 等引用指向描述该节点引脚配置的节点，其内容因平台而异。

[引脚控制（Pin Control）](../pinctrl_reference/P005_引脚控制设备树宏.md)

<a id="pwm"></a>

### [脉宽调制（PWM）](#id28)

这些辅助宏用于描述脉宽调制（PWM）控制器的节点及相关属性。

[设备树PWM API（Devicetree PWMs API）](../hardware/P264_设备树PWM宏.md)

<a id="reset-controller"></a>

### [复位控制器（Reset Controller）](#id29)

这些辅助宏用于描述复位控制器（Reset Controllers）的节点及相关属性。

[设备树复位控制器 API（Devicetree Reset Controller API）](../reset_reference/P007_复位控制器设备树辅助宏.md)

<a id="spi"></a>

### [串行外设接口（SPI）](#id30)

这些辅助宏根据具体情况用于描述串行外设接口（SPI）控制器或设备的节点。

[设备树SPI API（Devicetree SPI API）](../hardware/P329_SPI设备树宏.md)

<a id="chosen-nodes"></a>

<a id="devicetree-chosen-nodes"></a>

## [被选节点（Chosen Nodes）](#id31)

特殊的 `/chosen` 节点包含描述全系统设置的属性。[`DT_CHOSEN()`](../dt_node_reference/P002_设备树chosen节点宏.md#ga3412d0acecffa828984cf9e2c89889ed) 可获取被选节点（Chosen Node）的节点标识符。

[被选节点（Chosen Nodes）](../dt_node_reference/P002_设备树chosen节点宏.md)

<a id="zephyr-specific-chosen-nodes"></a>

<a id="devicetree-zephyr-chosen-nodes"></a>

## [Zephyr 专用被选节点（Zephyr-Specific Chosen Nodes）](#id32)

下表说明一些常用的 Zephyr 专用被选节点（Zephyr-Specific Chosen Nodes）。

有时，被选节点的 `label` 属性用于设置 Kconfig 选项的默认值，再由该选项配置特定硬件设备。这通常是为了兼容早于 Zephyr 设备树支持而存在的 Kconfig 选项。其他情况下没有 Kconfig 选项，源码直接使用设备树节点选择设备。

<a id="id2"></a>

**Zephyr 专用被选属性（Zephyr-Specific Chosen Properties）**

| 属性（Property） | 用途（Purpose） |
| --- | --- |
| `mcuboot,ram-load-dev` | 使用 [`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD) 构建由 MCUboot 加载到 RAM 的 Zephyr 应用时，此属性向 MCUboot 提供镜像加载地址，地址取被选节点的 `reg`。 |
| `zephyr,boot-mode` | 用于[启动模式（Boot Mode）](https://docs.zephyrproject.org/latest/services/storage/retention/index.html#boot-mode-api)选择，属于[保持系统（Retention System）](https://docs.zephyrproject.org/latest/services/storage/retention/index.html#retention-api)的一部分，指定设备应启动哪个镜像。 |
| `zephyr,bootloader-info` | 选择与引导加载程序（Bootloader）共享信息的保持系统区域。（参见：[保持系统（Retention System）](https://docs.zephyrproject.org/latest/services/storage/retention/index.html#retention-api)） |
| `zephyr,bt-c2h-uart` | 选择 [HCI 串口（HCI UART）](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth_hci_uart) 示例中与主机通信使用的 UART。 |
| `zephyr,bt-hci` | 选择蓝牙主机协议栈（Bluetooth Host Stack）使用的主机控制器接口（HCI）设备。 |
| `zephyr,bt-hci-ipc` | 选择 [HCI 进程间通信（HCI IPC）](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) 示例使用的进程间通信（IPC）设备，将蓝牙控制器提供给另一设备或 CPU。 |
| `zephyr,bt-mon-uart` | 设置蓝牙监视器日志（Bluetooth Monitor Logging）使用的 UART。 |
| `zephyr,camera` | 视频输入设备（Video Input Device），通常是摄像头。 |
| `zephyr,canbus` | 设置默认 CAN 控制器。 |
| `zephyr,code-partition` | Zephyr 镜像的代码段（Text Section）应链接到的闪存分区。 |
| `zephyr,console` | 设置控制台驱动（Console Driver）使用的 UART。 |
| `zephyr,cpu-load-counter` | 选择跟踪 CPU 空闲时间的[计数器（Counter）](https://docs.zephyrproject.org/latest/hardware/peripherals/counter.html#counter-api)设备。 |
| `zephyr,crc` | 选择 CRC 子系统用作加速器（Accelerator）的 CRC 设备。 |
| `zephyr,display` | 设置默认显示控制器（Display Controller）。 |
| `zephyr,dtcm` | 部分 Arm 片上系统（SoC）的数据紧耦合存储器（Data Tightly Coupled Memory，DTCM）节点。 |
| `zephyr,edac` | 选择[错误检测与纠正（Error Detection And Correction，EDAC）](https://docs.zephyrproject.org/latest/hardware/peripherals/edac/index.html#edac-api)子系统使用的 EDAC 设备。 |
| `zephyr,entropy` | 可作为全系统熵源（Entropy Source）的设备。 |
| `zephyr,flash` | 该节点的 `reg` 有时用于设置 [`CONFIG_FLASH_BASE_ADDRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_BASE_ADDRESS) 和 [`CONFIG_FLASH_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_SIZE) 的默认值。 |
| `zephyr,flash-controller` | 对应 `zephyr,flash` 节点所用闪存控制器设备的节点。 |
| `zephyr,gdbstub-uart` | 设置 [GDB 调试桩（GDB Stub）](https://docs.zephyrproject.org/latest/services/debugging/gdbstub.html#gdbstub)子系统使用的 UART。 |
| `zephyr,hdlc-rcp-if` | 选择 OpenThread HDLC 无线协处理器（RCP）接口使用的无线设备；该设备的 API 必须为 [`hdlc_api`](https://docs.zephyrproject.org/latest/doxygen/html/structhdlc__api.html)。 |
| `zephyr,host-cmd-espi-backend` | 参见[嵌入式控制器主机命令（EC Host Command）](https://docs.zephyrproject.org/latest/services/device_mgmt/ec_host_cmd.html#ec-host-cmd-backend-api)API 文档。 |
| `zephyr,host-cmd-shi-backend` | 参见[嵌入式控制器主机命令（EC Host Command）](https://docs.zephyrproject.org/latest/services/device_mgmt/ec_host_cmd.html#ec-host-cmd-backend-api)API 文档。 |
| `zephyr,host-cmd-spi-backend` | 参见[嵌入式控制器主机命令（EC Host Command）](https://docs.zephyrproject.org/latest/services/device_mgmt/ec_host_cmd.html#ec-host-cmd-backend-api)API 文档。 |
| `zephyr,host-cmd-uart-backend` | 参见[嵌入式控制器主机命令（EC Host Command）](https://docs.zephyrproject.org/latest/services/device_mgmt/ec_host_cmd.html#ec-host-cmd-backend-api)API 文档。 |
| `zephyr,ieee802154` | 网络子系统用它设置 IEEE 802.15.4 设备。 |
| `zephyr,ipc` | OpenAMP 子系统用它指定进程间通信（Inter-Process Communication，IPC）设备。 |
| `zephyr,ipc_rsc_table` | 指定 OpenAMP 资源表（Resource Table）使用的内存区域，仅启用 [`CONFIG_OPENAMP_COPY_RSC_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENAMP_COPY_RSC_TABLE) 时需要。 |
| `zephyr,ipc_rx` | `zephyr,ipc` 的替代方案。当发送（TX）和接收（RX）使用独立设备时，选择接收用 IPC 设备；同时必须提供 `zephyr,ipc_tx` 选择发送设备。提供这两个被选属性时，不得再提供单设备形式的 `zephyr,ipc` 兼容项。 |
| `zephyr,ipc_shm` | OpenAMP 子系统使用该节点的 `reg` 确定可用于进程间通信（IPC）的共享内存（Shared Memory，SHM）基址和大小。 |
| `zephyr,ipc_tx` | 参见 `zephyr,ipc_rx` 的说明。 |
| `zephyr,itcm` | 部分 Arm SoC 的指令紧耦合存储器（Instruction Tightly Coupled Memory，ITCM）节点。 |
| `zephyr,led-strip` | 用于确定 WS2812 GPIO 驱动时序的灯带（LED Strip）节点。 |
| `zephyr,log-ipc` | 选择日志子系统 IPC 服务后端（IPC Service Backend）使用的 IPC 设备。 |
| `zephyr,log-uart` | 设置日志子系统 UART 后端使用的一个或多个 UART。定义此属性后，UART 日志后端向该节点列出的设备输出。 |
| `zephyr,modem-uart` | 选择 [AT 命令客户端（AT Command Client）](../driver_samples/P019_AT命令客户端示例.md#at_client)示例使用的调制解调器 UART。 |
| `zephyr,ocm` | Xilinx Zynq-7000 与 ZynqMP SoC 的片上存储器（On-Chip Memory）节点。 |
| `zephyr,openthread-counter` | 启用 [`CONFIG_OPENTHREAD_ALARM_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_ALARM_COUNTER) 时，选择 OpenThread 平台微秒级报警定时器（Microsecond Alarm Timer）使用的计数器设备。 |
| `zephyr,osdp-uart` | 设置开放式受监控设备协议（OSDP）子系统使用的 UART。 |
| `zephyr,ot-uart` | OpenThread 用它指定 Spinel 协议使用的 UART。 |
| `zephyr,pcie-controller` | 对应 PCIe 控制器的节点。 |
| `zephyr,ppp-uart` | 设置点对点协议（PPP）使用的 UART。 |
| `zephyr,ram-console` | 选择控制台子系统 RAM 后端放置缓冲区的 [RAM 段（RAM Section）](../hardware/P557_内存区域绑定.md#std-dtcompatible-zephyr-memory-region)。 |
| `zephyr,rtc` | 设置默认实时时钟（RTC）设备。例如启用 [`CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC) 时，简单网络时间协议（SNTP）库可用它设置系统时间。（参见：[简单网络时间协议库（SNTP Library）](../networking/P034_SNTP时间同步库.md#sntp-interface)） |
| `zephyr,rtk-serial` | 选择串行 GNSS 实时动态定位（RTK）客户端使用的[通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）](../hardware/P006_UART.md#uart-api)设备。 |
| `zephyr,secure-storage-its-partition` | 固定分区节点（Fixed Partition Node），选择安全存储（Secure Storage）的 ZMS 后端使用的分区。 |
| `zephyr,sensor-clock` | 选择用作传感器时间源（Sensor Time Source）的计数器设备。（参见：[计数器（Counter）](https://docs.zephyrproject.org/latest/hardware/peripherals/counter.html#counter-api)） |
| `zephyr,settings-partition` | 固定分区节点。定义此属性时，选择 NVS 和 FCB 设置后端（Settings Backends）使用的分区。 |
| `zephyr,shell-uart` | 设置串行命令行（Serial Shell）后端使用的 UART。 |
| `zephyr,sram` | 链接期间，通过该节点的 `reg` 设置 Zephyr 镜像可用的静态随机存储器（SRAM）基址和大小。 |
| `zephyr,system-timer` | 选择作为 Zephyr 系统定时器（System Timer）的硬件定时器实例，这是全系统唯一的功能。若选用的系统定时器驱动对应的硬件可能有多个实例，则需要此被选属性：选择其中一个实例作为系统定时器，其他实例仍可配合其他 API 使用。若对应硬件只可能存在一个实例，例如 Cortex-M SysTick，则忽略此属性；其他情况下，它必须指向所选系统定时器驱动能够操作的节点。注意，Zephyr 系统定时器驱动由 [`CONFIG_CORTEX_M_SYSTICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK) 等 Kconfig 选项选择，而非由设备树选择。 |
| `zephyr,system-timer-companion` | 选择主系统定时器在低功耗状态下停止运行时继续计时的设备；它必须实现计数器 API（[计数器（Counter）](https://docs.zephyrproject.org/latest/hardware/peripherals/counter.html#counter-api) API）。 |
| `zephyr,tflm-storage` | 选择在 Arm Ethos-U55、U65、U85 神经网络处理器（NPU）上运行 TensorFlow Lite for Microcontrollers 示例所使用的内存区域。（参见：[内存区域（Memory Region）](../hardware/P557_内存区域绑定.md#std-dtcompatible-zephyr-memory-region)；[在 Arm Ethos-U55、U65、U85 NPU 上运行的 TensorFlow Lite for Microcontrollers](../basic_samples/P075_TensorFlowLiteMicro与EthosU示例.md#tflite-ethosu)） |
| `zephyr,touch` | 触摸屏控制器（Touchscreen Controller）设备节点。使用 LVGL 且启用 [`CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH) 时，创建以该控制器为输入源的 LVGL 指针输入设备（Pointer Input Device）。 |
| `zephyr,tracing-uart` | 设置跟踪（Tracing）子系统使用的 UART。 |
| `zephyr,uart-mcumgr` | [设备管理（Device Management）](https://docs.zephyrproject.org/latest/services/device_mgmt/index.html#device-mgmt)使用的 UART。 |
| `zephyr,uart-pipe` | 设置串行管道驱动（Serial Pipe Driver）使用的 UART。 |
| `zephyr,videoenc` | 视频编码器（Video Encoder）设备，通常为 H264 或 MJPEG 编码器。 |

译注：本页开头的头文件路径为 `<zephyr/devicetree.h>`，硬件专用API段落沿用原文的 `<devicetree.h>` 写法；原文路径均保留。

来源链接状态（2026-10-16）：原文引用的Wikipedia“传递闭包”页面经重试仍返回HTTP 403；保留原链接，未将该外部页面记为已翻译。

---

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/devicetree_api_index.md) · [全部主线](../reading/README.md) · [下一篇：绑定索引（Bindings Index）](P002_设备树绑定索引.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)

</details>

<!-- reading-navigation:end -->
