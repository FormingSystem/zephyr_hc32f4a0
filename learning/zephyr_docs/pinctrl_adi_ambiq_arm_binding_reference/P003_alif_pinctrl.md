---
id: learning.zephyr-docs.pinctrl-adi-ambiq-arm-binding-reference.page-3
title: alif_pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/alif,pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_alif_pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/alif,pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="alif-pinctrl"></a>
<a id="dtbinding-alif-pinctrl"></a>
<a id="std-dtcompatible-alif-pinctrl"></a>

兼容字符串（Compatible String）：`alif,pinctrl`。厂商：[ Alif Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-alif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=alif,pinctrl)。

驱动源码（Driver Source）：[drivers/pinctrl/pinctrl_alif.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_alif.c)。

<a id="description"></a>

Alif Semiconductor引脚控制器（Pin Controller）。

该控制器管理Alif SoC的引脚复用（Pin Multiplexing）和焊盘配置（Pad Configuration）。每个I/O引脚最多可选择8种复用功能，即外设信号；焊盘配置还控制输入使能、驱动强度（Drive Strength）和压摆率（Slew Rate）等电气属性。

I/O引脚按端口组织，每个端口最多8针。使用SoC专用Pinctrl头文件（例如 `alif-ensemble-pinctrl.h`）的预定义宏指定复用配置；这些宏编码端口、引脚编号和复用功能。例如 `PIN_P0_0__UART0_RX_A` 表示端口0、引脚0，选择UART0 RX功能。焊盘配置使用标准Pinctrl属性。

下方原例中：`&pinctrl` 引用SoC设备树定义的引脚控制器节点；`uart4_default` 是用户定义的状态节点，汇集UART4默认运行状态的引脚配置；`group0`、`group1` 是引脚组（Pin Group），同组引脚共享焊盘属性。RX引脚需要 `input-enable`，TX使用默认设置，因此分为两组。`pinmux = <PIN_P12_1__UART4_RX_B>` 选择端口12、引脚1的UART4 RX功能，宏定义在 `alif-ensemble-pinctrl.h` 中。`input-enable` 启用RX输入缓冲器，其他可用焊盘属性由属性允许列表（Property Allowlist）定义。

第二段原例通过UART4的 `pinctrl-0` 与 `pinctrl-names = "default"` 把该配置关联到设备。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。引脚控制器寄存器区域（Register Region），必须提供两个：1为GPIO端口P0～P14的主Pinctrl寄存器；2为低功耗GPIO的LPGPIO Pinctrl寄存器。 |
| `reg-names` | `string-array` | **必需**。寄存器区域名称：`pinctrl` 为主GPIO引脚控制寄存器；`lpgpio_pinctrl` 为低功耗GPIO引脚控制寄存器。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
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
| `pinmux` | `array` | **必需**。引脚功能选择数组。每项是32位数值，使用 `ALIF_PINMUX()` 或 `alif-ensemble-pinctrl.h` 的预定义宏（例如 `PIN_P0_0__UART0_RX_A`）编码端口、引脚和复用功能。 |
| `drive-strength` | `int` | 输出驱动强度（Drive Strength），单位为毫安：2对应2mA；4对应4mA（默认）；8对应8mA；12对应12mA。；默认值：`4`；合法值：`2, 4, 8, 12` |
| `slew-rate` | `string` | 输出压摆率控制（Slew Rate Control）：`slow` 为慢速（默认），`fast` 为快速。；默认值：`slow`；合法值：`slow, fast` |
| `bias-high-impedance` | `boolean` | 高阻抗模式（High Impedance），即三态或悬空（Third State／Floating）。 |
| `bias-bus-hold` | `boolean` | 弱锁存（Weak Latch）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `input-disable` | `boolean` | 禁用引脚输入，例如禁用输入缓冲器（Input Buffer）；不影响输出。 |
| `input-schmitt-enable` | `boolean` | 启用施密特触发模式（Schmitt-Trigger Mode）。 |
| `input-schmitt-disable` | `boolean` | 禁用施密特触发模式（Schmitt-Trigger Mode）。 |

## 引脚配置与设备关联原例

```dts
  #include <dt-bindings/pinctrl/alif-ensemble-pinctrl.h>
```

```dts
  &pinctrl {
    uart4_default: uart4_default {
      group0 {
        pinmux = <PIN_P12_1__UART4_RX_B>;
        input-enable;
      };
      group1 {
        pinmux = <PIN_P12_2__UART4_TX_B>;
      };
    };
  };
```

```dts
  &uart4 {
    pinctrl-0 = <&uart4_default>;
    pinctrl-names = "default";
  };
```

---

[上一章](P002_aesc_pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_ambiq_apollo2-pinctrl.md)
