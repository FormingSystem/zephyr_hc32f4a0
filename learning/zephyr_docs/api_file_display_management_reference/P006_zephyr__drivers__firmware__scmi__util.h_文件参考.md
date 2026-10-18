---
id: learning.zephyr-docs.api-file-display-management-reference.page-6
title: zephyr__drivers__firmware__scmi__util.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_util.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）工具宏（Utility Macros）的头文件。

查看此文件的源码。

<a id="details"></a>

系统控制与管理接口（SCMI）工具宏头文件。包含多种辅助宏，以及用于协议和传输“注册”（Registration）的宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_gaf302a6f14883fa949e87a6784bf965fa"></a>

```c
#define SCMI_PROTOCOL_NAME(proto)
```

相关声明：[SCMI_PROTOCOL_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaf302a6f14883fa949e87a6784bf965fa)。

根据协议 ID 构造协议名称（Protocol Name）。

<a id="r_ga93c77ce312d15ebc16e1cbeccff0f81d"></a>

```c
#define DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id)
```

相关声明：[DT_SCMI_TRANSPORT_PROTO_IS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga93c77ce312d15ebc16e1cbeccff0f81d)。

检查节点是否为基础 SCMI 传输节点（Base Transport Node）。

<a id="r_gaa5beb90cd8a9690ae5117df4b71d8917"></a>

```c
#define DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id)
```

相关声明：[DT_SCMI_TRANSPORT_PROTOCOL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaa5beb90cd8a9690ae5117df4b71d8917)。

从协议设备树节点（Protocol DT Node）获取协议 ID。

<a id="r_gaff1d7e88df451d043dc2e4e9d39288b3"></a>

```c
#define DT_INST_SCMI_TRANSPORT_DEFINE(inst, pm, data, config, level, prio, api)
```

相关声明：[DT_INST_SCMI_TRANSPORT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaff1d7e88df451d043dc2e4e9d39288b3)。

定义 SCMI 传输驱动（Transport Driver）。

<a id="r_gafe18d9f03ff8cbab0c61f1f001cdc1f1"></a>

```c
#define DT_SCMI_PROTOCOL_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, version_val, events)
```

相关声明：[DT_SCMI_PROTOCOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gafe18d9f03ff8cbab0c61f1f001cdc1f1)。

定义 SCMI 协议（Protocol）。

<a id="r_gad739a9de3bce089d7185c8cb35bd0b17"></a>

```c
#define DT_INST_SCMI_PROTOCOL_DEFINE(inst, init_fn, pm, data, config, level, prio, api, version, events)
```

相关声明：[DT_INST_SCMI_PROTOCOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gad739a9de3bce089d7185c8cb35bd0b17)。

与 `DT_SCMI_PROTOCOL_DEFINE()` 相同，但使用与 `DT_DRV_COMPAT` 兼容的实例（Instance），而非节点标识符。

<a id="r_ga346cdb9fe0818d6fe214e4866da646c8"></a>

```c
#define DT_SCMI_PROTOCOL_DEFINE_NODEV(node_id, data, version, events)
```

相关声明：[DT_SCMI_PROTOCOL_DEFINE_NODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga346cdb9fe0818d6fe214e4866da646c8)。

定义不带设备的 SCMI 协议（Protocol）。

<a id="r_ga21b369f9fa6d1a965ece4a589df88581"></a>

```c
#define SCMI_FIELD_MAKE(x, mask, shift)
```

相关声明：[SCMI_FIELD_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga21b369f9fa6d1a965ece4a589df88581)。

创建 SCMI 消息字段（Message Field）。

<a id="r_gaa7d5e12c8733162b93f2131fae0b9ff2"></a>

```c
#define SCMI_PROTOCOL_BASE 16
```

相关声明：[SCMI_PROTOCOL_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaa7d5e12c8733162b93f2131fae0b9ff2)。

SCMI 协议 ID（Protocol IDs）。

<a id="r_ga7434da13fae02cd2e32b148c77258564"></a>

```c
#define SCMI_PROTOCOL_POWER_DOMAIN 17
```

相关声明：[SCMI_PROTOCOL_POWER_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga7434da13fae02cd2e32b148c77258564)。

电源域管理协议（Power Domain Management Protocol）。

<a id="r_gab54b9be92cad1d9e35c20ea578daff14"></a>

```c
#define SCMI_PROTOCOL_SYSTEM 18
```

相关声明：[SCMI_PROTOCOL_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gab54b9be92cad1d9e35c20ea578daff14)。

系统电源管理协议（System Power Management Protocol）。

<a id="r_ga516870afb06683cc717cd24f5ac70065"></a>

