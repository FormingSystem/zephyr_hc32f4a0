---
id: learning.zephyr-docs.can-driver-reference.page-3
title: CAN收发器头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/can_2transceiver_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CAN收发器头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/can_2transceiver_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入CAN控制器与收发器头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

CAN收发器驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/can.h>
#include <zephyr/device.h>
```

查看此文件的源码。

CAN收发器驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_can_5Ftransceiver_5Fdriver_5Fapi"></a>

```c
struct can_transceiver_driver_api
```

相关声明：[can_transceiver_driver_api](../hardware/P055_CAN收发器操作结构.md)。

驱动操作（Driver Operations）：CAN收发器驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_gac9de770d729b6427979d83b2904f07cf"></a>

```c
typedef int(* can_transceiver_enable_t) (const struct device *dev, can_mode_t mode)
```

相关声明：[can_transceiver_enable_t](../hardware/P050_CAN收发器驱动后端接口.md#gac9de770d729b6427979d83b2904f07cf)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

使能CAN收发器时调用的回调API。

<a id="r_gacc56ddc312a7205bfadb9b612372b89c"></a>

```c
typedef int(* can_transceiver_disable_t) (const struct device *dev)
```

相关声明：[can_transceiver_disable_t](../hardware/P050_CAN收发器驱动后端接口.md#gacc56ddc312a7205bfadb9b612372b89c)、[device](../device_reference/P002_设备对象结构.md)。

禁用CAN收发器时调用的回调API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga0d0e87150b49198c41e2782a17cfd694"></a>

```c
static int can_transceiver_enable (const struct device *dev, can_mode_t mode)
```

相关声明：[can_transceiver_enable](../hardware/P041_CAN收发器接口参考.md#ga0d0e87150b49198c41e2782a17cfd694)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

使能CAN收发器（Enable）。

<a id="r_ga7509ca0b6ece81b4038b7d128af961be"></a>

```c
static int can_transceiver_disable (const struct device *dev)
```

相关声明：[can_transceiver_disable](../hardware/P041_CAN收发器接口参考.md#ga7509ca0b6ece81b4038b7d128af961be)、[device](../device_reference/P002_设备对象结构.md)。

禁用CAN收发器（Disable）。

## 3.4\_源码定位与版本边界

相对源码定位：[CAN控制器头文件](../../../include/zephyr/drivers/can.h)、[CAN收发器头文件](../../../include/zephyr/drivers/can/transceiver.h)、[公共实现](../../../drivers/can/can_common.c)、[系统调用处理](../../../drivers/can/can_handlers.c)、[配置选项](../../../drivers/can/Kconfig)、[GPIO收发器实现](../../../drivers/can/transceiver/can_transceiver_gpio.c)、[经典CAN绑定](../../../dts/bindings/can/can-controller.yaml)、[CAN FD绑定](../../../dts/bindings/can/can-fd-controller.yaml)和[可配置错误检查](../../../include/zephyr/sys/check.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：使用层级：官方约定由CAN控制器驱动管理收发器，应用通常调用can_start／can_stop，而不是直接切换收发器。使能／禁用包装直接调用can_transceiver设备类别的操作指针，不额外检查NULL或设备就绪；调用方需要传入正确的关联设备，不能把控制器指针当作收发器指针。

> 译注——源码核对：GPIO收发器实例：本次核对的通用GPIO实现至少需要enable-gpios或standby-gpios。初始化将使能信号置为逻辑无效、待机信号置为逻辑有效；使能时反过来，GPIO设备树极性决定实际电平。此实现忽略mode参数，不应推广为所有收发器都能提供监听等模式切换能力。运行时GPIO写入失败映射为-EIO。

> 译注——源码核对：操作不是事务：GPIO实现按顺序写enable再写standby，如果后一项失败，不回滚前一项。收到错误不能假定所有引脚仍处于调用前状态。收发器使能、CAN控制器启动与成功收发帧分别需要各自证据，文档与源码对照没有替代电气连接或总线实测。

> 译注——源码核对：版本边界：本批核对控制器与收发器头文件、CAN公共实现、系统调用处理、Kconfig、GPIO收发器实现、经典CAN与CAN FD绑定以及CHECKIF定义，共九份官方源码并记录摘要。两份源码页的非注释代码分别与读取的官方头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接CAN总线、发送帧或操作硬件。

本次验证范围为文档与源码对照，未构建固件、连接CAN总线或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [zephyr/drivers/can.h](P002_CAN驱动头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](P004_CAN收发器头文件源码.md)
- [can_transceiver_driver_api](../hardware/P055_CAN收发器操作结构.md)
- [can_transceiver_enable_t](../hardware/P050_CAN收发器驱动后端接口.md#gac9de770d729b6427979d83b2904f07cf)
- [device](../device_reference/P002_设备对象结构.md)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [can_transceiver_disable_t](../hardware/P050_CAN收发器驱动后端接口.md#gacc56ddc312a7205bfadb9b612372b89c)
- [can_transceiver_enable](../hardware/P041_CAN收发器接口参考.md#ga0d0e87150b49198c41e2782a17cfd694)
- [can_transceiver_disable](../hardware/P041_CAN收发器接口参考.md#ga7509ca0b6ece81b4038b7d128af961be)

<a id="header-details"></a>

---

[上一章](P002_CAN驱动头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_CAN收发器头文件源码.md)
