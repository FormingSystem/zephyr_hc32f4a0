---
id: learning.zephyr-docs.board-samples.page-54
title: ArgonKey传感器
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/96boards/argonkey/sensors/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="argonkey_sensors"></a>

# 第54章\_传感器（Sensors）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/96boards/argonkey/sensors/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/96boards/argonkey/sensors/README.rst/..)

<a id="overview"></a>

## 54.1 概述（Overview）

本示例展示如何读取 ArgonKey 开发板的传感器数据，并在控制台显示结果。示例同时使用触发（Trigger）与轮询（Poll）方式。

<a id="requirements"></a>

## 54.2 前提条件（Requirements）

本示例只需要 ArgonKey 开发板，可以采用以下两种供电方式之一：

- 夹层板模式（Mezzanine mode）：通过 96Board 低速连接器将 ArgonKey 插接到 HiKey 开发板。

- 独立模式（Standalone mode）：通过 P1 连接器直接提供 5 V 电源。

可以在 [samples/boards/96boards/argonkey/sensors/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/96boards/argonkey/sensors/prj.conf) 中启用或取消启用相应传感器。

注意，所有传感器相关代码都使用 `#ifdef` 指令进行条件编译，因此原文预期此示例在相应选择下总能正确构建。例如：

> 译注——条件编译的边界：#ifdef 只排除未启用分支；已选择驱动仍须满足 Kconfig 依赖、设备树实例及硬件连接要求，不能据此认为任何配置都保证构建、初始化成功。

```text
#ifdef CONFIG_HTS221
  struct device *hum_dev = DEVICE_DT_GET_ONE(st_hts221);

  if (!device_is_ready(hum_dev)) {
    printk("%s: device not ready.\n", hum_dev->name);
    return;
  }
#endif
```

<a id="references"></a>

## 54.3 参考资料（References）

- [Argonkey](https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html#96b_argonkey)

<a id="building-and-running"></a>

## 54.4 构建与运行（Building and Running）

> 译注——执行前提：本节 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链及对应板。构建目录由工具生成，下载与启动方式按具体板文档核对。本次仅核对文档和源码，未执行构建、烧录或硬件实验。

```text
west build -b 96b_argonkey samples/boards/96boards/argonkey/sensors
west build -t run
```

<a id="sample-output"></a>

### 54.4.1 输出示例（Sample Output）

USB 转 TTL 1.8 V 串口线可以连接到开发板背面低速连接器的 P3.5（TX）与 P3.7（RX）。可使用 minicom 等简单终端仿真器采集输出。

> ```text
> proxy: 1  ;
> distance: 0 m -- 09 cm;
> temp: 30.35 C; press: 97.466259 kPa
> humidity: 43.500000 %RH
> accel (0.004000 -0.540000 9.757000) m/s^2
> gyro (0.065000 -0.029000 -0.001000) rad/s
> magn (0.049500 0.208500 -0.544500) G
> - (6) (trig_cnt: 1878)
>
> <repeats endlessly every 2s>
> ```

本例每两秒轮询一次传感器，产生输出。

> 译注——输出周期与采样率：源码每轮休眠两秒，LSM6DSL 的加速度和角速度输出数据率（Output Data Rate，ODR）另设为 104 Hz。两秒是控制台轮询周期，不是所有传感器的硬件采样周期；trig_cnt 是已收到的触发次数，不能按循环次数解释。

传感器数据按以下顺序打印；未启用的传感器不打印数据：

1. VL53L0x 接近检测（Proximity）。

2. LPS22HB 气压／温度（Barometric pressure／Temperature）。

3. HTS221 湿度（Humidity）。

4. LSM6DSL 加速度（Acceleration）。

5. LSM6DSL 角速度（Gyroscope）。

6. LIS2MDL 磁力计（Magnetometer，连接到 LSM6DSL）。

接近传感器显示两行信息：

- 距离小于 10 cm 时置位的标志（proxy）。

- 到障碍物的绝对距离。

最后一行显示已收到的触发中断次数。启用 ARGONKEY_TEST_LOG 宏后，可显示每次触发时读取的传感器数据。

> 译注——日志单位：press 是压力，humidity 是相对湿度（Relative Humidity，RH），accel 是加速度，gyro 是角速度，magn 是磁场；G 表示高斯（Gauss）。原始日志数值只表示一次采集，启用逐次触发日志还可能改变串口负载和观察时序。

> 译注——源码入口：[main.c](../../../samples/boards/96boards/argonkey/sensors/src/main.c)；[prj.conf](../../../samples/boards/96boards/argonkey/sensors/prj.conf)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/96boards/argonkey/sensors/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/96boards/argonkey/sensors/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/96boards/argonkey/sensors/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P053_ArgonKey麦克风.md) · [返回大纲](大纲.md) · [下一章](P055_ArgonKey示例目录.md)
