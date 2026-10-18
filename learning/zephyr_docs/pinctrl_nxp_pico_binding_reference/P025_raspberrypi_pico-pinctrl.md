---
id: learning.zephyr-docs.pinctrl-nxp-pico-binding-reference.page-25
title: raspberrypi_pico-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第25章\_raspberrypi_pico-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="raspberrypi-pico-pinctrl"></a>
<a id="dtbinding-raspberrypi-pico-pinctrl"></a>
<a id="std-dtcompatible-raspberrypi-pico-pinctrl"></a>

兼容字符串（Compatible String）：`raspberrypi,pico-pinctrl`。厂商：[ Raspberry Pi Foundation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-raspberrypi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=raspberrypi,pico-pinctrl)。

<a id="description"></a>

Raspberry Pi Pico引脚控制器（Pin Controller）。这是管理引脚功能选择和属性的单例节点（Singleton Node），例如将UART0 RX路由至引脚1并启用上拉。SoC设备树中使用 `pinctrl` 标签，可按下方原例修改。

全部设备配置应放在其子节点中，可定义在开发板目录的 `board-pinctrl.dtsi` 或应用设备树覆盖文件（Overlay）中，并包含所用SoC变体的预定义组合头文件；原例为 `zephyr/dt-bindings/pinctrl/rpi-pico-rp2040-pinctrl.h`。

`uart0_default` 子节点编码设备特定状态，此处为默认即活动状态（Default／Active State）。每个子节点内按组组织配置，组的 `pinmux` 列出功能选择，其他属性由同组引脚共享。原例group1把P0配置为UART0 TX，group2把P1配置为UART0 RX并启用输入。

支持标准属性：`bias-disable` 禁用上下拉（默认，无需显式设置）；`bias-pull-up` 启用上拉；`bias-pull-down` 启用下拉；`input-enable` 启用引脚输入；`input-schmitt-enable` 启用输入迟滞（Input Hysteresis）；`drive-strength` 设置2、4、8、12mA驱动强度，默认4mA；`slew-rate` 为0时慢、1时快。

用带数字N的 `pinctrl-N` 关联设备。下方开发板DTS原例包含 `board-pinctrl.dtsi`，以UART0的 `pinctrl-0`、`pinctrl-1` 分别引用默认与休眠状态，名称为 `default`、`sleep`。

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
| `pinmux` | `array` | **必需**。共享相同组属性的引脚数组。每个元素是由引脚编号与其复用功能（Alternate Function）构造的整数。 |
| `drive-strength` | `int` | 引脚驱动强度（Drive Strength），单位为毫安。默认4mA，与上电复位值一致。；默认值：`4`；合法值：`2, 4, 8, 12` |
| `slew-rate` | `int` | 引脚压摆率（Slew Rate）：0为慢，1为快。默认0（慢），与上电复位值一致。；默认值：`0`；合法值：`0, 1` |
| `raspberrypi,oe-override` | `int` | 覆盖引脚输出使能（Output-Enable Override）：0 `RP2_GPIO_OVERRIDE_NORMAL` 由选定外设信号驱动使能；1 `RP2_GPIO_OVERRIDE_INVERT` 由该信号反相后驱动使能；2 `RP2_GPIO_OVERRIDE_LOW` 禁用输出；3 `RP2_GPIO_OVERRIDE_HIGH` 启用输出。默认0，与上电复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `raspberrypi,out-override` | `int` | 覆盖引脚输出（Output Override）：0 `RP2_GPIO_OVERRIDE_NORMAL` 由选定外设信号驱动；1 `RP2_GPIO_OVERRIDE_INVERT` 使用该信号的反相；2 `RP2_GPIO_OVERRIDE_LOW` 强制低；3 `RP2_GPIO_OVERRIDE_HIGH` 强制高。默认0，与上电复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `raspberrypi,in-override` | `int` | 覆盖引脚输入（Input Override）：0 `RP2_GPIO_OVERRIDE_NORMAL` 取选定引脚信号；1 `RP2_GPIO_OVERRIDE_INVERT` 取其反相；2 `RP2_GPIO_OVERRIDE_LOW` 强制低；3 `RP2_GPIO_OVERRIDE_HIGH` 强制高。默认0，与上电复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `raspberrypi,irq-override` | `int` | 覆盖引脚中断信号（Interrupt Signal Override）：0 `RP2_GPIO_OVERRIDE_NORMAL` 将中断信号送至选定外设；1 `RP2_GPIO_OVERRIDE_INVERT` 反相后送至外设；2 `RP2_GPIO_OVERRIDE_LOW` 强制低；3 `RP2_GPIO_OVERRIDE_HIGH` 强制高。默认0，与上电复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `input-schmitt-enable` | `boolean` | 启用施密特触发模式（Schmitt-Trigger Mode）。 |

## Pico默认与休眠状态关联原例

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
  #include <zephyr/dt-bindings/pinctrl/rpi-pico-rp2040-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    uart0_default: uart0_default {
      /* group 1 */
      group1 {
        /* configure P0 as UART0 TX */
        pinmux = <UART0_TX_P0>;
      };
      /* group 2 */
      group2 {
        /* configure P1 as UART0 RX */
        pinmux = <UART0_RX_P1>;
        /* enable input on pin 1 */
        input-enable;
      };
    };
  };
```

```dts
   #include "board-pinctrl.dtsi"

   &uart0 {
         pinctrl-0 = <&uart0_default>;
         pinctrl-1 = <&uart0_sleep>;
         pinctrl-names = "default", "sleep";
   };
```

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

[上一章](P024_quicklogic_eos-s3-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
