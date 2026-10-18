---
id: learning.zephyr-docs.charger-binding-reference.page-18
title: x-powers_axp2101-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/x-powers,axp2101-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第18章\_x-powers_axp2101-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/x-powers,axp2101-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="x-powers-axp2101-charger-on-axp2101-bus"></a>
<a id="dtbinding-x-powers-axp2101-charger"></a>
<a id="std-dtcompatible-x-powers-axp2101-charger"></a>

兼容字符串（Compatible String）：`x-powers,axp2101-charger`。厂商：[ X-Powers ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-x-powers)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=x-powers,axp2101-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_axp2101.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_axp2101.c)。

<a id="description"></a>

AXP2101电源管理单元（Power Management Unit，PMU）多功能设备（Multi-function Device，MFD）的充电器部分。

<a id="examples"></a>

## 充电器配置原例

```dts
axp2101@34 {
  compatible = "x-powers,axp2101";
  reg = <0x34>;

  charger {
    compatible = "x-powers,axp2101-charger";
    constant-charge-current-max-microamp = <300000>;
    constant-charge-voltage-max-microvolt = <4200000>;
  };

  regulators {
  ...
  }
}
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 18.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `constant-charge-current-max-microamp` | `int` | **必需**。最大恒定输入电流（Maximum Constant Input Current）；合法值：`100000, 125000, 150000, 175000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000` |
| `constant-charge-voltage-max-microvolt` | `int` | **必需**。最大恒定输入电压（Maximum Constant Input Voltage）；合法值：`4000000, 4100000, 4200000, 4350000, 4400000` |
| `charge-term-current-microamp` | `int` | 充电终止阶段（Charge Termination Phase）的电流；合法值：`0, 25000, 50000, 75000, 100000, 125000, 150000, 200000` |
| `vbackup-enable` | `boolean` | 启动时使能Vbackup，通常用于给某些实时时钟（Real-time Clock，RTC）芯片使用的纽扣电池充电 |
| `ts-disable` | `boolean` | 温度传感器（Temperature Sensor）默认使能。某些开发板省略传感器，改用100 Ω电阻将TS引脚接地；这种情况下必须设置TS禁用位，否则充电器会报故障 |
| `device-chemistry` | `string` | 描述电池的化学体系（Chemical Technology）。lithium-ion是所有锂离子电池（Lithium-ion Battery）的通用类型；未知具体化学体系时，可使用此值代替更精确的lithium-ion-X选项；合法值：`nickel-cadmium, nickel-metal-hydride, lithium-ion, lithium-ion-polymer, lithium-ion-iron-phosphate, lithium-ion-manganese-oxide` |
| `ocv-capacity-table-0` | `array` | 开路电压（Open-circuit Voltage，OCV）数组，根据当前OCV值查询电池容量，电压单位微伏。与Linux对应属性不同，此数组必须恰有11个元素，以10%为步进，表示0%至100%电量所对应的电压 |
| `charge-full-design-microamp-hours` | `int` | 电池设计容量（Battery Design Capacity） |
| `re-charge-voltage-microvolt` | `int` | 自动重新开始充电的阈值 |
| `precharge-current-microamp` | `int` | 预充电阶段（Pre-charge Phase）的电流 |
| `factory-internal-resistance-micro-ohms` | `int` | 电池出厂内阻（Factory Internal Resistance） |

本页没有已弃用的节点专用属性。

## 18.2\_基础属性

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

译注：原示例末尾节点缺少部分分号，原样保留，使用时需按设备树语法检查。

## 18.3\_寄存器块命名原例

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

[上一章](P017_ti_bq25713.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_zephyr_charger-gpio.md)
