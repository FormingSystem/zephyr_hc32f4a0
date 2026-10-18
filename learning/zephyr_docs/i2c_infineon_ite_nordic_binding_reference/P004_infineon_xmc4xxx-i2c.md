---
id: learning.zephyr-docs.i2c-infineon-ite-nordic-binding-reference.page-4
title: infineon_xmc4xxx-i2c
kind: reference
status: maintained
domains: [zephyr, devicetree, i2c]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/i2c/infineon,xmc4xxx-i2c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_infineon_xmc4xxx-i2c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/i2c/infineon,xmc4xxx-i2c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="infineon-xmc4xxx-i2c"></a>
<a id="dtbinding-infineon-xmc4xxx-i2c"></a>
<a id="std-dtcompatible-infineon-xmc4xxx-i2c"></a>

兼容字符串（Compatible String）：`infineon,xmc4xxx-i2c`。厂商：[ Infineon ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-infineon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,xmc4xxx-i2c)。

驱动源码（Driver Source）：[drivers/i2c/i2c_infineon_xmc4.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/i2c_infineon_xmc4.c)。

<a id="description"></a>

Infineon XMC4XXX I²C驱动，将通用串行接口通道（Universal Serial Interface Channel，USIC）配置为I²C设备。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
/* Example devicetree configuration with an adt7420 temperature sensor connected on the bus */
&usic1ch1 {
    compatible = "infineon,xmc4xxx-i2c";
    status = "okay";

    pinctrl-0 = <&i2c_scl_p0_13_u1c1 &i2c_sda_p3_15_u1c1>;
    pinctrl-names = "default";
    scl-src = "DX1B";
    sda-src = "DX0A";
    interrupts = <94 1>;

    #address-cells = <1>;
    #size-cells = <0>;

    clock-frequency = <I2C_BITRATE_STANDARD>;
    adt7420@48 {
        compatible = "adi,adt7420";
        reg = <0x48>;

  /* The associated pinctrl nodes need to be configured as open-drain and input-enable */
  &i2c_scl_p0_13_u1c1 {
    drive-strength = "strong-sharp-edge";
    drive-open-drain;
    hwctrl = "disabled";
  };

  &i2c_sda_p3_15_u1c1 {
    drive-strength = "strong-soft-edge";
    drive-open-drain;
    hwctrl = "disabled";
  };
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `scl-src` | `string` | **必需**。将I²C时钟线，即USIC DX1输入，连接到指定GPIO。DX1输入是连接不同GPIO的复用器（Multiplexer）；引脚与复用映射应查XMC4XXX参考手册。；合法值：`DX1A, DX1B, DX1C, DX1D, DX1E, DX1F, DX1G` |
| `sda-src` | `string` | **必需**。将I²C数据线，即USIC DX0输入，连接到指定GPIO。DX0输入是连接不同GPIO的复用器；引脚与复用映射应查XMC4XXX参考手册。；合法值：`DX0A, DX0B, DX0C, DX0D, DX0E, DX0F, DX0G` |
| `pinctrl-0` | `phandles` | **必需**。SCL、SDA端口引脚配置。节点引用应指向pinctrl节点，标签匹配Infineon定义，格式为`i2c_<signal>_p<port>_<pin>_<peripheral inst>`。下方保留原始pinctrl配置及开漏引脚例子。引脚应设为开漏，并禁用`hwctrl`。<br>原文说明该引脚同时为输入和输出，内部连到USIC2通道0的DX0与DOUT0；参见XMC4700／4800参考手册18-110页、图18-50。这限制了I²C可使用的引脚数量。<br>可改用没有该内部连接的独立输入／输出引脚，在板上外部连接。例如USIC2通道0的SDA可用P3.8作DOUT0、P6.5作DX0，节点标签分别为`i2c_sda_dout0_p3_8_u2c0`和`i2c_sda_dx0_p6_5_u2c0`，通用格式为`i2c_<signal>_<type>_p<port>_<pin>_<peripheral inst>`。<br>下方XMC4700原例将P3.8外接P6.5，P3.9外接P5.2。未在名称中注明dout0／dx0或dout1／dx1的引脚可承担任一功能，例如原文提到`i2c_scl_p5_0_u2c0`可为dout1或dx1。输出引脚dout0／dout1应设开漏，输入引脚dx0／dx1不应含该设置；原例输入注释分别要求USIC的`sda-src = DX0D`与`scl-src = DX1A`。 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `clock-frequency` | `int` | 初始时钟频率（Initial Clock Frequency），单位为Hz。 |
| `sq-size` | `int` | 阻塞请求（Blocking Request）的提交队列（Submission Queue）大小。；默认值：`4` |
| `cq-size` | `int` | 阻塞请求的完成队列（Completion Queue）大小。；默认值：`4` |
| `zephyr,transfer-timeout-ms` | `int` | 等待I²C传输完成的最长时间，单位为毫秒。未提供时采用`CONFIG_I2C_TRANSFER_TIMEOUT_MS`。 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 4.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。I²C中断使用的IRQ编号及优先级。各USIC必须使用指定编号范围：USIC0为84至89，USIC1为90至95，USIC2为96至101。 |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
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

## XMC4XXX引脚分配原例

共用输入／输出引脚：

```dts
pinctrl-0 = <&i2c_scl_p5_2_u2c0 &i2c_sda_p5_0_u2c0>;
```

板上外接的独立输入／输出引脚：

```dts
pinctrl-0 = <&i2c_sda_dout0_p3_8_u2c0 &i2c_sda_dx0_p6_5_u2c0
            &i2c_scl_dout1_p3_9_u2c0 &i2c_scl_p5_2_u2c0>;
```

## XMC4XXX引脚电气配置原例

共享引脚：

```dts
&i2c_scl_p5_2_u2c0 {
    drive-strength = "strong-sharp-edge";
    drive-open-drain;
    hwctrl = "disabled";
};
```

SDA输出引脚：

```dts
&i2c_sda_dout0_p3_8_u2c0 {
    drive-strength = "strong-sharp-edge";
    drive-open-drain;
    hwctrl = "disabled";
};
```

SCL输出引脚：

```dts
&i2c_scl_dout1_p3_9_u2c0 {
    drive-strength = "strong-sharp-edge";
    drive-open-drain;
    hwctrl = "disabled";
};
```

SDA输入引脚，USIC需要`sda-src = DX0D`：

```dts
&i2c_sda_dx0_p6_5_u2c0 {   /* will require USIC setting sda-src = DX0D */
    hwctrl = "disabled";
};
```

SCL输入引脚，USIC需要`scl-src = DX1A`：

```dts
&i2c_scl_p5_2_u2c0 {  /* will require USIC scl-src = DX1A */
    hwctrl = "disabled";
};
```

译注：前面的ADT7420温度传感器完整代码块按网页原样保留；原文没有闭合传感器和USIC节点的大括号，因此是未经修复的原文片段，不能直接视为可编译文件。原注释要求开漏及输入使能，所示配置实际包含`hwctrl = "disabled"`。

## 4.3\_寄存器块命名原例

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

[上一章](P003_infineon_i2c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_intel_sedi-i2c.md)
