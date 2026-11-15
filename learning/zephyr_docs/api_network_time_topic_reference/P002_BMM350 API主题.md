---
id: learning.zephyr-docs.api-network-time-topic-reference.page-2
title: BMM350 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_BMM350 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Bosch BMM350 三轴磁力计（3-Axis Magnetometer）。

<a id="details"></a>

Bosch BMM350 三轴磁力计（3-Axis Magnetometer）。

<a id="header-files"></a>
<a id="files"></a>

## 2.1\_文件（Files）

<a id="r_bmm350_2Eh"></a>

```c
file bmm350.h
```

相关声明：[bmm350.h](../api_file_configuration_reference/P011_zephyr__drivers__sensor__bmm350.h_文件参考.md)。

BMM350传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.2\_数据结构（Data Structures）

<a id="r_bmm350_5Fself_5Ftest_5Fresult"></a>

```c
struct bmm350_self_test_result
```

相关声明：[bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)。

BMM350 用户自检结果（User Self-test Result）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga48fad26fc2836975d1fddc7ae7b167b0"></a>

```c
int bmm350_self_test (const struct device *dev, struct bmm350_self_test_result *result)
```

相关声明：[bmm350_self_test](#ga48fad26fc2836975d1fddc7ae7b167b0)、[device](../device_reference/P002_设备对象结构.md)、[bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)。

运行 BMM350 内置用户自检（Built-In User Self-Test）。

<a id="r_ga482a53ae8c68a549e1436215cbc47302"></a>

```c
int bmm350_magnetic_reset (const struct device *dev)
```

相关声明：[bmm350_magnetic_reset](#ga482a53ae8c68a549e1436215cbc47302)、[device](../device_reference/P002_设备对象结构.md)。

执行磁复位（Magnetic Reset）。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga482a53ae8c68a549e1436215cbc47302"></a>

### `bmm350_magnetic_reset()`

```c
int bmm350_magnetic_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor/bmm350.h>
```

执行磁复位（Magnetic Reset）。

BMM350 提供从过强磁场影响中恢复的措施。设备复位后会自行触发磁复位（magnetic reset），但如果在挂起模式（suspend mode）下受到过强磁场作用，传感器无法检测该事件。如果明显的偏移或灵敏度漂移表明可能发生过这种情况，应用程序可以调用此函数。

较新 BMM350 修订版本支持的“增强型”磁复位（Enhanced Magnetic Reset）尚未实现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga48fad26fc2836975d1fddc7ae7b167b0"></a>

### `bmm350_self_test()`

```c
int bmm350_self_test ( const struct device * dev, struct bmm350_self_test_result * result )
```

```c
#include <zephyr/drivers/sensor/bmm350.h>
```

运行 BMM350 内置用户自检（Built-In User Self-Test）。

按照 Bosch SensorAPI 的流程，重新初始化隧道磁阻（TMR）传感器，并测量 X、Y 轴对正、负激励（excitation）的响应。返回时恢复调用前的设备配置。

调用方负责根据设备自检限值（self-test limit，参见 BMM350 数据手册）判断结果；此函数仅报告测得的响应。

传感器正在流式传输（streaming）时不得调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `result` | 输出：各轴的自检响应及差值（deltas）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 2.5\_原页交叉引用（Cross References）

- [bmm350.h](../api_file_configuration_reference/P011_zephyr__drivers__sensor__bmm350.h_文件参考.md)
- [bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_ADXL313 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_操作码聚合器客户端模型（Opcodes Aggregator Client model）.md)
