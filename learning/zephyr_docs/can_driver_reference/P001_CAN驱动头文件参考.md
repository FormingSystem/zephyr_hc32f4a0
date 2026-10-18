---
id: learning.zephyr-docs.can-driver-reference.page-1
title: CAN驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2can_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_CAN驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2can_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入CAN控制器与收发器头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

CAN（控制器局域网，Controller Area Network）控制器驱动API的头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <string.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/stats/stats.h>
#include <zephyr/syscalls/can.h>
```

查看此文件的源码。

CAN（控制器局域网，Controller Area Network）控制器驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_can_5Fframe"></a>

```c
struct can_frame
```

相关声明：[can_frame](../hardware/P363_CAN帧结构.md)。

CAN帧（Frame）结构。

<a id="r_can_5Ffilter"></a>

```c
struct can_filter
```

相关声明：[can_filter](../hardware/P364_CAN过滤器结构.md)。

CAN过滤器（Filter）结构。

<a id="r_can_5Fbus_5Ferr_5Fcnt"></a>

```c
struct can_bus_err_cnt
```

相关声明：[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

CAN控制器错误计数器（Error Counters）。

<a id="r_can_5Ftiming"></a>

```c
struct can_timing
```

相关声明：[can_timing](../hardware/P366_CAN时序结构.md)。

CAN总线时序（Bus Timing）结构。

<a id="r_can_5Fstate_5Fchange_5Fcallback"></a>

```c
struct can_state_change_callback
```

相关声明：[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)。

CAN状态变化回调（State Change Callback）。

<a id="r_can_5Fdriver_5Fconfig"></a>

```c
struct can_driver_config
```

相关声明：[can_driver_config](../hardware/P371_CAN驱动公共配置.md)。

CAN控制器驱动的公共配置（Common Configuration）。

<a id="r_can_5Fdriver_5Fdata"></a>

```c
struct can_driver_data
```

相关声明：[can_driver_data](../hardware/P372_CAN驱动公共数据.md)。

CAN控制器驱动的公共数据（Common Data）。

<a id="r_can_5Fdriver_5Fapi"></a>

```c
struct can_driver_api
```

相关声明：[can_driver_api](../hardware/P370_CAN驱动函数表.md)。

驱动操作（Driver Operations）：CAN控制器驱动操作。

<a id="r_can_5Fdevice_5Fstate"></a>

```c
struct can_device_state
```

相关声明：[can_device_state](../hardware/P368_CAN设备状态结构.md)。

CAN专用设备状态，允许加入CAN设备类别专用的扩展内容。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga0186885b4aaea6b77ae115b2faddabbb"></a>

```c
#define CAN_CALC_TDCO(_timing_data, _tdco_min, _tdco_max)
```

相关声明：[CAN_CALC_TDCO](../hardware/P369_CAN控制器后端接口.md#ga0186885b4aaea6b77ae115b2faddabbb)。

根据数据阶段时序参数计算发送器延迟补偿偏移（Transmitter Delay Compensation Offset，TDCO）。

<a id="r_ga86d706ecac2f5a50e6e550e9c0253668"></a>

```c
#define CAN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)
```

相关声明：[CAN_DT_DRIVER_CONFIG_GET](../hardware/P369_CAN控制器后端接口.md#ga86d706ecac2f5a50e6e550e9c0253668)。

can_driver_config结构的静态初始化器（Static Initializer）。

<a id="r_ga1bb18777df7e9fe397f86eea204965dc"></a>

```c
#define CAN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)
```

相关声明：[CAN_DT_DRIVER_CONFIG_INST_GET](../hardware/P369_CAN控制器后端接口.md#ga1bb18777df7e9fe397f86eea204965dc)。

根据DT_DRV_COMPAT实例生成can_driver_config结构的静态初始化器。

<a id="r_gaf6f7efa9d99f44af6f58352f558d7fec"></a>

```c
#define CAN_STATS_BIT_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_BIT_ERROR_INC](../hardware/P362_CAN控制器接口.md#gaf6f7efa9d99f44af6f58352f558d7fec)。

递增CAN设备的位错误（Bit Error）计数器。

<a id="r_ga120a37d5ae5064dcbf116e488f733764"></a>

```c
#define CAN_STATS_BIT0_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_BIT0_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga120a37d5ae5064dcbf116e488f733764)。

递增CAN设备的位0错误（Bit0 Error）计数器。

<a id="r_ga678b74039632302efcb5ef80f0e3a90b"></a>

```c
#define CAN_STATS_BIT1_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_BIT1_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga678b74039632302efcb5ef80f0e3a90b)。

递增CAN设备的位1错误，即隐性位错误（Recessive Bit Error）计数器。

<a id="r_gae4146843944b7ffb1c96636e889282f7"></a>

```c
#define CAN_STATS_STUFF_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_STUFF_ERROR_INC](../hardware/P362_CAN控制器接口.md#gae4146843944b7ffb1c96636e889282f7)。

递增CAN设备的位填充错误（Stuffing Error）计数器。

<a id="r_ga125ce05d40881476f5f156ad5e28c664"></a>

```c
#define CAN_STATS_CRC_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_CRC_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga125ce05d40881476f5f156ad5e28c664)。

递增CAN设备的循环冗余校验错误（Cyclic Redundancy Check Error，CRC Error）计数器。

<a id="r_gac5809b3f5e1a463822e76921cddc9909"></a>

```c
#define CAN_STATS_FORM_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_FORM_ERROR_INC](../hardware/P362_CAN控制器接口.md#gac5809b3f5e1a463822e76921cddc9909)。

递增CAN设备的格式错误（Form Error）计数器。

<a id="r_ga15f7ca18badbbe2fe24be68cacce6171"></a>

```c
#define CAN_STATS_ACK_ERROR_INC(dev_)
```

相关声明：[CAN_STATS_ACK_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga15f7ca18badbbe2fe24be68cacce6171)。

递增CAN设备的应答错误（Acknowledgement Error）计数器。

<a id="r_ga95fe455780b38c7202b48bc6004e6f4d"></a>

```c
#define CAN_STATS_RX_OVERRUN_INC(dev_)
```

相关声明：[CAN_STATS_RX_OVERRUN_INC](../hardware/P362_CAN控制器接口.md#ga95fe455780b38c7202b48bc6004e6f4d)。

递增CAN设备的接收溢出（RX Overrun）计数器。

<a id="r_ga06a9058924901e2d960858fb9e3a4a02"></a>

```c
#define CAN_STATS_RESET(dev_)
```

相关声明：[CAN_STATS_RESET](../hardware/P362_CAN控制器接口.md#ga06a9058924901e2d960858fb9e3a4a02)。

将CAN设备的所有统计值清零。

<a id="r_ga599d0695abe481411660d7af2893f4a5"></a>

```c
#define CAN_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, ...)
```

相关声明：[CAN_DEVICE_DT_DEFINE](../hardware/P362_CAN控制器接口.md#ga599d0695abe481411660d7af2893f4a5)。

类似DEVICE_DT_DEFINE()，并加入CAN设备专用处理。

<a id="r_ga20266dc5e962922144e078b85ccb8351"></a>

```c
#define CAN_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[CAN_DEVICE_DT_INST_DEFINE](../hardware/P362_CAN控制器接口.md#ga20266dc5e962922144e078b85ccb8351)。

