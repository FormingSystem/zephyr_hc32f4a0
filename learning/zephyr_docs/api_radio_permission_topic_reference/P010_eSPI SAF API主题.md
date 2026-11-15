---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-10
title: eSPI SAF API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_eSPI SAF API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI SAF 控制器接口；原文此处将 SAF 展开为串行附接 Flash（Serial Attached Flash）。

<a id="details"></a>

eSPI 串行附加闪存控制器接口（Serial Attached Flash，SAF）。引入版本（Since）：2.6；API 版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 10.1\_主题（Topics）

<a id="r_espi_5Fsaf_5Finterface_5Fbackend"></a>

相关声明：[eSPI SAF 驱动后端 API（Driver Backend API）](../api_network_time_topic_reference/P010_eSPI SAF 驱动后端 API（Driver Backend API）.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_espi_5Fsaf_5Fcfg"></a>

```c
struct espi_saf_cfg
```

相关声明：[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

eSPI从设备附属闪存（SAF）的配置参数。

<a id="r_espi_5Fsaf_5Fpacket"></a>

```c
struct espi_saf_packet
```

相关声明：[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

eSPI从设备附属闪存（SAF）事务的数据包格式。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_ga66bd7ad63051eefa407df554d5241d9e"></a>

```c
enum espi_taf_event { ESPI_TAF_EVENT_NO_REQUEST = 0 , ESPI_TAF_EVENT_HOST_REQUEST , ESPI_TAF_EVENT_EC0_REQUEST , ESPI_TAF_EVENT_MAX_REQUEST }
```

相关声明：[espi_taf_event](#ga66bd7ad63051eefa407df554d5241d9e)、[ESPI_TAF_EVENT_NO_REQUEST](#gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607)、[ESPI_TAF_EVENT_HOST_REQUEST](#gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74)、[ESPI_TAF_EVENT_EC0_REQUEST](#gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2)、[ESPI_TAF_EVENT_MAX_REQUEST](#gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1)。

eSPI TAF 通知类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_ga34b0f6336aec45016d97528767b09434"></a>

```c
int espi_saf_config (const struct device *dev, const struct espi_saf_cfg *cfg)
```

相关声明：[espi_saf_config](#ga34b0f6336aec45016d97528767b09434)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

配置 eSPI 控制器的运行方式。

<a id="r_ga273a9707f3ca501ed2dd3019cdeaa363"></a>

```c
int espi_saf_set_protection_regions (const struct device *dev, const struct espi_saf_protection *pr)
```

相关声明：[espi_saf_set_protection_regions](#ga273a9707f3ca501ed2dd3019cdeaa363)、[device](../device_reference/P002_设备对象结构.md)。

设置一个或多个从设备附接 Flash（Slave Attached Flash，SAF）保护区域。

<a id="r_gaafe30738c18a16b056ed8dcf8638eb84"></a>

```c
int espi_saf_activate (const struct device *dev)
```

相关声明：[espi_saf_activate](#gaafe30738c18a16b056ed8dcf8638eb84)、[device](../device_reference/P002_设备对象结构.md)。

激活 SAF 模块。

<a id="r_ga8b53a93559f0c67953e283f59107aa22"></a>

```c
bool espi_saf_get_channel_status (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[espi_saf_get_channel_status](#ga8b53a93559f0c67953e283f59107aa22)、[device](../device_reference/P002_设备对象结构.md)。

查询 SAF 是否就绪。

<a id="r_ga0f5017eac05f928e635fec8e5f877c7d"></a>

```c
int espi_saf_flash_read (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_read](#ga0f5017eac05f928e635fec8e5f877c7d)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的读取请求包。

<a id="r_ga104175f74019e58b8b7901f3dae245db"></a>

```c
int espi_saf_flash_write (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_write](#ga104175f74019e58b8b7901f3dae245db)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的写入请求包。

<a id="r_ga15855a2ac593b97dc1a3e83ac9eda300"></a>

```c
int espi_saf_flash_erase (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_erase](#ga15855a2ac593b97dc1a3e83ac9eda300)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的擦除请求包。

<a id="r_ga6c54d9274b1a8e883484bd892f606fd5"></a>

```c
int espi_saf_flash_unsuccess (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_unsuccess](#ga6c54d9274b1a8e883484bd892f606fd5)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应。

<a id="r_ga324283c28e6a33be112571621d1568e8"></a>

```c
static void espi_saf_init_callback (struct espi_callback *callback, espi_callback_handler_t handler, enum espi_bus_event evt_type)
```

相关声明：[espi_saf_init_callback](#ga324283c28e6a33be112571621d1568e8)、[espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)、[espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)。

回调模型（Callback model）。

<a id="r_gadb881f847082f713bb0159d1e474980a"></a>

```c
static int espi_saf_add_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_saf_add_callback](#gadb881f847082f713bb0159d1e474980a)、[device](../device_reference/P002_设备对象结构.md)。

添加应用回调。

<a id="r_gaf987842bc7dad310c7270aed50086af9"></a>

```c
static int espi_saf_remove_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_saf_remove_callback](#gaf987842bc7dad310c7270aed50086af9)、[device](../device_reference/P002_设备对象结构.md)。

移除应用回调。

## 10.5\_详细说明（Detailed Documentation）

<a id="ga66bd7ad63051eefa407df554d5241d9e"></a>

### `espi_taf_event`

```c
enum espi_taf_event
```

```c
#include <zephyr/drivers/espi_saf.h>
```

eSPI TAF 通知类型。

原始示例（Example）：

```c
+----------------------------------------------------------------------+
|                                                                      |
|  eSPI host                           +-------------+                 |
|                      +-----------+   |    Power    |   +----------+  |
|                      |Out of band|   |  management |   |   GPIO   |  |
|   ------------       |processor  |   |  controller |   |  sources |  |
|                      +-----------+   +-------------+   +----------+  |
|                            |                |               |        |
|   ------------             |                |               |        |
|                            +--------+       +---------------+        |
|                                     |               |                |
|            -----+   +--------+   +----------+  +----v-----+          |
|                 |   |  LPC   |   | Tunneled |  | Tunneled |          |
|                 |   | bridge |   |  SMBus   |  |   GPIO   |          |
|                 |   +--------+   +----------+  +----------+          |
|                 |        |             |             |               |
|                 |        ------+       |             |               |
|                 |              |       |             |               |
|          +------v-----+    +---v-------v-------------v----+          |
|          | eSPI Flash |    |    eSPI protocol block       |          |
|          |   access   +--->+                              |          |
|          +------------+    +------------------------------+          |
|                                    |                                 |
|       -----------                  |                                 |
|                                    v                                 |
|               XXXXXXXXXXXXXXXXXXXXXXX                                |
|                XXXXXXXXXXXXXXXXXXXXX                                 |
|                 XXXXXXXXXXXXXXXXXXX                                  |
+----------------------------------------------------------------------+
                          |
                 +-----------------+
  ---------      |  |   |   |   |  |
                 |  |   |   |   |  |
  ---------      |  +   +   +   +  |    eSPI bus
                 | CH0 CH1 CH2 CH3 |    (logical channels)
                 |  +   +   +   +  |
                 |  |   |   |   |  |
                 +-----------------+
                          |
+-----------------------------------------------------------------------+
|  eSPI slave                                                           |
|                                                                       |
|       CH0         |     CH1      |      CH2      |    CH3             |
|   eSPI endpoint   |    VWIRE     |      OOB      |   Flash            |
+-----------------------------------------------------------------------+
   |                                 |
   v                                 |
 +---------+                         |
 |  Flash  |  Slave Attached Flash   |
 +---------+                         |
                                     |
```

eSPI TAF 通知事件详情指出触发回调的事件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESPI_TAF_EVENT_NO_REQUEST` | TAF 通用事件（Generic Event）。 |
| `ESPI_TAF_EVENT_HOST_REQUEST` | TAF 闪存访问请求（Flash Access Request）来自主机 eSPI 控制器。 |
| `ESPI_TAF_EVENT_EC0_REQUEST` | TAF 闪存访问请求（Flash Access Request）来自嵌入式控制器固件门户 0（EC Firmware Portal 0）。 |
| `ESPI_TAF_EVENT_MAX_REQUEST` | 最大请求（Maximum Request） |

<a id="gaafe30738c18a16b056ed8dcf8638eb84"></a>

### `espi_saf_activate()`

```c
int espi_saf_activate ( const struct device * dev)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

激活 SAF 模块。

此例程激活 SAF 模块，仅应在 SAF 配置完成且 eSPI 主设备已启用闪存通道（Flash Channel）后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 激活 SAF 失败时。 |

<a id="gadb881f847082f713bb0159d1e474980a"></a>

### `espi_saf_add_callback()`

```c
int espi_saf_add_callback ( const struct device * dev, struct espi_callback * callback )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi_saf.h>
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

<a id="ga34b0f6336aec45016d97528767b09434"></a>

### `espi_saf_config()`

```c
int espi_saf_config ( const struct device * dev, const struct espi_saf_cfg * cfg )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

配置 eSPI 控制器的运行方式。

此例程提供覆盖 eSPI 控制器能力（Capabilities）的通用接口。

若此 eSPI 控制器充当从设备（Slave），主设备在初始化时发送 GET_CONFIGURATION 命令，将发现这里设置的值。

若此 eSPI 控制器充当主设备（Master），则使用这些值确定与 eSPI 从设备共同支持的最低能力，再通过 SET_CONFIGURATION 命令发送。

原始示例（Example）：

```c
+--------+   +---------+     +------+          +---------+   +---------+
|  eSPI  |   |  eSPI   |     | eSPI |          |  eSPI   |   |  eSPI   |
|  slave |   | driver  |     |  bus |          |  driver |   |  host   |
+--------+   +---------+     +------+          +---------+   +---------+
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
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | eSPI 从设备不支持此能力（Capability）。 |

<a id="ga15855a2ac593b97dc1a3e83ac9eda300"></a>

### `espi_saf_flash_erase()`

```c
int espi_saf_flash_erase ( const struct device * dev, struct espi_saf_packet * pckt )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 的擦除请求包。

此例程提供请求擦除 eSPI 主设备与从设备之间共享闪存组件的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存擦除事务（Erase Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被主设备禁用。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），向主设备发出的请求失败。 |

<a id="ga0f5017eac05f928e635fec8e5f877c7d"></a>

### `espi_saf_flash_read()`

```c
int espi_saf_flash_read ( const struct device * dev, struct espi_saf_packet * pckt )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 的读取请求包。

此例程提供请求读取 eSPI 主设备与从设备之间共享闪存组件的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存读取事务（Read Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被主设备禁用。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），向主设备发出的请求失败。 |

<a id="ga6c54d9274b1a8e883484bd892f606fd5"></a>

### `espi_saf_flash_unsuccess()`

```c
int espi_saf_flash_unsuccess ( const struct device * dev, struct espi_saf_packet * pckt )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应。

此例程提供响应接口，指示事务无效，并从目标端向控制器返回失败完成状态（Unsuccessful Completion）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存事务（Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被主设备禁用。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），向主设备发出的请求失败。 |

<a id="ga104175f74019e58b8b7901f3dae245db"></a>

### `espi_saf_flash_write()`

```c
int espi_saf_flash_write ( const struct device * dev, struct espi_saf_packet * pckt )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 的写入请求包。

此例程提供请求写入 eSPI 主设备与从设备之间共享闪存组件的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pckt` | 闪存写入事务（Write Flash Transaction）描述的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持 eSPI 闪存逻辑通道事务（Flash Logical Channel Transactions）。 |
| `-EBUSY` | eSPI 闪存通道（Flash Channel）未就绪，或已被主设备禁用。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），向主设备发出的请求失败。 |

<a id="ga8b53a93559f0c67953e283f59107aa22"></a>

### `espi_saf_get_channel_status()`

```c
bool espi_saf_get_channel_status ( const struct device * dev)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

查询 SAF 是否就绪。

此例程允许在使用前检查 SAF 是否就绪（Ready）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | eSPI SAF 已就绪时。 |
| `false` | 其他情况。 |

<a id="ga324283c28e6a33be112571621d1568e8"></a>

### `espi_saf_init_callback()`

```c
void espi_saf_init_callback ( struct espi_callback * callback, espi_callback_handler_t handler, enum espi_bus_event evt_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi_saf.h>
```

回调模型（Callback model）。

原始示例（Example）：

```c
+-------+                  +-------------+   +------+     +---------+
|  App  |                  | eSPI driver |   |  HW  |     |eSPI Host|
+---+---+                  +-------+-----+   +---+--+     +----+----+
    |                              |             |             |
    |   espi_init_callback         |             |             |
    +----------------------------> |             |             |
    |   espi_add_callback          |             |
    +----------------------------->+             |
    |                              |             |  eSPI reset |  eSPI host
    |                              |    IRQ      +<------------+  resets the
    |                              | <-----------+             |  bus
    |                              |             |             |
    |                              | Processed   |             |
    |                              | within the  |             |
    |                              | driver      |             |
    |                              |             |             |

    |                              |             |  VW CH ready|  eSPI host
    |                              |    IRQ      +<------------+  enables VW
    |                              | <-----------+             |  channel
    |                              |             |             |
    |                              | Processed   |             |
    |                              | within the  |             |
    |                              | driver      |             |
    |                              |             |             |
    |                              |             | Memory I/O  |  Peripheral
    |                              |             <-------------+  event
    |                              +<------------+             |
    +<-----------------------------+ callback    |             |
    | Report peripheral event      |             |             |
    | and data for the event       |             |             |
    |                              |             |             |
    |                              |             | SLP_S5      |  eSPI host
    |                              |             <-------------+  send VWire
    |                              +<------------+             |
    +<-----------------------------+ callback    |             |
    | App enables/configures       |             |             |
    | discrete regulator           |             |             |
    |                              |             |             |
    |   espi_send_vwire_signal     |             |             |
    +------------------------------>------------>|------------>|
    |                              |             |             |
    |                              |             | HOST_RST    |  eSPI host
    |                              |             <-------------+  send VWire
    |                              +<------------+             |
    +<-----------------------------+ callback    |             |
    | App reset host-related       |             |             |
    | data structures              |             |             |
    |                              |             |             |
    |                              |             |   C10       |  eSPI host
    |                              |             +<------------+  send VWire
    |                              <-------------+             |
    <------------------------------+             |             |
    | App executes                 |             |             |
    + power mgmt policy            |             |             |
```

正确初始化 struct espi_callback 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 有效的应用回调结构体指针（Callback Structure Pointer）。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `evt_type` | 指出与处理函数相关的 eSPI 事件；对于 VWIRE_RECEIVED 事件，数据表示新置为有效的电平。 |

<a id="gaf987842bc7dad310c7270aed50086af9"></a>

### `espi_saf_remove_callback()`

```c
int espi_saf_remove_callback ( const struct device * dev, struct espi_callback * callback )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/espi_saf.h>
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

<a id="ga273a9707f3ca501ed2dd3019cdeaa363"></a>

### `espi_saf_set_protection_regions()`

```c
int espi_saf_set_protection_regions ( const struct device * dev, const struct espi_saf_protection * pr )
```

```c
#include <zephyr/drivers/espi_saf.h>
```

设置一个或多个从设备附接 Flash（Slave Attached Flash，SAF）保护区域。

此例程提供覆盖 SAF 控制器默认闪存保护区域（Flash Protection Regions）的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pr` | 指向 SAF 保护区域结构体（Protection Region Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | eSPI 从设备不支持此能力（Capability）。 |


## 10.6\_原页交叉引用（Cross References）

- [eSPI SAF 驱动后端 API（Driver Backend API）](../api_network_time_topic_reference/P010_eSPI SAF 驱动后端 API（Driver Backend API）.md)
- [espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)
- [espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [zephyr/drivers/espi_saf.h](../peripheral_bus_storage_header_reference/P005_zephyr__drivers__espi_saf.h_头文件参考.md)
- [espi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7227c53d384eb0dc666361261f069f68)
- [accept](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [espi_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8d88e4e3893d610713195e5352ec2565)
- [espi_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gabf5f0ea01ec8ed5345b2e119181c2313)
- [send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607"></a>
<a id="gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74"></a>
<a id="gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2"></a>
<a id="gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__espi__interface_html_ga7227c53d384eb0dc666361261f069f68"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="agroup__espi__interface_html_ga8d88e4e3893d610713195e5352ec2565"></a>
<a id="agroup__espi__interface_html_gabf5f0ea01ec8ed5345b2e119181c2313"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>

---

[上一章](P009_DNS服务发现（Service Discovery）。.md) · [返回大纲](大纲.md) · [下一章](P011_HTTP请求方法（Request Methods）。.md)
