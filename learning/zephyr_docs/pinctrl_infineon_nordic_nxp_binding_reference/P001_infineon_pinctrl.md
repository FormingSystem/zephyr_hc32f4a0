---
id: learning.zephyr-docs.pinctrl-infineon-nordic-nxp-binding-reference.page-1
title: infineon_pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/infineon,pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_infineon_pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/infineon,pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="infineon-pinctrl"></a>
<a id="dtbinding-infineon-pinctrl"></a>
<a id="std-dtcompatible-infineon-pinctrl"></a>

兼容字符串（Compatible String）：`infineon,pinctrl`。厂商：[ Infineon Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-infineon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,pinctrl)。

<a id="description"></a>

Infineon CAT1引脚控制容器（Pinctrl Container）。

这是管理引脚功能与属性的单例节点（Singleton Node），例如把UART0 RX路由至指定端口／引脚并启用上拉。SoC设备树中使用 `pinctrl` 节点标签，可通过下方 `&pinctrl` 原例修改。

引脚配置也可指定电气属性，例如 `bias-pull-up`。支持的标准属性为：`bias-high-impedance` 高阻态；`bias-pull-up` 上拉；`bias-pull-down` 下拉；`drive-open-drain` 开漏；`drive-open-source` 开源；`drive-push-pull` 推挽强驱动；`input-enable` 启用输入缓冲器。

CAT1 SoC设备树包含一组预定义引脚控制节点，可通过制造商料号（Manufacturer Part Number，MPN）DTSI文件查找。例如 `cy8cproto_062_4343w` 开发板使用CY8C624ABZI_S2D44，板级文件 `boards/arm/cy8cproto_062_4343w/cy8cproto_062_4343w.dts` 包含 `infineon/psoc6/mpns/CY8C624ABZI_S2D44.dtsi`。每个MPN DTSI再包含封装DTSI，路径形式为 `../psoc6_xx/psoc6_xx.yyy-zzz.dtsi`；此例包含 `../psoc6_02/psoc6_02.124-bga.dtsi`。

封装文件中的预定义节点 `p3_0_scb2_uart_rx` 表示连接端口3.0的UART2（SCB2）RX引脚，原例保留在下方；完整节点列表见 `psoc6_02.124-bga.dtsi`。

注意1：预定义节点使用 `DT_CAT1_PINMUX(port_number, pin_number, hsiom)` 初始化 `pinmux`，其中 `hsiom` 来自 `zephyr/include/zephyr/dt-bindings/pinctrl/ifx_cat1-pinctrl.h` 的 `HSIOM_SEL_xxx` 宏。也可用此宏自定义节点，下方 `my_uart_rx` 原例选择端口3、引脚0和 `HSIOM_SEL_ACT_6`。

注意2：预定义节点没有偏置配置，可在 `board-pinctrl.dtsi` 更新。原例为UART2的TX、RTS启用推挽，为RX、CTS启用输入。最后一组开发板DTS原例通过UART5的 `pinctrl-0` 引用预定义TX、RX节点，并分别设置推挽与输入。全部原始配置保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 1.2\_基础属性

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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `int` | **必需**。编码端口／引脚与复用功能（Alternate Function）。 |
| `drive-strength` | `string` | 引脚输出驱动强度（Drive Strength）。；合法值：`full, half, one-fourth, one-eighth` |
| `infineon,cfgout3-mode` | `boolean` | 应用 `CY_GPIO_DM_CFGOUT3_STRONG_PULLUP_HIGHZ` 驱动模式（CFG_OUT3），某些芯片的I3C引脚必须使用此模式。设置后忽略其他驱动模式和偏置属性，并隐含启用 `input-enable`。 |
| `infineon,cfgout3-pullup-ohms` | `int` | CFGOUT3焊盘的内部上拉电阻值，单位为欧姆。仅在设置 `infineon,cfgout3-mode` 时有意义，直接对应外设驱动库（PDL）的 `Cy_GPIO_SetPullupResistance()` 数值：0为禁用，2800为2.8kΩ，依此类推至570Ω。省略时不配置上拉（`CY_GPIO_PULLUP_RES_DISABLE`）。；合法值：`0, 2800, 1800, 1100, 1200, 840, 720, 570` |
| `bias-high-impedance` | `boolean` | 高阻抗模式（High Impedance），即三态或悬空（Third State／Floating）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `drive-open-source` | `boolean` | 开源驱动（Open Source），实现硬件或（Hardware OR）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |

## CAT1预定义节点与偏置配置原例

```dts
&pinctrl {
    /* Your modifications go here */
};
```

```dts
  /omit-if-no-ref/ p3_0_scb2_uart_rx: p3_0_scb2_uart_rx {
        pinmux = <DT_CAT1_PINMUX(3, 0, HSIOM_SEL_ACT_6)>;
  };
```

```dts
        &pinctrl {
            my_uart_rx: my_uart_rx {
                pinmux = <DT_CAT1_PINMUX(3, 0, HSIOM_SEL_ACT_6)>;
            };
        };
```

```dts
  &pinctrl {
    /* Configure pin control Bias mode for uart2 pins */
    p3_1_scb2_uart_tx {
      drive-push-pull;
    };

    p3_0_scb2_uart_rx {
      input-enable;
    };

    p3_2_scb2_uart_rts {
      drive-push-pull;
    };

    p3_3_scb2_uart_cts {
      input-enable;
    };
  };
```

```dts
  &uart5 {
    pinctrl-0 = <&p5_1_scb5_uart_tx &p5_0_scb5_uart_rx>;
    pinctrl-names = "default";
  };
```

```dts
  &p5_1_scb5_uart_tx {
    drive-push-pull;
  };
```

```dts
  &p5_0_scb5_uart_rx {
    input-enable;
  };
```

## 1.3\_寄存器块命名原例

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

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_infineon_xmc4xxx-pinctrl.md)
