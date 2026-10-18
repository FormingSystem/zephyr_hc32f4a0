---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-18
title: 实用工具（Utilities）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_实用工具（Utilities）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCMI 驱动的辅助宏和工具。

<a id="details"></a>

SCMI 驱动的辅助宏和工具。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_util_2Eh"></a>

```c
file util.h
```

相关声明：[util.h](../api_file_display_management_reference/P006_zephyr__drivers__firmware__scmi__util.h_文件参考.md)。

系统控制与管理接口（SCMI）工具宏（Utility Macros）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_gaf302a6f14883fa949e87a6784bf965fa"></a>

```c
#define SCMI_PROTOCOL_NAME(proto)
```

相关声明：[SCMI_PROTOCOL_NAME](#gaf302a6f14883fa949e87a6784bf965fa)。

根据协议 ID 构造协议名称（Protocol Name）。

<a id="r_ga93c77ce312d15ebc16e1cbeccff0f81d"></a>

```c
#define DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id)
```

相关声明：[DT_SCMI_TRANSPORT_PROTO_IS_BASE](#ga93c77ce312d15ebc16e1cbeccff0f81d)。

检查节点是否为基础 SCMI 传输节点（Base Transport Node）。

<a id="r_gaa5beb90cd8a9690ae5117df4b71d8917"></a>

```c
#define DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id)
```

相关声明：[DT_SCMI_TRANSPORT_PROTOCOL_ID](#gaa5beb90cd8a9690ae5117df4b71d8917)。

从协议设备树节点（Protocol DT Node）获取协议 ID。

<a id="r_gaff1d7e88df451d043dc2e4e9d39288b3"></a>

```c
#define DT_INST_SCMI_TRANSPORT_DEFINE(inst, pm, data, config, level, prio, api)
```

相关声明：[DT_INST_SCMI_TRANSPORT_DEFINE](#gaff1d7e88df451d043dc2e4e9d39288b3)。

定义 SCMI 传输驱动（Transport Driver）。

<a id="r_gafe18d9f03ff8cbab0c61f1f001cdc1f1"></a>

```c
#define DT_SCMI_PROTOCOL_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, version_val, events)
```

相关声明：[DT_SCMI_PROTOCOL_DEFINE](#gafe18d9f03ff8cbab0c61f1f001cdc1f1)。

定义 SCMI 协议（Protocol）。

<a id="r_gad739a9de3bce089d7185c8cb35bd0b17"></a>

```c
#define DT_INST_SCMI_PROTOCOL_DEFINE(inst, init_fn, pm, data, config, level, prio, api, version, events)
```

相关声明：[DT_INST_SCMI_PROTOCOL_DEFINE](#gad739a9de3bce089d7185c8cb35bd0b17)。

与 `DT_SCMI_PROTOCOL_DEFINE()` 相同，但使用与 `DT_DRV_COMPAT` 兼容的实例（Instance），而非节点标识符。

<a id="r_ga346cdb9fe0818d6fe214e4866da646c8"></a>

```c
#define DT_SCMI_PROTOCOL_DEFINE_NODEV(node_id, data, version, events)
```

相关声明：[DT_SCMI_PROTOCOL_DEFINE_NODEV](#ga346cdb9fe0818d6fe214e4866da646c8)。

定义不带设备的 SCMI 协议（Protocol）。

<a id="r_ga21b369f9fa6d1a965ece4a589df88581"></a>

```c
#define SCMI_FIELD_MAKE(x, mask, shift)
```

相关声明：[SCMI_FIELD_MAKE](#ga21b369f9fa6d1a965ece4a589df88581)。

创建 SCMI 消息字段（Message Field）。

<a id="r_gaa7d5e12c8733162b93f2131fae0b9ff2"></a>

```c
#define SCMI_PROTOCOL_BASE 16
```

相关声明：[SCMI_PROTOCOL_BASE](#gaa7d5e12c8733162b93f2131fae0b9ff2)。

SCMI 协议 ID（Protocol IDs）。

<a id="r_ga7434da13fae02cd2e32b148c77258564"></a>

```c
#define SCMI_PROTOCOL_POWER_DOMAIN 17
```

相关声明：[SCMI_PROTOCOL_POWER_DOMAIN](#ga7434da13fae02cd2e32b148c77258564)。

电源域管理协议（Power Domain Management Protocol）。

<a id="r_gab54b9be92cad1d9e35c20ea578daff14"></a>

```c
#define SCMI_PROTOCOL_SYSTEM 18
```

相关声明：[SCMI_PROTOCOL_SYSTEM](#gab54b9be92cad1d9e35c20ea578daff14)。

系统电源管理协议（System Power Management Protocol）。

<a id="r_ga516870afb06683cc717cd24f5ac70065"></a>

```c
#define SCMI_PROTOCOL_PERF 19
```

相关声明：[SCMI_PROTOCOL_PERF](#ga516870afb06683cc717cd24f5ac70065)。

性能域管理协议（Performance Domain Management Protocol）。

<a id="r_ga69c4e6bc3b3a76fa86a4f25cfb0d9905"></a>

```c
#define SCMI_PROTOCOL_CLOCK 20
```

相关声明：[SCMI_PROTOCOL_CLOCK](#ga69c4e6bc3b3a76fa86a4f25cfb0d9905)。

时钟管理协议（Clock Management Protocol）。

<a id="r_ga50bd05b33b2b4915bd8e784542320d74"></a>

```c
#define SCMI_PROTOCOL_SENSOR 21
```

相关声明：[SCMI_PROTOCOL_SENSOR](#ga50bd05b33b2b4915bd8e784542320d74)。

传感器管理协议（Sensor Management Protocol）。

<a id="r_gab15815aabeb7f45670ec346144653f0e"></a>

```c
#define SCMI_PROTOCOL_RESET_DOMAIN 22
```

相关声明：[SCMI_PROTOCOL_RESET_DOMAIN](#gab15815aabeb7f45670ec346144653f0e)。

复位域管理协议（Reset Domain Management Protocol）。

<a id="r_gae8f54c2faae8340a25ddfb13789c7797"></a>

```c
#define SCMI_PROTOCOL_VOLTAGE_DOMAIN 23
```

相关声明：[SCMI_PROTOCOL_VOLTAGE_DOMAIN](#gae8f54c2faae8340a25ddfb13789c7797)。

电压域管理协议（Voltage Domain Management Protocol）。

<a id="r_ga4c6b58ea0571f9ef6bb2af29e23b0df8"></a>

```c
#define SCMI_PROTOCOL_PCAP_MONITOR 24
```

相关声明：[SCMI_PROTOCOL_PCAP_MONITOR](#ga4c6b58ea0571f9ef6bb2af29e23b0df8)。

功率上限控制与监测协议（Power Capping and Monitoring Protocol）。

<a id="r_ga48e1ebf3dbc53685127bccccc50977cb"></a>

```c
#define SCMI_PROTOCOL_PINCTRL 25
```

相关声明：[SCMI_PROTOCOL_PINCTRL](#ga48e1ebf3dbc53685127bccccc50977cb)。

引脚控制协议（Pin Control Protocol）。

## 18.3\_详细说明（Detailed Documentation）

<a id="gad739a9de3bce089d7185c8cb35bd0b17"></a>

### `DT_INST_SCMI_PROTOCOL_DEFINE`

```c
#define DT_INST_SCMI_PROTOCOL_DEFINE ( inst, init_fn, pm, data, config, level, prio, api, version, events )
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
DT_SCMI_PROTOCOL_DEFINE(DT_INST(inst, DT_DRV_COMPAT), init_fn, pm,      \
                        data, config, level, prio, api, version, events)
```

与 `DT_SCMI_PROTOCOL_DEFINE()` 相同，但使用与 `DT_DRV_COMPAT` 兼容的实例（Instance），而非节点标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号。 |
| `init_fn` | 指向协议初始化函数（Initialization Function）的指针 |
| `api` | 指向协议子系统 API（Subsystem API）的指针 |
| `pm` | 指向协议电源管理资源（Power Management Resources）的指针 |
| `data` | 指向协议私有数据（Private Data）的指针 |
| `config` | 指向协议私有常量数据（Private Constant Data）的指针 |
| `level` | 协议初始化级别（Initialization Level） |
| `prio` | 协议在其初始化级别中的优先级（Priority） |
| `version` | 驱动支持的协议版本（Protocol Version） |

<a id="gaff1d7e88df451d043dc2e4e9d39288b3"></a>

### `DT_INST_SCMI_TRANSPORT_DEFINE`

```c
#define DT_INST_SCMI_TRANSPORT_DEFINE ( inst, pm, data, config, level, prio, api )
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
DEVICE_DT_INST_DEFINE(inst, &scmi_core_transport_init,                  \
                      pm, data, config, level, prio, api)
```

定义 SCMI 传输驱动（Transport Driver）。

这只是 DEVICE_DT_INST_DEFINE() 的封装，但必不可少：传输层驱动不允许把自己的 init() 函数放入初始化段（Init Section），而应放入 scmi_core_transport_init()，再由该函数调用传输层驱动的 init()。原因是 SCMI 核心需要在传输层驱动初始化期间执行通道绑定与设置（Channel Binding and Setup）。

<a id="gafe18d9f03ff8cbab0c61f1f001cdc1f1"></a>

### `DT_SCMI_PROTOCOL_DEFINE`

```c
#define DT_SCMI_PROTOCOL_DEFINE ( node_id, init_fn, pm, data, config, level, prio, api, version_val, events )
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)                             \
DT_SCMI_PROTOCOL_DATA_DEFINE(node_id,                                   \
                             DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id),    \
                             data, version_val, events);                \
DEVICE_DT_DEFINE(node_id, init_fn, pm,                                  \
                 &SCMI_PROTOCOL_NAME(                                   \
                        DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id)),        \
                 config, level, prio, api)
```

定义 SCMI 协议（Protocol）。

此宏完成三项重要工作：

- 定义 struct scmi_protocol，所有协议驱动都需要用它与 SCMI API 交互。
- 声明绑定到该协议的静态通道（Static Channels）；仅在传输层驱动支持静态通道时适用。
- 创建 struct device，并将其 data 字段设为新定义的 struct scmi_protocol。这是必需的，因为协议驱动同时需要使用 SCMI API 和子系统 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 协议节点标识符（Protocol Node Identifier） |
| `init_fn` | 指向协议初始化函数（Initialization Function）的指针 |
| `api` | 指向协议子系统 API（Subsystem API）的指针 |
| `pm` | 指向协议电源管理资源（Power Management Resources）的指针 |
| `data` | 指向协议私有数据（Private Data）的指针 |
| `config` | 指向协议私有常量数据（Private Constant Data）的指针 |
| `level` | 协议初始化级别（Initialization Level） |
| `prio` | 协议在其初始化级别中的优先级（Priority） |
| `version_val` | 驱动支持的协议版本（Protocol Version） |

<a id="ga346cdb9fe0818d6fe214e4866da646c8"></a>

### `DT_SCMI_PROTOCOL_DEFINE_NODEV`

```c
#define DT_SCMI_PROTOCOL_DEFINE_NODEV ( node_id, data, version, events )
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)                             \
DT_SCMI_PROTOCOL_DATA_DEFINE(node_id,                                   \
                             DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id),    \
                             data, version, events)
```

定义不带设备的 SCMI 协议（Protocol）。

DT_SCMI_PROTOCOL_DEFINE() 的变体，但不创建 struct device，也不在系统初始化期间调用初始化函数。适用于并不真正属于带有 API 的子系统的协议，例如 pinctrl。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 协议节点标识符（Protocol Node Identifier） |
| `data` | 协议私有数据。 |
| `version` | 驱动支持的协议版本（Protocol Version） |

<a id="ga93c77ce312d15ebc16e1cbeccff0f81d"></a>

### `DT_SCMI_TRANSPORT_PROTO_IS_BASE`

```c
#define DT_SCMI_TRANSPORT_PROTO_IS_BASE ( node_id)
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
DT_NODE_HAS_COMPAT(node_id, DT_SCMI_TRANSPORT_COMPATIBLE)
```

检查节点是否为基础 SCMI 传输节点（Base Transport Node）。

此宏验证节点的 compatible 字符串是否匹配当前传输层定义 DT_SCMI_TRANSPORT_COMPATIBLE，以判断给定 node_id 是否对应主 SCMI 传输层（Primary Transport Layer，即基础节点）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 协议节点标识符（Protocol Node Identifier） |

**返回（Returns）**：返回值（Returns）：节点为基础传输节点时返回 1，否则返回 0。

<a id="gaa5beb90cd8a9690ae5117df4b71d8917"></a>

### `DT_SCMI_TRANSPORT_PROTOCOL_ID`

```c
#define DT_SCMI_TRANSPORT_PROTOCOL_ID ( node_id)
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id),                   \
            (SCMI_PROTOCOL_BASE),                                       \
            (DT_REG_ADDR_RAW(node_id)))
```

从协议设备树节点（Protocol DT Node）获取协议 ID。

将设备树（DT）协议节点映射为对应协议 ID。基础协议（Base Protocol）与传输层共享同一个 DT 节点，因此需要特殊处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 协议节点标识符（Protocol Node Identifier） |

**返回（Returns）**：返回值（Returns）：协议 ID（Protocol ID）。

<a id="ga21b369f9fa6d1a965ece4a589df88581"></a>

### `SCMI_FIELD_MAKE`

```c
#define SCMI_FIELD_MAKE ( x, mask, shift )
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
(((uint32_t)(x) & (mask)) << (shift))
```

创建 SCMI 消息字段（Message Field）。

数据不一定编码在 SCMI 消息参数／返回值的前 x 位中。构建这些参数／返回值时，此宏可派上用场。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 待编码的值（Value） |
| `mask` | 与 x 按位与（Bitwise AND）的值 |
| `shift` | 掩码处理后的 x 的左移位数（Left Shift） |

**返回（Returns）**：返回值（Returns）：编码后的消息字段（Encoded Message Field）。

<a id="gaa7d5e12c8733162b93f2131fae0b9ff2"></a>

### `SCMI_PROTOCOL_BASE`

```c
#define SCMI_PROTOCOL_BASE 16
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

SCMI 协议 ID（Protocol IDs）。

每个 SCMI 协议由一个 ID 标识。这些 ID 必须使用十进制，因为可能用于构建协议名称和静态通道名称。基础协议（Base Protocol）。

<a id="ga69c4e6bc3b3a76fa86a4f25cfb0d9905"></a>

### `SCMI_PROTOCOL_CLOCK`

```c
#define SCMI_PROTOCOL_CLOCK 20
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

时钟管理协议（Clock Management Protocol）。

<a id="gaf302a6f14883fa949e87a6784bf965fa"></a>

### `SCMI_PROTOCOL_NAME`

```c
#define SCMI_PROTOCOL_NAME ( proto)
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

展开值（Value）：

```c
CONCAT(scmi_protocol_, proto)
```

根据协议 ID 构造协议名称（Protocol Name）。

给定协议 ID，此宏将 scmi_protocol_ 前缀与该 ID 拼接，构建协议名称（Protocol Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 十进制格式的协议 ID（Protocol ID） |

**返回（Returns）**：返回值（Returns）：协议名称（Protocol Name）。

<a id="ga4c6b58ea0571f9ef6bb2af29e23b0df8"></a>

### `SCMI_PROTOCOL_PCAP_MONITOR`

```c
#define SCMI_PROTOCOL_PCAP_MONITOR 24
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

功率上限控制与监测协议（Power Capping and Monitoring Protocol）。

<a id="ga516870afb06683cc717cd24f5ac70065"></a>

### `SCMI_PROTOCOL_PERF`

```c
#define SCMI_PROTOCOL_PERF 19
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

性能域管理协议（Performance Domain Management Protocol）。

<a id="ga48e1ebf3dbc53685127bccccc50977cb"></a>

### `SCMI_PROTOCOL_PINCTRL`

```c
#define SCMI_PROTOCOL_PINCTRL 25
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

引脚控制协议（Pin Control Protocol）。

<a id="ga7434da13fae02cd2e32b148c77258564"></a>

### `SCMI_PROTOCOL_POWER_DOMAIN`

```c
#define SCMI_PROTOCOL_POWER_DOMAIN 17
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

电源域管理协议（Power Domain Management Protocol）。

<a id="gab15815aabeb7f45670ec346144653f0e"></a>

### `SCMI_PROTOCOL_RESET_DOMAIN`

```c
#define SCMI_PROTOCOL_RESET_DOMAIN 22
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

复位域管理协议（Reset Domain Management Protocol）。

<a id="ga50bd05b33b2b4915bd8e784542320d74"></a>

### `SCMI_PROTOCOL_SENSOR`

```c
#define SCMI_PROTOCOL_SENSOR 21
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

传感器管理协议（Sensor Management Protocol）。

<a id="gab54b9be92cad1d9e35c20ea578daff14"></a>

### `SCMI_PROTOCOL_SYSTEM`

```c
#define SCMI_PROTOCOL_SYSTEM 18
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

系统电源管理协议（System Power Management Protocol）。

<a id="gae8f54c2faae8340a25ddfb13789c7797"></a>

### `SCMI_PROTOCOL_VOLTAGE_DOMAIN`

```c
#define SCMI_PROTOCOL_VOLTAGE_DOMAIN 23
```

```c
#include <zephyr/drivers/firmware/scmi/util.h>
```

电压域管理协议（Voltage Domain Management Protocol）。


## 18.4\_原页交叉引用（Cross References）

- [util.h](../api_file_display_management_reference/P006_zephyr__drivers__firmware__scmi__util.h_文件参考.md)
- [DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)
- [DEVICE_DT_INST_DEFINE](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [DT_NODE_HAS_COMPAT](../dt_identity_reference/P002_设备树存在性与状态宏.md#gad8912ba5db980713e72257472ded3ced)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_REG_ADDR_RAW](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga14ebfb75548e45279f3954a75a5f9ac1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [CONCAT](../util_reference/P001_通用工具公共接口.md#ga770b921e59b3151931ee939a1ecf450e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-id_html_gae199b930cb21ff38dab284a696093ead"></a>
<a id="agroup__scmi__util_html_gafe18d9f03ff8cbab0c61f1f001cdc1f1"></a>
<a id="agroup__device__model_html_gada5ba4aca9e0662ccebb2232c7256419"></a>
<a id="agroup__scmi__util_html_gaa5beb90cd8a9690ae5117df4b71d8917"></a>
<a id="agroup__scmi__util_html_gaf302a6f14883fa949e87a6784bf965fa"></a>
<a id="agroup__devicetree-generic-exist_html_gad8912ba5db980713e72257472ded3ced"></a>
<a id="agroup__devicetree-reg-prop_html_ga14ebfb75548e45279f3954a75a5f9ac1"></a>
<a id="agroup__scmi__util_html_ga93c77ce312d15ebc16e1cbeccff0f81d"></a>
<a id="agroup__scmi__util_html_gaa7d5e12c8733162b93f2131fae0b9ff2"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__sys-util_html_ga770b921e59b3151931ee939a1ecf450e"></a>

---

[上一章](P017_瑞昱（Realtek）RTS5912.md) · [返回大纲](大纲.md) · [下一章](P019_USB Type-C 电源路径控制器（Power Path Controller）.md)