```c
#define SCMI_PROTOCOL_PERF 19
```

相关声明：[SCMI_PROTOCOL_PERF](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga516870afb06683cc717cd24f5ac70065)。

性能域管理协议（Performance Domain Management Protocol）。

<a id="r_ga69c4e6bc3b3a76fa86a4f25cfb0d9905"></a>

```c
#define SCMI_PROTOCOL_CLOCK 20
```

相关声明：[SCMI_PROTOCOL_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga69c4e6bc3b3a76fa86a4f25cfb0d9905)。

时钟管理协议（Clock Management Protocol）。

<a id="r_ga50bd05b33b2b4915bd8e784542320d74"></a>

```c
#define SCMI_PROTOCOL_SENSOR 21
```

相关声明：[SCMI_PROTOCOL_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga50bd05b33b2b4915bd8e784542320d74)。

传感器管理协议（Sensor Management Protocol）。

<a id="r_gab15815aabeb7f45670ec346144653f0e"></a>

```c
#define SCMI_PROTOCOL_RESET_DOMAIN 22
```

相关声明：[SCMI_PROTOCOL_RESET_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gab15815aabeb7f45670ec346144653f0e)。

复位域管理协议（Reset Domain Management Protocol）。

<a id="r_gae8f54c2faae8340a25ddfb13789c7797"></a>

```c
#define SCMI_PROTOCOL_VOLTAGE_DOMAIN 23
```

相关声明：[SCMI_PROTOCOL_VOLTAGE_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gae8f54c2faae8340a25ddfb13789c7797)。

电压域管理协议（Voltage Domain Management Protocol）。

<a id="r_ga4c6b58ea0571f9ef6bb2af29e23b0df8"></a>

```c
#define SCMI_PROTOCOL_PCAP_MONITOR 24
```

相关声明：[SCMI_PROTOCOL_PCAP_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga4c6b58ea0571f9ef6bb2af29e23b0df8)。

功率上限控制与监测协议（Power Capping and Monitoring Protocol）。

<a id="r_ga48e1ebf3dbc53685127bccccc50977cb"></a>

```c
#define SCMI_PROTOCOL_PINCTRL 25
```

相关声明：[SCMI_PROTOCOL_PINCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga48e1ebf3dbc53685127bccccc50977cb)。

引脚控制协议（Pin Control Protocol）。


## 6.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_system_reference/P009_util.h_源码浏览.md)
- [SCMI_PROTOCOL_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaf302a6f14883fa949e87a6784bf965fa)
- [DT_SCMI_TRANSPORT_PROTO_IS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga93c77ce312d15ebc16e1cbeccff0f81d)
- [DT_SCMI_TRANSPORT_PROTOCOL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaa5beb90cd8a9690ae5117df4b71d8917)
- [DT_INST_SCMI_TRANSPORT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaff1d7e88df451d043dc2e4e9d39288b3)
- [DT_SCMI_PROTOCOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gafe18d9f03ff8cbab0c61f1f001cdc1f1)
- [DT_INST_SCMI_PROTOCOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gad739a9de3bce089d7185c8cb35bd0b17)
- [DT_SCMI_PROTOCOL_DEFINE_NODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga346cdb9fe0818d6fe214e4866da646c8)
- [SCMI_FIELD_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga21b369f9fa6d1a965ece4a589df88581)
- [SCMI_PROTOCOL_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gaa7d5e12c8733162b93f2131fae0b9ff2)
- [SCMI_PROTOCOL_POWER_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga7434da13fae02cd2e32b148c77258564)
- [SCMI_PROTOCOL_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gab54b9be92cad1d9e35c20ea578daff14)
- [SCMI_PROTOCOL_PERF](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga516870afb06683cc717cd24f5ac70065)
- [SCMI_PROTOCOL_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga69c4e6bc3b3a76fa86a4f25cfb0d9905)
- [SCMI_PROTOCOL_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga50bd05b33b2b4915bd8e784542320d74)
- [SCMI_PROTOCOL_RESET_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gab15815aabeb7f45670ec346144653f0e)
- [SCMI_PROTOCOL_VOLTAGE_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#gae8f54c2faae8340a25ddfb13789c7797)
- [SCMI_PROTOCOL_PCAP_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga4c6b58ea0571f9ef6bb2af29e23b0df8)
- [SCMI_PROTOCOL_PINCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__util.html#ga48e1ebf3dbc53685127bccccc50977cb)

<a id="header-details"></a>

---

[上一章](P005_zephyr__bluetooth__data.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__mipi_dsi.h_文件参考.md)
