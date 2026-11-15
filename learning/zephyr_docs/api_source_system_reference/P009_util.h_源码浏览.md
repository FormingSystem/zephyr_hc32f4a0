---
id: learning.zephyr-docs.api-source-system-reference.page-9
title: util.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_util.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="foldopen00335"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00453"></a>
<a id="l00454"></a>

```c
/*
 * Copyright 2024,2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_UTIL_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_UTIL_H_


#define SCMI_PROTOCOL_NAME(proto) CONCAT(scmi_protocol_, proto)

#ifdef CONFIG_ARM_SCMI_MAILBOX_TRANSPORT
#define DT_SCMI_TRANSPORT_COMPATIBLE arm_scmi
#elif CONFIG_ARM_SCMI_SMC_TRANSPORT
#define DT_SCMI_TRANSPORT_COMPATIBLE arm_scmi_smc
#else
#error "Transport needs to define COMPATIBLE macro"
#endif

#define DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id) \
        DT_NODE_HAS_COMPAT(node_id, DT_SCMI_TRANSPORT_COMPATIBLE)

#define DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id)                                  \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id),                   \
                    (SCMI_PROTOCOL_BASE),                                       \
                    (DT_REG_ADDR_RAW(node_id)))

#ifdef CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS

#ifdef CONFIG_ARM_SCMI_MAILBOX_TRANSPORT
#define DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, idx)\
        DT_PROP_HAS_IDX(node_id, shmem, idx)
#elif CONFIG_ARM_SCMI_SMC_TRANSPORT
#define DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, idx)          \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id),   \
                    (DT_PROP_HAS_IDX(node_id, shmem, idx)),     \
                    (0))
#else
#error "Transport with static channels needs to define HAS_CHAN macro"
#endif

/* builds the symbol name of the static channel for a (proto, idx) pair */
#define SCMI_TRANSPORT_CHAN_NAME(proto, idx) CONCAT(scmi_channel_, proto, _, idx)


/*
 * Declare a TX SCMI channel.
 *
 * Given a @p node_id for a protocol, this macro declares the SCMI
 * TX channel statically bound to said protocol via the "extern"
 * qualifier. This is useful when the transport layer driver
 * supports static channels since all channel structures are
 * defined inside the transport layer driver. Internal helper used
 * by DT_SCMI_TRANSPORT_CHANNELS_DECLARE(); not meant to be used directly.
 *
 * @param node_id Protocol node identifier
 */
#define DT_SCMI_TRANSPORT_TX_CHAN_DECLARE(node_id)                              \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 0),               \
                    (extern struct scmi_channel                                 \
                     SCMI_TRANSPORT_CHAN_NAME(                                  \
                        DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id), 0);),           \
                    (extern struct scmi_channel                                 \
                     SCMI_TRANSPORT_CHAN_NAME(SCMI_PROTOCOL_BASE, 0);))         \


#define DT_SCMI_TRANSPORT_RX_CHAN_DECLARE_BASE_RAW(node_id)                             \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 1),                       \
                    (extern struct scmi_channel                                         \
                     SCMI_TRANSPORT_CHAN_NAME(SCMI_PROTOCOL_BASE, 1);),                 \
                    ())

#define DT_SCMI_TRANSPORT_RX_CHAN_DECLARE_BASE(node_id)                                 \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id),                           \
                    (DT_SCMI_TRANSPORT_RX_CHAN_DECLARE_BASE_RAW(node_id)),              \
                    (DT_SCMI_TRANSPORT_RX_CHAN_DECLARE_BASE_RAW(DT_PARENT(node_id))))   \

#define DT_SCMI_TRANSPORT_RX_CHAN_DECLARE(node_id)                                      \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 1),                       \
                    (extern struct scmi_channel                                         \
                     SCMI_TRANSPORT_CHAN_NAME(DT_REG_ADDR_RAW(node_id), 1);),           \
                    (DT_SCMI_TRANSPORT_RX_CHAN_DECLARE_BASE(node_id)))

#define DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)                             \
        DT_SCMI_TRANSPORT_TX_CHAN_DECLARE(node_id)                              \
        DT_SCMI_TRANSPORT_RX_CHAN_DECLARE(node_id)                              \

#define DT_INST_SCMI_TRANSPORT_CHANNELS_DECLARE(inst)                           \
        DT_SCMI_TRANSPORT_CHANNELS_DECLARE(DT_INST(inst, DT_DRV_COMPAT))

#define DT_SCMI_TRANSPORT_TX_CHAN(node_id)                                      \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 0),               \
                    (&SCMI_TRANSPORT_CHAN_NAME(                                 \
                        DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id), 0)),            \
                    (&SCMI_TRANSPORT_CHAN_NAME(SCMI_PROTOCOL_BASE, 0)))

#define DT_SCMI_TRANSPORT_RX_CHAN_BASE_RAW(node_id)                             \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 1),               \
                    (&SCMI_TRANSPORT_CHAN_NAME(SCMI_PROTOCOL_BASE, 1)),         \
                    (NULL))

#define DT_SCMI_TRANSPORT_RX_CHAN_BASE(node_id)                                 \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_IS_BASE(node_id),                   \
                    (DT_SCMI_TRANSPORT_RX_CHAN_BASE_RAW(node_id)),              \
                    (DT_SCMI_TRANSPORT_RX_CHAN_BASE_RAW(DT_PARENT(node_id))))

#define DT_SCMI_TRANSPORT_RX_CHAN(node_id)                                      \
        COND_CODE_1(DT_SCMI_TRANSPORT_PROTO_HAS_CHAN(node_id, 1),               \
                    (&SCMI_TRANSPORT_CHAN_NAME(DT_REG_ADDR_RAW(node_id), 1)),   \
                    (DT_SCMI_TRANSPORT_RX_CHAN_BASE(node_id)))


#define DT_SCMI_TRANSPORT_CHAN_DEFINE(node_id, idx, proto, pdata)               \
        struct scmi_channel SCMI_TRANSPORT_CHAN_NAME(proto, idx) =              \
        {                                                                       \
                .data = pdata,                                                  \
        }


/*
 * Define an SCMI protocol's data.
 *
 * Each SCMI protocol is identified by a struct scmi_protocol
 * placed in a linker section called scmi_protocol. Each protocol
 * driver is required to use this macro for "registration". Using
 * this macro directly is highly discouraged and users should opt
 * for macros such as DT_SCMI_PROTOCOL_DEFINE_NODEV() or
 * DT_SCMI_PROTOCOL_DEFINE(), which also takes care of the static
 * channel declaration (if applicable).
 *
 * @param node_id Protocol node identifier
 * @param proto Protocol ID in decimal format
 * @param pdata Protocol private data
 * @param version_val Protocol version supported by the driver
 * @param pevents Protocol registered events
 */
#define DT_SCMI_PROTOCOL_DATA_DEFINE(node_id, proto, pdata, version_val, pevents)       \
        STRUCT_SECTION_ITERABLE(scmi_protocol, SCMI_PROTOCOL_NAME(proto)) =             \
        {                                                                               \
                .id = proto,                                                            \
                .tx = DT_SCMI_TRANSPORT_TX_CHAN(node_id),                               \
                .rx = DT_SCMI_TRANSPORT_RX_CHAN(node_id),                               \
                .data = pdata,                                                          \
                .version = version_val,                                                 \
                .events = pevents                                                       \
        }

#else /* CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS */

/* no-op variant used when the transport does not support static channels */
#define DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)

/* variant used when the transport does not support static channels */
#define DT_SCMI_PROTOCOL_DATA_DEFINE(node_id, proto, pdata)                     \
        STRUCT_SECTION_ITERABLE(scmi_protocol, SCMI_PROTOCOL_NAME(proto)) =     \
        {                                                                       \
                .id = proto,                                                    \
                .data = pdata,                                                  \
        }

#endif /* CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS */

#define DT_INST_SCMI_TRANSPORT_DEFINE(inst, pm, data, config, level, prio, api) \
        DEVICE_DT_INST_DEFINE(inst, &scmi_core_transport_init,                  \
                              pm, data, config, level, prio, api)

#define DT_SCMI_PROTOCOL_DEFINE(node_id, init_fn, pm, data, config,             \
                                level, prio, api, version_val, events)          \
        DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)                             \
        DT_SCMI_PROTOCOL_DATA_DEFINE(node_id,                                   \
                                     DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id),    \
                                     data, version_val, events);                \
        DEVICE_DT_DEFINE(node_id, init_fn, pm,                                  \
                         &SCMI_PROTOCOL_NAME(                                   \
                                DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id)),        \
                         config, level, prio, api)

#define DT_INST_SCMI_PROTOCOL_DEFINE(inst, init_fn, pm, data, config,           \
                                     level, prio, api, version, events)         \
        DT_SCMI_PROTOCOL_DEFINE(DT_INST(inst, DT_DRV_COMPAT), init_fn, pm,      \
                                data, config, level, prio, api, version, events)

#define DT_SCMI_PROTOCOL_DEFINE_NODEV(node_id, data, version, events)           \
        DT_SCMI_TRANSPORT_CHANNELS_DECLARE(node_id)                             \
        DT_SCMI_PROTOCOL_DATA_DEFINE(node_id,                                   \
                                     DT_SCMI_TRANSPORT_PROTOCOL_ID(node_id),    \
                                     data, version, events)

#define SCMI_FIELD_MAKE(x, mask, shift)\
        (((uint32_t)(x) & (mask)) << (shift))

#define SCMI_PROTOCOL_BASE 16
#define SCMI_PROTOCOL_POWER_DOMAIN 17
#define SCMI_PROTOCOL_SYSTEM 18
#define SCMI_PROTOCOL_PERF 19
#define SCMI_PROTOCOL_CLOCK 20
#define SCMI_PROTOCOL_SENSOR 21
#define SCMI_PROTOCOL_RESET_DOMAIN 22
#define SCMI_PROTOCOL_VOLTAGE_DOMAIN 23
#define SCMI_PROTOCOL_PCAP_MONITOR 24
#define SCMI_PROTOCOL_PINCTRL 25


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_UTIL_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024,2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 120 行

为 `(proto, idx)` 组合构造静态通道符号名称（Static Channel Symbol Name）。

### 注释 3：原第 126 行

声明一个 SCMI 发送通道（TX Channel）。

给定协议的 `node_id`，本宏通过 `extern` 限定符声明与该协议静态绑定的 SCMI 发送通道。当传输层驱动（Transport Layer Driver）支持静态通道（Static Channels）时，这很有用，因为所有通道结构体均在传输层驱动内部定义。本宏是 `DT_SCMI_TRANSPORT_CHANNELS_DECLARE()` 使用的内部辅助宏（Internal Helper），不供直接使用。

参数（`@param`）`node_id`：协议节点标识（Protocol Node Identifier）。

### 注释 4：原第 277 行

定义 SCMI 协议的数据（Protocol Data）。

每个 SCMI 协议由放在名为 `scmi_protocol` 的链接器区段（Linker Section）中的 `struct scmi_protocol` 标识。每个协议驱动都必须使用本宏进行“注册”（Registration）。强烈不建议直接使用它；应选择 `DT_SCMI_PROTOCOL_DEFINE_NODEV()` 或 `DT_SCMI_PROTOCOL_DEFINE()` 等宏，它们也会在适用时处理静态通道声明（Static Channel Declaration）。

- 参数 `node_id`：协议节点标识（Protocol Node Identifier）。
- 参数 `proto`：十进制格式的协议标识（Protocol ID）。
- 参数 `pdata`：协议私有数据（Protocol Private Data）。
- 参数 `version_val`：驱动支持的协议版本（Protocol Version）。
- 参数 `pevents`：协议已注册的事件（Registered Events）。

### 注释 5：原第 306 行

条件编译配置（Configuration）标记：`CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`。

### 注释 6：原第 309 行

传输层（Transport）不支持静态通道（Static Channels）时使用的空操作变体（No-Op Variant）。

### 注释 7：原第 312 行

传输层（Transport）不支持静态通道（Static Channels）时使用的变体（Variant）。

### 注释 8：原第 321 行

条件编译配置（Configuration）标记：`CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`。

### 注释 9：原第 454 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_UTIL_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html)

---

[上一章](P008_digilent-pmod.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_dsa_core.h_源码浏览.md)
