---
id: learning.zephyr-docs.pinctrl-infineon-nordic-nxp-binding-reference.page-9
title: nordic_nrf-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_nordic_nrf-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-nrf-pinctrl"></a>
<a id="dtbinding-nordic-nrf-pinctrl"></a>
<a id="std-dtcompatible-nordic-nrf-pinctrl"></a>

兼容字符串（Compatible String）：`nordic,nrf-pinctrl`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf-pinctrl)。

<a id="description"></a>

Nordic nRF系列引脚控制器（Pin Controller）。

这是管理引脚功能和属性的单例节点（Singleton Node），例如把UART0 RX路由至P0.1并启用上拉。SoC设备树中使用 `pinctrl` 标签，可按下方原例修改。全部设备配置应放在其子节点中，可在开发板目录的 `board-pinctrl.dtsi` 或应用覆盖文件（Overlay）中定义。

`uart0_default` 子节点编码默认即活动状态（Default／Active State）；同一设备的低功耗配置应放在另一个子节点。原例group1将P0.1、P0.2配置为UART_TX、UART_RTS；group2将P0.3、P0.4配置为UART_RX、UART_CTS，并为两者启用上拉。组名（如group1）可任意选择。

每个子节点内按组组织配置，`psels` 列出引脚功能选择，使用 `NRF_PSEL` 宏编码；显式断开引脚时使用 `NRF_PSEL_DISCONNECTED`。可用功能见 `include/zephyr/dt-bindings/pinctrl/nrf-pinctrl.h`。

组内可共享属性，例如group2的 `bias-pull-up`。支持标准属性：`bias-disable` 禁用上下拉（默认，无须显式设置）；`bias-pull-up` 启用上拉；`bias-pull-down` 启用下拉；`low-power-enable` 将引脚设为输入并断开输入缓冲器（Input Buffer）。偏置选项互斥。

使用带数字N的 `pinctrl-N` 关联设备。下方开发板DTS原例包含 `board-pinctrl.dtsi`，通过UART0的 `pinctrl-0` 引用默认配置并设置状态名称。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 9.2\_基础属性

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
| `psels` | `array` | **必需**。共享相同组属性的引脚数组。使用 `NRF_PSEL` 辅助宏编码端口、引脚与功能；也可用 `NRF_PSEL_DISCONNECTED` 显式断开引脚。 |
| `nordic,drive-mode` | `int` | 引脚输出驱动模式（Drive Mode），预定义在 `nrf-pinctrl.h`；某些设备可能不支持附加模式。默认采用0、1均为标准驱动的 `NRF_DRIVE_S0S1`，也是SoC默认值；但 `nordic,nrf-twi` 与 `nordic,nrf-twim` 节点始终以 `NRF_DRIVE_S0D1` 覆盖它，即0为标准驱动，1为断开。；默认值：`0` |
| `nordic,invert` | `boolean` | 反转引脚极性，将有效状态设为低电平。仅对脉宽调制（PWM）通道输出引脚有效。 |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `low-power-enable` | `boolean` | 启用低功耗模式（Low Power Mode）。 |

## 引脚默认状态与设备关联原例

```dts
  &pinctrl {
          /* your modifications go here */
  };
```

```dts
  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */
  &pinctrl {
    /* configuration for uart0 device, default state */
    uart0_default: uart0_default {
      /* group 1 ('group1' name is arbitrary) */
      group1 {
        /* configure P0.1 as UART_TX and P0.2 as UART_RTS */
        psels = <NRF_PSEL(UART_TX, 0, 1)>, <NRF_PSEL(UART_RTS, 0, 2)>;
      };
      /* group 2 */
      group2 {
        /* configure P0.3 as UART_RX and P0.4 as UART_CTS */
        psels = <NRF_PSEL(UART_RX, 0, 3)>, <NRF_PSEL(UART_CTS, 0, 4)>;
        /* both P0.3 and P0.4 are configured with pull-up */
        bias-pull-up;
      };
    };
  };
```

```dts
   #include "board-pinctrl.dtsi"

   &uart0 {
         pinctrl-0 = <&uart0_default>;
         pinctrl-names = "default";
   };
```

## 9.3\_寄存器块命名原例

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

[上一章](P008_microchip_xec-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nuvoton_npcx-leakage-io.md)
