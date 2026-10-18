---
id: learning.zephyr-docs.pinctrl-nxp-pico-binding-reference.page-21
title: nxp_s32ze-siul2-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,s32ze-siul2-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第21章\_nxp_s32ze-siul2-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,s32ze-siul2-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-s32ze-siul2-pinctrl"></a>
<a id="dtbinding-nxp-s32ze-siul2-pinctrl"></a>
<a id="std-dtcompatible-nxp-s32ze-siul2-pinctrl"></a>

兼容字符串（Compatible String）：`nxp,s32ze-siul2-pinctrl`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,s32ze-siul2-pinctrl)。

<a id="description"></a>

NXP S32Z/E SoC的SIUL2引脚控制器（Pin Controller）。

这是管理引脚功能和属性的单例节点（Singleton Node），SoC设备树中标签为 `pinctrl`，通过引脚组（Pin Group）定义配置。每个组描述一个外设，每个编号子组包含该外设共享相同属性的引脚；`pinmux` 选择引脚，其他属性设置配置值。

要配置UART0，可在开发板或应用设备树覆盖文件（Overlay）中修改 `pinctrl`。下方原例包含封装头文件 `nxp/s32/pinctrl/S32Z27-BGA594-pinctrl.h` 的预定义引脚；group1选择 `PB10_LIN_0_TX` 并启用输出，group2选择 `PB11_LIN_0_RX` 并启用输入。

`uart0_default` 包含设备特定状态的配置，`default` 为活动状态（Active State）；其他状态可在 `pinctrl` 的不同子节点中定义。除 `pinmux` 外，组还可包含上拉 `bias-pull-up`、压摆率 `slew-rate` 等属性，应用于数组内全部引脚。`input-enable` 启用输入缓冲器，`output-enable` 启用输出缓冲器。

通过设备节点的 `pinctrl-N` 关联状态，其中N为从0开始的状态索引，0为默认状态。下方原例将 `uart0` 的 `pinctrl-0` 指向默认节点，状态名为 `default`，并以 `status = "okay"` 启用设备。

仅提供必需属性时采用以下复位值：输入／输出缓冲器禁用；内部上下拉不启用；开漏禁用；压摆率为4，具体含义见属性说明；终端电阻（Termination Resistor）、电流基准控制（Current Reference Control）和RX电流增强（Current Boost）均禁用，后三项仅影响LVDS焊盘。安全模式始终保持禁用的复位值；接收器选择始终保持复位值，即启用基于VREF的差分接收器。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 21.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 21.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `array` | **必需**。共享相同组属性的引脚数组。必须使用SoC封装头文件中的宏，以32位值编码全部引脚复用信息。 |
| `slew-rate` | `int` | 压摆率控制（Slew Rate Control），复位值4。对于3.3V／1.8V FAST焊盘，FMAX_3318在1.8V／3.3V下分别为：设置0时208／166MHz，4时166／150MHz，5时150／133MHz，6时133／100MHz，7时100／83MHz。对于1.8V GPIO焊盘，设置0、4、5、6、7时，FMAX_18分别为208、150、133、100、50MHz。对于3.3V GPIO焊盘，0保留，4、5、6时FMAX_33均为50MHz，7时为1MHz。完整原始对照保留在下方。；默认值：`4`；合法值：`0, 4, 5, 6, 7` |
| `nxp,current-reference-control` | `boolean` | 对相应引脚施加电流基准控制（Current Reference Control）。仅适用于低电压差分信号（LVDS）焊盘，对其他焊盘类型无效。 |
| `nxp,termination-resistor` | `boolean` | 为相应引脚施加终端电阻（Termination Resistor）。仅适用于低电压差分信号（LVDS）焊盘，对其他焊盘类型无效。 |
| `nxp,rx-current-boost` | `boolean` | 接收端LVDS电流增强（RX LVDS Current Boost），增强RX I/O电流，仅适用于LVDS焊盘。0为200µA电流基准，支持最高320Mbaud；1为1mA电流基准，支持最高420Mbaud。对其他焊盘类型无效。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `output-enable` | `boolean` | 启用引脚输出，例如启用输出缓冲器（Output Buffer），但不主动驱动该引脚。 |

## SIUL2或S32引脚配置与设备关联原例

```dts
  /* Include the SoC package header containing the predefined pins definitions */
  #include <nxp/s32/pinctrl/S32Z27-BGA594-pinctrl.h>

  &pinctrl {
    uart0_default: uart0_default {
      group1 {
        pinmux = <PB10_LIN_0_TX>;
        output-enable;
      };
      group2 {
        pinmux = <PB11_LIN_0_RX>;
        input-enable;
      };
    };
  };
```

```dts
  &uart0 {
    pinctrl-0 = <&uart0_default>;
    pinctrl-names = "default";
    status = "okay";
  };
```

## S32Z/E各类焊盘压摆率原始对照

```text
- For 3.3 V / 1.8 V FAST pads:
  0: FMAX_3318 = 208 MHz (at 1.8 V), 166 MHz (at 3.3 V)
  4: FMAX_3318 = 166 MHz (at 1.8 V), 150 MHz (at 3.3 V)
  5: FMAX_3318 = 150 MHz (at 1.8 V), 133 MHz (at 3.3 V)
  6: FMAX_3318 = 133 MHz (at 1.8 V), 100 MHz (at 3.3 V)
  7: FMAX_3318 = 100 MHz (at 1.8 V), 83 MHz (at 3.3 V)
- For 1.8 V GPIO pads:
  0: FMAX_18 = 208 MHz
  4: FMAX_18 = 150 MHz
  5: FMAX_18 = 133 MHz
  6: FMAX_18 = 100 MHz
  7: FMAX_18 = 50 MHz
- For 3.3 V GPIO pads:
  0: Reserved
  4: FMAX_33 = 50 MHz
  5: FMAX_33 = 50 MHz
  6: FMAX_33 = 50 MHz
  7: FMAX_33 = 1 MHz
```

## 21.3\_寄存器块命名原例

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

[上一章](P020_nxp_s32k5-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_openisa_rv32m1-pinctrl.md)
