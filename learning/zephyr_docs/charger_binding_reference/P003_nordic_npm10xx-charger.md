---
id: learning.zephyr-docs.charger-binding-reference.page-3
title: nordic_npm10xx-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nordic,npm10xx-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_nordic_npm10xx-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nordic,npm10xx-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-npm10xx-charger"></a>
<a id="dtbinding-nordic-npm10xx-charger"></a>
<a id="std-dtcompatible-nordic-npm10xx-charger"></a>

兼容字符串（Compatible String）：`nordic,npm10xx-charger`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,npm10xx-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_npm10xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_npm10xx.c)。

<a id="description"></a>

Nordic nPM10系列PMIC电池充电器（Battery Charger）。

<a id="examples"></a>

## 充电器配置原例

```dts
npm1012: pmic@6a {
  reg = <0x6a>;
  compatible = "nordic,npm10xx";
  /* ... */

  charger {
    compatible = "nordic,npm10xx-charger";
    charging-enable;
    charge-current-microamp = <25000>;
    term-voltage-microvolt = <4200000>;
    term-current-percent = "3.125%";
    /* ... */
  };

  /* ... */
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `charging-enable` | `boolean` | 使能充电（Charging） |
| `charge-current-microamp` | `int` | 充电电流，单位µA。可用范围：0.5至128 mA，步进0.5 mA；129至256 mA，步进1 mA |
| `term-voltage-microvolt` | `int` | 充电终止电压（Charge Termination Voltage），单位µV，可用范围3.5至4.65 V，步进10 mV |
| `term-current-percent` | `string` | 充电终止电流，以current-microamp的百分比表示；合法值：`12.5%, 100%, 50%, 25%, 6.25%, 3.125%, 1.56%, 0.78%` |
| `charge-current-warm-microamp` | `int` | 负温度系数热敏电阻（Negative Temperature Coefficient，NTC）偏热区的充电电流，单位µA，范围与current-microamp相同 |
| `term-voltage-warm-microvolt` | `int` | NTC偏热区的充电终止电压，单位µV，范围与term-microvolt相同 |
| `charge-current-cool-microamp` | `int` | NTC偏冷区的充电电流，单位µA，范围与current-microamp相同 |
| `term-voltage-cool-microvolt` | `int` | NTC偏冷区的充电终止电压，单位µV，范围与term-microvolt相同 |
| `trickle-current-percent` | `string` | 涓流充电电流（Trickle Charge Current），以current-microamp的百分比表示；合法值：`12.5%, 100%, 50%, 25%, 6.25%, 3.125%, 1.56%, 0.78%` |
| `trickle-voltage-microvolt` | `int` | 涓流充电电压，单位µV；合法值：`2900000, 2500000, 2700000, 3100000` |
| `throttle-current-percent` | `string` | 充电限流阶段（Throttle Charging）的电流，以current-microamp的百分比表示；合法值：`100%, 87.5%, 75%, 62.5%, 50%, 37.5%, 25%, 12.5%` |
| `throttle-level-microvolt` | `int` | 充电限流阶段的电压偏移量，单位µV。原公式：`Vthrottle = term-voltage-{,-cool,-warm}microvolt- - throttle-level-microvolt.`。译注：此处保留原文属性拼写及多出的连字符；合法值：`25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000` |
| `trickle-timeout-minute` | `int` | 涓流充电超时（Timeout），单位分钟；合法值：`10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120` |
| `charge-timeout-hour` | `int` | 充电周期超时，单位小时；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `thermistor-beta` | `int` | 所选热敏电阻的Beta值 |
| `thermistor-cold-degrees` | `int` | 热敏电阻低温（Cold）阈值，单位摄氏度 |
| `thermistor-cool-degrees` | `int` | 热敏电阻偏冷（Cool）阈值，单位摄氏度 |
| `thermistor-warm-degrees` | `int` | 热敏电阻偏热（Warm）阈值，单位摄氏度 |
| `thermistor-hot-degrees` | `int` | 热敏电阻高温（Hot）阈值，单位摄氏度 |
| `dietemp-reduce-degrees` | `int` | 芯片温度（Die Temperature）降流阈值，单位摄氏度；芯片温度超过阈值时降低充电电流 |
| `dietemp-resume-degrees` | `int` | 芯片温度恢复（Resume）阈值，单位摄氏度。温度降至此阈值以下时，充电电流逐渐增加；建议至少比dietemp-reduce-degrees低10度 |
| `disable-batt-monitoring` | `boolean` | 禁用充电期间的电池温度监测（Temperature Monitoring） |
| `disable-recharge` | `boolean` | 禁用自动再充电（Automatic Recharge） |
| `disable-warm-charging` | `boolean` | 禁用偏热电池充电 |
| `disable-cool-charging` | `boolean` | 禁用偏冷电池充电 |
| `enable-advanced-profile` | `boolean` | 在偏热和偏冷温区使用自定义终止电压和充电电流；否则使用默认JEITA值 |
| `enable-throttle-charging` | `boolean` | 使能限流充电（Throttle Charging） |
| `disable-lowbatt-charging` | `boolean` | 禁用低于VBATLOW阈值（2.1 V或1.1 V）的电池充电 |
| `vbat-low-microvolt` | `int` | VBATLOW阈值，在2.1 V与1.1 V之间选择；合法值：`2100000, 1100000` |
| `vbus-limit-microamp` | `int` | 初始化时设置的VBUS输入限流（Input Current Limit）；合法值：`100000, 10000, 225000, 300000` |
| `vbusdpm-microvolt` | `int` | 设备监测VBUS并限制SYSREG电流，使VBUS电压保持高于所选电平；本属性选择初始化时采用的电平；合法值：`4350000, 4500000, 4650000, 4800000` |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

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

译注：原说明使用current-microamp、term-microvolt等简称；本页实际属性名为charge-current-microamp、term-voltage-microvolt及各温区变体。为便于核对，说明中的原名保留。

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

[上一章](P002_maxim_max20335-charger.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_nxp_pca9422-charger.md)
