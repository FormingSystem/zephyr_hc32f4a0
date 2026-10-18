---
id: learning.zephyr-docs.pinctrl-stm32-ti-xilinx-binding-reference.page-10
title: ti_cc13xx-cc26xx-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/ti,cc13xx-cc26xx-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_ti_cc13xx-cc26xx-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/ti,cc13xx-cc26xx-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ti-cc13xx-cc26xx-pinctrl"></a>
<a id="dtbinding-ti-cc13xx-cc26xx-pinctrl"></a>
<a id="std-dtcompatible-ti-cc13xx-cc26xx-pinctrl"></a>

兼容字符串（Compatible String）：`ti,cc13xx-cc26xx-pinctrl`。厂商：[ Texas Instruments ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ti)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ti,cc13xx-cc26xx-pinctrl)。

驱动源码（Driver Source）：[drivers/pinctrl/pinctrl_cc13xx_cc26xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_cc13xx_cc26xx.c)。

<a id="description"></a>

TI SimpleLink CC13xx/CC26xx引脚控制器（Pin Controller）。设备引脚配置应放在此节点的子节点中；`pinmux` 由引脚编号与I/O功能配对组成。SoC设备树用 `pinctrl` 标签标识该节点，可通过 `&pinctrl` 修改；所有设备配置置于其子节点中，后文I2C0原例展示了这种结构。

支持的属性包括：`bias-disable` 禁用上拉／下拉，`bias-pull-down` 启用下拉，`bias-pull-up` 启用上拉；`drive-open-drain` 选择开漏（Open-drain）输出。原文下一项仍写 `drive-open-drain`，但说明为开源（Open-source）输出；该差异见译注。`drive-strength` 设置引脚能够拉出的最小电流；`input-enable` 使能输入；`input-schmitt-enable` 使能施密特输入电路（Schmitt Circuit）；`ti,input-edge-detect` 使能并配置边沿检测中断（Edge Detection Interrupt）。

CC13XX例子在开发板DTS中包含 `zephyr/dt-bindings/pinctrl/cc13xx_cc26xx-pinctrl.h`，将I2C引脚设置为开漏、启用上拉及输入。修改默认Pinctrl特性时，在开发板DTS引用该引脚并设置属性。I2C0设备引用SCL/SDA的默认与休眠配置；`i2c0_scl_default` 对应引脚4和 `IOC_PORT_MCU_I2C_MSSCL`，并启用上述特性。随后原例以引脚15、`IOC_PORT_MCU_PORT_EVENT0`、上拉和上升沿检测配置输入，可用于脉冲计数；以引脚16、`IOC_PORT_MCU_PORT_EVENT1`、禁用偏置和8 mA驱动配置输出，可用于脉宽调制（Pulse Width Modulation，PWM）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `array` | **必需**。CC13XX/CC26XX引脚配置，由I/O引脚与I/O功能组成。 |
| `drive-strength` | `int` | 控制配置为输出的I/O引脚的最小驱动强度（Minimum Drive Strength）。2表示至少2 mA，为SoC默认值；4表示至少4 mA；8对于双倍驱动能力I/O表示至少8 mA，对于普通I/O表示至少4 mA。；默认值：`2`；合法值：`2, 4, 8` |
| `ti,input-edge-detect` | `int` | 使能、禁用并配置边沿检测中断（Edge Detection Interrupt）。`IOC_NO_EDGE`：不检测边沿，为SoC默认值；`IOC_FALLING_EDGE`：检测下降沿；`IOC_RISING_EDGE`：检测上升沿；`IOC_BOTH_EDGES`：检测双边沿。；默认值：`0` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `drive-open-source` | `boolean` | 开源驱动（Open Source），实现硬件或（Hardware OR）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `input-schmitt-enable` | `boolean` | 启用施密特触发模式（Schmitt-Trigger Mode）。 |

## TI默认状态、输入与输出配置原例

```dts
  &pinctrl {
          /* your modifications go here */
  };
```

```dts
  #include <zephyr/dt-bindings/pinctrl/cc13xx_cc26xx-pinctrl.h>
```

```dts
  &i2c0 {
    pinctrl-0 = <&i2c0_scl_default &i2c0_sda_default>;
    pinctrl-1 = <&i2c0_scl_sleep &i2c0_sda_sleep>;
    pinctrl-names = "default", "sleep";
  }
```

```dts
  &pinctrl {
    i2c0_scl_default: i2c0_scl_default {
      pinmux = <4 IOC_PORT_MCU_I2C_MSSCL>;
      bias-pull-up;
      drive-open-drain;
      input-enable;
    };
  };
```

```dts
  &pinctrl {
    gpt0_edge_counter: gpt0_edge_counter {
      pinmux = <15 IOC_PORT_MCU_PORT_EVENT0>;
      input-enable;
      bias-pull-up;
      ti,input-edge-detect = <IOC_RISING_EDGE>;
    };
  };
```

```dts
  &pinctrl {
    gpt0_pwm: gpt0_pwm {
      pinmux = <16 IOC_PORT_MCU_PORT_EVENT1>;
      bias-disable;
      drive-strength = <8>; /* in mA */
    };
  };
```

译注：正文把开源输出属性也写为 `drive-open-drain`；本页属性表对应项为 `drive-open-source`。I2C设备节点原例的结束大括号后缺少分号，均保持原样。

## 10.3\_寄存器块命名原例

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

[上一章](P009_telink_b91-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_ti_cc23x0-pinctrl.md)
