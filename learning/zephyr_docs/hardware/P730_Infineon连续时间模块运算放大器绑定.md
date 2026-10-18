---
id: learning.zephyr-docs.hardware.opamp-0
title: Infineon连续时间模块运算放大器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/opamp/infineon,autanalog-ctb-opamp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第730章\_Infineon连续时间模块运算放大器绑定

<a id="dtbinding-infineon-autanalog-ctb-opamp"></a>

原文：[infineon,autanalog-ctb-opamp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/opamp/infineon,autanalog-ctb-opamp.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-ctb-opamp` 是设备树绑定（Devicetree Binding），描述Infineon自主模拟（Autonomous Analog，AutAnalog）连续时间模块（Continuous Time Block，CTB）内的运算放大器（Operational Amplifier，Opamp）。每个节点表示两个运放OA0、OA1中的一个，通过 `topology` 选择拓扑。可编程增益放大器（Programmable Gain Amplifier，PGA）、跨阻放大器（Transimpedance Amplifier，TIA）或差分放大器（Differential Amplifier，DiffAmp）的增益通过 `gain` 在构建时设定。**不支持运行时修改增益**：重新加载状态转换表（State Transition Table，STT）需要重启自主控制器（Autonomous Controller，AC），会扰乱共享逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter，SAR ADC）的序列器（Sequencer）。输入输出路由由开关矩阵（Switch Matrix）属性配置，详细引脚／参考映射见外设驱动库（Peripheral Driver Library，PDL）的 `cy_autanalog_ctb.h`。父节点必须具有兼容字符串 `infineon,autanalog-ctb`，参见[CTB父设备](P722_Infineon连续时间模块绑定.md)。

驱动为 [`drivers/opamp/opamp_infineon_autanalog_ctb.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/opamp_infineon_autanalog_ctb.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-ctb-opamp)。

## 730.1\_配置示例与编译期限制

以下为设备树源码（Devicetree Source，DTS）示例。`IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW` 是超低功耗模式常量，`IFX_AUTANALOG_CTB_OA_TOPO_PGA` 是PGA拓扑常量；`IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5` 与 `IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4` 是同相输入引脚映射常量，`IFX_AUTANALOG_CTB_OA_RES_REF_VSSA` 是将电阻梯底端参考接至模拟地的常量。

第一例使用配置头文件 `dt-bindings/opamp/infineon-autanalog-ctb.h`，配置OA0为超低功耗、同相PGA并将输出接至引脚。第二例为高级模式（Advanced Mode），在OA1下定义两个动态配置槽（Dynamic Configuration Slot），以有名称的子节点属性描述各槽。`VSSA` 表示模拟地，`OA0_P0_OA1_P5` 与 `OA0_P1_OA1_P4` 为分别适配OA0／OA1的引脚映射标识。

```dts
/*
 * Use constants from <dt-bindings/opamp/infineon-autanalog-ctb.h>
 */
ctb1: {
    compatible = "infineon,autanalog-ctb";
    opamp0: opamp@0 {
        compatible = "infineon,autanalog-ctb-opamp";
        reg = <0>;
        power-mode = <IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW>;
        topology = <IFX_AUTANALOG_CTB_OA_TOPO_PGA>;
        ninv-inp-pin = <IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5>;
        functional-mode = "non_inverting";
        out-to-pin;
    };
};
```

```dts
/*
 * Advanced mode: 2 dynamic config slots on opamp@1.
 * Each child node is one slot with named properties.
 */
ctb1: {
    compatible = "infineon,autanalog-ctb";
    opamp1: opamp@1 {
        compatible = "infineon,autanalog-ctb-opamp";
        reg = <1>;
        power-mode = <IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW>;
        topology = <IFX_AUTANALOG_CTB_OA_TOPO_PGA>;
        functional-mode = "non_inverting";

        dyn-cfg-0 {
            ninv-inp-pin = <IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5>;
            res-inp-ref = <IFX_AUTANALOG_CTB_OA_RES_REF_VSSA>;
            out-to-pin;
        };

        dyn-cfg-1 {
            ninv-inp-pin = <IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4>;
            res-inp-ref = <IFX_AUTANALOG_CTB_OA_RES_REF_VSSA>;
            out-to-pin;
        };
    };
};
```

