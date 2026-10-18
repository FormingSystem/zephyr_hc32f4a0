---
id: learning.zephyr-docs.mtd-atmel-bouffalo-binding-reference.page-11
title: bflb_sf-device
kind: reference
status: maintained
domains: [zephyr, devicetree, flash]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/bflb,sf-device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_bflb_sf-device

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/bflb,sf-device.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="bflb-sf-device"></a>
<a id="dtbinding-bflb-sf-device"></a>
<a id="std-dtcompatible-bflb-sf-device"></a>

兼容字符串（Compatible String）：`bflb,sf-device`。厂商：[ Bouffalo Lab (Nanjing) Co., Ltd. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-bflb)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=bflb,sf-device)。

<a id="description"></a>

Bouffalo Lab串行闪存控制器设备（Serial Flash Controller Device）。

<a id="examples"></a>

官方设备树配置原例：

```dts
// S3A1604 MRAM in QPI QIO
&sf_bank2 {
  reg = <0xa4000000 0x200000>;
  ranges = <0x0 0xa4000000 0x200000>;
  status = "okay";

  pinctrl-0 = <&sf3_default>;
  pinctrl-names = "default";

  s3a1604: mram@0 {
    compatible = "bflb,sf-device";
    reg = <0 0x200000>;

    spi-bus-mode = <4>;
    use-qpi;
    sf-pad = <3>;
    jedec-id = [d9 01 05];

    read-command = <0x0b>;
    read-dummy-cycles = <3>;
    write-command = <0xda>;
    write-dummy-cycles = <0>;
    enter-qpi-command = <0x38>;
    exit-qpi-command = <0xff>;

    initialization-sequence = <0x06 0x0 0x0 0x87 0x01250600 0x4>;
    quirk-bytes-read = [ a0 ];
    quirk-bytes-write = [ a0 ];
  };
};
```

```dts
// PM004MNI MRAM in QPI QIO
&sf_bank2 {
  reg = <0xa4000000 0x80000>;
  ranges = <0x0 0xa4000000 0x80000>;
  status = "okay";

  pinctrl-0 = <&sf2_default>;
  pinctrl-names = "default";

  pm004mni: mram@0 {
    compatible = "bflb,sf-device";
    reg = <0 0x80000>;

    spi-bus-mode = <4>;
    use-qpi;
    sf-pad = <2>;
    jedec-id = [29 55 00];

    read-command = <0xeb>;
    read-dummy-cycles = <0>;
    write-command = <0x38>;
    write-dummy-cycles = <0>;
    enter-qpi-command = <0x35>;
    exit-qpi-command = <0xf5>;
  };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sf-pad` | `int` | **必需**。设备使用的焊盘组（Pad），直接决定使用哪些引脚。Pad 1通常对应嵌入式闪存，Pad 2和Pad 3通常为外部连接；主要例外是BL70x/L，默认内嵌焊盘组为SF2。外部焊盘组需要在存储体（Bank）节点提供Pinctrl配置。；合法值：`1, 2, 3` |
| `spi-bus-mode` | `int` | **必需**。设备使用的SPI总线宽度和模式（Bus Width/Mode），数字表示相应阶段使用的线数。IO `<0>` 为1-1-1；DO `<1>` 为1-1-2；QO `<2>` 为1-1-4；DIO `<3>` 为1-2-2；QIO `<4>` 可为1-4-4、4-4-4四线外设接口（QPI），或0-4-4连续读取／原地执行（Continuous Read/XIP）模式。；合法值：`0, 1, 2, 3, 4` |
| `use-qpi` | `boolean` | 启用四线外设接口（QPI），仅支持4-4-4模式。 |
| `sf-pad-is-external` | `boolean` | 部分焊盘组（Pad）可以连接外部或内部器件，例如BL70x/L的SF2。设置此项以使用外部焊盘组连接，替代内部连接。 |
| `read-command` | `int` | 用于内存映射读取（Memory-mapped Reading）的SPI命令。 |
| `read-dummy-cycles` | `int` | 自动读取模式（Automatic Read Mode）的空周期（Dummy Cycles），以地址字节为单位表示：NIO、DO、QO中每字节8个周期，DIO中4个周期，QIO中2个周期。 |
| `continuous-read-command` | `int` | 使用此命令设置启用连续读取（Continuous Read）。 |
| `write-command` | `int` | 用于内存映射写入（Memory-mapped Writing）的SPI命令。设备不得要求显式擦除或按页大小擦除。 |
| `write-dummy-cycles` | `int` | 自动写入模式（Automatic Write Mode）的空周期（Dummy Cycles），以地址字节为单位表示：NIO、DO、QO中每字节8个周期，DIO中4个周期，QIO中2个周期。 |
| `initialization-sequence` | `array` | 初始化设置时依次写入由命令、数据、数据长度（Command/Data/Data Length）组成的三元组，例如解除块保护或设置空周期时序。每次最多发送4字节数据，注意字节顺序反转，即从右向左。后文保留为MX25L25645G将OC位设为11并禁用块保护的原例。**原文警告：在内部闪存上使用此属性可能非常危险；需要时可使用devcube／eflash loader恢复寄存器设置。** |
| `enter-qpi-command` | `int` | 进入QPI的命令（Enter QPI Command）。 |
| `exit-qpi-command` | `int` | 退出QPI的命令（Exit QPI Command）。 |
| `jedec-id` | `uint8-array` | JEDEC标识（JEDEC ID），依次表示厂商标识、存储器类型和存储密度。 |
| `read-delay` | `int` | 闪存读取延迟（Read Delay），默认值适合标准闪存速度。；默认值：`1`；合法值：`0, 1, 2, 3, 4` |
| `clock-invert` | `boolean` | 反转时钟信号（Invert Clock Signal）。 |
| `rx-clock-invert` | `boolean` | 反转接收时钟信号（Invert RX Clock Signal）。 |
| `quirk-bytes-write` | `uint8-array` | 在自动写入命令（Auto-write Command）的地址之后追加的字节，最多4字节。 |
| `quirk-bytes-read` | `uint8-array` | 在自动读取命令（Auto-read Command）的地址之后追加的字节，最多4字节。 |
| `tune-di` | `int` | 微调数据输入焊盘延迟（Data-in Pad Delay），范围0至3。通常无需微调。；默认值：`0` |
| `tune-do` | `int` | 微调数据输出焊盘延迟（Data-out Pad Delay），范围0至3。通常无需微调。；默认值：`0` |
| `tune-cs` | `int` | 微调片选焊盘延迟（CS Pad Delay），范围0至3。通常无需微调。；默认值：`0` |
| `tune-clk` | `int` | 微调时钟焊盘延迟（CLK Pad Delay），范围0至3。通常无需微调。；默认值：`0` |
| `tune-oe` | `int` | 微调输出使能焊盘延迟（Output-enable Pad Delay），范围0至3。通常无需微调。；默认值：`0` |
| `erase-block-size` | `int` | 闪存擦除操作所需的地址对齐（Address Alignment）。 |
| `write-block-size` | `int` | 闪存写入操作所需的地址对齐（Address Alignment）。 |

本页没有已弃用的节点专用属性。

## 11.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## Bouffalo Lab初始化命令序列原例

```dts
initialization-sequence = <0x06 0x0 0x0 0x1 0xc002 0x2>;
```

## 11.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[上一章](P010_atxp032-mspi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_bflb_sf-flash.md)
