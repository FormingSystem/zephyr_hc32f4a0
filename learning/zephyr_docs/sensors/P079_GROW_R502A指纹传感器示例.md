---
id: learning.zephyr-docs.sensors.page-79
title: GROW_R502A指纹传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/grow_r502a/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="grow_r502a"></a>

# 第79章\_GROW\_R502A指纹传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/grow_r502a/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 79.1 概述（Overview）

本示例展示GROW R502-A指纹传感器（Fingerprint sensor）的以下功能：

1. 使用Zephyr子系统的LED API控制传感器指示灯。
2. 显示传感器中已保存的指纹数量。
3. 显示设备配置，包括波特率（Baud rate）、指纹库容量（Library size）、设备地址及UART帧中的数据包大小。
4. 设置`SENSOR_ATTR_RECORD_FREE_IDX`时，在指纹库中查找空闲索引。
5. 设置`SENSOR_ATTR_RECORD_ADD`时，向传感器添加新指纹。
6. 设置`SENSOR_ATTR_RECORD_FIND`时，尝试匹配输入指纹；匹配成功后返回ID和置信度（Confidence）。
7. 设置`SENSOR_ATTR_RECORD_DEL`时，从传感器删除指纹。

原文注：只有设置`SENSOR_TRIG_TOUCH`时，指纹添加功能才会工作。

> 译注——当前接口名称与调用方向：原文中的四个属性名按原样保留。当前扩展接口名称包含`R502A`，分别为`SENSOR_ATTR_R502A_RECORD_FREE_IDX`、`SENSOR_ATTR_R502A_RECORD_ADD`、`SENSOR_ATTR_R502A_RECORD_FIND`和`SENSOR_ATTR_R502A_RECORD_DEL`；查找空闲索引及匹配结果使用`sensor_attr_get()`，添加与删除使用`sensor_attr_set()`。匹配结果的`val1`是记录索引，`val2`是匹配分数，不是百分比概率。

<a id="wiring"></a>

## 79.2 接线（Wiring）

本示例使用外接传感器转接板（Breakout board）。必须提供设备树覆盖文件，标明UART总线和控制传感器的GPIO；还可使用所述可选GPIO为传感器供电。

<a id="references"></a>

## 79.3 参考资料（References）

更多信息见[GROW R502-A官方产品资料](http://en.hzgrow.com/product/143.html)。

<a id="building-and-running"></a>

> 译注——外链状态：原GROW产品入口本次返回403，网页工具也未能读取；链接保持原样，没有将无法读取的内容视为已核验资料。

## 79.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，先按官方入门说明准备主机工具、模块与目标工具链。原生模拟目标还须满足相应主机环境要求；硬件分支需要目标板、设备树节点和接线。下方命令及日志来自官方文档，本次没有运行模拟器或硬件实验。

提供用于指定传感器位置的设备树覆盖文件之后，使用以下命令构建示例：

```sh
# From the root of the zephyr repository
west build -b esp32_devkitc/esp32/procpu samples/sensor/grow_r502a
west flash
```

> 译注——示例会修改指纹库：当前程序启动后读取已有模板数量和参数，随后**尝试删除索引3的记录**，再查找空闲位置，等待触摸以录入新指纹；录入成功后的触摸进入匹配流程。这是具有存储修改动作的官方演示，不是只读查询。复现前先对照`main.c`确认使用的记录和测试设备；本次仅翻译并核对代码，没有运行这些动作。默认配置使用传感器自己的触发线程。

<a id="sample-output"></a>

## 79.5 示例输出（Sample Output）

```text
*** Booting Zephyr OS build v3.6.0-3147-g8ae1a2e2718e ***
template count : 4
baud 57600
addr 0xffffffff
lib_size 200
data_pkt_size 128
Fingerprint Deleted at ID #3
Fingerprint template free idx at ID #3
Waiting for valid finger to enroll as ID #3
Place your finger
Fingerprint successfully stored at #3
template count : 4
Matched ID : 2
confidence : 110
<repeats endlessly>
```

`<repeats endlessly>`表示之后可持续进行触摸及匹配。`addr 0xffffffff`是传感器通信地址，`ID`是指纹记录编号，均不是仓库文件地址。

<a id="see-also"></a>

## 79.6 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/grow_r502a/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grow_r502a/src/main.c)、[samples/sensor/grow_r502a/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grow_r502a/prj.conf)、[samples/sensor/grow_r502a/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grow_r502a/tests.yaml)、[samples/sensor/grow_r502a/boards/esp32_devkitc_procpu.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grow_r502a/boards/esp32_devkitc_procpu.overlay)、[include/zephyr/drivers/sensor/grow_r502a.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor/grow_r502a.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/grow_r502a/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grow_r502a/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/grow_r502a/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/grow_r502a/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P078_流量计示例.md) · [返回大纲](大纲.md) · [下一章](P080_心率传感器示例.md)