译注：原例的 `ctb1: {` 在标签后没有节点名，CTB父节点也未写出父绑定要求的 `reg`；此处原样保留，实际应用需结合芯片设备树补全。通用 `programmable-gain` 描述以硬件支持为前提，不能据此推断本驱动支持运行时改增益；本设备的限制以本页概述和 `gain` 说明为准。

## 730.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandles` 为节点引用（Phandle）列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。

下表所称“同一头文件”均指 `dt-bindings/opamp/infineon-autanalog-ctb.h`。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `power-mode` | `int` | **必需**。运放功耗模式（Power Mode），使用 `dt-bindings/opamp/infineon-autanalog-ctb.h` 中的 `IFX_AUTANALOG_CTB_OA_PWR_*` 常量；各常量、数值与含义见模式对照；合法值：`0, 1, 2, 4, 6, 8, 10` |
| `topology` | `int` | **必需**。运放拓扑（Topology），使用 `dt-bindings/opamp/infineon-autanalog-ctb.h` 中的 `IFX_AUTANALOG_CTB_OA_TOPO_*` 常量；各常量、数值与含义见模式对照；合法值：`0, 1, 2, 3, 4, 5, 6` |
| `interrupt-mode` | `int` | 仅用于比较器拓扑的中断边沿检测模式（Edge Detection Mode）。使用 `dt-bindings/opamp/infineon-autanalog-ctb.h` 的 `IFX_AUTANALOG_CTB_COMP_INT_*` 常量：`DISABLED`（0）禁用、`EDGE_RISING`（1）上升沿、`EDGE_FALLING`（2）下降沿、`EDGE_BOTH`（3）双边沿；这些后缀均须加上前述完整前缀；默认值：`0`；合法值：`0, 1, 2, 3` |
| `fb-cap` | `int` | 反馈电容（Feedback Capacitor）配置值，范围0至15；使用 `dt-bindings/opamp/infineon-autanalog-ctb.h` 中的 `IFX_AUTANALOG_CTB_OA_FB_CAP_*` 常量；默认值：`0` |
| `cc-cap` | `int` | 补偿电容（Compensation Capacitor）配置值，范围0至8；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_CC_CAP_*` 常量，默认值8表示禁用；默认值：`8` |
| `ninv-inp-pin` | `int` | 同相输入（Non-Inverting Input）与引脚直接连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_NINV_PIN_*` 常量，映射见引脚对照；默认值：`0`；合法值：`0, 1, 2` |
| `ninv-inp-ref` | `int` | 同相输入参考连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_NINV_REF_*` 常量，顶层属性说明给出的范围为0至7；默认值：`0` |
| `inv-inp-pin` | `int` | 反相输入（Inverting Input）与引脚直接连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_INV_PIN_*` 常量，映射见引脚对照；默认值：`0`；合法值：`0, 1, 2` |
| `res-inp-pin` | `int` | 电阻梯（Resistor Ladder）底端引脚连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_RES_PIN_*` 常量，映射见引脚对照；默认值：`0`；合法值：`0, 1, 2` |
| `res-inp-ref` | `int` | 电阻梯底端参考连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_RES_REF_*` 常量，顶层属性说明给出的范围为0至5；默认值：`0` |
| `shared-mux-in` | `int` | 连接内部模拟总线的输入多路复用器（Input Multiplexer，MUX）；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_MUX_IN_*` 常量，顶层属性说明给出的范围为0至8；默认值：`0` |
| `shared-mux-out` | `int` | 来自内部模拟总线的输出多路复用器（Output Multiplexer）连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_MUX_OUT_*` 常量：`DISCONNECT`（0）断开、`NINV`（1）同相输入、`INV`（2）反相输入、`RES`（3）电阻梯；这些后缀均须加上前述完整前缀；默认值：`0`；合法值：`0, 1, 2, 3` |
| `gain` | `int` | 用于PGA、TIA或差分放大器拓扑的增益，在构建时设定，不支持运行时修改；仅对具有电阻梯的拓扑有意义。使用 `dt-bindings/mfd/infineon-autanalog.h` 中的 `IFX_AUTANALOG_CTB_OA_GAIN_*` 常量，完整对应关系见增益对照；默认值：`0` |
| `out-to-pin` | `boolean` | 将运放输出直接连接到引脚 |
| `functional-mode` | `string` | **必需**。选择运算放大器的功能模式（Functional Mode）；五种模式的接线、公式及原始电路图见“功能模式、电路图与增益枚举”节；合法值：`differential, inverting, non_inverting, follower, standalone` |
| `programmable-gain` | `string-array` | 可编程增益（Programmable Gain）列表。如果运放支持此功能，则可在运行时动态改变增益，数值必须取自规定的枚举；完整倍率对照见“功能模式、电路图与增益枚举”节；合法值：`OPAMP_GAIN_1_7, OPAMP_GAIN_1_3, OPAMP_GAIN_1, OPAMP_GAIN_5_3, OPAMP_GAIN_2, OPAMP_GAIN_11_5, OPAMP_GAIN_3, OPAMP_GAIN_4, OPAMP_GAIN_13_3, OPAMP_GAIN_7, OPAMP_GAIN_8, OPAMP_GAIN_15, OPAMP_GAIN_16, OPAMP_GAIN_31, OPAMP_GAIN_32, OPAMP_GAIN_33, OPAMP_GAIN_63, OPAMP_GAIN_64` |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。CTB内的运放索引，为0或1 |

