---
id: learning.zephyr-docs.clock-nordic-nuvoton-nxp-binding-reference.page-20
title: nxp_imx-ccm-rev3
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imx-ccm-rev3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第20章\_nxp_imx-ccm-rev3

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imx-ccm-rev3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-imx-ccm-rev3"></a>
<a id="dtbinding-nxp-imx-ccm-rev3"></a>
<a id="std-dtcompatible-nxp-imx-ccm-rev3"></a>

兼容字符串（Compatible String）：`nxp,imx-ccm-rev3`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,imx-ccm-rev3)。

驱动源码（Driver Source）：[drivers/clock_control/clock_control_mcux_ccm_rev3.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_mcux_ccm_rev3.c)。

<a id="description"></a>

NXP i.MX第三版时钟控制器模块（Clock Controller Module，CCM rev3）。

CCM将外设时钟表示为两个独立对象：控制总线时钟及功能时钟开关的时钟门（Gate，LPCG），以及通过复用选择器（Mux）和分频器决定频率的时钟根（Clock Root）。二者的标识空间互不相关，但都必须传给驱动。

共享NXP外设驱动只读取一个时钟单元 `DT_INST_CLOCKS_CELL(n, name)`，并将同一个值传给clock_control_on()、clock_control_get_rate()和clock_control_configure()，因此看不到第二个单元。两个标识用 `IMX_CCM_CLK()` 打包进一个单元，原始LPUART配置见下方。没有独立门的外设使用IMX_CCM_GATE_NONE；没有专用根时使用IMX_CCM_ROOT_NONE，查询后者频率会返回−ENOTSUP。

可配置时钟根是兼容字符串为 `nxp,imx-ccm-rev3-root` 的子节点。控制器初始化时按设备树顺序配置全部已启用子节点，使开发板或应用Overlay能单独改变某个根而无需修改C代码；下方保留peri3_rootclk原例。

### 逐设备时钟根：名为source的时钟条目

时钟根子节点描述配置，却不说明哪个外设依赖它。因此修改外设频率通常涉及两处：外设节点的门和频率查询，以及CCM子节点的Mux和分频器。若外设独占其根，可把配置放在自身clocks属性中，作为门条目之后的第二个条目；下方保留带gate／source的LPUART原例。

此时有两类单单元时钟说明符，均为 `#clock-cells = 1`：`IMX_CCM_CLK(gate, root)` 是普通门及频率查询单元，由clock_control_on()／clock_control_get_rate()读取，示例命名为gate；`IMX_CCM_ROOT_CFG(root, mux, div, snd_div)` 是根配置单元，携带根、源选择器和两个分频器，与根子节点属性相同，两个除数都不能为0，名称始终是source。

两类单元通过最高半字节（Top Nibble）中的固定标记区分，该标记不可能由门单元产生。共享LPUART和LPSPI驱动已会无条件把门单元传给clock_control_configure()，控制器须忽略它，不能误当成根配置。

clock-names负责选择根配置单元：使用者驱动按source名称查找，在开启外设门之前传给clock_control_configure()。这样在设备真正启动时配置其根，而非控制器初始化时配置所有根。未提供source名称的节点，包括没有时钟根的NXP系列，保持既有行为；同一驱动服务两种情况。

source是此绑定唯一保留名称。clock-names的其他名称由使用者驱动定义：FlexCAN和WDOG32使用clksrc0／clksrc1并通过clk-source选择，系统计数器使用base／slow，MIPI-DSI使用dphy／esc／pixel。强制第0项统一命名会冲突。驱动未指定名称时可用gate，如这里的LPUART和LPSPI；已有名称的外设保留名称并追加source。按名称而非索引查找，保证追加安全。

source和FlexCAN的clksrc0／clksrc1虽然都像是在选时钟源，实际属于不同层级的Mux，不能相互替代。clksrcN是完整门单元，指向不同上游时钟；clk-source既选择驱动使用哪一项，也写入CAN引擎内部的1位Mux。source不新增时钟，而是携带gate已指向的同一时钟根的Mux及分频参数，位置在IP外的CCM中。因此clksrcN传给clock_control_on()／clock_control_get_rate()，source只传给clock_control_configure()；clksrc0与clksrc1二选一，source则是附加项且最多一项。

这对外设提出两项限制。第一，使用者驱动必须显式支持source查找和clock_control_configure()调用；未支持时该单元只是不会生效的设备树数据，应继续用CCM子节点配置根。第二，不要为会读取clocks索引1及以后条目作自身用途的驱动追加source。树内USB EHCI的udc／uhc驱动把第1项当作USB PHY时钟；相关分支还要求第二个clock-rates元素才会发生误读，但节点无论如何都不正确，此类根应保留为CCM子节点。若根配置单元被误传给clock_control_on()，启动时的门范围检查会返回−EINVAL。

每个外设节点最多携带一个根配置单元，经多个根供钟的外设须保留CCM子节点。一个根只能由外设节点或CCM子节点中的一方拥有；两方同时写会竞争，最后写入者悄然覆盖另一方。多个外设共享的根也保留为CCM子节点。

### 单实例与多实例

