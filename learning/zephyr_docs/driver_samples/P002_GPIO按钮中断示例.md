---
id: learning.zephyr-docs.driver_samples.page-2
title: GPIO按钮中断示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/gpio/button_interrupt/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="button_interrupt"></a>

# 第2章\_GPIO按钮中断示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/gpio/button_interrupt/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 2.1\_概览（Overview）

本例演示带中断（Interrupt）的通用输入输出（General-Purpose Input/Output，GPIO）输入。每次按下按钮，程序都会在控制台输出一条消息。

<a id="requirements"></a>

## 2.2\_硬件与配置要求（Requirements）

开发板必须有一个通过GPIO引脚连接的按钮。许多[受支持开发板及扩展板](https://docs.zephyrproject.org/latest/boards/index.html#boards)将其称为用户按钮（User Button）。

按钮必须通过 `sw0` [设备树](../devicetree/P013_设备树文档入口.md#dt-guide)别名配置，通常位于 [BOARD.dts文件](../devicetree/P004_输入与输出文件.md#devicetree-in-out-files)中。对不支持的板构建时，会出现：

```text
Unsupported board: sw0 devicetree alias is not defined
```

这条错误表示sw0设备树别名未定义。若sw0存在但定义不正确，也可能出现其他构建错误。

本例还支持可选的 `led0` 别名，与[LED闪烁示例](../getting_started/P004_LED闪烁示例.md#blinky)使用相同别名。提供该别名后，按下按钮时LED亮起，释放时熄灭。

<a id="devicetree-details"></a>

### 2.2.1\_设备树细节（Devicetree details）

以下是支持本例的最小设备树片段，只包含sw0，为简洁省略了可选led0：

```dts
/ {
        aliases {
                sw0 = &button0;
        };

        soc {
                gpio0: gpio@0 {
                        status = "okay";
                        gpio-controller;
                        #gpio-cells = <2>;
                        /* ... */
                };
        };

        buttons {
                compatible = "gpio-keys";
                button0: button_0 {
                        gpios = <&gpio0 PIN FLAGS>;
                        label = "User button";
                };
                /* ... other buttons ... */
        };
};
```

sw0必须指向一个子节点，该子节点的父节点具有 `gpio-keys` [兼容字符串](../devicetree/P003_语法与结构.md#dt-important-props)。

这个常见配置中，`gpio0` 是指向GPIO控制器的示例节点标签（Node Label）；`PIN` 应替换为引脚号，例如 `8` 或 `0`；`FLAGS` 为适用于按钮的[GPIO配置标志](../hardware/P005_GPIO.md#gpio-api)组合，例如 `(GPIO_PULL_UP | GPIO_ACTIVE_LOW)`。

原例假定gpio0节点中 `#gpio-cells = <2>`，GPIO控制器的绑定（Binding）将两个单元（Cell）命名为pin和flags：

```yaml
gpio-cells:
  - pin
  - flags
```

本例要求 `gpios` 属性含 `pin` 单元；`flags` 单元可选，没有它仍可工作。

> 译注——片段用途：设备树与YAML块分别是节点配置和绑定格式示意，不能作为Shell命令执行。PIN、FLAGS及省略部分都要按真实板补齐；示例gpio@0不表示任意芯片的控制器地址。标志表达式中的 `|` 是按位或（Bitwise OR），用于组合独立标志位。

<a id="building-and-running"></a>

## 2.3\_构建与运行（Building and Running）

本例可用于多种开发板，原文以nucleo_f103rb为例：

```bash
west build -b nucleo_f103rb samples/drivers/gpio/button_interrupt
```

从Zephyr源码根构建，使用已经准备好工具链和模块的west环境。原文描述：启动后查找预定义GPIO设备，将引脚设为输入并启用下降沿中断；主循环每轮监视GPIO状态并输出到串口控制台。按钮按下时，中断处理函数输出事件和时间戳。

> 译注——以当前实现对照原文：[官方main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gpio/button_interrupt/src/main.c)使用GPIO_INT_EDGE_TO_ACTIVE，即转为逻辑有效状态的边沿；低有效按钮对应下降沿，高有效按钮可能对应上升沿。回调打印的时间值来自k_cycle_get_32，是周期计数而非直接以毫秒计时。所读版本的主循环在有LED时复制按钮逻辑状态到LED，没有每轮打印GPIO状态；原页这部分描述与源码存在差异。观察不到按键事件时，先核对别名、引脚、有效电平和中断配置。

<a id="see-also"></a>

## 2.4\_相关接口（See also）

[GPIO接口参考](../hardware/P266_GPIO公共接口.md)。


对应官方文档源码：[samples/drivers/gpio/button_interrupt/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gpio/button_interrupt/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/gpio/button_interrupt/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/gpio/button_interrupt/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P001_DAC数模转换示例.md) · [返回大纲](大纲.md) · [下一章](P003_SPI实时IO回环示例.md)