## 730.3\_模式与引脚常量对照

下列常量均来自 `dt-bindings/opamp/infineon-autanalog-ctb.h`；轨到轨（Rail-to-Rail）表示原文标注的输入范围特性。

| 常量 | 数值 | 中文含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTB_OA_PWR_OFF` | 0 | 关闭 |
| `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW` | 1 | 超低功耗 |
| `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL` | 2 | 超低功耗，轨到轨 |
| `IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL` | 4 | 低功耗，轨到轨 |
| `IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL` | 6 | 中等功耗，轨到轨 |
| `IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL` | 8 | 高功耗，轨到轨 |
| `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL` | 10 | 超高功耗，轨到轨 |
| `IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR` | 0 | 比较器（Comparator） |
| `IFX_AUTANALOG_CTB_OA_TOPO_PGA` | 1 | 可编程增益放大器 |
| `IFX_AUTANALOG_CTB_OA_TOPO_TIA` | 2 | 跨阻放大器 |
| `IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP` | 3 | 开环运算放大器（Open-Loop Opamp） |
| `IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER` | 4 | 差分放大器 |
| `IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR` | 5 | 带迟滞的比较器（Comparator with Hysteresis） |
| `IFX_AUTANALOG_CTB_OA_TOPO_BUFFER` | 6 | 缓冲器／电压跟随器 |

引脚连接的三组常量：

| 常量前缀 | 后缀及数值 | 连接含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTB_OA_NINV_PIN_` | `DISCONNECT`（0） | 断开 |
| `IFX_AUTANALOG_CTB_OA_NINV_PIN_` | `OA0_P0_OA1_P5`（1） | OA0接P0，OA1接P5 |
| `IFX_AUTANALOG_CTB_OA_NINV_PIN_` | `OA0_P1_OA1_P4`（2） | OA0接P1，OA1接P4 |
| `IFX_AUTANALOG_CTB_OA_INV_PIN_` | `DISCONNECT`（0） | 断开 |
| `IFX_AUTANALOG_CTB_OA_INV_PIN_` | `OA0_P0_OA1_P5`（1） | OA0接P0，OA1接P5 |
| `IFX_AUTANALOG_CTB_OA_INV_PIN_` | `OA0_P1_OA1_P4`（2） | OA0接P1，OA1接P4 |
| `IFX_AUTANALOG_CTB_OA_RES_PIN_` | `DISCONNECT`（0） | 断开 |
| `IFX_AUTANALOG_CTB_OA_RES_PIN_` | `OA0_P0_OA1_P5`（1） | OA0接P0，OA1接P5 |
| `IFX_AUTANALOG_CTB_OA_RES_PIN_` | `OA0_P1_OA1_P4`（2） | OA0接P1，OA1接P4 |

