---
id: learning.zephyr-docs.hardware.gpio
title: 通用输入输出GPIO
kind: reference
status: maintained
domains: [zephyr, gpio, driver]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/gpio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="gpio-api"></a>

# 第5章\_通用输入输出GPIO

原文：[General-Purpose Input/Output (GPIO)](https://docs.zephyrproject.org/latest/hardware/peripherals/gpio.html)。读取日期：2026-10-12，`latest`。

**通用输入输出（General-Purpose Input/Output，GPIO）**是没有固定专用功能、可由软件配置为输入或输出的数字信号引脚。

## 5.1\_功能概览

GPIO **应用程序编程接口（Application Programming Interface，API）** 提供统一的引脚访问方式，应用可以配置输入输出、读写状态和管理中断，主要能力包括：

- **引脚配置**：输入、输出或断开；内部上下拉及驱动强度配置。
- **数据访问**：读取输入值，写入输出值。
- **中断**：按上升沿、下降沿、低电平或高电平触发，并注册回调处理。
- **设备树集成**：通常在设备树中定义 GPIO，通过 `gpio_dt_spec` 让驱动和应用以不绑定具体硬件的方式引用它。

## 5.2\_设备树配置

GPIO 控制器节点带 `gpio-controller` 属性。`#gpio-cells` 通常为 `2`，表示引用一个 GPIO 时需要两个单元：引脚号与标志。

控制器定义示例：

```dts
gpio0: gpio@40022000 {
    compatible = "ti,cc13xx-cc26xx-gpio";
    reg = <0x40022000 0x400>;
    interrupts = <0 0>;
    gpio-controller;
    #gpio-cells = <2>;
};
```

引用 GPIO 的例子：

```dts
leds {
    compatible = "gpio-leds";
    led0: led_0 {
        gpios = <&gpio0 25 GPIO_ACTIVE_HIGH>;
        label = "Green LED";
    };
};
```

## 5.3\_基本操作

GPIO 操作通常通过 `gpio_dt_spec` 结构进行。它保存设备树中描述的引脚信息，通常由 `GPIO_DT_SPEC_GET` 或其变体填充。

若 GPIO 对应设备树别名 `led0`，可这样取得描述：

```c
#define LED0_NODE DT_ALIAS(led0)
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED0_NODE, gpios);
```

随后可将其配置为输出，初始保持非活动，再设置为活动状态：

```c
int ret;

ret = gpio_pin_configure_dt(&led, GPIO_OUTPUT_INACTIVE);
if (ret < 0) {
    return ret;
}

ret = gpio_pin_set_dt(&led, 1);
if (ret < 0) {
    return ret;
}
```

完整示例见[LED 闪烁](../getting_started/P004_LED闪烁示例.md)。也可以直接通过 GPIO 控制器设备指针操作；这时使用 `gpio_pin_configure()` 等接口，而不是接收描述结构的 `gpio_pin_configure_dt()`。

> 译注：前面的 **设备树源文件（Devicetree Source，DTS）** 只定义了节点标签 `led0:`，没有展示 `/aliases`；`DT_ALIAS(led0)` 还要求在设备树的 `aliases` 节点中定义 `led0 = &led0;`。另外，“活动”是逻辑意义，会受 `GPIO_ACTIVE_LOW/HIGH` 影响，不应总理解为物理高电平。

## 5.4\_GPIO Hogs

GPIO hog 机制在系统初始化时自动配置引脚，适合复位线、电源使能等只需设定初始状态、不需要应用在运行时控制的信号。

Hog 节点位于 GPIO 控制器下：`gpio-hog` 标明该节点用途，`gpios` 指定引脚和活动状态，`input`、`output-low`、`output-high` 之一指定配置。

设备树 overlay 示例：

```dts
&gpio0 {
    hog1 {
        gpio-hog;
        gpios = <1 GPIO_ACTIVE_LOW>;
        output-high;
    };

    hog2 {
        gpio-hog;
        gpios = <2 GPIO_ACTIVE_HIGH>;
        output-low;
    };
};
```

如果除了自动初始配置，还需要运行时控制这类引脚，可考虑改用[稳压器子系统](P106_稳压器.md)，并创建 [regulator-fixed 节点](P635_固定稳压器设备树绑定.md)。

## 5.5\_配置选项

原文列出的主要配置项如下，具体依赖和默认值见对应 Kconfig 说明：

- [CONFIG_GPIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)
- [CONFIG_GPIO_SHELL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_SHELL)
- [CONFIG_GPIO_GET_DIRECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_DIRECTION)
- [CONFIG_GPIO_GET_CONFIG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_CONFIG)
- [CONFIG_GPIO_HOGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_HOGS)
- [CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT)

## 5.6\_API与相关示例

完整接口见[官方 GPIO API](P266_GPIO公共接口.md)。原文关联的全部示例如下，尚未翻译的保持官方入口：

| 示例 | 内容 |
| --- | --- |
| [B-M2MEM-PACK1 扩展板](https://docs.zephyrproject.org/latest/samples/shields/b_m2mem_pack1/README.html) | 根据识别 EEPROM 中的数据检查内存模块。 |
| [基本线程操作](https://docs.zephyrproject.org/latest/samples/basic/threads/README.html) | 创建多个线程闪烁 **发光二极管（Light-Emitting Diode，LED）** 并输出控制台信息。 |
| [LED 闪烁](../getting_started/P004_LED闪烁示例.md) | 使用 GPIO API 持续闪烁 LED。 |
| [按钮中断](../driver_samples/P002_GPIO按钮中断示例.md) | 通过中断处理 GPIO 输入。 |
| [GPIO 唤醒引脚](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/wkup_pins/README.html) | 使用 GPIO 唤醒系统。 |
| [自定义设备树绑定控制 GPIO](https://docs.zephyrproject.org/latest/samples/basic/custom_dts_binding/README.html) | 用自定义绑定描述和控制 GPIO。 |
| [HD44780 LCD 控制器](../driver_samples/P045_HD44780液晶控制器示例.md) | 通过 GPIO 驱动基于 HD44780 的 LCD。 |
| [Pico W Wi-Fi 与 LED](https://docs.zephyrproject.org/latest/samples/boards/raspberrypi/pico_w_wifi_led/README.html) | 扫描 Wi-Fi 网络时闪烁板载 LED。 |
| [X-NUCLEO-53L0A1 扩展板](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_53l0a1/README.html) | 使用七段显示器和 VL53L0X 测距传感器。 |

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：引脚控制](P004_引脚控制.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：通用异步收发器UART](P006_UART.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：引脚控制](P004_引脚控制.md) · [下一章：UART](P006_UART.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
