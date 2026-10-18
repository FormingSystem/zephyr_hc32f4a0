---
id: learning.zephyr-docs.network-core-model-reference.page-41
title: ieee802154_radio_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__radio__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_ieee802154\_radio\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__radio__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4驱动的接口API。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

IEEE 802.15.4驱动接口API。

说明（Note）：为保持向后兼容，此结构仍称为无线电API（Radio API），但更合适的名称是“IEEE 802.15.4驱动API”。典型驱动除第一层无线电/物理层（L1/PHY）特性外，在厂商硬件或固件提供卸载机会时，也实现第二层媒体访问控制（L2/MAC）特性。

第一层特性完全由驱动实现，且可能（MAY）是满足某些应用要求的必要条件。第二层特性默认应当（SHOULD）可选，只需在驱动维护者认为需要优化性能或精确时序时实现。驱动无关的L2层应当（SHOULD）为全部L2/MAC特性提供回退实现，即软件MAC（Soft MAC）；尤其是在源码树内多数现有驱动的厂商硬件/固件尚未实现这些特性时。如果驱动提供卸载能力，L2实现则必须（SHALL）把性能关键或资源密集任务委托给驱动。

全部驱动必须（SHALL）支持两种外部可观察的接口运行状态：“UP”和“DOWN”。驱动还可以（MAY）支持“TESTING”状态，参见continuous_carrier()。适用规则如下：

- 接口能够发送和接收数据包时视为“UP”，否则为“DOWN”。精确定义见RFC 2863第3.1.14节中的相应ifOperStatus值、net_if_oper_state，以及下面的continuous_carrier()例外。
- 接口处于“UP”时，即使活动接收窗口配置使接收器暂时禁用，仍视为“UP”。
- start()返回0或-EALREADY后，上层认为接口为“UP”；stop()返回0或-EALREADY后，上层认为接口为“DOWN”。
- 驱动必须（SHALL）阻塞start()/stop()调用，直到接口完整转换到新状态，例如接收器已经可用、正在进行的发送已经完成等。如果等待新状态不需要CPU参与，驱动应当（SHOULD）让调用线程让出执行权，即休眠（Sleep）。
- 驱动负责保证状态变化的原子性（Atomicity），必须（SHALL）实现适当同步，例如锁或原子标志。
- 接口处于“DOWN”时，驱动必须（SHALL）进入尽可能低的功耗状态。驱动可以（MAY）在达到该功耗状态前从stop()返回，即异步管理电源。
- 接口处于“UP”时，驱动应当（SHOULD）尽可能自主、异步地转入较低功耗状态。如果驱动声明支持定时接收/发送（Timed RX/TX），且上层配置了接收时隙（RX Slot），驱动必须（SHALL）立即异步转入尽可能低的功耗状态，直到接收时隙开始或需要发送已调度的数据包。
- 驱动不得（SHALL NOT）自行改变接口的“UP”/“DOWN”状态。接口初始必须（SHALL）为“DOWN”。
- 实现可选continuous_carrier()操作的驱动，在该操作返回0后被视为进入RFC 2863的“testing” ifOperStatus状态。此状态持续到调用start()或stop()为止。continuous_carrier()返回非零值时，上层认为此前状态保持不变。
- start()/stop()返回0和-EALREADY之外的值时，上层认为接口处于RFC 2863定义的“lowerLayerDown”状态。当前不支持RFC 2863的“dormant”、“unknown”和“notPresent” ifOperStatus状态。
- ed_scan()、cca()和tx()操作必须（SHALL）仅在“UP”状态受支持，在其他状态返回-ENETDOWN。更多细节见下方各函数的API文档。

> 译注：原文在上述状态说明中还列有孤立短句“The lowerLevelUp state.”，没有给出相应定义或规则；这里保留其状态名lowerLevelUp，不补写含义。

