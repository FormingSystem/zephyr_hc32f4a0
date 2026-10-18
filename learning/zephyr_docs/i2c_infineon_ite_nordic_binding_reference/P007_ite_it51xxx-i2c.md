---
id: learning.zephyr-docs.i2c-infineon-ite-nordic-binding-reference.page-7
title: ite_it51xxx-i2c
kind: reference
status: maintained
domains: [zephyr, devicetree, i2c]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/i2c/ite,it51xxx-i2c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第7章\_ite_it51xxx-i2c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/i2c/ite,it51xxx-i2c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ite-it51xxx-i2c"></a>
<a id="dtbinding-ite-it51xxx-i2c"></a>
<a id="std-dtcompatible-ite-it51xxx-i2c"></a>

兼容字符串（Compatible String）：`ite,it51xxx-i2c`。厂商：[ ITE ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ite)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ite,it51xxx-i2c)。

驱动源码（Driver Source）：[drivers/i2c/i2c_ite_it51xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/i2c_ite_it51xxx.c)。

<a id="description"></a>

ITE IT51xxx集成电路间总线（I²C）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 7.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `scl-gpios` | `phandle-array` | **必需**。所选端口的SCL引脚。 |
| `sda-gpios` | `phandle-array` | **必需**。所选端口的SDA引脚。 |
| `port-num` | `int` | **必需**。端口序号0至8依次对应`SMB_CHANNEL_A`、`SMB_CHANNEL_B`、`SMB_CHANNEL_C`、`SMB_CHANNEL_D`、`SMB_CHANNEL_E`、`SMB_CHANNEL_F`、`SMB_CHANNEL_G`、`SMB_CHANNEL_H`、`SMB_CHANNEL_I`。；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8` |
| `channel-switch-sel` | `int` | **必需**。默认映射值1至13依次为`SMB_SWITCH_INTERFACE0`至`SMB_SWITCH_INTERFACE12`；接口N连接SMCLKN／SMDATN，即interface0连接SMCLK0／SMDAT0，依此类推至interface12。完整逐项对应表和原例见下方。<br>应用可交换`&i2c0`与`&i2c2`的`channel-switch-sel`，但不能修改`port-num`；修改通道选择时，相关pinctrl及总线恢复引脚也必须同步修改。<br>有效主机原例：A通道切到interface2，C通道切到interface0。无效主机原例：A通道切到interface2，但C通道仍维持原配置。有效目标端原例：A通道切到interface5，并启用`target-enable`及地址0x52的目标节点。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13` |
| `target-enable` | `boolean` | 启用I²C目标模式（Target Mode）时使用，防止将目标端口按I²C主机初始化。 |
| `target-fifo-mode` | `boolean` | 仅支持写模式或读模式，最大缓冲区为256字节；支持16字节专用FIFO模式（Dedicated FIFO Mode）。 |
| `target-shared-fifo-mode` | `boolean` | 支持非FIFO写入后使用共享FIFO读取的模式，最大共享FIFO为256字节。 |
| `fifo-enable` | `boolean` | I²C控制器支持两个32字节FIFO：FIFO1服务I²C端口0，FIFO2只能服务端口1至8中的一个，默认端口1。 |
| `fifo-ctrl-offset` | `int` | FIFO控制寄存器的偏移；存在此属性时，所有I²C通道的硬件均支持FIFO模式。 |
| `push-pull-recovery` | `boolean` | 以推挽GPIO输出驱动I²C总线恢复时启用。默认采用开漏。 |
| `clock-frequency` | `int` | 初始时钟频率（Initial Clock Frequency），单位为Hz。 |
| `sq-size` | `int` | 阻塞请求（Blocking Request）的提交队列（Submission Queue）大小。；默认值：`4` |
| `cq-size` | `int` | 阻塞请求的完成队列（Completion Queue）大小。；默认值：`4` |
| `zephyr,transfer-timeout-ms` | `int` | 等待I²C传输完成的最长时间，单位为毫秒。未提供时采用`CONFIG_I2C_TRANSFER_TIMEOUT_MS`。 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 7.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

