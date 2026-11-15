---
id: learning.zephyr-docs.can-driver-reference.page-4
title: CAN收发器头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/can_2transceiver_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_CAN收发器头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/can_2transceiver_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_CAN收发器头文件参考.md)和[公共API](../hardware/P041_CAN收发器接口参考.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00053"></a>
<a id="foldopen00077"></a>
<a id="foldopen00096"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2can_8h_html"></a>
<a id="agroup__can__controller_html_ga0b2a1456e66f4522a30cf1400fdfced7"></a>
<a id="agroup__can__transceiver__backend_html_gac9de770d729b6427979d83b2904f07cf"></a>
<a id="agroup__can__transceiver__backend_html_gacc56ddc312a7205bfadb9b612372b89c"></a>
<a id="agroup__can__transceiver_html_ga0d0e87150b49198c41e2782a17cfd694"></a>
<a id="agroup__can__transceiver_html_ga7509ca0b6ece81b4038b7d128af961be"></a>
<a id="astructcan__transceiver__driver__api_html"></a>
<a id="astructcan__transceiver__driver__api_html_ab28e2f8f1bbf96942349e1ae0b352d68"></a>
<a id="astructcan__transceiver__driver__api_html_afbf86ddecfcc818a9c84dd6fd0807505"></a>
<a id="astructdevice_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2022 Vestas Wind Systems A/S
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_CAN_TRANSCEIVER_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_DRIVERS_CAN_TRANSCEIVER_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/drivers/can.h&gt;
<a id="l00017"></a>#include &lt;zephyr/device.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00042"></a>typedef int (*can_transceiver_enable_t)(const struct device *dev, can_mode_t mode);
<a id="l00043"></a>
<a id="l00048"></a>typedef int (*can_transceiver_disable_t)(const struct device *dev);
<a id="l00049"></a>
<a id="l00053"></a>__subsystem struct can_transceiver_driver_api {
<a id="l00055"></a>        can_transceiver_enable_t enable;
<a id="l00057"></a>        can_transceiver_disable_t disable;
<a id="l00058"></a>};
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00077"></a>static inline int can_transceiver_enable(const struct device *dev, can_mode_t mode)
<a id="l00078"></a>{
<a id="l00079"></a>        return DEVICE_API_GET(can_transceiver, dev)-&gt;enable(dev, mode);
<a id="l00080"></a>}
<a id="l00081"></a>
<a id="l00096"></a>static inline int can_transceiver_disable(const struct device *dev)
<a id="l00097"></a>{
<a id="l00098"></a>        return DEVICE_API_GET(can_transceiver, dev)-&gt;disable(dev);
<a id="l00099"></a>}
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00105"></a>#ifdef __cplusplus
<a id="l00106"></a>}
<a id="l00107"></a>#endif
<a id="l00108"></a>
<a id="l00109"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_CAN_TRANSCEIVER_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2022 Vestas Wind Systems A/S；Apache-2.0许可证原文保留。

2. 结束CAN收发器头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_CAN_TRANSCEIVER_H_。

## 4.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API与宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `DEVICE_API_GET`

```c
#define DEVICE_API_GET(_class, _dev)
```

展开为指定设备类别的设备API指针。

定义位置（Definition）：device.h:1486。

符号定位：[DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)。

### `can.h`

CAN（控制器局域网，Controller Area Network）控制器驱动API的头文件。

符号定位：[can.h](P001_CAN驱动头文件参考.md)。

### `can_mode_t`

```c
uint32_t can_mode_t
```

提供用于保存CAN控制器配置标志的类型。

定义位置（Definition）：can.h:122。