说明（Note）：对于支持定时接收/发送（Timed RX/TX）的设备，“UP”状态不等于“接收器已启用”。如果在调用start()之前配置接收窗口，即接收时隙（RX Slot，见IEEE802154_CONFIG_RX_SLOT），转入“UP”状态时不会启用接收器。在接口已处于“UP”时配置接收窗口，则会立即禁用接收器，直到配置的接收时刻到来。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_aa955462d8c6950dc4b5935973f4575d8"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#aa955462d8c6950dc4b5935973f4575d8)。

网络接口API（Network Interface API）。

<a id="r_a09a4b5df81822845f718952c6029442c"></a>

```c
enum ieee802154_hw_caps(* get_capabilities )(const struct device *dev)
```

相关声明：[ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)、[get_capabilities](#a09a4b5df81822845f718952c6029442c)、[device](../device_reference/P002_设备对象结构.md)。

获取设备驱动能力（Device Driver Capabilities）。

<a id="r_a2cbbd0e64fae28f748bb3e4d654a92bf"></a>

```c
int(* cca )(const struct device *dev)
```

相关声明：[cca](#a2cbbd0e64fae28f748bb3e4d654a92bf)、[device](../device_reference/P002_设备对象结构.md)。

空闲信道评估（Clear Channel Assessment）：检查信道活动。

<a id="r_a9ad27a2ff0a839dc5b9a4e6317cc59b1"></a>

```c
int(* set_channel )(const struct device *dev, uint16_t channel)
```

相关声明：[set_channel](#a9ad27a2ff0a839dc5b9a4e6317cc59b1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

设置当前信道（Current Channel）。

<a id="r_aa9502e0e014a8d05ffe235567e8c98f3"></a>

```c
int(* filter )(const struct device *dev, bool set, enum ieee802154_filter_type type, const struct ieee802154_filter *filter)
```

相关声明：[filter](#aa9502e0e014a8d05ffe235567e8c98f3)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ieee802154_filter_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa1971591e72866d0f3f0d4db2931e25a)、[ieee802154_filter](P017_ieee802154_filter_结构体.md)。

设置或取消PAN ID、扩展地址或短地址过滤器（Filters）。

<a id="r_aeeab6dfcde08af23357ea40f8af68f66"></a>

```c
int(* set_txpower )(const struct device *dev, int16_t dbm)
```

相关声明：[set_txpower](#aeeab6dfcde08af23357ea40f8af68f66)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)。

设置发送功率（TX Power），单位为dBm。

<a id="r_a70139acec22642c1fc09f2323c383fe6"></a>

```c
int(* tx )(const struct device *dev, enum ieee802154_tx_mode mode, struct net_pkt *pkt, struct net_buf *frag)
```

相关声明：[tx](#a70139acec22642c1fc09f2323c383fe6)、[device](../device_reference/P002_设备对象结构.md)、[ieee802154_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab2bee8752291e082cb277145cef1225d)、[net_pkt](P114_net_pkt_结构体.md)、[net_buf](P046_net_buf_结构体.md)。

将一个数据包片段（Packet Fragment）作为单帧发送。

<a id="r_a0e4d57dc3a53299ddedf2140e172103d"></a>

```c
int(* start )(const struct device *dev)
```

相关声明：[start](#a0e4d57dc3a53299ddedf2140e172103d)、[device](../device_reference/P002_设备对象结构.md)。

启动设备（Start the Device）。

<a id="r_a75cfcfe2b9e69c2e4af53f00c8294b36"></a>

```c
int(* stop )(const struct device *dev)
```

相关声明：[stop](#a75cfcfe2b9e69c2e4af53f00c8294b36)、[device](../device_reference/P002_设备对象结构.md)。

停止设备（Stop the Device）。

<a id="r_a9acaf4810bd5d3b026cc381bff301071"></a>

```c
int(* configure )(const struct device *dev, enum ieee802154_config_type type, const struct ieee802154_config *config)
```

相关声明：[configure](#a9acaf4810bd5d3b026cc381bff301071)、[device](../device_reference/P002_设备对象结构.md)、[ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)、[ieee802154_config](P014_ieee802154_config_结构体.md)。

设置或更新驱动配置（Driver Configuration）。

<a id="r_a01fc17f85f2be33877a9347f59a84c54"></a>

```c
int(* ed_scan )(const struct device *dev, uint16_t duration, energy_scan_done_cb_t done_cb)
```

相关声明：[ed_scan](#a01fc17f85f2be33877a9347f59a84c54)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[energy_scan_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8c9ab3cecefe641a25f003eb6d014fc5)。

执行能量检测扫描（Energy Detection Scan）。

<a id="r_a829a0d59fdcda5b6cb029ef1334a6b8b"></a>

```c
net_time_t(* get_time )(const struct device *dev)
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[get_time](#a829a0d59fdcda5b6cb029ef1334a6b8b)、[device](../device_reference/P002_设备对象结构.md)。

获取相对于此网络接口所表示的网络子系统本地运行时长时钟（Local Uptime Clock）的当前时间，单位为纳秒。

<a id="r_ae4a3ef40a5b8031c868d72ead163c97d"></a>

```c
uint8_t(* get_sch_acc )(const struct device *dev)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[get_sch_acc](#ae4a3ef40a5b8031c868d72ead163c97d)、[device](../device_reference/P002_设备对象结构.md)。

获取网络子系统本地时钟当前估计的最坏情况精度（Worst Case Accuracy），即相对于标称频率的最大正负偏差；调度延迟接收或发送无线电操作时，用它计算容差和保护时间（Guard Times）。

<a id="r_a0b3e0ed1385dd428c861e08c79849ef4"></a>

```c
int(* attr_get )(const struct device *dev, enum ieee802154_attr attr, struct ieee802154_attr_value *value)
```

相关声明：[attr_get](#a0b3e0ed1385dd428c861e08c79849ef4)、[device](../device_reference/P002_设备对象结构.md)、[ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)、[ieee802154_attr_value](P005_ieee802154_attr_value_结构体.md)。

获取驱动专用属性（Driver Specific Attribute）的值。

## 41.2\_详细说明（Detailed Documentation）

<a id="a0b3e0ed1385dd428c861e08c79849ef4"></a>

### `attr_get`

```c
int(* ieee802154_radio_api::attr_get) (const struct device *dev, enum ieee802154_attr attr, struct ieee802154_attr_value *value)
```

获取驱动专用属性（Driver Specific Attribute）的值。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 驱动支持所请求的属性，可从对应的ieee802154_attr_value成员中取得值。 |
| `-ENOENT` | 驱动不提供所请求的属性。值结构未更新属性数据，value属性的内容未定义。 |

说明（Note）：此函数不得（SHALL NOT）返回任何可由MAC第二层（L2）配置的值；它仅用于来自驱动实现、且无法由L2直接或间接推导的非布尔属性，即标量或结构化属性。布尔属性必须（SHALL）实现为ieee802154_hw_caps。实现必须（SHALL）支持从中断服务程序调用（isr-ok），且不得（MUST NOT）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

<a id="a2cbbd0e64fae28f748bb3e4d654a92bf"></a>

### `cca`

```c
int(* ieee802154_radio_api::cca) (const struct device *dev)
```

空闲信道评估（Clear Channel Assessment）：检查信道活动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 信道可用（Channel Available）。 |
| `-EBUSY` | 信道忙（Channel Busy）。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-ENETDOWN` | 接口不处于“UP”状态。 |
| `-ENOTSUP` | 此驱动不支持空闲信道评估（CCA）。 |
| `-EIO` | 无法执行空闲信道评估（CCA）过程。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。接口不处于“UP”状态时必须（SHALL）返回-ENETDOWN。

<a id="a9acaf4810bd5d3b026cc381bff301071"></a>

### `configure`

```c
int(* ieee802154_radio_api::configure) (const struct device *dev, enum ieee802154_config_type type, const struct ieee802154_config *config)
```

设置或更新驱动配置（Driver Configuration）。

此方法会阻塞，直到接口完成重新配置；相对于正在进行的数据包接收、发送或其他驱动操作，该重新配置具有原子性（Atomicity）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `type` | 要设置的配置类型（Configuration Type）。 |
| `config` | 要为给定配置类型设置的配置参数（Configuration Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 配置成功（Configuration Successful）。 |
| `-EINVAL` | 配置参数对给定配置类型无效。 |
| `-ENOTSUP` | 此驱动不支持给定配置类型（Configuration Type）。 |
| `-EACCES` | 此驱动支持给定配置类型，但无法在当前接口运行状态（Operational State）下配置。 |
| `-ENOMEM` | 由于缺少内存资源（Memory Resources），无法保存配置。 |
| `-ENOENT` | 在配置中找不到配置参数所引用的资源（Resource）。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-EIO` | 尝试配置给定参数时发生内部错误（Internal Error）。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。某些配置选项并非在全部接口运行状态下都受支持，详见ieee802154_config_type；这种情况下操作返回-EACCES。

<a id="a01fc17f85f2be33877a9347f59a84c54"></a>

### `ed_scan`

```c
int(* ieee802154_radio_api::ed_scan) (const struct device *dev, uint16_t duration, energy_scan_done_cb_t done_cb)
```

执行能量检测扫描（Energy Detection Scan）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `duration` | 能量扫描（Energy Scan）的持续时间，单位为毫秒。 |
| `done_cb` | 能量扫描（Energy Scan）完成时调用的函数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功调度能量检测扫描（Energy Detection Scan）。 |
| `-EBUSY` | 目前无法调度能量检测扫描（Energy Detection Scan）。 |
| `-EALREADY` | 前一次能量检测扫描（Energy Detection Scan）尚未结束。 |
| `-ENETDOWN` | 接口不处于“UP”状态。 |
| `-ENOTSUP` | 此驱动不支持能量扫描（Energy Scans）。 |
| `-EIO` | 无法执行能量检测过程（Energy Detection Procedure）。 |

说明（Note）：需要IEEE802154_HW_ENERGY_SCAN能力。调用此函数前必须设置无线电信道（Radio Channel）。实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。接口不处于“UP”状态时必须（SHALL）返回-ENETDOWN。

<a id="aa9502e0e014a8d05ffe235567e8c98f3"></a>

### `filter`

```c
int(* ieee802154_radio_api::filter) (const struct device *dev, bool set, enum ieee802154_filter_type type, const struct ieee802154_filter *filter)
```

设置或取消PAN ID、扩展地址或短地址过滤器（Filters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `set` | true表示设置过滤器（Filter），false表示移除。 |
| `type` | 要向过滤器列表添加或从中移除的实体类型，即PAN ID或源/目的地址。 |
| `filter` | 要向过滤器列表（Filter List）添加或从中移除的实体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功添加或移除过滤器（Filter）。 |
| `-EINVAL` | 给定过滤实体（Filter Entity）或其类型无效。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-ENOTSUP` | 此驱动不支持设置或移除此过滤器（Filter）或过滤器类型。 |
| `-EIO` | 设置或移除过滤器（Filter）时出错。 |

说明（Note）：需要IEEE802154_HW_FILTER能力。实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。接口既不是“UP”也不是“DOWN”时必须（SHALL）返回-EIO。

<a id="a09a4b5df81822845f718952c6029442c"></a>

### `get_capabilities`

```c
enum ieee802154_hw_caps(* ieee802154_radio_api::get_capabilities) (const struct device *dev)
```

获取设备驱动能力（Device Driver Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），且不得（MUST NOT）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

返回（Returns）：包含全部受支持设备驱动能力（Capabilities）的位域。

<a id="ae4a3ef40a5b8031c868d72ead163c97d"></a>

### `get_sch_acc`

```c
uint8_t(* ieee802154_radio_api::get_sch_acc) (const struct device *dev)
```

获取网络子系统本地时钟当前估计的最坏情况精度（Worst Case Accuracy），即相对于标称频率的最大正负偏差；调度延迟接收或发送无线电操作时，用它计算容差和保护时间（Guard Times）。

偏差以百万分之一（Parts Per Million，PPM）为单位给出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

说明（Note）：需要IEEE802154_HW_TXTIME和/或IEEE802154_HW_RXTIME能力。实现可根据当前运行条件，例如温度，估计此值。实现必须（SHALL）支持从中断服务程序调用（isr-ok），且不得（MUST NOT）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

返回（Returns）：当前估计的时钟精度（Clock Accuracy），单位为PPM。

<a id="a829a0d59fdcda5b6cb029ef1334a6b8b"></a>

### `get_time`

```c
net_time_t(* ieee802154_radio_api::get_time) (const struct device *dev)
```

获取相对于此网络接口所表示的网络子系统本地运行时长时钟（Local Uptime Clock）的当前时间，单位为纳秒。

语义细节见net_time_t。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

说明（Note）：需要IEEE802154_HW_TXTIME和/或IEEE802154_HW_RXTIME能力。实现必须（SHALL）支持从中断服务程序调用（isr-ok），且不得（MUST NOT）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

返回（Returns）：相对于网络子系统本地时钟的纳秒数；发生错误或不支持此操作时返回-1。

<a id="aa955462d8c6950dc4b5935973f4575d8"></a>

### `iface_api`

```c
struct net_if_api ieee802154_radio_api::iface_api
```

网络接口API（Network Interface API）。

说明（Note）：网络设备必须扩展网络接口API（Network Interface API）。因此，必须将它放在驱动API结构的开头，使该结构可转换为网络接口类型。

<a id="a9ad27a2ff0a839dc5b9a4e6317cc59b1"></a>

### `set_channel`

```c
int(* ieee802154_radio_api::set_channel) (const struct device *dev, uint16_t channel)
```

设置当前信道（Current Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `channel` | 要设置的信道号（Channel Number），采用CPU字节序。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功设置信道（Channel）。 |
| `-EINVAL` | 给定信道不在驱动当前信道页（Channel Page）的有效信道范围内，见驱动属性IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-ENOTSUP` | 给定信道位于驱动当前信道页（Channel Page）的有效范围内，但当前驱动不支持。 |
| `-EIO` | 无法设置信道（Channel）。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。接口既不是“UP”也不是“DOWN”时必须（SHALL）返回-EIO。

<a id="aeeab6dfcde08af23357ea40f8af68f66"></a>

### `set_txpower`

```c
int(* ieee802154_radio_api::set_txpower) (const struct device *dev, int16_t dbm)
```

设置发送功率（TX Power），单位为dBm。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `dbm` | 发送功率（TX Power），单位为dBm。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功设置发送功率（TX Power）。 |
| `-EINVAL` | 给定dBm值无效，或驱动不支持该值。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-EIO` | 无法设置发送功率（TX Power）。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。接口既不是“UP”也不是“DOWN”时必须（SHALL）返回-EIO。

<a id="a0e4d57dc3a53299ddedf2140e172103d"></a>

### `start`

```c
int(* ieee802154_radio_api::start) (const struct device *dev)
```

启动设备（Start the Device）。

此操作返回0或-EALREADY后，上层认为接口处于“UP”状态。除非已配置接收时隙（RX Slot），否则返回前会把接口置于接收模式；即使该时隙已在过去，也属于例外，见IEEE802154_CONFIG_RX_SLOT。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功启动驱动。 |
| `-EALREADY` | 驱动已经处于“UP”状态。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-EIO` | 无法启动驱动。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

<a id="a75cfcfe2b9e69c2e4af53f00c8294b36"></a>

### `stop`

```c
int(* ieee802154_radio_api::stop) (const struct device *dev)
```

停止设备（Stop the Device）。

此操作返回0或-EALREADY后，上层认为接口处于“DOWN”状态。如果接收器此前已开启，驱动会在返回前将其关闭。调用此操作后，驱动进入尽可能低的功耗模式（Power Mode）；这可以（MAY）异步发生，即操作已返回控制权之后才达到该模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功停止驱动。 |
| `-EWOULDBLOCK` | 操作从中断服务程序（ISR）上下文调用，但暂时无法在不阻塞的情况下执行。 |
| `-EALREADY` | 驱动已经处于“DOWN”状态。 |
| `-EIO` | 无法停止驱动。 |

说明（Note）：实现必须（SHALL）支持从中断服务程序调用（isr-ok），并可以（MAY）休眠。驱动完全初始化并就绪（ready）后，可以（MAY）在任何接口状态调用。

<a id="a70139acec22642c1fc09f2323c383fe6"></a>

### `tx`

```c
int(* ieee802154_radio_api::tx) (const struct device *dev, enum ieee802154_tx_mode mode, struct net_pkt *pkt, struct net_buf *frag)
```

将一个数据包片段（Packet Fragment）作为单帧发送。

根据驱动支持的卸载功能（Offloading Features）程度，帧可能（MAY）尚未完全加密或认证，也可能（MAY）尚未包含帧校验序列（FCS）。L2实现负责按驱动宣告的卸载能力准备帧，并决定空闲信道评估（CCA）、载波侦听多路访问/冲突避免（CSMA/CA）、确认（ACK）或重传过程应在驱动外部的软件MAC（Soft MAC）中执行，还是在驱动内部的硬件MAC（Hard MAC）中执行。

来自L2的全部帧都必须（SHALL）预先分配并填充全部必需的信息元素（IEs），使驱动完全不必解析和修改IE。驱动没有IEEE802154_HW_RX_TX_ACK能力时，这也包括ACK数据包；具有此能力的驱动还应参见IEEE802154_CONFIG_ENH_ACK_HEADER_IE。

对于L2只有获知发送时间后才能准备的信息元素（IEs），例如CSL IE、会合时间IE、时间校正IE等，必须（SHALL）采用某种定时发送模式（Timed TX Mode）发送，并在IE中预填适当时序信息，使驱动完全不必解析和修改IE；驱动自行生成的帧除外。

支持并使用任意定时发送模式（Timed TX Mode）时，见ieee802154_hw_caps及ieee802154_tx_mode，驱动必须（SHALL）负责自主调度，并在精确设定的时刻发送数据包，不再需要上层参与。tx()调用会阻塞，直到数据包成功发送（可能包括取得信道及收到数据包确认），或发生终止性的传输错误。驱动必须（SHALL）在预定发送时刻到来之前，以及任何其他空闲等待期间休眠，并把功耗保持在尽可能低的水平。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向IEEE 802.15.4驱动设备（Device）的指针。 |
| `mode` | 发送模式（Transmission Mode）；其中部分模式需要特定卸载能力。 |
| `pkt` | 指向待发送网络数据包（Network Packet）的指针。 |
| `frag` | 指向网络缓冲区（Network Buffer）的指针；该缓冲区包含一个片段，片段中保存待发送的帧数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 帧已成功发送或调度。如果驱动支持确认卸载（ACK Offloading），且帧请求确认，即设置AR位，则还表示该数据包已经得到对端的成功确认。 |
| `-EINVAL` | 数据包无效，例如缺少预期信息元素（IE），或加密/认证状态不符合预期。 |
| `-EBUSY` | 介质忙，无法发送该帧；仅适用于CSMA/CA或CCA卸载功能。 |
| `-ENOMSG` | 帧未得到ACK数据包确认（仅适用于TX ACK卸载功能），或收到的ACK数据包无效。 |
| `-ENOBUFS` | 缺少内部资源，无法调度该帧；仅适用于定时发送卸载（Timed TX Offloading）功能。 |
| `-ENETDOWN` | 接口不处于“UP”状态。 |
| `-ENOTSUP` | 不支持给定发送模式（TX Mode）。 |
| `-EIO` | 由于未具体说明的驱动错误，例如驱动忙，无法发送该帧。 |

**警告（Warning）**：警告（Warning）：驱动不得（SHALL NOT）取得给定网络数据包及帧片段缓冲区的所有权（Ownership）。驱动所需的全部数据，包括实际帧内容，都必须同步读取；以后还需要使用时，必须在内部复制，例如协议配置所需的IE内容、帧计数器状态、序列号等。函数一返回，上层就可以（MAY）立即复用或释放数据包及缓冲区。

说明（Note）：实现可以（MAY）休眠，通常不支持从中断服务程序调用（非isr-ok），尤其是支持定时发送、CSMA/CA、重传、自动确认或其他需要较长空闲等待的卸载功能时。接口不处于“UP”状态时必须（SHALL）返回-ENETDOWN。

通常在set_channel()设置的无线电信道（Radio Channel）上发送。但是，如果设置了CONFIG_IEEE802154_SELECTIVE_TXCHANNEL，且驱动具有IEEE802154_HW_SELECTIVE_TXCHANNEL能力，则以IEEE802154_TX_MODE_TXTIME或IEEE802154_TX_MODE_TXTIME_CCA模式请求的发送，必须（SHALL）使用net_pkt_ieee802154_txchannel()返回的信道；帧请求确认时，还应在该信道接收ACK。操作后，驱动应回到此前set_channel()设置的信道。上层负责调用net_pkt_set_ieee802154_txchannel()为数据包设置所需信道。

此功能支持IEEE 802.15.4-2020第6.12.2.7节规定的跨多信道协调采样监听（CSL）发送。它允许尽可能晚地在发送前切换无线电信道，避免单独调用set_channel()时可能中断原本能够进行的接收。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [ieee802154_filter_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa1971591e72866d0f3f0d4db2931e25a)
- [ieee802154_filter](P017_ieee802154_filter_结构体.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [ieee802154_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab2bee8752291e082cb277145cef1225d)
- [net_pkt](P114_net_pkt_结构体.md)
- [net_buf](P046_net_buf_结构体.md)
- [ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)
- [ieee802154_config](P014_ieee802154_config_结构体.md)
- [energy_scan_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8c9ab3cecefe641a25f003eb6d014fc5)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)
- [ieee802154_attr_value](P005_ieee802154_attr_value_结构体.md)
- [RFC 2863, section-3.1.14](https://datatracker.ietf.org/doc/html/rfc2863#section-3.1.14)
- [net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)
- [EALREADY](../error_reference/P003_系统错误号公共接口.md#gaa4ccb54aa806de3e41a8515f06db85d4)
- [RFC 2863](https://datatracker.ietf.org/doc/html/rfc2863)
- [ENETDOWN](../error_reference/P003_系统错误号公共接口.md#gaac51995026fa19cdd0ad84a272304af0)
- [IEEE802154_CONFIG_RX_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)
- [EACCES](../error_reference/P003_系统错误号公共接口.md#gac2a2e9fa555401f94478f74e01868032)
- [IEEE802154_HW_RX_TX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03)
- [IEEE802154_CONFIG_ENH_ACK_HEADER_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)
- [IEEE802154_HW_SELECTIVE_TXCHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)
- [IEEE802154_TX_MODE_TXTIME_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_ieee802154_phy_supported_channels_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_ieee802154_req_params_结构体.md)
