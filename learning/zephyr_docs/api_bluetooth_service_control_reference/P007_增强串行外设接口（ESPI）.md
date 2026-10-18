---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-7
title: 增强串行外设接口（ESPI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_增强串行外设接口（ESPI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

增强串行外设接口（Enhanced Serial Peripheral Interface，eSPI）目标硬件接口。

<a id="details"></a>

增强串行外设接口（Enhanced Serial Peripheral Interface，eSPI）目标端硬件的接口。自 2.0 起提供；接口版本为 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_espi_5Finterface_5Fbackend"></a>

相关声明：[eSPI 驱动后端 API（Driver Backend API）](../api_transport_control_topic_reference/P006_eSPI 驱动后端 API（Driver Backend API）.md)。

<a id="r_espi_5Femul_5Finterface"></a>

相关声明：[eSPI 仿真接口（Emulation Interface）](../hardware/P486_eSPI总线仿真接口.md)。

eSPI 仿真接口（Emulation Interface）

<a id="r_espi_5Fsaf_5Finterface"></a>

相关声明：[eSPI SAF](../api_radio_permission_topic_reference/P010_eSPI SAF API主题.md)。

eSPI SAF 控制器接口；原文此处将 SAF 展开为串行附接 Flash（Serial Attached Flash）。

<a id="header-files"></a>
<a id="files"></a>

## 7.2\_文件（Files）

<a id="r_espi_2Eh"></a>

```c
file espi.h
```

相关声明：[espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)。

增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）驱动API的主头文件。

<a id="r_espi_5Frealtek_5Frts5912_2Eh"></a>

```c
file espi_realtek_rts5912.h
```

相关声明：[espi_realtek_rts5912.h](../api_file_reference/P108_zephyr__drivers__espi__espi_realtek_rts5912.h_文件参考.md)。

Realtek RTS5912 eSPI驱动的特殊操作（Special Operations）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.3\_数据结构（Data Structures）

<a id="r_espi_5Fevt_5Fdata_5Fkbc"></a>

```c
struct espi_evt_data_kbc
```

相关声明：[espi_evt_data_kbc](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md)。

键盘控制器（KBC）事件的数据格式。

<a id="r_espi_5Fevt_5Fdata_5Facpi"></a>

```c
struct espi_evt_data_acpi
```

相关声明：[espi_evt_data_acpi](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md)。

高级配置与电源接口（ACPI）事件的数据格式。

<a id="r_espi_5Fevt_5Fdata_5Fpvt"></a>

```c
struct espi_evt_data_pvt
```

相关声明：[espi_evt_data_pvt](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md)。

私有通道（Private Channel，PVT）事件的数据格式。

<a id="r_espi_5Fevent"></a>

```c
struct espi_event
```

相关声明：[espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)。

增强型串行外设接口（eSPI）事件。

<a id="r_espi_5Fcfg"></a>

```c
struct espi_cfg
```

