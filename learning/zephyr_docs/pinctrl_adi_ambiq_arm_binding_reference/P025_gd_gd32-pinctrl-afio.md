---
id: learning.zephyr-docs.pinctrl-adi-ambiq-arm-binding-reference.page-25
title: gd_gd32-pinctrl-afio
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第25章\_gd_gd32-pinctrl-afio

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="gd-gd32-pinctrl-afio"></a>
<a id="dtbinding-gd-gd32-pinctrl-afio"></a>
<a id="std-dtcompatible-gd-gd32-pinctrl-afio"></a>

兼容字符串（Compatible String）：`gd,gd32-pinctrl-afio`。厂商：[ GigaDevice Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-gd)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=gd,gd32-pinctrl-afio)。

<a id="description"></a>

GD32引脚控制器（Pin Controller，AFIO模型）。

这是管理引脚功能选择与属性的单例节点（Singleton Node），例如把USART0 RX路由至PA10并启用上拉。还支持重映射（Remapping）。

SoC设备树中使用 `pinctrl` 标签，可按下方原例用 `&pinctrl` 修改。全部设备引脚配置应放在其子节点中，可在开发板目录的 `board-pinctrl.dtsi` 等文件或应用覆盖文件（Overlay）中定义，并包含对应SoC变体的预定义组合头文件。

原例的 `usart0_default` 子节点编码默认即活动状态（Default／Active State）：group1将PA9和PA11配置为USART0 TX、CTS；group2将PA10和PA12配置为RX、RTS，并为两针启用上拉。`usart0_sleep` 编码低功耗模式所用的休眠状态（Sleep State），将PA9～PA12切换为模拟模式（Analog Mode）；该模式断开引脚上下拉电阻、施密特触发器（Schmitt Trigger）和输出缓冲器，因而用于低功耗状态。

子节点内按组组织配置，每组的 `pinmux` 可指定功能列表，并为组内全部引脚共享属性，例如group2的 `bias-pull-up`。支持的标准属性：`drive-push-pull` 为推挽驱动（默认，无需显式设置）；`drive-open-drain` 为开漏驱动；`bias-disable` 禁用上下拉（默认，无需显式设置）；`bias-pull-up` 启用上拉；`bias-pull-down` 启用下拉；`slew-rate` 设置输出最大速度及压摆率，默认2MHz。原文注明前五项仅适用于 `GPIO_IN` 模式，`slew-rate` 仅适用于 `ALTERNATE` 模式。

原文提示驱动与偏置选项是互斥的（Mutually Exclusive）。

可重映射外设的预定义宏以选定重映射方式为后缀：`CAN0_RX_PA11_NORMP` 不重映射，`CAN0_RX_PB8_PRMP` 部分重映射，`CAN0_RX_PD0_FRMP` 完全重映射。**所有 `pinmux` 条目必须使用相同重映射方式**。下方CAN0原例同时选用 `CAN0_RX_PD0_FRMP` 与 `CAN0_TX_PD1_FRMP`，即完全重映射。

使用带数字N的 `pinctrl-N` 属性把配置关联到设备。下方开发板DTS原例包含 `board-pinctrl.dtsi`，通过 `pinctrl-0` 和 `pinctrl-1` 分别引用默认与休眠配置，并设置状态名称 `default`、`sleep`。全部原始代码保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 25.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 25.2\_基础属性

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
| `slew-rate` | `string` | 设置引脚最大速度（Maximum Speed），实际限制输出信号的压摆率（Slew Rate）。默认 `max-speed-2mhz`，也是SoC默认值。并非所有SoC变体都支持 `max-speed-highest`；若选择此项但硬件不支持，则改用50MHz最大速度。使用 `max-speed-highest` 可能需要启用I/O补偿单元（I/O Compensation Cell），详见 `gd,gd32-afio` 绑定。；默认值：`max-speed-2mhz`；合法值：`max-speed-10mhz, max-speed-2mhz, max-speed-50mhz, max-speed-highest` |
| `pinmux` | `array` | **必需**。共享相同组属性的引脚数组。可使用预定义宏，也可根据SoC系列所用引脚复用模型，使用 `GD32_PINMUX_AF` 或 `GD32_PINMUX_AFIO` 辅助宏定义引脚。 |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |

## GD32默认、休眠与设备关联原例

```dts
  &pinctrl {
          /* your modifications go here */
  };
```

```dts
  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */

  /* include pre-defined combinations for the SoC variant used by the board */
  #include <dt-bindings/pinctrl/gd32f403z(k-i-g-e-c-b)xx-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    usart0_default: usart0_default {
      /* group 1 */
      group1 {
        /* configure PA9 as USART0 TX and PA11 as USART0 CTS (no remap) */
        pinmux = <USART0_TX_PA9_NORMP>, <USART0_CTS_PA11_NORMP>;
      };
      /* group 2 */
      group2 {
        /* configure PA10 as USART0 RX and PA12 as USART0 RTS (no remap) */
        pinmux = <USART0_RX_PA10_NORMP>, <USART0_RTS_PA12_NORMP>;
        /* both PA10 and PA12 have pull-up enabled */
        bias-pull-up;
      };

    /* configuration for the usart0 "sleep" state */
    usart0_sleep: usart0_sleep {
      /* group 1 */
      group1 {
        /* configure PA9, PA10, PA11 and PA12 in analog mode */
        pinmux = <ANALOG_PA9>, <ANALOG_PA10>, <ANALOG_PA12>, <ANALOG_PA11>;
      };
    };
```

```dts
   #include "board-pinctrl.dtsi"

   &usart0 {
         pinctrl-0 = <&usart0_default>;
         pinctrl-1 = <&usart0_sleep>;
         pinctrl-names = "default", "sleep";
   };
```

```dts
  &pinctrl {
    can0_default: can0_default {
      group1 {
        pinmux = <CAN0_RX_PD0_FRMP>, <CAN0_TX_PD1_FRMP>;
        /*                    ^^^^                ^^^^           */
        /* CAN0 pins are remapped choosing the full remap option */
      };
    };
  };
```

译注：官方默认／休眠状态片段的大括号未完整闭合；这里保存原始代码，实际配置需补全语法。

## 25.3\_寄存器块命名原例

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

[上一章](P024_gd_gd32-pinctrl-af.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
