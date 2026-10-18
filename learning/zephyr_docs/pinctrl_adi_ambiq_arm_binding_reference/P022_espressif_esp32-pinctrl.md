---
id: learning.zephyr-docs.pinctrl-adi-ambiq-arm-binding-reference.page-22
title: espressif_esp32-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第22章\_espressif_esp32-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="espressif-esp32-pinctrl"></a>
<a id="dtbinding-espressif-esp32-pinctrl"></a>
<a id="std-dtcompatible-espressif-esp32-pinctrl"></a>

兼容字符串（Compatible String）：`espressif,esp32-pinctrl`。厂商：[ Espressif Systems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-espressif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=espressif,esp32-pinctrl)。

<a id="description"></a>

ESP32引脚控制器（Pin Controller）。

Espressif引脚控制器按引脚状态（Pin State）管理配置、功能和属性。状态由预定义的引脚复用定义与用户提供的引脚属性按组组成。每个Zephyr应用有自己的复用与配置需求；以下用ESP-WROVER-KIT的I2C_0说明修改节点引脚状态的方法，适当调整也适用于其他开发板。

假设应用需要将I2C_0的SDA路由到GPIO_33。查看 `esp_wrover_kit.dts`，I2C_0节点已关联预定义状态：原例包含 `esp_wrover_kit-pinctrl.dtsi`，通过 `pinctrl-0 = <&i2c0_default>` 设置默认状态。该状态和其他状态定义在同目录的 `esp_wrover_kit-pinctrl.dtsi`。原始默认状态将SDA、SCL分别映射至GPIO21、GPIO22，同时设置上拉、开漏和输出高电平；相关代码完整保留在下方。

这些属性中只有 `pinmux` 必需，其他属性应根据应用需要及硬件支持选择。例如自制板在GPIO21焊盘上已有外部上拉电阻，可能就不需要 `bias-pull-up`。

要将SDA改至GPIO33，需要更新 `pinmux`。直接把 `I2C0_SDA_GPIO21` 换成 `I2C0_SDA_GPIO33` 虽然可能有效，但未经硬件文档核对不建议这样做，因为不能保证任意I/O都能路由任意信号。应检查目标SoC的[官方引脚复用宏定义目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/include/zephyr/dt-bindings/pinctrl)。ESP-WROVER-KIT基于ESP32，因此查看 `esp32-pinctrl.h`；其中确实定义了 `I2C0_SDA_GPIO33`，由 `ESP32_PINMUX(33, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)` 生成。

随后在 `esp_wrover_kit-pinctrl.dtsi` 新建状态，或替换／更新已有状态，使用该宏，把SDA改为GPIO33而SCL仍为GPIO22。前后状态与宏原例均保留在下方。相应调整后，这些步骤适用于其他开发板、SoC、外设和引脚组合。

注意，并非所有引脚都适用于某外设，取决于引脚是否支持外设所需的属性。引脚复用信息受 `hal_espressif` 中定义约束；偏置和驱动等属性则可以按需选择，但必须对外设信号有意义且目标GPIO具备支持。全部引脚属性都应按组组织，具有共同属性的引脚放在同组，例如原例的group1；其他外设可能需要多组。原文举例写作 `bias-push-pull`、`drive-open-drain`。

`sleep-hold-en` 是另一项有用属性：为该引脚启用系统休眠期间的ESP GPIO焊盘保持（Pad Hold），在进入低功耗模式前锁存引脚状态，整个休眠期间保持不变。这样，即使控制该引脚的外设断电或寄存器丢失状态，GPIO电平仍可保持。该属性适用于输入、输出模式，但仅能用于具备输出能力的GPIO。

对于深度休眠（Deep Sleep）周期，自动保持可能无法覆盖从进入休眠到应用恢复执行的完整时段。复位会导致寄存器状态丢失，驱动初始化阶段会释放保持配置。若输出必须保持稳定，例如边沿敏感信号，应用可能需要在请求断电（Power-Off）之前显式调用 `gpio_hold_en()`，使引脚保持贯穿深度休眠，并持续到应用再次运行。下方独立原例为LEDC通道0配置休眠保持。

<a id="examples"></a>

官方设备树配置原例：

```dts
ledc0_default: ledc0_default {
    group1 {
        pinmux = <LEDC_CH0_GPIO2>;
        sleep-hold-en;
    };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 22.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 22.2\_基础属性

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

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `array` | **必需**。数组每项表示一个引脚的复用信息（Pin Muxing Information）。元素使用Espressif硬件抽象层（HAL）提供的预声明宏。 |
| `sleep-hold-en` | `boolean` | 启用系统休眠期间的ESP GPIO焊盘保持（Pad Hold）。启用后，在进入休眠前锁存引脚状态，并在系统低功耗期间保持不变。 |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `output-enable` | `boolean` | 启用引脚输出，例如启用输出缓冲器（Output Buffer），但不主动驱动该引脚。 |
| `output-low` | `boolean` | 将引脚设置为低电平输出模式（Output Low）。 |
| `output-high` | `boolean` | 将引脚设置为高电平输出模式（Output High）。 |

## ESP32 I2C默认状态与GPIO33重路由原例

```dts
    #include "esp_wrover_kit-pinctrl.dtsi"

    &i2c0 {
            ...
            pinctrl-0 = <&i2c0_default>;
            pinctrl-names = "default";
    };

```

```dts
    i2c0_default: i2c0_default {
            group1 {
                    pinmux = <I2C0_SDA_GPIO21>,
                             <I2C0_SCL_GPIO22>;
                    bias-pull-up;
                    drive-open-drain;
                    output-high;
            };
    };
```

```dts
    i2c0_default: i2c0_default {
            group1 {
                    pinmux = <I2C0_SDA_GPIO33>,
                             <I2C0_SCL_GPIO22>;
                    bias-pull-up;
                    drive-open-drain;
                    output-high;
            };
    };
```

```dts
    #define I2C0_SDA_GPIO33 \
            ESP32_PINMUX(33, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
```

译注：原文写有 `pincrl-0` 与 `bias-push-pull`；前者按实际属性 `pinctrl-0` 翻译，后者作为原文举例保留，不能据此推定存在同名属性。

## 22.3\_寄存器块命名原例

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

[上一章](P021_ene_kb1200-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_gd_gd32-afio.md)