## IT51XXX接口切换取值表

| 数值 | 宏名 | 目标接口与引脚 |
| --- | --- | --- |
| 1 | `SMB_SWITCH_INTERFACE0` | interface0，SMCLK0／SMDAT0 |
| 2 | `SMB_SWITCH_INTERFACE1` | interface1，SMCLK1／SMDAT1 |
| 3 | `SMB_SWITCH_INTERFACE2` | interface2，SMCLK2／SMDAT2 |
| 4 | `SMB_SWITCH_INTERFACE3` | interface3，SMCLK3／SMDAT3 |
| 5 | `SMB_SWITCH_INTERFACE4` | interface4，SMCLK4／SMDAT4 |
| 6 | `SMB_SWITCH_INTERFACE5` | interface5，SMCLK5／SMDAT5 |
| 7 | `SMB_SWITCH_INTERFACE6` | interface6，SMCLK6／SMDAT6 |
| 8 | `SMB_SWITCH_INTERFACE7` | interface7，SMCLK7／SMDAT7 |
| 9 | `SMB_SWITCH_INTERFACE8` | interface8，SMCLK8／SMDAT8 |
| 10 | `SMB_SWITCH_INTERFACE9` | interface9，SMCLK9／SMDAT9 |
| 11 | `SMB_SWITCH_INTERFACE10` | interface10，SMCLK10／SMDAT10 |
| 12 | `SMB_SWITCH_INTERFACE11` | interface11，SMCLK11／SMDAT11 |
| 13 | `SMB_SWITCH_INTERFACE12` | interface12，SMCLK12／SMDAT12 |

## IT51XXX有效与无效切换原例

**有效主机示例（Host）第一部分**：A通道切至interface2。

```dts
&i2c0 {
       status = "okay";
       pinctrl-0 = <&i2c2_clk_gpf6_default
                    &i2c2_data_gpf7_default>;
       pinctrl-names = "default";
       scl-gpios = <&gpiof 6 0>;
       sda-gpios = <&gpiof 7 0>;
       channel-switch-sel = <SMB_SWITCH_INTERFACE2>;
};
```

**有效主机示例第二部分**：C通道切至interface0。

```dts
&i2c2 {
       status = "okay";
       pinctrl-0 = <&i2c0_clk_gpf2_default
                    &i2c0_data_gpf3_default>;
       pinctrl-names = "default";
       scl-gpios = <&gpiof 2 0>;
       sda-gpios = <&gpiof 3 0>;
       channel-switch-sel = <SMB_SWITCH_INTERFACE0>;
};
```

**无效主机示例第一部分**：A通道切至interface2。

```dts
&i2c0 {
       status = "okay";
       pinctrl-0 = <&i2c2_clk_gpf6_default
                    &i2c2_data_gpf7_default>;
       pinctrl-names = "default";
       scl-gpios = <&gpiof 6 0>;
       sda-gpios = <&gpiof 7 0>;
       channel-switch-sel = <SMB_SWITCH_INTERFACE2>;
};
```

**无效主机示例第二部分**：C通道仍保持原配置；与上一段组合即为官方列出的无效配置。

```dts
&i2c2 {
       status = "okay";
       pinctrl-0 = <&i2c2_clk_gpf6_default
                    &i2c2_data_gpf7_default>;
       pinctrl-names = "default";
};
```

**有效目标示例（Target）**：A通道切至interface5，启用地址为`0x52`的目标节点。

```dts
&i2c0 {
       status = "okay";
       pinctrl-0 = <&i2c5_clk_gpa4_default
                    &i2c5_data_gpa5_default>;
       pinctrl-names = "default";
       scl-gpios = <&gpioa 4 0>;
       sda-gpios = <&gpioa 5 0>;
       channel-switch-sel = <SMB_SWITCH_INTERFACE5>;

       target-enable;
       i2c0_target: target@52 {
           compatible = "ite,target-i2c";
           reg = <0x52>;
       };
};
```

## 7.3\_寄存器块命名原例

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

[上一章](P006_ite_enhance-i2c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_ite_it8xxx2-i2c.md)
