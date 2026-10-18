---
id: learning.zephyr-docs.pinctrl-infineon-nordic-nxp-binding-reference.page-6
title: microchip_port-g1-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/microchip,port-g1-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_microchip_port-g1-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/microchip,port-g1-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="microchip-port-g1-pinctrl"></a>
<a id="dtbinding-microchip-port-g1-pinctrl"></a>
<a id="std-dtcompatible-microchip-port-g1-pinctrl"></a>

兼容字符串（Compatible String）：`microchip,port-g1-pinctrl`。厂商：[ Microchip Technology Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-microchip)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,port-g1-pinctrl)。

<a id="description"></a>

Microchip PORT引脚控制容器节点（Pinctrl Container），即port-g1容器。

控制器是管理引脚功能选择和属性的单例节点（Singleton Node），例如将SERCOM0用作UART，把RX路由至PAD1并启用上拉。Group g1 PORT PINCTRL驱动支持以下硬件外设：模块名PORT、ID为U2210、版本2.2.0；PORT／U2210／3.1.0；PORT／03720／4a0；PORT／U2210／v1。

SoC设备树中使用 `pinctrl` 标签，可按下方 `&pinctrl` 原例修改。全部设备引脚配置应放在其子节点中，可写在开发板目录的 `<board>-pinctrl.dtsi` 或应用覆盖文件（Overlay）中，并包含SoC变体预定义组合；原例头文件为 `dt-bindings/pinctrl/sam/same54/atsame54p20a-pinctrl.h`。

原文以 `usart0_default` 说明子节点编码设备默认即活动状态（Default／Active State）。每个子节点内按组组织，通过 `pinmux` 指定引脚功能列表，并为组内引脚共享属性，例如group2的上拉。原例group1为安全域（Secure Domain），group2通过 `non-secure-enable = <1>` 分配到非安全域（Non-Secure Domain）；完整代码与注释保留在下方。

支持的标准属性包括：`bias-pull-up` 启用上拉；`bias-pull-down` 启用下拉；`drive-strength` 增加灌电流（Sink Current）；`input-enable` 启用输入；`output-enable` 启用输出但不主动驱动；`drive-open-drain` 启用开漏；`slew-rate` 从 `fast`、`slow4`、`slow8`、`slow12` 选择压摆率；`slew-limit-en` 启用输出引脚内部压摆率限制；`non-secure-enable` 选择安全域，0为安全域（默认），1为非安全域。

使用带数字N的 `pinctrl-N` 属性将配置关联到设备。下方开发板DTS原例包含 `board-pinctrl.dtsi`，为USART0引用默认配置并设置状态名称。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
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
| `pinmux` | `array` | **必需**。共享相同组属性的引脚数组。可使用预定义宏，或按SoC系列使用的复用模型采用 `MCHP_PINMUX` 辅助宏定义引脚。 |
| `drive-strength` | `int` | 控制已配置为输出的I/O引脚的输出驱动强度（Drive Strength）。0为正常驱动强度；1为更强的驱动强度。；默认值：`0`；合法值：`0, 1` |
| `slew-rate` | `string` | 引脚速度（Pin Speed）。`slew-rate` 默认为SoC上电复位值。压摆率控制（Slew Rate Control）可改善高速信号完整性：`fast` 禁用压摆率控制，即快速；`slow4` 启用控制、慢4倍；`slow8` 慢8倍；`slow12` 慢12倍。仅适用于PIC32CZ CA系列。；默认值：`fast`；合法值：`fast, slow4, slow8, slow12` |
| `slew-limit-en` | `int` | 为配置为输出的I/O引脚启用内部压摆率限制（Slew Rate Limit）：0为禁用，1为启用。仅适用于PIC32CM PL系列。；默认值：`0`；合法值：`0, 1` |
| `non-secure-enable` | `int` | 把引脚分配到安全域（Secure Domain）或非安全域（Non-Secure Domain）：0为安全域（默认），1为非安全域。；默认值：`0`；合法值：`0, 1` |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `output-enable` | `boolean` | 启用引脚输出，例如启用输出缓冲器（Output Buffer），但不主动驱动该引脚。 |

## 引脚默认状态与设备关联原例

```dts
  &pinctrl {
          /* your modifications go here */
  };
```

```dts
  /** You can put this in places like a <board>-pinctrl.dtsi file in
    * your board directory, or a devicetree overlay in your application.
    */

  /** include pre-defined combinations for the SoC variant used by the board */
  #include <dt-bindings/pinctrl/sam/same54/atsame54p20a-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    sercom0_uart_default: sercom0_uart_default {
      /* group 1 */
      group1 {
        /* configure PA6 as USART0 TX and PA8 as USART0 CTS */
        pinmux = <PA5D_SERCOM0_PAD1>, <PA6D_SERCOM0_PAD2>;
        /* pins are assigned to the secure domain by default */
        non-secure-enable = <0>;
      };
      /* group 2 */
      group2 {
        /* configure PA5 as USART0 RX and PA7 as USART0 RTS */
        pinmux = <PA4D_SERCOM0_PAD0>, <PA7D_SERCOM0_PAD3>;
        /* both PA5 and PA7 have pull-up enabled */
        bias-pull-up;
        /* pins are assigned to the non-secure domain */
        non-secure-enable = <1>;
      };
    };
  };
```

```dts
  #include "board-pinctrl.dtsi"

  &usart0 {
        pinctrl-0 = <&usart0_default>;
        pinctrl-names = "default";
  };
```

译注：原例声明 `sercom0_uart_default`，后文引用 `usart0_default`，部分注释的引脚号与宏也不同；这里完整保留原始代码。

## 6.3\_寄存器块命名原例

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

[上一章](P005_mediatek_mt8188-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_microchip_sama7g5-pinctrl.md)