某些SoC把CCM实现为单个可寻址块，另一些按子系统拆成多个实例。声明方法一致：每个硬件实例一个节点，具有自己的reg和时钟根子节点；驱动逐节点实例化设备，单块SoC无需特殊处理。

时钟根和时钟门的标识空间在全部实例之间统一，HAL按各实例标识范围确定归属。因此使用者的clocks节点引用（Phandle）表示时钟服务，而非特定块；任一实例都能解析任一说明符，单元中的标识已指出资源所属子系统。多实例SoC中应为使用者选择最自然的实例引用并保持一致。

时钟根子节点的reg描述配置它的寄存器块。参考手册在每个实例内用CLOCK_ROOT<N>编号硬件分片；每片占用固定、随SoC变化的步长：RT266x为0x10、RT1170为0x80、RT1180为0x40，因此根的reg为 `<N * stride  stride>`。下方保留含CLOCK_ROOT3的实例原例。

HAL则使用跨实例的统一根标识。标识不从reg推导，而由各根的nxp,root-id声明，因此绑定不需要每实例标识基数，驱动也不依赖可能被其他SoC编号方式破坏的算术规则。应将根放在标识范围包含它的实例下。这一放置用于描述硬件：HAL按标识而非节点位置解析实例，所以放错父实例仍可能正确配置，却错误描述硬件。跨实例初始化顺序取决于设备树依赖序号（Dependency Ordinal），不是节点书写顺序；需要固定相对顺序的两个根必须是同一实例的子节点。

### 与nxp,imx-ccm-rev2的关系

rev3是rev2的超集（Superset），绑定刻意不限定SoC，以便接纳rev2使用者。RT1176和RT1189同样用clock_lpcg_t标识门控外设，用 `CLOCK_SetRootClock(root, {clockOff, mux, div})` 配置根；rev3只增加第二级分频器。rev2声明name、offset、bits三个单元，但驱动仅读取第0项，其余两项没有提供信息。

迁移一个SoC需要：①将每个外设的 `<name offset bits>` 替换为 `IMX_CCM_CLK(gate, root)`；②将soc.c中的CLOCK_SetRootClock()序列表达为nxp,imx-ccm-rev3-root子节点；③删除rev2驱动逐外设switch中该SoC的分支。第一步会影响该系列全部开发板设备树，因此原文此次没有进行迁移。已知例外是i.MX 93和i.MX 95：它们通过CLOCK_GetIpFreq()而非CLOCK_GetRootClockFreq()解析外设频率，需要单独评估，可能更适合继续使用rev2。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 20.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`1` |

本页没有已弃用的节点专用属性。

## 20.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `ranges` | `compound` | 任何声明时钟根子节点的实例都必须提供此项，才能将子节点寄存器块映射到实际地址；没有子节点的实例可以省略。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
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

## 时钟定义头文件原始引用

```dts
    #include <nxp/imxrt/imxrt266x/clock/imx_ccm_rev3_rt266x.h>
```

## CCM门、根与实例原例

单单元门与时钟根标识：

```dts
    lpuart0: serial@42190000 {
            compatible = "nxp,lpuart";
            clocks = <&ccm IMX_CCM_CLK(IMX_CCM_LPCG_MAIN_HSP_LPUART0,
                                       IMX_CCM_ROOT_MAIN_LPUART0_FCLK)>;
    };
```

单独修改时钟根的覆盖原例：

```dts
    &peri3_rootclk {
            clock-mux = <IMX_CCM_MUX_PERI3_SYSPLL_DIVOUT2>;
    };
```

在外设节点添加source条目的原例：

```dts
    lpuart0: serial@42190000 {
            compatible = "nxp,lpuart";
            clock-names = "gate", "source";
            clocks = <&ccm IMX_CCM_CLK(IMX_CCM_LPCG_MAIN_HSP_LPUART0,
                                       IMX_CCM_ROOT_MAIN_LPUART0_FCLK)>,
                     <&ccm IMX_CCM_ROOT_CFG(IMX_CCM_ROOT_MAIN_LPUART0_FCLK,
                                            IMX_CCM_MUX_LPUART0_PERI3, 5, 1)>;
    };
```

带CLOCK_ROOT3子节点的CCM实例：

```dts
    cmpt_ccm: clock-controller@44060000 {
            compatible = "nxp,imx-ccm-rev3";
            reg = <0x44060000 0x4000>;
            #clock-cells = <1>;
            #address-cells = <1>;
            #size-cells = <1>;
            ranges = <0x0 0x44060000 0x4000>;

            /* CLOCK_ROOT3 */
            systick_rootclk: clock-root@30 {
                    compatible = "nxp,imx-ccm-rev3-root";
                    reg = <0x30 0x10>;
                    nxp,root-id = <IMX_CCM_ROOT_CMPT_SYSTICK_CLK0>;
                    clock-mux = <...>;
            };
    };
```

## 20.3\_寄存器块命名原例

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

<a id="specifier-cell-names"></a>

## 说明符单元名称

clock cells：`name`。依次为时钟标识。

---

[上一章](P019_nxp_imx-ccm-rev3-root.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P021_nxp_imx-ccm.md)
