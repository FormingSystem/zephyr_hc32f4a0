---
id: learning.zephyr-docs.mspi-binding-reference.page-3
title: cdns_xspi-nor
kind: reference
status: maintained
domains: [zephyr, devicetree, mspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mspi/cdns,xspi-nor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_cdns_xspi-nor

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mspi/cdns,xspi-nor.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="cdns-xspi-nor"></a>
<a id="dtbinding-cdns-xspi-nor"></a>
<a id="std-dtcompatible-cdns-xspi-nor"></a>

兼容字符串（Compatible String）：`cdns,xspi-nor`。厂商：[ Cadence ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-cdns)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=cdns,xspi-nor)。

驱动源码（Driver Source）：[drivers/mspi/mspi_cadence.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/mspi_cadence.c)。

<a id="description"></a>

带MSPI接口的Cadence xSPI闪存控制器，支持双线、四线及八线SPI。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | **必需**。驱动MSPI外设的时钟频率，单位为Hz。 |
| `read-buffer-size` | `int` | **必需**。内部外设SRAM总线中用于间接读取（Indirect Reads）的地址位数量，其余地址位用于间接写入。可用位数取决于外设内部SRAM深度；对应字节容量还取决于总线宽度，可能在SoC数据手册中说明。<br>建议查SoC数据手册／技术参考手册，将本值设为“SRAM Partition Configuration Register”（SRAM分区配置寄存器）最大值的一半，也是该寄存器复位值，从而一半位置用于间接读取，另一半用于间接写入。 |
| `cdns,nss-delay-ns` | `int` | **必需**。启动后事务之间CS保持无效的纳秒数。 |
| `cdns,btwn-delay-ns` | `int` | **必需**。启动后切换设备时，所有外设均未被选中的纳秒数。 |
| `cdns,after-delay-ns` | `int` | **必需**。最后一位传输结束后，CS继续保持有效的纳秒数。 |
| `cdns,init-delay-ns` | `int` | **必需**。将`n_ss_out`拉低到发送首个数据位之间的纳秒数。 |
| `op-mode` | `string` | 指定MSPI控制器使用控制器模式（Controller Mode）还是外设模式（Peripheral Mode）；驱动可在初始化时使用此设置。；合法值：`MSPI_OP_MODE_CONTROLLER, MSPI_OP_MODE_PERIPHERAL` |
| `duplex` | `string` | 指定MSPI全双工（Full-duplex）或半双工（Half-duplex）模式；驱动可将此设置与其能力核对。；合法值：`MSPI_HALF_DUPLEX, MSPI_FULL_DUPLEX` |
| `dqs-support` | `boolean` | 标示硬件是否支持数据选通（Data Strobe，DQS）；驱动可将此设置与其能力核对。 |
| `software-multiperipheral` | `boolean` | 标示驱动是否启用软件管理多外设（Software-managed Multi-peripheral）功能。至少应据此允许或禁止以`MSPI_DEVICE_CONFIG_NONE`调用`mspi_dev_config`。 |
| `ce-gpios` | `phandle-array` | 所用片选GPIO数组。每个元素指定一个GPIO，数组索引对应此芯片使能（Chip Enable，CE）GPIO控制的子节点。下方保留完整原例。<br>`mspi-device@0`使用`gpio0`的23号引脚、标志`GPIO_ACTIVE_LOW`；`mspi-device@1`使用`gpio1`的10号引脚、同样的低有效标志。更多设备可按同样方式配置。<br>不确定标志时，通常的`CEn`引脚可选择`GPIO_ACTIVE_LOW`；若中间硬件反相或线路本身高有效，可用`GPIO_ACTIVE_HIGH`。<br>**无论CE需要软件控制，还是控制器有专用CE引脚，都应定义本属性**，以便管理同一MSPI控制器上的多个设备。 |
| `packet-data-limit` | `int` | 控制器单个数据包可传输的最大数据长度。收发请求超过此值时必须拆为多个包；未指定时不设限制。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。MSPI配置寄存器及间接写FIFO所在位置的地址和长度。 |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
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

## 片选GPIO数组原例

```dts
  mspi@... {
          ce-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,
                        <&gpio1 10 GPIO_ACTIVE_LOW>,
                        ...;

          mspi-device@0 {
                  reg = <0>;
                  ...
          };
          mspi-device@1 {
                  reg = <1>;
                  ...
          };
          ...
  };
```

## 3.3\_寄存器块命名原例

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

[上一章](P002_ambiq_mspi-device.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_microchip_xec-qmspi-controller.md)