增益常量来自 `dt-bindings/mfd/infineon-autanalog.h`：

| 常量 | 配置值 | 增益 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTB_OA_GAIN_1_00` | 0 | 1.00（默认） |
| `IFX_AUTANALOG_CTB_OA_GAIN_1_42` | 1 | 1.42 |
| `IFX_AUTANALOG_CTB_OA_GAIN_2_00` | 2 | 2.00 |
| `IFX_AUTANALOG_CTB_OA_GAIN_2_78` | 3 | 2.78 |
| `IFX_AUTANALOG_CTB_OA_GAIN_4_00` | 4 | 4.00 |
| `IFX_AUTANALOG_CTB_OA_GAIN_5_82` | 5 | 5.82 |
| `IFX_AUTANALOG_CTB_OA_GAIN_8_00` | 6 | 8.00 |
| `IFX_AUTANALOG_CTB_OA_GAIN_10_67` | 7 | 10.67 |
| `IFX_AUTANALOG_CTB_OA_GAIN_16_00` | 8 | 16.00 |
| `IFX_AUTANALOG_CTB_OA_GAIN_21_33` | 9 | 21.33 |
| `IFX_AUTANALOG_CTB_OA_GAIN_32_00` | 10 | 32.00 |

## 730.4\_功能模式、电路图与增益枚举

以下为绑定继承的通用功能说明。`Rf` 为反馈电阻（Feedback Resistor），`Rin` 为输入电阻（Input Resistor），`Vin`／`Vin1`／`Vin2` 为输入电压（Input Voltage），`Vout` 为输出电压（Output Voltage），`GND` 为地（Ground）。原始字符电路图完整保留。

`differential`：差分（Differential）模式：两个输入端均接入信号，放大两者之差，抑制共模信号（Common-Mode Signal），用于仪表测量（Instrumentation）与噪声抑制（Noise Rejection）。`Vout = (Rf/Rin) * (Vin2 - Vin1)`，增益为 `Rf/Rin`。

```text
         Rin        Rf
Vin1 --/\/\/\--*--/\/\/\-----
               |            |
               |     |\     |
               ------|- \   |
                     |   >--*-- Vout
               ------|+ /
               |     |/
               |
Vin2 --/\/\/\--*--/\/\/\-----
         Rin        Rf      |
                           GND
```

`inverting`：反相（Inverting）模式：信号接入反相（−）端，同相（+）端接地，反馈电阻连接输出与反相端；输出与输入相差180°。`Vout = (-Rf/Rin) * Vin`，增益为 `-Rf/Rin`。

```text
        Rin        Rf
Vin --/\/\/\--*--/\/\/\-----
              |            |
              |     |\     |
              ------|- \   |
                    |   >--*-- Vout
              ------|+ /
              |     |/
            GND
```

`non_inverting`：同相（Non-Inverting）模式：信号接入同相（+）端，反相（−）端连接反馈网络，输出与输入同相。`Vout = (1 + (Rf/Rin)) * Vin`，增益为 `1 + Rf/Rin`。

```text
      Rin        Rf
 |--/\/\/\--*--/\/\/\-----
 |          |            |
GND         |     |\     |
            ------|- \   |
                  |   >--*-- Vout
        Vin ------|+ /
                  |/
