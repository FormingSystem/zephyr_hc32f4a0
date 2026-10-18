---
id: learning.zephyr-docs.qspi-ospi-xspi-binding-reference.page-14
title: nxp_s32-xspi
kind: reference
status: maintained
domains: [zephyr, devicetree, qspi, ospi, xspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/xspi/nxp,s32-xspi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第14章\_nxp_s32-xspi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/xspi/nxp,s32-xspi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-s32-xspi"></a>
<a id="dtbinding-nxp-s32-xspi"></a>
<a id="std-dtcompatible-nxp-s32-xspi"></a>

兼容字符串（Compatible String）：`nxp,s32-xspi`。厂商：[ NXP ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,s32-xspi)。

驱动源码（Driver Source）：[drivers/memc/memc_nxp_s32_xspi.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_nxp_s32_xspi.c)。

<a id="description"></a>

NXP S32扩展串行外设接口（eXpanded Serial Peripheral Interface，XSPI）控制器。

最多连接两个串行闪存设备；根据平台，每个设备最多具有8条双向数据线。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 14.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `data-rate` | `string` | 选择读取模式：单倍数据速率（Single Data Rate，SDR）在单个边沿采样输入数据；双倍数据速率（Double Data Rate，DDR）在两个边沿采样。；合法值：`SDR, DDR` |
| `hold-time-2x` | `boolean` | 在DDR模式下，将输入数据与2倍串行闪存半时钟对齐；未设置时与控制器内部参考时钟的上升沿对齐。 |
| `sample-delay-half-cycle` | `boolean` | 采样接收数据时，使用提前半周期的DQS延迟。 |
| `sample-phase-inverted` | `boolean` | 使用反相时钟采样接收数据。 |
| `cs-setup-time` | `int` | 片选建立时间，以串行时钟周期数表示。值越大，事务开始前越早使CS有效；必须大于或等于2。；默认值：`2` |
| `cs-hold-time` | `int` | 片选保持时间，以串行时钟周期数表示。值越大，事务结束后越晚释放CS；必须大于或等于2。；默认值：`2` |
| `column-space` | `int` | 列地址空间位宽。例如列地址位于`XSPI_SFAR`／AHB地址的位2:0时，位宽必须为3。如果所有连接的串行闪存均无列地址分隔，必须设为0。默认值对应字段复位值。；默认值：`0` |
| `word-addressable` | `boolean` | 串行闪存控制器按字（2字节）寻址时为真。 |
| `dword-addressable` | `boolean` | 串行闪存控制器按字（4字节）寻址时为真。 |
| `byte-swapping` | `boolean` | 八线DDR模式下，指定是否交换单个DQS周期上升沿及下降沿取得的两个字节，这两个字节组成一个字。 |
| `ahb-buffers-masters` | `array` | AHB接收缓冲区的主设备ID。检查每个输入请求的主设备ID，在其关联缓冲区返回或提取数据；最大缓冲区数量取决于SoC。 |
| `ahb-buffers-sizes` | `array` | AHB接收缓冲区的大小，单位为字节；最大缓冲区大小及数量取决于SoC。 |
| `ahb-buffers-all-masters` | `boolean` | 未关联到其他缓冲区的主设备访问，都路由至最后一个缓冲区。 |
| `a-rx-clock-source` | `string` | 选择A侧读取采样的DQS时钟源：`LOOPBACK`和`LOOPBACK_DQS`均使用焊盘回环时钟作选通信号；`EXTERNAL_DQS`使用外部选通信号。；合法值：`LOOPBACK, LOOPBACK_DQS, EXTERNAL_DQS` |
| `a-io2-idle-high` | `boolean` | 要求非活动状态下控制器IO2输出为高电平时设置；适用于A侧。 |
| `a-io3-idle-high` | `boolean` | 要求非活动状态下控制器IO3输出为高电平时设置；适用于A侧。 |
| `a-dll-mode` | `string` | 延迟锁定环（Delay-Locked Loop，DLL）模式，支持的模式取决于SoC；适用于A侧。；合法值：`BYPASSED, AUTO_UPDATE` |
| `a-dll-freq-enable` | `boolean` | 选择用于高频运行的延迟链（Delay Chain）；适用于A侧。 |
| `a-dll-ref-counter` | `int` | 选择DLL相位检测及参考延迟更新的“n+1”间隔。建议最小值为1，即复位值；适用于A侧。；默认值：`1`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `a-dll-resolution` | `int` | DLL相位检测器根据闪存时钟抖动维持锁定／失锁的最小分辨率。最小值为2，即复位值；适用于A侧。；默认值：`2`；合法值：`2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `a-dll-coarse-delay` | `int` | 设置每个延迟抽头的延迟单元数量，用于覆盖DLL生成的延迟值；适用于A侧。；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `a-dll-fine-delay` | `int` | 设置输入DQS的微调偏移延迟单元数量，最多16个，默认应为1个；适用于A侧。；默认值：`1`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `a-dll-tap-select` | `int` | 选择从延迟链提供的第N个抽头；适用于A侧。；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `a-differential-clock` | `boolean` | 在A侧CKN焊盘启用差分时钟输出（Differential Clock Output）。 |
| `dqs-as-an-output` | `boolean` | 启用DQS输出操作。当写数据阶段控制器也输出数据选通信号时，本字段有效；适用于HyperRAM，其数据选通信号承担读写数据选通（Read Write Data Strobe，RWDS）功能。 |
| `enable-hresp-mask` | `boolean` | 屏蔽AHB错误响应（Error Response）。启用后，访问错误不产生AHB错误响应，而在AHB读数据总线上返回错误载荷（Error Payload）。 |
| `error-payload-high` | `int` | 启用AHB HRESP错误屏蔽且发生访问错误时，在AHB读数据总线上返回的错误载荷高32位字。 |
| `error-payload-low` | `int` | 启用AHB HRESP错误屏蔽且发生访问错误时，在AHB读数据总线上返回的错误载荷低32位字。 |
| `ahb-timeout` | `int` | AHB超时计数器值，以50,000个AHB时钟周期为单位。XSPI不响应AHB传输、持续拉低HREADY时，开始计数。 |
| `transaction-timeout` | `int` | 用于中止进行中的读／写命令的事务超时计数器值。目标队列访问赢得仲裁且XSPI进入IDLE时开始计数，原文括注为`FSM_STAT`状态字段非`00`。 |
| `arbitration-timeout` | `int` | 仲裁锁超时计数器值。目标组锁定仲裁时开始计时；主设备未在计数到期前释放仲裁锁，则产生超时错误。 |
| `tg1-fixed-priority` | `boolean` | 为目标组1（Target Group 1，TG1）启用固定优先级。禁用时，TG1与其他目标组队列按先来先服务调度，TG0除外；启用时，TG1优先级高于除TG0以外的全部队列。 |
| `lock-configuration` | `boolean` | 初始化后锁定配置寄存器，直到下次复位。启用后，初始化阶段结束时所有配置寄存器变为只读。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 14.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `max-program-buffer-size` | `int` | **必需**。闪存设备的最大编程页缓冲区大小，以该闪存数据手册为准。 |
| `write-block-size` | `int` | **必需**。写操作使用的字节数。 |
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
| `jedec-id` | `uint8-array` | JEDEC标识，依次为制造商标识（Manufacturer ID）、存储器类型（Memory Type）及存储密度（Memory Density）。 |
| `size` | `int` | 闪存容量，单位为位（Bits）。 |
| `sfdp-bfp` | `uint8-array` | 包含JESD216串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的基本闪存参数（Basic Flash Parameters，BFP）表中的32位字，按小端字节序（Little-endian Byte Order）存放。在不希望运行时读取SFDP数据的情况下，用于提供特定闪存的配置。 |
| `sfdp-ff05` | `uint8-array` | 包含JESD216 SFDP xSPI Profile 1.0表的32位字，按小端字节序存放。 |
| `sfdp-ff84` | `uint8-array` | 包含JESD216 SFDP四字节地址指令参数表（4-byte Address Instruction Parameter Table）的32位字，按小端字节序存放。 |
| `quad-enable-requirements` | `string` | JESD216 BFP第15个双字（DW15）中的四线使能要求（Quad Enable Requirements）值。<br>设备通过指令识别1-1-4及1-4-4模式时使用`NONE`。若四线使能位QE位于第一个状态寄存器字节的第6位，并可通过`RDSR`读一个字节、再以`WRSR`写一个字节来配置，则使用`S1B6`。其他字段含义见规范。；合法值：`NONE, S2B1v1, S1B6, S2B7, S2B1v4, S2B1v5, S2B1v6` |
| `enter-4byte-addr` | `int` | JESD216 BFP DW16中的进入四字节寻址（Enter 4-Byte Addressing）值。<br>配置为通过`sfdp-bfp`取得SFDP数据（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时，本属性忽略。<br>在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下，本属性为DW16的31:24位构成的8位值，用来标示设备进入四字节寻址模式的方法。提供非零值时，驱动认为访问完整地址范围需要四字节寻址，并在初始化设备时自动切换到此模式。 |
| `page-size` | `int` | JESD216 BFP DW11规定的每页字节数。<br>仅在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下使用。通过`sfdp-bfp`提供SFDP（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时从设备读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时忽略。未指定时默认256字节。 |

## 14.3\_寄存器块命名原例

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

[上一章](P013_nxp_s32-xspi-sfp-mdad.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_nxp_xspi.md)