相关声明：[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

增强型串行外设接口（eSPI）的总线配置参数。

<a id="r_espi_5Frequest_5Fpacket"></a>

```c
struct espi_request_packet
```

相关声明：[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

eSPI外设请求（Peripheral Request）数据包。

<a id="r_espi_5Foob_5Fpacket"></a>

```c
struct espi_oob_packet
```

相关声明：[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

eSPI带外事务（Out-of-Band Transaction）的数据包格式。

<a id="r_espi_5Fflash_5Fpacket"></a>

```c
struct espi_flash_packet
```

相关声明：[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

eSPI闪存事务（Flash Transaction）的数据包格式。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.4\_宏定义（Macros）

<a id="r_ga8da8ac3b45044323fdb24f1361adaac7"></a>

```c
#define ESPI_INT_ALL_MASK
```

相关声明：[ESPI_INT_ALL_MASK](#ga8da8ac3b45044323fdb24f1361adaac7)。

选择所有 eSPI 通用中断。

<a id="r_gadeb45b8838f4d1fbf05095c36ca3faba"></a>

```c
#define ESPI_INT_BUS_ONLY_MASK
```

相关声明：[ESPI_INT_BUS_ONLY_MASK](#gadeb45b8838f4d1fbf05095c36ca3faba)。

仅选择 eSPI 总线硬件中断。

<a id="r_ga24b468de0013cd9cf9d814faff13b94e"></a>

```c
#define ESPI_INT_NONE_MASK 0U
```

相关声明：[ESPI_INT_NONE_MASK](#ga24b468de0013cd9cf9d814faff13b94e)。

禁用所有 eSPI 硬件事件。

<a id="r_gaa0807c908666cdcbb3a85f310bfbfccc"></a>

```c
#define HOST_KBC_EVT_IBF BIT(0)
```

相关声明：[HOST_KBC_EVT_IBF](#gaa0807c908666cdcbb3a85f310bfbfccc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

KBC 8042 事件：输入缓冲区满（Input Buffer Full）。

<a id="r_ga807bb75027f24e040cd28eba4bc1002c"></a>

```c
#define HOST_KBC_EVT_OBE BIT(1)
```

相关声明：[HOST_KBC_EVT_OBE](#ga807bb75027f24e040cd28eba4bc1002c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

KBC 8042 事件：输出缓冲区空（Output Buffer Empty）。

<a id="r_gaa45ee9beafbda94f8f9ad799e78089cd"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA 0
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA](#gaa45ee9beafbda94f8f9ad799e78089cd)。

ACPI 事件：输入缓冲区满。

<a id="r_ga01e61256f8be5e24d131c68d81ed8916"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD 1U
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD](#ga01e61256f8be5e24d131c68d81ed8916)。

ACPI 事件：输入缓冲区满。

<a id="r_ga6807d29b11134b76b14c8887053cbce1"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST 2U
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST](#ga6807d29b11134b76b14c8887053cbce1)。

ACPI 事件：输出缓冲区空。主机已读取嵌入式控制器（EC）写入 EC-to-Host 寄存器的数据。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.5\_类型定义（Typedefs）

<a id="r_ga9d848c7e367cf277230f365f73c15c46"></a>

```c
typedef void(* espi_callback_handler_t) (const struct device *dev, struct espi_callback *cb, struct espi_event espi_evt)
```

相关声明：[espi_callback_handler_t](#ga9d848c7e367cf277230f365f73c15c46)、[device](../device_reference/P002_设备对象结构.md)、[espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.6\_枚举（Enumerations）

<a id="r_ga0d7c61f1f4ec611d0c8a67ba73e2b4f0"></a>

```c
enum espi_io_mode { ESPI_IO_MODE_SINGLE_LINE = BIT(0) , ESPI_IO_MODE_DUAL_LINES = BIT(1) , ESPI_IO_MODE_QUAD_LINES = BIT(2) }
```

相关声明：[espi_io_mode](#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)、[ESPI_IO_MODE_SINGLE_LINE](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c)、[ESPI_IO_MODE_DUAL_LINES](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243)、[ESPI_IO_MODE_QUAD_LINES](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc)。

eSPI I/O 模式能力（Capabilities）。

<a id="r_gafaa3f7d54503c901ab23bd79a7f8a755"></a>

```c
enum espi_channel { ESPI_CHANNEL_PERIPHERAL = BIT(0) , ESPI_CHANNEL_VWIRE = BIT(1) , ESPI_CHANNEL_OOB = BIT(2) , ESPI_CHANNEL_FLASH = BIT(3) }
```

相关声明：[espi_channel](#gafaa3f7d54503c901ab23bd79a7f8a755)、[ESPI_CHANNEL_PERIPHERAL](#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206)、[ESPI_CHANNEL_VWIRE](#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6)、[ESPI_CHANNEL_OOB](#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54)、[ESPI_CHANNEL_FLASH](#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518)。

eSPI 通道（Channel）。

<a id="r_ga36ac3fbf9813f78bad90f047e1eb1128"></a>

```c
enum espi_bus_event { ESPI_BUS_RESET = BIT(0) , ESPI_BUS_EVENT_CHANNEL_READY = BIT(1) , ESPI_BUS_EVENT_VWIRE_RECEIVED = BIT(2) , ESPI_BUS_EVENT_OOB_RECEIVED = BIT(3) , ESPI_BUS_PERIPHERAL_NOTIFICATION = BIT(4) , ESPI_BUS_TAF_NOTIFICATION = BIT(5) }
```

相关声明：[espi_bus_event](#ga36ac3fbf9813f78bad90f047e1eb1128)、[ESPI_BUS_RESET](#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956)、[ESPI_BUS_EVENT_CHANNEL_READY](#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973)、[ESPI_BUS_EVENT_VWIRE_RECEIVED](#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2)、[ESPI_BUS_EVENT_OOB_RECEIVED](#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203)、[ESPI_BUS_PERIPHERAL_NOTIFICATION](#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea)、[ESPI_BUS_TAF_NOTIFICATION](#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014)。

eSPI 总线事件。

<a id="r_gac55098842dd9d181144ac4b4122a610e"></a>

```c
enum espi_pc_event { ESPI_PC_EVT_BUS_CHANNEL_READY = BIT(0) , ESPI_PC_EVT_BUS_MASTER_ENABLE = BIT(1) }
```

相关声明：[espi_pc_event](#gac55098842dd9d181144ac4b4122a610e)、[ESPI_PC_EVT_BUS_CHANNEL_READY](#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687)、[ESPI_PC_EVT_BUS_MASTER_ENABLE](#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1)。

eSPI 外设通道事件（Peripheral channel events）。

<a id="r_ga2629a5518a94f031419eeccd05f07373"></a>

```c
enum espi_virtual_peripheral { ESPI_PERIPHERAL_UART , ESPI_PERIPHERAL_8042_KBC , ESPI_PERIPHERAL_HOST_IO , ESPI_PERIPHERAL_DEBUG_PORT80 , ESPI_PERIPHERAL_HOST_IO_PVT , ESPI_PERIPHERAL_HOST_IO_PVT2 , ESPI_PERIPHERAL_HOST_IO_PVT3 , ESPI_PERIPHERAL_EC_HOST_CMD }
```

相关声明：[espi_virtual_peripheral](#ga2629a5518a94f031419eeccd05f07373)、[ESPI_PERIPHERAL_UART](#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867)、[ESPI_PERIPHERAL_8042_KBC](#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30)、[ESPI_PERIPHERAL_HOST_IO](#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8)、[ESPI_PERIPHERAL_DEBUG_PORT80](#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0)、[ESPI_PERIPHERAL_HOST_IO_PVT](#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)、[ESPI_PERIPHERAL_HOST_IO_PVT2](#gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231)、[ESPI_PERIPHERAL_HOST_IO_PVT3](#gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce)、[ESPI_PERIPHERAL_EC_HOST_CMD](#gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad)。

eSPI 外设通知类型（Notification type）。

<a id="r_ga4e35c754c720f262805689a94985272c"></a>

```c
enum espi_interrupt_flags { ESPI_BUS_EVENTS = BIT(0) , ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS = BIT(1) , ESPI_OOB_CHANNEL_EVENTS = BIT(2) , ESPI_FLASH_CHANNEL_EVENTS = BIT(3) , ESPI_PERIPHERAL_UART_EVENTS = BIT(4) , ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS = BIT(5) , ESPI_PERIPHERAL_8042_KBC_EVENTS = BIT(6) , ESPI_PERIPHERAL_HOST_IO_EVENTS = BIT(7) , ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS = BIT(8) }
```

相关声明：[espi_interrupt_flags](#ga4e35c754c720f262805689a94985272c)、[ESPI_BUS_EVENTS](#gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5)、[ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS](#gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee)、[ESPI_OOB_CHANNEL_EVENTS](#gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac)、[ESPI_FLASH_CHANNEL_EVENTS](#gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592)、[ESPI_PERIPHERAL_UART_EVENTS](#gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b)、[ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS](#gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800)、[ESPI_PERIPHERAL_8042_KBC_EVENTS](#gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b)、[ESPI_PERIPHERAL_HOST_IO_EVENTS](#gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3)、[ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS](#gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd)。

eSPI 中断标志。

<a id="r_ga3e52615f244d7fa8ccda495ab8ec8a5b"></a>

```c
enum espi_cycle_type { ESPI_CYCLE_MEMORY_READ32 , ESPI_CYCLE_MEMORY_READ64 , ESPI_CYCLE_MEMORY_WRITE32 , ESPI_CYCLE_MEMORY_WRITE64 , ESPI_CYCLE_MESSAGE_NODATA , ESPI_CYCLE_MESSAGE_DATA , ESPI_CYCLE_OK_COMPLETION_NODATA , ESPI_CYCLE_OKCOMPLETION_DATA , ESPI_CYCLE_NOK_COMPLETION_NODATA }
```

相关声明：[espi_cycle_type](#ga3e52615f244d7fa8ccda495ab8ec8a5b)、[ESPI_CYCLE_MEMORY_READ32](#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5)、[ESPI_CYCLE_MEMORY_READ64](#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79)、[ESPI_CYCLE_MEMORY_WRITE32](#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073)、[ESPI_CYCLE_MEMORY_WRITE64](#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7)、[ESPI_CYCLE_MESSAGE_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82)、[ESPI_CYCLE_MESSAGE_DATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f)、[ESPI_CYCLE_OK_COMPLETION_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f)、[ESPI_CYCLE_OKCOMPLETION_DATA](#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f)、[ESPI_CYCLE_NOK_COMPLETION_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)。

eSPI 外设通道支持的 eSPI 周期类型（Cycle types）。

<a id="r_gab65a0951a8912d9de398cfec0aef7d35"></a>

```c
enum espi_vwire_signal { ESPI_VWIRE_SIGNAL_SLP_S3 , ESPI_VWIRE_SIGNAL_SLP_S4 , ESPI_VWIRE_SIGNAL_SLP_S5 , ESPI_VWIRE_SIGNAL_OOB_RST_WARN , ESPI_VWIRE_SIGNAL_PLTRST , ESPI_VWIRE_SIGNAL_SUS_STAT , ESPI_VWIRE_SIGNAL_NMIOUT , ESPI_VWIRE_SIGNAL_SMIOUT , ESPI_VWIRE_SIGNAL_HOST_RST_WARN , ESPI_VWIRE_SIGNAL_SLP_A , ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK , ESPI_VWIRE_SIGNAL_SUS_WARN , ESPI_VWIRE_SIGNAL_SLP_WLAN , ESPI_VWIRE_SIGNAL_SLP_LAN , ESPI_VWIRE_SIGNAL_HOST_C10 , ESPI_VWIRE_SIGNAL_DNX_WARN , ESPI_VWIRE_SIGNAL_PME , ESPI_VWIRE_SIGNAL_WAKE , ESPI_VWIRE_SIGNAL_OOB_RST_ACK , ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS , ESPI_VWIRE_SIGNAL_ERR_NON_FATAL , ESPI_VWIRE_SIGNAL_ERR_FATAL , ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE , ESPI_VWIRE_SIGNAL_HOST_RST_ACK , ESPI_VWIRE_SIGNAL_RST_CPU_INIT , ESPI_VWIRE_SIGNAL_SMI , ESPI_VWIRE_SIGNAL_SCI , ESPI_VWIRE_SIGNAL_DNX_ACK , ESPI_VWIRE_SIGNAL_SUS_ACK , ESPI_VWIRE_SIGNAL_TARGET_GPIO_0 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_1 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_2 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_3 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_4 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_5 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_6 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_7 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_8 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_9 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_10 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_11 , ESPI_VWIRE_SIGNAL_COUNT }
```

相关声明：[espi_vwire_signal](#gab65a0951a8912d9de398cfec0aef7d35)、[ESPI_VWIRE_SIGNAL_SLP_S3](#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166)、[ESPI_VWIRE_SIGNAL_SLP_S4](#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73)、[ESPI_VWIRE_SIGNAL_SLP_S5](#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13)、[ESPI_VWIRE_SIGNAL_OOB_RST_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1)、[ESPI_VWIRE_SIGNAL_PLTRST](#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08)、[ESPI_VWIRE_SIGNAL_SUS_STAT](#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663)、[ESPI_VWIRE_SIGNAL_NMIOUT](#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238)、[ESPI_VWIRE_SIGNAL_SMIOUT](#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152)、[ESPI_VWIRE_SIGNAL_HOST_RST_WARN](#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e)、[ESPI_VWIRE_SIGNAL_SLP_A](#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592)、[ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK](#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18)、[ESPI_VWIRE_SIGNAL_SUS_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5)、[ESPI_VWIRE_SIGNAL_SLP_WLAN](#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779)、[ESPI_VWIRE_SIGNAL_SLP_LAN](#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615)、[ESPI_VWIRE_SIGNAL_HOST_C10](#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c)、[ESPI_VWIRE_SIGNAL_DNX_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146)、[ESPI_VWIRE_SIGNAL_PME](#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692)、[ESPI_VWIRE_SIGNAL_WAKE](#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f)、[ESPI_VWIRE_SIGNAL_OOB_RST_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e)、[ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS](#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c)、[ESPI_VWIRE_SIGNAL_ERR_NON_FATAL](#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527)、[ESPI_VWIRE_SIGNAL_ERR_FATAL](#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1)、[ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE](#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631)、[ESPI_VWIRE_SIGNAL_HOST_RST_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e)、[ESPI_VWIRE_SIGNAL_RST_CPU_INIT](#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d)、[ESPI_VWIRE_SIGNAL_SMI](#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3)、[ESPI_VWIRE_SIGNAL_SCI](#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c)、[ESPI_VWIRE_SIGNAL_DNX_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c)、[ESPI_VWIRE_SIGNAL_SUS_ACK](#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_4](#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_5](#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_6](#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_7](#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_8](#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_9](#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_10](#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_11](#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f)、[ESPI_VWIRE_SIGNAL_COUNT](#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)。

可通过虚拟线通道发送或接收的 eSPI 系统平台信号。

<a id="r_gad00b6a22843e5df9c6d6945d0d82310e"></a>

```c
enum lpc_peripheral_opcode { E8042_OBF_HAS_CHAR = 0x50 , E8042_IBF_HAS_CHAR , E8042_WRITE_KB_CHAR , E8042_WRITE_MB_CHAR , E8042_RESUME_IRQ , E8042_PAUSE_IRQ , E8042_CLEAR_OBF , E8042_READ_KB_STS , E8042_SET_FLAG , E8042_CLEAR_FLAG , EACPI_OBF_HAS_CHAR = EACPI_START_OPCODE , EACPI_IBF_HAS_CHAR , EACPI_WRITE_CHAR , EACPI_READ_STS , EACPI_WRITE_STS , EACPI_GET_SHARED_MEMORY , ECUSTOM_HOST_SUBS_INTERRUPT_EN = ECUSTOM_START_OPCODE , ECUSTOM_HOST_CMD_GET_PARAM_MEMORY , ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE , ECUSTOM_HOST_CMD_SEND_RESULT }
```

相关声明：[lpc_peripheral_opcode](#gad00b6a22843e5df9c6d6945d0d82310e)、[E8042_OBF_HAS_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9)、[E8042_IBF_HAS_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a)、[E8042_WRITE_KB_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6)、[E8042_WRITE_MB_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911)、[E8042_RESUME_IRQ](#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198)、[E8042_PAUSE_IRQ](#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475)、[E8042_CLEAR_OBF](#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534)、[E8042_READ_KB_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b)、[E8042_SET_FLAG](#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447)、[E8042_CLEAR_FLAG](#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1)、[EACPI_OBF_HAS_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d)、[EACPI_IBF_HAS_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e)、[EACPI_WRITE_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7)、[EACPI_READ_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173)、[EACPI_WRITE_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)、[EACPI_GET_SHARED_MEMORY](#ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91)、[ECUSTOM_HOST_SUBS_INTERRUPT_EN](#ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b)、[ECUSTOM_HOST_CMD_GET_PARAM_MEMORY](#ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8)、[ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE](#ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40)、[ECUSTOM_HOST_CMD_SEND_RESULT](#ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243)。

eSPI LPC 外设操作码（Opcodes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.7\_函数（Functions）

<a id="r_ga7227c53d384eb0dc666361261f069f68"></a>

```c
int espi_config (const struct device *dev, struct espi_cfg *cfg)
```

相关声明：[espi_config](#ga7227c53d384eb0dc666361261f069f68)、[device](../device_reference/P002_设备对象结构.md)、[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

配置 eSPI 设备的运行方式。

<a id="r_ga869551e20fc2c3be4311c21c3c53999d"></a>

```c
bool espi_get_channel_status (const struct device *dev, enum espi_channel ch)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[espi_get_channel_status](#ga869551e20fc2c3be4311c21c3c53999d)、[device](../device_reference/P002_设备对象结构.md)、[espi_channel](#gafaa3f7d54503c901ab23bd79a7f8a755)。

查询逻辑通道（Logical channel）是否就绪。

<a id="r_ga112f7554ba614c8e5f239b1319b4a763"></a>

```c
int espi_read_request (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_read_request](#ga112f7554ba614c8e5f239b1319b4a763)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="r_ga143ed88b1f220f9582c809165fd983fd"></a>

```c
int espi_write_request (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_write_request](#ga143ed88b1f220f9582c809165fd983fd)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息写入请求。

<a id="r_gaeaae20afa90d9d825d80997369f31465"></a>

```c
int espi_read_lpc_request (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_read_lpc_request](#gaeaae20afa90d9d825d80997369f31465)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 LPC 外设读取 SoC 数据，其中的信息通过 eSPI 更新。

<a id="r_ga880b6b04824f9f0deea10e8018573b88"></a>

```c
int espi_write_lpc_request (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_write_lpc_request](#ga880b6b04824f9f0deea10e8018573b88)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 LPC 外设写入数据，由此产生 eSPI 事务（Transaction）。

<a id="r_gacab2b3bff7d940e71ee1c2a9fdedf782"></a>

```c
int espi_send_vwire (const struct device *dev, enum espi_vwire_signal signal, uint8_t level)
```

相关声明：[espi_send_vwire](#gacab2b3bff7d940e71ee1c2a9fdedf782)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](#gab65a0951a8912d9de398cfec0aef7d35)、[signal](../api_file_reference/P391_____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考.md#a5d326f119f87d0facaa662520f8c322a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将系统/平台信号作为虚拟线（Virtual wire）数据包发送。

<a id="r_gaa8bb48b5592c4b49d27c9b8a42432410"></a>

```c
int espi_receive_vwire (const struct device *dev, enum espi_vwire_signal signal, uint8_t *level)
```

相关声明：[espi_receive_vwire](#gaa8bb48b5592c4b49d27c9b8a42432410)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](#gab65a0951a8912d9de398cfec0aef7d35)、[signal](../api_file_reference/P391_____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考.md#a5d326f119f87d0facaa662520f8c322a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取封装在虚拟线中的信号的电平状态。

<a id="r_ga2557cfc7a38f669d14e9826e3fb0fdee"></a>

```c
int espi_send_oob (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_send_oob](#ga2557cfc7a38f669d14e9826e3fb0fdee)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

通过 eSPI 总线发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="r_ga4b8f4fbf66a2b2ae394e00b16500f70d"></a>

```c
int espi_receive_oob (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_receive_oob](#ga4b8f4fbf66a2b2ae394e00b16500f70d)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

从 eSPI 总线接收 SMBus 事务的带外数据包。

<a id="r_ga0a97d11167367342283bfe6b6d66726e"></a>

```c
int espi_read_flash (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_read_flash](#ga0a97d11167367342283bfe6b6d66726e)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的读取请求包。

<a id="r_gab02d46fd690e33875cc1b2433c976891"></a>

```c
int espi_write_flash (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_write_flash](#gab02d46fd690e33875cc1b2433c976891)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的写入请求包。

<a id="r_gab42be7c76c4523cea96365aa77fd18be"></a>

```c
int espi_flash_erase (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_flash_erase](#gab42be7c76c4523cea96365aa77fd18be)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的擦除请求包。

<a id="r_ga8d88e4e3893d610713195e5352ec2565"></a>

```c
static void espi_init_callback (struct espi_callback *callback, espi_callback_handler_t handler, enum espi_bus_event evt_type)
```

相关声明：[espi_init_callback](#ga8d88e4e3893d610713195e5352ec2565)、[espi_callback_handler_t](#ga9d848c7e367cf277230f365f73c15c46)、[espi_bus_event](#ga36ac3fbf9813f78bad90f047e1eb1128)。

回调模型（Callback model）。

<a id="r_gabf5f0ea01ec8ed5345b2e119181c2313"></a>

```c
static int espi_add_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_add_callback](#gabf5f0ea01ec8ed5345b2e119181c2313)、[device](../device_reference/P002_设备对象结构.md)。

添加应用回调。

<a id="r_ga7f04f98ea6a4671b821cf6ddf6bbf2a6"></a>

```c
static int espi_remove_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_remove_callback](#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)、[device](../device_reference/P002_设备对象结构.md)。

移除应用回调。

<a id="r_ga1cd0afc52d533414b5bbc684cef8b9af"></a>

```c
static int espi_interrupt_config (const struct device *dev, uint32_t espi_flags, uint32_t espi_vendor_flags)
```

相关声明：[espi_interrupt_config](#ga1cd0afc52d533414b5bbc684cef8b9af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

控制 eSPI 中断。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.8\_USB-C 端口过流信号别名（Over current signal aliases）

<a id="r_gae4855b6cf8049de8aa6d67763f1be8c3"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_0 ESPI_VWIRE_SIGNAL_TARGET_GPIO_0
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_0](#gae4855b6cf8049de8aa6d67763f1be8c3)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)。

USB-C 端口 0 的过流信号（Over current signal）。

<a id="r_ga2ed490939e0249ff8196f77a74967727"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_1 ESPI_VWIRE_SIGNAL_TARGET_GPIO_1
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_1](#ga2ed490939e0249ff8196f77a74967727)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)。

USB-C 端口 1 的过流信号。

<a id="r_gaf35d03bc041dc6baefe35b74c163d73b"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_2 ESPI_VWIRE_SIGNAL_TARGET_GPIO_2
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_2](#gaf35d03bc041dc6baefe35b74c163d73b)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)。

USB-C 端口 2 的过流信号。

<a id="r_gaeae1765d801cd298c27404c173a94707"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_3 ESPI_VWIRE_SIGNAL_TARGET_GPIO_3
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_3](#gaeae1765d801cd298c27404c173a94707)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)。

USB-C 端口 3 的过流信号。

## 7.9\_详细说明（Detailed Documentation）

<a id="ga6807d29b11134b76b14c8887053cbce1"></a>

### `ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST`

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST 2U
```

```c
#include <zephyr/drivers/espi.h>
```

ACPI 事件：输出缓冲区空。主机已读取嵌入式控制器（EC）写入 EC-to-Host 寄存器的数据。

<a id="ga01e61256f8be5e24d131c68d81ed8916"></a>

### `ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD`

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD 1U
```

```c
#include <zephyr/drivers/espi.h>
```

ACPI 事件：输入缓冲区满。

主机已写入命令寄存器（Command Register）。

<a id="gaa45ee9beafbda94f8f9ad799e78089cd"></a>

### `ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA`

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA 0
```

```c
#include <zephyr/drivers/espi.h>
```

ACPI 事件：输入缓冲区满。

主机已写入数据寄存器（Data Register）。

<a id="ga8da8ac3b45044323fdb24f1361adaac7"></a>

### `ESPI_INT_ALL_MASK`

```c
#define ESPI_INT_ALL_MASK
```

```c
#include <zephyr/drivers/espi.h>
```

展开值（Value）：

```c
(ESPI_BUS_EVENTS | ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS | \
ESPI_OOB_CHANNEL_EVENTS | ESPI_FLASH_CHANNEL_EVENTS | \
ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS | ESPI_PERIPHERAL_8042_KBC_EVENTS | \
ESPI_PERIPHERAL_HOST_IO_EVENTS | ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS)
```

选择所有 eSPI 通用中断。

注意：此处不包括通过 eSPI 隧道传输的 UART 中断，因为 eSPI 驱动使用方通常需要区分它们。

<a id="gadeb45b8838f4d1fbf05095c36ca3faba"></a>

### `ESPI_INT_BUS_ONLY_MASK`

```c
#define ESPI_INT_BUS_ONLY_MASK
```

```c
#include <zephyr/drivers/espi.h>
```

展开值（Value）：

```c
(ESPI_BUS_EVENTS | ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS | \
ESPI_OOB_CHANNEL_EVENTS | ESPI_FLASH_CHANNEL_EVENTS)
```

仅选择 eSPI 总线硬件中断。

<a id="ga24b468de0013cd9cf9d814faff13b94e"></a>

### `ESPI_INT_NONE_MASK`

```c
#define ESPI_INT_NONE_MASK 0U
```

```c
#include <zephyr/drivers/espi.h>
```

禁用所有 eSPI 硬件事件。

<a id="gae4855b6cf8049de8aa6d67763f1be8c3"></a>

### `ESPI_VWIRE_SIGNAL_OCB_0`

```c
#define ESPI_VWIRE_SIGNAL_OCB_0 ESPI_VWIRE_SIGNAL_TARGET_GPIO_0
```

```c
#include <zephyr/drivers/espi.h>
```

USB-C 端口 0 的过流信号（Over current signal）。

<a id="ga2ed490939e0249ff8196f77a74967727"></a>

### `ESPI_VWIRE_SIGNAL_OCB_1`

```c
#define ESPI_VWIRE_SIGNAL_OCB_1 ESPI_VWIRE_SIGNAL_TARGET_GPIO_1
```

```c
#include <zephyr/drivers/espi.h>
```

USB-C 端口 1 的过流信号。

<a id="gaf35d03bc041dc6baefe35b74c163d73b"></a>

### `ESPI_VWIRE_SIGNAL_OCB_2`

```c
#define ESPI_VWIRE_SIGNAL_OCB_2 ESPI_VWIRE_SIGNAL_TARGET_GPIO_2
```

```c
#include <zephyr/drivers/espi.h>
```

USB-C 端口 2 的过流信号。

<a id="gaeae1765d801cd298c27404c173a94707"></a>

### `ESPI_VWIRE_SIGNAL_OCB_3`

```c
#define ESPI_VWIRE_SIGNAL_OCB_3 ESPI_VWIRE_SIGNAL_TARGET_GPIO_3
```

```c
#include <zephyr/drivers/espi.h>
```

USB-C 端口 3 的过流信号。

<a id="gaa0807c908666cdcbb3a85f310bfbfccc"></a>

### `HOST_KBC_EVT_IBF`

```c
#define HOST_KBC_EVT_IBF BIT(0)
```

```c
#include <zephyr/drivers/espi.h>
```

KBC 8042 事件：输入缓冲区满（Input Buffer Full）。

<a id="ga807bb75027f24e040cd28eba4bc1002c"></a>

### `HOST_KBC_EVT_OBE`

```c
#define HOST_KBC_EVT_OBE BIT(1)
```

```c
#include <zephyr/drivers/espi.h>
```

KBC 8042 事件：输出缓冲区空（Output Buffer Empty）。

<a id="ga9d848c7e367cf277230f365f73c15c46"></a>

### `espi_callback_handler_t`

```c
typedef void(* espi_callback_handler_t) (const struct device *dev, struct espi_callback *cb, struct espi_event espi_evt)
```

```c
#include <zephyr/drivers/espi.h>
```

定义应用程序回调处理函数的签名（Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | eSPI 设备的设备结构（Device Struct）。 |
| `cb` | 拥有此处理程序的原始 `struct espi_callback`。 |
| `espi_evt` | 触发回调处理程序的事件详情（Event Details）。 |

<a id="ga36ac3fbf9813f78bad90f047e1eb1128"></a>

### `espi_bus_event`

```c
enum espi_bus_event
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 总线事件。

eSPI 总线事件（Bus Event），表示用户可注册回调的事件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_BUS_RESET` | 表示 eSPI 总线已通过 eSPI 复位引脚（Reset Pin）复位。驱动应按照 eSPI 规范的复位引脚约定，将复位状态传递给驱动使用方：0 表示总线处于复位状态（In Reset），1 表示总线已退出复位（Out-of-reset）。注意：带内复位（In-band Reset）无需发送此回调。 |
| `ESPI_BUS_EVENT_CHANNEL_READY` | 表示 eSPI 硬件已从 eSPI 控制器（Controller）收到通道使能通知（Channel Enable Notification）。向控制器发出通道就绪信号后，驱动应通过此事件将 eSPI 通道就绪状态传递给驱动使用方。 |
| `ESPI_BUS_EVENT_VWIRE_RECEIVED` | 表示 eSPI 硬件已从 eSPI 控制器收到虚拟线消息（Virtual Wire Message）。驱动应传递虚拟线的最新状态。 |
| `ESPI_BUS_EVENT_OOB_RECEIVED` | 表示 eSPI 硬件已从 eSPI 控制器收到带外数据包（Out-of-band Packet）。 |
| `ESPI_BUS_PERIPHERAL_NOTIFICATION` | 表示 eSPI 硬件已收到来自 eSPI 主机控制器的外设事件（Peripheral Event），驱动应传递外设类型（Peripheral Type）。译注：原文 `has received a peripheral eSPI host controller` 表述不完整，此处结合后文理解为外设事件。 |
| `ESPI_BUS_TAF_NOTIFICATION` | 表示 eSPI 硬件已收到目标端连接闪存（Target Attached Flash，TAF）的通知事件。 |

<a id="gafaa3f7d54503c901ab23bd79a7f8a755"></a>

### `espi_channel`

```c
enum espi_channel
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 通道（Channel）。

原始示例（Example）：

```c
+----------------------------------------------------------------------+
|                                                                      |
|  eSPI controller                     +-------------+                 |
|                      +-----------+   |    Power    |   +----------+  |
|                      |Out of band|   |  management |   |   GPIO   |  |
|  +------------+      |processor  |   |  controller |   |  sources |  |
|  |  SPI flash |      +-----------+   +-------------+   +----------+  |
|  | controller |            |                |               |        |
|  +------------+            |                |               |        |
|   |  |    |                +--------+       +---------------+        |
|   |  |    |                         |               |                |
|   |  |    +-----+   +--------+   +----------+  +----v-----+          |
|   |  |          |   |  LPC   |   | Tunneled |  | Tunneled |          |
|   |  |          |   | bridge |   |  SMBus   |  |   GPIO   |          |
|   |  |          |   +--------+   +----------+  +----------+          |
|   |  |          |        |             |             |               |
|   |  |          |        ------+       |             |               |
|   |  |          |              |       |             |               |
|   |  |   +------v-----+    +---v-------v-------------v----+          |
|   |  |   | eSPI Flash |    |    eSPI protocol block       |          |
|   |  |   |   access   +--->+                              |          |
|   |  |   +------------+    +------------------------------+          |
|   |  |                             |                                 |
|   |  +-----------+                 |                                 |
|   |              v                 v                                 |
|   |           XXXXXXXXXXXXXXXXXXXXXXX                                |
|   |            XXXXXXXXXXXXXXXXXXXXX                                 |
|   |             XXXXXXXXXXXXXXXXXXX                                  |
+----------------------------------------------------------------------+
   |                      |
   v             +-----------------+
 +---------+     |  |   |   |   |  |
 |  Flash  |     |  |   |   |   |  |
 +---------+     |  +   +   +   +  |    eSPI bus
                 | CH0 CH1 CH2 CH3 |    (logical channels)
                 |  +   +   +   +  |
                 |  |   |   |   |  |
                 +-----------------+
                          |
+-----------------------------------------------------------------------+
|  eSPI target                                                          |
|                                                                       |
|       CH0         |     CH1      |      CH2      |    CH3             |
|   eSPI endpoint   |    VWIRE     |      OOB      |   Flash            |
+-----------------------------------------------------------------------+
```

标识 eSPI 目标端硬件支持的各个逻辑通道（Logical Channels）。各通道允许独立传输，但通道类型到通道编号的分配关系是固定的。

注意：通用命令（Generic Commands）不关联任何通道，因此即使所有通道均被禁用或尚未就绪，eSPI 上仍可发生传输。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_CHANNEL_PERIPHERAL` | 外设通道（Peripheral Channel），通道 0。 |
| `ESPI_CHANNEL_VWIRE` | 虚拟线通道（Virtual Wire Channel），通道 1。 |
| `ESPI_CHANNEL_OOB` | 带外通道（Out-of-Band Channel），通道 2。 |
| `ESPI_CHANNEL_FLASH` | 闪存访问通道（Flash Access Channel），通道 3。 |

<a id="ga3e52615f244d7fa8ccda495ab8ec8a5b"></a>

### `espi_cycle_type`

```c
enum espi_cycle_type
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 外设通道支持的 eSPI 周期类型（Cycle types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_CYCLE_MEMORY_READ32` | 32 位存储器读周期（Memory Read Cycle）。 |
| `ESPI_CYCLE_MEMORY_READ64` | 64 位存储器读周期（Memory Read Cycle）。 |
| `ESPI_CYCLE_MEMORY_WRITE32` | 32 位存储器写周期（Memory Write Cycle）。 |
| `ESPI_CYCLE_MEMORY_WRITE64` | 64 位存储器写周期（Memory Write Cycle）。 |
| `ESPI_CYCLE_MESSAGE_NODATA` | 不带数据的消息周期（Message Cycle）。 |
| `ESPI_CYCLE_MESSAGE_DATA` | 带数据的消息周期（Message Cycle）。 |
| `ESPI_CYCLE_OK_COMPLETION_NODATA` | 成功完成（Successful Completion），不带数据。 |
| `ESPI_CYCLE_OKCOMPLETION_DATA` | 成功完成（Successful Completion），带数据。 |
| `ESPI_CYCLE_NOK_COMPLETION_NODATA` | 未成功完成（Unsuccessful Completion），不带数据。 |

<a id="ga4e35c754c720f262805689a94985272c"></a>

### `espi_interrupt_flags`

```c
enum espi_interrupt_flags
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 中断标志。

eSPI 中断标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_BUS_EVENTS` | 使能 eSPI 总线复位中断和通道协商变化（Channel Negotiation Changes）事件。 |
| `ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS` | 使能 eSPI 虚拟线（VW）接收中断。 |
| `ESPI_OOB_CHANNEL_EVENTS` | 使能 eSPI 带外（OOB）接收中断。 |
| `ESPI_FLASH_CHANNEL_EVENTS` | 使能 eSPI 闪存操作（Flash Operations）中断。 |
| `ESPI_PERIPHERAL_UART_EVENTS` | 硬件支持时，使能 UART 中断。 |
| `ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS` | 硬件支持时，使能端口 80（Port80）eSPI 中断。 |
| `ESPI_PERIPHERAL_8042_KBC_EVENTS` | 硬件支持时，使能 8042 中断。 |
| `ESPI_PERIPHERAL_HOST_IO_EVENTS` | 硬件支持时，使能所有 ACPI eSPI 主机接口（Host Interface）中断。 |
| `ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS` | 硬件支持时，使能 eSPI 共享内存（Shared Memory）中断。 |

<a id="ga0d7c61f1f4ec611d0c8a67ba73e2b4f0"></a>

### `espi_io_mode`

```c
enum espi_io_mode
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI I/O 模式能力（Capabilities）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_IO_MODE_SINGLE_LINE` | 单数据线模式（Single Data Line Mode），即传统 SPI。 |
| `ESPI_IO_MODE_DUAL_LINES` | 双数据线模式（Dual Data Line Mode）。 |
| `ESPI_IO_MODE_QUAD_LINES` | 四数据线模式（Quad Data Line Mode）。 |

<a id="gac55098842dd9d181144ac4b4122a610e"></a>

### `espi_pc_event`

```c
enum espi_pc_event
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 外设通道事件（Peripheral channel events）。

用于通知用户的 eSPI 外设通道事件类型（Peripheral Channel Event Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_PC_EVT_BUS_CHANNEL_READY` | 总线通道就绪事件（Bus Channel Ready Event）。 |
| `ESPI_PC_EVT_BUS_MASTER_ENABLE` | 总线主控使能事件（Bus Master Enable Event）。 |

<a id="ga2629a5518a94f031419eeccd05f07373"></a>

### `espi_virtual_peripheral`

```c
enum espi_virtual_peripheral
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI 外设通知类型（Notification type）。

eSPI 外设通知事件详情（Peripheral Notification Event Details），用于指示哪个外设触发了 eSPI 回调。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_PERIPHERAL_UART` | UART 外设（Peripheral）。 |
| `ESPI_PERIPHERAL_8042_KBC` | 8042 键盘外设（Keyboard Peripheral）。 |
| `ESPI_PERIPHERAL_HOST_IO` | 主机 I/O 外设（Host I/O Peripheral）。 |
| `ESPI_PERIPHERAL_DEBUG_PORT80` | 调试端口 80 外设（Debug Port 80 Peripheral）。 |
| `ESPI_PERIPHERAL_HOST_IO_PVT` | 专用主机 I/O 外设（Private Host I/O Peripheral）。 |
| `ESPI_PERIPHERAL_HOST_IO_PVT2` | 专用主机 I/O 外设 2（Private Host I/O Peripheral 2）。 |
| `ESPI_PERIPHERAL_HOST_IO_PVT3` | 专用主机 I/O 外设 3（Private Host I/O Peripheral 3）。 |
| `ESPI_PERIPHERAL_EC_HOST_CMD` | 嵌入式控制器主机命令外设（Embedded Controller Host Command Peripheral）。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD` 时可用。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD` 时可用。

<a id="gab65a0951a8912d9de398cfec0aef7d35"></a>

### `espi_vwire_signal`

```c
enum espi_vwire_signal
```

```c
#include <zephyr/drivers/espi.h>
```

可通过虚拟线通道发送或接收的 eSPI 系统平台信号。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_VWIRE_SIGNAL_SLP_S3` | 睡眠 S3 状态信号（Sleep S3 State Signal）。 |
| `ESPI_VWIRE_SIGNAL_SLP_S4` | 睡眠 S4 状态信号（Sleep S4 State Signal）。 |
| `ESPI_VWIRE_SIGNAL_SLP_S5` | 睡眠 S5 状态信号（Sleep S5 State Signal）。 |
| `ESPI_VWIRE_SIGNAL_OOB_RST_WARN` | 带外复位预警信号（Out-of-band Reset Warning Signal）。 |
| `ESPI_VWIRE_SIGNAL_PLTRST` | 平台复位信号（Platform Reset Signal）。 |
| `ESPI_VWIRE_SIGNAL_SUS_STAT` | 挂起状态信号（Suspend Status Signal）。 |
| `ESPI_VWIRE_SIGNAL_NMIOUT` | 不可屏蔽中断（NMI）输出信号。 |
| `ESPI_VWIRE_SIGNAL_SMIOUT` | 系统管理中断（SMI）输出信号。 |
| `ESPI_VWIRE_SIGNAL_HOST_RST_WARN` | 主机复位预警信号（Host Reset Warning Signal）。 |
| `ESPI_VWIRE_SIGNAL_SLP_A` | 睡眠 A 状态信号（Sleep A State Signal）。 |
| `ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK` | 挂起断电确认信号（Suspend Power Down Acknowledge Signal）。 |
| `ESPI_VWIRE_SIGNAL_SUS_WARN` | 挂起预警信号（Suspend Warning Signal）。 |
| `ESPI_VWIRE_SIGNAL_SLP_WLAN` | 无线局域网睡眠信号（Sleep WLAN Signal）。 |
| `ESPI_VWIRE_SIGNAL_SLP_LAN` | 局域网睡眠信号（Sleep LAN Signal）。 |
| `ESPI_VWIRE_SIGNAL_HOST_C10` | 主机 C10 状态信号（Host C10 State Signal）。 |
| `ESPI_VWIRE_SIGNAL_DNX_WARN` | 调试与异常（Debug and eXception，DNX）预警信号。 |
| `ESPI_VWIRE_SIGNAL_PME` | 电源管理事件信号（Power Management Event Signal）。 |
| `ESPI_VWIRE_SIGNAL_WAKE` | 唤醒信号（Wake Signal）。 |
| `ESPI_VWIRE_SIGNAL_OOB_RST_ACK` | 带外复位确认信号（Out-of-band Reset Acknowledge Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS` | 目标端启动状态信号（Target Boot Status Signal）。 |
| `ESPI_VWIRE_SIGNAL_ERR_NON_FATAL` | 非致命错误信号（Non-fatal Error Signal）。 |
| `ESPI_VWIRE_SIGNAL_ERR_FATAL` | 致命错误信号（Fatal Error Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE` | 目标端启动完成信号（Target Boot Done Signal）。 |
| `ESPI_VWIRE_SIGNAL_HOST_RST_ACK` | 主机复位确认信号（Host Reset Acknowledge Signal）。 |
| `ESPI_VWIRE_SIGNAL_RST_CPU_INIT` | 复位 CPU 初始化信号（Reset CPU Initialization Signal）。 |
| `ESPI_VWIRE_SIGNAL_SMI` | 系统管理中断信号（System Management Interrupt Signal）。 |
| `ESPI_VWIRE_SIGNAL_SCI` | 系统控制中断信号（System Control Interrupt Signal）。 |
| `ESPI_VWIRE_SIGNAL_DNX_ACK` | DNX 确认信号（Acknowledge Signal）。 |
| `ESPI_VWIRE_SIGNAL_SUS_ACK` | 挂起确认信号（Suspend Acknowledge Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_0` | 目标端 GPIO 0 信号（Target GPIO 0 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_1` | 目标端 GPIO 1 信号（Target GPIO 1 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_2` | 目标端 GPIO 2 信号（Target GPIO 2 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_3` | 目标端 GPIO 3 信号（Target GPIO 3 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_4` | 目标端 GPIO 4 信号（Target GPIO 4 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_5` | 目标端 GPIO 5 信号（Target GPIO 5 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_6` | 目标端 GPIO 6 信号（Target GPIO 6 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_7` | 目标端 GPIO 7 信号（Target GPIO 7 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_8` | 目标端 GPIO 8 信号（Target GPIO 8 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_9` | 目标端 GPIO 9 信号（Target GPIO 9 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_10` | 目标端 GPIO 10 信号（Target GPIO 10 Signal）。 |
| `ESPI_VWIRE_SIGNAL_TARGET_GPIO_11` | 目标端 GPIO 11 信号（Target GPIO 11 Signal）。 |
| `ESPI_VWIRE_SIGNAL_COUNT` | 虚拟线（Virtual Wire）信号数量。 |

<a id="gad00b6a22843e5df9c6d6945d0d82310e"></a>

### `lpc_peripheral_opcode`

```c
enum lpc_peripheral_opcode
```

```c
#include <zephyr/drivers/espi.h>
```

eSPI LPC 外设操作码（Opcodes）。

通过 eSPI 隧道传输的低引脚数总线（LPC）外设操作码（Opcodes），用于与传统 LPC 设备交互。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `E8042_OBF_HAS_CHAR` | 检查 8042 输出缓冲区（Output Buffer）是否有字符。 |
| `E8042_IBF_HAS_CHAR` | 检查 8042 输入缓冲区（Input Buffer）是否有字符。 |
| `E8042_WRITE_KB_CHAR` | 向 8042 键盘缓冲区（Keyboard Buffer）写入字符。 |
| `E8042_WRITE_MB_CHAR` | 向 8042 鼠标缓冲区（Mouse Buffer）写入字符。 |
| `E8042_RESUME_IRQ` | 恢复 8042 中断处理（Interrupt Processing）。 |
| `E8042_PAUSE_IRQ` | 暂停 8042 中断处理（Interrupt Processing）。 |
| `E8042_CLEAR_OBF` | 清空 8042 输出缓冲区（Output Buffer）。 |
| `E8042_READ_KB_STS` | 读取 8042 键盘状态（Keyboard Status）。 |
| `E8042_SET_FLAG` | 设置 8042 标志（Flag）。 |
| `E8042_CLEAR_FLAG` | 清除 8042 标志（Flag）。 |
| `EACPI_OBF_HAS_CHAR` | 检查 ACPI 输出缓冲区（Output Buffer）是否有字符。 |
| `EACPI_IBF_HAS_CHAR` | 检查 ACPI 输入缓冲区（Input Buffer）是否有字符。 |
| `EACPI_WRITE_CHAR` | 向 ACPI 输出缓冲区（Output Buffer）写入字符。 |
| `EACPI_READ_STS` | 读取 ACPI 状态（Status）。 |
| `EACPI_WRITE_STS` | 写入 ACPI 状态（Status）。 |
| `EACPI_GET_SHARED_MEMORY` | 支持通过共享内存区域（Shared Memory Region）返回 ACPI 响应数据。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION` 时可用。 |
| `ECUSTOM_HOST_SUBS_INTERRUPT_EN` | 使能主机子系统中断（Host Subsystem Interrupt），自定义操作。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。已弃用（Deprecated）：请改用 `espi_interrupt_config`。 |
| `ECUSTOM_HOST_CMD_GET_PARAM_MEMORY` | 获取主机命令参数内存（Host Command Parameter Memory），自定义操作。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。 |
| `ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE` | 获取主机命令参数内存大小（Host Command Parameter Memory Size），自定义操作。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。 |
| `ECUSTOM_HOST_CMD_SEND_RESULT` | 发送主机命令结果（Host Command Result），自定义操作。注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `espi_interrupt_config`。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE` 时可用。

<a id="gabf5f0ea01ec8ed5345b2e119181c2313"></a>

### `espi_add_callback()`

```c
int espi_add_callback ( const struct device * dev, struct espi_callback * callback )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi.h>
```

添加应用回调。

注意：可根据需要向同一设备添加任意数量的回调（Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `callback` | 有效的应用回调结构体指针（Callback Structure Pointer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

**说明（Note）**：注意（Note）：可在回调处理函数执行期间向设备添加回调，但未规定新回调是否会针对当前 eSPI 事件执行。

<a id="ga7227c53d384eb0dc666361261f069f68"></a>

### `espi_config()`

```c
int espi_config ( const struct device * dev, struct espi_cfg * cfg )
```

```c
#include <zephyr/drivers/espi.h>
```

配置 eSPI 设备的运行方式。

此例程提供用于覆盖 eSPI 硬件能力（Hardware Capabilities）的通用接口。

如果该 eSPI 控制器充当目标端（Target），初始化期间，eSPI 控制器发出的 `GET_CONFIGURATION` 命令将发现此处设置的值。

如果该 eSPI 控制器充当控制端（Controller），它将使用此处设置的值确定与 eSPI 目标端共同支持的最低能力（Minimum Common Capabilities），然后通过 `SET_CONFIGURATION` 命令发送。

原始示例（Example）：

```c
+---------+   +---------+     +------+          +---------+   +-------------+
|  eSPI   |   |  eSPI   |     | eSPI |          |  eSPI   |   |  eSPI       |
|  target |   | driver  |     |  bus |          |  driver |   |  controller |
+---------+   +---------+     +------+          +---------+   +-------------+
    |              |            |                   |             |
    | espi_config  | Set eSPI   |       Set eSPI    | espi_config |
    +--------------+ ctrl regs  |       cap ctrl reg| +-----------+
    |              +-------+    |          +--------+             |
    |              |<------+    |          +------->|             |
    |              |            |                   |             |
    |              |            |                   |             |
    |              |            | GET_CONFIGURATION |             |
    |              |            +<------------------+             |
    |              |<-----------|                   |             |
    |              | eSPI caps  |                   |             |
    |              |----------->+    response       |             |
    |              |            |------------------>+             |
    |              |            |                   |             |
    |              |            | SET_CONFIGURATION |             |
    |              |            +<------------------+             |
    |              |            |  accept           |             |
    |              |            +------------------>+             |
    +              +            +                   +             +
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `cfg` | eSPI 控制器的设备运行时配置（Runtime Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | eSPI 目标端（Target）不支持此能力。 |

<a id="gab42be7c76c4523cea96365aa77fd18be"></a>

### `espi_flash_erase()`

```c
int espi_flash_erase ( const struct device * dev, struct espi_flash_packet * pckt )
```

```c
#include <zephyr/drivers/espi.h>
```

发送共享 Flash 的擦除请求包。

此例程提供发送请求的接口，用于擦除 eSPI 控制器和目标端共享的闪存组件（Flash Components）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存擦除事务（Erase Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被控制器禁用。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="ga869551e20fc2c3be4311c21c3c53999d"></a>

### `espi_get_channel_status()`

```c
bool espi_get_channel_status ( const struct device * dev, enum espi_channel ch )
```

```c
#include <zephyr/drivers/espi.h>
```

查询逻辑通道（Logical channel）是否就绪。

此例程允许在使用逻辑通道（Logical Channel）前检查其是否就绪。注意：查询不受支持的通道时始终返回 `false`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `ch` | 要获取状态的 eSPI 通道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | eSPI 通道是否就绪（Ready）。 |
| `false` | 其他情况。 |

<a id="ga8d88e4e3893d610713195e5352ec2565"></a>

### `espi_init_callback()`

```c
void espi_init_callback ( struct espi_callback * callback, espi_callback_handler_t handler, enum espi_bus_event evt_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi.h>
```

回调模型（Callback model）。

原始示例（Example）：

```c
+-------------+            +-------------+   +--------+     +------------+
|  Zephyr App |            | eSPI driver |   |  eSPI  |     |   eSPI     |
|       on    |            |             |   | target |     | controller |
| eSPI target |            |             |   |   HW   |     |            |
+---+---------+            +-------+-----+   +---+----+     +----+-------+
    |                              |             |               |
    |   espi_init_callback         |             |               |
    +----------------------------> |             |               |
    |   espi_add_callback          |             |               |
    +----------------------------->+             |               |
    |                              |             |  eSPI reset   |  eSPI controller
    |                              |    IRQ      +<--------------+  resets the
    |                              | <-----------+               |  bus
    |<-----------------------------|             |               |
    | Report eSPI bus reset        | Processed   |               |
    |                              | within the  |               |
    |                              | driver      |               |
    |                              |             |               |
    |                              |             |  VW CH ready  |  eSPI controller
    |                              |    IRQ      +<--------------+  enables VW
    |                              | <-----------+               |  channel
    |                              |             |               |
    |                              | Processed   |               |
    |                              | within the  |               |
    |                              | driver      |               |
    |                              |             |               |
    |                              |             | Memory I/O    |  Peripheral
    |                              |             <---------------+  event
    |                              +<------------+               |
    +<-----------------------------+ callback    |               |
    | Report peripheral event      |             |               |
    | and data for the event       |             |               |
    |                              |             |               |
    |                              |             | SLP_S5        |  eSPI controller
    |                              |             <---------------+  send VWire
    |                              +<------------+               |
    +<-----------------------------+ callback    |               |
    | App enables/configures       |             |               |
    | discrete regulator           |             |               |
    |                              |             |               |
    |   espi_send_vwire_signal     |             |               |
    +------------------------------>------------>|-------------->|
    |                              |             |               |
    |                              |             | HOST_RST      |  eSPI controller
    |                              |             <---------------+  send VWire
    |                              +<------------+               |
    +<-----------------------------+ callback    |               |
    | App reset host-related       |             |               |
    | data structures              |             |               |
    |                              |             |               |
    |                              |             |   C10         |  eSPI controller
    |                              |             +<--------------+  send VWire
    |                              <-------------+               |
    <------------------------------+             |               |
    | App executes                 |             |               |
    + power mgmt policy            |             |               |
```

用于正确初始化 `espi_callback` 结构的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针（Callback Structure Pointer）。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `evt_type` | 指出与处理函数相关的 eSPI 事件；对于 VWIRE_RECEIVED 事件，数据表示新置为有效的电平。 |

<a id="ga1cd0afc52d533414b5bbc684cef8b9af"></a>

### `espi_interrupt_config()`

```c
int espi_interrupt_config ( const struct device * dev, uint32_t espi_flags, uint32_t espi_vendor_flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi.h>
```

控制 eSPI 中断。

此例程为 eSPI 驱动使用方提供使能／禁用驱动模块中断（Interrupts）的方法。

如果 eSPI 驱动未在初始化期间使能中断，驱动使用方需要在完成 eSPI 配置后，以及每次 eSPI 总线复位事件后，显式使能中断。

原始示例（Example）：

```c
+---------+        +---------+     +------+          +---------+   +---------+
|  eSPI   |        |  eSPI   |     | eSPI |          |  eSPI   |   |  eSPI   |
|  target |        | driver  |     |  bus |          |  driver |   |  host   |
+--------+        +---------+     +------+          +---------+   +---------+
    |                   |            |                   |             |
    |                   +- eSPI---|  |                   |             |
    +                   +<- init--|  |                   |             |
    |                   |            |                   |             |
    |                   |            |                   |             |
    | espi_config       | Set eSPI   |                   |             |
    +-------------------+ ctrl regs  |                   |             |
    |                   +-------+    |                   |             |
    |                   |<------+    |                   |             |
    |                   |            |                   |             |
    | interrupt_config  |            |                   |             |
    +-------------------+            |                   |             |
    |                   |            |                   |             |  eSPI host
    |                   |            |    VW  packet     +<------------+  sends VW
    |                   |    ISR     | <-----------------+             |
    |  VWIRE_RECEIVED   |<-----------|                   |             |
    +<------------------+            +                   +             +
    |                   |            |                   |             |
    |                   |            |                   |             |  eSPI host
    |                   |            |    eSPI reset     +<------------+  resets the
    |                   |    ISR     | <-----------------+             |  bus
    |      callback     |<-----------|                   |             |
    +<------------------+            +                   +             +
    |                   |            |                   |             |
    | interrupt_config  |            |                   |             |
    +-------------------+            |                   |             |
```

注意：两种情况下，1 均表示使能对应中断事件（Interrupt Event），0 表示禁用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `espi_flags` | 用于选择通用 eSPI 中断事件（Interrupt Events）的位图。 |
| `espi_vendor_flags` | 用于选择厂商专用 eSPI 中断事件（Vendor-specific Interrupt Events）的位图。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | eSPI 目标端（Target）不支持此能力。 |

<a id="ga0a97d11167367342283bfe6b6d66726e"></a>

### `espi_read_flash()`

```c
int espi_read_flash ( const struct device * dev, struct espi_flash_packet * pckt )
```

```c
#include <zephyr/drivers/espi.h>
```

发送共享 Flash 的读取请求包。

此例程提供发送请求的接口，用于读取 eSPI 控制器和目标端共享的闪存组件（Flash Component）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存读取事务（Read Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被控制器禁用。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="gaeaae20afa90d9d825d80997369f31465"></a>

### `espi_read_lpc_request()`

```c
int espi_read_lpc_request ( const struct device * dev, enum lpc_peripheral_opcode op, uint32_t * data )
```

```c
#include <zephyr/drivers/espi.h>
```

从 LPC 外设读取 SoC 数据，其中的信息通过 eSPI 更新。

此例程提供通用接口，用于读取信息已被 eSPI 事务（Transaction）更新的模块。读取操作可能触发事务。eSPI 数据包由硬件模块（Hardware Block）组装。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `op` | 表示外设类型和读取请求操作码（Opcode）的枚举。 |
| `data` | 要从 LPC 外设读取的参数（Parameter）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | eSPI 外设（Peripheral）已关闭或不受支持。 |
| `-EINVAL` | LPC 操作码（Opcode）处于有效范围内，但尚未实现。 |

<a id="ga112f7554ba614c8e5f239b1319b4a763"></a>

### `espi_read_request()`

```c
int espi_read_request ( const struct device * dev, struct espi_request_packet * req )
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送内存、I/O 或消息读取请求。

此例程提供发送读取请求数据包（Read Request Packet）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `req` | 表示存储器、I/O 或消息读取请求（Read Request）的结构地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | eSPI 控制器不支持原始数据包（Raw Packets），而是由控制器硬件直接处理低地址存储器事务（Low Memory Transactions）。 |
| `-EIO` | 一般输入／输出错误（I/O error），通过总线发送失败。 |

<a id="ga4b8f4fbf66a2b2ae394e00b16500f70d"></a>

### `espi_receive_oob()`

```c
int espi_receive_oob ( const struct device * dev, struct espi_oob_packet * pckt )
```

```c
#include <zephyr/drivers/espi.h>
```

从 eSPI 总线接收 SMBus 事务的带外数据包。

此例程提供从 eSPI 总线接收并解码系统管理总线（SMBus）事务的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 表示 SMBus 事务（Transaction）的数据包地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="gaa8bb48b5592c4b49d27c9b8a42432410"></a>

### `espi_receive_vwire()`

```c
int espi_receive_vwire ( const struct device * dev, enum espi_vwire_signal signal, uint8_t * level )
```

```c
#include <zephyr/drivers/espi.h>
```

获取封装在虚拟线中的信号的电平状态。

此例程提供通用接口，用于向 eSPI 控制器请求虚拟线数据包（Virtual Wire Packet）并获取信号电平。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` signal` | 要向 eSPI 控制器请求的信号（Signal）。 |
| `[out] level` | 所请求信号的电平（Level）：`0b` 表示低（LOW），`1b` 表示高（HIGH）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="ga7f04f98ea6a4671b821cf6ddf6bbf2a6"></a>

### `espi_remove_callback()`

```c
int espi_remove_callback ( const struct device * dev, struct espi_callback * callback )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi.h>
```

移除应用回调。

注意：可移除通过 espi_add_callback() 添加的任意多个回调（Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `callback` | 有效的应用回调结构体指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

**警告（Warning）**：警告（Warning）：明确允许在回调处理函数内部注销当前正在执行的回调，即 callback。尝试注销同一设备上的其他回调，可能导致未定义行为（Undefined Behavior），包括漏调仍注册的回调，以及意外调用已移除的回调。

<a id="ga2557cfc7a38f669d14e9826e3fb0fdee"></a>

### `espi_send_oob()`

```c
int espi_send_oob ( const struct device * dev, struct espi_oob_packet * pckt )
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 总线发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

此例程提供封装 SMBus 事务（Transaction）并通过 eSPI 总线以数据包形式发送的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 表示 SMBus 事务（Transaction）的数据包地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="gacab2b3bff7d940e71ee1c2a9fdedf782"></a>

### `espi_send_vwire()`

```c
int espi_send_vwire ( const struct device * dev, enum espi_vwire_signal signal, uint8_t level )
```

```c
#include <zephyr/drivers/espi.h>
```

将系统/平台信号作为虚拟线（Virtual wire）数据包发送。

此例程提供从目标端向控制器发送虚拟线数据包（Virtual Wire Packet）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `signal` | 要发送给 eSPI 控制器的信号（Signal）。 |
| `level` | 所请求信号的电平（Level）：低（LOW）为 0，高（HIGH）为 1。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error），通过总线发送失败。 |
| `-EINVAL` | 信号（Signal）无效。 |
| `-ETIMEDOUT` | 等待 eSPI 控制器处理虚拟线（VW）超时。 |

<a id="gab02d46fd690e33875cc1b2433c976891"></a>

### `espi_write_flash()`

```c
int espi_write_flash ( const struct device * dev, struct espi_flash_packet * pckt )
```

```c
#include <zephyr/drivers/espi.h>
```

发送共享 Flash 的写入请求包。

此例程提供发送请求的接口，用于写入 eSPI 控制器和目标端共享的闪存组件（Flash Components）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存写入事务（Write Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被控制器禁用。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），向控制器发出的请求失败。 |

<a id="ga880b6b04824f9f0deea10e8018573b88"></a>

### `espi_write_lpc_request()`

```c
int espi_write_lpc_request ( const struct device * dev, enum lpc_peripheral_opcode op, uint32_t * data )
```

```c
#include <zephyr/drivers/espi.h>
```

向 LPC 外设写入数据，由此产生 eSPI 事务（Transaction）。

此例程提供向模块写入数据的通用接口，写入会触发 eSPI 事务（Transaction）。eSPI 数据包由硬件模块（Hardware Block）组装。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `op` | 表示外设类型和写入请求操作码（Opcode）的枚举。 |
| `data` | 传递给 LPC 外设的参数（Parameter）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | eSPI 外设（Peripheral）已关闭或不受支持。 |
| `-EINVAL` | LPC 操作码（Opcode）处于有效范围内，但尚未实现。 |

<a id="ga143ed88b1f220f9582c809165fd983fd"></a>

### `espi_write_request()`

```c
int espi_write_request ( const struct device * dev, struct espi_request_packet * req )
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送内存、I/O 或消息写入请求。

此例程提供发送写入请求数据包（Write Request Packet）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `req` | 表示存储器、I/O 或消息写入请求（Write Request）的结构地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | eSPI 控制器不支持原始数据包（Raw Packets），而是由控制器硬件直接处理低地址存储器事务（Low Memory Transactions）。 |
| `-EIO` | 一般输入／输出错误（I/O error），通过总线发送失败。 |


## 7.10\_原页交叉引用（Cross References）

- [eSPI 驱动后端 API（Driver Backend API）](../api_transport_control_topic_reference/P006_eSPI 驱动后端 API（Driver Backend API）.md)
- [eSPI 仿真接口（Emulation Interface）](../hardware/P486_eSPI总线仿真接口.md)
- [eSPI SAF](../api_radio_permission_topic_reference/P010_eSPI SAF API主题.md)
- [espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [espi_realtek_rts5912.h](../api_file_reference/P108_zephyr__drivers__espi__espi_realtek_rts5912.h_文件参考.md)
- [espi_evt_data_kbc](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md)
- [espi_evt_data_acpi](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md)
- [espi_evt_data_pvt](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md)
- [espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)
- [espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)
- [espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)
- [espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)
- [espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [signal](../api_file_reference/P391_____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考.md#a5d326f119f87d0facaa662520f8c322a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)
- [CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)
- [CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000008)
- [accept](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea"></a>
<a id="gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014"></a>
<a id="ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206"></a>
<a id="ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6"></a>
<a id="ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54"></a>
<a id="ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f"></a>
<a id="gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b"></a>
<a id="gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5"></a>
<a id="gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee"></a>
<a id="gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac"></a>
<a id="gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592"></a>
<a id="gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b"></a>
<a id="gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800"></a>
<a id="gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b"></a>
<a id="gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3"></a>
<a id="gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd"></a>
<a id="gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c"></a>
<a id="gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243"></a>
<a id="gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc"></a>
<a id="ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687"></a>
<a id="ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1"></a>
<a id="gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867"></a>
<a id="gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30"></a>
<a id="gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8"></a>
<a id="gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0"></a>
<a id="gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e"></a>
<a id="gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231"></a>
<a id="gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce"></a>
<a id="gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f"></a>
<a id="ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40"></a>
<a id="ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__espi__interface_html_ga7227c53d384eb0dc666361261f069f68"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="agroup__espi__interface_html_ga8d88e4e3893d610713195e5352ec2565"></a>
<a id="agroup__espi__interface_html_gabf5f0ea01ec8ed5345b2e119181c2313"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>

---

[上一章](P006_电话簿访问配置文件（Phone Book Access Profile，PBAP）.md) · [返回大纲](大纲.md) · [下一章](P008_外设时钟（Peripheral Clocks），编号 41–163.md)
