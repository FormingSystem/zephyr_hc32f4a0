---
id: learning.zephyr-docs.modem-fibocom-nordic-quectel-binding-reference.page-6
title: quectel_bc66
kind: reference
status: maintained
domains: [zephyr, devicetree, modem]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/modem/quectel,bc66.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_quectel_bc66

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/modem/quectel,bc66.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="quectel-bc66-on-uart-bus"></a>
<a id="dtbinding-quectel-bc66"></a>
<a id="std-dtcompatible-quectel-bc66"></a>

兼容字符串（Compatible String）：`quectel,bc66`。厂商：[ Quectel Wireless Solutions Co., Ltd. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-quectel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=quectel,bc66)。

<a id="description"></a>

Quectel BC66窄带物联网调制解调器（Narrowband Internet of Things Modem，NB-IoT Modem）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mdm-boot-gpios` | `phandle-array` | **必需**。启动引脚（BOOT Pin），即PWRKEY。 |
| `mdm-rst-gpios` | `phandle-array` | **必需**。复位引脚（RST Pin）。 |
| `mdm-psm-gpios` | `phandle-array` | **必需**。省电模式引脚（Power Saving Mode Pin，PSM Pin），即PSM_EINT。 |
| `mdm-power-gpios` | `phandle-array` | 调制解调器电源控制GPIO（Power Control GPIO）。 |
| `mdm-reset-gpios` | `phandle-array` | 调制解调器复位GPIO（Reset GPIO）。 |
| `zephyr,mdm-reset-behavior` | `string-array` | 调制解调器复位GPIO行为（Reset GPIO Behavior）。`hold_on_suspend`：模块挂起时保持复位GPIO有效，即逻辑高；模块从空闲恢复时释放复位GPIO，即逻辑低。`toggle_on_resume`：从挂起恢复时切换复位GPIO。`toggle_on_recovery`：触发模块恢复流程时切换复位GPIO，例如模块不响应初始化AT命令时。可通过字符串数组同时指定多种行为。；合法值：`hold_on_suspend, toggle_on_resume, toggle_on_recovery` |
| `mdm-wake-gpios` | `phandle-array` | 调制解调器唤醒GPIO（Wake GPIO）。 |
| `mdm-ring-gpios` | `phandle-array` | 调制解调器振铃指示GPIO（Ring Indicator GPIO）。 |
| `mdm-dtr-gpios` | `phandle-array` | 调制解调器数据终端就绪GPIO（Data Terminal Ready，DTR）。UART活动时置为有效，即逻辑高；UART不活动、掉电或处于低功耗模式时置为无效，即逻辑低。 |
| `mdm-status-gpios` | `phandle-array` | 报告调制解调器电源状态（Power Status）的GPIO，按输入读取。模块已上电时信号有效；提供此属性后，驱动在启动时读取该信号，若模块已经运行则跳过上电脉冲，避免仅MCU复位时反而将仍在运行的模块关闭。未接线时应省略。 |
| `cmux-enable-runtime-power-save` | `boolean` | 使用CMUX串口复用的节能控制命令（Power Saving Control，PSC）启用运行时节能（Runtime Power Saving）。要求模块在保持数据连接活动时支持CMUX与PSC命令。 |
| `cmux-close-pipe-on-power-save` | `boolean` | 进入节能模式时关闭调制解调器管道（Modem Pipe）；启用运行时电源管理（Runtime Power Management）时会关闭UART。要求模块能够通过RING信号唤醒UART。 |
| `cmux-no-powersave-handshake` | `boolean` | 进入和退出节能模式时均跳过CMUX带内节能握手（In-Band Power-Save Handshake）。框架直接在已连接与节能状态之间转换；要求模块通过CMUX之外的硬件线路控制睡眠与唤醒，而非带内响应。 |
| `autostarts` | `boolean` | 模块上电后自动启动、不需要外部电源或复位脉冲时设置。设置后，主机先等待模块就绪指示（Ready Indication），再发送AT命令。 |
| `cmux-idle-timeout-ms` | `int` | CMUX进入节能模式前的等待时间（Power-Save Timeout），单位毫秒。；默认值：`10000` |
| `zephyr,use-default-pdp-ctx` | `int` | 模块注册到网络时会自动配置并连接默认分组数据协议上下文（Packet Data Protocol Context，PDP Context），其 `cid=0`。设为1时，驱动不配置任何接入点名称（Access Point Name，APN），也不通过 `AT+CGACT` 激活PDP上下文。采用枚举（Enum）定义，允许设备专用绑定覆盖默认值。；合法值：`0, 1` |
| `zephyr,use-default-apn` | `int` | 模块注册到网络时自动配置接入点名称（APN）。设为1时，驱动使用 `AT+CGDCONT=1,"IP",""` 配置PDP上下文，并将APN名称传为空字符串。采用枚举（Enum）定义，允许设备专用绑定覆盖默认值。；合法值：`0, 1` |

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

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

## 6.3\_寄存器块命名原例

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

[上一章](P005_openisa_rv32m1-genfsk.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_quectel_bc660k.md)