```

`follower`：跟随器（Follower）模式，即电压跟随器（Voltage Follower）或缓冲器（Buffer）：同相放大器的特例，`Vout = 1 * Vin`，增益为1；输出直接反馈至反相输入，输入阻抗很高、输出阻抗很低，用于阻抗匹配（Impedance Matching）。

```text
    --------------
    |            |
    |     |\     |
    ------|- \   |
          |   >--*-- Vout
Vin ------|+ /
          |/
```

`standalone`：独立（Standalone）模式：运放工作方式由外部电路决定。

```text
          |\
Vin- -----|- \
          |   >---- Vout
Vin+ -----|+ /
          |/
```

原文参考：[运算放大器教程](https://www.electronics-tutorials.ws/category/opamp)。

可编程增益枚举与倍率如下；是否支持运行时改变仍取决于具体硬件与驱动。

| 枚举 | 倍率 |
| --- | --- |
| `OPAMP_GAIN_1_7` | 1/7 |
| `OPAMP_GAIN_1_3` | 1/3 |
| `OPAMP_GAIN_1` | 1 |
| `OPAMP_GAIN_5_3` | 5/3 |
| `OPAMP_GAIN_2` | 2 |
| `OPAMP_GAIN_11_5` | 11/5 |
| `OPAMP_GAIN_3` | 3 |
| `OPAMP_GAIN_4` | 4 |
| `OPAMP_GAIN_13_3` | 13/3 |
| `OPAMP_GAIN_7` | 7 |
| `OPAMP_GAIN_8` | 8 |
| `OPAMP_GAIN_15` | 15 |
| `OPAMP_GAIN_16` | 16 |
| `OPAMP_GAIN_31` | 31 |
| `OPAMP_GAIN_32` | 32 |
| `OPAMP_GAIN_33` | 33 |
| `OPAMP_GAIN_63` | 63 |
| `OPAMP_GAIN_64` | 64 |

## 730.5\_动态配置子节点属性

以下属性适用于动态配置槽子节点；原页未为这些子属性列出顶层属性中的数值枚举，默认值按子节点绑定独立保留。常量仍来自 `dt-bindings/opamp/infineon-autanalog-ctb.h`。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ninv-inp-pin` | `int` | 同相输入（Non-Inverting Input）与引脚直接连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_NINV_PIN_*` 常量，映射见引脚对照；默认值：`0` |
| `ninv-inp-ref` | `int` | 同相输入参考连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_NINV_REF_*` 常量；默认值：`0` |
| `inv-inp-pin` | `int` | 反相输入（Inverting Input）与引脚直接连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_INV_PIN_*` 常量，映射见引脚对照；默认值：`0` |
| `res-inp-pin` | `int` | 电阻梯（Resistor Ladder）底端引脚连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_RES_PIN_*` 常量，映射见引脚对照；默认值：`0` |
| `res-inp-ref` | `int` | 电阻梯底端参考连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_RES_REF_*` 常量；默认值：`0` |
| `shared-mux-in` | `int` | 连接内部模拟总线的输入多路复用器（Input Multiplexer，MUX）；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_MUX_IN_*` 常量；默认值：`0` |
| `shared-mux-out` | `int` | 来自内部模拟总线的输出多路复用器（Output Multiplexer）连接；使用同一头文件中的 `IFX_AUTANALOG_CTB_OA_MUX_OUT_*` 常量：`DISCONNECT`（0）断开、`NINV`（1）同相输入、`INV`（2）反相输入、`RES`（3）电阻梯；这些后缀均须加上前述完整前缀；默认值：`0` |
| `out-to-pin` | `boolean` | 将运放输出直接连接到引脚 |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；标为必需的要求以本页为准。

## 730.6\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。


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

## 730.7\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 730.8\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 730.9\_DMA、输入输出与邮箱通道

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

## 730.10\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 730.11\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：TLE9104多功能设备绑定](P729_TLE9104多功能设备绑定.md) · [下一章：NXP高速运算放大器绑定](P731_NXP高速运算放大器绑定.md) · [返回大纲](大纲.md)
