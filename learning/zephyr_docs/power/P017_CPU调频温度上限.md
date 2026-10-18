---
id: learning.zephyr-docs.power.cpufreq-5
title: CPU调频温度上限
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/services/cpu_freq/thermal_cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第17章\_CPU调频温度上限

原文：[CPU Frequency Thermal Cap](https://docs.zephyrproject.org/latest/services/cpu_freq/thermal_cap.html)。读取日期：2026-10-13，`latest`。

## 17.1\_性能需求与温度约束

温度限制（Thermal Cap）是[CPU调频子系统](P012_CPU调频概述.md)的可选约束层。CPU 即中央处理器（Central Processing Unit）。活动策略选择请求的性能状态（Performance State，P-state），温度触发点（Temperature Trip Point）生效时，温度约束限制允许使用的最高性能状态。

这样便将性能需求和降温控制分开：调频策略依据自己的指标与阈值选择请求状态；温度约束再将请求限制在当前温度所允许的最高性能范围内。限制处理后的状态交给片上系统（System on Chip，SoC）的性能状态驱动。

## 17.2\_设备树配置

在设备树（Devicetree）中添加兼容标识为 `zephyr,cpu-freq-thermal-cap` 的节点，并启用 Kconfig 配置选项 [`CONFIG_CPU_FREQ_THERMAL_CAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_THERMAL_CAP)，即可开启此功能。

示例中的 `trip_0`、`trip_1` 是温度触发点节点，`pstate_1`、`pstate_2` 是所引用的性能状态节点标签：

```devicetree
cpu_freq_thermal_cap: cpu_freq_thermal_cap {
        compatible = "zephyr,cpu-freq-thermal-cap";
        sensor = <&temp0>;
        sensor-channel = "die-temp";
        polling-delay-ms = <1000>;
        trip-active-polling-delay-ms = <100>;

        trip_0 {
                temperature-millicelsius = <85000>;
                hysteresis-millicelsius = <5000>;
                cap-pstate = <&pstate_1>;
        };

        trip_1 {
                temperature-millicelsius = <95000>;
                hysteresis-millicelsius = <3000>;
                cap-pstate = <&pstate_2>;
        };
};
```

`trip_0` 生效时，CPU 频率请求限制为 `pstate_1` 或更低性能状态；`trip_1` 生效时，限制为 `pstate_2` 或更低性能状态。约束不会强制 CPU 运行在指定状态；如果策略本来就请求更低性能状态，请求保持不变。

温度约束使用 CPU 性能状态的索引顺序：索引越小，性能越高；索引越大，性能越低，约束越严格。每个 `cap-pstate` 必须通过节点引用（Phandle）引用这一有序表中的性能状态。

完整属性定义见[温度约束绑定](../hardware/P622_CPU调频温度约束绑定.md)。

## 17.3\_运行时行为

因为传感器驱动可能执行阻塞操作，温度采样在可延迟工作项（Delayable Work Item）中完成。CPU 调频定时器应用策略结果时，只读取缓存的限制值。

原文说明，如果温度采样连续失败，约束层应用最低性能状态，即表中索引最大的状态，作为故障安全（Fail-Safe）约束。

译注：[官方Kconfig源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig)还提供 `CONFIG_CPU_FREQ_THERMAL_CAP_FAIL_SAFE` 开关，默认启用；禁用后保留上次计算的温度限制。连续失败阈值由 `CONFIG_CPU_FREQ_THERMAL_CAP_SENSOR_FAILURE_LIMIT` 控制，默认3次，范围1～255。原文上述故障安全行为应结合这些配置理解。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：时序噪声CPU调频策略](P016_时序噪声CPU调频策略.md) · [本模块主线目录](../reading/power.md) · [全部主线](../reading/README.md) · [下一篇：电源管理接口目录](P030_电源管理接口目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：时序噪声CPU调频策略](P016_时序噪声CPU调频策略.md) · [下一章：CPU调频示例目录](P018_CPU调频示例目录.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