符号定位：[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

### `can_transceiver_enable_t`

```c
int(* can_transceiver_enable_t)(const struct device *dev, can_mode_t mode)
```

使能CAN收发器时调用的回调API。

定义位置（Definition）：transceiver.h:42。

符号定位：[can_transceiver_enable_t](../hardware/P050_CAN收发器驱动后端接口.md#gac9de770d729b6427979d83b2904f07cf)。

### `can_transceiver_disable_t`

```c
int(* can_transceiver_disable_t)(const struct device *dev)
```

禁用CAN收发器时调用的回调API。

定义位置（Definition）：transceiver.h:48。

符号定位：[can_transceiver_disable_t](../hardware/P050_CAN收发器驱动后端接口.md#gacc56ddc312a7205bfadb9b612372b89c)。

### `can_transceiver_enable`

```c
static int can_transceiver_enable(const struct device *dev, can_mode_t mode)
```

使能CAN收发器（Enable）。

定义位置（Definition）：transceiver.h:77。

符号定位：[can_transceiver_enable](../hardware/P041_CAN收发器接口参考.md#ga0d0e87150b49198c41e2782a17cfd694)。

### `can_transceiver_disable`

```c
static int can_transceiver_disable(const struct device *dev)
```

禁用CAN收发器（Disable）。

定义位置（Definition）：transceiver.h:96。

符号定位：[can_transceiver_disable](../hardware/P041_CAN收发器接口参考.md#ga7509ca0b6ece81b4038b7d128af961be)。

### `can_transceiver_driver_api`

驱动操作（Driver Operations）：CAN收发器驱动操作；原提示含有格式标签。

定义位置（Definition）：transceiver.h:53。

符号定位：[can_transceiver_driver_api](../hardware/P055_CAN收发器操作结构.md)。

### `can_transceiver_driver_api::disable`

```c
can_transceiver_disable_t disable
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：transceiver.h:57。

符号定位：[can_transceiver_driver_api::disable](../hardware/P055_CAN收发器操作结构.md#ab28e2f8f1bbf96942349e1ae0b352d68)。

### `can_transceiver_driver_api::enable`

```c
can_transceiver_enable_t enable
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：transceiver.h:55。

符号定位：[can_transceiver_driver_api::enable](../hardware/P055_CAN收发器操作结构.md#afbf86ddecfcc818a9c84dd6fd0807505)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

## 4.4\_源码跟踪译注

> 译注——使用层级：官方约定由CAN控制器驱动管理收发器，应用通常调用can_start／can_stop，而不是直接切换收发器。使能／禁用包装直接调用can_transceiver设备类别的操作指针，不额外检查NULL或设备就绪；调用方需要传入正确的关联设备，不能把控制器指针当作收发器指针。

> 译注——GPIO收发器实例：本次核对的通用GPIO实现至少需要enable-gpios或standby-gpios。初始化将使能信号置为逻辑无效、待机信号置为逻辑有效；使能时反过来，GPIO设备树极性决定实际电平。此实现忽略mode参数，不应推广为所有收发器都能提供监听等模式切换能力。运行时GPIO写入失败映射为-EIO。

> 译注——操作不是事务：GPIO实现按顺序写enable再写standby，如果后一项失败，不回滚前一项。收到错误不能假定所有引脚仍处于调用前状态。收发器使能、CAN控制器启动与成功收发帧分别需要各自证据，文档与源码对照没有替代电气连接或总线实测。

> 译注——版本边界：本批核对控制器与收发器头文件、CAN公共实现、系统调用处理、Kconfig、GPIO收发器实现、经典CAN与CAN FD绑定以及CHECKIF定义，共九份官方源码并记录摘要。两份源码页的非注释代码分别与读取的官方头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接CAN总线、发送帧或操作硬件。

头文件相对定位：[include/zephyr/drivers/can/transceiver.h](../../../include/zephyr/drivers/can/transceiver.h)，关联实现／接口：[drivers/can/transceiver/can_transceiver_gpio.c](../../../drivers/can/transceiver/can_transceiver_gpio.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/can/transceiver.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/transceiver/can_transceiver_gpio.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、连接CAN总线、收发帧或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_CAN收发器头文件参考.md)
- [zephyr/drivers/can.h](P001_CAN驱动头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [can_transceiver_enable_t](../hardware/P050_CAN收发器驱动后端接口.md#gac9de770d729b6427979d83b2904f07cf)
- [device](../device_reference/P002_设备对象结构.md)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [can_transceiver_disable_t](../hardware/P050_CAN收发器驱动后端接口.md#gacc56ddc312a7205bfadb9b612372b89c)
- [can_transceiver_driver_api](../hardware/P055_CAN收发器操作结构.md)
- [enable](../hardware/P055_CAN收发器操作结构.md#afbf86ddecfcc818a9c84dd6fd0807505)
- [disable](../hardware/P055_CAN收发器操作结构.md#ab28e2f8f1bbf96942349e1ae0b352d68)
- [can_transceiver_enable](../hardware/P041_CAN收发器接口参考.md#ga0d0e87150b49198c41e2782a17cfd694)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [can_transceiver_disable](../hardware/P041_CAN收发器接口参考.md#ga7509ca0b6ece81b4038b7d128af961be)

---

[上一章](P003_CAN收发器头文件参考.md) · [返回大纲](大纲.md)