用于与DT_DRV_COMPAT匹配的实例，作用类似CAN_DEVICE_DT_DEFINE()。

<a id="define-members-0"></a>

### CAN帧定义（Frame Definitions）

<a id="r_ga4cd8ce34887b90baeeaa6a4aa048b398"></a>

```c
#define CAN_STD_ID_MASK 0x7FFU
```

相关声明：[CAN_STD_ID_MASK](../hardware/P362_CAN控制器接口.md#ga4cd8ce34887b90baeeaa6a4aa048b398)。

标准11位CAN标识符（Standard Identifier）的位掩码。

<a id="r_ga15ee71e8abcf51008925585049125986"></a>

```c
#define CAN_EXT_ID_MASK 0x1FFFFFFFU
```

相关声明：[CAN_EXT_ID_MASK](../hardware/P362_CAN控制器接口.md#ga15ee71e8abcf51008925585049125986)。

扩展29位CAN标识符（Extended Identifier）的位掩码。

<a id="r_gadc209a027ee700faf10461e2417bee50"></a>

```c
#define CAN_MAX_DLC 8U
```

相关声明：[CAN_MAX_DLC](../hardware/P362_CAN控制器接口.md#gadc209a027ee700faf10461e2417bee50)。

CAN 2.0A／2.0B的最大数据长度码（Data Length Code，DLC）。

<a id="r_gad4b7310536c7e3252c2056abe64c0333"></a>

```c
#define CANFD_MAX_DLC 15U
```

相关声明：[CANFD_MAX_DLC](../hardware/P362_CAN控制器接口.md#gad4b7310536c7e3252c2056abe64c0333)。

CAN FD（灵活数据速率CAN，CAN with Flexible Data-Rate）的最大数据长度码。

<a id="define-members-1"></a>

### CAN控制器模式标志（Controller Mode Flags）



<a id="r_ga89cd5ea2e9d70a51bc12b100be28ca3d"></a>

```c
#define CAN_MODE_NORMAL 0
```

相关声明：[CAN_MODE_NORMAL](../hardware/P362_CAN控制器接口.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)。

正常模式（Normal Mode）。

<a id="r_ga891031afc77974a041accb3d0ceb21bb"></a>

```c
#define CAN_MODE_LOOPBACK BIT(0)
```

相关声明：[CAN_MODE_LOOPBACK](../hardware/P362_CAN控制器接口.md#ga891031afc77974a041accb3d0ceb21bb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器处于环回模式（Loopback Mode），会接收自己发送的帧。

<a id="r_ga117d04b9118a1b3f839c557ef6b596cb"></a>

```c
#define CAN_MODE_LISTENONLY BIT(1)
```

相关声明：[CAN_MODE_LISTENONLY](../hardware/P362_CAN控制器接口.md#ga117d04b9118a1b3f839c557ef6b596cb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器不允许发送显性位（Dominant Bits）。

<a id="r_gabb4d99736d8386a5ab62a5e44374d13a"></a>

```c
#define CAN_MODE_FD BIT(2)
```

相关声明：[CAN_MODE_FD](../hardware/P362_CAN控制器接口.md#gabb4d99736d8386a5ab62a5e44374d13a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器允许发送／接收CAN FD帧。

<a id="r_ga033d7ade1966299c7e6249b945f38202"></a>

```c
#define CAN_MODE_ONE_SHOT BIT(3)
```

相关声明：[CAN_MODE_ONE_SHOT](../hardware/P362_CAN控制器接口.md#ga033d7ade1966299c7e6249b945f38202)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

仲裁失败或缺少应答（ACK）时，控制器不进行重传。

<a id="r_gaf0821983174ad781e1bb63a976a18fab"></a>

```c
#define CAN_MODE_3_SAMPLES BIT(4)
```

相关声明：[CAN_MODE_3_SAMPLES](../hardware/P362_CAN控制器接口.md#gaf0821983174ad781e1bb63a976a18fab)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器使用三次采样模式（Triple Sampling Mode）。

<a id="r_ga3d8675253125b2af2bd22f0b2cc60cdd"></a>

```c
#define CAN_MODE_MANUAL_RECOVERY BIT(5)
```

相关声明：[CAN_MODE_MANUAL_RECOVERY](../hardware/P362_CAN控制器接口.md#ga3d8675253125b2af2bd22f0b2cc60cdd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器进入总线关闭状态（Bus-off State）后，需要手动恢复（Manual Recovery）。

<a id="define-members-2"></a>

### CAN帧标志（Frame Flags）



<a id="r_ga9ed5a06a97db2c955a7db4b6e386d5e3"></a>

```c
#define CAN_FRAME_IDE BIT(0)
```

相关声明：[CAN_FRAME_IDE](../hardware/P362_CAN控制器接口.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧使用扩展29位CAN ID。

<a id="r_gaed376ef16b84cd1974255fbb26dc3d7f"></a>

```c
#define CAN_FRAME_RTR BIT(1)
```

相关声明：[CAN_FRAME_RTR](../hardware/P362_CAN控制器接口.md#gaed376ef16b84cd1974255fbb26dc3d7f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧是远程传输请求（Remote Transmission Request，RTR）。

<a id="r_ga22f85e1d16b93e46200f9673abdbb589"></a>

```c
#define CAN_FRAME_FDF BIT(2)
```

相关声明：[CAN_FRAME_FDF](../hardware/P362_CAN控制器接口.md#ga22f85e1d16b93e46200f9673abdbb589)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧使用CAN FD格式（FD Format，FDF）。

<a id="r_ga1fdf15ce4a3b333488f9b630ec836d52"></a>

```c
#define CAN_FRAME_BRS BIT(3)
```

相关声明：[CAN_FRAME_BRS](../hardware/P362_CAN控制器接口.md#ga1fdf15ce4a3b333488f9b630ec836d52)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧使用CAN FD速率切换（Baud Rate Switch，BRS）。

<a id="r_ga83f8b7af6eb45e43aaac355de3e69e52"></a>

```c
#define CAN_FRAME_ESI BIT(4)
```

相关声明：[CAN_FRAME_ESI](../hardware/P362_CAN控制器接口.md#ga83f8b7af6eb45e43aaac355de3e69e52)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

CAN FD错误状态指示（Error State Indicator，ESI）。

<a id="define-members-3"></a>

### CAN过滤器标志（Filter Flags）



<a id="r_gafa40c165d016955ec0c856a7fd53168f"></a>

```c
#define CAN_FILTER_IDE BIT(0)
```

相关声明：[CAN_FILTER_IDE](../hardware/P362_CAN控制器接口.md#gafa40c165d016955ec0c856a7fd53168f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

过滤器匹配使用扩展29位CAN ID的帧。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga0b2a1456e66f4522a30cf1400fdfced7"></a>

```c
typedef uint32_t can_mode_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

提供用于保存CAN控制器配置标志的类型。

<a id="r_gab3675297d3e528bf19e2072f6a84bfca"></a>

```c
typedef void(* can_tx_callback_t) (const struct device *dev, int error, void *user_data)
```

相关声明：[can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)、[device](../device_reference/P002_设备对象结构.md)。

定义应用程序回调处理函数的签名（Callback Handler Signature）。

<a id="r_gaab9525fafab78c0da0a78a2dae39bd6f"></a>

```c
typedef void(* can_rx_callback_t) (const struct device *dev, struct can_frame *frame, void *user_data)
```

相关声明：[can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)、[device](../device_reference/P002_设备对象结构.md)、[can_frame](../hardware/P363_CAN帧结构.md)。

定义接收用应用程序回调处理函数的签名。

<a id="r_ga002ff7ba1f5be374510a902459dd9d3d"></a>

```c
typedef void(* can_state_change_callback_t) (const struct device *dev, enum can_state state, struct can_bus_err_cnt err_cnt, void *user_data)
```

相关声明：[can_state_change_callback_t](../hardware/P362_CAN控制器接口.md#ga002ff7ba1f5be374510a902459dd9d3d)、[device](../device_reference/P002_设备对象结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

定义状态变化回调处理函数的签名。

<a id="r_ga1dc18f69fe06a1d919b13f929100fa85"></a>

```c
typedef void(* can_state_change_callback_handler_t) (const struct device *dev, struct can_state_change_callback *callback, enum can_state state, struct can_bus_err_cnt err_cnt)
```

相关声明：[can_state_change_callback_handler_t](../hardware/P362_CAN控制器接口.md#ga1dc18f69fe06a1d919b13f929100fa85)、[device](../device_reference/P002_设备对象结构.md)、[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

定义状态变化回调处理函数的签名。

<a id="r_ga01a5f028d947582dd4195b467dae8b94"></a>

```c
typedef int(* can_set_timing_t) (const struct device *dev, const struct can_timing *timing)
```

相关声明：[can_set_timing_t](../hardware/P369_CAN控制器后端接口.md#ga01a5f028d947582dd4195b467dae8b94)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

设置CAN总线时序时调用的回调API；参数说明见can_set_timing()。

<a id="r_ga7be2d21503b59cde52369d589ccff80f"></a>

```c
typedef int(* can_set_timing_data_t) (const struct device *dev, const struct can_timing *timing_data)
```

相关声明：[can_set_timing_data_t](../hardware/P369_CAN控制器后端接口.md#ga7be2d21503b59cde52369d589ccff80f)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

设置CAN FD数据阶段总线时序时调用的可选回调API（Optional Callback API）。

<a id="r_ga2fd489217c19977d239d51f0b3fcfc19"></a>

```c
typedef int(* can_get_capabilities_t) (const struct device *dev, can_mode_t *cap)
```

相关声明：[can_get_capabilities_t](../hardware/P369_CAN控制器后端接口.md#ga2fd489217c19977d239d51f0b3fcfc19)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

取得CAN控制器能力（Capabilities）时调用的回调API；参数说明见can_get_capabilities()。

<a id="r_gaecca113e6b8cc7caba3d19fdd104aaa7"></a>

```c
typedef int(* can_start_t) (const struct device *dev)
```

相关声明：[can_start_t](../hardware/P369_CAN控制器后端接口.md#gaecca113e6b8cc7caba3d19fdd104aaa7)、[device](../device_reference/P002_设备对象结构.md)。

启动CAN控制器时调用的回调API；参数说明见can_start()。

<a id="r_ga1ab69e7991b8492e36c4b3f359db1961"></a>

```c
typedef int(* can_stop_t) (const struct device *dev)
```

相关声明：[can_stop_t](../hardware/P369_CAN控制器后端接口.md#ga1ab69e7991b8492e36c4b3f359db1961)、[device](../device_reference/P002_设备对象结构.md)。

停止CAN控制器时调用的回调API；参数说明见can_stop()。

<a id="r_ga231b61f4d1413e0d28dd5a8bc25a89b3"></a>

```c
typedef int(* can_set_mode_t) (const struct device *dev, can_mode_t mode)
```

相关声明：[can_set_mode_t](../hardware/P369_CAN控制器后端接口.md#ga231b61f4d1413e0d28dd5a8bc25a89b3)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

设置CAN控制器模式时调用的回调API；参数说明见can_set_mode()。

<a id="r_ga89108f1d99fa1ba784808f1e99763a58"></a>

```c
typedef int(* can_send_t) (const struct device *dev, const struct can_frame *frame, k_timeout_t timeout, can_tx_callback_t callback, void *user_data)
```

相关声明：[can_send_t](../hardware/P369_CAN控制器后端接口.md#ga89108f1d99fa1ba784808f1e99763a58)、[device](../device_reference/P002_设备对象结构.md)、[can_frame](../hardware/P363_CAN帧结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)。

发送CAN帧时调用的回调API；参数说明见can_send()。

<a id="r_ga3bc249502cb65bf89bce2ca87535ac6b"></a>

```c
typedef int(* can_add_rx_filter_t) (const struct device *dev, can_rx_callback_t callback, void *user_data, const struct can_filter *filter)
```

相关声明：[can_add_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga3bc249502cb65bf89bce2ca87535ac6b)、[device](../device_reference/P002_设备对象结构.md)、[can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

添加接收过滤器（RX Filter）时调用的回调API；参数说明见can_add_rx_filter()。

<a id="r_ga20ee94c5122acb6fd7fe5939a20ba748"></a>

```c
typedef void(* can_remove_rx_filter_t) (const struct device *dev, int filter_id)
```

相关声明：[can_remove_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga20ee94c5122acb6fd7fe5939a20ba748)、[device](../device_reference/P002_设备对象结构.md)。

移除接收过滤器时调用的回调API；参数说明见can_remove_rx_filter()。

<a id="r_ga8bcafa14e23f2ba70e17c1432449d744"></a>

```c
typedef int(* can_recover_t) (const struct device *dev, k_timeout_t timeout)
```

相关声明：[can_recover_t](../hardware/P369_CAN控制器后端接口.md#ga8bcafa14e23f2ba70e17c1432449d744)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

手动将CAN控制器从总线关闭状态恢复时调用的可选回调API；参数说明见can_recover()。

<a id="r_ga14210ea7870ef23072cd61c10043540f"></a>

```c
typedef int(* can_get_state_t) (const struct device *dev, enum can_state *state, struct can_bus_err_cnt *err_cnt)
```

相关声明：[can_get_state_t](../hardware/P369_CAN控制器后端接口.md#ga14210ea7870ef23072cd61c10043540f)、[device](../device_reference/P002_设备对象结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

取得CAN控制器状态时调用的回调API；参数说明见can_get_state()。

<a id="r_ga4d44354cda4cfe0af5262189549d6523"></a>

```c
typedef int(* can_get_core_clock_t) (const struct device *dev, uint32_t *rate)
```

相关声明：[can_get_core_clock_t](../hardware/P369_CAN控制器后端接口.md#ga4d44354cda4cfe0af5262189549d6523)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得CAN核心时钟频率（Core Clock Rate）时调用的回调API；参数说明见can_get_core_clock()。

<a id="r_ga946dd40c12eba40c34afa7572d61456c"></a>

```c
typedef int(* can_get_max_filters_t) (const struct device *dev, bool ide)
```

相关声明：[can_get_max_filters_t](../hardware/P369_CAN控制器后端接口.md#ga946dd40c12eba40c34afa7572d61456c)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

取得可同时使用的CAN接收过滤器最大数量时调用的可选回调API；参数说明见can_get_max_filters()。

<a id="r_ga80424a027933c3bc0d973f37333d2618"></a>

```c
typedef int(* can_state_change_callbacks_enabled_t) (const struct device *dev, bool enabled)
```

相关声明：[can_state_change_callbacks_enabled_t](../hardware/P369_CAN控制器后端接口.md#ga80424a027933c3bc0d973f37333d2618)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

用于通知状态变化回调何时启用的可选回调API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_gac7ec472c26c564dd7067c49f67c8d2f7"></a>

```c
enum can_state { CAN_STATE_ERROR_ACTIVE , CAN_STATE_ERROR_WARNING , CAN_STATE_ERROR_PASSIVE , CAN_STATE_BUS_OFF , CAN_STATE_STOPPED }
```

相关声明：[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[CAN_STATE_ERROR_ACTIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)、[CAN_STATE_ERROR_WARNING](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)、[CAN_STATE_ERROR_PASSIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)、[CAN_STATE_BUS_OFF](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)、[CAN_STATE_STOPPED](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)。

定义CAN控制器的状态（State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gaba24cc4eb2fa759ff8394dd096021982"></a>

```c
void can_fire_state_change_callbacks (const struct device *dev, enum can_state state, struct can_bus_err_cnt err_cnt)
```

相关声明：[can_fire_state_change_callbacks](../hardware/P369_CAN控制器后端接口.md#gaba24cc4eb2fa759ff8394dd096021982)、[device](../device_reference/P002_设备对象结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

触发已注册的CAN状态变化处理回调。

<a id="func-members-0"></a>

### CAN控制器配置（Controller Configuration）

<a id="r_ga4af6d0d9ab72b195909f511ac65cb8fa"></a>

```c
int can_get_core_clock (const struct device *dev, uint32_t *rate)
```

相关声明：[can_get_core_clock](../hardware/P362_CAN控制器接口.md#ga4af6d0d9ab72b195909f511ac65cb8fa)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得CAN核心时钟频率。

<a id="r_ga343456749eec6144a91bacae0d94b114"></a>

```c
uint32_t can_get_bitrate_min (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_get_bitrate_min](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)、[device](../device_reference/P002_设备对象结构.md)。

取得支持的最低比特率（Minimum Bitrate）。

<a id="r_ga1e6dc8026e4d922bce4d398d9f32a457"></a>

```c
uint32_t can_get_bitrate_max (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_get_bitrate_max](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)、[device](../device_reference/P002_设备对象结构.md)。

取得支持的最高比特率（Maximum Bitrate）。

<a id="r_ga5a57627de4764f0bd3b4bafe07f56e6f"></a>

```c
const struct can_timing * can_get_timing_min (const struct device *dev)
```

相关声明：[can_timing](../hardware/P366_CAN时序结构.md)、[can_get_timing_min](../hardware/P362_CAN控制器接口.md#ga5a57627de4764f0bd3b4bafe07f56e6f)、[device](../device_reference/P002_设备对象结构.md)。

取得支持的时序参数最小值。

<a id="r_gabe385d0f003b1e990c78ef7a2a3f9616"></a>

```c
const struct can_timing * can_get_timing_max (const struct device *dev)
```

相关声明：[can_timing](../hardware/P366_CAN时序结构.md)、[can_get_timing_max](../hardware/P362_CAN控制器接口.md#gabe385d0f003b1e990c78ef7a2a3f9616)、[device](../device_reference/P002_设备对象结构.md)。

取得支持的时序参数最大值。

<a id="r_gac27fe64142603f0d32d422594356b2d7"></a>

```c
int can_calc_timing (const struct device *dev, struct can_timing *res, uint32_t bitrate, uint16_t sample_pnt)
```

相关声明：[can_calc_timing](../hardware/P362_CAN控制器接口.md#gac27fe64142603f0d32d422594356b2d7)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

根据比特率和采样点（Sample Point）计算时序参数。

<a id="r_ga6399ef0cefdab3da738136f8a5c59c2f"></a>

```c
const struct can_timing * can_get_timing_data_min (const struct device *dev)
```

相关声明：[can_timing](../hardware/P366_CAN时序结构.md)、[can_get_timing_data_min](../hardware/P362_CAN控制器接口.md#ga6399ef0cefdab3da738136f8a5c59c2f)、[device](../device_reference/P002_设备对象结构.md)。

取得数据阶段（Data Phase）支持的时序参数最小值。

<a id="r_ga47a2f6d6b42121b390aa92160c833b80"></a>

```c
const struct can_timing * can_get_timing_data_max (const struct device *dev)
```

相关声明：[can_timing](../hardware/P366_CAN时序结构.md)、[can_get_timing_data_max](../hardware/P362_CAN控制器接口.md#ga47a2f6d6b42121b390aa92160c833b80)、[device](../device_reference/P002_设备对象结构.md)。

取得数据阶段支持的时序参数最大值。

<a id="r_ga358cd73ed59c2099f4b2c6ceb397ca11"></a>

```c
int can_calc_timing_data (const struct device *dev, struct can_timing *res, uint32_t bitrate, uint16_t sample_pnt)
```

相关声明：[can_calc_timing_data](../hardware/P362_CAN控制器接口.md#ga358cd73ed59c2099f4b2c6ceb397ca11)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

计算数据阶段的时序参数。

<a id="r_ga606cf9fda4c66a0f4abf74e1d357eac2"></a>

```c
int can_set_timing_data (const struct device *dev, const struct can_timing *timing_data)
```

相关声明：[can_set_timing_data](../hardware/P362_CAN控制器接口.md#ga606cf9fda4c66a0f4abf74e1d357eac2)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

配置CAN FD控制器数据阶段的总线时序。

<a id="r_ga0afd2c446fc5e685370641a1678f87b7"></a>

```c
int can_set_bitrate_data (const struct device *dev, uint32_t bitrate_data)
```

相关声明：[can_set_bitrate_data](../hardware/P362_CAN控制器接口.md#ga0afd2c446fc5e685370641a1678f87b7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置CAN FD控制器数据阶段的比特率。

<a id="r_ga1b134af5d6286ea0fee130b6da5217da"></a>

```c
int can_set_timing (const struct device *dev, const struct can_timing *timing)
```

相关声明：[can_set_timing](../hardware/P362_CAN控制器接口.md#ga1b134af5d6286ea0fee130b6da5217da)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

配置CAN控制器的总线时序。

<a id="r_ga4afd7776c5039dec8acb089499dc1168"></a>

```c
int can_get_capabilities (const struct device *dev, can_mode_t *cap)
```

相关声明：[can_get_capabilities](../hardware/P362_CAN控制器接口.md#ga4afd7776c5039dec8acb089499dc1168)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

取得CAN控制器支持的模式。

<a id="r_gae012d26711c2a7ce1419d21c38cae63a"></a>

```c
const struct device * can_get_transceiver (const struct device *dev)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[can_get_transceiver](../hardware/P362_CAN控制器接口.md#gae012d26711c2a7ce1419d21c38cae63a)、[device](../device_reference/P002_设备对象结构.md)。

取得与CAN控制器关联的CAN收发器（Transceiver）。

<a id="r_gae48dfa8bc5b52f233b9b1a08aac2675a"></a>

```c
int can_start (const struct device *dev)
```

相关声明：[can_start](../hardware/P362_CAN控制器接口.md#gae48dfa8bc5b52f233b9b1a08aac2675a)、[device](../device_reference/P002_设备对象结构.md)。

启动CAN控制器。

<a id="r_ga1b0ac9185341cb0bde85ec64e4c490a5"></a>

```c
int can_stop (const struct device *dev)
```

相关声明：[can_stop](../hardware/P362_CAN控制器接口.md#ga1b0ac9185341cb0bde85ec64e4c490a5)、[device](../device_reference/P002_设备对象结构.md)。

停止CAN控制器。

<a id="r_gae04c3c884b3ed26dfea4745b7dff2c5f"></a>

```c
int can_set_mode (const struct device *dev, can_mode_t mode)
```

相关声明：[can_set_mode](../hardware/P362_CAN控制器接口.md#gae04c3c884b3ed26dfea4745b7dff2c5f)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

将CAN控制器设置为指定工作模式（Operation Mode）。

<a id="r_gabd201b5b1fca54048985a8a24dd51e55"></a>

```c
can_mode_t can_get_mode (const struct device *dev)
```

相关声明：[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)、[can_get_mode](../hardware/P362_CAN控制器接口.md#gabd201b5b1fca54048985a8a24dd51e55)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN控制器的工作模式。

<a id="r_ga0685ebfacfb79d33131167ac3aaa6f9b"></a>

```c
int can_set_bitrate (const struct device *dev, uint32_t bitrate)
```

相关声明：[can_set_bitrate](../hardware/P362_CAN控制器接口.md#ga0685ebfacfb79d33131167ac3aaa6f9b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置CAN控制器的比特率。

<a id="func-members-1"></a>

### 发送CAN帧（Transmitting CAN Frames）

<a id="r_ga446ee31913699de3c80be05d837b5fd5"></a>

```c
int can_send (const struct device *dev, const struct can_frame *frame, k_timeout_t timeout, can_tx_callback_t callback, void *user_data)
```

相关声明：[can_send](../hardware/P362_CAN控制器接口.md#ga446ee31913699de3c80be05d837b5fd5)、[device](../device_reference/P002_设备对象结构.md)、[can_frame](../hardware/P363_CAN帧结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)。

将CAN帧加入队列，等待在CAN总线上发送。

<a id="func-members-2"></a>

### CAN总线错误报告与处理（Error Reporting and Handling）

<a id="r_gab98c121578c8349d9dfb41d60f356857"></a>

```c
int can_get_state (const struct device *dev, enum can_state *state, struct can_bus_err_cnt *err_cnt)
```

相关声明：[can_get_state](../hardware/P362_CAN控制器接口.md#gab98c121578c8349d9dfb41d60f356857)、[device](../device_reference/P002_设备对象结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

取得CAN控制器的当前状态。

<a id="r_gac474e56a50685736a1c25dca277aab5e"></a>

```c
int can_recover (const struct device *dev, k_timeout_t timeout)
```

相关声明：[can_recover](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从总线关闭状态恢复。

<a id="r_gacda2bc21fa0cbd7b3406dd096827923c"></a>

```c
void can_set_state_change_callback (const struct device *dev, can_state_change_callback_t callback, void *user_data)
```

相关声明：[can_set_state_change_callback](../hardware/P362_CAN控制器接口.md#gacda2bc21fa0cbd7b3406dd096827923c)、[device](../device_reference/P002_设备对象结构.md)、[can_state_change_callback_t](../hardware/P362_CAN控制器接口.md#ga002ff7ba1f5be374510a902459dd9d3d)。

设置CAN控制器状态变化事件的回调。

<a id="r_gabf813d9f21982f674b213708adee9e96"></a>

```c
static void can_init_state_change_callback (struct can_state_change_callback *callback, can_state_change_callback_handler_t handler)
```

相关声明：[can_init_state_change_callback](../hardware/P362_CAN控制器接口.md#gabf813d9f21982f674b213708adee9e96)、[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)、[can_state_change_callback_handler_t](../hardware/P362_CAN控制器接口.md#ga1dc18f69fe06a1d919b13f929100fa85)。

初始化CAN控制器状态变化回调结构。

<a id="r_gace0dd2797a133bd293d34a9ac5348e2a"></a>

```c
int can_add_state_change_callback (const struct device *dev, struct can_state_change_callback *callback)
```

相关声明：[can_add_state_change_callback](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)、[device](../device_reference/P002_设备对象结构.md)、[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)。

添加CAN控制器状态变化事件的回调。

<a id="r_ga5c1c7633e020aec2936a6ce3ba68b256"></a>

```c
int can_remove_state_change_callback (const struct device *dev, struct can_state_change_callback *callback)
```

相关声明：[can_remove_state_change_callback](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)、[device](../device_reference/P002_设备对象结构.md)、[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)。

移除CAN控制器状态变化事件的回调。

<a id="func-members-3"></a>

### CAN统计（Statistics）

<a id="r_ga27b277f3b5146590f159171f602904db"></a>

```c
uint32_t can_stats_get_bit_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_bit_errors](../hardware/P362_CAN控制器接口.md#ga27b277f3b5146590f159171f602904db)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的位错误计数器值。

<a id="r_ga7c380f6c4a529e5b5e6010ab4e6c7680"></a>

```c
uint32_t can_stats_get_bit0_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_bit0_errors](../hardware/P362_CAN控制器接口.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的位0错误计数器值。

<a id="r_ga4c7d40951a2ae6eaa72e5d1f7a26ac75"></a>

```c
uint32_t can_stats_get_bit1_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_bit1_errors](../hardware/P362_CAN控制器接口.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的位1错误计数器值。

<a id="r_ga162fde4e622fb06dcbbcf2f31bb35d38"></a>

```c
uint32_t can_stats_get_stuff_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_stuff_errors](../hardware/P362_CAN控制器接口.md#ga162fde4e622fb06dcbbcf2f31bb35d38)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的位填充错误计数器值。

<a id="r_ga31692aef7962172532f8200fed7aecd2"></a>

```c
uint32_t can_stats_get_crc_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_crc_errors](../hardware/P362_CAN控制器接口.md#ga31692aef7962172532f8200fed7aecd2)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的CRC错误计数器值。

<a id="r_gabf9ce221f4f6a8dbaafcff9b7a5c5a10"></a>

```c
uint32_t can_stats_get_form_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_form_errors](../hardware/P362_CAN控制器接口.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的格式错误计数器值。

<a id="r_ga4f8414d64b75d4d1ffb7a0feff36f698"></a>

```c
uint32_t can_stats_get_ack_errors (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_ack_errors](../hardware/P362_CAN控制器接口.md#ga4f8414d64b75d4d1ffb7a0feff36f698)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的应答错误计数器值。

<a id="r_ga8664fbaa13f4bb89540493264d2a041d"></a>

```c
uint32_t can_stats_get_rx_overruns (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[can_stats_get_rx_overruns](../hardware/P362_CAN控制器接口.md#ga8664fbaa13f4bb89540493264d2a041d)、[device](../device_reference/P002_设备对象结构.md)。

取得CAN设备的接收溢出计数器值。

<a id="func-members-4"></a>

### CAN辅助函数（Utility Functions）

<a id="r_gaa1d866167c0c23f8d5c0c15385589601"></a>

```c
static uint8_t can_dlc_to_bytes (uint8_t dlc)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[can_dlc_to_bytes](../hardware/P362_CAN控制器接口.md#gaa1d866167c0c23f8d5c0c15385589601)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将数据长度码（DLC）转换为数据字节数。

<a id="r_ga8314716fe2b66d567b3fd377b8ee9dc3"></a>

```c
static uint8_t can_bytes_to_dlc (uint8_t num_bytes)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[can_bytes_to_dlc](../hardware/P362_CAN控制器接口.md#ga8314716fe2b66d567b3fd377b8ee9dc3)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将字节数转换为数据长度码（DLC）。

<a id="r_gaafc54ac799e3a3a098a9f6941d7f2ea8"></a>

```c
static bool can_frame_matches_filter (const struct can_frame *frame, const struct can_filter *filter)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[can_frame_matches_filter](../hardware/P362_CAN控制器接口.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)、[can_frame](../hardware/P363_CAN帧结构.md)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

检查CAN帧是否匹配CAN过滤器。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.6\_接收CAN帧（Receiving CAN Frames）

<a id="r_ga7af0acdfbdad07fc3eba4cbd29bc090b"></a>

```c
#define CAN_MSGQ_DEFINE(name, max_frames)
```

相关声明：[CAN_MSGQ_DEFINE](../hardware/P362_CAN控制器接口.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)。

静态定义并初始化CAN接收消息队列（RX Message Queue）。

<a id="r_gae9dd69a13b960f773ab07bb0bb13b5e9"></a>

```c
int can_add_rx_filter (const struct device *dev, can_rx_callback_t callback, void *user_data, const struct can_filter *filter)
```

相关声明：[can_add_rx_filter](../hardware/P362_CAN控制器接口.md#gae9dd69a13b960f773ab07bb0bb13b5e9)、[device](../device_reference/P002_设备对象结构.md)、[can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

为指定CAN过滤器添加回调函数。

<a id="r_gaaac20a068b7f32d2f38d1601d588b35c"></a>

```c
int can_add_rx_filter_msgq (const struct device *dev, struct k_msgq *msgq, const struct can_filter *filter)
```

相关声明：[can_add_rx_filter_msgq](../hardware/P362_CAN控制器接口.md#gaaac20a068b7f32d2f38d1601d588b35c)、[device](../device_reference/P002_设备对象结构.md)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

为指定过滤器添加消息队列的简易包装函数（Wrapper）。

<a id="r_ga822aa3142ea01582d5cfb8b478fb2847"></a>

```c
void can_remove_rx_filter (const struct device *dev, int filter_id)
```

相关声明：[can_remove_rx_filter](../hardware/P362_CAN控制器接口.md#ga822aa3142ea01582d5cfb8b478fb2847)、[device](../device_reference/P002_设备对象结构.md)。

移除CAN接收过滤器。

<a id="r_ga526c08539094486f07dc52aad8ed0dcc"></a>

```c
int can_get_max_filters (const struct device *dev, bool ide)
```

相关声明：[can_get_max_filters](../hardware/P362_CAN控制器接口.md#ga526c08539094486f07dc52aad8ed0dcc)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

取得接收过滤器的最大数量。

## 1.7\_源码定位与版本边界

相对源码定位：[CAN控制器头文件](../../../include/zephyr/drivers/can.h)、[CAN收发器头文件](../../../include/zephyr/drivers/can/transceiver.h)、[公共实现](../../../drivers/can/can_common.c)、[系统调用处理](../../../drivers/can/can_handlers.c)、[配置选项](../../../drivers/can/Kconfig)、[GPIO收发器实现](../../../drivers/can/transceiver/can_transceiver_gpio.c)、[经典CAN绑定](../../../dts/bindings/can/can-controller.yaml)、[CAN FD绑定](../../../dts/bindings/can/can-fd-controller.yaml)和[可配置错误检查](../../../include/zephyr/sys/check.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：控制器与收发器：CAN控制器（Controller）管理帧、仲裁和位时序，收发器（Transceiver）是单独的关联设备。can_get_transceiver读取公共配置中的phy，可能返回NULL；这不是总线连通性探测。CAN_DT_DRIVER_CONFIG_GET组合控制器／收发器比特率边界，并读取初始比特率与采样点；can_get_mode读取公共运行数据中的mode，不是重新测量总线状态。具体启动、停止和模式设置交给驱动操作。当前数据阶段时序最小／最大值查询直接返回驱动函数表内对应字段的地址，没有单独检查FD能力；不能仅以返回指针非空推断设备支持CAN FD。

> 译注——源码核对：DLC与载荷长度：CAN_MAX_DLC为8，CANFD_MAX_DLC为15；CONFIG_CAN_FD_MODE控制can_frame内载荷数组为8或64字节，不等于每帧都采用FD格式。can_dlc_to_bytes把DLC 9至15映射为12、16、20、24、32、48、64字节，大于15的输入被钳位到末项。can_bytes_to_dlc向上选择可容纳长度的编码，大于48的输入均返回15；两者都不是帧合法性检查。回传统计中的dlc“指示字节长度”不应理解为dlc字段恒等于字节数。

> 译注——源码核对：过滤匹配范围：can_frame_matches_filter先要求标准／扩展标识符类型相同，再计算(frame.id XOR filter.id) AND filter.mask；结果为0才匹配。掩码位为0表示不比较该位；此辅助函数不检查RTR、FDF、BRS或ESI，也不表示安装过滤器后的硬件资源一定可用。CAN_MODE_*、CAN_FRAME_*与CAN_FILTER_*属于不同对象，数值位相同不能互换语义。

> 译注——源码核对：发送等待边界：can_send的timeout用于等待空闲发送邮箱（TX Mailbox）。callback为空时，公共实现安装内部完成回调；驱动接受发送后以K_FOREVER等待信号量，再返回完成状态，因此该timeout不是整个同步发送的截止时间。提供回调时，公共包装把回调和用户数据转交驱动。用户态系统调用复制帧结构并要求callback为NULL，不能据此认为用户态可以安装同样的发送完成回调。

> 译注——源码核对：接收消息队列：can_add_rx_filter_msgq要求消息大小等于sizeof(struct can_frame)，回调以K_NO_WAIT复制整帧到队列。队列满时记录溢出错误，不能承诺保留该帧或自动等待空间。CAN_MSGQ_DEFINE负责静态创建匹配元素类型的队列；队列容量、过滤器数量和硬件接收容量是不同限制。消息队列包装直接调用驱动add_rx_filter，并未复用普通can_add_rx_filter入口的全部参数检查。

> 译注——源码核对：参数检查的配置：公共发送与普通过滤器安装中的若干校验使用CHECKIF。默认运行时检查展开为条件判断并可返回-EINVAL；CONFIG_ASSERT_ON_ERRORS改为断言且不执行所包围的错误处理块；CONFIG_NO_RUNTIME_CHECKS在编译时省略检查。因此这些参数约束始终应由调用者满足，不能假定任意构建都会返回相同的错误码。系统调用的对象与内存访问校验是另一层边界。

> 译注——源码核对：时序计算：sample_pnt以千分比表示，875对应87.5%；值0根据比特率选择默认采样点：大于800 kbit/s用750，大于500 kbit/s用800，其余用875。计算器寻找核心时钟可整除的预分频与时间量子组合；成功可能返回正的采样点误差，不应把所有非零值当失败。当前经典／仲裁阶段计算上限为1 Mbit/s，数据阶段为8 Mbit/s，这些上限不代表某个驱动或收发器一定支持。失败后不要使用输出时序。

> 译注——源码核对：应用时序与补偿：can_set_bitrate及数据阶段版本还检查控制器／收发器的最低与最高比特率，计算误差超过CONFIG_CAN_SAMPLE_POINT_MARGIN时返回-ERANGE。can_set_timing检查各字段上下限，并要求sjw不大于phase_seg1和phase_seg2，再委托驱动。CAN_CALC_TDCO按(1 + prop_seg + phase_seg1)乘prescaler计算并钳位到传入边界；宏本身不验证完整时序是否适用。计算、写入时序与启动总线分别是不同动作。

> 译注——源码核对：状态回调与锁：新接口用can_state_change_callback节点维护回调列表，init仅设置handler，add才加入列表。当前触发函数持有state_change_callback_lock自旋锁时依次调用handler；处理函数不能阻塞，也不能重入需要取得同一锁的增删操作。添加已有节点会先移除再追加；首次启用通知或最后禁用通知的驱动钩子即使返回错误，已经执行的链表修改也不会回滚。旧式单回调接口通过内部节点适配，且忽略增删接口的返回值。

> 译注——源码核对：状态与统计：原状态提示使用RX／TX错误计数阈值作简写，这里保留其文字；实际状态由驱动get_state或状态事件报告，can_bus_err_cnt的两个字段仅为uint8_t，不能靠它们表达256并自行替代总线关闭判断。CAN_STATS_*维护独立的32位软件统计，不是这两个硬件错误计数器；bit0／bit1递增宏同时增加总bit_error，未启用统计时递增与清零宏为空。手动恢复还受CONFIG_CAN_MANUAL_RECOVERY_MODE和驱动recover操作支持情况约束。

> 译注——源码核对：版本边界：本批核对控制器与收发器头文件、CAN公共实现、系统调用处理、Kconfig、GPIO收发器实现、经典CAN与CAN FD绑定以及CHECKIF定义，共九份官方源码并记录摘要。两份源码页的非注释代码分别与读取的官方头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接CAN总线、发送帧或操作硬件。

本次验证范围为文档与源码对照，未构建固件、连接CAN总线或操作硬件。

## 1.8\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html)
- [查看此文件的源码](P002_CAN驱动头文件源码.md)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)
- [can_timing](../hardware/P366_CAN时序结构.md)
- [can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)
- [can_driver_config](../hardware/P371_CAN驱动公共配置.md)
- [can_driver_data](../hardware/P372_CAN驱动公共数据.md)
- [can_driver_api](../hardware/P370_CAN驱动函数表.md)
- [can_device_state](../hardware/P368_CAN设备状态结构.md)
- [CAN_CALC_TDCO](../hardware/P369_CAN控制器后端接口.md#ga0186885b4aaea6b77ae115b2faddabbb)
- [CAN_DT_DRIVER_CONFIG_GET](../hardware/P369_CAN控制器后端接口.md#ga86d706ecac2f5a50e6e550e9c0253668)
- [CAN_DT_DRIVER_CONFIG_INST_GET](../hardware/P369_CAN控制器后端接口.md#ga1bb18777df7e9fe397f86eea204965dc)
- [CAN_STATS_BIT_ERROR_INC](../hardware/P362_CAN控制器接口.md#gaf6f7efa9d99f44af6f58352f558d7fec)
- [CAN_STATS_BIT0_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga120a37d5ae5064dcbf116e488f733764)
- [CAN_STATS_BIT1_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga678b74039632302efcb5ef80f0e3a90b)
- [CAN_STATS_STUFF_ERROR_INC](../hardware/P362_CAN控制器接口.md#gae4146843944b7ffb1c96636e889282f7)
- [CAN_STATS_CRC_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga125ce05d40881476f5f156ad5e28c664)
- [CAN_STATS_FORM_ERROR_INC](../hardware/P362_CAN控制器接口.md#gac5809b3f5e1a463822e76921cddc9909)
- [CAN_STATS_ACK_ERROR_INC](../hardware/P362_CAN控制器接口.md#ga15f7ca18badbbe2fe24be68cacce6171)
- [CAN_STATS_RX_OVERRUN_INC](../hardware/P362_CAN控制器接口.md#ga95fe455780b38c7202b48bc6004e6f4d)
- [CAN_STATS_RESET](../hardware/P362_CAN控制器接口.md#ga06a9058924901e2d960858fb9e3a4a02)
- [CAN_DEVICE_DT_DEFINE](../hardware/P362_CAN控制器接口.md#ga599d0695abe481411660d7af2893f4a5)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [CAN_DEVICE_DT_INST_DEFINE](../hardware/P362_CAN控制器接口.md#ga20266dc5e962922144e078b85ccb8351)
- [CAN_STD_ID_MASK](../hardware/P362_CAN控制器接口.md#ga4cd8ce34887b90baeeaa6a4aa048b398)
- [CAN_EXT_ID_MASK](../hardware/P362_CAN控制器接口.md#ga15ee71e8abcf51008925585049125986)
- [CAN_MAX_DLC](../hardware/P362_CAN控制器接口.md#gadc209a027ee700faf10461e2417bee50)
- [CANFD_MAX_DLC](../hardware/P362_CAN控制器接口.md#gad4b7310536c7e3252c2056abe64c0333)
- [CAN_MODE_NORMAL](../hardware/P362_CAN控制器接口.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)
- [CAN_MODE_LOOPBACK](../hardware/P362_CAN控制器接口.md#ga891031afc77974a041accb3d0ceb21bb)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CAN_MODE_LISTENONLY](../hardware/P362_CAN控制器接口.md#ga117d04b9118a1b3f839c557ef6b596cb)
- [CAN_MODE_FD](../hardware/P362_CAN控制器接口.md#gabb4d99736d8386a5ab62a5e44374d13a)
- [CAN_MODE_ONE_SHOT](../hardware/P362_CAN控制器接口.md#ga033d7ade1966299c7e6249b945f38202)
- [CAN_MODE_3_SAMPLES](../hardware/P362_CAN控制器接口.md#gaf0821983174ad781e1bb63a976a18fab)
- [CAN_MODE_MANUAL_RECOVERY](../hardware/P362_CAN控制器接口.md#ga3d8675253125b2af2bd22f0b2cc60cdd)
- [CAN_FRAME_IDE](../hardware/P362_CAN控制器接口.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)
- [CAN_FRAME_RTR](../hardware/P362_CAN控制器接口.md#gaed376ef16b84cd1974255fbb26dc3d7f)
- [CAN_FRAME_FDF](../hardware/P362_CAN控制器接口.md#ga22f85e1d16b93e46200f9673abdbb589)
- [CAN_FRAME_BRS](../hardware/P362_CAN控制器接口.md#ga1fdf15ce4a3b333488f9b630ec836d52)
- [CAN_FRAME_ESI](../hardware/P362_CAN控制器接口.md#ga83f8b7af6eb45e43aaac355de3e69e52)
- [CAN_FILTER_IDE](../hardware/P362_CAN控制器接口.md#gafa40c165d016955ec0c856a7fd53168f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)
- [device](../device_reference/P002_设备对象结构.md)
- [can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)
- [can_state_change_callback_t](../hardware/P362_CAN控制器接口.md#ga002ff7ba1f5be374510a902459dd9d3d)
- [can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [can_state_change_callback_handler_t](../hardware/P362_CAN控制器接口.md#ga1dc18f69fe06a1d919b13f929100fa85)
- [can_set_timing_t](../hardware/P369_CAN控制器后端接口.md#ga01a5f028d947582dd4195b467dae8b94)
- [can_set_timing()](../hardware/P362_CAN控制器接口.md#ga1b134af5d6286ea0fee130b6da5217da)
- [can_set_timing_data_t](../hardware/P369_CAN控制器后端接口.md#ga7be2d21503b59cde52369d589ccff80f)
- [can_get_capabilities_t](../hardware/P369_CAN控制器后端接口.md#ga2fd489217c19977d239d51f0b3fcfc19)
- [can_get_capabilities()](../hardware/P362_CAN控制器接口.md#ga4afd7776c5039dec8acb089499dc1168)
- [can_start_t](../hardware/P369_CAN控制器后端接口.md#gaecca113e6b8cc7caba3d19fdd104aaa7)
- [can_start()](../hardware/P362_CAN控制器接口.md#gae48dfa8bc5b52f233b9b1a08aac2675a)
- [can_stop_t](../hardware/P369_CAN控制器后端接口.md#ga1ab69e7991b8492e36c4b3f359db1961)
- [can_stop()](../hardware/P362_CAN控制器接口.md#ga1b0ac9185341cb0bde85ec64e4c490a5)
- [can_set_mode_t](../hardware/P369_CAN控制器后端接口.md#ga231b61f4d1413e0d28dd5a8bc25a89b3)
- [can_set_mode()](../hardware/P362_CAN控制器接口.md#gae04c3c884b3ed26dfea4745b7dff2c5f)
- [can_send_t](../hardware/P369_CAN控制器后端接口.md#ga89108f1d99fa1ba784808f1e99763a58)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [can_send()](../hardware/P362_CAN控制器接口.md#ga446ee31913699de3c80be05d837b5fd5)
- [can_add_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga3bc249502cb65bf89bce2ca87535ac6b)
- [can_add_rx_filter()](../hardware/P362_CAN控制器接口.md#gae9dd69a13b960f773ab07bb0bb13b5e9)
- [can_remove_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga20ee94c5122acb6fd7fe5939a20ba748)
- [can_remove_rx_filter()](../hardware/P362_CAN控制器接口.md#ga822aa3142ea01582d5cfb8b478fb2847)
- [can_recover_t](../hardware/P369_CAN控制器后端接口.md#ga8bcafa14e23f2ba70e17c1432449d744)
- [can_recover()](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e)
- [can_get_state_t](../hardware/P369_CAN控制器后端接口.md#ga14210ea7870ef23072cd61c10043540f)
- [can_get_state()](../hardware/P362_CAN控制器接口.md#gab98c121578c8349d9dfb41d60f356857)
- [can_get_core_clock_t](../hardware/P369_CAN控制器后端接口.md#ga4d44354cda4cfe0af5262189549d6523)
- [can_get_core_clock()](../hardware/P362_CAN控制器接口.md#ga4af6d0d9ab72b195909f511ac65cb8fa)
- [can_get_max_filters_t](../hardware/P369_CAN控制器后端接口.md#ga946dd40c12eba40c34afa7572d61456c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [can_get_max_filters()](../hardware/P362_CAN控制器接口.md#ga526c08539094486f07dc52aad8ed0dcc)
- [can_state_change_callbacks_enabled_t](../hardware/P369_CAN控制器后端接口.md#ga80424a027933c3bc0d973f37333d2618)
- [CAN_STATE_ERROR_ACTIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)
- [CAN_STATE_ERROR_WARNING](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)
- [CAN_STATE_ERROR_PASSIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)
- [CAN_STATE_BUS_OFF](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)
- [CAN_STATE_STOPPED](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)
- [can_fire_state_change_callbacks](../hardware/P369_CAN控制器后端接口.md#gaba24cc4eb2fa759ff8394dd096021982)
- [can_get_bitrate_min](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)
- [can_get_bitrate_max](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)
- [can_get_timing_min](../hardware/P362_CAN控制器接口.md#ga5a57627de4764f0bd3b4bafe07f56e6f)
- [can_get_timing_max](../hardware/P362_CAN控制器接口.md#gabe385d0f003b1e990c78ef7a2a3f9616)
- [can_calc_timing](../hardware/P362_CAN控制器接口.md#gac27fe64142603f0d32d422594356b2d7)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [can_get_timing_data_min](../hardware/P362_CAN控制器接口.md#ga6399ef0cefdab3da738136f8a5c59c2f)
- [can_get_timing_data_max](../hardware/P362_CAN控制器接口.md#ga47a2f6d6b42121b390aa92160c833b80)
- [can_calc_timing_data](../hardware/P362_CAN控制器接口.md#ga358cd73ed59c2099f4b2c6ceb397ca11)
- [can_set_timing_data](../hardware/P362_CAN控制器接口.md#ga606cf9fda4c66a0f4abf74e1d357eac2)
- [can_set_bitrate_data](../hardware/P362_CAN控制器接口.md#ga0afd2c446fc5e685370641a1678f87b7)
- [can_get_transceiver](../hardware/P362_CAN控制器接口.md#gae012d26711c2a7ce1419d21c38cae63a)
- [can_get_mode](../hardware/P362_CAN控制器接口.md#gabd201b5b1fca54048985a8a24dd51e55)
- [can_set_bitrate](../hardware/P362_CAN控制器接口.md#ga0685ebfacfb79d33131167ac3aaa6f9b)
- [can_set_state_change_callback](../hardware/P362_CAN控制器接口.md#gacda2bc21fa0cbd7b3406dd096827923c)
- [can_init_state_change_callback](../hardware/P362_CAN控制器接口.md#gabf813d9f21982f674b213708adee9e96)
- [can_add_state_change_callback](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)
- [can_remove_state_change_callback](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)
- [can_stats_get_bit_errors](../hardware/P362_CAN控制器接口.md#ga27b277f3b5146590f159171f602904db)
- [can_stats_get_bit0_errors](../hardware/P362_CAN控制器接口.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)
- [can_stats_get_bit1_errors](../hardware/P362_CAN控制器接口.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)
- [can_stats_get_stuff_errors](../hardware/P362_CAN控制器接口.md#ga162fde4e622fb06dcbbcf2f31bb35d38)
- [can_stats_get_crc_errors](../hardware/P362_CAN控制器接口.md#ga31692aef7962172532f8200fed7aecd2)
- [can_stats_get_form_errors](../hardware/P362_CAN控制器接口.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)
- [can_stats_get_ack_errors](../hardware/P362_CAN控制器接口.md#ga4f8414d64b75d4d1ffb7a0feff36f698)
- [can_stats_get_rx_overruns](../hardware/P362_CAN控制器接口.md#ga8664fbaa13f4bb89540493264d2a041d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [can_dlc_to_bytes](../hardware/P362_CAN控制器接口.md#gaa1d866167c0c23f8d5c0c15385589601)
- [can_bytes_to_dlc](../hardware/P362_CAN控制器接口.md#ga8314716fe2b66d567b3fd377b8ee9dc3)
- [can_frame_matches_filter](../hardware/P362_CAN控制器接口.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)
- [CAN_MSGQ_DEFINE](../hardware/P362_CAN控制器接口.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)
- [can_add_rx_filter_msgq](../hardware/P362_CAN控制器接口.md#gaaac20a068b7f32d2f38d1601d588b35c)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)

<a id="CAN_MODE_FLAGS"></a>
<a id="CAN_FRAME_FLAGS"></a>
<a id="CAN_FILTER_FLAGS"></a>
<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_CAN驱动头文件源码.md)
