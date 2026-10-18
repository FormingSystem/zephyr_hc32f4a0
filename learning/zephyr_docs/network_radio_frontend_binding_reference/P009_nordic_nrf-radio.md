---
id: learning.zephyr-docs.network-radio-frontend-binding-reference.page-9
title: nordic_nrf-radio
kind: reference
status: maintained
domains: [zephyr, devicetree, networking, radio]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/net/wireless/nordic,nrf-radio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_nordic_nrf-radio

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/net/wireless/nordic,nrf-radio.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-nrf-radio"></a>
<a id="dtbinding-nordic-nrf-radio"></a>
<a id="std-dtcompatible-nordic-nrf-radio"></a>

兼容字符串（Compatible String）：`nordic,nrf-radio`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf-radio)。

<a id="description"></a>

Nordic nRF系列无线电外设（RADIO Peripheral）。

控制nRF5x SoC上的2.4 GHz无线收发器，可用于蓝牙、IEEE 802.15.4和专有无线协议。并非所有SoC都支持全部这些协议，具体以产品规格为准；此绑定不适用于nRF91x基带无线电（Baseband Radio）。

前端模块（Front-End Module，FEM）支持：外部FEM用于扩展无线通信距离，提升链路可靠性和链路预算（Link Budget）。系统使用外部FEM时，通过本绑定的 `fem` 属性配置，完整原例见后文。目前支持的FEM兼容字符串为 [`radio-fem-two-ctrl-pins`](P012_radio-fem-two-ctrl-pins.md) 和 [`nordic,nrf21540-fem`](P011_nordic_nrf21540-fem.md)，具体配置参见对应绑定。

测向扩展（Direction Finding Extension，DFE）：部分无线电支持蓝牙DFE，支持时会设置 `dfe-supported`。`dfegpio[n]-gpios` 配置用于驱动天线切换的GPIO，每项初始化对应的 `PSEL.DFEGPIO[n]` 寄存器。由于具体使用哪些寄存器取决于场景，这些属性均未标为必需；但DFE至少需要两根天线，因此至少要提供一个这样的GPIO属性，使无线电能够在两根天线间切换。12根天线需要4个GPIO，因为4位最多可切换16根天线。GPIO按属性索引顺序使用，该顺序决定天线切换模式与引脚的映射。

天线切换模式（Antenna Switching Pattern）是二进制数，每一位作用于一个天线GPIO。例如 `0x3` 使索引0、1的GPIO置位，后续GPIO不置位。配置的GPIO数量限制模式数量和值域；使用4个GPIO时，模式数不得超过16，最大模式值为15。通过写入 `SWITCHPATTERN` 寄存器将模式存入DFE内部存储器。DFE代码在恒定音调扩展（Constant Tone Extension，CTE）的接收过程，即到达角模式（Angle of Arrival，AoA），或发送过程，即出发角模式（Angle of Departure，AoD）中应用这些模式。

DFE有四种工作状态：

- 空闲（Idle）：发送协议数据单元（Protocol Data Unit，PDU），使用 `SWITCHPATTERN[0]` 选择天线；无线电控制器代码把下述 `dfe-pdu-antenna` 属性值写入此项。
- 保护（Guard）：准备接收或发送CTE，使用 `SWITCHPATTERN[1]` 选择天线。
- 参考（Reference）：开始接收或发送CTE；在AoA模式下收集参考同相／正交采样（In-Phase/Quadrature Samples，IQ Samples），所用天线与保护状态相同。
- 切换采样（Switch-Sample）：执行实际天线切换，依次应用 `SWITCHPATTERN[2..N]`。若切换采样周期数超过已存储的模式数量，则回到 `SWITCHPATTERN[2]` 循环。

译注：`dfegpio0-gpios` 的原始说明示例实际写成 `dfegpio1-gpios`。下方保持原例，不能把该编号差异理解为属性别名。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `fem` | `phandle` | 将RADIO节点连接到外部前端模块（FEM）的节点引用。 |
| `coex` | `phandle` | 将RADIO节点连接到外部无线电共存仲裁器（Radio Coexistence Arbitrator）的节点引用。 |
| `dfe-supported` | `boolean` | 表示无线电硬件支持测向扩展（DFE）。此属性应视为只读（Read-Only），不应覆盖；目标SoC已经提供正确值。 |
| `dfe-antenna-num` | `int` | DFE可用天线数量（Antenna Count）。仅在 `dfe-supported` 为真时设置，设置值至少为2。 |
| `dfe-pdu-antenna` | `int` | 在开始发送CTE之前，用于发送PDU的天线切换模式（Antenna Switch Pattern）。仅在 `dfe-supported` 为真时设置。此模式存放在实际天线切换模式之前的 `SWITCHPATTERN[0]`；无线电释放天线切换GPIO控制权时，也用此模式驱动GPIO。 |
| `dfegpio0-gpios` | `phandle-array` | DFE引脚0的引脚选择（Pin Select），仅在 `dfe-supported` 为真时设置。后文原例分别使用nRF5x的P0.2和P1.4；属性最后一个 `flags` 单元不使用，应按原例设为0。；长度范围：`1 to 1` |
| `dfegpio1-gpios` | `phandle-array` | DFE引脚1的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio2-gpios` | `phandle-array` | DFE引脚2的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio3-gpios` | `phandle-array` | DFE引脚3的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio4-gpios` | `phandle-array` | DFE引脚4的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio5-gpios` | `phandle-array` | DFE引脚5的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio6-gpios` | `phandle-array` | DFE引脚6的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `dfegpio7-gpios` | `phandle-array` | DFE引脚7的引脚选择（Pin Select），参见 `dfegpio0-gpios`。；长度范围：`1 to 1` |
| `ieee802154-supported` | `boolean` | 表示无线电硬件支持IEEE 802.15.4模式。 |
| `ble-2mbps-supported` | `boolean` | 支持2 Mbps物理层（Physical Layer，PHY），对应蓝牙5.0规范。 |
| `ble-coded-phy-supported` | `boolean` | 支持用于长距离通信（Long Range）的编码物理层（Coded PHY），对应蓝牙5.0规范。 |
| `ble-cte-tx-supported` | `boolean` | 支持以出发角（AoD）模式进行测向的CTE发送，对应蓝牙5.1规范。 |
| `ble-cte-rx-supported` | `boolean` | 支持以到达角（AoA）模式进行测向、带IQ采样的CTE接收；需要 `ble-cte-tx-supported` 能力，对应蓝牙5.1规范。 |
| `ble-cs-supported` | `boolean` | 支持BLE信道探测（Channel Sounding）特性，对应蓝牙6.0规范。 |
| `radio-tx-high-power-supported` | `boolean` | 表示无线电硬件支持高发射功率设置（High TX Power），可超过标准功率等级，通常大于10 dBm。此属性应视为只读，不应覆盖；目标SoC已经提供正确值。 |

本页没有已弃用的节点专用属性。

## 9.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

## 无线电外部前端配置原例

```dts
  &radio {
          fem = <&nrf_radio_fem>;
  };
```

```dts
  nrf_radio_fem: my-fem {
          compatible = "...";
          ....
  };
```

## DFE引脚选择原例

原例：使用P0.2。

```dts
  dfegpio1-gpios = <&gpio0 2 0>;
```

原例：使用P1.4。

```dts
  dfegpio1-gpios = <&gpio1 4 0>;
```

## 9.3\_寄存器块命名原例

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

[上一章](P008_nordic_nrf-nfct.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nordic_nrf21540-fem-spi.md)
