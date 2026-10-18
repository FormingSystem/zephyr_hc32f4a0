---
id: learning.zephyr-docs.mtd-nxp-st-ti-partition-binding-reference.page-23
title: zephyr_mapped-partition
kind: reference
status: maintained
domains: [zephyr, devicetree, flash]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/zephyr,mapped-partition.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第23章\_zephyr_mapped-partition

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/zephyr,mapped-partition.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-mapped-partition"></a>
<a id="dtbinding-zephyr-mapped-partition"></a>
<a id="std-dtcompatible-zephyr-mapped-partition"></a>

兼容字符串（Compatible String）：`zephyr,mapped-partition`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,mapped-partition)。

<a id="description"></a>

闪存或其他非易失性存储器的内存映射分区（Memory-mapped Partition）。`zephyr,mapped-partition` 应是非易失性存储器（NVM）节点的子孙节点：可以直接作为子节点，也可位于中间分组节点或父级 `zephyr,mapped-partition` 节点下。

NVM存储器节点和NVM控制器节点都必须提供 `ranges`，说明它们属于SoC地址空间并给出完整NVM区域范围；通常是在 `reg` 的偏移值前加上0x0。支持嵌套映射分区，父分区也应设置 `ranges`，向子节点说明自身范围。

后文完整原例的控制器节点将NVM映射到CPU地址空间。每个NVM存储器节点描述连续的非易失物理存储区域，所加分区需遵守 `write-block-size` 等物理限制。原例注释要求提供地址映射，并建议定义节点标签（Node Label），便于应用添加分区。

`partitions` 分组是可选的，便于通过设备树覆盖文件（Overlay）等方式一次清除所有分区；如使用该分组，需要提供 `ranges`、`#address-cells` 和 `#size-cells`。分区偏移相对于 `flash0`：若其基址为 `0x10000000`，偏移0即表示地址 `0x10000000`。

原例的storage分区设置 `status = "disabled"`；使用闪存映射子系统（Flash Map Subsystem）的默认映射时，该分区不会出现在Flash Map中。另一组 `flash1` 示例省略 `partitions` 分组，并展示父分区中的两个嵌套分区。

<a id="examples"></a>

官方设备树配置原例：

```dts
/*
 * The NVM controller node defines the ranges which map the NVM memory nodes to the CPU address
 * space.
 */
flash_controller: flash-controller@4001e000 {
        compatible = "vnd,flash-controller"
        reg = <0x4001e000 0x1000>
        ranges;
        #address-cells = <1>;
        #size-cells = <1>;

        /*
         * An NVM memory node describes a consecutive block of non volatile physical memory.
         * Partitions are added to the this node, adhering to physical limitations like
         * write-block-size. An empty `ranges;` property is required to ensure any partition
         * added to the NVM memory is mapped correctly to the CPU address space, and a
         * nodelabel should be defined make it easier for applications to add add partitions
         * to the NVM memory node.
         */
        flash0: flash@0 {
                compatible = "soc-nv-flash"
                reg = <0x0 DT_SIZE_K(1024)>;
                ranges = <0x0 0x0 DT_SIZE_K(1024)>
                #address-cells = <1>;
                #size-cells = <1>;

                /*
                 * The 'partitions' grouping is optional, it allows for clearing all partitions
                 * in a device (e.g. using a dtc overlay file) but is not required. If used,
                 * then it needs a `ranges;` property and to specify the #address-cells and
                 * #size-cells properties
                 */
                partitions {
                        ranges;
                        #address-cells = <1>;
                        #size-cells = <1>;

                        /*
                         * Offsets are relative to the flash0 node, if flash0 had an address of
                         * 0x10000000 then the below offset of 0x0 means address 0x10000000
                         */
                        boot_partition: partition@0 {
                                compatible = "zephyr,mapped-partition";
                                label = "mcuboot";
                                reg = <0x0 0xc000>;
                        };

                        slot0_partition: partition@c000 {
                                compatible = "zephyr,mapped-partition";
                                label = "image-0";
                                reg = <0xc000 0x76000>;
                        };

                        slot1_partition: partition@82000 {
                                compatible = "zephyr,mapped-partition";
                                label = "image-1";
                                reg = <0x82000 0x76000>;
                        };

                        /*
                         * Below example disables an NVM partition, if using the flash map
                         * subsystem with the default mappings then the below partition will
                         * not be present in the flash map
                         */
                        storage_partition: partition@f8000 {
                                compatible = "zephyr,mapped-partition";
                                label = "storage";
                                reg = <0xf8000 0x8000>;
                                status = "disabled";
                         };
                };
        };

        flash1: flash@10000000 {
                compatible = "soc-nv-flash"
                reg = <0x10000000 DT_SIZE_K(256)>;
                ranges = <0x0 0x10000000 DT_SIZE_K(256)>;
                #address-cells = <1>;
                #size-cells = <1>;

                /*
                 * Below demonstrates usage without partitions {}; grouping, and demos
                 * partitions inside of a parent partition
                 */
                external_partition: partition@0 {
                        compatible = "zephyr,mapped-partition";
                        reg = <0x0 0x10000>;
                        ranges = <0x0 0x0 0x10000>;
                        #address-cells = <1>;
                        #size-cells = <1>;

                        external_inner_a_partition: partition@0 {
                                compatible = "zephyr,mapped-partition";
                                reg = <0x0 0x6000>;
                        };

                        external_inner_b_partition: partition@6000 {
                                compatible = "zephyr,mapped-partition";
                                reg = <0x6000 0xa000>;
                        };
                };
        };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 23.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `read-only` | `boolean` | 分区为只读（Read-only）时设置此属性。 |

本页没有已弃用的节点专用属性。

## 23.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | 表示子节点 `reg` 属性地址所需的单元数量（Address Cells），必须足以表示每个分区的起始偏移。 |
| `#size-cells` | `int` | 表示子节点 `reg` 属性大小所需的单元数量（Size Cells），必须足以表示每个分区的字节大小。原文在前半句将对象写为address。 |
| `label` | `string` | 描述非易失性存储分区（NVM Partition）的可读字符串。 |
| `reg` | `array` | **必需**。格式为 `<OFFSET SIZE>`。`OFFSET` 是闪存分区相对于父存储器基址的偏移，`SIZE` 是分区大小，单位字节。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

译注：原始DTS部分属性行缺少分号；注释要求空 `ranges;`，随后代码给出显式范围。原例完整保留，使用前应核对地址映射并补全语法。`#size-cells` 原文前半句写address，后半句明确表示分区字节大小。

## 23.3\_寄存器块命名原例

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

[上一章](P022_zephyr_i2c-target-eeprom.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
