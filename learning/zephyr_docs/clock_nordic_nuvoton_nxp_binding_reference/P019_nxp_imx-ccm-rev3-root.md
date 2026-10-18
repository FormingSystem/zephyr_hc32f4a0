---
id: learning.zephyr-docs.clock-nordic-nuvoton-nxp-binding-reference.page-19
title: nxp_imx-ccm-rev3-root
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imx-ccm-rev3-root.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_nxp_imx-ccm-rev3-root

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imx-ccm-rev3-root.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-imx-ccm-rev3-root"></a>
<a id="dtbinding-nxp-imx-ccm-rev3-root"></a>
<a id="std-dtcompatible-nxp-imx-ccm-rev3-root"></a>

兼容字符串（Compatible String）：`nxp,imx-ccm-rev3-root`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,imx-ccm-rev3-root)。

<a id="description"></a>

NXP i.MX CCM rev3控制器的一个可配置时钟根（Clock Root）。

时钟根是CCM中选择时钟源并对其分频的部分，决定外设收到的频率。将时钟根声明为设备树节点，可让开发板或应用覆盖文件（Overlay）修改时钟树，不必修改开发板C文件。

控制器初始化时，按设备树顺序配置所有已启用的时钟根子节点。一个时钟根向另一个供钟时，顺序十分重要；所选源尚未运行的时钟根不会输出时钟。下方保留CLOCK_ROOT40配置原例。

复用选择器（Mux）的值属于各自的时钟根：每个根都有独立源列表，必须使用属于当前根的 `IMX_CCM_MUX_<root>_<source>` 标识。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `nxp,root-id` | `int` | **必需**。HAL据以分派操作的统一时钟根标识（Flat Clock-root Identifier），即CLOCK_SetRootClock()接收的clock_root_t值，应使用SoC的 `IMX_CCM_ROOT_*` 宏填写。特意要求显式声明，而不从reg推导：reg是参考手册中的寄存器块，nxp,root-id是HAL使用的编号，两者描述同一硬件分片（Slice）的不同事实。从一个推算另一个需要SoC专属规则，即实例标识起点加上偏移除以分片步长；若共享驱动固定此规则，后续SoC可能使其失效，且各值仍看似合理而悄然出错。因此此项必填、没有默认值；错误标识会配置另一个分片。 |
| `clock-mux` | `int` | **必需**。当前时钟根的源选择器（Source Selector），取自SoC的 `IMX_CCM_MUX_<root>_<source>` 定义。Mux编号由各根独立定义；使用其他根的值会选中无关的时钟源。 |
| `clock-div` | `int` | 对所选源应用的分频值（Divider），填写实际除数，而非编码后的寄存器字段。；默认值：`1` |
| `clock-second-div` | `int` | 第二级分频器（Second Divider）；只有一级分频器的SoC忽略此项。默认值为1，因为这些属性保存实际除数，1表示一分频，0没有意义。这也避免一种与HAL版本有关的风险：HAL按value−1写硬件字段，未防护的实现会把0变成全1字段，随后频率计算会读回该字段并据此计算外设频率。RT266x实板初始移植曾遇到此问题。当前RT266x HAL已对0作特殊处理、写成一分频，但此绑定不限定SoC，不能假定所有HAL均如此。；默认值：`1` |
| `clock-shutdown` | `boolean` | 配置完复用选择器与分频器后，保持当前时钟根被门控关闭（Gated Off），不使其运行。 |
| `nxp,preconfigured` | `boolean` | 控制器**不得重新配置**此时钟根：其值在Zephyr运行前已经确定，即使重写相同值也会破坏工作状态。节点仍声明复用选择器和分频器，使配置由设备树保存且get_rate能够报告频率，但控制器初始化循环会跳过它。此属性表示“绝不能触碰”，并非“其他代码也会配置”。若SoC启动代码读取同一节点配置该根，则不应标记：控制器之后重写现有值是幂等（Idempotent）操作，无需保护；乱用标记会掩盖真正不能重写的根。符合条件的是启动介质（Boot Medium）时钟路径上的根：①当前镜像执行所用存储器的功能时钟根。控制器循环及所调用HAL函数都可能在原地执行闪存（Execute In Place，XIP Flash）中运行，重配会切断正在进行的取指所需时钟。安全操作需要先让控制器静止并禁用它、临时切换到自由运行源、从片上RAM执行；PRE_KERNEL_1设备初始化无法做到这些。②启动ROM已按其频率校准的时钟根，必须逐位保留而非重新计算。i.MX RT266x的XSPI1／PSRAM根固定在ROM的分频值上，因为ROM延迟锁定环（Delay-Locked Loop，DLL）校准点依赖此频率；即使改成看似等效的值，也会使ROM DLL锁定的DDR读选通不再对齐。③上述根的任一源根，修改它同样改变派生频率。是否位于启动介质路径是开发板事实，而非SoC事实。SoC设备树为常见启动配置标记这些根；从不同介质启动的开发板应在自己的DTS中用 `/delete-property/` 删除标记。此项不能由Kconfig驱动：设备树先于Kconfig处理，`cmake/modules/zephyr_default.cmake` 将dts排在kconfig前，设备树阶段生成Kconfig.dts供Kconfig使用，因此这里没有可见的CONFIG_符号。另有一个限制：对于XSPI功能根，SoC用驻留RAM的代码直接写寄存器，运行时闪存时钟已临时切换。节点允许报告频率并显式声明目标mux／div，但修改属性尚不会改变该代码的写入值，因为它无法在运行时读取设备树。要由设备树驱动，需先将推导出的寄存器值预计算到片上RAM，这是另一项改动。不符合上述条件的根不应加此属性：它应进入控制器初始化循环，或由拥有它的外设通过clock_control_configure()配置。 |

本页没有已弃用的节点专用属性。

## 19.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。硬件分片（Slice）在父CCM实例内的寄存器块：参考手册中该实例的CLOCK_ROOT<N>对应偏移 `N * <stride>`、大小 `<stride>`。步长随SoC变化，RT266x为0x10、RT1170为0x80、RT1180为0x40，即对应SoC的CLOCK_ROOT寄存器数组步长。 |
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

## CLOCK_ROOT40配置原例

```dts
    peri3_rootclk: clock-root@280 {
            compatible = "nxp,imx-ccm-rev3-root";
            reg = <0x280 0x10>;
            nxp,root-id = <IMX_CCM_ROOT_CGU_PERI_ROOTCLK3>;
            clock-mux = <IMX_CCM_MUX_PERI3_MAINPLL_DIVX>;
            clock-div = <1>;
    };
```

## 19.3\_寄存器块命名原例

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

[上一章](P018_nxp_imx-ccm-rev2.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_nxp_imx-ccm-rev3.md)
