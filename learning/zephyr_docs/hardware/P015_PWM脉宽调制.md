---
id: learning.zephyr-docs.hardware.pwm
title: PWM脉宽调制
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/pwm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="pwm-api"></a>

# 第15章\_PWM脉宽调制

原文：[Pulse Width Modulation (PWM)](https://docs.zephyrproject.org/latest/hardware/peripherals/pwm.html)。读取日期：2026-10-12，`latest`。

**脉宽调制（Pulse Width Modulation，PWM）**通过改变数字信号的占空比编码信息或控制功率。信号以一定频率在高低状态之间切换，一个周期中处于高电平的比例就是正常极性下的占空比。

典型用途包括调节 **发光二极管（Light-Emitting Diode，LED）** 亮度、直流电机速度、舵机位置、产生音调，以及降压/升压转换器和 D 类放大器等功率转换。原文分别以占空比对应亮度、平均电压与占空比成比例、脉宽编码角度、频率决定音调说明这些用途。

> 译注：LED 人眼感知亮度不必与占空比线性对应，电机转速也受负载和控制方式影响；这些是使用方向，不是通用精确传递关系。

## 15.1\_信号参数

周期是一次完整开关循环的持续时间，单位为纳秒；脉宽是高电平或有效状态持续时间，同样以纳秒计；占空比等于脉宽除以周期，通常用百分比表示。50% 表示有效状态占半个周期。

```text
|<-- pulse -->|
+--------------+            +-
|              |            |
+              +------------+
|<----------- period -------->|
```

> 译注：图和“高电平持续时间”的表述针对正常极性；反相极性下有效脉冲可为低电平，应同时考虑极性标志。

## 15.2\_驱动模型与单位

每个 PWM 控制器暴露一个或多个通道，以从零开始的索引标识，每通道驱动一个输出引脚。所有驱动采用 `include/zephyr/drivers/pwm.h` 的接口，核心函数 `pwm_set()` 设置通道周期与脉宽。

时间换算辅助宏包括：`PWM_HZ` 按 Hz 频率换成纳秒周期，例如 `PWM_HZ(1000)` 为 1 ms；`PWM_KHZ` 按 kHz 换算；`PWM_USEC` 将微秒周期或脉宽转成纳秒；`PWM_MSEC` 将毫秒转成纳秒。

> 译注：原文称通道“独立”，但实际硬件可能共享计数器和周期。通道号不同不保证频率可独立设置，必须核对目标驱动与定时器限制。

## 15.3\_设备树配置

设备树中用 `pwms` 属性描述 PWM。每个条目包含控制器 phandle、通道号、纳秒周期和绑定规定的极性标志：

```dts
/ {
    my_node {
        pwms = <&pwm0 0 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
        pwm-names = "servo";
    };
};
```

在 C 代码中通过 `PWM_DT_SPEC_GET` 系列宏取得配置：

```c
static const struct pwm_dt_spec servo =
    PWM_DT_SPEC_GET(DT_NODELABEL(my_node));
```

> 译注：原例把节点写成 `my_node { ... };`，但 C 使用 `DT_NODELABEL(my_node)`。节点名不自动成为节点标签，实际设备树需写为 `my_node: my_node { ... };`，或改用匹配路径的访问方式。设备树中的 PWM 宏也需有对应绑定头文件定义。

## 15.4\_使用示例

下面用 `pwm_dt_spec` 设置占空比：

```c
#include <zephyr/drivers/pwm.h>

static const struct pwm_dt_spec led_pwm =
    PWM_DT_SPEC_GET(DT_ALIAS(pwm_led0));

int set_led_brightness(uint8_t percent)
{
    if (!device_is_ready(led_pwm.dev)) {
        return -ENODEV;
    }

    /* pulse = period * duty_cycle / 100 */
    uint32_t pulse = led_pwm.period / 100 * percent;

    return pwm_set_dt(&led_pwm, led_pwm.period, pulse);
}
```

> 译注：应检查 `percent <= 100`。原例先除后乘会产生截断；需要更高精度时可先用足够宽的整数乘法，再除以 100，并确保最终参数不溢出。`device_is_ready()` 只检查设备就绪，不能替代参数范围检查。

下面用 20 ms 周期内的 1～2 ms 脉宽设置舵机角度：

```c
#include <zephyr/drivers/pwm.h>

#define SERVO_PERIOD_NS   PWM_MSEC(20)
#define SERVO_MIN_PULSE   PWM_USEC(1000)
#define SERVO_MAX_PULSE   PWM_USEC(2000)

int set_servo_angle(const struct device *pwm_dev, uint32_t channel,
                    uint8_t angle_deg)
{
    uint32_t pulse = SERVO_MIN_PULSE +
        (SERVO_MAX_PULSE - SERVO_MIN_PULSE) * angle_deg / 180;

    return pwm_set(pwm_dev, channel, SERVO_PERIOD_NS, pulse,
                   PWM_POLARITY_NORMAL);
}
```

> 译注：此例假设角度为 0～180 度，且设备采用所示脉宽范围。实际调用需检查角度、设备就绪状态与返回码；不同舵机的有效脉宽范围应按其规格确定。

## 15.5\_PWM捕获

部分控制器支持输入捕获，测量外部信号的周期或脉宽，可用于读取遥控接收器、传感器等输出的 PWM。

用 `pwm_configure_capture()` 配置，再调用 `pwm_enable_capture()` 启用。下例单次捕获周期和脉宽：

```c
void pwm_capture_cb(const struct device *dev, uint32_t channel,
                    uint32_t period_cycles, uint32_t pulse_cycles,
                    int status, void *user_data)
{
    if (status != 0) {
        return;
    }
    /* convert cycles to nanoseconds using pwm_get_cycles_per_sec() */
}

/* configure for single-shot capture of both period and pulse */
pwm_configure_capture(dev, channel,
                      PWM_CAPTURE_TYPE_BOTH | PWM_CAPTURE_MODE_SINGLE,
                      pwm_capture_cb, NULL);
pwm_enable_capture(dev, channel);
```

> 译注：回调的 `period_cycles`、`pulse_cycles` 是硬件周期计数，不是纳秒；原例提示通过 `pwm_get_cycles_per_sec()` 换算。配置和启用调用都需要检查返回值，具体控制器也不一定支持捕获。

## 15.6\_配置、接口与示例

配置项为 `CONFIG_PWM`、`CONFIG_PWM_SHELL`、`CONFIG_PWM_CAPTURE`、`CONFIG_PWM_EVENT`。接口分为 [PWM](P255_PWM公共接口.md) 与 [Fake PWM](P260_PWM模拟控制器.md)。

原页关联示例：

- [LED 渐变](https://docs.zephyrproject.org/latest/samples/basic/fade_led/README.html)：通过 PWM 调节 LED 亮度。
- [PWM 闪烁](https://docs.zephyrproject.org/latest/samples/basic/blinky_pwm/README.html)：使用 PWM 闪烁 LED。
- [PWM 捕获](P169_PWM输入捕获示例.md)：捕获 PWM 信号。
- [PWM 事件](P170_PWM事件示例.md)：处理 PWM 信号事件。
- [PWM RGB LED](https://docs.zephyrproject.org/latest/samples/basic/rgb_led/README.html)：驱动 RGB LED。
- [舵机](https://docs.zephyrproject.org/latest/samples/basic/servo_motor/README.html)：通过 PWM 驱动舵机。
- [声音](https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/sound/README.html)：使用 BBC micro:bit 的压电蜂鸣器。
- [STM32 PWM 主模式](https://docs.zephyrproject.org/latest/samples/boards/st/pwm/mastermode/README.html)：通过设备树配置定时器主从能力，实现实例同步。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SPI总线](P014_SPI总线.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：看门狗](P016_看门狗.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：SPI总线](P014_SPI总线.md) · [下一章：看门狗](P016_看门狗.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
