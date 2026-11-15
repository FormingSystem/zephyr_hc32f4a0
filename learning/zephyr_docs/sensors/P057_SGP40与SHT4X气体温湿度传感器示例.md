---
id: learning.zephyr-docs.sensors.page-57
title: SGP40与SHT4X气体温湿度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/sgp40_sht4x/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sgp40_sht4x"></a>

# 第57章\_SGP40与SHT4X气体温湿度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/sgp40_sht4x/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="description"></a>

## 57.1 说明（Description）

本示例周期性测量SGP40与SHT4X设备提供的环境温度（Ambient temperature）、湿度（Humidity）和原始气体传感器值（Raw gas sensor value），并在控制台输出结果。

可以将SHT4X测得的数值传给SGP40，以使用其片上温度／相对湿度补偿（Temperature/Relative Humidity compensation，T/RH compensation）。应用默认启用此功能；设置`APP_USE_COMPENSATION=n`可关闭它。

SHT4X还可以使用加热器（Heater），这对某些环境或应用有意义，具体条件参阅数据手册。要使用加热器，请查看本应用的Kconfig配置选项。

> 译注——配置写法：原文的`APP_USE_COMPENSATION`是Kconfig符号名；在`.conf`配置文件中写作`CONFIG_APP_USE_COMPENSATION=n`。当前实现先取得SHT4X温湿度，再把整数部分传给SGP40补偿属性，当前SGP40驱动也只使用`val1`；这条路径并没有传递小数部分精度。

<a id="references"></a>

## 57.2 参考资料（References）

- [SHT4X传感器官方产品资料](https://sensirion.com/products/catalog/SHT40)。
- [SGP40传感器官方产品资料](https://sensirion.com/products/catalog/SGP40)。

<a id="wiring"></a>

## 57.3 接线（Wiring）

示例通过I2C接口控制SHT4X和SGP40。连接电源引脚`VDD`、`GND`及接口引脚`SDA`、`SCL`。供电电压范围为1.7—3.6 V。根据所用底板，SDA和SCL线路可能需要上拉电阻（Pull-up resistor）。

<a id="building-and-running"></a>

## 57.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目向控制台输出传感器数据，需要SHT4X与SGP40两个传感器。原文说明它应可用于具有I2C外设接口的平台，并提供[Black Pill V2.0](https://docs.zephyrproject.org/latest/boards/weact/blackpill_f411ce/doc/index.html#blackpill_f411ce)开发板的示例设备树覆盖文件（Devicetree overlay）。

```sh
# From the root of the zephyr repository
west build -b blackpill_f411ce samples/sensor/sgp40_sht4x
west flash
```

> 译注——加热与读取顺序：当前应用默认不启用加热器。启用后，满足湿度阈值且温度低于代码规定上限时，执行带加热的读取，只更新湿度值；随后仍使用先前读取的温度参与补偿和显示。普通分支每轮休眠2秒，启用加热且选择长脉冲时休眠20秒。这是示例的实现行为，实际加热条件和占空比应结合对应器件资料核对。

<a id="sample-output"></a>

### 57.4.1 示例输出（Sample Output）

```text
*** Booting Zephyr OS build v2.6.0-rc1-315-g50d8d1187138  ***
SHT4X: 23.64 Temp. [C] ; 30.74 RH [%] -- SGP40: 30531 Gas [a.u.]
[00:00:00.250,000] <dbg> SGP40.sgp40_init: SGP40: Selftest succeeded!
SHT4X: 23.66 Temp. [C] ; 32.16 RH [%] -- SGP40: 30541 Gas [a.u.]
SHT4X: 23.63 Temp. [C] ; 30.83 RH [%] -- SGP40: 30522 Gas [a.u.]
```

数据手册说明SGP40的原始信号与传感器电阻的对数成正比，因此示例将其单位标为`[a.u.]`，表示任意单位（Arbitrary units）。

> 译注——读数含义：`RH [%]`是相对湿度百分数，`Gas [a.u.]`是原始气体信号，不能直接当成ppm浓度或已经计算好的VOC指数（VOC Index）。当前示例打印的是驱动返回的原始值，没有在本应用内运行VOC指数算法。

<a id="see-also"></a>

## 57.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/sgp40_sht4x/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/src/main.c)、[samples/sensor/sgp40_sht4x/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/prj.conf)、[samples/sensor/sgp40_sht4x/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/tests.yaml)、[samples/sensor/sgp40_sht4x/boards/blackpill_f411ce.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/boards/blackpill_f411ce.overlay)、[drivers/sensor/sensirion/sgp40/sgp40.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/sensor/sensirion/sgp40/sgp40.c)、[samples/sensor/sgp40_sht4x/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/Kconfig)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/sgp40_sht4x/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sgp40_sht4x/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/sgp40_sht4x/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/sgp40_sht4x/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P056_MS5837数字压力传感器示例.md) · [返回大纲](大纲.md) · [下一章](P058_APDS9960颜色光照与手势传感器示例.md)
