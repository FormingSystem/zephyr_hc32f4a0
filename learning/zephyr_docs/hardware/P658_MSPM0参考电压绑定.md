---
id: learning.zephyr-docs.hardware.reginternal-12
title: MSPM0参考电压绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/ti,mspm0-vref.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第658章\_MSPM0参考电压绑定

<a id="dtbinding-ti-mspm0-vref"></a>

原文：[ti,mspm0-vref](https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/ti,mspm0-vref.html)。读取日期：2026-10-13，`latest`。

`ti,mspm0-vref` 是设备树绑定（Devicetree Binding），描述Texas Instruments的MSPM0参考电压（Voltage Reference，VREF）稳压器。

驱动为 [`drivers/regulator/regulator_mspm0_vref.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_mspm0_vref.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ti,mspm0-vref)。

## 658.1\_参考电压与采样保持

本页 `int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。电压的 `microvolt` 单位为微伏（Microvolt，µV），电流的 `microamp` 单位为微安（Microampere，µA），时间的 `us` 单位为微秒（Microsecond，µs），温度的 `kelvin` 单位为开尔文（Kelvin，K）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `regulator-uv` | `int` | **必需**。输出电压，合法值为1.4 V或2.5 V，以微伏表示。原文将通常的最小支持输出写为1400000（1.4 V），最大支持输出写为2500000（2.5 V）；合法值：`1400000, 2500000` |
| `ti,sample-hold-enable` | `boolean` | 启用采样保持模式（Sample-and-Hold Mode） |
| `ti,sample-cycles` | `int` | 采样保持模式中的采样周期数；默认值：`8` |
| `ti,hold-cycles` | `int` | 采样保持模式中的保持周期数；默认值：`64` |
| `ti,clk-div` | `int` | 原页未提供文字说明，保留默认值与合法取值；默认值：`1`；合法值：`1, 2, 4, 6, 8` |

## 658.2\_稳压器通用属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `regulator-name` | `string` | 为稳压器输出提供描述性名称 |
| `regulator-init-microvolt` | `int` | 初始化时设置的电压 |
| `regulator-min-microvolt` | `int` | 用电方可以设置的最小电压 |
| `regulator-max-microvolt` | `int` | 用电方可以设置的最大电压 |
| `regulator-microvolt-offset` | `int` | 为补偿电压降而施加的电压偏移量 |
| `regulator-init-microamp` | `int` | 初始化时设置的电流 |
| `regulator-min-microamp` | `int` | 用电方可以设置的最小电流 |
| `regulator-max-microamp` | `int` | 用电方可以设置的最大电流 |
| `regulator-input-current-limit-microamp` | `int` | 稳压器允许的最大输入电流 |
| `regulator-always-on` | `boolean` | 稳压器始终开启，不应被禁用 |
| `regulator-boot-on` | `boolean` | 引导加载器（Bootloader）／固件已启用稳压器，预期引导加载器会让它保持开启。若没有保持开启，操作系统（Operating System，OS）应在启动时打开它，但不应阻止之后关闭。本属性仅用于软件无法读取稳压器状态的设备 |
| `regulator-boot-off` | `boolean` | 启动时应禁用稳压器 |
| `regulator-allow-bypass` | `boolean` | 允许稳压器进入旁路模式（Bypass Mode） |
| `regulator-allow-set-load` | `boolean` | 允许配置稳压器的性能级别（Performance Level） |
| `regulator-ramp-delay` | `int` | 稳压器的电压变化斜率，单位为微伏/微秒（µV/µs）。原文名称为 Ramp Delay。对于支持禁用变化斜率的硬件，必须显式设为零，即 `regulator-ramp-delay = <0>`，才能禁用此功能 |
| `regulator-enable-ramp-delay` | `int` | 电源轨（Supply Rail）达到目标电压及板级设计规定正负容差所需的时间，单位为微秒。这是稳压器内部电压爬升与板级因素共同决定的系统总爬升时间，板级因素包括走线电容和供电负载 |
| `regulator-settling-time-us` | `int` | 电压变化后的稳定时间（Settling Time），单位为微秒；用于任何幅度的电压变化都需要固定稳定时间的稳压器，特别适合电压按指数变化的情况 |
| `regulator-settling-time-up-us` | `int` | 电压升高后的稳定时间，单位为微秒；用于任何幅度的升压都需要固定稳定时间的稳压器，特别适合电压按指数变化的情况 |
| `regulator-settling-time-down-us` | `int` | 电压降低后的稳定时间，单位为微秒；用于任何幅度的降压都需要固定稳定时间的稳压器，特别适合电压按指数变化的情况 |
| `regulator-soft-start` | `boolean` | 启用软启动（Soft Start），让电压缓慢上升 |
| `regulator-initial-mode` | `int` | 初始工作模式（Initial Operating Mode）。可用模式取决于具体硬件能力，各设备绑定文档说明其稳压器支持的取值 |
| `regulator-allowed-modes` | `array` | 允许运行时由软件配置的工作模式列表；元素顺序不限。可用模式取决于具体硬件能力，各设备绑定文档说明其稳压器支持的取值 |
| `regulator-system-load` | `int` | 稳压器上未由任何用电方请求计入的负载，单位为微安 |
| `regulator-pull-down` | `boolean` | 稳压器禁用时启用下拉电阻（Pull-Down Resistor） |
| `regulator-over-current-protection` | `boolean` | 启用过流保护（Overcurrent Protection） |
| `regulator-oc-protection-microamp` | `int` | 设置过流（Overcurrent）保护阈值；达到此阈值时，硬件执行紧急关断。`0` 禁用保护；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-oc-error-microamp` | `int` | 设置过流（Overcurrent）错误阈值；达到此阈值时，部分硬件可能已工作异常，需要采取防损坏措施。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-oc-warn-microamp` | `int` | 设置过流（Overcurrent）警告阈值；达到此阈值时，假定硬件仍可工作，但已接近损坏界限，应开始恢复操作。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-ov-protection-microvolt` | `int` | 设置过压（Overvoltage）保护阈值；达到此阈值时，硬件执行紧急关断。`0` 禁用保护；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-ov-error-microvolt` | `int` | 设置过压（Overvoltage）错误阈值；达到此阈值时，部分硬件可能已工作异常，需要采取防损坏措施。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-ov-warn-microvolt` | `int` | 设置过压（Overvoltage）警告阈值；达到此阈值时，假定硬件仍可工作，但已接近损坏界限，应开始恢复操作。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-uv-protection-microvolt` | `int` | 设置欠压（Undervoltage）保护阈值；达到此阈值时，硬件执行紧急关断。`0` 禁用保护；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-uv-error-microvolt` | `int` | 设置欠压（Undervoltage）错误阈值；达到此阈值时，部分硬件可能已工作异常，需要采取防损坏措施。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-uv-warn-microvolt` | `int` | 设置欠压（Undervoltage）警告阈值；达到此阈值时，假定硬件仍可工作，但已接近损坏界限，应开始恢复操作。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置。阈值以相对于稳压器设定电压的微伏偏移量给出 |
| `regulator-temp-protection-kelvin` | `int` | 设置过温（Overtemperature）保护阈值；达到此阈值时，硬件执行紧急关断。`0` 禁用保护；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-temp-error-kelvin` | `int` | 设置过温（Overtemperature）错误阈值；达到此阈值时，部分硬件可能已工作异常，需要采取防损坏措施。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-temp-warn-kelvin` | `int` | 设置过温（Overtemperature）警告阈值；达到此阈值时，假定硬件仍可工作，但已接近损坏界限，应开始恢复操作。`0` 禁用检测；`1` 表示启用，但可以省略具体阈值设置 |
| `regulator-active-discharge` | `int` | 主动放电（Active Discharge）采用三态配置：`0` 禁用，`1` 启用；省略此属性则保持默认配置；合法值：`0, 1` |
| `regulator-max-step-microvolt` | `int` | 单步能够安全改变的当前电压与目标电压之间的最大差值 |
| `startup-delay-us` | `int` | 启动时间，单位为微秒 |
| `off-on-delay-us` | `int` | 从关闭到开启的延迟，单位为微秒 |
| `supply-gpios` | `phandle-array` | 控制设备供电的通用输入输出（General-Purpose Input/Output，GPIO）说明符。设备有独立供电开关时应提供此属性；供电状态完全由设备驱动负责。与共享稳压器引用 `vin-supply` 相对 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器节点引用；被引用节点必须具有稳压器兼容字符串。由共享稳压器供电时应提供此属性，供电状态取决于所有用电设备的请求状态。与独立开关 `supply-gpios` 相对。两者同时存在时，必须先请求稳压器，再将供电GPIO置为有效；释放稳压器前，必须先将供电GPIO置为无效 |

## 658.3\_引脚状态

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

基础属性 `reg`（类型 `array`）为**必需**，其寄存器地址与大小格式见下节。

基础属性 `clocks`（类型 `phandle-array`）也是**必需**，它描述设备的时钟提供者，具体约定见后文。

没有已弃用的节点专用属性。以下完整列出继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 658.4\_状态、兼容字符串与寄存器

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

## 658.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 658.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 658.7\_DMA、输入输出与邮箱通道

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

## 658.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 658.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：SiliconLabs_Series2直流转换器绑定](P657_SiliconLabs_Series2直流转换器绑定.md) · [下一章：Infineon可编程参考模块绑定](P659_Infineon可编程参考模块绑定.md) · [返回大纲](大纲.md)
