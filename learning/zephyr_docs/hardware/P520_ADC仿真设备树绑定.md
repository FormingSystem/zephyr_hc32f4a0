---
id: learning.zephyr-docs.hardware.emubind-0
title: ADC仿真设备树绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/zephyr,adc-emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第520章\_ADC仿真设备树绑定

<a id="dtbinding-zephyr-adc-emul"></a>

原文：[zephyr,adc-emul](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/zephyr,adc-emul.html)。读取日期：2026-10-13，`latest`。

`zephyr,adc-emul` 是 Zephyr Project 提供的**模数转换器（Analog-to-Digital Converter，ADC）**仿真器设备树绑定。驱动为 [`drivers/adc/adc_emul.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/adc_emul.c)，使用该兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,adc-emul)。

## 520.1\_控制器属性与参考电压

下列属性作用于控制器节点本身，没有已弃用的专用属性。参考电压采用**毫伏（Millivolt，mV）**；VDD 是供电电压的符号。`ADC_REF_*` 是 ADC 参考源选择标识。

属性类型 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `nchannels` | `int` | 仿真 ADC 通道数量，必需，范围 `1`～`32` |
| `ref-internal-mv` | `int` | 内部参考电压，默认 `0`；未提供或为零时，选择 `ADC_REF_INTERNAL` 的通道配置失败 |
| `ref-vdd-mv` | `int` | VDD 参考电压，默认 `0`；未提供或为零时，选择 `ADC_REF_VDD_X` 系列参考的通道配置失败 |
| `ref-external0-mv` | `int` | 外部参考输入 0 的电压，默认 `0`；未提供或为零时，选择 `ADC_REF_EXTERNAL0` 的通道配置失败 |
| `ref-external1-mv` | `int` | 外部参考输入 1 的电压，默认 `0`；未提供或为零时，选择 `ADC_REF_EXTERNAL1` 的通道配置失败 |
| `#io-channel-cells` | `int` | 必需属性；原页没有给出进一步属性说明 |

本绑定继承的 `#address-cells` 固定为 `1`，`#size-cells` 固定为 `0`。输入输出（Input/Output，I/O）通道说明单元名称为 `input`。基础属性全文在后文保留；并非全部通用属性都适用于当前兼容字符串。

## 520.2\_通道子节点

通道子节点的 `reg`（`array` 类型）是**必需的通道标识**。下列增益和参考选择属性也都必需，合法值完整列出。

`zephyr,gain` 的类型为 `string`，选择**增益（Gain）**：

| 合法值 | 增益倍数 |
| --- | --- |
| `ADC_GAIN_1_6` | 1/6 |
| `ADC_GAIN_1_5` | 1/5 |
| `ADC_GAIN_1_4` | 1/4 |
| `ADC_GAIN_2_7` | 2/7 |
| `ADC_GAIN_1_3` | 1/3 |
| `ADC_GAIN_2_5` | 2/5 |
| `ADC_GAIN_1_2` | 1/2 |
| `ADC_GAIN_2_3` | 2/3 |
| `ADC_GAIN_4_5` | 4/5 |
| `ADC_GAIN_1` | 1 |
| `ADC_GAIN_2` | 2 |
| `ADC_GAIN_3` | 3 |
| `ADC_GAIN_4` | 4 |
| `ADC_GAIN_6` | 6 |
| `ADC_GAIN_8` | 8 |
| `ADC_GAIN_12` | 12 |
| `ADC_GAIN_16` | 16 |
| `ADC_GAIN_24` | 24 |
| `ADC_GAIN_32` | 32 |
| `ADC_GAIN_64` | 64 |
| `ADC_GAIN_128` | 128 |

`zephyr,reference` 的类型为 `string`，选择**参考源（Reference）**：

| 合法值 | 参考源 |
| --- | --- |
| `ADC_REF_VDD_1` | 供电电压 VDD |
| `ADC_REF_VDD_1_2` | 供电电压的一半（VDD/2） |
| `ADC_REF_VDD_1_3` | 供电电压的三分之一（VDD/3） |
| `ADC_REF_VDD_1_4` | 供电电压的四分之一（VDD/4） |
| `ADC_REF_INTERNAL` | 内部参考 |
| `ADC_REF_EXTERNAL0` | 外部参考输入 0 |
| `ADC_REF_EXTERNAL1` | 外部参考输入 1 |

通道可以使用**单端输入（Single-Ended Input）**或**差分输入（Differential Input）**。后者测量正、负输入的差。其余子节点属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `zephyr,vref-mv` | `int` | 指定此通道所选参考源的毫伏值，供应用计算使用；内部参考通常可通过专门的 ADC 应用程序编程接口（Application Programming Interface，API）取得电压而无需此属性，其他参考源则可利用它 |
| `zephyr,acquisition-time` | `int` | 必需的采集时间（Acquisition Time）；使用 `ADC_ACQ_TIME` 宏组合值，或使用 `ADC_ACQ_TIME_DEFAULT` 采用硬件默认设置，例如硬件不支持配置采集时间时 |
| `zephyr,differential` | `boolean` | 设置时选择差分输入；否则通常使用单端输入，但指定 `zephyr,input-negative` 时会隐式选择差分模式 |
| `zephyr,input-positive` | `int` | 正 ADC 输入；仅用于选择 Kconfig 配置项 `ADC_CONFIGURABLE_INPUTS` 的驱动 |
| `zephyr,input-negative` | `int` | 负 ADC 输入；仅用于选择 `ADC_CONFIGURABLE_INPUTS` 的驱动，指定后隐式选择差分输入 |
| `zephyr,resolution` | `int` | 通道使用的 ADC 分辨率（Resolution） |
| `zephyr,oversampling` | `int` | 通道过采样（Oversampling）设置；给定值为 N 时，每个样本取 `2^N` 次转换结果的平均值 |
| `zephyr,current-source-pin` | `uint8-array` | 电流源（Current Source）输出引脚选择，实际解释取决于驱动；仅用于选择 `ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN` 的驱动 |
| `zephyr,vbias-pins` | `int` | 偏置电压（Bias Voltage）输出引脚选择，实际解释取决于驱动；仅用于选择 `ADC_CONFIGURABLE_VBIAS_PIN` 的驱动 |

`uint8-array` 表示 8 位无符号数数组；后三个 `ADC_CONFIGURABLE_*` 名称是 Kconfig 配置选项。以下基础属性描述控制器节点，不能把其中通用 `reg` 的地址含义替代上述通道子节点标识含义。

## 520.3\_状态、兼容字符串与寄存器

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

## 520.4\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 520.5\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 520.6\_DMA、输入输出与邮箱通道

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

## 520.7\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 520.8\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：伪稳压器设备树绑定](P519_伪稳压器设备树绑定.md) · [下一章：GPIO仿真设备树绑定](P521_GPIO仿真设备树绑定.md) · [返回大纲](大纲.md)
