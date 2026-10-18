---
id: learning.zephyr-docs.hardware.regpmic-0
title: nPM10xx稳压器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/nordic,npm10xx-regulator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第660章\_nPM10xx稳压器绑定

<a id="dtbinding-nordic-npm10xx-regulator"></a>

原文：[nordic,npm10xx-regulator](https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/nordic,npm10xx-regulator.html)。读取日期：2026-10-13，`latest`。

`nordic,npm10xx-regulator` 是设备树绑定（Devicetree Binding），描述Nordic Semiconductor的nPM10xx电源管理集成电路（Power Management Integrated Circuit，PMIC）稳压器。

本页BUCK表示降压转换器（Buck Converter），LDO表示低压差稳压器（Low-Dropout Regulator），LDSW或LOADSW表示负载开关（Load Switch）。GPIO为通用输入输出（General-Purpose Input/Output），SoC为片上系统（System on Chip）。

驱动为 [`drivers/regulator/regulator_npm10xx.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_npm10xx.c)。使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,npm10xx-regulator)。

## 660.1\_原始设备树示例

以下保留官方设备树源码（Devicetree Source，DTS）示例及其中的子节点名称。示例中的宏 `GPIO_ACTIVE_HIGH` 表示高电平有效（Active High）。

```dts
npm1012: pmic@6a {
  reg = <0x6a>;
  compatible = "nordic,npm10xx";
  /* ... */

  regulators {
    compatible = "nordic,npm10xx-regulator";
    dvs-gpios = <&gpio0 0 GPIO_ACTIVE_HIGH>, <&gpio0 1 GPIO_ACTIVE_HIGH>;

    BUCK {
      regulator-init-microvolt = <2500000>;
      pwr-mode-gpio-config = <0 GPIO_ACTIVE_HIGH>;
      /* ... */
    };

    LDO {
      regulator-init-microvolt = <1800000>;
      enable-gpio-config = <1 GPIO_ACTIVE_HIGH>;
      /* ... */
    };

    LDSW {
      regulator-boot-off;
      regulator-soft-start-microamp = <10000>;
      /* ... */
    };
  };

  /* ... */
};
```

## 660.2\_父节点的动态电压控制

本页 `int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。电压的 `microvolt` 单位为微伏（Microvolt，µV），电流的 `microamp` 单位为微安（Microampere，µA），时间的 `us` 单位为微秒（Microsecond，µs），温度的 `kelvin` 单位为开尔文（Kelvin，K）。

动态电压调节（Dynamic Voltage Scaling，DVS）通过片上系统GPIO与PMIC GPIO之间的连接控制稳压器。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `dvs-gpios` | `phandle-array` | 连接到PMIC、用作稳压器控制的SoC GPIO列表；最多提供3个引脚，因为nPM10xx有3个GPIO。状态改变的作用由各稳压器模块的 `*-gpio-config` 属性定义 |

`regulator_parent_dvs_state_set` 函数按状态标识的位驱动引脚：

| 状态 | 引脚行为 |
| --- | --- |
| `0 (0b000)` | 所有引脚无效 |
| `1 (0b001)` | 仅第一个引脚有效 |
| `2 (0b010)` | 仅第二个引脚有效 |
| `3 (0b011)` | 第一、第二个引脚同时有效 |

后续状态依此按位组合。

## 660.3\_稳压器子节点属性

GPIO配置数组使用 `<idx flags>`，其中 `idx` 为引脚索引，`flags` 为GPIO标志。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `regulator-init-microvolt` | `int` | 初始化时设置的电压；有效范围1 V至3.3 V，步进50 mV，用于BUCK和LDO |
| `regulator-min-microvolt` | `int` | 用电方可以设置的最小电压；有效范围1 V至3.3 V，步进50 mV，用于BUCK和LDO |
| `regulator-max-microvolt` | `int` | 用电方可以设置的最大电压；有效范围1 V至3.3 V，步进50 mV，用于BUCK和LDO |
| `regulator-alternate-microvolt` | `int` | 备用输出电压（Alternate Output Voltage），范围1 V至3.3 V，步进50 mV；仅用于BUCK |
| `regulator-init-microamp` | `int` | 初始化时设置的峰值电流限制（Peak Current Limit），仅用于BUCK；合法值：`66000, 91000, 117000, 142000, 167000, 192000, 217000, 291000` |
| `regulator-min-microamp` | `int` | 允许的最小峰值电流限制，仅用于BUCK；合法值：`66000, 91000, 117000, 142000, 167000, 192000, 217000, 291000` |
| `regulator-max-microamp` | `int` | 允许的最大峰值电流限制，仅用于BUCK；合法值：`66000, 91000, 117000, 142000, 167000, 192000, 217000, 291000` |
| `regulator-allow-bypass` | `boolean` | 当输入供电电压偏低，导致BUCK输出达不到目标时，启用自动直通模式（Automatic Pass-Through Mode）；仅用于BUCK |
| `regulator-soft-start-microamp` | `int` | 启动峰值电流限制。LDO和LOADSW使用10、20、35、50 mA；BUCK使用66、91、117、142、167、192、217、291 mA。下列合法值以微安表示；合法值：`10000, 20000, 35000, 50000, 66000, 91000, 117000, 142000, 167000, 192000, 217000, 291000` |
| `regulator-soft-start-us` | `int` | 软启动时间（Soft Start Time），单位为微秒；用于LDO和LOADSW；合法值：`1500, 4500, 7500, 10500` |
| `regulator-pull-down-ohms` | `int` | 下拉电阻（Pull-Down Resistance），单位为欧姆（Ohm，Ω）；仅用于BUCK；合法值：`250, 500, 1000, 2000` |
| `regulator-ripple` | `string` | 输出电压纹波（Output Voltage Ripple）；仅用于BUCK。`default`、`low`、`high` 分别为默认、低、高；合法值：`default, low, high` |
| `enable-gpio-config` | `array` | 由指定GPIO引脚控制稳压器使能，格式为 `<idx flags>` |
| `pwr-mode-gpio-config` | `array` | 由指定GPIO引脚控制稳压器电源模式，格式为 `<idx flags>`；仅用于BUCK |
| `alternate-vout-gpio-config` | `array` | 由指定GPIO引脚控制备用输出电压，格式为 `<idx flags>`；仅用于BUCK |
| `regulator-name` | `string` | 为稳压器输出提供描述性名称 |
| `regulator-always-on` | `boolean` | 稳压器始终开启，不应被禁用 |
| `regulator-boot-on` | `boolean` | 引导加载器（Bootloader）／固件已启用稳压器，预期引导加载器会让它保持开启。若没有保持开启，操作系统（Operating System，OS）应在启动时打开它，但不应阻止之后关闭。本属性仅用于软件无法读取稳压器状态的设备 |
| `regulator-boot-off` | `boolean` | 启动时应禁用稳压器 |
| `regulator-initial-mode` | `int` | 初始工作模式（Initial Operating Mode）。可用模式取决于具体硬件能力，各设备绑定文档说明其稳压器支持的取值 |
| `regulator-allowed-modes` | `array` | 允许运行时由软件配置的工作模式列表；元素顺序不限。可用模式取决于具体硬件能力，各设备绑定文档说明其稳压器支持的取值 |
| `regulator-over-current-protection` | `boolean` | 启用过流保护（Overcurrent Protection） |
| `regulator-active-discharge` | `int` | 主动放电（Active Discharge）采用三态配置：`0` 禁用，`1` 启用；省略此属性则保持默认配置；合法值：`0, 1` |

没有已弃用的节点专用属性。以下完整列出父节点继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 660.4\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

`reg-names` 的类型为 `string-array`，为 `reg` 中各寄存器块提供可选名称。以下保留官方示例；`#address-cells` 和 `#size-cells` 分别声明地址与长度使用的 32 位单元数。

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

`uart@1000` 节点有两个寄存器块：名称 `foo` 对应基址 `0x1000`、大小 `0x2000`；名称 `bar` 对应基址 `0x3000`、大小 `0x4000`。这里 uart 是**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**节点名称，示例只是演示寄存器块命名。

## 660.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 660.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 660.7\_DMA、输入输出与邮箱通道

**直接存储器访问（Direct Memory Access，DMA）**属性描述设备的 DMA 能力、通道和地址映射；输入输出（Input/Output，I/O）及邮箱（Mailbox）属性描述关联通道。IPM 是**处理器间消息（Inter-Processor Messaging）**接口。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |

## 660.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 660.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：Infineon可编程参考模块绑定](P659_Infineon可编程参考模块绑定.md) · [下一章：nPM1100稳压器绑定](P661_nPM1100稳压器绑定.md) · [返回大纲](大纲.md)
